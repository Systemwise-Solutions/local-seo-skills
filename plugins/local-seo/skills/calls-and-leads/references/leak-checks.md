# Leak checks, stage by stage

Each stage: the question, what to check, and what makes it a finding. Check the routes this business actually makes money through (calls, forms, bookings, reservations, orders, walk-ins) and skip the ones it doesn't use. Compare against the business's own baseline and against the businesses beside it in the map pack. Don't use industry "average conversion rates": they vary too much by business and search to mean anything for this one.

## Contents
1. Seen
2. Acted
3. Profile converts
4. Page converts
5. Reached
6. Converted
7. Counted

---

## 1. Seen

Question: are fewer people seeing the business, or never were enough?

| Check | Finding when |
|---|---|
| Profile views, same months last year | Down clearly (the script flags 20%, Mani's working rule of thumb) and not explained by the season. |
| Views split Search vs Maps | One side fell and the other didn't: often a ranking change on that surface. |
| Search terms (profile search terms or Search Console) | Views come mostly from the business name, not what it sells. A visibility problem dressed up as a leads problem. |
| Rankings for the money searches | Weaker than the businesses winning them, or the strong radius is smaller than where customers come from. |

If Seen is the leak: hand to `local-seo-audit` for rankings. Keep going here.

## 2. Acted

Question: of the people who see the profile, do as many act?

| Check | Finding when |
|---|---|
| Profile action rate (the actions that matter here, divided by views) | Fell clearly against the baseline (the script flags 15%). |
| One action against another | One fell while another held or rose. Calls falling while website clicks rise often means the number is hard to find or wrong, or people are leaving to check something the profile doesn't say (prices, hours, menu, area, availability). Directions falling while views hold, for a business customers visit, often points at hours, photos or reviews. |
| Profile search terms | The profile shows for searches that don't fit (a different offer, another town): views rise, actions don't. |

## 3. Profile converts

Question: does the profile give people a reason to pick this business over the ones beside it?

Open the profile on a phone next to the competitors that show with it.

| Check | Finding when |
|---|---|
| Phone number | Wrong, old, doesn't ring through, or a tracking number not set up as primary with the main number as additional. Impact high, effort low. |
| Hours | Shows closed when people try to call or visit (compare with the call log or footfall by hour), holiday hours missing, or shows open when nobody answers. |
| Booking, order, menu and website links | Missing, broken, pointing at a generic page instead of the one that sells the money search, or at an old booking or ordering tool. No UTM. |
| Reviews | Newest review much older than competitors', rating well below theirs, recent negative reviews unanswered. |
| Photos | Few, old or stock, against competitors with recent photos of the real place, work, products or team. |
| Services, products, prices | Missing or vaguely named. No price guidance where competitors give it. |
| Description and attributes | Doesn't say what, where and for whom. Relevant attributes missing (for example accessibility, payment options, online appointments, delivery). |
| Edit history | Google or a user changed the number, hours, address or link and nobody noticed. |

## 4. Page converts

Question: does the landing page turn a phone visit into the action this business makes money from?

Open the page the profile links to at phone width (about 390px).

| Check | Finding when |
|---|---|
| Above the fold on mobile | The main action (call, book, reserve, order, get directions, ask for a quote) isn't visible without scrolling, or sits below a large image or slider. |
| Call link | Not a `tel:` link, or the number differs from the profile with no reason (call tracking aside). |
| The form works | A marked test submission doesn't arrive within a few minutes, goes to an old inbox or spam, or a success message shows while nothing is sent. Most common after a rebuild. Impact high. |
| Form length | Asks for more than the business needs to reply before the person can send. |
| Booking, reservation or order path | Errors, forces an account, shows no availability when there is some, or takes more taps than competitors' to a confirmed slot or order. Stop a test before payment. |
| Speed on mobile | Slow enough that the main action appears late (PageSpeed Insights, mobile). A priority only when it's clearly costing actions. |
| What the page says | Doesn't say what, where, price guidance and proof, so people leave to check a competitor. |
| Key events by landing page (GA4) | One page converts far worse than the rest, or a page's key events fell to near zero on a date (a broken form, widget or tag). |

## 5. Reached

Question: when someone calls, writes, books or turns up, does the business respond in time?

| Check | Finding when |
|---|---|
| Answer rate (phone log), for a business where calls matter | Fell against the baseline, or sits below about 85 to 90%. That floor is Mani's working rule of thumb from client work, not a published benchmark: a missed call from search usually goes to the next business. |
| Missed calls by hour and day | Clusters before opening, at lunch, after hours or at weekends. Compare with the profile's hours and peak times. |
| Out of hours | Voicemail full or generic, no promise of a call-back time, no text back. |
| Call-back and form reply time | Slower than the customer will wait. Compare with how fast competitors reply if you can test it. |
| Bookings, reservations and orders | Not confirmed, confirmed late, or left pending; orders accepted for times or areas the business can't serve. |
| Walk-ins | The profile, signage or site send people to the wrong entrance, at the wrong hours, or without parking or access information. |
| Who responds | The person who answers is also doing the work, so responses wait. Plan a call-back routine, a missed-call text, cover at peak times, or an answering service. |

## 6. Converted

Question: do enquiries become revenue?

| Check | Finding when |
|---|---|
| Outcome rate (the revenue event divided by enquiries) | Fell against the baseline. |
| Lead quality | Enquiries for things the business doesn't sell, outside the area, or at prices it can't do. Fix at the source: profile, services and page copy saying clearly what and where. |
| Follow-up | Quotes sent and never chased; abandoned bookings or orders never followed up where the tool allows it. |
| No-shows and cancellations | Rising, with no reminder or deposit where the business could use one. |
| Price shock | People drop off once they hear the price. Price guidance on the page filters them earlier and saves everyone time. |

## 7. Counted

Question: can the business see which stage moved?

| Check | Finding when |
|---|---|
| Call tracking on the profile | None, or the tracking number replaced the main number everywhere. Set up per tracking.md. |
| UTM on the profile links | Missing: profile visits blend into organic search in analytics. |
| Key events | No key events for the main actions: calls (tel: taps), forms (successful submission, not button click), bookings, reservations or orders (confirmed, not started). |
| Source on bookings or orders | The booking, order or job system doesn't record where the customer came from. |
| Walk-ins | No count at all. Even a weekly tally, or asking "how did you find us" at the till, beats nothing. |
| One number of truth | Profile actions, tracked events and the business's own records are never compared. They'll differ; know why. |
