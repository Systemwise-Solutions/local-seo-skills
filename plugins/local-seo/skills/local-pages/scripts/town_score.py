#!/usr/bin/env python3
"""Score candidate towns or areas for location pages: create, hold or don't create, with reasons.

A location page earns its place only where the business can compete (close enough,
real work or customers there) and has something specific to say (real examples there,
reviews naming the place, local facts, staff or premises there). This script applies
that rule the same way every time so the page plan is consistent. It is the same for
every kind of business; what changes is the input (see "Reading the lens" below).

Input JSON:
  {
    "business": {"name": "Example Business", "lat": 51.50, "lng": -0.12,
                 "max_travel_km": 20,          # how far the business travels, or customers travel to it (default 30)
                 "strong_radius_km": 3,        # optional, from the audit's grid.py summary
                 "jobs_target": 10,            # optional: count in the window that means "plenty" (default 10)
                 "unit": "jobs"},              # optional: what is being counted, in the owner's words:
                                               # jobs, customers, orders, bookings, clients (default "jobs")
    "towns": [
      {"name": "Northside",
       "lat": 51.52, "lng": -0.10,             # or "distance_km": 4.2
       "is_base": false,                       # true for the town the business is based in
       "jobs": 14,                             # how many there in the window; "customers", "orders" or "bookings" also accepted
       "monthly_searches": 50,                 # optional; from a keyword tool, give the source
       "demand_source": "Keyword Planner range 10-100 (reported)",
       "competition": "medium",                # optional: low | medium | high
       "content": {"jobs_with_photos": 6,      # real examples there with photos; "examples" also accepted
                   "reviews_naming_town": 2,
                   "local_facts": ["fact that changes what customers there need", "travel or access detail"],
                   "team_or_depot": false},    # staff or premises there; "staff_or_premises" also accepted
       "existing_page": "/areas/northside/",   # optional, if the site already has one
       "page_leads": 0}                        # optional, enquiries that page brought in the window
    ]
  }

Reading the lens:
  Goes to customers: max_travel_km is how far the business goes for work; count work done in each place.
  Customers come to it: max_travel_km is how far customers genuinely travel in; count customers from
  each place (postcodes from bookings, orders or loyalty data). Expect few or no "create" results.

Scoring (0 to 100): proximity 35, work there 35, search demand 15, competition 15.
Demand and competition are left out and the rest re-weighted when not known.
Local proof is counted separately, out of 4: 3+ examples with photos, 2+ reviews naming
the place, 2+ local facts, staff or premises there. These thresholds, and the score
cut-offs below, are Mani Bharij's working rule of thumb, not a published standard.

Decisions:
  don't create  base town (the service pages already cover it), beyond max travel,
                no work or customers there, or score under 40
  create        score 60+ and local proof 3+ of 4
  hold          everything else: worth a page once the missing proof is collected

Usage:
  python town_score.py towns.json
  python town_score.py towns.json --json
"""
import argparse
import json
import math
import sys

WEIGHTS = {"proximity": 35, "jobs": 35, "demand": 15, "competition": 15}
COMPETITION = {"low": 1.0, "medium": 0.6, "high": 0.25}
DEMAND_FULL = 100  # monthly searches at which demand scores full marks


