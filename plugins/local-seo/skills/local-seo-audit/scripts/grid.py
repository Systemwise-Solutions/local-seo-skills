#!/usr/bin/env python3
"""Geo-grid rankings: summarise a grid, or run one with your own DataForSEO key.

SUMMARY (works anywhere, no network):
  python grid.py summary grid.json [--business "Name"]

  grid.json:
    {"keyword": "emergency plumber", "business": "Example Plumbing",
     "center": [51.5074, -0.1278],
     "points": [{"lat": 51.5074, "lng": -0.1278, "rank": 2, "top": ["A", "B", "C"]}, ...]}
  "rank" is the business's map pack / Maps position at that point, or null if not in the results.
  "top" (optional) lists the businesses ranking 1-3 there, to find edge competitors.
  A 5-point phone check works too: give the 5 points with approximate coordinates.

SCAN (needs network and a DataForSEO account; costs money):
  export DATAFORSEO_LOGIN=... DATAFORSEO_PASSWORD=...
  python grid.py scan --keyword "emergency plumber" --lat 51.5074 --lng -0.1278 \
      --size 5 --spacing-km 1 --business "Example Plumbing" --out grid.json [--yes]

  Without --yes it only prints how many requests it would make. Each grid point is one
  Google Maps live request. Matches the business by name (case-insensitive substring)
  or by --domain.
"""
import argparse
import base64
import json
import math
import os
import sys
import urllib.request

API = "https://api.dataforseo.com/v3/serp/google/maps/live/advanced"


def km_between(a, b):
    r = 6371.0
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def grid_points(lat, lng, size, spacing_km):
    half = (size - 1) / 2
    dlat = spacing_km / 110.574
    dlng = spacing_km / (111.320 * math.cos(math.radians(lat)))
    return [(round(lat + (half - r) * dlat, 7), round(lng + (c - half) * dlng, 7), r, c)
            for r in range(size) for c in range(size)]


# ---------------------------------------------------------------- summary

def summarise(data, business=None):
    pts = data["points"]
    center = data.get("center") or [pts[0]["lat"], pts[0]["lng"]]
    name = business or data.get("business") or "the business"
    for p in pts:
        p["km"] = km_between(center, (p["lat"], p["lng"]))
    n = len(pts)
    top3 = [p for p in pts if p.get("rank") and p["rank"] <= 3]
    top10 = [p for p in pts if p.get("rank") and p["rank"] <= 10]

    # Strong radius: the largest distance d where at least 75% of points within d rank top 3.
    strong = 0.0
    for d in sorted({round(p["km"], 2) for p in pts}):
        inside = [p for p in pts if p["km"] <= d + 1e-9]
        if sum(1 for p in inside if p.get("rank") and p["rank"] <= 3) / len(inside) >= 0.75:
            strong = d
        else:
            break
    furthest = max(p["km"] for p in pts)

    out = [f"**{data.get('keyword', 'Search')}**, {name}, {n} points, furthest {furthest:.1f} km from the business",
           f"- Top 3 at {len(top3)} of {n} points ({100 * len(top3) / n:.0f}%), top 10 at {len(top10)} ({100 * len(top10) / n:.0f}%)",
           f"- Strong radius: {strong:.1f} km" + (" (not top 3 at the centre)" if strong == 0 else "")]
    center_pt = min(pts, key=lambda p: p["km"])
    if not center_pt.get("rank") or center_pt["rank"] > 3:
        out.append(f"- At the business itself: {'not found' if not center_pt.get('rank') else 'position ' + str(center_pt['rank'])}. Check relevance (category, services, landing page) before anything else.")
    lost = [p for p in pts if not (p.get("rank") and p["rank"] <= 3)]
    counts = {}
    for p in lost:
        for t in p.get("top", [])[:3]:
            if business and business.lower() in t.lower():
                continue
            counts[t] = counts.get(t, 0) + 1
    if counts:
        ranked = sorted(counts.items(), key=lambda kv: -kv[1])[:5]
        out.append("- Taking over where you drop out: " + ", ".join(f"{k} ({v} points)" for k, v in ranked))

    # ASCII map when the points form a square grid.
    size = int(round(math.sqrt(n)))
    if size * size == n and size >= 3 and all("row" in p and "col" in p for p in pts):
        out.append("\n```")
        for r in range(size):
            row = sorted((p for p in pts if p["row"] == r), key=lambda p: p["col"])
            out.append(" ".join(f"{p['rank']:>3}" if p.get("rank") else "  -" for p in row))
        out.append("```\n(- = not in the results; centre is the business)")
    return "\n".join(out)


