#!/usr/bin/env python3
"""Compare review velocity and recency for a business against its competitors.

Input JSON:
  {
    "as_of": "2026-11-19",                       # optional, defaults to today
    "businesses": [
      {"name": "Your business", "you": true, "total": 84, "rating": 4.8,
       "dates": ["2026-11-02", "2026-10-15", ...]},   # recent review dates, newest 20-30 is enough
      {"name": "Competitor A", "total": 210, "rating": 4.7, "dates": [...]}
    ]
  }
Relative dates such as "3 weeks ago" or "2 months ago" (as Google Maps shows them) are accepted.

Output: a table and the findings that apply, as Markdown.

Usage:
  python review_velocity.py reviews.json
"""
import argparse
import json
import math
import re
import statistics
import sys
from datetime import date, datetime, timedelta

UNITS = {"day": 1, "week": 7, "month": 30, "year": 365}


def parse_date(s, today):
    s = s.strip().lower()
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d").date()
    except ValueError:
        pass
    if s in ("today", "just now"):
        return today
    if s == "yesterday":
        return today - timedelta(days=1)
    m = re.match(r"(a|an|\d+)\s+(day|week|month|year)s?\s+ago", s)
    if m:
        n = 1 if m.group(1) in ("a", "an") else int(m.group(1))
        return today - timedelta(days=n * UNITS[m.group(2)])
    sys.exit(f"Can't read the date '{s}'. Use YYYY-MM-DD or 'N weeks ago'.")


def stats(b, today):
    ds = sorted((parse_date(d, today) for d in b.get("dates", [])), reverse=True)
    last90 = sum(1 for d in ds if (today - d).days <= 90)
    newest = (today - ds[0]).days if ds else None
    gaps = [(ds[i] - ds[i + 1]).days for i in range(len(ds) - 1)]
    typical_gap = statistics.median(gaps) if gaps else None
    # Burst: half or more of the listed reviews arrived within 14 days of each other.
    burst = False
    if len(ds) >= 6:
        for i in range(len(ds)):
            window = [d for d in ds if 0 <= (ds[i] - d).days <= 14]
            if len(window) >= len(ds) / 2:
                burst = True
                break
    return {"name": b["name"], "you": b.get("you", False), "total": b.get("total"), "rating": b.get("rating"),
            "last90": last90, "per_month": round(last90 / 3, 1), "newest_days": newest, "typical_gap": typical_gap,
            "burst": burst, "sample": len(ds)}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("reviews")
    a = ap.parse_args()
    with open(a.reviews, encoding="utf-8") as fh:
        data = json.load(fh)
    today = datetime.strptime(data["as_of"], "%Y-%m-%d").date() if data.get("as_of") else date.today()
    rows = [stats(b, today) for b in data["businesses"]]
    you = next((r for r in rows if r["you"]), None)
    if not you:
        sys.exit('Mark your business with "you": true')
    comps = [r for r in rows if not r["you"]]

    print("| Business | Total | Rating | Last 90 days | Per month | Newest (days ago) | Typical gap (days) |")
    print("|---|---|---|---|---|---|---|")
    for r in rows:
        name = f"**{r['name']}**" if r["you"] else r["name"]
        print(f"| {name} | {r['total'] or '-'} | {r['rating'] or '-'} | {r['last90']} | {r['per_month']} | {r['newest_days'] if r['newest_days'] is not None else '-'} | {round(r['typical_gap']) if r['typical_gap'] is not None else '-'} |")

    findings = []
    if comps:
        med90 = statistics.median(c["last90"] for c in comps)
        if you["last90"] < med90:
            findings.append(f"Velocity: {you['last90']} new reviews in 90 days against a competitor median of {med90:g}. "
                            f"To match it, aim for about {math.ceil(med90 / 3)} a month.")
        gapped = [c for c in comps if c["typical_gap"] is not None]
        if gapped and you["newest_days"] is not None:
            best = min(gapped, key=lambda c: c["typical_gap"])
            if you["newest_days"] > best["typical_gap"] * 2:
                findings.append(f"Recency: newest review is {you['newest_days']} days old; {best['name']} typically gets one every {round(best['typical_gap'])} days.")
        if any(c["sample"] and c["last90"] == c["sample"] for c in comps):
            findings.append("Note: at least one competitor's sample is entirely from the last 90 days. Add more dates for that competitor to measure its velocity properly.")
    if you["burst"]:
        findings.append("Bursts: half or more of the recent reviews arrived within two weeks, then slowed. A routine (SMS within the hour, one email follow-up) flattens this.")
    if you["sample"] < 10:
        findings.append(f"Only {you['sample']} dates supplied for the business. Results are rough.")

    print("\n**Findings**\n" if findings else "\nNo review velocity findings against these competitors.")
    for f in findings:
        print(f"- {f}")


if __name__ == "__main__":
    main()
