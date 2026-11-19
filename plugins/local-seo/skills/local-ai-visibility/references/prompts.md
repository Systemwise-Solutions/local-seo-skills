# Building the prompt set

## What goes in it

5 to 10 prompts, the way a customer would type or say them to an assistant. Build them from the brief:

- **Money searches as questions.** "emergency plumber" becomes "who's a good emergency plumber in Leeds?" and "best emergency plumber near Chapel Allerton".
- **The area, three ways.** The town or city, the neighbourhood, and a landmark or "near me" style ("near Clifton Down"). Assistants handle each differently.
- **The reason people choose.** "physio for a running injury", "dentist for nervous patients", "solicitor for a quick house sale". This is where specialists win or lose.
- **One comparison.** "<business> or <top competitor>, which is better for <service>?" Shows how the assistant describes both.
- **One branded check.** "What do you know about <business> in <area>?" Shows whether the facts it holds are right.

Keep the set the same between months. Change it only when the business changes what it sells; note the change in the report.

For several locations, use the same prompt set per location with the area swapped, and start with 3 locations (strongest, weakest, typical).

## Which assistants

Ask which ones customers use. Default: ChatGPT, Gemini, Google AI Overviews (in normal Google results) and Google AI Mode. Add Perplexity and Copilot if the customers are likely to use them (often true for professional and B2B services). Don't make the user run more than they will actually keep doing.

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

Location matters: assistants use the user's location for "near me" prompts. Ask them to run the checks from inside the area the business serves, or to name the area in every prompt.

## The runs file

Top of `runs.txt`, before the first run:

```
business: <name> | <other names it goes by> | <website domain>
competitor: <name> | <domain if known>
```

Add a competitor line for each business named in more than one run. The script lists names it found that aren't on the list.
