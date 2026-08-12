---
tags: [pytheas, sat, math, geometry, trigonometry, crash-course]
created: 2026-08-12
source: "Foundations Knowledge Check G1-G8"
related: ["[[../Foundations Knowledge Check]]", "[[../Research/Bluebook Parity, Khan Academy, Strategy, and Social Advice Research (2026-08-12)]]"]
---

# Math — Geometry & Trigonometry Crash Course

This domain is ~15% of the Math section (5–7 questions per the existing
[[../Research/Official SAT Structure and Content Research (2026-08-07)|Official SAT Structure research]]) — the smallest of the three math
domains, but a good one to lock down fast since most of it is either given
to you outright or a short, memorizable rule. Covers G1–G8 from the
[[../Foundations Knowledge Check]].

**The reference-sheet split — know this before you study anything below.**
Per the [[../Research/Bluebook Parity, Khan Academy, Strategy, and Social Advice Research (2026-08-12)|2026-08-12 research]], the digital SAT's
built-in reference sheet is **geometry-only** — about 15 formulas: area of a
rectangle/triangle/circle, circumference, volumes of a rectangular solid,
cylinder, sphere, cone, and pyramid, the Pythagorean theorem, both special
right triangle ratios (drawn out as diagrams), "a circle has 360° = 2π
radians," and "the angles of a triangle sum to 180°." That's it — nothing
about coordinate geometry, similarity, or trig is on it. Per skill:

| Skill | On the reference sheet? |
|---|---|
| G1 — area/volume formulas | **Yes, fully.** Every formula you need is given. |
| G2 — Pythagorean theorem + special right triangles | **Yes, fully.** Both the theorem and both triangle ratio diagrams are given. |
| G3 — arc length, sector area, central/inscribed angles | **Partially.** Circle area/circumference and "360° = 2π radians" are given; the arc-length/sector-area *proportion setup* and the central-inscribed angle relationship are **not** — you must know how to use the givens. |
| G4 — circle equation | **No.** Memorize $(x-h)^2+(y-k)^2=r^2$. |
| G5 — similar triangles | **No.** No proportion formula is given; know the method. |
| G6 — right-triangle trig (SOH-CAH-TOA) | **No.** Not on the sheet at all. |
| G7 — trig identities | **No.** Not on the sheet at all. |
| G8 — angle relationships | **Partially.** Triangle angle sum (180°) is given; parallel-line/transversal angle rules are **not**. |

So the real memorization load in this domain is G4, G5, G6, G7, and the
transversal half of G8 — five and a half items, not eight. The rest is
about recognizing *when* to reach for a formula that's already sitting in
front of you.

---

### G1 — Area/perimeter/volume formulas

**What this actually tests:** can you pick the right formula out of the
reference sheet and plug in correctly — including 3D shapes where it's easy
to mix up which dimension is which.

**Reference sheet:** ON it — rectangle, triangle, circle area/circumference,
and volumes of a rectangular solid, cylinder, sphere, cone, and pyramid are
all given formulas.

**Core rule:**
$$A_{\text{rect}} = lw \qquad A_{\text{triangle}} = \tfrac{1}{2}bh \qquad A_{\text{circle}} = \pi r^2 \qquad C = 2\pi r$$
$$V_{\text{rect. solid}} = lwh \qquad V_{\text{cylinder}} = \pi r^2 h \qquad V_{\text{sphere}} = \tfrac{4}{3}\pi r^3 \qquad V_{\text{cone}} = \tfrac{1}{3}\pi r^2 h$$

**Worked example:** A cylindrical water tank has radius 4 ft and height 9 ft.
Find its volume in terms of $\pi$.
$$V = \pi r^2 h = \pi (4)^2 (9) = \pi (16)(9) = 144\pi \text{ ft}^3$$

