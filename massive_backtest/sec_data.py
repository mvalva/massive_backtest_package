"""
Caricamento dati SEC (Form 4, solo P) dalla root del progetto.
Raggruppamento per cluster (ticker + data) o lista singoli acquisti.
"""

from __future__ import annotations

import os
from typing import Callable
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEC_TOOLS = ROOT / "sec_tools"
for p in (str(ROOT), str(SEC_TOOLS)):
    if p not in sys.path:
        sys.path.insert(0, p)

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
    load_dotenv(Path(__file__).resolve().parent / ".env", override=True)
except Exception:
    pass

try:
    from sec_latest_buys import fetch_transactions, extract_buys
except ImportError:
    fetch_transactions = None
    extract_buys = None

FUND_PATTERN = re.compile(r"\b(fund|etf|trust|reit)\b", re.I)

# Ultima copertura SEC calcolata da load_sec_buys:
# lista di tuple (start_date, end_date, count, truncated_flag)
LAST_SEC_COVERAGE: list[tuple[str, str, int, bool]] = []


def load_sec_buys(
    days: int = 182,
    max_results: int = 3000,
    exclude_funds: bool = True,
    progress_callback: Callable[[str, float], None] | None = None,
) -> tuple[list[dict], str | None]:
    """
    Carica transazioni P da SEC API; opzionale filtro no fondi.
    progress_callback(msg, pct) opzionale per aggiornamenti durante il fetch (pct 0-10).
    Ritorna (lista righe, errore). Se errore è non None, la lista può essere vuota.
    """
    def _progress(msg: str, pct: float) -> None:
        if progress_callback:
            progress_callback(msg, pct)

    if not fetch_transactions or not extract_buys:
        return [], "Modulo sec_latest_buys non disponibile (fetch_transactions/extract_buys)."
    key = os.getenv("SEC_API_KEY", "").strip()
    if not key:
        return [], "SEC_API_KEY non impostata nel .env."
    global LAST_SEC_COVERAGE
    try:
        import datetime as dt
        today = dt.date.today()
        coverage_info: list[tuple[str, str, int, bool]] = []
        # Se days <= 365: singola finestra (comportamento classico).
        # Se days > 365: spezza l'intervallo in finestre di ~365 giorni per coprire davvero tutto il periodo,
        # evitando che il limite max_results tagli via gli anni più vecchi.
        if days <= 365:
            _progress("Caricamento SEC (singola finestra, può richiedere alcuni minuti)...", 0)
            if days == 1:
                start_d = today
                end_d = today + dt.timedelta(days=1)
            else:
                start_d = today - dt.timedelta(days=days)
                end_d = today + dt.timedelta(days=1)
            txs = fetch_transactions(key, days=days, page_size=50, max_results=max_results, only_buy_p=True)
            coverage_info.append((start_d.isoformat(), end_d.isoformat(), len(txs), len(txs) >= max_results > 0 if max_results else False))
        else:
            earliest = today - dt.timedelta(days=days)
            txs_all: list = []
            # Calcola quante finestre per il progresso
            _st = earliest
            n_windows = 0
            while _st < today:
                n_windows += 1
                _st = min(_st + dt.timedelta(days=365), today)
            # Finestre [start, end] di al massimo 365 giorni ciascuna, fino a oggi
            start = earliest
            win = 0
            while start < today:
                end = min(start + dt.timedelta(days=365), today)
                win += 1
                start_s = start.isoformat()
                end_s = (end + dt.timedelta(days=1)).isoformat()
                pct = 10 * (win - 1) / max(n_windows, 1)
                _progress(f"Caricamento SEC finestra {win}/{n_windows} ({start_s} -> {end_s[:10]})...", pct)
                seg = fetch_transactions(
                    key,
                    days=0,
                    page_size=50,
                    max_results=max_results,
                    only_buy_p=True,
                    start_date=start_s,
                    end_date=end_s,
                )
                txs_all.extend(seg)
                coverage_info.append((start_s, end_s, len(seg), len(seg) >= max_results > 0 if max_results else False))
                start = end
            txs = txs_all
    except Exception as e:
        return [], f"Errore lettura SEC API: {type(e).__name__}: {e}"
    try:
        rows = extract_buys(txs)
    except Exception as e:
        return [], f"Errore estrazione acquisti SEC: {type(e).__name__}: {e}"
    # Log di copertura per l'utente (stderr): quali finestre sono state coperte e se sono probabilmente troncate
    LAST_SEC_COVERAGE = coverage_info
    if rows:
        print("Copertura dati SEC (per finestre filing_day):", file=sys.stderr)
        for start_s, end_s, count, truncated in coverage_info:
            msg = f"  Finestra [{start_s} -> {end_s}) - {count} filing"
            if truncated:
                msg += f" (ATTENZIONE: raggiunto max_results={max_results}, possibile taglio dati in questa finestra)"
            print(msg, file=sys.stderr)
    if not exclude_funds:
        return rows, None
    out = []
    for r in rows:
        company = (r.get("company") or "").strip()
        if company and FUND_PATTERN.search(company):
            continue
        out.append(r)
    return out, None


