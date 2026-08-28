---
title: Claude Code → Codex / GPT-5.6 Migration
date: 2026-08-25
tags: [handoff, migration, codex, gpt-5.6, tooling]
status: historical migration checklist — critical backup task completed
related: ["[[00 — START HERE]]", "[[01 — DONOVAN Master Context]]"]
---

# Claude Code → Codex / GPT-5.6 Migration

**Context:** the Claude Code subscription ends 2026-08-26. Codex is already
installed (`~/.local/bin/codex`, config at `~/.codex/config.toml`, with
`~/Documents/Obsidian/pytheas` and `~/home/donovan` already marked
`trust_level = "trusted"`). This is the list of what carries over, what needs
rebuilding, and what dies.

> [!success] Status correction — 2026-08-27
> The critical backup task is complete: private `Corsaya/chiron` exists and
> local `dev` tracks `origin/dev`. There are five current vault repositories,
> not six. The SAT test/drill apps mentioned below were removed from Chiron on
> 2026-08-26; its generic Classroom interface remains.

---

## 1. Do these before the subscription lapses

| # | Action | Why it's urgent |
|---|---|---|
| 1 | ✅ **Push `~/code/chiron` to a private GitHub remote** | Completed: private `Corsaya/chiron`; local `dev` tracks `origin/dev` |
| 2 | Verify `~/code/pytheas`, `~/code/jarvis`, and all 5 vault repos have live remotes and clean trees | All have off-machine `Corsaya` repositories; local remote URLs still need normalization |
| 3 | Confirm `AGENTS.md` is at `~/Documents/Obsidian/` | Codex's equivalent of `CLAUDE.md`. Without it, GPT-5.6 starts every session blind to the vault rules |
| 4 | Export claude-mem before it's orphaned | ~360k tokens of prior work context in `~/.claude-mem/claude-mem.db` |

---

## 2. What carries over unchanged

These are plain files and standard tools — no Claude dependency at all.

- **All five Obsidian vaults.** Markdown + git. Fully portable, which was the
  point of insisting everything be linked to Obsidian.
- **All code** — `~/code/{pytheas,jarvis,chiron,repo-scout,vault-atlas,trading,
  algo-scout,usage-monitor}`. Python and JS.
- **Chiron itself**, including its model-router abstraction. Chiron already
  supports direct API providers and local Ollama — **it never needed the Claude
  subscription to run.** Point it at an OpenAI key and it keeps working.
- **The Pytheas engine router** (`claude` / `api:<provider>:<model>` /
  `ollama:<model>`). The `api:` slot is exactly the seam this migration needs.
  Its `claude` tier goes dark; the other two don't.
- **Local voice** — faster-whisper STT + piper TTS. Fully local, unaffected.
- `~/.codex/config.toml` trust settings — already in place.

---

## 3. What needs rebuilding on the Codex side

### 3.1 `CLAUDE.md` → `AGENTS.md` ✅ delivered with this handoff

Codex reads `AGENTS.md`. An `AGENTS.md` has been written at
`~/Documents/Obsidian/AGENTS.md` carrying the vault rules forward, and it points
at `01 — DONOVAN Master Context` for identity. **Keep `CLAUDE.md` in place** —
it costs nothing, and it means a future Claude session (or OpenClaw) still works.

### 3.2 Hooks — 245 lines total, all Python/bash, all portable logic

| Hook | Event | Fate |
|---|---|---|
| `secret-scanner.py` (32 ln) | PreToolUse: Write\|Edit | **Rebuild.** Highest value of the four — it's the thing standing between him and a committed API key |
| `pre-push-check.sh` (8 ln) | PreToolUse: Bash | **Rebuild.** Trivial |
| `session-logger.py` (133 ln) | Stop | Rebuild if he wants the conversation archive to continue. 12 dated folders exist today, git-ignored, local-only |
| `incognito-toggle.py` (72 ln) | UserPromptSubmit | Only meaningful alongside the logger |

