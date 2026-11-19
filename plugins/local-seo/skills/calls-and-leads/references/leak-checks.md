# Leak checks, stage by stage

Each stage: the question, what to check, and what makes it a finding. Compare against the business's own baseline and against the 3 businesses beside it in the map pack. Don't use industry "average conversion rates": they vary too much by sector and search to mean anything for one business.

## Contents
1. Seen
2. Acted
3. Profile converts
4. Page converts
5. Reached
6. Booked
7. Counted

---

## 1. Seen

Question: are fewer people seeing the business, or never were enough?

| Check | Finding when |
|---|---|
| Profile views, same months last year | Down 20% or more and not explained by the season. |
| Views split Search vs Maps | One side fell and the other didn't: often a ranking change on that surface. |
| Search terms (profile search terms or Search Console) | Views come mostly from the business name, not services. A visibility problem dressed up as a leads problem. |
| Rankings for the money searches | Not in the top 3 at the business's own location, or the strong radius is smaller than where customers come from. |

If Seen is the leak: hand to `local-seo-audit` for rankings. Keep going here.

## 2. Acted

Question: of the people who see the profile, do as many act?

| Check | Finding when |
|---|---|
| Profile action rate (calls + website clicks + directions) / views | Fell 15% or more against the baseline. |
| Call rate vs website click rate | One fell while the other held or rose. Calls falling while clicks rise often means the phone number is hard to find or wrong, or people are going to the site to check something the profile doesn't say (prices, hours, area). |
| Profile search terms | The profile shows for searches that don't fit (a different service, another town): views rise, actions don't. |

## 3. Profile converts

Question: does the profile give people a reason to pick this business over the two beside it?

Open the profile on a phone next to the 3 competitors.

| Check | Finding when |
|---|---|
| Phone number | Wrong, an old number, a number that doesn't ring through, or a tracking number not set up as primary with the main number as additional. Impact high, effort low. |
| Hours | Profile shows closed when people call (compare with the call log by hour). Holiday hours missing. Shows open when nobody answers. |
| Booking link and website link | Missing, broken, or pointing at a generic homepage rather than the page that sells the money search. No UTM. |
| Reviews | Newest review much older than competitors'. Rating well below theirs. Recent negative reviews unanswered. |
| Photos | Few, old or stock, against competitors with recent photos of real work and the team. |
| Prices and services | Services missing or vaguely named. No price guidance where competitors give it. |
| Description and attributes | Doesn't say what, where and for whom. Relevant attributes missing (for example wheelchair access, free estimates, online appointments). |
| Suggested edits | Google or a user changed the number, hours or website and nobody noticed. Check the edit history. |

## 4. Page converts

Question: does the landing page turn a phone visit into a call, form or booking?

Open the page the profile links to at phone width (about 390px).

| Check | Finding when |
|---|---|
| Above the fold on mobile | No call button, no book or quote button, or they sit below a large image or slider. |
| Call link | Number isn't a `tel:` link, or the number differs from the profile with no reason (call tracking aside). |
| The form works | A test submission doesn't arrive within a few minutes, goes to an old inbox or spam, or the success message shows but nothing is sent. Most common after a rebuild. Impact high. |
| Form length | Asks for more than the business needs to call back (address, budget, how they heard) before the person can send. |
| Booking path | Errors, asks for an account, shows no availability, or takes more than a few taps to a confirmed slot. |
| Speed on mobile | Slow enough that the call button appears late (PageSpeed Insights, mobile). Only a priority when it's clearly costing actions. |
| What the page says | Doesn't say what, where, price guidance and proof. People leave to check a competitor. |
| Key events by landing page (GA4) | One page converts far worse than the rest, or a page's key events fell to near zero on a date (a broken form or tag). |

## 5. Reached

Question: when someone calls or sends a form, does a person get back to them in time?

| Check | Finding when |
|---|---|
| Answer rate (phone log) | Under about 85 to 90% for a business that lives on calls, or fell against the baseline. Every missed call from search is often a lost job: people ring the next business. This is a working rule from client work, not a published benchmark. |
| Missed calls by hour and day | Clusters before opening, at lunch, after 5pm or on Saturdays. Compare with the profile's hours. |
| Out of hours | Voicemail full or generic, no promise of a call-back time, no text back. |
| Call-back time | Missed calls not returned the same day. |
| Form reply time | Replies take longer than a working day, or go unanswered. |
| Who answers | Calls go to a mobile on a roof, under a sink, or in clinic. Plan a call-back routine, a missed-call text, or an answering service. |

## 6. Booked

Question: do enquiries become jobs?

| Check | Finding when |
|---|---|
| Booking rate (bookings / calls + forms) | Fell against the baseline. |
| Lead quality | Enquiries for jobs the business doesn't do, outside the area, or price shoppers. Fix at the source: services, page copy and profile saying clearly what and where. |
| Quote follow-up | Quotes sent and never chased. |
| Price shock | Callers drop off once they hear the price. Publishing price guidance on the page filters them earlier and saves time. |

## 7. Counted

Question: can the business see which stage moved?

| Check | Finding when |
|---|---|
| Call tracking on the profile | None, or the tracking number replaced the main number everywhere. Set up per tracking.md. |
| UTM on the profile website link | Missing: profile visits blend into organic search in GA4. |
| GA4 key events | No key events for calls (tel: link clicks), forms (successful submission, not button click) or bookings (confirmed booking). |
| Bookings by source | The booking system or diary doesn't record where the customer came from. |
| One number of truth | Profile calls, tracked calls and the phone log are never compared. They'll differ: profile calls are taps, not connected calls. |
