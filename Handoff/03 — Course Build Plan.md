---
title: Course Build Plan
date: 2026-08-25
tags: [handoff, courses, japanese, genki, jlpt, projects, curriculum]
status: spec — ready to build, nothing built yet
related: ["[[01 — DONOVAN Master Context]]", "[[02 — AI Workspace Master Plan]]", "[[../Courses/Home]]"]
---

# Course Build Plan

Full-course specs for: **Japanese (Genki + JLPT)** and **every one of his own
projects**, authored in the short-form study/edu content style.

> **Note on the source material.** Three Instagram Reels were given as the style
> reference (`DcRJg5fDdsJ`, `DbdtA0jDSzG`, `DbnhWPsDZyK`). **They could not be
> read** — Instagram serves nothing to a logged-out request, so there is zero
> content behind those links from this side. Donovan confirmed the intended
> reference is **dense short-form study/education content**: hook first, one idea
> per beat, no throat-clearing. The format below is built to that brief. If the
> Reels were doing something more specific, paste the captions and this spec gets
> corrected in one pass.

---

## 1. The format (derived, not invented)

He already validated a course format under real pressure: the eight SAT crash
courses, written in ~10 days, in the run-up to a live test. That format works and
it maps almost exactly onto short-form pedagogy. Formalize it as **the house
style** rather than inventing a new one.

**The atomic unit is a "beat" — one skill, one screen, four moves:**

```
### <ID> — <the skill, stated as a verb>

**What this actually tests:** <the real thing being measured, one sentence>
**The rule:** <the minimum formal statement — formula, pattern, or grammar frame>
**Worked example:** <one concrete instance, fully solved, no steps skipped>
**Trips people up:** <the specific failure mode, not a generic warning>
```

**Why this is already short-form-native:**

| Short-form move | The beat's equivalent |
|---|---|
| Hook in the first second | "What this actually tests" — reframes before teaching |
| One idea per video | One skill per beat, IDs so it's addressable |
| Show, don't describe | Worked example, always concrete |
| The "actually…" payoff | "Trips people up" — the retained part |
| Rewatchable in 30s | A beat is scannable in under a minute |

**House rules, non-negotiable:**
- **Every beat gets a stable ID** (`M1`, `G1`, `K5`). IDs are what let progress
  tracking, spaced repetition, and gap analysis attach to content. Without IDs
  a course is prose; with IDs it's a database. This is the whole difference.
- **"Trips people up" must be specific.** "Be careful with signs" is not a
  failure mode. "When *b* is negative but *c* is positive, both numbers must be
  negative" is.
- **Every course ends in a knowledge check** whose items map 1:1 to beat IDs, so
  a wrong answer names the exact beat to reread. The SAT `Foundations Knowledge
  Check` → `Crash Course` → `Gap Lessons` chain already does this. Copy it.
- **No motivational filler.** Standing directive: no flattery, nothing written to
  please. A course that congratulates him is a course he stops trusting.

---

## 2. Japanese — Genki + JLPT

### 2.1 A decision that changed

The vault currently recommends **Tae Kim as the grammar spine** (`learning/
Japanese/Resources/Genki vs Tae Kim.md`) on the reasoning that it's free and
suits a proactive self-directed learner. **His stated choice is Genki + JLPT
books.** Treat that as the decision and update the resource note.

**And the new choice is probably the better one, for a reason the old note
missed.** That note argued Tae Kim because he's "the proactive type." But the
honest record (Master Context §6, §12) says the opposite is his risk: the
Japanese roadmap has been immaculate since May 2026 and he is still at ~90%
hiragana with katakana untouched. **His failure mode is self-directed work with
no external structure enforcing it.** Genki's chapters, workbook, and audio *are*
that external structure. Tae Kim optimizes for a learner who doesn't need
scaffolding; Genki optimizes for one who does. Pick the one that fixes the actual
bottleneck.

### 2.2 Honest current state

- **Stage 0 — Foundations.** Hiragana ~90% and rusty (untouched for months).
  Katakana not started.
- Pace: 7 hr/wk sustainable, 10 hr/wk committed → N1 in ~7–8 years.
- **Nothing above Stage 0 should be built until Stage 0 is finished.** Building
  the N3 course now would repeat the exact pattern that produced this state.

### 2.3 Course structure

| Course | Beats | Source spine | Gate to start |
|---|---|---|---|
| **JP-00 · Kana** | ~110 (46 hiragana + 46 katakana + dakuten/combos) | — | **Now. This is the only one that starts today.** |
| **JP-01 · Genki I** | ~23 chapters × ~6 grammar beats ≈ 140 | Genki I + workbook | Kana at 100%, both sets, cold recall |
| **JP-02 · Genki II** | ≈ 140 | Genki II + workbook | Genki I chapters 1–23 complete |
| **JP-03 · N5 Consolidation** | ~80 | JLPT N5 prep books | Genki I done |
| **JP-04 · N4 Consolidation** | ~120 | JLPT N4 prep books | Genki II done |
| **JP-05 · Kanji Track** | runs parallel, ~2,200 beats staged by JLPT level | Kanji books + SRS | Runs alongside JP-01 onward |

### 2.4 Beat format, adapted for language

```
### G1-07 — て-form of う-verbs

**What this actually tests:** whether you can apply the ending-swap table fast
enough to conjugate mid-sentence, not whether you can recite the table.
**The rule:** う/つ/る → って · む/ぶ/ぬ → んで · く → いて · ぐ → いで · す → して
**Worked example:** 待つ (matsu, to wait) → つ is in the first group → 待って
(matte). 「ちょっと待って」= "wait a second."
**Trips people up:** 行く (iku) is the one irregular in this group — it looks like
a く verb but becomes 行って (itte), not 行いて. It's the single most common verb
this rule breaks on, which is why it's the one you'll hit first.
```

