# Agente strategie SEC

L’agente usa i **buy SEC** (Form 4, codice P) e i **prezzi Massive** per:
1. Caricare **3 anni** di acquisti insider dalla SEC (ultimi 3 anni da oggi)
2. Eseguire il **backtest** su ogni cluster (ticker + data filing) con prezzi Massive
3. Valutare **decine di strategie** (combinazioni di filtri + orizzonte di hold)
4. Restituire le **migliori strategie** in base a rendimento medio, win rate, Sharpe
5. Mostrare **ogni singolo ticker** con performance e uso nell’analisi (report per ticker)
6. Creare la **migliore strategia con 10k USD** per massimizzare il risultato in un anno (portfolio simulato)
7. Creare un **database di tutti i ticker/stock** usati, con data di filing, entry price in entrambe le modalità (open e news), massimi e minimi per orizzonte come descritti sopra
8. Selezionare, sulla base dei 3 anni storici, la **strategia operativa “da oggi a 1 anno”**: confrontare le strategie (inclusa la 10k sequenziale) e scegliere se puntare a **molti take‑profit piccoli e frequenti** (es. +1/+2% in 7–10 giorni) o a **pochi trade più lunghi** con target più alti (es. +20/+50% su 30–60 giorni), usando i risultati storici per stimare quale profilo è più adatto al proprio obiettivo di rendimento/rischio.

---

## Strategie considerate

Le strategie sono **composizioni** di:

- **Ruolo:** *esempi* — singoli (CEO, CFO, Director, 10% Owner) e combo (CEO+CFO, CEO+Director, CFO+Director). **Non solo questi**: altri ruoli e combinazioni sono possibili.
- **Variazione % posizione:** *esempi* — 10% / 20% / 30% (da dati SEC post-transazione). **Non solo queste soglie**: altre percentuali sono possibili.
- **Combinazioni ruolo × variazione %:** *esempi* — CEO only + Position +10%, 10% Owner + Position +20%, CEO+CFO + Position +10%.
- **Dimensione:** *esempi* — valore $ (≥50k, ≥100k, ≥500k, ≥1M) e quantità azioni. **Non solo queste soglie**: altre dimensioni sono possibili.
- **Analisi tecnica a entry:** *esempi* — RSI(14) oversold (&lt;30) / overbought (&gt;70), prezzo sopra/sotto MA50 e MA200. **Non solo questi**: altri indicatori e soglie sono possibili e configurabili.
- **Combinazioni TA + ruolo:** *esempi* — RSI oversold + CEO/CFO, Price &gt; MA50 + CEO/CFO.
- **Altri filtri:** *esempi* — multiple buys, small/large cap, 52w high. **Non solo questi**: altri filtri sono possibili e configurabili.
- **Entry:** *open* = primo prezzo a mercato aperto (solo regular); *news* = prezzo fattibile quando esce la notizia SEC (pre/after market, spread conservativo). Per **ogni ticker** (cluster) vengono registrati **prezzo e data di entry open** e **prezzo e data di entry news**, usati nelle analisi e nel database.
- **Orizzonte:** *esempi* — 1, 2, 3, 5, 7, 10, 14, 30, 60, 90 **giorni di borsa** (solo giorni in cui il mercato è aperto). **Non solo questi**: altri orizzonti sono possibili e configurabili.
- **Metrica:** *high* = massimo % raggiunto nel periodo (best case), *low* = minimo % (worst case)

Ogni strategia è valutata con: **N**, **Win rate %**, **Avg ret %**, **Total ret %**, **Sharpe (approssimato)**, Min/Max %.

### Cosa significano Ret high e Ret low (performance) — tutti gli orizzonti

Nel report per ticker e nei CSV sono mostrati **tutti gli orizzonti** disponibili: **1, 2, 3, 5, 7, 10, 14, 30, 60, 90 giorni di borsa** (colonne tipo **H1d %**, **L1d %**, … **H30d %**, **L30d %**, **H60d %**, **L60d %**, **H90d %**, **L90d %**).

