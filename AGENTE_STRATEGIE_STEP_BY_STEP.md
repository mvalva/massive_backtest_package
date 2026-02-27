on v## Agente strategie SEC — Step by step

Questo file descrive a grandi linee il flusso dell’agente strategie, utile per capire dove intervenire e come leggere gli output.

---

### 1. Caricamento dati SEC + Massive

- Lettura dei Form 4 (acquisti) dalla SEC API per `--days` giorni indietro (default 1095 = 3 anni).
- Normalizzazione in **cluster** (ticker + filing + informazioni su ruolo, quantità, valore, % posizione, ecc.).
- Enrichment con dati Massive (prezzi storici, market cap, TA, 52w, ecc.).

---

### 2. Backtest per cluster

- Per ogni cluster si calcolano i rendimenti `ret_high_Nd_open` / `ret_low_Nd_open` per tutti gli orizzonti (1, 2, 3, 5, 7, 10, 14, 30, 60, 90 giorni di borsa).
- Per ogni orizzonte vengono calcolati anche:
  - `datetime_high_Nd` / `datetime_low_Nd` = data/ora del massimo/minimo nell’orizzonte.
  - `exit_high_Nd_open_price` / `exit_low_Nd_open_price` (e varianti *news*) = **exit price** al massimo/minimo.
- Il risultato completo per cluster finisce in `STRATEGY_AGENT_CASES.csv`.

---

### 3. Costruzione ranking strategie

- Partendo dai cluster, si applicano tutte le combinazioni di:
  - filtri su ruolo (CEO, CFO, Director, 10% Owner, combo),
  - filtri su variazione % posizione, valore, TA, market cap (Large/Small cap, soglie ≥500M/≥1B/≥2B/≥5B/≥10B, ecc.),
  - orizzonte di hold (es. `ret_high_7d_open`, `ret_high_30d_open`, ecc.).
- Per ogni combinazione (una **strategia**) si calcolano:
  - N casi, Win rate %, Avg ret %, Total ret %, Sharpe approx, Min/Max %.
- Le strategie vengono ordinate per Avg ret % decrescente:
  - tabella principale nel report (`STRATEGY_AGENT_REPORT.txt`),
  - `STRATEGY_AGENT_RANKING.csv`,
  - dettaglio leggibile in `STRATEGY_AGENT_STRATEGIES.md`.

---

### 4. Analisi caso per caso (CASES)

- `build_cases_report` genera `STRATEGY_AGENT_CASES_REPORT.md` con:
  - **Migliori** casi (top per rendimento massimo),
  - **Peggiori** casi (worst case),
  - elenco **Tutti i casi** (se abilitato).
- Ogni tabella mostra:
  - ticker, filedAt, entry_datetime, entry_price, entry_price_news,
  - rendimenti per orizzonte,
  - `datetime_high_30d` / `datetime_low_30d`,
  - `exit_high_30d_open_price` / `exit_low_30d_open_price` (exit price 30d),
  - value_tot, titles (riassunto ruolo).
- `STRATEGY_AGENT_CASES_KEYS.csv` contiene un **sottoinsieme di colonne chiave** per analisi rapide (ticker, filing_day/filedAt, entry, exit price 7d/30d, ret% principali).

---

### 5. Report per ticker

- `build_tickers_report` produce:
  - `STRATEGY_AGENT_TICKERS.csv` — riepilogo per ticker (N cluster, ret high/low medio, value_tot, colonna di testo per uso analisi).
  - `STRATEGY_AGENT_TICKERS.md` — report leggibile con sezione per ogni ticker.
- Per ogni ticker:
  - riepilogo aggregato (N cluster, ret medi, valore totale),
  - tabella dettaglio di tutte le apparizioni (filedAt, entry, quantità, ruolo, costo, aumento % posizione, ret % per tutti gli orizzonti, eventuali datetime_high/low 30d, exit price 30d high/low).

---

### 6. Strategia 10k USD (tre finestre + raccomandazione)

- `build_10k_strategy` usa `df_results` + ranking per simulare tre finestre:
  - oggi-3 anni → anno successivo,
  - oggi-2 anni → anno successivo,
  - oggi-1 anno → anno successivo.
- Per ogni finestra:
  - seleziona le prime `top_strategies_k` strategie del ranking,
  - per ogni strategia testa due modalità di allocazione:
    - **all-in sequenziale** (compounding),
    - **parti uguali** (no compounding),
  - sceglie (o forza) l’allocazione in base a `prefer_allocation`:
    - `auto` = prende quella con rendimento migliore,
    - `all_in` = forza all-in,
    - `equal_weight` = forza parti uguali.
- Output:
  - `STRATEGY_AGENT_10K.md` — report dettagliato con:
    - migliore strategia per finestra,
    - tabella con tutte le strategie testate per finestra,
    - **Raccomandazione per i prossimi 365 giorni** (strategia + allocazione + stabilità finestre + filtro market cap),
    - confronto allocazione all-in vs parti uguali per la strategia raccomandata,
    - dettaglio posizioni per ogni finestra.
  - `STRATEGY_AGENT_10K.csv` — posizioni della finestra “1 anno fa” (entry/exit, ret %, P&L, ticker, filing_day, allocation, shares).

---

### 7. Auto-miglioramento

- `strategy_improver.build_improvement_report` genera `STRATEGY_AGENT_IMPROVEMENT.txt` a partire dal ranking:
  - analisi dei pattern più forti (hold key, temi ricorrenti),
  - idee per nuove strategie da testare (modifiche TA, filtri aggiuntivi, ecc.).

---

### 8. File principali da conoscere

- `run_strategy_agent.py` — entry point CLI (parsing argomenti, progress, chiamata a `run_agent` e `build_report`).
- `massive_backtest/strategy_agent.py` — logica principale (definizione strategie, backtest, report, strategia 10k).
- `massive_backtest/backtest_engine.py` — orizzonti di trading e calcolo ret/high/low + exit price.
- `AGENTE_STRATEGIE_README.md` — guida utente (setup, esecuzione, descrizione output).
- `MIGLIORAMENTI_AGENTE.md` — elenco suggerimenti di miglioramento e priorità.

