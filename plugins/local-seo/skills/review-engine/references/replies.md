# Replies

Reply to every review, because it shows the business is active and tells the next customer how problems get handled. Replies matter more for winning the click than for ranking.

**Speed** (Mani's working rule): within two working days; negative reviews the same working day, even if only to acknowledge, because an unanswered complaint reads as indifference to everyone who sees it.

**Every reply:**
- Thank them, and be specific to what they wrote, not to what you know about them, because the reply is public.
- Short: two to four sentences for positive, three to five for negative.
- Sign off with a first name or role, so it reads like a person.
- No personal details: theirs, staff surnames, addresses, what they paid.
- Vary the wording. Identical replies in a row read as automated.
- Write for the next customer reading it as much as for the reviewer.

Placeholders: `{first name}`, `{sender}`, `{business}`, `{phone}`, `{email}`, `{staff first name}`, `{what they mentioned}`, `{area they mentioned}`.

## First: are there rules on what a reply may say?

Check the lens (loop.md). Where confidentiality, a regulator or brand rules apply, a reply never confirms the person was a customer or client and never refers to what they came for, their case, the person who served them, or the outcome, even when the reviewer wrote about it first. Don't repeat the name of a product or service the business may not promote. Use the "nothing specific" set below for every reply, and run `review_tracker.py --confidential` (plus the business's own phrases with `avoid_in_replies`) to catch existing replies that slip. Flag the templates for whoever signs off public wording.

Everywhere else, use the standard sets.

## Positive (4 and 5 stars)

Mention what the reviewer mentioned, and the place if they named it. It reinforces what the business does and where.

> Thanks {first name}, really glad {what they mentioned} worked out. Good to hear from {area they mentioned}, and hope to see you again. {sender}

> Thank you for taking the time to write this. Pleased {what they mentioned} was sorted first time. {sender}, {business}

> Thanks {first name}! We'll pass this on to {staff first name}, who'll be very pleased. {sender}

Short review ("Great service"):

> Thank you, {first name}. Glad it all went smoothly, and thanks for recommending us. {sender}

## Neutral (3 stars, or mixed)

Thank them, take the criticism seriously in one line, say what changes, invite them back.

> Thanks for the honest review, {first name}. You're right that we should have let you know we were running late, and we've changed how the team keeps customers updated. If there's anything else, I'm on {phone}. {sender}

> Thank you for the feedback. Glad {what they mentioned} was right, and sorry the price wasn't clearer up front. We now confirm every price in writing before we start. {sender}

## Negative (1 and 2 stars)

Acknowledge, don't argue, take it offline, give a named way to reach a person. Don't explain at length or correct their account in public, because readers side with whoever sounds calmer. If it gets resolved, they may update the review; ask once, never push.

> {First name}, I'm sorry to read this. That's not the experience we want anyone to have. I'd like to understand what happened and put it right: please call me on {phone} or email {email}. {sender}

> Thank you for telling us. We've looked into this and I'd like to talk it through with you directly. Please get in touch on {phone} and ask for {sender}.

When the review doesn't match any customer (wrong business, something you never did):

> We can't find a record of this, and we'd like to understand what happened. Please call us on {phone} so we can look into it. {sender}

If it's fake, spam or from a competitor, report it (removals.md). Keep the reply calm: readers judge the reply more than the review.

## Nothing specific (where there are rules on what a reply may say)

**Positive**
> Thank you for taking the time to leave a review. We're glad you found the team helpful.

> Thank you for your kind words. We'll share them with the team.

> Thank you for this lovely review. It means a lot to everyone here.

**Neutral**
> Thank you for your feedback. We take every comment seriously and use it to improve. If you'd like to discuss anything, please contact {role} on {phone}.

**Negative**
> We're sorry to read this. We can't discuss individual circumstances here, but we'd welcome the chance to talk. Please contact {role} on {phone} or {email}.

> Thank you for raising this. We can't respond to specifics publicly, but we'd like to hear from you directly. Please call {phone} and ask for {role}.

Don't write, in this set: "your {service}", "your appointment", "your case", "when we saw you", "as our client", "our records show", or the name of the person who served them.

## With SearchOps

`draft_review_reply` drafts one reply in the business's saved style; `save_review_reply_draft` saves one you've written. Both save a draft for a person to post. Use them one review at a time and only when the user asks; show the text first. Where there are reply rules, check every draft against them before saving.
