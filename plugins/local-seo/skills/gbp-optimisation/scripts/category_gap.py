#!/usr/bin/env python3
"""Compare a Business Profile's categories, services and name against the competitors beating it.

Input JSON:
  {
    "money_searches": ["boiler installation", "boiler repair"],
    "business": {
      "name": "Example Heating Co | Boiler Repair Walthamstow",   # as it shows on the profile
      "signage_name": "Example Heating Co",                      # optional: name on signage, van, registration
      "areas": ["Walthamstow", "Leyton"],                        # optional: towns it serves, for the name check
      "primary": "Plumber",
      "secondary": ["Gas engineer"],
      "services": ["Boiler repair", "Leak detection"],
      "offers": ["boiler installation", "bathroom fitting"]       # optional: what it really does, to sanity-check gaps
    },
    "competitors": [
      {"name": "Competitor A", "primary": "Heating contractor", "secondary": ["Plumber"],
       "services": ["Boiler installation", "Boiler servicing"]},
      ...
    ]
  }
Competitor services are optional (they are not always visible). Use the top 3 businesses for the
money searches, from where the customers are, not national brands.

Output: Markdown with the category table, the primary category call, secondary and service gaps,
money searches no service covers, and a business name check.

Usage:
  python category_gap.py compare.json
"""
import argparse
import json
import re
import sys
from collections import Counter

STOP = {"and", "the", "of", "for", "in", "a", "an", "to", "with", "near", "me", "my", "your"}
NAME_FLAGS = {"24/7", "24hr", "24 hour", "emergency", "near me", "best", "cheap", "cheapest", "local", "no 1", "number 1",
              "top rated", "affordable", "specialist", "specialists", "experts", "expert"}


def stem(w):
    for suf in ("ing", "es", "s"):
        if len(w) > 4 and w.endswith(suf):
            w = w[: -len(suf)]
            break
    if len(w) > 4 and w.endswith("e"):
        w = w[:-1]
    return w


def tokens(s):
    s = (s or "").lower().replace("&", " and ")
    s = re.sub(r"[^\w\s/]", " ", s)
    return {stem(w) for w in s.split() if w not in STOP}


def key(s):
    return " ".join(sorted(tokens(s)))


def covers(service, search):
    """A service covers a search when every meaningful word of the search is in the service name."""
    st = tokens(search)
    return bool(st) and st <= tokens(service)


def offered(cat, offers):
    if offers is None:
        return None
    ct = tokens(cat)
    return any(ct <= tokens(o) or len(ct & tokens(o)) > len(ct) / 2 for o in offers)


