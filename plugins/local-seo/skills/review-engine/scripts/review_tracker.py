#!/usr/bin/env python3
"""Monthly review tracking: how many arrived, how fast they were answered, and what they say.

Input JSON:
  {
    "as_of": "2026-11-19",                         # optional, defaults to today
    "services": ["physiotherapy", "sports massage", "back pain"],   # words customers use for the services
    "places": ["Didsbury", "Withington", "Chorlton"],              # the town and nearby areas
    "requests": {"2026-10": 48, "2026-11": 31},    # optional: review requests sent per month
    "reviews": [
      {"date": "2026-11-12", "rating": 5, "text": "...", "reply_date": "2026-11-13", "reply_text": "..."},
      {"date": "3 weeks ago", "rating": 2, "text": "...", "reply_date": null}
    ]
  }
Relative dates ("3 weeks ago") are accepted. Leave reply_date null when there is no reply.

Output: a month-by-month table, unanswered reviews (lowest rating first), and findings.
With --regulated (clinics, healthcare, legal), also checks reply text for wording that
confirms the reviewer was a patient or client, or mentions their care.

Usage:
  python review_tracker.py reviews-log.json
  python review_tracker.py reviews-log.json --months 6 --regulated
"""
import argparse
import json
import re
import statistics
import sys
from datetime import date, datetime, timedelta

UNITS = {"day": 1, "week": 7, "month": 30, "year": 365}

# Phrases in a reply that confirm someone was a patient or client, or discuss their care.
CONFIRMS = [
    r"your (treatment|appointment|visit|session|consultation|procedure|operation|surgery|scan|assessment|course|therapy|recovery|condition|injury|diagnosis|results?|care|case|matter|claim)",
    r"(as|being) (a|our) (patient|client)", r"when (you|we) (saw|treated|visited|came in)", r"(seeing|treating) you",
    r"(glad|pleased|happy) (we|the team) (could )?(help(ed)?|fix(ed)?|treat(ed)?) (you|your)",
    r"\byour (knee|back|neck|shoulder|hip|ankle|skin|teeth|tooth|acne|scar|mole)\b",
    r"\b(our records|your records|your notes|your file)\b",
]


def parse_date(s, today):
    if s is None:
        return None
    s = str(s).strip().lower()
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


def mentions(text, words):
    t = (text or "").lower()
    return any(re.search(r"(?<!\w)" + re.escape(w.lower()), t) for w in words)


def month_key(d):
    return f"{d.year}-{d.month:02d}"


