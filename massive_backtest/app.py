"""
Massive Backtest — Lettura dati base.
- Caricamento SEC (Form 4, P) + backtest Massive.com.
- Solo dati di lettura base: riepilogo per orizzonte, metriche dataset, win rate per ruolo.
Esegui dalla root: streamlit run massive_backtest/app.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from dotenv import load_dotenv
    load_dotenv(ROOT / ".env")
    load_dotenv(Path(__file__).resolve().parent / ".env", override=True)
except Exception:
    pass

import pandas as pd
import streamlit as st

try:
    from massive_backtest.sec_data import load_sec_buys, group_by_cluster, get_rows_for_clustering
    from massive_backtest.backtest_engine import run_backtest
    from massive_backtest.ai_analysis import compute_base_summary
except ImportError:
    from sec_data import load_sec_buys, group_by_cluster, get_rows_for_clustering
    from backtest_engine import run_backtest
    from ai_analysis import compute_base_summary

TIME_RANGES = [
    ("Ultimi 10 giorni", 10, 200),
    ("Ultimi 30 giorni", 30, 500),
    ("Ultimi 6 mesi", 182, 3000),
    ("Ultimo anno", 365, 5000),
    ("Ultimi 2 anni", 730, 10_000),
    ("Ultimi 3 anni", 1095, 15_000),
]


# Soglie per % posizioni: gain >= 1%, 1.5%, ... 10%, 10%+ ; loss <= -1%, ... -10%, -10%+
GAIN_THRESHOLDS = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
LOSS_THRESHOLDS = [-0.5, -1, -1.5, -2, -2.5, -3, -3.5, -4, -4.5, -5, -5.5, -6, -6.5, -7, -7.5, -8, -8.5, -9, -9.5, -10]
WINDOWS = ["24h", "48h", "5d", "7d", "14d", "30d", "60d"]


def _ensure_strategy_scores(rank_df: pd.DataFrame) -> pd.DataFrame:
    """
    Garantisce la presenza delle colonne Score_strategy e Ranking_strategy nel ranking,
    ricalcolandole se mancanti a partire da Avg_ret_% e Win_rate_% medi per Strategia.
    """
    if rank_df.empty:
        return rank_df
    if "Score_strategy" in rank_df.columns and "Ranking_strategy" in rank_df.columns:
        return rank_df
    if "Strategia" not in rank_df.columns or "Avg_ret_%" not in rank_df.columns or "Win_rate_%" not in rank_df.columns:
        return rank_df
    agg = rank_df.groupby("Strategia", dropna=False).agg(
        mean_avg_ret=("Avg_ret_%", "mean"),
        mean_win_rate=("Win_rate_%", "mean"),
    ).reset_index()
    if agg.empty:
        return rank_df
    r_min, r_max = agg["mean_avg_ret"].min(), agg["mean_avg_ret"].max()
    w_min, w_max = agg["mean_win_rate"].min(), agg["mean_win_rate"].max()
    if (r_max - r_min) != 0:
        norm_ret = (agg["mean_avg_ret"] - r_min) / (r_max - r_min)
    else:
        norm_ret = 0.5
    if (w_max - w_min) != 0:
        norm_win = (agg["mean_win_rate"] - w_min) / (w_max - w_min)
    else:
        norm_win = 0.5
    agg["_score"] = 0.5 * norm_ret + 0.5 * norm_win
    agg = agg.sort_values("_score", ascending=False)
    strat_to_rank = {s: i for i, s in enumerate(agg["Strategia"], 1)}
    strat_to_score = dict(zip(agg["Strategia"], (agg["_score"] * 100).round(2)))
    out = rank_df.copy()
    out["Ranking_strategy"] = out["Strategia"].map(strat_to_rank)
    out["Score_strategy"] = out["Strategia"].map(strat_to_score)
    return out


def _load_allowed_users() -> set[str]:
    """
    Carica la lista di email autorizzate ad accedere all'explorer strategie.
    - Variabile d'ambiente ALLOWED_USERS: lista separata da virgole.
    - File ROOT / ALLOWED_USERS.txt: una email per riga (righe che iniziano con # ignorate).
    Se la lista risultante è vuota, nessuna restrizione viene applicata (accesso libero).
    """
    allowed: set[str] = set()
    # Da env (es. "a@example.com,b@example.com")
    raw_env = os.getenv("ALLOWED_USERS", "")
    if raw_env:
        for part in raw_env.split(","):
            email = part.strip().lower()
            if email:
                allowed.add(email)
    # Da file ALLOWED_USERS.txt, una email per riga
    txt_path = ROOT / "ALLOWED_USERS.txt"
    if txt_path.exists():
        try:
            for line in txt_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                allowed.add(line.lower())
        except OSError:
            # In caso di errore di lettura, ignoriamo il file e procediamo solo con l'env
            pass
    return allowed


def _require_login_for_explorer() -> str | None:
    """
    Richiede inserimento email e verifica contro la allowlist.
    Restituisce l'email normalizzata se autorizzata.
    Se la allowlist è vuota, non applica restrizioni e ritorna None.
    """
    allowed = _load_allowed_users()
    if not allowed:
        # Nessuna restrizione configurata: accesso libero
        return None
    email = st.text_input("Email (per accesso all'explorer strategie)", key="explorer_email")
    if not email:
        st.info("Inserisci la tua email per accedere all'explorer strategie (lista utenti invitati).")
        st.stop()
    email_norm = email.strip().lower()
    if email_norm not in allowed:
        st.error("Email non autorizzata. Contatta l'amministratore per essere aggiunto alla lista ALLOWED_USERS.")
        st.stop()
    return email_norm


def get_gain_loss_columns(df: pd.DataFrame) -> list[str]:
    """Colonne 'max gain %' e 'max loss %' per finestra."""
    return [c for c in df.columns if "max gain %" in c or "max loss %" in c]


def analyze_csv_gain_loss(df: pd.DataFrame) -> tuple[pd.DataFrame, list[dict], pd.DataFrame, pd.DataFrame]:
    """Analisi performance: stats, riepilogo, % posizioni per soglia gain, % posizioni per soglia loss."""
    cols = get_gain_loss_columns(df)
    if not cols:
        raise ValueError("Nessuna colonna 'max gain %' o 'max loss %' trovata nel CSV.")
    for c in cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    stats = df[cols].agg(["mean", "median", "min", "max", "std", "count"]).round(4)
    gain_cols = [c for c in df.columns if "max gain %" in c]
    loss_cols = [c for c in df.columns if "max loss %" in c]
    summary = []
    for w in WINDOWS:
        g = [c for c in gain_cols if w in c]
        l = [c for c in loss_cols if w in c]
        if g and l:
            summary.append({
                "Finestra": w,
                "Avg max gain %": round(df[g[0]].mean(), 2),
                "Avg max loss %": round(df[l[0]].mean(), 2),
            })

    n = len(df)
    # % posizioni con max gain >= soglia (per ogni finestra)
    gain_pct_rows = []
    for t in GAIN_THRESHOLDS:
        row = {"Soglia": f"{t}%" if t < 10 else "10%+"}
        for w in WINDOWS:
            g = [c for c in gain_cols if w in c]
            if g:
                pct = (df[g[0]] >= t).sum() / n * 100 if n else 0
                row[w] = round(pct, 1)
        gain_pct_rows.append(row)
    gain_pct_df = pd.DataFrame(gain_pct_rows)

    # % posizioni con max loss <= soglia (es. <= -1% = almeno 1% di perdita)
    loss_pct_rows = []
    for t in LOSS_THRESHOLDS:
        row = {"Soglia": f"{t}%" if t > -10 else "-10%+"}
        for w in WINDOWS:
            l = [c for c in loss_cols if w in c]
            if l:
                pct = (df[l[0]] <= t).sum() / n * 100 if n else 0
                row[w] = round(pct, 1)
        loss_pct_rows.append(row)
    loss_pct_df = pd.DataFrame(loss_pct_rows)

    return stats, summary, gain_pct_df, loss_pct_df


def main():
    st.set_page_config(page_title="Massive Backtest — Dati base", layout="wide")
    st.title("Massive Backtest — Dati di lettura base")
    st.caption("Caricamento SEC (Form 4, acquisti P) + prezzi Massive. Statistiche per orizzonte e ruoli, senza filtri.")
    st.caption("↑ Usa la tab **Analisi CSV gain/loss** (a destra) per caricare un CSV e vedere le performance medie per finestra.")

    tab_backtest, tab_csv, tab_agent, tab_explorer = st.tabs(
        ["Backtest e dati base", "Analisi CSV gain/loss", "Agente strategie", "Explorer strategie SEC"]
    )

    with tab_backtest:
        if not os.getenv("MASSIVE_API_KEY"):
            st.error("MASSIVE_API_KEY non impostata. Aggiungila nel file .env (root o massive_backtest/).")
        elif not os.getenv("SEC_API_KEY"):
            st.error("SEC_API_KEY non impostata. Aggiungila nel file .env nella root del progetto.")
        else:
            _render_backtest_tab()
        if not (os.getenv("MASSIVE_API_KEY") and os.getenv("SEC_API_KEY")):
            st.info("Vai alla tab **Analisi CSV gain/loss** per caricare un CSV e vedere le performance medie per finestra.")

    with tab_csv:
        _render_csv_analysis_tab()

    with tab_agent:
        _render_strategy_agent_tab()

    with tab_explorer:
        _render_strategy_explorer_tab()


def _render_strategy_agent_tab() -> None:
    st.subheader("Agente strategie SEC — risultati da output esistenti")
    st.caption(
        "Questa vista NON lancia una nuova run né chiama le API. "
        "Usa i file già generati (CASES/RANKING/ERRORS) come database: ideale per l'app online."
    )
    try:
        from massive_backtest.strategy_agent import (
            build_report, build_cases_report, build_tickers_report, build_10k_strategy,
            STRATEGY_10K_BUDGET, STRATEGY_10K_LOOKBACK_DAYS, STRATEGY_10K_MAX_POSITIONS,
        )
    except ImportError:
        from strategy_agent import (
            build_report, build_cases_report, build_tickers_report, build_10k_strategy,
            STRATEGY_10K_BUDGET, STRATEGY_10K_LOOKBACK_DAYS, STRATEGY_10K_MAX_POSITIONS,
        )
    base = st.text_input("Prefisso base dei file output", value="STRATEGY_AGENT", key="agent_base_prefix")
    if not base:
        return

    out_dir = ROOT
    cases_path = out_dir / f"{base}_CASES.csv"
    ranking_path = out_dir / f"{base}_RANKING.csv"
    errors_path = out_dir / f"{base}_ERRORS.csv"

    if not cases_path.exists() or not ranking_path.exists():
        st.error(
            f"Non trovo i file necessari nella root del progetto per il prefisso '{base}'.\n\n"
            f"Richiesti: {base}_CASES.csv e {base}_RANKING.csv (opzionale: {base}_ERRORS.csv).\n"
            "Esegui una run dell'agente da riga di comando, poi ricarica questa pagina."
        )
        return

    if st.button("Carica risultati da CSV esistenti", type="primary", key="load_agent_outputs_btn"):
        try:
            df_results = pd.read_csv(cases_path, sep=";", encoding="utf-8-sig", low_memory=False)
        except Exception as e:
            st.error(f"Errore lettura {cases_path.name}: {type(e).__name__}: {e}")
            return
        try:
            ranking_df = pd.read_csv(ranking_path, sep=";", encoding="utf-8-sig", low_memory=False)
        except Exception as e:
            st.error(f"Errore lettura {ranking_path.name}: {type(e).__name__}: {e}")
            return

        ranking_df = _ensure_strategy_scores(ranking_df)
        errors_list: list[dict] = []
        if errors_path.exists():
            try:
                err_df = pd.read_csv(errors_path, sep=";", encoding="utf-8-sig", low_memory=False)
                errors_list = err_df.to_dict("records") if not err_df.empty else []
            except Exception:
                errors_list = []

        ranking_records = ranking_df.to_dict("records")

        st.success(
            f"Risultati caricati da file: {len(df_results)} cluster in {cases_path.name}, "
            f"{len(ranking_records)} righe in {ranking_path.name}."
        )

        # Costruisci struttura cluster_year per filtri per anno, riusata come in Explorer
        cases_df = df_results.copy()
        if "filing_day" in cases_df.columns:
            cases_df["filing_day"] = pd.to_datetime(cases_df["filing_day"], errors="coerce")
            cases_df["year"] = cases_df["filing_day"].dt.year
        else:
            cases_df["year"] = None
        if "cluster_key" not in cases_df.columns:
            def _mk_cluster_key_agent(row) -> str:
                t = str(row.get("ticker", "")).strip().upper()
                d = str(row.get("filing_day", "") or row.get("filedAt", "")).strip()[:10]
                return f"{t}|{d}" if t and d else ""
            cases_df["cluster_key"] = cases_df.apply(_mk_cluster_key_agent, axis=1)
        cluster_year = dict(zip(cases_df["cluster_key"], cases_df["year"]))

        # Filtri strategie (gli stessi dell'Explorer)
        with st.expander("Filtri strategie", expanded=True):
            dataset_choice = st.radio(
                "Dataset strategie",
                ["Tutte le strategie", "Solo SEC (no analisi tecnica)"],
                horizontal=True,
                key="agent_dataset_choice",
            )
            order_choice = st.radio(
                "Ordina per",
                ["Score (Base_name)", "Score_strategy (Strategia esatta)"],
                horizontal=True,
                key="agent_order_choice",
            )
            cols_top = st.columns(4)
            with cols_top[0]:
                years = sorted([y for y in cases_df["year"].dropna().unique().tolist() if y])
                if years:
                    selected_years = st.multiselect("Anni filing", options=years, default=years, key="agent_years")
                else:
                    selected_years = []
            with cols_top[1]:
                ta_profiles = sorted([p for p in ranking_df.get("TA_profile", pd.Series(dtype=str)).dropna().unique().tolist()])
                if ta_profiles:
                    selected_ta = st.multiselect("Analisi tecnica (TA_profile)", options=ta_profiles, default=ta_profiles, key="agent_ta")
                else:
                    selected_ta = []
            with cols_top[2]:
                news_opts = sorted([n for n in ranking_df.get("News_vs_Open", pd.Series(dtype=str)).dropna().unique().tolist()])
                if news_opts:
                    selected_news = st.multiselect("Entry (News_vs_Open)", options=news_opts, default=news_opts, key="agent_news")
                else:
                    selected_news = []
            with cols_top[3]:
                insider_opts = sorted([i for i in ranking_df.get("Insider_type", pd.Series(dtype=str)).dropna().unique().tolist()])
                if insider_opts:
                    selected_insider = st.multiselect("Tipo insider", options=insider_opts, default=insider_opts, key="agent_insider")
                else:
                    selected_insider = []

            cols_bottom = st.columns(2)
            with cols_bottom[0]:
                base_names = sorted([b for b in ranking_df.get("Base_name", pd.Series(dtype=str)).dropna().unique().tolist()])
                selected_bases = st.multiselect("Macrocategorie (Base_name)", options=base_names, default=base_names, key="agent_bases")
            with cols_bottom[1]:
                metric_kinds = sorted([m for m in ranking_df.get("Metric_kind", pd.Series(dtype=str)).dropna().unique().tolist()])
                selected_metric = st.multiselect("Metrica (high/low/mean)", options=metric_kinds, default=metric_kinds, key="agent_metric")

        rank_filtered = ranking_df.copy()

        # SEC only vs tutte
        if dataset_choice.startswith("Solo") and "TA_profile" in rank_filtered.columns:
            rank_filtered = rank_filtered[rank_filtered["TA_profile"] == "SEC only"]

        # Filtro per anno: mantieni solo strategie con almeno un cluster nell'anno selezionato
        if selected_years:
            valid_clusters = {ck for ck, y in cluster_year.items() if y in selected_years}

            def _has_cluster_in_year_agent(clusters_str: str) -> bool:
                if not clusters_str:
                    return False
                for ck in str(clusters_str).split(","):
                    if ck.strip() in valid_clusters:
                        return True
                return False

            if "Clusters_used_N" in rank_filtered.columns:
                rank_filtered = rank_filtered[rank_filtered["Clusters_used_N"].apply(_has_cluster_in_year_agent)]

        if selected_ta and "TA_profile" in rank_filtered.columns:
            rank_filtered = rank_filtered[rank_filtered["TA_profile"].isin(selected_ta)]
        if selected_news and "News_vs_Open" in rank_filtered.columns:
            rank_filtered = rank_filtered[rank_filtered["News_vs_Open"].isin(selected_news)]
        if selected_insider and "Insider_type" in rank_filtered.columns:
            rank_filtered = rank_filtered[rank_filtered["Insider_type"].isin(selected_insider)]
        if selected_bases and "Base_name" in rank_filtered.columns:
            rank_filtered = rank_filtered[rank_filtered["Base_name"].isin(selected_bases)]
        if selected_metric and "Metric_kind" in rank_filtered.columns:
            rank_filtered = rank_filtered[rank_filtered["Metric_kind"].isin(selected_metric)]

        # Ordinamento per Score base_name o Score_strategy
        if order_choice.startswith("Score_strategy") and "Score_strategy" in rank_filtered.columns:
            rank_filtered = rank_filtered.sort_values("Score_strategy", ascending=False)
        elif "Score" in rank_filtered.columns:
            rank_filtered = rank_filtered.sort_values("Score", ascending=False)

        if rank_filtered.empty:
            st.warning("Nessuna strategia soddisfa i filtri selezionati.")
            return

        st.markdown("#### Anteprima strategie (prime 20 dopo filtri)")
        display_cols = [
            "Ranking", "Score", "Ranking_strategy", "Score_strategy",
            "Strategia", "Base_name", "TA_profile", "News_vs_Open", "Insider_type",
            "Metric_kind", "Horizon_days", "Entry_kind", "N", "Win_rate_%", "Avg_ret_%", "Median_ret_%", "Total_ret_%",
        ]
        display_cols = [c for c in display_cols if c in rank_filtered.columns]
        st.dataframe(rank_filtered.head(20)[display_cols], use_container_width=True, hide_index=True)
        st.markdown("#### Tutte le strategie (ranking completo dopo filtri)")
        st.dataframe(rank_filtered[display_cols], use_container_width=True, height=400, hide_index=True)

        report_txt = build_report(df_results, ranking_records, errors_list, out_path=None)
        st.download_button(
            "Scarica report completo", data=report_txt,
            file_name=f"{base}_REPORT.txt", mime="text/plain", key="dl_agent_report"
        )

        st.markdown("---")
        st.markdown("#### Analisi caso per caso (azioni)")
        st.caption("Ogni riga è un cluster (ticker + data filing). Report: **migliori**, **peggiori** e **tutti i casi**; dati completi in CSV.")
        cases_report_md = build_cases_report(df_results, out_path=None, top_n=30, bottom_n=30, include_all=True)
        with st.expander("Report caso per caso (Migliori e Peggiori)", expanded=True):
            st.markdown(cases_report_md)
        col_cases1, col_cases2 = st.columns(2)
        with col_cases1:
            st.download_button(
                "Scarica report caso per caso (MD)",
                data=cases_report_md,
                file_name=f"{base}_CASES_REPORT.md",
                mime="text/markdown",
                key="dl_cases_report",
            )
        with col_cases2:
            st.download_button(
                "Scarica tutti i casi (CSV)",
                data=df_results.to_csv(index=False, sep=";").encode("utf-8-sig"),
                file_name=f"{base}_CASES.csv",
                mime="text/csv",
                key="dl_cases_csv",
            )

        st.markdown("---")
        st.markdown("#### Ogni singolo ticker — Performance e uso nell'analisi")
        tickers_report_md = build_tickers_report(df_results, out_path=None, out_path_csv=None)
        with st.expander("Report per ticker (tutti i ticker con n cluster, ret medio, value tot)", expanded=False):
            st.markdown(tickers_report_md)
        st.download_button(
            "Scarica report ticker (MD)",
            data=tickers_report_md,
            file_name=f"{base}_TICKERS.md",
            mime="text/markdown",
            key="dl_tickers_md",
        )

        st.markdown("---")
        st.markdown("#### Strategia 10k USD — Massimizzare il risultato in un anno")
        strategy_10k_md, positions_10k = build_10k_strategy(
            df_results,
            ranking_records,
            out_path=None,
            out_path_csv=None,
            budget_usd=STRATEGY_10K_BUDGET,
            lookback_days=STRATEGY_10K_LOOKBACK_DAYS,
            max_positions=STRATEGY_10K_MAX_POSITIONS,
            top_strategies_k=10,
        )
        with st.expander("Portfolio simulato 10.000 USD (più strategie testate per finestra)", expanded=True):
            st.markdown(strategy_10k_md)
        col_10k1, col_10k2 = st.columns(2)
        with col_10k1:
            st.download_button(
                "Scarica strategia 10k (MD)",
                data=strategy_10k_md,
                file_name=f"{base}_10K.md",
                mime="text/markdown",
                key="dl_10k_md",
            )
        with col_10k2:
            if positions_10k:
                st.download_button(
                    "Scarica posizioni 10k (CSV)",
                    data=pd.DataFrame(positions_10k).to_csv(index=False, sep=";").encode("utf-8-sig"),
                    file_name=f"{base}_10K.csv",
                    mime="text/csv",
                    key="dl_10k_csv",
                )


def _render_strategy_explorer_tab() -> None:
    """
    Explorer interattivo basato sugli output esistenti (STRATEGY_AGENT_RANKING.csv / STRATEGY_AGENT_CASES.csv).
    Permette:
      - filtri globali (anno, TA_profile, News_vs_Open, Insider_type, Base_name)
      - selezione di una strategia → elenco cluster inclusi
      - selezione di un cluster → dettaglio completo.
    L'accesso può essere limitato tramite ALLOWED_USERS (env o ALLOWED_USERS.txt).
    """
    st.subheader("Explorer strategie SEC (da output esistenti)")
    st.caption(
        "Esplora ranking, strategie e cluster partendo dai file STRATEGY_AGENT_RANKING.csv e STRATEGY_AGENT_CASES.csv "
        "già generati dalla run dell'agente. I filtri modificano le tabelle mostrati e la lista dei cluster."
    )

    # Controllo accesso (lista utenti invitati)
    _require_login_for_explorer()

    base = "STRATEGY_AGENT"
    ranking_path = ROOT / f"{base}_RANKING.csv"
    cases_path = ROOT / f"{base}_CASES.csv"
    if not ranking_path.exists() or not cases_path.exists():
        st.error(
            "Non trovo i file necessari nella root del progetto.\n\n"
            "Assicurati che esistano **STRATEGY_AGENT_RANKING.csv** e **STRATEGY_AGENT_CASES.csv** "
            "nella directory principale (esegui prima `run_strategy_agent.py`)."
        )
        return

    try:
        ranking_df = pd.read_csv(ranking_path, sep=";", encoding="utf-8-sig", low_memory=False)
        cases_df = pd.read_csv(cases_path, sep=";", encoding="utf-8-sig", low_memory=False)
    except Exception as e:
        st.error(f"Errore lettura CSV: {type(e).__name__}: {e}")
        return

    ranking_df = _ensure_strategy_scores(ranking_df)
    # Parsing date e anno filing
    if "filing_day" in cases_df.columns:
        cases_df["filing_day"] = pd.to_datetime(cases_df["filing_day"], errors="coerce")
        cases_df["year"] = cases_df["filing_day"].dt.year
    else:
        cases_df["year"] = None

    # cluster_key per join strategia → cluster
    if "cluster_key" not in cases_df.columns:
        def _mk_cluster_key(row) -> str:
            t = str(row.get("ticker", "")).strip().upper()
            d = str(row.get("filing_day", "") or row.get("filedAt", "")).strip()[:10]
            return f"{t}|{d}" if t and d else ""
        cases_df["cluster_key"] = cases_df.apply(_mk_cluster_key, axis=1)

    # Mappa anni per cluster (usata per filtrare strategie con almeno un cluster nell'anno selezionato)
    cluster_year = dict(zip(cases_df["cluster_key"], cases_df["year"]))

    with st.expander("Filtri globali", expanded=True):
        dataset_choice = st.radio(
            "Dataset strategie",
            ["Tutte le strategie", "Solo SEC (no analisi tecnica)"],
            horizontal=True,
            key="explorer_dataset_choice",
        )
        order_choice = st.radio(
            "Ordina per",
            ["Score (Base_name)", "Score_strategy (Strategia esatta)"],
            horizontal=True,
            key="explorer_order_choice",
        )
        cols_top = st.columns(4)
        # Filtro per anno filing (multi-select)
        with cols_top[0]:
            years = sorted([y for y in cases_df["year"].dropna().unique().tolist() if y])
            if years:
                selected_years = st.multiselect("Anni filing", options=years, default=years)
            else:
                selected_years = []
        # Filtro per profilo TA
        with cols_top[1]:
            ta_profiles = sorted([p for p in ranking_df.get("TA_profile", pd.Series(dtype=str)).dropna().unique().tolist()])
            if ta_profiles:
                selected_ta = st.multiselect("Analisi tecnica (TA_profile)", options=ta_profiles, default=ta_profiles)
            else:
                selected_ta = []
        # Filtro News/Open
        with cols_top[2]:
            news_opts = sorted([n for n in ranking_df.get("News_vs_Open", pd.Series(dtype=str)).dropna().unique().tolist()])
            if news_opts:
                selected_news = st.multiselect("Entry (News_vs_Open)", options=news_opts, default=news_opts)
            else:
                selected_news = []
        # Filtro tipo insider
        with cols_top[3]:
            insider_opts = sorted([i for i in ranking_df.get("Insider_type", pd.Series(dtype=str)).dropna().unique().tolist()])
            if insider_opts:
                selected_insider = st.multiselect("Tipo insider", options=insider_opts, default=insider_opts)
            else:
                selected_insider = []

        cols_bottom = st.columns(2)
        with cols_bottom[0]:
            base_names = sorted([b for b in ranking_df.get("Base_name", pd.Series(dtype=str)).dropna().unique().tolist()])
            selected_bases = st.multiselect("Macrocategorie (Base_name)", options=base_names, default=base_names)
        with cols_bottom[1]:
            metric_kinds = sorted([m for m in ranking_df.get("Metric_kind", pd.Series(dtype=str)).dropna().unique().tolist()])
            selected_metric = st.multiselect("Metrica (high/low/mean)", options=metric_kinds, default=metric_kinds)

    # Applica filtri al ranking
    rank_filtered = ranking_df.copy()

    # SEC only vs tutte
    if dataset_choice.startswith("Solo") and "TA_profile" in rank_filtered.columns:
        rank_filtered = rank_filtered[rank_filtered["TA_profile"] == "SEC only"]

    # Filtro per anno: mantieni solo strategie con almeno un cluster nell'anno selezionato
    if selected_years:
        valid_clusters = {ck for ck, y in cluster_year.items() if y in selected_years}

        def _has_cluster_in_year(clusters_str: str) -> bool:
            if not clusters_str:
                return False
            for ck in str(clusters_str).split(","):
                if ck.strip() in valid_clusters:
                    return True
            return False

        if "Clusters_used_N" in rank_filtered.columns:
            rank_filtered = rank_filtered[rank_filtered["Clusters_used_N"].apply(_has_cluster_in_year)]

    if selected_ta and "TA_profile" in rank_filtered.columns:
        rank_filtered = rank_filtered[rank_filtered["TA_profile"].isin(selected_ta)]
    if selected_news and "News_vs_Open" in rank_filtered.columns:
        rank_filtered = rank_filtered[rank_filtered["News_vs_Open"].isin(selected_news)]
    if selected_insider and "Insider_type" in rank_filtered.columns:
        rank_filtered = rank_filtered[rank_filtered["Insider_type"].isin(selected_insider)]
    if selected_bases and "Base_name" in rank_filtered.columns:
        rank_filtered = rank_filtered[rank_filtered["Base_name"].isin(selected_bases)]
    if selected_metric and "Metric_kind" in rank_filtered.columns:
        rank_filtered = rank_filtered[rank_filtered["Metric_kind"].isin(selected_metric)]

    # Ordinamento per Score / Score_strategy
    if order_choice.startswith("Score_strategy") and "Score_strategy" in rank_filtered.columns:
        rank_filtered = rank_filtered.sort_values("Score_strategy", ascending=False)
    elif "Score" in rank_filtered.columns:
        rank_filtered = rank_filtered.sort_values("Score", ascending=False)

    if rank_filtered.empty:
        st.warning("Nessuna strategia soddisfa i filtri selezionati.")
        return

    st.markdown("#### Ranking strategie (dopo filtri)")
    display_cols = [
        "Ranking", "Score", "Ranking_strategy", "Score_strategy",
        "Strategia", "Base_name", "TA_profile", "News_vs_Open", "Insider_type",
        "Metric_kind", "Horizon_days", "Entry_kind", "N", "Win_rate_%", "Avg_ret_%", "Median_ret_%", "Total_ret_%",
    ]
    display_cols = [c for c in display_cols if c in rank_filtered.columns]
    st.dataframe(rank_filtered[display_cols], use_container_width=True, hide_index=True, height=min(500, 40 + 25 * len(rank_filtered)))

    st.markdown("#### Seleziona una strategia per vedere i cluster inclusi")
    strategy_names = rank_filtered["Strategia"].tolist()
    default_strategy = strategy_names[0] if strategy_names else None
    selected_strategy = st.selectbox("Strategia", options=strategy_names, index=0 if default_strategy else None, key="explorer_strategy")
    if not selected_strategy:
        return

    strat_rows = rank_filtered[rank_filtered["Strategia"] == selected_strategy]
    if strat_rows.empty:
        st.warning("Nessuna riga trovata per la strategia selezionata.")
        return
    strat_row = strat_rows.iloc[0]
    st.caption(f"Base_name: **{strat_row.get('Base_name', '')}** | TA_profile: **{strat_row.get('TA_profile', '')}** | "
               f"Metric: **{strat_row.get('Metric_kind', '')}**, {strat_row.get('Horizon_days', '')}d, entry **{strat_row.get('Entry_kind', '')}**.")

    clusters_str = str(strat_row.get("Clusters_used_N") or strat_row.get("Clusters_used") or "")
    cluster_keys = [ck.strip() for ck in clusters_str.split(",") if ck.strip()]
    if selected_years:
        cluster_keys = [ck for ck in cluster_keys if cluster_year.get(ck) in selected_years]

    if not cluster_keys:
        st.info("Questa strategia non ha cluster nel periodo / con i filtri selezionati.")
        return

    clusters_df = cases_df[cases_df["cluster_key"].isin(cluster_keys)].copy()
    if clusters_df.empty:
        st.info("Nessun cluster trovato nel database per questa strategia e filtri.")
        return

    st.markdown("#### Cluster inclusi nella strategia (filtrati)")
    cluster_display_cols = [
        "cluster_key", "ticker", "filing_day", "filedAt",
        "entry_datetime", "entry_price", "entry_price_news", "entry_price_news_bot", "insider_entry_price",
        "value_usd", "shares", "role", "company", "market_cap",
    ]
    cluster_display_cols = [c for c in cluster_display_cols if c in clusters_df.columns]
    st.dataframe(
        clusters_df[cluster_display_cols].sort_values(["filing_day", "ticker"], ascending=[False, True]),
        use_container_width=True,
        hide_index=True,
        height=min(500, 40 + 25 * len(clusters_df)),
    )

    st.markdown("#### Dettaglio cluster")
    selected_cluster_key = st.selectbox(
        "Scegli un cluster (ticker | data filing)",
        options=clusters_df["cluster_key"].tolist(),
        key="explorer_cluster",
    )
    cluster_detail = clusters_df[clusters_df["cluster_key"] == selected_cluster_key]
    if cluster_detail.empty:
        st.info("Nessun dettaglio trovato per il cluster selezionato.")
        return

    # Mostra tutte le colonne del cluster selezionato (trasposto per leggibilità)
    st.dataframe(cluster_detail.T, use_container_width=True, height=min(600, 25 * len(cluster_detail.columns)))


def _render_csv_analysis_tab() -> None:
    st.subheader("Analisi performance medie (gain/loss) per finestra")
    st.caption("Carica un CSV con colonne tipo «24h max gain %», «24h max loss %», «48h max gain %», … (date escluse).")
    uploaded = st.file_uploader("Carica CSV max gain/loss per finestra", type=["csv"], key="csv_gain_loss")
    if uploaded is None:
        st.info("Carica un file CSV per vedere l’analisi.")
        return
    try:
        df = pd.read_csv(uploaded)
    except Exception as e:
        st.error(f"Errore lettura CSV: {e}")
        return
    cols = get_gain_loss_columns(df)
    if not cols:
        st.error("Nel CSV non risultano colonne «max gain %» o «max loss %». Controlla l’intestazione.")
        return
    try:
        stats_df, summary, gain_pct_df, loss_pct_df = analyze_csv_gain_loss(df)
    except Exception as e:
        st.error(f"Errore analisi: {e}")
        return
    n = len(df)
    st.metric("Righe analizzate (posizioni)", n, "")
    st.caption("Le percentuali sotto sono sempre **aggregate**: % di tutte queste posizioni, per ogni lasso temporale e per ogni soglia.")
    st.markdown("#### Riepilogo per finestra temporale")
    summary_df = pd.DataFrame(summary)
    st.dataframe(summary_df, use_container_width=True, hide_index=True)
    st.markdown("#### Statistiche per colonna (media, mediana, min, max, std, count)")
    st.dataframe(stats_df, use_container_width=True, height=min(280, 80 + 35 * len(stats_df)))

    st.markdown("#### Percentuale aggregata — gain (quante posizioni sono sopra la soglia, per lasso e per %)")
    st.caption(
        f"Ogni cella = **% di tutte le {n} posizioni** che in quel lasso temporale (24h, 48h, …) hanno avuto max gain ≥ soglia. "
        "Es.: «24h» in riga «1%» = percentuale di tutte le posizioni che entro 24h sono state almeno +1%."
    )
    st.dataframe(gain_pct_df, use_container_width=True, hide_index=True, height=min(420, 80 + 25 * len(gain_pct_df)))
    st.markdown("#### Percentuale aggregata — loss (quante posizioni sono sotto la soglia, per lasso e per %)")
    st.caption(
        f"Ogni cella = **% di tutte le {n} posizioni** che in quel lasso temporale hanno avuto max loss ≤ soglia. "
        "Es.: «24h» in riga «-1%» = percentuale di tutte le posizioni che entro 24h hanno toccato almeno -1%."
    )
    st.dataframe(loss_pct_df, use_container_width=True, hide_index=True, height=min(420, 80 + 25 * len(loss_pct_df)))

    st.markdown("---")
    st.caption("Scarica i risultati in CSV.")
    col_dl1, col_dl2, col_dl3, col_dl4 = st.columns(4)
    with col_dl1:
        st.download_button(
            "Scarica riepilogo (CSV)",
            data=summary_df.to_csv(index=False),
            file_name="analisi_csv_riepilogo_finestre.csv",
            mime="text/csv",
            key="dl_csv_riepilogo",
        )
    with col_dl2:
        st.download_button(
            "Scarica statistiche complete (CSV)",
            data=stats_df.to_csv(),
            file_name="analisi_csv_statistiche_complete.csv",
            mime="text/csv",
            key="dl_csv_stats",
        )
    with col_dl3:
        st.download_button(
            "Scarica % soglie gain (CSV)",
            data=gain_pct_df.to_csv(index=False),
            file_name="analisi_csv_pct_soglie_gain.csv",
            mime="text/csv",
            key="dl_csv_gain_pct",
        )
    with col_dl4:
        st.download_button(
            "Scarica % soglie loss (CSV)",
            data=loss_pct_df.to_csv(index=False),
            file_name="analisi_csv_pct_soglie_loss.csv",
            mime="text/csv",
            key="dl_csv_loss_pct",
        )


def _render_backtest_tab() -> None:
    st.markdown("---")
    st.subheader("Caricamento dati da CSV esistenti (nessun backtest live)")
    with st.expander("Criteri sui dati SEC", expanded=False):
        st.markdown("""
        - **Codice P** — Solo acquisti open market / private purchase  
        - **Esclusione fondi** — Niente fund, ETF, trust, REIT nel nome  
        - **Cluster** — Raggruppamento per ticker + data filing  
        - **Entry** — Open del primo giorno di borsa ≥ data filing  
        - **Rendimenti** — ret_4h, ret_24h, ret_48h, ret_5d … ret_30d (giorni calendario)
        """)
    with st.expander("Perché mancano alcune voci rispetto a Open Insider?", expanded=False):
        st.markdown("""
        Possibili motivi:

        1. **Esclusione fondi** — Se la company ha nel nome "fund", "ETF", "trust", "REIT" la riga viene scartata.  
           Es.: **RCG** (Renn **Fund**, Inc.) non compare per questo motivo.

        2. **Limite risultati SEC** — La pipeline chiede un massimo di transazioni (es. 200 per «Ultimi 10 gg»).  
           Con molti filing nello stesso periodo, le ultime per data/ora possono non entrare. Prova un lasso più lungo o più `max_results` se ti servono tutte le voci.

        3. **Backtest Massive fallito** — Se per un ticker Massive non ha prezzi (es. titolo OTC/illiquido, ticker non trovato), il cluster viene escluso dalla tabella finale e finisce in «Dettaglio errori». Controlla l’expander errori dopo il caricamento.

        4. **Fonte diversa** — Open Insider può usare aggiornamenti o criteri leggermente diversi dalla SEC API che usiamo; l’ordine o il set delle transazioni può non coincidere al 100%.
        """)

    # Sorgenti CSV già generate dalla pipeline (nessuna chiamata API/live)
    sources = {
        "ALL_CLUSTERS_DB.csv (database cumulativo)": ROOT / "ALL_CLUSTERS_DB.csv",
        "STRATEGY_AGENT_CASES.csv (ultima run agente)": ROOT / "STRATEGY_AGENT_CASES.csv",
    }
    label = st.selectbox("Sorgente dati cluster", options=list(sources.keys()))
    csv_path = sources[label]

    if not csv_path.exists():
        st.error(
            f"Non trovo il file {csv_path.name} nella root del progetto.\n\n"
            "Generalo con una run locale (run_strategy_agent.py) e ricarica la pagina, "
            "oppure carica manualmente il CSV nella stessa cartella del progetto."
        )
        return

    if st.button("Carica dati da CSV esistente", type="primary", key="load_backtest_csv_btn"):
        try:
            df_loaded = pd.read_csv(csv_path, sep=";", encoding="utf-8-sig", low_memory=False)
        except Exception as e:
            st.error(f"Errore lettura {csv_path.name}: {type(e).__name__}: {e}")
            return
        st.session_state["mb_df"] = df_loaded

    if "mb_df" not in st.session_state:
        st.info("Seleziona la sorgente CSV e premi «Carica dati da CSV esistente» per vedere i dati base.")
        return

    df = st.session_state["mb_df"].copy()

    # Filtri sui cluster caricati
    with st.expander("Filtri cluster", expanded=True):
        years = None
        if "filing_day" in df.columns:
            df["filing_day"] = pd.to_datetime(df["filing_day"], errors="coerce")
            df["year"] = df["filing_day"].dt.year
            years = sorted([y for y in df["year"].dropna().unique().tolist() if y])
        else:
            df["year"] = None
        cols_top = st.columns(4)
        with cols_top[0]:
            if years:
                selected_years = st.multiselect("Anni filing", options=years, default=years, key="backtest_years")
            else:
                selected_years = []
        with cols_top[1]:
            roles_opts = []
            if "titles" in df.columns:
                base_titles = ["CEO", "CFO", "Director", "Officer", "10% Owner"]
                roles_opts = [t for t in base_titles if df["titles"].fillna("").str.contains(t, case=False, na=False).any()]
            elif "role" in df.columns:
                roles_opts = sorted(df["role"].dropna().unique().tolist())
            selected_roles = st.multiselect("Ruoli insider", options=roles_opts, default=roles_opts, key="backtest_roles")
        with cols_top[2]:
            min_val, max_val = None, None
            if "value_tot" in df.columns:
                vals = pd.to_numeric(df["value_tot"], errors="coerce").dropna()
                if not vals.empty:
                    min_val = float(vals.min())
                    max_val = float(vals.max())
            if min_val is not None and max_val is not None and min_val < max_val:
                v_min, v_max = st.slider(
                    "Range value_tot (USD)",
                    min_value=float(min_val),
                    max_value=float(max_val),
                    value=(float(min_val), float(max_val)),
                    key="backtest_value_range",
                )
            else:
                v_min, v_max = None, None
        with cols_top[3]:
            min_mc, max_mc = None, None
            if "market_cap" in df.columns:
                mcs = pd.to_numeric(df["market_cap"], errors="coerce").dropna()
                if not mcs.empty:
                    min_mc = float(mcs.min())
                    max_mc = float(mcs.max())
            if min_mc is not None and max_mc is not None and min_mc < max_mc:
                mc_min, mc_max = st.slider(
                    "Range market_cap (USD)",
                    min_value=float(min_mc),
                    max_value=float(max_mc),
                    value=(float(min_mc), float(max_mc)),
                    key="backtest_mcap_range",
                )
            else:
                mc_min, mc_max = None, None

        ticker_filter = st.text_input("Filtro ticker (contiene…)", key="backtest_ticker_filter").strip().upper()

    # Applica filtri
    if "year" in df.columns and selected_years:
        df = df[df["year"].isin(selected_years)]
    if selected_roles:
        if "titles" in df.columns:
            mask = False
            titles_series = df["titles"].fillna("")
            for r in selected_roles:
                mask = mask | titles_series.str.contains(r, case=False, na=False)
            df = df[mask]
        elif "role" in df.columns:
            df = df[df["role"].isin(selected_roles)]
    if v_min is not None and v_max is not None and "value_tot" in df.columns:
        vals = pd.to_numeric(df["value_tot"], errors="coerce")
        df = df[(vals >= v_min) & (vals <= v_max)]
    if mc_min is not None and mc_max is not None and "market_cap" in df.columns:
        mcs = pd.to_numeric(df["market_cap"], errors="coerce")
        df = df[(mcs >= mc_min) & (mcs <= mc_max)]
    if ticker_filter and "ticker" in df.columns:
        df = df[df["ticker"].fillna("").str.upper().str.contains(ticker_filter)]
    ret_order = ["ret_4h", "ret_24h", "ret_48h", "ret_5d", "ret_7d", "ret_10d", "ret_14d", "ret_30d"]
    ret_cols_present = [c for c in ret_order if c in df.columns]
    if ret_cols_present:
        other_cols = [c for c in df.columns if c not in ret_cols_present]
        idx_col = other_cols.index("entry_datetime") + 1 if "entry_datetime" in other_cols else len(other_cols)
        df = df[other_cols[:idx_col] + ret_cols_present + other_cols[idx_col:]]

    st.markdown("---")
    st.subheader("Tabella cluster")
    st.caption(f"{len(df)} righe. entry_date = giorno acquisto; entry_datetime = ora entry. ret_* = rendimento % a 4h, 24h, 48h, 5d … 30d.")
    n_no_ret = df["ret_30d"].isna().sum() if "ret_30d" in df.columns else 0
    if n_no_ret == len(df) and len(df) > 0:
        st.info("I rendimenti ret_* sono vuoti se i filing sono troppo recenti (es. per ret_30d servono ~30 giorni da entry).")
    st.dataframe(df, use_container_width=True, height=400)
    st.download_button("Scarica CSV cluster", data=df.to_csv(index=False), file_name="massive_backtest_clusters.csv", mime="text/csv", key="dl_csv")

    ret_cols = [c for c in ret_order if c in df.columns]
    if not ret_cols:
        st.warning("Nessuna colonna ret_* disponibile.")
        return

    base = compute_base_summary(df)
    if base.get("error"):
        st.warning(base.get("error", "Errore calcolo dati base."))
        return

    st.markdown("---")
    st.subheader("Dati di lettura base")
    st.caption("Statistiche per orizzonte e sul dataset. Dati grezzi, nessun filtro applicato.")

    s = base.get("summary", {})
    base_df = pd.DataFrame(base["base_table"])

    # Metriche dataset in evidenza
    st.markdown("#### Riepilogo dataset")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1:
        st.metric("Righe totali", s.get("tot_righe", 0), "")
    with c2:
        v = s.get("value_mediana")
        st.metric("Value mediana", f"${v:,.0f}" if v and v > 0 else "—", "")
    with c3:
        p25, p75 = s.get("value_p25"), s.get("value_p75")
        val = f"${p25:,.0f} / ${p75:,.0f}" if (p25 and p75) else (f"${p25:,.0f}" if p25 else (f"${p75:,.0f}" if p75 else "—"))
        st.metric("Value P25 / P75", val, "")
    with c4:
        m = s.get("mcap_mediana_M")
        st.metric("Mcap mediana", f"{m:.1f} M$" if m is not None else "—", "")
    with c5:
        pt = s.get("pct_con_titles")
        st.metric("% con titolo", f"{pt}%" if pt is not None else "—", "")
    with c6:
        roles = [f"CEO:{s.get('n_CEO',0)}", f"CFO:{s.get('n_CFO',0)}", f"Dir:{s.get('n_Director',0)}", f"Off:{s.get('n_Officer',0)}"]
        st.metric("Ruoli", " | ".join(roles), "")

    # Tabella per orizzonte
    st.markdown("#### Statistiche per orizzonte")
    st.caption("**n** = trade con dato valido · **Win %** = % con rendimento > 0 · **Vincitori/Perdenti** = conteggi · **Avg %** = media % · **Mediana %** = mediana · **Std/Min/Max %** = dispersione.")
    if not base_df.empty:
        base_df_display = base_df.copy()
        for col in ["Win %", "Avg %", "Mediana %", "Std %", "Min %", "Max %"]:
            if col in base_df_display.columns:
                base_df_display[col] = base_df_display[col].apply(lambda x: f"{x:.2f}" if isinstance(x, (int, float)) and not pd.isna(x) else "—")
        st.dataframe(base_df_display, use_container_width=True, hide_index=True, height=min(380, 50 + 40 * len(base_df_display)))

    # Win rate per ruolo
    role_analysis = base.get("role_analysis", {})
    if role_analysis:
        st.markdown("#### Win rate per ruolo (orizzonte ret_7d)")
        st.caption("Solo ruoli con almeno 2 trade. Win % = % trade con ret_7d > 0.")
        role_rows = []
        for k, v in sorted(role_analysis.items(), key=lambda x: -(x[1].get("win_rate_pct") or 0)):
            role_rows.append({
                "Ruolo": k,
                "Win %": f"{v.get('win_rate_pct', 0):.1f}" if v.get("win_rate_pct") is not None else "—",
                "n": v.get("n", 0),
                "Avg %": f"{v.get('avg_ret', 0):.2f}" if v.get("avg_ret") is not None else "—",
            })
        st.dataframe(pd.DataFrame(role_rows), use_container_width=True, hide_index=True)

    with st.expander("Guida dati base", expanded=False):
        st.markdown("""
        - **Orizzonte**: ret_4h/24h/48h = rendimento a 4h/24h/48h da entry; ret_5d … ret_30d = giorni calendario.
        - **Win %**: percentuale di trade con rendimento positivo.
        - **n**: numero di cluster con quel rendimento valorizzato.
        - **Value / Mcap**: valore acquisto e capitalizzazione (se presenti nei dati).
        - **Ruoli**: conteggio CEO, CFO, Director, Officer dai titoli SEC.
        """)


if __name__ == "__main__":
    main()
