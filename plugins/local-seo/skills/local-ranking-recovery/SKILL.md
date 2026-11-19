---
name: local-ranking-recovery
description: Diagnoses a sudden local search drop the way consultant Mani Bharij does it, for any kind of local business, then lays out the fix and how to confirm recovery. Pins down exactly what dropped (which searches, Maps, local pack, organic or AI Mode, which locations, from when), builds a dated timeline, and tests each likely cause against it: Business Profile edits, suspensions, verification requests, duplicate merges, website changes, confirmed Google updates, review changes, competitor moves and filtering. Handles suspended profiles, from finding the cause to the reinstatement request. Use when someone says they lost their map pack or local rankings, calls or bookings dropped, the phone stopped ringing, their Google Business Profile disappeared or got suspended, they vanished from Google Maps, or traffic fell after a website change, redesign or migration.
license: MIT
metadata:
  author: Mani Bharij
  homepage: https://localseoconsultant.net/skills/
  version: 0.3.0
---

# Local ranking recovery

A business that has dropped is a business where something changed, and the change is nearly always findable. The advantage here is that a before and an after both exist. Guessing throws that away, so this skill pins down what dropped and when before it says why.

Read [references/loop.md](references/loop.md) first: it is how every skill in this pack works (the loop, the lens for reading any business, the brief and log, evidence rules, limits). This file is recovery's job within that loop.

Recovery is the loop in its plainest form. Each likely cause is a hypothesis. Test it against the timeline, act on the most likely one, re-measure, and if the numbers don't come back, move to the next hypothesis. Never act on several at once: if everything changes together, nobody can tell what worked.

## Done when

- You know exactly what dropped (searches, surface, locations, date, cliff or slope), what didn't, and the baseline it dropped from.
- Every plausible cause has been tested against the timeline, and the most likely one is stated with its evidence, a confidence, and what would rule it out.
- The fix for that cause is written out in order, ready to use, with one sensitive change at a time.
- There are dated re-checks and a plain definition of "recovered" in this business's own numbers.
- The brief, `local-seo-log.md` and `recovery.json` are written, so the next pass starts from here.

On a later pass, done means the series is back near its baseline; or every cause the business controls has been tested and what remains (an update, a competitor who is simply closer) is explained honestly; or the problem has been handed over by name.

## Orient

Find out, from what you can see before you ask: the business and its profile, the drop in the user's words, which locations, roughly when, and what changed around then. Changes are often already recorded: `local-seo-log.md`, the repo's git history for website changes, the profile's own notices, emails the user can forward. [references/orient.md](references/orient.md) lists what recovery needs, where to look for each piece, and why it matters. Ask only for what's still missing, in one message.

If the profile is suspended, say so in your first reply and tell the user not to create a new profile or keep editing the old one while you work. Both make reinstatement harder, and the damage is done before the diagnosis is.

Read the business through the lens in loop.md, because the shape of the business decides which causes are plausible and which numbers count:
- **Comes to them or goes to them**: an address or pin change matters most when customers visit; a hidden-address mismatch matters most when they don't.
- **Travel distance**: sets the area to re-measure. A shrinking radius means something different for a business people walk to than for one that drives an hour.
- **How a customer becomes revenue**: the series that matters is the one that carries money (calls, bookings, direction requests, orders), not whichever is easiest to export.
- **Rules on what it can say**: shapes the suspension evidence (registrations, licences) and any review replies.
- **One location or many, or several under one roof**: decides whether to look for a shared cause or a local one, and whether filtering is likely.

Then check which data tools are connected ([references/data-sources.md](references/data-sources.md)) and say in two lines what history you can get and what you'll ask the user for. Recovery needs dated series from before and after the drop; if only today's checks are possible, say how rough the read will be.

## Measure

**What exactly dropped, before any view on why.** Pin down:

- **Which searches.** Money searches, the business name, or both. Gone for the name too points at eligibility (suspension, duplicate, merge), because relevance problems don't hide a business from its own name.
- **Which surface.** Maps, the local pack, organic, AI Mode. Different surfaces have different inputs, so what fell and what held narrows the cause.
- **Which locations.** All at once points at something shared (the website, a brand-wide edit, an update); one points at that place.
- **When, and what shape.** A cliff on one date points at an edit, a suspension, a launch or a filter. A slope over weeks points at a competitor, review decay, an update or season.
- **Real or measurement.** Rule out a broken tracking number, a disconnected profile, an Analytics change or reporting lag first. It is the cheapest cause to find, and a profile that stops reporting is not a profile with zero calls.

**The timeline.** One dated list of everything that changed from about 90 days before the drop to today, built with [references/timeline.md](references/timeline.md). Collect first, judge later: the event that looks irrelevant is often the one that matters. Mark every date confirmed or remembered.

