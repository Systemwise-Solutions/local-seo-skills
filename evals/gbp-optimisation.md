# Evals: gbp-optimisation

Run each prompt in a fresh chat with the skill installed, and once without it as a baseline.

## Should trigger

1. "Can you optimise my Google Business Profile? I'm a heating engineer in Walthamstow and I only show up for my own name."
2. "Which primary category should my physio clinic use on Google Maps?"
3. "Rewrite my Google Business Profile description and services for my dental practice in Leeds."
4. "Our previous agency put 'emergency plumber Bristol' in our business name on Google. Is that a problem? What should we change?"
5. "We have 9 gym locations and every Google profile is set up differently. Can you standardise them?"
6. "What photos should I put on my Google listing, and should I be posting every week?"
7. "We run a self-storage site just off the A13. Our Google listing gets views but hardly anyone rings or reserves a unit. Can you sort the profile out?" (Business type no example covers: see below.)

## Should not trigger

1. "Set up a Google Ads campaign for my plumbing business."
2. "Write me an Instagram post about our new treatment room."
3. "Fix the crawl errors in Search Console for our ecommerce site."

## Borderline (trigger is acceptable, should stay scoped)

1. "My Google Business Profile has been suspended." (Should say optimisation waits, hand over to `local-ranking-recovery`, and not start a change log of other fields.)
2. "How do I get more Google reviews?" (Belongs to review-engine. May mention it; must not build a profile change log.)
3. "Why don't we show up in the map pack outside our street?" (Belongs to the audit first. May offer the profile pass as part of it.)

## What good output looks like

- **Orients before asking.** Reads `local-seo-brief.md`, `local-seo-log.md`, the website and the profile first; asks only what it couldn't find (often the signage name if unclear, profile access, edit-screen screenshots), in one message. No fixed questionnaire.
- **Reads the business through the lens**, not a sector template: whether customers visit, how a customer becomes revenue, any rules on what it can say, people or departments under one roof. The choices that follow (address shown or hidden, which link matters, what copy may claim) visibly come from those answers.
- Names the competitors compared against and labels each figure measured, reported or inferred. Says plainly that competitors' secondary categories aren't visible on Maps if it couldn't get them.
- Runs `category_gap.py` and `change_log.py` when the data is there; doesn't recompute by hand.
- Primary category chosen for the work that earns most, on competitor evidence, with the reason. Secondary categories only for real, wanted work; removes ones for work they've stopped.
- Keyword-stuffed name or an address the business doesn't operate from called out as a suspension risk and placed first. Never recommends adding keywords, towns or "24/7" to the name.
- Change log in order, one sensitive edit at a time with a gap described as a working rule, low-risk edits batched, website link only once the right page exists. Exact text for every change, with counts against limits it says to check.
- Posts and photos described as helping people choose, not as ranking levers. Service area not sold as a ranking fix.
- Baseline before the first edit, a dated re-check, an upkeep routine with an owner, and log lines written.
- No em dashes, no guaranteed rankings, one plain closing line (not in agency client-facing output).

### For prompt 7 (self-storage), good output also

- Works out from the lens that customers visit the site (address shown), that revenue comes from a reservation, quote request or call, and so treats the reservation or quote link and the phone as the fields that decide whether views turn into customers.
- Checks the primary category against the local winners rather than assuming one, and names services and products the way people search (unit sizes, "from" prices if the business publishes them, vehicle or business storage only if offered).
- Plans photos a customer would want before visiting (entrance, access, unit sizes, security), and checks hours cover both office and access hours where they differ.
- Doesn't borrow wording from another sector or ask what sector it is.