- **Ret high Nd %** (in tabella: **H Nd %**) = **miglior rendimento** (in %) che il titolo avrebbe potuto dare **entro N giorni di borsa** dall’entry. È il massimo raggiunto dal prezzo in quel periodo rispetto al prezzo di ingresso (es. compri a 100, in 7 giorni tocca 105 → H7d = +5%). Indica il *best case* se avessi venduto al top in quell’orizzonte.
- **Ret low Nd %** (in tabella: **L Nd %**) = **peggior rendimento** (in %) toccato **entro N giorni di borsa** dall’entry. È il minimo raggiunto dal prezzo in quel periodo (es. compri a 100, a un certo punto scende a 97 → L7d = -3%). Indica il *worst case* e il rischio di drawdown in quell’orizzonte.

Entrambi sono calcolati con **prezzo di entry “open”** (primo prezzo a mercato aperto il giorno dopo il filing). L’orizzonte è in **giorni di borsa** (solo giorni in cui il mercato è aperto), non giorni di calendario. Per ogni orizzonte sono registrate **data e ora** in cui il ticker raggiunge il massimo e il minimo (`date_high_Nd`, `date_low_Nd`, `datetime_high_Nd`, `datetime_low_Nd`).


### Dati per ticker e database per strategia

- **Per ogni ticker (cluster)** nei report e nel CSV sono indicati: **prezzo open** (`entry_price`) e **data e ora open** (`entry_datetime`), **prezzo news** (`entry_price_news`), **data e ora filing** (`filedAt`; `filing_day` = solo data), più tutti i **massimi e minimi** per orizzonte e le **date/ora in cui vengono raggiunti** (`datetime_high_Nd`, `datetime_low_Nd`, e `date_high_Nd`, `date_low_Nd` per N = 1, 2, 3, 5, 7, 10, 14, 30, 60, 90 giorni di borsa).
- **Nelle analisi successive** (report per ticker, casi, strategie) per ogni ticker sono sempre disponibili: prezzi e date di acquisto (open/news), **massimo %** e **minimo %** raggiunti in ogni orizzonte (best/worst case), drawdown e run-up.
- **Database per strategia:** il file **STRATEGY_AGENT_CASES.csv** è il database completo: una riga per cluster (ticker + data e ora filing) con tutte le colonne. Ogni informazione di data include **data e ora** dove disponibile (`filedAt`, `entry_datetime`; per ogni orizzonte anche `datetime_high_Nd` e `datetime_low_Nd` = data e ora in cui il ticker raggiunge massimo e minimo). Filtrando per i criteri di una strategia si ottiene l'elenco di tutti i ticker con dettagli: prezzo e data/ora acquisto (open/news), rendimenti e date/ora di massimo/minimo, quantità, valore, TA, market_cap, ecc.

---


## Prima della run

1. **Chiavi API** — Crea o verifica il file `.env` nella root (o in `massive_backtest/.env`) con `SEC_API_KEY` e `MASSIVE_API_KEY`. Vedi **CONFIGURAZIONE_API.md** e `env_template.txt`.
2. **Verifica ambiente** — Dalla root: `python check_before_run.py` (controlla chiavi e dipendenze).
3. **Dipendenze** — `pip install -r massive_backtest/requirements.txt`. Per l'app: streamlit.
4. **Parametri** — Per 3 anni conviene `--max-results 15000` o più. Prova veloce: `--days 30 --max-results 500`.
5. **Output** — La run sovrascrive i file; copia i report se vuoi conservarli.

---

## Come eseguire l'agente

### Da riga di comando (consigliato per 3 anni di dati)

Dalla **root del progetto** (`massive_backtest_package`):

```bash
python run_strategy_agent.py
```

Opzioni:
- `--days 1095` — giorni indietro per la SEC (default 1095 = 3 anni da oggi)
- `--max-results 5000` — massimo numero di transazioni SEC (default 5000; per 3 anni conviene aumentare, es. 15000)
- `--out FILE.txt` — file di output del report (default: `STRATEGY_AGENT_REPORT.txt`)
- `--budget-usd 10000` — budget USD per la simulazione 10k (default 10000)
- `--lookback-days 365` — giorni per finestra della strategia 10k (default 365)
- `--max-positions 0` — massimo numero di posizioni per finestra nella 10k (0 = tutte le posizioni disponibili)
- `--top-strategies-k 10` — numero di strategie top dal ranking da testare nella 10k (default 10)
- `--prefer-allocation {auto,all_in,equal_weight}` — scelta allocazione nella 10k: `auto` (sceglie la migliore tra all-in e parti uguali), `all_in` (forza all-in sequenziale), `equal_weight` (forza parti uguali)
- `--min-strategy-n N` — esclude dal 10k le strategie con meno di `N` cluster (0 = nessun filtro)
- `--max-clusters N` — backtesta al massimo N cluster (0 = tutti). Utile per limitare i tempi: con ~2400 cluster la run resta in genere sotto le **2 ore**.
- `--parallel N` — usa N worker paralleli per il backtest (0 = sequenziale). Es. `--parallel 4` riduce i tempi se l’API Massive lo consente.

