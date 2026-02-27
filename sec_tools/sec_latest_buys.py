"""
Tool: stampa le ultime transazioni SEC (solo BUY, codice P) lette dall'API sec-api.io insider-trading.
Usa SEC_API_KEY da ambiente o .env (come gli altri script del progetto).

Uso:
    python sec_latest_buys.py
    python sec_latest_buys.py --days 3 --limit 100
"""

from __future__ import annotations

import os
import sys
import argparse
import datetime as dt

try:
    import requests
except ImportError:
    print("Installa requests: pip install requests", file=sys.stderr)
    sys.exit(1)

# carica .env da root progetto
try:
    from dotenv import load_dotenv
    from pathlib import Path
    _root = Path(__file__).resolve().parent.parent
    load_dotenv(_root / ".env")
    load_dotenv(_root / "massive_backtest" / ".env", override=True)
    load_dotenv()
except Exception:
    pass

API_URL = "https://api.sec-api.io/insider-trading"
BUY_CODES = {"P"}  # P = open market or private purchase (solo acquisti)


def get_key() -> str:
    k = os.getenv("SEC_API_KEY")
    if not k:
        print("ERRORE: SEC_API_KEY non impostata. Mettila in .env o nell'ambiente.", file=sys.stderr)
        sys.exit(1)
    return k


def fetch_transactions(
    key: str,
    days: int,
    page_size: int,
    max_results: int,
    only_buy_p: bool = True,
    start_date: str | None = None,
    end_date: str | None = None,
) -> list:
    """
    Chiama l'API insider-trading.
    - days: se usato da solo, indica la lunghezza della finestra (ultimi N giorni).
    - start_date/end_date: se forniti, hanno priorità su days e permettono di spezzare il range in più finestre.
    """
    today = dt.date.today()
    if start_date and end_date:
        start = start_date
        end = end_date
    else:
        # days=1 → solo oggi (start=oggi, end=domani). days>1 → ultimi N giorni.
        if days == 1:
            start = today.isoformat()
            end = (today + dt.timedelta(days=1)).isoformat()
        else:
            start = (today - dt.timedelta(days=days)).isoformat()
            end = (today + dt.timedelta(days=1)).isoformat()
    # Query ufficiale sec-api: solo filing che contengono almeno una transazione con coding.code=P
    if only_buy_p:
        query = f"nonDerivativeTable.transactions.coding.code:P AND filedAt:[{start} TO {end}]"
    else:
        query = f"filedAt:[{start} TO {end}]"
    page_size = min(page_size, 50)  # API max 50
    out: list = []
    cursor = 0
    # max_results <= 0 = nessun limite lato client: continua finché l'API restituisce dati.
    limit = max_results if max_results and max_results > 0 else None
    while True:
        payload = {
            "query": query,
            "from": str(cursor),
            "size": str(page_size),
            "sort": [{"filedAt": {"order": "desc"}}],
        }
        r = requests.post(API_URL, json=payload, headers={"Authorization": key}, timeout=60)
        if r.status_code != 200:
            print(f"API error {r.status_code}: {r.text[:300]}", file=sys.stderr)
            break
        data = r.json()
        txs = data.get("transactions") or []
        if not txs:
            break
        for t in txs:
            out.append(t)
        # Se abbiamo un limite client e l'abbiamo raggiunto, tronchiamo e usciamo.
        if limit is not None and len(out) >= limit:
            if len(out) > limit:
                out = out[:limit]
            break
        cursor += len(txs)
        if len(txs) < page_size:
            break
    return out


