---
tags: [pytheas, sat, math, linear-equations, course]
created: 2026-08-02
status: template — pending review
---

# SAT Math — Unit 1 Examples: Linear Equations, Systems, and Slope-Intercept Form
**8 worked problems, easy → hard | MC = multiple choice, SPR = student-produced response**

---

## Example 1 — Solving a linear equation (Easy, MC)

$$3(x - 4) = 2x + 5$$

What is the value of $x$?

(A) $-17$  (B) $1$  (C) $9$  (D) $17$

**Solution**

Distribute the 3:
$$3x - 12 = 2x + 5$$

Subtract $2x$ from both sides:
$$x - 12 = 5$$

Add 12:
$$x = \mathbf{17}$$

Check: $3(17-4) = 3(13) = 39$ and $2(17)+5 = 39$ ✓

**Answer: D**

> *Why this trap exists:* choice (C) is what you get if you distribute the 3 to only the $x$ and forget the $-4$ ($3x - 4 = 2x + 5 \Rightarrow x = 9$). Distribution errors are the #1 source of missed easy questions.

---

## Example 2 — Slope and intercept from standard form (Easy, SPR)

Line $\ell$ is defined by $4x + 2y = 10$. What is the slope of line $\ell$?

**Solution**

Solve for $y$:
$$2y = -4x + 10 \;\Rightarrow\; y = -2x + 5$$

Slope $m = \mathbf{-2}$ (y-intercept is 5).

*Faster route:* from $Ax + By = C$, $m = -\dfrac{A}{B} = -\dfrac{4}{2} = -2$. No rearranging needed.

**Answer: −2** (negatives are permitted in the grid-in field)

> *Why this trap exists:* students read "$4x$" and answer $4$, or answer $-4$ having forgotten to divide by $B$. The coefficient of $x$ in standard form is **not** the slope.

---

## Example 3 — Building a linear model from context (Easy–Medium, MC)

A gym charges a one-time registration fee of \$25 plus \$18 for each month of membership. Which equation gives the total cost $C$, in dollars, for $m$ months of membership?

(A) $C = 25m + 18$
(B) $C = 18m + 25$
(C) $C = 43m$
(D) $C = 18(m + 25)$

**Solution**

Apply the two-question method:
- *Cost when $m = 0$?* The \$25 registration fee is charged regardless → $b = 25$.
- *What changes per month?* \$18 → $m$-coefficient $= 18$.

$$C = 18m + 25$$

Sanity check at $m = 3$: $18(3) + 25 = 79$. By hand: \$25 + \$54 = \$79 ✓

**Answer: B**

> *Why this trap exists:* (A) is the slope/intercept swap — the single most common context error in this domain. (C) adds the fee to the rate as if the registration were monthly.

---

## Example 4 — System by elimination (Medium, SPR)

$$\begin{aligned} 2x + 3y &= 12 \\ 4x - 3y &= 6 \end{aligned}$$

If $(x, y)$ is the solution to the system, what is the value of $x + y$?

**Solution**

The $y$-coefficients are already opposites. **Add** the equations:
$$6x = 18 \;\Rightarrow\; x = 3$$

Back-substitute into the first equation:
$$2(3) + 3y = 12 \;\Rightarrow\; 3y = 6 \;\Rightarrow\; y = 2$$

$$x + y = 3 + 2 = \mathbf{5}$$

Check in the second equation: $4(3) - 3(2) = 12 - 6 = 6$ ✓

**Answer: 5**

> *Why this trap exists:* the question asks for $x + y$, not $x$. A student who solves correctly and grids `3` gets it wrong with no answer choice to catch them. Circle the requested quantity before solving.

---

## Example 5 — Perpendicular line through a point (Medium, MC)

In the $xy$-plane, line $k$ is perpendicular to the line $y = \frac{3}{4}x + 2$ and passes through the point $(6, -1)$. What is the y-intercept of line $k$?

(A) $-9$  (B) $-1$  (C) $7$  (D) $\frac{25}{4}$

**Solution**

Perpendicular slope = negative reciprocal of $\frac34$:
$$m_k = -\frac{4}{3}$$

Point-slope through $(6, -1)$:
$$y - (-1) = -\tfrac{4}{3}(x - 6)$$
$$y + 1 = -\tfrac{4}{3}x + 8$$
$$y = -\tfrac{4}{3}x + 7$$

y-intercept $= \mathbf{7}$.

Check: at $x = 6$, $y = -8 + 7 = -1$ ✓

**Answer: C**

