"""Static site generator for OpenAPIHub."""
import json, os, html, pathlib, shutil, sys

SITE = pathlib.Path(__file__).resolve().parent
DATA_FILE = SITE / "data" / "apis.json"
DIST = SITE / "dist"

SITE_NAME = os.environ.get("SITE_NAME", "OpenAPIHub")
SITE_TAGLINE = os.environ.get("SITE_TAGLINE", "A free directory of public APIs for developers")
SITE_ORIGIN = os.environ.get("SITE_ORIGIN", "").rstrip("/")
ADSENSE_CLIENT = os.environ.get("ADSENSE_CLIENT", "")
# Analytics: free, cookieless. Either Cloudflare Web Analytics beacon token
# (get it from dash.cloudflare.com -> Web Analytics -> Add a site) or a
# self-hosted/Plausible Cloud domain. Leave blank to ship without analytics.
CF_ANALYTICS_TOKEN = os.environ.get("CF_ANALYTICS_TOKEN", "")
PLAUSIBLE_DOMAIN = os.environ.get("PLAUSIBLE_DOMAIN", "")
# Affiliate base URLs. Append your real ref code as ?ref=YOUR_ID via env so
# clicks are attributed to your account. Examples:
#   AFFILIATE_VERCEL=https://vercel.com/?ref=your-vercel-ref
AFFILIATE_VERCEL = os.environ.get("AFFILIATE_VERCEL", "https://vercel.com")
AFFILIATE_RENDER = os.environ.get("AFFILIATE_RENDER", "https://render.com")
AFFILIATE_SUPABASE = os.environ.get("AFFILIATE_SUPABASE", "https://supabase.com")
# Donation / tip-jar link (BuyMeACoffee, Ko-fi, GitHub Sponsors). No approval
# needed, pays out immediately. Leave blank to hide the CTA.
DONATE_URL = os.environ.get("DONATE_URL", "")
# utm_source stamped on every outgoing affiliate click so we can measure which
# pages actually convert, in whatever analytics backend we later wire up.
AFFILIATE_SOURCE = os.environ.get("AFFILIATE_SOURCE", "openapihub")


def aff_url(base, medium, campaign):
    """Stamp UTM params on an outgoing affiliate link so every click is
    attributable, regardless of whether the destination ref param is set.
    Keeps any existing query the env-configured base URL already carries."""
    sep = "&" if "?" in base else "?"
    return (base + sep + "utm_source=" + AFFILIATE_SOURCE
            + "&utm_medium=" + medium + "&utm_campaign=" + campaign)


def analytics_head():
    """Return head snippet for whichever free cookieless analytics backend is
    configured. Cloudflare Web Analytics is the default since the site is
    already on Cloudflare; Plausible is a drop-in alternative."""
    out = ""
    if CF_ANALYTICS_TOKEN:
        beacon = chr(123) + chr(34) + "token" + chr(34) + ": " + chr(34) + esc(CF_ANALYTICS_TOKEN) + chr(34) + chr(125)
        out += "<script defer src=\"https://static.cloudflareinsights.com/beacon.min.js\" data-cf-beacon='" + beacon + "'></script>"
    if PLAUSIBLE_DOMAIN:
        out += '<script defer data-domain="' + esc(PLAUSIBLE_DOMAIN) + '" src="https://plausible.io/js/script.js"></script>'
    return out


def social_meta(canonical, title, description):
    """Open Graph + Twitter Card tags so shares on HN/Reddit/Twitter render a
    rich preview. Biggest lever for off-site traffic (which is the biggest
    lever for revenue). Uses a generated SVG card so no image hosting needed."""
    card_url = canonical
    return (
        '<meta property="og:type" content="website">\n'
        '<meta property="og:url" content="' + esc(canonical) + '">\n'
        '<meta property="og:title" content="' + esc(title) + '">\n'
        '<meta property="og:description" content="' + esc(description) + '">\n'
        '<meta property="og:site_name" content="' + esc(SITE_NAME) + '">\n'
        '<meta name="twitter:card" content="summary">\n'
        '<meta name="twitter:title" content="' + esc(title) + '">\n'
        '<meta name="twitter:description" content="' + esc(description) + '">\n'
    )


