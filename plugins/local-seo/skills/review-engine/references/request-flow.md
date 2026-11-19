# The request flow

Four touches. Everyone gets asked, because asking only some customers is both unfair (loop.md, limits) and the commonest reason reviews dry up.

| Touch | When | How | Who |
|---|---|---|---|
| 1. Text message | Soon after the customer has the value: the job finished, the visit over, the stay ended, the order delivered, the matter closed | A short text with the one-tap review link | Automatic from the system that marks it done, or the person who served them |
| 2. Email | A few days later, once, only to those who haven't reviewed (or to everyone, if the system can't tell) | The same link. Never a third | Automatic |
| 3. QR code | Where the customer pays, collects or receives the work | On the counter, receipt, invoice, packaging, job sheet or leave-behind | Printed once |
| 4. Staff prompt | When the customer says something positive, or at handover | One line, then the card or "I'll text you the link" | Whoever is with the customer |

Why this shape: texts get opened, emails get filed. The hour or so after the value lands is when the customer still feels it. One follow-up catches people who meant to; a second starts to annoy. Mani's working rule is a text within the hour and the follow-up two to three days later; adjust if the value lands later than the transaction (a product that needs using first, a result that takes time to show), because the ask should follow the moment the customer can judge it.

If the business has no phone numbers but does have emails, the email becomes touch 1, sent the same day.

## Repeat customers

Where people come back often (memberships, courses, regular appointments, subscriptions, repeat orders), don't ask after every visit. Ask once in a while (Mani's rule of thumb: about every six months per customer), on a visit worth reviewing: early in a run once they've seen the value, at the end of a course, or after something bigger than usual. Most systems can filter on "not asked in the last X days"; if not, keep a column in the customer list.

## Why reviews stop: the usual failing step

| Symptom | Likely failing step | Fix |
|---|---|---|
| Burst after a team push, then nothing | Asking depends on people remembering | Automate the ask from the system that marks the sale or job done |
| Few reviews despite lots of customers | The ask goes days later, or only by email | Move to a text soon after the value lands |
| People say they tried and couldn't | Link opens the profile or Maps, not the review form, or needs a desktop sign-in | Use the direct review link; test it on a phone |
| Reviews short and generic ("Great service") | No invitation to say what and where | Add the one light line to the message and staff prompt |
| One branch or person gets all the reviews | Only some staff ask | The same automatic ask for every branch, each with its own link |
| Requests sent, reviews down | Timing slipped, or the link broke | Check send times in the system and tap the link yourself |

## The direct review link

The link should open the "write a review" box, not the profile.

1. **From the Business Profile.** Signed in as an owner or manager, find the business on Google and use the option to ask for reviews (the label changes: check what it says now). Copy the link it gives.
2. **From the Place ID.** Find the Place ID with Google's Place ID Finder (in the Google Maps Platform docs). The link is `https://search.google.com/local/writereview?placeid=<PLACE_ID>`.

Test it on a phone that isn't signed in to the business account: it should open the star rating box in one tap. Many locations: one link per location, and check each opens the right one.

Use the link as it is. Generic link shorteners can look like spam in a text and some phones flag them.

## The QR code

Make it from the direct link with a generator that makes static codes, because static codes don't stop working if a subscription lapses. Print it big enough to scan from arm's length, with a line of text above it ("Leave us a Google review"). Test it with two phones before printing a batch.

## Setting it up in the systems they have

- **A booking, job, ordering or till system with automations:** most can send a message when an appointment, job or order is marked complete. Set the trigger, the delay, the message and the link, following the system's own help pages.
- **A review or messaging tool:** fine if it sends to everyone. Turn off any "check satisfaction first" step, because that is gating and it gets reviews removed.
- **No system:** the person who served the customer sends the text from the business phone, with the message saved as a template. Weekly, the owner checks sales or jobs against texts sent.

## Practical risks

loop.md covers fairness (everyone asked, no incentives, no fake, staff or bought reviews). In practice also:

- **Don't blast an old customer list in one day.** A spike looks unnatural and some reviews may be filtered. To ask past customers, spread it over several weeks.
- **Don't hand customers a device to review on the spot.** Reviews from the business's own device or network are often filtered.
- **Keep offers out of the request.** A request with a promotion in it becomes a marketing message, which needs the customer's marketing consent. Keep it to the ask and the link, and give a way to stop emails.
- **Incentives are a legal risk as well as a platform one** in some places (in the UK, undisclosed incentivised and fake reviews are banned). One line is enough; then give the timing fix.
