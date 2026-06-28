(function () {
  var params = new URLSearchParams(window.location.search);
  var q = (params.get("q") || "").trim();
  var input = document.getElementById("search-input");
  var resultsEl = document.getElementById("search-results");
  var emptyEl = document.getElementById("search-empty");
  var form = document.getElementById("search-form");

  function render(query) {
    resultsEl.innerHTML = "";
    if (!query) {
      emptyEl.style.display = "none";
      return;
    }
    var needle = query.toLowerCase();
    var matches = (window.__APIS__ || []).filter(function (a) {
      return a.n.toLowerCase().indexOf(needle) !== -1
        || a.d.toLowerCase().indexOf(needle) !== -1
        || a.c.toLowerCase().indexOf(needle) !== -1;
    }).slice(0, 60);

    if (!matches.length) {
      emptyEl.style.display = "block";
      return;
    }
    emptyEl.style.display = "none";
    matches.forEach(function (a) {
      var card = document.createElement("a");
      card.className = "api-card";
      card.href = "/api/" + encodeURIComponent(a.s);
      var desc = a.d.slice(0, 140) + (a.d.length > 140 ? "\u2026" : "");
      card.innerHTML =
        "<h3>" + a.n + "</h3>"
        + "<p>" + desc + "</p>"
        + '<div class="api-meta"><span class="badge">' + a.c + "</span></div>";
      resultsEl.appendChild(card);
    });
  }

  if (q) input.value = q;
  render(q);

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var v = input.value.trim();
    var newUrl = window.location.pathname + (v ? "?q=" + encodeURIComponent(v) : "");
    window.history.replaceState(null, "", newUrl);
    render(v);
  });

  input.addEventListener("input", function () {
    var v = input.value.trim();
    var newUrl = window.location.pathname + (v ? "?q=" + encodeURIComponent(v) : window.location.pathname);
    window.history.replaceState(null, "", newUrl);
    render(v);
  });
})();
