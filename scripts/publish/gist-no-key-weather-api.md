# Call a free weather API with NO API key (Open-Meteo) - working in 2026

Open-Meteo is one of the few weather APIs that is genuinely free, needs no API
key, and needs no signup. Below are working snippets in 4 languages.

> Found via [OpenAPIHub](https://openapihub.410185103.workers.dev/api/open-meteo),
> a free directory of 1581 public APIs. Each entry there lists auth requirement,
> HTTPS, and CORS so you can pick an API before signing up for anything.

## Current weather for any lat/lon

```bash
curl "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m"
```

```javascript
// Node 18+ or browser - no dependencies
const res = await fetch(
  "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m"
);
const data = await res.json();
console.log(data.current); // { temperature_2m: 18.4, wind_speed_10m: 12.3 }
```

```python
import urllib.request, json
url = ("https://api.open-meteo.com/v1/forecast"
       "?latitude=52.52&longitude=13.41"
       "&current=temperature_2m,wind_speed_10m")
with urllib.request.urlopen(url) as r:
    data = json.load(r)
print(data["current"])  # {'temperature_2m': 18.4, 'wind_speed_10m': 12.3}
```

```go
package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

func main() {
	res, _ := http.Get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m")
	body, _ := io.ReadAll(res.Body)
	var data map[string]any
	json.Unmarshal(body, &data)
	fmt.Println(data["current"])
}
```

## Why this matters

Most "free" weather APIs (OpenWeatherMap, WeatherAPI) require you to register,
verify an email, and grab an API key before the first call. Open-Meteo skips all
of that — useful for hackathons, quick demos, and tutorials where you just want
something working in 30 seconds.

## More no-key APIs

Open-Meteo is not alone. Others that need zero signup:

- **[REST Countries](https://openapihub.410185103.workers.dev/api/rest-countries)** — country names, flags, currencies, calling codes
- **[Exchangerate.host](https://openapihub.410185103.workers.dev/api/exchangerate-host)** — currency conversion
- **[Dog Facts](https://openapihub.410185103.workers.dev/api/dog-facts)** — random dog facts

Browse all 1581 (filterable by auth / HTTPS / CORS) at
[openapihub.410185103.workers.dev](https://openapihub.410185103.workers.dev).