**Shortcut/trap:** the cone and pyramid volumes have an extra $\tfrac{1}{3}$
that the cylinder/rectangular-solid versions don't — it's easy to forget
that factor under time pressure even with the formula right in front of
you. Double-check you copied the whole formula, not just the shape part.

---

### G2 — Pythagorean theorem + special right triangles

**What this actually tests:** finding a missing side of a right triangle,
either generically or via the fixed ratios of 30-60-90 and 45-45-90
triangles (much faster than Pythagorean theorem when they apply).

**Reference sheet:** ON it — the theorem and both special-triangle diagrams
(with ratios labeled) are given.

**Core rule:**
$$a^2 + b^2 = c^2 \quad (c = \text{hypotenuse})$$
- **45-45-90:** legs are equal, ratio $x : x : x\sqrt{2}$ (leg : leg : hypotenuse).
- **30-60-90:** ratio $x : x\sqrt{3} : 2x$ (short leg opposite 30° : long leg opposite 60° : hypotenuse).

**Worked example:** A 30-60-90 triangle has a short leg of 5. Find the
hypotenuse and long leg.
Using $x : x\sqrt{3} : 2x$ with $x = 5$: hypotenuse $= 2(5) = 10$, long leg
$= 5\sqrt{3}$.

**Shortcut/trap:** recognizing a special triangle (angles given, or side
ratios that look like $1:\sqrt3:2$ or equal legs) saves a full Pythagorean
calculation — but if you're not sure it's actually 30-60-90 or 45-45-90,
Pythagorean theorem always works and never assumes an angle you haven't
confirmed.

---

### G3 — Circle theorems: arc length, sector area, central/inscribed angles

**What this actually tests:** treating an arc or sector as a *fraction of
the whole circle*, and knowing the fixed 2:1 relationship between a central
angle and the inscribed angle that intercepts the same arc.

**Reference sheet:** PARTIAL — circle area/circumference and "a circle has
360° (or $2\pi$ radians) of arc" are given; the proportion setup itself and
the inscribed-angle rule are not spelled out — you have to know how to
build them from those givens.

**Core rule:**
$$\text{arc length} = \frac{\theta}{360^\circ} \times 2\pi r \qquad \text{sector area} = \frac{\theta}{360^\circ} \times \pi r^2$$
where $\theta$ is the central angle in degrees. **Inscribed angle theorem:**
an inscribed angle is always **half** the central angle that intercepts the
same arc.

**Worked example:** A circle has radius 9. A central angle of 60° cuts off
an arc. Find the arc length.
$$\text{arc length} = \frac{60}{360} \times 2\pi(9) = \frac{1}{6} \times 18\pi = 3\pi$$

**Shortcut/trap:** it's always "part over 360," never "part over the whole
circumference/area number directly" — write the fraction $\theta/360$ first,
then multiply by the *whole-circle* formula, so you don't accidentally use
the arc's own length as if it were the radius.

---

### G4 — Circle equation

**What this actually tests:** reading off (or reverse-engineering via
completing the square) a circle's center and radius from its equation.

**Reference sheet:** NOT on it — memorize the form.

**Core rule:**
$$(x-h)^2 + (y-k)^2 = r^2 \quad \Rightarrow \quad \text{center } (h,k), \text{ radius } r$$
If the equation is given in general form ($x^2+y^2+Dx+Ey+F=0$), complete
the square on the $x$-terms and $y$-terms separately to get it into
$(x-h)^2+(y-k)^2=r^2$ form.

**Worked example:** Find the center and radius of $(x-3)^2 + (y+2)^2 = 25$.
Rewrite $(y+2)^2$ as $(y-(-2))^2$: center $(3, -2)$, and $r^2 = 25$ so
$r = 5$.

**Shortcut/trap:** the signs inside the parentheses flip — $(x-3)^2$ means
the center's $x$-coordinate is $+3$, and $(y+2)^2$ means the center's
$y$-coordinate is $-2$. Read it as "$x$ minus $h$," not "$x$ plus whatever
number is written."

