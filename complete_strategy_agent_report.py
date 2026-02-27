"""
Completa i report dell'agente strategie a partire dai file già generati (CASES.csv e RANKING.csv).
Utile se una run è terminata con errore durante l'export (es. KeyError) e vuoi rigenerare
solo 10K.md, CASES_REPORT.md, TICKERS.md/csv senza rilanciare il backtest.

Uso (dalla root del progetto):
    python complete_strategy_agent_report.py
    python complete_strategy_agent_report.py --base BACKTEST_STRATEGIE   # se hai *_CASES.csv e *_RANKING.csv con quel prefisso
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "massive_backtest") not in sys.path:
    sys.path.insert(0, str(ROOT / "massive_backtest"))

def main() -> None:
    import pandas as pd
    from massive_backtest.strategy_agent import (
        build_cases_report,
        build_tickers_report,
        build_10k_strategy,
        REPORT_CASES_TOP_N,
        REPORT_CASES_BOTTOM_N,
        STRATEGY_10K_BUDGET,
        STRATEGY_10K_LOOKBACK_DAYS,
        STRATEGY_10K_MAX_POSITIONS,
    )

    ap = argparse.ArgumentParser(description="Rigenera report da CASES.csv e RANKING.csv")
    ap.add_argument("--base", type=str, default="STRATEGY_AGENT", help="Prefisso file (es. STRATEGY_AGENT o BACKTEST_STRATEGIE)")
    args = ap.parse_args()
    base = (args.base or "STRATEGY_AGENT").strip()

    cases_path = ROOT / f"{base}_CASES.csv"
    ranking_path = ROOT / f"{base}_RANKING.csv"
    if not cases_path.exists():
        print(f"ERRORE: {cases_path.name} non trovato. Esegui prima run_strategy_agent.py (o specifica --base).", file=sys.stderr)
        sys.exit(1)
    if not ranking_path.exists():
        print(f"ERRORE: {ranking_path.name} non trovato. Esegui prima run_strategy_agent.py (o specifica --base).", file=sys.stderr)
        sys.exit(1)

    df_results = pd.read_csv(cases_path, sep=";", encoding="utf-8-sig", low_memory=False)
    rank_df = pd.read_csv(ranking_path, sep=";", encoding="utf-8-sig")
    ranking = rank_df.to_dict("records")
    cases_report_path = ROOT / f"{base}_CASES_REPORT.md"
    tickers_md_path = ROOT / f"{base}_TICKERS.md"
    tickers_csv_path = ROOT / f"{base}_TICKERS.csv"
    strategy_10k_md_path = ROOT / f"{base}_10K.md"
    strategy_10k_csv_path = ROOT / f"{base}_10K.csv"

    print("Rigenerazione report da CASES + RANKING...", file=sys.stderr)
    try:
        build_cases_report(df_results, out_path=cases_report_path, top_n=REPORT_CASES_TOP_N, bottom_n=REPORT_CASES_BOTTOM_N, include_all=True)
        print(f"  {cases_report_path.name}", file=sys.stderr)
    except Exception as e:
        print(f"  CASES_REPORT: {e}", file=sys.stderr)
    try:
        build_tickers_report(df_results, out_path=tickers_md_path, out_path_csv=tickers_csv_path, ranking=ranking)
        print(f"  {tickers_md_path.name}, {tickers_csv_path.name}", file=sys.stderr)
    except Exception as e:
        print(f"  TICKERS: {e}", file=sys.stderr)
    try:
        build_10k_strategy(
            df_results,
            ranking,
            out_path=strategy_10k_md_path,
            out_path_csv=strategy_10k_csv_path,
            budget_usd=STRATEGY_10K_BUDGET,
            lookback_days=STRATEGY_10K_LOOKBACK_DAYS,
            max_positions=STRATEGY_10K_MAX_POSITIONS,
            top_strategies_k=10,
            prefer_allocation="auto",
            min_strategy_n=0,
        )
        print(f"  {strategy_10k_md_path.name}, {strategy_10k_csv_path.name}", file=sys.stderr)
    except Exception as e:
        print(f"  10K: {e}", file=sys.stderr)

    print("Completato. Controlla i file nella root del progetto.", file=sys.stderr)


if __name__ == "__main__":
    main()
