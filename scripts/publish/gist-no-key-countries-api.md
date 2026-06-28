# Country list API with NO key (REST Countries) - working 2026

REST Countries gives you every country's name, flag, currency, calling code, and
borders — no API key, no signup. The classic geographic reference dataset.

> Found via [OpenAPIHub](https://openapihub.410185103.workers.dev/api/rest-countries),
> a free directory of 1581 public APIs.

## All countries (name + flag + currency)

```bash
curl "https://restcountries.com/v3.1/all?fields=name,flag,currencies"
```

```javascript
const res = await fetch("https://restcountries.com/v3.1/all?fields=name,flag,currencies");
const countries = await res.json();
console.log(countries.length + " countries"); // ~250
```

```python
import urllib.request, json
with urllib.request.urlopen("https://restcountries.com/v3.1/all?fields=name,flag,currencies") as r:
    countries = json.load(r)
print(len(countries), "countries")
```

## Lookup by name

```bash
curl "https://restcountries.com/v3.1/name/france?fields=name,capital,population"
```

## Filter by currency (find every country using the Euro)

```bash
curl "https://restcountries.com/v3.1/currency/eur?fields=name"
```

## More no-key APIs

- **[Open-Meteo](https://openapihub.410185103.workers.dev/api/open-meteo)** — free weather, no key
- **[Exchangerate.host](https://openapihub.410185103.workers.dev/api/exchangerate-host)** — free currency conversion
- **[CoinGecko](https://openapihub.410185103.workers.dev/api/coingecko)** — free crypto prices

All 1581 (filterable by auth / HTTPS / CORS):
[openapihub.410185103.workers.dev](https://openapihub.410185103.workers.dev)