def months_back(today, n):
    y, m = today.year, today.month
    out = []
    for _ in range(n):
        out.append(f"{y}-{m:02d}")
        m -= 1
        if m == 0:
            y, m = y - 1, 12
    return list(reversed(out))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("log")
    ap.add_argument("--months", type=int, default=6, help="months to show (default 6)")
    ap.add_argument("--regulated", action="store_true", help="check replies for wording that confirms a patient or client")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    with open(a.log, encoding="utf-8") as fh:
        data = json.load(fh)
    today = datetime.strptime(data["as_of"], "%Y-%m-%d").date() if data.get("as_of") else date.today()
    services, places = data.get("services", []), data.get("places", [])
    requests = data.get("requests", {})
    reviews = []
    for r in data.get("reviews", []):
        d = parse_date(r.get("date"), today)
        rd = parse_date(r.get("reply_date"), today) if r.get("reply_date") else None
        reviews.append({**r, "_d": d, "_rd": rd})
    if not reviews:
        sys.exit("No reviews in the file.")

    keys = months_back(today, a.months)
    print("| Month | New reviews | Avg rating | Requests sent | Reviews per 100 requests | Replied | Median days to reply | Mention a service | Mention a place |")
    print("|---|---|---|---|---|---|---|---|---|")
    rows = {}
    for k in keys:
        rs = [r for r in reviews if month_key(r["_d"]) == k]
        n = len(rs)
        replied = [r for r in rs if r["_rd"]]
        days = [(r["_rd"] - r["_d"]).days for r in replied]
        req = requests.get(k)
        row = {
            "n": n,
            "avg": round(statistics.mean(r["rating"] for r in rs), 1) if rs and all("rating" in r for r in rs) else None,
            "req": req,
            "conv": round(100 * n / req) if req else None,
            "replied": f"{len(replied)} of {n}" if n else "-",
            "reply_rate": len(replied) / n if n else None,
            "med": statistics.median(days) if days else None,
            "svc": round(100 * sum(mentions(r.get("text"), services) for r in rs) / n) if n and services else None,
            "plc": round(100 * sum(mentions(r.get("text"), places) for r in rs) / n) if n and places else None,
        }
        rows[k] = row
        f = lambda v, suf="": "-" if v is None else f"{v:g}{suf}"
        print(f"| {k} | {n} | {f(row['avg'])} | {f(row['req'])} | {f(row['conv'])} | {row['replied']} | {f(row['med'])} | {f(row['svc'], '%')} | {f(row['plc'], '%')} |")
    if keys[-1] == month_key(today):
        print(f"\n{keys[-1]} is the current month, to {today.isoformat()}.")

    # ------------------------------------------------------------ unanswered
    open_ = sorted((r for r in reviews if not r["_rd"]), key=lambda r: (r.get("rating", 5), r["_d"]))
    print("\n**Unanswered**\n")
    if open_:
        for r in open_:
            snippet = (r.get("text") or "(no text)").strip().replace("\n", " ")
            snippet = snippet[:90] + ("..." if len(snippet) > 90 else "")
            stars = r.get("rating", "?")
            print(f"- {stars} star{'' if stars == 1 else 's'}, {(today - r['_d']).days} days old: \"{snippet}\"")
    else:
        print("None.")

    # ------------------------------------------------------------ findings
    findings = []
    recent = [rows[k] for k in keys[-3:]]
    empty = [k for k in keys if rows[k]["n"] == 0 and k != month_key(today)]
    if empty:
        findings.append(f"No new reviews in {', '.join(empty)}. Check the request step that month: were requests sent, and within the hour?")
    counts = [rows[k]["n"] for k in keys if k != month_key(today)]
    if len(counts) >= 3 and max(counts) >= 3 * max(1, statistics.median(counts)):
        findings.append(f"Uneven flow: the best month had {max(counts)} reviews against a median of {statistics.median(counts):g}. A routine flattens bursts.")
    convs = [r["conv"] for r in recent if r["conv"] is not None]
    if convs:
        findings.append(f"Reviews per 100 requests over the last {len(convs)} month(s) with request counts: {', '.join(str(c) for c in convs)}. "
                        "If this falls while requests hold steady, look at timing (was it within the hour?) and the link (does it open the review form?).")
    elif not requests:
        findings.append("No request counts supplied. Count requests sent each month (your SMS or booking tool shows it) so you can see which step fails.")
    total = [r for r in reviews if r["_d"] >= today - timedelta(days=90)]
    if total:
        rate = sum(1 for r in total if r["_rd"]) / len(total)
        if rate < 1:
            findings.append(f"Replies: {round(100 * rate)}% of reviews from the last 90 days have a reply. Aim for all of them.")
        days = [(r["_rd"] - r["_d"]).days for r in total if r["_rd"]]
        if days and statistics.median(days) > 2:
            findings.append(f"Reply speed: median {statistics.median(days):g} days. Aim for within 2 working days; negative reviews the same day.")
        if services:
            s = round(100 * sum(mentions(r.get("text"), services) for r in total) / len(total))
            if s < 50:
                findings.append(f"Only {s}% of reviews in the last 90 days mention a service. Add the prompt to mention what was done, without scripting the words.")
        if places:
            p = round(100 * sum(mentions(r.get("text"), places) for r in total) / len(total))
            if p < 25:
                findings.append(f"Only {p}% mention a place. The request can ask which area they're in, or say 'it helps people nearby find us'.")
    low_open = [r for r in open_ if r.get("rating", 5) <= 3]
    if low_open:
        findings.append(f"{len(low_open)} review(s) rated 3 or below have no reply. Answer those first: the next customer reads how you handle problems.")

    if a.regulated:
        risky = []
        pats = CONFIRMS + ([r"\byour (" + "|".join(re.escape(w.lower()) for w in services) + r")"] if services else [])
        for r in reviews:
            t = (r.get("reply_text") or "").lower()
            hits = [m.group(0) for p in pats for m in [re.search(p, t)] if m]
            if hits:
                risky.append((r, hits))
        if risky:
            findings.append(f"{len(risky)} repl{'y' if len(risky) == 1 else 'ies'} may confirm the reviewer was a patient or client, or mention their care. Edit them:")
            for r, hits in risky:
                findings.append(f"  - Review of {r['_d'].isoformat()}: reply says \"{hits[0]}\"")
        else:
            findings.append("Regulated check: no reply wording found that confirms a patient or client. Still read them: this check catches common phrases, not all.")

    print("\n**Findings**\n" if findings else "\nNo findings.")
    for f_ in findings:
        print(f_ if f_.startswith("  -") else f"- {f_}")


if __name__ == "__main__":
    main()
