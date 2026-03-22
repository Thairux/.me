# Workflows

## Local Development

1. Install Ruby and Bundler.
2. Install project gems.
3. Serve or build the Jekyll site.

```bash
bundle install
bundle exec jekyll serve
bundle exec jekyll build
```

## Copilot CLI Setup

Install the repository MCP entry into your local Copilot CLI config:

```bash
python mcp/install_copilot_mcp.py
```

This updates `~/.copilot/mcp-config.json` and adds the `portfolioSite` server while preserving existing MCP entries.

## Copilot Content Editing Flow

1. Start Copilot CLI in the repository root.
2. Ask Copilot to inspect the portfolio content map.
3. Let Copilot use the `portfolioSite` MCP tools for content work.
4. Review the diff after each change.
5. Run a build before pushing when Bundler is available.

```text
Review this portfolio and use the portfolioSite MCP server to update the homepage intro and add a new project case study.
```

## Verification

Use the MCP build tool or run the command directly:

```bash
bundle exec jekyll build
```

If Bundler is unavailable, install it first and rerun the build.

## Troubleshooting

- If Copilot does not see the MCP server, restart Copilot CLI after running `python mcp/install_copilot_mcp.py`.
- If the build fails because `bundle` is missing, install Ruby and Bundler, then run `bundle install`.
- If a content file is rejected by the MCP server, make sure the path is one of the allowed targets in `docs/integrations.md`.
