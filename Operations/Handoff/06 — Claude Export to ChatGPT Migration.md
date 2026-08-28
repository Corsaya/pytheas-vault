---
title: Claude Export to ChatGPT Migration
date: 2026-08-25
updated: 2026-08-25
tags: [handoff, migration, claude, chatgpt, memory]
status: local archive complete — ChatGPT memory seed pending review
---

# Claude Export to ChatGPT Migration

## Source

Manifest received at:

`~/Downloads/manifest-788e337c-0fc9-4da0-9b09-dda5ab28f522-1787710159-7c700fd0-2026-08-26-02-09-59.json`

The manifest identifies four one-use ZIP archives:

1. `light_metadata-000.zip`
2. `projects-000.zip`
3. `memories-000.zip`
4. `conversations-000.zip`

Direct command-line downloads returned HTTP 403 because Claude required an
authenticated browser session. The four archives were subsequently downloaded
through the browser and processed locally.

## Completed local migration

- Verified all four ZIP archives successfully.
- Parsed **417 conversations and 5,874 messages**, dated 2025-10-14 through
  2026-08-26.
- Converted conversations to Markdown under
  `learning/ai-improvement/Conversations/Claude Export/`.
- Confirmed the searchable archive is ignored by Git.
- Detected private-key, API-key, and password/secret-shaped content and redacted
  it from the searchable Markdown copy.
- Stored the complete raw JSON outside Obsidian at
  `~/.local/share/claude-export-20260825/` with owner-only permissions.
- Added a tracked review at
  `learning/ai-improvement/Memory-Export/Claude Memory Candidate Review.md`.

## Migration target

There is no assumed one-click Claude-to-ChatGPT account migration. Treat the
export as portable source material with three destinations:

| Source data | Destination | Purpose |
|---|---|---|
| Projects and project instructions | Pytheas vault project/handoff notes | Durable, reviewable operating context |
| Explicit Claude memories | A reviewed memory summary | Candidate ChatGPT memories and Codex context; do not import blindly |
| Conversations | Local archive under `learning/ai-improvement/Conversations/Claude Export/` | Searchable historical record; local-only under the standing privacy rule |
| High-value decisions and lessons | Existing `Key Decisions.md`, `Gotchas.md`, and project maps | Active knowledge rather than buried transcripts |

## Procedure used

1. Verified archive integrity and inventoried filenames without publishing content.
2. Extracted into a temporary directory, not directly into a vault.
3. Detected secrets and credentials before enabling searchable copies.
4. Converted conversations to stable Markdown with source IDs and timestamps.
5. Kept raw conversations local-only and outside every Git repository.
6. Produced a human-reviewable memory candidate list instead of asking ChatGPT
   to remember the entire export.
7. Deferred promotion of durable facts until the candidate review is accepted.

## ChatGPT limitation

OpenAI's documented account-transfer workaround accepts exported ChatGPT
conversation JSON as a reference file in a new conversation, but it does not
recreate individual chats, settings, or memories. A Claude export uses a
different schema, so it must be normalized and reviewed before being used as
reference material.
