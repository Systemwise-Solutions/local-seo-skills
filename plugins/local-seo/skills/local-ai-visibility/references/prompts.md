# Building the prompt set

## What goes in it

5 to 10 prompts, the way a customer would type or say them to an assistant (Mani's working range: enough to see which needs the business is missing on, few enough that the user keeps running them monthly). Build them from the brief:

- **Money searches as questions**, because people ask assistants in sentences, not keywords. "<service> <town>" becomes "who's good for <service> in <town>?" and "best <service> near <neighbourhood>".
- **The area, the ways people say it.** For a business people visit: the town, the neighbourhood, and a landmark or "near me" style. For a business that travels: the towns and districts it covers. Assistants handle each differently.
- **The reason people choose.** The need or situation behind the search ("a venue for 80 guests with parking", "an accountant who knows small limited companies", "a groomer for a nervous dog"). This is where specialists win or lose, so take it from what reviews and the site say customers value.
- **One comparison.** "<business> or <top competitor>, which is better for <need>?" Shows how the assistant describes both.
- **One branded check.** "What do you know about <business> in <area>?" Shows whether the facts it holds are right.

Keep the set the same between months, because a changed prompt makes the comparison meaningless. Change it only when the business changes what it offers, and note the change in the report and the log.

For several locations, use the same prompt set per location with the area swapped, and start with three (strongest, weakest, typical), because repeated faults show up in a sample.

## Which assistants

Ask which ones customers use, or read GA4 referral sources if connected. Default: ChatGPT, Gemini, Google AI Overviews (in normal Google results) and Google AI Mode. Add Perplexity and Copilot where the customers are likely to use them (work-related purchases, customers who research at a desk). Don't ask the user to run more than they will keep doing, because a baseline nobody repeats is wasted.

## The copy-paste block for the user

Give them this, filled in. Keep it short; they'll do it on their phone or laptop.

```
How to run the AI check (about 20 minutes per assistant)

For each assistant: ChatGPT, Gemini, <others>
- Open a new chat for every run. If you can, sign out or turn memory off, so past chats don't affect the answer.
- Paste prompt 1. Copy the whole answer. Then open a new chat and do it again, 3 times in total.
- Repeat for each prompt.
- For Google AI Overviews: search each prompt on Google 3 times (private window), and copy the AI Overview if one shows. If none shows, write "no AI Overview".

Prompts:
1. <prompt>
2. <prompt>
...

Paste everything back in this format. One block per run. Keep the links the answer shows.

=== ChatGPT | <prompt 1>
<the whole answer>
Sources: <links or site names the answer showed, or "none shown">

=== ChatGPT | <prompt 1>
<second run>
...
```

If they paste in a different shape, convert it to this format yourself before running the script, and keep their text unchanged.

Location matters: assistants use the user's location for "near me" prompts. Ask them to run the checks from inside the area the business serves, or to name the area in every prompt, because otherwise the answers describe somewhere else.

## The runs file

Top of `runs.txt`, before the first run:

```
business: <name> | <other names it goes by> | <website domain>
competitor: <name> | <domain if known>
```

Add a competitor line for each business named in more than one run. The script lists names it found that aren't on the list.
