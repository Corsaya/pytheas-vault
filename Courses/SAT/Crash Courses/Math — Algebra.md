---
tags: [pytheas, sat, math, algebra, crash-course]
created: 2026-08-12
source: "Foundations Knowledge Check A1-A10"
related: ["[[../Foundations Knowledge Check]]", "[[../Diagnostic Gap Lessons (2026-08-07)]]"]
---

# Math — Algebra Crash Course

Algebra is the single biggest domain on the digital SAT math section — roughly
**35% of the test (13–15 questions)**, per
[[../Research/Official SAT Structure and Content Research (2026-08-07)]] — and this
doc covers all 10 skills (A1–A10) from the
[[../Foundations Knowledge Check]] in one pass.

---

### A1 — Solve a linear equation in one variable

**What this actually tests:** can you isolate a variable through a clean, ordered
sequence of inverse operations, including when there's distribution or
like-terms cleanup first. This is the single most repeated mechanical skill
underneath half the other Algebra skills (A3, A5, A6, A9 all end in "now solve
a linear equation").

**The core method:**
1. Distribute anything in parentheses.
2. Combine like terms on each side separately.
3. Move variable terms to one side, constants to the other (add/subtract).
4. Divide by the coefficient on the variable.
5. Check by plugging back into the *original* equation, not a middle step.

**Worked example:** Solve $3(x-2) + 5 = 2x + 7$.
$$3x - 6 + 5 = 2x + 7$$
$$3x - 1 = 2x + 7$$
$$x = 8$$
Check: $3(8-2)+5 = 3(6)+5 = 23$, and $2(8)+7 = 23$. Matches.

**Trips people up:** distributing a negative sign — $-2(x-4)$ becomes
$-2x+8$, not $-2x-8$. Do the distribution as its own written step instead of
in your head when there's a negative out front.

---

### A2 — Solve a linear inequality in one variable

Same steps as A1, with one extra rule: dividing or multiplying both sides by a
**negative number flips the inequality sign**. This is already covered in full
(rule, worked example, and a 4-question drill) in
[[../Diagnostic Gap Lessons (2026-08-07)#Lesson 2 — Algebra: the inequality-flip rule]]
— go there for the complete lesson instead of a rewrite here.

---

### A3 — Build a linear equation/inequality from a word problem

**What this actually tests:** translating English into algebra — identifying
the *fixed* part (a flat fee, a starting amount) versus the *variable* part
(a per-unit rate times a quantity), then setting up the equation before
solving anything.

**The core method:**
- Find the flat/starting value — it stands alone, no variable attached.
- Find the rate — it's always multiplied by the changing quantity.
- Assemble: **total = flat amount + (rate × quantity)**, or as an inequality
  if the problem says "at least," "at most," "no more than," etc.
- Only then solve using A1/A2 mechanics.

**Worked example:** A phone plan charges a flat fee of \$20 plus \$0.10 per
minute. A bill came to \$35.50. How many minutes were used?
$$20 + 0.10m = 35.50$$
$$0.10m = 15.50$$
$$m = 155 \text{ minutes}$$

**Trips people up:** watch for inequality keywords ("no more than" → $\le$,
"at least" → $\ge$, "more than"/"fewer than" → strict $<$/$>$) — the SAT tests
whether you know these translate to non-strict vs. strict inequalities, not
just that you can solve the equation.

---

### A4 — Interpret slope and y-intercept in context

**What this actually tests:** reading a linear model $y = mx + b$ (or any
letters standing in for $x$ and $y$) and stating what $m$ and $b$ *mean in the
real-world scenario*, not just naming them "slope" and "intercept."

**The core method:**
- $b$ (or whatever term stands alone, no variable) = the **starting value** —
  what's true at time zero / quantity zero.
- $m$ (the coefficient multiplying the variable) = the **rate of change** —
  how much $y$ changes per one unit of $x$. Sign matters: positive = increasing,
  negative = decreasing.
- Always attach units from the problem when stating the interpretation.

**Worked example:** A tank's water level (in gallons), $t$ minutes after a
drain valve opens, is modeled by $L = 50 - 2t$. Interpret the slope and the
$y$-intercept.
- $y$-intercept $50$: the tank starts with 50 gallons before draining begins.
- Slope $-2$: the water level decreases by 2 gallons every minute.

**Trips people up:** the sign of the slope is not optional in the answer —
"the level changes by 2 gallons per minute" is an incomplete/wrong answer on
a question where direction (draining vs. filling) is part of what's being
tested.

---

### A5 — Solve a system of two linear equations (substitution)

**What this actually tests:** using one equation (already solved, or easy to
solve, for one variable) to eliminate that variable from the other equation,
collapsing two unknowns into one.

**The core method:**
1. Solve one equation for one variable, if it isn't already.
2. Substitute that expression into the *other* equation everywhere that
   variable appears.
3. Solve the resulting one-variable equation (A1 mechanics).
4. Plug that value back into either original equation to get the second
   variable.

**Worked example:** Solve $y = 2x + 1$ and $3x + y = 16$.
$$3x + (2x+1) = 16$$
$$5x + 1 = 16$$
$$x = 3, \quad y = 2(3)+1 = 7$$
Check in the other equation: $3(3) + 7 = 16$. Matches.

**Trips people up:** substitute into the equation you *didn't* use to solve
for the variable — plugging back into the same equation you started from just
gives you a trivially true statement (like $0=0$), not an answer.

---

### A6 — Solve a system of two linear equations (elimination)

**What this actually tests:** the same underlying idea as substitution
(collapse two variables into one) but by adding or subtracting the two
equations directly, after scaling one or both so a variable's coefficients
cancel.

**The core method:**
1. Look for a variable whose coefficients are already equal, or opposite,
   in the two equations (or multiply one/both equations by a constant to
   make that true).
2. Add the equations (if coefficients are opposite) or subtract (if equal) —
   one variable cancels out.
3. Solve the resulting one-variable equation.
4. Substitute back into either original equation for the second variable.

**Worked example:** Solve $3x + 2y = 12$ and $3x - 2y = 0$.
$$\underline{+\; (3x+2y) + (3x-2y) = 12 + 0}$$
$$6x = 12 \Rightarrow x = 2$$
$$3(2) - 2y = 0 \Rightarrow 2y = 6 \Rightarrow y = 3$$
Check in the first equation: $3(2)+2(3) = 6+6 = 12$. Matches.

**Trips people up:** when you scale an equation to set up cancellation, scale
*every term on both sides* — a common error is multiplying only the
left-hand side and forgetting the constant on the right.

---

### A7 — Determine when a linear system has no solution / infinite solutions

**What this actually tests:** recognizing that a system's solution count is
about how the two lines relate geometrically (crossing once, parallel, or
identical) — and that you can determine which case applies just from the
coefficients, without fully solving.

**The core rule:** write both equations in the same form (e.g. $Ax+By=C$).
Compare the ratios of corresponding coefficients:
- $\dfrac{A_1}{A_2} \ne \dfrac{B_1}{B_2}$ → lines cross once → **exactly one
  solution**.
- $\dfrac{A_1}{A_2} = \dfrac{B_1}{B_2} \ne \dfrac{C_1}{C_2}$ → same slope,
  different line → **no solution** (parallel).
- $\dfrac{A_1}{A_2} = \dfrac{B_1}{B_2} = \dfrac{C_1}{C_2}$ → literally the same
  line → **infinitely many solutions**.

**Worked example:** For what value of $k$ does this system have no solution?
$$kx + 6y = 12 \qquad 2x + 3y = 9$$
Set the variable-coefficient ratios equal: $\dfrac{k}{2} = \dfrac{6}{3} = 2
\Rightarrow k = 4$. Check the constant ratio doesn't also match:
$\dfrac{12}{9} = \dfrac{4}{3} \ne 2$ — confirmed, $k=4$ gives no solution
(parallel, non-identical lines).

**Trips people up:** these questions almost never ask you to actually solve
the system — they ask for the value of a constant that produces a *type* of
solution. Solving fully still works but wastes time; set up the ratio
comparison directly instead.

---

### A8 — Graph interpretation: find slope/intercept from a line's graph

**What this actually tests:** reading two clear points off a graphed line
(or a labeled point plus the $y$-intercept) and converting that into slope and
equation form — same math as A4/A5 but starting from a picture instead of an
equation.

**The core method:**
1. Identify two points the line clearly passes through (grid intersections
   are chosen deliberately so this is exact, not estimated).
2. Slope: $m = \dfrac{y_2-y_1}{x_2-x_1}$.
3. $y$-intercept: read directly where the line crosses the $y$-axis, or
   solve for $b$ using $y=mx+b$ and one known point if the intercept isn't
   a clean grid point.

**Worked example:** A line passes through $(-2, 5)$ and $(4, -7)$. Find its
slope and $y$-intercept.
$$m = \frac{-7 - 5}{4 - (-2)} = \frac{-12}{6} = -2$$
$$y - 5 = -2(x-(-2)) \Rightarrow y = -2x - 4 + 5 = -2x + 1$$
$y$-intercept is $1$. Check with $(4,-7)$: $-2(4)+1 = -7$. Matches.

**Trips people up:** it's easy to swap the order and compute $\frac{y_1-y_2}{x_2-x_1}$
by accident — keep the same point as "point 1" in both the numerator and
denominator.

---

### A9 — Linear function notation: evaluate f(x), interpret f(a)=b in context

**What this actually tests:** function notation is just a labeled equation —
$f(x)$ means "the output of the rule $f$ when the input is $x$." Evaluating
$f(4)$ means substitute $4$ for $x$; being told $f(a) = b$ means the *output*
is $b$ and you're solving for the input $a$.

**The core method:**
- $f(\text{number})$: substitute that number for $x$ everywhere, compute.
- $f(x) = \text{value}$: set the expression equal to that value, solve for
  $x$ (A1 mechanics) — this gives you the *input* that produces it.
- In a word problem, $f(\text{input})$ = output in the units given (cost,
  distance, height, etc.) — state both the number and what it means.

**Worked example:** A rental company charges $f(x) = 35x + 60$, where $x$ is
the number of days rented. Evaluate $f(5)$, then interpret what $f(x)=305$
means and solve for $x$.
$$f(5) = 35(5) + 60 = 235 \quad \text{(5 days costs \$235)}$$
$$35x + 60 = 305 \Rightarrow 35x = 245 \Rightarrow x = 7 \quad \text{(a \$305 bill means 7 days)}$$

**Trips people up:** $f(a) = b$ is frequently misread as "plug $b$ into $f$."
It's the reverse — $b$ is the *output*, $a$ is the *input* you're solving for.

---

### A10 — Absolute value equations — two-case solving

**What this actually tests:** absolute value strips a sign, so $|X| = n$
(for positive $n$) means the expression inside could have been $n$ *or*
$-n$ before the absolute value was applied. Both cases are real, separate
solutions unless one gets ruled out.

**The core method:**
1. Isolate the absolute value expression on one side, alone, first (if
   there's anything added/multiplied outside the bars).
2. Split into two equations: (inside) $= n$, and (inside) $= -n$.
3. Solve each normally (A1 mechanics).
4. Both answers are valid unless the problem gives an extra restriction that
   rules one out (e.g. "$x$ must be positive").

**Worked example:** Solve $|2x - 3| = 9$.
$$\text{Case 1: } 2x - 3 = 9 \Rightarrow x = 6$$
$$\text{Case 2: } 2x - 3 = -9 \Rightarrow x = -3$$
Check: $|2(6)-3| = |9| = 9$. $|2(-3)-3| = |-9| = 9$. Both valid.

**Trips people up:** if there's anything outside the bars (like
$|2x-3| + 4 = 13$), isolate the absolute value bars *first* ($|2x-3|=9$)
before splitting into two cases — splitting too early keeps the outside term
tangled into both branches incorrectly.

---

## Mini-Diagnostic

One question per skill, A1–A10. Answer key with brief solution steps is at
the bottom — don't peek until you've attempted all 10.

**A1.** Solve for $x$: $4(x+3) - 5 = 2x + 9$

**A2.** Solve: $6 - 3x > 18$

**A3.** A gym charges a \$25 sign-up fee plus \$15 per month. Write an
equation for total cost $C$ after $m$ months, and find how many months until
the total reaches \$175.

**A4.** A candle's height (in cm), $t$ hours after being lit, is modeled by
$h = 24 - 2t$. What does the value $2$ represent in this context, and how
tall is the candle after 6 hours?

**A5.** Solve the system using substitution: $y = 4x - 1$, $\;2x + y = 11$

**A6.** Solve the system using elimination: $5x + 2y = 16$, $\;3x - 2y = 0$

**A7.** For what value of $k$ does this system have no solution?
$$kx + 6y = 12 \qquad 2x + 3y = 9$$

**A8.** A line on a graph passes through $(-2, 5)$ and $(4, -7)$. Find its
slope and $y$-intercept.

**A9.** A ride-share fare is modeled by $f(x) = 2.5x + 4$, where $x$ is
miles traveled. Evaluate $f(6)$, then find $x$ if $f(x) = 26.5$.

**A10.** Solve $|5x - 10| = 30$.

---

### Answer key

**A1.** $4x+12-5=2x+9 \Rightarrow 4x+7=2x+9 \Rightarrow 2x=2 \Rightarrow x=1$

**A2.** $6-3x>18 \Rightarrow -3x>12 \Rightarrow x<-4$ (flipped — divided by $-3$)

**A3.** $C = 25+15m$. Set $175=25+15m \Rightarrow 150=15m \Rightarrow m=10$ months.

**A4.** $2$ = the burn rate, 2 cm lost per hour. $h(6)=24-2(6)=12$ cm.

**A5.** $2x+(4x-1)=11 \Rightarrow 6x=12 \Rightarrow x=2$, then $y=4(2)-1=7$.

**A6.** Add the equations: $8x=16 \Rightarrow x=2$. Then $3(2)-2y=0 \Rightarrow y=3$.

**A7.** $\dfrac{k}{2}=\dfrac{6}{3}=2 \Rightarrow k=4$ (and $\dfrac{12}{9}\ne 2$, confirming no solution rather than infinite).

**A8.** $m=\dfrac{-7-5}{4-(-2)}=\dfrac{-12}{6}=-2$. Using $(4,-7)$: $-7=-2(4)+b \Rightarrow b=1$. Slope $-2$, $y$-intercept $1$.

**A9.** $f(6)=2.5(6)+4=19$. For $f(x)=26.5$: $2.5x+4=26.5 \Rightarrow 2.5x=22.5 \Rightarrow x=9$ miles.

**A10.** $5x-10=30 \Rightarrow x=8$; $5x-10=-30 \Rightarrow x=-4$. Both check: $|5(8)-10|=30$, $|5(-4)-10|=30$.