def name_check(b, comps):
    name = b.get("name", "")
    signage = b.get("signage_name")
    out = []
    low = name.lower()
    flagged = sorted(f for f in NAME_FLAGS if re.search(r"(?<!\w)" + re.escape(f) + r"(?!\w)", low))
    words = set()
    if signage:
        extra = tokens(name) - tokens(signage)
        if extra:
            words = extra
            out.append(f"Profile name '{name}' has words that aren't in the signage name '{signage}': "
                       f"{', '.join(sorted(extra))}. Change the profile name to '{signage}'. Keywords in the name are one of "
                       "the most common reasons profiles get suspended; categories, services and the landing page carry the same relevance without the risk.")
        elif name.strip().lower() != signage.strip().lower():
            out.append(f"Profile name '{name}' differs from signage '{signage}' only in wording or punctuation. Match it exactly.")
    vocab = set()
    for c in [b] + comps:
        for f in ("primary",):
            vocab |= tokens(c.get(f))
        for f in ("secondary", "services"):
            for x in c.get(f, []) or []:
                vocab |= tokens(x)
    vocab |= {stem(a.lower()) for a in b.get("areas", []) or []}
    hits = sorted((tokens(name) & vocab) - (tokens(signage) if signage else set()))
    if not signage and (hits or flagged):
        out.append(f"Profile name '{name}' contains service, place or sales words ({', '.join(hits + flagged)}). "
                   "Check it against the signage and registered name; if they aren't on the signage, remove them.")
    elif signage and flagged and not words:
        out.append(f"Name contains {', '.join(flagged)}. Fine only if that is genuinely part of the signed, registered name.")
    loud = ("emergency", "24/7", "24 hour", "near me", "best ", "cheap", " | ", " - ")
    stuffed = [c["name"] for c in comps if c.get("name") and any(f in c["name"].lower() for f in loud)]
    if stuffed:
        out.append(f"Competitors that look keyword-stuffed: {', '.join(stuffed)}. Don't copy them. If they are beating you, "
                   "report them through Google's Business Redressal Complaint Form with screenshots of their signage or registered name.")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("compare")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    with open(a.compare, encoding="utf-8") as fh:
        data = json.load(fh)
    b = data.get("business")
    comps = data.get("competitors", [])
    if not b or not b.get("primary"):
        sys.exit("Need business.primary")
    if not comps:
        sys.exit("Need at least one competitor")
    offers = b.get("offers")
    n = len(comps)

    # ------------------------------------------------------------ categories
    labels = {}
    prim, sec = Counter(), Counter()
    for c in comps:
        if c.get("primary"):
            k = key(c["primary"]); labels.setdefault(k, c["primary"]); prim[k] += 1
        for s in c.get("secondary", []) or []:
            k = key(s); labels.setdefault(k, s); sec[k] += 1
    yp = key(b["primary"]); labels.setdefault(yp, b["primary"])
    ys = {key(s) for s in b.get("secondary", []) or []}
    for s in b.get("secondary", []) or []:
        labels.setdefault(key(s), s)

    allk = sorted(set(prim) | set(sec) | {yp} | ys, key=lambda k: (-(prim[k] * 2 + sec[k]), labels[k]))
    print(f"# Category and service gaps: {b.get('signage_name') or b.get('name', 'the business')}\n")
    print(f"Compared with {n} competitor{'s' if n != 1 else ''}: {', '.join(c.get('name', '?') for c in comps)}\n")
    print("| Category | You | Competitors' primary | Competitors' secondary |")
    print("|---|---|---|---|")
    for k in allk:
        you = "primary" if k == yp else ("secondary" if k in ys else "-")
        print(f"| {labels[k]} | {you} | {prim[k]} of {n} | {sec[k]} of {n} |")

    print("\n## Primary category\n")
    top, cnt = prim.most_common(1)[0] if prim else (None, 0)
    tied = [k for k, v in prim.items() if v == cnt]
    if yp == top and len(tied) == 1:
        print(f"Your primary, {labels[yp]}, matches {cnt} of {n} competitors. Keep it.")
    elif cnt > n / 2 and yp != top:
        print(f"{cnt} of {n} competitors use **{labels[top]}** as primary; you use {labels[yp]}. "
              f"Switch to {labels[top]} if it describes the job that pays most, and keep {labels[yp]} as a secondary if you still do that work.")
    else:
        print(f"Competitors split ({', '.join(f'{labels[k]} {v}' for k, v in prim.most_common())}); you use {labels[yp]}. "
              "No majority, so choose the category that matches the money search that pays most, and check who ranks for that search specifically.")

    print("\n## Secondary categories to consider\n")
    gaps = [k for k in allk if k != yp and k not in ys and (prim[k] + sec[k]) >= max(2, (n + 1) // 2)]
    if gaps:
        for k in gaps:
            o = offered(labels[k], offers)
            note = "" if o is None else (" Matches something you offer." if o else " Nothing in your offers list matches: add only if you really do this.")
            if k == top and cnt > n / 2:
                note += " (Recommended as primary above; if you switch, it doesn't need adding again.)"
            print(f"- **{labels[k]}**: used by {prim[k] + sec[k]} of {n}.{note}")
    else:
        print("None used by most competitors that you lack.")
    extras = [k for k in ys if prim[k] + sec[k] == 0]
    if extras:
        print("\nYour secondaries no competitor uses (keep only if it's real work you want; each extra dilutes the primary a little): "
              + ", ".join(labels[k] for k in sorted(extras)))

    # ------------------------------------------------------------ services
    print("\n## Services\n")
    ysv = b.get("services", []) or []
    # Group competitor services: "New boiler installation" counts towards "Boiler installation".
    allsv = sorted({(key(x), x) for c in comps for x in (c.get("services") or [])}, key=lambda kx: (len(tokens(kx[1])), kx[1]))
    groups = []  # (key, label, token set)
    for k, x in allsv:
        if not any(t <= tokens(x) for _, _, t in groups):
            groups.append((k, x, tokens(x)))
    csv_counts, csv_labels = Counter(), {}
    for gk, gl, gt in groups:
        csv_labels[gk] = gl
        csv_counts[gk] = sum(1 for c in comps if any(gt <= tokens(x) for x in (c.get("services") or [])))
    ykeys = {key(s) for s in ysv}
    missing = [(k, v) for k, v in sorted(csv_counts.items(), key=lambda kv: (-kv[1], csv_labels[kv[0]]))
               if k not in ykeys and not any(covers(y, csv_labels[k]) for y in ysv)]
    if not csv_counts:
        print("No competitor services supplied, so only the money-search check below applies.")
    elif missing:
        print("Competitor services you don't list:")
        for k, v in missing:
            o = offered(csv_labels[k], offers)
            note = "" if o is None else ("" if o else " (not in your offers list)")
            print(f"- {csv_labels[k]}: {v} of {n}{note}")
    else:
        print("You list every service the competitors list.")

    searches = data.get("money_searches", [])
    uncovered = [s for s in searches if not any(covers(y, s) for y in ysv)]
    if searches:
        print("\nMoney searches with no service named for them:" if uncovered else "\nEvery money search has a service named for it.")
        for s in uncovered:
            print(f"- \"{s}\": add a service called something close to \"{s[:1].upper() + s[1:]}\", in the words customers type.")

    # ------------------------------------------------------------ name
    nc = name_check(b, comps)
    print("\n## Business name\n")
    print("\n".join(f"- {x}" for x in nc) if nc else "No keyword, place or sales words found in the name.")
    print("\nCategory names vary by country and change: confirm each one exists in the profile's own category picker before planning the edit.")


if __name__ == "__main__":
    main()
