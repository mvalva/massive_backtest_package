"""
Esegue l'agente strategie SEC: 3 anni di dati SEC + backtest Massive,
valutazione di tutte le strategie (filtri + orizzonti hold) e report delle migliori.

Richiede: SEC_API_KEY e MASSIVE_API_KEY nel .env (root o massive_backtest/).
Prima della run: python check_before_run.py (verifica chiavi e dipendenze).

Uso:
    python run_strategy_agent.py
    python run_strategy_agent.py --days 1095 --max-results 15000
    python run_strategy_agent.py --days 30 --max-results 500   # prova veloce
    python run_strategy_agent.py --update-outputs-only   # rigenera report/bot da CASES+RANKING senza backtest
    python run_strategy_agent.py --max-clusters 200   # run veloce con 200 cluster
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
if str(ROOT / "massive_backtest") not in sys.path:
    sys.path.insert(0, str(ROOT / "massive_backtest"))

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
    load_dotenv(ROOT / "massive_backtest" / ".env", override=True)
except Exception:
    pass

# Suffissi file di output per (out_dir, base). ALL_CLUSTERS_DB è in out_dir senza prefisso base.
OUTPUT_STEMS = (
    "{base}_REPORT.txt", "{base}_REPORT.pdf",
    "{base}_RANKING.csv", "{base}_RANKING.xlsx",
    "{base}_RANKING_SEC_ONLY.csv", "{base}_RANKING_SEC_ONLY.xlsx",
    "{base}_STRATEGIES.md", "{base}_STRATEGIES.pdf",
    "{base}_CASES.csv", "{base}_CASES.xlsx",
    "{base}_CASES_KEYS.csv", "{base}_CASES_KEYS.xlsx",
    "{base}_CASES_KEYS_LONG.csv", "{base}_CASES_KEYS_LONG.xlsx",
    "{base}_CASES_REPORT.md", "{base}_CASES_REPORT.pdf",
    "{base}_TICKERS.md", "{base}_TICKERS.pdf", "{base}_TICKERS.csv", "{base}_TICKERS.xlsx",
    "{base}_TICKER_STRATEGIES.csv", "{base}_TICKER_STRATEGIES.xlsx",
    "{base}_10K.md", "{base}_10K.pdf", "{base}_10K.csv", "{base}_10K.xlsx",
    "{base}_ERRORS.csv", "{base}_ERRORS.xlsx",
    "{base}_SEC_TRANSACTIONS.csv", "{base}_SEC_TRANSACTIONS.xlsx",
    "{base}_SEC_CLUSTERS_ALL.csv", "{base}_SEC_CLUSTERS_ALL.xlsx",
    "{base}_IMPROVEMENT.txt",
    "{base}_BOT_SUGGESTIONS.csv", "{base}_BOT_SUGGESTIONS.xlsx",
    "{base}_TICKER_BUY_RANKING.csv", "{base}_TICKER_BUY_RANKING.xlsx",
    "ALL_CLUSTERS_DB.csv", "ALL_CLUSTERS_DB.xlsx",
    "{base}_ALL_XLSX.xlsx",
)
# Riepilogo a fine run: (stem, etichetta). Usa OUTPUT_STEMS per cleanup.
OUTPUT_SUMMARY = (
    ("{base}_STRATEGIES.md", "Tutte le strategie (Markdown)"),
    ("{base}_CASES.csv", "Risultati caso per caso (database completo)"),
    ("{base}_CASES_REPORT.md", "Report caso per caso"),
    ("{base}_TICKERS.md", "Report per ticker"),
    ("{base}_10K.md", "Strategia 10k USD"),
    ("{base}_BOT_SUGGESTIONS.csv", "Suggerimenti bot"),
    ("{base}_SEC_TRANSACTIONS.csv", "Transazioni SEC"),
)
PROGRESS_FILE = ROOT / "STRATEGY_AGENT_PROGRESS.txt"


def _write_progress(path: Path, text: str, append: bool = False) -> None:
    """Scrive una riga nel file progresso. Se append=True accoda, altrimenti sovrascrive."""
    try:
        with path.open("a" if append else "w", encoding="utf-8") as f:
            f.write(text + "\n")
            f.flush()
            os.fsync(f.fileno())
    except OSError:
        pass


def _cleanup_outputs(out_dir: Path, base: str) -> int:
    """Elimina i file di output esistenti per (out_dir, base). Ritorna il numero di file rimossi."""
    removed = 0
    for stem in OUTPUT_STEMS:
        name = stem.format(base=base)
        p = out_dir / name
        if p.exists():
            try:
                p.unlink()
                removed += 1
            except OSError:
                pass
    if PROGRESS_FILE.exists():
        try:
            PROGRESS_FILE.unlink()
            removed += 1
        except OSError:
            pass
    return removed


def _load_update_only_data(out_dir: Path, base: str):
    """Carica df_results, ranking, errors da CASES/RANKING/ERRORS. Solleva SystemExit se file mancanti."""
    import pandas as pd
    cases_path = out_dir / f"{base}_CASES.csv"
    ranking_path = out_dir / f"{base}_RANKING.csv"
    if not cases_path.exists():
        print(f"ERRORE: {cases_path.name} non trovato. Esegui prima una run completa (senza --update-outputs-only).", file=sys.stderr)
        sys.exit(1)
    if not ranking_path.exists():
        print(f"ERRORE: {ranking_path.name} non trovato. Esegui prima una run completa (senza --update-outputs-only).", file=sys.stderr)
        sys.exit(1)
    df_results = pd.read_csv(cases_path, sep=";", encoding="utf-8-sig", low_memory=False)
    rank_df = pd.read_csv(ranking_path, sep=";", encoding="utf-8-sig")
    ranking = rank_df.to_dict("records")
    errors_path = out_dir / f"{base}_ERRORS.csv"
    if errors_path.exists():
        try:
            err_df = pd.read_csv(errors_path, sep=";", encoding="utf-8-sig")
            errors = err_df.to_dict("records") if not err_df.empty else []
        except Exception:
            errors = []
    else:
        errors = []
    return df_results, ranking, errors


def main() -> None:
    """Esegue agente SEC: carica dati, backtest, ranking strategie e genera report."""
    import argparse
    ap = argparse.ArgumentParser(description="Agente strategie SEC — backtest 3 anni Massive")
    from massive_backtest.strategy_agent import (
        run_agent,
        build_report,
        export_all_xlsx_to_one,
        STRATEGY_DEFINITIONS_UNIFIED,
        STRATEGY_10K_BUDGET,
        STRATEGY_10K_LOOKBACK_DAYS,
        STRATEGY_10K_MAX_POSITIONS,
    )

    ap.add_argument("--days", type=int, default=1095, help="Giorni indietro per SEC (default 1095 = 3 anni)")
    ap.add_argument("--max-results", type=int, default=5000, help="Max risultati SEC API (default 5000)")
    ap.add_argument("--out", type=str, default="", help="File report output (default: STRATEGY_AGENT_REPORT.txt)")
    ap.add_argument("--budget-usd", type=float, default=STRATEGY_10K_BUDGET, help="Budget USD per la simulazione 10k (default 10000)")
    ap.add_argument("--lookback-days", type=int, default=STRATEGY_10K_LOOKBACK_DAYS, help="Giorni per finestra 10k (default 365)")
    ap.add_argument("--max-positions", type=int, default=STRATEGY_10K_MAX_POSITIONS, help="Max posizioni per finestra 10k (0 = tutte)")
    ap.add_argument("--top-strategies-k", type=int, default=10, help="Numero di strategie top dal ranking da testare nel 10k (default 10)")
    ap.add_argument("--prefer-allocation", type=str, choices=["auto", "all_in", "equal_weight"], default="auto",
                    help="Allocazione 10k: auto, all_in, equal_weight")
    ap.add_argument("--min-strategy-n", type=int, default=0, help="Escludi dal 10k strategie con meno di N cluster (0 = nessun filtro)")
    ap.add_argument("--max-clusters", type=int, default=0, help="Backtesta al massimo N cluster (0 = tutti). Es. 200 per prova veloce.")
    ap.add_argument("--parallel", type=int, default=0, metavar="N", help="Worker paralleli per il backtest (0 = sequenziale)")
    ap.add_argument("--update-outputs-only", action="store_true",
                    help="Aggiorna solo i file di output da CASES.csv e RANKING.csv senza backtest né API.")
    ap.add_argument("--no-clean", action="store_true", help="Non cancellare i file di output esistenti prima della run.")
    args = ap.parse_args()

    update_only = args.update_outputs_only
    if not update_only and (args.days <= 0 or args.max_results <= 0):
        print("ERRORE: --days e --max-results devono essere positivi.", file=sys.stderr)
        sys.exit(1)
    if not update_only and (not os.getenv("SEC_API_KEY") or not os.getenv("MASSIVE_API_KEY")):
        print("ERRORE: Imposta SEC_API_KEY e MASSIVE_API_KEY nel file .env (root o massive_backtest/.env).", file=sys.stderr)
        print("Verifica l'ambiente con: python check_before_run.py", file=sys.stderr)
        sys.exit(1)

    out_path = Path(args.out) if args.out else ROOT / "STRATEGY_AGENT_REPORT.txt"
    out_dir = out_path.parent
    base = out_path.stem.replace("_REPORT", "") or out_path.stem

    def progress(msg: str, pct: float) -> None:
        line = f"[{pct:.0f}%] {msg}"
        print(line, flush=True)
        _write_progress(PROGRESS_FILE, line, append=True)

    if update_only:
        _write_progress(PROGRESS_FILE, "=== Aggiornamento output (nessun backtest) ===", append=False)
        print("Aggiornamento file di output da CASES + RANKING (nessun backtest)...", file=sys.stderr)
        df_results, ranking, errors = _load_update_only_data(out_dir, base)
        sec_rows = None
    else:
        # Precheck: verifica ambiente e dipendenze
        import check_before_run
        if check_before_run.main() != 0:
            sys.exit(1)
        # Cancella output esistenti (stesso base) prima della run
        if not args.no_clean:
            n = _cleanup_outputs(out_dir, base)
            if n:
                print(f"Rimossi {n} file di output esistenti.", file=sys.stderr)
        _write_progress(PROGRESS_FILE, "=== Avvio agente (backtest + ranking) ===", append=False)
        print("Avvio agente: SEC + backtest Massive + ranking strategie...", file=sys.stderr)
        print(f"Progresso in tempo reale: {PROGRESS_FILE.name}", file=sys.stderr)
        errors = []
        try:
            df_results, errors, ranking, sec_rows = run_agent(
                days_sec=args.days,
                max_results_sec=args.max_results,
                max_clusters=args.max_clusters,
                parallel_workers=args.parallel,
                progress_callback=progress,
                errors_list=errors,
            )
        except Exception as e:
            print(f"ERRORE: {e}", file=sys.stderr)
            _write_progress(PROGRESS_FILE, f"ERRORE: {e}", append=True)
            sys.exit(1)

    from massive_backtest.strategy_improver import build_improvement_report

    report = build_report(
        df_results,
        ranking,
        errors,
        out_path=out_path,
        strategy_10k_budget=args.budget_usd,
        strategy_10k_lookback_days=args.lookback_days,
        strategy_10k_max_positions=args.max_positions,
        top_strategies_k=args.top_strategies_k,
        prefer_allocation=args.prefer_allocation,
        min_strategy_n=args.min_strategy_n,
        sec_rows=sec_rows,
    )
    enc = getattr(sys.stdout, "encoding", None) or "utf-8"
    try:
        print(report)
    except UnicodeEncodeError:
        print(report.encode(enc, errors="replace").decode(enc))
    print("", file=sys.stderr)
    print(f"Report salvato in: {out_path.resolve()}", file=sys.stderr)

    try:
        build_improvement_report(
            ranking,
            [s.name for s in STRATEGY_DEFINITIONS_UNIFIED],
            out_path=out_dir / f"{base}_IMPROVEMENT.txt",
        )
        print(f"Suggerimenti miglioramento: {(out_dir / f'{base}_IMPROVEMENT.txt').resolve()}", file=sys.stderr)
    except Exception as e:
        print(f"Improvement report non generato: {e}", file=sys.stderr)

    try:
        from strategy_bot import run_bot
        bot_path = run_bot(
            base, root=out_dir, metric_kind="high",
            min_n=args.min_strategy_n,
            top_k=min(5, args.top_strategies_k or 5),
            days_back=7,
        )
        if bot_path:
            print(f"Suggerimenti bot (strategia futura): {bot_path.resolve()}", file=sys.stderr)
    except Exception as e:
        print(f"BOT_SUGGESTIONS non generato: {e}", file=sys.stderr)

    try:
        export_all_xlsx_to_one(out_dir, base)
        all_xlsx_path = out_dir / f"{base}_ALL_XLSX.xlsx"
        if all_xlsx_path.exists():
            print(f"Tutti gli XLSX in un unico file: {all_xlsx_path.resolve()}", file=sys.stderr)
    except Exception as e:
        print(f"ALL_XLSX.xlsx non generato: {e}", file=sys.stderr)

    for stem_tpl, label in OUTPUT_SUMMARY:
        p = out_dir / stem_tpl.format(base=base)
        if p.exists():
            print(f"{label}: {p.resolve()}", file=sys.stderr)
    if errors:
        print(f"Cluster con errori/saltati: {len(errors)}", file=sys.stderr)
    _write_progress(PROGRESS_FILE, "Completato.", append=True)


if __name__ == "__main__":
    main()
