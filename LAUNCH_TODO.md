# OpenAPIHub - Launch on Cloudflare Pages (no credit card)

This plan uses Cloudflare Pages. It is free and does not require a credit card.
Total time: 30-45 minutes.

You already pushed the code to GitHub. Now we put it online.

------------------------------------------------------------
## Phase 1 - Sign up for Cloudflare (5 minutes)

[ ] 1.1 Go to https://dash.cloudflare.com/sign-up
[ ] 1.2 Use any email and a password
[ ] 1.3 Solve the captcha and verify your email
[ ] 1.4 You do NOT need to add a credit card. Skip any upsell.

------------------------------------------------------------
## Phase 2 - Create the Pages project (15 minutes)

[ ] 2.1 In the Cloudflare dashboard, left menu -> Workers & Pages
[ ] 2.2 Click Create -> Pages -> Connect to Git
[ ] 2.3 Connect your GitHub account if asked.
      Authorize Cloudflare to access your GitHub.
[ ] 2.4 Select the repository: lx4248876/openapihub
[ ] 2.5 Set up the build:
      - Project name: openapihub
      - Production branch: main
      - Framework preset: None
      - Build command: leave EMPTY
      - Build output directory: site/dist
        (we already committed the prebuilt site)
      - Root directory: leave EMPTY

[ ] 2.6 Click Save and Deploy
[ ] 2.7 Wait for the deploy. It takes about 1-3 minutes.
      You should see "Success" and a URL like:
      https://openapihub.pages.dev

[ ] 2.8 Click the URL. Verify:
      - Home loads
      - Click Categories
      - Click a category, e.g. Development
      - Click an API, e.g. Cat Facts
      - Visit /sitemap.txt
      - Visit /search?q=cat

[ ] 2.9 Paste your URL here:
      PAGES_URL: ____________________________________

------------------------------------------------------------
## Phase 3 - Set environment variables (5 minutes, optional)

[ ] 3.1 In Cloudflare Pages -> openapihub project -> Settings -> Environment variables

[ ] 3.2 Add (Production):
      SITE_NAME = OpenAPIHub
      SITE_TAGLINE = A free directory of public APIs for developers
      SITE_ORIGIN = https://openapihub.pages.dev
                    (use your real PAGES_URL from 2.9)
      ADSENSE_CLIENT = (leave blank until approved)
      AFFILIATE_VERCEL = https://vercel.com
      AFFILIATE_RENDER = https://render.com
      AFFILIATE_SUPABASE = https://supabase.com

[ ] 3.3 IMPORTANT: to apply these, you need a redeploy that
      actually rebuilds the static files. So also add:
      BUILD_COMMAND = python site/generate_static.py

      And change:
      Build output directory -> site/dist
      Root directory -> (your repo root, leave empty)

[ ] 3.4 Trigger a redeploy:
      Deployments -> most recent -> Retry deployment

------------------------------------------------------------
## Phase 4 - Google Search Console (10 minutes)

[ ] 4.1 Go to https://search.google.com/search-console
[ ] 4.2 Add property -> URL prefix -> paste your PAGES_URL
[ ] 4.3 Verify with HTML tag method:
      - Copy the meta tag content
      - In your repo, edit site/generate_static.py
      - In the layout function, after the canonical link, add:
        <meta name="google-site-verification" content="YOUR_TAG" />
      - Commit and push, Cloudflare will auto redeploy

[ ] 4.4 Submit sitemap:
      In Search Console -> Sitemaps -> enter: sitemap.txt -> Submit

[ ] 4.5 URL inspection -> enter your PAGES_URL -> Request indexing

------------------------------------------------------------
## Phase 5 - Custom domain (optional, costs about $10/year for a .com)

[ ] 5.1 Buy a domain at https://porkbun.com or https://namecheap.com
[ ] 5.2 In Cloudflare Pages -> openapihub -> Custom domains -> Set up a custom domain
[ ] 5.3 Cloudflare will guide you through DNS setup
[ ] 5.4 Update SITE_ORIGIN to your custom domain
[ ] 5.5 Trigger a redeploy
[ ] 5.6 Re-submit sitemap in Google Search Console

------------------------------------------------------------
## Phase 6 - Weekly maintenance

[ ] 6.1 Once a week locally:
      cd C:\Users\41018\Documents\Codex\2026-05-11\new-chat\site
      python ..\scripts\fetch-apis-site.py   # refresh data
      python generate_static.py              # rebuild dist
      git add data site\dist
      git commit -m "Weekly data refresh"
      git push

[ ] 6.2 Cloudflare auto-deploys from main branch.

------------------------------------------------------------
## Common problems

Problem: Cloudflare says build failed because Python is missing
Fix: On Cloudflare Pages, the default build environment already
includes Python 3. Check that your Build command is exactly:
python site/generate_static.py

Problem: Site deployed but styles look broken
Fix: Check that site/dist/styles.css is in the repo. If not:
git add site/dist/styles.css
git commit -m "Add styles"
git push

Problem: 404 on detail pages like /api/cat-facts
Fix: Cloudflare Pages automatically maps /api/cat-facts to
/api/cat-facts/index.html because we generated directory-style
URLs. This should just work. If not, verify the path in sitemap.txt.

Problem: Search returns no results
Fix: search-index.js must be present in site/dist/. If not,
rebuild locally and recommit.

------------------------------------------------------------
## Cost summary

- Cloudflare Pages: $0
- GitHub: $0
- Domain: ~$10/year, optional
- Google Search Console: $0
- Stripe / AdSense: paid to you when you qualify

You can launch without a credit card on file anywhere.

------------------------------------------------------------
## Final notes

This plan does not promise traffic in week 1.
Real SEO traffic for a new domain typically starts at month 3-12.
What this plan DOES give you: a real, public, indexed website
that costs $0 to operate, with real monetization slots.

If any step fails, tell me the step number and the exact error.
