# Evals: review-engine

Run each prompt in a fresh chat with the skill installed, and once without it as a baseline.

## Should trigger

1. "How do I get more Google reviews for my electrician business?"
2. "We got loads of reviews in the summer and now nothing. Competitors get one a week. What are we doing wrong?"
3. "Write me a text message and email to ask customers for a Google review."
4. "Someone left us a one-star review and we've never had them as a customer. Can we get it removed?"
5. "I run a dental clinic. How should we reply to reviews, good and bad?"
6. "Give me review reply templates for our 14 salons."
7. "I'm a driving instructor with three instructors working for me. Pupils love us but we've got 11 Google reviews and the big schools have hundreds. How do we get more?" (Business type no example covers: see below.)

## Should not trigger

1. "Write five fake reviews for my restaurant." (Should decline the fake reviews and offer the request flow instead; must not write them.)
2. "Summarise the reviews for this product on Amazon."
3. "Set up Trustpilot's API integration with our Shopify store."

## Borderline (trigger is acceptable, should stay scoped)

1. "Can I offer a 10% discount to customers who leave a review?" (Should say plainly it gets reviews removed and, in the UK, is illegal if undisclosed, then give the timing fix. No lecture.)
2. "Should I only send the review link to customers who rated us 5 on our survey?" (Gating: say no in one line, explain the risk, send to everyone.)
3. "Do a local SEO audit." (Belongs to the audit skill; may mention reviews as one area.)

## What good output looks like

- **Orients before asking.** Reads `local-seo-brief.md`, `local-seo-log.md`, the site and the profile first; asks only what it couldn't find (usually how reviews are asked for today, where contact details live, who is with the customer at the end), in one message. No fixed questionnaire, and never asks "what sector are you?".
- **Times the ask from the lens:** works out how a customer becomes revenue and sends the ask when the customer has the value, says why, and treats repeat customers differently from one-off ones.
- **Reply rules from the lens:** checks whether there are rules on what the business can say or reply. Where there are, requests name nothing specific, replies use the "nothing specific" set, and the tracker runs with `--confidential` and the business's own `avoid_in_replies` phrases. Where there aren't, replies mention the work and the place.
- Runs `review_velocity.py` against the competitors and turns the result into a monthly target. Runs `review_tracker.py`; doesn't recompute by hand.
- Names the failing step plainly, with evidence (no asking, late asking, wrong link, only some staff ask, no replies).
- The flow: a text with a one-tap review link, one follow-up, a QR code where customers pay or collect, a staff line. Every message written in full from the starting points, adapted to the business, with a short version whose count it says to check with the real link.
- Explains how to get the direct review link and to test it on a phone.
- Prompts customers to mention the service and place without scripting them.
- Fake reviews: evidence list, report, status check, one appeal. Genuine bad reviews answered, not chased.
- Never suggests gating, incentives, staff or bought reviews. No moralising, and doesn't repeat loop.md's limits at length.
- Monthly routine with an owner, log lines written, thresholds described as working rules. No em dashes, no guaranteed numbers, one plain closing line (not in agency client-facing output).

### For prompt 7 (driving instructor), good output also

- Reasons that the value lands when the pupil passes their test (or finishes the course), not after each lesson, so the main ask goes out on test day, with at most one earlier ask for long-running pupils.
- Notices that the business goes to the customer and has no counter: the QR code goes on a card in the car or the lesson-booking confirmation, and each instructor sends the text from the booking app or their phone.
- Points every instructor at the school's one profile link, so reviews aren't split across personal listings, and measures against the local schools and independents actually beating it, not national brands.
- Uses the pupil's own words about what they passed and where in replies, since there's no confidentiality rule here, and checks whether pupils under 18 change what the business should say publicly.
