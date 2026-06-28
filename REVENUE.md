# OpenAPIHub — Revenue Roadmap (honest, no bullshit)

This site is live at `https://openapihub.410185103.workers.dev`.
Zero hosting cost (Cloudflare free tier). Every monetization hook is **already
wired in code** and activates the moment you fill in the matching env var.

## Reality check first

A directory site makes money in this order, and **not faster**:

1. **Phase 0 — wiring** (DONE in code, this commit): analytics, affiliate
   tracking, donate button, ad slots. Costs $0, earns $0 until traffic +
   your accounts exist.
2. **Phase 1 — affiliate + tips (weeks 1–4)**: real money *can* start the day
   you sign up for affiliate programs and a tip jar. You earn only when
   someone clicks your link AND signs up. Needs *some* traffic to convert.
3. **Phase 2 — SEO traffic (months 1–6)**: Google indexes the 1633 pages,
   organic search brings visitors. This is where real volume comes from.
4. **Phase 3 — AdSense (month 3+)**: apply once you have ~50+ daily visitors
   and original content. Often rejected first try — add content, reapply.

**There is no path that earns money today without (a) traffic and (b) your own
accounts on the affiliate/ad networks.** Anyone telling you otherwise is lying.

---

## Phase 1 — do this now (30 min, $0, pays out for real)

### 1. Tip jar (instant payout, no approval)
- Go to https://www.buymeacoffee.com (or ko-fi.com) → sign up → grab your link
  (looks like `https://www.buymeacoffee.com/yourhandle`)
- Set env var: `DONATE_URL=https://www.buymeacoffee.com/yourhandle`
- The orange "Support this project" button + "Buy me a coffee" link appear on
  every page. Pays you directly via PayPal/Stripe. No middleman approval.

### 2. Affiliate programs (commission on signups)
Each provider has a referral program. Sign up, copy YOUR link, set the env var:

| Provider   | Sign up at                              | Env var to set |
|------------|-----------------------------------------|----------------|
| Vercel     | https://vercel.com/referral             | `AFFILIATE_VERCEL=https://vercel.com/?ref=YOUR_ID` |
| Render     | https://render.com/referral             | `AFFILIATE_RENDER=https://render.com/?ref=YOUR_ID` |
| Supabase   | https://supabase.com/partners           | `AFFILIATE_SUPABASE=https://supabase.com/?ref=YOUR_ID` |

All clicks are auto-stamped with `utm_source=openapihub&utm_medium=affiliate`
so you can see in the provider's dashboard which pages convert. Example of a
fully-wired link after rebuild:
`https://vercel.com/?ref=YOUR_ID&utm_source=openapihub&utm_medium=affiliate&utm_campaign=detail-deploy`

### 2b. Email newsletter (the highest-ROI asset, do this early)
A subscriber list is worth 10-50x the ad revenue per user, needs NO approval,
and compounds. Sign up free at https://buttondown.email (purpose-built for
developer newsletters, free up to 100 subscribers):
- Create a newsletter -> Settings -> copy the **form action URL**
- Set env var: `NEWSLETTER_FORM_URL=https://buttondown.email/api/emails/yournews`
- The dark "Get one new API worth integrating, every week" capture card appears
  on the homepage. Visitors who subscribe become a re-marketable asset you can
  email forever — promote affiliate deals, your own products, paid content.
- Later: email the list weekly with "API of the week" + your affiliate links.

### 3. Free analytics (see what actually gets traffic)
- Cloudflare dashboard → **Web Analytics** → **Add a site** → paste your
  `*.workers.dev` URL → copy the `token` from the snippet
- Set env var: `CF_ANALYTICS_TOKEN=that_token`
- Cookieless, free, no consent banner needed. Tells you which of the 1581 API
  pages actually get visitors, so you know what to optimize.

---

## Phase 2 — get traffic (the actual money lever, months 1–6)

Without traffic, Phase 1 earns ~$0. Traffic sources, easiest first:

1. **Google Search Console** (free, do today):
   - https://search.google.com/search-console → add property → enter
     `https://openapihub.410185103.workers.dev`
   - Verify (DNS or HTML file — Workers makes the file method easy)
   - Submit `https://openapihub.410185103.workers.dev/sitemap.txt`
   - Wait 1–6 weeks for indexing. The 1633 pages are your asset.
2. **Programmatic SEO**: each `/api/<slug>` and `/c/<category>` page targets a
   long-tail search ("weather API free", "cat facts API", etc.). 1581 pages =
   1581 chances to rank. The generator already writes unique titles, meta
   descriptions, canonical URLs, and JSON-LD — that's most of the SEO work.
3. **Backlinks**: post the site on Hacker News, Reddit r/webdev, dev.to,
   Product Hunt, GitHub awesome-lists. One good HN submission > months of SEO.
4. **Custom domain** (later, ~$10/yr): a `.com` ranks better than
   `*.workers.dev`. Cloudflare sells domains at cost.

---

## Phase 3 — AdSense (only after traffic exists)

Do NOT apply before ~50 daily visitors + some original content, or you'll be
rejected and it's harder to get approved later. When ready:

1. https://adsense.google.com → sign up with the site URL
2. Get approved (1–14 days, often rejected first try — add a blog, reapply)
3. Copy your publisher ID (`ca-pub-XXXXXXXXXXXXXXXX`)
4. Set env var: `ADSENSE_CLIENT=ca-pub-XXXXXXXXXXXXXXXX`
5. The ad slots (top banner, in-content, category footer, in-detail) auto-fill
   with real ads. Revenue is ~$2–10 RPM for dev-tool traffic.

---

## How to apply env vars and redeploy

After setting any env var above, rebuild + push:

```powershell
cd site
# set the vars (PowerShell)
$env:CF_ANALYTICS_TOKEN="..."
$env:DONATE_URL="..."
python generate_static.py
git add dist/ && git commit -m "wire monetization" && git push origin main
```

Cloudflare auto-rebuilds from the repo on every push, so you can also just set
the vars as **build variables** in Cloudflare's dashboard (Workers & Pages →
openapihub → Settings → Build → Variables) and never touch local env again.

---

## What I (Codex) can and cannot do

**Can do (done):** wire every monetization path in code so it activates on
env var; rebuild; deploy; verify.

**Cannot do (needs you):** register the affiliate accounts (your identity),
create the AdSense account (your identity + bank), buy a domain, write
content, drive traffic. These are inherently human/account actions. I will not
fake any of them.
