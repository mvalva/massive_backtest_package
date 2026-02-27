# Analisi strategica — Come massimizzare i gain (basata sul report)

**Fonte:** ANALISI_CSV_REPORT.txt — 1370 posizioni, max gain/loss per finestra (24h → 60d).

---

## 1. Cosa dicono i dati in sintesi

- **Rapporto gain/loss:** In ogni finestra la **media dei max gain** (in valore assoluto) è **maggiore** della media dei max loss. Es.: 24h +4.76% vs -3.35%; 60d +21.98% vs -9.32%. Il potenziale di rialzo supera, in media, il potenziale di ribasso e il rapporto migliora con l’orizzonte (a 60d circa 2,4x).
- **Probabilità di toccare una soglia di gain:** Più tieni, più sale la % di posizioni che toccano almeno +1%, +3%, +5%, +10%. Es.: +1% in 24h ≈ 80%, in 60d ≈ 94%; +5% in 24h ≈ 32%, in 60d ≈ 73%; +10% in 24h ≈ 13%, in 60d ≈ 55%.
- **Rischio di drawdown:** Allungare l’orizzonte aumenta anche la % di posizioni che toccano perdite più grosse. Es.: almeno -5% in 24h ≈ 22%, in 60d ≈ 54%; almeno -10% in 24h ≈ 7%, in 60d ≈ 32%.

Quindi: **tenere più a lungo aumenta sia la probabilità di gain alti sia la probabilità di drawdown ampi.**

---

## 2. Tre approcci strategici (coerenti con i numeri)

### A) Strategia conservativa — “Take profit basso, stop stretto”

- **Obiettivo:** Realizzare spesso un gain modesto e limitare le perdite.
- **Numeri di riferimento:**
  - ~80% delle posizioni tocca almeno +1% entro 24h, ~84% entro 48h.
  - ~69% tocca almeno +1.5% in 24h, ~77% in 48h.
  - ~69% tocca almeno -1% in 24h; ~59% almeno -1.5%.
- **Proposta operativa:**
  - **Target:** +1.5% o +2%.
  - **Orizzonte:** 24–48h (monitorare e uscire al target).
  - **Stop loss:** -1.5% o -2% (stretto).
- **Pro:** Alta probabilità di chiudere in gain; drawdown medio contenuto (-3.35% a 24h).  
- **Contro:** Rinunci a gran parte del potenziale: molte posizioni andranno oltre +2% (es. media max gain 4.76% a 24h, molto sopra +5% a 60d).

---

### B) Strategia bilanciata — “Target moderato, orizzonte 7–14 giorni”

- **Obiettivo:** Bilanciare probabilità di successo e dimensione del gain.
- **Numeri di riferimento:**
  - A 7d: ~67% tocca almeno +3%, ~51% almeno +5%; media max gain 7.83%, max loss -5.33%.
  - A 14d: ~75% almeno +3%, ~60% almeno +5%; media max gain 10.33%, max loss -6.45%.
  - A 7d ~53% tocca almeno -3%, ~37% almeno -5%.
- **Proposta operativa:**
  - **Target:** +3% o +5%.
  - **Orizzonte:** 7–14 giorni.
  - **Stop loss:** -4% / -5% (in linea con la media di max loss in quel lasso).
- **Pro:** Buona probabilità di raggiungere +3%/+5%; rapporto gain/loss ancora favorevole.  
- **Contro:** Più esposizione alla volatilità rispetto alla strategia A; alcune posizioni verranno tagliate dallo stop prima di eventuali recuperi.

---

### C) Strategia aggressiva — “Lasciar correre i winner”

- **Obiettivo:** Catturare i movimenti più grandi (+7%, +10% e oltre).
- **Numeri di riferimento:**
  - A 30d: ~60% tocca almeno +7%, ~49% almeno +10%; media max gain 14.54%, max loss -8.01%.
  - A 60d: ~66% almeno +7%, ~55% almeno +10%; media max gain 21.98%, max loss -9.32%.
  - A 60d ~32% delle posizioni tocca almeno -10%.
- **Proposta operativa:**
  - **Target:** +7% o +10% (o “10%+” lasciando correre oltre).
  - **Orizzonte:** 30–60 giorni.
  - **Stop loss:** largo (-8% / -10%) o **trailing stop** per proteggere parte del gain senza uscire troppo presto.
- **Pro:** Massimo potenziale di gain (medie 14–22%); oltre la metà delle posizioni tocca almeno +10% a 60d.  
- **Contro:** Drawdown medio alto; circa 1 posizione su 3 tocca -10% o peggio a 60d. Richiede gestione del rischio (dimensione posizione, stop, eventuale scale-out).

---

## 3. Strategia ibrida (take profit scalare + trailing)

I dati supportano l’idea di **non trattare tutte le posizioni allo stesso modo**:

1. **Prima tranche — “realizza qualcosa subito”**  
   Su una parte della posizione (es. 30–40%): target +1.5% / +2% in 24–48h, stop -1.5% / -2%. Allineata alla **strategia conservativa**.

2. **Seconda tranche — “target medio”**  
   Su un’altra parte (es. 30–40%): target +3% / +5% in 7–14 giorni, stop -4% / -5%. Allineata alla **strategia bilanciata**.

3. **Terza tranche — “let winners run”**  
   Sul resto: nessun target fisso, trailing stop (es. -3% / -4% dal massimo) o stop loss largo -8% / -10%, orizzonte fino a 30–60d. Allineata alla **strategia aggressiva**.

In questo modo usi i numeri del report: molte posizioni danno un gain veloce (soglie basse a 24–48h), una parte consistente arriva a +3%/+5% in 7–14d, e una frazione non trascurabile arriva a +7%/+10% o più su 30–60d.

---

## 4. Raccomandazione sintetica

- **Se l’obiettivo è stabilità e frequenza di gain piccoli:**  
  → **Strategia A** (target +1.5% / +2%, 24–48h, stop -1.5% / -2%).

- **Se l’obiettivo è un bilanciamento tra frequenza e dimensione del gain:**  
  → **Strategia B** (target +3% / +5%, 7–14d, stop -4% / -5%).

- **Se l’obiettivo è massimizzare il gain e puoi sopportare drawdown e volatilità:**  
  → **Strategia C** (target +7% / +10%+, 30–60d, stop largo o trailing).

- **Se vuoi combinare sicurezza e upside:**  
  → **Strategia ibrida** con scale-out su 3 tranche come sopra.

I numeri del report (medie, mediane, % aggregate per soglia e per lasso) sono coerenti con queste conclusioni e con l’uso di take profit e stop loss differenziati per orizzonte e per “slice” di posizione.
