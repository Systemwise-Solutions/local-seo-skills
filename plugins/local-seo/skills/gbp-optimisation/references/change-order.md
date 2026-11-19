# Making the changes in order

Some fields are sensitive. Editing the name, address or primary category can prompt a fresh review by Google, and occasionally a request to re-verify. So the changes go in one at a time, in a planned order, each logged with its date. If Google asks a question, or rankings move, you know which edit prompted it.

## The order

| Stage | Fields | Sensitivity | Why here |
|---|---|---|---|
| Day 1, in parallel | Duplicate and practitioner clean-up (support requests) | Parallel | Doesn't touch the main profile; support can take weeks, so start early. |
| 1 | Name to match the signage, address or service-area fix | High | Suspension risks first. Everything else is wasted if the profile goes down. |
| 2 | Primary category | High | The strongest relevance signal. Alone, so its effect can be read. |
| 3 | Secondary categories (add and remove) | Medium | After the primary has settled. |
| 4 | Services, products, description, hours, holiday hours, attributes, booking link | Low | These go in together on one day. |
| 5 | Phone, website link | Medium | The website link only once the right page is live. |
| 6 | Photos, Q&A, posts | Ongoing | From the low-risk day on, then on a schedule. |

`change_log.py` applies this order. The gaps it uses (7 days after a high-sensitivity edit, 3 after a medium one) are a working rule, long enough to see the edit go live on Maps and to notice any verification request before the next one. They aren't a Google rule; change them with `--gap` and `--gap-medium` if there's a reason.

Move something earlier only with a reason, and note it in the output. Typical reasons: hours are wrong and losing calls today (move to day 1, it's low risk); a page for the website link is already live (it can go in stage 4).

## The log

Every change gets: the date made, the date it showed as live on Maps, whether Google asked anything, and notes. Keep it with the brief. It is how anyone working on the profile later knows what was changed, when, and why.

## If Google asks to re-verify

- Don't make any other edits until it's resolved.
- Follow the method Google offers. For video verification, show in one continuous take: the street and signage outside, the entrance, the inside or the work equipment, and something only the business would have (keys to the premises, a branded van, the business's tools). Do it in daylight.
- Have ready: business registration in the name on the profile, a utility bill or lease for the address, photos of permanent signage.

## If the profile is suspended

Stop optimising. Don't create a new profile. Don't appeal until the likely cause is fixed (name, address, duplicate, or the last sensitive edit). Gather evidence that matches what Google can see: registration documents in the profile's name, a bill or lease for the address, photos of permanent signage, and a website and listings showing the same name, address and phone. Treat the appeal as one good chance.

## Upkeep (hand this over)

**Monthly, 20 minutes:**
- Check for "Google updated" notices and reject any that aren't true.
- Add 2 to 4 new photos of real work.
- Answer any new questions; post if there's something useful to say.
- Check hours; set holiday hours before every bank holiday.

**Never change casually:** the name, the address, the primary category. Change them only with a reason, one at a time, and log it.

**One owner.** Keep one owner account in the business. Agencies and consultants get manager access, removed when the work ends.
