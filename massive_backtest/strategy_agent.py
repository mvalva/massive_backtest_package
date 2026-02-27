"""
Agente che propone strategie per sfruttare i buy SEC (Form 4, codice P),
esegue backtest su 3 anni di dati Massive e seleziona le migliori strategie.

Strategie = combinazioni di:
- Ruolo, variazione % posizione, dimensione, filtri
- Entry: open (primo prezzo a mercato aperto) o news (prezzo fattibile a notizia, pre/after market)
- Orizzonte: N giorni di borsa (1, 2, 3, 5, 7, 10, 14, 30, 60, 90)
- Metrica: high = massimo raggiunto nel periodo, low = minimo raggiunto (best/worst case)
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Callable, Protocol

import pandas as pd


class ProgressCallback(Protocol):
    """Callback per aggiornamento progresso: (messaggio, percentuale 0-100)."""

    def __call__(self, msg: str, pct: float) -> None: ...

try:
    from massive_backtest.sec_data import load_sec_buys, group_by_cluster, get_rows_for_clustering, rows_with_aggregated, insider_entry_prices_by_cluster, LAST_SEC_COVERAGE
    from massive_backtest.backtest_engine import run_backtest, TRADING_DAY_HORIZONS
except ImportError:
    from sec_data import load_sec_buys, group_by_cluster, get_rows_for_clustering, rows_with_aggregated, insider_entry_prices_by_cluster, LAST_SEC_COVERAGE
    from backtest_engine import run_backtest, TRADING_DAY_HORIZONS

# Chiavi hold = (high/low) x (open / news / news_bot / insider) x orizzonte in giorni borsa
HOLD_KEYS = [
    k
    for n in TRADING_DAY_HORIZONS
    for k in (
        f"ret_high_{n}d_open", f"ret_low_{n}d_open",
        f"ret_high_{n}d_news", f"ret_low_{n}d_news",
        f"ret_high_{n}d_news_bot", f"ret_low_{n}d_news_bot",
        f"ret_high_{n}d_insider", f"ret_low_{n}d_insider",
    )
]

# Costanti per report e strategia 10k (evitano magic number sparsi)
REPORT_CASES_TOP_N = 30
REPORT_CASES_BOTTOM_N = 30
STRATEGY_10K_BUDGET = 10_000.0
STRATEGY_10K_LOOKBACK_DAYS = 365
# 0 o None = nessun limite sul numero di posizioni (tutte quelle che rispettano la strategia)
STRATEGY_10K_MAX_POSITIONS = 0

# Lunghezza massima per data/ora in tabelle report (evita colonne troppo larghe)
_DATETIME_DISPLAY_LEN = 22
# Timezone di tutti gli orari nei report (filedAt SEC, entry, uscita, datetime_high/low)
REPORT_DATETIME_TZ = "ET (America/New_York)"


def _cluster_key_from_row(row) -> str:
    """Chiave univoca cluster: TICKER|YYYY-MM-DD (da ticker + filing_day/filedAt)."""
    t = str(row.get("ticker", "")).strip().upper()
    d = str(row.get("filing_day", "") or row.get("filedAt", "")).strip()[:10]
    return f"{t}|{d}" if t and d else ""


def _canonical_cluster_columns(columns: list[str], include_run_base: bool = False) -> list[str]:
    """
    Ordine logico e consistente per tutti i file cluster/backtest (CASES, ALL_CLUSTERS_DB, CASES_KEYS).
    Per ogni orizzonte: ret/exit high/low/mean per open, news, news_bot, insider; mean_price; date/datetime.
    """
    identity = ["ticker", "filing_day", "filedAt"]
    entry = ["entry_date", "entry_datetime", "entry_price", "entry_price_news", "entry_price_news_bot", "insider_entry_price", "days_since_filing"]
    per_horizon = []
    for n in TRADING_DAY_HORIZONS:
        per_horizon.extend([
            f"ret_high_{n}d_open", f"ret_low_{n}d_open", f"ret_mean_{n}d_open",
            f"ret_high_{n}d_news", f"ret_low_{n}d_news", f"ret_mean_{n}d_news",
            f"ret_high_{n}d_news_bot", f"ret_low_{n}d_news_bot", f"ret_mean_{n}d_news_bot",
            f"ret_high_{n}d_insider", f"ret_low_{n}d_insider", f"ret_mean_{n}d_insider",
            f"exit_high_{n}d_open_price", f"exit_low_{n}d_open_price", f"exit_mean_{n}d_open_price",
            f"exit_high_{n}d_news_price", f"exit_low_{n}d_news_price", f"exit_mean_{n}d_news_price",
            f"exit_high_{n}d_news_bot_price", f"exit_low_{n}d_news_bot_price", f"exit_mean_{n}d_news_bot_price",
            f"exit_high_{n}d_insider_price", f"exit_low_{n}d_insider_price", f"exit_mean_{n}d_insider_price",
            f"mean_price_{n}d_open", f"mean_price_{n}d_news", f"mean_price_{n}d_news_bot", f"mean_price_{n}d_insider",
            f"date_high_{n}d", f"date_low_{n}d", f"datetime_high_{n}d", f"datetime_low_{n}d",
        ])
    alias = ["ret_24h", "ret_48h", "ret_72h"] + [f"ret_{n}d" for n in TRADING_DAY_HORIZONS]
    risk = ["max_drawdown_pct", "max_runup_pct"]
    ta = ["volume_entry", "vwap_entry", "range_pct_entry", "volume_avg_20d", "pct_from_52w_high", "rsi_entry", "ma50_entry", "ma200_entry"]
    company = ["market_cap", "list_date", "primary_exchange", "sic_code", "sic_description"]
    run_meta = ["run_base"] if include_run_base else []
    other_known = ["backtest_reason"]
    ordered = identity + entry + per_horizon + alias + risk + ta + company + run_meta + other_known
    # Solo colonne presenti in columns, nell'ordine definito; il resto in coda (alfabetico)
    col_set = set(columns)
    out = [c for c in ordered if c in col_set]
    remainder = sorted(col_set - set(out))
    return out + remainder


def _fmt(v, decimals=2):
    """Formatta valore per tabelle report; gestisce None/NaN."""
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return ""
    if isinstance(v, float):
        return f"{v:.{decimals}f}" if v == v else ""
    return str(v)


@dataclass
class StrategyDef:
    """Definizione di una strategia: nome, filtro sui cluster, orizzonte di hold."""
    name: str
    filter_fn: Callable[[dict], bool]
    hold_key: str  # es. "ret_7d"
    description: str = ""


def _title_contains(cluster: dict, *keywords: str) -> bool:
    titles = (cluster.get("titles") or "").lower()
    return any(kw.lower() in titles for kw in keywords)


def _value_tot(cluster: dict) -> float:
    try:
        return float(cluster.get("value_tot") or 0)
    except (TypeError, ValueError):
        return 0.0


def _qty_tot(cluster: dict) -> float:
    try:
        return float(cluster.get("qty_tot") or 0)
    except (TypeError, ValueError):
        return 0.0


def all_clusters(_: dict) -> bool:
    return True


def filter_ceo_cfo(c: dict) -> bool:
    return _title_contains(c, "CEO", "CFO", "Chief Executive", "Chief Financial")


def filter_ceo_only(c: dict) -> bool:
    """Cluster dove chi compra include CEO (Chief Executive)."""
    return _title_contains(c, "CEO", "Chief Executive")


def filter_cfo_only(c: dict) -> bool:
    """Cluster dove chi compra include CFO (Chief Financial)."""
    return _title_contains(c, "CFO", "Chief Financial")


def filter_director(c: dict) -> bool:
    return _title_contains(c, "Director")


def filter_director_only(c: dict) -> bool:
    """Solo Director (nessun CEO/CFO nello stesso cluster)."""
    return _title_contains(c, "Director") and not _title_contains(c, "CEO", "CFO", "Chief Executive", "Chief Financial")


def _has_role(cluster: dict, *keywords: str) -> bool:
    """True se titles contiene almeno uno dei keyword (per combinazioni ruolo)."""
    return _title_contains(cluster, *keywords)


def filter_ceo_and_cfo(c: dict) -> bool:
    """Cluster dove comprano sia CEO sia CFO (combo)."""
    return _has_role(c, "CEO", "Chief Executive") and _has_role(c, "CFO", "Chief Financial")


def filter_ceo_and_director(c: dict) -> bool:
    """Cluster con almeno CEO e Director."""
    return _has_role(c, "CEO", "Chief Executive") and _has_role(c, "Director")


def filter_cfo_and_director(c: dict) -> bool:
    """Cluster con almeno CFO e Director."""
    return _has_role(c, "CFO", "Chief Financial") and _has_role(c, "Director")


def filter_officer(c: dict) -> bool:
    return _title_contains(c, "Officer", "President", "CEO", "CFO", "Chief")


def filter_value_gt_50k(c: dict) -> bool:
    return _value_tot(c) >= 50_000


def filter_value_gt_100k(c: dict) -> bool:
    return _value_tot(c) >= 100_000


def filter_value_gt_500k(c: dict) -> bool:
    return _value_tot(c) >= 500_000


def filter_value_gt_1m(c: dict) -> bool:
    return _value_tot(c) >= 1_000_000


def filter_qty_ge(cluster: dict, min_shares: float) -> bool:
    return _qty_tot(cluster) >= min_shares


def filter_qty_ge_5k(c: dict) -> bool:
    return _qty_tot(c) >= 5_000


def filter_qty_ge_10k(c: dict) -> bool:
    return _qty_tot(c) >= 10_000


def filter_qty_ge_50k(c: dict) -> bool:
    return _qty_tot(c) >= 50_000


def filter_qty_ge_100k(c: dict) -> bool:
    return _qty_tot(c) >= 100_000


def filter_multiple_buys(c: dict) -> bool:
    return (c.get("n_buys") or 0) >= 2


def filter_ten_percent_owner(c: dict) -> bool:
    return _title_contains(c, "10% Owner", "10% owner")


def _make_cap_ge_filter(min_cap: float):
    """Restituisce un filtro: market cap >= min_cap (in USD)."""
    def fn(c: dict) -> bool:
        mc = c.get("market_cap")
        try:
            return mc is not None and float(mc) >= min_cap
        except (TypeError, ValueError):
            return False
    return fn


def _make_cap_range_filter(min_cap: float, max_cap: float):
    """Restituisce un filtro: min_cap <= market cap <= max_cap (USD)."""
    def fn(c: dict) -> bool:
        mc = c.get("market_cap")
        try:
            return mc is not None and min_cap <= float(mc) <= max_cap
        except (TypeError, ValueError):
            return False
    return fn


# Filtri market cap (1 = escludi mc=0)
filter_small_cap = _make_cap_range_filter(1, 1_000_000_000)
filter_micro_cap = _make_cap_range_filter(1, 250_000_000)
filter_micro_cap_100m = _make_cap_range_filter(1, 100_000_000)
filter_micro_cap_50m = _make_cap_range_filter(1, 50_000_000)
filter_mid_cap = _make_cap_range_filter(1_000_000_000, 10_000_000_000)
filter_large_cap = _make_cap_ge_filter(10_000_000_000)
filter_cap_ge_1b = _make_cap_ge_filter(1_000_000_000)


# Soglie market cap testate (più granulari: micro, small, mid, large)
# La migliore emerge dal backtest/ranking.
CAP_THRESHOLDS = [
    (250_000_000, "250M"),
    (500_000_000, "500M"),
    (750_000_000, "750M"),
    (1_000_000_000, "1B"),
    (2_000_000_000, "2B"),
    (3_000_000_000, "3B"),
    (5_000_000_000, "5B"),
    (10_000_000_000, "10B"),
    (20_000_000_000, "20B"),
    (50_000_000_000, "50B"),
    (100_000_000_000, "100B"),
]
_filter_cap_ge_cache: dict[float, Callable[[dict], bool]] = {}
for _cap_val, _ in CAP_THRESHOLDS:
    _filter_cap_ge_cache[_cap_val] = _make_cap_ge_filter(_cap_val)


def filter_near_52w_high(c: dict) -> bool:
    """Titoli vicini ai massimi a 52 settimane (es. entro -10%)."""
    v = c.get("pct_from_52w_high")
    try:
        return v is not None and float(v) >= -10.0
    except (TypeError, ValueError):
        return False


def filter_far_52w_high(c: dict) -> bool:
    """Titoli ben sotto i massimi (es. <= -30%)."""
    v = c.get("pct_from_52w_high")
    try:
        return v is not None and float(v) <= -30.0
    except (TypeError, ValueError):
        return False


# Analisi tecnica a entry (RSI, MA)
def _float_entry(c: dict, key: str) -> float | None:
    v = c.get(key)
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _rsi_entry(c: dict) -> float | None:
    return _float_entry(c, "rsi_entry")


def _ma50_entry(c: dict) -> float | None:
    return _float_entry(c, "ma50_entry")


def _ma200_entry(c: dict) -> float | None:
    return _float_entry(c, "ma200_entry")


def filter_rsi_oversold(c: dict) -> bool:
    """RSI(14) a entry < 30 (oversold, potenziale rimbalzo)."""
    rsi = _rsi_entry(c)
    return rsi is not None and rsi < 30


def filter_rsi_overbought(c: dict) -> bool:
    """RSI(14) a entry > 70 (overbought)."""
    rsi = _rsi_entry(c)
    return rsi is not None and rsi > 70


def filter_rsi_neutral(c: dict) -> bool:
    """RSI(14) tra 40 e 60 (zona neutra)."""
    rsi = _rsi_entry(c)
    return rsi is not None and 40 <= rsi <= 60


def _make_price_vs_ma_filter(above: bool, ma_key: str):
    """Restituisce un filtro: prezzo entry > MA o < MA (secondo above)."""
    get_ma = _ma50_entry if ma_key == "ma50_entry" else _ma200_entry

    def fn(c: dict) -> bool:
        entry = c.get("entry_price")
        ma = get_ma(c)
        if entry is None or ma is None or (above and ma == 0):
            return False
        try:
            return (float(entry) > float(ma)) if above else (float(entry) < float(ma))
        except (TypeError, ValueError):
            return False
    return fn


filter_price_above_ma50 = _make_price_vs_ma_filter(True, "ma50_entry")   # momentum positivo
filter_price_below_ma50 = _make_price_vs_ma_filter(False, "ma50_entry")
filter_price_above_ma200 = _make_price_vs_ma_filter(True, "ma200_entry")  # trend lungo
filter_price_below_ma200 = _make_price_vs_ma_filter(False, "ma200_entry")


def _pct_increase_max(cluster: dict) -> float | None:
    """Variazione % posizione (max nel cluster). None se dato non disponibile."""
    v = cluster.get("pct_increase_position_max")
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def filter_pct_increase_ge_10(c: dict) -> bool:
    """Almeno un insider ha aumentato la propria posizione del 10% o più."""
    v = _pct_increase_max(c)
    return v is not None and v >= 10.0


def filter_pct_increase_ge_20(c: dict) -> bool:
    """Almeno un insider ha aumentato la propria posizione del 20% o più."""
    v = _pct_increase_max(c)
    return v is not None and v >= 20.0


def filter_pct_increase_ge_30(c: dict) -> bool:
    """Almeno un insider ha aumentato la propria posizione del 30% o più."""
    v = _pct_increase_max(c)
    return v is not None and v >= 30.0


# Catalogo strategie: (filtro, hold) con nome e descrizione
STRATEGY_DEFINITIONS: list[StrategyDef] = []

for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Tutti — hold {hk}",
        filter_fn=all_clusters,
        hold_key=hk,
        description="Tutti i cluster SEC P, nessun filtro.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO/CFO — hold {hk}",
        filter_fn=filter_ceo_cfo,
        hold_key=hk,
        description="Solo insider con titolo CEO o CFO.",
    ))

# Ruolo singolo: CEO only, CFO only, Director only
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO only — hold {hk}",
        filter_fn=filter_ceo_only,
        hold_key=hk,
        description="Solo cluster dove chi compra include CEO.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CFO only — hold {hk}",
        filter_fn=filter_cfo_only,
        hold_key=hk,
        description="Solo cluster dove chi compra include CFO.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Director — hold {hk}",
        filter_fn=filter_director,
        hold_key=hk,
        description="Solo Director (può coesistere con altri ruoli).",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Director only (no C-level) — hold {hk}",
        filter_fn=filter_director_only,
        hold_key=hk,
        description="Solo Director, nessun CEO/CFO nello stesso cluster.",
    ))

# Combinazioni di ruoli (es. CEO e CFO insieme)
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO + CFO (combo) — hold {hk}",
        filter_fn=filter_ceo_and_cfo,
        hold_key=hk,
        description="Cluster dove comprano sia CEO sia CFO.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO + Director (combo) — hold {hk}",
        filter_fn=filter_ceo_and_director,
        hold_key=hk,
        description="Cluster con almeno CEO e Director.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CFO + Director (combo) — hold {hk}",
        filter_fn=filter_cfo_and_director,
        hold_key=hk,
        description="Cluster con almeno CFO e Director.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Value ≥100k — hold {hk}",
        filter_fn=filter_value_gt_100k,
        hold_key=hk,
        description="Solo cluster con valore totale acquisto ≥ 100k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO/CFO + Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_cfo, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="CEO/CFO e valore totale ≥ 100k $.",
    ))

# Officer / President
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Officer/President — hold {hk}",
        filter_fn=filter_officer,
        hold_key=hk,
        description="Officer / President / C-level.",
    ))

# 10% Owner
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"10% Owner — hold {hk}",
        filter_fn=filter_ten_percent_owner,
        hold_key=hk,
        description="Solo insider con ruolo 10% Owner.",
    ))

# Ruolo × valore: CEO/CFO/ Director/10% + soglia valore
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO only + Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_only, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="CEO e valore totale acquisto ≥ 100k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO only + Value ≥500k — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_only, f2=filter_value_gt_500k: f1(c) and f2(c),
        hold_key=hk,
        description="CEO e valore totale ≥ 500k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CFO only + Value ≥50k — hold {hk}",
        filter_fn=lambda c, f1=filter_cfo_only, f2=filter_value_gt_50k: f1(c) and f2(c),
        hold_key=hk,
        description="CFO e valore totale ≥ 50k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CFO only + Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_cfo_only, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="CFO e valore totale ≥ 100k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Director only + Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_director_only, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="Solo Director (no C-level) e valore ≥ 100k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"10% Owner + Value ≥500k — hold {hk}",
        filter_fn=lambda c, f1=filter_ten_percent_owner, f2=filter_value_gt_500k: f1(c) and f2(c),
        hold_key=hk,
        description="10% Owner e valore totale ≥ 500k $.",
    ))

# Variazione % posizione (hanno aumentato posizione del 10% / 20% / 30%) — pure e per ruolo
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Position +10% — hold {hk}",
        filter_fn=filter_pct_increase_ge_10,
        hold_key=hk,
        description="Almeno un insider ha aumentato la propria posizione del 10% o più.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Position +20% — hold {hk}",
        filter_fn=filter_pct_increase_ge_20,
        hold_key=hk,
        description="Almeno un insider ha aumentato la posizione del 20% o più.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Position +30% — hold {hk}",
        filter_fn=filter_pct_increase_ge_30,
        hold_key=hk,
        description="Almeno un insider ha aumentato la posizione del 30% o più.",
    ))

# Ruolo × variazione % posizione (es. CEO + Position +10%)
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO only + Position +10% — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_only, f2=filter_pct_increase_ge_10: f1(c) and f2(c),
        hold_key=hk,
        description="CEO e aumento posizione ≥10%.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO only + Position +20% — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_only, f2=filter_pct_increase_ge_20: f1(c) and f2(c),
        hold_key=hk,
        description="CEO e aumento posizione ≥20%.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CFO only + Position +10% — hold {hk}",
        filter_fn=lambda c, f1=filter_cfo_only, f2=filter_pct_increase_ge_10: f1(c) and f2(c),
        hold_key=hk,
        description="CFO e aumento posizione ≥10%.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CFO only + Position +20% — hold {hk}",
        filter_fn=lambda c, f1=filter_cfo_only, f2=filter_pct_increase_ge_20: f1(c) and f2(c),
        hold_key=hk,
        description="CFO e aumento posizione ≥20%.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Director only + Position +10% — hold {hk}",
        filter_fn=lambda c, f1=filter_director_only, f2=filter_pct_increase_ge_10: f1(c) and f2(c),
        hold_key=hk,
        description="Solo Director e aumento posizione ≥10%.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"10% Owner + Position +10% — hold {hk}",
        filter_fn=lambda c, f1=filter_ten_percent_owner, f2=filter_pct_increase_ge_10: f1(c) and f2(c),
        hold_key=hk,
        description="10% Owner e aumento posizione ≥10%.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"10% Owner + Position +20% — hold {hk}",
        filter_fn=lambda c, f1=filter_ten_percent_owner, f2=filter_pct_increase_ge_20: f1(c) and f2(c),
        hold_key=hk,
        description="10% Owner e aumento posizione ≥20%.",
    ))

# Combo ruoli × variazione % posizione
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO+CFO (combo) + Position +10% — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_and_cfo, f2=filter_pct_increase_ge_10: f1(c) and f2(c),
        hold_key=hk,
        description="CEO e CFO insieme e aumento posizione ≥10%.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"CEO+CFO (combo) + Position +20% — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_and_cfo, f2=filter_pct_increase_ge_20: f1(c) and f2(c),
        hold_key=hk,
        description="CEO e CFO insieme e aumento posizione ≥20%.",
    ))

# Quantità (azioni) pure: bande qty_tot
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Qty ≥5k shares — hold {hk}",
        filter_fn=filter_qty_ge_5k,
        hold_key=hk,
        description="Almeno 5k azioni acquistate nel cluster.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Qty ≥10k shares — hold {hk}",
        filter_fn=filter_qty_ge_10k,
        hold_key=hk,
        description="Almeno 10k azioni acquistate.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Qty ≥50k shares — hold {hk}",
        filter_fn=filter_qty_ge_50k,
        hold_key=hk,
        description="Almeno 50k azioni acquistate.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Qty ≥100k shares — hold {hk}",
        filter_fn=filter_qty_ge_100k,
        hold_key=hk,
        description="Almeno 100k azioni acquistate.",
    ))

# Value ≥50k e ≥500k e ≥1M
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Value ≥50k — hold {hk}",
        filter_fn=filter_value_gt_50k,
        hold_key=hk,
        description="Valore totale acquisto ≥ 50k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Value ≥500k — hold {hk}",
        filter_fn=filter_value_gt_500k,
        hold_key=hk,
        description="Valore totale acquisto ≥ 500k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Value ≥1M — hold {hk}",
        filter_fn=filter_value_gt_1m,
        hold_key=hk,
        description="Valore totale acquisto ≥ 1M $.",
    ))

# Multiple buys (almeno 2 trade nel cluster)
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Multiple buys (n≥2) — hold {hk}",
        filter_fn=filter_multiple_buys,
        hold_key=hk,
        description="Almeno 2 transazioni P nello stesso cluster (buy ripetuti).",
    ))

# Combinazioni più sofisticate: market cap (dettaglio micro / small / mid / large)
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Micro cap (≤50M) CEO/CFO — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_cfo, f2=filter_micro_cap_50m: f1(c) and f2(c),
        hold_key=hk,
        description="Solo micro cap (market cap ≤50M) con insider CEO/CFO.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Micro cap (≤100M) CEO/CFO — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_cfo, f2=filter_micro_cap_100m: f1(c) and f2(c),
        hold_key=hk,
        description="Solo micro cap (market cap ≤100M) con insider CEO/CFO.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Micro cap (≤250M) CEO/CFO — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_cfo, f2=filter_micro_cap: f1(c) and f2(c),
        hold_key=hk,
        description="Solo micro cap (market cap ≤250M) con insider CEO/CFO.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Small cap (≤1B) CEO/CFO — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_cfo, f2=filter_small_cap: f1(c) and f2(c),
        hold_key=hk,
        description="Solo small cap (market cap ≤1B) con insider CEO/CFO.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Mid cap (1B–10B) CEO/CFO — hold {hk}",
        filter_fn=lambda c, f1=filter_ceo_cfo, f2=filter_mid_cap: f1(c) and f2(c),
        hold_key=hk,
        description="Solo mid cap (market cap tra 1B e 10B) con insider CEO/CFO.",
    ))
for cap_val, cap_label in CAP_THRESHOLDS:
    _f = _filter_cap_ge_cache[cap_val]
    for hk in HOLD_KEYS:
        STRATEGY_DEFINITIONS.append(StrategyDef(
            name=f"Large cap (≥{cap_label}) CEO/CFO — hold {hk}",
            filter_fn=lambda c, f1=filter_ceo_cfo, f2=_f: f1(c) and f2(c),
            hold_key=hk,
            description=f"Solo market cap ≥{cap_label} con insider CEO/CFO. Soglie testate: 250M, 500M, 750M, 1B, 2B, 3B, 5B, 10B, 20B, 50B.",
        ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Micro cap (≤50M) Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_micro_cap_50m, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="Micro cap (≤50M) con acquisti di valore ≥100k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Micro cap (≤100M) Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_micro_cap_100m, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="Micro cap (≤100M) con acquisti di valore ≥100k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Micro cap (≤250M) Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_micro_cap, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="Micro cap (≤250M) con acquisti di valore ≥100k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Small cap (≤1B) Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_small_cap, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="Small cap con acquisti di valore ≥100k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Mid cap (1B–10B) Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_mid_cap, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="Mid cap (1B–10B) con acquisti di valore ≥100k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Near 52w high + CEO/CFO — hold {hk}",
        filter_fn=lambda c, f1=filter_near_52w_high, f2=filter_ceo_cfo: f1(c) and f2(c),
        hold_key=hk,
        description="Titoli vicini ai massimi a 52w con insider CEO/CFO (momentum insider).",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Far 52w high + Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_far_52w_high, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="Titoli ben sotto i massimi (value) con grossi acquisti ≥100k $.",
    ))

# Analisi tecnica: RSI, prezzo vs MA
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"RSI oversold (<30) — hold {hk}",
        filter_fn=filter_rsi_oversold,
        hold_key=hk,
        description="RSI(14) a entry < 30 (oversold).",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"RSI overbought (>70) — hold {hk}",
        filter_fn=filter_rsi_overbought,
        hold_key=hk,
        description="RSI(14) a entry > 70.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Price > MA50 — hold {hk}",
        filter_fn=filter_price_above_ma50,
        hold_key=hk,
        description="Prezzo entry sopra media mobile 50 gg.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Price < MA50 — hold {hk}",
        filter_fn=filter_price_below_ma50,
        hold_key=hk,
        description="Prezzo entry sotto MA50.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Price > MA200 — hold {hk}",
        filter_fn=filter_price_above_ma200,
        hold_key=hk,
        description="Prezzo entry sopra MA200 (trend lungo).",
    ))
# Combinazioni TA + ruolo
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"RSI oversold + CEO/CFO — hold {hk}",
        filter_fn=lambda c, f1=filter_rsi_oversold, f2=filter_ceo_cfo: f1(c) and f2(c),
        hold_key=hk,
        description="RSI < 30 e insider CEO/CFO.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"RSI oversold + Value ≥100k — hold {hk}",
        filter_fn=lambda c, f1=filter_rsi_oversold, f2=filter_value_gt_100k: f1(c) and f2(c),
        hold_key=hk,
        description="RSI oversold e acquisti ≥100k $.",
    ))
for hk in HOLD_KEYS:
    STRATEGY_DEFINITIONS.append(StrategyDef(
        name=f"Price > MA50 + CEO/CFO — hold {hk}",
        filter_fn=lambda c, f1=filter_price_above_ma50, f2=filter_ceo_cfo: f1(c) and f2(c),
        hold_key=hk,
        description="Prezzo sopra MA50 e insider CEO/CFO.",
    ))

# Strategie unificate: una riga per filtro con colonne high e low (orizzonte 30d). Usato per ranking e report.
HOLD_PRIMARY = "ret_high_30d_open"

def _strategy_name_base(name: str) -> str:
    """Estrae il nome base della strategia (senza ' — hold ...')."""
    if " — hold " in name:
        return name.split(" — hold ")[0].strip()
    return name


def _insider_type_from_strategy_name(name: str) -> str:
    """Estrae il tipo di insider dalla strategia (nome o base_name). Es: CEO, CFO, CEO+CFO, Director, 10% Owner, Officer, Qualsiasi."""
    s = (name or "").lower()
    if "ceo only" in s and "cfo" not in s:
        return "CEO"
    if "cfo only" in s:
        return "CFO"
    if "ceo" in s and "cfo" in s:
        return "CEO+CFO"
    if "10% owner" in s:
        return "10% Owner"
    if "director only" in s or "director" in s:
        return "Director"
    if "officer" in s or "president" in s:
        return "Officer"
    if "position" in s or "variazione" in s or "pct" in s:
        return "Position change"
    if "value" in s or "qty" in s or "shares" in s:
        return "Qualsiasi (value/qty)"
    return "Qualsiasi"


def _ta_profile_from_strategy_name(name: str) -> str:
    """
    Classifica la strategia per profilo di analisi tecnica, per filtri UI/ranking fine.

    Valori possibili (principali):
        - "SEC only"         → nessun uso di TA (solo ruolo/cap/value/qty/posizione)
        - "RSI / momentum"   → strategie che usano RSI/overbought/oversold/neutral
        - "52w range"        → strategie che usano distanza da 52w high/low
        - "MA / trend"       → strategie che usano MA50/MA200/Price vs MA
        - "TA combo"         → altre combinazioni di segnali tecnici
    """
    s = (name or "").lower()
    if _is_sec_only_strategy(s):
        return "SEC only"
    has_rsi = ("rsi" in s) or ("oversold" in s) or ("overbought" in s) or ("neutral" in s)
    has_52w = ("52w" in s) or ("near 52w" in s) or ("far 52w" in s)
    has_ma = ("ma50" in s) or ("ma200" in s) or ("price > ma" in s) or ("price < ma" in s)
    if has_rsi and not (has_52w or has_ma):
        return "RSI / momentum"
    if has_52w and not (has_rsi or has_ma):
        return "52w range"
    if has_ma and not (has_rsi or has_52w):
        return "MA / trend"
    return "TA combo"


def _is_sec_only_strategy(strategy_name: str) -> bool:
    """
    True se la strategia usa solo dati SEC (ruolo, value, qty, market cap, multiple buys, pct posizione).
    False se usa analisi tecnica (RSI, 52w, MA50, MA200, Price vs MA).
    """
    s = (strategy_name or "").lower()
    if not s:
        return True
    ta_keywords = ("rsi", "52w", "52w high", "ma50", "ma200", "price > ma", "price < ma", "oversold", "overbought", "neutral", "far 52w", "near 52w")
    return not any(k in s for k in ta_keywords)


def _market_cap_description_from_strategy_name(sname: str) -> str:
    """
    Da nome strategia estrae una descrizione chiara del filtro market cap per report/10K.
    Es.: "Large cap (≥2B) CEO/CFO" → "Market cap ≥ 2B"; "Micro cap (≤250M) CEO/CFO" → "Market cap ≤ 250M (micro cap)".
    """
    s = (sname or "").strip()
    if not s or "cap" not in s.lower():
        return "Nessun filtro market cap (tutti i market cap)"
    import re
    # Micro cap (≤50M, ≤100M, ≤250M)
    if "micro cap" in s.lower():
        if "50m" in s.lower() or "50M" in s:
            return "Market cap ≤ 50M (micro cap)"
        if "100m" in s.lower() or "100M" in s:
            return "Market cap ≤ 100M (micro cap)"
        if "250" in s:
            return "Market cap ≤ 250M (micro cap)"
    # Small cap (≤1B)
    if "small cap" in s.lower() and "1b" in s.lower():
        return "Market cap ≤ 1B (small cap)"
    # Mid cap (1B–10B)
    if "mid cap" in s.lower() and "1b" in s.lower() and "10b" in s.lower():
        return "Market cap 1B–10B (mid cap)"
    # Large cap (≥X)
    m = re.search(r"large\s*cap\s*\(≥\s*([^)]+)\)", s, re.I)
    if m:
        return "Market cap ≥ " + m.group(1).strip()
    # Fallback: estrai frammento tipo "cap (≥2B)" o "Small cap"
    idx = s.lower().find("cap")
    if idx != -1:
        frag = s[idx:]
        end = frag.find(")") + 1 if ")" in frag else len(frag)
        frag = frag[:end].strip()
        if frag:
            return "Market cap: " + frag
    return "Filtro market cap (vedi nome strategia)"


STRATEGY_DEFINITIONS_UNIFIED: list[StrategyDef] = []
_seen: set[str] = set()
for sd in STRATEGY_DEFINITIONS:
    base = _strategy_name_base(sd.name)
    if base in _seen:
        continue
    _seen.add(base)
    cand = next((x for x in STRATEGY_DEFINITIONS if _strategy_name_base(x.name) == base and x.hold_key == HOLD_PRIMARY), None)
    ref = cand if cand is not None else sd
    STRATEGY_DEFINITIONS_UNIFIED.append(StrategyDef(name=base, filter_fn=ref.filter_fn, hold_key=HOLD_PRIMARY, description=ref.description))


def compute_metrics(returns: pd.Series) -> dict:
    """Calcola metriche su una serie di rendimenti % (es. ret_7d)."""
    r = returns.dropna()
    if len(r) == 0:
        return {
            "n": 0,
            "win_rate_%": None,
            "avg_ret_%": None,
            "median_ret_%": None,
            "total_ret_%": None,
            "std_%": None,
            "sharpe_approx": None,
            "min_%": None,
            "max_%": None,
        }
    n = len(r)
    wins = (r > 0).sum()
    win_rate = wins / n * 100
    avg_ret = r.mean()
    median_ret = r.median()
    total_ret = r.sum()
    std_ret = r.std()
    sharpe_approx = (avg_ret / std_ret) if std_ret and std_ret != 0 else None
    return {
        "n": n,
        "win_rate_%": round(win_rate, 1),
        "avg_ret_%": round(avg_ret, 2),
        "median_ret_%": round(median_ret, 2),
        "total_ret_%": round(total_ret, 2),
        "std_%": round(std_ret, 2) if std_ret is not None else None,
        "sharpe_approx": round(sharpe_approx, 2) if sharpe_approx is not None else None,
        "min_%": round(r.min(), 2),
        "max_%": round(r.max(), 2),
    }


def run_agent(
    days_sec: int = 1095,
    max_results_sec: int = 5000,
    max_clusters: int = 0,
    parallel_workers: int = 0,
    progress_callback: ProgressCallback | None = None,
    errors_list: list | None = None,
) -> tuple[pd.DataFrame, list[dict], list[dict], list[dict]]:
    """
    Carica SEC buys, esegue backtest Massive, valuta tutte le strategie.

    Ritorna:
        - df_risultati_backtest (una riga per cluster SEC)
        - lista_errori_backtest
        - tabella_ranking_strategie come list[dict] (una riga per strategia+hold)
        - righe_SEC_originali per export (usate per SEC_TRANSACTIONS.csv)

    Note:
        - Per il backtest, più BUY sullo stesso ticker e stesso timestamp sono aggregati
          in una singola posizione (qty/value/price aggregati).
        - Nel ranking sono presenti tutte le combinazioni filtro + hold (ret_high/ret_low,
          1d/2d/…/90d, open/news/news_bot/insider). Per ogni riga:
              * Metric_kind ∈ {high, low, mean}
              * Horizon_days ∈ {1,2,3,5,7,10,14,30,60,90}
              * Entry_kind ∈ {open, news, news_bot, insider} (entry_price, entry_price_news, entry_price_news_bot, insider_entry_price)
        - Le righe con Metric_kind='mean' usano ret_mean_* = rendimento verso la media aritmetica
          di tutti i valori prezzo (O,H,L,C) nel periodo (barre es. 5 min); per analisi, non in 10k.
        - Se max_clusters > 0, vengono backtestati solo i primi max_clusters (utile
          per run veloci).
    """
    errors_list = errors_list if errors_list is not None else []
    if progress_callback:
        progress_callback("Caricamento SEC...", 0)
    rows, sec_err = load_sec_buys(
        days=days_sec,
        max_results=max_results_sec,
        exclude_funds=True,
        progress_callback=progress_callback,
    )
    if sec_err:
        raise RuntimeError(f"SEC: {sec_err}")
    if not rows:
        raise RuntimeError("Nessuna transazione SEC nel periodo.")
    if progress_callback:
        progress_callback(f"Cluster da {len(rows)} acquisti...", 10)
    # Per il backtest usiamo una riga aggregata per (ticker, filedAt):
    # qty = somma, value = somma, price = media ponderata (value/qty).
    rows_for_cluster = get_rows_for_clustering(rows)
    clusters = group_by_cluster(rows_for_cluster)
    if not clusters:
        raise RuntimeError("Nessun cluster.")
    if max_clusters and max_clusters > 0 and len(clusters) > max_clusters:
        clusters = clusters[:max_clusters]
        if progress_callback:
            progress_callback(f"Limitato a {len(clusters)} cluster (--max-clusters)...", 12)
    if progress_callback:
        progress_callback(f"Backtest Massive su {len(clusters)} cluster...", 20)
    def _progress(i: int, total: int, ticker: str, err: str | None):
        if progress_callback and total:
            pct = 20 + 60 * (i / total)
            progress_callback(f"Backtest {i}/{total} — {ticker}", pct)

    results = run_backtest(
        clusters,
        progress_callback=_progress,
        errors_list=errors_list,
        exclude_future_entry=True,
        parallel_workers=parallel_workers,
    )
    if progress_callback:
        progress_callback("Valutazione strategie...", 85)
    df = pd.DataFrame(results)
    # Prezzo di acquisto insider da SEC (value/qty per cluster): usato nell'analisi oltre a entry_price open/news
    insider_prices = insider_entry_prices_by_cluster(rows) if rows else {}
    if insider_prices:
        def _insider_price_for_row(r):
            t = str(r.get("ticker") or "").strip().upper()
            d = str(r.get("filing_day") or r.get("filedAt") or "")[:10]
            return insider_prices.get((t, d)) if t and len(d) >= 10 else None
        df["insider_entry_price"] = df.apply(_insider_price_for_row, axis=1)
    else:
        df["insider_entry_price"] = None
    # Rendimenti e exit price relativi a insider_entry_price (stesso high/low/mean del periodo, base = insider)
    for n in TRADING_DAY_HORIZONS:
        exit_high = f"exit_high_{n}d_open_price"
        exit_low = f"exit_low_{n}d_open_price"
        mean_col = f"mean_price_{n}d_open"
        if exit_high not in df.columns or exit_low not in df.columns:
            continue
        ins = pd.to_numeric(df["insider_entry_price"], errors="coerce")
        ok = ins.notna() & (ins > 0)
        eh = pd.to_numeric(df[exit_high], errors="coerce")
        el = pd.to_numeric(df[exit_low], errors="coerce")
        df[f"ret_high_{n}d_insider"] = ((eh - ins) / ins * 100).round(2).where(ok & eh.notna())
        df[f"ret_low_{n}d_insider"] = ((el - ins) / ins * 100).round(2).where(ok & el.notna())
        df[f"exit_high_{n}d_insider_price"] = df[exit_high]
        df[f"exit_low_{n}d_insider_price"] = df[exit_low]
        df[f"mean_price_{n}d_insider"] = df[mean_col] if mean_col in df.columns else None
        df[f"exit_mean_{n}d_insider_price"] = df[mean_col] if mean_col in df.columns else None
        if mean_col in df.columns:
            mn = pd.to_numeric(df[mean_col], errors="coerce")
            df[f"ret_mean_{n}d_insider"] = ((mn - ins) / ins * 100).round(2).where(ok & mn.notna())

    def _parse_hold_key(hold_key: str) -> tuple[str, int | None, str]:
        """
        Esempi:
            ret_high_30d_open -> ('high', 30, 'open')
            ret_low_7d_news   -> ('low', 7, 'news')
        """
        if hold_key.startswith("ret_high_"):
            metric_kind = "high"
        elif hold_key.startswith("ret_low_"):
            metric_kind = "low"
        elif hold_key.startswith("ret_mean_"):
            metric_kind = "mean"
        else:
            metric_kind = "other"
        try:
            core = hold_key.replace("ret_high_", "").replace("ret_low_", "").replace("ret_mean_", "")
            days_part, entry_kind = core.split("_", 1)
            horizon_days = int(days_part.replace("d", "")) if "d" in days_part else None
            if "news_bot" in entry_kind:
                entry_kind = "news_bot"
            elif "insider" in entry_kind:
                entry_kind = "insider"
            elif "news" in entry_kind:
                entry_kind = "news"
            else:
                entry_kind = "open"
        except Exception:
            horizon_days = None
            entry_kind = "open"
        return metric_kind, horizon_days, entry_kind

    # Costruiamo il ranking completo: una riga per ogni StrategyDef (filtro+hold).
    # Se esiste una colonna ret_mean_{n}d_{entry_kind}, aggiungiamo anche una riga "mean".
    strategy_rows: list[dict] = []
    empty_metrics = compute_metrics(pd.Series(dtype=float))

    mean_added: set[tuple[str, str]] = set()

    for sd in STRATEGY_DEFINITIONS:
        hold_col = sd.hold_key
        metric_kind, horizon_days, entry_kind = _parse_hold_key(hold_col)
        mask = df.apply(sd.filter_fn, axis=1)
        sub = df.loc[mask]
        if hold_col in df.columns:
            m = compute_metrics(sub[hold_col])
        else:
            m = empty_metrics
        base_name = _strategy_name_base(sd.name)
        # Lista ticker/cluster usati dalla strategia (per debug/verifiche).
        clusters_used_all: list[str] = []
        tickers_used_all: set[str] = set()
        clusters_used_n: list[str] = []
        tickers_used_n: set[str] = set()
        if not sub.empty:
            for _, row in sub.iterrows():
                ck = _cluster_key_from_row(row)
                if ck:
                    tickers_used_all.add(ck.split("|")[0])
                    clusters_used_all.append(ck)
            if hold_col in sub.columns:
                sub_valid = sub[sub[hold_col].notna()]
                for _, row in sub_valid.iterrows():
                    ck = _cluster_key_from_row(row)
                    if ck:
                        tickers_used_n.add(ck.split("|")[0])
                        clusters_used_n.append(ck)
        row = {
            "Strategia": sd.name,
            "Base_name": base_name,
            "Descrizione": sd.description,
            "Hold": hold_col,
            "Metric_kind": metric_kind,
            "Horizon_days": horizon_days,
            "Entry_kind": entry_kind,
            "News_vs_Open": "News" if entry_kind == "news" else ("News_bot" if entry_kind == "news_bot" else ("Insider" if entry_kind == "insider" else "Open")),
            "Insider_type": _insider_type_from_strategy_name(base_name),
            "TA_profile": _ta_profile_from_strategy_name(sd.name),
            # Tutti i cluster/ticker che passano il filtro
            "Tickers_used": ",".join(sorted(tickers_used_all)) if tickers_used_all else "",
            "Clusters_used": ",".join(clusters_used_all) if clusters_used_all else "",
            # Solo quelli effettivamente inclusi in N (serie non NaN per Hold)
            "Tickers_used_N": ",".join(sorted(tickers_used_n)) if tickers_used_n else "",
            "Clusters_used_N": ",".join(clusters_used_n) if clusters_used_n else "",
            "N": m["n"],
            "N_filter": len(sub),
            "Win_rate_%": m["win_rate_%"],
            "Avg_ret_%": m["avg_ret_%"],
            "Median_ret_%": m["median_ret_%"],
            "Total_ret_%": m["total_ret_%"],
            "Std_%": m["std_%"],
            "Sharpe": m["sharpe_approx"],
            "Min_%": m["min_%"],
            "Max_%": m["max_%"],
        }
        strategy_rows.append(row)
        # Aggiungi UNA sola riga "mean" per (Base_name, Horizon_days, Entry_kind) se esiste la colonna ret_mean_* coerente
        if horizon_days is not None:
            mean_col = f"ret_mean_{horizon_days}d_{entry_kind}"
            key_mean = (base_name, mean_col)
            if mean_col in df.columns and key_mean not in mean_added:
                try:
                    m_mean = compute_metrics(sub[mean_col])
                except Exception:
                    m_mean = empty_metrics
                row_mean = {
                    "Strategia": f"{base_name} — hold {mean_col}",
                    "Base_name": base_name,
                    "Descrizione": sd.description + " (mean: media aritmetica di tutti i valori O,H,L,C nel periodo, barre es. 5 min).",
                    "Hold": mean_col,
                    "Metric_kind": "mean",
                    "Horizon_days": horizon_days,
                    "Entry_kind": entry_kind,
                    "News_vs_Open": "News" if entry_kind == "news" else ("News_bot" if entry_kind == "news_bot" else ("Insider" if entry_kind == "insider" else "Open")),
                    "Insider_type": _insider_type_from_strategy_name(base_name),
                    "TA_profile": _ta_profile_from_strategy_name(sd.name),
                    "Tickers_used": ",".join(sorted(tickers_used_all)) if tickers_used_all else "",
                    "Clusters_used": ",".join(clusters_used_all) if clusters_used_all else "",
                    "Tickers_used_N": ",".join(sorted(tickers_used_n)) if tickers_used_n else "",
                    "Clusters_used_N": ",".join(clusters_used_n) if clusters_used_n else "",
                    "N": m_mean["n"],
                    "N_filter": len(sub),
                    "Win_rate_%": m_mean["win_rate_%"],
                    "Avg_ret_%": m_mean["avg_ret_%"],
                    "Median_ret_%": m_mean["median_ret_%"],
                    "Total_ret_%": m_mean["total_ret_%"],
                    "Std_%": m_mean["std_%"],
                    "Sharpe": m_mean["sharpe_approx"],
                    "Min_%": m_mean["min_%"],
                    "Max_%": m_mean["max_%"],
                }
                strategy_rows.append(row_mean)
                mean_added.add(key_mean)

    ranking_df = pd.DataFrame(strategy_rows)
    # Ordinamento di default: Avg_ret_% decrescente, poi per Horizon (es. 30d prima), poi tipo metrica.
    if not ranking_df.empty:
        ranking_df = ranking_df.sort_values(
            by=["Avg_ret_%", "Horizon_days", "Metric_kind"],
            ascending=[False, True, True],
            na_position="last",
        ).reset_index(drop=True)
        # Score / Ranking per strategia esatta (oltre a quelli per Base_name calcolati in export).
        strat_agg = ranking_df.groupby("Strategia", dropna=False).agg(
            mean_avg_ret=("Avg_ret_%", "mean"),
            mean_win_rate=("Win_rate_%", "mean"),
        ).reset_index()
        if not strat_agg.empty:
            r_min, r_max = strat_agg["mean_avg_ret"].min(), strat_agg["mean_avg_ret"].max()
            w_min, w_max = strat_agg["mean_win_rate"].min(), strat_agg["mean_win_rate"].max()
            if (r_max - r_min) != 0:
                norm_ret = (strat_agg["mean_avg_ret"] - r_min) / (r_max - r_min)
            else:
                norm_ret = 0.5
            if (w_max - w_min) != 0:
                norm_win = (strat_agg["mean_win_rate"] - w_min) / (w_max - w_min)
            else:
                norm_win = 0.5
            strat_agg["_score"] = 0.5 * norm_ret + 0.5 * norm_win
            strat_agg = strat_agg.sort_values("_score", ascending=False)
            strat_to_rank = {s: i for i, s in enumerate(strat_agg["Strategia"], 1)}
            strat_to_score = dict(zip(strat_agg["Strategia"], (strat_agg["_score"] * 100).round(2)))
            ranking_df["Ranking_strategy"] = ranking_df["Strategia"].map(strat_to_rank)
            ranking_df["Score_strategy"] = ranking_df["Strategia"].map(strat_to_score)
    if progress_callback:
        progress_callback("Completato.", 100)
    return df, errors_list, ranking_df.to_dict("records"), rows


def _cases_performance_score(row: pd.Series, prefer_high: bool = True) -> float:
    """Score per ordinare i casi: usa ret_high_30d_open (o 14d/7d) per 'migliori', ret_low_30d per 'peggiori'."""
    candidates_high = ["ret_high_30d_open", "ret_high_14d_open", "ret_high_7d_open", "ret_high_5d_open"]
    candidates_low = ["ret_low_30d_open", "ret_low_14d_open", "ret_low_7d_open", "ret_low_5d_open"]
    val = None
    if prefer_high:
        for k in candidates_high:
            if k in row and not pd.isna(row.get(k)):
                val = row.get(k)
                break
    else:
        for k in candidates_low:
            if k in row and not pd.isna(row.get(k)):
                val = row.get(k)
                break
    if val is None or pd.isna(val):
        return float("-inf") if prefer_high else float("inf")
    try:
        return float(val)
    except (TypeError, ValueError):
        return float("-inf") if prefer_high else float("inf")


def build_cases_report(
    df_results: pd.DataFrame,
    out_path: Path | None = None,
    top_n: int = 30,
    bottom_n: int = 30,
    include_all: bool = True,
) -> str:
    """
    Report caso per caso: azioni/cluster con evidenza migliori, peggiori e (se include_all) elenco completo.
    Genera un report leggibile (MD) e salva in out_path se fornito.
    Ritorna il testo del report.
    """
    if df_results.empty:
        report = "Nessun caso da analizzare (df_results vuoto)."
        if out_path:
            out_path.write_text(report, encoding="utf-8")
        return report
    df = df_results.copy()
    # Score migliori = ret_high massimo (best case)
    df["_score_best"] = df.apply(lambda r: _cases_performance_score(r, prefer_high=True), axis=1)
    # Score peggiori = ret_low minimo (worst case)
    df["_score_worst"] = df.apply(lambda r: _cases_performance_score(r, prefer_high=False), axis=1)
    df_best = df.nlargest(top_n, "_score_best").drop(columns=["_score_best", "_score_worst"], errors="ignore")
    df_worst = df.nsmallest(bottom_n, "_score_worst").drop(columns=["_score_best", "_score_worst"], errors="ignore")
    df_all_sorted = df.sort_values("_score_best", ascending=False).drop(columns=["_score_best", "_score_worst"], errors="ignore")
    # Data e ora: filedAt (filing), entry_datetime (entry); date/ora massimo e minimo; exit price (prezzo uscita) per orizzonte
    cols_display = ["ticker", "filedAt", "entry_datetime", "entry_price", "entry_price_news"]
    ret_cols = [c for c in df.columns if c.startswith("ret_high_") and "open" in c and c.endswith("d_open")]
    ret_cols = sorted(ret_cols, key=lambda x: int(x.split("_")[2].replace("d", "")))
    cols_display += ret_cols
    for suffix in ["datetime_high_30d", "datetime_low_30d"]:
        if suffix in df.columns:
            cols_display.append(suffix)
    for exit_col in ["exit_high_30d_open_price", "exit_low_30d_open_price"]:
        if exit_col in df.columns:
            cols_display.append(exit_col)
    cols_display += ["value_tot", "titles"]
    cols_display = [c for c in cols_display if c in df.columns]
    header = "| " + " | ".join(cols_display) + " |"
    sep = "|" + "|".join(["---"] * len(cols_display)) + "|"

    def _row_cells(r, cols):
        cells = [_fmt(r.get(c)) for c in cols]
        if "titles" in cols:
            idx = cols.index("titles")
            cells[idx] = (cells[idx] or "")[:60] + ("…" if len(cells[idx] or "") > 60 else "")
        for k in ("filedAt", "entry_datetime"):
            if k in cols:
                idx = cols.index(k)
                s = cells[idx] or ""
                cells[idx] = s[:_DATETIME_DISPLAY_LEN] + ("…" if len(s) > _DATETIME_DISPLAY_LEN else "")
        return cells

    lines = []
    lines.append("# Report caso per caso — Azioni (cluster SEC)")
    lines.append("")
    lines.append(f"**Timezone:** Tutti gli orari (filedAt, entry_datetime, datetime_high_30d, datetime_low_30d) sono in **{REPORT_DATETIME_TZ}**.")
    lines.append("")
    lines.append("**Entry price** = prezzo di acquisto (open) all’entry. **Exit price** = prezzo di uscita al massimo/minimo nell’orizzonte (entry × (1 + ret%/100)).")
    lines.append("")
    lines.append(f"Totale casi backtestati: **{len(df)}**. Per il **database completo** con tutte le colonne (data e ora filing, entry, **exit price** per ogni orizzonte, data/ora massimo e minimo, TA, market_cap) aprire **STRATEGY_AGENT_CASES.csv**.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Migliori (top per rendimento massimo nell’orizzonte)")
    lines.append("")
    lines.append("Casi con il **maggior rendimento massimo** (ret_high) nei giorni successivi all’entry (best case). **datetime_high_30d** / **datetime_low_30d** = data e ora in cui il ticker raggiunge massimo/minimo (orizzonte 30d), in " + REPORT_DATETIME_TZ + ".")
    lines.append("")
    if df_best.empty:
        lines.append("Nessun dato.")
    else:
        lines.append(header)
        lines.append(sep)
        for _, r in df_best.iterrows():
            lines.append("| " + " | ".join(_row_cells(r, cols_display)) + " |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Peggiori (bottom per rendimento minimo nell’orizzonte)")
    lines.append("")
    lines.append("Casi con il **minore rendimento minimo** (ret_low) nei giorni successivi (worst case).")
    lines.append("")
    if df_worst.empty:
        lines.append("Nessun dato.")
    else:
        lines.append(header)
        lines.append(sep)
        for _, r in df_worst.iterrows():
            lines.append("| " + " | ".join(_row_cells(r, cols_display)) + " |")
    if include_all:
        lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("## Tutti i casi (ordinati per rendimento massimo decrescente)")
        lines.append("")
        lines.append("Elenco completo di ogni cluster (ticker + data filing). Per dati estesi (TA, 52w, ecc.) usare **STRATEGY_AGENT_CASES.csv**.")
        lines.append("")
        lines.append(header)
        lines.append(sep)
        for _, r in df_all_sorted.iterrows():
            lines.append("| " + " | ".join(_row_cells(r, cols_display)) + " |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("**STRATEGY_AGENT_CASES.csv** = database completo: una riga per cluster, tutte le colonne. Per ogni orizzonte: ret/exit per open, news, news_bot, insider (exit_high_Nd_open_price, exit_high_Nd_news_price, exit_high_Nd_news_bot_price, exit_high_Nd_insider_price, ecc.); TA, market_cap, ecc.")
    report = "\n".join(lines)
    if out_path:
        out_path.write_text(report, encoding="utf-8")
    return report


def export_cases_keys_csv(df_results: pd.DataFrame, out_path: Path) -> None:
    """Esporta un CSV leggero con le colonne chiave per analisi rapide. Ordine logico: per orizzonte ret + exit + mean_price."""
    if df_results.empty:
        return
    key_cols = ["ticker", "filing_day", "filedAt", "entry_datetime", "entry_price", "entry_price_news", "entry_price_news_bot", "insider_entry_price"]
    for n in TRADING_DAY_HORIZONS:
        block = [
            f"ret_high_{n}d_open", f"ret_low_{n}d_open", f"ret_mean_{n}d_open",
            f"exit_high_{n}d_open_price", f"exit_low_{n}d_open_price", f"exit_mean_{n}d_open_price",
            f"mean_price_{n}d_open",
            f"ret_high_{n}d_news", f"ret_low_{n}d_news", f"ret_mean_{n}d_news",
            f"exit_high_{n}d_news_price", f"exit_low_{n}d_news_price", f"exit_mean_{n}d_news_price",
            f"mean_price_{n}d_news",
            f"ret_high_{n}d_news_bot", f"ret_low_{n}d_news_bot", f"ret_mean_{n}d_news_bot",
            f"exit_high_{n}d_news_bot_price", f"exit_low_{n}d_news_bot_price", f"exit_mean_{n}d_news_bot_price",
            f"mean_price_{n}d_news_bot",
            f"ret_high_{n}d_insider", f"ret_low_{n}d_insider", f"ret_mean_{n}d_insider",
            f"exit_high_{n}d_insider_price", f"exit_low_{n}d_insider_price", f"exit_mean_{n}d_insider_price",
            f"mean_price_{n}d_insider",
        ]
        key_cols.extend(c for c in block if c in df_results.columns)
    key_cols = [c for c in key_cols if c in df_results.columns]
    if not key_cols:
        return
    df_results[key_cols].to_csv(out_path, index=False, encoding="utf-8-sig", sep=";")


def export_cases_keys_long_csv(df_results: pd.DataFrame, out_path: Path) -> None:
    """
    Esporta un CSV in formato "long": 3 righe per combinazione (ticker, filing_day, horizon_days):
    kind ∈ {high, low, mean}, con ret ed exit price per open, news, news_bot, insider.
    Colonne: ticker, filing_day, filedAt, entry_datetime, entry_price, entry_price_news, entry_price_news_bot, insider_entry_price,
             kind, horizon_days, ret_open_%, ret_news_%, ret_news_bot_%, ret_insider_%, exit_open_price, exit_news_price, exit_news_bot_price, exit_insider_price.
    """
    if df_results.empty:
        return
    rows_out: list[dict] = []
    ret_high_cols = [
        c for c in df_results.columns
        if c.startswith("ret_high_") and c.endswith("d_open")
    ]
    horizons: list[int] = []
    for c in ret_high_cols:
        try:
            n = int(c.replace("ret_high_", "").replace("d_open", ""))
            horizons.append(n)
        except Exception:
            continue
    horizons = sorted(set(horizons))
    for _, r in df_results.iterrows():
        ticker = r.get("ticker")
        filing_day = r.get("filing_day") or r.get("filedAt")
        filed_at = r.get("filedAt")
        entry_dt = r.get("entry_datetime")
        entry_price = r.get("entry_price")
        entry_price_news = r.get("entry_price_news")
        entry_price_news_bot = r.get("entry_price_news_bot")
        insider_entry_price = r.get("insider_entry_price")
        for n in horizons:
            for kind in ("high", "low", "mean"):
                if kind == "high":
                    col_open, col_news = f"ret_high_{n}d_open", f"ret_high_{n}d_news"
                    col_news_bot, col_insider = f"ret_high_{n}d_news_bot", f"ret_high_{n}d_insider"
                    exit_open_col = f"exit_high_{n}d_open_price"
                    exit_news_col = f"exit_high_{n}d_news_price"
                    exit_news_bot_col = f"exit_high_{n}d_news_bot_price"
                    exit_insider_col = f"exit_high_{n}d_insider_price"
                elif kind == "low":
                    col_open, col_news = f"ret_low_{n}d_open", f"ret_low_{n}d_news"
                    col_news_bot, col_insider = f"ret_low_{n}d_news_bot", f"ret_low_{n}d_insider"
                    exit_open_col = f"exit_low_{n}d_open_price"
                    exit_news_col = f"exit_low_{n}d_news_price"
                    exit_news_bot_col = f"exit_low_{n}d_news_bot_price"
                    exit_insider_col = f"exit_low_{n}d_insider_price"
                else:
                    col_open, col_news = f"ret_mean_{n}d_open", f"ret_mean_{n}d_news"
                    col_news_bot, col_insider = f"ret_mean_{n}d_news_bot", f"ret_mean_{n}d_insider"
                    exit_open_col = exit_news_col = exit_news_bot_col = exit_insider_col = None
                if col_open not in df_results.columns and col_news not in df_results.columns:
                    continue
                row = {
                    "ticker": ticker,
                    "filing_day": filing_day,
                    "filedAt": filed_at,
                    "entry_datetime": entry_dt,
                    "entry_price": entry_price,
                    "entry_price_news": entry_price_news,
                    "entry_price_news_bot": entry_price_news_bot,
                    "insider_entry_price": insider_entry_price,
                    "kind": kind,
                    "horizon_days": n,
                    "ret_open_%": r.get(col_open),
                    "ret_news_%": r.get(col_news),
                    "ret_news_bot_%": r.get(col_news_bot) if col_news_bot in df_results.columns else None,
                    "ret_insider_%": r.get(col_insider) if col_insider in df_results.columns else None,
                }
                def _exit_or_mean(exit_col: str | None, mean_suffix: str):
                    if exit_col and exit_col in df_results.columns:
                        return r.get(exit_col)
                    if kind == "mean":
                        mc = f"mean_price_{n}d_{mean_suffix}"
                        if mc in df_results.columns:
                            return r.get(mc)
                    return None
                row["exit_open_price"] = _exit_or_mean(exit_open_col, "open")
                row["exit_news_price"] = _exit_or_mean(exit_news_col, "news")
                row["exit_news_bot_price"] = _exit_or_mean(exit_news_bot_col, "news_bot")
                row["exit_insider_price"] = _exit_or_mean(exit_insider_col, "insider")
                rows_out.append(row)
    if not rows_out:
        return
    long_cols = [
        "ticker", "filing_day", "filedAt", "entry_datetime", "entry_price", "entry_price_news", "entry_price_news_bot", "insider_entry_price",
        "kind", "horizon_days", "ret_open_%", "ret_news_%", "ret_news_bot_%", "ret_insider_%", "exit_open_price", "exit_news_price", "exit_news_bot_price", "exit_insider_price",
    ]
    df_long = pd.DataFrame(rows_out)
    df_long = df_long[[c for c in long_cols if c in df_long.columns]]
    df_long.to_csv(out_path, index=False, encoding="utf-8-sig", sep=";")


def _filter_quality_clusters(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """
    Applica un filtro di qualità ai cluster usati per l'analisi (report, TICKERS, 10k).

    - Rimuove righe con entry_price mancante o non numerico.
    - Rimuove righe con ret_high_30d_open mancante se la colonna esiste (usata spesso come hold key).
    - Segnala (ma non rimuove) ritorni estremi su 1 giorno se disponibili.
    """
    stats = {
        "total": len(df),
        "dropped_entry_missing": 0,
        "dropped_ret30_missing": 0,
        "extreme_1d": 0,
    }
    if df.empty:
        return df, stats
    mask = pd.Series(True, index=df.index)
    if "entry_price" in df.columns:
        bad_entry = df["entry_price"].isna()
        stats["dropped_entry_missing"] = int(bad_entry.sum())
        mask &= ~bad_entry
    if "ret_high_30d_open" in df.columns:
        bad_ret30 = df["ret_high_30d_open"].isna()
        stats["dropped_ret30_missing"] = int(bad_ret30.sum())
        mask &= ~bad_ret30
    # Stima variazioni estreme 1d (solo per statistiche)
    for col in ("ret_high_1d_open", "ret_low_1d_open"):
        if col in df.columns:
            extreme = df[col].abs() > 500
            stats["extreme_1d"] += int(extreme.sum())
    df_clean = df[mask].copy()
    return df_clean, stats


def _check_exit_price_consistency(df: pd.DataFrame) -> dict:
    """
    Controlla coerenza exit price = entry * (1 + ret/100) per alcune colonne chiave.
    Ritorna statistiche con numero di mismatch per colonna.
    """
    stats: dict[str, int] = {}
    if df.empty or "entry_price" not in df.columns:
        return stats
    for ret_col in [c for c in df.columns if c.startswith("ret_high_") and c.endswith("d_open")]:
        n = ret_col.replace("ret_high_", "").replace("d_open", "")
        exit_col = f"exit_high_{n}d_open_price"
        if exit_col not in df.columns:
            continue
        try:
            expected = df["entry_price"] * (1 + df[ret_col] / 100.0)
            diff = (df[exit_col] - expected).abs()
            mismatches = int((diff > expected.abs() * 1e-3 + 1e-4).sum())
            stats[exit_col] = mismatches
        except Exception:
            continue
    return stats


def build_tickers_report(
    df_results: pd.DataFrame,
    out_path: Path | None = None,
    out_path_csv: Path | None = None,
    ranking: list[dict] | None = None,
) -> str:
    """
    Report per ogni singolo ticker: riepilogo + dettaglio di ogni apparizione (data, quantità, ruolo, costo, aumento % posizione, ret).
    """
    if df_results.empty:
        report = "Nessun dato per il report ticker."
        if out_path:
            out_path.write_text(report, encoding="utf-8")
        return report
    df = df_results.copy()
    if "ticker" not in df.columns:
        report = "Colonna 'ticker' non presente."
        if out_path:
            out_path.write_text(report, encoding="utf-8")
        return report
    df["ticker"] = df["ticker"].astype(str).str.strip().str.upper()
    ret_high_col = "ret_high_30d_open" if "ret_high_30d_open" in df.columns else next((c for c in df.columns if c.startswith("ret_high_") and "open" in c), None)
    ret_low_col = "ret_low_30d_open" if "ret_low_30d_open" in df.columns else next((c for c in df.columns if c.startswith("ret_low_") and "open" in c), None)
    date_col = "filing_day" if "filing_day" in df.columns else ("filedAt" if "filedAt" in df.columns else None)
    if not date_col:
        report = "Colonna 'filing_day' o 'filedAt' non presente."
        if out_path:
            out_path.write_text(report, encoding="utf-8")
        return report
    agg_dict = {date_col: "count"}
    if ret_high_col:
        agg_dict[ret_high_col] = "mean"
    if ret_low_col and ret_low_col != ret_high_col:
        agg_dict[ret_low_col] = "mean"
    if "value_tot" in df.columns:
        agg_dict["value_tot"] = "sum"
    by_ticker = df.groupby("ticker", as_index=False).agg(agg_dict)
    by_ticker = by_ticker.rename(columns={date_col: "n_cluster"})
    # Mappa ticker -> strategie e cluster in cui appare (dal ranking, se fornito)
    strategies_by_ticker: dict[str, set[str]] = {}
    clusters_by_ticker: dict[str, set[str]] = {}
    if ranking:
        for row in ranking:
            tickers_used = (row.get("Tickers_used") or "").split(",") if row.get("Tickers_used") else []
            clusters_used = (row.get("Clusters_used") or "").split(",") if row.get("Clusters_used") else []
            strat_name = row.get("Strategia") or ""
            for t in tickers_used:
                t_clean = t.strip().upper()
                if not t_clean:
                    continue
                strategies_by_ticker.setdefault(t_clean, set()).add(strat_name)
            for c in clusters_used:
                if "|" not in c:
                    continue
                t_sym, key = c.split("|", 1)
                t_sym = t_sym.strip().upper()
                if not t_sym:
                    continue
                clusters_by_ticker.setdefault(t_sym, set()).add(key)
    if ret_high_col:
        by_ticker["ret_high_avg_%"] = by_ticker[ret_high_col].round(2)
    if ret_low_col:
        by_ticker["ret_low_avg_%"] = by_ticker[ret_low_col].round(2)
    by_ticker = by_ticker.sort_values("n_cluster", ascending=False).reset_index(drop=True)
    if out_path_csv:
        export_df = by_ticker.copy()
        export_df["uso_analisi"] = export_df["n_cluster"].astype(str) + " cluster nel backtest"
        export_df["strategies"] = export_df["ticker"].map(
            lambda t: ",".join(sorted(strategies_by_ticker.get(str(t).upper(), set()))) if strategies_by_ticker else ""
        )
        export_df["clusters_keys"] = export_df["ticker"].map(
            lambda t: ",".join(sorted(clusters_by_ticker.get(str(t).upper(), set()))) if clusters_by_ticker else ""
        )
        cols_out = [c for c in ["ticker", "n_cluster", "ret_high_avg_%", "ret_low_avg_%", "value_tot", "strategies", "clusters_keys", "uso_analisi"] if c in export_df.columns]
        export_df[[c for c in cols_out if c in export_df.columns]].to_csv(out_path_csv, index=False, encoding="utf-8-sig", sep=";")
    # Colonne ret per tutti gli orizzonti disponibili (1, 2, 3, 5, 7, 10, 14, 30 giorni di borsa)
    ret_high_cols = sorted(
        [c for c in df.columns if c.startswith("ret_high_") and "open" in c and c.endswith("d_open")],
        key=lambda x: int(x.replace("ret_high_", "").replace("d_open", "")),
    )
    ret_low_cols = sorted(
        [c for c in df.columns if c.startswith("ret_low_") and "open" in c and c.endswith("d_open")],
        key=lambda x: int(x.replace("ret_low_", "").replace("d_open", "")),
    )
    lines = []
    lines.append("# Report per ticker — Performance e uso nell'analisi")
    lines.append("")
    lines.append(f"Ticker distinti: **{len(by_ticker)}** | Totale cluster: **{int(by_ticker['n_cluster'].sum())}**")
    lines.append("")
    lines.append("Per ogni ticker: riepilogo (N cluster, ret medio, value tot) e **dettaglio di ogni apparizione**: data, quantità, ruolo, costo, aumento % posizione, **ret % per orizzonte** (1d, 2d, 3d, 5d, 7d, 10d, 14d, 30d, 60d, 90d giorni di borsa).")
    lines.append("")
    lines.append("**H Nd %** = Ret high (miglior rendimento % in N giorni borsa dall'entry). **L Nd %** = Ret low (peggior rendimento % in N giorni). **Exit price (30d high/low)** = prezzo di uscita al massimo/minimo nell'orizzonte 30 giorni. Entry = prezzo open a mercato aperto.")
    lines.append("")
    # Indice dei ticker (prime N voci per navigazione rapida)
    max_index_entries = 100
    lines.append("## Indice ticker")
    lines.append("")
    lines.append("Elenco rapido dei primi ticker nel report (clicca per saltare alla sezione):")
    lines.append("")
    for i, (_, sum_row) in enumerate(by_ticker.iterrows()):
        if i >= max_index_entries:
            lines.append(f"- … (+{len(by_ticker) - max_index_entries} ticker)")
            break
        t = str(sum_row["ticker"])
        anchor = t.lower()
        lines.append(f"- [{t}](#{anchor})")
    lines.append("")
    for _, sum_row in by_ticker.iterrows():
        ticker = sum_row["ticker"]
        n_cluster = int(sum_row["n_cluster"])
        rh_avg = sum_row.get("ret_high_avg_%", sum_row.get(ret_high_col, ""))
        rl_avg = sum_row.get("ret_low_avg_%", sum_row.get(ret_low_col, ""))
        vt_sum = sum_row.get("value_tot", "")
        if isinstance(vt_sum, (int, float)) and not pd.isna(vt_sum):
            vt_sum = f"{vt_sum:,.0f}"
        lines.append("---")
        lines.append("")
        lines.append(f"## {ticker}")
        lines.append("")
        strat_list = ", ".join(sorted(strategies_by_ticker.get(str(ticker).upper(), set()))) if strategies_by_ticker else ""
        cluster_keys = ", ".join(sorted(clusters_by_ticker.get(str(ticker).upper(), set()))) if clusters_by_ticker else ""
        lines.append(f"**Riepilogo:** N cluster: **{n_cluster}** | Ret high avg %: **{_fmt(rh_avg)}** | Ret low avg %: **{_fmt(rl_avg)}** | Value tot: **{vt_sum}** USD")
        if strat_list:
            lines.append("")
            lines.append(f"**Strategie in cui compare:** {strat_list}")
        if cluster_keys:
            lines.append("")
            lines.append(f"**Cluster (ticker|filing_day) usati nelle strategie:** {cluster_keys}")
        lines.append("")
        sub = df[df["ticker"] == ticker].sort_values("filing_day" if "filing_day" in df.columns else ("filedAt" if "filedAt" in df.columns else df.columns[0]), ascending=False)
        headers = ["Data e ora filing (" + REPORT_DATETIME_TZ + ")", "Entry (data e ora " + REPORT_DATETIME_TZ + ")", "Quantità", "Ruolo", "Costo USD", "Aumento % pos."]
        if "datetime_high_30d" in df.columns:
            headers.extend(["Data/ora max 30d (" + REPORT_DATETIME_TZ + ")", "Data/ora min 30d (" + REPORT_DATETIME_TZ + ")"])
        if "exit_high_30d_open_price" in df.columns:
            headers.extend(["Exit price (30d high)", "Exit price (30d low)"])
        for c in ret_high_cols:
            n = c.replace("ret_high_", "").replace("d_open", "")
            headers.append(f"H{n}d %")
        for c in ret_low_cols:
            n = c.replace("ret_low_", "").replace("d_open", "")
            headers.append(f"L{n}d %")
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("|" + "|".join(["---"] * len(headers)) + "|")
        for _, r in sub.iterrows():
            data_filing = str(r.get("filedAt", "") or r.get("filing_day", "") or "")[:_DATETIME_DISPLAY_LEN]
            entry_dt = str(r.get("entry_datetime", "") or r.get("entry_date", "") or "")[:_DATETIME_DISPLAY_LEN]
            qty = _fmt(r.get("qty_tot"), 0) if "qty_tot" in r else ""
            ruolo = (str(r.get("titles", "")) or "")[:50] + ("…" if len(str(r.get("titles", ""))) > 50 else "")
            costo = r.get("value_tot")
            if isinstance(costo, (int, float)) and not pd.isna(costo):
                costo = f"{costo:,.0f}"
            else:
                costo = ""
            aumento = r.get("pct_increase_position_max")
            if isinstance(aumento, (int, float)) and not pd.isna(aumento):
                aumento = f"{float(aumento) * 100:.2f}%" if abs(aumento) < 1 else f"{aumento:.2f}%"
            else:
                aumento = ""
            row_cells = [data_filing, entry_dt, qty, ruolo, costo, aumento]
            if "datetime_high_30d" in df.columns:
                row_cells.append((_fmt(r.get("datetime_high_30d")) or "")[:_DATETIME_DISPLAY_LEN])
                row_cells.append((_fmt(r.get("datetime_low_30d")) or "")[:_DATETIME_DISPLAY_LEN])
            if "exit_high_30d_open_price" in df.columns:
                row_cells.append(_fmt(r.get("exit_high_30d_open_price")))
                row_cells.append(_fmt(r.get("exit_low_30d_open_price")))
            for c in ret_high_cols:
                row_cells.append(_fmt(r.get(c)))
            for c in ret_low_cols:
                row_cells.append(_fmt(r.get(c)))
            lines.append("| " + " | ".join(row_cells) + " |")
        lines.append("")
    report = "\n".join(lines)
    if out_path:
        out_path.write_text(report, encoding="utf-8")
    return report


def _run_10k_window(
    df: pd.DataFrame,
    sd: StrategyDef,
    top_hold: str,
    ref_date_start: str,
    ref_date_end: str,
    budget_usd: float,
    max_positions: int,
    allocation_mode: str = "all_in",
) -> tuple[float, float, list[dict], int, str]:
    """
    Esegue una singola simulazione 10k su una finestra [ref_date_start, ref_date_end].
    allocation_mode: "all_in" = tutto il capitale su ogni trade in sequenza (compounding);
    "equal_weight" = budget diviso in parti uguali tra le N posizioni (nessun compounding).
    Ritorna (ret_pct_totale, pnl_totale, rows_out, n_pos, allocation_mode).
    """
    date_col = "filing_day" if "filing_day" in df.columns else ("filedAt" if "filedAt" in df.columns else None)
    if not date_col or top_hold not in df.columns:
        return 0.0, 0.0, [], 0, allocation_mode
    mask = df[date_col].astype(str).str[:10] >= ref_date_start
    mask &= df[date_col].astype(str).str[:10] <= ref_date_end
    w = df.loc[mask].copy()
    w = w[w.apply(lambda r: sd.filter_fn(r.to_dict()), axis=1)]
    if top_hold not in w.columns:
        return 0.0, 0.0, [], 0, allocation_mode
    w = w.dropna(subset=[top_hold]).copy()
    if w.empty:
        return 0.0, 0.0, [], 0, allocation_mode
    w[date_col] = w[date_col].astype(str).str[:10]
    w = w.sort_values(date_col, ascending=True).reset_index(drop=True)
    horizon_days = None
    if "ret_high_" in top_hold and "d_" in top_hold:
        try:
            part = top_hold.split("ret_high_")[1].split("d_")[0]
            horizon_days = int(part)
        except Exception:
            horizon_days = None
    # Raccogliamo le stesse N trade in ordine cronologico (stessa logica free_after)
    trades_list: list[dict] = []  # [{r, entry, ret_pct, filing_day, sell_date_str, sell_dt, ...}]
    current_free_after: str | None = None
    for _, r in w.iterrows():
        filing_day = str(r.get("filing_day") or r.get(date_col) or "")[:10]
        if not filing_day:
            continue
        if current_free_after and filing_day <= current_free_after:
            continue
        entry = r.get("entry_price") or 0
        try:
            entry = float(entry)
        except Exception:
            entry = 0.0
        if not entry or entry <= 0:
            continue
        ret_raw = r.get(top_hold)
        try:
            ret_pct = float(ret_raw if ret_raw is not None else 0.0)
        except Exception:
            ret_pct = 0.0
        sell_date = r.get(f"date_high_{horizon_days}d") if horizon_days else None
        sell_dt = r.get(f"datetime_high_{horizon_days}d") if horizon_days else None
        sell_date_str = str(sell_date or "")[:10]
        effective_sell_day = sell_date_str or filing_day
        current_free_after = effective_sell_day
        trades_list.append({"r": r, "entry": entry, "ret_pct": ret_pct, "filing_day": filing_day, "sell_date_str": sell_date_str, "sell_dt": sell_dt})
        if max_positions and max_positions > 0 and len(trades_list) >= max_positions:
            break
    n_pos = len(trades_list)
    if n_pos == 0:
        return 0.0, 0.0, [], 0, allocation_mode

    def _one_row(t: dict, allocation_amt: float, pnl_amt: float, sell_price_val: float) -> dict:
        r, entry, ret_pct = t["r"], t["entry"], t["ret_pct"]
        return {
            "ticker": r.get("ticker", ""),
            "filing_day": t["filing_day"],
            "filedAt": str(r.get("filedAt", ""))[:_DATETIME_DISPLAY_LEN],
            "entry_datetime": str(r.get("entry_datetime", "") or r.get("entry_date", ""))[:_DATETIME_DISPLAY_LEN],
            "sell_date": t["sell_date_str"],
            "sell_datetime": str(t["sell_dt"] or "")[:_DATETIME_DISPLAY_LEN],
            "entry_price": round(entry, 2),
            "allocation_usd": round(allocation_amt, 2),
            "shares": round(allocation_amt / entry, 2) if entry and entry > 0 else 0,
            "ret_%": round(ret_pct, 2),
            "pnl_usd": round(pnl_amt, 2),
            "sell_price": sell_price_val,
            "exit_price": sell_price_val,
            "window": f"{ref_date_start} / {ref_date_end}",
        }

    rows_out: list[dict] = []
    if allocation_mode == "equal_weight":
        allocation_per = budget_usd / n_pos
        total_pnl = 0.0
        for t in trades_list:
            r, entry, ret_pct = t["r"], t["entry"], t["ret_pct"]
            pnl = allocation_per * ret_pct / 100.0
            total_pnl += pnl
            sell_price = round(entry * (1 + ret_pct / 100.0), 2)
            rows_out.append(_one_row(t, allocation_per, pnl, sell_price))
        total_ret_pct = (total_pnl / budget_usd * 100.0) if budget_usd else 0.0
        return total_ret_pct, total_pnl, rows_out, n_pos, allocation_mode
    # all_in: capitale tutto su ogni trade in sequenza (compounding)
    capital = budget_usd
    for t in trades_list:
        r, entry, ret_pct = t["r"], t["entry"], t["ret_pct"]
        allocation = capital
        pnl = allocation * ret_pct / 100.0
        capital = allocation + pnl
        sell_price = round(entry * (1 + ret_pct / 100.0), 2)
        rows_out.append(_one_row(t, allocation, pnl, sell_price))
    total_pnl = capital - budget_usd
    total_ret_pct = (capital / budget_usd * 100.0 - 100.0) if budget_usd else 0.0
    return total_ret_pct, total_pnl, rows_out, n_pos, "all_in"


def build_10k_strategy(
    df_results: pd.DataFrame,
    ranking: list[dict],
    out_path: Path | None = None,
    out_path_csv: Path | None = None,
    budget_usd: float = STRATEGY_10K_BUDGET,
    lookback_days: int = STRATEGY_10K_LOOKBACK_DAYS,
    max_positions: int = STRATEGY_10K_MAX_POSITIONS,
    top_strategies_k: int = 10,
    prefer_allocation: str = "auto",
    min_strategy_n: int = 0,
) -> tuple[str, list[dict]]:
    """
    Strategia 10k USD: tre simulazioni (oggi-3y, -2y, -1y) su finestra anno successivo.
    Per ogni finestra si testano le prime top_strategies_k strategie del ranking e si confrontano
    i rendimenti per capire quale sarebbe stata più conveniente (anche comprare/vendere più volte).
    Ritorna (report_md, lista posizioni della finestra «1 anno fa» per export CSV).
    """
    empty_positions: list[dict] = []
    if df_results.empty:
        report = "Nessun dato per la strategia 10k."
        if out_path:
            out_path.write_text(report, encoding="utf-8")
        return report, empty_positions
    if not ranking:
        report = "Nessun ranking strategie disponibile."
        if out_path:
            out_path.write_text(report, encoding="utf-8")
        return report, empty_positions
    df = df_results.copy()
    if "filing_day" not in df.columns:
        report = "Colonna filing_day non presente."
        if out_path:
            out_path.write_text(report, encoding="utf-8")
        return report, empty_positions
    today = date.today()
    # Tre date di inizio: oggi-3y, oggi-2y, oggi-1y; per ognuna finestra di 365 giorni
    refs = [
        (today - timedelta(days=3 * 365), "3 anni fa (anno successivo)"),
        (today - timedelta(days=2 * 365), "2 anni fa (anno successivo)"),
        (today - timedelta(days=1 * 365), "1 anno fa (anno successivo)"),
    ]
    if min_strategy_n and min_strategy_n > 0:
        ranking_filtered = [
            r
            for r in ranking
            if int(r.get("N") or 0) >= min_strategy_n
        ]
    else:
        ranking_filtered = ranking
    strategies_to_test = ranking_filtered[: min(top_strategies_k, len(ranking_filtered))]
    window_results = []
    for ref_date, label in refs:
        start_s = ref_date.isoformat()
        end_date = ref_date + timedelta(days=lookback_days)
        end_s = end_date.isoformat()
        per_strategy = []
        for r in strategies_to_test:
            sname_full = r.get("Strategia", "")
            base_name = _strategy_name_base(sname_full)
            hold_key = r.get("Hold", "")
            if isinstance(hold_key, list):
                hold_key = hold_key[0] if hold_key else ""
            elif not isinstance(hold_key, str):
                hold_key = str(hold_key) if hold_key else ""
            if not hold_key or hold_key not in df.columns:
                continue
            # Per il filtro usiamo la strategia unificata (base) corrispondente.
            sd = next((s for s in STRATEGY_DEFINITIONS_UNIFIED if s.name == base_name), None)
            if sd is None:
                continue
            # Prova entrambe le allocazioni; per default usa quella con rendimento % migliore,
            # ma se prefer_allocation è impostato forziamo la modalità scelta.
            ret_a, pnl_a, rows_a, n_a, _ = _run_10k_window(
                df, sd, hold_key, start_s, end_s, budget_usd, max_positions, "all_in"
            )
            ret_e, pnl_e, rows_e, n_e, _ = _run_10k_window(
                df, sd, hold_key, start_s, end_s, budget_usd, max_positions, "equal_weight"
            )
            alloc_mode = "all_in"
            ret_chosen, pnl_chosen, rows_chosen, n_chosen = ret_a, pnl_a, rows_a, n_a
            if prefer_allocation == "equal_weight":
                alloc_mode = "equal_weight"
                ret_chosen, pnl_chosen, rows_chosen, n_chosen = ret_e, pnl_e, rows_e, n_e
            elif prefer_allocation == "auto":
                if ret_e > ret_a:
                    alloc_mode = "equal_weight"
                    ret_chosen, pnl_chosen, rows_chosen, n_chosen = ret_e, pnl_e, rows_e, n_e
            # Se prefer_allocation == "all_in" lasciamo alloc_mode e risultati dell'all-in
            per_strategy.append((sname_full, ret_chosen, pnl_chosen, n_chosen, rows_chosen, alloc_mode))
        window_results.append((label, start_s, end_s, per_strategy))
    # Per CSV esportiamo le posizioni della simulazione "1 anno fa" (la più recente)
    rows_1y = []
    if len(window_results) >= 3 and window_results[2][3]:
        best = max(window_results[2][3], key=lambda x: x[1])
        rows_1y = best[4]  # rows
    elif window_results and window_results[-1][3]:
        best = max(window_results[-1][3], key=lambda x: x[1])
        rows_1y = best[4]
    # Rimuovi chiave "window" dalle righe per il CSV se vogliamo formato come prima
    rows_out = [{k: v for k, v in row.items() if k != "window"} for row in rows_1y]
    # Assicura che exit_price sia sempre presente (alias di sell_price); entry_price è già nelle row
    for row in rows_out:
        if "exit_price" not in row and "sell_price" in row:
            row["exit_price"] = row["sell_price"]
    lines = []
    lines.append("# Strategia 10k USD — Confronto strategie su tre finestre (1 anno ciascuna)")
    lines.append("")
    lines.append("**Timezone:** Tutti gli orari nei report (data/ora filing, entry, uscita) sono in **" + REPORT_DATETIME_TZ + "**.")
    lines.append("")
    lines.append("Per ogni finestra (3 anni fa, 2 anni fa, 1 anno fa) sono state testate le prime **" + str(top_strategies_k) + "** strategie del ranking. La sezione **Simulazione per i prossimi 365 giorni** indica quale strategia e allocazione seguire **da oggi per i prossimi 365 giorni** per puntare al massimo rendimento (basata sull’analisi della finestra più recente).")
    lines.append("")
    lines.append("**Strategia sul futuro (cluster e importi):** il file con suffisso **_10K.csv** contiene i **cluster consigliati** (ticker, filing_day, **entry_price**, **exit_price**, allocation_usd, ret %, pnl_usd) della strategia vincente sulla finestra più recente. Per i prossimi 365 giorni puoi **acquistare più stock alla volta** applicando gli stessi criteri ai nuovi Form 4, con **importi uguali** (parti uguali) o **diversi** (es. in proporzione al valore del filing o al rendimento atteso); la colonna allocation_usd indica l'importo suggerito per ogni cluster.")
    lines.append("")
    lines.append("**Come applicarla da oggi in pratica:**")
    lines.append("")
    lines.append("- Prendi dal report qui sotto la **strategia raccomandata per la finestra più recente** (filtro, Hold, modalità allocazione).")
    lines.append("- Usa lo **stesso filtro** sui nuovi Form 4 (es. solo CEO/CFO, solo Value ≥100k, solo Small cap, ecc.).")
    lines.append("- Usa lo **stesso orizzonte Hold** (es. ret_high_30d_open ⇒ tieni fino al massimo a 30 giorni borsa dall’entry).")
    lines.append("- Usa la **stessa modalità di allocazione** scelta (all-in sequenziale o parti uguali).")
    lines.append("- Ogni volta che arriva un nuovo filing che soddisfa il filtro, lo aggiungi alla lista dei trade da fare, replicando la logica storica per i prossimi 365 giorni.")
    lines.append("")
    max_pos_str = "tutte (nessun limite)" if not max_positions or max_positions <= 0 else str(max_positions)
    lines.append(f"Budget: **${budget_usd:,.0f}** | Max posizioni: **{max_pos_str}** | Giorni/finestra: **{lookback_days}**")
    lines.append("")
    lines.append("## Come funziona (logica)")
    lines.append("")
    lines.append("- Per ogni **finestra** si considera l’intervallo di date **filing_day** (data del Form 4 SEC) da *data inizio* a *data fine* (1 anno).")
    lines.append("- Per ogni **strategia** si filtrano i cluster (ticker + data filing) che rispettano i criteri (ruolo, % posizione, valore, **market cap**, ecc.). Per il **market cap** si testano **bande dettagliate**: Micro cap (≤50M, ≤100M, ≤250M), Small cap (≤1B), Mid cap (1B–10B), Large cap con soglie ≥250M, ≥500M, ≥750M, ≥1B, ≥2B, ≥3B, ≥5B, ≥10B, ≥20B, ≥50B, ≥100B; la **migliore** emerge dal backtest/ranking. Si ordinano per rendimento nell'orizzonte scelto (es. ret_high_30d_open) in ordine decrescente; si possono prendere tutte le posizioni disponibili (oppure, se configurato, un massimo predefinito). **Allocazione:** per ogni (finestra, strategia) si testano due modalità e si usa quella con rendimento storico migliore: **(1) all-in sequenziale** — tutto il capitale su un trade alla volta, quando chiude si reinveste sul successivo; **(2) parti uguali** — budget diviso in N parti uguali (una per posizione), nessun compounding. Il **risultato** mostrato è il migliore tra le due.")
    lines.append("- (Nella tabella sotto, per ogni strategia è indicata l'allocazione usata: all-in sequenziale o parti uguali.) nell’orizzonte scelto (es. ret_high_30d_open) in ordine decrescente; si possono prendere tutte le posizioni disponibili (oppure, se configurato, un massimo predefinito).")
    lines.append("- Se una finestra mostra **0 posizioni** e 0%: in quel periodo non ci sono filing nel database che rispettano i criteri di nessuna strategia testata. Possibili cause: i dati SEC del backtest non coprono quel periodo (es. API con pochi risultati storici) oppure in quel periodo non ci sono acquisti che soddisfano i filtri (ruolo CEO/CFO, % posizione, market cap, ecc.).")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Migliore strategia per finestra")
    lines.append("")
    for label, start_s, end_s, per_strategy in window_results:
        if not per_strategy:
            lines.append(f"**{label}** ({start_s} → {end_s}): nessun dato.")
            continue
        best = max(per_strategy, key=lambda x: x[1])
        sname, ret_pct, pnl, n_pos, rows, alloc_mode = best
        entry_prices = [r.get("entry_price") for r in rows if r.get("entry_price") is not None]
        exit_prices = [r.get("sell_price") for r in rows if r.get("sell_price") is not None]
        entry_avg = f"${sum(entry_prices) / len(entry_prices):,.2f}" if entry_prices else "—"
        exit_avg = f"${sum(exit_prices) / len(exit_prices):,.2f}" if exit_prices else "—"
        alloc_label = "all-in sequenziale" if alloc_mode == "all_in" else "parti uguali (budget/N)"
        lines.append(f"- **{label}**: **{sname}** → **{ret_pct:.2f}%** | P&L ${pnl:,.2f} | {n_pos} pos. | Allocazione: **{alloc_label}** | Entry price (media) {entry_avg} | Exit price (media) {exit_avg}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Confronto (tutte le strategie testate per finestra)")
    lines.append("")
    lines.append("| Finestra | Strategia | Rend.% | P&L USD | N pos | Allocazione | Entry price (media) | Exit price (media) |")
    lines.append("|----------|-----------|--------|--------|------|--------------|----------------------|---------------------|")
    for label, start_s, end_s, per_strategy in window_results:
        short = label.split(" ")[0] + " " + label.split(" ")[1]
        for sname, ret_pct, pnl, n_pos, rows, alloc_mode in sorted(per_strategy, key=lambda x: -x[1]):
            sn = (sname[:45] + "…") if len(sname) > 45 else sname
            entry_prices = [r.get("entry_price") for r in rows if r.get("entry_price") is not None]
            exit_prices = [r.get("sell_price") for r in rows if r.get("sell_price") is not None]
            entry_avg = f"${sum(entry_prices) / len(entry_prices):,.2f}" if entry_prices else "—"
            exit_avg = f"${sum(exit_prices) / len(exit_prices):,.2f}" if exit_prices else "—"
            alloc_label = "all-in" if alloc_mode == "all_in" else "parti uguali"
            lines.append(f"| {short} | {sn} | {ret_pct:.2f} | ${pnl:,.2f} | {n_pos} | {alloc_label} | {entry_avg} | {exit_avg} |")
    best_abs = None
    best_abs_label = None
    for (label, _s, _e, per_strategy) in window_results:
        for t in per_strategy:
            if best_abs is None or t[1] > best_abs[1]:
                best_abs = t
                best_abs_label = label
    if best_abs:
        a = "all-in sequenziale" if best_abs[5] == "all_in" else "parti uguali"
        lines.append("")
        lines.append(f"**Miglior risultato assoluto:** {best_abs[0]} → **{best_abs[1]:.2f}%** (P&L ${best_abs[2]:,.2f}, allocazione: {a}).")
    # Analisi out-of-sample 2y train / 1y test (se abbiamo almeno 3 finestre)
    oos_summary: str | None = None
    oos_row: tuple[str, float, float, float] | None = None
    if len(window_results) >= 3:
        train_labels = {window_results[0][0], window_results[1][0]}
        test_label = window_results[2][0]
        train_perfs: dict[str, list[float]] = {}
        for label, _s, _e, per_strategy in window_results:
            if label not in train_labels:
                continue
            for sname, ret_pct, _pnl, _n_pos, _rows, _alloc in per_strategy:
                train_perfs.setdefault(sname, []).append(ret_pct)
        best_train_name = None
        best_train_avg = None
        for sname, rets in train_perfs.items():
            if not rets:
                continue
            avg_ret = sum(rets) / len(rets)
            if best_train_avg is None or avg_ret > best_train_avg:
                best_train_avg = avg_ret
                best_train_name = sname
        if best_train_name is not None and best_train_avg is not None:
            test_ret = None
            test_pnl = None
            for label, _s, _e, per_strategy in window_results:
                if label != test_label:
                    continue
                for sname, ret_pct, pnl, _n_pos, _rows, _alloc in per_strategy:
                    if sname == best_train_name:
                        test_ret = ret_pct
                        test_pnl = pnl
                        break
            if test_ret is not None and test_pnl is not None:
                oos_summary = f"Strategia selezionata sui 2 anni di train: **{best_train_name}** (avg train {best_train_avg:.2f}%). Su finestra test {test_label} → **{test_ret:.2f}%** (P&L ${test_pnl:,.2f})."
                oos_row = (best_train_name, best_train_avg, test_ret, test_pnl)
    # Simulazione per i prossimi 365 giorni: raccomandazione per massimizzare il rendimento da oggi
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Simulazione per i prossimi 365 giorni — strategia reale fondata sui dati (date, esempi, massimo nel passato)")
    lines.append("")
    future_label, future_start, future_end, future_per = window_results[-1] if window_results else (None, None, None, [])
    if best_abs is not None and best_abs_label is not None:
        sname_f, ret_f, pnl_f, n_pos_f, rows_f, alloc_f = best_abs

        # Calcola stabilità della strategia raccomandata sulle finestre disponibili
        stability_total = 0
        stability_positive = 0
        stability_rows: list[tuple[str, float, float]] = []
        for label, _s, _e, per_strategy in window_results:
            entry = next((t for t in per_strategy if t[0] == sname_f), None)
            if entry:
                stability_total += 1
                if entry[1] > 0:
                    stability_positive += 1
                stability_rows.append((label, entry[1], entry[2]))

        # Descrizione dettagliata filtro market cap per la strategia raccomandata
        mc_desc = _market_cap_description_from_strategy_name(sname_f)

        # Confronto allocazione all-in vs parti uguali per la finestra della raccomandazione
        alloc_compare: dict[str, tuple[float, float, int]] | None = None
        try:
            best_rank = next((r for r in ranking if r.get("Strategia") == sname_f), None)
            hold_key_best = best_rank.get("Hold", "") if best_rank else ""
            if isinstance(hold_key_best, list):
                hold_key_best = hold_key_best[0] if hold_key_best else ""
            elif not isinstance(hold_key_best, str):
                hold_key_best = str(hold_key_best) if hold_key_best else ""
            sd_best = next((s for s in STRATEGY_DEFINITIONS_UNIFIED if s.name == sname_f), None)
            start_best, end_best = None, None
            for label, s_s, e_s, per_strategy in window_results:
                if label == best_abs_label:
                    start_best, end_best = s_s, e_s
                    break
            if sd_best is not None and hold_key_best and start_best and end_best:
                ret_a_c, pnl_a_c, rows_a_c, n_a_c, _ = _run_10k_window(
                    df, sd_best, hold_key_best, start_best, end_best, budget_usd, max_positions, "all_in"
                )
                ret_e_c, pnl_e_c, rows_e_c, n_e_c, _ = _run_10k_window(
                    df, sd_best, hold_key_best, start_best, end_best, budget_usd, max_positions, "equal_weight"
                )
                alloc_compare = {
                    "all_in": (ret_a_c, pnl_a_c, n_a_c),
                    "equal_weight": (ret_e_c, pnl_e_c, n_e_c),
                }
        except Exception:
            alloc_compare = None

        alloc_future = "all-in sequenziale" if alloc_f == "all_in" else "parti uguali (budget ÷ N posizioni)"
        lines.append("L’analisi usa la **finestra più recente** (" + (best_abs_label or "") + "). La strategia e fondata su **dati reali** (date, ticker, P&L) dettagliati sotto. **Prossimi 365 giorni**: le strategie sono state testate su un anno di filing passati e la migliore in quel periodo è raccomandata per il periodo da oggi ai prossimi 365 giorni. Obiettivo: **massimizzare il rendimento** con la strategia e l’allocazione che nel backtest hanno ottenuto il risultato più alto nella finestra più vicina a oggi.")
    lines.append("")
    if best_abs is not None and best_abs_label is not None:
        lines.append("### Raccomandazione per i prossimi 365 giorni (dati reali)")
        lines.append("")
        lines.append("| Elemento | Valore |")
        lines.append("|----------|--------|")
        lines.append("| **Strategia da seguire** | " + sname_f + " |")
        lines.append("| **Allocazione** | " + alloc_future + " |")
        lines.append("| **Rendimento (backtest, dati reali)** | " + f"{ret_f:.2f}%" + " |")
        lines.append("| **P&L (backtest, dati reali)** | " + f"${pnl_f:,.2f}" + " |")
        lines.append("| **N. posizioni** | " + str(n_pos_f) + " |")
        lines.append("| **Finestra in cui e stato ottenuto (date reali)** | " + best_abs_label + " |")
        if 'stability_total' in locals() and stability_total:
            lines.append("| **Stabilità finestre** | " + f"{stability_positive}/{stability_total} finestre in utile" + " |")
        lines.append("| **Filtro market cap** | " + mc_desc + " |")
        lines.append("")
        if 'stability_rows' in locals() and stability_rows:
            lines.append("**Rendimento per finestra (stessa strategia):**")
            lines.append("")
            lines.append("| Finestra | Rend.% | P&L USD |")
            lines.append("|----------|--------|---------|")
            for label, r_pct, pnl_win in stability_rows:
                lines.append(f"| {label} | {r_pct:.2f} | ${pnl_win:,.2f} |")
            lines.append("")
        if 'alloc_compare' in locals() and alloc_compare:
            lines.append("**Confronto allocazione per la strategia raccomandata (finestra " + best_abs_label + "):**")
            lines.append("")
            lines.append("| Allocazione | Rend.% | P&L USD | N pos |")
            lines.append("|------------|--------|---------|-------|")
            for mode, (ret_c, pnl_c, n_c) in alloc_compare.items():
                label_mode = "all-in sequenziale" if mode == "all_in" else "parti uguali (budget ÷ N)"
                lines.append(f"| {label_mode} | {ret_c:.2f} | ${pnl_c:,.2f} | {n_c} |")
        if oos_summary:
            lines.append("")
            lines.append("### Out-of-sample (2 anni train / 1 anno test)")
            lines.append("")
            lines.append(oos_summary)
        lines.append("**Come applicarla da oggi:** filtrare i cluster SEC (Form 4 P) che rispettano i criteri della strategia sopra; ordinare per data di filing (cronologico); selezionare le posizioni (fino al massimo configurato); allocare il budget secondo la modalità indicata (all-in su un trade alla volta oppure parti uguali). Uscita: al prezzo massimo raggiunto nell’orizzonte della strategia (es. ret_high_7d → hold fino al massimo a 7 giorni). Posizioni reali: vedi Dettaglio per finestra -> " + best_abs_label + ". Stessa logica per i prossimi 365 giorni.")
    else:
        lines.append("Nessun dato in nessuna finestra: non e possibile raccomandare una strategia. Eseguire di nuovo il backtest quando saranno disponibili filing.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Dettaglio per finestra: strategia usata e posizioni (ticker, entry, P&L)")
    lines.append("")
    for label, start_s, end_s, per_strategy in window_results:
        short = label.split(" ")[0] + " " + label.split(" ")[1]
        lines.append("### Finestra: " + label)
        lines.append("")
        lines.append(f"**Intervallo date (filing_day):** da **{start_s}** a **{end_s}** (365 giorni).")
        lines.append("")
        if not per_strategy:
            lines.append("In questa finestra non ci sono cluster (filing SEC) con data in questo intervallo che rispettino i criteri delle strategie testate. Possibili cause: i dati del backtest non coprono quel periodo (es. SEC API con pochi risultati storici) oppure in quel periodo non ci sono acquisti che soddisfano i filtri (ruolo CEO/CFO, % posizione, ecc.).")
            lines.append("")
            lines.append("---")
            lines.append("")
            continue
        best = max(per_strategy, key=lambda x: x[1])
        sname, ret_pct, pnl, n_pos, rows, alloc_mode = best
        alloc_label = "all-in sequenziale (tutto il capitale su ogni trade, reinvestimento al chiudere)" if alloc_mode == "all_in" else "parti uguali (budget ÷ N posizioni, nessun compounding)"
        lines.append("**Strategia migliore:** " + sname)
        lines.append("")
        lines.append("**Allocazione usata (migliore nel backtest):** " + alloc_label + ".")
        lines.append("")
        if n_pos and n_pos > 0:
            lines.append("**Risultato:** " + f"Rendimento **{ret_pct:.2f}%** | P&L **${pnl:,.2f}** | **{n_pos}** posizioni (budget ${budget_usd:,.0f} ÷ {n_pos} = **${budget_usd / n_pos:,.0f}** per titolo).")
        else:
            lines.append("**Risultato:** " + f"Rendimento **{ret_pct:.2f}%** | P&L **${pnl:,.2f}** | **0** posizioni (nessun cluster nella finestra che rispetti i criteri).")
        lines.append("")
        lines.append("**Come si arriva al risultato:** si selezionano i cluster con data di filing nell’intervallo sopra che rispettano i criteri della strategia; si ordinano **cronologicamente** per data filing crescente; si prendono tutte le posizioni disponibili (o si può configurare un massimo); si investe **tutto il capitale disponibile** su ogni trade (una posizione alla volta); quando un trade chiude (data di uscita = massimo nell'orizzonte), il capitale (incluso profitto) viene reinvestito nel trade successivo. Tabella sotto: ticker, data filing, entry/uscita, allocazione USD, n. azioni, ret % (nell’orizzonte), P&L USD.")
        lines.append("")
        if not rows:
            lines.append("Nessuna posizione in questa finestra.")
        else:
            lines.append("| Ticker | Data filing | Entry (data/ora " + REPORT_DATETIME_TZ + ") | Uscita (data/ora, peak " + REPORT_DATETIME_TZ + ") | Allocation USD | N. azioni | Prezzo entry | Prezzo uscita | Ret % | P&L USD |")
            lines.append("|--------|-------------|-------------------------------|----------------------------------|----------------|-----------|--------------|----------------|-------|--------|")
            for row in rows:
                cells = [
                    str(row.get("ticker", "")),
                    str(row.get("filing_day", "")),
                    str(row.get("entry_datetime", "")),
                    str(row.get("sell_datetime", "")),
                    str(row.get("allocation_usd", "")),
                    str(row.get("shares", "")),
                    str(row.get("entry_price", "")),
                    str(row.get("sell_price", "")),
                    str(row.get("ret_%", "")),
                    str(row.get("pnl_usd", "")),
                ]
                lines.append("| " + " | ".join(cells) + " |")
        lines.append("")
        lines.append("---")
        lines.append("")
    report = "\n".join(lines)
    if out_path:
        out_path.write_text(report, encoding="utf-8")
    if out_path_csv and rows_out:
        pd.DataFrame(rows_out).to_csv(out_path_csv, index=False, encoding="utf-8-sig", sep=";")
    return report, rows_out


def build_report(
    df_results: pd.DataFrame,
    ranking: list[dict],
    errors: list[dict],
    out_path: Path | None = None,
    strategy_10k_budget: float = STRATEGY_10K_BUDGET,
    strategy_10k_lookback_days: int = STRATEGY_10K_LOOKBACK_DAYS,
    strategy_10k_max_positions: int = STRATEGY_10K_MAX_POSITIONS,
    top_strategies_k: int = 10,
    prefer_allocation: str = "auto",
    min_strategy_n: int = 0,
    sec_rows: list[dict] | None = None,
) -> str:
    """Genera report testuale e opzionalmente salva in out_path. Se sec_rows è fornito, esporta SEC_TRANSACTIONS.csv (righe originali + BUY_AGGREGATED)."""
    lines = []
    lines.append("=" * 72)
    lines.append("  AGENTE STRATEGIE SEC — Backtest 3 anni, dati Massive")
    lines.append("=" * 72)
    lines.append("")
    lines.append("--- SINTESI ---")
    lines.append("")
    df_clean, quality_stats = _filter_quality_clusters(df_results)
    exit_stats = _check_exit_price_consistency(df_results)

    lines.append(f"Cluster (acquisti SEC) backtestati (grezzi): {len(df_results)}")
    lines.append(f"Cluster usati per analisi (dopo filtri qualità): {len(df_clean)}")
    dropped_total = quality_stats.get("dropped_entry_missing", 0) + quality_stats.get("dropped_ret30_missing", 0)
    if dropped_total:
        lines.append(
            f"  - Rimossi per qualità: entry_price mancante={quality_stats.get('dropped_entry_missing', 0)}, "
            f"ret_high_30d_open mancante={quality_stats.get('dropped_ret30_missing', 0)}"
        )
    if quality_stats.get("extreme_1d"):
        lines.append(f"  - Segnalazione: {quality_stats['extreme_1d']} cluster con variazioni estreme su 1 giorno (|ret_1d|>500%).")
    if exit_stats:
        total_mismatch = sum(exit_stats.values())
        if total_mismatch:
            parts = [f"{col}={n}" for col, n in exit_stats.items() if n]
            lines.append(f"  - Coerenza exit price: {total_mismatch} valori non allineati a entry*(1+ret/100) (dettaglio: {', '.join(parts)}).")
        else:
            lines.append("  - Coerenza exit price: nessuna anomalia rilevante sulle colonne principali.")
    lines.append(f"Errori / cluster saltati: {len(errors)}")
    lines.append(f"Strategie valutate: {len(ranking)} (tutte le combinazioni filtro + orizzonte hold)")
    lines.append("")
    # Copertura dati SEC (se disponibile da load_sec_buys)
    if 'LAST_SEC_COVERAGE' in globals() and LAST_SEC_COVERAGE:
        lines.append("--- Copertura dati SEC (finestre filing_day) ---")
        for start_s, end_s, count, truncated in LAST_SEC_COVERAGE:
            msg = f"Finestra [{start_s} → {end_s}) — {count} filing"
            if truncated:
                msg += "  **ATTENZIONE: raggiunto max_results, possibile taglio dati in questa finestra**"
            lines.append(msg)
        lines.append("")
    lines.append("--- TUTTE LE STRATEGIE (ordinamento per Avg_ret_high_% decrescente; high/low = orizzonte 30d) ---")
    lines.append("")
    lines.append("Include strategie «Tutti i cluster» (nessun filtro), per ruolo (CEO, CFO, Director, 10% Owner),")
    lines.append("combo, variazione % posizione, dimensione valore, analisi tecnica, ecc.")
    lines.append("")
    if not ranking:
        lines.append("Nessuna strategia con dati.")
    else:
        lines.append(pd.DataFrame(ranking).to_string(index=False))
    lines.append("")
    lines.append("--- FILE GENERATI (dati completi e report leggibili) ---")
    lines.append("")
    _base = out_path.stem.replace("_REPORT", "") if out_path else "STRATEGY_AGENT"
    lines.append("  Ogni output è disponibile in CSV + XLSX (Excel) e in MD + PDF (leggibile/allineato).")
    lines.append(f"  Report principale: {_base}_REPORT.txt e .pdf (questo riepilogo).")
    lines.append("")
    lines.append(f"  {_base}_RANKING.csv / .xlsx — Tabella strategie (tutte), con colonna **Score** (punteggio 0–100 su cui è basato il ranking).")
    lines.append("    Come si calcola lo Score: per ogni macrocategoria (Base_name) si fa la media di Avg_ret_% e di Win_rate_% sulle righe che la compongono.")
    lines.append("    Si normalizzano entrambe le medie tra 0 e 1 (min=0, max=1 sul set delle macrocategorie). Score = 50% × (media rendimento normalizzata) + 50% × (media win rate normalizzata), riportato in scala 0–100. Ordine: Score decrescente → Ranking 1, 2, 3, ...")
    lines.append(f"  {_base}_RANKING_SEC_ONLY.csv / .xlsx — Ranking solo dati SEC (no analisi tecnica: RSI, 52w, MA, Price vs MA). Stesso calcolo Score.")
    lines.append(f"  {_base}_STRATEGIES.md / .pdf — Strategie in Markdown e PDF.")
    lines.append(f"  {_base}_CASES.csv / .xlsx — DATABASE COMPLETO: una riga per cluster. Per ogni orizzonte: ret/exit per open, news, news_bot, insider (entry_price, entry_price_news, entry_price_news_bot, insider_entry_price).")
    lines.append(f"  {_base}_CASES_KEYS.csv / .xlsx, {_base}_CASES_KEYS_LONG.csv / .xlsx — Chiavi e formato long (stessi 4 entry: open, news, news_bot, insider).")
    lines.append(f"  {_base}_CASES_REPORT.md / .pdf — Analisi caso per caso: migliori, peggiori.")
    lines.append(f"  {_base}_TICKERS.md / .pdf, {_base}_TICKERS.csv / .xlsx — Report per ticker.")
    lines.append(f"  {_base}_ERRORS.csv / .xlsx — Cluster con errori/saltati.")
    lines.append("")
    lines.append("--- Strategia futura e Bot ---")
    lines.append("")
    lines.append(f"  {_base}_10K.md / .pdf, {_base}_10K.csv / .xlsx — STRATEGIA SUL FUTURO (10k USD, tre finestre).")
    lines.append("    Il CSV contiene i cluster consigliati dalla strategia vincente (ticker, filing_day, entry_price, exit_price, allocation_usd, ret %, pnl_usd).")
    lines.append("    Usalo per applicare da oggi: stessi criteri sui nuovi Form 4, importi in allocation_usd.")
    lines.append("")
    lines.append(f"  {_base}_BOT_SUGGESTIONS.csv / .xlsx — Suggerimenti del bot (generato in automatico a fine run).")
    lines.append(f"  {_base}_TICKER_BUY_RANKING.csv / .xlsx — Quale ticker comprare per primo (ultimi 5 gg), con hold/take profit %/stop loss %.")
    lines.append("")
    lines.append(f"  {_base}_SEC_TRANSACTIONS.csv / .xlsx — Transazioni SEC (originali + BUY_AGGREGATED).")
    lines.append(f"  {_base}_SEC_CLUSTERS_ALL.csv / .xlsx — Cluster SEC con in_backtest, in_strategies, strategies (macrocategoria).")
    lines.append("  ALL_CLUSTERS_DB.csv / .xlsx — Database cumulativo cluster (entry/exit high, low, mean).")
    lines.append(f"  {_base}_ALL_XLSX.xlsx — Tutti gli XLSX in un unico file (un foglio per XLSX).")
    lines.append("")
    lines.append("=" * 72)
    report = "\n".join(lines)
    if out_path:
        out_path.write_text(report, encoding="utf-8")
        # PDF del report principale (stesso contenuto, facile da leggere)
        try:
            import markdown
            from weasyprint import HTML
            def _escape(s: str) -> str:
                return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
            html_body = f"<pre style='font-family:Consolas,monospace;font-size:11pt;line-height:1.4;'>{_escape(report)}</pre>"
            html_doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8"/><style>body {{ font-family: Segoe UI, sans-serif; margin: 1.5cm; }}</style></head><body>{html_body}</body></html>"""
            PDF_PATH = out_path.with_suffix(".pdf")
            HTML(string=html_doc).write_pdf(PDF_PATH)
        except Exception:
            pass
        # Export CSV e Markdown nella stessa cartella (estraibili e condivisibili)
        out_dir = out_path.parent
        base = out_path.stem.replace("_REPORT", "")
        csv_path = out_dir / f"{base}_RANKING.csv"
        md_path = out_dir / f"{base}_STRATEGIES.md"
        cases_path = out_dir / f"{base}_CASES.csv"
        cases_keys_path = out_dir / f"{base}_CASES_KEYS.csv"
        cases_keys_long_path = out_dir / f"{base}_CASES_KEYS_LONG.csv"
        cases_report_path = out_dir / f"{base}_CASES_REPORT.md"
        tickers_md_path = out_dir / f"{base}_TICKERS.md"
        tickers_csv_path = out_dir / f"{base}_TICKERS.csv"
        ticker_strategies_path = out_dir / f"{base}_TICKER_STRATEGIES.csv"
        strategy_10k_md_path = out_dir / f"{base}_10K.md"
        strategy_10k_csv_path = out_dir / f"{base}_10K.csv"
        errors_path = out_dir / f"{base}_ERRORS.csv"
        sec_transactions_path = out_dir / f"{base}_SEC_TRANSACTIONS.csv"
        sec_clusters_all_path = out_dir / f"{base}_SEC_CLUSTERS_ALL.csv"
        all_clusters_db_path = out_dir / "ALL_CLUSTERS_DB.csv"

        def _export_step(name: str, fn):
            try:
                fn()
            except Exception as e:
                print(f"Avviso: export '{name}' non completato ({type(e).__name__}: {e})", file=sys.stderr)

        def _to_xlsx(path_xlsx: Path, df: pd.DataFrame) -> None:
            """Export opzionale in Excel (.xlsx) con colonne leggibili; fallback silenzioso se openpyxl manca."""
            try:
                import openpyxl  # noqa: F401
                df.to_excel(path_xlsx, index=False, engine="openpyxl")
            except ImportError:
                pass
            except Exception as e:
                print(f"Avviso: export xlsx non completato ({type(e).__name__}: {e})", file=sys.stderr)

        def _text_to_pdf(src_path: Path, pdf_path: Path, is_markdown: bool = True) -> None:
            """Genera PDF da file .md o .txt (leggibile e allineato); fallback silenzioso se weasyprint manca."""
            if not src_path.exists():
                return
            try:
                import markdown
                from weasyprint import HTML
                text = src_path.read_text(encoding="utf-8")
                if is_markdown:
                    html_body = markdown.markdown(text, extensions=["tables", "fenced_code", "nl2br"])
                else:
                    html_body = f"<pre style='font-family:Consolas,monospace;font-size:11pt;line-height:1.4;'>{_escape_html(text)}</pre>"
                html_doc = f"""<!DOCTYPE html><html><head><meta charset="utf-8"/><style>
body {{ font-family: Segoe UI, sans-serif; font-size: 11pt; line-height: 1.4; margin: 1.5cm; }}
table {{ border-collapse: collapse; margin: 1em 0; }}
th, td {{ border: 1px solid #ccc; padding: 4px 8px; text-align: left; }}
</style></head><body>{html_body}</body></html>"""
                HTML(string=html_doc).write_pdf(pdf_path)
            except ImportError:
                pass
            except Exception as e:
                print(f"Avviso: export pdf non completato ({type(e).__name__}: {e})", file=sys.stderr)

        def _escape_html(s: str) -> str:
            return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

        RANKING_COL_ORDER = [
            "Ranking", "Score", "Strategia", "Base_name", "Descrizione", "Hold", "Metric_kind", "Horizon_days", "Entry_kind",
            "News_vs_Open", "Insider_type",
            "Tickers_used", "Clusters_used", "Tickers_used_N", "Clusters_used_N", "N", "N_filter",
            "Win_rate_%", "Avg_ret_%", "Median_ret_%", "Total_ret_%", "Std_%", "Sharpe", "Min_%", "Max_%",
        ]

        def _rank_by_base_name(df: pd.DataFrame, col_order: list[str]) -> pd.DataFrame:
            """
            Assegna Ranking e Score per macrocategoria (Base_name).
            Score (0–100): 50% media Avg_ret_% normalizzata + 50% media Win_rate_% normalizzata.
            """
            if df.empty:
                return df
            agg = df.groupby("Base_name", dropna=False).agg(
                mean_avg_ret=("Avg_ret_%", "mean"),
                mean_win_rate=("Win_rate_%", "mean"),
            ).reset_index()
            r_min, r_max = agg["mean_avg_ret"].min(), agg["mean_avg_ret"].max()
            w_min, w_max = agg["mean_win_rate"].min(), agg["mean_win_rate"].max()
            norm_ret = (agg["mean_avg_ret"] - r_min) / (r_max - r_min) if (r_max - r_min) != 0 else 0.5
            norm_win = (agg["mean_win_rate"] - w_min) / (w_max - w_min) if (w_max - w_min) != 0 else 0.5
            agg["_score"] = 0.5 * norm_ret + 0.5 * norm_win
            agg = agg.sort_values("_score", ascending=False)
            base_to_rank = {b: r for r, b in enumerate(agg["Base_name"], 1)}
            base_to_score = dict(zip(agg["Base_name"], (agg["_score"] * 100).round(2)))
            out = df.copy()
            out["Ranking"] = out["Base_name"].map(base_to_rank)
            out["Score"] = out["Base_name"].map(base_to_score)
            return out[[c for c in col_order if c in out.columns]]

        def _export_csv_xlsx(df: pd.DataFrame, csv_path: Path, xlsx_path: Path) -> None:
            df.to_csv(csv_path, index=False, encoding="utf-8-sig", sep=";")
            _to_xlsx(xlsx_path, df)

        try:
            rank_df = pd.DataFrame(ranking)
            if not rank_df.empty:
                rank_df = _rank_by_base_name(rank_df, RANKING_COL_ORDER)
                _export_csv_xlsx(rank_df, csv_path, out_dir / f"{base}_RANKING.xlsx")
                ranking_sec_only = [r for r in ranking if _is_sec_only_strategy(str(r.get("Strategia") or ""))]
                if ranking_sec_only:
                    rank_df_sec = _rank_by_base_name(pd.DataFrame(ranking_sec_only), RANKING_COL_ORDER)
                    _export_csv_xlsx(rank_df_sec, out_dir / f"{base}_RANKING_SEC_ONLY.csv", out_dir / f"{base}_RANKING_SEC_ONLY.xlsx")
                # Esporta anche mappa ticker-strategia (macro, senza giorni): una riga per (ticker, Base_name)
                ts_rows: list[dict] = []
                for r in ranking:
                    base_name = r.get("Base_name") or ""
                    tickers_used = (r.get("Tickers_used") or "").split(",") if r.get("Tickers_used") else []
                    for t in tickers_used:
                        t_clean = t.strip().upper()
                        if not t_clean or not base_name:
                            continue
                        ts_rows.append({"ticker": t_clean, "strategia": base_name})
                if ts_rows:
                    ts_df = pd.DataFrame(ts_rows).drop_duplicates()
                    _export_csv_xlsx(ts_df, ticker_strategies_path, out_dir / f"{base}_TICKER_STRATEGIES.xlsx")
            if ranking and not rank_df.empty:
                md_lines = [
                    "# Agente strategie SEC — Tutte le strategie (tutte le combinazioni filtro + hold)",
                    "",
                    f"Cluster backtestati: {len(df_results)} | Errori/saltati: {len(errors)} | Strategie (righe ranking): {len(ranking)}",
                    "",
                    "Ogni riga = una combinazione (filtro, orizzonte, metrica, entry). **Ranking** = posizione per macrocategoria (Base_name), ordinata per **Score** decrescente.",
                    "",
                    "**Come si calcola lo Score (0–100):** per ogni macrocategoria (Base_name) si calcola la media di *Avg_ret_%* e la media di *Win_rate_%* sulle righe che la compongono. Le due medie vengono normalizzate tra 0 e 1 (min e max sul set di tutte le macrocategorie). Score = 50% × (media rendimento normalizzata) + 50% × (media win rate normalizzata), in scala 0–100. Più alto lo Score, migliore la posizione nel ranking.",
                    "",
                    "| # | Ranking | Score | Strategia | Base_name | News_vs_Open | Insider_type | Metric_kind | Horizon_days | N | Win_rate_% | Avg_ret_% | Median_ret_% | Total_ret_% | Std_% | Sharpe | Min_% | Max_% |",
                    "|---|--------|------|-----------|-----------|--------------|--------------|------------|--------------|---|------------|-----------|--------------|-------------|------|--------|-------|-------|",
                ]
                for i, r in enumerate(rank_df.to_dict("records"), 1):
                    md_lines.append(
                        f"| {i} | {r.get('Ranking', '')} | {r.get('Score', '')} | {r.get('Strategia', '')} | {r.get('Base_name', '')} | {r.get('News_vs_Open', '')} | {r.get('Insider_type', '')} | {r.get('Metric_kind', '')} | {r.get('Horizon_days', '')} | {r.get('N', '')} | {r.get('Win_rate_%', '')} | {r.get('Avg_ret_%', '')} | {r.get('Median_ret_%', '')} | {r.get('Total_ret_%', '')} | {r.get('Std_%', '')} | {r.get('Sharpe', '')} | {r.get('Min_%', '')} | {r.get('Max_%', '')} |"
                    )
                md_path.write_text("\n".join(md_lines), encoding="utf-8")
                _text_to_pdf(md_path, md_path.with_suffix(".pdf"), is_markdown=True)
        except Exception as e:
            print(f"Avviso: export RANKING/STRATEGIES non completato ({type(e).__name__}: {e})", file=sys.stderr)
        if not df_results.empty:
            def _export_cases() -> None:
                cols = _canonical_cluster_columns(list(df_results.columns), include_run_base=False)
                df_ordered = df_results[cols]
                _export_csv_xlsx(df_ordered, cases_path, out_dir / f"{base}_CASES.xlsx")
            _export_step("CASES.csv", _export_cases)
            def _export_cases_keys() -> None:
                export_cases_keys_csv(df_results, cases_keys_path)
                if cases_keys_path.exists():
                    _to_xlsx(out_dir / f"{base}_CASES_KEYS.xlsx", pd.read_csv(cases_keys_path, sep=";", encoding="utf-8-sig"))
            _export_step("CASES_KEYS.csv", _export_cases_keys)
            def _export_cases_keys_long() -> None:
                export_cases_keys_long_csv(df_results, cases_keys_long_path)
                if cases_keys_long_path.exists():
                    _to_xlsx(out_dir / f"{base}_CASES_KEYS_LONG.xlsx", pd.read_csv(cases_keys_long_path, sep=";", encoding="utf-8-sig"))
            _export_step("CASES_KEYS_LONG.csv", _export_cases_keys_long)
            def _export_cases_report() -> None:
                build_cases_report(
                    df_clean,
                    out_path=cases_report_path,
                    top_n=REPORT_CASES_TOP_N,
                    bottom_n=REPORT_CASES_BOTTOM_N,
                    include_all=True,
                )
                if cases_report_path.exists():
                    _text_to_pdf(cases_report_path, cases_report_path.with_suffix(".pdf"), is_markdown=True)
            _export_step("CASES_REPORT", _export_cases_report)
            def _export_tickers() -> None:
                build_tickers_report(df_clean, out_path=tickers_md_path, out_path_csv=tickers_csv_path, ranking=ranking)
                if tickers_md_path.exists():
                    _text_to_pdf(tickers_md_path, tickers_md_path.with_suffix(".pdf"), is_markdown=True)
                if tickers_csv_path.exists():
                    _to_xlsx(out_dir / f"{base}_TICKERS.xlsx", pd.read_csv(tickers_csv_path, sep=";", encoding="utf-8-sig"))
            _export_step("TICKERS", _export_tickers)
            def _export_10k() -> None:
                build_10k_strategy(
                    df_clean,
                    ranking,
                    out_path=strategy_10k_md_path,
                    out_path_csv=strategy_10k_csv_path,
                    budget_usd=strategy_10k_budget,
                    lookback_days=strategy_10k_lookback_days,
                    max_positions=strategy_10k_max_positions,
                    top_strategies_k=top_strategies_k,
                    prefer_allocation=prefer_allocation,
                    min_strategy_n=min_strategy_n,
                )
                if strategy_10k_md_path.exists():
                    _text_to_pdf(strategy_10k_md_path, strategy_10k_md_path.with_suffix(".pdf"), is_markdown=True)
                if strategy_10k_csv_path.exists():
                    _to_xlsx(out_dir / f"{base}_10K.xlsx", pd.read_csv(strategy_10k_csv_path, sep=";", encoding="utf-8-sig"))
            _export_step("10K", _export_10k)
            if errors:
                def _export_errors() -> None:
                    err_df = pd.DataFrame(errors)
                    _export_csv_xlsx(err_df, errors_path, out_dir / f"{base}_ERRORS.xlsx")
                _export_step("ERRORS.csv", _export_errors)
        if sec_rows:
            # Tutte le transazioni SEC (originali + summary per timestamp con più BUY)
            def _export_sec_transactions() -> None:
                df_st = pd.DataFrame(rows_with_aggregated(sec_rows))
                _export_csv_xlsx(df_st, sec_transactions_path, sec_transactions_path.with_suffix(".xlsx"))
            _export_step("SEC_TRANSACTIONS.csv", _export_sec_transactions)
            # Tutti i cluster SEC (anche senza prezzi), con flag se usati nel backtest / ranking
            def _export_sec_clusters_all() -> None:
                clusters = group_by_cluster(sec_rows)
                if not clusters:
                    return
                df_cl = pd.DataFrame(clusters)
                df_cl["cluster_key"] = df_cl.apply(_cluster_key_from_row, axis=1)
                used_keys_backtest = set()
                if not df_results.empty:
                    for _, r in df_results.iterrows():
                        k = _cluster_key_from_row(r)
                        if k:
                            used_keys_backtest.add(k)
                used_keys_strat = set()
                strat_by_key: dict[str, set[str]] = {}
                for r in ranking:
                    base_name = (r.get("Base_name") or "").strip() or (r.get("Strategia") or "")
                    clusters_used = (r.get("Clusters_used") or "").split(",") if r.get("Clusters_used") else []
                    for ck in clusters_used:
                        ck = ck.strip()
                        if not ck:
                            continue
                        used_keys_strat.add(ck)
                        if base_name:
                            strat_by_key.setdefault(ck, set()).add(base_name)
                df_cl["in_backtest"] = df_cl["cluster_key"].isin(used_keys_backtest)
                df_cl["in_strategies"] = df_cl["cluster_key"].isin(used_keys_strat)
                df_cl["strategies"] = df_cl["cluster_key"].map(
                    lambda ck: ",".join(sorted(strat_by_key.get(ck, set())))
                )
                # Ordine logico: chiave e flag prima, poi resto
                sec_first = [c for c in ["cluster_key", "ticker", "filing_day", "filedAt", "in_backtest", "in_strategies", "strategies"] if c in df_cl.columns]
                sec_rest = sorted([c for c in df_cl.columns if c not in sec_first])
                df_cl = df_cl[sec_first + sec_rest]
                _export_csv_xlsx(df_cl, sec_clusters_all_path, sec_clusters_all_path.with_suffix(".xlsx"))
            _export_step("SEC_CLUSTERS_ALL.csv", _export_sec_clusters_all)

        # Database cumulativo di tutti i cluster (per run future / analisi veloci)
        if not df_results.empty:
            def _update_all_clusters() -> None:
                key_cols = [c for c in ("ticker", "filing_day", "filedAt") if c in df_results.columns]
                df_db = df_results.copy()
                df_db["run_base"] = base
                if all_clusters_db_path.exists():
                    existing = pd.read_csv(all_clusters_db_path, sep=";", encoding="utf-8-sig", low_memory=False)
                    combined = pd.concat([existing, df_db], ignore_index=True)
                    # Se un cluster (ticker+data) esiste già, teniamo la versione più recente (ultima run),
                    # così eventuali correzioni/calcoli nuovi sovrascrivono quelli vecchi.
                    if key_cols:
                        combined = combined.drop_duplicates(subset=key_cols, keep="last")
                else:
                    combined = df_db
                cols = _canonical_cluster_columns(list(combined.columns), include_run_base=True)
                combined = combined[cols]
                _export_csv_xlsx(combined, all_clusters_db_path, out_dir / "ALL_CLUSTERS_DB.xlsx")
            _export_step("ALL_CLUSTERS_DB.csv", _update_all_clusters)

    return report


