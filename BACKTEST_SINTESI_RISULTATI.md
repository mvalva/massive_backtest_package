# Sintesi risultati backtest delle 3 strategie

**Dati:** 1370 posizioni dal CSV max_gain_loss_per_window.  
**Regola:** quando in una finestra sia il target che lo stop sono stati toccati, il backtest è stato calcolato in due modi: **A) stop colpito per primo** (conservativo), **B) target colpito per primo** (ottimistico). Lo scenario reale sarà in mezzo, a seconda dell’ordine con cui i prezzi hanno toccato le soglie.

---

## Risultati in sintesi

### Scenario A — Stop colpito per primo (conservativo)

| Strategia | Win rate % | Avg PnL % per posizione | Total PnL % (somma 1370) | Esito |
|-----------|------------|--------------------------|---------------------------|--------|
| Conservativa (24h, +1.5% / -1.5%) | 31.1 | **-0.42** | -573 | Perdita media |
| Conservativa (48h, +1.5% / -1.5%) | 29.6 | **-0.53** | -723 | Perdita media |
| Conservativa (24h, +2% / -2%) | 32.6 | **-0.36** | -492 | Perdita media |
| Conservativa (48h, +2% / -2%) | 33.1 | **-0.46** | -626 | Perdita media |
| Bilanciata (7d, +3% / -4%) | 40.8 | **-0.52** | -719 | Perdita media |
| Bilanciata (14d, +5% / -5%) | 37.7 | **-0.23** | -315 | Perdita media |
| **Aggressiva (30d, +10% / -10%)** | **36.6** | **+1.04** | **+1420** | **Profitto** |
| **Aggressiva (60d, +10% / -10%)** | **37.7** | **+0.61** | **+840** | **Profitto** |

In questo scenario **solo le strategie aggressive (30d e 60d) sono in profitto**. Le strategie conservative e bilanciate hanno più stop che target colpiti (in media) e quindi PnL medio negativo.

---

### Scenario B — Target colpito per primo (ottimistico)

| Strategia | Win rate % | Avg PnL % per posizione | Total PnL % (somma 1370) |
|-----------|------------|--------------------------|---------------------------|
| Conservativa (24h, +1.5% / -1.5%) | 69.7 | +0.74 | +1014 |
| Conservativa (48h, +1.5% / -1.5%) | 76.6 | +0.88 | +1206 |
| Conservativa (24h, +2% / -2%) | 62.3 | +0.83 | +1136 |
| Conservativa (48h, +2% / -2%) | 69.3 | +0.99 | +1358 |
| Bilanciata (7d, +3% / -4%) | 66.7 | +1.29 | +1766 |
| Bilanciata (14d, +5% / -5%) | 60.2 | +2.02 | +2765 |
| Aggressiva (30d, +10% / -10%) | 48.7 | +3.46 | +4740 |
| Aggressiva (60d, +10% / -10%) | 54.9 | +4.06 | +5560 |

Se in caso di ambiguità si assume che il target venga colpito prima dello stop, **tutte le strategie** risultano in profitto; la **bilanciata 14d** e le **aggressive** hanno i total PnL più alti.

---

## Cosa ne dedurre

1. **Ordine di esecuzione conta:** con stop prima del target (scenario A) le strategie a target basso e stop stretto perdono spesso; con target prima (scenario B) sono tutte profittevoli. Nella realtà l’ordine dipende dal path dei prezzi, quindi i risultati veri staranno **tra A e B**.

2. **Scenario conservativo (A):** solo **Aggressiva 30d** e **60d** danno **media positiva** e **total PnL positivo**. La migliore in media è Aggressiva 30d (+1.04% per posizione, +1420% totale).

3. **Scenario ottimistico (B):** la **Aggressiva 60d** ha il total PnL più alto (+5560%); la **Bilanciata 14d** ha un’ottima media (+2.02% per posizione) e un total PnL molto alto (+2765%).

4. **Strategia conservativa (24–48h):** in A perde perché molte posizioni toccano -1.5% / -2% prima di +1.5% / +2%. Per averla profittevole servirebbe che il target fosse colpito prima dello stop in una quota significativa di casi (come in B).

5. **Raccomandazione operativa:**  
   - Se vuoi essere **prudente**, usa i numeri dello **scenario A**: le uniche strategie con risultato positivo sono le **aggressive (30d e 60d, +10% / -10%)**.  
   - Se ritieni che in media il target venga spesso toccato prima dello stop, anche **conservativa** e **bilanciata** possono dare risultati positivi (scenario B); in quel caso **bilanciata 14d** e **aggressiva 60d** sono le più forti in termini di total PnL.

---

**File generati:**  
- `BACKTEST_STRATEGIE_REPORT.txt` — tabelle complete scenario A e B  
- `BACKTEST_STRATEGIE_RISULTATI.csv` — risultati scenario A in CSV  
- `backtest_strategies.py` — script per rilanciare il backtest
