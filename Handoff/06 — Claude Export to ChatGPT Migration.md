---
title: Claude Export to ChatGPT Migration
date: 2026-08-25
updated: 2026-08-25
tags: [handoff, migration, claude, chatgpt, memory]
status: blocked — export archives require authenticated browser download
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

Direct command-line downloads returned HTTP 403 because Claude requires an
authenticated browser session. Download each archive from Claude while signed
in and place it in `~/Downloads/` before continuing.

## Migration target

There is no assumed one-click Claude-to-ChatGPT account migration. Treat the
export as portable source material with three destinations:

| Source data | Destination | Purpose |
|---|---|---|
| Projects and project instructions | Pytheas vault project/handoff notes | Durable, reviewable operating context |
| Explicit Claude memories | A reviewed memory summary | Candidate ChatGPT memories and Codex context; do not import blindly |
| Conversations | Local archive under `learning/ai-improvement/Conversations/Claude Export/` | Searchable historical record; local-only under the standing privacy rule |
| High-value decisions and lessons | Existing `Key Decisions.md`, `Gotchas.md`, and project maps | Active knowledge rather than buried transcripts |

## Procedure after the ZIPs arrive

1. Verify archive integrity and inventory filenames without publishing content.
2. Extract into a temporary directory, not directly into a vault.
3. Detect secrets, credentials, private attachments, and duplicate material.
4. Convert conversations to stable Markdown with source IDs and timestamps.
5. Keep raw conversations local-only; do not add them to Git.
6. Produce a short, human-reviewable memory candidate list rather than asking
   ChatGPT to remember the entire export.
7. Copy only approved durable facts into active context documents.

## ChatGPT limitation

OpenAI's documented account-transfer workaround accepts exported ChatGPT
conversation JSON as a reference file in a new conversation, but it does not
recreate individual chats, settings, or memories. A Claude export uses a
different schema, so it must be normalized and reviewed before being used as
reference material.
