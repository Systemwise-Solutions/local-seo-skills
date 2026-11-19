#!/usr/bin/env python3
"""Score candidate towns or areas for location pages: create, hold or don't create, with reasons.

A location page earns its place only where the business can compete (close enough,
real work there) and has something specific to say (jobs with photos, reviews naming
the town, local facts, a team member or depot there). This script applies that rule
the same way every time so the page plan is consistent.

Input JSON:
  {
    "business": {"name": "Example Heating", "lat": 53.841, "lng": -1.638,
                 "max_travel_km": 20,          # how far you'll actually go for a job (default 30 if left out)
                 "strong_radius_km": 3,        # optional, from the audit's grid.py summary
                 "jobs_target": 10},           # optional: jobs in the window that count as "plenty" (default 10)
    "towns": [
      {"name": "Headingley",
       "lat": 53.819, "lng": -1.580,           # or "distance_km": 4.2
       "is_base": false,                       # true for the town the business is based in
       "jobs": 14,                             # jobs or customers there in the window you're using
       "monthly_searches": 50,                 # optional; from a keyword tool, give the source
       "demand_source": "Keyword Planner range 10-100 (reported)",
       "competition": "medium",                # optional: low | medium | high
       "content": {"jobs_with_photos": 6, "reviews_naming_town": 2,
                   "local_facts": ["Victorian terraces, lots of combi swaps", "student lets: landlord certificates"],
                   "team_or_depot": false},
       "existing_page": "/areas/headingley/",  # optional, if the site already has one
       "page_leads": 0}                        # optional, enquiries that page brought in the window
    ]
  }

Scoring (0 to 100): proximity 35, jobs 35, search demand 15, competition 15.
Demand and competition are left out and the rest re-weighted when not known.
Local proof is counted separately, out of 4: 3+ jobs with photos, 2+ reviews naming
the town, 2+ local facts, a team member or depot there.

Decisions:
  don't create  base town (the service pages already cover it), beyond max travel,
                no jobs there, or score under 40
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


def proof(t):
    c = t.get("content") or {}
    have, missing = [], []
    checks = [
        (c.get("jobs_with_photos", 0) >= 3, f"{c.get('jobs_with_photos', 0)} jobs with photos", f"3+ jobs there with photos (have {c.get('jobs_with_photos', 0)})"),
        (c.get("reviews_naming_town", 0) >= 2, f"{c.get('reviews_naming_town', 0)} reviews naming the town", f"2+ reviews that name the town (have {c.get('reviews_naming_town', 0)})"),
        (len(c.get("local_facts") or []) >= 2, f"{len(c.get('local_facts') or [])} local facts", f"2+ facts specific to the place, such as housing stock, parking or local rules (have {len(c.get('local_facts') or [])})"),
        (bool(c.get("team_or_depot")), "team member or depot there", "a team member or depot there (optional)"),
    ]
    for ok, label, need in checks:
        (have if ok else missing).append(label if ok else need)
    return sum(1 for ok, _, _ in checks if ok), have, missing


def score_town(biz, t):
    d = distance(biz, t)
    max_km = float(biz.get("max_travel_km") or 0) or None
    jobs = t.get("jobs", t.get("customers")) or 0
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
    n_proof, have, missing = proof(t)

    # Reasons, in plain words
    reasons.append(f"{d:.1f} km away" + (f" (you travel up to {max_km:g} km)" if max_km else ""))
    sr = biz.get("strong_radius_km")
    if sr is not None:
        if d <= sr:
            reasons.append(f"inside your strong radius ({sr:g} km): you can already win the map pack here")
        else:
            reasons.append(f"{d - sr:.1f} km beyond your strong radius: the page has to win in the organic results first")
    reasons.append(f"{jobs} job{'s' if jobs != 1 else ''} there" if jobs else "no jobs there yet")
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
        decision, why = "don't create", "outside where you travel for work"
    elif not jobs:
        decision, why = "don't create", "no work there to show, so the page could only swap the town name"
    elif score >= 60 and n_proof >= 3:
        decision, why = "create", "close enough to compete, real work there, and enough to say that no competitor could copy"
    elif score < 40:
        decision, why = "don't create", "too far or too little work there to compete; the service pages and profile cover it"
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
    print("| Town | km | Jobs | Searches/mo | Competition | Local proof | Score | Decision | Site action |")
    print("|---|---|---|---|---|---|---|---|---|")
    for r in rows:
        print(f"| {r['name']} | {r['km']} | {r['jobs']} | {r['demand'] if r['demand'] is not None else 'unknown'} | "
              f"{r['competition'] or 'unknown'} | {r['proof']}/4 | {r['score']} | **{r['decision']}** | {r['action']} |")
    print("\n**Reasons**\n")
    for r in rows:
        print(f"- **{r['name']}** ({r['decision']}): {r['why']}. {'; '.join(r['reasons'])}.")
    unknown = [r["name"] for r in rows if r["demand"] is None]
    if unknown and len(unknown) == len(rows):
        print("\nNo search demand supplied, so scores rest on distance, jobs and proof. That is usually enough for a small service area.")


if __name__ == "__main__":
    main()
