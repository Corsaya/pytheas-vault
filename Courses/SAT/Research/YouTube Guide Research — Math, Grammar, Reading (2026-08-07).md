---
tags: [mega-prompt, sat, research]
date: 2026-08-07
status: partial — August-specific cluster + 2 videos blocked by yt-analysis MCP quota/tool errors, retry needed
---

# SAT YouTube Guide Research — 2026-08-07

Source: curated "best guide per topic, skip duplicates, prioritize August-focused" pull
across [@PenguinTestPrep](https://www.youtube.com/@PenguinTestPrep),
[@JamesLuSAT](https://www.youtube.com/@JamesLuSAT), and
[@satgamified](https://www.youtube.com/@satgamified), processed via the yt-analysis MCP
tools. Four parallel research passes; two completed clean, two hit tool failures
(see **Status / what's still missing** at the bottom — retry once resolved).

This feeds the SAT course build in `Courses/SAT/Units/`. Donovan's diagnosed weak spots
(per `SAT Diagnostic — Score History and Domain Analysis.md`): **Advanced Math** domain
and **Conventions of Standard English**.

---

## 1. Math domain (5/5 videos processed — satgamified unless noted)

### Digital SAT math domain weights (stated in "All of SAT Math Explained in One Video")
Algebra ~33% · Advanced Math ~33% · Geometry & Trig ~15% · Problem-Solving & Data Analysis ~19%

**Advanced Math is explicitly called "probably the most missed section" and "what separates
600 scores from 750+ scores"** — matches Donovan's diagnosed weak spot exactly; anchor the
course here.

### Algebra
- Word-problem cues: "per" = multiply, "is/was" = equals sign.
- Inequality sign flips when multiplying/dividing by a negative.
- $f(x)$ as input-output machine.
- $y=mx+b$; parallel = same slope, perpendicular = negative reciprocal.
- **Standard-form slope shortcut:** for $Ax+By=C$, slope $=-A/B$ (no need to rearrange to
  slope-intercept first).
- Systems: intersection = solution; parallel = no solution; identical lines = infinite solutions.
- Six exponent rules: product, quotient, power, zero, negative, fractional.

### Advanced Math (highest priority)
- Three quadratic forms: standard $ax^2+bx+c$, vertex $a(x-h)^2+k$, factored $a(x-p)(x-q)$.
- Quadratic formula + discriminant $b^2-4ac$ to count real solutions.
- **Vertex x-shortcut:** $x=-b/(2a)$. **Sum-of-solutions shortcut:** $-b/a$.
- Polynomials: even-degree factors "bounce" off the x-axis, odd-degree factors pass through.
- Exponential growth/decay $y=ab^x$; rational function asymptotes; graph transformation rules
  (shifts/reflections).
- No-solution system trick example: $-\tfrac{3}{14}py+\tfrac{t}{6}=9-\tfrac{5}{42}y$ solved
  for $p$ under the no-solution condition → $p=0.556$.

### Geometry & Trig (smallest domain, ~15%, but formulas are finite/memorizable)
- **"There is no geometry button on Desmos. You just have to learn it."** — geometry can't be
  calculator-hacked the way algebra/advanced math can.
- Angle pairs (vertical, supplementary, corresponding, alternate interior); triangle angle sum
  180°; polygon interior angle sum $180(n-2)$; Exterior Angle Theorem; Triangle Inequality
  Theorem.
- Pythagorean theorem; SOHCAHTOA; **Complementary Angle Theorem:** $\sin(x)=\cos(90-x)$.
- Special right triangles: 45-45-90 ($s,s,s\sqrt2$), 30-60-90 ($s,s\sqrt3,2s$).
- Similarity provable via SAS/AA/SSS.
- Memorize (not on reference sheet per video): sphere surface area $4\pi r^2$, cylinder
  surface area $2\pi rh+2\pi r^2$.
- **Scale factor rule:** linear scale $k$ → area scales $k^2$ → volume scales $k^3$. (Example:
  surface-area ratio 25:1 → linear ratio 5:1 → volume ratio 125:1.)
- Circle: $(x-h)^2+(y-k)^2=r^2$; arc length ∝ central angle; tangent ⟂ radius at tangency point;
  **central angle = 2× inscribed angle** on the same arc (flagged as commonly forgotten).
- Altitude shortcuts: general $h=2\cdot\text{Area}/\text{base}$; right-triangle
  altitude-to-hypotenuse $h=(\text{leg}_1\cdot\text{leg}_2)/\text{hypotenuse}$, or equivalently
  $h=\sqrt{\text{segment}_1\cdot\text{segment}_2}$ for the two hypotenuse segments it creates.
- Trap: **diagram angles are drawn deceptively** — never assume equal-looking angles are equal;
  prove via one of the four angle-pair rules.

### Problem-Solving & Data Analysis (~19%, called "one of the largest sections")
- Mean vs. median: mean is pulled toward outliers, median is robust.
- **Shift Rule:** add/subtract a constant → shifts center only, spread/SD unchanged;
  multiply/divide → changes both center and spread.
- Scatterplots: distinguish **actual data points** from the **model/prediction line**.
- Percent-change formula: **(new − old) / old**.
- Probability = target/total — watch for the word **"given"**, which changes the denominator
  from the grand total to a subgroup total (flagged as a major trap).
- Sampling only generalizes to a population with **random selection**; margin of error defines
  a plausible range around a sample estimate.
- Unit conversion trap: squared/cubed units need the conversion factor squared/cubed too
  (e.g. $3\text{in}^2 \to 19.35\text{cm}^2$, not a straight linear conversion).

### Percentages (small ~3.66–4% of math section, but high error rate — good quick-review ROI)
- "Increased by 500%" = **600%** of the original (100% + 500%), not 500% — the headline trap.
- Multi-step percent problems (discount then tax): each percentage must apply to the **correct
  base**, not always the original number.
- Mixture formula: $(\text{conc}_1)(\text{amt}_1)+(\text{conc}_2)(\text{amt}_2)=(\text{conc}_{total})(\text{amt}_{total})$.
- "Percent greater than" comparisons: pick an arbitrary starting number (e.g. 100) to make the
  arithmetic concrete instead of working symbolically.

### Desmos (framed as single highest-leverage skill — but NOT a substitute for concept mastery)
- Use the **College Board in-test Desmos**, not the public web app (same engine, test context).
- Shortcuts: Shift+6 for exponents, `/` for fractions, direct percent/trig typing, direct
  stats functions (mean, median, etc.), direct percent expressions ("50% of 6").
- Solve single-variable equations by graphing both sides and reading the intersection's
  x-coordinate. Systems of equations = intersection point. Systems of inequalities = overlapping
  shaded region.
- **Tilde (`~`) regression** — solve equations with multiple unknowns without building a data
  table; called "probably the most powerful thing in Desmos."
- Table-based regression for linear/quadratic/exponential best-fit curves from raw data points.
- Circle lookup: type $(x-h)^2+(y-k)^2=r^2$ directly to read center/radius/diameter.
- Verify equivalent expressions by graphing both and checking for exact overlap (skip manual
  expand/factor).
- Heuristic: "Any time you see an expression, equation, or point in a problem, you probably
  should be using Desmos." Explicit caveat: "You still need to know how the math works" for
  harder Advanced Math items — Desmos speeds execution, doesn't replace understanding.

---

## 2. Conventions of Standard English (Donovan's #1 weak spot — 2/3 videos processed)

### "All of SAT Grammar in 37 Minutes" (satgamified) — full
Frame: grammar is "a pattern game with tiny fixed moves," not a memory test — 7 predictable
question types. **Punctuation (boundaries) and verb questions make up the majority of the
Conventions section** and are where students struggle most.

- **Independent Clause (IC) test:** subject + main verb; verb can't start with "to"/"that" or
  end in "-ing"; no **WASABI** word (While, After, Since, Although, Because, If) opening the
  clause, or it's a Dependent Clause (DC).
- IC/IC joins: period, semicolon, or comma+FANBOYS (for, and, nor, but, or, yet, so).
  IC/DC joins: comma or nothing.
- **Colon rule:** left side must independently pass the IC test and "promise" something; right
  side "delivers." If the left side fails the IC test, no colon.
- **"However" placement trick:** if the contradiction is between sentence 1 and the first half
  of sentence 2 → "A. B, however; C." If the contradiction is between the two halves of sentence
  2 → "A. B; however, C."
- **Complex lists:** upgrade to semicolons when list items already contain commas — giveaway is
  a semicolon followed by "and."
- Dashes usually travel in pairs to bracket an interruption; can also function like a colon.
- Non-essential info (deletable without changing core meaning) gets set off with commas/dashes
  — flagged as **one of the hardest, most-missed patterns on the whole test**.
- Direct question → question mark; indirect/reported question → period.
- **Verb Count:** adding "S" makes a *verb* singular (opposite of nouns) — find the true subject
  (often buried after a long noun phrase) to check agreement.
- **Verb Time:** "had" = past-before-the-past (double past).
- **Verb "engine" rule:** every sentence needs exactly one main verb. If one already exists,
  the answer must be a non-verb form (e.g. "-ing"); if missing, pick the finite verb.
- Modifiers: the noun right after an opening comma must be the thing actually doing the
  modifying action, or it's dangling.
- Pronouns must match antecedent in number and case. Possession: 's = one owner, s' = multiple.
- **"Odd one out" shortcut:** in verb-form questions, if 3 choices are singular and 1 is
  plural, the plural one is usually correct (the test can't have two "correct" singular options).
- Commonly missed: Verb Count/Tense (even grammar-confident students lose points here by not
  isolating the true subject) and Non-essential Info.

### "All of SAT Transitions Explained in 11 Minutes" (satgamified) — full
- **Visualization strategy:** mentally picture the scene/action in each sentence to feel the
  logical relationship, rather than abstractly parsing grammar.
- **Prediction method:** predict the relationship/word before viewing answer choices — stops
  you from being swayed by plausible-but-wrong distractor transitions.
- Categories: **Contradiction** (however, nevertheless, on the other hand) · **Cause & Effect**
  (therefore, consequently, thus) · **Specification** (for example, specifically) ·
  **Agreement/Addition** (similarly, moreover, in addition) · **Sequencing** (then, afterward).

### Cross-cutting signal (appeared across videos → high test-value)
- **"However"** shows up as its own dedicated punctuation-placement rule *and* as the flagship
  Contradiction-category example — strong signal it's heavily tested.
- **Predict-before-you-look** is the shared meta-strategy for both grammar and transitions —
  mechanical rule application over "vibes."
- Punctuation, verbs, and transitions are the three pillars to prioritize.

### ⚠️ Missing: punctuation-specific deep dive
"The Last SAT Punctuation Guide You'll Need" (James Lu, WL61t23IOyE) **failed to process** —
every yt-analysis call returned `400 INVALID_ARGUMENT` (distinct from the quota errors seen
elsewhere, so likely a captions/transcript availability issue specific to this video, not just
rate-limiting). Given punctuation is confirmed as the majority-share Conventions topic, this
gap should be filled — either retry this video later, or swap in an alternate punctuation-only
video (e.g. Penguin's "All of SAT Punctuation Explained in Under 4 Minutes" or satgamified's
"All SAT Punctuation Rules in 15 Minutes").

---

## 3. Reading & Writing strategy (2/3 videos processed)

### "All of SAT Reading & Writing in 22 Minutes (2026)" (satgamified) — full
Question-first approach throughout — read the question before the passage/notes to know the
goal.

| Type | Strategy |
|---|---|
| Words in Context | Summarize each sentence in your own words as you read; predict the word before viewing choices; use prefix/root/suffix knowledge to decode unfamiliar options. |
| Grammar | (see Conventions section above — same rule set) |
| Transitions | Summarize the logical relationship, predict the transition before viewing choices. Buckets: Contradiction, Cause & Effect, Specification. |
| Student Notes | Skip the passage/notes; read only the stated goal; pick the choice that directly satisfies it. |
| Passage Questions (main idea/inference/purpose, Command of Evidence) | Question → Passage → Prediction → **Elimination** (focus on disqualifying unsupported choices, not hunting for "the right one"). For data/graphs: don't pre-study the graph — only consult it to verify a specific choice. |

No explicit per-passage timing or paired-passage/dual-text guidance given in this video.

### "Every SAT Reading Strategy in 22 Minutes" (satgamified) — full
- Grammar: "glance, then read" — scan choices to see what's being tested, then read only the
  blank's sentence. Same verb "odd one out" shortcut as the Grammar video (~5-second check).
- Passage/inference: full sentence-by-sentence mental rephrasing as you read; only pick answers
  with **direct textual support** — eliminate anything requiring an outside assumption.
- Command of Evidence: identify whose claim needs supporting evidence first; "graph minimalism"
  — consult data only to verify, not to pre-analyze.
- Transitions: same predict-first method, simplified to "but" vs. "so" style categorization.
- Student Notes: goal-oriented — find the choice that accomplishes the stated goal.
- **Words in Context — "blanking" technique:** cover the vocab word, think of a simple/"dumb"
  synonym that fits (e.g. "important," "confusing"), then match that to the real answer choices.
  For negated/complex sentences, use the same rephrasing technique plus nearby descriptor
  context clues, falling back to roots/etymology if the choice word itself is unfamiliar.
- Trap-answer framing: choices that "sound right" without answering the specific question asked
  (analogy given: looks appealing on the menu but isn't what was ordered).

### ⚠️ Missing: full-test structural overview
"EVERYTHING You Need to Know about the SAT (2026)" (satgamified, 9IC3WMCAAwc) — **not
processed**, blocked by yt-analysis quota exhaustion before any content came through. This was
meant to cover section/module structure, adaptive-difficulty mechanics, timing, question counts
per domain, and scoring range mechanics — useful as the structural backbone for the whole
course. Needs a retry pass.

---

## 4. August-specific strategy & predictions — ❌ NOT PROCESSED (0/5 videos)

All five hit the yt-analysis MCP quota wall with zero content extracted. **Nothing below
should be treated as real signal — none of it exists yet.** Needs a full retry once the
tool issue clears:

1. "If You're Taking the August SAT, Study This" (satgamified) — https://www.youtube.com/watch?v=4uDfg3kw_HA
   — flagged a different error signature (`400 INVALID_ARGUMENT`, not quota) on its very first
   attempt, so may need investigation beyond just waiting for quota reset.
2. "How to Ace the August SAT in 2 Months" (satgamified) — https://www.youtube.com/watch?v=kUNjqVEX8WU
3. "Taking the August SAT? Here's Your 2-Week Survival Plan" (satgamified) — https://www.youtube.com/watch?v=nsjfDB1ybDE
4. "August 2026 SAT Predictions" (Penguin Test Prep) — https://www.youtube.com/watch?v=I8a7nmOAeB0
   — this was meant to be the actual predicted-content list; still needed.
5. "Timed SAT Test Walkthrough | Got a 1580" (James Lu) — https://www.youtube.com/watch?v=1UGO6uXnbgk
   — real-time pacing/tactics from an actual timed Bluebook run; still needed for test-taking
   strategy ahead of Donovan's own timed practice test.

---

## Status / what's still missing (retry checklist)

- [ ] August-specific cluster (5 videos, all zero data) — retry once yt-analysis quota resets
      (appears to be a daily cap; try tomorrow).
- [ ] "EVERYTHING You Need to Know about the SAT (2026)" — structural/scoring overview, retry.
- [ ] "The Last SAT Punctuation Guide You'll Need" — distinct tool error (not quota); may need
      a substitute video instead of a retry.
- [ ] "If You're Taking the August SAT, Study This" — same distinct error signature as above on
      first attempt before quota hit; worth checking if it's a captions-availability issue.
- [ ] General (non-video) SAT research pass — official College Board released-test analysis,
      question banks, released-test repos — not yet started (separate from this video pass,
      per the earlier scoping conversation).
- [ ] Research-tooling scouting (repos/tools to improve research capability, both general and
      SAT-content-sourcing specific) — not yet started.
