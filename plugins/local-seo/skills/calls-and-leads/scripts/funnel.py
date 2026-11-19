#!/usr/bin/env python3
"""Compare a local business's enquiry funnel across two periods and show where the drop is.

The funnel: people see the Business Profile (views), act on it (calls, website clicks,
directions), the website turns visits into form fills and bookings, calls get answered,
and enquiries become booked jobs. Counts move with the season and with rankings. Rates
show which stage changed. This script works out both and names the stage that fell most.

Input JSON (two periods; the first is the baseline):
  {
    "business": "Example Roofing (fictional)",
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

What each rate means:
  profile action rate   (calls + website clicks + directions) / views
  call rate             calls / views
  website click rate    website clicks / views
  form rate             form fills / website clicks (read as a trend if form fills are site-wide)
  answer rate           calls answered / (answered + missed)
  booking rate          bookings / (calls + form fills)

Usage:
  python funnel.py funnel.json
  python funnel.py funnel.json --json
"""
import argparse
import json
import sys

COUNTS = ["views", "calls", "website_clicks", "directions", "form_fills", "bookings", "calls_answered", "calls_missed"]
LABELS = {"views": "Profile views", "calls": "Calls from profile", "website_clicks": "Website clicks",
          "directions": "Direction requests", "form_fills": "Form fills", "bookings": "Bookings",
          "calls_answered": "Calls answered", "calls_missed": "Calls missed"}
DROP = 0.15       # a rate falling by 15% or more of its old value counts as a drop
VIEWS_DROP = 0.20  # views falling 20% or more points at visibility or season
NOISY = 30        # under this many in a month, treat changes as rough


def div(a, b):
    if a is None or b in (None, 0):
        return None
    return a / b


def add(*xs):
    return None if any(x is None for x in xs) else sum(xs)


def monthly(p):
    m = p.get("months") or 1
    return {k: (p[k] / m if p.get(k) is not None else None) for k in COUNTS}


def rates(p):
    actions = add(p.get("calls"), p.get("website_clicks"), p.get("directions"))
    answered, missed = p.get("calls_answered"), p.get("calls_missed")
    return {
        "profile action rate": div(actions, p.get("views")),
        "call rate": div(p.get("calls"), p.get("views")),
        "website click rate": div(p.get("website_clicks"), p.get("views")),
        "form rate": div(p.get("form_fills"), p.get("website_clicks")),
        "answer rate": div(answered, add(answered, missed)),
        "booking rate": div(p.get("bookings"), add(p.get("calls"), p.get("form_fills"))),
    }


# Which stage each rate belongs to, what to look at, and which base count it multiplies.
STAGES = [
    ("call rate", "Profile converts (calls)", "the profile: hours, phone number, photos, reviews, prices, booking link", "views", "calls"),
    ("website click rate", "Profile converts (website)", "the profile: website link, booking link, what the profile promises", "views", "website clicks"),
    ("form rate", "Website converts", "the landing page on a phone: call and book above the fold, the form actually sending, speed", "website_clicks", "form fills"),
    ("answer rate", "Calls get answered", "who answers, when people call against opening hours, voicemail and call-back", None, "answered calls"),
    ("booking rate", "Enquiries become bookings", "speed of reply, quoting, lead quality (are they the jobs you want?)", None, "bookings"),
]


def pct(x):
    return "-" if x is None else f"{100 * x:.1f}%"


def change(a, b):
    if a in (None, 0) or b is None:
        return None
    return (b - a) / a


