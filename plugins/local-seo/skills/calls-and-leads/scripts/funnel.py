#!/usr/bin/env python3
"""Compare a local business's enquiry funnel across two periods and show where the drop is.

The funnel: people see the Business Profile (views), act on it (calls, website clicks,
directions, bookings or orders through the profile), the website turns visits into the
action this business makes money from (forms, bookings, orders, reservations), enquiries
get answered, and enquiries become revenue (booked jobs, kept appointments, paid orders).
Counts move with the season and with rankings. Rates show which stage changed. This
script works out both and names the stage that fell most.

Input JSON (two periods; the first is the baseline):
  {
    "business": "Example Business (fictional)",
    "funnel": { ... optional, see "Fitting the funnel to the business" ... },
    "periods": [
      {"label": "Aug-Oct 2025", "months": 3,
       "views": 9800, "calls": 310, "website_clicks": 420, "directions": 60,
       "form_fills": 95, "bookings": 120,
       "calls_answered": 290, "calls_missed": 20,      # optional, from the phone system or call tracking
       "source": "Business Profile performance screenshots (reported)"},
      {"label": "Aug-Oct 2026", "months": 3, ...}
    ]
  }
"before" and "after" keys work instead of "periods". Any field can be null when unknown.
Counts are totals for the period; "months" (default 1) turns them into a monthly average,
so periods of different length compare fairly. Compare the same months a year apart when
the business is seasonal.

Fitting the funnel to the business (all optional; the defaults suit a business that
lives on calls and forms):
  "funnel": {
    "actions":     ["calls", "website_clicks", "directions"],  # profile actions, summed for the action rate
    "site":        ["form_fills"],       # what the website turns clicks into; each gets a rate per website click
    "enquiries":   ["calls", "form_fills"],  # what counts as an enquiry, the base for the outcome rate
    "outcome":     "bookings",           # the revenue event: bookings, orders, sales, covers, jobs_won ...
    "labels":      {"online_orders": "Online orders"},  # display names for any field
    "answer_rate_floor": 0.85            # flag an answer rate below this whatever the trend
  }
Any field name works as long as the periods use it. Examples:
  Takes orders online:  "site": ["online_orders"], "enquiries": ["calls", "online_orders"], "outcome": "paid_orders"
  Takes reservations:   "site": ["reservations"], "enquiries": ["calls", "reservations"], "outcome": "covers_seated"
  Walk-in business:     "actions": ["calls", "website_clicks", "directions"], "site": [], "enquiries": ["directions"],
                        "outcome": "walk_ins"  (walk-ins counted at the door or till; read the rate as a trend)

What each rate means:
  profile action rate   sum of actions / views
  call rate             calls / views (if calls are an action)
  website click rate    website clicks / views
  <site> rate           each site field / website clicks ("form rate" for form_fills)
  answer rate           calls answered / (answered + missed)
  <outcome> rate        outcome / sum of enquiries ("booking rate" for bookings)

Thresholds: a rate falling by 15% or more of its old value counts as a drop, views falling
20% or more points at visibility or season, and an answer rate under 85% is flagged. These
are Mani Bharij's working rules of thumb from client work, not published benchmarks; change
them with --drop, --views-drop and answer_rate_floor.

Usage:
  python funnel.py funnel.json
  python funnel.py funnel.json --json
  python funnel.py funnel.json --drop 0.10 --views-drop 0.25
"""
import argparse
import json
import sys

DEFAULTS = {"actions": ["calls", "website_clicks", "directions"], "site": ["form_fills"],
            "enquiries": ["calls", "form_fills"], "outcome": "bookings", "answer_rate_floor": 0.85}
LABELS = {"views": "Profile views", "calls": "Calls from profile", "website_clicks": "Website clicks",
          "directions": "Direction requests", "form_fills": "Form fills", "bookings": "Bookings",
          "calls_answered": "Calls answered", "calls_missed": "Calls missed"}
RATE_NAMES = {"form_fills": "form rate", "bookings": "booking rate"}
NOISY = 30  # under this many in a month, treat changes as rough


def div(a, b):
    if a is None or b in (None, 0):
        return None
    return a / b


def add(*xs):
    return None if not xs or any(x is None for x in xs) else sum(xs)