def esc(s):
    return html.escape(str(s)) if s is not None else ""


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def load():
    items = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    by_cat = {}
    for a in items:
        by_cat.setdefault(a["categorySlug"], {
            "category": a["category"],
            "categorySlug": a["categorySlug"],
            "apis": []
        })["apis"].append(a)
    for c in by_cat.values():
        c["apis"].sort(key=lambda x: x["name"].lower())
    cats = sorted(by_cat.values(), key=lambda c: -len(c["apis"]))
    return items, cats


ITEMS, CATS = load()


def layout(title, description, canonical, body, extra_head=""):
    adsense_line = ""
    if ADSENSE_CLIENT:
        adsense_line = (
            '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client='
            + esc(ADSENSE_CLIENT)
            + '" crossorigin="anonymous"></script>'
        )
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>' + esc(title) + '</title>\n'
        '<meta name="description" content="' + esc(description) + '">\n'
        '<link rel="canonical" href="' + esc(canonical) + '">\n'
        + social_meta(canonical, title, description)
        + '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">\n'
        '<link rel="stylesheet" href="/styles.css">\n'
        + adsense_line + "\n"
        + extra_head + "\n"
        + analytics_head() + "\n"
        + '</head>\n<body>\n'
        '<header class="site-header"><div class="wrap">'
        '<a class="brand" href="/"><span class="brand-mark">{ }</span><span>' + esc(SITE_NAME) + '</span></a>'
        '<nav class="site-nav">'
        '<a href="/">Home</a>'
        '<a href="/categories">Categories</a>'
        '<a href="/search">Search</a>'
        '<a href="/about">About</a>'
        '</nav></div></header>\n'
        '<main>\n' + body + '\n</main>\n'
        '<footer class="site-footer"><div class="wrap">'
        '<p>' + esc(SITE_NAME) + ' &middot; ' + esc(SITE_TAGLINE) + '</p>'
        '<p class="muted">Built from the open-source public-apis dataset. Affiliate links may earn us a commission.</p>'
        + ("" if not DONATE_URL else '<p class="footer-cta"><a class="donate-link" href="' + esc(DONATE_URL) + '" rel="noopener" target="_blank">Support this project &rarr;</a></p>')
        + '</div></footer>\n'
        '</body>\n</html>\n'
    )


def ad_slot(label):
    if not ADSENSE_CLIENT:
        return '<div class="ad-slot placeholder"><span>' + esc(label) + ' &mdash; connect AdSense to monetize</span></div>'
    return ('<ins class="adsbygoogle ad-slot" style="display:block" '
            'data-ad-client="' + esc(ADSENSE_CLIENT) + '" '
            'data-ad-slot="" data-ad-format="auto" data-full-width-responsive="true"></ins>')


def affiliate_rail():
    # Each affiliate link is stamped with UTM params so clicks are attributable
    # end-to-end. Set AFFILIATE_VERCEL etc. to include your real ?ref= code and
    # the UTM tracking rides on top.
    donate_li = ""
    if DONATE_URL:
        donate_li = ('<li class="rail-donate"><a href="' + esc(DONATE_URL)
                     + '" rel="noopener" target="_blank">Found this useful? Buy me a coffee &hearts;</a></li>')
    return (
        '<aside class="rail"><h3>Sponsored</h3><ul class="rail-list">'
        '<li><a href="' + esc(aff_url(AFFILIATE_VERCEL, "affiliate", "rail-vercel")) + '" rel="sponsored noopener" target="_blank">Deploy this API on Vercel &rarr;</a></li>'
        '<li><a href="' + esc(aff_url(AFFILIATE_RENDER, "affiliate", "rail-render")) + '" rel="sponsored noopener" target="_blank">Host your backend on Render &rarr;</a></li>'
        '<li><a href="' + esc(aff_url(AFFILIATE_SUPABASE, "affiliate", "rail-supabase")) + '" rel="sponsored noopener" target="_blank">Supabase: open-source Postgres + Auth &rarr;</a></li>'
        + donate_li +
        '</ul></aside>'
    )


