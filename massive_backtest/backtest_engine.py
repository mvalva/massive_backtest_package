"""
Motore backtest: due tipi di entry (open regolare + prezzo fattibile a notizia),
orizzonti in soli giorni di borsa, metriche = prezzo massimo e minimo nell'arco (high/low).
- Entry open: primo prezzo acquistabile a mercato aperto (solo regular, no pre/after market).
- Entry news: prezzo fattibile quando esce la notizia SEC (include pre-market/after-hours, spread conservativo).
- Orizzonte 1d/2d/... = 1, 2, ... giorni di borsa (non calendario).
- Per ogni orizzonte: ret_high_% = massimo raggiunto, ret_low_% = minimo raggiunto (strategia su best/worst case).
"""

from __future__ import annotations

import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from threading import Lock
from typing import Callable

import pandas as pd

# Delay (secondi) tra richieste API per evitare rate limit. Riducibile (es. 0.02) per velocità; aumentare se compaiono errori 429.
BACKTEST_DELAY_SEC = float(os.getenv("BACKTEST_DELAY_SEC", "0.02"))

try:
    from massive_backtest.massive_client import fetch_daily_aggs, fetch_aggs, fetch_ticker_details
except ImportError:
    from massive_client import fetch_daily_aggs, fetch_aggs, fetch_ticker_details

try:
    from zoneinfo import ZoneInfo
except ImportError:
    ZoneInfo = None

# Orizzonte in giorni di borsa (1 = primo giorno dopo entry, 2 = due giorni borsa, ecc.)
TRADING_DAY_HORIZONS = [1, 2, 3, 5, 7, 10, 14, 30, 60, 90]


def _compute_rsi(closes: list[float], period: int = 14) -> float | None:
    """RSI (Relative Strength Index) su lista di close. Ritorna None se dati insufficienti."""
    if len(closes) < period + 1:
        return None
    try:
        deltas = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
        gains = [d if d > 0 else 0.0 for d in deltas[-period:]]
        losses = [-d if d < 0 else 0.0 for d in deltas[-period:]]
        avg_gain = sum(gains) / period
        avg_loss = sum(losses) / period
        if avg_loss == 0:
            return 100.0
        rs = avg_gain / avg_loss
        return round(100 - (100 / (1 + rs)), 2)
    except (ZeroDivisionError, TypeError, IndexError):
        return None


def _compute_sma(closes: list[float], period: int) -> float | None:
    """Media mobile semplice sugli ultimi `period` close."""
    if len(closes) < period:
        return None
    try:
        return round(sum(closes[-period:]) / period, 2)
    except (TypeError, ZeroDivisionError):
        return None


def _normalize_ticker_for_api(ticker: str) -> str:
    """Pulisce il ticker per la chiamata Massive: rimuove prefissi (NYSE:), parentesi [], prende primo se comma."""
    if not ticker or not isinstance(ticker, str):
        return ""
    s = ticker.strip().upper()
    if ":" in s:
        s = s.split(":")[-1].strip()
    if "[" in s or "]" in s:
        s = s.replace("[", "").replace("]", "").strip()
    if "," in s:
        s = s.split(",")[0].strip()
    if " " in s:
        s = s.split()[0].strip()
    return s


def _bar_date_iso(bar: dict) -> str:
    """Data YYYY-MM-DD da barra (t in ms)."""
    t = bar.get("t")
    if t is None:
        return ""
    try:
        dt = datetime.utcfromtimestamp(int(t) / 1000.0)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return ""


def _bar_datetime_iso(bar: dict) -> str:
    """Data e ora ISO (YYYY-MM-DDTHH:MM:SSZ) da barra (t in ms UTC)."""
    t = bar.get("t")
    if t is None:
        return ""
    try:
        dt = datetime.utcfromtimestamp(int(t) / 1000.0)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:
        return ""


def _parse_filed_at(filed_at: str) -> tuple[str, int, int, bool, bool]:
    """
    Parse filedAt ISO (es. 2026-02-10T16:17:30-05:00). Ritorna (date_iso, hour, minute, is_weekday, is_during_market).
    Mercato USA: 9:30-16:00 ET, Lun-Ven. hour/minute in ET (da offset -05 o -04).
    """
    date_iso, hour, minute = "", 9, 30
    is_weekday, is_during = True, False
    if not filed_at or len(filed_at) < 16:
        return date_iso, hour, minute, is_weekday, is_during
    try:
        date_iso = filed_at[:10]
        if "T" in filed_at:
            t_part = filed_at.split("T")[1]
            hhmm = t_part[:5]
            if ":" in hhmm:
                h, m = hhmm.split(":")[:2]
                hour, minute = int(h), int(m) if len(m) >= 2 else 0
        # Offset: -05:00 o -04:00 → già in ET
        dt = datetime.strptime(date_iso, "%Y-%m-%d")
        is_weekday = dt.weekday() < 5
        # Durante mercato: 9:30-16:00 (16:00 = chiusura, 16:01 = dopo)
        is_during = is_weekday and ((hour > 9) or (hour == 9 and minute >= 30)) and (hour < 16 or (hour == 16 and minute == 0))
    except Exception:
        pass
    return date_iso, hour, minute, is_weekday, is_during


