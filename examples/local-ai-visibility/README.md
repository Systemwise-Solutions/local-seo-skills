# Example: AI visibility for a fictional physio practice

Example Physio, Clifton, Bristol, does not exist. Nor do its competitors (Avonside Physio, Downs Movement Clinic, Physio Lane Clinic, Hotwells Back Care) or the sites ending `.example`. The answers in `runs.txt` were written to show the method working; they are not real assistant output. Real directory names (Doctify, Yell, Top Doctors, Reddit) appear only as source types, and nothing here says anything about how they treat any real business.

Files:
- `local-seo-brief.md`: the brief the skill wrote.
- `prompt-set.md`: the prompt set and the copy-paste block the skill gave the user.
- `source-check.md`: the skill's own web search source map (fictional results).
- `runs.txt`: the 30 runs the user pasted back (fictional), in the script's text format.
- `mention-rate-output.md`: the real output of `mention_rate.py` on `runs.txt`.
- `output.md`: the finished AI visibility write-up.

```
S=../../plugins/local-seo/skills/local-ai-visibility/scripts
python $S/mention_rate.py runs.txt
python $S/mention_rate.py runs.txt --json
```
