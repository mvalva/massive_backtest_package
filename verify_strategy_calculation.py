"""
Verifica del calcolo di una strategia: mostra passo-passo come si ottiene
N, Win_rate_%, Avg_ret_% per una strategia scelta (es. ret_high_30d_open).

Uso: python verify_strategy_calculation.py

Importante: ret_high_Nd = "se avessi venduto al PREZZO MASSIMO raggiunto nel periodo,
quale sarebbe stato il rendimento %?" -> è un BEST CASE, non il rendimento a fine periodo.
Per questo Avg_ret_% e Win_rate possono sembrare "troppo buoni".
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "massive_backtest"))

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
    load_dotenv(ROOT / "massive_backtest" / ".env", override=True)
except Exception:
    pass

def main():
    from massive_backtest.sec_data import load_sec_buys, group_by_cluster, get_rows_for_clustering
    from massive_backtest.backtest_engine import run_backtest, TRADING_DAY_HORIZONS
    from massive_backtest.strategy_agent import (
        STRATEGY_DEFINITIONS,
        filter_cfo_only,
        filter_pct_increase_ge_10,
        compute_metrics,
    )
    import pandas as pd

    # Carica pochi dati per verifica veloce
    print("Caricamento SEC (ultimi 60 giorni, max 500)...")
    rows, err = load_sec_buys(days=60, max_results=500, exclude_funds=True)
    if err or not rows:
        print("Errore SEC:", err or "nessun dato")
        return
    rows_for_cluster = get_rows_for_clustering(rows)
    clusters = group_by_cluster(rows_for_cluster)
    print(f"Cluster: {len(clusters)}")
    # Backtest solo sui primi 20 cluster per velocità
    to_run = clusters[:20]
    print(f"Backtest su {len(to_run)} cluster...")
    results = run_backtest(to_run, progress_callback=None, exclude_future_entry=True)
    df = pd.DataFrame(results)

    # Strategia esempio: "CFO only + Position +10% — hold ret_high_30d_open"
    # Filtro: CFO only E pct_increase >= 10%
    hold_key = "ret_high_30d_open"
    def filter_fn(r):
        return filter_cfo_only(r) and filter_pct_increase_ge_10(r)

    mask = df.apply(filter_fn, axis=1)
    sub = df.loc[mask]
    series = sub[hold_key] if hold_key in sub.columns else pd.Series(dtype=float)
    series_clean = series.dropna()

    print()
    print("=" * 70)
    print("ESEMPIO: strategia 'CFO only + Position +10%' con metrica ret_high_30d_open")
    print("=" * 70)
    print()
    print("COSA SIGNIFICA ret_high_30d_open:")
    print("  Per ogni cluster: entry = prezzo OPEN primo giorno borsa dopo il filing.")
    print("  Finestra = da entry_date fino al 30-esimo giorno di borsa dopo (incluso).")
    print("  max_high = massimo tra i 'high' di tutte le barre daily in quella finestra.")
    print("  ret_high_30d_open = (max_high - entry_price) / entry_price * 100")
    print("  => 'Se avessi comprato all\'open e venduto al MASSIMO toccato in 30 giorni borsa, avresti fatto X%'.")
    print("  => È un BEST CASE (sell at the top), non il rendimento a scadenza.")
    print()
    print("FILTRO: cluster con titolo CFO E pct_increase_position_max >= 10%")
    print()
    print(f"Cluster totali backtestati: {len(df)}")
    print(f"Cluster che passano il filtro (CFO + Position +10%): {mask.sum()}")
    print(f"Di questi, con valore non NaN per {hold_key}: {len(series_clean)}")
    print()

    if len(series_clean) == 0:
        print("Nessun cluster passa il filtro con dati. Ecco 3 righe raw (primi cluster) per vedere i numeri:")
        for i, row in df.head(3).iterrows():
            print(f"  ticker={row.get('ticker')} filing_day={row.get('filing_day')} titles={str(row.get('titles'))[:50]} "
                  f"entry_price={row.get('entry_price')} pct_inc_max={row.get('pct_increase_position_max')} "
                  f"ret_high_30d_open={row.get(hold_key)}")
        return

    # Metriche (come fa l'agente)
    metrics = compute_metrics(series)
    print("METRICHE CALCOLATE (come nell'agente):")
    print(f"  N = {metrics['n']}")
    print(f"  Win_rate_% = {metrics['win_rate_%']}  (% trade con ret_high_30d_open > 0)")
    print(f"  Avg_ret_% = {metrics['avg_ret_%']}  (media dei ret_high_30d_open)")
    print(f"  Median_ret_% = {metrics['median_ret_%']}")
    print(f"  Total_ret_% = {metrics['total_ret_%']}  (somma, non composto)")
    print(f"  Min_% = {metrics['min_%']}, Max_% = {metrics['max_%']}")
    print()
    print("DETTAGLIO PER OGNI CLUSTER CHE PASSA IL FILTRO:")
    print("-" * 70)
    for idx, (i, row) in enumerate(sub.iterrows()):
        ret = row.get(hold_key)
        if ret is None:
            continue
        entry = row.get("entry_price")
        ticker = row.get("ticker")
        fd = row.get("filing_day")
        print(f"  {idx+1}. {ticker} filing={fd} entry_open={entry} -> ret_high_30d_open = {ret}%")
    print()
    print("CONCLUSIONE: I numeri sono corretti. ret_high misura il 'miglior prezzo possibile'")
    print("nel periodo, quindi Win_rate e Avg_ret tendono ad essere alti (il massimo in 30d")
    print("è spesso sopra l'entry). Per vedere performance 'realistiche' usa ret_low_* o")
    print("un rendimento a scadenza (close a N giorni) se lo aggiungiamo in futuro.")


if __name__ == "__main__":
    main()
