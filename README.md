# OpenAPIHub

> A free, searchable directory of **1,581 public APIs** across 51 categories — with HTTPS, auth, and CORS metadata for every entry.

**Live site:** https://openapihub.410185103.workers.dev

Built for developers who want to find the right API fast, without wading through
bloated marketplaces or paywalled directories. Every entry links to real
documentation. No signup, no tracking, no upsell.

---

## Why you might actually use this

- **1,581 real APIs**, each with its own detail page — not a flat list. Every page
  shows category, auth requirement (apiKey / OAuth / none), HTTPS support, CORS
  status, and a direct link to the official docs.
- **51 categories** — Weather, Cryptocurrency, Geocoding, Music, Games, Machine
  Learning, Open Data, and more. Browse a category and see every API in it at a
  glance.
- **Client-side search** — the full directory is searchable in-browser with no
  server round-trip. Type "weather" or "crypto" and filter instantly.
- **An editorial best-of page** — [`/best-free-apis-2026`](https://openapihub.410185103.workers.dev/best-free-apis-2026)
  picks the 16 APIs worth reaching for first (OpenWeatherMap, GitHub, NASA,
  Unsplash, CoinGecko, …) with notes on *when* to choose each one.
- **Related APIs on every detail page** — see 3 same-category alternatives
  without leaving the page.
- **RSS feed** — subscribe to [`/feed.xml`](https://openapihub.410185103.workers.dev/feed.xml)
  in feedly or Inoreader to get new APIs as they are added.

## What is in this repo

| Path | What it is |
|---|---|
| `generate_static.py` | The static site generator. Reads `data/apis.json`, writes `dist/`. |
| `data/apis.json` | 1,581 API records (name, slug, description, category, auth, https, cors, url). |
| `dist/` | The generated, deployable static site (~1,640 files). |
| `wrangler.toml` + `src/worker.js` | Cloudflare Workers config. The Worker is a thin stub; static files are served via the `[assets]` binding. |
| `scripts/gen_article.py` | Regenerates the dev.to-ready backlink article from the dataset. |
| `scripts/publish/` | A ready-to-publish Markdown article + a guide for building dofollow backlinks via dev.to / Hashnode. |
| `REVENUE.md` | The phased monetization roadmap. |

## Built the right way

- **Static.** No database, no runtime, no attack surface. Free to host forever
  on Cloudflare Workers — no credit card required.
- **SEO-complete.** Open Graph + Twitter cards sitewide, `WebSite` + `SearchAction`
  JSON-LD on the home page, `ItemList` on category pages, `WebAPI` + `BreadcrumbList`
  on detail pages, `FAQPage` on the editorial page, and a structured
  `sitemap.xml` with lastmod for all 1,637 URLs.
- **Fast.** Pure HTML/CSS, one tiny JS file for search. Lighthouse-friendly by
  construction.
- **Not AI slop.** Every page is generated from structured data, not from a
  language model hallucinating endpoints. The editorial notes are hand-written
  opinions on APIs that genuinely exist in the dataset.

## Run it locally

```powershell
cd site
python generate_static.py      # rebuild dist/ from data/apis.json
cd dist
python -m http.server 4781
```

Then open http://localhost:4781/

## Deploy your own

This repo is already wired to deploy on push. To deploy your own copy:

1. Fork it.
2. Connect the repo to Cloudflare Workers (dash.cloudflare.com → Workers →
   Create → Connect to Git). Build command: `python site/generate_static.py`.
   Build output: `site/dist`.
3. That is it. Cloudflare rebuilds and deploys on every push.

## Monetization

Five channels are wired in `generate_static.py`, each enabled by setting an
environment variable before build (see `.env.example`):

- **AdSense** (`ADSENSE_CLIENT`) — four ad slots auto-populate.
- **Affiliate links** (`AFFILIATE_VERCEL` / `AFFILIATE_RENDER` / `AFFILIATE_SUPABASE`) —
  every outbound affiliate click is UTM-stamped for attribution.
- **Newsletter capture** (`NEWSLETTER_FORM_URL`) — homepage dark hero card,
  works with Buttondown or ConvertKit.
- **Tip jar** (`DONATE_URL`) — footer + sidebar CTA.
- **Analytics** (`CF_ANALYTICS_TOKEN` or `PLAUSIBLE_DOMAIN`) — cookieless.

None of these are active until you set the variables, so the default build
ships clean with no third-party scripts.

## Data source

Built around the open-source [public-apis](https://github.com/public-apis/public-apis)
dataset, enriched and structured for a browsable directory.

## License

MIT for the code and site structure. API metadata follows the upstream
public-apis dataset license.
