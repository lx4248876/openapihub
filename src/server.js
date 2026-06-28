const http = require("node:http");
const fs = require("node:fs");
const fsp = require("node:fs/promises");
const path = require("node:path");

const PORT = Number(process.env.PORT || 4781);
const ROOT = __dirname;
const DATA_FILE = path.join(ROOT, "..", "data", "apis.json");
const PUBLIC_DIR = path.join(ROOT, "..", "public");

const SITE_NAME = process.env.SITE_NAME || "OpenAPIHub";
const SITE_TAGLINE = process.env.SITE_TAGLINE || "A free directory of public APIs for developers";
const SITE_ORIGIN = process.env.SITE_ORIGIN || `http://localhost:${PORT}`;
const ADSENSE_CLIENT = process.env.ADSENSE_CLIENT || ""; // ca-pub-XXXXXXXXXXXXXXXX
const AFFILIATE_VERCEL = process.env.AFFILIATE_VERCEL || "https://vercel.com";
const AFFILIATE_RENDER = process.env.AFFILIATE_RENDER || "https://render.com";
const AFFILIATE_SUPABASE = process.env.AFFILIATE_SUPABASE || "https://supabase.com";

let CACHE = null;
let CATEGORIES = null;
let BY_SLUG = null;

async function loadData() {
  if (CACHE) return CACHE;
  const raw = await fsp.readFile(DATA_FILE, "utf8");
  const items = JSON.parse(raw);
  CACHE = items;

  BY_SLUG = new Map();
  for (const item of items) BY_SLUG.set(item.slug, item);

  const map = new Map();
  for (const item of items) {
    if (!map.has(item.categorySlug)) {
      map.set(item.categorySlug, {
        category: item.category,
        categorySlug: item.categorySlug,
        apis: []
      });
    }
    map.get(item.categorySlug).apis.push(item);
  }
  for (const c of map.values()) c.apis.sort((a, b) => a.name.localeCompare(b.name));
  CATEGORIES = [...map.values()].sort((a, b) => b.apis.length - a.apis.length);

  return CACHE;
}

