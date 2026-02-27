"""
Analisi acquisti insider: filtri APPLICABILI A ENTRY (no lookahead), percentili, significatività statistica.
- Filtri ret_4h sono LOOKAHEAD: non usabili per acquisti futuri (ret_4h si conosce solo dopo 4h)
- Filtri percentili: value top 25%, value/market_cap, ecc.
- Min n=20 per filtri "actionabili" (n<15 = rumore)
"""

from __future__ import annotations

try:
    import pandas as pd
except ImportError:
    pd = None

# Filtri basati su ret_4h/ret_24h = LOOKAHEAD (non applicabili all'entry)
LOOKAHEAD_PREFIXES = ("ret_4h", "ret_24h", "ret_48h")

MIN_N_ACTIONABLE = 20  # sotto questa soglia = bassa confidenza


def _is_entry_time_filter(name: str) -> bool:
    """True se il filtro è applicabile al momento dell'acquisto (no lookahead)."""
    n = (name or "").lower()
    return not any(n.startswith(p) or p in n for p in ("ret_4h", "ret_24h", "ret_48h"))


def compute_win_rate(df: "pd.DataFrame", return_col: str) -> dict:
    """Win rate e metriche per return_col."""
    if pd is None or df is None or df.empty or return_col not in df.columns:
        return {}
    valid = df[df[return_col].notna()].copy()
    if len(valid) == 0:
        return {}
    rets = pd.to_numeric(valid[return_col], errors="coerce").dropna()
    if len(rets) == 0:
        return {}
    n = len(rets)
    n_winners = (rets > 0).sum()
    std_val = float(rets.std()) if len(rets) > 1 else 0.0
    return {
        "n": n,
        "n_winners": int(n_winners),
        "n_losers": int(n - n_winners),
        "win_rate_pct": round(100 * n_winners / n, 1),
        "avg_ret": round(float(rets.mean()), 2),
        "median_ret": round(float(rets.median()), 2),
        "std_ret": round(std_val, 2),
        "min_ret": round(float(rets.min()), 2),
        "max_ret": round(float(rets.max()), 2),
    }


def compute_base_summary(df: "pd.DataFrame") -> dict:
    """
    Statistiche BASE per ogni orizzonte e dataset. Per tabella dati base prima dell'analisi AI.
    """
    if pd is None or df is None or df.empty:
        return {"error": "DataFrame vuoto."}
    ret_cols = [c for c in ["ret_4h", "ret_24h", "ret_48h", "ret_5d", "ret_7d", "ret_10d", "ret_14d", "ret_30d"] if c in df.columns]
    if not ret_cols:
        return {"error": "Nessuna colonna ret_*."}

    rows = []
    for rc in ret_cols:
        m = compute_win_rate(df, rc)
        if m:
            rows.append({
                "Orizzonte": rc,
                "n": m["n"],
                "Win %": m["win_rate_pct"],
                "Vincitori": m["n_winners"],
                "Perdenti": m["n_losers"],
                "Avg %": m["avg_ret"],
                "Mediana %": m["median_ret"],
                "Std %": m.get("std_ret"),
                "Min %": m.get("min_ret"),
                "Max %": m.get("max_ret"),
            })

    # Summary dataset
    summary = {"tot_righe": len(df)}
    if "value_tot" in df.columns:
        vt = pd.to_numeric(df["value_tot"], errors="coerce").dropna()
        if len(vt) > 0:
            summary["value_mediana"] = round(float(vt.median()), 0)
            summary["value_p75"] = round(float(vt.quantile(0.75)), 0)
            summary["value_p25"] = round(float(vt.quantile(0.25)), 0)
    if "market_cap" in df.columns:
        mc = pd.to_numeric(df["market_cap"], errors="coerce").dropna()
        mc = mc[mc > 0]
        if len(mc) > 0:
            summary["mcap_mediana_M"] = round(float(mc.median()) / 1e6, 1)
    if "titles" in df.columns:
        has_titles = df["titles"].fillna("").str.strip() != ""
        summary["pct_con_titles"] = round(100 * has_titles.sum() / len(df), 1) if len(df) > 0 else 0
        for t in ["CEO", "CFO", "Director", "Officer"]:
            cnt = df["titles"].fillna("").str.contains(t, case=False, na=False).sum()
            summary[f"n_{t}"] = int(cnt)

    # Win rate per ruolo (dato base, usa ret_7d)
    role_analysis = {}
    if "titles" in df.columns and ret_cols:
        ref_col = "ret_7d" if "ret_7d" in ret_cols else ret_cols[0]
        if ref_col in df.columns:
            for title in ["CEO", "CFO", "Director", "10% Owner", "President", "Chairman", "Officer"]:
                sub = df[df["titles"].fillna("").str.contains(title, case=False, na=False)]
                m = compute_win_rate(sub, ref_col)
                if m and m.get("n", 0) >= 2:
                    role_analysis[title] = m

    return {"base_table": rows, "summary": summary, "role_analysis": role_analysis}