- `--update-outputs-only` — **aggiorna solo i file di output** (report, 10K, TICKERS, CASES_REPORT, BOT_SUGGESTIONS, TICKER_BUY_RANKING, ecc.) leggendo da `*_CASES.csv` e `*_RANKING.csv` **senza eseguire backtest né chiamate API**. Utile per rigenerare report e bot dopo aver modificato parametri (es. budget 10k, top-strategies-k) o dopo un errore durante l'export. Non richiede chiavi API. Non rigenera `*_SEC_TRANSACTIONS.csv` né `*_SEC_CLUSTERS_ALL.csv` (restano quelli della run precedente).

**Velocizzare il backtest:** in ambiente puoi impostare `BACKTEST_DELAY_SEC=0.02` (default ora 0.02; prima era 0.1). Se compaiono errori 429 (rate limit), aumenta a 0.05 o 0.1. Con `--parallel 4` e delay basso la run può essere 2–3× più veloce.

Esempio (run completa 3 anni):
```bash
python run_strategy_agent.py --days 1095 --max-results 15000 --out STRATEGY_AGENT_REPORT.txt
```

Esempio **run entro ~2 ore** (1 anno, max 2400 cluster, 4 worker):
```bash
python run_strategy_agent.py --days 365 --max-results 15000 --max-clusters 2400 --parallel 4 --out BACKTEST_STRATEGIE_REPORT.txt
```

Il report viene salvato nella root del progetto e stampato in console.

**Dove vedere il progresso** — Durante l'esecuzione la percentuale di avanzamento è visibile in due modi:
1. **File** — Apri il file **STRATEGY_AGENT_PROGRESS.txt** nella root del progetto: viene aggiornato a ogni passo (es. `[38%] Backtest 1989/6529 — ARAY`). A fine run troverai "Completato." o un messaggio di errore.
2. **Terminale** — Lo stesso messaggio viene stampato nel terminale da cui hai lanciato lo script (pannello Terminal in Cursor).

### Dall’app Streamlit

1. Avvia l’app: `streamlit run massive_backtest/app.py`
2. Apri la tab **«Agente strategie»**
3. Imposta giorni e max risultati (opzionale)
4. Clicca **«Esegui agente (backtest 3 anni + ranking strategie)»**
5. Attendi il termine (può richiedere diversi minuti per 3 anni e migliaia di cluster)
6. Visualizza **tutte le strategie** (tabella completa); puoi scaricare il report in .txt e le strategie in Markdown

---

## Requisiti

- **SEC_API_KEY** e **MASSIVE_API_KEY** nel file `.env` (root o `massive_backtest/.env`). Verifica con: `python check_before_run.py`
- Dipendenze: `pandas`, `requests`, `python-dotenv`; per l’app anche `streamlit`

---

## Output

