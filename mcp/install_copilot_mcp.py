#!/usr/bin/env python3

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path


SERVER_NAME = "portfolioSite"
FIGMA_SERVER_NAME = "figma"
PORTFOLIO_SERVER_TIMEOUT_SECONDS = 16000


def build_server_config(repo_root: Path) -> dict[str, object]:
    server_path = repo_root / "mcp" / "portfolio_site_mcp_server.py"
    return {
        "type": "local",
        "command": "python",
        "timeout": PORTFOLIO_SERVER_TIMEOUT_SECONDS,
        "args": [str(server_path), "--repo", str(repo_root)],
    }


def build_figma_server_config() -> dict[str, object]:
    return {
        "type": "http",
        "url": "https://mcp.figma.com/mcp",
        "headers": {
            # Keep auth in env var to avoid writing secrets to disk.
            "Authorization": "Bearer ${FIGMA_OAUTH_TOKEN}",
            "X-Figma-Region": "us-east-1",
        },
    }


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    copilot_dir = Path.home() / ".copilot"
    copilot_dir.mkdir(parents=True, exist_ok=True)
    config_path = copilot_dir / "mcp-config.json"

    existing: dict[str, object] = {}
    if config_path.exists():
        existing = json.loads(config_path.read_text(encoding="utf-8"))
        backup_path = config_path.with_name(
            f"mcp-config.backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        )
        backup_path.write_text(json.dumps(existing, indent=2) + "\n", encoding="utf-8")

    existing.setdefault("servers", {})
    existing.setdefault("mcpServers", {})

    server_config = build_server_config(repo_root)
    figma_config = build_figma_server_config()
    existing["servers"][SERVER_NAME] = server_config
    existing["mcpServers"][SERVER_NAME] = server_config
    existing["servers"][FIGMA_SERVER_NAME] = figma_config
    existing["mcpServers"][FIGMA_SERVER_NAME] = figma_config

    config_path.write_text(json.dumps(existing, indent=2) + "\n", encoding="utf-8")
    print(config_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