def _build_multi_factor_combinations(
    valid: "pd.DataFrame",
    wr,
    min_sample: int,
) -> list[dict]:
    """
    Genera combinazioni 3–8 variabili da building blocks.
    Una sola condizione per famiglia (no value>=100k + value>=250k).
    Molti spezzoni per value, volume, pct_52w, ecc.
    """
    import itertools
    # blocks_by_family: una sola scelta per famiglia per combo
    blocks_by_family: dict[str, list[tuple[str, "pd.Series"]]] = {}

    # Ruoli
    if "titles" in valid.columns:
        roles = []
        for t in ["CEO", "CFO", "Director", "President", "Chairman", "Officer", "10% Owner"]:
            m = valid["titles"].fillna("").str.contains(t, case=False, na=False)
            if m.sum() >= min_sample:
                roles.append((f"Ruolo:{t}", m))
        if roles:
            blocks_by_family["role"] = roles

    # Value: molti spezzoni (25k–3M)
    vt = pd.to_numeric(valid["value_tot"], errors="coerce") if "value_tot" in valid.columns else None
    if vt is not None:
        value_threshs = [
            (25_000, "25k"), (50_000, "50k"), (75_000, "75k"), (100_000, "100k"),
            (125_000, "125k"), (150_000, "150k"), (175_000, "175k"), (200_000, "200k"),
            (250_000, "250k"), (300_000, "300k"), (350_000, "350k"), (400_000, "400k"),
            (500_000, "500k"), (600_000, "600k"), (750_000, "750k"), (1_000_000, "1M"),
            (1_250_000, "1.25M"), (1_500_000, "1.5M"), (2_000_000, "2M"), (2_500_000, "2.5M"), (3_000_000, "3M"),
        ]
        vals = [(f"value>={lab}", vt >= thresh) for thresh, lab in value_threshs if (vt >= thresh).sum() >= min_sample]
        if vals:
            blocks_by_family["value"] = vals

    # Market cap
    mc = pd.to_numeric(valid["market_cap"], errors="coerce") if "market_cap" in valid.columns else None
    if mc is not None:
        mcap_ranges = [
            (0, 300e6, "<300M"), (0, 500e6, "<500M"), (300e6, 1e9, "300M-1B"),
            (500e6, 1e9, "500M-1B"), (1e9, 5e9, "1B-5B"), (5e9, 50e9, "5B-50B"),
            (50e9, 1e15, ">50B"), (0, 5e9, "<5B"), (0, 1e9, "<1B"),
        ]
        mcaps = []
        for low, high, lab in mcap_ranges:
            m = (mc >= low) & (mc < high) if high < 1e15 else (mc >= low)
            if m.sum() >= min_sample:
                mcaps.append((f"mcap:{lab}", m))
        if mcaps:
            blocks_by_family["mcap"] = mcaps

    # pct_from_52w_high
    pct = pd.to_numeric(valid["pct_from_52w_high"], errors="coerce") if "pct_from_52w_high" in valid.columns else None
    if pct is not None:
        pct_threshs = [0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50]
        pcts = [(f"pct52w>={t}%", pct >= t) for t in pct_threshs if (pct >= t).sum() >= min_sample]
        if pcts:
            blocks_by_family["pct52w"] = pcts

    # Volume
    ve = pd.to_numeric(valid["volume_entry"], errors="coerce") if "volume_entry" in valid.columns else None
    if ve is not None:
        vol_threshs = [
            (25_000, "25k"), (50_000, "50k"), (75_000, "75k"), (100_000, "100k"),
            (150_000, "150k"), (200_000, "200k"), (250_000, "250k"), (300_000, "300k"),
            (500_000, "500k"), (750_000, "750k"), (1_000_000, "1M"),
        ]
        vols = [(f"vol>={lab}", ve >= thresh) for thresh, lab in vol_threshs if (ve >= thresh).sum() >= min_sample]
        if vols:
            blocks_by_family["volume"] = vols

    # n_buys
    nb = pd.to_numeric(valid["n_buys"], errors="coerce") if "n_buys" in valid.columns else None
    if nb is not None:
        nbs = [(f"n_buys>={n}", nb >= n) for n in [2, 3, 4, 5, 6, 7] if (nb >= n).sum() >= min_sample]
        if nbs:
            blocks_by_family["n_buys"] = nbs

    # value/market_cap
    if vt is not None and mc is not None:
        ratio = vt / mc.replace(0, pd.NA)
        val_mcap_pcts = [0.0005, 0.001, 0.0015, 0.002, 0.0025, 0.005, 0.0075, 0.01, 0.015, 0.02, 0.025, 0.03]
        valmcaps = [(f"val/mcap>={p*100:.2f}%", ratio >= p) for p in val_mcap_pcts if (ratio >= p).sum() >= min_sample]
        if valmcaps:
            blocks_by_family["val_mcap"] = valmcaps

    # range_pct_entry
    rp = pd.to_numeric(valid["range_pct_entry"], errors="coerce") if "range_pct_entry" in valid.columns else None
    if rp is not None:
        range_buckets = [(0, 1), (1, 2), (2, 3), (3, 5), (5, 10), (10, 20), (20, 50)]
        rps = []
        for lo, hi in range_buckets:
            m = (rp >= lo) & (rp < hi)
            if m.sum() >= min_sample:
                rps.append((f"range{lo}-{hi}%", m))
        if rps:
            blocks_by_family["range"] = rps

    # primary_exchange
    if "primary_exchange" in valid.columns:
        exs = []
        for ex in valid["primary_exchange"].dropna().unique()[:10]:
            if ex:
                m = valid["primary_exchange"] == ex
                if m.sum() >= min_sample:
                    exs.append((f"ex:{ex}", m))
        if exs:
            blocks_by_family["exchange"] = exs

    # sic_description (settore)
    if "sic_description" in valid.columns:
        sics = []
        for sic in valid["sic_description"].dropna().unique()[:12]:
            if sic and len(str(sic)) > 2:
                m = valid["sic_description"] == sic
                if m.sum() >= min_sample:
                    sics.append((f"settore:{str(sic)[:25]}", m))
        if sics:
            blocks_by_family["settore"] = sics

    families = list(blocks_by_family.keys())
    if len(families) < 3:
        return []

    out: list[dict] = []
    seen: set[str] = set()
    max_combos_per_k = 8000
    max_total = 200

    for k in range(3, min(9, len(families) + 1)):
        for fam_combo in itertools.combinations(families, k):
            blocks_list = [blocks_by_family[f] for f in fam_combo]
            count = 0
            for block_combo in itertools.product(*blocks_list):
                if count >= max_combos_per_k:
                    break
                count += 1
                names = [b[0] for b in block_combo]
                key = "+".join(sorted(names))
                if key in seen:
                    continue
                mask = block_combo[0][1]
                for _, m in block_combo[1:]:
                    mask = mask & m
                if mask.sum() < min_sample:
                    continue
                seen.add(key)
                sub = valid[mask]
                res = wr(sub)
                if res:
                    out.append({"filter_name": " + ".join(names), "is_entry_filter": True, **res})
                    if len(out) >= max_total:
                        break
            if len(out) >= max_total:
                break
        if len(out) >= max_total:
            break

    out.sort(key=lambda x: (x.get("win_rate_pct", 0), x.get("n", 0), x.get("avg_ret", 0)), reverse=True)
    return out[:150]


