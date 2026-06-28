# OpenAPIHub - Launch TODO

Read this top to bottom. Do them in order. Do not skip steps.
Each step tells you: where to click, what to type, and how to verify it worked.
Estimated total time: 60-90 minutes if you do not get stuck on naming.

------------------------------------------------------------
## Phase 0 - Local final check (5 minutes)

Goal: confirm the site still runs before pushing.

[ ] 0.1 Open PowerShell in this folder:
    C:\Users\41018\Documents\Codex\2026-05-11\new-chat\site

[ ] 0.2 Run:
    node src\server.js

[ ] 0.3 Open these in your browser. All should load:
    - http://localhost:4781/
    - http://localhost:4781/categories
    - http://localhost:4781/c/development
    - http://localhost:4781/api/cat-facts
    - http://localhost:4781/sitemap.txt

[ ] 0.4 Stop the server with Ctrl+C in PowerShell.

If any page is broken, stop and tell me before continuing.

------------------------------------------------------------
## Phase 1 - GitHub repository (10 minutes)

Goal: put the code on GitHub so Render can deploy it.

[ ] 1.1 Sign in to https://github.com
    If you do not have an account, create one (free).

[ ] 1.2 Click the + icon in the top right -> New repository

[ ] 1.3 Fill in:
    - Repository name: openapihub
    - Description: A free directory of public APIs for developers
    - Public (recommended, Render free tier needs public repo)
    - DO NOT check "Add a README"
    - DO NOT add .gitignore (we already have one)

[ ] 1.4 Click Create repository

[ ] 1.5 On the next page, GitHub shows you commands under
    "…or push an existing repository from the command line".
    You will see a URL like:
    https://github.com/your-username/openapihub.git
    Copy that URL. Paste it here so you do not lose it:
    YOUR_REPO_URL: ____________________________________

[ ] 1.6 In PowerShell, inside the site folder, run:
    git remote add origin https://github.com/YOUR_USERNAME/openapihub.git
    git branch -M main
    git push -u origin main

    Replace YOUR_USERNAME with your real GitHub username.

[ ] 1.7 Refresh the GitHub repo page. You should see your files
    including src/server.js and data/apis.json.

------------------------------------------------------------
## Phase 2 - Pick a domain (10 minutes, optional but recommended)

Goal: have a real domain for SEO.

[ ] 2.1 Buy a domain at one of:
    - https://www.namecheap.com
    - https://www.porkbun.com
    - https://www.cloudflare.com/products/registrar/

    Pick something brandable, short, .com preferred.
    Examples of the style: openapihub.com, apifind.com, useapis.dev

[ ] 2.2 Write your domain here:
    YOUR_DOMAIN: ____________________________________

    If you skip the domain for now, Render gives you a free
    subdomain like openapihub.onrender.com which is fine to start.

------------------------------------------------------------
## Phase 3 - Sign up for affiliate programs (20 minutes)

Goal: get real links that pay you.

