# Come ottenere questi gain — strategia operativa

L’obiettivo è **realizzare i gain** che i dati mostrano (es. +1.5% in 48h per ~77% delle posizioni, +5% in 14d per ~60%, +10% in 60d per ~55%). Lo **stop loss** serve solo per non restare in posizioni molto negative, non come leva principale.

---

## 1. Idea in breve

- **Leva principale:** **take profit** (uscire quando il prezzo arriva al target).
- **Stop loss:** solo **protezione** da situazioni estreme (es. -10% / -15%), non stretto.
- In questo modo massimizzi le uscite in gain e usi lo stop solo per tagliare le posizioni “terribili”.

---

## 2. Regole operative

### Entry
- Come già fai: segnale da SEC (Form 4, acquisti P), entry al prezzo di apertura del primo giorno di borsa dopo il filing (o alla tua regola attuale).

### Take profit (dove realizzare i gain)

Scegli **uno** di questi schemi (o combinali con scale-out):

| Opzione | Target | Orizzonte | Cosa fare |
|--------|--------|-----------|-----------|
| **A – Veloce** | +1.5% o +2% | 24–48h | Ordine limite (limit sell) a entry × 1.015 (o 1.02). Se eseguito, hai realizzato il gain. |
| **B – Medio** | +3% o +5% | 7–14 giorni | Limit sell a +3% o +5%. Controllare ogni 2–3 giorni se il prezzo ha toccato il target. |
| **C – Ampio** | +7% o +10% | 30–60 giorni | Limit sell a +7% o +10%. Lasciar correre con calma. |
| **D – Scale-out** | Più target | – | Es. vendi 1/3 a +1.5%, 1/3 a +5%, 1/3 a +10% (o trailing). Così catturi sia i gain veloci sia quelli più grandi. |

In pratica: **imposta ordini limite (take profit) ai livelli che vuoi** (es. +1.5%, +2%, +5%, +10%). Quando il prezzo li tocca, vendi e il gain è realizzato.

### Stop loss (solo per non restare in posizioni terribili)

- **Non** usare uno stop stretto tipo -1.5% / -2% come leva principale: aumenterebbe le uscite in perdita prima che il prezzo possa raggiungere il target.
- Usa uno stop **largo**, solo di protezione, ad esempio:
  - **-10%** rispetto all’entry: esci solo se la posizione va molto male.
  - Oppure **-15%** se vuoi dare ancora più spazio.
- In pratica: **stop loss a -10% (o -15%)** — da impostare come ordine stop (stop loss order) o come alert + vendita manuale.

### Tempo massimo in posizione (opzionale)

- Se dopo 60 giorni non hai né take profit né stop, puoi decidere di **uscire a mercato** (es. “chiudo tutto a 60 giorni qualunque sia il prezzo”). Così eviti di tenere posizioni “zombie” a tempo indefinito.

---

## 3. Esempio concreto

- **Entry:** compri a 100 (dopo un filing SEC).
- **Take profit:**  
  - Limit sell a 101.5 (+1.5%) e/o 105 (+5%) e/o 110 (+10%), a seconda che tu scelga A, B, C o D (scale-out).
- **Stop loss:**  
  - Stop a 90 (-10%) — solo per non restare in posizioni terribili.
- **Tempo:**  
  - (Opzionale) Se a 60 giorni non sei uscito né in gain né in stop, chiudi a mercato.

Se il prezzo tocca prima 101.5, realizzi +1.5%; se tocca prima 90, esci in -10%. In mezzo non fai nulla finché non viene colpito un livello.

---

## 4. Cosa evitare

- **Stop troppo stretto** (es. -1.5%): molti trade verrebbero chiusi in perdita prima di poter toccare +1.5% o +2%, come mostrato dal backtest in scenario “stop first”.
- **Nessun take profit**: senza un target chiaro è più difficile “incassare” i gain che i dati mostrano (es. 77% che tocca +1.5% in 48h).
- **Dimenticare lo stop di protezione**: senza almeno uno stop largo (-10% / -15%) rischi di restare in posizioni molto negative (nel CSV ci sono anche max loss fino a -100%).

---

## 5. Riepilogo in una riga

**Take profit ai livelli che vuoi (es. +1.5%, +5%, +10%) + stop loss largo solo di protezione (es. -10%) + eventuale uscita a tempo (es. 60 giorni).**

In questo modo punti a ottenere i gain che i dati mostrano e usi lo stop solo per non restare in posizioni terribili.
