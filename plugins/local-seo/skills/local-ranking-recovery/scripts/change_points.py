#!/usr/bin/env python3
"""Find where dated metrics changed, and list the events just before each change.

Give it weekly (or daily, or monthly) series such as profile calls, website clicks,
grid coverage, average grid rank or Search Console clicks, plus a dated list of
events (profile edits, suspensions, website launches, review changes, competitor
moves, confirmed Google updates). It finds the biggest step changes in each series,
says whether each one was a cliff or a slope, lines up the events in a window before
it, and says whether local and organic moved together.

It finds timing, not cause. An event in the window is a lead to check, not proof.

Input JSON:
  {
    "business": "Example Business (fictional)",
    "series": [
      {"name": "Profile calls", "surface": "profile", "higher_is_better": true,
       "points": [["2026-06-01", 41], ["2026-06-08", 38], ...]},
      {"name": "Avg grid rank: main service", "surface": "maps", "higher_is_better": false,
       "points": [{"date": "2026-06-01", "value": 2.4}, ...]}
    ],
    "events": [
      {"date": "2026-08-12", "type": "profile_edit", "what": "Primary category changed"},
      {"date": "2026-09-03", "type": "google_update", "what": "Core update", "confirmed": false,
       "source": "user remembers 'early September'"}
    ]
  }

surface: profile, maps, local_pack, ai_mode, organic or other. Organic series let the
script tell a local-only drop from a site-wide one.
higher_is_better: false for ranks and positions (lower is better). Default true.
value null = a gap (not reported), never treated as zero.
Event types: profile_edit, suspension, verification, merge, website, google_update,
reviews, competitor, filtering, measurement, other. "confirmed": false marks a date
nobody has checked (Google updates must be checked against Google's own status page).

A CSV of series also works: --csv series.csv with a "date" column and one column
per metric. Columns with "rank" or "position" in the name are treated as lower is
better; add "[organic]", "[maps]" etc. to a column name to set its surface.

Usage:
  python change_points.py recovery.json
  python change_points.py recovery.json --window-days 28 --min-change 0.15
  python change_points.py events.json --csv series.csv
  python change_points.py recovery.json --json
"""
import argparse
import csv
import json
import math
import re
import statistics
import sys
from datetime import datetime, timedelta

SURFACES = {"profile", "maps", "local_pack", "ai_mode", "organic", "other"}
LOCAL = {"profile", "maps", "local_pack", "ai_mode"}
EVENT_TYPES = {"profile_edit", "suspension", "verification", "merge", "website", "google_update",
               "reviews", "competitor", "filtering", "measurement", "other"}


def parse_date(s):
    try:
        return datetime.strptime(str(s).strip()[:10], "%Y-%m-%d").date()
    except ValueError:
        sys.exit(f"Can't read the date '{s}'. Use YYYY-MM-DD.")


def read_points(raw, name):
    pts = []
    for p in raw:
        if isinstance(p, dict):
            d, v = p.get("date"), p.get("value")
        else:
            d, v = p[0], p[1]
        if v is None or v == "":
            continue
        try:
            pts.append((parse_date(d), float(v)))
        except (TypeError, ValueError):
            sys.exit(f"Series '{name}': can't read the value '{v}' on {d}.")
    pts.sort()
    return pts


