---
tags: [pytheas, sat, drill, adaptive, crash-course]
created: 2026-08-19
source: "Chiron classroom app — static/classroom-apps/sat-drill/"
related: ["[[Crash Courses/Math — Advanced Math]]", "[[Crash Courses/R&W — Standard English Conventions]]", "[[Crash Courses/R&W — SAT Grammar Rules Reference]]", "[[SAT Master Guide — Score Higher (2026-08-12)]]"]
---

# SAT Adaptive Drill

Opening this file in Chiron's Classroom launches the interactive drill, not this
text. This page is the written explanation of what the drill does and how to use
it — the app itself is at **Classroom → SAT → SAT Adaptive Drill**.

## How the ladder works

Every skill is a ladder of questions at four difficulty levels. You always enter
at **level 0 — real SAT difficulty**.

| Level | What it is |
|---|---|
| **+1** | Stretch. Harder than the real test — disguised setups, two rules interacting. |
| **0** | Real SAT difficulty. Where you start, and the only level that predicts your score. |
| **−1** | Same skill, stripped down. Smaller numbers, fewer steps, nothing hidden. |
| **−2** | The concept underneath the skill. The prerequisite, asked directly. |

- **Get it right** → you climb a rung. Clear the stretch rung and the skill is done.
- **Get it wrong** → you get one hint and a second try at the same question.
- **Wrong again** → full worked explanation, then you **drop a rung**.
- **Keep failing** → you keep dropping, down to the foundations rung. The drill
  is looking for the level you actually know, then rebuilding upward from there.
- **Bottom out** → the skill is flagged as a real gap and **requeued**, so it
  comes back around later in the same session instead of being quietly skipped.

The point of dropping is diagnostic. If you miss the level-0 question but nail
the level −2 one, the gap is in applying the skill under SAT disguise. If you
miss −2 too, the gap is the underlying concept and that is what to study.

**A low session percentage does not mean a low score.** Sub-level-0 rungs are
scaffolding, not SAT-difficulty questions — you only see them because you missed
something, so they are structurally biased toward your weak areas.

## Desmos

Every math question that is genuinely faster with the built-in Desmos graphing
calculator carries a **Faster in Desmos** box under the explanation, with the
literal keystrokes to type and what to read off the screen. Desmos is available
on the entire Math section of the digital SAT — for a large share of Advanced
Math and Algebra questions, graphing and clicking the intersection is faster and
less error-prone than doing the algebra.

Practise the Desmos method even on questions you can already do by hand. The
speed matters more than the elegance on test day.

## Priority order

Ordered by the score history in [[SAT Diagnostic — Score History and Domain Analysis]]:

1. **Advanced Math** — confirmed weak spot across both official sittings. Deepest ladders.
2. **Standard English Conventions** — confirmed weak spot. Deepest ladders.
3. Everything else, as time allows.

The two weak-spot domains have four-rung ladders on every skill. The other six
have three rungs (−1, 0, +1).

## The review doc

At the end of a session, hit **Export review doc to vault**. It writes
`Courses/SAT/Review/Pre-Test Review — <date>.md` containing:

- Every skill you bottomed out on, and every one you only got after dropping a rung
- Every question you missed, with what you picked and what was correct
- **Every question you asked the tutor chatbot, with its answers**

That last part is the one to have open before the test. Tutor questions are
collected automatically as you ask them — you don't have to save anything
yourself. Exporting clears the collected questions, so each export covers the
work since the last one.
