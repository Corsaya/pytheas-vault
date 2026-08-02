---
tags: [pytheas, research, benchmarks, models, claude, fable-5, mythos-5, prompt-log]
created: 2026-08-02
status: research complete
type: prompt-log
related: ["[[../Ultimate Workspace Roadmap]]"]
---

# Frontier model benchmark comparison (2026-08-02)

**Prompt:** requested research on current AI model capabilities/benchmarks,
formatted like a reference image (Anthropic's own "Claude Mythos 5 and
Fable 5" comparison table), to inform which model(s) should author SAT
course content in Pytheas.

**AI:** Claude Sonnet 5 (this session) — verified the reference image
against live web search before treating its numbers as fact (the model
name "Mythos 5" wasn't in this session's known model list, so it needed
checking, not assuming).

## Verification

Confirmed real via multiple outlets: Anthropic announced **Claude Fable 5**
and **Claude Mythos 5** (~June 2026), debut models in a new "Mythos-class"
architecture built for long-horizon, multi-day agentic tasks.
- **Mythos 5** is the same underlying model **without general safety
  restrictions** — access is tightly restricted to government/vetted
  critical-infrastructure use ("Project Glasswing"), not available for
  general use.
- **Fable 5** is the public flagship — "Anthropic's most capable model to
  date," leading frontier benchmarks in software engineering, vision, and
  scientific research, with safety fallbacks to Claude Opus 4.8 on certain
  sensitive topics. This matches the `claude-fable-5` model ID and the
  $100 Fable-credit grant already visible in this session's `ccdash` usage
  data — Fable 5 access is metered by that credit, separate from normal
  5h/7d Claude usage.

Sources:
[CNBC — Anthropic releases Mythos-like AI model, Claude Fable 5](https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html),
[MobiHealthNews — Anthropic unveils Claude Fable 5 and Mythos 5 with safeguards](https://www.mobihealthnews.com/news/anthropic-unveils-claude-fable-5-and-mythos-5-safeguards),
[Anthropic — Claude Mythos](https://www.anthropic.com/claude/mythos),
[Anthropic Red Team — Assessing Claude Mythos Preview's cybersecurity capabilities](https://red.anthropic.com/2026/mythos-preview/).

## Benchmark comparison (source: Anthropic's own release chart)

| Benchmark | Claude Mythos 5 / Fable 5 | Claude Mythos Preview | Claude Opus 4.8 | GPT 5.5 | Gemini 3.1 Pro |
|---|---|---|---|---|---|
| Agentic coding — SWE-Bench Pro | **80.3%** | 77.8% | 69.2% | 58.6% | 54.2% |
| Agentic coding — FrontierCode (Diamond, xhigh) | **29.3%** | — | 13.4% | 5.7% | — |
| Knowledge work — GDPval-AA | **1932** | — | 1890 | 1769 | 1314 |
| Knowledge work vision — GDP.pdf (no tools) | **29.8%** | — | 22.5% | 24.9% | 16.7% |
| Spatial reasoning — Blueprint-Bench 2 | **38.6%** | — | 14.5% | 36.2% | 26.5% |
| Tool use — AutomationBench | **17.4%** | — | 15.5% | 12.9% | 9.6% |
| Computer use — OSWorld-Verified | 85.0% | **85.4%** | 83.4% | 78.7% | 76.2% |
| Legal — Legal Agent Benchmark | **13.3%** | — | 10.4% | 2.1% | 0.0% |
| Multidisciplinary reasoning — Humanity's Last Exam (no tools) | **59.0%** | 56.8% | 49.8% | 41.4% | 44.4% |
| Multidisciplinary reasoning — HLE (with tools) | 64.5% | **64.7%** | 57.9% | 52.2% | 51.4% |
| Biology — BioMysteryBench (hard) | **46.1%** | 29.6% | 40.0% | — | — |
| Agentic coding — Terminal-Bench 2.1 | **88.0%** | — | 82.7% | 83.4% (Codex CLI) | 70.7% (Gemini CLI) |
| Cybersecurity — ExploitBench (Cap%) | **78.0%** | 69.0% | 40.0% | 34.0% | — |
| Health — HealthBench Professional | **66.0%** | 64.7% | 56.9% | 51.8% | — |

**Caveat:** this is Anthropic's own comparison chart — self-reported and
naturally selected to flatter Fable 5/Mythos 5. Treat the *ranking
direction* as credible (multiple independent benchmark suites, wide
margins) but not as neutral third-party verification. No separate
third-party writing-quality/instruction-following benchmark was pulled in
this pass.

## Relevance to Pytheas / SAT content authoring

The most relevant rows for **authoring educational content** (not coding)
are Knowledge work (GDPval-AA), Knowledge work vision, and Multidisciplinary
reasoning (Humanity's Last Exam) — Fable 5 leads all three by a clear
margin over Opus 4.8, GPT 5.5, and Gemini 3.1 Pro.

**Practical takeaway for right now:** Mythos 5 is inaccessible (restricted).
Between what's actually available in this session — **Claude Opus 5**
(this session's high-reasoning tier, no metered credit) and **Claude
Fable 5** (metered, $15.71 of the $100 credit left per today's `ccdash`
check) — Donovan's instruction was to use **Opus** for the SAT content
template specifically, which also avoids spending down the limited Fable
credit on a first draft/template pass. Fable 5 stays available as a
higher-ceiling option for a later polish pass if the Opus-authored
template needs a capability Opus can't match.
