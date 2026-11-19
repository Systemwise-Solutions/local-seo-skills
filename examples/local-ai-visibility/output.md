# AI visibility: Example Physio

19 November 2026 · 1 location · Data: your 30 runs across ChatGPT, Gemini, Perplexity and Google AI Overviews, plus my web search of the sources. Example Physio and everything in this file is fictional.

## The short version
Gemini and Google's AI Overviews name you in 2 of every 3 runs, but ChatGPT names you in 2 of 9 and Perplexity in 1 of 9, while Avonside Physio is named in every run on every assistant. The split points at the sources: Google's AI leans on your own site and profile, which carry you, while ChatGPT and Perplexity lean on Doctify, a Bristol comparison article and Reddit, which either don't list you or still show your old Hotwells address. Fixing how those sources describe you, and putting plain facts on your site, is the work most likely to change what ChatGPT and Perplexity say.

This is the newest and least certain part of local search. Answers change between runs and models, so these are patterns from a sample of 30, and nobody can guarantee a mention.

## Do these three first
1. **Correct your Doctify listing.** Doctify was cited in 13 of the 30 runs, more than any other source, and only 3 of those runs named you. Your listing still has the Hotwells address and says "general physiotherapy". Owner: you. Effort: low.
2. **Put the facts on your homepage.** Your site was cited in 10 runs and every one of them named you, so it works when an assistant reads it, but the homepage doesn't say what you treat, your prices or that your physios are HCPC registered. The copy is below. Owner: your web person. Effort: low.
3. **Ask the Bristol guide to consider you.** "The best physios in Bristol" on bristol-guide.example was cited in 11 runs, mostly by Perplexity, and lists Avonside, Downs Movement and Physio Lane, not you. Send the email below. Owner: you. Effort: medium.

## How often you're named

Measured from your runs (mention_rate.py):

| Assistant | Runs | Named | Mention rate | Your site cited |
|---|---|---|---|---|
| ChatGPT | 9 | 2 | 22% | 1 of 9 |
| Gemini | 9 | 6 | 67% | 6 of 9 |
| Perplexity | 9 | 1 | 11% | 1 of 9 |
| Google AI Overviews | 3 | 2 | 67% | 2 of 3 |

By prompt, named / runs:

| Prompt | ChatGPT | Gemini | Perplexity | AI Overviews |
|---|---|---|---|---|
| best physio in Clifton Bristol | 1/3 | 2/3 | 0/3 | 2/3 |
| physio for running injury near Clifton | 1/3 | 2/3 | 1/3 | not run |
| back pain physio recommendations, Bristol | 0/3 | 2/3 | 0/3 | not run |

Who is named instead: Avonside Physio in 100% of runs on every assistant; Downs Movement Clinic in 89 to 100%. Physio Lane Clinic (13 runs) and Hotwells Back Care (7 runs) also appear often.

The back pain prompt is your weakest on ChatGPT and Perplexity: 0 of 6. You treat back pain, but nothing outside your own site says so.

## Where the answers come from

| Source | Cited in | Runs naming you | Lists you? | What it says |
|---|---|---|---|---|
| doctify.com | 13 runs (ChatGPT, Perplexity, AI Overviews) | 3 | Yes | Old Hotwells address, "general physiotherapy", 6 reviews against Avonside's 48 |
| bristol-guide.example | 11 (ChatGPT, Perplexity) | 1 | No | Lists Avonside, Downs, Physio Lane |
| your site | 10 (all four) | 10 | - | Named every time it was read |
| avonsidephysio.example | 10 | 5 | - | Competitor's site |
| reddit.com (r/bristol) | 7 (all but AI Overviews) | 0 | No | Running-injury thread recommending Avonside and Downs |
| yell.com | 3 (ChatGPT) | 0 | No listing found | Lists Avonside, Hotwells Back Care |
| topdoctors.co.uk | 2 (Perplexity) | 0 | No | Lists Downs |

Listing status is from my web search (fictional results in source-check.md), except Doctify, which you confirmed.

## How you're described

- **Address**: Doctify still shows Hotwells. Your profile and site show Clifton village. Two addresses for one practice is the kind of disagreement that makes an assistant less sure of you.
- **What you do**: your profile says "Physiotherapist"; Doctify says "general physiotherapy"; your homepage says "friendly practice". Avonside is described as "sports injuries and running assessments" on its site, Doctify and the Bristol guide alike. That consistency is most of why it's named every time.
- **Credentials**: nowhere outside your site's team page mentions HCPC registration.

