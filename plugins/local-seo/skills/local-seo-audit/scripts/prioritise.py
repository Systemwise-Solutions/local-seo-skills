#!/usr/bin/env python3
"""Turn audit findings into a ranked fix list and a 90-day plan.

Order: real breaks (impact 2 or 3) before polish (impact 1). Within each, the
Visibility Ladder rung first (eligible before understood before ranked before
chosen before named), then impact over effort, then confidence.
The lowest broken rung goes first because work on higher rungs is wasted while
it stays broken. A minor inconsistency is polish, not a broken rung.

Months: each fix goes in the earliest month with effort budget left, so quick
fixes never get stranded behind big ones. Findings marked "routine": true (a
habit to start, such as review requests) always start in month 1.

Input: a JSON list of findings, each with
  id, area, rung, title, evidence, fix, owner, impact (1-3), effort (1-3), confidence,
  and optionally routine (true/false)
Output: Markdown to stdout (or JSON with --json).

Usage:
  python prioritise.py findings.json
  python prioritise.py findings.json --json
"""
import argparse
import json
import sys

RUNGS = ["eligible", "understood", "ranked", "chosen", "named"]
CONFIDENCE = {"measured": 0, "reported": 1, "inferred": 2}
EFFORT_WORD = {1: "low", 2: "medium", 3: "high"}
# Month capacity: how many fixes a small team can realistically land per month.
# Effort points per month; a high-effort fix uses 3.
MONTH_BUDGET = 6


def validate(f, i):
    missing = [k for k in ("title", "rung", "fix", "impact", "effort") if k not in f]
    if missing:
        sys.exit(f"Finding #{i + 1} is missing: {', '.join(missing)}")
    if f["rung"] not in RUNGS:
        sys.exit(f"Finding '{f['title']}': rung must be one of {RUNGS}, got '{f['rung']}'")
    for k in ("impact", "effort"):
        if f[k] not in (1, 2, 3):
            sys.exit(f"Finding '{f['title']}': {k} must be 1, 2 or 3")


def score(f):
    return (
        0 if f["impact"] >= 2 else 1,
        RUNGS.index(f["rung"]),
        -(f["impact"] / f["effort"]),
        -f["impact"],
        CONFIDENCE.get(f.get("confidence", "inferred"), 2),
    )


def plan(findings):
    ordered = sorted(findings, key=score)
    breaks = [f for f in ordered if f["impact"] >= 2] or ordered
    lowest = min((f["rung"] for f in breaks), key=RUNGS.index) if breaks else None
    months, used = {1: [], 2: [], 3: []}, {1: 0, 2: 0, 3: 0}
    for f in ordered:
        if f.get("routine"):
            m = 1
        else:
            m = next((k for k in (1, 2, 3) if used[k] + f["effort"] <= MONTH_BUDGET), 3)
        months[m].append(f)
        used[m] += f["effort"]
    return ordered, lowest, months


def to_markdown(ordered, lowest, months):
    out = []
    if not ordered:
        return "No findings."
    out.append(f"Lowest broken rung: **{lowest}**\n")
    out.append("## Do these three first")
    for i, f in enumerate(ordered[:3], 1):
        out.append(f"{i}. **{f['title']}** Fix: {f['fix']} Owner: {f.get('owner', 'you')}. Effort: {EFFORT_WORD[f['effort']]}.")
    for m in (1, 2, 3):
        if not months[m]:
            continue
        out.append(f"\n### Month {m}")
        for f in months[m]:
            out.append(f"- **{f['title']}** ({f['rung']}, impact {f['impact']}, effort {EFFORT_WORD[f['effort']]}, {f.get('confidence', 'inferred')})")
            if f.get("evidence"):
                out.append(f"  - Evidence: {f['evidence']}")
            out.append(f"  - Fix: {f['fix']} Owner: {f.get('owner', 'you')}.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("findings", help="findings.json")
    ap.add_argument("--json", action="store_true", help="output JSON instead of Markdown")
    a = ap.parse_args()
    with open(a.findings, encoding="utf-8") as fh:
        findings = json.load(fh)
    if not isinstance(findings, list):
        sys.exit("findings.json must be a JSON list")
    for i, f in enumerate(findings):
        validate(f, i)
    ordered, lowest, months = plan(findings)
    if a.json:
        print(json.dumps({"lowest_rung": lowest, "order": [f.get("id", f["title"]) for f in ordered],
                          "months": {m: [f.get("id", f["title"]) for f in fs] for m, fs in months.items()}}, indent=2))
    else:
        print(to_markdown(ordered, lowest, months))


if __name__ == "__main__":
    main()
