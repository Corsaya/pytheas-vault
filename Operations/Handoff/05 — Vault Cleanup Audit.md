---
title: Vault Cleanup Audit
date: 2026-08-25
tags: [handoff, vault, cleanup, maintenance]
status: APPLIED 2026-08-25 — sections A and B done; section C left open
---

# Vault Cleanup Audit

Scanned the five current vaults on 2026-08-25 for content the 2026-08-12 restructure left
behind.

> [!success] Approved and applied, 2026-08-25
> **Every item in sections A and B below has been fixed.** The findings are kept
> as the record of what was wrong and why it was changed — read them as history,
> not as a to-do list. **Section C (structural suggestions) was deliberately not
> done** and is still open.
>
> What changed:
> - `pytheas/Home.md` — rewritten as a real Pytheas vault index (was titled
>   "Jarvis — Scratchpad" and pointed at the wrong repo)
> - `pytheas/Summary.md` — marked as a 2026-05-30 historical snapshot
> - `learning/ai-improvement/North Star.md` — refreshed to current focus, broken
>   `../personal/Health/...` link fixed, Shifts Log entry added, new anti-goal
>   ("don't answer execution failure with more plans")
> - `pytheas/Development Roadmap.md` — header block corrected; workstreams untouched
> - `learning/ai-improvement/Pytheas Capability Map.md` — vault paths + safety posture
> - `learning/ai-improvement/CLAUDE.md` — **deleted** (frozen duplicate, nothing
>   unique; recoverable via `git show HEAD~1:ai-improvement/CLAUDE.md`)
> - root `CLAUDE.md` — three dead MERGED paths corrected, `card-flip` repo line
>   fixed, companion-files callout added, "Retired rules" section appended
> - `learning/Japanese/Resources/Genki vs Tae Kim.md` — Genki decision block added
> - `Gotchas.md` — two entries marked superseded; three new 2026-08-25 entries
> - `Key Decisions.md` — the 2026-08-12 reversal recorded, plus Genki + migration
> - `Ultimate Workspace Roadmap.md` — snapshot notice pointing at the current plan
> - `pytheas/Operations/Prompts/*` — untouched, as they must be

**The distinction that matters:** some of these files are *live docs* that should
be corrected. Others are *dated logs* — `Gotchas.md` explicitly says "append,
don't prune; note the date it was superseded rather than deleting the line."
Those get a superseded note appended, never a rewrite. They're mixed together
below and labelled.

---

## A. Live docs that are actively wrong — fix these

### 1. `pytheas/Home.md` — wrong on three counts ⚠ highest priority
The entry point to the pytheas vault still describes the pre-rename project.
- Titled **"Jarvis — Scratchpad"**; the vault is Pytheas.
- Says the code lives at `~/code/jarvis/`. Pytheas's code is `~/code/pytheas`,
  and the fork is `~/code/chiron`. `~/code/jarvis` is a *separate*,
  design-only repo.
- Says the `learning-vault/` symlink "Never points at `personal-private/` — that
  vault stays walled off from this one." **The wall was retired 2026-08-12.**
- Doesn't mention Chiron, the SAT courses, or `Handoff/` at all.

**Fix:** rewrite as the Pytheas vault index. This is the file a new agent or a
future Donovan opens first — it being three months stale is the worst single
piece of drift in the vault set.

### 2. `pytheas/Summary.md` — flatly false
Says Pytheas is *"Fully architected but not yet implemented — the repo is
design-only; no `.py` files exist yet."* `~/code/pytheas` currently contains
`server.py`, `voice.py`, `courses.py`, `research.py`, `models.py`, `actions.py`,
`briefing.py`, `chats.py`, `emailcal.py`, `permissions.py`, and more.

**Fix:** either rewrite against reality, or — better — mark it clearly as a
**2026-05-30 historical snapshot of the Jarvis design phase** and point to the
Capability Map as current. It's a fine artifact; it's a terrible current summary.

### 3. `learning/ai-improvement/North Star.md` — stale and has a broken link
- Dated 2026-07-06. Its short-term goals are done or superseded; the SAT (the
  thing that consumed all of August) isn't mentioned; the workspace-by-senior-year
  goal isn't in it.
- **Broken link:** `[[../personal/Health/Crew/Season Plan/2026-27 Season Plan]]`.
  That path no longer exists — it's now under `life/personal-private/Health/`.
  (Note: `Season Plan/` as a subfolder also isn't in the current tree; the file
  present is `Health/Crew/Rowing_Training_Plan_2026-2027.md`. Confirm which is
  meant before relinking.)

**Fix:** this is the single most valuable file to refresh, because it's the one
the working rules tell every agent to read before planning. It has a Shifts Log
built in for exactly this — add an entry, don't silently overwrite.

### 4. `pytheas/Development Roadmap.md` — retired access rules stated as current
Its header lists the pre-restructure vault roots (`personal`, `ai-improvement`,
`card-flip`, `minecraft-event` as top-level) and states that
`personal/Journal`, `personal/Daily`, `personal/Work`, and
`personal/Private-Reference.md` are *"never AI-readable, never AI-writable, no
exceptions."* **Retired 2026-08-12.** An agent reading this will refuse work it's
allowed to do.

