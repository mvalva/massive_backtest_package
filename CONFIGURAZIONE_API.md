# Dove sostituire le API (Massive e SEC)

Per usare il backtest e gli strumenti SEC servono **due chiavi**:

| Variabile        | Uso                    | Dove ottenerla        |
|------------------|------------------------|------------------------|
| **MASSIVE_API_KEY** | Prezzi, OHLC, ticker (Massive.com / Polygon) | https://massive.com o https://polygon.io |
| **SEC_API_KEY**    | Filing SEC Form 4, acquisti insider (sec-api.io) | https://sec-api.io |

---

## Dove mettere le chiavi

1. **File `.env` nella root del progetto**  
   Percorso: `massive_backtest_package/.env`

   Apri (o crea) quel file e imposta:
   ```env
   MASSIVE_API_KEY=la_tua_chiave_massive
   SEC_API_KEY=la_tua_chiave_sec
   ```

2. **In alternativa: `massive_backtest/.env`**  
   L’app Streamlit legge anche da qui. Puoi avere solo questo, o entrambi.

---

## Sostituire le chiavi

- Per **cambiare** la chiave Massive: modifica `MASSIVE_API_KEY` nel `.env` (root o `massive_backtest/`).
- Per **cambiare** la chiave SEC: modifica `SEC_API_KEY` nello stesso file.

Non mettere le chiavi nel codice sorgente: usare sempre il file `.env` (che di solito non viene committato).

---

## Riferimento

Il file **`env_template.txt`** nella root contiene un esempio delle variabili da copiare nel `.env`.

**Prima della prima run:** dalla root del progetto esegui `python check_before_run.py` per verificare che le chiavi siano caricate e le dipendenze installate (vedi **AGENTE_STRATEGIE_README.md** → sezione «Prima della run»).
