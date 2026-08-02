---
tags: [pytheas, sat, math, linear-equations, course]
created: 2026-08-02
status: template — pending review
---

# SAT Math — Unit 1 Notes: Linear Equations, Systems, and Slope-Intercept Form
**Domain: Algebra (formerly "Heart of Algebra") | ~35% of the Math section | Test date: 2026-08-22**

---

## Diagnostic: your specific weak spots (real data, 2026-08-02)

Source: two official College Board score reports (Dec 6, 2025 and
Mar 14, 2026). Full analysis: [[../SAT Diagnostic — Score History and Domain Analysis|SAT Diagnostic — Score History and Domain Analysis]].

- **Algebra performance band dropped between sittings: 680-800 (Dec) →
  610-670 (Mar)** — a full band, at the highest question weight in Math
  (35%, 13-15 questions). This is *not* your most consistently weak
  domain (Advanced Math and Standard English Conventions were mid-band
  on both tests, which is a stronger signal of a real gap) — but a drop
  at this weight is worth a genuine review pass, not just confidence.
- Your total score was **identical (1280) across both sittings** while
  Math gained 30 and Reading & Writing lost 30 — the flat total plus
  large swings in individual domains (this one included) points more
  toward **pacing/consistency issues than missing knowledge**. Practical
  read: you likely know this material — the Progress Check below should
  be run **timed**, and any misses should go in the error log to check
  for a pattern (careless sign errors, running out of time, second-guessing) rather than assuming you need to relearn the concept.
- Priority ranking across all 8 SAT domains for the ~20 days remaining
  puts this unit **3rd**, behind Advanced Math and Standard English
  Conventions (both consistently mid-band, not just volatile) — see the
  diagnostic doc for the full ordering.

---

## Quick Reference — the whole unit on one screen

> [!check] The four forms of a line
> | Form | Equation | Use it when |
> |---|---|---|
> | Slope-intercept | $y = mx + b$ | You know slope + y-intercept, or need to read them off fast |
> | Point-slope | $y - y_1 = m(x - x_1)$ | You know a slope and **any** one point |
> | Standard | $Ax + By = C$ | Elimination, and finding intercepts quickly |
> | Two-point slope | $m = \dfrac{y_2 - y_1}{x_2 - x_1}$ | You're given two points and nothing else |

> [!check] Slope relationships
> - **Parallel:** $m_1 = m_2$ (same slope, different intercept)
> - **Perpendicular:** $m_1 m_2 = -1$, i.e. $m_2 = -\dfrac{1}{m_1}$ (negative *reciprocal* — flip **and** change sign)
> - Horizontal line $y = k$: slope $0$. Vertical line $x = k$: slope **undefined** (not zero).

> [!check] System outcome test (memorize this — it's ~1 question per test)
> For $a_1x + b_1y = c_1$ and $a_2x + b_2y = c_2$:
> - $\dfrac{a_1}{a_2} \neq \dfrac{b_1}{b_2}$ → **exactly one solution** (lines cross once)
> - $\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} \neq \dfrac{c_1}{c_2}$ → **no solution** (parallel, never meet)
> - $\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} = \dfrac{c_1}{c_2}$ → **infinitely many solutions** (same line twice)

> [!warning] Trap — "slope vs. intercept in context"
> In $C = 18m + 25$, the **25 is the one-time/starting amount** and the **18 is the per-unit rate**. The SAT writes distractors that swap them. Ask: "which number is attached to the variable?" That one is always the rate of change.

> [!danger] Critical — sign errors in elimination
> When you subtract equations, distribute the minus sign to **every** term on both sides. More than half of missed Algebra questions at the 1300 level are arithmetic, not conceptual. Prefer **adding** a negated equation over subtracting.

---

## Topic 1.1: Solving Linear Equations in One Variable

**What the test actually asks:** solve for $x$; solve for a variable in terms of others (literal equations); or determine what value of a constant makes an equation have no solution / infinitely many solutions.

**Standard procedure:**
1. Distribute to clear parentheses.
2. Clear fractions by multiplying **every** term by the LCD.
3. Collect variable terms on one side, constants on the other.
4. Divide by the coefficient.

$$3(x - 4) = 2x + 5 \;\Rightarrow\; 3x - 12 = 2x + 5 \;\Rightarrow\; x = 17$$

**One-variable equations with no / infinite solutions:**
- If the variable terms cancel and you're left with a **false** statement ($0 = 7$) → **no solution**.
- If you're left with a **true** statement ($0 = 0$) → **infinitely many solutions** (identity).
- Setup: $ax + b = cx + d$ has no solution when $a = c$ and $b \neq d$; infinitely many when $a = c$ **and** $b = d$.

**Literal equations:** treat every other letter as a number. To solve $P = 2\ell + 2w$ for $w$: $w = \dfrac{P - 2\ell}{2}$. Don't "cancel" a term that is added — only factors cancel.

---

## Topic 1.2: Slope-Intercept Form, $y = mx + b$

- $m$ = **slope** = rate of change = rise/run = "how much $y$ changes when $x$ increases by 1."
- $b$ = **y-intercept** = value of $y$ when $x = 0$ = starting value.