def label(k, labels):
    return labels.get(k) or LABELS.get(k) or k.replace("_", " ").capitalize()


def rate_name(k, labels):
    return RATE_NAMES.get(k) or f"{label(k, labels).lower()} rate"


def pct(x):
    return "-" if x is None else f"{100 * x:.1f}%"


def change(a, b):
    if a in (None, 0) or b is None:
        return None
    return (b - a) / a


def fmt_change(c):
    return "-" if c is None else f"{'+' if c >= 0 else ''}{100 * c:.0f}%"


def build(cfg):
    """Return the ordered count fields, and the rate definitions as (name, stage, look, numerator, denominator fields, unit)."""
    acts, site, enq, out, labels = cfg["actions"], cfg["site"], cfg["enquiries"], cfg["outcome"], cfg["labels"]
    counts = []
    for k in ["views", *acts, *site, *enq, out, "calls_answered", "calls_missed"]:
        if k and k not in counts:
            counts.append(k)
    rates = [("profile action rate", None, None, ("+", acts), ("views",), None)]
    if "calls" in acts:
        rates.append(("call rate", "Profile converts (calls)",
                      "the profile: hours, phone number, photos, reviews, prices, booking or order link", ("calls",), ("views",), "calls"))
    if "website_clicks" in acts:
        rates.append(("website click rate", "Profile converts (website)",
                      "the profile: website link, booking or order link, what the profile promises", ("website_clicks",), ("views",), "website clicks"))
    for k in site:
        rates.append((rate_name(k, labels), "Website converts",
                      "the landing page on a phone: the main action above the fold, whether a test one actually goes through and arrives, speed",
                      (k,), ("website_clicks",), label(k, labels).lower()))
    rates.append(("answer rate", "Calls get answered", "who answers, when people call against opening hours, voicemail and call-back",
                  ("calls_answered",), ("+", ["calls_answered", "calls_missed"]), "answered calls"))
    rates.append((rate_name(out, labels), f"Enquiries become {label(out, labels).lower()}",
                  "speed of reply, quoting or confirming, no-shows, lead quality (are they the customers you want?)",
                  (out,), ("+", enq), label(out, labels).lower()))
    return counts, rates


