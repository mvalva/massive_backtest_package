from __future__ import annotations

"""
Bot di base per usare i risultati dell'agente strategie in modo operativo.

Funzioni principali:
- Legge il file {base}_RANKING.csv e seleziona le strategie migliori secondo un criterio.
- Legge {base}_SEC_CLUSTERS_ALL.csv e individua i cluster "nuovi" (es. ultimi X giorni).
- Per ogni strategia scelta, genera una lista di trade da eseguire (ticker, filtro, orizzonte, tipo entry).

Nota: questo script non manda ordini al broker; produce solo un piano di trading
che puoi poi collegare a un'esecuzione reale.
"""

import argparse
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import List

import pandas as pd


def _safe_print(msg: str) -> None:
    """Stampa su console evitando UnicodeEncodeError su Windows (cp1252)."""
    try:
        print(msg)
    except UnicodeEncodeError:
        print(msg.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8"))


@dataclass
class StrategyChoice:
    name: str
    base_name: str
    metric_kind: str
    horizon_days: int
    entry_kind: str
    avg_ret: float
    win_rate: float
    n: int


def load_ranking(base: str, root: Path | None = None) -> pd.DataFrame:
    root = root or Path(__file__).resolve().parent
    path = root / f"{base}_RANKING.csv"
    if not path.exists():
        raise FileNotFoundError(f"{path} non trovato")
    return pd.read_csv(path, sep=";", encoding="utf-8-sig")


def select_best_strategies(
    rank_df: pd.DataFrame,
    metric_kind: str = "mean",
    min_n: int = 30,
    top_k: int = 5,
) -> List[StrategyChoice]:
    df = rank_df.copy()
    df = df[df["Metric_kind"].str.lower() == metric_kind.lower()]
    df = df[df["N"] >= min_n]
    if df.empty:
        return []
    # Criterio: rendimento medio per giorno di borsa (Avg_ret_% / Horizon_days), decrescente
    df["ret_per_day"] = df["Avg_ret_%"] / df["Horizon_days"].replace(0, pd.NA)
    df = df.sort_values(["ret_per_day", "Avg_ret_%"], ascending=False)
    choices: List[StrategyChoice] = []
    for _, r in df.head(top_k).iterrows():
        choices.append(
            StrategyChoice(
                name=str(r.get("Strategia")),
                base_name=str(r.get("Base_name")),
                metric_kind=str(r.get("Metric_kind")),
                horizon_days=int(r.get("Horizon_days") or 0),
                entry_kind=str(r.get("Entry_kind")),
                avg_ret=float(r.get("Avg_ret_%") or 0.0),
                win_rate=float(r.get("Win_rate_%") or 0.0),
                n=int(r.get("N") or 0),
            )
        )
    return choices


def load_sec_clusters_all(base: str, root: Path | None = None) -> pd.DataFrame:
    root = root or Path(__file__).resolve().parent
    path = root / f"{base}_SEC_CLUSTERS_ALL.csv"
    if not path.exists():
        raise FileNotFoundError(f"{path} non trovato")
    return pd.read_csv(path, sep=";", encoding="utf-8-sig", low_memory=False)


def recommend_trades_for_strategy(
    clusters_df: pd.DataFrame,
    strategy: StrategyChoice,
    days_back: int = 7,
) -> pd.DataFrame:
    """
    Suggerisce trade "futuri" per una strategia:
    - prende solo i cluster degli ultimi `days_back` giorni (filing_day recente)
    - usa la colonna in_strategies/strategies di SEC_CLUSTERS_ALL per filtrare quelli
      che la strategia ha usato storicamente (stesso pattern di cluster).
    """
    df = clusters_df.copy()
    if "filing_day" not in df.columns:
        if "filedAt" in df.columns:
            df["filing_day"] = df["filedAt"].astype(str).str[:10]
        else:
            return pd.DataFrame()
    df["filing_day"] = df["filing_day"].astype(str).str[:10]
    today = date.today()
    cutoff = (today - timedelta(days=days_back)).isoformat()
    df_recent = df[df["filing_day"] >= cutoff].copy()
    if df_recent.empty:
        return df_recent
    # Teniamo solo i cluster che storicamente sono usati da questa strategia (colonna strategies = Base_name)
    base_name = strategy.base_name
    def _used_by(row: pd.Series) -> bool:
        s = str(row.get("strategies") or "")
        return base_name in [x.strip() for x in s.split(",")] if s else False
    df_recent = df_recent[df_recent.apply(_used_by, axis=1)]
    # Output minimale per un bot: ticker, filing_day, company, value_tot, n_buys
    cols = [c for c in ["ticker", "filing_day", "company", "value_tot", "qty_tot", "n_buys", "pct_increase_position_max"] if c in df_recent.columns]
    return df_recent[cols].sort_values("filing_day", ascending=True)


# Ultimi N giorni (calendar days come proxy per giorni bancari) per il ranking "quale ticker comprare"
TICKER_BUY_DAYS_BACK = 5


def _load_cluster_prices(root: Path, base: str) -> dict[tuple[str, str], dict]:
    """
    Carica (ticker, filing_day) -> {entry_price, exit_high_Nd, exit_low_Nd, mean_price_Nd, ma50, ma200, rsi}.
    Prova {base}_CASES.csv poi ALL_CLUSTERS_DB.csv.
    """
    out: dict[tuple[str, str], dict] = {}
    for path in [root / f"{base}_CASES.csv", root / "ALL_CLUSTERS_DB.csv"]:
        if not path.exists():
            continue
        try:
            df = pd.read_csv(path, sep=";", encoding="utf-8-sig", low_memory=False)
        except Exception:
            continue
        if "ticker" not in df.columns or "filing_day" not in df.columns:
            if "filedAt" in df.columns:
                df["filing_day"] = df["filedAt"].astype(str).str[:10]
            else:
                continue
        df["filing_day"] = df["filing_day"].astype(str).str[:10]
        for _, r in df.iterrows():
            t = str(r.get("ticker", "")).strip().upper()
            fd = str(r.get("filing_day", ""))[:10]
            if not t or not fd:
                continue
            key = (t, fd)
            if key in out:
                continue
            entry = r.get("entry_price")
            try:
                entry = float(entry) if entry is not None and str(entry).strip() not in ("", "nan") else None
            except (TypeError, ValueError):
                entry = None
            out[key] = {
                "entry_price": entry,
                "ma50_entry": _num(r.get("ma50_entry")),
                "ma200_entry": _num(r.get("ma200_entry")),
                "rsi_entry": _num(r.get("rsi_entry")),
                "pct_from_52w_high": _num(r.get("pct_from_52w_high")),
            }
            for n in [1, 2, 3, 5, 7, 10, 14, 30]:
                hcol = f"exit_high_{n}d_open_price"
                lcol = f"exit_low_{n}d_open_price"
                mcol = f"mean_price_{n}d_open"
                vh = _num(r.get(hcol)) if hcol in df.columns else None
                vl = _num(r.get(lcol)) if lcol in df.columns else None
                vm = _num(r.get(mcol)) if mcol in df.columns else None
                if vh is not None:
                    out[key][f"exit_high_{n}d"] = vh
                if vl is not None:
                    out[key][f"exit_low_{n}d"] = vl
                if vm is not None:
                    out[key][f"mean_price_{n}d"] = vm
        break
    return out


def _num(x) -> float | None:
    if x is None or (isinstance(x, float) and pd.isna(x)):
        return None
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def _load_insider_prices_from_sec_transactions(root: Path, base: str) -> dict[tuple[str, str], float]:
    """
    Prezzo di acquisto insider da SEC_TRANSACTIONS.
    Preferisce le righe BUY_AGGREGATED (is_summary=True) quando presenti: una riga per (ticker, filedAt)
    con value/qty già aggregati. Se non c'è aggregata, usa la somma delle righe BUY originali.
    Ritorna (ticker, filing_day) -> price (float).
    """
    path = root / f"{base}_SEC_TRANSACTIONS.csv"
    if not path.exists():
        return {}
    try:
        df = pd.read_csv(path, sep=";", encoding="utf-8-sig", low_memory=False)
    except Exception:
        return {}
    if "ticker" not in df.columns:
        return {}
    filed_col = "filedAt" if "filedAt" in df.columns else None
    if not filed_col:
        return {}
    has_summary = "is_summary" in df.columns
    # Per ogni (ticker, fd): se esiste riga BUY_AGGREGATED usala; altrimenti somma righe BUY
    by_key: dict[tuple[str, str], list[tuple[float, float]]] = defaultdict(list)
    aggregated_keys: set[tuple[str, str]] = set()
    for _, r in df.iterrows():
        t = str(r.get("ticker", "")).strip().upper()
        fd = str(r.get(filed_col, ""))[:10]
        if not t or not fd or len(fd) < 10:
            continue
        qty = _num(r.get("qty"))
        value = _num(r.get("value"))
        if qty is None or value is None or qty <= 0:
            continue
        is_agg = has_summary and (r.get("is_summary") is True or str(r.get("is_summary", "")).upper() == "TRUE")
        if is_agg:
            by_key[(t, fd)] = [(value, qty)]
            aggregated_keys.add((t, fd))
        elif (t, fd) not in aggregated_keys:
            by_key[(t, fd)].append((value, qty))
    result = {}
    for (t, fd), pairs in by_key.items():
        total_val = sum(v for v, _ in pairs)
        total_qty = sum(q for _, q in pairs)
        if total_qty and total_qty > 0:
            result[(t, fd)] = total_val / total_qty
    return result


def _load_cluster_strategies(root: Path, base: str) -> dict[tuple[str, str], list[str]]:
    """
    Carica (ticker, filing_day) -> lista di Base_name (strategie a cui appartiene il cluster).
    Da SEC_CLUSTERS_ALL, colonna "strategies" (comma-separated).
    """
    path = root / f"{base}_SEC_CLUSTERS_ALL.csv"
    out: dict[tuple[str, str], list[str]] = {}
    if not path.exists():
        return out
    try:
        df = pd.read_csv(path, sep=";", encoding="utf-8-sig", low_memory=False)
    except Exception:
        return out
    if "ticker" not in df.columns or "strategies" not in df.columns:
        return out
    if "filing_day" not in df.columns and "filedAt" in df.columns:
        df = df.copy()
        df["filing_day"] = df["filedAt"].astype(str).str[:10]
    for _, r in df.iterrows():
        t = str(r.get("ticker", "")).strip().upper()
        fd = str(r.get("filing_day", "") or r.get("filedAt", ""))[:10]
        if not t or not fd:
            continue
        raw = r.get("strategies")
        if raw is None or (isinstance(raw, float) and pd.isna(raw)):
            bases = []
        else:
            bases = [x.strip() for x in str(raw).split(",") if x.strip()]
        out[(t, fd)] = bases
    return out


def _most_specific_strategy(
    strats: list[dict],
    cluster_base_names: list[str],
) -> dict:
    """
    Tra le strategie che includono il ticker, sceglie la più specifica per questo cluster.
    Es: se il cluster è CEO + large company, preferisce "CEO only + Value ≥100k" rispetto a "CEO only" o "Tutti".
    Specificità = numero di filtri (più " + " nel Base_name = più specifico); tra quelle che matchano il cluster.
    Se nessuna strategia del cluster è in lista, fallback alla migliore per rank/avg_ret.
    """
    if not strats:
        return None
    # Solo strategie il cui Base_name è tra quelle del cluster (situazione più simile nel passato)
    matching = [s for s in strats if s.get("base_name", "").strip() in cluster_base_names]
    if not matching:
        matching = strats
    # Ordina per specificità: più " + " nel nome = più filtri = più specifico; poi per rank, poi avg_ret
    def specificity_key(s):
        bn = s.get("base_name") or ""
        n_plus = bn.count(" + ")
        return (-n_plus, -len(bn), s.get("rank", 9999), -s.get("avg_ret", 0))
    return min(matching, key=specificity_key)


def build_ticker_buy_ranking(
    all_rows: list[dict],
    rank_df: pd.DataFrame,
    best: List[StrategyChoice],
    base: str,
    root: Path,
    trading_days_back: int = TICKER_BUY_DAYS_BACK,
) -> Path | None:
    """
    Ranking "quale ticker comprare per primo": ultimi `trading_days_back` giorni.
    La strategia indicata è la MACRO (Base_name), non la variante singola (hold/high/mean/low).
    Take profit e stop loss sono calcolati sull'insieme della macro:
    - Take profit % = media di Avg_ret_% su tutte le varianti della macro (hold/high/mean/low).
    - Stop loss % = -|min(Min_%)| su tutte le varianti (peggior caso storico della macro).
    - suggested_hold_days = orizzonte della variante con miglior Avg_ret_% nella macro.
    insider_entry_price = prezzo reale acquisto insider da SEC_TRANSACTIONS (media ponderata value/qty); fallback da CASES se assente.
    """
    if not all_rows or rank_df.empty:
        return None
    today = date.today()
    cutoff = (today - timedelta(days=trading_days_back)).isoformat()
    rank_df = rank_df.reset_index(drop=True)
    cluster_strategies = _load_cluster_strategies(root, base)
    # Raccogli per (ticker, base_name) tutte le righe del RANKING (ogni riga = variante hold/high/mean/low)
    # Poi aggregiamo per macro: take profit = media Avg_ret_%, stop loss = min Min_%, strategia mostrata = Base_name
    macro_raw: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for i, r in rank_df.iterrows():
        base_name = str(r.get("Base_name") or "").strip()
        if not base_name:
            continue
        rank_val = r.get("Ranking")
        try:
            rank_val = int(rank_val) if rank_val is not None and str(rank_val).strip() not in ("", "nan") else i + 1
        except (TypeError, ValueError):
            rank_val = i + 1
        raw = r.get("Tickers_used")
        if raw is None or (isinstance(raw, float) and pd.isna(raw)):
            tickers_used = []
        else:
            tickers_used = str(raw).strip().split(",") if str(raw).strip() else []
        row_data = {
            "rank": rank_val,
            "avg_ret": float(r.get("Avg_ret_%") or 0),
            "min_ret": float(r.get("Min_%") or 0),
            "horizon_days": int(r.get("Horizon_days") or 0),
        }
        for t in tickers_used:
            t = t.strip().upper()
            if not t:
                continue
            macro_raw[(t, base_name)].append(row_data)
    # Una voce per (ticker, base_name): media Avg_ret_%, min Min_%, orizzonte = quello con max Avg_ret_%, rank = min
    ticker_to_strategies: dict[str, list[dict]] = {}
    for (ticker, base_name), rows in macro_raw.items():
        if not rows:
            continue
        avg_vals = [x["avg_ret"] for x in rows if x["avg_ret"] is not None and not (isinstance(x["avg_ret"], float) and pd.isna(x["avg_ret"]))]
        min_vals = [x["min_ret"] for x in rows if x["min_ret"] is not None and not (isinstance(x["min_ret"], float) and pd.isna(x["min_ret"]))]
        avg_ret_macro = sum(avg_vals) / len(avg_vals) if avg_vals else 0.0
        min_ret_macro = min(min_vals) if min_vals else 0.0
        best_row = max(rows, key=lambda x: x["avg_ret"] if x["avg_ret"] is not None and not (isinstance(x["avg_ret"], float) and pd.isna(x["avg_ret"])) else -1.0)
        rank_macro = min(x["rank"] for x in rows)
        if ticker not in ticker_to_strategies:
            ticker_to_strategies[ticker] = []
        ticker_to_strategies[ticker].append({
            "name": base_name,
            "base_name": base_name,
            "rank": rank_macro,
            "avg_ret": avg_ret_macro,
            "min_ret": min_ret_macro,
            "horizon_days": best_row["horizon_days"],
        })
    recent = [row for row in all_rows if str(row.get("filing_day", ""))[:10] >= cutoff]
    if not recent:
        return None
    by_ticker: dict[str, dict] = {}
    for row in recent:
        ticker = str(row.get("ticker", "")).strip().upper()
        if not ticker:
            continue
        fd = str(row.get("filing_day", ""))[:10]
        if ticker not in by_ticker:
            by_ticker[ticker] = {
                "ticker": ticker,
                "company": row.get("company", ""),
                "filing_day": fd,
                "value_tot": row.get("value_tot"),
            }
        if fd > by_ticker[ticker]["filing_day"]:
            by_ticker[ticker]["filing_day"] = fd
            by_ticker[ticker]["company"] = row.get("company", "")
            by_ticker[ticker]["value_tot"] = row.get("value_tot")
    cluster_prices = _load_cluster_prices(root, base)
    insider_prices_sec = _load_insider_prices_from_sec_transactions(root, base)
    rows_out = []
    for ticker, data in by_ticker.items():
        strats = ticker_to_strategies.get(ticker, [])
        if not strats:
            continue
        key = (ticker, data["filing_day"])
        cluster_bases = cluster_strategies.get(key, [])
        best_strat = _most_specific_strategy(strats, cluster_bases)
        if not best_strat:
            continue
        score = best_strat["avg_ret"]
        h = best_strat["horizon_days"]
        prices = cluster_prices.get(key, {})
        # insider_entry_price = prezzo reale acquisto insider da SEC_TRANSACTIONS (value/qty); fallback a CASES
        entry_insider = insider_prices_sec.get(key)
        if entry_insider is None:
            entry_insider = prices.get("entry_price")
        if entry_insider is None and prices:
            for n in [1, 2, 3, 5, 7, 10, 14, 30]:
                if h <= n and prices.get(f"mean_price_{n}d") is not None:
                    entry_insider = prices[f"mean_price_{n}d"]
                    break
        if entry_insider is not None:
            entry_insider = round(float(entry_insider), 2)
        # stop_loss_pct = sempre negativo (es. -5 = uscita se -5% rispetto a entry insider)
        min_ret = best_strat["min_ret"]
        stop_loss_pct = -abs(min_ret) if min_ret is not None else None
        if stop_loss_pct is not None:
            stop_loss_pct = round(stop_loss_pct, 2)
        # Exit prices legati all'insider entry: target = entry*(1+take_profit%), stop = entry*(1+stop_loss%)
        take_pct = best_strat["avg_ret"]
        exit_target = round(entry_insider * (1 + take_pct / 100.0), 2) if entry_insider is not None and take_pct is not None else None
        exit_stop = round(entry_insider * (1 + (stop_loss_pct or 0) / 100.0), 2) if entry_insider is not None and stop_loss_pct is not None else None
        ma50 = prices.get("ma50_entry")
        ma200 = prices.get("ma200_entry")
        rsi = prices.get("rsi_entry")
        row_out = {
            "ticker": ticker,
            "company": data.get("company", ""),
            "filing_day": data["filing_day"],
            "n_strategies": len(strats),
            "score_avg_ret": round(score, 2),
            "best_strategy": best_strat["name"],
            "suggested_hold_days": best_strat["horizon_days"],
            "take_profit_pct": round(best_strat["avg_ret"], 2),
            "stop_loss_pct": stop_loss_pct,
            "value_tot": data.get("value_tot"),
            "insider_entry_price": entry_insider,
            "entry_price_potential": entry_insider,
            "exit_price_potential": exit_target,
            "exit_price_stop_potential": exit_stop,
        }
        if ma50 is not None:
            row_out["ma50_support"] = round(ma50, 2)
        if ma200 is not None:
            row_out["ma200_support"] = round(ma200, 2)
        if rsi is not None:
            row_out["rsi_entry"] = round(rsi, 1)
        rows_out.append(row_out)
    if not rows_out:
        return None
    df = pd.DataFrame(rows_out)
    df = df.sort_values("score_avg_ret", ascending=False).reset_index(drop=True)
    df.insert(0, "rank", range(1, len(df) + 1))
    out_path = root / f"{base}_TICKER_BUY_RANKING.csv"
    df.to_csv(out_path, index=False, encoding="utf-8-sig", sep=";")
    try:
        df.to_excel(root / f"{base}_TICKER_BUY_RANKING.xlsx", index=False, engine="openpyxl")
    except Exception:
        pass
    return out_path


def run_bot(
    base: str,
    root: Path | None = None,
    metric_kind: str = "high",
    min_n: int = 0,
    top_k: int = 5,
    days_back: int = 7,
) -> Path | None:
    """
    Genera {base}_BOT_SUGGESTIONS.csv senza usare argparse.
    Genera anche {base}_TICKER_BUY_RANKING.csv (quale ticker comprare per primo, ultimi 5 gg, hold/take profit/stop loss).
    Restituisce il path del file BOT_SUGGESTIONS scritto, o None se nessun suggerimento o errore.
    """
    root = root or Path(__file__).resolve().parent
    out_suggestions = root / f"{base}_BOT_SUGGESTIONS.csv"
    try:
        rank_df = load_ranking(base, root=root)
        best = select_best_strategies(rank_df, metric_kind=metric_kind, min_n=min_n, top_k=top_k)
        if not best:
            return None
        clusters_all = load_sec_clusters_all(base, root=root)
        all_rows: list[dict] = []
        for s in best:
            trades = recommend_trades_for_strategy(clusters_all, s, days_back=days_back)
            for _, row in trades.iterrows():
                rec = dict(row)
                rec["strategia"] = s.name
                rec["metric_kind"] = s.metric_kind
                rec["horizon_days"] = s.horizon_days
                rec["entry_kind"] = s.entry_kind
                all_rows.append(rec)
        if all_rows:
            df_out = pd.DataFrame(all_rows)
            df_out.to_csv(out_suggestions, index=False, encoding="utf-8-sig", sep=";")
            try:
                xlsx_path = out_suggestions.with_suffix(".xlsx")
                df_out.to_excel(xlsx_path, index=False, engine="openpyxl")
            except Exception:
                pass
            build_ticker_buy_ranking(all_rows, rank_df, best, base, root, trading_days_back=TICKER_BUY_DAYS_BACK)
            return out_suggestions
    except Exception:
        pass
    return None


def main() -> None:
    ap = argparse.ArgumentParser(description="Bot base per usare le strategie SEC in modo operativo")
    ap.add_argument("--base", type=str, default="STRATEGY_AGENT", help="Prefisso dei file (es. STRATEGY_AGENT o STRATEGY_AGENT_TEST)")
    ap.add_argument("--metric-kind", type=str, default="mean", choices=["high", "low", "mean"], help="Tipo metrica da preferire (high/low/mean)")
    ap.add_argument("--min-n", type=int, default=30, help="Minimo N cluster per considerare una strategia")
    ap.add_argument("--top-k", type=int, default=3, help="Numero di strategie top da considerare")
    ap.add_argument("--days-back", type=int, default=7, help="Giorni indietro per suggerimenti futuri (nuovi filing)")
    args = ap.parse_args()

    base = args.base
    root = Path(__file__).resolve().parent
    out_suggestions = root / f"{base}_BOT_SUGGESTIONS.csv"
    rank_df = load_ranking(base)
    best = select_best_strategies(rank_df, metric_kind=args.metric_kind, min_n=args.min_n, top_k=args.top_k)
    if not best:
        print("Nessuna strategia soddisfa i criteri (Metric_kind, min_n).")
        return
    _safe_print(f"Strategie selezionate (obiettivo: piu soldi in meno tempo, usando {args.metric_kind}):")
    for s in best:
        _safe_print(
            f"- {s.name} | kind={s.metric_kind}, horizon={s.horizon_days}d, entry={s.entry_kind}, "
            f"N={s.n}, Avg_ret_%={s.avg_ret}, Win_rate_%={s.win_rate}"
        )
    clusters_all = load_sec_clusters_all(base)
    print("")
    _safe_print(f"Suggerimenti trade per gli ultimi {args.days_back} giorni:")
    all_rows: list[dict] = []
    for s in best:
        print("")
        _safe_print(f"=== Strategia: {s.name} (kind={s.metric_kind}, horizon={s.horizon_days}d, entry={s.entry_kind}) ===")
        trades = recommend_trades_for_strategy(clusters_all, s, days_back=args.days_back)
        if trades.empty:
            print("Nessun cluster recente compatibile.")
        else:
            _safe_print(trades.to_string(index=False))
            for _, row in trades.iterrows():
                rec = dict(row)
                rec["strategia"] = s.name
                rec["metric_kind"] = s.metric_kind
                rec["horizon_days"] = s.horizon_days
                rec["entry_kind"] = s.entry_kind
                all_rows.append(rec)
    if all_rows:
        pd.DataFrame(all_rows).to_csv(out_suggestions, index=False, encoding="utf-8-sig", sep=";")
        build_ticker_buy_ranking(all_rows, rank_df, best, base, root, trading_days_back=TICKER_BUY_DAYS_BACK)
        print("")
        print(f"Piano di trading salvato in: {out_suggestions}")
        ticker_rank_path = root / f"{base}_TICKER_BUY_RANKING.csv"
        if ticker_rank_path.exists():
            print(f"Ranking ticker (quale comprare per primo): {ticker_rank_path}")


if __name__ == "__main__":
    main()

