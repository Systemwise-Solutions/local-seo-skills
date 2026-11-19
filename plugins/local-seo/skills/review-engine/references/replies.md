# Replies

Reply to every review. It shows the business is active, and it tells the next customer how problems get handled. Replies matter more for winning the click than for ranking.

**Speed:** within 2 working days; negative reviews the same working day, even if only to acknowledge.

**For every reply:**
- Thank them, and be specific to what they wrote (not to what you know about them).
- Short: 2 to 4 sentences for positive, 3 to 5 for negative.
- Sign off with a first name or role, so it reads like a person.
- Never share personal details: theirs, staff surnames, job addresses, what they paid.
- Vary the wording. Ten identical replies in a row read as automated.
- The reply is for the next customer reading it as much as for the reviewer.

## Positive (4 and 5 stars)

General businesses can mention the job and the place the reviewer mentioned. It reinforces what the business does and where.

> Thanks {first name}, really glad the new boiler's keeping you warm. It was a pleasure working in Leyton, and we'll see you for the first service next year. {sender}

> Thank you for taking the time to write this. Good to hear the bathroom leak was sorted on the first visit. {sender}, {business}

> Thanks {first name}! We'll pass this on to {staff first name}, who'll be very pleased. {sender}

Short review ("Great service"):

> Thank you, {first name}. Glad it all went smoothly, and thanks for recommending us. {sender}

## Neutral (3 stars, or mixed)

Thank, take the criticism seriously in one line, say what changes, invite them back.

> Thanks for the honest review, {first name}. You're right that we should have called ahead when we were running late, and we've changed how the team lets customers know. If there's anything else, I'm on {phone}. {sender}, owner

> Thank you for the feedback. Glad the work was right, and sorry the price wasn't clearer up front. We now send every quote in writing before we start. {sender}

## Negative (1 and 2 stars)

Acknowledge, don't argue, take it offline, give a named way to reach a person. Don't explain at length or correct their account in public. If it gets resolved, they may update the review; ask once, never push.

> {First name}, I'm sorry to read this. That's not the experience we want anyone to have. I'd like to understand what happened and put it right: please call me on {phone} or email {email}. {sender}, owner

> Thank you for telling us. We've looked into this and I'd like to talk it through with you directly. Please get in touch on {phone}, and ask for {sender}.

When the review is factually wrong (wrong business, a job you never did):

> We can't find a record of this, and we'd like to understand what happened. Please call us on {phone} so we can look into it. {sender}

If it's fake, spam or from a competitor, report it (removals.md). Keep the reply calm: readers judge the reply more than the review.

## Regulated sectors: safe replies

Clinics, dentists, physios, therapists, pharmacies, vets in some cases, solicitors and accountants. The rule: **a reply never confirms the person was a patient or client, and never mentions their treatment, condition, practitioner, visit or outcome.** Even when the reviewer wrote about it first. Professional regulators expect the same confidentiality online as anywhere else.

Don't write: "your treatment", "your appointment", "your sessions with Tom", "glad your knee is better", "as a patient", "our records show". Don't repeat the name of a prescription-only medicine the reviewer mentions.

**Positive:**
> Thank you for taking the time to leave a review. We're glad you found the team helpful.

> Thank you for your kind words. We'll share them with the team.

> Thank you for this lovely review. It means a lot to everyone here.

**Neutral:**
> Thank you for your feedback. We take every comment seriously and use it to improve. If you'd like to discuss anything, please contact our practice manager on {phone}.

**Negative:**
> We're sorry to read this. We can't discuss individual circumstances here, but we'd welcome the chance to talk. Please contact our practice manager on {phone} or {email}.

> Thank you for raising this. Confidentiality means we can't respond to specifics publicly, but we'd like to hear from you directly. Please call {phone} and ask for our practice manager.

**Solicitors and accountants:** the same templates with "client" wording removed and "the firm" in place of "the team" where it fits.

Run `review_tracker.py --regulated` monthly to catch replies that slip.

## With SearchOps

`draft_review_reply` drafts one reply in the business's saved style; `save_review_reply_draft` saves one you've written. Both save a draft for a person to post. Use them one review at a time and only when the user asks; show the text first. For regulated sectors, check every draft against the rule above before saving.