def fmt_change(c):
    return "-" if c is None else f"{'+' if c >= 0 else ''}{100 * c:.0f}%"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("funnel", help="funnel.json")
    ap.add_argument("--json", action="store_true", help="output JSON instead of Markdown")
    a = ap.parse_args()
    with open(a.funnel, encoding="utf-8") as fh:
        data = json.load(fh)
    periods = data.get("periods") or [p for p in (data.get("before"), data.get("after")) if p]
    if len(periods) != 2:
        sys.exit("Give exactly two periods (\"periods\": [before, after], or \"before\" and \"after\").")
    A, B = periods
    la, lb = A.get("label", "Before"), B.get("label", "After")
    ma, mb = monthly(A), monthly(B)
    ra, rb = rates(A), rates(B)

    findings, warnings = [], []
    vc = change(ma["views"], mb["views"])
    if vc is not None and vc <= -VIEWS_DROP:
        findings.append({"stage": "Seen", "change": vc,
                         "text": f"Profile views fell {abs(100 * vc):.0f}% a month. Fewer people are seeing the profile: check rankings "
                                 "(run local-seo-audit) and whether the season explains it (compare the same months last year)."})
    for key, stage, look, base, unit in STAGES:
        c = change(ra[key], rb[key])
        if c is None or c > -DROP:
            continue
        lost = None
        if base and mb.get(base) is not None:
            lost = (ra[key] - rb[key]) * mb[base]
        elif key == "answer rate" and None not in (mb["calls_answered"], mb["calls_missed"]):
            lost = (ra[key] - rb[key]) * (mb["calls_answered"] + mb["calls_missed"])
        elif key == "booking rate" and None not in (mb["calls"], mb["form_fills"]):
            lost = (ra[key] - rb[key]) * (mb["calls"] + mb["form_fills"])
        text = f"{stage}: {key} fell from {pct(ra[key])} to {pct(rb[key])} ({fmt_change(c)}). Look at {look}."
        if lost and lost >= 1:
            text += f" At the old rate you'd have about {lost:.0f} more {unit} a month (inferred)."
        findings.append({"stage": stage, "change": c, "text": text})

    # Absolute answer rate matters even without a drop
    if rb["answer rate"] is not None and rb["answer rate"] < 0.85 and not any(f["stage"] == "Calls get answered" for f in findings):
        findings.append({"stage": "Calls get answered", "change": 0,
                         "text": f"Calls get answered: {pct(rb['answer rate'])} of calls answered in {lb}. Every missed call from search is usually a lost job; fix this whatever the trend."})

    for p, m, label in ((A, ma, la), (B, mb, lb)):
        small = [LABELS[k] for k in ("calls", "form_fills", "bookings") if m.get(k) is not None and m[k] < NOISY]
        if small:
            warnings.append(f"{label}: under {NOISY} a month for {', '.join(small).lower()}. Treat changes there as rough.")
        enq = add(p.get("calls"), p.get("form_fills"))
        if p.get("bookings") is not None and enq and p["bookings"] > enq:
            warnings.append(f"{label}: more bookings ({p['bookings']}) than calls plus form fills ({enq}). Bookings probably include other sources "
                            "(repeat customers, referrals, direct calls to the main number). Booking rate is not meaningful until they're split.")
        if p.get("calls") is not None and p.get("calls_answered") is not None and add(p["calls_answered"], p.get("calls_missed") or 0) < p["calls"]:
            warnings.append(f"{label}: the phone system shows fewer calls than the profile. Profile calls count taps on the call button, not connected calls.")
    missing = [LABELS[k] for k in COUNTS[:6] if A.get(k) is None or B.get(k) is None]
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
    for k in COUNTS:
        if ma[k] is None and mb[k] is None:
            continue
        f = lambda v: "-" if v is None else f"{v:,.0f}"
        print(f"| {LABELS[k]} | {f(ma[k])} | {f(mb[k])} | {fmt_change(change(ma[k], mb[k]))} |")
    print(f"\n| Rate | {la} | {lb} | Change |")
    print("|---|---|---|---|")
    for k in ra:
        if ra[k] is None and rb[k] is None:
            continue
        print(f"| {k[0].upper() + k[1:]} | {pct(ra[k])} | {pct(rb[k])} | {fmt_change(change(ra[k], rb[k]))} |")

    print()
    if biggest:
        print(f"**Biggest drop: {biggest['stage']}**\n")
    elif findings:
        print("**No stage fell by 15% or more, but see below.**\n")
    else:
        print("**No stage fell by 15% or more.** If enquiries still feel low, the leak may predate the baseline, or sit outside this funnel "
              "(for example calls to the main number, or lead quality).\n")
    for f in sorted(findings, key=lambda f: f["change"]):
        print(f"- {f['text']}")
    if warnings:
        print("\n**Read with care**\n")
        for w in warnings:
            print(f"- {w}")


if __name__ == "__main__":
    main()
