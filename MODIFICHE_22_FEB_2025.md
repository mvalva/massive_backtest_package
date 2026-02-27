# Modifiche effettuate il 22 febbraio 2025

Riepilogo di tutte le modifiche apportate oggi al package `massive_backtest_package` (agente strategie SEC, report 10K, casi, timezone).

---

## 1. Exit price (prezzo di uscita) ovunque nei report 10K

- **Tabella "Confronto (tutte le strategie testate per finestra)"**: aggiunta colonna **Exit price (media)** con il prezzo di uscita medio (media dei `sell_price`) per ogni riga (finestra + strategia). Se non ci sono posizioni viene mostrato "—".
- **Sezione "Migliore strategia per finestra"**: in ogni riga aggiunto **Exit price (media)** (es. `$X.XX` o "—").
- **Tabella "Dettaglio per finestra"**: aggiunta colonna **Prezzo uscita** subito dopo "Prezzo entry" per ogni posizione (il `sell_price` usato per quel trade).
- Il prezzo di uscita è quello del backtest: `entry_price * (1 + ret_% / 100)`, coerente con l’orizzonte della strategia (es. ret_high_7d_news → uscita al massimo a 7 giorni).

**File modificato:** `massive_backtest/strategy_agent.py` (funzione `build_10k_strategy`).

---

## 2. Distinzione market cap (la migliore emerge dal backtest, non fissata a 1B)

- La soglia di market cap **non è fissata a 1 miliardo**: si testano **più soglie** e la **migliore** emerge dal backtest/ranking.
- **Soglie testate:** Large cap ≥500M, ≥1B, ≥2B, ≥5B, ≥10B (costante `CAP_THRESHOLDS` e filtri generati con `_make_cap_ge_filter`).
- **Strategie:** per ogni soglia, "Large cap (≥500M) CEO/CFO — hold {orizzonte}", "Large cap (≥1B) CEO/CFO — hold {orizzonte}", … fino a ≥10B. Restano **Small cap** (≤1B) e strategie senza filtro market cap.
- Nel report 10K, **Come funziona** spiega che per il market cap si testano più soglie (≥500M, ≥1B, ≥2B, ≥5B, ≥10B) e la migliore emerge dal backtest.

**File modificato:** `massive_backtest/strategy_agent.py` (`CAP_THRESHOLDS`, `_filter_cap_ge_cache`, loop su soglie in `STRATEGY_DEFINITIONS`).

---

## 3. Allocazione ottimale (migliore per passato/futuro)

- Per ogni **(finestra, strategia)** vengono ora testate **due modalità di allocazione**:
  1. **All-in sequenziale**: tutto il capitale su un trade alla volta; alla chiusura il capitale (incluso P&L) viene reinvestito sul trade successivo (compounding).
  2. **Parti uguali**: budget diviso in **N** parti uguali (una per posizione), senza compounding.
- Viene **scelta la modalità con rendimento storico migliore** (confronto sul rendimento %).
- Nel report 10K:
  - **Come funziona**: spiegazione delle due modalità e che il risultato mostrato è il migliore tra le due.
  - **Migliore strategia per finestra**: per ogni finestra è indicata l’**allocazione usata** (all-in sequenziale o parti uguali) e l’exit price medio.
  - **Tabella Confronto**: colonna **Allocazione** (all-in / parti uguali) per ogni riga.
  - **Miglior risultato assoluto**: indica anche l’allocazione usata.
  - **Dettaglio per finestra**: riga **"Allocazione usata (migliore nel backtest)"** e testo che spiega come si arriva al risultato (incluso filtro market cap e scelta allocazione).

**File modificati:** `massive_backtest/strategy_agent.py`:
- `_run_10k_window`: nuovo parametro `allocation_mode` ("all_in" | "equal_weight"); la funzione restituisce anche il mode usato; implementata la logica "equal_weight" (stesse N trade in ordine cronologico, allocazione = budget/N per posizione).
- `build_10k_strategy`: per ogni (finestra, strategia) vengono lanciate entrambe le modalità e si conserva il risultato (e il mode) con rendimento % più alto.

---

## 4. Simulazione per i prossimi 365 giorni — quale strategia seguire per ottenere il massimo

