# Example: connecting data for a fictional heating engineer

Example Heating, Leeds, does not exist. The configs, answers and tool results here are made up to show the skill working. The config files contain placeholder values marked FAKE; none are real keys.

Files:
- `user-request.md`: what the user said, and their answers to the skill's questions.
- `fake-home/.claude.json` and `project/.mcp.json`: the fictional Claude Code config the skill found.
- `check_env-output.md`: the real output of `check_env.py` run on those files, with two fictional environment variables set.
- `output.md`: the skill's reply, from detection to verification. Tool results in it are fictional.
- `local-seo-brief.md`: the brief the skill wrote, with the Data available section filled in.

To reproduce the script output (bash, from this folder):

```
S=../../plugins/local-seo/skills/local-seo-connect/scripts
env -i PATH="$PATH" DATAFORSEO_USERNAME=x DATAFORSEO_PASSWORD=x python $S/check_env.py --home fake-home --project project
```

`env -i` clears your real environment so the script reads only the fictional setup. Without `--home`, it reads your own machine's config.
