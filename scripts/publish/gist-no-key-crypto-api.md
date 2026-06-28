# Free crypto price API with NO API key (CoinGecko) - working 2026

CoinGecko's public endpoints give you crypto prices, market caps, and historical
data without an API key. Below are working snippets.

> Found via [OpenAPIHub](https://openapihub.410185103.workers.dev/api/coingecko),
> a free directory of 1581 public APIs across 51 categories.

## Top 10 coins by market cap (no key)

```bash
curl "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
```

```javascript
const res = await fetch("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1");
const coins = await res.json();
console.log(coins.map(c => c.symbol + ": $" + c.current_price));
```

```python
import urllib.request, json
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1"
with urllib.request.urlopen(url) as r:
    coins = json.load(r)
for c in coins:
    print(c["symbol"], "$" + str(c["current_price"]))
```

## Simple price lookup for one coin

```bash
curl "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
# {"bitcoin":{"usd":67000},"ethereum":{"usd":3500}}
```

## Notes

- Public endpoints rate-limit to ~10-30 calls/min. Fine for personal projects.
- No signup, no key for read-only market data.

## Browse 1581 more free APIs

Filterable by auth / HTTPS / CORS at
[openapihub.410185103.workers.dev](https://openapihub.410185103.workers.dev).