def load_csv(path):
    with open(path, encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if not rows or "date" not in rows[0]:
        sys.exit("The CSV needs a 'date' column.")
    out = []
    for col in rows[0]:
        if col == "date":
            continue
        m = re.search(r"\[(\w+)\]", col)
        surface = m.group(1).lower() if m and m.group(1).lower() in SURFACES else "other"
        name = re.sub(r"\s*\[\w+\]", "", col).strip()
        lower_better = bool(re.search(r"rank|position", name, re.I))
        out.append({"name": name, "surface": surface, "higher_is_better": not lower_better,
                    "points": [[r["date"], r[col] if r[col] != "" else None] for r in rows]})
    return out


# ---------------------------------------------------------------- change points

def sse(v):
    if not v:
        return 0.0
    m = sum(v) / len(v)
    return sum((x - m) ** 2 for x in v)


def best_split(vals, min_side):
    n = len(vals)
    best = None
    for k in range(min_side, n - min_side + 1):
        cost = sse(vals[:k]) + sse(vals[k:])
        if best is None or cost < best[1]:
            best = (k, cost)
    if best is None:
        return None
    k, cost = best
    left, right = vals[:k], vals[k:]
    ml, mr = statistics.mean(left), statistics.mean(right)
    sd = math.sqrt(cost / (n - 2)) if n > 2 else 0.0
    gap = abs(mr - ml)
    score = math.inf if sd == 0 and gap > 0 else (gap / sd * math.sqrt(len(left) * len(right) / n) if sd else 0.0)
    return k, ml, mr, score


def rel(a, b):
    return (b - a) / abs(a) if a else (math.inf if b > a else -math.inf if b < a else 0.0)


def segment(vals, lo, hi, min_side, threshold, min_change, found, cap):
    if len(found) >= cap or hi - lo < 2 * min_side:
        return
    r = best_split(vals[lo:hi], min_side)
    if not r:
        return
    k, ml, mr, score = r
    if score < threshold or abs(rel(ml, mr)) < min_change:
        return
    found.append(lo + k)
    segment(vals, lo, lo + k, min_side, threshold, min_change, found, cap)
    segment(vals, lo + k, hi, min_side, threshold, min_change, found, cap)


def shape(before, step):
    """Cliff or slope: was the series already moving the same way before the split?"""
    tail = before[-6:]
    if len(tail) < 3 or step == 0:
        return "cliff"
    xs = range(len(tail))
    mx, my = statistics.mean(xs), statistics.mean(tail)
    den = sum((x - mx) ** 2 for x in xs)
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, tail)) / den if den else 0.0
    drift = slope * (len(tail) - 1)
    return "slope" if drift * step > 0 and abs(drift) >= 0.5 * abs(step) else "cliff"


def changes_for(series, args):
    pts = series["pts"]
    dates, vals = [d for d, _ in pts], [v for _, v in pts]
    gaps = [(dates[i + 1] - dates[i]).days for i in range(len(dates) - 1)]
    bucket = int(statistics.median(gaps)) if gaps else 7
    found = []
    segment(vals, 0, len(vals), args.min_side, args.threshold, args.min_change, found, args.max_changes)
    found.sort()
    bounds = [0] + found + [len(vals)]
    out = []
    for i, k in enumerate(found):
        before, after = vals[bounds[i]:k], vals[k:bounds[i + 2]]
        ml, mr = statistics.mean(before), statistics.mean(after)
        worse = mr < ml if series["higher_is_better"] else mr > ml
        r = best_split(before + after, 1)
        out.append({
            "series": series["name"], "surface": series["surface"],
            "last_before": dates[k - 1], "first_after": dates[k], "bucket_days": bucket,
            "mean_before": ml, "mean_after": mr, "change": rel(ml, mr),
            "direction": "drop" if worse else "rise",
            "shape": shape(before, mr - ml),
            "strength": "clear" if (r and r[3] >= args.threshold * 1.5) else "possible",
            "score": r[3] if r else 0.0,
            "n_before": len(before), "n_after": len(after),
        })
    return out, bucket


def events_near(day, last_before, bucket, events, window):
    """Events from `window` days before the first worse period to `window` days after it.

    Returns (event, label, before) where before is True if the event could have
    triggered the change (it falls before the end of the first changed period).
    """
    end = day + timedelta(days=bucket - 1)
    hits = []
    for e in events:
        delta = (day - e["d"]).days
        if e["d"] < day - timedelta(days=window) or e["d"] > day + timedelta(days=window):
            continue
        if e["d"] < day:
            label = f"{delta} days before the first changed period"
            if e["d"] > last_before:
                label += ", inside the last period that still looked normal"
            hits.append((e, label, True))
        elif e["d"] <= end:
            hits.append((e, "during the first changed period", True))
        else:
            hits.append((e, f"{-delta} days after the change began: not the trigger, may slow recovery", False))
    hits.sort(key=lambda h: (not h[2], h[0]["d"]))
    return hits


def cluster_frame(cl):
    """The earliest first-changed date, and the finest-grained series' last normal date and bucket."""
    day = min(c["first_after"] for c in cl)
    bucket = min(c["bucket_days"] for c in cl)
    fine = [c for c in cl if c["bucket_days"] == bucket]
    last_before = min(c["last_before"] for c in fine)
    return day, last_before, bucket


def around(series, day, n=4):
    pts = series["pts"]
    before = [v for d, v in pts if d < day][-n:]
    after = [v for d, v in pts if d >= day][:n]
    if not before or not after:
        return None
    return rel(statistics.mean(before), statistics.mean(after))