---

### G5 — Similar triangles

**What this actually tests:** matching up corresponding sides between two
similar triangles and solving a proportion — including "shadow"/real-world
setups where the triangles aren't drawn overlapping.

**Reference sheet:** NOT on it — no formula is given, but the method is
simple enough it shouldn't need one.

**Core rule:** if two triangles are similar (same angles, proportional
sides — often established via AA: two matching angles), then corresponding
sides are all in the same ratio:
$$\frac{AB}{DE} = \frac{BC}{EF} = \frac{AC}{DF}$$
Match vertices in the *order the similarity is stated* ($\triangle ABC \sim
\triangle DEF$ means $A \leftrightarrow D$, $B \leftrightarrow E$, $C
\leftrightarrow F$) — that tells you which sides correspond.

**Worked example:** $\triangle ABC \sim \triangle DEF$, with $AB = 6$,
$BC = 8$, $DE = 9$. Find $EF$.
$$\frac{AB}{DE} = \frac{BC}{EF} \Rightarrow \frac{6}{9} = \frac{8}{EF} \Rightarrow 6 \cdot EF = 72 \Rightarrow EF = 12$$

**Shortcut/trap:** cross-multiply, don't cross-cancel by eye under time
pressure — mismatching which side pairs with which is the single most
common error here, especially when the two triangles are drawn at
different orientations or aren't drawn touching at all.

---

### G6 — Right-triangle trig: sin/cos/tan (SOH-CAH-TOA)

**What this actually tests:** given a right triangle and an angle, finding
a trig ratio (or, in reverse, a side length given a ratio).

**Reference sheet:** NOT on it — memorize SOH-CAH-TOA.

**Core rule:** for an acute angle $\theta$ in a right triangle, relative to
$\theta$:
$$\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}} \qquad \cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}} \qquad \tan\theta = \frac{\text{opposite}}{\text{adjacent}}$$

**Worked example:** A right triangle has an angle $\theta$ with the side
opposite $\theta$ equal to 5 and hypotenuse 13. Find $\sin\theta$,
$\cos\theta$, $\tan\theta$.
First find the adjacent side: $\text{adj} = \sqrt{13^2 - 5^2} = \sqrt{169-25} = \sqrt{144} = 12$.
$$\sin\theta = \frac{5}{13} \qquad \cos\theta = \frac{12}{13} \qquad \tan\theta = \frac{5}{12}$$

**Shortcut/trap:** "opposite" and "adjacent" are defined *relative to
whichever angle you're evaluating* — the same triangle gives different
opposite/adjacent labels depending on which of the two acute angles you're
computing the ratio for. Always re-check which angle is $\theta$ before
labeling sides.

---

### G7 — Trig identities: co-function relationship, Pythagorean identity

**What this actually tests:** using one trig value or ratio to get another
without a triangle drawn, via two fixed identities.

**Reference sheet:** NOT on it — memorize both identities.

**Core rule:**
$$\sin^2\theta + \cos^2\theta = 1 \quad \text{(Pythagorean identity)}$$
$$\sin(\theta) = \cos(90^\circ - \theta) \quad \text{(co-function identity — complementary angles)}$$
The co-function identity follows directly from SOH-CAH-TOA: in any right
triangle the two acute angles sum to 90°, and what's "opposite" one of them
is "adjacent" to the other — so sine of one angle always equals cosine of
its complement.

**Worked example:** If $\sin\theta = \tfrac{3}{5}$ and $\theta$ is acute,
find $\cos\theta$.
$$\sin^2\theta + \cos^2\theta = 1 \Rightarrow \cos^2\theta = 1 - \frac{9}{25} = \frac{16}{25} \Rightarrow \cos\theta = \frac{4}{5}$$
(positive root, since $\theta$ is acute — cosine of an acute angle is always positive.)

