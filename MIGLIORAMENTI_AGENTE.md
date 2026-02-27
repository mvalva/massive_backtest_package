# Suggerimenti per migliorare l'agente strategie SEC

Documento di proposta: cosa fare per rendere l'agente più utile, robusto e interpretabile, in linea con l'obiettivo di **strategia reale fondata su dati**, **massimizzare il risultato nel passato e replicarlo nel futuro**.

---

## 1. Exit price e trasparenza dati

- **Fatto:** Exit price è ora esposto ovunque (report 10K, CASES, TICKERS, CSV con colonne `exit_price` / `exit_high_Nd_open_price` ecc.).
- **Possibili miglioramenti:**
  - Nel report CASES, aggiungere una riga di legenda in cima alle tabelle: "Exit price = prezzo di uscita al massimo/minimo nell'orizzonte (entry × (1 + ret%/100))."
  - Opzione in `run_strategy_agent` per esportare un CSV "solo colonne chiave" (ticker, filing_day, entry_price, exit_price per orizzonte 7d/30d, ret%, pnl) per analisi rapide.

---

## 2. Strategia e allocazione (compounding vs no compounding)

- **Fatto:** Per ogni (finestra, strategia) si testano **all-in** (compounding) e **parti uguali** (no compounding); si usa quella con rendimento storico migliore e si mostra quale è stata scelta.
- **Possibili miglioramenti:**
  - Nel report 10K, aggiungere una mini-tabella "Confronto allocazione": per la strategia raccomandata, mostrare esplicitamente ret% e P&L con all-in vs con parti uguali (così si vede quanto ha pesato il compounding).
  - Parametro configurabile (es. `--prefer-all-in` o `--prefer-equal-weight`) per chi vuole forzare una modalità invece della scelta automatica.

---

## 3. Market cap e soglie

- **Fatto:** Soglie multiple (≥500M, ≥1B, ≥2B, ≥5B, ≥10B) testate; la migliore emerge dal ranking.
- **Possibili miglioramenti:**
  - Nel report 10K, una frase tipo "In questa run la soglia di market cap con miglior risultato nella top 10 è stata: …" (estrarre dalla strategia vincente se contiene "Large cap (≥X)").
  - Opzione per escludere dal ranking strategie con troppo pochi cluster (es. N &lt; 5) per evitare strategie "fortunate" su pochi dati.

---

## 4. Robustezza e qualità dati

- **Filtro qualità cluster:** escludere (o segnalare) cluster con entry_price nullo, ret_high mancante per l'orizzonte usato, o con dati prezzi sospetti (es. variazioni estreme in 1 giorno).
- **Gestione errori API:** retry con backoff per SEC/Massive; salvare in un CSV gli errori per ticker/filing_day così si può rieseguire solo i cluster falliti.
- **Check coerenza:** prima di scrivere i report, controllare che le colonne exit_high_Nd_open_price siano coerenti con entry_price e ret_high_Nd_open (exit = entry × (1 + ret/100)); segnalare eventuali incoerenze.

---

## 5. Strategia "prossimi 365 giorni" e backtest

- **Fatto:** Raccomandazione = migliore di tutta l'analisi (anche da finestra più vecchia); testo "nel passato" / "nel futuro" e riferimento alle posizioni reali nel Dettaglio.
- **Possibili miglioramenti:**
  - **Out-of-sample:** usare solo 2 anni per il ranking e tenere 1 anno "blind" per una stima out-of-sample della strategia raccomandata (così si vede se la strategia regge su periodo non usato per selezionarla).
  - **Stabilità:** mostrare per la strategia raccomandata in quante delle tre finestre ha dato risultato positivo (es. "3/3 finestre in utile") per segnalare consistenza.
  - **Orario/Timezone:** già indicato ET ovunque; aggiungere in README che tutti i timestamp sono in ET (America/New_York).

---

## 6. Report e usabilità

- **File step-by-step:** creare (o mantenere aggiornato) un documento **AGENTE_STRATEGIE_STEP_BY_STEP.md** che descriva in ordine: 1) caricamento SEC e cluster, 2) backtest per cluster, 3) costruzione CASES e ranking, 4) strategia 10K e tre finestre, 5) scelta della strategia per i prossimi 365 giorni, 6) output prodotti. Così è più facile analizzare e modificare il flusso.
- **Indice nei report lunghi:** per STRATEGY_AGENT_STRATEGIES.md e TICKERS.md, aggiungere in cima un indice con link alle sezioni (es. titoli ticker) per navigazione rapida.
- **CSV con separatore e encoding:** documentare in README che i CSV usano `;` come separatore e UTF-8 con BOM per Excel (già fatto nel codice).

---

## 7. Performance e parametri

- **Cache prezzi:** ridurre chiamate API ripetute per lo stesso ticker/data (già parzialmente fatto con ticker_details_cache); estendere a barre daily/minute dove possibile.
- **Parametri dalla CLI:** esporre `--top-strategies-k`, `--budget-usd`, `--lookback-days`, `--max-positions` da riga di comando (oltre a days e max-results) per test rapidi senza modificare il codice.
- **Parallelismo:** valutare esecuzione backtest in parallelo per ticker (con limite di concorrenza per non saturare le API).

---

## 8. Priorità suggerite

| Priorità | Azione |
|----------|--------|
| Alta     | Out-of-sample (2y train / 1y test) per la strategia raccomandata; indicatore "stabilità" (N/3 finestre in utile). |
| Alta     | Documento step-by-step aggiornato (AGENTE_STRATEGIE_STEP_BY_STEP.md) e README con exit price e timezone. |
| Media    | Confronto esplicito all-in vs parti uguali per la strategia raccomandata; parametri 10K da CLI. |
| Media    | Filtro qualità cluster e CSV errori per retry. |
| Bassa    | Indice nei report lunghi; opzione CSV "solo colonne chiave"; cache API estesa. |

---

*Questo file può essere aggiornato man mano che si implementano i miglioramenti o si definiscono nuove priorità.*