def test_filter_combinations(
    df: "pd.DataFrame",
    return_col: str,
    min_sample: int = 5,
) -> list[dict]:
    """
    Filtri APPLICABILI A ENTRY + filtri lookahead (separati).
    Esclude: value>0, n_buys>=1 (banali).
    Aggiunge: percentili, value/market_cap.
    """
    if pd is None or df is None or df.empty or return_col not in df.columns:
        return []
    valid = df[df[return_col].notna()].copy()
    if len(valid) < min_sample:
        return []

    def wr(sub: "pd.DataFrame") -> dict | None:
        if sub is None or len(sub) < min_sample:
            return None
        m = compute_win_rate(sub, return_col)
        return m if m.get("n", 0) >= min_sample else None

    results: list[dict] = []
    if (m := wr(valid)):
        results.append({"filter_name": "Tutti", "is_entry_filter": True, **m})

    # --- Ruolo insider ---
    if "titles" in valid.columns:
        for title in ["CEO", "CFO", "Director", "10% Owner", "President", "Chairman", "Officer"]:
            sub = valid[valid["titles"].fillna("").str.contains(title, case=False, na=False)]
            if (m := wr(sub)):
                results.append({"filter_name": f"Ruolo: {title}", "is_entry_filter": True, **m})

    # --- Value: percentili (non soglie arbitrarie) ---
    if "value_tot" in valid.columns:
        vt = pd.to_numeric(valid["value_tot"], errors="coerce").dropna()
        if len(vt) >= 10:
            q75 = vt.quantile(0.75)
            q50 = vt.quantile(0.5)
            q25 = vt.quantile(0.25)
            for label, thresh in [("value top 25%", q75), ("value top 50%", q50), ("value top 75%", q25)]:
                if thresh > 0 and (m := wr(valid[pd.to_numeric(valid["value_tot"], errors="coerce") >= thresh])):
                    results.append({"filter_name": label, "is_entry_filter": True, **m})
        for thresh in [25_000, 50_000, 75_000, 100_000, 150_000, 200_000, 250_000, 300_000, 400_000, 500_000, 750_000, 1_000_000, 1_500_000, 2_000_000]:
            sub = valid[pd.to_numeric(valid["value_tot"], errors="coerce") >= thresh]
            if len(sub) >= min_sample and (m := wr(sub)):
                lab = f"{thresh/1000:.0f}k" if thresh < 1e6 else f"{thresh/1e6:.1f}M"
                results.append({"filter_name": f"value >= ${lab}", "is_entry_filter": True, **m})

    # --- value / market_cap (rapporto significativo) ---
    if "value_tot" in valid.columns and "market_cap" in valid.columns:
        vt = pd.to_numeric(valid["value_tot"], errors="coerce")
        mc = pd.to_numeric(valid["market_cap"], errors="coerce").replace(0, pd.NA)
        ratio = vt / mc
        for pct in [0.0005, 0.001, 0.0015, 0.002, 0.0025, 0.005, 0.0075, 0.01, 0.015, 0.02, 0.025, 0.03]:
            sub = valid[ratio >= pct]
            if len(sub) >= min_sample and (m := wr(sub)):
                results.append({"filter_name": f"value/mcap >= {pct*100:.2f}%", "is_entry_filter": True, **m})

    # --- n_buys: solo >=2 (>=1 è banale) ---
    if "n_buys" in valid.columns:
        nb = pd.to_numeric(valid["n_buys"], errors="coerce")
        for n in [2, 3, 4, 5, 6, 7]:
            if (m := wr(valid[nb >= n])):
                results.append({"filter_name": f"n_buys >= {n}", "is_entry_filter": True, **m})

    # --- market_cap ---
    if "market_cap" in valid.columns:
        mc = pd.to_numeric(valid["market_cap"], errors="coerce")
        for low, high, label in [
            (0, 500e6, "mcap < $500M"),
            (500e6, 5e9, "mcap $500M-$5B"),
            (5e9, 50e9, "mcap $5B-$50B"),
            (50e9, 1e15, "mcap >= $50B"),
        ]:
            if (m := wr(valid[(mc >= low) & (mc < high)])):
                results.append({"filter_name": label, "is_entry_filter": True, **m})

    # --- pct_from_52w_high ---
    if "pct_from_52w_high" in valid.columns:
        pct = pd.to_numeric(valid["pct_from_52w_high"], errors="coerce")
        for thresh in [0, -5, -10, -15, -20, -25, -30, -35, -40, -45, -50]:
            if (m := wr(valid[pct >= thresh])):
                results.append({"filter_name": f"pct_52w >= {thresh}%", "is_entry_filter": True, **m})

    # --- volume_entry ---
    if "volume_entry" in valid.columns:
        ve = pd.to_numeric(valid["volume_entry"], errors="coerce")
        for thresh in [25_000, 50_000, 75_000, 100_000, 150_000, 200_000, 250_000, 500_000, 750_000, 1_000_000]:
            if (m := wr(valid[ve >= thresh])):
                lab = f"{thresh/1000:.0f}k" if thresh < 1e6 else f"{thresh/1e6:.0f}M"
                results.append({"filter_name": f"volume >= {lab}", "is_entry_filter": True, **m})

    # --- range_pct_entry ---
    if "range_pct_entry" in valid.columns:
        rp = pd.to_numeric(valid["range_pct_entry"], errors="coerce")
        for low, high in [(0, 1), (1, 2), (2, 3), (3, 5), (5, 10), (10, 20), (20, 50), (50, 100)]:
            if (m := wr(valid[(rp >= low) & (rp < high)])):
                results.append({"filter_name": f"range_pct {low}-{high}%", "is_entry_filter": True, **m})

    # --- exchange, settore ---
    if "primary_exchange" in valid.columns:
        for ex in valid["primary_exchange"].dropna().unique()[:6]:
            if ex and (m := wr(valid[valid["primary_exchange"] == ex])):
                results.append({"filter_name": f"Exchange: {ex}", "is_entry_filter": True, **m})
    if "sic_description" in valid.columns:
        for sic in valid["sic_description"].dropna().unique()[:8]:
            if sic and len(str(sic)) > 2 and (m := wr(valid[valid["sic_description"] == sic])):
                results.append({"filter_name": f"Settore: {str(sic)[:35]}", "is_entry_filter": True, **m})

    # --- Combinazioni ruolo + value ---
    if "titles" in valid.columns and "value_tot" in valid.columns:
        vt = pd.to_numeric(valid["value_tot"], errors="coerce")
        for title in ["CEO", "CFO", "Director"]:
            sub = valid[
                valid["titles"].fillna("").str.contains(title, case=False, na=False)
                & (vt >= 250_000)
            ]
            if (m := wr(sub)):
                results.append({"filter_name": f"{title} + value >= $250k", "is_entry_filter": True, **m})

    # --- Combinazioni ruolo + market_cap ---
    if "titles" in valid.columns and "market_cap" in valid.columns:
        mc = pd.to_numeric(valid["market_cap"], errors="coerce")
        for title in ["CEO", "CFO", "Director"]:
            sub = valid[
                valid["titles"].fillna("").str.contains(title, case=False, na=False)
                & (mc > 0) & (mc < 5e9)
            ]
            if len(sub) >= min_sample and (m := wr(sub)):
                results.append({"filter_name": f"{title} + mcap < $5B", "is_entry_filter": True, **m})

    # --- Combinazioni pct_52w + value (oversold + buy significativo) ---
    if "pct_from_52w_high" in valid.columns and "value_tot" in valid.columns:
        pct = pd.to_numeric(valid["pct_from_52w_high"], errors="coerce")
        vt = pd.to_numeric(valid["value_tot"], errors="coerce")
        for pct_thresh in [-20, -30]:
            sub = valid[(pct >= pct_thresh) & (vt >= 100_000)]
            if len(sub) >= min_sample and (m := wr(sub)):
                results.append({"filter_name": f"pct_52w>={pct_thresh}% + value>=100k", "is_entry_filter": True, **m})

    # --- Combinazioni 3–6 variabili (building blocks) ---
    multi_results = _build_multi_factor_combinations(valid, wr, min_sample)
    results.extend(multi_results)

    # --- Filtri LOOKAHEAD (solo per analisi strategia hold, NON per entry) ---
    if "ret_4h" in valid.columns and return_col != "ret_4h":
        r4 = pd.to_numeric(valid["ret_4h"], errors="coerce")
        if (m := wr(valid[r4 > 0])):
            results.append({"filter_name": "ret_4h>0 (lookahead)", "is_entry_filter": False, **m})
        if (m := wr(valid[r4 < 0])):
            results.append({"filter_name": "ret_4h<0 (lookahead)", "is_entry_filter": False, **m})

    results.sort(key=lambda x: (x.get("win_rate_pct", 0), x.get("avg_ret", 0)), reverse=True)
    return results


