"""
Backtest delle 3 strategie (conservativa, bilanciata, aggressiva) sui dati CSV
max_gain_loss_per_window. Ogni riga = una posizione con max gain % e max loss % per finestra.

Regola: se in finestra sia target che stop sono toccati, si assume stop colpito per primo (conservativo).
Se nessuno dei due è toccato → PnL = 0% (non abbiamo il prezzo a fine finestra).
"""

import pandas as pd
import sys
from pathlib import Path

DEFAULT_CSV = r"c:\Users\mvalvaso\OneDrive - Stryker\Downloads\massive_backtest_max_gain_loss_per_window (3).csv"

# Definizione strategie: (nome, finestra, target %, stop %)
STRATEGIES = [
    # Conservativa: +1.5% / -1.5%, 24h e 48h
    ("Conservativa (24h, +1.5% / -1.5%)", "24h", 1.5, -1.5),
    ("Conservativa (48h, +1.5% / -1.5%)", "48h", 1.5, -1.5),
    ("Conservativa (24h, +2% / -2%)", "24h", 2.0, -2.0),
    ("Conservativa (48h, +2% / -2%)", "48h", 2.0, -2.0),
    # Bilanciata: +3% / -4% a 7d, +5% / -5% a 14d
    ("Bilanciata (7d, +3% / -4%)", "7d", 3.0, -4.0),
    ("Bilanciata (14d, +5% / -5%)", "14d", 5.0, -5.0),
    # Aggressiva: +10% / -10% a 30d e 60d
    ("Aggressiva (30d, +10% / -10%)", "30d", 10.0, -10.0),
    ("Aggressiva (60d, +10% / -10%)", "60d", 10.0, -10.0),
]


def get_gain_loss_col(df: pd.DataFrame, window: str, kind: str) -> str | None:
    """Restituisce il nome colonna per window (es. '24h', '7d') e kind ('gain' o 'loss')."""
    for c in df.columns:
        if window in c and kind in c and "max" in c and "%" in c:
            return c
    return None


def backtest_strategy(
    df: pd.DataFrame,
    window: str,
    target_pct: float,
    stop_pct: float,
    assume_target_first_when_both: bool = False,
) -> pd.Series:
    """
    Per ogni riga: regola dipende da assume_target_first_when_both.
    - Se False (default, conservativo): stop colpito per primo → se max_loss <= stop allora PnL=stop; else se max_gain >= target allora PnL=target; else 0.
    - Se True (ottimistico): target colpito per primo → se max_gain >= target allora PnL=target; else se max_loss <= stop allora PnL=stop; else 0.
    """
    col_gain = get_gain_loss_col(df, window, "gain")
    col_loss = get_gain_loss_col(df, window, "loss")
    if not col_gain or not col_loss:
        return pd.Series(dtype=float)
    gain = pd.to_numeric(df[col_gain], errors="coerce")
    loss = pd.to_numeric(df[col_loss], errors="coerce")
    pnl = pd.Series(0.0, index=df.index)
    hit_stop = loss <= stop_pct
    hit_target = gain >= target_pct
    if assume_target_first_when_both:
        pnl[hit_target] = target_pct
        pnl[(~hit_target) & hit_stop] = stop_pct
    else:
        pnl[hit_stop] = stop_pct
        pnl[(~hit_stop) & hit_target] = target_pct
    return pnl


def summary_stats(pnl: pd.Series) -> dict:
    """Statistiche su una serie di PnL %."""
    n = len(pnl)
    wins = (pnl > 0).sum()
    losses = (pnl < 0).sum()
    neutral = (pnl == 0).sum()
    win_rate = (wins / n * 100) if n else 0
    avg_pnl = pnl.mean()
    total_pnl = pnl.sum()
    median_pnl = pnl.median()
    return {
        "N": n,
        "Wins": int(wins),
        "Losses": int(losses),
        "Neutral": int(neutral),
        "Win_rate_%": round(win_rate, 1),
        "Avg_PnL_%": round(avg_pnl, 2),
        "Total_PnL_%": round(total_pnl, 2),
        "Median_PnL_%": round(median_pnl, 2),
    }


def run_all(csv_path: str, assume_target_first: bool = False) -> pd.DataFrame:
    """Esegue il backtest di tutte le strategie e restituisce una tabella riepilogativa."""
    df = pd.read_csv(csv_path)
    rows = []
    for name, window, target, stop in STRATEGIES:
        pnl = backtest_strategy(df, window, target, stop, assume_target_first_when_both=assume_target_first)
        if pnl.empty:
            rows.append({"Strategia": name, **{k: None for k in ["N", "Wins", "Losses", "Neutral", "Win_rate_%", "Avg_PnL_%", "Total_PnL_%", "Median_PnL_%"]}})
            continue
        stats = summary_stats(pnl)
        rows.append({"Strategia": name, **stats})
    return pd.DataFrame(rows)


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CSV
    path = Path(csv_path)
    if not path.exists():
        print(f"File non trovato: {csv_path}")
        print("Uso: python backtest_strategies.py [percorso_file.csv]")
        sys.exit(1)

    script_dir = Path(__file__).resolve().parent
    result_stop_first = run_all(csv_path, assume_target_first=False)
    result_target_first = run_all(csv_path, assume_target_first=True)
    out_txt = script_dir / "BACKTEST_STRATEGIE_REPORT.txt"

    lines = []
    lines.append("=" * 72)
    lines.append("  BACKTEST STRATEGIE - Risultati su dati CSV (max gain/loss per finestra)")
    lines.append("=" * 72)
    lines.append("")
    lines.append("--- SCENARIO A: Stop colpito per primo (quando entrambi target e stop toccati) ---")
    lines.append("    Interpretazione conservativa: in caso di ambiguita' si conta la perdita.")
    lines.append("")
    lines.append(result_stop_first.to_string(index=False))
    lines.append("")
    lines.append("--- SCENARIO B: Target colpito per primo (quando entrambi toccati) ---")
    lines.append("    Interpretazione ottimistica: in caso di ambiguita' si conta il gain.")
    lines.append("")
    lines.append(result_target_first.to_string(index=False))
    lines.append("")
    lines.append("--- NOTE ---")
    lines.append("  Neutral = posizioni in cui ne' target ne' stop sono stati toccati (PnL = 0%).")
    lines.append("  Lo scenario reale sara' tra A e B a seconda dell'ordine di esecuzione dei prezzi.")
    lines.append("")
    lines.append("=" * 72)

    report = "\n".join(lines)
    print(report)
    out_txt.write_text(report, encoding="utf-8")
    print("\nReport salvato in: {}".format(out_txt.resolve()))

    # Salva anche CSV dei risultati (scenario conservativo come default)
    out_csv = script_dir / "BACKTEST_STRATEGIE_RISULTATI.csv"
    result_stop_first.to_csv(out_csv, index=False)
    print("Risultati CSV (scenario stop first) salvati in: {}".format(out_csv.resolve()))


if __name__ == "__main__":
    main()
