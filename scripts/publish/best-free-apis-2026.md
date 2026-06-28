---
title: "The 16 Best Free Public APIs in 2026 for Side Projects and Hackathons"
published: true
description: >-
  A hand-picked list of the most useful free APIs - weather, payments, maps,
  media, and more - with notes on free-tier limits and when to pick each one.
tags: webdev, api, beginners, programming
canonical_url: https://openapihub.410185103.workers.dev/best-free-apis-2026
---

Finding a good API is half the battle when you are starting a side project. You want something useful, well-documented, and ideally free enough that you can ship a demo without thinking about billing.

I went through a directory of **1581 public APIs** and picked the 16 that I would actually reach for first. Every entry below has either a real free tier or needs no key at all, and I have noted *why* you would choose each one rather than just listing names.

> This article is cross-posted from [OpenAPIHub](https://openapihub.410185103.workers.dev), a free directory of 1581 public APIs across 51 categories. Each entry below links to a deeper profile there.

## The list

### 1. [OpenWeatherMap](https://openapihub.410185103.workers.dev/api/openweathermap)

**Category:** [Weather](https://openapihub.410185103.workers.dev/c/weather) - **Auth:** needs an API key - **Transport:** HTTPS only

The default weather API. Its free tier covers 60 calls/minute and roughly a million calls per month - more than enough for most side projects. Paid plans add historical data going back years.

### 2. [Open-Meteo](https://openapihub.410185103.workers.dev/api/open-meteo)

**Category:** [Weather](https://openapihub.410185103.workers.dev/c/weather) - **Auth:** no key required - **Transport:** HTTPS only

The rare weather API that is genuinely free with no API key and no signup. You get current conditions plus a 16-day forecast for anywhere on earth. Ideal for quick demos and hackathons where you just want something working in ten minutes.

### 3. [GitHub](https://openapihub.410185103.workers.dev/api/github)

**Category:** [Development](https://openapihub.410185103.workers.dev/c/development) - **Auth:** needs an API key - **Transport:** HTTPS only

Read repos, issues, and commits without authentication, within rate limits. This is the backbone of most developer-portfolio dashboards and open-source analytics tools.

### 4. [Google Firebase](https://openapihub.410185103.workers.dev/api/google-firebase)

**Category:** [Development](https://openapihub.410185103.workers.dev/c/development) - **Auth:** needs an API key - **Transport:** HTTPS only

Realtime database, authentication, and file storage bundled into one SDK. Probably the fastest path from zero to a working mobile backend if you do not want to run your own server.

### 5. [CoinGecko](https://openapihub.410185103.workers.dev/api/coingecko)

**Category:** [Cryptocurrency](https://openapihub.410185103.workers.dev/c/cryptocurrency) - **Auth:** no key required - **Transport:** HTTPS only

Free cryptocurrency prices, market caps, and historical data. Public endpoints need no key, and the rate limits are generous enough for personal projects.

### 6. [Exchangerate.host](https://openapihub.410185103.workers.dev/api/exchangerate-host)

**Category:** [Currency Exchange](https://openapihub.410185103.workers.dev/c/currency-exchange) - **Auth:** no key required - **Transport:** HTTPS only

Free currency conversion with no key required for basic lookups. You can drop it straight into a pricing page or checkout flow.

### 7. [NASA](https://openapihub.410185103.workers.dev/api/nasa)

**Category:** [Science & Math](https://openapihub.410185103.workers.dev/c/science-math) - **Auth:** no key required - **Transport:** HTTPS only

Astronomy Picture of the Day, Mars Rover photos, and near-Earth object tracking. A genuinely fun dataset for learning REST and building visual demos.

### 8. [Unsplash](https://openapihub.410185103.workers.dev/api/unsplash)

**Category:** [Photography](https://openapihub.410185103.workers.dev/c/photography) - **Auth:** needs an API key - **Transport:** HTTPS only

High-quality, royalty-free photos behind a clean REST API. The standard choice for placeholder imagery in design tools and landing-page builders.

### 9. [Giphy](https://openapihub.410185103.workers.dev/api/giphy)

**Category:** [Photography](https://openapihub.410185103.workers.dev/c/photography) - **Auth:** needs an API key - **Transport:** HTTPS only

Search and serve GIFs. Perfect for reactions, chat apps, and adding a little life to otherwise empty UI states.

### 10. [Spotify](https://openapihub.410185103.workers.dev/api/spotify)

**Category:** [Music](https://openapihub.410185103.workers.dev/c/music) - **Auth:** needs an API key - **Transport:** HTTPS only

Rich music metadata, audio feature analysis, and track recommendations. Great for building playlists, mood detectors, or personal listening dashboards.

### 11. [TMDb](https://openapihub.410185103.workers.dev/api/tmdb)

**Category:** [Video](https://openapihub.410185103.workers.dev/c/video) - **Auth:** needs an API key - **Transport:** HTTPS only

Movie and TV metadata, posters, and cast lists. The modern successor to the older movie-database APIs.

### 12. [YouTube](https://openapihub.410185103.workers.dev/api/youtube)

**Category:** [Video](https://openapihub.410185103.workers.dev/c/video) - **Auth:** needs an API key - **Transport:** HTTPS only

Search videos, pull channel statistics, and fetch thumbnail URLs. Powers most video-aggregator and tutorial-discovery tools.

### 13. [Twitter](https://openapihub.410185103.workers.dev/api/twitter)

**Category:** [Social](https://openapihub.410185103.workers.dev/c/social) - **Auth:** needs an API key - **Transport:** HTTPS only

Post and read tweets via the v2 API. Useful for social dashboards and sentiment experiments, though it does require an API key.

### 14. [Reddit](https://openapihub.410185103.workers.dev/api/reddit)

**Category:** [Social](https://openapihub.410185103.workers.dev/c/social) - **Auth:** needs an API key - **Transport:** HTTPS only

Read public posts and comments via simple JSON endpoints. Great for trend monitors and content aggregators - no official SDK needed.

### 15. [Mapbox](https://openapihub.410185103.workers.dev/api/mapbox)

**Category:** [Geocoding](https://openapihub.410185103.workers.dev/c/geocoding) - **Auth:** needs an API key - **Transport:** HTTPS only

Maps, geocoding, and routing with a generous free tier. The go-to choice for any location-aware web application.

### 16. [REST Countries](https://openapihub.410185103.workers.dev/api/rest-countries)

**Category:** [Geocoding](https://openapihub.410185103.workers.dev/c/geocoding) - **Auth:** no key required - **Transport:** HTTPS only

Country names, flags, currencies, and calling codes. No key, no signup - the classic geographic reference dataset.

## How to choose between them

A quick heuristic that has served me well:

- **Need a working demo in an hour?** Pick [Open-Meteo](https://openapihub.410185103.workers.dev/api/open-meteo) or [REST Countries](https://openapihub.410185103.workers.dev/api/rest-countries) - zero signup, zero keys.
- **Building something real that will ship?** [OpenWeatherMap](https://openapihub.410185103.workers.dev/api/openweathermap), [GitHub](https://openapihub.410185103.workers.dev/api/github), and [Mapbox](https://openapihub.410185103.workers.dev/api/mapbox) all have free tiers that survive real usage.
- **Want a dataset that is genuinely fun?** [NASA](https://openapihub.410185103.workers.dev/api/nasa) and [Unsplash](https://openapihub.410185103.workers.dev/api/unsplash) are hard to beat for visual demos.

## Where to find more

If none of these fit, there are 1581 more in the [full OpenAPIHub directory](https://openapihub.410185103.workers.dev/), searchable and filterable by category, auth requirement, HTTPS support, and CORS. There is also an [editorial best-of page](https://openapihub.410185103.workers.dev/best-free-apis-2026) that this article is adapted from, and an [RSS feed](https://openapihub.410185103.workers.dev/feed.xml) if you want new APIs as they are added.

---

*If this list saved you time, the best thing you can do is link to [OpenAPIHub](https://openapihub.410185103.workers.dev) from your own project README or blog. Backlinks are how a free directory like this stays independent.*