def run_full_analysis(df: "pd.DataFrame") -> dict:
    """
    Analisi completa. best_predictive_combo = solo filtri ENTRY (no lookahead).
    Preferisce n >= MIN_N_ACTIONABLE per significatività statistica.
    """
    if pd is None or df is None or df.empty:
        return {"error": "DataFrame vuoto."}
    ret_cols = [c for c in df.columns if c.startswith("ret_") and c in df.columns]
    ret_cols = [c for c in ["ret_4h", "ret_24h", "ret_48h", "ret_5d", "ret_7d", "ret_10d", "ret_14d", "ret_30d"] if c in ret_cols]
    if not ret_cols:
        return {"error": "Nessuna colonna ret_* con dati."}

    per_ret: dict = {}
    all_best: list[dict] = []
    entry_only: list[dict] = []

    for rc in ret_cols:
        overall = compute_win_rate(df, rc)
        if not overall or overall.get("n", 0) < 5:
            continue
        filters = test_filter_combinations(df, rc, min_sample=5)
        best = filters[0] if filters else None
        best_entry = next((f for f in filters if f.get("is_entry_filter", True) and f.get("filter_name") != "Tutti"), None)
        per_ret[rc] = {
            "overall": overall,
            "best_filter": best,
            "best_entry_filter": best_entry,
            "all_filters": filters[:20],
        }
        for f in filters:
            if f.get("filter_name") == "Tutti":
                continue
            rec = {
                "return_col": rc,
                "filter_name": f["filter_name"],
                "win_rate_pct": f["win_rate_pct"],
                "n": f["n"],
                "avg_ret": f["avg_ret"],
                "base_win_rate": overall["win_rate_pct"],
                "edge": f["win_rate_pct"] - overall["win_rate_pct"],
                "is_entry_filter": f.get("is_entry_filter", True),
            }
            all_best.append(rec)
            if rec["is_entry_filter"]:
                entry_only.append(rec)

    # Miglior combinazione ENTRY (applicabile a acquisti futuri), preferendo n>=20
    def score_entry(e):
        n = e.get("n", 0)
        wr = e.get("win_rate_pct", 0)
        edge = e.get("edge", 0)
        conf = 1 if n >= MIN_N_ACTIONABLE else 0.5
        return (conf * wr, edge, n)

    best_predictive = max(entry_only, key=score_entry) if entry_only else None

    # Ruolo insider
    role_analysis: dict = {}
    if "titles" in df.columns:
        ref_col = "ret_7d" if "ret_7d" in ret_cols else (ret_cols[0] if ret_cols else None)
        if ref_col and ref_col in df.columns:
            for title in ["CEO", "CFO", "Director", "10% Owner", "President", "Chairman", "Officer"]:
                sub = df[df["titles"].fillna("").str.contains(title, case=False, na=False)]
                m = compute_win_rate(sub, ref_col)
                if m and m.get("n", 0) >= 2:
                    role_analysis[title] = m

    return {
        "per_ret": per_ret,
        "best_predictive_combo": best_predictive,
        "all_best": sorted(all_best, key=lambda x: (-x["is_entry_filter"], x["win_rate_pct"], x["edge"]), reverse=True),
        "entry_filters": sorted(entry_only, key=lambda x: (x["win_rate_pct"], x["edge"]), reverse=True),
        "role_analysis": role_analysis,
    }