def km_between(a, b):
    r = 6371.0
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    h = math.sin((la2 - la1) / 2) ** 2 + math.cos(la1) * math.cos(la2) * math.sin((lo2 - lo1) / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def distance(biz, t):
    if t.get("distance_km") is not None:
        return float(t["distance_km"])
    if None not in (t.get("lat"), t.get("lng"), biz.get("lat"), biz.get("lng")):
        return km_between((biz["lat"], biz["lng"]), (t["lat"], t["lng"]))
    sys.exit(f"Town '{t.get('name')}': give distance_km, or lat and lng for the town and the business")


def proof(t, unit="jobs"):  # unit: what the owner counts, used in the wording only
    c = dict(t.get("content") or {})
    if "jobs_with_photos" not in c and "examples" in c:
        c["jobs_with_photos"] = c["examples"]
    if "team_or_depot" not in c and "staff_or_premises" in c:
        c["team_or_depot"] = c["staff_or_premises"]
    have, missing = [], []
    checks = [
        (c.get("jobs_with_photos", 0) >= 3, f"{c.get('jobs_with_photos', 0)} real examples there", f"3+ real examples there ({unit} you can show, with photos or detail) (have {c.get('jobs_with_photos', 0)})"),
        (c.get("reviews_naming_town", 0) >= 2, f"{c.get('reviews_naming_town', 0)} reviews naming the town", f"2+ reviews that name the town (have {c.get('reviews_naming_town', 0)})"),
        (len(c.get("local_facts") or []) >= 2, f"{len(c.get('local_facts') or [])} local facts", f"2+ facts specific to the place, such as travel time, access, local rules or what customers there typically need (have {len(c.get('local_facts') or [])})"),
        (bool(c.get("team_or_depot")), "staff or premises there", "staff or premises there (optional)"),
    ]
    for ok, label, need in checks:
        (have if ok else missing).append(label if ok else need)
    return sum(1 for ok, _, _ in checks if ok), have, missing


def score_town(biz, t):
    d = distance(biz, t)
    max_km = float(biz.get("max_travel_km") or 0) or None
    jobs = next((t[k] for k in ("jobs", "customers", "orders", "bookings") if t.get(k) is not None), 0) or 0
    unit = biz.get("unit") or "jobs"
    one = unit[:-1] if unit.endswith("s") else unit
    target = biz.get("jobs_target") or 10
    parts, reasons = {}, []

    parts["proximity"] = max(0.0, 1 - d / max_km) if max_km else max(0.0, 1 - d / 30)
    parts["jobs"] = min(1.0, math.log1p(jobs) / math.log1p(target))
    if t.get("monthly_searches") is not None:
        parts["demand"] = min(1.0, math.log1p(t["monthly_searches"]) / math.log1p(DEMAND_FULL))
    comp = (t.get("competition") or "").lower()
    if comp in COMPETITION:
        parts["competition"] = COMPETITION[comp]
    total_w = sum(WEIGHTS[k] for k in parts)
    score = round(100 * sum(WEIGHTS[k] * v for k, v in parts.items()) / total_w)
    n_proof, have, missing = proof(t, unit)

    # Reasons, in plain words
    reasons.append(f"{d:.1f} km away" + (f" (travel limit {max_km:g} km)" if max_km else ""))
    sr = biz.get("strong_radius_km")
    if sr is not None:
        if d <= sr:
            reasons.append(f"inside your strong radius ({sr:g} km): you can already win the map pack here")
        else:
            reasons.append(f"{d - sr:.1f} km beyond your strong radius: the page has to win in the organic results first")
    reasons.append(f"{jobs} {unit if jobs != 1 else one} there" if jobs else f"no {unit} there yet")
    if "demand" in parts:
        reasons.append(f"about {t['monthly_searches']} searches a month" + (f" ({t['demand_source']})" if t.get("demand_source") else ""))
    else:
        reasons.append("search demand not known")
    if "competition" in parts:
        reasons.append(f"{comp} competition")
    if have:
        reasons.append("local proof: " + ", ".join(have))

    # Decision
    if t.get("is_base"):
        decision, why = "don't create", "base town: the homepage and service pages already target it; a separate page would compete with them"
    elif max_km and d > max_km:
        decision, why = "don't create", "beyond how far you, or your customers, actually travel"
    elif not jobs:
        decision, why = "don't create", f"no {unit} there to show, so the page could only swap the town name"
    elif score >= 60 and n_proof >= 3:
        decision, why = "create", f"close enough to compete, real {unit} there, and enough to say that no competitor could copy"
    elif score < 40:
        decision, why = "don't create", f"too far or too few {unit} there to compete; the service pages and profile cover it"
    else:
        decision = "hold"
        why = "worth a page once you have: " + "; ".join(m for m in missing if "optional" not in m) if score >= 60 \
            else "borderline: build the service pages first, then revisit at the next review"

    existing = t.get("existing_page")
    if decision == "create":
        action = "keep, rebuild with the local detail" if existing else "create"
    elif decision == "hold":
        action = "keep, add the missing detail" if existing else "hold"
    elif existing and (t.get("page_leads") or 0) > 0:
        action = f"keep ({t['page_leads']} enquiries), rebuild with real detail or fold into a stronger page"
    elif existing:
        action = "merge: 301 to the closest service page"
    else:
        action = "-"

    return {"name": t["name"], "km": round(d, 1), "jobs": jobs, "demand": t.get("monthly_searches"),
            "competition": comp or None, "proof": n_proof, "score": score, "decision": decision,
            "why": why, "reasons": reasons, "missing_proof": missing, "existing_page": existing, "action": action}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("towns", help="towns.json")
    ap.add_argument("--json", action="store_true", help="output JSON instead of Markdown")
    a = ap.parse_args()
    with open(a.towns, encoding="utf-8") as fh:
        data = json.load(fh)
    biz, towns = data.get("business") or {}, data.get("towns") or []
    if not towns:
        sys.exit("No towns in the input")
    order = {"create": 0, "hold": 1, "don't create": 2}
    rows = sorted((score_town(biz, t) for t in towns), key=lambda r: (order[r["decision"]], -r["score"]))

    if a.json:
        print(json.dumps(rows, indent=2))
        return
    counts = {k: sum(1 for r in rows if r["decision"] == k) for k in order}
    dont = counts["don't create"]
    print(f"**{biz.get('name', 'Business')}**: {counts['create']} create, {counts['hold']} hold, {dont} don't create\n")
    unit = (biz.get("unit") or "jobs").capitalize()
    print(f"| Town | km | {unit} | Searches/mo | Competition | Local proof | Score | Decision | Site action |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['name']} | {r['km']} | {r['jobs']} | {r['demand'] if r['demand'] is not None else 'unknown'} | "
              f"{r['competition'] or 'unknown'} | {r['proof']}/4 | {r['score']} | **{r['decision']}** | {r['action']} |")
    print("\n**Reasons**\n")
    for r in rows:
        print(f"- **{r['name']}** ({r['decision']}): {r['why']}. {'; '.join(r['reasons'])}.")
    unknown = [r["name"] for r in rows if r["demand"] is None]
    if unknown and len(unknown) == len(rows):
        print("\nNo search demand supplied, so scores rest on distance, where the work is and proof. That is usually enough for a small area.")


if __name__ == "__main__":
    main()