## What your site should say

Homepage, directly under the main heading. Confirm every fact before it goes live; gaps are marked [like this].

> Example Physio is a physiotherapy practice in Clifton village, Bristol, at [full address]. We treat sports and running injuries, back and neck pain, and recovery after surgery.
>
> All our physiotherapists are registered with the HCPC. [Number] physios, treating patients in Clifton since [year].
>
> An initial assessment is £55 and takes [45] minutes. Follow-up sessions are £[price]. We see patients from Clifton, Redland, Cotham and Hotwells, and you don't need a GP referral.
>
> Rated [4.9] from [41] Google reviews. Book online or call [phone]. Open [hours], including [evenings].

Running injury page (or a new one if there isn't one), opening lines:

> Running injury physio in Clifton, Bristol. We assess how you run, find what's causing the pain, and give you a plan to get back to running. Common problems we treat: [runner's knee, shin splints, Achilles pain, plantar fasciitis].

Back pain page, opening lines:

> Back pain physio in Clifton, Bristol, for desk-job back pain, sciatica and back injuries. Your first appointment is a full assessment and a plan you can start that day. [Add one line on how many sessions people usually need, only if it's true across most patients.]

No outcome promises ("cure", "pain-free in 3 sessions"); they're a problem for a regulated profession. Make sure the LocalBusiness schema on the homepage has the Clifton address and phone, matching the profile exactly.

## The plan

### This month
- **Doctify**: change the address to Clifton, replace "general physiotherapy" with your three main services (sports and running injuries, back and neck pain, post-surgery rehab), add HCPC registration and prices. Owner: you. Effort: low.
- **Homepage and service pages**: paste the copy above. Owner: web person. Effort: low.
- **Yell**: create the listing with the same name, address, phone and services as the profile. Owner: you. Effort: low.
- **Review requests that name the treatment**: SMS with your Google review link within the hour after each appointment, one follow-up two days later. Ask patients to mention what they came in for, without scripting the words. Alternate with Doctify, which has 6 reviews to Avonside's 48. Owner: you. Effort: low, routine.

### Next two months
- **Bristol guide**: email the editor (below). Effort: medium.
- **Top Doctors**: create a listing for your lead physio. Effort: low.
- **Reddit**: nothing planted. If you or a physio already use Reddit under your own name, a helpful answer in a running-injury thread, saying who you are, is fine. Otherwise leave it; it follows from reviews.
- **Re-run the check** in mid-December with the same 3 prompts, 3 runs each, on the same four assistants.

Email to the Bristol guide:

> Subject: A Clifton physio for your Bristol list
>
> Hi [name], I run Example Physio in Clifton village. I saw your guide to the best physios in Bristol and wondered if you'd consider us when you next update it. We specialise in running injuries and back pain, all our physios are HCPC registered, and we're rated [4.9] from [41] Google reviews. Happy to answer any questions or send anything you'd need. Thanks, [name], [phone]

## Not checked
- Google AI Mode and Copilot: not run. Add them next month if your patients use them.
- AI Overviews for prompts 2 and 3: not run.
- Visits from assistants in GA4: not shared. A referral report filtered to chatgpt.com, gemini.google.com and perplexity.ai would give a baseline (a floor, not a total).
- Whether Top Doctors and Yell have an old listing under a different name: search them by your phone number.

## How to measure progress
- Re-run the same 3 prompts, 3 runs each, on the same assistants, monthly. Paste them in the same format and run mention_rate.py.
- Count a change only when it's more than one run per prompt and shows on more than one prompt.
- Watch Doctify's share: it should start naming you in more of the runs that cite it once the listing is fixed.

## Log lines added
- 2026-11-19: AI visibility baseline, 30 runs, 3 prompts (prompt-set.md). Named: ChatGPT 2/9, Gemini 6/9, Perplexity 1/9, AI Overviews 2/3. Avonside Physio named in every run. Re-run the same set 2026-12-17.
- 2026-11-19: Doctify listing shows the old Hotwells address. Correct this month; re-check the listing 2026-12-01.

## Next steps
If you'd rather have it done with you: localseoconsultant.net/consulting/ai-search-visibility/