def verdict(cluster, all_series, window):
    surfaces = {c["surface"] for c in cluster}
    day = min(c["first_after"] for c in cluster)
    organic = [s for s in all_series if s["surface"] == "organic"]
    local_hit = surfaces & LOCAL
    if not organic:
        return "No organic series supplied, so a local-only drop can't be told apart from a site-wide one. Add Search Console clicks (non-branded if possible)."
    if "organic" in surfaces and local_hit:
        return "Local and organic dropped together. Check the website first (launch, migration, removed pages, noindex, changed NAP) and any confirmed Google update, then the profile."
    if "organic" in surfaces:
        return "Organic dropped, local surfaces did not. This is a website or Google update question: hand to technical SEO."
    steady = []
    for s in organic:
        a = around(s, day)
        if a is not None:
            steady.append(f"{s['name']} {a:+.0%}")
    return ("Local only: organic held (" + ", ".join(steady) + " over the same weeks). Look at the profile, filtering, reviews and competitors before the website."
            if steady else "Local surfaces dropped; the organic series doesn't cover these dates.")


def fmt_val(v, s):
    return f"{v:.1f}" if not s["higher_is_better"] or abs(v) < 20 else f"{v:.0f}"


def fmt_change(c, s):
    if not s["higher_is_better"]:
        return f"{c['mean_after'] - c['mean_before']:+.1f} positions"
    return f"{c['change']:+.0%}"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="JSON with series and/or events")
    ap.add_argument("--csv", help="series as CSV (date column plus one column per metric)")
    ap.add_argument("--window-days", type=int, default=28, help="look this far back for events before a change (default 28)")
    ap.add_argument("--min-change", type=float, default=0.15, help="smallest relative change to report, 0.15 = 15%% (default)")
    ap.add_argument("--threshold", type=float, default=3.0, help="how clean a step must be to count (default 3.0; lower finds more)")
    ap.add_argument("--min-side", type=int, default=3, help="points needed each side of a change (default 3)")
    ap.add_argument("--max-changes", type=int, default=3, help="most changes to report per series (default 3)")
    ap.add_argument("--json", action="store_true", help="output JSON instead of Markdown")
    args = ap.parse_args()

    with open(args.file, encoding="utf-8") as fh:
        data = json.load(fh)
    raw_series = list(data.get("series", [])) + (load_csv(args.csv) if args.csv else [])
    if not raw_series:
        sys.exit("No series found. Add a 'series' list to the JSON or pass --csv.")
    series, warnings = [], []
    for s in raw_series:
        surface = (s.get("surface") or "other").lower()
        if surface not in SURFACES:
            warnings.append(f"Series '{s['name']}': unknown surface '{surface}', treated as other.")
            surface = "other"
        pts = read_points(s.get("points", []), s["name"])
        gaps = len(s.get("points", [])) - len(pts)
        if gaps:
            warnings.append(f"Series '{s['name']}': {gaps} gap(s) with no value, skipped rather than counted as zero.")
        raw_dates = [parse_date(p["date"] if isinstance(p, dict) else p[0]) for p in s.get("points", [])]
        if pts and raw_dates and max(raw_dates) > pts[-1][0]:
            warnings.append(f"Series '{s['name']}' stops reporting after {pts[-1][0]}. A profile that stops reporting can mean a suspension "
                            "or a disconnected profile. Don't read it as zero; use call tracking or grid scans for those weeks.")
        if len(pts) < 2 * args.min_side:
            warnings.append(f"Series '{s['name']}': only {len(pts)} points, too few to find a change.")
        series.append({"name": s["name"], "surface": surface, "higher_is_better": s.get("higher_is_better", True), "pts": pts})

    events = []
    for e in data.get("events", []):
        t = (e.get("type") or "other").lower()
        if t not in EVENT_TYPES:
            warnings.append(f"Event '{e.get('what', '?')}': unknown type '{t}'.")
        events.append({**e, "type": t, "d": parse_date(e["date"]), "confirmed": e.get("confirmed", True)})
    events.sort(key=lambda e: e["d"])

    changes = []
    for s in series:
        if len(s["pts"]) >= 2 * args.min_side:
            changes.extend(changes_for(s, args)[0])
    changes.sort(key=lambda c: (c["direction"] != "drop", c["first_after"]))

    # Group changes on different series that show up within one bucket of each other.
    clusters = []
    for c in [c for c in changes if c["direction"] == "drop"]:
        for cl in clusters:
            if abs((cl[0]["first_after"] - c["first_after"]).days) <= max(cl[0]["bucket_days"], c["bucket_days"]):
                cl.append(c)
                break
        else:
            clusters.append([c])

    span = max((s["pts"][-1][0] - s["pts"][0][0]).days for s in series if s["pts"])
    if span < 365:
        warnings.append(f"The data covers {span} days, less than a year, so seasonality can't be ruled out. Compare with the same weeks last year if you have them.")
    unconfirmed = [e for e in events if not e["confirmed"]]

    if args.json:
        conv = lambda o: o.isoformat() if hasattr(o, "isoformat") else str(o)
        out = {"changes": [{**c, "events": [{"date": e["date"], "type": e["type"], "what": e.get("what"), "confirmed": e["confirmed"], "when": w, "could_trigger": b}
                                            for e, w, b in events_near(c["first_after"], c["last_before"], c["bucket_days"], events, args.window_days)]} for c in changes],
               "drop_groups": [{"from": str(min(c["first_after"] for c in cl)), "series": [c["series"] for c in cl],
                                "verdict": verdict(cl, series, args.window_days)} for cl in clusters],
               "warnings": warnings}
        print(json.dumps(out, indent=2, default=conv))
        return

    print(f"# Change points: {data.get('business', 'the business')}\n")
    print(f"{len(series)} series, {len(events)} events. Events listed from {args.window_days} days before each change "
          f"to {args.window_days} days after. Timing is a lead, not proof of cause.\n")
    if not changes:
        print("No change bigger than the threshold in any series. If the user is sure something dropped, check the data "
              "covers the dates, or lower --threshold / --min-change and say so in the report.")
    for i, cl in enumerate(clusters, 1):
        day = cluster_frame(cl)[0]
        print(f"## Drop {i}: shows from the period starting {day}\n")
        print("| Series | Surface | Before | After | Change | Shape | Strength |")
        print("|---|---|---|---|---|---|---|")
        for c in cl:
            s = next(x for x in series if x["name"] == c["series"])
            print(f"| {c['series']} | {c['surface']} | {fmt_val(c['mean_before'], s)} | {fmt_val(c['mean_after'], s)} | "
                  f"{fmt_change(c, s)} | {c['shape']} | {c['strength']} |")
        print(f"\n{verdict(cl, series, args.window_days)}\n")
        cday, clast, cbucket = cluster_frame(cl)
        hits = events_near(cday, clast, cbucket, events, args.window_days)
        before = [h for h in hits if h[2]]
        after = [h for h in hits if not h[2]]
        if before:
            print("Events that could have triggered it (in date order):")
            for e, w, _ in before:
                flag = " **(date not confirmed)**" if not e["confirmed"] else ""
                src = f" Source: {e['source']}." if e.get("source") else ""
                print(f"- {e['date']} [{e['type']}] {e.get('what', '')}: {w}.{flag}{src}")
        else:
            print(f"No events in the {args.window_days} days before. Ask what changed in those weeks: profile edits, the website, reviews, competitors, tracking.")
        if any(e["type"] == "suspension" for e, _, _ in before):
            print("\nA suspension is in the window. It explains the drop. The work is finding what caused the suspension, "
                  "which may be an edit made months earlier and outside this window.")
        if after:
            print("\nAfter it began:")
            for e, w, _ in after:
                flag = " **(date not confirmed)**" if not e["confirmed"] else ""
                print(f"- {e['date']} [{e['type']}] {e.get('what', '')}: {w}.{flag}")
        print()
        if any(c["shape"] == "slope" for c in cl):
            print("At least one series was already falling before this date (slope). Slopes point more to competitors, decay or an update than to a single edit.\n")
    rises = [c for c in changes if c["direction"] == "rise"]
    if rises:
        print("## Rises\n")
        for c in rises:
            s = next(x for x in series if x["name"] == c["series"])
            print(f"- {c['series']} ({c['surface']}): {fmt_change(c, s)} from the period starting {c['first_after']} ({c['shape']}, {c['strength']})")
            for e, w, b in events_near(c["first_after"], c["last_before"], c["bucket_days"], events, args.window_days):
                if b:
                    print(f"  - {e['date']} [{e['type']}] {e.get('what', '')}: {w}.")
        print()
    if unconfirmed:
        print("## Dates to confirm\n")
        for e in unconfirmed:
            print(f"- {e['date']} {e.get('what', '')}" + (f" ({e['source']})" if e.get("source") else ""))
        print("Check Google updates against Google's own status page before naming one as a cause.\n")
    if warnings:
        print("## Notes\n")
        for w in warnings:
            print(f"- {w}")


if __name__ == "__main__":
    main()
