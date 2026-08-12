---
tags: [pytheas, sat, math, psda, crash-course]
created: 2026-08-12
source: "Foundations Knowledge Check P1-P9"
related: ["[[../Foundations Knowledge Check]]", "[[../Diagnostic Gap Lessons (2026-08-07)]]"]
---

# Math — Problem-Solving & Data Analysis Crash Course

Per [[../Research/Official SAT Structure and Content Research (2026-08-07)|the Official SAT Structure research]], this domain is worth **~15% of the Math section (5–7 questions)** — this doc covers all nine skills tracked as P1–P9 in [[../Foundations Knowledge Check]].

---

### P1 — Percent of a number, percent increase/decrease (chained/multi-step)

Already fully covered — this was a confirmed diagnostic gap and got its own lesson. The short version: convert percent to a decimal and multiply; for a discount then tax (or any chained percent problem), each step applies to the **current** value, not the original. Full worked examples, practice, and answers here: [[../Diagnostic Gap Lessons (2026-08-07)#Lesson 4 — Problem-Solving & Data Analysis: percent-of-a-number refresher]].

---

### P2 — Ratios and proportions

**What this actually tests:** whether you can set up two equivalent fractions and solve for a missing piece — recipes scaled up, map scales, mixture problems, "for every X there are Y" setups.

**The core move:** write the ratio as a fraction, set it equal to a second fraction with the unknown, and cross-multiply.
$$\frac{a}{b} = \frac{c}{d} \implies ad = bc$$
Keep the same *quantity* in the same position in both fractions (e.g., always flour on top, sugar on bottom) — mixing up which number goes where is the #1 source of errors here, not the algebra itself.

**Worked example:** A recipe uses flour to sugar in a ratio of 5 : 3. A baker uses 40 cups of flour. How much sugar is needed?
$$\frac{5}{3} = \frac{40}{x}$$
$$5x = 120$$
$$x = 24 \text{ cups of sugar}$$

**Trips people up:** watch for ratios given as "5 to 3" vs. "5 : 8" (part-to-part vs. part-to-whole) — reread the question to confirm which one you're given before setting up the fraction.

---

### P3 — Unit conversion / rate problems

**What this actually tests:** converting between units (minutes ↔ hours, miles ↔ feet) and applying a rate (amount per unit time) — often both in the same question.

**The core move:** treat a rate as a fraction (quantity / time) and multiply by a conversion factor written as a fraction that cancels the unit you don't want:
$$\text{rate} \times \text{new time} = \text{total amount}$$
When converting, write the conversion as a fraction equal to 1 (e.g., $\frac{60 \text{ min}}{1 \text{ hr}}$) so the unwanted unit cancels on paper — this keeps you from accidentally multiplying when you should divide.

**Worked example:** A pump fills bottles at a rate of 3 widgets every 8 minutes. At this rate, how many widgets does it produce in 6 hours?
$$6 \text{ hr} \times \frac{60 \text{ min}}{1 \text{ hr}} = 360 \text{ min}$$
$$\frac{3 \text{ widgets}}{8 \text{ min}} \times 360 \text{ min} = \frac{3 \times 360}{8} = 135 \text{ widgets}$$

**Shortcut:** convert everything to one consistent unit *first* (here, minutes), then apply the rate once — don't try to convert mid-calculation.

---

### P4 — Mean, median, mode, range — outliers

**What this actually tests:** computing the four basic stats and, more importantly, reasoning about how an outlier distorts each one differently.

**The core rules:**
- **Mean** = sum of values ÷ count. Pulled hard toward outliers.
- **Median** = middle value when sorted (average the middle two if the count is even). Resistant to outliers.
- **Mode** = most frequent value (can be none, one, or several).
- **Range** = max − min.

**Worked example:** Six data points: $4, 7, 7, 9, 12, 50$.
$$\text{mean} = \frac{4+7+7+9+12+50}{6} = \frac{89}{6} \approx 14.83$$
$$\text{median: sorted already} \to \frac{7+9}{2} = 8$$
$$\text{mode} = 7 \qquad \text{range} = 50 - 4 = 46$$
The mean (≈14.8) is dragged well above where most of the data actually sits, because the outlier ($50$) pulls it up; the median (8) stays representative of the typical value. This gap — mean noticeably higher/lower than median — is exactly what SAT questions are testing when they ask "which measure better represents the data" after showing an outlier.

**Trips people up:** "range" sounds like it should be an interval — it's a single number (max − min), not "4 to 50."

---

### P5 — Two-way frequency tables

**What this actually tests:** reading a table with two categories (rows and columns) and correctly picking the right row, column, or cell to answer a fraction/percent question — the hard part is identifying the right denominator, not the arithmetic.

**The core move:** identify whether the question wants a fraction of a **row total**, a **column total**, or the **grand total**, then divide the relevant cell(s) by that total.

**Table — survey of 100 students on preferred pet:**

|          | Dogs | Cats | Total |
|----------|------|------|-------|
| Freshman | 28   | 12   | 40    |
| Senior   | 22   | 38   | 60    |
| **Total**| 50   | 50   | 100   |

**Worked example:** Of the students who prefer cats, what percentage are seniors?
"Of the students who prefer cats" means the denominator is the **Cats column total** (50), not 100.
$$\frac{38}{50} = 0.76 = 76\%$$

**Trips people up:** using the grand total (100) by default instead of the column/row the question actually restricts you to — always find the phrase "of the ___" and use that group's total as the denominator.

---

### P6 — Scatterplot: line of best fit, interpreting slope

**What this actually tests:** using a given line-of-best-fit equation to predict a value, and translating the slope into a plain-English rate. You are never asked to compute the regression line by hand — it's either given or shown on the graph.

**The core rule:** a line of best fit has the form $y = mx + b$. To predict, plug in $x$. To interpret the slope $m$ in context: "for each additional [unit of $x$], [$y$] changes by $m$ [units of $y$], on average."

**Table — hours studied vs. test score (5 students):**

| Hours studied ($x$) | Test score ($y$) |
|---|---|
| 2 | 71 |
| 4 | 77 |
| 5 | 82 |
| 7 | 91 |
| 8 | 93 |

The points don't fall exactly on a line (real data scatters), but the line of best fit for this data is given as:
$$y = 62 + 4x$$

**Worked example:** Using the line of best fit, predict the score for a student who studies 7 hours, and interpret the slope.
$$y = 62 + 4(7) = 62 + 28 = 90$$
Slope interpretation: each additional hour studied is associated with an average increase of 4 points on the test.

**Trips people up:** the $y$-intercept ($62$ here) is *not* "the score with zero studying" in a literal sense if $x=0$ falls outside the tested range — the SAT sometimes asks you to note this ("no data point near $x=0$" is a valid critique of extrapolating).

---

### P7 — Basic probability from a table or set

**What this actually tests:** probability = favorable outcomes ÷ total possible outcomes, usually pulled directly from a table, often with a "given that" condition that restricts the denominator to one row or column.

**The core rule:**
$$P(\text{event}) = \frac{\text{count of outcomes matching the event}}{\text{total count in the relevant group}}$$
"Given that" or "if selected from [group]" restricts your denominator to just that subgroup, same logic as P5.

**Worked example (using the P5 table):** If a student is selected at random from the seniors, what is the probability that the student prefers dogs?
"Given that" the student is a senior restricts the denominator to the Senior row total (60):
$$P(\text{dogs} \mid \text{senior}) = \frac{22}{60} = \frac{11}{30} \approx 0.367 = 36.7\%$$

**Shortcut:** this is the same skill as P5 with "probability" language instead of "percentage" language — if you can find the right cell and denominator for a two-way table, you already know how to do both.

---

### P8 — Standard deviation (conceptual)

**What this actually tests:** whether you understand standard deviation as a measure of **spread** (how far values tend to be from the mean) — you are never asked to compute it by hand on the SAT, only to compare or reason about it.

**The core rule:** larger standard deviation = data points are more spread out from the mean; smaller standard deviation = data points are tightly clustered near the mean. Two data sets can have the *same mean* and very different standard deviations.

**Worked scenario:** Two vending machines both advertise 30-gram bags of chips. Sampled bag weights (grams):
- Machine A: $29, 30, 30, 31, 30$
- Machine B: $20, 25, 30, 35, 40$

Both sets have a mean of exactly 30 g. Which machine has the greater standard deviation, and what does that mean in practice?
Machine B's weights are much farther from 30 on average (as far as 10 g off) while Machine A's weights stay within 1 g of 30. So **Machine B has the greater standard deviation** — its bags are far less consistent, even though both machines average out to the advertised weight.

**Trips people up:** adding the same constant to every value in a set shifts the mean but does **not** change the standard deviation (the spread between values is unchanged); multiplying every value by a constant *does* scale the standard deviation by that same constant.

---

### P9 — Margin of error / sampling (conceptual)

**What this actually tests:** reasoning about what actually makes a survey estimate trustworthy — sample size and randomness — without any computation.

**The core rules:**
- A **larger, randomly selected** sample produces a **smaller margin of error** (more precision), all else equal.
- Margin of error only accounts for random sampling variability — it does **not** fix a **biased** sample (e.g., a non-representative location or self-selected respondents). A huge biased sample can still be a bad estimate.
- "Margin of error" describes a range the true population value likely falls within — a smaller margin means a tighter, more confident estimate.

**Worked scenario:** A researcher wants to estimate what percentage of a city's residents support a new transit proposal. Option A: survey 50 people outside a single downtown train station. Option B: survey 800 randomly selected residents from across the whole city. Which gives a better estimate, and why?
Option B is better on *two* counts: its sample is random and representative of the whole city (Option A is biased toward people who already ride transit, regardless of sample size), and its much larger sample size would shrink the margin of error even if both were equally random. A bigger sample doesn't rescue a biased one — Option A's core problem is *who* was asked, not *how many*.

**Trips people up:** "increase the sample size" is only a valid fix for margin of error if the sampling method is already random/unbiased — the SAT sometimes offers "survey more people at the same biased location" as a wrong-answer trap.

---

## Mini-Diagnostic

One question per skill, P1–P9. Work them cold, then check the answer key.

**P1.** A \$150 jacket is discounted 20%, and then a 6% sales tax is applied to the discounted price. What is the final price?

**P2.** A map has a scale of 2 inches : 15 miles. Two cities are 7 inches apart on the map. How many miles apart are they?

**P3.** A pump fills a tank at a rate of 12 gallons every 5 minutes. At this rate, how many gallons will it fill in 2 hours?

**P4.** Six employees have the following years of experience: $2, 3, 3, 4, 5, 25$. By how much does the mean exceed the median?

**P5.** Survey of 80 gym members:

|             | Cardio | Weights | Total |
|-------------|--------|---------|-------|
| Under 30    | 18     | 22      | 40    |
| 30 and over | 26     | 14      | 40    |
| **Total**   | 44     | 36      | 80    |

What percentage of members under 30 prefer weights?

**P6.** A line of best fit relating hours of sleep ($x$) to reaction time in milliseconds ($y$) is $y = 450 - 15x$. Based on this line, what is the predicted reaction time for someone who sleeps 6 hours, and what does the slope mean in context?

**P7.** Using the table from P5, if a member is selected at random from those aged 30 and over, what is the probability that the member prefers cardio?

**P8.** Two vending machines both advertise 30-gram bags of chips. Machine A's sampled bags weigh $29, 30, 30, 31, 30$ grams. Machine B's sampled bags weigh $20, 25, 30, 35, 40$ grams. Which machine has the greater standard deviation?

**P9.** A researcher wants to estimate the average number of hours per week adults in a state spend exercising. Which would produce a smaller margin of error, all else equal: surveying 200 randomly selected adults statewide, or surveying 1,000 randomly selected adults statewide? Why?

---

### Answer key

**P1.** $150 \times 0.80 = 120$; $120 \times 1.06 = \$127.20$.

**P2.** $\frac{2}{15} = \frac{7}{x} \Rightarrow 2x = 105 \Rightarrow x = 52.5$ miles.

**P3.** $2 \text{ hr} = 120 \text{ min}$; $\frac{12}{5} \times 120 = 288$ gallons.

**P4.** Mean $= \frac{2+3+3+4+5+25}{6} = \frac{42}{6} = 7$. Median (sorted, middle two are 3 and 4) $= 3.5$. Difference: $7 - 3.5 = 3.5$.

**P5.** Denominator is the Under-30 row total (40): $\frac{22}{40} = 55\%$.

**P6.** $y = 450 - 15(6) = 450 - 90 = 360$ ms. Slope: each additional hour of sleep is associated with a 15 ms decrease in reaction time, on average.

**P7.** Denominator is the 30-and-over row total (40): $\frac{26}{40} = \frac{13}{20} = 65\%$.

**P8.** Both average 30 g, but Machine B's weights are much farther from 30 (up to 10 g off) vs. Machine A's (within 1 g). **Machine B** has the greater standard deviation.

**P9.** The 1,000-person sample — a larger random sample size reduces margin of error (more precision), all else equal.