def value(p, spec):
    if spec and spec[0] == "+":
        return add(*(p.get(k) for k in spec[1]))
    return p.get(spec[0])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("funnel", help="funnel.json")
    ap.add_argument("--json", action="store_true", help="output JSON instead of Markdown")
    ap.add_argument("--drop", type=float, default=0.15, help="a rate falling by this share of its old value counts as a drop (default 0.15)")
    ap.add_argument("--views-drop", type=float, default=0.20, help="views falling by this share point at visibility or season (default 0.20)")
    a = ap.parse_args()
    with open(a.funnel, encoding="utf-8") as fh:
        data = json.load(fh)
    periods = data.get("periods") or [p for p in (data.get("before"), data.get("after")) if p]
    if len(periods) != 2:
        sys.exit("Give exactly two periods (\"periods\": [before, after], or \"before\" and \"after\").")
    cfg = {**DEFAULTS, "labels": {}, **(data.get("funnel") or {})}
    counts, rate_defs = build(cfg)
    labels = cfg["labels"]

    A, B = periods
    la, lb = A.get("label", "Before"), B.get("label", "After")
    mon = lambda p: {k: (p[k] / (p.get("months") or 1) if p.get(k) is not None else None) for k in counts}
    ma, mb = mon(A), mon(B)
    rat = lambda p: {name: div(value(p, num), value(p, den)) for name, _, _, num, den, _ in rate_defs}
    ra, rb = rat(A), rat(B)

    findings, warnings = [], []
    vc = change(ma["views"], mb["views"])
    if vc is not None and vc <= -a.views_drop:
        findings.append({"stage": "Seen", "change": vc,
                         "text": f"Profile views fell {abs(100 * vc):.0f}% a month. Fewer people are seeing the profile: check rankings "
                                 "(run local-seo-audit) and whether the season explains it (compare the same months last year)."})
    for name, stage, look, num, den, unit in rate_defs:
        if not stage:
            continue
        c = change(ra[name], rb[name])
        if c is None or c > -a.drop:
            continue
        base = value(mb, den)
        lost = (ra[name] - rb[name]) * base if base is not None else None
        text = f"{stage}: {name} fell from {pct(ra[name])} to {pct(rb[name])} ({fmt_change(c)}). Look at {look}."
        if lost and lost >= 1:
            text += f" At the old rate you'd have about {lost:.0f} more {unit} a month (inferred)."
        findings.append({"stage": stage, "change": c, "text": text})

    floor = cfg.get("answer_rate_floor")
    if floor and rb["answer rate"] is not None and rb["answer rate"] < floor and not any(f["stage"] == "Calls get answered" for f in findings):
        findings.append({"stage": "Calls get answered", "change": 0,
                         "text": f"Calls get answered: {pct(rb['answer rate'])} of calls answered in {lb}, under the {pct(floor)} working floor. "
                                 "A missed call from search usually goes to the next business; fix this whatever the trend."})

    out, enq = cfg["outcome"], cfg["enquiries"]
    for p, m, lab in ((A, ma, la), (B, mb, lb)):
        small = [label(k, labels) for k in [*enq, out] if m.get(k) is not None and m[k] < NOISY]
        small = list(dict.fromkeys(small))
        if small:
            warnings.append(f"{lab}: under {NOISY} a month for {', '.join(small).lower()}. Treat changes there as rough.")
        total = add(*(p.get(k) for k in enq))
        if p.get(out) is not None and total and p[out] > total:
            warnings.append(f"{lab}: more {label(out, labels).lower()} ({p[out]}) than enquiries counted ({total}). They probably include other sources "
                            "(repeat customers, referrals, walk-ins, direct calls to the main number). The outcome rate is not meaningful until they're split.")
        if p.get("calls") is not None and p.get("calls_answered") is not None and add(p["calls_answered"], p.get("calls_missed") or 0) < p["calls"]:
            warnings.append(f"{lab}: the phone system shows fewer calls than the profile. Profile calls count taps on the call button, not connected calls.")
    core = [k for k in counts if k not in ("calls_answered", "calls_missed")]
    missing = [label(k, labels) for k in core if A.get(k) is None or B.get(k) is None]
    if missing:
        warnings.append("Not known for both periods: " + ", ".join(missing).lower() + ". Those stages can't be compared.")

    biggest = min((f for f in findings if f["change"] < 0), key=lambda f: f["change"], default=None)

    if a.json:
        print(json.dumps({"monthly": {la: ma, lb: mb}, "rates": {la: ra, lb: rb}, "findings": findings,
                          "biggest_drop": biggest["stage"] if biggest else None, "warnings": warnings}, indent=2))
        return

    print(f"**{data.get('business', 'Funnel')}**: {la} against {lb}, monthly averages\n")
    print(f"| | {la} | {lb} | Change |")
    print("|---|---|---|---|")
    f = lambda v: "-" if v is None else f"{v:,.0f}"
    for k in counts:
        if ma[k] is None and mb[k] is None:
            continue
        print(f"| {label(k, labels)} | {f(ma[k])} | {f(mb[k])} | {fmt_change(change(ma[k], mb[k]))} |")
    print(f"\n| Rate | {la} | {lb} | Change |")
    print("|---|---|---|---|")
    for k in ra:
        if ra[k] is None and rb[k] is None:
            continue
        print(f"| {k[0].upper() + k[1:]} | {pct(ra[k])} | {pct(rb[k])} | {fmt_change(change(ra[k], rb[k]))} |")

    print()
    threshold = f"{100 * a.drop:.0f}%"
    if biggest:
        print(f"**Biggest drop: {biggest['stage']}**\n")
    elif findings:
        print(f"**No stage fell by {threshold} or more, but see below.**\n")
    else:
        print(f"**No stage fell by {threshold} or more.** If enquiries still feel low, the leak may predate the baseline, or sit outside this funnel "
              "(for example calls to the main number, walk-ins nobody counts, or lead quality).\n")
    for fd in sorted(findings, key=lambda fd: fd["change"]):
        print(f"- {fd['text']}")
    if warnings:
        print("\n**Read with care**\n")
        for w in warnings:
            print(f"- {w}")


if __name__ == "__main__":
    main()
