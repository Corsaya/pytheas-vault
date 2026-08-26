---
tags: [project, pytheas, chiron, ai, home]
type: vault-index
updated: 2026-08-25
repos: ["~/code/pytheas", "~/code/chiron", "~/code/jarvis (design-only)"]
---

# Pytheas — Vault Home

Notes for **Pytheas**, Donovan's personal AI assistant, and **Chiron**, the
Odysseus fork that became its workspace shell. Source code lives outside the
vault; this vault holds the thinking, the roadmaps, the courses, and the
briefings.

**[[Pytheas and Chiron Project Map]]** is the canonical responsibility map for
the two codebases and their relationship to Obsidian and the planned database.

> [!important] Start here if you're new to this vault
> **[[Handoff/00 — START HERE|Handoff/]]** — written 2026-08-25 at the Claude
> Code → Codex migration. Identity/context doc, the senior-year workspace plan,
> the course plan, the migration checklist, and a vault cleanup audit.

## Where the code actually lives

| Repo | What it is | State |
|---|---|---|
| `~/code/pytheas` | The Pytheas desktop app (Python). `server.py`, `voice.py`, `courses.py`, `research.py`, `models.py`, `actions.py`, `briefing.py`, `chats.py`, `emailcal.py`, `permissions.py` | **Live and implemented** |
| `~/code/chiron` | Personal fork of Odysseus. Docker, port 7001, ingests all six vaults. Custom SAT classroom app built to Bluebook parity | **Live.** ⚠ No personal git remote — see [[Handoff/02 — AI Workspace Master Plan]] §1 |
| `~/code/jarvis` | The original terminal CLI. Fully architected, never implemented | **Design-only.** Historical |

## What lives in this vault

- **`Handoff/`** — the 2026-08-25 context transfer. Read `00 — START HERE` first.
- **`Courses/`** — course content. `SAT/` is the fully built one (8 crash
  courses, 2 full-length tests, diagnostic + gap system). Also `Basketball
  Rules`, `Pytheas Benchmark - SAT Test`.
- **`Briefings/`** — daily AI-news briefs, ISO-dated, written by
  `~/code/pytheas/briefing.py`.
- **`Prompts/`** — the prompt-logging convention. **Immutable — never edit
  these**, their value is being a true record of what was asked.
- **`Research/`**, **`Surveys/`** (weekly setup surveys), **`session-wraps/`**.

## The roadmaps, newest first

- **[[Handoff/02 — AI Workspace Master Plan]]** (2026-08-25) — **current.** The
  senior-year goal: own workspace + database by June 2027.
- **[[Ultimate Workspace Roadmap]]** (2026-08-02) — snapshot. Superseded in
  direction by the above, but its research (CalDAV decision, Notion ruled out)
  is still the reasoning of record.
- **[[Development Roadmap]]** (2026-07-29) — the four technical workstreams
  (Atlas, environment-context injection, vault-pyramid agents, Hermes). Still
  the live technical plan.
- **[[perfect-assistant-goals-2026-07-15]]** — the four capability goals and the
  "graduating from Claude" ladder.
- **[[capabilities-roadmap]]** · **[[jarvis-desk-app]]** · **[[Pytheas 2.0 Changelog]]**

## Historical

- **[[Summary]]** — a 2026-05-30 snapshot of the *Jarvis design phase*. Kept as
  an artifact; it does not describe the current system.

## Symlinks

- `code/` → `~/code` — the source repos
- `learning-vault/` → `~/Documents/Obsidian/learning`

> [!note] Access
> Full read/write across all six vaults by default since 2026-08-12. The old
> `personal-private` wall is retired. The one override is a doc Donovan marks
> **"locked"**. See `~/Documents/Obsidian/AGENTS.md`.
