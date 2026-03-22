#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PROTOCOL_VERSION = "2024-11-05"
SERVER_NAME = "portfolio-site-mcp"
SERVER_VERSION = "0.1.0"

PAGE_PATHS = {
    "home": "index.md",
    "about": "about.md",
    "projects": "projects.md",
    "blog": "blog/index.md",
}


class MCPError(Exception):
    def __init__(self, code: int, message: str, data: Any | None = None) -> None:
        super().__init__(message)
        self.code = code
        self.message = message
        self.data = data


def load_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo", required=True, help="Absolute path to the portfolio repository"
    )
    return parser.parse_args()


def read_message() -> dict[str, Any] | None:
    headers: dict[str, str] = {}
    while True:
        line = sys.stdin.buffer.readline()
        if not line:
            return None
        if line in (b"\r\n", b"\n"):
            break
        header = line.decode("utf-8").strip()
        if not header:
            break
        name, value = header.split(":", 1)
        headers[name.strip().lower()] = value.strip()

    content_length = headers.get("content-length")
    if not content_length:
        raise MCPError(-32700, "Missing Content-Length header")

    body = sys.stdin.buffer.read(int(content_length))
    if not body:
        return None
    return json.loads(body.decode("utf-8"))


def send_message(payload: dict[str, Any]) -> None:
    body = json.dumps(payload, ensure_ascii=True).encode("utf-8")
    sys.stdout.buffer.write(f"Content-Length: {len(body)}\r\n\r\n".encode("ascii"))
    sys.stdout.buffer.write(body)
    sys.stdout.buffer.flush()


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def yaml_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if value is None:
        return '""'
    if isinstance(value, str):
        if re.fullmatch(r"[A-Za-z0-9_./:+-]+", value):
            return value
        return yaml_quote(value)
    raise MCPError(-32602, f"Unsupported scalar type: {type(value).__name__}")


