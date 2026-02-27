# Strategia 10k USD — Confronto strategie su tre finestre (1 anno ciascuna)

**Timezone:** Tutti gli orari nei report (data/ora filing, entry, uscita) sono in **ET (America/New_York)**.

Per ogni finestra (3 anni fa, 2 anni fa, 1 anno fa) sono state testate le prime **10** strategie del ranking. La sezione **Simulazione per i prossimi 365 giorni** indica quale strategia e allocazione seguire **da oggi per i prossimi 365 giorni** per puntare al massimo rendimento (basata sull’analisi della finestra più recente).

**Strategia sul futuro (cluster e importi):** il file con suffisso **_10K.csv** contiene i **cluster consigliati** (ticker, filing_day, **entry_price**, **exit_price**, allocation_usd, ret %, pnl_usd) della strategia vincente sulla finestra più recente. Per i prossimi 365 giorni puoi **acquistare più stock alla volta** applicando gli stessi criteri ai nuovi Form 4, con **importi uguali** (parti uguali) o **diversi** (es. in proporzione al valore del filing o al rendimento atteso); la colonna allocation_usd indica l'importo suggerito per ogni cluster.

**Come applicarla da oggi in pratica:**

- Prendi dal report qui sotto la **strategia raccomandata per la finestra più recente** (filtro, Hold, modalità allocazione).
- Usa lo **stesso filtro** sui nuovi Form 4 (es. solo CEO/CFO, solo Value ≥100k, solo Small cap, ecc.).
- Usa lo **stesso orizzonte Hold** (es. ret_high_30d_open ⇒ tieni fino al massimo a 30 giorni borsa dall’entry).
- Usa la **stessa modalità di allocazione** scelta (all-in sequenziale o parti uguali).
- Ogni volta che arriva un nuovo filing che soddisfa il filtro, lo aggiungi alla lista dei trade da fare, replicando la logica storica per i prossimi 365 giorni.

Budget: **$10,000** | Max posizioni: **tutte (nessun limite)** | Giorni/finestra: **365**

## Come funziona (logica)

