"""
Estrae dal report testuale STRATEGY_AGENT_REPORT.txt i risultati in CSV e Markdown
(formato apribile in Excel, condivisibile, leggibile).
Uso: python export_strategy_report.py [STRATEGY_AGENT_REPORT.txt]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def parse_report_table(content: str) -> list[dict]:
    """Estrae la tabella 'TUTTE LE STRATEGIE' dal report (pandas to_string)."""
    lines = content.splitlines()
    start = None
    for i, line in enumerate(lines):
        if "TUTTE LE STRATEGIE" in line and "---" in line:
            start = i + 2  # dopo la riga vuota e l'header
            break
    if start is None:
        return []
    # Header: Strategia, Descrizione, Hold, N, Win_rate_%, ...
    header = "Strategia Descrizione Hold N Win_rate_% Avg_ret_% Median_ret_% Total_ret_% Std_% Sharpe_approx Min_% Max_%".split()
    rows = []
    for line in lines[start:]:
        if line.strip().startswith("=") or not line.strip():
            break
        # Split per 2+ spazi: prima parte = "Strategia — hold Hold", seconda = Descrizione, poi N, Win_rate, ...
        parts = re.split(r"\s{2,}", line.strip())
        if len(parts) < 11:
            continue
        # Ultimi 9: N, Win_rate_%, Avg_ret_%, Median_ret_%, Total_ret_%, Std_%, Sharpe_approx, Min_%, Max_%
        try:
            n = int(parts[-9].replace(",", ""))
        except (ValueError, IndexError):
            continue
        # parts[0] = "Nome strategia — hold ret_high_30d_news", parts[1] = Descrizione
        if " — hold " in parts[0]:
            strategia, hold = parts[0].split(" — hold ", 1)
            strategia, hold = strategia.strip(), hold.strip()
        else:
            strategia, hold = parts[0].strip(), ""
        descrizione = parts[1].strip() if len(parts) > 2 else ""
        try:
            win = float(parts[-8].replace(",", "."))
            avg = float(parts[-7].replace(",", "."))
            med = float(parts[-6].replace(",", "."))
            tot = float(parts[-5].replace(",", "."))
            std = float(parts[-4].replace(",", "."))
            sharpe_val = parts[-3].strip()
            sharpe = float(sharpe_val.replace(",", ".")) if sharpe_val and sharpe_val not in ("None", "") else None
            mn = float(parts[-2].replace(",", "."))
            mx = float(parts[-1].replace(",", "."))
        except (ValueError, IndexError):
            continue
        rows.append({
            "Strategia": strategia,
            "Descrizione": descrizione,
            "Hold": hold,
            "N": n,
            "Win_rate_%": win,
            "Avg_ret_%": avg,
            "Median_ret_%": med,
            "Total_ret_%": tot,
            "Std_%": std,
            "Sharpe_approx": sharpe,
            "Min_%": mn,
            "Max_%": mx,
        })
    return rows


def main():
    report_path = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "STRATEGY_AGENT_REPORT.txt"
    if not report_path.is_file():
        print(f"File non trovato: {report_path}", file=sys.stderr)
        sys.exit(1)
    content = report_path.read_text(encoding="utf-8")
    rows = parse_report_table(content)
    if not rows:
        print("Nessuna riga estratta dal report.", file=sys.stderr)
        sys.exit(1)
    out_dir = report_path.parent
    csv_path = out_dir / "STRATEGY_AGENT_RANKING.csv"
    md_path = out_dir / "STRATEGY_AGENT_STRATEGIES.md"
    # CSV (separatore ; per Excel italiano)
    import csv
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(rows)
    print(f"CSV salvato: {csv_path}")
    # Markdown: tutte le strategie
    md_lines = [
        "# Agente strategie SEC — Tutte le strategie",
        "",
        "| # | Strategia | N | Win_rate_% | Avg_ret_% | Total_ret_% | Sharpe |",
        "|---|-----------|---|------------|-----------|-------------|-------|",
    ]
    for i, r in enumerate(rows, 1):
        md_lines.append(
            f"| {i} | {r['Strategia']} | {r['N']} | {r['Win_rate_%']} | {r['Avg_ret_%']} | {r['Total_ret_%']} | {r.get('Sharpe_approx', '')} |"
        )
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"Markdown salvato: {md_path}")


if __name__ == "__main__":
    main()