Never supply a Google update date from memory. Check Google's own Search Status Dashboard or announcements with web search, or record the event with `"confirmed": false`. A wrong date sends the whole diagnosis the wrong way, and many local changes are never announced at all.

**Line the drop up.** Put the series and events in `recovery.json` (shape in the script's `--help`) and run:

```bash
python scripts/change_points.py recovery.json
```

It finds the biggest step changes in each series, calls each a cliff or a slope, lists the events before and after, and says whether local and organic moved together. Use it rather than eyeballing a chart, because the timing has to come out the same every time it's re-run. It finds timing, not cause: an event in the window is a lead to test.

## Diagnose

Turn the leads into hypotheses and test each against its signature in [references/causes.md](references/causes.md): what it drops, on which surface, in what shape, what it leaves alone, and the one independent check that confirms or rules it out. What didn't drop is often the most telling evidence.

Split the problem first, because it decides who fixes it:
- **Local only** (profile, Maps and local pack fell; organic held): the profile, filtering, reviews and competitors. Stay in this skill.
- **Local and organic together, or organic only**: start with the website. Whole-site technical recovery belongs to SEO for AI Agents: if that pack is installed, hand over to its `rescue` job (`seo-access-migrations` for redirects and URL changes, `seo-access-reach` for crawling and indexing). If not, give the short version in causes.md and point to github.com/manibharij/seo-for-ai-agents. Still fix the local fallout here: the profile's website link and the pages it relies on.

Rank the hypotheses and state the most likely with a confidence:
- **High**: timing matches, the mechanism fits what dropped and what didn't, and an independent check confirms it.
- **Medium**: timing and mechanism fit; nothing independent confirms it yet.
- **Low**: timing only, or several causes fit equally.

Say what would raise the confidence and what would rule the cause out, and keep the rest of the list: it is the order for the next pass if this one doesn't recover. Where two causes overlap, fix the one the business controls first, because it is the only one whose effect can be read.

## Act

Fix the cause, not the symptoms, and keep the fix inside what keeps a profile live (loop.md, section 5). In practice:

- **One sensitive change at a time** (name, address, category, website link), because each can prompt a fresh review by Google and because a recovery you can't attribute teaches nothing.
- **Fix it everywhere it lives**: the profile, the website and the main listings, because Google judges the business by what it can see across all of them.
- **No unrelated improvements during a recovery.** They muddy the read on what worked. Park them for the audit.
- **Never copy what a competitor is getting away with.** A competitor's keyword-stuffed name is answered with Google's redressal process and better proof on the business's own profile, because copying it is the fastest route to a suspension.

Each action is usable as written: the exact setting, the text to paste, the URL to redirect, the person to remove. If you can make the change yourself (a redirect or a page in the repo, a draft in a connected tool), offer to; change nothing live without a yes.

**Suspended profile.** Follow [references/suspension.md](references/suspension.md): find the likely cause, fix it everywhere, gather evidence of the real business, then file the reinstatement request through Google's own help page. The order matters because a request filed before the cause is fixed is usually wasted, and a rejection leaves a record. Link Google's help page; never hard-code a form URL, because Google changes the process. If the honest answer is that the address isn't one the business works from, say so: that won't be reinstated, and the fix is a real address or a service-area profile.

## Verify

Re-measure exactly as you measured: the same searches, the same grid points, the same series, on dates set now. Add the fix to `recovery.json` as an event and re-run the script; a real recovery shows as a rise that starts after the fix date, not before it.

Write down, in this business's own numbers, what "recovered" means (for example, top-3 coverage for the main money search back above most of its old level, and the revenue series back near baseline) and when you'll look. Reinstatement and re-ranking times vary and nobody outside Google controls them, so give re-check dates, never a promise.

At each re-check, read the result as a test of the hypothesis:
- **Recovered**: record it and stop.
- **Partly recovered**: suspect a second, overlapping cause. Take the next hypothesis on the list.
- **Not moved after a fair wait**: the hypothesis was wrong or the fix didn't land everywhere. Check the fix is live and consistent, then go back to Diagnose with that cause marked as tested.

## Report and record

[references/report-template.md](references/report-template.md) lists what the report must contain. Lead with what dropped and the most likely cause in three sentences, then the actions in order. Report multi-location drops branch by branch, because a network average hides the branches that fell; group the fixes by cause.

Add lines to `local-seo-log.md` for the drop, the cause found, each fix with its date, and each re-check date. Keep `recovery.json` as the baseline: the next pass, or another skill, starts from it.

For agency clients, keep the report white-label and put the next-steps line in your reply to the agency, not in the report.