def dump_frontmatter(frontmatter: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in frontmatter.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {yaml_scalar(item)}")
        else:
            lines.append(f"{key}: {yaml_scalar(value)}")
    lines.append("---")
    return "\n".join(lines)


def parse_frontmatter(text: str) -> tuple[OrderedDict[str, Any], str]:
    if not text.startswith("---\n"):
        return OrderedDict(), text

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return OrderedDict(), text

    raw_frontmatter = parts[0].splitlines()[1:]
    body = parts[1]
    data: OrderedDict[str, Any] = OrderedDict()
    current_list_key: str | None = None

    for line in raw_frontmatter:
        if not line.strip():
            continue
        if line.startswith("  - ") and current_list_key:
            data.setdefault(current_list_key, [])
            data[current_list_key].append(parse_scalar(line[4:].strip()))
            continue
        current_list_key = None
        if ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        value = raw_value.strip()
        if value == "":
            current_list_key = key
            data[key] = []
        else:
            data[key] = parse_scalar(value)

    return data, body


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        return value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    if value in {"true", "false"}:
        return value == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


class PortfolioSiteServer:
    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root.resolve()

    def run(self) -> None:
        while True:
            message = read_message()
            if message is None:
                return
            if "method" not in message:
                continue

            method = message["method"]
            message_id = message.get("id")
            params = message.get("params", {})

            if method == "notifications/initialized":
                continue

            try:
                if method == "initialize":
                    result = self.initialize(params)
                elif method == "tools/list":
                    result = {"tools": self.list_tools()}
                elif method == "tools/call":
                    result = self.call_tool(params)
                elif method == "ping":
                    result = {}
                else:
                    raise MCPError(-32601, f"Method not found: {method}")

                if message_id is not None:
                    send_message({"jsonrpc": "2.0", "id": message_id, "result": result})
            except MCPError as error:
                if message_id is not None:
                    payload: dict[str, Any] = {
                        "jsonrpc": "2.0",
                        "id": message_id,
                        "error": {"code": error.code, "message": error.message},
                    }
                    if error.data is not None:
                        payload["error"]["data"] = error.data
                    send_message(payload)

    def initialize(self, params: dict[str, Any]) -> dict[str, Any]:
        client_version = params.get("protocolVersion")
        if client_version and client_version != PROTOCOL_VERSION:
            pass
        return {
            "protocolVersion": PROTOCOL_VERSION,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        }

    def list_tools(self) -> list[dict[str, Any]]:
        return [
            {
                "name": "get_site_content_map",
                "description": "Show editable portfolio content locations and conventions.",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False,
                },
            },
            {
                "name": "list_content_files",
                "description": "List editable page, project, and post content files.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "kind": {
                            "type": "string",
                            "enum": ["all", "pages", "projects", "posts"],
                            "default": "all",
                        }
                    },
                    "additionalProperties": False,
                },
            },
            {
                "name": "get_content_file",
                "description": "Read a portfolio content file with parsed frontmatter.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "relative_path": {"type": "string"},
                    },
                    "required": ["relative_path"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "write_content_file",
                "description": "Create or update an allowed portfolio content file.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "relative_path": {"type": "string"},
                        "frontmatter": {"type": "object"},
                        "body": {"type": "string"},
                    },
                    "required": ["relative_path", "frontmatter", "body"],
                    "additionalProperties": False,
                },
            },
            {
                "name": "build_site",
                "description": "Run `bundle exec jekyll build` in the portfolio repository.",
                "inputSchema": {
                    "type": "object",
                    "properties": {},
                    "additionalProperties": False,
                },
            },
        ]

    def call_tool(self, params: dict[str, Any]) -> dict[str, Any]:
        name = params.get("name")
        arguments = params.get("arguments", {})

        handlers = {
            "get_site_content_map": self.tool_get_site_content_map,
            "list_content_files": self.tool_list_content_files,
            "get_content_file": self.tool_get_content_file,
            "write_content_file": self.tool_write_content_file,
            "build_site": self.tool_build_site,
        }
        if name not in handlers:
            raise MCPError(-32601, f"Unknown tool: {name}")

        text = handlers[name](arguments)
        return {"content": [{"type": "text", "text": text}]}

    def tool_get_site_content_map(self, _: dict[str, Any]) -> str:
        payload = {
            "repo_root": str(self.repo_root),
            "editable_pages": PAGE_PATHS,
            "editable_patterns": [
                "_projects/*.md",
                "_posts/YYYY-MM-DD-slug.md",
            ],
            "page_defaults": {
                "index.md": {"layout": "default", "title": "Home"},
                "about.md": {
                    "layout": "default",
                    "title": "About",
                    "permalink": "/about/",
                },
                "projects.md": {
                    "layout": "default",
                    "title": "Projects",
                    "permalink": "/projects/",
                },
                "blog/index.md": {
                    "layout": "default",
                    "title": "Blog",
                    "permalink": "/blog/",
                },
            },
            "project_required_frontmatter": ["layout", "title", "description"],
            "post_required_frontmatter": ["layout", "title", "date"],
            "notes": [
                "This server is intentionally limited to site content files, not layouts, CSS, JS, or arbitrary files.",
                "Use get_content_file before write_content_file when updating an existing page so structure is preserved.",
            ],
        }
        return json.dumps(payload, indent=2)

    def tool_list_content_files(self, arguments: dict[str, Any]) -> str:
        kind = arguments.get("kind", "all")
        if kind not in {"all", "pages", "projects", "posts"}:
            raise MCPError(-32602, "kind must be one of: all, pages, projects, posts")

        result: dict[str, Any] = {}
        if kind in {"all", "pages"}:
            result["pages"] = [
                self.describe_file(Path(path)) for path in PAGE_PATHS.values()
            ]
        if kind in {"all", "projects"}:
            result["projects"] = [
                self.describe_file(path)
                for path in sorted((self.repo_root / "_projects").glob("*.md"))
            ]
        if kind in {"all", "posts"}:
            result["posts"] = [
                self.describe_file(path)
                for path in sorted((self.repo_root / "_posts").glob("*.md"))
            ]
        return json.dumps(result, indent=2)

    def tool_get_content_file(self, arguments: dict[str, Any]) -> str:
        relative_path = arguments.get("relative_path")
        if not isinstance(relative_path, str) or not relative_path:
            raise MCPError(-32602, "relative_path is required")

        file_path = self.resolve_content_path(relative_path)
        if not file_path.exists():
            raise MCPError(-32602, f"Content file does not exist: {relative_path}")

        text = file_path.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(text)
        payload = {
            "relative_path": self.to_relative(file_path),
            "frontmatter": frontmatter,
            "body": body,
        }
        return json.dumps(payload, indent=2)

    def tool_write_content_file(self, arguments: dict[str, Any]) -> str:
        relative_path = arguments.get("relative_path")
        frontmatter = arguments.get("frontmatter")
        body = arguments.get("body")

        if not isinstance(relative_path, str) or not relative_path:
            raise MCPError(-32602, "relative_path is required")
        if not isinstance(frontmatter, dict):
            raise MCPError(-32602, "frontmatter must be an object")
        if not isinstance(body, str):
            raise MCPError(-32602, "body must be a string")

        file_path = self.resolve_content_path(relative_path)
        normalized_frontmatter = self.normalize_frontmatter(file_path, frontmatter)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        output = (
            dump_frontmatter(normalized_frontmatter) + "\n\n" + body.rstrip() + "\n"
        )
        file_path.write_text(output, encoding="utf-8", newline="\n")

        payload = {
            "status": "written",
            "relative_path": self.to_relative(file_path),
            "frontmatter": normalized_frontmatter,
        }
        return json.dumps(payload, indent=2)

    def tool_build_site(self, _: dict[str, Any]) -> str:
        try:
            result = subprocess.run(
                ["bundle", "exec", "jekyll", "build"],
                cwd=self.repo_root,
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            return json.dumps(
                {
                    "ok": False,
                    "command": "bundle exec jekyll build",
                    "message": "Bundler is not installed or not available on PATH.",
                },
                indent=2,
            )

        payload = {
            "ok": result.returncode == 0,
            "command": "bundle exec jekyll build",
            "returncode": result.returncode,
            "stdout": result.stdout[-4000:],
            "stderr": result.stderr[-4000:],
        }
        return json.dumps(payload, indent=2)

    def describe_file(self, path: Path) -> dict[str, Any]:
        file_path = path if path.is_absolute() else self.repo_root / path
        if not file_path.exists():
            return {"relative_path": self.to_relative(file_path), "exists": False}

        frontmatter, _ = parse_frontmatter(file_path.read_text(encoding="utf-8"))
        summary = {
            "relative_path": self.to_relative(file_path),
            "exists": True,
        }
        for key in ("title", "description", "date", "order"):
            if key in frontmatter:
                summary[key] = frontmatter[key]
        return summary

    def resolve_content_path(self, relative_path: str) -> Path:
        relative_path = relative_path.replace("\\", "/")
        candidate = (self.repo_root / relative_path).resolve()
        try:
            candidate.relative_to(self.repo_root)
        except ValueError as exc:
            raise MCPError(-32602, "Path must stay within the repository") from exc

        normalized = self.to_relative(candidate)
        if normalized in PAGE_PATHS.values():
            return candidate
        if normalized.startswith("_projects/") and normalized.endswith(".md"):
            return candidate
        if normalized.startswith("_posts/") and normalized.endswith(".md"):
            filename = candidate.name
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}-[a-z0-9-]+\.md", filename):
                raise MCPError(
                    -32602, "Post filenames must look like YYYY-MM-DD-slug.md"
                )
            return candidate
        raise MCPError(
            -32602, f"Path is not an allowed content target: {relative_path}"
        )

    def normalize_frontmatter(
        self, file_path: Path, frontmatter: dict[str, Any]
    ) -> OrderedDict[str, Any]:
        relative_path = self.to_relative(file_path)
        data = OrderedDict()
        incoming = OrderedDict(frontmatter)

        if relative_path in PAGE_PATHS.values():
            defaults = {
                "index.md": OrderedDict([("layout", "default"), ("title", "Home")]),
                "about.md": OrderedDict(
                    [
                        ("layout", "default"),
                        ("title", "About"),
                        ("permalink", "/about/"),
                    ]
                ),
                "projects.md": OrderedDict(
                    [
                        ("layout", "default"),
                        ("title", "Projects"),
                        ("permalink", "/projects/"),
                    ]
                ),
                "blog/index.md": OrderedDict(
                    [("layout", "default"), ("title", "Blog"), ("permalink", "/blog/")]
                ),
            }[relative_path]
            for key, value in defaults.items():
                data[key] = incoming.pop(key, value)
        elif relative_path.startswith("_projects/"):
            title = incoming.get("title")
            description = incoming.get("description")
            if not title or not description:
                raise MCPError(
                    -32602,
                    "Projects require frontmatter.title and frontmatter.description",
                )
            data["layout"] = incoming.pop("layout", "project")
            data["title"] = incoming.pop("title")
            data["description"] = incoming.pop("description")
        elif relative_path.startswith("_posts/"):
            title = incoming.get("title")
            if not title:
                raise MCPError(-32602, "Posts require frontmatter.title")
            filename_date = file_path.name[:10]
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", filename_date):
                raise MCPError(-32602, "Post filename must begin with YYYY-MM-DD")
            data["layout"] = incoming.pop("layout", "post")
            data["title"] = incoming.pop("title")
            data["date"] = incoming.pop(
                "date",
                f"{filename_date} {datetime.now(timezone.utc).strftime('%H:%M:%S')} +0000",
            )
            if "author" in incoming:
                data["author"] = incoming.pop("author")
            if "permalink" in incoming:
                data["permalink"] = incoming.pop("permalink")

        for key, value in incoming.items():
            self.validate_frontmatter_value(key, value)
            data[key] = value

        for key, value in data.items():
            self.validate_frontmatter_value(key, value)
        return data

    def validate_frontmatter_value(self, key: str, value: Any) -> None:
        if not re.fullmatch(r"[A-Za-z0-9_-]+", key):
            raise MCPError(-32602, f"Invalid frontmatter key: {key}")
        if isinstance(value, list):
            for item in value:
                if not isinstance(item, (str, int, bool)):
                    raise MCPError(-32602, f"Unsupported list item type for {key}")
            return
        if not isinstance(value, (str, int, bool)) and value is not None:
            raise MCPError(-32602, f"Unsupported frontmatter value type for {key}")

    def to_relative(self, path: Path) -> str:
        return path.resolve().relative_to(self.repo_root).as_posix()


def main() -> int:
    args = load_args()
    repo_root = Path(args.repo)
    if not repo_root.exists():
        raise SystemExit(f"Repository path does not exist: {repo_root}")
    PortfolioSiteServer(repo_root).run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
