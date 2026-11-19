# Connecting in each environment

How a tool connects depends on where the user runs Claude. Checked against the linked docs in November 2026. Menus and commands change: if you can fetch pages, fetch the linked doc and follow it over this file.

## Contents
- Remote servers and local servers
- Claude app (web and desktop)
- Claude Code
- Cursor and other agents
- Keys and secrets

---

## Remote servers and local servers

- **Remote (a URL)**: the vendor hosts the server. You add its URL and sign in, or send a key in a header. Works in the Claude app, Claude Code and Cursor. SearchOps, Local Falcon, BrightLocal and DataForSEO all offer one.
- **Local (a command)**: the server runs on the user's computer, started with `npx`, `pipx` or similar. Works in Claude Code, Cursor and the Claude desktop app. Not in the Claude web app. Google's Analytics MCP and most Search Console MCPs are local.

If the user only uses the Claude web app, recommend remote servers only.

## Claude app (web and desktop)

Docs: https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp

**Directory connectors.** Some vendors are listed in Claude's connector directory (Local Falcon lists itself there, per localfalcon.com/features/mcp). Add from the directory, sign in to the vendor, allow. Easiest route where it exists.

**Custom connectors** (a remote URL). As of November 2026, Claude's help page says:
- Available on Free, Pro, Max, Team and Enterprise plans. **Free plans are limited to one custom connector.** So on Free, pick the one that answers their goal.
- Pro and Max: Customize > Connectors, then + Add, then Add custom connector. Paste the vendor's URL, Add, then Connect and sign in to the vendor.
- Team and Enterprise: an owner (or an Enterprise role with the right permission) adds the connector in Organization settings > Connectors; each member then connects it from Customize > Connectors. If the user isn't an owner or admin, they need to ask one.
- The server must be on the public internet on port 443.
- To change a connector's details, remove it and add it again.

Some vendor guides describe the menu as "Settings > Connectors". Claude's menus have been renamed before; follow Claude's help page for the path and the vendor's page for the URL.

**Local servers in the desktop app.** The desktop app can run local servers from its config file or from a one-click extension bundle where a vendor ships one (Local Falcon publishes an `.mcpb` bundle on its GitHub releases). Docs: https://modelcontextprotocol.io/docs/develop/connect-local-servers. This needs the user to install the runtime (Node.js or Python) first. Only recommend it for Google Analytics or Search Console when they won't use Claude Code.

**After connecting:** start a new chat. Check the connector is switched on for that chat (the tools menu in the message box).

## Claude Code

Docs: https://code.claude.com/docs/en/mcp

Remote server, sign-in:
```bash
claude mcp add --transport http <name> <vendor URL>
```
Then inside Claude Code run `/mcp` and choose Authenticate (or `claude mcp login <name>` from the shell).

Remote server, key in a header:
```bash
claude mcp add --transport http <name> <vendor URL> --header "Authorization: Bearer <key>"
```

Local server with environment variables:
```bash
claude mcp add --transport stdio --env NAME=value <name> -- <command> <args>
```
Put another option (such as `--transport stdio`) between `--env` and the server name, or the CLI reads the name as another variable.

Scopes (`--scope`): `local` (default, this project, only you), `user` (all your projects), `project` (writes `.mcp.json` into the repo, shared with anyone who clones it). **Never use project scope for a server whose command includes a key**, or the key ends up in version control. For a local SEO consultant working across clients, `user` scope is usually right.

Check: `claude mcp list` shows each server as connected, needs authentication, or failed. `claude mcp get <name>` shows one.

Windows: if an `npx` server fails to start, vendors' own guides wrap it in `cmd /c` (DataForSEO's Claude Code guide shows this). Follow the vendor's Windows instructions where given.

Servers added during a session may not appear until the user restarts Claude Code or reconnects with `/mcp`.

## Cursor and other agents

Cursor docs: https://cursor.com/docs/context/mcp

Cursor reads `~/.cursor/mcp.json` (all projects) or `.cursor/mcp.json` (one project). Remote server with a key:
```json
{ "mcpServers": { "<name>": { "url": "<vendor URL>", "headers": { "Authorization": "Bearer <key>" } } } }
```
Local server:
```json
{ "mcpServers": { "<name>": { "command": "<command>", "args": ["<args>"], "env": { "NAME": "value" } } } }
```

Other agents (VS Code, Windsurf, Gemini CLI, n8n and others): ask which one, fetch its MCP docs, and use the vendor's URL and auth. Most accept the same remote URL with a bearer token.

## Keys and secrets

- The user creates keys in the vendor's dashboard and types them into the command or config themselves. Never ask for one in chat. If one is pasted, tell them to revoke it and make a new one.
- Prefer sign-in where offered: nothing to leak.
- A key typed into a command lands in shell history. In bash or zsh they can set it as a variable first and reference it (`--header "Authorization: Bearer $VENDOR_KEY"`); in PowerShell, `$env:VENDOR_KEY`.
- Some vendors put the key in the URL (Local Falcon and BrightLocal both document this). It works, but anyone who sees the config sees the key. Prefer their sign-in or header option.
- Keep keys out of project-scoped files that go into git.
