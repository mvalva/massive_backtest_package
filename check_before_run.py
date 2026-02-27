"""
Verifica ambiente e configurazione prima di eseguire l'agente strategie SEC.
Esegui dalla root: python check_before_run.py

Controlla:
- Presenza e validità di .env con SEC_API_KEY e MASSIVE_API_KEY
- Dipendenze Python (pandas, requests, python-dotenv)
- Opzionale: suggerimento per una run di test veloce
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> int:
    errors: list[str] = []
    # Carica .env (root e massive_backtest)
    try:
        from dotenv import load_dotenv
        load_dotenv(ROOT / ".env")
        load_dotenv(ROOT / "massive_backtest" / ".env", override=True)
    except ImportError:
        errors.append("Modulo python-dotenv non trovato. Esegui: pip install python-dotenv")
        # Continua per verificare le chiavi via os.getenv (potrebbero essere già in ambiente)

    sec_key = os.getenv("SEC_API_KEY", "").strip()
    massive_key = os.getenv("MASSIVE_API_KEY", "").strip()

    if not sec_key:
        errors.append("SEC_API_KEY non impostata o vuota nel .env (root o massive_backtest/.env)")
    if not massive_key:
        errors.append("MASSIVE_API_KEY non impostata o vuota nel .env (root o massive_backtest/.env)")

    # Dipendenze
    for mod in ("pandas", "requests"):
        try:
            __import__(mod)
        except ImportError:
            errors.append(f"Modulo '{mod}' non trovato. Esegui: pip install -r massive_backtest/requirements.txt")

    if errors:
        print("Controllo pre-run fallito:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        print("", file=sys.stderr)
        print("Vedi CONFIGURAZIONE_API.md e AGENTE_STRATEGIE_README.md (sezione 'Prima della run').", file=sys.stderr)
        return 1

    # Verifica import modulo principale (evita errori a run avviata)
    try:
        sys.path.insert(0, str(ROOT))
        sys.path.insert(0, str(ROOT / "massive_backtest"))
        from massive_backtest.strategy_agent import run_agent, build_report, STRATEGY_DEFINITIONS_UNIFIED  # noqa: F401
    except Exception as e:
        print(f"Avviso: import strategy_agent fallito ({e}). Controlla il codice prima della run.", file=sys.stderr)
        return 1

    print("OK: .env con SEC_API_KEY e MASSIVE_API_KEY presenti; dipendenze base ok.")
    print("")
    print("Suggerimenti prima della run completa:")
    print("  - Per 3 anni di dati usa: python run_strategy_agent.py --days 1095 --max-results 15000")
    print("  - Per una prova veloce (pochi cluster): python run_strategy_agent.py --days 30 --max-results 500")
    print("")
    return 0


if __name__ == "__main__":
    sys.exit(main())