**Shortcut/trap:** the co-function identity is the fast way to solve "if
$\sin(x°) = \cos(y°)$, find $x$ in terms of $y$" questions — set
$x = 90 - y$ directly instead of trying to compute either value numerically.

---

### G8 — Angle relationships (parallel lines + transversal, triangle angle sum)

**What this actually tests:** two separate, small rule sets — the fixed
angle relationships created when a transversal crosses parallel lines, and
the fact that a triangle's angles always sum to 180°.

**Reference sheet:** PARTIAL — triangle angle sum (180°) is given;
parallel-line/transversal rules are **not** on the sheet.

**Core rule:** when a transversal crosses two **parallel** lines, eight
angles are formed, but only two measures exist among them:
- **Equal:** corresponding angles, alternate interior angles, alternate
  exterior angles, vertical angles.
- **Supplementary (sum to 180°):** co-interior / same-side interior angles,
  and any linear pair.

Triangle angle sum: $A + B + C = 180°$ for any triangle.

**Worked example:** Two parallel lines are cut by a transversal. One angle
formed measures 118°. Find its alternate interior angle and its co-interior
(same-side interior) angle.
Alternate interior angles are equal: $118°$.
Co-interior angles are supplementary: $180° - 118° = 62°$.

**Shortcut/trap:** don't try to memorize which named pair ("alternate
exterior," "corresponding," etc.) goes with which picture under time
pressure — instead just sort every angle in the diagram into one of two
buckets, "same as the angle I'm given" or "supplementary to it." Only
same-side interior pairs (and linear pairs) are supplementary; everything
else that isn't literally the same angle is equal.

---

## Mini-Diagnostic

One question per skill, no notes. Answer key with brief solution steps is
at the bottom — don't peek until you've attempted all 8.

**G1.** A cone has radius 6 and height 8. Find its volume in terms of $\pi$.

**G2.** A 45-45-90 right triangle has a hypotenuse of 12. Find the length of one leg.

**G3.** In a circle, a central angle measures 80°. What is the measure of the inscribed angle that intercepts the same arc?

**G4.** A circle is given by the equation $x^2 + y^2 + 8x - 2y + 8 = 0$. Find its center and radius.

**G5.** A 6-foot person casts a 4-foot shadow at the same time a nearby tree casts a 30-foot shadow. How tall is the tree?

**G6.** A right triangle has legs of length 8 and 15 (hypotenuse 17). For the acute angle $\theta$ opposite the side of length 8, find $\tan\theta$.

**G7.** If $\sin(x°) = \cos(50°)$ and $0 < x < 90$, what is $x$?

**G8.** In $\triangle PQR$, the angles measure $3x$, $5x$, and $4x$ degrees. Find the measure of $\angle R$ (the $4x$ angle).

---

### Answer key

**G1.** $V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi(36)(8) = 96\pi$

**G2.** Leg $: $leg$\sqrt2 = $hyp, so leg $= 12/\sqrt2 = 6\sqrt2$

**G3.** Inscribed angle = half the central angle: $80° \div 2 = 40°$

**G4.** Complete the square: $x^2+8x=(x+4)^2-16$, $y^2-2y=(y-1)^2-1$. So $(x+4)^2+(y-1)^2-16-1+8=0 \Rightarrow (x+4)^2+(y-1)^2=9$. Center $(-4, 1)$, radius $3$.

**G5.** Proportion: $\frac{6}{4} = \frac{h}{30} \Rightarrow 4h = 180 \Rightarrow h = 45$ ft

**G6.** $\tan\theta = \frac{\text{opp}}{\text{adj}} = \frac{8}{15}$

**G7.** Co-function identity: $\sin(x°) = \cos(90°-x°)$, so $90 - x = 50 \Rightarrow x = 40$

**G8.** $3x + 5x + 4x = 180 \Rightarrow 12x = 180 \Rightarrow x = 15$, so $\angle R = 4(15) = 60°$
