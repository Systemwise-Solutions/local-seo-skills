# Orient: what recovery needs, and where to find it

Find each piece yourself first. Ask the user only for what you can't find, in one message, and say why you need it. Someone whose calls have stopped wants a diagnosis, not a form, so every question has to earn its place.

| Recovery needs | Look here first | Why it matters |
|---|---|---|
| The business and its profile | The brief, the website, the Maps listing, a connected tool | Everything is measured against this listing. Note the exact name as it shows on Maps and the name on the signage: a gap between them is a cause in itself. |
| The drop, in the user's words | The conversation | "Calls stopped" and "we're gone for our own name" point at different causes. Keep their words in the brief. |
| Which locations | The brief, location pages, a connected tool's location list | All at once points at something shared; one points at that place. |
| Roughly when, and how fast | The user, the profile's performance screen, a connected tool's history | A date turns guessing into a test. "Overnight" and "over a couple of months" rule out different things. |
| What changed around then | `local-seo-log.md`; the repo's git history (`git log --since` around the drop) for website changes; deploy or CMS logs; the profile's notices and Google's emails; who has access to the profile | Most recoveries are solved by the timeline. Dates from a log, a commit or an email are confirmed; remembered dates are leads. |
| The searches that bring revenue | The brief, Search Console queries, the profile's search terms, the site's main service pages | The drop is measured on these, not the business name, because the name rarely tells you what lost money. |
| The shape of the business | The brief, the site, the profile (address shown or hidden) | The lens in loop.md: it decides which causes are plausible and which series matters. |
| History: dated series from before and after | A connected tool first; then the user's exports (profile performance, Search Console, call tracking, old scans) | Without a before there is no baseline, only today. Say how rough that makes the read. |
| Suspension details, if any | The email or notice, word for word; whether anyone has already appealed; whether a second profile was made | Decides the order of work. A request already filed, or a duplicate already made, changes what to do first. |
| Who the work is for | The conversation, the brief | Owner, in-house team or agency client changes wording, owners named and white-labelling, not the method. |

## Asking well

When you do have to ask, ask everything still missing in one message, with short options where they speed up the answer, for example "What changed in the three months before? Profile edits, a new website, a move or rebrand, new people with profile access, reviews disappearing, a new competitor, or nothing you know of." Skip anything you already found, and say what you found so the user can correct it.

## The brief and the working files

Update `local-seo-brief.md` with what you learned: the business, its shape from the lens, money searches, area, locations, data available, and the drop under the problems reported. If a brief exists, add to it rather than replacing it; other skills read it, so use plain labels rather than a fixed form.

Alongside it, keep the series and timeline as `recovery.json`, the input to `scripts/change_points.py`. It is the record of what was found and when, and the baseline for every later re-check. Add each fix and re-check to `local-seo-log.md` as you go.

In Claude Code save these in the working folder; in the Claude app show them and offer them as files.