- Per ogni **finestra** si considera l’intervallo di date **filing_day** (data del Form 4 SEC) da *data inizio* a *data fine* (1 anno).
- Per ogni **strategia** si filtrano i cluster (ticker + data filing) che rispettano i criteri (ruolo, % posizione, valore, **market cap**, ecc.). Per il **market cap** si testano **bande dettagliate**: Micro cap (≤50M, ≤100M, ≤250M), Small cap (≤1B), Mid cap (1B–10B), Large cap con soglie ≥250M, ≥500M, ≥750M, ≥1B, ≥2B, ≥3B, ≥5B, ≥10B, ≥20B, ≥50B, ≥100B; la **migliore** emerge dal backtest/ranking. Si ordinano per rendimento nell'orizzonte scelto (es. ret_high_30d_open) in ordine decrescente; si possono prendere tutte le posizioni disponibili (oppure, se configurato, un massimo predefinito). **Allocazione:** per ogni (finestra, strategia) si testano due modalità e si usa quella con rendimento storico migliore: **(1) all-in sequenziale** — tutto il capitale su un trade alla volta, quando chiude si reinveste sul successivo; **(2) parti uguali** — budget diviso in N parti uguali (una per posizione), nessun compounding. Il **risultato** mostrato è il migliore tra le due.
- (Nella tabella sotto, per ogni strategia è indicata l'allocazione usata: all-in sequenziale o parti uguali.) nell’orizzonte scelto (es. ret_high_30d_open) in ordine decrescente; si possono prendere tutte le posizioni disponibili (oppure, se configurato, un massimo predefinito).
- Se una finestra mostra **0 posizioni** e 0%: in quel periodo non ci sono filing nel database che rispettano i criteri di nessuna strategia testata. Possibili cause: i dati SEC del backtest non coprono quel periodo (es. API con pochi risultati storici) oppure in quel periodo non ci sono acquisti che soddisfano i filtri (ruolo CEO/CFO, % posizione, market cap, ecc.).

---

## Migliore strategia per finestra

- **3 anni fa (anno successivo)**: **CEO + Director (combo) — hold ret_high_60d_open** → **0.00%** | P&L $0.00 | 0 pos. | Allocazione: **all-in sequenziale** | Entry price (media) — | Exit price (media) —
- **2 anni fa (anno successivo)**: **CEO + Director (combo) — hold ret_high_60d_open** → **39.42%** | P&L $3,942.00 | 1 pos. | Allocazione: **all-in sequenziale** | Entry price (media) $5.20 | Exit price (media) $7.25
- **1 anno fa (anno successivo)**: **CEO + Director (combo) — hold ret_high_60d_open** → **0.00%** | P&L $0.00 | 0 pos. | Allocazione: **all-in sequenziale** | Entry price (media) — | Exit price (media) —

---

## Confronto (tutte le strategie testate per finestra)

| Finestra | Strategia | Rend.% | P&L USD | N pos | Allocazione | Entry price (media) | Exit price (media) |
|----------|-----------|--------|--------|------|--------------|----------------------|---------------------|
| 3 anni | CEO + Director (combo) — hold ret_high_60d_op… | 0.00 | $0.00 | 0 | all-in | — | — |
| 3 anni | Small cap (≤1B) CEO/CFO — hold ret_high_60d_o… | 0.00 | $0.00 | 0 | all-in | — | — |
| 3 anni | CEO + Director (combo) — hold ret_high_90d_op… | 0.00 | $0.00 | 0 | all-in | — | — |
| 3 anni | Small cap (≤1B) CEO/CFO — hold ret_high_90d_o… | 0.00 | $0.00 | 0 | all-in | — | — |
| 3 anni | CEO + Director (combo) — hold ret_high_60d_ne… | 0.00 | $0.00 | 0 | all-in | — | — |
| 3 anni | Small cap (≤1B) CEO/CFO — hold ret_high_60d_n… | 0.00 | $0.00 | 0 | all-in | — | — |
| 3 anni | CEO + Director (combo) — hold ret_high_90d_ne… | 0.00 | $0.00 | 0 | all-in | — | — |
| 3 anni | Small cap (≤1B) CEO/CFO — hold ret_high_90d_n… | 0.00 | $0.00 | 0 | all-in | — | — |
| 3 anni | CEO only — hold ret_high_90d_news | 0.00 | $0.00 | 0 | all-in | — | — |
| 3 anni | CEO only — hold ret_high_90d_open | 0.00 | $0.00 | 0 | all-in | — | — |
| 2 anni | CEO + Director (combo) — hold ret_high_60d_op… | 39.42 | $3,942.00 | 1 | all-in | $5.20 | $7.25 |
| 2 anni | Small cap (≤1B) CEO/CFO — hold ret_high_60d_o… | 39.42 | $3,942.00 | 1 | all-in | $5.20 | $7.25 |
| 2 anni | CEO + Director (combo) — hold ret_high_90d_op… | 39.42 | $3,942.00 | 1 | all-in | $5.20 | $7.25 |
| 2 anni | Small cap (≤1B) CEO/CFO — hold ret_high_90d_o… | 39.42 | $3,942.00 | 1 | all-in | $5.20 | $7.25 |
| 2 anni | CEO + Director (combo) — hold ret_high_60d_ne… | 38.10 | $3,810.00 | 1 | parti uguali | $5.20 | $7.18 |
| 2 anni | Small cap (≤1B) CEO/CFO — hold ret_high_60d_n… | 38.10 | $3,810.00 | 1 | parti uguali | $5.20 | $7.18 |
| 2 anni | CEO + Director (combo) — hold ret_high_90d_ne… | 38.10 | $3,810.00 | 1 | parti uguali | $5.20 | $7.18 |
| 2 anni | Small cap (≤1B) CEO/CFO — hold ret_high_90d_n… | 38.10 | $3,810.00 | 1 | parti uguali | $5.20 | $7.18 |
| 2 anni | CEO only — hold ret_high_90d_news | 25.19 | $2,519.00 | 1 | parti uguali | $41.99 | $52.57 |
| 2 anni | CEO only — hold ret_high_90d_open | 23.43 | $2,343.00 | 1 | parti uguali | $41.99 | $51.83 |
| 1 anno | CEO + Director (combo) — hold ret_high_60d_op… | 0.00 | $0.00 | 0 | all-in | — | — |
| 1 anno | Small cap (≤1B) CEO/CFO — hold ret_high_60d_o… | 0.00 | $0.00 | 0 | all-in | — | — |
| 1 anno | CEO + Director (combo) — hold ret_high_90d_op… | 0.00 | $0.00 | 0 | all-in | — | — |
| 1 anno | Small cap (≤1B) CEO/CFO — hold ret_high_90d_o… | 0.00 | $0.00 | 0 | all-in | — | — |
| 1 anno | CEO + Director (combo) — hold ret_high_60d_ne… | 0.00 | $0.00 | 0 | all-in | — | — |
| 1 anno | Small cap (≤1B) CEO/CFO — hold ret_high_60d_n… | 0.00 | $0.00 | 0 | all-in | — | — |
| 1 anno | CEO + Director (combo) — hold ret_high_90d_ne… | 0.00 | $0.00 | 0 | all-in | — | — |
| 1 anno | Small cap (≤1B) CEO/CFO — hold ret_high_90d_n… | 0.00 | $0.00 | 0 | all-in | — | — |
| 1 anno | CEO only — hold ret_high_90d_news | 0.00 | $0.00 | 0 | all-in | — | — |
| 1 anno | CEO only — hold ret_high_90d_open | 0.00 | $0.00 | 0 | all-in | — | — |

**Miglior risultato assoluto:** CEO + Director (combo) — hold ret_high_60d_open → **39.42%** (P&L $3,942.00, allocazione: all-in sequenziale).

---

## Simulazione per i prossimi 365 giorni — strategia reale fondata sui dati (date, esempi, massimo nel passato)

L’analisi usa la **finestra più recente** (2 anni fa (anno successivo)). La strategia e fondata su **dati reali** (date, ticker, P&L) dettagliati sotto. **Prossimi 365 giorni**: le strategie sono state testate su un anno di filing passati e la migliore in quel periodo è raccomandata per il periodo da oggi ai prossimi 365 giorni. Obiettivo: **massimizzare il rendimento** con la strategia e l’allocazione che nel backtest hanno ottenuto il risultato più alto nella finestra più vicina a oggi.

### Raccomandazione per i prossimi 365 giorni (dati reali)

| Elemento | Valore |
|----------|--------|
| **Strategia da seguire** | CEO + Director (combo) — hold ret_high_60d_open |
| **Allocazione** | all-in sequenziale |
| **Rendimento (backtest, dati reali)** | 39.42% |
| **P&L (backtest, dati reali)** | $3,942.00 |
| **N. posizioni** | 1 |
| **Finestra in cui e stato ottenuto (date reali)** | 2 anni fa (anno successivo) |
| **Stabilità finestre** | 1/3 finestre in utile |
| **Filtro market cap** | Nessun filtro market cap (tutti i market cap) |

**Rendimento per finestra (stessa strategia):**

| Finestra | Rend.% | P&L USD |
|----------|--------|---------|
| 3 anni fa (anno successivo) | 0.00 | $0.00 |
| 2 anni fa (anno successivo) | 39.42 | $3,942.00 |
| 1 anno fa (anno successivo) | 0.00 | $0.00 |


### Out-of-sample (2 anni train / 1 anno test)

Strategia selezionata sui 2 anni di train: **CEO + Director (combo) — hold ret_high_60d_open** (avg train 19.71%). Su finestra test 1 anno fa (anno successivo) → **0.00%** (P&L $0.00).
**Come applicarla da oggi:** filtrare i cluster SEC (Form 4 P) che rispettano i criteri della strategia sopra; ordinare per data di filing (cronologico); selezionare le posizioni (fino al massimo configurato); allocare il budget secondo la modalità indicata (all-in su un trade alla volta oppure parti uguali). Uscita: al prezzo massimo raggiunto nell’orizzonte della strategia (es. ret_high_7d → hold fino al massimo a 7 giorni). Posizioni reali: vedi Dettaglio per finestra -> 2 anni fa (anno successivo). Stessa logica per i prossimi 365 giorni.

---

## Dettaglio per finestra: strategia usata e posizioni (ticker, entry, P&L)

### Finestra: 3 anni fa (anno successivo)

**Intervallo date (filing_day):** da **2023-02-27** a **2024-02-27** (365 giorni).

**Strategia migliore:** CEO + Director (combo) — hold ret_high_60d_open

**Allocazione usata (migliore nel backtest):** all-in sequenziale (tutto il capitale su ogni trade, reinvestimento al chiudere).

**Risultato:** Rendimento **0.00%** | P&L **$0.00** | **0** posizioni (nessun cluster nella finestra che rispetti i criteri).

**Come si arriva al risultato:** si selezionano i cluster con data di filing nell’intervallo sopra che rispettano i criteri della strategia; si ordinano **cronologicamente** per data filing crescente; si prendono tutte le posizioni disponibili (o si può configurare un massimo); si investe **tutto il capitale disponibile** su ogni trade (una posizione alla volta); quando un trade chiude (data di uscita = massimo nell'orizzonte), il capitale (incluso profitto) viene reinvestito nel trade successivo. Tabella sotto: ticker, data filing, entry/uscita, allocazione USD, n. azioni, ret % (nell’orizzonte), P&L USD.

Nessuna posizione in questa finestra.

---

### Finestra: 2 anni fa (anno successivo)

**Intervallo date (filing_day):** da **2024-02-27** a **2025-02-26** (365 giorni).

**Strategia migliore:** CEO + Director (combo) — hold ret_high_60d_open

**Allocazione usata (migliore nel backtest):** all-in sequenziale (tutto il capitale su ogni trade, reinvestimento al chiudere).

**Risultato:** Rendimento **39.42%** | P&L **$3,942.00** | **1** posizioni (budget $10,000 ÷ 1 = **$10,000** per titolo).

**Come si arriva al risultato:** si selezionano i cluster con data di filing nell’intervallo sopra che rispettano i criteri della strategia; si ordinano **cronologicamente** per data filing crescente; si prendono tutte le posizioni disponibili (o si può configurare un massimo); si investe **tutto il capitale disponibile** su ogni trade (una posizione alla volta); quando un trade chiude (data di uscita = massimo nell'orizzonte), il capitale (incluso profitto) viene reinvestito nel trade successivo. Tabella sotto: ticker, data filing, entry/uscita, allocazione USD, n. azioni, ret % (nell’orizzonte), P&L USD.

| Ticker | Data filing | Entry (data/ora ET (America/New_York)) | Uscita (data/ora, peak ET (America/New_York)) | Allocation USD | N. azioni | Prezzo entry | Prezzo uscita | Ret % | P&L USD |
|--------|-------------|-------------------------------|----------------------------------|----------------|-----------|--------------|----------------|-------|--------|
| STGW | 2024-02-28 | 2024-02-29 09:30 | 2024-05-02T04:00:00Z | 10000.0 | 1923.08 | 5.2 | 7.25 | 39.42 | 3942.0 |

---

### Finestra: 1 anno fa (anno successivo)

**Intervallo date (filing_day):** da **2025-02-26** a **2026-02-26** (365 giorni).

**Strategia migliore:** CEO + Director (combo) — hold ret_high_60d_open

**Allocazione usata (migliore nel backtest):** all-in sequenziale (tutto il capitale su ogni trade, reinvestimento al chiudere).

**Risultato:** Rendimento **0.00%** | P&L **$0.00** | **0** posizioni (nessun cluster nella finestra che rispetti i criteri).

**Come si arriva al risultato:** si selezionano i cluster con data di filing nell’intervallo sopra che rispettano i criteri della strategia; si ordinano **cronologicamente** per data filing crescente; si prendono tutte le posizioni disponibili (o si può configurare un massimo); si investe **tutto il capitale disponibile** su ogni trade (una posizione alla volta); quando un trade chiude (data di uscita = massimo nell'orizzonte), il capitale (incluso profitto) viene reinvestito nel trade successivo. Tabella sotto: ticker, data filing, entry/uscita, allocazione USD, n. azioni, ret % (nell’orizzonte), P&L USD.

Nessuna posizione in questa finestra.

---