def extract_buys(transactions: list) -> list[dict]:
    """Da ogni transaction estrae le righe con codice P (buy); una riga per ogni transazione non-derivative P."""
    rows = []
    for t in transactions:
        issuer = (t.get("issuer") or {})
        raw_owner = t.get("reportingOwner") or t.get("reportingOwners")
        if isinstance(raw_owner, list) and raw_owner:
            owner = raw_owner[0]
        else:
            owner = raw_owner if isinstance(raw_owner, dict) else {}
        rel = (owner.get("relationship") or {})
        title = rel.get("officerTitle") or owner.get("officerTitle") or ""
        if not title:
            if rel.get("isDirector"):
                title = "Director"
            elif rel.get("isOfficer"):
                title = "Officer"
            elif rel.get("isTenPercentOwner"):
                title = "10% Owner"
            elif rel.get("isOther"):
                title = "Other"
        if not title and isinstance(rel, dict):
            for k in ("officerTitle", "title"):
                if rel.get(k):
                    title = str(rel.get(k))
                    break
        nd = (t.get("nonDerivativeTable") or {}).get("transactions") or []
        for x in nd:
            # sec-api: coding.code; alcuni endpoint usano transactionCode
            code = (x.get("coding") or {}).get("code") or x.get("transactionCode") or ""
            code = str(code).strip().upper()
            if code not in BUY_CODES:
                continue
            amounts = (x.get("amounts") or {})
            shares = amounts.get("shares")
            price = amounts.get("pricePerShare")
            value = amounts.get("value")
            if shares is not None and price is not None:
                try:
                    value = float(shares) * float(price)
                except Exception:
                    pass
            # Variazione % posizione: shares dopo - shares acquistate = prima; increase % = 100 * (acquistate / prima)
            post = (x.get("postTransactionAmounts") or {})
            shares_after = post.get("sharesOwnedFollowingTransaction")
            pct_increase_position = None
            if shares is not None and shares_after is not None:
                try:
                    q = float(shares)
                    after = float(shares_after)
                    before = after - q
                    if before and before > 0:
                        pct_increase_position = round(100.0 * (q / before), 2)
                except (TypeError, ValueError):
                    pass
            rows.append({
                "filedAt": t.get("filedAt") or "",
                "tradeDate": x.get("transactionDate") or t.get("periodOfReport") or "",
                "ticker": issuer.get("tradingSymbol") or "",
                "company": issuer.get("name") or "",
                "insider": owner.get("name") or "",
                "title": title,
                "code": code,
                "qty": shares,
                "price": price,
                "value": value,
                "link": t.get("linkToFilingDetails") or "",
                "pct_increase_position": pct_increase_position,
            })
    return rows


def main():
    ap = argparse.ArgumentParser(description="Ultime transazioni SEC solo BUY (API sec-api.io)")
    ap.add_argument("--days", type=int, default=7, help="Giorni indietro per filedAt (default 7)")
    ap.add_argument("--limit", type=int, default=200, help="Max transazioni API da leggere (default 200)")
    ap.add_argument("--page-size", type=int, default=50, help="Page size API (max 50)")
    ap.add_argument("--all", action="store_true", help="Scarica tutte le transazioni (poi filtra P); default: query API solo per codice P")
    args = ap.parse_args()

    key = get_key()
    only_p = not args.all
    print(f"Fetch ultimi {args.days} giorni (query solo codice P: {only_p}, max {args.limit} filing)...", file=sys.stderr)
    txs = fetch_transactions(key, args.days, args.page_size, args.limit, only_buy_p=only_p)
    buys = extract_buys(txs)
    print(f"Transazioni lette: {len(txs)} | Solo BUY (codice P): {len(buys)}\n", file=sys.stderr)

    if not buys:
        print("Nessun acquisto trovato nel periodo.")
        return

    # Print tabella
    col_widths = {"filedAt": 22, "tradeDate": 12, "ticker": 8, "company": 28, "insider": 22, "title": 18, "code": 4, "qty": 10, "price": 8, "value": 12}
    header = f"{'Filing Date':<22} {'Trade Date':<12} {'Ticker':<8} {'Company':<28} {'Insider':<22} {'Title':<18} {'Code':<4} {'Qty':>10} {'Price':>8} {'Value':>12}"
    print(header)
    print("-" * len(header))
    for r in buys:
        qty_s = str(r["qty"]) if r["qty"] is not None else ""
        price_s = f"{float(r['price']):.2f}" if r["price"] is not None else ""
        value_s = f"${float(r['value']):,.0f}" if r["value"] is not None else ""
        print(
            f"{(r['filedAt'] or '')[:22]:<22} {(str(r['tradeDate']) or '')[:12]:<12} {r['ticker']:<8} {r['company'][:28]:<28} {r['insider'][:22]:<22} {r['title'][:18]:<18} {r['code']:<4} {qty_s:>10} {price_s:>8} {value_s:>12}"
        )
    print()
    print(f"Link primo filing: {buys[0].get('link', '')}" if buys else "")


if __name__ == "__main__":
    main()