def render_home():
    top = CATS[:12]
    cat_cards = "".join(
        '<a class="cat-card" href="/c/' + esc(c["categorySlug"]) + '"><h3>' + esc(c["category"]) + '</h3><span>' + str(len(c["apis"])) + ' APIs</span></a>'
        for c in top
    )
    featured = ""
    for a in ITEMS[:24]:
        desc = a["description"][:140] + ("\u2026" if len(a["description"]) > 140 else "")
        https_badge = "badge-ok" if a.get("https") == "Yes" else "badge-no"
        auth_badge = "badge-ok" if a.get("auth") == "No" else "badge-warn"
        featured += (
            '<a class="api-card" href="/api/' + esc(a["slug"]) + '">'
            '<h3>' + esc(a["name"]) + '</h3>'
            '<p>' + esc(desc) + '</p>'
            '<div class="api-meta">'
            '<span class="badge">' + esc(a["category"]) + '</span>'
            '<span class="badge ' + https_badge + '">HTTPS ' + esc(a.get("https", "")) + '</span>'
            '<span class="badge ' + auth_badge + '">Auth ' + esc(a.get("auth", "")) + '</span>'
            '</div></a>'
        )
    body = (
        '<section class="hero wrap">'
        '<div>'
        '<p class="eyebrow">' + str(len(ITEMS)) + ' public APIs across ' + str(len(CATS)) + ' categories</p>'
        '<h1>Stop hunting for APIs.<br>Start shipping.</h1>'
        '<p class="hero-text">' + esc(SITE_TAGLINE) + '. Each entry links directly to its docs, so you can compare and integrate in minutes.</p>'
        '<form class="search" role="search" action="/search" method="get">'
        '<input type="search" name="q" placeholder="Search APIs, e.g. weather, crypto, cat facts">'
        '<button type="submit">Search</button>'
        '</form>'
        '</div>'
        + ad_slot("Top banner") +
        '</section>'
        '<section class="wrap"><h2 class="section-h">Popular categories</h2><div class="cat-grid">' + cat_cards + '</div></section>'
        '<section class="wrap two-col"><div>'
        '<h2 class="section-h">Recently added</h2>'
        '<div class="api-grid">' + featured + '</div>'
        '<p><a class="more" href="/categories">Browse all ' + str(len(CATS)) + ' categories &rarr;</a></p>'
        '</div>'
        + affiliate_rail() +
        '</section>'
        '<section class="wrap">' + ad_slot("In-content ad") + '</section>'
    )
    desc = "Browse " + str(len(ITEMS)) + " public APIs across " + str(len(CATS)) + " categories. Free developer directory with HTTPS, auth, and CORS metadata."
    home_ld = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "url": SITE_ORIGIN + "/",
        "description": SITE_TAGLINE,
        "potentialAction": {
            "@type": "SearchAction",
            "target": SITE_ORIGIN + "/search?q={search_term_string}",
            "query-input": "required name=search_term_string",
        },
    }
    extra = '<script type="application/ld+json">' + json.dumps(home_ld) + '</script>'
    return layout(SITE_NAME + " - " + SITE_TAGLINE, desc, SITE_ORIGIN + "/", body, extra)


def render_categories():
    rows = "".join(
        '<li><a href="/c/' + esc(c["categorySlug"]) + '"><span class="row-name">' + esc(c["category"]) + '</span><span class="row-count">' + str(len(c["apis"])) + ' APIs</span></a></li>'
        for c in CATS
    )
    body = '<section class="wrap"><p class="eyebrow">All categories</p><h1>Pick a category</h1><ul class="cat-list">' + rows + '</ul></section>'
    return layout("All API Categories - " + SITE_NAME, "Browse all " + str(len(CATS)) + " API categories.", SITE_ORIGIN + "/categories", body)