def _entry_datetime_from_filed_at(filed_at: str, entry_date: str) -> str:
    """
    Calcola entry_datetime da filedAt e entry_date.
    - Filing durante mercato (9:30-16:00 ET): entry = ora filing + 15 min (tempo per vedere ed eseguire)
    - Filing prima 9:30: entry = 09:30 stesso giorno
    - Filing dopo 16:00 o weekend: entry = 09:30 giorno successivo (entry_date è già il giorno giusto)
    """
    if not entry_date or len(entry_date) < 10:
        return ""
    _, hour, minute, is_weekday, is_during = _parse_filed_at(filed_at or "")
    if is_during:
        m = minute + 15
        h = hour + (m // 60)
        m = m % 60
        if h >= 16:
            h, m = 16, 0
        return f"{entry_date[:10]} {h:02d}:{m:02d}"
    return f"{entry_date[:10]} 09:30"


def _et_to_unix_ms(year: int, month: int, day: int, hour: int, minute: int) -> int:
    """Timestamp Unix ms per (date, hour, minute) in ET."""
    if not ZoneInfo:
        return 0
    dt = datetime(year, month, day, hour, minute, 0, tzinfo=ZoneInfo("America/New_York"))
    return int(dt.timestamp() * 1000)


def _fetch_intraday_bars(ticker: str, date: str, multiplier: int = 1) -> tuple[list[dict], str | None]:
    """Barre intraday (multiplier x minute) per sessione 9:30-16:00 ET. multiplier: 1, 5, 15, 30, 60."""
    ticker_api = _normalize_ticker_for_api(ticker)
    tkr = ticker_api or ticker
    limit = 500 if multiplier <= 5 else 100
    try:
        y, m, d = int(date[:4]), int(date[5:7]), int(date[8:10])
        from_ms = _et_to_unix_ms(y, m, d, 9, 30)
        to_ms = _et_to_unix_ms(y, m, d, 16, 0)
        bars, err = fetch_aggs(tkr, str(from_ms), str(to_ms), multiplier=multiplier, timespan="minute", limit=limit)
        if bars:
            return bars, err
        bars2, _ = fetch_aggs(tkr, date, date, multiplier=multiplier, timespan="minute", limit=limit)
        return (bars2, None) if bars2 else (bars, err)
    except Exception:
        return fetch_aggs(tkr, date, date, multiplier=multiplier, timespan="minute", limit=limit)


def _fetch_extended_hours_bars(ticker: str, date: str, multiplier: int = 5) -> tuple[list[dict], str | None]:
    """Barre minute con pre-market e after-hours (4:00-20:00 ET) per prezzo 'a notizia'."""
    if not ZoneInfo:
        return [], None
    ticker_api = _normalize_ticker_for_api(ticker)
    tkr = ticker_api or ticker
    try:
        y, m, d = int(date[:4]), int(date[5:7]), int(date[8:10])
        from_ms = _et_to_unix_ms(y, m, d, 4, 0)
        to_ms = _et_to_unix_ms(y, m, d, 20, 0)
        bars, err = fetch_aggs(tkr, str(from_ms), str(to_ms), multiplier=multiplier, timespan="minute", limit=500)
        return (bars or [], err)
    except Exception:
        return [], None


def _filed_at_to_unix_ms(filed_at: str) -> int | None:
    """Converte filedAt ISO (es. 2026-02-10T16:17:30-05:00) in Unix ms (interpretato come ET)."""
    if not filed_at or len(filed_at) < 10 or not ZoneInfo:
        return None
    try:
        date_iso = filed_at[:10]
        t_part = (filed_at.split("T")[1][:8]) if "T" in filed_at else "09:30:00"
        h, mi, s = 9, 30, 0
        if ":" in t_part:
            parts = t_part.split(":")
            h = int(parts[0])
            mi = int(parts[1]) if len(parts) > 1 else 30
            s = int(parts[2]) if len(parts) > 2 else 0
        y, mo, d = int(date_iso[:4]), int(date_iso[5:7]), int(date_iso[8:10])
        dt = datetime(y, mo, d, h, mi, s, tzinfo=ZoneInfo("America/New_York"))
        return int(dt.timestamp() * 1000)
    except Exception:
        return None


def _bar_containing_or_after(bars: list[dict], filed_at_ms: int | None, bar_duration_ms: int = 300000):
    """Trova la barra che contiene filed_at_ms o la prima barra con inizio >= filed_at_ms. Ritorna (bar, in_bar)."""
    if not bars or filed_at_ms is None:
        return None, False
    for b in bars:
        t = b.get("t")
        if t is None:
            continue
        if t <= filed_at_ms < t + bar_duration_ms:
            return b, True
    for b in sorted(bars, key=lambda x: x.get("t") or 0):
        if (b.get("t") or 0) >= filed_at_ms:
            return b, False
    return None, False


def _feasible_buy_price_from_extended_bars(bars: list[dict], filed_at_ms: int | None, bar_duration_ms: int = 300000) -> float | None:
    """
    Prezzo fattibile di acquisto quando esce la notizia (pre/after market, spread conservativo).
    Usa la barra che contiene filed_at_ms; prezzo = high della barra (worst case buy, spread incluso).
    bar_duration_ms: 5 min = 300000.
    """
    b, _ = _bar_containing_or_after(bars, filed_at_ms, bar_duration_ms)
    if b is None:
        return None
    h = b.get("h")
    return float(h) if h is not None else None


def _first_bar_at_or_after(bars: list[dict], filed_at_ms: int | None):
    """Prima barra con inizio (t) >= filed_at_ms. Per il bot = primo prezzo disponibile *dopo* la notizia."""
    if not bars or filed_at_ms is None:
        return None
    for b in sorted(bars, key=lambda x: x.get("t") or 0):
        if (b.get("t") or 0) >= filed_at_ms:
            return b
    return None


def _feasible_buy_price_bot_from_extended_bars(bars: list[dict], filed_at_ms: int | None, bar_duration_ms: int = 300000) -> float | None:
    """
    Prezzo plausibile per un bot che compra subito dopo la notizia SEC.
    Usa la *prima barra che inizia* al momento del filing o dopo (t >= filed_at_ms): prezzo = open di quella barra.
    Così l'open è il primo prezzo disponibile *dopo* la notizia (con la granularità delle barre, es. 5 min),
    con le limitazioni del caso (spread, liquidità pre/after market).
    """
    b = _first_bar_at_or_after(bars, filed_at_ms)
    if b is None:
        return None
    o = b.get("o")
    return float(o) if o is not None else None


def _fetch_minute_bars(ticker: str, date: str) -> tuple[list[dict], str | None]:
    """Barre intraday per ret_4h. Prova 1-min, poi 15-min se poche barre o prezzo non trovato."""
    bars, err = _fetch_intraday_bars(ticker, date, multiplier=1)
    return bars, err


def _bar_duration_ms(bars: list[dict]) -> int:
    """Durata barra in ms (da intervallo tra prime due). Supporta 1/5/15/30/60 min."""
    if len(bars) < 2:
        return 60000
    t0, t1 = bars[0].get("t"), bars[1].get("t")
    if t0 is not None and t1 is not None:
        d = int(t1) - int(t0)
        if 50000 <= d <= 3600000:
            return d
    return 60000


def _price_from_bars(bars: list[dict], date: str, hour: int, minute: int) -> float | None:
    """Prezzo open dalla barra che contiene (date, hour, minute) ET. Supporta 1-min e 5-min."""
    if not ZoneInfo or not bars:
        return None
    try:
        dt_et = datetime(
            int(date[:4]), int(date[5:7]), int(date[8:10]),
            hour, minute, 0, tzinfo=ZoneInfo("America/New_York")
        )
        ts_ms = int(dt_et.timestamp() * 1000)
    except Exception:
        return None
    duration = _bar_duration_ms(bars)
    for b in bars:
        t = b.get("t")
        if t is None:
            continue
        if t <= ts_ms < t + duration:
            o = b.get("o")
            return float(o) if o is not None else None
    return None


def _price_at_datetime_et(ticker: str, entry_date: str, hour: int, minute: int) -> float | None:
    """Prezzo alla barra 1-min che contiene (entry_date, hour, minute) ET. Fetch + lookup."""
    bars, err = _fetch_minute_bars(ticker, entry_date)
    if err or not bars:
        return None
    return _price_from_bars(bars, entry_date, hour, minute)


def _filing_requires_next_day(filed_at: str) -> bool:
    """True se il filing è dopo chiusura (16:00 ET) o in weekend → entry al giorno successivo."""
    _, hour, minute, is_weekday, is_during = _parse_filed_at(filed_at or "")
    if not is_weekday:
        return True
    if is_during:
        return False
    return hour >= 16 or (hour == 16 and minute > 0)


def _next_trading_day_after(date_str: str) -> str | None:
    """Prossimo giorno di borsa (Lun-Ven) dopo date_str. Ritorna YYYY-MM-DD."""
    try:
        d = datetime.strptime(date_str[:10], "%Y-%m-%d").date()
        for _ in range(7):
            d += timedelta(days=1)
            if d.weekday() < 5:
                return d.strftime("%Y-%m-%d")
    except Exception:
        pass
    return None


def _nth_trading_day_after(date_str: str, n: int) -> str | None:
    """N-esimo giorno di borsa dopo date_str (n=1 = primo, n=2 = secondo). Ritorna YYYY-MM-DD."""
    if n < 1:
        return None
    # 90 trading days ≈ 126 calendar days; usiamo 150 per coprire il max orizzonte (TRADING_DAY_HORIZONS).
    max_calendar_days = 150
    try:
        d = datetime.strptime(date_str[:10], "%Y-%m-%d").date()
        count = 0
        for _ in range(max_calendar_days):
            d += timedelta(days=1)
            if d.weekday() < 5:
                count += 1
                if count == n:
                    return d.strftime("%Y-%m-%d")
    except Exception:
        pass
    return None


def _expected_entry_date(filing_day: str, filed_at: str) -> str:
    """Data di entry attesa (YYYY-MM-DD) in base a filing_day e filedAt."""
    if _filing_requires_next_day(filed_at or ""):
        next_d = _next_trading_day_after(filing_day)
        return next_d or filing_day
    return filing_day


def _entry_and_forward_from_daily(
    ticker: str, filing_day: str, filed_at: str = ""
) -> tuple[float | None, str | None, str | None, dict[int, float | None], float | None, float | None, dict, str | None]:
    """
    Entry = open primo giorno borsa in cui il mercato era aperto quando si è saputo del filing.
    Ritorna: (entry_price, entry_date, entry_datetime, forward_returns, max_dd, max_runup, extra_dict, errore).
    extra_dict: volume_entry, vwap_entry, range_pct_entry, volume_avg_20d, pct_from_52w_high.
    """
    # Entry NON deve essere distante più di 1 giorno di borsa dal filing:
    # usiamo sempre la data di entry attesa (filing_day o prossimo giorno di borsa),
    # e se non esiste una barra in quella data, consideriamo il cluster non tradabile.
    expected_entry_date = _expected_entry_date(filing_day, filed_at or "")
    try:
        from_d = datetime.strptime(filing_day, "%Y-%m-%d").date() - timedelta(days=400)
        from_date = from_d.strftime("%Y-%m-%d")
        # 90 giorni di borsa ≈ 130 giorni di calendario; usiamo 150 per sicurezza
        to_d = datetime.strptime(filing_day, "%Y-%m-%d").date() + timedelta(days=150)
        to_date = to_d.strftime("%Y-%m-%d")
    except Exception:
        from_date, to_date = filing_day, filing_day
    ticker_api = _normalize_ticker_for_api(ticker)
    bars, api_error = fetch_daily_aggs(ticker_api or ticker, from_date, to_date)
    _empty_extra = {"volume_entry": None, "vwap_entry": None, "range_pct_entry": None, "volume_avg_20d": None, "pct_from_52w_high": None, "rsi_entry": None, "ma50_entry": None, "ma200_entry": None, "entry_price_news_bot": None}
    _empty_hl = {
        n: {
            "high_open": None, "low_open": None, "high_news": None, "low_news": None,
            "date_high": None, "date_low": None, "datetime_high": None, "datetime_low": None,
        }
        for n in TRADING_DAY_HORIZONS
    }
    if api_error:
        return None, None, None, None, _empty_hl, None, None, _empty_extra, api_error
    if not bars:
        return None, None, None, None, _empty_hl, None, None, _empty_extra, "Nessun dato prezzi"
    bars = sorted(bars, key=lambda b: b.get("t") or 0)
    entry_price = None
    entry_date = None
    entry_bar = None
    entry_bar_idx = -1
    target_date = expected_entry_date or filing_day
    for idx, b in enumerate(bars):
        d = _bar_date_iso(b)
        if not d:
            continue
        if d != target_date:
            continue
        entry_price = b.get("o")
        entry_date = d
        entry_bar = b
        entry_bar_idx = idx
        break
    entry_datetime = _entry_datetime_from_filed_at(filed_at or "", entry_date or "") if entry_date else ""
    if entry_price is None or not entry_date:
        return None, None, None, None, _empty_hl, None, None, _empty_extra, "Nessuna barra nel giorno di entry atteso"
    entry_price = float(entry_price)
    # Entry open: se filing durante mercato, prezzo intraday (1-min) invece di daily open
    minute_bars_cache: list[dict] | None = None
    _, eh, em, _, is_during = _parse_filed_at(filed_at or "")
    if is_during:
        m = em + 15
        eh = eh + (m // 60)
        em = m % 60
        if eh < 16 or (eh == 16 and em == 0):
            time.sleep(0.15)
            minute_bars_cache, _ = _fetch_minute_bars(ticker_api or ticker, entry_date)
            if minute_bars_cache:
                intraday_px = _price_from_bars(minute_bars_cache, entry_date, eh, em)
                if intraday_px is not None:
                    entry_price = intraday_px
    # Entry news: prezzo fattibile quando esce la notizia (pre/after market)
    # entry_price_news = high della barra (conservativo, investitore umano); entry_price_news_bot = open (bot che compra subito)
    entry_price_news = None
    entry_price_news_bot = None
    filed_ms = _filed_at_to_unix_ms(filed_at or "")
    if filed_ms is not None:
        for try_date in [filing_day[:10], entry_date]:
            if not try_date:
                continue
            time.sleep(0.1)
            ext_bars, _ = _fetch_extended_hours_bars(ticker_api or ticker, try_date, multiplier=5)
            if ext_bars:
                entry_price_news = _feasible_buy_price_from_extended_bars(ext_bars, filed_ms, bar_duration_ms=300000)
                entry_price_news_bot = _feasible_buy_price_bot_from_extended_bars(ext_bars, filed_ms, bar_duration_ms=300000)
                if entry_price_news is not None:
                    break
    # Per ogni orizzonte (N giorni di borsa): max high, min low e media aritmetica di tutti i valori prezzo nel periodo.
    # mean = media aritmetica di O,H,L,C di ogni barra (es. 5 min) nella finestra [entry_date, end_date];
    # più date_high/date_low e datetime_high/datetime_low in cui il prezzo raggiunge max/min.
    high_low_returns = {}
    for n in TRADING_DAY_HORIZONS:
        end_n = _nth_trading_day_after(entry_date, n)
        if not end_n:
            high_low_returns[n] = {
                "high_open": None, "low_open": None, "mean_open": None,
                "high_news": None, "low_news": None, "mean_news": None,
                "high_news_bot": None, "low_news_bot": None, "mean_news_bot": None,
                "date_high": None, "date_low": None, "datetime_high": None, "datetime_low": None,
            }
            continue
        max_high_n = None
        min_low_n = None
        bar_high_n = None  # barra in cui è stato raggiunto il massimo
        bar_low_n = None   # barra in cui è stato raggiunto il minimo
        sum_price_n = 0.0
        cnt_price_n = 0
        for b in bars:
            d = _bar_date_iso(b)
            if not d or d < entry_date or d > end_n:
                continue
            hi, lo = b.get("h"), b.get("l")
            if hi is not None:
                if max_high_n is None or float(hi) > max_high_n:
                    max_high_n = float(hi)
                    bar_high_n = b
            if lo is not None:
                if min_low_n is None or float(lo) < min_low_n:
                    min_low_n = float(lo)
                    bar_low_n = b
            # Media aritmetica di tutti i valori nel lasso di tempo: O, H, L, C di ogni barra (es. 5 min).
            o, h, l, c = b.get("o"), b.get("h"), b.get("l"), b.get("c")
            if o is not None and h is not None and l is not None and c is not None:
                try:
                    sum_price_n += float(o) + float(h) + float(l) + float(c)
                    cnt_price_n += 4
                except (TypeError, ValueError):
                    pass
        if max_high_n is None:
            max_high_n = entry_price
        if min_low_n is None:
            min_low_n = entry_price
        mean_price_n = None
        if cnt_price_n > 0:
            try:
                mean_price_n = sum_price_n / cnt_price_n
            except (TypeError, ZeroDivisionError):
                mean_price_n = None
        ret_high_open = round((max_high_n - entry_price) / entry_price * 100, 2) if entry_price and entry_price != 0 else None
        ret_low_open = round((min_low_n - entry_price) / entry_price * 100, 2) if entry_price and entry_price != 0 else None
        ret_mean_open = None
        if mean_price_n is not None and entry_price and entry_price != 0:
            ret_mean_open = round((mean_price_n - entry_price) / entry_price * 100, 2)
        ret_high_news = round((max_high_n - entry_price_news) / entry_price_news * 100, 2) if entry_price_news and entry_price_news != 0 else None
        ret_low_news = round((min_low_n - entry_price_news) / entry_price_news * 100, 2) if entry_price_news and entry_price_news != 0 else None
        ret_mean_news = None
        if mean_price_n is not None and entry_price_news and entry_price_news != 0:
            ret_mean_news = round((mean_price_n - entry_price_news) / entry_price_news * 100, 2)
        ret_high_news_bot = round((max_high_n - entry_price_news_bot) / entry_price_news_bot * 100, 2) if entry_price_news_bot and entry_price_news_bot != 0 else None
        ret_low_news_bot = round((min_low_n - entry_price_news_bot) / entry_price_news_bot * 100, 2) if entry_price_news_bot and entry_price_news_bot != 0 else None
        ret_mean_news_bot = None
        if mean_price_n is not None and entry_price_news_bot and entry_price_news_bot != 0:
            ret_mean_news_bot = round((mean_price_n - entry_price_news_bot) / entry_price_news_bot * 100, 2)
        date_high = _bar_date_iso(bar_high_n) if bar_high_n else None
        date_low = _bar_date_iso(bar_low_n) if bar_low_n else None
        datetime_high = _bar_datetime_iso(bar_high_n) if bar_high_n else None
        datetime_low = _bar_datetime_iso(bar_low_n) if bar_low_n else None
        high_low_returns[n] = {
            "high_open": ret_high_open,
            "low_open": ret_low_open,
            "mean_open": ret_mean_open,
            "high_news": ret_high_news,
            "low_news": ret_low_news,
            "mean_news": ret_mean_news,
            "high_news_bot": ret_high_news_bot,
            "low_news_bot": ret_low_news_bot,
            "mean_news_bot": ret_mean_news_bot,
            "date_high": date_high,
            "date_low": date_low,
            "datetime_high": datetime_high,
            "datetime_low": datetime_low,
            "mean_price": mean_price_n,
        }
    # Max drawdown e max run-up (30 giorni borsa): da entry open
    min_low = entry_price
    max_high = entry_price
    end_30 = _nth_trading_day_after(entry_date, 30)
    cutoff_30 = end_30 or (datetime.strptime(entry_date, "%Y-%m-%d") + timedelta(days=35)).strftime("%Y-%m-%d")
    for b in bars:
        d = _bar_date_iso(b)
        if not d or d < entry_date or d > cutoff_30:
            continue
        lo = b.get("l")
        hi = b.get("h")
        if lo is not None:
            min_low = min(min_low, float(lo))
        if hi is not None:
            max_high = max(max_high, float(hi))
    max_dd = round((entry_price - min_low) / entry_price * 100, 2) if entry_price and entry_price != 0 else None
    max_runup = round((max_high - entry_price) / entry_price * 100, 2) if entry_price and entry_price != 0 else None
    # Extra da barra entry e storico
    extra = _empty_extra.copy()
    if entry_bar:
        v = entry_bar.get("v")
        vw = entry_bar.get("vw")
        h, l_, c = entry_bar.get("h"), entry_bar.get("l"), entry_bar.get("c")
        extra["volume_entry"] = int(v) if v is not None else None
        extra["vwap_entry"] = round(float(vw), 2) if vw is not None else None
        if c and c != 0 and h is not None and l_ is not None:
            extra["range_pct_entry"] = round((float(h) - float(l_)) / float(c) * 100, 2)
    if entry_bar_idx >= 20:
        vols = [float(b.get("v") or 0) for b in bars[entry_bar_idx - 20 : entry_bar_idx] if b.get("v") is not None]
        extra["volume_avg_20d"] = round(sum(vols) / len(vols), 0) if vols else None
    if entry_bar_idx >= 0:
        lookback = min(entry_bar_idx + 1, 252)
        highs = [float(b.get("h") or 0) for b in bars[entry_bar_idx - lookback + 1 : entry_bar_idx + 1] if b.get("h") is not None]
        if highs and entry_price and entry_price != 0:
            h52 = max(highs)
            if h52 > 0:
                extra["pct_from_52w_high"] = round((entry_price - h52) / h52 * 100, 2)
    # Analisi tecnica a entry: RSI(14), MA50, MA200 (su close delle barre fino a entry)
    closes = []
    for b in bars[: entry_bar_idx + 1]:
        c = b.get("c")
        if c is not None:
            try:
                closes.append(float(c))
            except (TypeError, ValueError):
                pass
    if len(closes) >= 15:
        extra["rsi_entry"] = _compute_rsi(closes, 14)
    if len(closes) >= 50:
        extra["ma50_entry"] = _compute_sma(closes, 50)
    if len(closes) >= 200:
        extra["ma200_entry"] = _compute_sma(closes, 200)
    extra["entry_price_news_bot"] = entry_price_news_bot
    return entry_price, entry_date, entry_datetime, entry_price_news, high_low_returns, max_dd, max_runup, extra, None


def _process_one_cluster(
    i: int,
    row: dict,
    today: str,
    exclude_future_entry: bool,
    cache: dict,
    cache_lock: Lock,
) -> tuple[int, dict | None, dict | None, str, str | None]:
    """Elabora un singolo cluster; ritorna (i, rec|None, err_entry|None, ticker, reason)."""
    if i > 0 and BACKTEST_DELAY_SEC > 0:
        time.sleep(BACKTEST_DELAY_SEC)
    ticker = (row.get("ticker") or "").strip().upper()
    filing_day = (row.get("filing_day") or row.get("filedAt") or "")[:10]
    filed_at = str(row.get("filedAt") or "")
    try:
        from_d = datetime.strptime(filing_day, "%Y-%m-%d").date()
        to_d = datetime.now().date()
        days_since_filing = (to_d - from_d).days
    except Exception:
        days_since_filing = None
    if not ticker or not filing_day:
        if exclude_future_entry:
            err = {"ticker": ticker or "?", "filing_day": filing_day or "?", "error": "Ticker o filing_day mancante"}
        _empty = {}
        for n in TRADING_DAY_HORIZONS:
            _empty[f"ret_high_{n}d_open"] = _empty[f"ret_low_{n}d_open"] = _empty[f"ret_mean_{n}d_open"] = None
            _empty[f"ret_high_{n}d_news"] = _empty[f"ret_low_{n}d_news"] = _empty[f"ret_mean_{n}d_news"] = None
            _empty[f"ret_high_{n}d_news_bot"] = _empty[f"ret_low_{n}d_news_bot"] = _empty[f"ret_mean_{n}d_news_bot"] = None
            _empty[f"date_high_{n}d"] = _empty[f"date_low_{n}d"] = None
            _empty[f"datetime_high_{n}d"] = _empty[f"datetime_low_{n}d"] = None
            rec = {**row, "entry_price": None, "entry_price_news": None, "entry_price_news_bot": None, "entry_date": None, "entry_datetime": None, "max_drawdown_pct": None, "max_runup_pct": None, "days_since_filing": days_since_filing, "volume_entry": None, "vwap_entry": None, "range_pct_entry": None, "volume_avg_20d": None, "pct_from_52w_high": None, "rsi_entry": None, "ma50_entry": None, "ma200_entry": None, "market_cap": None, "list_date": None, "primary_exchange": None, "sic_code": None, "sic_description": None, **_empty}
            return (i, rec, err, ticker or "?", "Ticker o filing_day mancante")
        _empty = {}
        for n in TRADING_DAY_HORIZONS:
            _empty[f"ret_high_{n}d_open"] = _empty[f"ret_low_{n}d_open"] = _empty[f"ret_mean_{n}d_open"] = None
            _empty[f"ret_high_{n}d_news"] = _empty[f"ret_low_{n}d_news"] = _empty[f"ret_mean_{n}d_news"] = None
            _empty[f"ret_high_{n}d_news_bot"] = _empty[f"ret_low_{n}d_news_bot"] = _empty[f"ret_mean_{n}d_news_bot"] = None
            _empty[f"date_high_{n}d"] = _empty[f"date_low_{n}d"] = None
            _empty[f"datetime_high_{n}d"] = _empty[f"datetime_low_{n}d"] = None
        rec = {**row, "entry_price": None, "entry_price_news": None, "entry_price_news_bot": None, "entry_date": None, "entry_datetime": None, "max_drawdown_pct": None, "max_runup_pct": None, "days_since_filing": days_since_filing, "volume_entry": None, "vwap_entry": None, "range_pct_entry": None, "volume_avg_20d": None, "pct_from_52w_high": None, "rsi_entry": None, "ma50_entry": None, "ma200_entry": None, "market_cap": None, "list_date": None, "primary_exchange": None, "sic_code": None, "sic_description": None, **_empty}
        return (i, rec, None, ticker or "?", "Ticker o filing_day mancante")
    if exclude_future_entry:
        exp_entry = _expected_entry_date(filing_day, filed_at)
        if exp_entry and exp_entry > today:
            return (i, None, {"ticker": ticker, "filing_day": filing_day, "error": "Entry date futura"}, ticker, "Entry date futura")
    entry_price, entry_date, entry_datetime, entry_price_news, high_low_returns, max_dd, max_runup, extra, api_error = _entry_and_forward_from_daily(ticker, filing_day, filed_at)
    reason = api_error if (entry_price is None and api_error) else None
    if exclude_future_entry and entry_price is None:
        return (i, None, {"ticker": ticker, "filing_day": filing_day, "error": reason or "Nessun dato prezzi"}, ticker, reason)
    rec = {
        **row,
        "entry_price": entry_price,
        "entry_price_news": entry_price_news,
        "entry_date": entry_date,
        "entry_datetime": entry_datetime,
        "max_drawdown_pct": max_dd,
        "max_runup_pct": max_runup,
        "days_since_filing": days_since_filing,
    }
    rec.update(extra)
    if reason:
        rec["backtest_reason"] = reason
    for n in TRADING_DAY_HORIZONS:
        hl = high_low_returns.get(n) or {}
        rec[f"ret_high_{n}d_open"] = hl.get("high_open")
        rec[f"ret_low_{n}d_open"] = hl.get("low_open")
        rec[f"ret_mean_{n}d_open"] = hl.get("mean_open")
        rec[f"ret_high_{n}d_news"] = hl.get("high_news")
        rec[f"ret_low_{n}d_news"] = hl.get("low_news")
        rec[f"ret_mean_{n}d_news"] = hl.get("mean_news")
        rec[f"ret_high_{n}d_news_bot"] = hl.get("high_news_bot")
        rec[f"ret_low_{n}d_news_bot"] = hl.get("low_news_bot")
        rec[f"ret_mean_{n}d_news_bot"] = hl.get("mean_news_bot")
        rec[f"date_high_{n}d"] = hl.get("date_high")
        rec[f"date_low_{n}d"] = hl.get("date_low")
        rec[f"datetime_high_{n}d"] = hl.get("datetime_high")
        rec[f"datetime_low_{n}d"] = hl.get("datetime_low")
        # Prezzo medio del periodo (stesso valore per open/news): usato per ret_mean
        mean_price_n = hl.get("mean_price")
        rec[f"mean_price_{n}d_open"] = mean_price_n
        rec[f"mean_price_{n}d_news"] = mean_price_n
        if entry_price not in (None, 0) and hl.get("high_open") is not None:
            rec[f"exit_high_{n}d_open_price"] = round(entry_price * (1 + hl["high_open"] / 100.0), 4)
        if entry_price not in (None, 0) and hl.get("low_open") is not None:
            rec[f"exit_low_{n}d_open_price"] = round(entry_price * (1 + hl["low_open"] / 100.0), 4)
        # Exit "mean": livello di prezzo medio nel periodo (valore assoluto, non un vero trade)
        if mean_price_n is not None and entry_price not in (None, 0):
            rec[f"exit_mean_{n}d_open_price"] = mean_price_n
        if entry_price_news not in (None, 0) and hl.get("high_news") is not None:
            rec[f"exit_high_{n}d_news_price"] = round(entry_price_news * (1 + hl["high_news"] / 100.0), 4)
        if entry_price_news not in (None, 0) and hl.get("low_news") is not None:
            rec[f"exit_low_{n}d_news_price"] = round(entry_price_news * (1 + hl["low_news"] / 100.0), 4)
        if mean_price_n is not None and entry_price_news not in (None, 0):
            rec[f"exit_mean_{n}d_news_price"] = mean_price_n
        entry_price_news_bot = rec.get("entry_price_news_bot")
        if entry_price_news_bot not in (None, 0) and hl.get("high_news_bot") is not None:
            rec[f"exit_high_{n}d_news_bot_price"] = round(entry_price_news_bot * (1 + hl["high_news_bot"] / 100.0), 4)
        if entry_price_news_bot not in (None, 0) and hl.get("low_news_bot") is not None:
            rec[f"exit_low_{n}d_news_bot_price"] = round(entry_price_news_bot * (1 + hl["low_news_bot"] / 100.0), 4)
        if mean_price_n is not None and entry_price_news_bot not in (None, 0):
            rec[f"exit_mean_{n}d_news_bot_price"] = mean_price_n
        rec[f"mean_price_{n}d_news_bot"] = mean_price_n
    for n in TRADING_DAY_HORIZONS:
        rec[f"ret_{n}d"] = rec.get(f"ret_high_{n}d_open")
    rec["ret_24h"] = rec.get("ret_high_1d_open")
    rec["ret_48h"] = rec.get("ret_high_2d_open")
    rec["ret_72h"] = rec.get("ret_high_3d_open")
    ticker_api = _normalize_ticker_for_api(ticker)
    if entry_price is not None and entry_date:
        cache_key = f"{ticker_api or ticker}:{entry_date[:10]}"
        with cache_lock:
            if cache_key not in cache:
                if BACKTEST_DELAY_SEC > 0:
                    time.sleep(BACKTEST_DELAY_SEC)
                details, _ = fetch_ticker_details(ticker_api or ticker, entry_date)
                cache[cache_key] = details
            details = cache[cache_key]
        if details:
            rec["market_cap"] = details.get("market_cap")
            rec["list_date"] = details.get("list_date")
            rec["primary_exchange"] = details.get("primary_exchange")
            rec["sic_code"] = details.get("sic_code")
            rec["sic_description"] = details.get("sic_description")
        else:
            for k in ("market_cap", "list_date", "primary_exchange", "sic_code", "sic_description"):
                rec[k] = None
    else:
        for k in ("market_cap", "list_date", "primary_exchange", "sic_code", "sic_description"):
            rec[k] = None
    err_entry = {"ticker": ticker, "filing_day": filing_day, "error": reason} if reason else None
    return (i, rec, err_entry, ticker, reason)


def run_backtest(
    clusters: list[dict],
    progress_callback: Callable[[int, int, str, str | None], None] | None = None,
    errors_list: list[dict] | None = None,
    exclude_future_entry: bool = True,
    parallel_workers: int = 0,
) -> list[dict]:
    """
    Per ogni cluster: entry_price (open), entry_price_news (prezzo a notizia), ret_high/low per orizzonte (giorni borsa), max_drawdown_pct, max_runup_pct.
    progress_callback(i, total, ticker, error) opzionale per UI. errors_list: lista dove appendere {ticker, filing_day, error}.
    exclude_future_entry: se True, salta cluster dove entry sarebbe nel futuro (nessun prezzo disponibile).
    parallel_workers: se > 0, elabora i cluster in parallelo (es. 4); riduce i tempi se l'API lo consente.
    """
    out: list[dict] = []
    err_list = errors_list if errors_list is not None else []
    today = datetime.now().date().strftime("%Y-%m-%d")
    total = len(clusters)
    ticker_details_cache: dict[str, dict | None] = {}
    cache_lock = Lock()
    progress_lock = Lock()
    done_count = [0]  # list per mutabilità in closure

    def _run_one(args: tuple) -> tuple[int, dict | None, dict | None, str, str | None]:
        return _process_one_cluster(args[0], args[1], today, exclude_future_entry, ticker_details_cache, cache_lock)

    if parallel_workers and parallel_workers > 0:
        index_to_result: dict[int, tuple[dict | None, dict | None, str, str | None]] = {}
        with ThreadPoolExecutor(max_workers=parallel_workers) as executor:
            futures = {executor.submit(_run_one, (i, row)): i for i, row in enumerate(clusters)}
            for fut in as_completed(futures):
                i = futures[fut]
                try:
                    i, rec, err_entry, ticker, reason = fut.result()
                    index_to_result[i] = (rec, err_entry, ticker, reason)
                except Exception as e:
                    index_to_result[i] = (None, {"ticker": clusters[i].get("ticker", "?"), "filing_day": clusters[i].get("filing_day", "?"), "error": str(e)}, str(clusters[i].get("ticker", "?")), str(e))
                with progress_lock:
                    done_count[0] += 1
                    if progress_callback:
                        progress_callback(done_count[0], total, ticker, reason if err_entry else None)
        for idx in range(total):
            rec, err_entry, _t, _r = index_to_result[idx]
            if rec is not None:
                out.append(rec)
            if err_entry is not None:
                err_list.append(err_entry)
        return out

    for i, row in enumerate(clusters):
        if i > 0 and BACKTEST_DELAY_SEC > 0:
            time.sleep(BACKTEST_DELAY_SEC)
        ticker = (row.get("ticker") or "").strip().upper()
        filing_day = (row.get("filing_day") or row.get("filedAt") or "")[:10]
        filed_at = str(row.get("filedAt") or "")
        try:
            from_d = datetime.strptime(filing_day, "%Y-%m-%d").date()
            to_d = datetime.now().date()
            days_since_filing = (to_d - from_d).days
        except Exception:
            days_since_filing = None
        if not ticker or not filing_day:
            if exclude_future_entry:
                err_list.append({"ticker": ticker or "?", "filing_day": filing_day or "?", "error": "Ticker o filing_day mancante"})
                if progress_callback:
                    progress_callback(i + 1, total, ticker or "?", "Ticker o filing_day mancante")
                continue
            _empty_hl_keys = {}
            for n in TRADING_DAY_HORIZONS:
                _empty_hl_keys[f"ret_high_{n}d_open"] = _empty_hl_keys[f"ret_low_{n}d_open"] = None
                _empty_hl_keys[f"ret_high_{n}d_news"] = _empty_hl_keys[f"ret_low_{n}d_news"] = None
                _empty_hl_keys[f"ret_high_{n}d_news_bot"] = _empty_hl_keys[f"ret_low_{n}d_news_bot"] = None
                _empty_hl_keys[f"date_high_{n}d"] = _empty_hl_keys[f"date_low_{n}d"] = None
                _empty_hl_keys[f"datetime_high_{n}d"] = _empty_hl_keys[f"datetime_low_{n}d"] = None
            rec = {**row, "entry_price": None, "entry_price_news": None, "entry_price_news_bot": None, "entry_date": None, "entry_datetime": None, "max_drawdown_pct": None, "max_runup_pct": None, "days_since_filing": days_since_filing, "volume_entry": None, "vwap_entry": None, "range_pct_entry": None, "volume_avg_20d": None, "pct_from_52w_high": None, "rsi_entry": None, "ma50_entry": None, "ma200_entry": None, "market_cap": None, "list_date": None, "primary_exchange": None, "sic_code": None, "sic_description": None, **_empty_hl_keys}
            out.append(rec)
            if progress_callback:
                progress_callback(i + 1, total, ticker or "?", "Ticker o filing_day mancante")
            continue
        # Escludi filing con entry futura (prossimo giorno borsa non ancora disponibile)
        if exclude_future_entry:
            exp_entry = _expected_entry_date(filing_day, filed_at)
            if exp_entry and exp_entry > today:
                err_list.append({"ticker": ticker, "filing_day": filing_day, "error": "Entry date futura"})
                if progress_callback:
                    progress_callback(i + 1, total, ticker, "Entry date futura")
                continue
        entry_price, entry_date, entry_datetime, entry_price_news, high_low_returns, max_dd, max_runup, extra, api_error = _entry_and_forward_from_daily(ticker, filing_day, filed_at)
        reason = api_error if (entry_price is None and api_error) else None
        if exclude_future_entry and entry_price is None:
            err_list.append({"ticker": ticker, "filing_day": filing_day, "error": reason or "Nessun dato prezzi"})
            if progress_callback:
                progress_callback(i + 1, total, ticker, reason)
            continue
        rec = {
            **row,
            "entry_price": entry_price,
            "entry_price_news": entry_price_news,
            "entry_date": entry_date,
            "entry_datetime": entry_datetime,
            "max_drawdown_pct": max_dd,
            "max_runup_pct": max_runup,
            "days_since_filing": days_since_filing,
        }
        rec.update(extra)
        if reason:
            rec["backtest_reason"] = reason
        # Rendimento % per orizzonte + date/ora max/min
        for n in TRADING_DAY_HORIZONS:
            hl = high_low_returns.get(n) or {}
            ret_high_open = hl.get("high_open")
            ret_low_open = hl.get("low_open")
            ret_high_news = hl.get("high_news")
            ret_low_news = hl.get("low_news")
            mean_price_n = hl.get("mean_price")
            rec[f"ret_high_{n}d_open"] = ret_high_open
            rec[f"ret_low_{n}d_open"] = ret_low_open
            rec[f"ret_high_{n}d_news"] = ret_high_news
            rec[f"ret_low_{n}d_news"] = ret_low_news
            rec[f"ret_high_{n}d_news_bot"] = hl.get("high_news_bot")
            rec[f"ret_low_{n}d_news_bot"] = hl.get("low_news_bot")
            rec[f"ret_mean_{n}d_open"] = hl.get("mean_open")
            rec[f"ret_mean_{n}d_news"] = hl.get("mean_news")
            rec[f"ret_mean_{n}d_news_bot"] = hl.get("mean_news_bot")
            rec[f"mean_price_{n}d_open"] = mean_price_n
            rec[f"mean_price_{n}d_news"] = mean_price_n
            rec[f"mean_price_{n}d_news_bot"] = mean_price_n
            rec[f"date_high_{n}d"] = hl.get("date_high")
            rec[f"date_low_{n}d"] = hl.get("date_low")
            rec[f"datetime_high_{n}d"] = hl.get("datetime_high")
            rec[f"datetime_low_{n}d"] = hl.get("datetime_low")
            # Exit price calcolati dalle % di rendimento dove possibile
            if entry_price not in (None, 0) and ret_high_open is not None:
                rec[f"exit_high_{n}d_open_price"] = round(entry_price * (1 + ret_high_open / 100.0), 4)
            if entry_price not in (None, 0) and ret_low_open is not None:
                rec[f"exit_low_{n}d_open_price"] = round(entry_price * (1 + ret_low_open / 100.0), 4)
            if mean_price_n is not None and entry_price not in (None, 0):
                rec[f"exit_mean_{n}d_open_price"] = round(mean_price_n, 4)
            if entry_price_news not in (None, 0) and ret_high_news is not None:
                rec[f"exit_high_{n}d_news_price"] = round(entry_price_news * (1 + ret_high_news / 100.0), 4)
            if entry_price_news not in (None, 0) and ret_low_news is not None:
                rec[f"exit_low_{n}d_news_price"] = round(entry_price_news * (1 + ret_low_news / 100.0), 4)
            if mean_price_n is not None and entry_price_news not in (None, 0):
                rec[f"exit_mean_{n}d_news_price"] = round(mean_price_n, 4)
            entry_price_news_bot = rec.get("entry_price_news_bot")
            if entry_price_news_bot not in (None, 0) and hl.get("high_news_bot") is not None:
                rec[f"exit_high_{n}d_news_bot_price"] = round(entry_price_news_bot * (1 + hl["high_news_bot"] / 100.0), 4)
            if entry_price_news_bot not in (None, 0) and hl.get("low_news_bot") is not None:
                rec[f"exit_low_{n}d_news_bot_price"] = round(entry_price_news_bot * (1 + hl["low_news_bot"] / 100.0), 4)
            if mean_price_n is not None and entry_price_news_bot not in (None, 0):
                rec[f"exit_mean_{n}d_news_bot_price"] = round(mean_price_n, 4)
        # Alias per compatibilità con app/ai_analysis: ret_Nd = ret_high_Nd_open
        for n in TRADING_DAY_HORIZONS:
            rec[f"ret_{n}d"] = rec.get(f"ret_high_{n}d_open")
        rec["ret_24h"] = rec.get("ret_high_1d_open")
        rec["ret_48h"] = rec.get("ret_high_2d_open")
        rec["ret_72h"] = rec.get("ret_high_3d_open")
        # Reference API: market_cap, list_date, primary_exchange, sic_code
        ticker_api = _normalize_ticker_for_api(ticker)
        if entry_price is not None and entry_date:
            cache_key = f"{ticker_api or ticker}:{entry_date[:10]}"
            if cache_key not in ticker_details_cache:
                if BACKTEST_DELAY_SEC > 0:
                    time.sleep(BACKTEST_DELAY_SEC)
                details, _ = fetch_ticker_details(ticker_api or ticker, entry_date)
                ticker_details_cache[cache_key] = details
            details = ticker_details_cache[cache_key]
            if details:
                rec["market_cap"] = details.get("market_cap")
                rec["list_date"] = details.get("list_date")
                rec["primary_exchange"] = details.get("primary_exchange")
                rec["sic_code"] = details.get("sic_code")
                rec["sic_description"] = details.get("sic_description")
            else:
                for k in ("market_cap", "list_date", "primary_exchange", "sic_code", "sic_description"):
                    rec[k] = None
        else:
            for k in ("market_cap", "list_date", "primary_exchange", "sic_code", "sic_description"):
                rec[k] = None
        out.append(rec)
        if reason:
            err_list.append({"ticker": ticker, "filing_day": filing_day, "error": reason})
        if progress_callback:
            progress_callback(i + 1, total, ticker, reason)
    return out