- Il report 10K non serve solo a confrontare il passato: deve indicare **cosa usare per i prossimi investimenti**.
- Aggiunta la sezione **"Strategia consigliata per il futuro"** nel report 10K:
  - Si usa la **migliore strategia (e allocazione) della finestra più recente** ("1 anno fa"), perché è il periodo più vicino a oggi e più rilevante per il futuro.
  - Tabella di raccomandazione: **Strategia** (nome), **Allocazione** (all-in sequenziale o parti uguali), rendimento e P&L del backtest sulla finestra recente, n. posizioni.
  - Testo **"Come applicarla"**: filtrare i cluster SEC che rispettano i criteri, ordinare per data filing, allocare il budget come indicato, uscita al massimo nell’orizzonte.
- Se nella finestra più recente non ci sono dati, il report indica che non è possibile raccomandare una strategia e suggerisce di rieseguire il backtest quando ci saranno più dati.
- Nell’intro del report è specificato che in fondo si trova la sezione **Simulazione per i prossimi 365 giorni**, che indica quale strategia seguire da oggi per i prossimi 365 giorni per puntare al massimo rendimento.

**File modificato:** `massive_backtest/strategy_agent.py` (funzione `build_10k_strategy`: nuova sezione e intro).

---

## 5. Timezone: specifica per tutti gli orari

- **Costante** `REPORT_DATETIME_TZ = "ET (America/New_York)"` in `strategy_agent.py`: tutti gli orari nei report sono in Eastern Time (America/New_York), coerentemente con i dati SEC (filedAt) e con il backtest (entry e barre in ET).
- **Report 10K** (`STRATEGY_AGENT_*_10K.md`):
  - In cima al report: riga **"Timezone: Tutti gli orari nei report (data/ora filing, entry, uscita) sono in ET (America/New_York)."**
  - Tabella dettaglio posizioni: intestazioni **"Entry (data/ora ET (America/New_York))"** e **"Uscita (data/ora, peak ET (America/New_York))"**.
- **Report casi** (`STRATEGY_AGENT_CASES_REPORT.md` / build_cases_md):
  - Riga **"Timezone: Tutti gli orari (filedAt, entry_datetime, datetime_high_30d, datetime_low_30d) sono in ET (America/New_York)."**
  - Testo sui datetime_high_30d/datetime_low_30d che specifica "in ET (America/New_York)".
- **Report per ticker** (build_tickers_md): intestazioni tabelle con timezone:
  - "Data e ora filing (ET (America/New_York))", "Entry (data e ora ET (America/New_York))", "Data/ora max 30d (ET (America/New_York))", "Data/ora min 30d (ET (America/New_York))".

**File modificato:** `massive_backtest/strategy_agent.py` (costante `REPORT_DATETIME_TZ` e aggiornamento di `build_10k_strategy`, `build_cases_md`, sezione ticker in build_tickers_md).

---

## Riepilogo file toccati

| File | Modifiche |
|------|-----------|
| `massive_backtest/strategy_agent.py` | Exit price in tabelle e sezioni 10K; filtro `filter_cap_ge_1b` e strategie Large cap (≥1B); allocation_mode in `_run_10k_window` e scelta migliore in `build_10k_strategy`; **sezione "Strategia consigliata per il futuro"** (raccomandazione dalla finestra più recente); costante `REPORT_DATETIME_TZ` e note timezone in report 10K, casi e ticker. |

---

## Come vedere le modifiche nei file di output

Dopo aver rigenerato i report (eseguendo di nuovo l’agente o lo script che produce 10K, casi, ranking):

- **STRATEGY_AGENT_60d_10K.md** (o **STRATEGY_AGENT_10K.md**): timezone in cima, colonne Exit price e Allocazione, note su market cap e allocazione.
- **STRATEGY_AGENT_60d_CASES_REPORT.md**: timezone e riferimenti ET negli orari.
- **STRATEGY_AGENT_60d_TICKERS.md**: intestazioni tabelle con timezone.
- **STRATEGY_AGENT_60d_RANKING.csv**: possono comparire le nuove strategie "Large cap (≥1B) CEO/CFO — hold ...".

Questo documento è stato generato il 22 febbraio 2025.