> *Why this trap exists:* (D) comes from using the **parallel** slope $\frac34$ instead of the perpendicular one. (B) comes from confusing the given point's $y$-value with the intercept.

---

## Example 6 — No-solution system (Medium–Hard, SPR)

$$\begin{aligned} kx - 2y &= 8 \\ 6x - 4y &= 10 \end{aligned}$$

In the system of equations above, $k$ is a constant. If the system has no solution, what is the value of $k$?

**Solution**

No solution means the lines are **parallel**: coefficient ratios equal, constant ratio different.

$$\frac{k}{6} = \frac{-2}{-4} = \frac{1}{2} \;\Rightarrow\; k = 3$$

Verify the constants do **not** match that ratio: $\dfrac{8}{10} = \dfrac{4}{5} \neq \dfrac{1}{2}$ ✓ — so the lines are genuinely parallel, not identical, and the system has no solution.

**Answer: 3**

*Alternate route (slope comparison):* $kx - 2y = 8 \Rightarrow y = \frac{k}{2}x - 4$; $6x - 4y = 10 \Rightarrow y = \frac32 x - \frac52$. Parallel requires $\frac{k}{2} = \frac32 \Rightarrow k = 3$, with different intercepts ($-4 \neq -\frac52$) ✓

> *Why this trap exists:* students try to solve the system for $x$ and $y$, which is impossible and burns 2+ minutes. Recognizing "for what value of $k$… no solution" as a **ratio question**, not a solving question, is the entire skill.

---

## Example 7 — Two-equation word problem (Hard, MC)

A theater sold a total of 500 tickets to a performance. Adult tickets cost \$12 each and student tickets cost \$7.50 each. The total revenue from ticket sales was \$5,100. How many adult tickets were sold?

(A) 200  (B) 250  (C) 300  (D) 350

**Solution**

Define: $a$ = adult tickets, $s$ = student tickets.

Counting equation: $a + s = 500$
Value equation: $12a + 7.5s = 5100$

Substitute $s = 500 - a$:
$$12a + 7.5(500 - a) = 5100$$
$$12a + 3750 - 7.5a = 5100$$
$$4.5a = 1350$$
$$a = \mathbf{300}$$

Then $s = 200$. Check: $12(300) + 7.5(200) = 3600 + 1500 = 5100$ ✓

**Answer: C**

> *Why this trap exists:* (A) is $s$, the other variable — correct work, wrong quantity reported. Label your variables explicitly with what they count, then re-read the final question before choosing.

---

## Example 8 — Interpreting a linear model and its graph (Hard, MC + SPR pair)

A water tank is being drained. The volume of water $W$, in gallons, remaining in the tank after $t$ hours is modeled by
$$W = 240 - 8t$$

**Part (a) — MC:** Which of the following is the best interpretation of the number 8 in this model?

(A) The tank initially holds 8 gallons.
(B) The tank drains at a rate of 8 gallons per hour.
(C) The tank is empty after 8 hours.
(D) The tank drains 8 gallons in total.

**Part (b) — SPR:** After how many hours does the tank contain 96 gallons?

**Solution — (a)**

Rewrite as $W = -8t + 240$. The coefficient attached to $t$ is the **rate of change**: $-8$ gallons per hour. Since $W$ is decreasing, the magnitude 8 is the draining rate.

**Answer: B**

**Solution — (b)**

$$96 = 240 - 8t$$
$$8t = 240 - 96 = 144$$
$$t = \mathbf{18}$$

Check: $240 - 8(18) = 240 - 144 = 96$ ✓

**Answer: 18**

**Graph reading, same model:** the y-intercept $(0, 240)$ is the starting volume; the x-intercept is found by setting $W = 0$: $t = 240/8 = 30$ hours, the moment the tank is empty. The line falls left-to-right because the slope is negative.

> *Why this trap exists:* (A) reports the slope as the intercept; (C) confuses the coefficient 8 with the x-intercept (which is actually 30). Every distractor here is a real number **from the problem** attached to the wrong meaning — the SAT builds interpretation distractors this way almost every time.

---

## Desmos check on these

- **Ex. 4:** type both equations, click the intersection dot → $(3, 2)$ appears. Then add $3 + 2$ mentally. ~20 seconds, zero sign risk.
- **Ex. 6:** define $k$ with a slider, drag until the lines visibly become parallel → lands on 3. Good confirmation, slower than the ratio test.
- **Ex. 8:** graph $y = 240 - 8x$ and $y = 96$, click intersection → $(18, 96)$.
- **Ex. 3, 8(a):** Desmos is no help — these are interpretation questions. Solve by reasoning.
