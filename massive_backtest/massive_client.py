"""
Client per Massive.com (ex Polygon.io) API.
Barre OHLC (aggregates) in Eastern Time; supporto pre-market, regular, after-hours.
Vedi: https://polygon.io/docs/rest/stocks/aggregates/custom-bars
"""

from __future__ import annotations

import os
from datetime import datetime, timedelta

try:
    import requests
except ImportError:
    requests = None

MASSIVE_BASE = "https://api.polygon.io"
# Alternative: https://api.massive.com (stessa chiave)


def get_api_key() -> str | None:
    key = os.getenv("MASSIVE_API_KEY", "").strip()
    return key or None


def fetch_aggs(
    ticker: str,
    from_ts: str,
    to_ts: str,
    multiplier: int = 5,
    timespan: str = "minute",
    limit: int = 50000,
    adjusted: bool = True,
) -> tuple[list[dict], str | None]:
    """
    Barre OHLC per un ticker in un intervallo. Ritorna (lista barre, messaggio_errore); errore non None in caso di fallimento.
    from_ts, to_ts: YYYY-MM-DD oppure timestamp in millisecondi.
    multiplier × timespan = es. 5 minute, 1 day.
    Ritorna lista di dict con t (ms), o, h, l, c, v, vw, n.
    """
    if not requests or not get_api_key():
        return [], "Modulo requests o MASSIVE_API_KEY mancante"
    ticker = (ticker or "").strip().upper()
    if not ticker:
        return [], "Ticker vuoto"
    url = f"{MASSIVE_BASE}/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_ts}/{to_ts}"
    params = {
        "apiKey": get_api_key(),
        "adjusted": "true" if adjusted else "false",
        "sort": "asc",
        "limit": min(limit, 50000),
    }
    try:
        r = requests.get(url, params=params, timeout=30)
        if r.status_code != 200:
            msg = f"HTTP {r.status_code}"
            try:
                body = r.json()
                if isinstance(body, dict) and body.get("error"):
                    msg = body.get("error") or msg
                if isinstance(body, dict) and body.get("message"):
                    msg = body.get("message") or msg
            except Exception:
                pass
            return [], msg
        data = r.json()
        results = data.get("results") or []
        return results, None
    except requests.exceptions.Timeout:
        return [], "Timeout richiesta Massive"
    except requests.exceptions.RequestException as e:
        return [], f"Errore rete Massive: {e}"
    except Exception as e:
        return [], f"Errore Massive: {type(e).__name__}: {e}"


def fetch_daily_aggs(ticker: str, from_date: str, to_date: str) -> tuple[list[dict], str | None]:
    """Barre daily (1 day). Ritorna (barre, errore); errore non None in caso di fallimento."""
    return fetch_aggs(ticker, from_date, to_date, multiplier=1, timespan="day", limit=5000)


def fetch_minute_aggs(
    ticker: str, from_date: str, to_date: str, minute_multiplier: int = 5
) -> tuple[list[dict], str | None]:
    """Barre intraday (5min default). Ritorna (barre, errore)."""
    return fetch_aggs(
        ticker, from_date, to_date, multiplier=minute_multiplier, timespan="minute", limit=50000
    )


def fetch_ticker_details(ticker: str, date: str | None = None) -> tuple[dict | None, str | None]:
    """
    Dettagli ticker da Reference API (market_cap, list_date, primary_exchange, sic_code, sic_description).
    date: YYYY-MM-DD opzionale per point-in-time. Ritorna (results dict, errore).
    """
    if not requests or not get_api_key():
        return None, "Modulo requests o MASSIVE_API_KEY mancante"
    ticker = (ticker or "").strip().upper()
    if not ticker:
        return None, "Ticker vuoto"
    url = f"{MASSIVE_BASE}/v3/reference/tickers/{ticker}"
    params = {"apiKey": get_api_key()}
    if date:
        params["date"] = date[:10]
    try:
        r = requests.get(url, params=params, timeout=15)
        if r.status_code != 200:
            msg = f"HTTP {r.status_code}"
            try:
                body = r.json()
                if isinstance(body, dict) and body.get("error"):
                    msg = body.get("error") or msg
                if isinstance(body, dict) and body.get("message"):
                    msg = body.get("message") or msg
            except Exception:
                pass
            return None, msg
        data = r.json()
        results = data.get("results")
        return results, None
    except requests.exceptions.Timeout:
        return None, "Timeout richiesta Massive"
    except requests.exceptions.RequestException as e:
        return None, f"Errore rete Massive: {e}"
    except Exception as e:
        return None, f"Errore Massive: {type(e).__name__}: {e}"