function esc(s) {
  return String(s ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function layout({ title, description, canonical, body, extraHead = "" }) {
  return `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${esc(title)}</title>
<meta name="description" content="${esc(description)}">
<link rel="canonical" href="${esc(canonical)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif&family=Space+Grotesk:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
${ADSENSE_CLIENT ? `<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=${esc(ADSENSE_CLIENT)}" crossorigin="anonymous"></script>` : ""}
${extraHead}
</head>
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/"><span class="brand-mark">{ }</span><span>${esc(SITE_NAME)}</span></a>
    <nav class="site-nav">
      <a href="/">Home</a>
      <a href="/categories">Categories</a>
      <a href="/about">About</a>
    </nav>
  </div>
</header>
<main>
${body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <p>${esc(SITE_NAME)} &middot; ${esc(SITE_TAGLINE)}</p>
    <p class="muted">Built from the open-source public-apis dataset. Affiliate links may earn us a commission.</p>
  </div>
</footer>
</body>
</html>`;
}

function adSlot(label) {
  if (!ADSENSE_CLIENT) {
    return `<div class="ad-slot placeholder"><span>${esc(label)} &mdash; connect AdSense to monetize</span></div>`;
  }
  return `<ins class="adsbygoogle ad-slot" style="display:block" data-ad-client="${esc(ADSENSE_CLIENT)}" data-ad-slot="" data-ad-format="auto" data-full-width-responsive="true"></ins>`;
}

function affiliateRail() {
  return `
<aside class="rail">
  <h3>Sponsored</h3>
  <ul class="rail-list">
    <li><a href="${esc(AFFILIATE_VERCEL)}" rel="sponsored noopener" target="_blank">Deploy this API on Vercel &rarr;</a></li>
    <li><a href="${esc(AFFILIATE_RENDER)}" rel="sponsored noopener" target="_blank">Host your backend on Render &rarr;</a></li>
    <li><a href="${esc(AFFILIATE_SUPABASE)}" rel="sponsored noopener" target="_blank">Supabase: open-source Postgres + Auth &rarr;</a></li>
  </ul>
</aside>`;
}

function renderHome(items, categories) {
  const top = categories.slice(0, 12);
  const catCards = top.map(c => `
    <a class="cat-card" href="/c/${esc(c.categorySlug)}">
      <h3>${esc(c.category)}</h3>
      <span>${c.apis.length} APIs</span>
    </a>`).join("");

  const featured = items.slice(0, 24).map(a => `
    <a class="api-card" href="/api/${esc(a.slug)}">
      <h3>${esc(a.name)}</h3>
      <p>${esc(a.description.slice(0, 140))}${a.description.length > 140 ? "&hellip;" : ""}</p>
      <div class="api-meta">
        <span class="badge">${esc(a.category)}</span>
        <span class="badge ${a.https === "Yes" ? "badge-ok" : "badge-no"}">HTTPS ${esc(a.https)}</span>
        <span class="badge ${a.auth === "No" ? "badge-ok" : "badge-warn"}">Auth ${esc(a.auth)}</span>
      </div>
    </a>`).join("");

  const body = `
  <section class="hero wrap">
    <div>
      <p class="eyebrow">${items.length} public APIs across ${categories.length} categories</p>
      <h1>Stop hunting for APIs.<br>Start shipping.</h1>
      <p class="hero-text">${esc(SITE_TAGLINE)}. Each entry links directly to its docs, so you can compare and integrate in minutes.</p>
      <form class="search" role="search" action="/search" method="get">
        <input type="search" name="q" placeholder="Search APIs, e.g. weather, crypto, cat facts">
        <button type="submit">Search</button>
      </form>
    </div>
    ${adSlot("Top banner")}
  </section>

  <section class="wrap">
    <h2 class="section-h">Popular categories</h2>
    <div class="cat-grid">${catCards}</div>
  </section>

  <section class="wrap two-col">
    <div>
      <h2 class="section-h">Recently added</h2>
      <div class="api-grid">${featured}</div>
      <p><a class="more" href="/categories">Browse all ${categories.length} categories &rarr;</a></p>
    </div>
    ${affiliateRail()}
  </section>

  <section class="wrap">
    ${adSlot("In-content ad")}
  </section>
  `;
  return layout({
    title: `${SITE_NAME} - ${SITE_TAGLINE}`,
    description: `Browse ${items.length} public APIs across ${categories.length} categories. Free developer directory with HTTPS, auth, and CORS metadata.`,
    canonical: SITE_ORIGIN + "/",
    body
  });
}

function renderCategoriesIndex(categories) {
  const rows = categories.map(c => `
    <li>
      <a href="/c/${esc(c.categorySlug)}">
        <span class="row-name">${esc(c.category)}</span>
        <span class="row-count">${c.apis.length} APIs</span>
      </a>
    </li>`).join("");

  const body = `
  <section class="wrap">
    <p class="eyebrow">All categories</p>
    <h1>Pick a category</h1>
    <ul class="cat-list">${rows}</ul>
  </section>`;
  return layout({
    title: `All API Categories - ${SITE_NAME}`,
    description: `Browse all ${categories.length} API categories.`,
    canonical: SITE_ORIGIN + "/categories",
    body
  });
}

function renderCategory(category) {
  const cards = category.apis.map(a => `
    <a class="api-card" href="/api/${esc(a.slug)}">
      <h3>${esc(a.name)}</h3>
      <p>${esc(a.description.slice(0, 140))}${a.description.length > 140 ? "&hellip;" : ""}</p>
      <div class="api-meta">
        <span class="badge ${a.https === "Yes" ? "badge-ok" : "badge-no"}">HTTPS ${esc(a.https)}</span>
        <span class="badge ${a.auth === "No" ? "badge-ok" : "badge-warn"}">Auth ${esc(a.auth)}</span>
        <span class="badge">CORS ${esc(a.cors || "Unknown")}</span>
      </div>
    </a>`).join("");

  const body = `
  <section class="wrap">
    <nav class="crumbs"><a href="/">Home</a> &rsaquo; <a href="/categories">Categories</a> &rsaquo; <span>${esc(category.category)}</span></nav>
    <h1>${esc(category.category)} APIs <span class="count">${category.apis.length}</span></h1>
    <div class="api-grid">${cards}</div>
  </section>
  <section class="wrap">${adSlot("Category footer")}</section>`;
  return layout({
    title: `${category.category} APIs - ${SITE_NAME}`,
    description: `Browse ${category.apis.length} ${category.category} APIs with HTTPS, auth, and CORS metadata.`,
    canonical: `${SITE_ORIGIN}/c/${category.categorySlug}`,
    body
  });
}

function renderDetail(a) {
  const body = `
  <section class="wrap detail two-col">
    <article class="detail-main">
      <nav class="crumbs"><a href="/">Home</a> &rsaquo; <a href="/c/${esc(a.categorySlug)}">${esc(a.category)}</a> &rsaquo; <span>${esc(a.name)}</span></nav>
      <h1>${esc(a.name)}</h1>
      <p class="lede">${esc(a.description)}</p>
      <ul class="meta-list">
        <li><strong>Category</strong><span><a href="/c/${esc(a.categorySlug)}">${esc(a.category)}</a></span></li>
        <li><strong>Auth</strong><span>${esc(a.auth)}</span></li>
        <li><strong>HTTPS</strong><span>${esc(a.https)}</span></li>
        <li><strong>CORS</strong><span>${esc(a.cors || "Unknown")}</span></li>
        <li><strong>Docs</strong><span><a href="${esc(a.url)}" rel="nofollow noopener" target="_blank">${esc(a.url)}</a></span></li>
      </ul>
      <div class="cta-row">
        <a class="button-primary" href="${esc(a.url)}" rel="nofollow noopener" target="_blank">Open documentation &rarr;</a>
        <a class="button-secondary" href="${esc(AFFILIATE_VERCEL)}" rel="sponsored noopener" target="_blank">Deploy in 1 click on Vercel</a>
      </div>
      ${adSlot("In-detail ad")}
      <h2>How to use ${esc(a.name)}</h2>
      <ol class="howto">
        <li>Open the documentation linked above and request any required API key.</li>
        <li>Choose a client library that matches the API (REST, GraphQL, or SDK).</li>
        <li>Store your API key in environment variables, never in source files.</li>
        <li>Deploy your integration to a host such as Vercel or Render.</li>
      </ol>
    </article>
    ${affiliateRail()}
  </section>`;

  const ld = {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    name: a.name,
    applicationCategory: "DeveloperApplication",
    description: a.description,
    url: a.url,
    operatingSystem: "Web"
  };

  return layout({
    title: `${a.name} API documentation and overview - ${SITE_NAME}`,
    description: `${a.name} is a ${a.category.toLowerCase()} API. ${a.description}`.slice(0, 160),
    canonical: `${SITE_ORIGIN}/api/${a.slug}`,
    body,
    extraHead: `<script type="application/ld+json">${JSON.stringify(ld)}</script>`
  });
}

function renderAbout() {
  const body = `
  <section class="wrap">
    <h1>About ${esc(SITE_NAME)}</h1>
    <p>${esc(SITE_NAME)} is a free developer directory of public APIs. Each entry is sourced from the open-source public-apis dataset and enriched with HTTPS, auth, and CORS metadata so you can quickly decide whether an API fits your project.</p>
    <h2>How we make money</h2>
    <p>We monetize through display ads and affiliate links to hosting and developer-tool providers. Clicking an affiliate link may earn us a commission at no extra cost to you.</p>
    <h2>Contact</h2>
    <p>This site is operated by an indie developer. Suggest new APIs or report broken links via the upstream repository.</p>
  </section>`;
  return layout({
    title: `About - ${SITE_NAME}`,
    description: `About ${SITE_NAME}, a free public-API directory for developers.`,
    canonical: SITE_ORIGIN + "/about",
    body
  });
}

function renderSearch(items, q) {
  const needle = q.toLowerCase();
  const filtered = items.filter(a =>
    a.name.toLowerCase().includes(needle) ||
    a.description.toLowerCase().includes(needle) ||
    a.category.toLowerCase().includes(needle)
  ).slice(0, 60);
  const cards = filtered.map(a => `
    <a class="api-card" href="/api/${esc(a.slug)}">
      <h3>${esc(a.name)}</h3>
      <p>${esc(a.description.slice(0, 140))}${a.description.length > 140 ? "&hellip;" : ""}</p>
      <div class="api-meta"><span class="badge">${esc(a.category)}</span></div>
    </a>`).join("");

  const body = `
  <section class="wrap">
    <p class="eyebrow">Search results</p>
    <h1>${filtered.length} result${filtered.length === 1 ? "" : "s"} for &ldquo;${esc(q)}&rdquo;</h1>
    <div class="api-grid">${cards || "<p>No matches. Try a broader keyword.</p>"}</div>
  </section>`;
  return layout({
    title: `Search: ${q} - ${SITE_NAME}`,
    description: `Search results for ${q} on ${SITE_NAME}.`,
    canonical: `${SITE_ORIGIN}/search?q=${encodeURIComponent(q)}`,
    body
  });
}

function renderSitemap(items, categories) {
  const urls = [
    `${SITE_ORIGIN}/`,
    `${SITE_ORIGIN}/categories`,
    `${SITE_ORIGIN}/about`
  ];
  for (const c of categories) urls.push(`${SITE_ORIGIN}/c/${c.categorySlug}`);
  for (const a of items) urls.push(`${SITE_ORIGIN}/api/${a.slug}`);
  return urls.join("\n") + "\n";
}

function renderRobots() {
  return `User-agent: *
Allow: /
Sitemap: ${SITE_ORIGIN}/sitemap.txt
`;
}

async function handle(req, res, url) {
  await loadData();

  if (req.method !== "GET") {
    res.writeHead(405, { "Content-Type": "text/plain" });
    res.end("Method not allowed");
    return;
  }

  const p = url.pathname;

  if (p === "/" ) {
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    res.end(renderHome(CACHE, CATEGORIES));
    return;
  }
  if (p === "/categories") {
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    res.end(renderCategoriesIndex(CATEGORIES));
    return;
  }
  if (p === "/about") {
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    res.end(renderAbout());
    return;
  }
  if (p === "/sitemap.txt") {
    res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
    res.end(renderSitemap(CACHE, CATEGORIES));
    return;
  }
  if (p === "/robots.txt") {
    res.writeHead(200, { "Content-Type": "text/plain; charset=utf-8" });
    res.end(renderRobots());
    return;
  }
  if (p === "/search") {
    const q = (url.searchParams.get("q") || "").trim();
    if (!q) {
      res.writeHead(302, { Location: "/" });
      res.end();
      return;
    }
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    res.end(renderSearch(CACHE, q.slice(0, 60)));
    return;
  }
  if (p.startsWith("/c/")) {
    const slug = decodeURIComponent(p.replace("/c/", ""));
    const cat = CATEGORIES.find(c => c.categorySlug === slug);
    if (!cat) {
      res.writeHead(404, { "Content-Type": "text/plain" });
      res.end("Not found");
      return;
    }
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    res.end(renderCategory(cat));
    return;
  }
  if (p.startsWith("/api/")) {
    const slug = decodeURIComponent(p.replace("/api/", ""));
    const a = BY_SLUG.get(slug);
    if (!a) {
      res.writeHead(404, { "Content-Type": "text/plain" });
      res.end("Not found");
      return;
    }
    res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    res.end(renderDetail(a));
    return;
  }

  // static files
  const filePath = path.join(PUBLIC_DIR, path.normalize(p).replace(/^(\.\.[\\/])+/, ""));
  if (!filePath.startsWith(PUBLIC_DIR)) {
    res.writeHead(403, { "Content-Type": "text/plain" });
    res.end("Forbidden");
    return;
  }
  try {
    const data = await fsp.readFile(filePath);
    const ext = path.extname(filePath).toLowerCase();
    const types = { ".css":"text/css", ".png":"image/png", ".svg":"image/svg+xml", ".ico":"image/x-icon", ".js":"application/javascript" };
    res.writeHead(200, { "Content-Type": (types[ext] || "application/octet-stream") + "; charset=utf-8" });
    res.end(data);
  } catch {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Not found");
  }
}

const server = http.createServer(async (req, res) => {
  try {
    const host = req.headers.host || `localhost:${PORT}`;
    const url = new URL(req.url || "/", `http://${host}`);
    await handle(req, res, url);
  } catch (err) {
    console.error(err);
    res.writeHead(500, { "Content-Type": "text/plain" });
    res.end("Server error");
  }
});

loadData().then(() => {
  server.listen(PORT, () => {
    console.log(`${SITE_NAME} running on http://localhost:${PORT}`);
    console.log(`Loaded ${CACHE.length} APIs across ${CATEGORIES.length} categories`);
  });
});
