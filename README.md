# OpenAPIHub - public API directory site

A real, deployable developer directory of 1500+ public APIs, monetized through display ads and affiliate links. Built around the open-source [public-apis](https://github.com/public-apis/public-apis) dataset.

## Why this site model works for an indie operator

- Each API gets its own indexable URL, so SEO scales with the dataset
- Developer traffic commands higher ad RPMs than generic content
- Affiliate links to Vercel, Render, and Supabase convert well on developer audiences
- You do not need to write articles. Refreshing the dataset expands the site

## Run locally

```powershell
cd site
npm install   # optional, no runtime deps required
npm run fetch # refresh data/apis.json from the public-apis repo
npm start
```

Open:
- http://localhost:4781/
- http://localhost:4781/categories
- http://localhost:4781/c/development
- http://localhost:4781/api/cat-facts
- http://localhost:4781/sitemap.txt
- http://localhost:4781/robots.txt

## Configuration

Environment variables:

| Variable | Purpose | Example |
|---|---|---|
| PORT | Listen port | 4781 |
| SITE_ORIGIN | Canonical base URL | https://your-domain.com |
| SITE_NAME | Brand name | OpenAPIHub |
| ADSENSE_CLIENT | Google AdSense client id | ca-pub-1234567890 |
| AFFILIATE_VERCEL | Vercel affiliate link | https://vercel.com/?ref=yourtag |
| AFFILIATE_RENDER | Render affiliate link | https://render.com/?ref=yourtag |
| AFFILIATE_SUPABASE | Supabase affiliate link | https://supabase.com/?ref=yourtag |

## Deploy on Render

A `render.yaml` is included with:
- Node web service
- Persistent disk for /opt/data (optional cache)
- All monetization env vars kept secret

## Monetization setup

1. Apply to Google AdSense after you have meaningful content and traffic. Until approved, ad slots show a friendly placeholder.
2. Sign up for Vercel, Render, and Supabase affiliate programs:
   - Vercel affiliate is run through Impact
   - Render has a referral program
   - Supabase runs its program through Rewardful
3. Drop your links into the env vars above and redeploy.

## Reality check

- SEO traction for a new domain typically takes 3 to 12 months
- AdSense approval is not guaranteed; common rejections cite thin content
- The dataset refresh cadence is the main SEO signal, not new content
- Pure AI text pages are not added here. Each page is structured data
