#!/usr/bin/env python3
"""Export user/assistant messages from a Codex rollout JSONL to Markdown.

Hidden instructions, reasoning blocks, tool calls, and tool output are excluded.
The script is intentionally narrow so the `finito` workflow can archive the
visible conversation without copying internal execution data into Obsidian.
"""

from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path


def text_blocks(content: object) -> str:
    if not isinstance(content, list):
        return ""
    parts: list[str] = []
    for block in content:
        if not isinstance(block, dict):
            continue
        if block.get("type") in {"input_text", "output_text", "text"}:
            value = block.get("text")
            if isinstance(value, str) and value.strip():
                parts.append(value.strip())
    return "\n\n".join(parts)


def export(source: Path, destination: Path, title: str) -> int:
    messages: list[tuple[str, str]] = []
    with source.open(encoding="utf-8") as handle:
        for line in handle:
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                continue
            if item.get("type") != "response_item":
                continue
            payload = item.get("payload") or {}
            if payload.get("type") != "message":
                continue
            role = payload.get("role")
            if role not in {"user", "assistant"}:
                continue
            text = text_blocks(payload.get("content"))
            if text:
                messages.append((role, text))

    destination.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().astimezone().isoformat(timespec="seconds")
    lines = [
        "---",
        f'title: "{title.replace(chr(34), chr(39))}"',
        f"date: {stamp[:10]}",
        "tags: [conversation, codex, chiron, devices, roadmap]",
        "source: Codex rollout transcript",
        "scope: visible user and assistant messages only",
        "excludes: hidden instructions, internal reasoning, tool calls, tool output",
        "---",
        "",
        f"# {title}",
        "",
        f"Exported: {stamp}",
        "",
        "> This is a mechanical export of visible user and assistant messages from",
        "> the local Codex rollout. Environment-context wrappers are retained when",
        "> they were stored as visible user messages.",
        "",
    ]
    for role, message in messages:
        lines.extend((f"## {'Donovan' if role == 'user' else 'Codex'}", "", message, ""))
    destination.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    return len(messages)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("--title", required=True)
    args = parser.parse_args()
    count = export(args.source, args.destination, args.title)
    print(f"exported {count} visible messages to {args.destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
