---
tags: [pytheas, sat, test-1, debrief, self-graded]
created: 2026-08-16
source: "Self-graded off the vault's Full-Length Practice Test 1 (98Q) markdown file — NOT taken through Chiron's app (that wiring wasn't live in the running container yet at test time; fixed same day)."
related: ["[[SAT Full-Length Practice Test 1 (2026-08-12)]]", "[[../../SAT Diagnostic — Score History and Domain Analysis]]", "[[../../SAT Master Guide — Score Higher (2026-08-12)]]"]
status: score confirmed by student; three R&W 0% domains explained (early submission, not a grading error); LaTeX rendering bug found and fixed
---

# Test 1 — Results and Debrief (2026-08-16)

## How this was taken

Math: completed in full (44Q). R&W: answered through roughly Q13 of the
domain sequence, then submitted early — remaining questions left blank
rather than guessed through on autopilot. Correct call: the student
noticed comprehension degrading ("words start blending... focus
depletes") around question 15 and stopped rather than generating junk
data by pushing through exhausted.

**This was not run through Chiron.** Checked at the time: the app's
32-question diagnostic didn't include this 98Q test yet (a commit wiring
it in had landed but the Docker image hadn't been rebuilt — same-day
bug, now fixed), and even once wired in, the runner only ever saves to
browser `localStorage`, never a server — so nothing would have been
recorded automatically either way. Self-graded off the vault markdown
file, then reported here.

## Score

**39/98 — 40% overall**

| Domain | Score | % |
|---|---|---|
| Algebra | 9/15 | 60% |
| Advanced Math | 8/15 | 53% |
| Problem-Solving & Data Analysis | 5/7 | 71% |
| Geometry & Trig | 5/7 | 71% |
| Information and Ideas | 12/14 | 86% |
| Craft and Structure | 0/15 | 0% |
| Expression of Ideas | 0/11 | 0% |
| Standard English Conventions | 0/14 | 0% |

## The three 0% domains — explained, not a grading error

Correction: an earlier draft of this note guessed the 0/15, 0/11, 0/14
in Craft and Structure, Expression of Ideas, and Standard English
Conventions was a self-grading alignment mistake. That was wrong, and
ignored what the student had already said directly — **the test wasn't
finished.** R&W was submitted early around Q13–15 of the section
because of genuine fatigue ("words start blending... focus depletes"),
which is exactly the right call over pushing through on autopilot. The
R&W domain order is Information and Ideas (Q45–58, 14Q) → Craft and
Structure (Q59–73, 15Q) → Expression of Ideas (Q74–84, 11Q) → Standard
English Conventions (Q85–98, 14Q). Stopping partway through Information
and Ideas/right after it means everything from Craft and Structure
onward was never attempted — blank, not wrong, not mis-graded. 0/15 on
15 unanswered questions isn't a statistical anomaly; it's certain. These
three domains have **no real score yet**, not a bad one — they need a
finished attempt to mean anything, not a re-grade.

## What was actually correct (math, ChatGPT-assisted)

Four Advanced Math problems were worked with ChatGPT's help mid-test
(completing the square, vertex form, one/no/infinite-solutions cases,
arc length, circle equation). All four were mathematically correct:

- Completing the square (x²−10x+7=0 → k=18): right method, right answer.
- Vertex form max of f(x)=−2(x+4)²+9 at x=−4: read directly off (h,k),
  correct.
- Arc length, r=12, θ=150°: 10π, correct.
- Circle x²+y²−6x+4y−3=0 → center (3,−2), radius 4: correct.

Worth being honest about: needing ChatGPT for these isn't a one-off —
Advanced Math is the one domain that stayed a **stable mid-band weak
spot across both real official SAT sittings** (see `SAT Diagnostic —
Score History and Domain Analysis`), never touching the top band either
time. This test's 53% Advanced Math score isn't a fluke; it's confirming
a gap that was already known. That's useful signal, not a new problem.

## Other flags raised

- **"&s and bad syntax" — confirmed and fixed.** Three Math (Algebra)
  system-of-equations questions used raw `\begin{aligned}...\end{aligned}`
  LaTeX with `&` alignment markers that the test runner's math renderer
  didn't know how to handle, so the student saw literal LaTeX source
  (`begin{aligned} 2x + 5y &= 19 ...`) instead of a formatted system of
  equations — on flagged questions Q2 and another that were left
  unanswered, this unreadable rendering was likely a real contributing
  factor, not just fatigue. Fixed in `sat-test.js`'s `renderMath()`:
  aligned blocks now stack cleanly, and several other unhandled LaTeX
  commands found in the same sweep (`\sin`, `\cos`, `\tan`, `\theta`,
  `\approx`, `\times`, `\to`, `\triangle`, `\dfrac`) are now rendered
  properly too instead of leaking raw backslash-commands into the
  question text.
- **"Most answers were obvious — longest/most detailed choice was
  usually correct"** — a real pattern-matching shortcut worth being
  aware of both ways: it can work as a tell on genuinely uncertain
  questions, but over-relying on it risks missing a shorter correct
  answer once the question-writer is aware of the habit. Not yet
  analyzed against this specific test's answer key to confirm the
  pattern actually held here.

## Same-day build-out

All 8 SAT crash-course files (Advanced Math, Algebra, Geometry & Trig,
Problem-Solving & Data Analysis, Craft and Structure, Expression of
Ideas, Information and Ideas, Standard English Conventions) were
expanded from 1 to 3 worked examples per subcategory (65 subcategories
total) the same day this test was debriefed — Advanced Math and Standard
English Conventions got full-depth treatment first, since those are the
two confirmed stable weak spots.
