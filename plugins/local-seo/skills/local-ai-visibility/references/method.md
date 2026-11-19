# Method: measuring AI answers as a pattern

## Where this sits

AI visibility is the top rung of the Visibility Ladder: eligible, understood, ranked, chosen, named. Being named seems to need other sources describing the business the same way. Work here is wasted while a lower rung is broken: an assistant can't confidently name a business whose name, address and services disagree across the web.

This is the newest part of Mani's model and the least certain. State that once in every report. Be clear about which parts are evidence, which are observation from client work, and which are inference.

## What we know, and how sure we are

- **Answers are unstable.** In the largest public study Mani cites (Steady Demand, August 2026, 14,472 citations from 1,487 local searches across 50 US cities, reported by MarTech), Gemini named the same top business about 7% of the time when asked again, against about 90% for Google's local pack. ChatGPT and Gemini recommended the same top business 4.2% of the time. US market; the pattern is what matters. (Published study.)
- **Each engine needs measuring on its own.** Same study: the engines rarely agree. (Published study.)
- **Business websites are cited heavily.** Same study: nearly 60% of Gemini's citations were business websites, with Reddit second at 13.7%. So the business's own site counts, and so do forums. (Published study, Gemini only.)
- **Different assistants lean on different things.** Google's AI features draw on Google's own index and Business Profile data. Other assistants lean on web search results and the directories, review sites and articles those results point to. (Mani's working model.)
- **The businesses named most aren't always the best ranked in Maps.** They're the easiest to describe with confidence. (Mani's observation from client work, being tested in his research; say so if you use it.)
- **What decides whether a business is named**, in Mani's working model: whether it's findable in the sources the assistant uses for that kind of question; whether those sources agree about what it is, what it does and where; and whether there's a reason to pick it (reviews that describe the service, a specialism, something other sites repeat).

Don't add figures beyond these. If the user asks for a stat you don't have, say there isn't good public data yet.

## How to measure

The same idea as a geo-grid: a pattern from many readings, not one reading.

- **Same prompts, several runs, each assistant.** 3 runs per prompt per assistant is Mani's working minimum for a by-hand check; more is better, because answers vary run to run. Fresh chat each time, so earlier answers don't carry over.
- **Mention rate** = runs naming the business / runs, per assistant. Never pooled across assistants, because they draw on different sources and a pooled rate hides which one to fix.
- **Who is named instead**: every business named, counted the same way. The one named in most runs is the benchmark.
- **Sources**: every link or source the answers show, counted by domain. Where an assistant shows none, note "no sources shown".
- **By prompt**: a business can be named for one need and absent for another it also serves (named for weddings, absent for corporate events). That points at a specific gap: nothing outside its own site connects it with that need.

## Reading the numbers

| Pattern | What it usually means |
|---|---|
| Named in under half the runs, a competitor in most | The core finding. Compare the sources and the descriptions. |
| Named by Gemini or AI Overviews, rarely by ChatGPT or Perplexity | Google's own data (profile, index) is working; the third-party sources the others lean on don't carry the business. Source gaps first. |
| Named by ChatGPT or Perplexity, not by Google's AI | Look at the Business Profile and the site's indexing and relevance: the lower rungs. |
| Named for one prompt, absent for others | The site and sources don't connect the business with those services or needs. Quotable facts and service pages. |
| Never named anywhere | Check the lower rungs before anything else. |
| Named, but described wrongly (old address, wrong services) | Consistency. Fix the sources the answers lean on. |
| One run in three different from the others | Noise. Don't act on it. |

Report a change between months only when it's bigger than one run per prompt and holds across more than one prompt (Mani's working rule of thumb), because smaller moves are within run-to-run noise.

## Visits from assistants

GA4 shows some visits from assistants (SearchOps `get_analytics_ai_referrals`, or a referral report filtered to chatgpt.com, gemini.google.com, perplexity.ai, copilot.microsoft.com and similar). It's a floor, not a total: some assistants pass no referrer, and Google's AI Overviews count as ordinary organic search. Useful as a trend, never as proof that visibility changed.

## Don't prioritise these

- **Chasing one screenshot.** A client or owner seeing a competitor named once proves nothing.
- **"LLM-only" pages.** Pages written for assistants rather than customers. Plain, quotable copy for customers serves both.
- **Programmatic location pages.** They give assistants nothing worth quoting.
- **Special files or markup sold as an AI fix.** There's no good evidence any single file or tag gets a local business named. Clear facts on real pages, and other sources agreeing, are the work.
- **Gaming forums.** Planted posts get spotted and removed and damage trust. Take part as the business, openly, where it's genuinely useful.
