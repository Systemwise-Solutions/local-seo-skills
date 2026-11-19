# Evals: local-ranking-recovery

Run each prompt in a fresh chat with the skill installed, and once without it as a baseline. Where a prompt needs data, use the fictional inputs in `examples/local-ranking-recovery/`.

## Should trigger

1. "We've lost our map pack rankings for 'emergency plumber' since August. What happened?"
2. "Our Google Business Profile got suspended yesterday. How do we get it back?"
3. "Calls from Google have halved in the last month and nobody can tell me why."
4. "We launched a new website three weeks ago and our local traffic fell off a cliff."
5. "Three of our 14 branches disappeared from Google Maps last week. The rest are fine."
6. "Our listing doesn't even show up when people search our business name any more."

## Should not trigger

1. "Run a local SEO audit for my new bakery." (local-seo-audit)
2. "How do I get more Google reviews?"
3. "Plan the redirects for our website migration next month." (no drop yet: SEO for AI Agents `migrate`, or a migration skill)
4. "Write a Google Business Profile description for my salon."

## Borderline (trigger is acceptable, must stay on the drop)

1. "We never ranked well in Maps. How do we start?" (no drop: should suggest the audit, not build a timeline)
2. "Our organic traffic dropped after the core update. We're a SaaS company." (not local: hand to SEO for AI Agents `rescue`, don't run the local method)
3. "A competitor has 'Best Plumber Leeds' as their business name and outranks us." (competitor cause: redressal process with evidence and better proof; never suggest copying it)

## New business type: storefront with walk-in revenue

Prompt: "I run an independent café on a high street. Since about mid-October we're not coming up in Google Maps when people search 'coffee near me' or 'brunch' round here, and the Saturday queue has gone. Nothing's changed on our end." (The examples don't cover a business whose revenue is walk-ins.)

Good output:
- Orients from the lens rather than a sector template: customers come to the business on foot or nearby, so the area to measure is small (streets, not miles), and the revenue series is direction requests and website clicks, not calls.
- Doesn't accept "nothing changed" at face value: checks the profile's notices for edits Google made itself or edits suggested by the public that went live (a moved pin, changed hours, a changed category), and asks who has access.
- Treats each candidate (a moved pin or address, hours now showing closed, a new café nearby, filtering by a neighbour in the same category, a measurement gap) as a hypothesis with its signature, and checks the strongest first: for a pin move, the centre of strength moving off the door.
- Acts on one cause, says how to re-check from the same few points and on what dates, and names the next hypothesis if the numbers haven't moved.
- No invented update date; any "Google update" is checked or marked unconfirmed.

## What good output looks like

- Orients from what it can find first (brief, `local-seo-log.md`, the repo's git history for website changes, the profile's notices, connected tools) and asks only for what's missing, in one message. No fixed questionnaire.
- Pins down what dropped (searches, surface, locations, date, cliff or slope) before saying why. Asks for the date and what changed if it doesn't have them.
- Checks the drop is real (tracking, a disconnected profile, gaps reported as zero) before diagnosing rankings.
- Builds a dated timeline and marks each date confirmed or not. Never supplies a Google update date from memory; checks it or marks it unconfirmed.
- Runs `change_points.py` when there are dated series, and treats its events as leads, not proof.
- Separates local-only drops from site-wide ones, and hands site-wide technical causes to SEO for AI Agents (`rescue`, `seo-access-migrations`, `seo-access-reach`) in one line, with the short version if that pack isn't installed.
- States one most likely cause with evidence, a confidence (high, medium, low), what would rule it out, and the other causes considered.
- Fixes in order, one sensitive edit at a time, and says how to confirm recovery against a baseline, with no guaranteed timeframe.
- Treats the cause as a hypothesis: sets re-check dates and a definition of "recovered" in the business's own numbers, and says which cause it tests next if the numbers don't come back (partial recovery points at an overlapping cause).
- Writes the brief, `recovery.json` and log lines to `local-seo-log.md`.
- Suspensions: tells the user straight away not to create a new profile or keep editing; finds and fixes the cause before the appeal; lists the evidence; links Google's own help page rather than a hard-coded form URL; writes the explanation ready to paste; says plainly when an address can't be reinstated.
- Category-change example: identifies the 12 August category edit as the cause with high confidence, notes the boiler repair rise as supporting evidence, dismisses the unconfirmed September update and the later competitor.
- Suspension example: names the keyword-stuffed name as the likely cause, the hours edit as the probable trigger, and the 12 September duplicate as something to remove before appealing.
- No em dashes, no keyword-stuffed names, virtual offices, new duplicate profiles or review bursts recommended. Agency runs are white-label. One plain next-steps line at the end, matched to the cause: the suspension page for a suspension, the migration page after a website change, otherwise the audit.