def _is_date_iso(s: str) -> bool:
    """Verifica che s sia una data YYYY-MM-DD valida (solo formato)."""
    if not s or len(s) < 10:
        return False
    try:
        y, m, d = int(s[:4]), int(s[5:7]), int(s[8:10])
        return 1 <= m <= 12 and 1 <= d <= 31 and y >= 1990
    except (ValueError, IndexError):
        return False


def get_rows_for_clustering(rows: list[dict]) -> list[dict]:
    """
    Per il backtest: una riga per (ticker, filedAt). Stesso ticker + stesso timestamp → una sola
    posizione con quantity = somma, price = media ponderata (value/qty).
    Non modifica le righe originali; ritorna una nuova lista da passare a group_by_cluster.
    """
    if not rows:
        return []
    from collections import defaultdict
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in rows:
        ticker = (r.get("ticker") or "").strip().upper()
        if not ticker:
            continue
        filed_at = (r.get("filedAt") or "").strip()
        if not filed_at:
            continue
        key = (ticker, filed_at)
        groups[key].append(r)
    out = []
    for (ticker, filed_at), items in groups.items():
        try:
            qtys = [float(x.get("qty") or 0) for x in items]
            values = [float(x.get("value") or 0) for x in items]
        except (TypeError, ValueError):
            qtys, values = [0.0] * len(items), [0.0] * len(items)
        sum_qty = sum(qtys)
        sum_value = sum(values)
        weighted_price = sum_value / sum_qty if sum_qty and sum_qty != 0 else (items[0].get("price") if items else None)
        first = items[0]
        pct_increases = [x.get("pct_increase_position") for x in items if x.get("pct_increase_position") is not None]
        try:
            pct_max = max(float(x) for x in pct_increases) if pct_increases else None
        except (TypeError, ValueError):
            pct_max = None
        out.append({
            "ticker": ticker,
            "filedAt": filed_at,
            "company": first.get("company") or "",
            "insider": first.get("insider") or "",
            "title": first.get("title") or "",
            "code": first.get("code") or "P",
            "qty": sum_qty,
            "value": sum_value,
            "price": weighted_price,
            "tradeDate": first.get("tradeDate") or "",
            "link": first.get("link") or "",
            "pct_increase_position": pct_max,
        })
    return out


def rows_with_aggregated(rows: list[dict]) -> list[dict]:
    """
    Mantiene TUTTE le righe originali e aggiunge UNA riga extra per ogni gruppo (stesso ticker + stesso timestamp, BUY).
    - Originali: signal='BUY', is_summary=False (copia per non mutare).
    - Extra per gruppo: signal='BUY_AGGREGATED', is_summary=True, quantity=sum(qty), price=media ponderata, value=sum(value).
    """
    if not rows:
        return []
    from collections import defaultdict
    # Copia originali con signal e is_summary
    out = []
    for r in rows:
        copy = dict(r)
        copy["signal"] = "BUY"
        copy["is_summary"] = False
        out.append(copy)
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in rows:
        ticker = (r.get("ticker") or "").strip().upper()
        filed_at = (r.get("filedAt") or "").strip()
        if not ticker or not filed_at:
            continue
        groups[(ticker, filed_at)].append(r)
    for (ticker, filed_at), items in groups.items():
        try:
            qtys = [float(x.get("qty") or 0) for x in items]
            values = [float(x.get("value") or 0) for x in items]
        except (TypeError, ValueError):
            qtys, values = [0.0] * len(items), [0.0] * len(items)
        sum_qty = sum(qtys)
        sum_value = sum(values)
        weighted_price = sum_value / sum_qty if sum_qty and sum_qty != 0 else None
        pct_increases = [x.get("pct_increase_position") for x in items if x.get("pct_increase_position") is not None]
        try:
            pct_max = max(float(x) for x in pct_increases) if pct_increases else None
        except (TypeError, ValueError):
            pct_max = None
        # Aggiungi una riga aggregata solo se ci sono almeno 2 BUY nello stesso (ticker, filedAt).
        # insider = tutti i nomi di chi ha comprato, separati da "+"; idem title.
        if len(items) > 1:
            first = items[0]
            insiders_seen: list[str] = []
            titles_seen: list[str] = []
            for r in items:
                i = str(r.get("insider") or "").strip()
                t = str(r.get("title") or "").strip()
                if i and i not in insiders_seen:
                    insiders_seen.append(i)
                if t and t not in titles_seen:
                    titles_seen.append(t)
            agg_insider = "+".join(insiders_seen) if insiders_seen else "AGGREGATED"
            agg_title = "+".join(titles_seen) if titles_seen else "AGGREGATED"
            out.append({
                "ticker": ticker,
                "filedAt": filed_at,
                "signal": "BUY_AGGREGATED",
                "is_summary": True,
                "company": first.get("company") or "",
                "insider": agg_insider,
                "title": agg_title,
                "code": "P",
                "qty": sum_qty,
                "value": sum_value,
                "price": weighted_price,
                "tradeDate": first.get("tradeDate") or "",
                "link": first.get("link") or "",
                "pct_increase_position": pct_max,
            })
    return out


