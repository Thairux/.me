# Copilot MCP Plan

## Objective

Resume MCP troubleshooting from the exported Copilot session, verify why `portfolioSite` and `figma` fail to connect, and apply the smallest safe fix needed to make the working servers connect reliably.

## Current State

- The repository already contains a local MCP server at `mcp/portfolio_site_mcp_server.py` plus setup docs under `docs/`.
- The exported Copilot session shows repeated false-positive success messages followed by real runtime failures for both `figma` and `portfolioSite` after `/mcp reload`.
- The user-level Copilot config at `C:\Users\ptmth\.copilot\mcp-config.json` currently defines `googleStitch`, `figma`, and `portfolioSite`; `portfolioSite` now launches with `python3` on Windows.
- Git status is dirty with existing user work in `README.md`, `.github/`, `docs/`, `mcp/`, and the exported session file, so changes must stay scoped.

## Step-by-Step Plan

1. Inspect the resumed session, current MCP config, and available logs to avoid repeating the prior mistaken diagnosis.
2. Test the local `portfolioSite` server command and perform a direct MCP initialize and tools-list handshake.
3. Test the HTTP MCP endpoints for `figma` and `googleStitch` to identify whether failures come from auth, account tier, or transport.
4. Fix any confirmed local configuration issue, especially Windows command/runtime problems, without touching unrelated user settings.
5. Report the verified root causes, what changed, and what the user should run next in Copilot CLI.

## Assumptions And Risks

- GitHub Copilot CLI still reads MCP server definitions from `C:\Users\ptmth\.copilot\mcp-config.json`.
- A Windows `python3` launcher mismatch is a likely cause of the local server red X, but this must be verified before editing config.
- HTTP MCP endpoints may reject plain `GET` checks, so protocol-aware probing or log evidence may be needed before concluding a token is bad.
- Existing user MCP servers and secrets must be preserved; no destructive git or config cleanup is allowed.

## Success Criteria

- `portfolioSite` is verified with a successful local MCP handshake and a valid command in the Copilot config.
- `figma` and `googleStitch` have evidence-backed status notes instead of guesses.
- Any change made to config or code is minimal, scoped, and documented here.
- The user gets exact next commands to verify the servers in Copilot CLI.
