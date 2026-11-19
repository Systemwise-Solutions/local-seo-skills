# Evals: gbp-optimisation

Run each prompt in a fresh chat with the skill installed, and once without it as a baseline.

## Should trigger

1. "Can you optimise my Google Business Profile? I'm a heating engineer in Walthamstow and I only show up for my own name."
2. "Which primary category should my physio clinic use on Google Maps?"
3. "Rewrite my Google Business Profile description and services for my dental practice in Leeds."
4. "Our previous agency put 'emergency plumber Bristol' in our business name on Google. Is that a problem? What should we change?"
5. "We have 9 gym locations and every Google profile is set up differently. Can you standardise them?"
6. "What photos should I put on my Google listing, and should I be posting every week?"

## Should not trigger

1. "Set up a Google Ads campaign for my plumbing business."
2. "Write me an Instagram post about our new treatment room."
3. "Fix the crawl errors in Search Console for our ecommerce site."

## Borderline (trigger is acceptable, should stay scoped)

1. "My Google Business Profile has been suspended." (Should say optimisation waits, explain the fix-the-cause-then-appeal order in short, and not start a change log of other fields.)
2. "How do I get more Google reviews?" (Belongs to review-engine. May mention it; must not build a profile change log.)
3. "Why don't we show up in the map pack outside our street?" (Belongs to the audit first. May offer the profile pass as part of it.)

## What good output looks like

- Asks only the missing intake questions in one message, including the signage name and whether customers visit. Reuses `local-seo-brief.md` if present.
- Names the three competitors it compared against and labels each figure measured, reported or inferred. Says plainly that competitors' secondary categories aren't visible on Maps if it couldn't get them.
- Runs `category_gap.py` and `change_log.py` when the data is there; doesn't recompute by hand.
- Primary category chosen for the job that pays most, on competitor evidence. Secondary categories only for real work; removes ones for work they've stopped.
- Keyword-stuffed name or virtual office called out as a suspension risk and placed first in the log. Never recommends adding keywords, towns or "24/7" to the name, or an address they don't trade from.
- Change log in order, one sensitive edit at a time with a logged date, low-risk edits batched, website link only once the right page exists. Exact text to paste for every change, within the character limits.
- Website link follows the rule: one dominant service links to that page; multi-location links to each location page.
- Posts written for customers and described as not a ranking lever. Service area settings not sold as a ranking fix.
- Photo plan, four posts, baseline and six-week re-check, upkeep routine.
- No em dashes, no guaranteed rankings, one plain closing line (not in agency client-facing output).
