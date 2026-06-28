"""Generate a ready-to-publish Markdown article from the best-of page.

Copy-paste scripts/publish/best-free-apis-2026.md into dev.to, Hashnode, or
HackerNoon. These platforms give dofollow backlinks, the fastest zero-cost way
to build SEO authority and real traffic for a brand-new site."""
import json, pathlib

SITE = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((SITE / "data" / "apis.json").read_text(encoding="utf-8"))
by_slug = {a["slug"]: a for a in DATA}
ORIGIN = "https://openapihub.410185103.workers.dev"

BEST_OF = [
    ("openweathermap", "The default weather API. Its free tier covers 60 calls/minute and roughly a million calls per month - more than enough for most side projects. Paid plans add historical data going back years."),
    ("open-meteo", "The rare weather API that is genuinely free with no API key and no signup. You get current conditions plus a 16-day forecast for anywhere on earth. Ideal for quick demos and hackathons where you just want something working in ten minutes."),
    ("github", "Read repos, issues, and commits without authentication, within rate limits. This is the backbone of most developer-portfolio dashboards and open-source analytics tools."),
    ("google-firebase", "Realtime database, authentication, and file storage bundled into one SDK. Probably the fastest path from zero to a working mobile backend if you do not want to run your own server."),
    ("coingecko", "Free cryptocurrency prices, market caps, and historical data. Public endpoints need no key, and the rate limits are generous enough for personal projects."),
    ("exchangerate-host", "Free currency conversion with no key required for basic lookups. You can drop it straight into a pricing page or checkout flow."),
    ("nasa", "Astronomy Picture of the Day, Mars Rover photos, and near-Earth object tracking. A genuinely fun dataset for learning REST and building visual demos."),
    ("unsplash", "High-quality, royalty-free photos behind a clean REST API. The standard choice for placeholder imagery in design tools and landing-page builders."),
    ("giphy", "Search and serve GIFs. Perfect for reactions, chat apps, and adding a little life to otherwise empty UI states."),
    ("spotify", "Rich music metadata, audio feature analysis, and track recommendations. Great for building playlists, mood detectors, or personal listening dashboards."),
    ("tmdb", "Movie and TV metadata, posters, and cast lists. The modern successor to the older movie-database APIs."),
    ("youtube", "Search videos, pull channel statistics, and fetch thumbnail URLs. Powers most video-aggregator and tutorial-discovery tools."),
    ("twitter", "Post and read tweets via the v2 API. Useful for social dashboards and sentiment experiments, though it does require an API key."),
    ("reddit", "Read public posts and comments via simple JSON endpoints. Great for trend monitors and content aggregators - no official SDK needed."),
    ("mapbox", "Maps, geocoding, and routing with a generous free tier. The go-to choice for any location-aware web application."),
    ("rest-countries", "Country names, flags, currencies, and calling codes. No key, no signup - the classic geographic reference dataset."),
]
used = [(by_slug[slug], note) for slug, note in BEST_OF if slug in by_slug]

lines = []
lines.append("---")
lines.append('title: "The ' + str(len(used)) + ' Best Free Public APIs in 2026 for Side Projects and Hackathons"')
lines.append("published: true")
lines.append("description: >-")
lines.append("  A hand-picked list of the most useful free APIs - weather, payments, maps,")
lines.append("  media, and more - with notes on free-tier limits and when to pick each one.")
lines.append("tags: webdev, api, beginners, programming")
lines.append("canonical_url: " + ORIGIN + "/best-free-apis-2026")
lines.append("---")
lines.append("")
lines.append("Finding a good API is half the battle when you are starting a side project. You want something useful, well-documented, and ideally free enough that you can ship a demo without thinking about billing.")
lines.append("")
lines.append("I went through a directory of **" + str(len(DATA)) + " public APIs** and picked the " + str(len(used)) + " that I would actually reach for first. Every entry below has either a real free tier or needs no key at all, and I have noted *why* you would choose each one rather than just listing names.")
lines.append("")
lines.append("> This article is cross-posted from [OpenAPIHub](" + ORIGIN + "), a free directory of " + str(len(DATA)) + " public APIs across " + str(len({a['category'] for a in DATA})) + " categories. Each entry below links to a deeper profile there.")
lines.append("")
lines.append("## The list")
lines.append("")
for i, (a, note) in enumerate(used, 1):
    lines.append("### " + str(i) + ". [" + a["name"] + "](" + ORIGIN + "/api/" + a["slug"] + ")")
    lines.append("")
    auth_label = "needs an API key" if a.get("auth", "").lower() not in ("no", "") else "no key required"
    https_label = "HTTPS only" if a.get("https", "").lower() == "yes" else "HTTP/HTTPS"
    lines.append("**Category:** [" + a["category"] + "](" + ORIGIN + "/c/" + a["categorySlug"] + ") - **Auth:** " + auth_label + " - **Transport:** " + https_label)
    lines.append("")
    lines.append(note)
    lines.append("")
lines.append("## How to choose between them")
lines.append("")
lines.append("A quick heuristic that has served me well:")
lines.append("")
lines.append("- **Need a working demo in an hour?** Pick [Open-Meteo](" + ORIGIN + "/api/open-meteo) or [REST Countries](" + ORIGIN + "/api/rest-countries) - zero signup, zero keys.")
lines.append("- **Building something real that will ship?** [OpenWeatherMap](" + ORIGIN + "/api/openweathermap), [GitHub](" + ORIGIN + "/api/github), and [Mapbox](" + ORIGIN + "/api/mapbox) all have free tiers that survive real usage.")
lines.append("- **Want a dataset that is genuinely fun?** [NASA](" + ORIGIN + "/api/nasa) and [Unsplash](" + ORIGIN + "/api/unsplash) are hard to beat for visual demos.")
lines.append("")
lines.append("## Where to find more")
lines.append("")
lines.append("If none of these fit, there are " + str(len(DATA)) + " more in the [full OpenAPIHub directory](" + ORIGIN + "/), searchable and filterable by category, auth requirement, HTTPS support, and CORS. There is also an [editorial best-of page](" + ORIGIN + "/best-free-apis-2026) that this article is adapted from, and an [RSS feed](" + ORIGIN + "/feed.xml) if you want new APIs as they are added.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("*If this list saved you time, the best thing you can do is link to [OpenAPIHub](" + ORIGIN + ") from your own project README or blog. Backlinks are how a free directory like this stays independent.*")
lines.append("")
content = "\n".join(lines)
out_dir = SITE / "scripts" / "publish"
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "best-free-apis-2026.md").write_text(content, encoding="utf-8")
(SITE / "dist" / "best-free-apis-2026.md").write_text(content, encoding="utf-8")
print("wrote scripts/publish/best-free-apis-2026.md")
print("wrote dist/best-free-apis-2026.md")
print("article length:", len(content), "chars")
print("entries:", len(used))
