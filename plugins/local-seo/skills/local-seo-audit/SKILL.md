---
name: local-seo-audit
description: Runs a full local SEO audit the way consultant Mani Bharij does it, for any kind of local business. Works out where the business shows up across its area in Google Maps, the local pack and AI answers, checks the Business Profile, website, reviews, listings and AI recommendations against the businesses actually winning, finds the lowest broken step, and returns a ranked fix list and a 90-day plan. Use when someone asks for a local SEO audit, why they aren't showing in Google Maps or the map pack, why competitors outrank them locally, how to rank in a town or for near me searches, a Google Business Profile review, or whether ChatGPT or Gemini recommends their business. Works for one location, many locations, or an agency auditing a client.
license: MIT
metadata:
  author: Mani Bharij
  homepage: https://localseoconsultant.net/skills/
  version: 0.3.0
---

# Local SEO audit

The audit finds the few things stopping this business getting customers from local search, and puts them in the order to fix them. It does not list everything a tool could find.

Read [references/loop.md](references/loop.md) first: it is how every skill in this pack works (the loop, the lens for reading any business, the brief and log, evidence rules, limits). This file is the audit's job within that loop.

## Done when

- You know where the business stands for its money searches, across the area its customers come from, and who wins where it doesn't.
- You have found the lowest broken rung on the Visibility Ladder, with evidence.
- There is a ranked fix list with the exact actions, and a 90-day plan with re-checks.
- The brief and log are written, so the next run (or another skill) starts from here.

## Orient

Find out, from what you can see before you ask: what the business sells and to whom, where customers come from, how a customer becomes revenue, the searches that bring revenue, one location or many, and who the audit is for. [references/orient.md](references/orient.md) lists what the audit needs and where to find each piece. Ask only for what's still missing, in one message.

Read the business through the lens in loop.md. The lens decides which checks matter most: a business customers visit is measured from its door outwards; one that travels to customers is measured across the area it serves; one with rules on what it can say gets its copy and replies checked against those rules.

Then check which data tools are connected ([references/data-sources.md](references/data-sources.md)) and say in two lines what you can measure and what you'll ask the user to check by hand.

## Measure

Work through the six areas in [references/checks.md](references/checks.md). Each check says what to look at, how to do it at each data level, and what makes it a finding. Start with the areas the reported problem points at; you can stop early in an area once its rung is clearly sound.

The six areas, and the question each answers:

1. **Where you rank**: where in the area does the business show up, and where does it disappear?
2. **Business Profile**: is Google sure what the business is?
3. **Website**: does the page the profile links to deserve to rank?
4. **Reviews**: do they help the business rank and get chosen?
5. **Consistency across the web**: does everything describe the same business?
6. **AI answers**: when someone asks an assistant, is it named?

Compare against the businesses actually winning the money searches in this area, never a generic benchmark, because the bar is set locally.

Record findings as you go:

```json
{"id": "F1", "area": "profile", "rung": "understood", "title": "...", "evidence": "...", "fix": "...", "owner": "you", "impact": 3, "effort": 1, "confidence": "measured"}
```

`rung`: eligible, understood, ranked, chosen or named. `impact` and `effort`: 1 to 3, where impact 1 means polish rather than a broken rung. `confidence`: measured, reported or inferred. Add `"routine": true` for habits that take months to pay off, so they start in month 1.

Scripts (Python 3, standard library; run with `--help` for inputs). Use them rather than doing the maths by hand:
- `scripts/grid.py`: summarise a geo-grid, or run one with the user's DataForSEO key.
- `scripts/review_velocity.py`: review pace and recency against competitors.
- `scripts/nap_check.py`: name, address and phone across listings.
- `scripts/prioritise.py`: findings into a ranked fix list and 90-day plan.

## Diagnose

Use [references/method.md](references/method.md): the Visibility Ladder and Proximity, Prominence, Proof. Place the business on the ladder and find the lowest broken rung. Work above it is wasted while it stays broken, however interesting it looks. If the honest answer is distance (they are simply too far from the searchers), say so and aim the effort where they can win.

Check the "don't prioritise" list in method.md and stop the user spending effort there.

## Act

Save findings as `findings.json` and run `python scripts/prioritise.py findings.json`. It orders real breaks by rung, then impact over effort, and spreads them over three months. Check the order fits this business; if you change it, say why in one line.

Each action must be usable as written: the category to choose, the text to paste, the page to create and what goes on it, the message to send. Where another skill in the pack does the job in depth, name it as the next step (for example `gbp-optimisation` for the profile copy, `local-pages` for the page plan, `review-engine` for the request flow).

## Verify

The plan includes how to tell whether it worked: the same searches re-checked from the same points at 30, 60 and 90 days, calls, clicks and directions from the profile each month, and review pace against the same competitors. Put each re-check in the log with its date.

## Report

[references/report-template.md](references/report-template.md) lists what the report must contain. Lead with the three things to do first. Keep the list to the findings that matter, usually 8 to 20, and aim for 1,000 to 1,800 words for one location.

For agency clients, keep the report white-label and put the next-steps line in your reply to the agency, not in the report.
