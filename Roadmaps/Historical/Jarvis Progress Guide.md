---
date: 2026-07-08
tags: [jarvis, guide, progress]
---

# Jarvis Progress Guide — building the ultimate assistant

Written by real Fable 5 during the 2026-07-08 build session, as both a status
map and the manual for continuing the build without Fable. Source of truth
for code state: `~/code/jarvis` (ARCHITECTURE.md + DECISIONS.md); this note
is the narrative layer.

## Where the build stands (2026-07-08)

**v1 is complete and beyond — 147/147 tests.** Every ARCHITECTURE.md
component exists, plus three things v1 didn't promise:

| Piece | State | Where |
|---|---|---|
| Config loader (fail-fast, secrets) | ✅ DEC-009/010 | `jarvis/config.py` |
| Memory (identity + facts, `/remember`) | ✅ DEC-006/007 | `jarvis/memory.py` |
| Prompt builder (system\|history\|input) | ✅ DEC-015 | `jarvis/prompt.py` |
| Session window (10 msgs, ephemeral) | ✅ DEC-018 | `jarvis/session.py` |
| Model router (tiers + overrides) | ✅ DEC-017 | `jarvis/llm/router.py` |
| Subprocess client (`claude -p`, subscription) | ✅ DEC-016 | `jarvis/llm/client.py` |
| **Api client (`llm.mode: api`, stdlib)** | ✅ **NEW** DEC-023 | `jarvis/llm/client.py` |
| Usage tracker + spend log for ccdash | ✅ DEC-019/021 | `jarvis/usage.py`, cli |
| CLI loop + meta-commands | ✅ DEC-020 | `jarvis/cli.py` |
| Self-improvement engine (propose→approve) | ✅ DEC-022, first live run pending | `jarvis/improve.py` |
| **Daily brief + weekly survey at startup** | ✅ **NEW** DEC-024 | `jarvis/briefing.py` |
| **repo-scout (find + safely adopt repos)** | ✅ **NEW**, own repo | `~/code/repo-scout` |
| ccdash (usage dashboard, **now with Fable gauge**) | ✅ | `~/code/usage-monitor` |
| Self-improvement playbook | ✅ | `~/code/jarvis/SELF-IMPROVEMENT.md` |

Verified live this session: a real `jarvis` startup wrote the weekly survey
(`Surveys/2026-W28.md`), attempted the news brief, hit the 5-hour session
cap, and degraded exactly as designed (one line, retry next launch). The
web-tools invocation was verified separately (needs `--allowedTools`, now a
Gotcha in CLAUDE.md).

**Not committed yet:** the jarvis repo changes await your review
(`git diff` in `~/code/jarvis`). repo-scout and ccdash are committed.

## Your queue (human-only items, highest leverage first)

1. **Fill `memory/identity.md`** — still blank; it's the first thing in every
   prompt and nobody else may write it. Use the interview kit
   (`ai-improvement/needs-wants-interview-kit.md`) + `donny-operating-system.md`.
2. **Review + commit the jarvis diff** (DEC-023, DEC-024, briefing, tests).
3. **Fire the first `jarvis improve` run** (spends full-tier; see
   SELF-IMPROVEMENT.md §3).
4. **Answer `Surveys/2026-W28.md`** — it steers next week's loop.

## How to keep building without Fable 5

The method that built everything above, in order:

1. **Plan at the top tier you have** (Fable while the gauge lasts, then Opus
   with the clone persona — `ai-improvement/capability-scouting/fable5-clone-persona-v2.md`).
   Output = a blueprint in `~/code/jarvis/blueprints/` using `_TEMPLATE.md`:
   exact files, exact steps, definition of done, ASSUMPTION escape hatch.
2. **Build with Sonnet** (or Haiku for mechanical work): fresh session, paste
   the one-line prompt inside the blueprint. The repo's CLAUDE.md forces the
   propose→approve protocol on it.
3. **Verify like this session did**: full test suite + one live smoke of the
   real flow, including the failure path.
4. **Record**: DEC entry, Gotchas line, session-wrap note. That's what makes
   session N+1 smarter than session N.

## Roadmap: from "CLI with memory" to "self-growing assistant"

**Phase A — close the loop (this month, cheap models can do all of it):**
weekly repo-scan automation in the Briefing component · first improve run ·
survey readback design (needs a DEC — it touches the no-Obsidian-reads rule).

**Phase B — memory that scales:** `memory/facts.md` flat-load is v1's known
limit. Build selective retrieval behind MemoryStore's load interface (the
DEC-007 seam) — recency window first, semantic search only if actually felt.

**Phase C — reach:** Obsidian read-only context injector (extension point in
prompt.py) · daemon/notification surface (extension point in cli layer) ·
voice via local TTS/STT if wanted.

**Phase D — graduation from Claude models:** the whole design converges here.
`LLMClient` (jarvis/llm/base.py) is the only provider contact point, so a
local-model client (Ollama) is one new class in one module + a config entry.
Router tiers then mix local (fast/free) with Claude (hard problems) until
local is good enough to take `standard`. Watch the `local llm assistant`
scan query; the identity/facts memory, the discipline docs, and the
self-improvement loop all transfer unchanged because none of them are
Claude-specific.

## Budget rules (why the gauges exist)

`ccdash --brief` now shows **5h · 7d · Fable** live. Fable is the scarce
resource: planning/blueprints only. When it's spent, the clone persona +
blueprints ARE the Fable substitute — that was the point of building them
while it lasted.
