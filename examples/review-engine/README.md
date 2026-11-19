# Example: a fictional physiotherapy clinic

Sector detail here is illustration only; the skill itself works from the lens in `references/loop.md`. Here the lens answers were: customers come to it, revenue is a booked course of appointments, and there are rules on what replies may confirm.

Example Physiotherapy, Didsbury, does not exist. Nor do its competitors or any reviewer. The data here is made up to show the skill and its scripts working.

```
S=../../plugins/local-seo/skills/review-engine/scripts
python $S/review_velocity.py reviews.json                                  # saved as velocity-output.md
python $S/review_tracker.py reviews-log.json --months 6 --confidential     # saved as tracker-output.md
```

- `local-seo-brief.md`: the brief the skill wrote while orienting.
- `reviews.json`: review counts and recent dates for the clinic and three competitors.
- `reviews-log.json`: the clinic's own reviews for six months, with text and replies, and `avoid_in_replies`: the phrases this clinic's reply rules rule out, on top of the built-in `--confidential` set.
- `sample-output.md`: the full output the skill wrote from this data.