- **STRATEGY_AGENT_REPORT.txt** — Tutte le strategie (tabella completa) con N, Win rate %, Avg ret %, Total ret %, Sharpe, Min/Max %
- **STRATEGY_AGENT_RANKING.csv** — Stessa tabella strategie in CSV (apribile in Excel)
- **STRATEGY_AGENT_STRATEGIES.md** — Tutte le strategie in Markdown (leggibile/condivisibile)
- **STRATEGY_AGENT_CASES.csv** — Risultati **caso per caso**: una riga per cluster (ticker, **data e ora filing** `filedAt`, **data e ora entry** `entry_datetime`, entry_price, entry_price_news, ret_high/low per orizzonte, **exit price** per ogni orizzonte: `exit_high_Nd_open_price`, `exit_low_Nd_open_price`, `exit_high_Nd_news_price`, `exit_low_Nd_news_price`, **data/ora massimo e minimo** `datetime_high_Nd`/`datetime_low_Nd`, titoli, value_tot, TA, ecc.). Serve per analisi dettagliata e filtri su singoli trade.
- **STRATEGY_AGENT_CASES_REPORT.md** — **Analisi caso per caso**: report leggibile con le **azioni** (cluster) evidenziate: **Migliori** (top 30 per rendimento massimo nell’orizzonte) , **Peggiori** e **Tutti i casi** (elenco completo). Per il database completo: **STRATEGY_AGENT_CASES.csv**. Dopo l’analisi puoi aprire questo file per vedere subito i migliori e peggiori casi; in Streamlit la stessa sezione è disponibile sotto «Analisi caso per caso» con download MD e CSV.
- **STRATEGY_AGENT_IMPROVEMENT.txt** — **Auto-miglioramento**: analisi del ranking (hold key e temi più presenti nelle top) + suggerimenti per nuove strategie da testare (es. aggiungere TA a strategie forti, confrontare ret_low oltre a ret_high). Ogni run genera suggerimenti da valutare per il prossimo run.
- **STRATEGY_AGENT_TICKERS.md** / **STRATEGY_AGENT_TICKERS.csv** — **Ogni singolo ticker**: per ogni ticker, riepilogo (N cluster, ret medio, value tot) e **dettaglio di ogni apparizione**: data, quantità, ruolo, costo, aumento % posizione, **ret % per orizzonte 1d, 2d, 3d, 5d, 7d, 10d, 14d, 30d, 60d, 90d** (H Nd % = best case, L Nd % = worst case in N giorni borsa). Vedi sopra per il significato di Ret high/Ret low.
- **STRATEGY_AGENT_10K.md** / **STRATEGY_AGENT_10K.csv** — **Strategia 10k USD**: tre simulazioni (3, 2 e 1 anno fa) su finestra successiva di 365 giorni; per ogni finestra vengono testate più strategie del ranking (quale sarebbe stata più conveniente, es. più trade vs un solo buy). Il report confronta i rendimenti e mostra **exit price** (prezzo uscita) ovunque; il CSV contiene le posizioni con colonne **entry_price**, **exit_price** (e sell_price), ticker, filing_day, allocation_usd, ret %, pnl_usd.
- **STRATEGY_AGENT_BOT_SUGGESTIONS.csv** / **STRATEGY_AGENT_TICKER_BUY_RANKING.csv** — Generati dal bot a fine run. Il **TICKER_BUY_RANKING** risponde a “quale ticker comprare per primo” (ultimi 5 giorni): per ogni ticker indica **insider_entry_price** (prezzo open al filing), **best_strategy** (macrocategoria, es. “CEO only + Value ≥100k”, non la variante singola hold/high/mean/low), **take_profit_pct**, **stop_loss_pct**, **exit_price_potential** e **exit_price_stop_potential** (derivati da insider_entry_price e dalle %).
  - **Come si scelgono take profit e stop loss:** la strategia mostrata è la **macro** (Base_name). Take profit e stop loss usano **tutto l’insieme della macro** (tutte le varianti hold/high/mean/low): **Take profit %** = *media* di Avg_ret_% su tutte le varianti della macro; **Stop loss %** = *-|min(Min_%)|* su tutte le varianti (peggior caso storico della macro). I prezzi di uscita sono calcolati da **insider_entry_price**.
- In Streamlit: stesse tabelle + report per ticker + strategia 10k + pulsanti download

Tutti i timestamp (filedAt, filing_day, entry_datetime, datetime_high/low, sell_datetime) sono espressi in **ET (America/New_York)**.

Le strategie sono ordinate per **Avg ret %** (rendimento medio) decrescente; le prime in lista sono le più performanti sul periodo backtestato.

---

## Manutenzione / Riferimenti codice

- **Entry point:** `run_strategy_agent.py` → `strategy_agent.run_agent()` → `build_report()` (che scrive anche CASES, TICKERS, 10K).
- **Orizzonte giorni di borsa:** definito una sola volta in `massive_backtest/backtest_engine.py` → `TRADING_DAY_HORIZONS = [1, 2, 3, 5, 7, 10, 14, 30, 60, 90]`.
- **Costanti report/10k:** in `strategy_agent.py` → `REPORT_CASES_TOP_N`, `REPORT_CASES_BOTTOM_N`, `STRATEGY_10K_BUDGET`, `STRATEGY_10K_LOOKBACK_DAYS`, `STRATEGY_10K_MAX_POSITIONS` (modificabili per cambiare top/bottom casi e parametri strategia 10k).
- **Formattazione valori report:** funzione unica `_fmt()` in `strategy_agent.py`.