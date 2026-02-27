"""
Analisi delle performance medie (gain/loss) per finestra temporale
dal CSV del backtest max_gain_loss_per_window.
Ignora le colonne date; elabora solo le colonne % gain e % loss.
"""

import pandas as pd
import sys
from pathlib import Path

# Percorso default del CSV (Downloads)
DEFAULT_CSV = r"c:\Users\mvalvaso\OneDrive - Stryker\Downloads\massive_backtest_max_gain_loss_per_window (3).csv"

GAIN_THRESHOLDS = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
LOSS_THRESHOLDS = [-0.5, -1, -1.5, -2, -2.5, -3, -3.5, -4, -4.5, -5, -5.5, -6, -6.5, -7, -7.5, -8, -8.5, -9, -9.5, -10]
WINDOWS = ["24h", "48h", "5d", "7d", "14d", "30d", "60d"]


def get_gain_loss_columns(df: pd.DataFrame) -> list[str]:
    """Estrae i nomi delle colonne che sono 'max gain %' o 'max loss %' (per ogni finestra)."""
    return [c for c in df.columns if "max gain %" in c or "max loss %" in c]


def analyze(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    cols = get_gain_loss_columns(df)
    if not cols:
        raise ValueError("Nessuna colonna 'max gain %' o 'max loss %' trovata nel CSV.")
    # Forza numerico, coercendo errori a NaN
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    stats = df[cols].agg(["mean", "median", "min", "max", "std", "count"]).round(4)
    return stats


def build_report(csv_path: str) -> str:
    """Genera il report completo in formato testo chiaro."""
    df = pd.read_csv(csv_path)
    gain_cols = [c for c in df.columns if "max gain %" in c]
    loss_cols = [c for c in df.columns if "max loss %" in c]
    for c in gain_cols + loss_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    n = len(df)
    stats = df[get_gain_loss_columns(df)].agg(["mean", "median", "min", "max", "std", "count"]).round(4)

    lines = []
    lines.append("=" * 72)
    lines.append("  REPORT ANALISI - Max gain/loss per finestra (file: {})".format(Path(csv_path).name))
    lines.append("=" * 72)
    lines.append("")
    lines.append("Posizioni analizzate: {}".format(n))
    lines.append("")
    lines.append("--- 1. Riepilogo per finestra (media max gain % | media max loss %) ---")
    lines.append("")
    for w in WINDOWS:
        g = [c for c in gain_cols if w in c]
        l = [c for c in loss_cols if w in c]
        if g and l:
            avg_g = df[g[0]].mean()
            avg_l = df[l[0]].mean()
            lines.append("  {:>4}   avg max gain: {:>7.2f}%   |   avg max loss: {:>7.2f}%".format(w, avg_g, avg_l))
    lines.append("")
    lines.append("--- 2. Statistiche per colonna (mean, median, min, max, std, count) ---")
    lines.append("")
    pd.set_option("display.width", 200)
    pd.set_option("display.max_columns", 30)
    lines.append(stats.to_string())
    lines.append("")
    lines.append("--- 3. Percentuale aggregata GAIN (% di tutte le posizioni con max gain >= soglia, per lasso) ---")
    lines.append("     Ogni colonna = lasso temporale; ogni riga = soglia. Valori in %.")
    lines.append("")
    gain_pct_rows = []
    for t in GAIN_THRESHOLDS:
        row = {"Soglia": f"{t}%" if t < 10 else "10%+"}
        for w in WINDOWS:
            g = [c for c in gain_cols if w in c]
            if g:
                row[w] = round((df[g[0]] >= t).sum() / n * 100, 1)
        gain_pct_rows.append(row)
    lines.append(pd.DataFrame(gain_pct_rows).to_string(index=False))
    lines.append("")
    lines.append("--- 4. Percentuale aggregata LOSS (% di tutte le posizioni con max loss <= soglia, per lasso) ---")
    lines.append("     Ogni colonna = lasso temporale; ogni riga = soglia. Valori in %.")
    lines.append("")
    loss_pct_rows = []
    for t in LOSS_THRESHOLDS:
        row = {"Soglia": f"{t}%" if t > -10 else "-10%+"}
        for w in WINDOWS:
            l = [c for c in loss_cols if w in c]
            if l:
                row[w] = round((df[l[0]] <= t).sum() / n * 100, 1)
        loss_pct_rows.append(row)
    lines.append(pd.DataFrame(loss_pct_rows).to_string(index=False))
    lines.append("")
    lines.append("=" * 72)
    lines.append("  Fine report")
    lines.append("=" * 72)
    return "\n".join(lines)


def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CSV
    out_path = None
    if len(sys.argv) >= 3 and sys.argv[1] == "-o":
        out_path = sys.argv[2]
        csv_path = sys.argv[3] if len(sys.argv) > 3 else DEFAULT_CSV
    elif len(sys.argv) >= 2 and not sys.argv[1].startswith("-"):
        csv_path = sys.argv[1]
    path = Path(csv_path)
    if not path.exists():
        print(f"File non trovato: {csv_path}")
        print("Uso: python analyze_backtest_csv.py [percorso_file.csv]")
        print("     python analyze_backtest_csv.py -o report.txt [percorso_file.csv]")
        sys.exit(1)

    report_text = build_report(csv_path)
    print(report_text)

    if out_path:
        Path(out_path).write_text(report_text, encoding="utf-8")
        print("\nReport salvato in: {}".format(Path(out_path).resolve()))
    else:
        # Salva nella cartella dello script (progetto) per evitare permessi in altre cartelle
        script_dir = Path(__file__).resolve().parent
        default_report = script_dir / "ANALISI_CSV_REPORT.txt"
        default_report.write_text(report_text, encoding="utf-8")
        print("\nReport salvato in: {}".format(default_report.resolve()))


if __name__ == "__main__":
    main()
