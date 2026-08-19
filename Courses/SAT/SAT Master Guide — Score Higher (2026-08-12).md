---
tags: [pytheas, sat, course, index]
created: 2026-08-12
status: in progress
source: entry point linking all SAT course material
related: ["[[SAT Study System — Claude Bridge]]", "[[Adaptive Review System]]", "[[Test Day Execution]]"]
---

# SAT Master Guide — Score Higher

10 days out from the **August 22, 2026** SAT. This is the entry point into everything built
for this prep — start here, use it to decide what to work on next.

## Current operating system

Before creating or changing a crash course, read [[SAT Study System — Claude Bridge]]. It defines
the current Bluebook-to-course workflow: record every question, distinguish wrong answers from
guesses, capture timing, and build only the targeted lessons and morning-of review packet supported
by that evidence. Use [[Adaptive Review System]] for the review record and [[Test Day Execution]]
for the practice-test protocol.

## Where things stand

| | Dec 6, 2025 | Mar 14, 2026 | Diagnostic (2026-08-07) |
|---|---|---|---|
| Total | 1280 (84th pct) | 1280 (84th pct) | 28/32 (87.5%) |
| Reading & Writing | 660 (87th pct) | 630 (81st pct) | strong |
| Math | 620 (81st pct) | 650 (85th pct) | Advanced Math is the weak spot |

Full history and per-domain breakdown: [[SAT Diagnostic — Score History and Domain Analysis]].
Confirmed weak spots across both official score history and the fresh diagnostic: **Advanced
Math** (asymptotes specifically) and **Standard English Conventions** (subject-verb agreement
with buried/interrupting subjects) — see the diagnostic's revised priority list for the full
reasoning.

## Study path

1. **[[Foundations Knowledge Check]]** — full conversational skill inventory across all 42
   skills in both sections (not timed, not multiple choice — just "do you actually know the
   steps"). Use this to find gaps before drilling.
2. **Crash Courses** (`Crash Courses/`) — one per official College Board domain, each with a
   worked-example walkthrough per skill plus a mini-diagnostic with an answer key:
   - Math — [[Math — Algebra]] · [[Math — Advanced Math]] ·
     [[Math — Problem-Solving and Data Analysis]] · [[Math — Geometry and Trigonometry]]
   - Reading & Writing — [[R&W — Standard English Conventions]] (flagged highest-priority) ·
     [[R&W — Information and Ideas]] · [[R&W — Craft and Structure]] ·
     [[R&W — Expression of Ideas]]
3. **[[Diagnostic Gap Lessons (2026-08-07)]]** — four short targeted lessons for the specific
   gaps the 2026-08-07 diagnostic confirmed, plus a 12-question retest.
4. **[[SAT Diagnostic Test (2026-08-07)]]** — the fresh 32-question scaled diagnostic that
   established current standing (already taken, graded, and interviewed).
5. **[[SAT Full-Length Practice Test 1 (2026-08-12)]]** — the real thing: 98 questions (44
   Math / 54 R&W) at full official question counts and domain weightings, single
   fixed-difficulty form. Take this in one sitting once the crash courses are done, to see how
   the skills hold up at full length and full time pressure.
6. **Chiron practice runner** (`~/code/chiron`, live at the Classroom UI) — Bluebook-style
   timed test-taking tool: Mark for Review, answer Eliminator, a real Desmos calculator, an
   on-demand geometry reference sheet (Math only), and a results/review screen that makes clear
   there's no penalty for guessing. Currently loads the 2026-08-07 diagnostic's 16-question
   Math module; the data file (`sat-test-data.js`) would need updating to run the full 98Q test
   through the same runner — not yet done.

## Reference / background

- [[Official SAT Structure and Content Research (2026-08-07)]] — structure, timing, official
  domain weightings, registration dates, what's official vs. prep-community consensus.
- [[Bluebook Parity, Khan Academy, Strategy, and Social Advice Research (2026-08-12)]] —
  Bluebook tool details, pacing/strategy consensus, Khan Academy angle.
- [[YouTube Guide Research — Math, Grammar, Reading (2026-08-07)]] — prep-channel strategy
  content that fed the crash courses' worked-example approach.

## Open items

- Master Guide (this file) didn't actually exist until 2026-08-12, despite an earlier session
  log claiming it did — flagged and fixed same day.
- Full-length test's 98 questions aren't wired into the Chiron runner yet (still hand-authored
  vault markdown, no vault-to-quiz ingestion pipeline exists — see the runner note above).
- No second full-length test yet — one data point at full length isn't enough to separate
  timing/execution issues from real content gaps the way the diagnostic's interview did.