**Getting to slope-intercept from standard form** — solve for $y$:
$$4x + 2y = 10 \;\Rightarrow\; 2y = -4x + 10 \;\Rightarrow\; y = -2x + 5$$
Slope $-2$, y-intercept $5$.

**Fast facts you should be able to state without writing anything:**
- Slope from $Ax + By = C$ is $m = -\dfrac{A}{B}$. (Useful for parallel/perpendicular questions — no need to solve for $y$.)
- x-intercept: set $y = 0$. y-intercept: set $x = 0$.
- Positive $m$ rises left→right; negative $m$ falls; $|m|$ large = steep.

---

## Topic 1.3: Point-Slope Form

$$y - y_1 = m(x - x_1)$$

Use it any time you have **a slope and a point**. It is faster than plugging into $y = mx + b$ and solving for $b$, and it produces fewer sign errors.

Example: slope $-\frac{4}{3}$ through $(6, -1)$:
$$y + 1 = -\tfrac{4}{3}(x - 6) \;\Rightarrow\; y = -\tfrac{4}{3}x + 8 - 1 \;\Rightarrow\; y = -\tfrac{4}{3}x + 7$$

**Sign trap:** $x - x_1$ with $x_1 = -2$ becomes $x + 2$. The formula has a *minus* built in; a negative coordinate flips it to a plus.

---

## Topic 1.4: Parallel and Perpendicular Lines

| Relationship | Slope rule | Intercept |
|---|---|---|
| Parallel | $m_2 = m_1$ | must differ (else same line) |
| Perpendicular | $m_2 = -1/m_1$ | anything |
| Same line | $m_2 = m_1$ | $b_2 = b_1$ |

- Perpendicular to slope $\frac{1}{5}$ → slope $-5$. Perpendicular to slope $-\frac{2}{3}$ → slope $\frac{3}{2}$.
- Perpendicular to a **horizontal** line is **vertical** ($x = k$), and vice versa — the $m_1m_2 = -1$ rule does not apply because one slope is undefined.

---

## Topic 1.5: Systems of Two Linear Equations

### Substitution
Best when one equation is already solved for a variable, or a coefficient is $1$ or $-1$.
1. Solve one equation for the easiest variable.
2. Substitute into the other equation (use parentheses).
3. Solve, then back-substitute for the second variable.

### Elimination
Best when the equations are both in $Ax + By = C$ form.
1. Scale one or both equations so one variable's coefficients are opposites.
2. **Add** the equations.
3. Solve, back-substitute.

$$\begin{aligned} 2x + 3y &= 12 \\ 4x - 3y &= 6 \end{aligned} \;\xrightarrow{\text{add}}\; 6x = 18 \;\Rightarrow\; x = 3,\; y = 2$$

### The shortcut the SAT rewards
Many system questions ask for **$x + y$** or **$2x - y$**, not for $x$ and $y$ separately. Try adding or subtracting the two equations *as given* first — often the requested combination falls out in one step with no solving at all.

### No solution / infinitely many (constant-hunting questions)
When a system contains a constant $k$ and the question says "the system has no solution," set the **coefficient ratios equal** and confirm the constant ratio does **not** match:
$$\begin{aligned} kx - 2y &= 8 \\ 6x - 4y &= 10 \end{aligned} \quad \frac{k}{6} = \frac{-2}{-4} = \frac12 \Rightarrow k = 3, \quad \text{check } \frac{8}{10} \neq \frac12 \;\checkmark$$

Geometric meaning: **no solution = parallel lines**; **infinitely many = the same line written twice**; **one solution = one intersection point**.

---

## Topic 1.6: Writing Linear Models from Word Problems

**The two-question method** — for any "cost/distance/amount" story:
1. *What am I charged/given even if the variable is zero?* → that's $b$.
2. *What changes per unit?* → that's $m$.

| Story phrase | Translates to |
|---|---|
| "a one-time fee of \$25" | $b = 25$ |
| "\$18 per month" | $m = 18$ |
| "decreases by 4 gallons each hour" | $m = -4$ |
| "initially / at the start / already has" | $b$ |
| "for each additional…" | $m$ |
| "total of 500 tickets" | $a + s = 500$ (a counting equation) |
| "total revenue of \$5100" | $12a + 7.5s = 5100$ (a value equation) |

**Two-equation word problems almost always pair one *counting* equation with one *value* equation.** Write both before doing any algebra.

**Interpretation questions** ("what does the 18 represent?") expect a full sentence in context, with **units**: "the monthly cost of the membership, in dollars." A distractor will describe the intercept instead.

---

## Topic 1.7: Interpreting Graphs of Linear Equations

- **y-intercept** = where the line hits the vertical axis = the model's starting value.
- **x-intercept** = where the quantity reaches zero (tank empty, debt paid off, break-even).
- **Slope** = the units on the vertical axis **per** the units on the horizontal axis. Always name it that way: "dollars per month," "meters per second."
- **Intersection of two lines on a graph** = the solution to the system = the moment/quantity at which two models are equal (break-even point).
- A **steeper** line has larger $|m|$; if two plans are graphed, the steeper one overtakes the other after their intersection.