def render_category(c):
    cards = ""
    for a in c["apis"]:
        desc = a["description"][:140] + ("\u2026" if len(a["description"]) > 140 else "")
        https_badge = "badge-ok" if a.get("https") == "Yes" else "badge-no"
        auth_badge = "badge-ok" if a.get("auth") == "No" else "badge-warn"
        cards += (
            '<a class="api-card" href="/api/' + esc(a["slug"]) + '">'
            '<h3>' + esc(a["name"]) + '</h3>'
            '<p>' + esc(desc) + '</p>'
            '<div class="api-meta">'
            '<span class="badge ' + https_badge + '">HTTPS ' + esc(a.get("https", "")) + '</span>'
            '<span class="badge ' + auth_badge + '">Auth ' + esc(a.get("auth", "")) + '</span>'
            '<span class="badge">CORS ' + esc(a.get("cors", "Unknown")) + '</span>'
            '</div></a>'
        )
    body = (
        '<section class="wrap">'
        '<nav class="crumbs"><a href="/">Home</a> &rsaquo; <a href="/categories">Categories</a> &rsaquo; <span>' + esc(c["category"]) + '</span></nav>'
        '<h1>' + esc(c["category"]) + ' APIs <span class="count">' + str(len(c["apis"])) + '</span></h1>'
        '<div class="api-grid">' + cards + '</div>'
        '</section>'
        '<section class="wrap">' + ad_slot("Category footer") + '</section>'
    )
    item_list = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": c["category"] + " APIs",
        "numberOfItems": len(c["apis"]),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": a["name"], "url": SITE_ORIGIN + "/api/" + a["slug"]}
            for i, a in enumerate(c["apis"][:20])
        ],
    }
    cat_ld = '<script type="application/ld+json">' + json.dumps(item_list) + '</script>'
    return layout(c["category"] + " APIs - " + SITE_NAME,
                  "Browse " + str(len(c["apis"])) + " " + c["category"] + " APIs with HTTPS, auth, and CORS metadata.",
                  SITE_ORIGIN + "/c/" + c["categorySlug"], body, cat_ld)


def render_detail(a):
    body = (
        '<section class="wrap detail two-col"><article class="detail-main">'
        '<nav class="crumbs"><a href="/">Home</a> &rsaquo; <a href="/c/' + esc(a["categorySlug"]) + '">' + esc(a["category"]) + '</a> &rsaquo; <span>' + esc(a["name"]) + '</span></nav>'
        '<h1>' + esc(a["name"]) + '</h1>'
        '<p class="lede">' + esc(a["description"]) + '</p>'
        '<ul class="meta-list">'
        '<li><strong>Category</strong><span><a href="/c/' + esc(a["categorySlug"]) + '">' + esc(a["category"]) + '</a></span></li>'
        '<li><strong>Auth</strong><span>' + esc(a.get("auth", "")) + '</span></li>'
        '<li><strong>HTTPS</strong><span>' + esc(a.get("https", "")) + '</span></li>'
        '<li><strong>CORS</strong><span>' + esc(a.get("cors", "Unknown")) + '</span></li>'
        '<li><strong>Docs</strong><span><a href="' + esc(a["url"]) + '" rel="nofollow noopener" target="_blank">' + esc(a["url"]) + '</a></span></li>'
        '</ul>'
        '<div class="cta-row">'
        '<a class="button-primary" href="' + esc(a["url"]) + '" rel="nofollow noopener" target="_blank">Open documentation &rarr;</a>'
        '<a class="button-secondary" href="' + esc(aff_url(AFFILIATE_VERCEL, "affiliate", "detail-deploy")) + '" rel="sponsored noopener" target="_blank">Deploy in 1 click on Vercel</a>'
        '</div>'
        + ad_slot("In-detail ad") +
        '<h2>How to use ' + esc(a["name"]) + '</h2>'
        '<ol class="howto">'
        '<li>Open the documentation linked above and request any required API key.</li>'
        '<li>Choose a client library that matches the API (REST, GraphQL, or SDK).</li>'
        '<li>Store your API key in environment variables, never in source files.</li>'
        '<li>Deploy your integration to a host such as Vercel or Render.</li>'
        '</ol>'
        '</article>'
        + affiliate_rail() +
        '</section>'
    )
    # WebAPI is the precise schema.org type for a web API (not SoftwareApplication).
    # Rich metadata here can earn Google rich-result eligibility per page.
    ld = {
        "@context": "https://schema.org",
        "@type": "WebAPI",
        "name": a["name"],
        "description": a["description"],
        "url": a["url"],
        "documentation": a["url"],
        "category": a["category"],
    }
    if a.get("https"):
        ld["providerTransport"] = ("HTTPS" if str(a["https"]).lower() == "yes" else "HTTP")
    ld_breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE_ORIGIN + "/"},
            {"@type": "ListItem", "position": 2, "name": a["category"], "item": SITE_ORIGIN + "/c/" + a["categorySlug"]},
            {"@type": "ListItem", "position": 3, "name": a["name"], "item": SITE_ORIGIN + "/api/" + a["slug"]},
        ],
    }
    extra = ('<script type="application/ld+json">' + json.dumps(ld) + '</script>\n'
             + '<script type="application/ld+json">' + json.dumps(ld_breadcrumb) + '</script>')
    desc = (a["name"] + " is a " + a["category"].lower() + " API. " + a["description"])[:160]
    return layout(a["name"] + " API documentation and overview - " + SITE_NAME,
                  desc,
                  SITE_ORIGIN + "/api/" + a["slug"],
                  body, extra)


