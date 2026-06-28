// Cloudflare Workers entry point.
// Static assets in ../dist are served automatically via the [assets] binding
// in wrangler.toml. This Worker is intentionally minimal: when a request does
// not match a static file, the assets binding's not_found_handling returns
// dist/404.html. We keep a fetch handler so `wrangler deploy` is happy and so
// the project remains a valid Worker.
export default {
  async fetch(request, env, ctx) {
    // ASSETS binding is auto-injected when [assets] directory is set.
    // Forward any unhandled request to the assets binding as a fallback.
    if (env.ASSETS) {
      return env.ASSETS.fetch(request);
    }
    return new Response("Not Found", { status: 404 });
  },
};