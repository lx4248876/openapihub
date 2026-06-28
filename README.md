# OpenAPIHub - public API directory site

A real, deployable developer directory of 1500+ public APIs, monetized
through display ads and affiliate links. Built around the open-source
[public-apis](https://github.com/public-apis/public-apis) dataset.

## What this is

A static site (no backend) that has:
- 1,581 real API detail pages
- 51 category pages
- Home, About, Search, 404
- sitemap.txt with 1,636 real URLs
- robots.txt
- JSON-LD structured data on every detail page
- AdSense ad slots
- Affiliate CTAs for Vercel, Render, Supabase

## Why static instead of dynamic

Static hosting on Cloudflare Pages is free and does not require a
credit card. Dynamic hosting on Render Free requires a verified
account with payment method. So this version generates the whole
site upfront into dist/ and serves only static files.

## Local development

```powershell
cd site
python ..\scripts\fetch-apis-site.py    # refresh data/apis.json
python generate_static.py               # rebuild dist/
```

To preview locally, use any static server, for example:

```powershell
cd dist
python -m http.server 4781
```

Then open http://localhost:4781/

## Environment variables (used by generate_static.py)

| Variable | Purpose | Example |
|---|---|---|
| SITE_NAME | Brand name | OpenAPIHub |
| SITE_TAGLINE | Tagline | A free directory of public APIs for developers |
| SITE_ORIGIN | Canonical public URL | https://openapihub.pages.dev |
| ADSENSE_CLIENT | AdSense client id | ca-pub-1234 |
| AFFILIATE_VERCEL | Vercel affiliate link | https://vercel.com/?ref=you |
| AFFILIATE_RENDER | Render affiliate link | https://render.com/?ref=you |
| AFFILIATE_SUPABASE | Supabase affiliate link | https://supabase.com/?ref=you |

## Deploy

Follow LAUNCH_TODO.md for step-by-step Cloudflare Pages deployment.

In short:

1. Push this repo to GitHub (already done)
2. Connect Cloudflare Pages to the GitHub repo
3. Build output directory: site/dist
4. Build command: python site/generate_static.py
5. Add environment variables
6. Deploy

## Reality check

- SEO traction for a new domain typically takes 3-12 months
- AdSense approval is not guaranteed; common rejections cite thin content
- The dataset refresh cadence is the main SEO signal
- Pure AI text pages are NOT added. Each page is structured data
