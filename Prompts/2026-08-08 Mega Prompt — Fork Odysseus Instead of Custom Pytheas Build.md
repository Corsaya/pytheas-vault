---
tags: [pytheas, mega-prompt, roadmap, odysseus, architecture-pivot, sat, courses]
created: 2026-08-08
status: raw
type: prompt-log
result: "[[../Ultimate Workspace Roadmap]]"
model: Claude Sonnet 5 (claude-sonnet-5)
---

# Mega Prompt — Fork Odysseus Instead of Custom Pytheas Build (2026-08-08)

> Raw capture, per the standing prompt-logging convention. Came mid-session
> during the new SAT Foundations Knowledge Check (built earlier this
> session — see [[../Courses/SAT/Foundations Knowledge Check]]), when
> Donovan paused the live quiz to raise a bigger architecture question.

## Prompt (verbatim)

> i like the way this is, but would prefer if this came from a better UI
> rather than just Claude Code terminal. THis is what I'd like courses to
> be, not only a storage of Notebook elements, but a place to quick access
> different tools made for this, I'd also like the vaults to be organized
> to contain these conversations, starting with this one, from "continue",
> and being recorded in Obsidian and then copied into Pytheas UI, if these
> chats are recorded, minus incognito or chat cleared ones to protect
> privacy, and a way to delete a conversation both from pytheas and
> obsidian, (btw the file they are in should be git ignored). These
> conversations as well as records of the results from these diagnostics
> will help you understand me better, as I believe growth can be made
> fastest through improved understanding of one another. (even though I'm
> trying to utilize other models, but pretty much trying to clone Odysseus.
> yknow, for this upcoming build, can you just clone Odysseus, but add the
> vault integration, briefings, tasks, put all stuff under tools except new
> chat search chats and email. Pretty much just Odysseus with vault
> integration is all I need, which I see now can just be done by filling
> Odysseus with my Obsidian vaults. Can you check if I can connect my vault
> repos to odysseus, and if so, if everything planned or has been worked on
> even needs chiron, and could just be done in odysseus. IF yes, just move
> everything to odysseus.

## Context immediately preceding

Live in the middle of the new SAT Foundations Knowledge Check (quizzing
domain by domain, on A5 of Algebra when this landed). Donovan liked the
Q&A-style knowledge-check format but wants it running inside the actual
Pytheas app UI, not the Claude Code terminal — that's what triggered the
wider "what should the app actually be" question, which cascaded into the
Odysseus question.

## Research done in response

Read Odysseus's actual ingestion source (`src/personal_docs.py`,
`routes/personal_routes.py`, `core/database.py`) via an Explore agent
rather than guessing from the README. Findings:

- **Document ingestion exists** (`PersonalDocsManager`) — chunked RAG via
  Chroma, handles `.md/.txt/.json/.pdf`/Office/epub.
- **No live vault connection.** Ingestion is confined by
  `_resolve_allowed_personal_dir` to a single app-owned
  `data/personal_docs/` root (symlinks outside it explicitly rejected) —
  vaults would need to be *copied* in, not linked.
- **No filesystem watcher anywhere in the codebase** — re-index is a
  manual `POST /api/personal/reload` call, not automatic.
- **No git-awareness** for documents (the only `git` usage is cloning
  llama.cpp for local model builds — unrelated).
- **No Obsidian syntax support** — wikilinks/frontmatter/callouts/embeds
  all read as flat text, chunked by raw character offset.
- Chat history is real and usable (SQLite, `owner`-scoped, single-user
  fine). Task scheduler exists and works. No "briefings" concept at all.

Verdict given to Donovan: not a clean "just connect it" — making Odysseus
actually do live, git-aware, Obsidian-native vault sync is itself a real
build project on top of Odysseus's existing code, not a config toggle.

## Decision

Presented three options via AskUserQuestion (fork Odysseus and build vault
integration on top / keep building Pytheas custom and cherry-pick patterns
per workstream 18 / defer, return to the SAT quiz). **Donovan chose: fork
Odysseus, add vault integration.** This supersedes the "build Pytheas from
scratch" framing implicit in the 2026-08-04 North Star pillar 1 — pillar 1
still holds (Odysseus feature-parity, Obsidian brain as the differentiator)
but the *mechanism* changes from "build toward it" to "start from
Odysseus's actual codebase and build the missing pieces on top."

## Result

Logged here and as a new workstream in `Ultimate Workspace Roadmap.md`
(see that doc for the concrete scope/open-questions breakdown). Not
executed yet — no fork created, no code forked, no files moved. Explicitly
sequenced *after* finishing the current session's SAT Foundations Knowledge
Check, which resumed immediately after this decision was made.

Also bundled into this same prompt, not yet separately scoped:
- Chat/conversation logging: record sessions into Obsidian (this vault),
  mirrored into the (future, forked) Pytheas UI — excluding incognito-mode
  and manually-cleared conversations. Needs a delete path that removes a
  conversation from both sides. Storage file(s) must be **git-ignored**
  (chat content, unlike roadmap/course docs, isn't meant to be committed).
- Diagnostic/quiz results (like this session's Foundations Knowledge Check)
  should also feed into whatever "understand Donovan better" mechanism
  gets built — ties directly into North Star pillar 2 (continuous
  record-and-learn), not a separate feature.
- Nav/IA request: consolidate most non-chat features under a single
  "Tools" area; keep New Chat, Search Chats, and Email as their own
  top-level items, everything else nested under Tools.
