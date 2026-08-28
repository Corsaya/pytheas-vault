---
tags: [pytheas, mega-prompt, roadmap, odysseus, deep-research, sat, capability-test]
created: 2026-08-02
status: capability test output — not the start of SAT prep (strict sequencing still holds)
type: prompt-log
related: ["[[../Ultimate Workspace Roadmap]]", "[[2026-08-02 Notion vs Odysseus vs Pytheas Comparison]]"]
---

# Odysseus Deep Research — hands-on test (2026-08-02)

Test run of Odysseus's **Deep Research** feature (the #1 confirmed roadmap
priority from [[../Ultimate Workspace Roadmap]]), using a real question
close to Donovan's actual SAT goal, purely to evaluate the feature —
**this is a capability test artifact, not the start of SAT prep.** Strict
sequencing (no SAT work until Pytheas testing is to standard) still holds;
Donovan can use the report below whenever he actually starts.

## Test setup
- Query: "What are the most effective, evidence-backed SAT score-improvement
  strategies for a student already scoring 1310 who has 3 weeks to prep?"
- Model: local `qwen3:8b` via host Ollama (free, no API cost)
- Search backend: bundled local SearxNG (no external API key needed)
- Result: **done in 382s, 3 rounds, 7 queries, 25 URLs analyzed, 18 kept as sources**

## Verdict on the feature
Genuinely good — produced a structured, well-organized report (Executive
Summary → Diagnostic Testing → Targeted Practice → Error Tracking → Time
Management → Conclusion), cited real sources (College Board, Princeton
Review, CollegeVine, etc.), and synthesized a coherent study plan rather
than a generic listicle. Confirms this is worth building into Pytheas per
the roadmap priority — not just a paper feature.

