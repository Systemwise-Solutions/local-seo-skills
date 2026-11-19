#!/usr/bin/env python3
"""Compare name, address and phone (NAP) across listings against the Business Profile.

Input JSON:
  {
    "reference": {"source": "Google Business Profile", "name": "...", "address": "...", "phone": "..."},
    "listings": [
      {"source": "Yell", "url": "https://...", "name": "...", "address": "...", "phone": "..."},
      ...
    ]
  }

Normalises case, punctuation, common address abbreviations and UK/US phone formats
before comparing, so "St." and "Street" or "+44 20 7946 0000" and "020 7946 0000" match.

Usage:
  python nap_check.py listings.json
"""
import argparse
import json
import re

ABBR = {
    "st": "street", "rd": "road", "ave": "avenue", "av": "avenue", "ln": "lane", "dr": "drive", "ct": "court",
    "pl": "place", "sq": "square", "blvd": "boulevard", "hwy": "highway", "pk": "park", "cres": "crescent",
    "ste": "suite", "fl": "floor", "n": "north", "s": "south", "e": "east", "w": "west", "&": "and",
}
NAME_NOISE = {"ltd", "limited", "llc", "inc", "plc", "the", "co", "company"}


def norm_text(s, abbr=False, drop=()):
    s = (s or "").lower().replace("&", " and ")
    s = re.sub(r"[^\w\s]", " ", s)
    words = [ABBR.get(w, w) if abbr else w for w in s.split()]
    return " ".join(w for w in words if w not in drop)


def norm_phone(p):
    d = re.sub(r"\D", "", p or "")
    if d.startswith("44"):
        d = "0" + d[2:]
    elif d.startswith("1") and len(d) == 11:
        d = d[1:]
    return d


def postcode(addr):
    m = re.search(r"\b([A-Z]{1,2}\d[A-Z\d]?)\s*(\d[A-Z]{2})\b", (addr or "").upper())
    if m:
        return f"{m.group(1)} {m.group(2)}"
    m = re.search(r"\b\d{5}(?:-\d{4})?\b", addr or "")
    return m.group(0) if m else None


def compare(ref, l):
    issues = []
    if l.get("name") and norm_text(l["name"], drop=NAME_NOISE) != norm_text(ref["name"], drop=NAME_NOISE):
        issues.append(f"name '{l['name']}'")
    if l.get("address"):
        rp, lp = postcode(ref["address"]), postcode(l["address"])
        first = lambda a: norm_text(a.split(",")[0], abbr=True)
        if rp and lp and rp != lp:
            issues.append(f"address '{l['address']}' (postcode {lp}, should be {rp})")
        elif rp and lp and first(l["address"]) == first(ref["address"]):
            pass  # same postcode and same first line: town or county wording doesn't matter
        elif norm_text(l["address"], abbr=True) != norm_text(ref["address"], abbr=True):
            issues.append(f"address '{l['address']}'")
    if l.get("phone") and norm_phone(l["phone"]) != norm_phone(ref["phone"]):
        issues.append(f"phone '{l['phone']}'")
    missing = [k for k in ("name", "address", "phone") if not l.get(k)]
    return issues, missing


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("listings")
    a = ap.parse_args()
    with open(a.listings, encoding="utf-8") as fh:
        data = json.load(fh)
    ref = data["reference"]
    bad, ok, notes = [], [], []
    for l in data["listings"]:
        issues, missing = compare(ref, l)
        label = l.get("source", "?") + (f" ({l['url']})" if l.get("url") else "")
        if issues:
            bad.append(f"- **{label}**: " + "; ".join(issues))
        else:
            ok.append(l.get("source", "?"))
        if missing:
            notes.append(f"- {l.get('source', '?')}: no {', '.join(missing)} recorded")
    print(f"Reference: {ref['name']} | {ref['address']} | {ref['phone']}")
    print("(Company suffixes such as Ltd and Limited are ignored when comparing names.)\n")
    print(f"**{len(bad)} of {len(data['listings'])} listings don't match**\n" if bad else "All listings match.\n")
    print("\n".join(bad))
    if ok:
        print(f"\nMatching: {', '.join(ok)}")
    if notes:
        print("\nIncomplete records (check by hand):")
        print("\n".join(notes))


if __name__ == "__main__":
    main()
