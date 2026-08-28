---
title: START HERE — Handoff Index
date: 2026-08-25
tags: [handoff, index, codex, gpt-5.6]
status: historical handoff — post-handoff corrections below
---

# START HERE

Written 2026-08-25, the last day of the Claude Code subscription, as the handoff
to ChatGPT / Codex (GPT-5.6 "Sol").

> [!important] Post-handoff correction — 2026-08-27
> The system now has five vaults. `Corsaya/chiron` exists as a private remote,
> local `dev` tracks `origin/dev`, and the SAT test/drill apps were removed from
> Chiron on 2026-08-26. The cleanup audit's approved sections A and B were
> applied on 2026-08-25. Historical statements below are retained as the state
> of the handoff, not current instructions.

## The four documents

| # | Document | What it's for |
|---|---|---|
| **01** | [[01 — DONOVAN Master Context]] | **Everything about him.** The interview, values, decision rules, achievements, failures, projects, voice. Read this first, in full |
| **02** | [[02 — AI Workspace Master Plan]] | The senior-year goal: his own AI workspace + database by June 2027. Architecture, 7 phases, what to cut, decisions still owed |
| **03** | [[03 — Course Build Plan]] | Full course specs — Japanese (Genki + JLPT) and one course per project. Format, build order, kill criteria |
| **04** | [[04 — Claude Code to Codex Migration]] | What carries over, what needs rebuilding, what dies |
| **05** | [[05 — Vault Cleanup Audit]] | The 2026-08-25 cleanup audit. Sections A and B were approved and applied; section C remained open |

Plus **`~/Documents/Obsidian/AGENTS.md`** — the vault working rules, in the file
Codex reads automatically. `CLAUDE.md` stays beside it, unchanged.

And **`learning/ai-improvement/Memory-Export/`** — claude-mem's entire history
(2,329 observations, 401 session summaries, and every prompt he ever wrote)
exported to portable markdown on 2026-08-25, so ~360k tokens of accumulated
context survives the platform change instead of dying with the plugin.

## The five things that matter most

1. **Keep `~/code/chiron` backed up.** The original no-remote risk was resolved:
   private `Corsaya/chiron` exists and local `dev` tracks `origin/dev`.
2. **Never flatter him.** Rushed agreement reads as a lie. Criticism is the
   trust-building move, not the risk.
3. **His failure mode is self-directed prep with nothing enforcing it** — that's
   what the beach-patrol failure was, and it's what the Japanese roadmap is.
   The workspace's job is enforcement, not storage. Everything else is a database.
4. **Nobody schedules Donny but Donny.** Advise on card pricing, health, hard
   messages, and his calendar — decide none of them.
5. **The novel is his and his friend's.** Editor only. Never author.

## What was NOT done

Stated plainly so nothing here reads as more complete than it is:

- **The three Instagram Reels could not be read.** Instagram serves nothing to a
  logged-out request. The course format in 03 is built from his confirmed
  "short-form study/edu content" brief plus the SAT crash-course format he already
  validated — **not** from those specific videos. If they were doing something
  more particular, paste the captions and 03 gets corrected in one pass.
- **No code was written.** These are plans and context, not implementation.
- **The SAT retake on 2026-08-22 has no score yet.** Nothing in these documents
  assumes an outcome.
- **JLPT prep-book editions were not verified**, and the vault doesn't record
  which books he owns. See 03 §2.6 before building JP-03/JP-04.
- **Codex's hook/extension surface was not verified live.** 04 §3.2 flags this —
  don't assume a 1:1 mapping from Claude Code hooks.

## The opening prompt for the first GPT-5.6 session

```
Read ~/Documents/Obsidian/AGENTS.md, then read
~/Documents/Obsidian/pytheas/Operations/Handoff/01 — DONOVAN Master Context.md in full.

Then, before proposing anything: tell me the three things in that document you
think are most likely to be wrong or out of date, and why. Don't fix them.
Don't be agreeable about it.
```