**The catch, and be honest about it:** Codex's hook/extension surface is not the
same as Claude Code's, and this document does **not** claim to know the exact
current equivalents. **Verify against live Codex documentation before porting** —
do not assume a 1:1 mapping. If Codex has no equivalent event, the fallback that
definitely works is a **git `pre-commit` hook** running `secret-scanner.py`, which
is arguably where a secret scanner belonged from the start — it protects the repo
regardless of which agent is driving.

### 3.3 Plugin-delivered capabilities that go away

These came from the Claude Code plugin marketplace and **do not exist in Codex.**
Listed by whether they're worth replacing:

| Capability | Verdict |
|---|---|
| **claude-mem** (cross-session memory, ~360k tokens of history) | **Export the SQLite DB, don't try to port the plugin.** Best replacement: dump the observations to markdown into `learning/ai-improvement/`, where they become vault content the new agent reads natively. Turning proprietary memory into portable markdown is strictly an upgrade |
| **last30days** (7-source research → daily briefings) | Standalone-ish; briefings are generated into `pytheas/Generated/Briefings/`. **Worth checking whether it runs outside Claude Code.** If not, the daily-brief pipeline in `~/code/pytheas/briefing.py` is his own code and can call any API |
| **obsidian skills** (defuddle, json-canvas, bases, obsidian-cli) | `obsidian-cli` and `defuddle` are separate CLI tools — install directly, use from any agent. The skill wrappers are what's lost, not the tools |
| **karpathy-skills** | Prompt guidance. Paste the content into `AGENTS.md` if he wants it |
| `ccdash` | **Claude-specific by definition** — it reads Anthropic plan limits. It dies with the subscription. Needs a rewrite against OpenAI usage if he wants the equivalent. **Also: delete the standing "run ccdash every response" rule from the working instructions**, since it becomes a broken command |

### 3.4 The standing rules that must be restated

`CLAUDE.md` encodes six behavioral rules that a new agent will not infer. All are
carried into `AGENTS.md`, but flagging them because they are the ones most likely
to get quietly dropped:

1. **Ask, don't assume** — batch questions, don't guess on judgment calls.
2. **Manual approval for edits** — show diffs before saving non-trivial changes.
   Add files freely; edit/delete needs approval each time.
3. **Push after every vault-changing response** — not batched.
4. **Prompt logging** — substantive prompts saved to the relevant vault's
   `Prompts/` folder, with model, tags, and result.
5. **"Locked" is the one override keyword** — open access everywhere by default;
   a doc or folder is off-limits only when explicitly marked locked. Nothing is
   locked as of 2026-08-25.
6. **Don't fabricate.** If a price, formula, or date isn't known, say so.

---

## 4. What genuinely gets lost

Say this plainly rather than pretending the migration is free:

- **~360k tokens of accumulated session memory**, unless exported now.
- **The skill/plugin ecosystem** — the ~40 loaded skills. Some are wrappers over
  real CLIs (recoverable); some aren't.
- **`ccdash`** and the usage-discipline habit built around it.
- **Continuity of the conversation archive**, unless the logger is rebuilt.

**And one thing gets gained, which is the actual argument for doing this:** every
capability that survives is one he owns — his code, his markdown, his database.
The migration is a forced audit of how much of the system was ever really his.
Per the Master Context, the long-run goal was always *"build something even
better in-house."* This is that pressure arriving early.

---

## 5. First session with GPT-5.6 / Codex — the opening move

```
Read ~/Documents/Obsidian/AGENTS.md, then read
~/Documents/Obsidian/pytheas/Operations/Handoff/01 — DONOVAN Master Context.md in full.

Then, before proposing anything: tell me the three things in that document you
think are most likely to be wrong or out of date, and why. Don't fix them.
Don't be agreeable about it.
```

That opener does three things at once: loads the context, tests whether the
handoff actually transferred, and immediately establishes the no-flattery rule
by asking for criticism as the first output. If the answer is agreeable mush,
the model isn't calibrated yet and the rest of §1 of the Master Context needs
restating.
