# Local ranking recovery: Calder Heating & Plumbing (fictional)

19 November 2026 · 1 location · Data: SearchOps grid scans every two weeks since May, Business Profile performance and Search Console (measured), plus the dates of your changes (reported)

## The short version
Calls from your Business Profile fell from about 33 a week to 19 from the week of 17 August, and in the same fortnight you fell out of the map pack for "emergency plumber" across most of your area, while your website's search traffic didn't move. Five days earlier the primary category was changed from "Plumber" to "Heating contractor", and the searches that fell are the plumbing ones while "boiler repair" went up: I'm confident (high) that the category change caused it. Putting "Plumber" back as the primary category should bring the plumbing searches back, at the cost of some of the boiler repair gain, which a services list and the boiler page can protect.

## What dropped

| Series | Before | After | From | Shape |
|---|---|---|---|---|
| Profile calls, per week | 33 | 19 (-42%) | week of 17 Aug | cliff |
| Profile website clicks, per week | 51 | 34 (-33%) | week of 17 Aug | cliff |
| Maps top-3 coverage, "emergency plumber" | 62% of points | 24% | scan of 24 Aug | cliff |
| Average grid rank, "plumber" | 2.5 | 8.0 | scan of 24 Aug | cliff |
| Maps top-3 coverage, "boiler repair" | 29% of points | 39% (up) | scan of 24 Aug | cliff |

All measured (SearchOps), run through `change_points.py`. The previous scan, on 10 August, was still normal.

What didn't drop: Search Console non-branded clicks held at about 118 a week (-2% over the same weeks). That rules out the website and points at the profile.

## What changed around then

- **12 August**, confirmed: primary category changed from "Plumber" to "Heating contractor", with "Plumber" moved to secondary. Made by the office manager.
- 28 July, confirmed: a boiler servicing page added to the site. Organic didn't move, and a new page doesn't lower plumbing rankings.
- 26 August, seen in the grid results: Kirkstall Plumbing Co appeared about 0.6 miles away. This is nine days after your calls had already dropped, so it isn't the trigger, but it now holds some of the points you lost.
- "A Google update in September", not confirmed. The drop started in mid-August, before it, so it isn't the cause whatever its date.

## Most likely cause
**The primary category change on 12 August.** Confidence: high.
- Evidence: the drop is a cliff that shows in the first week after the edit, on the profile and Maps only. The plumbing searches fell and "boiler repair" rose on the same scan, which is exactly what moving the primary category from plumbing to heating does. The competitors now holding "emergency plumber" at your lost points use "Plumber" as their primary (names from the grid's top 3 at those points, categories checked on their Maps profiles).
- What would rule it out: plumbing coverage staying down for several scans after the category is restored.
- Other causes considered: the boiler page (organic held, wrong direction); Kirkstall Plumbing Co (arrived after the drop; affects the north-west side only); a Google update (unconfirmed, and later than the drop).

## What to do, in order
1. **Put "Plumber" back as your primary category.** Your money is in plumbing: calls overall fell 42% when you swapped, so the boiler gain didn't make up for it. Steps: in your Business Profile, edit the business category, set "Plumber" as the primary and keep "Heating contractor" as an additional category. Change nothing else on the profile the same day. Owner: you. Effort: low.
2. **Protect boiler repair with services, not the category.** Add "Boiler repair" and "Boiler servicing" to your profile services, each with a line saying you cover Headingley, Kirkstall, Meanwood and Horsforth. Do this a week after step 1, so each change can be read on its own. Owner: you. Effort: low.
3. **Keep the boiler page, and link to it.** The page added in July is fine. Link to it from the homepage and from the plumbing pages so it stays found for boiler searches. Owner: your web person. Effort: low.
4. **Agree who edits the profile.** One person owns it, keeps a short change log (date, what, why), and doesn't change the name, address or category without a reason. This drop came from a well-meant edit nobody else knew about. Owner: you. Effort: low.
5. **Watch Kirkstall Plumbing Co.** Once you're back, compare its categories, services and reviews with yours for the north-west side. Don't act yet; let step 1 settle first. Owner: you. Effort: low.

## Don't do these now
- **Don't make other profile edits for a fortnight after step 1.** Any change to the category can prompt Google to re-check the profile; that's normal, but piling edits on top makes the result impossible to read.
- **Don't chase the "September update".** Nothing in your data points at it.

## Not checked
- Whether "Boiler repair" coverage falls back after the change. The next two scans will show it.
- Last year's August, to rule out seasonality. Your data starts in May. The cliff shape and the boiler rise make seasonality very unlikely.

## How to confirm recovery
- Baseline: about 33 calls and 51 website clicks a week; "emergency plumber" top 3 at 62% of points.
- Re-check the same SearchOps grids (same keywords, same points) at each fortnightly scan, and profile calls weekly, for 8 weeks after the change.
- Add the category fix to `recovery.json` as a `profile_edit` event with its date and re-run `change_points.py`. A recovery shows as a rise in calls and "emergency plumber" coverage starting after that date.
- Recovered means: "emergency plumber" top-3 coverage back above 50% and calls back near 30 a week. The drop showed within a week; a recovery can take longer, and no timeframe is guaranteed.

If plumbing coverage hasn't moved by the second scan after the fix, the next hypothesis is Kirkstall Plumbing Co on the north-west side: compare its categories, services and reviews with yours there.

## Log lines added
```
2026-11-19 | Drop found: profile calls -42% and Maps "emergency plumber" top-3 62% to 24% from w/c 17 Aug; organic held | Cause: primary category changed Plumber to Heating contractor on 12 Aug (high) | Re-check: n/a
2026-11-19 | Fix: primary category back to Plumber, Heating contractor kept as additional | Re-check: each fortnightly scan to 2027-01-14; target top 3 above 50%, calls near 30/week
2026-11-26 | Planned: add Boiler repair and Boiler servicing to profile services (one week after the category fix) | Re-check: boiler repair coverage at next two scans
```

## Next steps
If you'd rather have it done with you: localseoconsultant.net/consulting/local-seo-audit/
