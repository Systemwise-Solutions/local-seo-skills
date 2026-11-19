#!/usr/bin/env python3
"""Put Business Profile edits in a safe order and print the change log, with dates and the text to paste.

Why an order: edits to the name, address and primary category can prompt a fresh review by Google,
and sometimes a request to re-verify. Making them one at a time, with a gap, means that if Google
asks a question or rankings move, you know which edit caused it. Low-risk edits (services,
description, attributes, photos) can go in together.

Input JSON: a list of changes, each
  {"field": "primary_category", "from": "Bicycle store", "to": "Bicycle repair shop",
   "why": "2 of 3 competitors beating you use it", "location": "optional, for multi-location"}
"to" is the exact text to paste. Long text (over 120 characters) is printed as a copy block
under the table.

Fields, by sensitivity:
  high (own day, then --gap days):        name, address, primary_category
  medium (own day, then --gap-medium):    secondary_categories, website, phone, service_area
  low (batched on one day):               services, products, description, hours, special_hours,
                                          attributes, booking_link, opening_date
  ongoing (from the low-risk day on):     photos, posts, qa
  parallel (support requests, day 1):     duplicates, practitioners

Default order: risky truth fixes (name, address) first, then primary and secondary categories,
then services, products, description and the rest, then the website link, then ongoing items.
Set "order": <number> on a change to override.

Usage:
  python change_log.py changes.json --start 2026-11-23
  python change_log.py changes.json --start 2026-11-23 --gap 7 --gap-medium 3
"""
import argparse
import json
import sys
from datetime import date, datetime, timedelta

SENS = {
    "name": "high", "address": "high", "primary_category": "high",
    "secondary_categories": "medium", "website": "medium", "phone": "medium", "service_area": "medium",
    "services": "low", "products": "low", "description": "low", "hours": "low", "special_hours": "low",
    "attributes": "low", "booking_link": "low", "opening_date": "low",
    "photos": "ongoing", "posts": "ongoing", "qa": "ongoing",
    "duplicates": "parallel", "practitioners": "parallel",
}
ORDER = ["duplicates", "practitioners", "name", "address", "primary_category", "secondary_categories", "service_area",
         "services", "products", "description", "hours", "special_hours", "attributes", "booking_link", "opening_date",
         "phone", "website", "photos", "qa", "posts"]
LABEL = {"primary_category": "Primary category", "secondary_categories": "Secondary categories", "qa": "Q&A",
         "booking_link": "Booking link", "special_hours": "Holiday hours", "service_area": "Service area",
         "opening_date": "Opening date"}
WAIT = {
    "high": "Wait {g} days. Check the edit is live on Maps and no verification request has arrived before the next change.",
    "medium": "Wait {g} days and check it is live.",
    "low": "None: these go in together.",
    "ongoing": "Keep going on the schedule below.",
    "parallel": "Runs alongside: it doesn't edit this profile.",
}


def label(f):
    return LABEL.get(f, f.replace("_", " ").capitalize())


def esc(s):
    return str(s or "").replace("|", r"\|")


def cell(s, n, blocks):
    s = str(s or "").strip()
    if len(s) > 120 or "\n" in s:
        blocks.append((n, s))
        return f"See copy block {n}"
    return esc(s) or "-"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("changes")
    ap.add_argument("--start", help="first day of changes, YYYY-MM-DD (default today)")
    ap.add_argument("--gap", type=int, default=7, help="days after a high-sensitivity edit (default 7, a working rule, not a Google one)")
    ap.add_argument("--gap-medium", type=int, default=3, help="days after a medium-sensitivity edit (default 3)")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    with open(a.changes, encoding="utf-8") as fh:
        changes = json.load(fh)
    if not isinstance(changes, list) or not changes:
        sys.exit("changes.json must be a non-empty JSON list")
    for i, c in enumerate(changes):
        if c.get("field") not in SENS:
            sys.exit(f"Change #{i + 1}: field must be one of {', '.join(ORDER)}; got '{c.get('field')}'")
    start = datetime.strptime(a.start, "%Y-%m-%d").date() if a.start else date.today()

    ranked = sorted(enumerate(changes), key=lambda ic: (ic[1].get("order", ORDER.index(ic[1]["field"]) + 100), ic[0]))
    day = start
    blocks = []
    low_day = None
    pending_low = []
    seq = []
    # Build the sequence: parallel on day 1; high/medium one per slot; low batched at the slot where the
    # first low change falls; ongoing from the low-risk day.
    for _, c in ranked:
        s = SENS[c["field"]]
        if s == "parallel":
            seq.append((start, c, s))
        elif s in ("high", "medium"):
            if pending_low:
                for lc in pending_low:
                    seq.append((day, lc, "low"))
                low_day = day
                pending_low = []
                day += timedelta(days=1)
            seq.append((day, c, s))
            day += timedelta(days=a.gap if s == "high" else a.gap_medium)
        elif s == "low":
            pending_low.append(c)
        else:
            if pending_low:
                for lc in pending_low:
                    seq.append((day, lc, "low"))
                low_day = day
                pending_low = []
                day += timedelta(days=1)
            seq.append((low_day or day, c, s))
    for lc in pending_low:
        seq.append((day, lc, "low"))
    seq.sort(key=lambda x: x[0])  # stable: same-day items keep their order

    print("| Step | Date | Field | Change from | Change to (paste this) | Why | Sensitivity | Before the next step |")
    print("|---|---|---|---|---|---|---|---|")
    for i, (d, c, s) in enumerate(seq, 1):
        loc = f" ({c['location']})" if c.get("location") else ""
        g = a.gap if s == "high" else a.gap_medium
        print(f"| {i} | {d.isoformat()} | {label(c['field'])}{loc} | {cell(c.get('from'), f'{i}a', blocks)} | "
              f"{cell(c.get('to'), i, blocks)} | {esc(c.get('why'))} | {s} | {WAIT[s].format(g=g)} |")

    last = max(d for d, _, _ in seq)
    print(f"\nLast edit: {last.isoformat()}. Re-check rankings from the same points six weeks after it: around {(last + timedelta(weeks=6)).isoformat()}.")

    if blocks:
        print("\n## Copy blocks\n")
        for k, text in blocks:
            print(f"**Copy block {k}** ({len(text)} characters)\n")
            print("```")
            print(text)
            print("```\n")

    print("## Log (fill in as you go)\n")
    print("| Step | Made on | Live on Maps on | Google asked anything? | Notes |")
    print("|---|---|---|---|---|")
    for i in range(1, len(seq) + 1):
        print(f"| {i} | | | | |")


if __name__ == "__main__":
    main()