def render_about():
    body = (
        '<section class="wrap">'
        '<h1>About ' + esc(SITE_NAME) + '</h1>'
        '<p>' + esc(SITE_NAME) + ' is a free developer directory of public APIs. Each entry is sourced from the open-source public-apis dataset and enriched with HTTPS, auth, and CORS metadata so you can quickly decide whether an API fits your project.</p>'
        '<h2>How we make money</h2>'
        '<p>We monetize through display ads and affiliate links to hosting and developer-tool providers. Clicking an affiliate link may earn us a commission at no extra cost to you.</p>'
        '</section>'
    )
    return layout("About - " + SITE_NAME, "About " + SITE_NAME + ", a free public-API directory for developers.", SITE_ORIGIN + "/about", body)


def render_search():
    body = (
        '<section class="wrap"><p class="eyebrow">Search</p><h1>Find an API</h1>'
        '<form class="search" id="search-form">'
        '<input type="search" id="search-input" name="q" placeholder="Search APIs, e.g. weather, crypto, cat facts" autocomplete="off">'
        '<button type="submit">Search</button>'
        '</form>'
        '<div id="search-results" class="api-grid" style="margin-top:1.5rem"></div>'
        '<p id="search-empty" class="muted" style="margin-top:1rem;display:none">No matches. Try a broader keyword.</p>'
        '</section>'
        '<script src="/search-index.js" defer></script>'
        '<script src="/search.js" defer></script>'
    )
    return layout("Search - " + SITE_NAME, "Search " + SITE_NAME + ", a free public-API directory for developers.", SITE_ORIGIN + "/search", body)


def render_404():
    body = '<section class="wrap"><h1>404</h1><p class="muted">That page does not exist.</p><p><a class="button-primary" href="/">Back to home</a></p></section>'
    return layout("404 - " + SITE_NAME, "Page not found", SITE_ORIGIN + "/", body)


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    shutil.copy(SITE / "public" / "styles.css", DIST / "styles.css")
    write(DIST / "index.html", render_home())
    write(DIST / "categories" / "index.html", render_categories())
    write(DIST / "about" / "index.html", render_about())
    write(DIST / "search" / "index.html", render_search())
    write(DIST / "404.html", render_404())
    for c in CATS:
        write(DIST / "c" / c["categorySlug"] / "index.html", render_category(c))
    for a in ITEMS:
        write(DIST / "api" / a["slug"] / "index.html", render_detail(a))
    origin = SITE_ORIGIN
    urls = [origin + "/", origin + "/categories", origin + "/about", origin + "/search"]
    for c in CATS:
        urls.append(origin + "/c/" + c["categorySlug"])
    for a in ITEMS:
        urls.append(origin + "/api/" + a["slug"])
    write(DIST / "sitemap.txt", "\n".join(urls) + "\n")
    write(DIST / "robots.txt", "User-agent: *\nAllow: /\nSitemap: " + origin + "/sitemap.txt\n")
    idx = [{"n": a["name"], "d": a["description"], "c": a["category"], "s": a["slug"]} for a in ITEMS]
    write(DIST / "search-index.js", "window.__APIS__ = " + json.dumps(idx) + ";\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print("generated: " + str(len(ITEMS)) + " detail pages, " + str(len(CATS)) + " category pages")
    print("output: " + str(DIST))


if __name__ == "__main__":
    main()