**Fix:** update the header block only. The four workstreams below it are still
good and shouldn't be touched.

### 5. `learning/ai-improvement/Pytheas Capability Map.md` — old vault roots
"Vault integration points" lists `jarvis/`, `learning/Courses/`,
`ai-improvement/`, and `personal/` with "writes hook-blocked (unchanged)". Two of
those paths don't exist; the hook was removed before the policy changed. Also
dated 2026-07-24 and predates Chiron entirely.

**Fix:** update paths and the safety-posture line; add a Chiron section.

### 6. `learning/ai-improvement/CLAUDE.md` — nested instructions, now doubly stale
A second CLAUDE.md scoped to `ai-improvement/`, written when it was a top-level
vault. It's now a subfolder of `learning/`, and its rules predate both the
restructure and the migration off Claude Code.

**Fix:** either delete it (its useful content is in the root file) or convert to
`AGENTS.md` scoped to that folder. **Recommend delete** — two instruction files
disagreeing is worse than one imperfect one.

### 7. Root `CLAUDE.md` — mostly excellent, three dead references
- References `personal.MERGED-into-life-2026-08-12/`,
  `minecraft-event.MERGED-into-life-2026-08-12/`, and
  `card-flip.MERGED-into-finance-2026-08-12/`. **Verified: none of these
  directories exist any more.** They were cleaned up and the doc wasn't told.
- The `ccdash`-every-response rule and the claude-mem session-end rule are dead
  post-migration (both carried into `AGENTS.md` §9 as explicitly retired).
- Lists `card-flip` as a sub-vault with its own repo; it's now inside `finance/`.

**Fix:** small surgical edits. Keep the file — a future Claude session or
OpenClaw still reads it.

### 8. `learning/Japanese/Resources/Genki vs Tae Kim.md` — decision superseded
Recommends **Tae Kim as the spine**. Donovan's stated choice on 2026-08-25 is
**Genki + JLPT books.** See `03 — Course Build Plan` §2.1 — the new choice is also
the better one, for a reason that note's reasoning missed.

**Fix:** add a dated "Decision (2026-08-25)" block at the top. Keep the comparison
— it's good, and the reasoning is worth preserving even where it was wrong.

---

## B. Dated logs — append a superseded note, do NOT rewrite

These correctly describe what was true on their date. Their staleness is the
point.

- **`learning/ai-improvement/Gotchas.md`** — the 2026-07-06 entries about the
  `personal/` wall and `private-vault-guard.py`. Per the file's own rule, append:
  *"— superseded 2026-08-12: wall retired, hook removed."*
- **`learning/ai-improvement/Key Decisions.md`** — the 2026-07-05 vault-split and
  2026-07-06 hook entries. Add a 2026-08-12 entry recording the reversal, so the
  log reads as a sequence of decisions rather than a contradiction.
- **`learning/ai-improvement/2026-07-15-perfect-assistant-thought-dump.md`** —
  dated by filename. Leave it alone entirely.
- **`pytheas/Ultimate Workspace Roadmap.md`** — a 2026-08-02 snapshot. Its status
  is already `draft`. Add a pointer to `02 — AI Workspace Master Plan` as the
  current version; don't edit the body.
- **`pytheas/Operations/Prompts/*`** — **never edit these.** The prompt-logging convention's
  entire value is that they're an immutable record of what was actually asked.

---

## C. Structural suggestions (low priority, all optional)

- **`pytheas/Generated/Briefings/` has flat dated files** and grows daily. Foldering by month
  (`2026-07/`, `2026-08/`) would help — **but** it breaks any existing wikilinks
  and the briefing generator writes to the flat path. **Fix the generator first
  or don't do it.** Genuinely optional.
- **The last four briefings (08-22 → 08-25) are raw research dumps** with the
  header *"claude synthesis unavailable"* — the synthesis step has been silently
  failing since the subscription wound down. Post-migration the briefing pipeline
  (`~/code/pytheas/briefing.py`) needs repointing at a working model regardless.
- **`learning/School/Senior Year (2026-2027)/` is empty.** School starts in about
  a week. Building it out with the AP Chem structure is the highest-value
  *content* work available right now — but per the vault's own convention, only
  build it when actively used, not preemptively.
- **`learning/ai-improvement/Memory-Export/` (new, 2.6 MB, added today)** — the
  full claude-mem history as markdown. It's machine-generated log data, not
  authored notes. Consider whether it belongs in git or should be gitignored like
  `Conversations/`. **Recommend committing it** — the whole point was surviving
  the platform change, and local-only is what put it at risk.

---

## Suggested order

1. `pytheas/Home.md` — worst drift, most-read file.
2. Root `CLAUDE.md` — three dead paths, quick.
3. `North Star.md` — refresh + fix the broken link + Shifts Log entry.
4. Delete `learning/ai-improvement/CLAUDE.md`.
5. `Development Roadmap.md` header block.
6. Everything else as it comes up.

Items 1–4 are perhaps 30 minutes total and remove every actively misleading
statement an incoming agent would trip on.
