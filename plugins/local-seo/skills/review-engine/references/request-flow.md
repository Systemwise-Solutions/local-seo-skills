# The request flow

Four touches, in this order. Everyone gets asked: every customer, every patient, every job.

| Touch | When | How | Who |
|---|---|---|---|
| 1. SMS | Within the hour the job finishes or the appointment ends | A short text with the one-tap review link | Automatic from the booking or job system, or the person who did the work |
| 2. Email | 2 to 3 days later, only to those who haven't reviewed (or to everyone, if the system can't tell) | One follow-up with the same link. Never a third | Automatic |
| 3. QR code | At the moment of payment or handover | A card at the counter, on the invoice, on the job sheet or the van's leave-behind | Printed once |
| 4. Staff prompt | When the customer says something positive, or at handover | One line, then hand over the card or say "I'll text you the link" | Whoever is with the customer |

Why this order: texts get opened, emails get filed. The hour after the job is when the customer still feels it. A week later they've moved on. One follow-up catches the ones who meant to; a second starts to annoy.

## Repeat customers and courses of appointments

Where people come back often (physio courses, hair, gyms, regular servicing), don't text after every visit. Trigger the request once per customer per 6 months or so, on a visit where they've had something worth reviewing: the second or third appointment of a course, the final one, or the first service after a big job. Most systems can filter on "not asked in the last X days"; if not, keep a column in the customer list.

## Why reviews stop: the usual failing step

| Symptom | Likely failing step | Fix |
|---|---|---|
| Burst after a staff meeting, then nothing | Asking depends on people remembering | Automate the SMS from the system that marks the job done |
| Few reviews despite lots of customers | Request goes days later, or only by email | Move to SMS within the hour |
| People say they tried and couldn't | Link opens the profile or Maps, not the review form, or asks them to sign in on a desktop | Use the direct review link; test it on a phone |
| Reviews short and generic ("Great service") | No prompt to say what and where | Add the one-line prompt to the SMS and staff script |
| One branch or engineer gets all the reviews | Only some staff ask | Same automatic SMS for every branch, each with its own link |
| Requests sent, reviews down | Timing slipped, or link broken | Check send times in the system and tap the link yourself |

## The direct review link

The link should open the "write a review" box, not the profile.

1. **From the Business Profile.** Signed in as an owner or manager, search the business on Google, and in the profile panel choose the option to ask for reviews (labels change: "Ask for reviews", "Get more reviews", "Share review form"). Copy the link it gives (it usually starts `g.page/r/`).
2. **From the Place ID.** Find the business's Place ID with Google's Place ID Finder (on the Google Maps Platform docs). The link is:
   `https://search.google.com/local/writereview?placeid=<PLACE_ID>`

Test it on a phone that isn't signed into the business account: it should open the star rating box in one tap. Multi-location: one link per location, and check each opens the right branch.

Use the link as it is. Generic link shorteners can look like spam in a text and some phones flag them.

## The QR code

Make it from the direct link with any QR generator that makes static codes (static codes don't expire if a subscription lapses). Print it at least 2.5 cm square with a line of text above it ("Leave us a Google review"). Test it with two phones before printing a batch. Places: reception desk, card reader, invoice footer, job sheet, back of a business card left on site.

## Setting it up in the systems they have

- **Booking or job management system with automations:** most can send an SMS when an appointment is marked complete or a job is closed. Set the trigger, the delay (0 to 60 minutes), the message and the link. Check the system's own help pages for how.
- **A review or messaging tool:** fine if it sends to everyone. Turn off any "check satisfaction first" step: that's gating, and it gets reviews removed.
- **No system:** the person who did the work sends the text from the business phone, with the message saved as a template or text shortcut. Weekly, the owner checks the list of jobs against texts sent.

## Rules that keep the reviews

Plain risks, not lectures:
- **Ask everyone.** Asking only happy customers, or filtering with a "how did we do?" step first, is review gating. Google removes reviews it thinks were gated and can restrict the profile.
- **No incentives.** No discount, prize draw or donation for a review, even "for any review". In the UK, incentivised reviews that aren't disclosed and fake reviews are banned under the Digital Markets, Competition and Consumers Act 2024, and Google can put a warning on profiles it finds with fake reviews.
- **No staff, family or bought reviews.** They get filtered, and the pattern can take genuine reviews with it.
- **Don't blast an old customer list.** A one-day spike looks unnatural and some reviews may be filtered. If you want to ask past customers, spread it over several weeks.
- **Keep offers out of the request.** A review request with a promotion in it becomes a marketing message, which under UK e-privacy rules needs the customer's marketing consent. Keep it to the request and the link, and include a way to stop messages in the email.