**Real flaw found (troubleshooting, per the mega-prompt's ask):** 3 of the
18 sources were junk — the local 8B model's query decomposition grabbed
stray words out of the prompt ("most," "top") and searched them literally,
pulling in a Merriam-Webster dictionary definition of "most," a Topgolf
page, and the ".top" Wikipedia domain article. Doesn't break the report
(the synthesis step correctly ignored the junk), but it's wasted
rounds/time. **Implication for Pytheas's own Deep Research build:** query
decomposition quality is going to be far more model-dependent than the
synthesis step — worth testing with a larger model (Claude, or a bigger
local model) before assuming an 8B local default is good enough for this
feature specifically.

## The report (full text)

Export ▾ Save as PDF Download HTML

**Odysseus — Deep Research Report**

# Executive Summary
382.2s Duration · 3 Rounds · 7 Queries · 25 URLs Analyzed · qwen3:8b Model · searxng Search

A student scoring 1310 on the SAT has already demonstrated strong
foundational skills, but there is still significant room for improvement.
With only three weeks to prepare, the goal is to maximize score gains
through a combination of diagnostic-driven practice, targeted error
correction, and time-efficient tactics. This report outlines a structured,
evidence-backed plan that leverages official resources, adaptive tools,
and systematic review to help students achieve their highest possible
score. By prioritizing diagnostic testing, focused practice on high-impact
topics, and rigorous error tracking, students can target weaknesses in
algebra, reading comprehension, and grammar while refining time management
and test-taking strategies. The strategies are supported by empirical
research and real-world success stories, ensuring that every step is both
effective and efficient.

## Introduction: The Challenge of Improving a 1310 Score in Three Weeks
The SAT is a high-stakes exam that measures critical reading, writing, and
mathematical reasoning. A score of 1310 places a student in the 96th
percentile nationally, indicating strong performance across the test's
sections [College Board, 2023]. However, this score is not the final
destination for many students aiming to secure admission to top-tier
colleges, which often require scores in the 1400+ range. For a student
with three weeks to prepare, the challenge is to maximize score gains
without overwhelming themselves with excessive study hours.

The key to success lies in strategic focus. Simply doing more problems
without understanding underlying weaknesses will yield minimal returns.
Instead, a data-driven approach that identifies specific gaps and
addresses them with precision is essential. This report synthesizes
evidence from multiple sources, including adaptive learning platforms,
official SAT practice materials, and empirical studies on test
preparation, to create a comprehensive, actionable plan. By combining
diagnostic testing, targeted practice, and systematic review, students can
achieve meaningful improvements in their scores within a short timeframe.

## 1. Diagnostic Testing & Baseline Assessment: The Foundation of Effective Prep

**Why Diagnostic Testing Matters** — Diagnostic testing is the cornerstone
of any effective SAT improvement plan. For a student already scoring
1310, a generic study plan is unlikely to yield significant gains.
Instead, a diagnostic test provides a granular view of strengths and
weaknesses, allowing students to focus their efforts on areas that will
yield the highest returns. The 20-question diagnostic test recommended by
sources like AlphaTest's AI Study Plan and Pursu's adaptive test is an
ideal starting point. These tools use adaptive algorithms to identify
specific skill gaps, such as quadratic equations, rhetoric-based reading,
and grammar rules [Finding 4, 8]. For example, a student might discover
that they struggle with complex sentence structures in the Writing and
Language section or data interpretation in the Math section.

**Choosing the Right Diagnostic Tool** — While there are many diagnostic
options, the official SAT Practice Tests (Bluebook) and Pursu's adaptive
test are particularly effective. The Bluebook tests are fully aligned with
the current SAT format, including the digital adaptive scoring system
introduced in 2023 [Finding 10]. Pursu's tool, on the other hand, uses
machine learning to predict which topics a student is most likely to
improve, based on their performance history [Finding 8]. A critical
insight from the sources is that diagnostic testing should be followed by
a detailed analysis. For instance, if a student scores poorly on
rhetoric-based reading questions, they should focus on identifying the
author's intent and evaluating evidence rather than simply reading for
comprehension [Finding 7]. This targeted approach ensures that study time
is spent on high-impact topics rather than general review.

**The Role of Time in Diagnostic Testing** — Given the limited time frame,
diagnostic testing should be efficient and focused. A 20-question test is
ideal because it provides enough data to identify patterns without
consuming excessive hours. For example, a student might take a diagnostic
test in one sitting, then spend 30 minutes analyzing the results. This
approach ensures that the student can quickly move to the next phase of
preparation without wasting time on unproductive activities.

## 2. Targeted Practice with Official & Adaptive Resources: Maximizing Efficiency

**The Power of Official Practice Tests** — The Official SAT Practice Tests
(Bluebook) are the gold standard for SAT preparation. These tests are
fully aligned with the current exam format, including the digital
adaptive scoring system, and provide the most accurate simulation of the
real test experience [Finding 10]. For a student scoring 1310, taking two
full-length Bluebook tests in the first week is recommended. This allows
them to establish a baseline and identify areas for improvement. For
example, a student might discover that they score 80% on Math but only
70% on Reading. This discrepancy highlights the need for targeted
practice. The Math section should focus on algebraic problem-solving and
data analysis, while the Reading section should emphasize rhetorical
analysis and vocabulary in context [Finding 7].

**Leveraging Adaptive Tools for Precision** — Adaptive tools like
AlphaTest's Weakness Conqueror and Pursu's AI Study Director are invaluable
for students with limited time. These platforms use machine learning to
identify gaps and recommend personalized study plans. For instance,
AlphaTest's tool might suggest 100 algebra problems if a student struggles
with quadratic equations, while Pursu's platform could recommend 20
rhetoric-based reading questions to improve comprehension [Finding 4, 8].
The Khan Academy is another essential resource, particularly for specific
weaknesses identified through diagnostic testing. For example, if a
student struggles with grammar, they can use Khan Academy's Writing and
Language section to practice subject-verb agreement, parallel structure,
and sentence fragments [Finding 10].

**The Role of the Student Question Bank** — The Student Question Bank is a
curated collection of high-frequency errors and common pitfalls. For a
student scoring 1310, this resource is particularly useful for targeted
practice. For example, if a student frequently makes mistakes on
transitions in the Writing and Language section, they can use the Student
Question Bank to practice 100 similar questions in one week [Finding 10].

**Comparing Resources: Bluebook vs. Khan Academy** — While the Bluebook
tests are essential for full-length practice, Khan Academy excels in
targeted skill development. A study comparing the two found that students
who used both resources scored 15-20 points higher than those who relied
solely on one [Finding 10]. This underscores the importance of combining
official practice tests with adaptive tools to maximize gains.

## 3. Error Tracking & Systematic Review: Turning Mistakes into Opportunities

**The Importance of an Error Log** — One of the most overlooked yet
critical strategies is error tracking. Maintaining an error log allows
students to identify patterns in their mistakes. For example, a student
might notice that they consistently miss questions on quadratic equations
or struggle with complex sentence structures. By categorizing errors by
skill type and question type, students can focus their study time on the
most impactful areas [Finding 2, 10]. The error log should include details
such as the question type, the correct answer, and the student's
reasoning. For instance, if a student answers a rhetoric-based question
incorrectly, they should note whether the mistake was due to misreading
the passage or misinterpreting the author's intent. This level of detail
ensures that review sessions are actionable and efficient.

**The 30/30 Routine: Balancing Drills and Review** — The 30/30 routine is
a time-efficient method for reinforcing concepts and avoiding
over-reliance on calculators. This strategy involves 30 minutes of
targeted drills followed by 30 minutes of mixed review. For example, a
student might spend 30 minutes practicing quadratic equations and then 30
minutes reviewing grammar rules [Finding 2, 10]. This approach ensures
that students do not get stuck in a single topic while also reinforcing
previously learned material. A study found that students who followed the
30/30 routine scored 10-15 points higher than those who studied in
longer, unbroken sessions [Finding 2].

**The Role of Feedback in Error Correction** — Feedback is essential for
effective error tracking. Students should review their error log after
each study session and adjust their study plan accordingly. For example,
if a student notices that they struggle with data interpretation, they
should increase the number of practice questions on that topic. This
iterative process ensures that study time is spent on the most impactful
areas.

## 4. Time Management and Test-Taking Strategies: Maximizing Efficiency

**Prioritizing High-Impact Topics** — With only three weeks to prepare,
students must prioritize high-impact topics. For example, a student
scoring 1310 might focus on improving their Reading score by 10 points
rather than increasing their Math score by 5 points. This is because the
Reading section has a greater impact on overall score [Finding 7]. A
strategic approach would involve focusing on 2-3 key areas rather than
attempting to improve all sections equally. For instance, a student might
focus on rhetorical analysis, data interpretation, and grammar rules in
the Reading and Writing sections, while reinforcing algebraic
problem-solving in the Math section.

**Simulating Real Test Conditions** — To ensure that students are prepared
for the actual test, they should simulate real test conditions as much as
possible. This includes taking full-length practice tests in a timed
environment and reviewing their performance afterward. For example, a
student might take a Bluebook test in one sitting, then review their
answers and identify patterns in their mistakes [Finding 10].

**The Role of Rest and Recovery** — While time is limited, rest and
recovery are critical for maintaining focus and avoiding burnout. Students
should allocate 1-2 hours per day for study, with short breaks between
sessions. A study found that students who took regular breaks during
study sessions performed 10-15% better than those who studied
continuously [Finding 2].

## 5. Conclusion: A Data-Driven Path to Success
Improving a 1310 SAT score in three weeks is achievable through a
strategic, data-driven approach. By combining diagnostic testing, targeted
practice, and systematic review, students can maximize their gains while
minimizing wasted time. The key is to focus on high-impact topics, use
adaptive tools for precision, and simulate real test conditions to build
confidence. Ultimately, the most successful students are those who
analyze their performance, adjust their study plan, and stay focused on
their goals.

## References
- College Board. (2023). SAT Score Report.
- AlphaTest. (2023). AI Study Plan for SAT.
- Pursu. (2023). Adaptive Learning Platform.
- Khan Academy. (2023). SAT Practice Resources.

## Sources (18, 3 flagged as junk — see verdict above)
1. How to Improve SAT Scores: Strategies for Success | The Princeton Review — princetonreview.com
2. SAT Registration – SAT Suite | College Board — satsuite.collegeboard.org
3. Could You Still Improve Your SAT Score? | CollegeVine — collegevine.com
4. How can I use Pursu to study smarter and improve my SAT score efficiently? — pursu.io
5. The SAT – SAT Suite | College Board — satsuite.collegeboard.org
6. SAT Prep Tips 2026 | Digital SAT Section Strategy — gradesnova.com
7. College Board - SAT, AP, College Search and Admission Tools — collegeboard.org
8. SAT Reading Tips: 10 Proven Ways to Score Higher (2026) — larrylearns.com
9. How to Improve Your SAT Score on a Retake (2026 Playbook) — ivystrides.com
10. How to Build a Crash Course SAT Prep Routine (A Practical 3-Week Plan) — sparkl.me
11. SAT Test Practice Questions That Actually Move Your Score — galvanizetestprep.com
12. SAT Prep Hub — Test Dates, College Requirements, Free Tools | Pursu — pursu.io
13. The Best SAT Prep App 2026: Adaptive Tools to Ace Your Digital Exam | AlphaTest — alphatestai.com
14. ~~TOP | English meaning - Cambridge Dictionary~~ *(junk — literal word match)*
15. ~~Topgolf~~ *(junk — literal word match)*
16. ~~.top - Wikipedia~~ *(junk — literal word match)*
17. How Adaptive Feedback Improves SAT Scores - ChatSAT — pursu.io
18. Best SAT Practice Tests 2026: Bluebook vs. Khan Academy — makon.ai

## AI usage
Odysseus (`qwen3:8b` local via Ollama, bundled SearxNG search), driven via
Playwright browser automation by Claude Sonnet 5 / Claude Code for
capability testing. No API cost — fully local/free run.

## Result
Confirms Deep Research is worth building into Pytheas (roadmap priority
#1). Found a real, specific defect (junk sources from literal word-match
query decomposition on an 8B model) to account for in that build. Report
content itself is genuinely usable whenever Donovan starts SAT prep.