# ---------------------------------------------------------------- scan

def request(task, login, password):
    body = json.dumps([task]).encode("utf-8")
    auth = base64.b64encode(f"{login}:{password}".encode()).decode()
    req = urllib.request.Request(API, data=body, method="POST",
                                 headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def scan(a):
    pts = grid_points(a.lat, a.lng, a.size, a.spacing_km)
    print(f"{len(pts)} grid points = {len(pts)} DataForSEO Maps requests for '{a.keyword}'.", file=sys.stderr)
    if not a.yes:
        print("Dry run. Re-run with --yes to make the requests.", file=sys.stderr)
        return
    login, password = os.environ.get("DATAFORSEO_LOGIN"), os.environ.get("DATAFORSEO_PASSWORD")
    if not login or not password:
        sys.exit("Set DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD as environment variables.")
    results, cost = [], 0.0
    for lat, lng, r, c in pts:
        task = {"keyword": a.keyword, "location_coordinate": f"{lat},{lng},{a.zoom}z",
                "language_code": a.language, "device": "mobile", "depth": a.depth}
        try:
            res = request(task, login, password)
        except Exception as e:  # network or HTTP error: record and carry on
            print(f"Point {r},{c} failed: {e}", file=sys.stderr)
            results.append({"lat": lat, "lng": lng, "row": r, "col": c, "rank": None, "top": [], "error": str(e)})
            continue
        cost += res.get("cost") or 0
        t = (res.get("tasks") or [{}])[0]
        items = ((t.get("result") or [{}])[0] or {}).get("items") or []
        organic = [i for i in items if i.get("type") == "maps_search"]
        rank = None
        for i in organic:
            title, domain = (i.get("title") or "").lower(), (i.get("domain") or "").lower()
            if (a.business and a.business.lower() in title) or (a.domain and a.domain.lower() in domain):
                rank = i.get("rank_group")
                break
        results.append({"lat": lat, "lng": lng, "row": r, "col": c, "rank": rank,
                        "top": [i.get("title") for i in organic[:3]]})
        print(f"{r},{c}: {rank or '-'}", file=sys.stderr)
    data = {"keyword": a.keyword, "business": a.business, "center": [a.lat, a.lng], "points": results,
            "source": "DataForSEO Google Maps live", "reported_cost_usd": round(cost, 4)}
    with open(a.out, "w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2)
    print(f"Saved {a.out}. API-reported cost: ${cost:.4f}", file=sys.stderr)
    print(summarise(data, a.business))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("summary", help="summarise a grid JSON file")
    s.add_argument("file")
    s.add_argument("--business")
    sc = sub.add_parser("scan", help="run a grid with DataForSEO (costs money)")
    sc.add_argument("--keyword", required=True)
    sc.add_argument("--lat", type=float, required=True)
    sc.add_argument("--lng", type=float, required=True)
    sc.add_argument("--size", type=int, default=5, help="points per side (odd number), default 5")
    sc.add_argument("--spacing-km", type=float, default=1.0)
    sc.add_argument("--business", help="business name as shown on Maps")
    sc.add_argument("--domain", help="business website domain, an alternative match")
    sc.add_argument("--zoom", type=int, default=15)
    sc.add_argument("--depth", type=int, default=20)
    sc.add_argument("--language", default="en")
    sc.add_argument("--out", default="grid.json")
    sc.add_argument("--yes", action="store_true", help="actually make the paid requests")
    a = ap.parse_args()
    if a.cmd == "summary":
        with open(a.file, encoding="utf-8") as fh:
            print(summarise(json.load(fh), a.business))
    else:
        if a.size % 2 == 0:
            sys.exit("--size must be odd so the business sits at the centre")
        if not (a.business or a.domain):
            sys.exit("Give --business or --domain so the business can be found in the results")
        scan(a)


if __name__ == "__main__":
    main()