def get_ai_agent_analysis(df: "pd.DataFrame", full_analysis: dict) -> str | None:
    """
    AI: criteri APPLICABILI A ENTRY. Vietato raccomandare ret_4h come filtro entry (lookahead).
    Evitare filtri banali. Evidenziare significatività statistica (n>=20).
    """
    import os
    key = os.getenv("OPENAI_API_KEY", "").strip()
    if not key:
        return None
    try:
        import openai
    except ImportError:
        return None

    per_ret = full_analysis.get("per_ret", {})
    best_combo = full_analysis.get("best_predictive_combo", {})
    role_analysis = full_analysis.get("role_analysis", {})
    entry_filters = full_analysis.get("entry_filters", [])

    base = compute_base_summary(df)
    base_table = base.get("base_table", [])
    summary = base.get("summary", {})

    lines = [f"Dataset: {len(df)} righe. Colonne: {', '.join(c for c in df.columns if c not in ('insiders','company'))}"]
    lines.append("")
    lines.append("=== DATI BASE (statistiche per orizzonte) ===")
    for r in base_table:
        lines.append(f"  {r.get('Orizzonte','')}: n={r.get('n',0)}, Win%={r.get('Win %',0)}, Avg%={r.get('Avg %',0)}, Mediana%={r.get('Mediana %','')}, Std%={r.get('Std %','')}, Min%={r.get('Min %','')}, Max%={r.get('Max %','')}")
    lines.append("")
    lines.append("=== SUMMARY DATASET ===")
    v = summary.get("value_mediana")
    lines.append(f"  Value mediana: ${v:,.0f}" if v is not None and v > 0 else "  Value: (nessun dato)")
    m = summary.get("mcap_mediana_M")
    lines.append(f"  Mcap mediana: {m}M" if m is not None else "  Mcap: (nessun dato)")
    lines.append(f"  % righe con titles: {summary.get('pct_con_titles',0)}%" if summary.get("pct_con_titles") is not None else "  Titles: (nessun dato)")
    lines.append(f"  Ruoli: CEO={summary.get('n_CEO',0)}, CFO={summary.get('n_CFO',0)}, Director={summary.get('n_Director',0)}, Officer={summary.get('n_Officer',0)}")
    lines.append("")
    lines.append("=== WIN RATE BASE (per orizzonte) ===")
    for rc, data in per_ret.items():
        o = data.get("overall", {})
        lines.append(f"  {rc}: {o.get('win_rate_pct',0)}% (n={o.get('n',0)}, avg {o.get('avg_ret',0)}%)")
    lines.append("")
    lines.append("=== RUOLO INSIDER (titles) ===")
    if role_analysis:
        for title, m in sorted(role_analysis.items(), key=lambda x: -x[1].get("win_rate_pct", 0)):
            lines.append(f"  {title}: {m.get('win_rate_pct',0)}% (n={m.get('n',0)})")
    else:
        lines.append("  (nessun dato)")
    lines.append("")
    lines.append("=== FILTRI APPLICABILI A ENTRY (no lookahead) — Top per win rate ===")
    for x in entry_filters[:10]:
        conf = "✓" if x.get("n", 0) >= MIN_N_ACTIONABLE else "⚠ bassa confidenza"
        lines.append(f"  {x.get('filter_name','')} @ {x.get('return_col','')}: {x.get('win_rate_pct',0)}% (n={x.get('n',0)}) {conf}")
    if best_combo:
        lines.append("")
        lines.append(f"MIGLIOR FILTRO ENTRY: {best_combo.get('filter_name','')} @ {best_combo.get('return_col','')} -> {best_combo.get('win_rate_pct',0)}% (n={best_combo.get('n',0)})")

    context = "\n".join(lines)

    system_prompt = """Sei un analista quantitativo per acquisti insider (Form 4, P).

REGOLE CRITICHE:
1. **NO LOOKAHEAD**: ret_4h, ret_24h NON sono noti all'entry. NON raccomandare mai "se ret_4h>0" come filtro per acquisti futuri. È un bias.
2. **Significatività**: n<20 = rumore, non segnale. Evidenzia quando un filtro ha campione troppo piccolo.
3. **NO filtri banali**: value>0, n_buys>=1 sono inutili (tutti i dati li soddisfano).
4. **Filtri utili**: ruolo (CEO/CFO/Director), value percentili, value/market_cap, market_cap, pct_52w, volume.

COMPITI:
- Quale RUOLO ha edge reale (con n sufficiente)?
- Quali filtri ENTRY (value, mcap, ruolo) sono statisticamente significativi?
- Quale timeframe (ret_7d, ret_14d...) è più prevedibile?
- Criteri CONCRETI per acquisti futuri: cosa filtrare, soglie, cosa evitare.

Risposta operativa: 5-7 punti. Max 300 parole."""

    user_prompt = f"""Dati backtest:

{context}

Analisi: filtri applicabili a entry, ruolo, significatività. Criteri concreti per acquisti futuri."""

    try:
        client = openai.OpenAI(api_key=key)
        r = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=700,
        )
        if r.choices:
            return (r.choices[0].message.content or "").strip()
    except Exception:
        pass
    return None