**Reading points off a graph:** the SAT often gives a graph with a labeled point and asks for the equation. Get slope from two lattice points (points on exact grid intersections), then read $b$ directly off the axis.

---

## Digital SAT test theory — this domain

**How much it's worth.** The digital SAT Math section is 2 adaptive modules × 22 questions = **44 questions in 70 minutes** (~95 seconds per question average). The **Algebra** domain — this unit's content plus linear inequalities and linear functions — is about **35% of the Math section, roughly 13–15 questions**. Linear equations, systems, and slope account for the large majority of those. There is no faster point-per-hour-of-study content on the test.

**Where a 1310 typically leaks points here.** Not on concept — on execution. The three recurring failure modes:
1. **Sign errors in elimination**, especially when subtracting equations. Fix: multiply through by $-1$ and *add* instead of subtracting.
2. **Slope/intercept swap in context questions.** Fix: the number multiplied by the variable is always the rate.
3. **No-solution / infinite-solution setups.** Students solve for $x$ instead of comparing ratios, burn 2 minutes, and guess. Fix: recognize the "for what value of $k$…" phrasing instantly and go straight to the ratio test.

Two more worth naming: **answering the wrong quantity** (question asks for $x + y$, you bubble $x$), and **dropping units or a negative sign** in a student-produced response.

**Student-produced response (SPR) mechanics.** ~25% of Math questions are grid-ins. Negatives are allowed. No commas, no percent signs, no mixed numbers ($1\frac12$ must be entered as `3/2` or `1.5`). Answers may be fractions or decimals; if a decimal doesn't terminate, enter it truncated or rounded to fill the field. If more than one value satisfies the question, enter only one.

**Desmos (built into the test app) — where it actually helps in this unit:**
- **Systems:** type both equations, click the intersection point. Exact coordinates appear. This is often faster and always safer than elimination, and it fully removes the sign-error risk.
- **Verifying an answer choice:** graph your derived line and the given point; confirm the point is on it.
- **No-solution questions:** graph both lines with a slider on $k$ and watch for the moment they become parallel.
- **Where Desmos is *slower*:** literal equations, "interpret the meaning of…" questions, and any question with variables in the answer choices. Solve those by hand.
- **Cost:** typing an equation into Desmos takes ~15–20 seconds. Worth it for systems and messy fractions; not worth it for one-step solves.

**Pacing.** Target ~60–75 seconds on Algebra questions in Module 1 so you bank time for the harder back half. If a linear question passes ~2 minutes, mark and move — the digital SAT lets you flag and return within the module, but not across modules. Module 1's performance determines whether Module 2 is the harder (higher-scoring) form, so accuracy on these routine questions in Module 1 is disproportionately valuable.

---

## Pattern Recognition — Unit 1

| If you see… | It's testing… | Key move |
|---|---|---|
| "For what value of $k$ does the system have no solution?" | Coefficient ratio test | $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$ |
| "…infinitely many solutions" | Same line | All three ratios equal |
| "What is the value of $x + y$?" | Combination shortcut | Add/subtract the equations as given first |
| Two points given, asked for equation | Slope formula + point-slope | $m = \frac{\Delta y}{\Delta x}$, then $y - y_1 = m(x-x_1)$ |
| "Line $\ell$ is perpendicular to…" | Negative reciprocal | Flip **and** negate |
| Given $Ax + By = C$, asked for slope | Rearranging | $m = -A/B$, don't fully solve |
| "What does the number 25 represent?" | Slope vs. intercept in context | The number *not* attached to a variable is the starting value |
| Story with "total items" + "total cost" | Two-equation system | One counting equation, one value equation |
| Graph with two lines, "when are they equal?" | Intersection = solution | Read the intersection point |
| "…crosses the x-axis at" | x-intercept | Set $y = 0$ |
| Equation with variable on both sides, asked "no solution" | One-variable identity | Same coefficient, different constant |

---

## Critical Reminders — Unit 1

> [!danger] Perpendicular means flip AND negate
> The negative reciprocal of $\frac{2}{3}$ is $-\frac{3}{2}$ — not $\frac{3}{2}$ and not $-\frac{2}{3}$. Both partial moves appear as answer choices.

> [!warning] Vertical lines have undefined slope, not zero slope
> $x = 4$ is vertical, slope undefined. $y = 4$ is horizontal, slope $0$. These are swapped in distractors constantly.

> [!warning] Answer the question that was asked
> Circle the requested quantity ($x$? $y$? $x+y$? $2x$?) before you start solving. On grid-ins there is no answer choice to catch the mistake.

> [!check] Add a negated equation instead of subtracting
> $\text{Eq1} - \text{Eq2}$ becomes $\text{Eq1} + (-1)\cdot\text{Eq2}$. One extra line of writing removes the single most common error in this domain.

> [!check] Plug your answer back in
> A 10-second substitution check catches nearly every arithmetic slip. Budget for it on grid-ins specifically, where partial recognition is impossible.

> [!check] Desmos is a checking tool, not a first resort
> Solve algebraically, then verify with a graph when time allows. Reaching for Desmos first on every question is the most common pacing mistake on the digital format.