def insider_entry_prices_by_cluster(rows: list[dict]) -> dict[tuple[str, str], float]:
    """
    Per ogni cluster (ticker, filing_day) calcola il prezzo di acquisto insider come media ponderata
    (sum(value)/sum(qty)) sulle righe SEC. Usato per arricchire i risultati del backtest.
    Ritorna dict (ticker_upper, filing_day_YYYY-MM-DD) -> price (float).
    """
    from collections import defaultdict
    out: dict[tuple[str, str], list[tuple[float, float]]] = defaultdict(list)
    for r in rows:
        ticker = (r.get("ticker") or "").strip().upper()
        filed_at = r.get("filedAt") or ""
        filing_day = (filed_at[:10]) if len(filed_at) >= 10 else ""
        if not ticker or not filing_day or len(filing_day) < 10:
            continue
        try:
            qty = float(r.get("qty") or 0)
            value = float(r.get("value") or 0)
        except (TypeError, ValueError):
            continue
        if qty <= 0:
            continue
        out[(ticker, filing_day)].append((value, qty))
    result = {}
    for (ticker, fd), pairs in out.items():
        total_val = sum(v for v, _ in pairs)
        total_qty = sum(q for _, q in pairs)
        if total_qty and total_qty > 0:
            result[(ticker, fd)] = total_val / total_qty
    return result


def group_by_cluster(rows: list[dict]) -> list[dict]:
    """
    Una riga per (ticker, filing_day). filing_day = data calendario (YYYY-MM-DD) condivisa da tutti gli acquisti del cluster.
    Criterio filing date del cluster:
    - filing_day: è il giorno (data) in cui cade almeno un filing; tutti i trade del cluster hanno filedAt in quel giorno.
    - filedAt esposto: il primo filing del giorno (min tra i filedAt del gruppo), così l'entry backtest è coerente
      con "quando il mercato ha visto la prima notizia".
    """
    if not rows:
        return []
    from collections import defaultdict
    groups = defaultdict(list)
    for r in rows:
        ticker = (r.get("ticker") or "").strip().upper()
        if not ticker:
            continue
        filed_at = r.get("filedAt") or ""
        filing_day = (filed_at[:10]) if len(filed_at) >= 10 else ""
        if not filing_day or not _is_date_iso(filing_day):
            continue
        try:
            val = float(r.get("value") or 0)
            qty = float(r.get("qty") or 0)
        except (TypeError, ValueError):
            val, qty = 0.0, 0.0
        pct_inc = r.get("pct_increase_position")
        if pct_inc is not None:
            try:
                pct_inc = float(pct_inc)
            except (TypeError, ValueError):
                pct_inc = None
        groups[(ticker, filing_day)].append({
            "value": val, "qty": qty, "company": r.get("company") or "",
            "filedAt": filed_at, "insider": r.get("insider") or "", "title": r.get("title") or "",
            "pct_increase_position": pct_inc,
        })
    out = []
    for (ticker, filing_day), items in groups.items():
        value_tot = sum(x["value"] for x in items)
        qty_tot = sum(x["qty"] for x in items)
        # Variazione % posizione: max tra le transazioni del cluster (almeno un insider ha aumentato di almeno X%)
        pct_increases = [x["pct_increase_position"] for x in items if x.get("pct_increase_position") is not None]
        pct_increase_position_max = max(pct_increases) if pct_increases else None
        # Primo filing del giorno (min filedAt) → coerenza con "quando il mercato ha visto la notizia"
        filed_at_sorted = sorted(x["filedAt"] for x in items if x.get("filedAt"))
        filed_at_first = filed_at_sorted[0] if filed_at_sorted else (items[0]["filedAt"] if items else "")
        # Numero di BUY "effettivi": consideriamo un solo buy per timestamp (filedAt) uguale,
        # così split tecnici dello stesso trade non contano come trade multipli.
        unique_filed_at = {x["filedAt"] for x in items if x.get("filedAt")}
        n_buys = len(unique_filed_at) if unique_filed_at else len(items)
        first = items[0]
        titles = " | ".join(sorted({(x.get("title") or "").strip() for x in items if (x.get("title") or "").strip()}))
        insiders = " | ".join(sorted({(x.get("insider") or "").strip() for x in items if (x.get("insider") or "").strip()}))
        out.append({
            "ticker": ticker,
            "filing_day": filing_day,
            "filedAt": filed_at_first,
            "company": first["company"],
            "value_tot": value_tot,
            "qty_tot": qty_tot,
            "n_buys": n_buys,
            "titles": titles,
            "insiders": insiders,
            "pct_increase_position_max": pct_increase_position_max,
        })
    return out