def export_all_xlsx_to_one(out_dir: Path, base: str) -> None:
    """Scrive un unico XLSX con tutti gli XLSX (base_*.xlsx e ALL_CLUSTERS_DB.xlsx) come fogli. Chiamare dopo report e bot."""
    xlsx_files = sorted(out_dir.glob(f"{base}_*.xlsx")) + (
        [out_dir / "ALL_CLUSTERS_DB.xlsx"] if (out_dir / "ALL_CLUSTERS_DB.xlsx").exists() else []
    )
    # Escludi il file di output stesso se già presente
    out_path = out_dir / f"{base}_ALL_XLSX.xlsx"
    xlsx_files = [p for p in xlsx_files if p.resolve() != out_path.resolve()]
    if not xlsx_files:
        return
    try:
        import openpyxl  # noqa: F401
        with pd.ExcelWriter(out_path, engine="openpyxl") as writer:
            for p in xlsx_files:
                sheets = pd.read_excel(p, sheet_name=None, engine="openpyxl")
                for orig_name, df in sheets.items():
                    # Nome foglio: stem del file (es. RANKING) o stem_sheet se più fogli; max 31 caratteri
                    name = p.stem if len(sheets) == 1 else f"{p.stem}_{orig_name}"
                    sheet_name = name[:31].replace("\\", "_").replace("/", "_").replace("*", "_").replace("?", "_").replace(":", "_").replace("[", "_").replace("]", "_")
                    if not sheet_name:
                        sheet_name = "Sheet"
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
    except ImportError:
        pass
    except Exception as e:
        print(f"Avviso: export ALL_XLSX.xlsx non completato ({type(e).__name__}: {e})", file=sys.stderr)