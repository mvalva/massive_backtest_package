"""
Modulo di auto-miglioramento: analizza il ranking delle strategie e suggerisce
nuove strategie da testare (es. combinazioni con analisi tecnica, ruoli, valore).
Non modifica automaticamente STRATEGY_DEFINITIONS: produce un report di suggerimenti
che l'utente può usare per aggiungere strategie al prossimo run.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import pandas as pd


def _normalize_strategy_name(name: str) -> str:
    """Nome strategia normalizzato per confronto (senza 'hold ret_...')."""
    return re.sub(r"\s*—\s*hold\s+ret_[^\s]+", "", name).strip()


def analyze_ranking(ranking: list[dict] | pd.DataFrame) -> dict[str, Any]:
    """
    Analizza il ranking: quali hold_key e quali 'temi' (CEO, CFO, RSI, Value, ecc.)
    compaiono di più nelle top strategie.
    Ritorna un dict con statistiche e liste utili per i suggerimenti.
    """
    if isinstance(ranking, pd.DataFrame):
        ranking = ranking.to_dict("records")
    if not ranking:
        return {"top_hold_keys": [], "top_themes": [], "top_n": [], "suggestions": []}

    top_n = min(50, len(ranking))
    top = ranking[:top_n]

    # Frequenza hold_key nelle top
    hold_counts: dict[str, int] = {}
    for r in top:
        h = r.get("Hold") or ""
        if h:
            hold_counts[h] = hold_counts.get(h, 0) + 1
    top_hold_keys = sorted(hold_counts.keys(), key=lambda x: -hold_counts[x])[:15]

    # Temi dalle strategie (keyword nelle prime 50)
    theme_counts: dict[str, int] = {}
    keywords = [
        "CEO", "CFO", "Director", "10% Owner", "Position +10%", "Position +20%", "Position +30%",
        "Value ≥100k", "Value ≥500k", "RSI oversold", "RSI overbought", "Price > MA50", "Price < MA50",
        "Price > MA200", "Small cap", "Near 52w", "Far 52w", "Multiple buys", "CEO+CFO", "combo",
    ]
    for r in top:
        name = (r.get("Strategia") or "").lower()
        for kw in keywords:
            if kw.lower() in name:
                theme_counts[kw] = theme_counts.get(kw, 0) + 1
    top_themes = sorted(theme_counts.keys(), key=lambda x: -theme_counts[x])[:20]

    return {
        "top_hold_keys": top_hold_keys,
        "hold_counts": hold_counts,
        "top_themes": top_themes,
        "theme_counts": theme_counts,
        "top_n": top_n,
        "avg_ret_top10": sum((r.get("Avg_ret_%") or 0) for r in top[:10]) / 10 if top else 0,
    }


def suggest_new_strategies(
    ranking: list[dict] | pd.DataFrame,
    current_strategy_names: list[str],
) -> list[dict[str, str]]:
    """
    Suggerisce nuove strategie da aggiungere: combinazioni che appaiono
    spesso nelle top ma che potrebbero non essere ancora coperte (es. aggiungere TA
    a strategie già forti).
    Ritorna lista di dict con chiavi: name_suggestion, description, reason.
    """
    analysis = analyze_ranking(ranking)
    current_normalized = {_normalize_strategy_name(n) for n in current_strategy_names}
    suggestions = []

    # Suggerimento 1: se ret_high_30d_open/news domina, suggerire anche ret_low per bilanciare
    hold_keys = analysis.get("top_hold_keys", [])
    high_30 = [h for h in hold_keys if "ret_high_30d" in h]
    if high_30 and not any("ret_low_30d" in h for h in hold_keys[:5]):
        suggestions.append({
            "name_suggestion": "Confronta anche ret_low_30d (worst case) per le stesse strategie",
            "description": "Le top strategie usano ret_high (best case). Valuta ret_low per rischio.",
            "reason": "Diversificare metriche (best vs worst case).",
        })

    # Suggerimento 2: se molte top hanno CEO/CFO ma poche hanno RSI, suggerire RSI + CEO/CFO
    themes = analysis.get("theme_counts", {})
    has_ceo_cfo = (themes.get("CEO", 0) + themes.get("CFO", 0) + themes.get("CEO+CFO", 0)) >= 3
    has_rsi = (themes.get("RSI oversold", 0) + themes.get("RSI overbought", 0)) >= 1
    if has_ceo_cfo and not has_rsi:
        suggestions.append({
            "name_suggestion": "RSI oversold + CEO only / CFO only (già presenti) + altre combo RSI + ruolo",
            "description": "Aggiungi filtri TA (RSI, MA) alle strategie ruolo per vedere se migliorano.",
            "reason": "Top strategie sono ruolo-based; TA non presente nelle top → prova combinazioni.",
        })

    # Suggerimento 3: Price > MA200 + best role
    if themes.get("Price > MA50", 0) >= 1 and themes.get("Price > MA200", 0) == 0:
        suggestions.append({
            "name_suggestion": "Price > MA200 + CEO/CFO o + Position +10%",
            "description": "Trend lungo (sopra MA200) + insider buying.",
            "reason": "MA200 usato meno di MA50; può filtrare trend più stabili.",
        })

    # Suggerimento 4: da top 5, proporre variante TA (RSI) per una strategia già presente e senza RSI/MA
    if isinstance(ranking, pd.DataFrame):
        ranking = ranking.to_dict("records")
    for r in (ranking or [])[:5]:
        name = r.get("Strategia") or ""
        if "RSI" not in name and "MA" not in name:
            base = _normalize_strategy_name(name)
            if base and base in current_normalized:
                suggestions.append({
                    "name_suggestion": f"Variante TA: '{base}' + RSI oversold",
                    "description": f"La strategia '{base}' è in top; prova ad aggiungere filtro RSI < 30.",
                    "reason": "Aggiungere analisi tecnica a strategie già performanti.",
                })
                break  # uno solo

    return suggestions[:8]  # max 8 suggerimenti


def build_improvement_report(
    ranking: list[dict] | pd.DataFrame,
    current_strategy_names: list[str],
    out_path: Path | None = None,
) -> str:
    """
    Genera un report di miglioramento: analisi del ranking + suggerimenti.
    Se out_path è fornito, salva il report su file.
    """
    analysis = analyze_ranking(ranking)
    suggestions = suggest_new_strategies(ranking, current_strategy_names)

    lines = []
    lines.append("=" * 70)
    lines.append("  AGENTE STRATEGIE — Report di auto-miglioramento")
    lines.append("=" * 70)
    lines.append("")
    lines.append("--- ANALISI TOP STRATEGIE ---")
    lines.append("")
    lines.append("Hold key più presenti nelle top 50:")
    for h in analysis.get("top_hold_keys", [])[:10]:
        cnt = analysis.get("hold_counts", {}).get(h, 0)
        lines.append(f"  {h}: {cnt} volte")
    lines.append("")
    lines.append("Temi ricorrenti (keyword nei nomi):")
    for t in analysis.get("top_themes", [])[:12]:
        cnt = analysis.get("theme_counts", {}).get(t, 0)
        lines.append(f"  {t}: {cnt} volte")
    lines.append("")
    lines.append("--- SUGGERIMENTI PER NUOVE STRATEGIE ---")
    lines.append("")
    if not suggestions:
        lines.append("Nessun suggerimento automatico. Le strategie coperte sono già ampie.")
    else:
        for i, s in enumerate(suggestions, 1):
            lines.append(f"{i}. {s.get('name_suggestion', '')}")
            lines.append(f"   Motivo: {s.get('reason', '')}")
            lines.append(f"   Descrizione: {s.get('description', '')}")
            lines.append("")
    lines.append("=" * 70)
    report = "\n".join(lines)
    if out_path:
        out_path.write_text(report, encoding="utf-8")
    return report