[ ] 3.1 Vercel affiliate program
    Go to: https://vercel.com/affiliates
    Sign up. They run it through Impact (https://app.impact.com).
    After approval, get your Vercel affiliate URL.
    Paste it here:
    AFFILIATE_VERCEL: ____________________________________

[ ] 3.2 Render referral
    Go to: https://render.com referral dashboard inside your Render account.
    Get your referral link.
    Paste it here:
    AFFILIATE_RENDER: ____________________________________

[ ] 3.3 Supabase
    Go to: https://supabase.com/affiliates
    Sign up. They run it through Rewardful.
    Get your Supabase affiliate URL.
    Paste it here:
    AFFILIATE_SUPABASE: ____________________________________

If any of them reject you or take time, that is OK. Skip that one
and use the default URL. You can fill it in later.

------------------------------------------------------------
## Phase 4 - Sign up for Google AdSense (5 minutes, comes later)

Goal: get ad revenue. This step takes longer in real time.

[ ] 4.1 Go to: https://www.google.com/adsense/start/
[ ] 4.2 Sign in with your Google account
[ ] 4.3 Add your site URL (after Phase 5 deploy)
[ ] 4.4 Google will review. This typically takes days to weeks.
[ ] 4.5 After approval, get your client id, format ca-pub-XXXXXXXXX
    Paste it here:
    ADSENSE_CLIENT: ____________________________________

AdSense will likely reject your first application because the
domain is new. That is normal. Reapply after 30 days and 10+ good
posts/refreshes. Until then ad slots show a friendly placeholder.

------------------------------------------------------------
## Phase 5 - Deploy to Render (20 minutes)

Goal: get a public URL.

[ ] 5.1 Go to: https://render.com
[ ] 5.2 Sign up with your GitHub account
[ ] 5.3 Click New + -> Web Service
[ ] 5.4 Connect your GitHub account if asked
[ ] 5.5 Find and select your openapihub repo
[ ] 5.6 Settings:
    - Name: openapihub
    - Region: closest to you
    - Branch: main
    - Runtime: Node
    - Build Command: leave blank or "true" (we have no deps)
    - Start Command: node src/server.js
    - Instance Type: Free

[ ] 5.7 Scroll down to Environment Variables. Add these:

    Key                       Value
    -------------------------------------------------------
    NODE_VERSION              24.14.0
    SITE_NAME                 OpenAPIHub
    SITE_ORIGIN               https://openapihub.onrender.com
                              (replace with your Render URL after first deploy)
    ADSENSE_CLIENT            (paste from 4.5, or leave blank)
    AFFILIATE_VERCEL          (paste from 3.1)
    AFFILIATE_RENDER          (paste from 3.2)
    AFFILIATE_SUPABASE        (paste from 3.3)

[ ] 5.8 Click Create Web Service
[ ] 5.9 Wait for the build to finish. Watch the logs.
    You should see:
    OpenAPIHub running on port 10000
    Loaded 1581 APIs across 51 categories

[ ] 5.10 When status is Live, click the URL Render gives you at
    the top. Open it. Verify:
    - Home page loads
    - Click Categories
    - Click a category
    - Click an API
    - sitemap.txt loads at /sitemap.txt

[ ] 5.11 After deploy, copy your Render URL
    (something like https://openapihub.onrender.com)
    Paste it here:
    RENDER_URL: ____________________________________

[ ] 5.12 Go back to your service -> Environment
    Update SITE_ORIGIN to your real Render URL
    Trigger a manual deploy (Manual Deploy -> Deploy latest commit)

------------------------------------------------------------
## Phase 6 - Google Search Console (15 minutes)

Goal: tell Google you exist.

[ ] 6.1 Go to: https://search.google.com/search-console
[ ] 6.2 Add a property -> URL prefix -> paste your Render URL
[ ] 6.3 Verify. Easiest method is HTML tag:
    - Copy the meta tag Google gives you
    - In your repo, edit src/server.js
    - Find the layout function, inside <head> add the meta tag
    - Commit and push, Render will redeploy

[ ] 6.4 After verification, submit your sitemap:
    In Search Console -> Sitemaps -> Add new sitemap
    Enter: sitemap.txt
    Submit

[ ] 6.5 Request indexing for your homepage:
    URL inspection -> enter your home URL -> Request indexing

------------------------------------------------------------
## Phase 7 - Custom domain (10 minutes, optional)

Goal: move from openapihub.onrender.com to yourdomain.com

[ ] 7.1 In Render -> your service -> Settings -> Custom Domains
[ ] 7.2 Add your domain
[ ] 7.3 Render gives you DNS records (CNAME or A)
[ ] 7.4 Add those records at your domain registrar's DNS panel
[ ] 7.5 Wait for DNS to propagate (minutes to hours)
[ ] 7.6 Update SITE_ORIGIN env var to your custom domain
[ ] 7.7 Update Google Search Console to add the custom domain
    and submit sitemap.txt again

------------------------------------------------------------
## Phase 8 - Weekly maintenance (ongoing)

Goal: keep content fresh. Google rewards consistency.

[ ] 8.1 Once a week, locally run:
    cd C:\Users\41018\Documents\Codex\2026-05-11\new-chat\site
    npm run fetch
    git add data/apis.json
    git commit -m "Weekly data refresh"
    git push

[ ] 8.2 Render auto-deploys from main branch.

[ ] 8.3 Once a month, check Search Console for new queries
    your site is showing up for.

------------------------------------------------------------
## Common problems

Problem: git push asks for password
Fix: GitHub no longer accepts password auth. Use a Personal Access
Token from Settings -> Developer settings -> Personal access tokens.

Problem: Render build fails
Fix: Check logs. The most common cause is wrong Start Command.
It must be exactly: node src/server.js

Problem: Site loads but styles look broken
Fix: Make sure public/styles.css is in the repo. If not, run:
git add public/styles.css
git commit -m "Add styles"
git push

Problem: AdSense rejected
Fix: This is normal. Continue refreshing content weekly.
Reapply after 30 days.

Problem: No SEO traffic after 1 month
Fix: This is expected. Real SEO traffic for a new domain starts
showing between months 3 and 12. Keep refreshing data weekly.

------------------------------------------------------------
## Final notes

This plan is honest. It does not promise money in week 1.
It does promise: a real, deployable site, with real data,
with real monetization slots, in less than 2 hours of clicking.

If any step blocks you, tell me which step number and what error
you see, and I will fix it.