def analyze_patterns(df: "pd.DataFrame", return_col: str) -> dict:
    """Analisi su singola colonna (backward compat)."""
    if return_col not in df.columns:
        return {"error": f"Colonna {return_col} non presente."}
    valid = df[df[return_col].notna()]
    if len(valid) < 5:
        return {"error": "Troppe poche righe."}
    overall = compute_win_rate(df, return_col)
    filter_results = test_filter_combinations(df, return_col, min_sample=5)
    best = filter_results[0] if filter_results else None
    summary = [
        f"Win rate ({return_col}): {overall.get('win_rate_pct',0)}% (n={overall.get('n',0)})",
        f"Rendimento medio: {overall.get('avg_ret',0)}%",
    ]
    if best:
        summary.append(f"Miglior filtro: {best['filter_name']} -> {best['win_rate_pct']}%")
    return {
        "overall_metrics": overall,
        "filter_results": filter_results,
        "summary_lines": summary,
    }


def get_llm_summary_if_available(summary_dict: dict, return_col: str) -> str | None:
    return None


def analyze_winners(df: "pd.DataFrame", return_col: str = "ret_7d", top_pct: float = 25.0) -> dict:
    out = analyze_patterns(df, return_col)
    if out:
        out["winners_df"] = pd.DataFrame()
        out["title_counts"] = {}
    return out