### 2.5 The three things that make it a course and not a textbook summary

1. **Every beat is an SRS item**, scheduled from the core DB (Workspace Plan
   Phase 3). Grammar points decay exactly like vocabulary; treating them as
   read-once content is why grammar review is the thing everyone skips.
2. **Kanji beats and grammar beats share one review queue.** Separate queues mean
   one gets abandoned, and it's always the same one.
3. **Immersion is scheduled, not aspirational.** The roadmap is already
   reading-first and media-driven; the course must convert that into specific
   assigned material per stage, in the calendar, or it stays a preference.

### 2.6 Honest note on JLPT books

Specific JLPT prep series (Shin Kanzen Master, Sou Matome, Try!, Nihongo So-Matome,
etc.) were **not** verified against current editions, availability, or price as
part of this plan, and nothing in the vault records which ones he owns. Before
building JP-03/JP-04, establish **which books he actually has in hand** — course
beats must map to real page numbers or the whole ID system decouples from the
source and silently rots.

---

## 3. Project courses — "How I Built This"

The stated purpose, from the original mega-prompt: **teach him to build similar
things without AI generating it for him.** That single sentence dictates the
format, and it makes these fundamentally different from the Japanese courses.

**The design constraint:** a project course that just explains what the code does
is documentation, and it teaches nothing. It must be **reconstructive** — each
beat presents the problem *as it was faced*, makes him decide, and only then
shows what was actually done and why.

```
### PY-12 — Why Desmos broke on every navigation

**The situation:** The SAT test runner rebuilt the question area with innerHTML
on every next/previous click. The Desmos calculator was initialized once, on load.
**Your move:** Before reading on — what breaks, and what are your two options?
**What actually happened:** innerHTML replaced the DOM node Desmos was mounted to.
The widget kept running against a detached element — no error, no calculator.
Fixed by re-attaching after every rebuild.
**The transferable rule:** any third-party widget mounted into a container you
later overwrite must be re-attached or re-created. innerHTML is not a repaint,
it's a replacement.
**Where this bit you again:** <cross-links to other beats with the same root cause>
```

The raw material for all of this already exists and is unusually good: git logs,
`DECISIONS.md` (DEC-001 → DEC-024), session wraps, the `Gotchas.md` file, and the
Development Roadmap's bug write-ups. **The gotchas are the highest-value source in
the entire vault for this** — each one is a real failure with a real cause.

### The five project courses

| Course | Covers | Best source material | Priority |
|---|---|---|---|
| **PY · How Pytheas Was Built** | Python app architecture, model routing, voice pipeline, permissions, the Odysseus fork, Docker, CSP debugging | `~/code/pytheas` + `~/code/chiron` git logs, `DECISIONS.md`, session wraps, `Gotchas.md` | **1st** — most material, most transferable |
| **CF · card-flip** | Market thesis vs. expertise, pull-rate pricing, the drop monitor (Playwright), SOP discipline, the $20→$13 lesson | `finance/card-flip/` SOPs, flip logs, `learnings/` | 2nd |
| **MC · The Minecraft Event** | Java/Paper plugin dev, server infra, game-systems design (the four-way counter loop is genuinely good design), running a crew | `~/minecraft-event`, `TECH_ARCHITECTURE.md`, `WORLD_DESIGN.md` | 3rd — highest Java learning value |
| **VS · The Vault System** | Information architecture, git subtree merges, conventions that survive contact, agent access boundaries | `CLAUDE.md` history, `Key Decisions.md`, the 2026-08-12 restructure | 4th |
| **AI · Prompting & AI Behavior** | How to actually direct models; the interview kit as method; the knowledge-map idea | `learning/ai-improvement/` in full | 5th — build after a model of what he knows exists |

### The open question this raises (still unanswered, and it's the important one)

The original mega-prompt wants the assistant to *"know exactly what I do and don't
know."* That is not a course feature — **it's a data model.** A per-topic
knowledge-state store, updated by course progress and knowledge checks, injected
into context the way environment context is.

**This is the actual reason to have a database at all**, and it is the connective
tissue between this document and the Workspace Plan. Courses write to it; the
enforcement layer (Phase 3) reads from it and decides what to surface. Build the
schema in Phase 1 even if courses come in Phase 4 — a `knowledge_state` table
keyed on beat IDs, with last-reviewed, confidence, and source.

---

## 4. Build order

1. **JP-00 Kana.** Small, finishable, unblocks everything Japanese, and closes a
   gap that's been open since May 2026. Ship it first for the momentum alone.
2. **The beat-ID schema + `knowledge_state` table** (Workspace Phase 1). Do this
   before authoring bulk content, so nothing has to be retrofitted.
3. **PY · How Pytheas Was Built.** Material already exists; it mostly needs
   restructuring, not research. Highest ratio of value to effort.
4. **JP-01 Genki I**, chapter by chapter, gated on kana being genuinely done.
5. Everything else, as windows allow.

**The kill criterion, stated in advance so it's honest later:** if JP-00 Kana is
built and katakana still isn't learned 30 days after, the problem is not the
course format — it's the enforcement layer, and the fix belongs in Workspace
Phase 3, not in writing more course content. **Do not respond to that failure by
building another course.**
