---
tags: [project, jarvis, ai, home]
type: scratchpad
repo: ~/code/jarvis/
---

# Jarvis — Scratchpad

Personal-vault notes for Jarvis, your terminal personal AI assistant. The design
docs and (eventual) source live in their own repo; this folder is for ideas,
wishlists, and how Jarvis should plug into the rest of the second brain.

> [!info] The code lives elsewhere (moved 2026-07-01)
> Architecture, decisions, and source now live in their own repo at
> **`~/code/jarvis/`** (moved out of the Obsidian vault per the repo-split plan).
> Keep this folder for cross-vault thinking — what you want Jarvis to know about
> *you*, and how it should read (read-only) from these Obsidian vaults.

## What lives here

- Feature wishlist and "wouldn't it be nice if…" notes
- Raw material for `memory/identity.md` (still blank in the repo)
- How Jarvis should surface vault context (v2 Obsidian integration is read-only)
- Build-order reminders and parking-lot ideas

## Symlinks (added 2026-07-05)

- `code/` → `~/code` — the actual jarvis source repo and sibling code projects
- `learning-vault/` → `~/Documents/Obsidian/learning` — the AI-accessible
  reference vault, for recent school/entertainment/Japanese context. Never
  points at `personal-private/` — that vault stays walled off from this one.

## The repo at a glance

- `README.md` — setup, meta-commands, project layout
- `ARCHITECTURE.md` — 9-component design, data flow, invariants, non-goals
- `DECISIONS.md` — DEC-001 → DEC-024, full rationale (011 subprocess, 012
  Fable 5, 016 subprocess client, 022 improve, 023 api client, 024 briefing)
- `CLAUDE.md` — working rules for Claude Code sessions
- `SELF-IMPROVEMENT.md` — the standing discover→evaluate→adopt→record loop
- `blueprints/` — build-ready specs for cheap models (Blueprint Vault run)
- `memory/identity.md` — injected every session; **still blank — fill this in**
- `memory/facts.md` — written by `/remember`

## This vault's map

- **[[Jarvis Progress Guide]]** — full build status + roadmap to graduation
- **[[jarvis-desk-app]]** — the native desktop workspace (Odysseus+ build,
  2026-07-16): what shipped, what's verified, what's next
- **[[perfect-assistant-goals-2026-07-15]]** — the four capability goals
  (self-improvement scan, parity, voice, laptop), Odysseus plan, own-model path
- **[[capabilities-roadmap]]** · **[[Summary]]** — earlier status notes
- `Surveys/` — auto-written weekly setup surveys (answer them; they steer the loop)
- `session-wraps/` — per-session status handoffs
