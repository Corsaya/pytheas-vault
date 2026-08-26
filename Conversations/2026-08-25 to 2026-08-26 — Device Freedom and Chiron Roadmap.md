---
title: "Device Freedom and Chiron Roadmap — 2026-08-25 to 2026-08-26"
date: 2026-08-26
tags: [conversation, codex, chiron, devices, roadmap]
source: Codex rollout transcript
scope: visible user and assistant messages only
excludes: hidden instructions, internal reasoning, tool calls, tool output
---

# Device Freedom and Chiron Roadmap — 2026-08-25 to 2026-08-26

Exported: 2026-08-26T00:38:10-04:00

> This is a mechanical export of visible user and assistant messages from
> the local Codex rollout. Environment-context wrappers are retained when
> they were stored as visible user messages.

## Donovan

<environment_context>
  <cwd>/home/donovan</cwd>
  <shell>bash</shell>
  <current_date>2026-08-25</current_date>
  <timezone>America/New_York</timezone>
  <filesystem><workspace_roots><root>/home/donovan</root></workspace_roots><permission_profile type="managed"><file_system type="restricted"><entry access="read"><special>:root</special></entry><entry access="write"><path>/home/donovan</path></entry><entry access="write"><special>:slash_tmp</special></entry><entry access="write"><special>:tmpdir</special></entry><entry access="read"><path>/home/donovan/.git</path></entry><entry access="read"><path>/home/donovan/.agents</path></entry><entry access="read"><path>/home/donovan/.codex</path></entry></file_system></permission_profile></filesystem>
</environment_context>

## Donovan

open /home/donovan/Downloads/Donovan.pdf and /home/donovan/Documents/Obsidian, with a focus on Obsidian. This is my current Obsidian vault structure. I'd like to optimally organize it, are there any plugins you can use or systems you can put in place to recall certain files, like graphify or anything that uses Obsidian, my github account is https://github.com/Corsaya. My first goal is for you to learn the pytheas/Chiron project, then organize my Obsidian vault structure and Github repo structures.

## Codex

I’ll first map the PDF, the Obsidian vault, and the local Git repositories, then inspect the Pytheas/Chiron code and your GitHub layout. I’m also using the plugin-management skill because you explicitly asked what plugins could improve recall and graph-based navigation; I’ll keep any structural changes reversible and won’t move vault or repo content until the current relationships are understood.

## Codex

The initial map shows you already have a strong multi-vault design and a dedicated `pytheas` vault with symlinks into both the codebase and learning vault. The main risk is duplication: Pytheas, Chiron, Jarvis, AI-improvement notes, handoffs, and session wraps overlap, so the best organization will come from clarifying which system is canonical rather than adding many more folders or plugins.

## Codex

Two important findings already change the recommendation. First, the public GitHub URL you gave (`Corsaya`) does not match the remotes on disk, which still point to `TheBiggerMann`. Second, Chiron is nine commits ahead of upstream with no personal remote; that is an immediate backup risk. I’m treating GitHub ownership/naming as a decision to confirm, not silently rewriting remotes.

## Codex

I completed the first-pass audit. I did not modify files, vault settings, Git remotes, or GitHub repositories.

The core conclusion: your problem is not insufficient folders or plugins. It is unclear canonical ownership across Pytheas, Chiron, older Jarvis material, and several overlapping vault/repository names.

## What Pytheas and Chiron are

- **Pytheas** is your smaller, native/local-first Python desktop assistant. It owns voice, notes, briefings, research, model routing, permissions, and computer actions.
- **Chiron** is your much larger Odysseus fork and prospective long-term workspace shell. Your nine local commits add multi-vault ingestion, vault synchronization, classroom/SAT functionality, and related infrastructure.
- The strongest long-term architecture is:
  - Obsidian Markdown = human-readable knowledge
  - A separate SQLite database = events, tasks, progress, and other structured data
  - Chiron = primary workspace interface
  - Pytheas = experimental capability layer and smaller native assistant
- Jarvis should remain historical unless a specific component is deliberately extracted.

The dangerous fact: `/home/donovan/code/chiron` is nine commits ahead of upstream and has no personal remote. Those commits exist only on this computer.

## Current Obsidian diagnosis

Keep the current multi-vault structure. Combining everything into one repository would damage privacy boundaries, Git history, and project separation. The Pytheas vault already functions as the cross-vault control center through its symlinks.

The immediate problems are drift and inconsistent entry points:

- [learning/Home.md](/home/donovan/Documents/Obsidian/learning/Home.md) still describes the retired vault split and says AI cannot access areas that are now accessible.
- [finance/Home.md](/home/donovan/Documents/Obsidian/finance/Home.md) points to an obsolete standalone `card-flip` location.
- `life/` has no root `Home.md`.
- Pytheas has several overlapping roadmap, capability, handoff, and historical documents without a universal status vocabulary.
- There are 686 Markdown notes across the four active vaults and roughly 1,895 wikilinks. That is large enough to benefit from better retrieval, but not large enough to justify an elaborate knowledge-graph platform.

Recommended structure:

```text
Obsidian/
├── pytheas/       AI system, courses, briefings, cross-vault control
├── learning/      School, Japanese, entertainment, AI-improvement
├── finance/       Work, trading, card-flip
├── life/          Daily life, health, journal, Minecraft event
└── agonizing-sentience/   Leave structurally unchanged
```

Inside each vault, use:

- `Home.md` as the human entry point.
- `_Templates/` for templates.
- `Inbox/` only where capture actually occurs.
- Properties such as `type`, `status`, `project`, `created`, and `updated`.
- Maps of content—ordinary curated notes—for important domains.
- `archive/` only for superseded content, not merely old content.

I would not reorganize by PARA or convert everything into atomic notes. Both would create extensive churn without solving your recall problem.

## Recall and graph recommendation

Start with four layers:

1. **Obsidian Search and Backlinks** for exact recall.
2. **Home notes and maps of content** for intentional navigation.
3. **Obsidian Bases** for property-driven views such as active projects, current roadmaps, and stale notes.
4. **Chiron indexing** for cross-vault semantic retrieval.

For community plugins, keep the set small:

- **Omnisearch**: stronger fuzzy/full-text retrieval.
- **Smart Related Notes** or **Smart Connections**: semantic “this note resembles…” recall.
- **Dataview** only if Bases cannot express a needed dashboard.
- A graph-analysis plugin only after link hygiene improves. Obsidian already includes a graph view; Graph Analysis adds similarity, link prediction, co-citation, and community detection, but its listed release is five years old, so I would test it in one vault before trusting it broadly. [Obsidian Graph documentation](https://github.com/obsidianmd/obsidian-help/blob/master/en/Plugins/Graph%20view.md), [Graph Analysis listing](https://community.obsidian.md/plugins/graph-analysis)

I would not install an AI plugin that automatically rewrites links throughout the vault. That produces a prettier graph while lowering the meaning of each edge.

The plugin-management review also clarified that a ChatGPT plugin is not the missing component here. The useful layer is native Obsidian retrieval plus Chiron’s cross-vault index.

## GitHub diagnosis

Your authenticated `Corsaya` account currently contains 17 private repositories and zero public repositories. That conflicts with the “GitHub portfolio” goal in your PDF.

There are also redundant or legacy repositories:

- `personal-vault` and `learning-vault`
- `ai-improvement-vault`, although AI-improvement now lives inside learning
- `card-flip`, `card-flip-vault`, and the current finance-contained card-flip material
- `minecraft-event`, `minecraft-event-vault`, and its life-vault mirror
- `jarvis`, `pytheas`, and the currently unbacked-up Chiron fork

Local remotes still use the former `TheBiggerMann` name. GitHub probably redirects these after the account rename, but the remotes should eventually be updated explicitly.

Recommended GitHub end state:

```text
Corsaya/
├── chiron                 private, active flagship workspace
├── pytheas                private until publishable
├── pytheas-vault          private
├── personal-vault         private; actually the learning vault
├── finance-vault          private
├── life-vault             private
├── agonizing-sentience    private/shared
├── minecraft-event        private/shared
└── selected portfolio repositories
    └── public, documented, runnable
```

Old repositories should be archived, not deleted, after confirming that every unique commit exists in the canonical replacement.

## PDF finding

`Donovan.pdf` is not presently a résumé despite its metadata title. It is a three-page Corsaya OS manifesto with project ideas, mission, philosophy, and priorities. That is useful as a personal constitution, but a recruiter will not treat it as a résumé because it lacks education, dated experience, demonstrated skills, links, and concrete project outcomes.

It should become one of two things:

- `Corsaya OS.pdf`, preserving its current purpose; or
- a real one-page engineering résumé derived from it.

## Approval batch

Before I change anything, I need your approval on these three decisions:

1. May I create a private `Corsaya/chiron` repository, add it as `origin`, and push the current `dev` branch?
2. May I draft corrections for `learning/Home.md`, `finance/Home.md`, a new `life/Home.md`, and a canonical Pytheas/Chiron project map for your review before saving?
3. May I install **Omnisearch** and one local semantic-related-notes plugin in the Pytheas mega-vault first, as a limited trial?

## Donovan

you may do all three

## Codex

I’ll proceed in this order: secure Chiron on GitHub, draft and apply the four approved vault navigation changes, then install the two retrieval plugins only in the Pytheas vault and verify Obsidian recognizes them. The plugin-management review is keeping this scoped to native Obsidian plugins rather than adding an unrelated ChatGPT connector.

## Codex

Chiron is now backed up at `Corsaya/chiron`; local `dev` tracks `origin/dev`.

Here is the approved vault draft I’m applying:

- `learning/Home.md`: remove the retired AI-access wall, make `ai-improvement/` an explicit area, and replace the obsolete list of old standalone vaults with the four current sibling vaults.
- `finance/Home.md`: define finance as the canonical home of card-flip, trading, and work; remove the dead `~/Documents/Obsidian/card-flip/` pointer.
- `life/Home.md`: add a new entry point covering private life records and the Minecraft project, with the journal authorship and generated-mirror boundaries stated.
- `pytheas/Pytheas and Chiron Project Map.md`: make Chiron the primary workspace shell, Pytheas the smaller native capability lab, Obsidian the durable knowledge layer, SQLite the future structured-data layer, and Jarvis historical. I’ll link this map from `pytheas/Home.md`.

## Donovan

/home/donovan/Downloads/manifest-788e337c-0fc9-4da0-9b09-dda5ab28f522-1787710159-7c700fd0-2026-08-26-02-09-59.json Claude data, migrating to ChatGPT

## Codex

I’ll add that Claude export to the migration work. I’m using the OpenAI documentation skill because this now involves moving data into ChatGPT/Codex; I’ll inspect the manifest first, determine what it actually contains and what ChatGPT can import natively, then preserve the useful parts in your existing portable-memory structure without exposing private data. The vault edits above are applied but not yet committed—I’ll validate and include them in the required vault commit after this migration assessment.

## Codex

The file is only a download manifest, not the Claude data itself. It points to four one-use archives: metadata, projects, memories, and conversations. I’m downloading those exact archives now, then I’ll inventory them locally before deciding what belongs in ChatGPT versus the Obsidian memory archive.

## Codex

Claude rejected all four one-use URLs with HTTP 403 because they require your authenticated Claude browser session; the data was not downloaded. I’ll preserve the migration plan, but you’ll need to click each export link while signed into Claude and place the four ZIPs in `Downloads`. Meanwhile I’m continuing the already-approved Obsidian plugin installation and vault validation.

## Codex

The two plugins are installed and enabled in the Pytheas vault: Omnisearch 1.30.1 and Smart Related Notes 3.1.0. Smart Related Notes runs its embedding model locally and is desktop-only, which is the right privacy tradeoff for this trial. I’ve also added a migration handoff that keeps raw Claude conversations local-only and requires reviewing memory candidates before anything is promoted into active ChatGPT/Codex context.

## Donovan

/home/donovan/Downloads/conversations-000.zip /home/donovan/Downloads/light_metadata-000.zip /home/donovan/Downloads/memories-000.zip /home/donovan/Downloads/projects-000.zip

## Codex

All four archives are present now. I’ll verify them for corruption and unsafe paths, extract them into a temporary staging directory, identify schemas and sensitive material, and then build a local-only conversation archive plus a reviewable memory summary. I will not upload the raw Claude export to ChatGPT or commit private conversations to Git.

## Codex

The export contains 417 conversations and 5,874 messages spanning October 2025 through August 2026, plus four Claude projects and one global memory record. The global memory is useful but already stale in places—for example, it still identifies the old GitHub handle and older project states—so importing it wholesale would contaminate the new system.

The migration draft is therefore:

- Raw JSON and converted transcripts → ignored, local-only `learning/ai-improvement/Conversations/Claude Export/`.
- One Markdown file per conversation, preserving UUIDs and timestamps.
- Claude memories → preserved verbatim in the local archive, then distilled into a separate candidate review; nothing becomes authoritative automatically.
- Project exports → archived first; only project instructions that remain current get promoted later.
- Existing authoritative handoff documents remain higher priority than Claude’s generated memory summaries.

## Codex

The safety scan found one private-key block, one API-key-shaped value, and nine password/secret assignment patterns in the export. I’m changing the migration accordingly: raw JSON will live outside every Obsidian vault with owner-only permissions, and the searchable Markdown copy will redact those patterns before Obsidian or Chiron can index it. This is a direct consequence of the migration safety review; uploading the raw export to ChatGPT would be a bad move.

## Codex

The searchable archive is now built: 417 redacted Markdown conversations (6.1 MB) under the Git-ignored Conversations area. The complete 45 MB raw export is outside Obsidian at `/home/donovan/.local/share/claude-export-20260825` with `0700` owner-only access.

I’m adding one tracked review document—not the raw memory itself—with these corrections before any ChatGPT memory seed is made:

- Replace `TheBiggerMann` with `Corsaya`.
- Replace the old “Claude Code is primary” workflow with the current Codex/ChatGPT transition.
- Treat Card Flip, Grand Scheme, Arb Bot, Jarvis, and TFG status as dated snapshots requiring repo verification.
- Preserve durable preferences: direct recommendations, verification before claims, architecture-first work, and portable/local ownership.
- Do not preserve credentials, account identifiers, exact private operational details, or volatile project statistics as saved memory.

## Codex

The Claude migration is complete locally and safely staged. The only remaining operation in this turn is the required Git synchronization for the four vault repositories. I’m pushing only the commits created here; the pre-existing deletion and untracked `.obsidian/` directory in `life` remain untouched.

## Codex

Three vaults pushed successfully. Finance was rejected because its remote has commits not present locally, so I’m inspecting the divergence before integrating anything; I will not force-push or overwrite the remote. The successful pushes also confirmed that several remotes still use the redirected `TheBiggerMann` URLs, which belongs in the upcoming GitHub cleanup.

## Codex

Completed all three goals plus the Claude migration.

- Created private `Corsaya/chiron`, pushed `dev`, and verified the remote.
- Organized the learning, finance, life, and Pytheas vault entry points.
- Added the canonical [Pytheas and Chiron Project Map](</home/donovan/Documents/Obsidian/pytheas/Pytheas and Chiron Project Map.md>).
- Installed Omnisearch 1.30.1 and Smart Related Notes 3.1.0 in Pytheas. Restart Obsidian to load them.
- Converted 417 Claude conversations containing 5,874 messages into a local searchable archive.
- Redacted detected keys and secret assignments from the searchable copy.
- Stored complete raw data at `/home/donovan/.local/share/claude-export-20260825` with owner-only permissions.
- Added [Claude Memory Candidate Review](</home/donovan/Documents/Obsidian/learning/ai-improvement/Memory-Export/Claude Memory Candidate Review.md>).
- Documented the process in [Claude Export to ChatGPT Migration](</home/donovan/Documents/Obsidian/pytheas/Handoff/06 — Claude Export to ChatGPT Migration.md>).
- Committed and pushed all four affected vault repositories.

ChatGPT cannot recreate Claude conversations or directly import Claude memories as native history. Official OpenAI guidance similarly says uploaded exports serve as reference rather than rebuilding chats, settings, or memories. [OpenAI migration guidance](https://help.openai.com/en/articles/9106926-transferring-conversations-from-1-chatgpt-account-to-another-chatgpt-account)

I left the pre-existing `life` deletion and untracked `.obsidian/` directory untouched. The next step is reviewing the memory candidates before I create a concise `ChatGPT Memory Seed.md`.

## Donovan

tomorrow i will give you my summer work, then I want you to copy Notion and Odysseus' systems to create a decent workspace using my Obsidian database, then Copy Google Classroom and use Google Docs Sheets and Slides as LibreOffice

## Codex

Understood. Tomorrow, August 26, we’ll handle it in this order:

1. Inventory and organize your summer work.
2. Reproduce the useful workflows from Notion and Odysseus—not blindly clone their interfaces.
3. Build the workspace around your Obsidian Markdown vaults as the durable source of truth.
4. Create a Google Classroom-style layer for courses, assignments, deadlines, submissions, grades, and progress.
5. Integrate LibreOffice as the local replacement for:
   - Google Docs → Writer
   - Google Sheets → Calc
   - Google Slides → Impress
6. Connect those documents to Chiron, Obsidian, and the planned structured database.

The important boundary: Obsidian should own knowledge, SQLite should own structured classroom/workspace state, LibreOffice should own complex documents, and Chiron should unify them. Trying to make Markdown imitate all four systems would produce a fragile mess.

When you provide the summer work, I’ll inspect the actual materials before designing or building the workspace.

## Donovan

what is the system for chiron right now. Also, I want my vault to be better organized. Can you come up with some example file structures, did you read my Obsidian codebase yet btw?

## Codex

Yes—but not exhaustively.

I read:

- The complete top-level Obsidian structure and file inventory.
- The vault instructions and handoff documents.
- The important Home pages, roadmaps, cleanup audit, migration plan, and project map.
- Pytheas’s README, history, modules, and repository state.
- Chiron’s README, directory architecture, remotes, and all nine personal commits relative to Odysseus.
- Plugin configurations and Git state across the vaults.

I have not read every line of Chiron or all 686 Markdown notes. So I understand the architecture and project history, but I would still inspect the relevant code before changing a Chiron subsystem.

## Chiron right now

Chiron is currently:

```text
Odysseus upstream
       │
       ▼
~/code/chiron
       │
       ├── Core workspace services
       │   ├── Authentication and sessions
       │   ├── Database
       │   ├── Model routing
       │   ├── Agents and tools
       │   └── Security policies
       │
       ├── Feature services
       │   ├── Chat and memory
       │   ├── Research
       │   ├── Documents
       │   ├── Notes and tasks
       │   ├── Calendar and email
       │   ├── Search/RAG
       │   └── Local models
       │
       ├── Donovan’s additions
       │   ├── Multi-vault ingestion
       │   ├── Live vault watching
       │   ├── Vault Git synchronization
       │   ├── Classroom experiments
       │   └── SAT experiments
       │
       └── Corsaya/chiron
           └── Private backup of dev
```

The current architectural layers are:

- `core/`: authentication, database, middleware, sessions, atomic I/O.
- `services/`: reusable domain services such as memory, research, search, hardware detection, speech, and documents.
- `routes/`: HTTP/API boundaries for features.
- `src/`: application logic, schedulers, model context, security, and integrations.
- `static/`: the browser interface.
- `scripts/`: administration and command-line tools.
- `mcp_servers/`: memory, RAG, email, and image-generation tool servers.

One correction to the older vault documentation: the newest personal Chiron commit removed the standalone SAT test and drill applications. Classroom infrastructure remains, but “the complete SAT app currently lives in Chiron” is no longer accurate.

Chiron is functional infrastructure, but it is not yet your coherent personal workspace. It remains mostly Odysseus with a Donovan-specific patch layer.

## What the final system should become

```text
Obsidian Markdown
Human-readable knowledge
        │
        ├──────────────┐
        ▼              ▼
Chiron index       Core SQLite DB
notes/search       tasks/events/progress
        │              │
        └──────┬───────┘
               ▼
          Chiron UI
               │
      ┌────────┼─────────┐
      ▼        ▼         ▼
 Classroom  LibreOffice  AI/agents
```

Chiron should not replace Obsidian. It should provide workflows on top of it.

## Example 1: Minimal-change vault structure

This is my recommendation. It improves navigation without moving hundreds of files.

```text
Obsidian/
├── pytheas/
│   ├── Home.md
│   ├── Pytheas and Chiron Project Map.md
│   ├── Handoff/
│   ├── Courses/
│   ├── Briefings/
│   ├── Research/
│   ├── Prompts/
│   ├── Surveys/
│   ├── session-wraps/
│   └── Archive/
│
├── learning/
│   ├── Home.md
│   ├── School/
│   ├── Japanese/
│   ├── Entertainment/
│   ├── ai-improvement/
│   └── _Templates/
│
├── finance/
│   ├── Home.md
│   ├── card-flip/
│   ├── trading/
│   └── Work/
│
├── life/
│   ├── Home.md
│   ├── personal-private/
│   │   ├── Home.md
│   │   ├── Inbox/
│   │   ├── Daily/
│   │   ├── Journal/
│   │   └── Health/
│   └── minecraft-event/
│
└── agonizing-sentience/
    └── unchanged
```

Most of this already exists. The work would focus on navigation, properties, stale links, and archival rules.

## Example 2: Project-centered Pytheas vault

This would make Pytheas and Chiron easier to distinguish:

```text
pytheas/
├── Home.md
├── Projects/
│   ├── Chiron/
│   │   ├── Home.md
│   │   ├── Architecture.md
│   │   ├── Roadmap.md
│   │   ├── Decisions.md
│   │   └── Classroom/
│   ├── Pytheas/
│   │   ├── Home.md
│   │   ├── Architecture.md
│   │   ├── Roadmap.md
│   │   └── Capabilities.md
│   └── Jarvis/
│       └── Historical Summary.md
├── Courses/
├── Operations/
│   ├── Briefings/
│   ├── Surveys/
│   └── Session Wraps/
├── Research/
├── Prompts/
├── Handoff/
└── Archive/
```

This is cleaner, but it requires many moves and could break generators and wikilinks. I would not apply it all at once.

## Example 3: Classroom-oriented learning structure

This prepares for the Google Classroom-style system:

```text
learning/School/
├── Home.md
├── 2026-2027/
│   ├── Dashboard.md
│   ├── Assignments/
│   ├── Gradebook/
│   ├── Calendar/
│   └── Courses/
│       ├── AP Chemistry/
│       │   ├── Home.md
│       │   ├── Syllabus.md
│       │   ├── Units/
│       │   ├── Assignments/
│       │   ├── Assessments/
│       │   └── Resources/
│       ├── Course 2/
│       └── Course 3/
└── Archive/
    └── 2025-2026/
```

Obsidian would store course material; SQLite would store assignment status, deadlines, grades, and submissions. Writer, Calc, and Impress files would be linked as course resources rather than converted into giant Markdown files.

My recommendation is Example 1 now, then selectively introduce the project grouping from Example 2 and the school-year structure from Example 3. A complete folder overhaul before importing your summer work would be premature.

## Donovan

add this goal, to be able to integrate other google accounts to be able to recieve necessary information, think like if my school account was connected to notion but notion is just this workspace, what I dont like about the organization is that some things I make are very small and incomplete compared to others, tomorrow I will do a cleanup, but the new structure should contain enough suifficient data to be worth being made. For example the School FOlder will be massive, and the subfolders should be of the subjects, but putting school next to something like Briefings which is just a bunch of the low quality Claude generated briefings is kind of odd. I'd like to be more broad and develop better systems for consistant output, like a daily journal (which should have some lock so that you cannot read, but you may move or delete or duplicate etc, making a good email and calendar systems across myt devices. By the way I'm thinking of switching my current iPhone 16 to another brand, but I need ideas on a phone that I have a lot of freedom with, since I don't like how locked apple is, since the freedom of Linux makes my phone feel like a cage. Here's my goals right now in order as the school year starts. 1. Finish summer work (reading The Kite Runner, In Cold Blood, and Night before the third week of school (more detailed date later), completing my AP Calc and AP Physics packet before the 14th) 2. Get my fitness tracked and be in a better habit so I can go towards my crew goals. I'm willing to get a smart watch, like Garmin, for fitness tracking, and I'll log all exercises in my workspace, as I develop it. 3. SAT, if it's not at a score I find satisfying, and I know I can do better with enough practice before October 3rd, I will take it one last time. 4 (could be switched with 2 and 3), complete my college essay. 5. apply to all of the colleges I want to. 6. Make the most out of my senior year, while working on my workspace, and possibly starting a YT channel about the Corsaya lifestyle. 7. Hobbies, currently SSB Melee and Miencraft Modpack TerraFirmaGreg.

## Codex

I’m treating this as a new authoritative senior-year/workspace requirements snapshot, not immediately reshuffling folders before tomorrow’s cleanup. I’ll record the priorities and the new multi-account integration goal in a new vault note, then use current official sources to outline the Google-account architecture and realistic phone options. Your “small incomplete areas beside major systems” criticism is correct: the next hierarchy should be based on durable domains and operational weight, while low-quality generated outputs become subordinate archives rather than peers.

## Codex

The goal is now recorded as a concrete system requirement. The key technical constraint is school-account policy: Google Classroom can expose courses, coursework, materials, topics, and permitted submission data, but OAuth scopes and school-domain administration determine what your account is actually allowed to provide. We’ll design per-account connections so a restrictive school account cannot break personal email/calendar integration.

## Codex

I recorded and pushed the new goal in [Senior Year Priorities and Workspace Requirements](</home/donovan/Documents/Obsidian/pytheas/Handoff/07 — Senior Year Priorities and Workspace Requirements.md>). I also added multi-account Google integration to the [Pytheas and Chiron Project Map](</home/donovan/Documents/Obsidian/pytheas/Pytheas and Chiron Project Map.md>).

Your organizational criticism is valid: output formats should not be peers of life domains.

The future hierarchy should revolve around:

- School and college
- Health and performance
- Projects and engineering
- Knowledge and learning
- Life and reflection
- Finance and work
- Creative and public work

Briefings, prompts, imports, generated reports, and session wraps belong underneath the system that produced them—probably in an `_Generated/` or `_Operations/` area. They should not sit conceptually beside School.

For Google integration, each school or personal account will have separate OAuth credentials, permissions, synchronization state, and disconnect controls. Google Classroom can provide courses, coursework, materials, topics, announcements, and whatever submission information your student account is permitted to access. School administrators and requested OAuth scopes can restrict availability. [Google Classroom resource model](https://developers.google.com/workspace/classroom/guides/key-concepts/api-structure), [OAuth scope guidance](https://developers.google.com/workspace/classroom/guides/auth)

For the journal, a written “do not read” rule is insufficient. The proposed design uses encrypted content outside Chiron’s index with a narrow management service that supports listing opaque entries, moving, duplicating, and confirmed deletion—but has no operation for reading their contents.

For replacing your iPhone, the strongest starting candidate is an unlocked Pixel 10 or Pixel 10 Pro running GrapheneOS:

- Bootloader and alternate-OS freedom.
- Separate user profiles for school, personal, and experimental identities.
- Ability to use sandboxed Google services where needed.
- Seven-year support horizon through August 2032.
- Stronger security model than leaving a conventional Android phone permanently bootloader-unlocked.

GrapheneOS officially supports the Pixel 10 family and recommends unlocked devices rather than carrier-locked variants. [GrapheneOS supported devices](https://grapheneos.org/faq#supported-devices), [Pixel 10 Pro specifications](https://store.google.com/product/pixel_10_pro_specs?hl=en-US)

A Fairphone is the repairability-first alternative and officially permits bootloader unlocking, but US availability, carrier support, camera quality, and alternative-OS support need closer investigation before buying. [Fairphone bootloader documentation](https://support.fairphone.com/hc/en-us/articles/10492476238865-How-to-unlock-and-re-lock-the-bootloader)

For fitness, Garmin is directionally appropriate because its watches track recovery, HRV, sleep, acute load, training readiness, and indoor rowing metrics. We should choose the exact watch only after establishing which metrics can be exported into Chiron without depending permanently on Garmin’s cloud. [Garmin training-readiness inputs](https://www8.garmin.com/manuals/webhelp/GUID-025D75CF-3445-49E1-8D81-1AA74AB4E00F/EN-US/GUID-C21BE0C8-A08E-4DA1-B6C6-2E0E2DDDB372.html)

Tomorrow’s cleanup should classify existing material into those durable domains before we move anything. That will expose which small folders deserve promotion, consolidation, archival, or deletion.

## Donovan

I still have some time, any questions for me to clear things up, I have one for you, is there a master file that you read that you follow before all your responses that change how you answer based on whats in it, as well as keywords or other quirks I want? Then, give me two things (both phone and watch, actually good earbuds as well) to look over tonight.

## Codex

I’ll answer the Codex instruction-file question from current official documentation, then give you two serious candidates in each category—phone, watch, and earbuds—based on ownership/freedom, rowing usefulness, cross-device compatibility, and current support. I’ll also batch the few questions that materially affect tomorrow’s vault design.

## Codex

Yes. There is effectively an instruction stack.

## What changes how I answer

1. **OpenAI system and developer instructions**

   These govern safety, tool use, file editing, and general behavior. You cannot replace them with a vault file.

2. **[AGENTS.md](/home/donovan/Documents/Obsidian/AGENTS.md)**

   This is the main file you control for how Codex works inside the Obsidian directory. It currently tells me to:

   - Avoid flattery and fabricated claims.
   - Ask before judgment calls.
   - Show drafts before non-trivial edits.
   - Commit and push vault changes.
   - Preserve the novel and journal authorship boundaries.
   - Log substantive prompts.
   - Read specific context documents.
   - Respect special keywords.

3. **[DONOVAN Master Context](</home/donovan/Documents/Obsidian/pytheas/Handoff/01 — DONOVAN Master Context.md>)**

   `AGENTS.md` instructs me to read this before substantive vault work. It contains your preferences, history, decision rules, projects, strengths, and failure modes. It is not automatically reread before every message, but I read it during this session and continue using it.

4. **Current-state documents**

   These prevent the master context from becoming a stale biography:

   - `North Star.md`
   - `Key Decisions.md`
   - `Gotchas.md`
   - [Senior Year Priorities](</home/donovan/Documents/Obsidian/pytheas/Handoff/07 — Senior Year Priorities and Workspace Requirements.md>)
   - [Pytheas and Chiron Project Map](</home/donovan/Documents/Obsidian/pytheas/Pytheas and Chiron Project Map.md>)

Current keywords include:

- **`locked`**: do not read or modify the marked material.
- **`sync mc-mirror`**: run the specific Minecraft reference synchronization.
- Retired Claude-specific keywords are documented but deliberately inactive.

We can add quirks and commands. A good arrangement would be:

```text
AGENTS.md
├── Non-negotiable behavior
├── File-editing rules
├── Privacy boundaries
├── Keywords/commands
└── Documents to consult

DONOVAN Master Context
└── Durable identity and decision rules

Senior Year Priorities
└── Current goals and deadlines

Key Decisions / Gotchas
└── Historical decisions and lessons
```

That is better than putting everything into one enormous master prompt. Official OpenAI guidance likewise recommends keeping policy in one place and avoiding duplicated instructions. [OpenAI model guidance](https://developers.openai.com/api/docs/guides/latest-model)

## Questions for you

These would materially clarify tomorrow’s design:

1. Does your school use Google Classroom for every subject, or do teachers also use another portal such as PowerSchool, Canvas, or Blackbaud?
2. Can you authorize third-party applications with your school Google account, or does your administrator block OAuth applications?
3. Should the locked journal expose dates and titles to me, or should I see only opaque identifiers such as `Journal Entry 2026-08-26`?
4. Should Google integration begin strictly read-only for all accounts?
5. Do you want one Obsidian application vault spanning everything, or separate Git-backed vaults presented through one Chiron interface?
6. What carrier do you use, and is your iPhone paid off/unlocked?
7. Are you comfortable installing GrapheneOS yourself, or do you want the replacement phone to remain on its factory operating system?
8. Rough combined budget for phone, watch, and earbuds?

## Two phones to inspect

### 1. Unlocked Pixel 10 Pro + GrapheneOS — my current recommendation

Why:

- Proper alternate-OS support with a relockable bootloader.
- GrapheneOS supports separate encrypted user profiles.
- Good school/personal account separation.
- Strong camera and everyday hardware.
- Supported through August 2032.
- You can still run sandboxed Google services without making them privileged system components.

Do not buy a carrier model unless OEM unlocking is confirmed; GrapheneOS specifically warns that carrier variants can block installation. [GrapheneOS devices](https://grapheneos.org/faq#supported-devices), [Pixel specifications](https://store.google.com/product/pixel_10_pro_specs?hl=en-US)

### 2. Fairphone Gen 6 or Gen 6+ — ownership-first alternative

Why:

- User-replaceable battery and modular parts.
- microSD expansion up to 2 TB.
- Official bootloader unlocking.
- Android or a directly sold `/e/OS` version.
- Long software-support promise.

Tradeoff: weaker camera/performance and alternative-OS security than Pixel plus GrapheneOS. Its appeal is repairability and physical ownership. [Fairphone specifications](https://www.fairphone.com/the-fairphone-gen-6), [Fairphone `/e/OS` model](https://www.fairphone.com/the-fairphone-gen-6-e-operating-system)

## Two watches to inspect

### 1. Garmin Forerunner 570 — sensible choice

Likely enough for your actual needs:

- Training readiness and status.
- Sleep, HRV, recovery, stress, and training load.
- Multisport tracking.
- Less expensive and lighter than the 970.

This is where I would start unless the 970 has a rowing-specific capability you will actually use. [Forerunner 570 manual](https://www8.garmin.com/manuals/webhelp/GUID-25E3235D-44D2-4384-A591-DD1D71BEBCB1/EN-US/Forerunner_570_OM_EN-US.pdf)

### 2. Garmin Forerunner 970 — premium option

- Training-readiness inputs include sleep, recovery, HRV, acute load, and recent stress.
- Indoor rowing fields include current, average, lap, and interval pace per 500 metres.
- More premium materials, mapping, and higher-end training functionality.

It may be excessive if rowing logs and recovery are the actual objective. [Training readiness](https://www8.garmin.com/manuals/webhelp/GUID-025D75CF-3445-49E1-8D81-1AA74AB4E00F/EN-US/GUID-C21BE0C8-A08E-4DA1-B6C6-2E0E2DDDB372.html), [rowing data fields](https://www8.garmin.com/manuals/webhelp/GUID-025D75CF-3445-49E1-8D81-1AA74AB4E00F/EN-US/Forerunner_970_OM_EN-US.pdf)

## Two earbuds to inspect

### 1. Nothing Ear (3) — freedom/cross-platform pick

- Works across Android, Windows, and iOS.
- LDAC, AAC, and SBC rather than a Pixel-only audio stack.
- Dual-device connection.
- Adaptive ANC and customizable EQ.
- Up to 5.5 hours with ANC, 38 hours from the case without ANC.
- IP54 earbuds.

The case microphone is unusual but potentially useful for voice capture into Chiron. [Nothing Ear (3)](https://nothing.tech/products/ear-3)

### 2. Pixel Buds Pro 2 — Pixel integration pick

- Better fit if you choose a Pixel.
- Eight hours with ANC and 30 hours with the case.
- Bluetooth 5.4, wireless charging, ANC, transparency, and conversation detection.
- Compatible with ordinary Bluetooth devices.

Tradeoff: full functionality requires Android, a Google account, and internet access. That conflicts somewhat with your desire to escape locked ecosystems, even though basic Bluetooth remains open. [Pixel Buds Pro 2 specifications](https://store.google.com/us/product/pixel_buds_pro_2_specs?hl=en-us)

My preliminary combination is **unlocked Pixel 10 Pro + GrapheneOS, Garmin Forerunner 570, and Nothing Ear (3)**. It gives you the most freedom without turning every device into an enthusiast project.

## Donovan

One candidate is fine if necessary, but I dont want anything to deal with Google, Apple, or Microsoft, I want to degoogle myself, like Pewdiepie, except he needs it for YouTube. Same here, and need Microsoft for games. I want rid of Apple tho

## Codex

That removes the Pixel from consideration. Even with GrapheneOS, it is still Google hardware, and recommending it would ignore your actual goal.

My single shortlist:

- **Phone:** Fairphone Gen 6 with `/e/OS`
- **Watch:** Garmin Forerunner 570
- **Earbuds:** Nothing Ear (3)

## Phone: Fairphone Gen 6 with `/e/OS`

This is the most realistic non-Google daily-driver choice—not a Linux phone that becomes a second job.

- Sold with `/e/OS` preinstalled.
- No Google account required.
- Replaceable battery and modular components.
- microSD up to 2 TB.
- Six major OS upgrades promised.
- Fairphone supports bootloader unlocking.
- Ordinary Android applications can run through `/e/OS` compatibility services.

It is not absolutely Google-free at the network-protocol level: `/e/OS` uses open-source compatibility components for applications expecting Google services. But Google does not control the operating system or require your identity.

Check carrier compatibility before buying. Also confirm that your banking, school-authentication, Garmin, and Microsoft-authenticator applications work acceptably on `/e/OS`. [Fairphone `/e/OS`](https://www.fairphone.com/the-fairphone-gen-6-e-operating-system)

I would not recommend PinePhone, Librem 5, or another Linux phone as your only phone during senior year. They maximize theoretical freedom while sacrificing cameras, battery, applications, cellular reliability, and school compatibility.

## Watch: Garmin Forerunner 570

Garmin is not Google, Apple, or Microsoft, and it provides serious athletic data. However, Garmin Connect is still a proprietary cloud dependency. That is the compromise.

Our longer-term system should:

1. Sync Garmin data.
2. Export it into your own Chiron database.
3. Make Chiron—not Garmin Connect—the permanent training record.
4. Preserve original FIT/TCX files so changing watch companies does not erase history.

Open-source watches such as PineTime provide more software freedom but are not credible replacements for training readiness, HRV, recovery, sleep, rowing, and serious athletic analysis.

## Earbuds: Nothing Ear (3)

These are ordinary cross-platform Bluetooth earbuds rather than ecosystem accessories.

- No Google, Apple, or Microsoft hardware dependency.
- Nothing account is not required for basic Bluetooth use.
- LDAC, AAC, and SBC.
- Dual-device connection.
- Custom EQ, ANC, and transparency through the optional Nothing X application.
- Compatible with Linux and `/e/OS`.

## Degoogle strategy

Your workspace should follow the same principle:

```text
Google services you cannot avoid
School Classroom · YouTube · occasional Docs
                 │
        isolated connectors
                 │
                 ▼
          Chiron-owned data
                 │
    ┌────────────┼────────────┐
    ▼            ▼            ▼
 Obsidian      SQLite      LibreOffice
 knowledge     records      documents
```

Google becomes an external supplier, not the foundation:

- School Google account receives its own isolated profile and OAuth tokens.
- YouTube receives a dedicated creator identity.
- No personal mail, calendar, contacts, photos, passwords, or primary file storage in Google.
- LibreOffice replaces Docs, Sheets, and Slides for authored work.
- Chiron imports necessary Classroom information.
- Your calendar’s canonical provider should eventually be something CalDAV-compatible outside Google.
- Microsoft remains isolated to gaming and software that genuinely requires it.
- Apple data gets exported before the iPhone is sold or wiped.

The practical goal is not “never send a packet to Google.” It is: **Google owns no irreplaceable data, no primary identity, and no essential workflow.**

## Donovan

can Fairphone Gen 6 use apps like social medias, have data, SMS, can use VPNs, pretty much functioning the same as an iPhone minus the bloat and lack of freedom

## Codex

I’m checking the exact `/e/OS` app-compatibility, US cellular-band, SMS, and VPN situation before giving you a yes/no. The broad answer is “mostly yes,” but banking, school authentication, RCS, eSIM/carrier activation, and DRM are the places where a de-Googled phone can stop feeling iPhone-equivalent.

## Codex

Yes—the Fairphone Gen 6 with `/e/OS` is intended to function as a normal smartphone, not a limited Linux-phone experiment.

It supports:

- Cellular calling
- SMS/MMS
- 4G and 5G mobile data
- Wi-Fi and hotspot/tethering
- Bluetooth
- Physical SIM
- VPN applications and Android’s built-in VPN configuration
- Social-media and messaging applications
- Banking and school applications when their security checks permit
- Camera, maps, navigation, notifications, fingerprint unlock and ordinary Android applications

`/e/OS` uses microG, an open-source compatibility implementation for applications expecting Google Play Services. This lets many mainstream apps receive push notifications, use location and otherwise behave normally without installing privileged Google Play Services or signing into a Google account. [microG on `/e/OS`](https://doc.e.foundation/support-topics/micro-g.html)

## The major US limitation: your carrier

The US `/e/OS` Fairphone is primarily a **T-Mobile phone**.

- **T-Mobile:** supported, although Fairphone says eSIM is unavailable and some advanced network/emergency features have limitations.
- **Mint, Metro and Tello:** generally supported because they use T-Mobile.
- **AT&T:** the newer US compatibility page says BYOD is supported, but Wi-Fi calling, RCS and some carrier features are unavailable.
- **Verizon, Visible and Verizon-based services:** do not buy it. Fairphone explicitly says they are unsupported, with coverage and emergency-calling risks.

[Fairphone US carrier matrix](https://us.fairphone.com/carrier-compatibility)

Therefore, the first question is: **which carrier do you currently use?**

## Applications

These should generally work:

- Instagram
- TikTok
- Reddit
- Discord
- Spotify
- YouTube
- Firefox and Chromium browsers
- Signal
- WhatsApp
- Telegram
- ProtonVPN, Mullvad, WireGuard and conventional Android VPNs
- Microsoft applications when you deliberately need them
- Garmin Connect
- Obsidian
- LibreOffice-compatible document viewers/editors
- Most school applications

However, I would test these before permanently switching:

- Your banking application
- School authentication/MFA application
- Google Classroom
- Garmin Connect
- Snapchat
- Any game with Play Integrity or aggressive anti-cheat
- Streaming applications that enforce strong DRM

`/e/OS` can satisfy basic Play Integrity, but not Google’s stronger Device or Strong verdicts. A minority of banking, DRM and security-sensitive applications may therefore refuse to run. [microG integrity limitations](https://doc.e.foundation/support-topics/micro-g.html)

## What you lose from the iPhone

- iMessage
- FaceTime
- AirDrop
- Apple Pay
- Apple Watch compatibility
- Seamless integration with existing Apple-only purchases and accessories
- Some camera/video polish
- Guaranteed compatibility with every mainstream financial application

Replacements include:

- iMessage/FaceTime → Signal
- AirDrop → LocalSend or KDE Connect
- iCloud Photos → Immich
- iCloud Drive → Nextcloud
- Apple Passwords → Bitwarden or KeePassXC
- Apple Maps → Organic Maps
- Apple Pay → physical cards; privacy-friendly contactless payment is a weak point
- Find My → another self-hosted or privacy-oriented location system

## Honest verdict

On T-Mobile or a compatible T-Mobile-based carrier, it can be your normal everyday phone. You can text, call, browse, use social media, stream music, run VPNs, use school apps and connect a Garmin.

It will not be as frictionless as an iPhone. You are exchanging perhaps 5–10% of ecosystem convenience for substantially more ownership, repairability and control. That trade is reasonable for you—but only after verifying carrier, banking and school-authentication compatibility.

## Donovan

My family uses AT&T

## Codex

That changes the recommendation materially. Fairphone’s current pages conflict: the newer US Gen 6+ matrix says AT&T BYOD is supported, while the `/e/OS` US partnership documentation says its phones are optimized for—or limited to—T-Mobile. I’m resolving which exact US model `/e/OS` buyers receive before recommending you spend anything.

## Codex

Then I withdraw the Fairphone recommendation unless your line can leave the AT&T family plan.

The current Murena Fairphone Gen 6 and Gen 6+ `/e/OS` listings explicitly recommend T-Mobile and T-Mobile-based carriers—not AT&T. Although the hardware contains many AT&T bands, carrier provisioning, VoLTE, Wi-Fi calling, RCS and emergency-service reliability are separate concerns. [Murena Fairphone 6+ listing](https://murena.com/america/shop/smartphones/brand-new/fairphone-gen-6-plus/)

Fairphone’s newer US compatibility page says the official Gen 6+ supports AT&T BYOD, but that does not override Murena’s warning for the `/e/OS` version. Buying a $700 phone and hoping AT&T provisions it correctly would be a poor decision.

Your realistic choices are:

1. **Move only your line to T-Mobile or a T-Mobile MVNO**, such as Mint or Tello, then use the Fairphone with `/e/OS`. Your family can remain on AT&T, though you may lose family-plan savings.

2. **Remain on AT&T and keep the iPhone temporarily** while we research an AT&T-certified, genuinely de-Googled phone. Most dependable custom-ROM options are Pixels, which you have ruled out, and I will not recommend a questionable niche phone merely to produce an answer.

3. **Buy the official AT&T-compatible Fairphone Gen 6+ and install `/e/OS` yourself** only after confirming its exact IMEI with AT&T and verifying that Murena’s build supports that hardware variant. This is plausible, but currently unproven—not purchase-ready.

The decisive question is: **would your family allow your line to leave the AT&T plan for T-Mobile, Mint, or Tello?** If not, Fairphone should come off tonight’s shortlist.

## Donovan

what is your best AT&T recommendation, that has the same loses from the iPhone and nothing more, unless minor. I'm fine with being laughed at for a strange phone, but dont want them to be right about not functioning well as a phone.

## Codex

I’m looking for the narrow intersection you actually want: non-Google hardware, AT&T-certified calling/data, relockable or responsibly unlockable bootloader, mature de-Googled Android, and ordinary app compatibility. I’m excluding Linux phones that are philosophically clean but objectively worse at being phones.

## Codex

The honest answer is that no phone currently satisfies all three requirements perfectly:

1. Non-Google hardware and operating system.
2. Fully approved, reliable AT&T service.
3. iPhone-level application compatibility with only minor losses.

My best AT&T-compatible compromise is the **unlocked US OnePlus 12, exact model CPH2583**.

## Why the OnePlus 12

AT&T explicitly lists the CPH2583 as tested and approved. That means calling, SMS, mobile data and normal network provisioning are substantially less speculative than Fairphone on AT&T. [Current AT&T approved-device list](https://www.att.com/scmsassets/support/wireless/devices-working-on-att-network-1.pdf)

The hardware remains strong:

- Snapdragon 8 Gen 3
- 12 or 16 GB RAM
- 256 or 512 GB storage
- Excellent 120 Hz display
- 5,400 mAh battery
- 80 W wired and 50 W wireless charging
- Good main, ultrawide and telephoto cameras
- Full AT&T-oriented LTE and 5G bands
- NFC, Wi-Fi 7 and dual SIM

[OnePlus 12 specifications](https://www.oneplus.com/us/12/specs)

## The operating-system decision

There are two paths, and neither should be disguised.

### Reliable path: OxygenOS, heavily de-Googled

Keep the locked factory operating system, but:

- Do not sign into a Google account.
- Disable or remove Google applications.
- Use F-Droid and Obtainium for open-source applications.
- Use Aurora Store anonymously when a Play Store application is unavoidable.
- Replace Google services with Proton, Nextcloud, Immich, Organic Maps, Signal and your Chiron workspace.
- Restrict remaining Google components with permissions and network controls.

This is not completely de-Googled—the underlying certified Android system retains Google components—but it preserves banking, school, DRM, notifications and device security. It is the closest match to “iPhone losses and nothing more.”

### True de-Googled path: `/e/OS`

The OnePlus 12 is supported by `/e/OS`, including the US CPH2583 model, with no currently listed device-specific issues. [OnePlus 12 `/e/OS` page](https://doc.e.foundation/devices/waffle)

But the current build is:

- A community release, not an official production build.
- `userdebug`, rather than a production `user` build.
- Unable to relock the bootloader.
- Only tentatively expected to pass basic Play Integrity.

That introduces meaningful additional losses: weaker physical security, possible banking/school-app failures and more responsibility for updates and troubleshooting. Under your stated standard, I would not put this build on your only phone immediately.

## My actual recommendation

Buy—or preferably borrow/test—a US OnePlus 12 CPH2583 and run locked OxygenOS without a Google account first. Make it operationally de-Googled while retaining full AT&T and application compatibility.

Then follow this progression:

```text
Week 1–2
OnePlus 12 + locked OxygenOS
No Google account
Replace Google apps and services

After verification
Test every bank, school, Garmin, social and MFA app

Only afterward
Decide whether true /e/OS is worth the unlocked-bootloader tradeoff
```

Do not flash `/e/OS` on day one. First prove that the phone works reliably for calling, emergency communication, banking and school. Freedom that prevents the device from functioning as a phone is cosmetic freedom.

If completely eliminating Google is non-negotiable, the better move is changing your line from AT&T to T-Mobile and buying the Murena Fairphone. If staying on AT&T is non-negotiable, the OnePlus 12 with restrained OxygenOS is the least dishonest recommendation.

## Donovan

OnePlus is fine by deGoogle as long as it doesnt depend on my google account to function it should be ok

## Codex

Then OnePlus is a strong fit. Your actual requirement is **Google-account independence**, not necessarily removing every Google-derived component from Android.

A OnePlus can function normally without signing into Google:

- Calls, SMS and AT&T mobile data work.
- OnePlus system updates do not require Google.
- Camera, files, Bluetooth, hotspot and VPNs work.
- Install open-source apps through F-Droid or Obtainium.
- Install mainstream Android apps anonymously through Aurora Store.
- Use Signal, Discord, Instagram, Spotify, Garmin Connect and similar apps independently.
- Replace Google services with Proton, Bitwarden, Organic Maps, Nextcloud/Immich and Chiron.

Some applications may individually demand Google services or authentication, but the phone itself will not depend on your Google account.

The setup would be:

```text
OnePlus
├── OnePlus account: skip unless demonstrably needed
├── Google account: skip
├── Google apps: disable/remove where safe
├── Google Play Services: retain initially for compatibility
├── App sources
│   ├── F-Droid
│   ├── Obtainium
│   └── Aurora Store
└── Personal services
    ├── Proton
    ├── Bitwarden
    ├── Immich/Nextcloud
    ├── Obsidian
    └── Chiron
```

Keep Google Play Services installed but unsigned initially. That preserves notifications and application compatibility without connecting the device to your Google identity. Removing the framework entirely can come later if testing proves it unnecessary.

Before buying, we should compare the AT&T-approved US **OnePlus 12, 13, 13R and 14**. The OnePlus 12 remains attractive because it has an `/e/OS` escape route later; a newer model may offer longer official support. The exact model number matters—do not buy a cheaper international variant and assume AT&T will provision it.

## Donovan

<environment_context>
  <cwd>/home/donovan</cwd>
  <shell>bash</shell>
  <current_date>2026-08-25</current_date>
  <timezone>America/New_York</timezone>
  <filesystem><workspace_roots><root>/home/donovan</root></workspace_roots><permission_profile type="managed"><file_system type="restricted"><entry access="read"><special>:root</special></entry><entry access="write"><path>/home/donovan</path></entry><entry access="write"><special>:slash_tmp</special></entry><entry access="write"><special>:tmpdir</special></entry><entry access="read"><path>/home/donovan/.git</path></entry><entry access="read"><path>/home/donovan/.agents</path></entry><entry access="read"><path>/home/donovan/.codex</path></entry></file_system></permission_profile></filesystem>
</environment_context>

## Donovan

Let's compare, give me the specs and prices, and what I can change about it, give me the links as well

## Codex

I’ll compare the AT&T-approved U.S. OnePlus models on the points that matter here: price, hardware, support life, Google-account independence, and how far you can safely deGoogle or modify each one. I’ll use current official listings and flag anything that depends on community ROM support.

## Codex

My best fit for you is the **OnePlus 13**, while the **13R** is the value choice and the **OnePlus 12** is the experimentation choice.

### Practical comparison

| Model | Price | Important specifications | Main compromises |
|---|---:|---|---|
| **OnePlus 13** | **$899.99 MSRP**; discontinued/new-old-stock pricing varies | Snapdragon 8 Elite, 12/256 or 16/512 GB, 6.82-inch QHD+ 120 Hz display, 6,000 mAh battery, 80 W wired + 50 W wireless charging, three 50 MP rear cameras including 3× telephoto, IP68/IP69 | Expensive; no microSD or headphone jack; curved-ish premium flagship size |
| **OnePlus 13R** | **$599.99 MSRP** | Snapdragon 8 Gen 3, 12/256 GB, 6.78-inch 1.5K 120 Hz flat display, 6,000 mAh battery, up to 80 W wired charging, 50 MP main + 50 MP 2× + 8 MP ultrawide, IP65 | No wireless charging; significantly weaker ultrawide camera; lower water protection |
| **OnePlus 12** | **$799.99 original MSRP**; used/refurbished price varies | Snapdragon 8 Gen 3, 12/256 or 16/512 GB, 6.82-inch QHD+ 120 Hz display, 5,400 mAh battery, 80 W wired + 50 W wireless charging, excellent 50+64+48 MP camera system | Older and has less official support remaining; `/e/OS` installation weakens security |
| **OnePlus 15** | **$899.99 for 12/256; $999.99 for 16/512** | Snapdragon 8 Elite Gen 5, 6.78-inch 1.5K display up to 165 Hz, enormous 7,300 mAh battery, 80 W wired + 50 W wireless, triple 50 MP cameras, eSIM, Wi-Fi 7 | Currently shown as out of stock/stop-sale by OnePlus; AT&T’s list confusingly calls CPH2749 “OnePlus 14,” so I would verify the IMEI before buying |

Official specifications: [OnePlus 13 series](https://www.oneplus.com/us/press/press-release/oneplus-launches-new-smartphone-flagship-series-in-north-america), [OnePlus 12](https://www.oneplus.com/us/12/specs), [OnePlus 15](https://www.oneplus.com/us/15/specs).

### My ranking for you

1. **OnePlus 13 — best dependable choice**
2. **OnePlus 13R — best if saving $300 matters**
3. **OnePlus 12 — best if experimenting with alternative operating systems matters**
4. **OnePlus 15 — strongest hardware, but only after AT&T accepts its exact IMEI**

The 13 is the closest to “lose Apple’s restrictions without losing normal-phone reliability.” Compared with the 13R, that extra $300 buys better cameras, wireless charging, substantially better water resistance and a more complete flagship.

### AT&T compatibility

AT&T explicitly lists these exact variants:

- OnePlus 13: **CPH2655**
- OnePlus 13R: **CPH2647**
- OnePlus 12: **CPH2583**
- OnePlus 12R: **CPH2611**

AT&T’s March 27, 2026 list also contains **CPH2749**, but labels it OnePlus 14 even though OnePlus skipped that product name in its public U.S. lineup. That ambiguity is why I would not blindly order a OnePlus 15.

Use the [official AT&T approved-device list](https://www.att.com/scmsassets/support/wireless/devices-working-on-att-network.pdf) and then run the actual phone’s IMEI through [AT&T BYOD](https://www.att.com/buy/byod/identify?devicetype=phone) before the return window expires. **Do not buy an international or Chinese variant simply because the seller says “AT&T compatible.”**

### What you can change safely

On the factory OxygenOS installation, without a Google account, you can:

- Use calls, SMS, mobile data, hotspot, Bluetooth, VPNs and AT&T normally.
- Skip Google-account login during setup.
- Replace the launcher, keyboard, browser, maps, email, cloud storage and password manager.
- Install applications from F-Droid, Obtainium, Aurora Store or direct APKs.
- Disable most visible Google applications.
- Use Firefox, Organic Maps, Proton/Tuta, Bitwarden, Syncthing and your Obsidian workspace.
- Keep Play Services installed but unsigned-in for applications that require its notification or compatibility infrastructure.
- Use separate browser profiles for school Google services instead of signing the entire phone into Google.

This is not perfectly deGoogled: Android and Play Services remain underneath OxygenOS. But Google does **not** need to be your identity, storage provider, email provider or application-store account.

### Deeper modifications

You can unlock the bootloader, install a custom recovery, use ADB, root with Magisk and potentially install aftermarket Android distributions. However:

- Bootloader unlocking wipes the phone.
- An unlocked bootloader reduces physical security.
- Banking, school, streaming and authentication applications may reject the device.
- OTA updating becomes more complicated.
- OnePlus 13/13R aftermarket-ROM support is less established than OnePlus 12 support.

The OnePlus 12 has a current community `/e/OS` build, but it is `userdebug`, its bootloader cannot be relocked, and Play Integrity is not assured. That makes it interesting as a project phone, but I would **not** begin senior year with that configuration on your only phone. See the [`/e/OS` OnePlus 12 page](https://doc.e.foundation/devices/waffle).

My exact recommendation: **buy an unlocked North American OnePlus 13 CPH2655**, keep OxygenOS and the bootloader locked, skip Google login, and deGoogle it gradually. That preserves reliable AT&T operation while giving you far more control than the iPhone.

## Donovan

<environment_context>
  <current_date>2026-08-26</current_date>
  <timezone>America/New_York</timezone>
  <filesystem><workspace_roots><root>/home/donovan</root></workspace_roots><permission_profile type="managed"><file_system type="restricted"><entry access="read"><special>:root</special></entry><entry access="write"><path>/home/donovan</path></entry><entry access="write"><special>:slash_tmp</special></entry><entry access="write"><special>:tmpdir</special></entry><entry access="read"><path>/home/donovan/.git</path></entry><entry access="read"><path>/home/donovan/.agents</path></entry><entry access="read"><path>/home/donovan/.codex</path></entry></file_system></permission_profile></filesystem>
</environment_context>

## Donovan

https://www.msn.com/en-in/news/other/oneplus-13-price-drops-by-rs-11118-on-flipkart-how-to-get-this-deal/ar-AA2arYii

## Codex

I’ll check the deal’s region, seller/model details, and whether that specific OnePlus 13 would be safe to use on your family’s AT&T plan. The model number matters more than the headline discount.

## Codex

That deal is real, but it is **not a good purchase for you in the United States**.

The article describes an Indian Flipkart offer:

- OnePlus 13, **16 GB RAM / 512 GB**
- Listed price: **₹69,349**
- With an eligible Flipkart Axis Bank card: approximately **₹65,881–₹66,000**
- The full ₹11,118 saving includes the card discount; the ordinary price reduction is only ₹7,650.
- An additional ₹220 “Protect Promise” fee appears on the listing.
- The advertised exchange discount is conditional and should not be treated as part of the price. [Flipkart listing](https://www.flipkart.com/oneplus-13-arctic-dawn-512-gb/p/itmb4659fd2a037f), [original Digit report](https://www.digit.in/news/mobile-phones/oneplus-13-price-drops-by-rs-11118-on-flipkart-how-to-get-this-deal.html)

Why I would skip it:

- It is an **Indian-market phone**, whereas AT&T approves the North American OnePlus 13 model **CPH2655**.
- The Indian unit may have a different model number, modem configuration and carrier software certification.
- Having compatible radio bands does not guarantee AT&T will provision HD Voice, Wi-Fi calling, visual voicemail or every 5G feature.
- Flipkart normally serves India, complicating payment, shipping and returns.
- The stated one-year manufacturer warranty may not be honored by OnePlus USA.
- Import tax, forwarding and payment costs would consume some of the discount.
- An Indian unit uses **100 W charging**, while the official North American version is rated for **80 W**—another clue that these are not identical regional packages.

The relevant AT&T document is its [official approved-device list](https://www.att.com/scmsassets/support/wireless/devices-working-on-att-network.pdf). It specifically identifies **CPH2655**, so that is the number I would require on the box and in Settings.

Verdict: **good deal for someone living in India; poor-risk deal for an AT&T customer in America.** Look for an unlocked **CPH2655** from OnePlus USA, Best Buy, Amazon when sold by Amazon, or a reputable U.S. refurbished seller. I would pay moderately more for the American model because dependable calls, warranty coverage and carrier features are worth considerably more than the apparent import saving.

## Donovan

look for news around oneplus, and a little of at&t

## Codex

I’ll scan recent OnePlus developments—especially U.S. availability, software/support, bootloader freedom, and new models—then check AT&T news that could affect bringing an unlocked OnePlus onto your family plan.

## Codex

The major news changes my recommendation: **OnePlus officially ended new product rollouts in North America and Europe on July 16, 2026.** It is no longer a normal long-term U.S. phone brand.

### What happened to OnePlus

OnePlus’s official notice says:

- No more new OnePlus product launches in North America or Europe.
- Existing phones will continue receiving their originally promised software and security updates.
- Existing warranties and eligible repair service remain in effect.
- North American customer-support channels remain open.
- The U.S. OnePlus Community closed on August 16, 2026.
- Eligible devices will eventually be offered a **voluntary** transition from OxygenOS to ColorOS 17.
- Owners may remain on OxygenOS, and OnePlus promises a rollback option for those who try ColorOS, although exact versions and procedures have not been published.

That comes directly from [OnePlus’s official business-adjustment notice](https://www.oneplus.com/us/adjustment?from=ribbon). The [U.S. repair portal](https://www.oneplus.com/us/support/repair) is still operating, although OnePlus warns that processing can take five additional business days.

Remaining OnePlus 15 inventory subsequently sold out in the United States, and OnePlus’s store currently shows the 15 and 15R unavailable. Future models such as the OnePlus 16 will not receive official U.S. releases.

### What this means for a OnePlus 13

A North American **OnePlus 13 CPH2655** should not suddenly stop working:

- AT&T still lists it as tested and approved.
- Calls, SMS, data and 5G should continue.
- OnePlus says updates, warranty service and repairs will continue.
- The phone remains extremely capable hardware.

But the longer-term disadvantages have grown:

- No future OnePlus upgrade path in America.
- Replacement parts and accessories may gradually become harder to find.
- Resale value will probably suffer.
- Support quality may deteriorate even if OnePlus formally honors its commitments.
- OxygenOS is effectively reaching the end of its independent life.
- ColorOS is more tightly associated with Oppo’s ecosystem and is less attractive for someone prioritizing modification freedom.
- Buying an imported OnePlus 16 later would introduce exactly the AT&T, warranty and bootloader risks we are trying to avoid.

This doesn’t make the OnePlus 13 unusable. It makes paying a premium price for one much harder to justify.

### Software and modification news

There is uncertainty around future bootloader freedom. Chinese OnePlus models have become considerably more restrictive, and newer ColorOS devices may require approved “deep testing” procedures or prohibit normal unlocking entirely. OnePlus has not clearly documented what ColorOS 17 will mean for bootloader unlocking on existing North American phones.

Consequently:

- Keep the bootloader locked on your primary phone.
- Don’t import a Chinese phone and flash global firmware.
- Don’t voluntarily install ColorOS 17 immediately after release.
- Wait for independent testing of bootloader behavior, application compatibility and rollback.
- A OnePlus 12 remains the better ROM experiment because it has existing `/e/OS` support—but it is still not an ideal secure daily driver with `/e/OS` because the bootloader cannot be relocked.

### AT&T news

AT&T announced on August 6 that it is deploying newly acquired **600 MHz spectrum** using Ericsson radios. It says this should improve indoor and rural coverage, capacity and reliability. [AT&T announcement](https://about.att.com/story/2026/att-ericsson-enhance-wireless-nationwide.html)

That makes exact U.S. radio-band support increasingly important. The North American OnePlus 13 supports band 71/n71, which covers 600 MHz operation, but an imported regional version might not receive the same AT&T provisioning. This reinforces the rule: **CPH2655 only**, followed by an AT&T IMEI check.

AT&T’s March 27 approved-device document currently lists:

- OnePlus 13: CPH2655
- OnePlus 13R: CPH2647
- OnePlus 12: CPH2583
- OnePlus 12R: CPH2611

See the [current AT&T approved-device list](https://www.att.com/scmsassets/support/wireless/devices-working-on-att-network.pdf) and [AT&T BYOD checker](https://www.att.com/wireless/byod/).

### Revised buying recommendation

I would now apply these rules:

- **OnePlus 13 around $500–600, new U.S. CPH2655:** still compelling.
- **OnePlus 13 around $700:** questionable; only buy if you particularly love its hardware.
- **OnePlus 13 near its $900 MSRP:** do not buy.
- **Indian or Chinese import:** do not buy for AT&T.
- **Used unit:** only with the model number, IMEI, battery condition and remaining warranty confirmed.

So OnePlus remains a possible choice, but it is no longer my uncomplicated top recommendation. It has become a **high-quality discontinued-platform purchase**: worthwhile at the right discount, not something I would buy at flagship pricing expecting a stable American ecosystem for the next six years.

## Donovan

whats a new top choice

## Codex

I’m reassessing from scratch against your actual constraints: officially reliable on AT&T, usable without a Google account, current U.S. support, and meaningful ownership/modification freedom. The OnePlus exit makes longevity and repairability more important than raw benchmark performance.

## Codex

The new top choice is the **Fairphone Gen 6+ U.S. edition**.

It launched in the United States on August 18, 2026—so it fixes the main problem that previously stopped me from recommending Fairphone to your AT&T family.

### Why it is now the best match

- Officially sold in the United States
- Fairphone explicitly says it is **AT&T BYOD supported and IMEI-whitelisted**
- $649.99 unlocked
- Does not require a Google account for calls, SMS, data or ordinary operation
- Bootloader is officially unlockable
- Supports alternative systems including `/e/OS`, LineageOS and Ubuntu Touch
- Bootloader can potentially be relocked with a compatible signed OS
- Twelve user-replaceable components
- Replaceable battery, display, cameras, USB port and other parts
- MicroSD expansion up to 2 TB
- Five-year warranty after registration
- Software support through 2033
- Fairphone says bootloader modification alone generally does not automatically invalidate coverage for unrelated hardware defects

[Fairphone U.S. store — $649.99](https://us.fairphone.com/)
[Official AT&T compatibility details](https://us.fairphone.com/carrier-compatibility)
[Official bootloader instructions](https://support.fairphone.com/hc/en-us/articles/10492476238865-How-to-unlock-and-re-lock-the-bootloader)
[Fairphone’s Google-free Android explanation](https://support.fairphone.com/hc/en-us/articles/9979154556817-Google-free-Android)

### Specifications

| Component | Fairphone Gen 6+ |
|---|---|
| Price | $649.99 |
| Processor | Snapdragon 7s Gen 4 |
| Memory | 12 GB RAM |
| Storage | 256 GB UFS 3.1 |
| Expansion | microSD up to 2 TB |
| Display | 6.31-inch LTPO OLED, 120 Hz |
| Battery | 4,415 mAh, removable |
| Charging | 30 W wired |
| Rear cameras | 50 MP main + 13 MP ultrawide |
| Front camera | 32 MP |
| OS | Android 16 |
| Updates | Through 2033 |
| Warranty | Five years after registration |
| Repairability | Twelve replaceable modules |
| SIM | Physical SIM and eSIM support |
| Water resistance | IP55 |
| Wireless charging | None |

This is midrange performance, not OnePlus 13 flagship performance. It will handle Obsidian, messaging, social media, navigation, VPNs, Garmin, music, video and ordinary games comfortably, but it is not intended to compete with high-end gaming phones.

### The AT&T compromises

Fairphone says the U.S. Gen 6+ is supported for AT&T BYOD, but it discloses these limitations:

- No AT&T Wi-Fi calling
- No AT&T RCS provisioning
- No LTE bands 14, 29 or 30
- No FirstNet support
- No mmWave 5G
- No 600 MHz n71 support

Ordinary cellular calls, SMS, LTE and sub-6 5G are supported. The phone covers AT&T’s important LTE bands 2, 4, 5, 12, 17 and 66, plus 5G n2, n5, n66 and n77.

The most noticeable loss compared with an iPhone is **Wi-Fi calling**. If your house or school has weak AT&T reception and relies on Wi-Fi calling, this could be more than a minor inconvenience. AT&T’s recent investment in 600 MHz coverage also won’t fully benefit this phone because it lacks n71.

### How I would configure it

Initially:

1. Purchase the **U.S. Gen 6+**, not the European Gen 6 or an imported model.
2. Keep Fairphone OS and the bootloader locked.
3. Skip Google-account login.
4. Disable the Google applications you don’t want.
5. Use F-Droid, Obtainium and Aurora Store.
6. Test calls, SMS, voicemail, data, hotspot and emergency calling throughout your normal locations.
7. Only install `/e/OS` after several months, once the U.S. model’s AT&T behavior and relocking procedure are well documented.

That gives you reliable stock software during school while preserving a genuine path to a Google-free system later.

The phone is currently shown as **out of stock** on Fairphone’s U.S. store, but there is a restock notification option. I would wait for official U.S. inventory instead of importing one.

My revised verdict:

- **Best match for freedom, repairability and long ownership:** Fairphone Gen 6+
- **Best raw hardware at a discount:** OnePlus 13
- **Best guaranteed AT&T feature completeness:** neither—mainstream AT&T phones still win there

For your priorities, I would choose the **Fairphone Gen 6+**, provided you first confirm that you do not depend on AT&T Wi-Fi calling.

## Donovan

compare to iPhone 16 Pro, what do I lose, what do I get?

## Codex

I’ll make this a practical switch comparison—not just a spec sheet—including the Apple ecosystem features you would actually surrender, Fairphone’s gains in ownership and privacy, and the AT&T limitations that could affect daily reliability.

## Codex

The Fairphone Gen 6+ gives you dramatically more ownership, repairability, and software freedom—but it is a noticeable hardware and carrier-feature downgrade from your iPhone 16 Pro.

## At a glance

| | iPhone 16 Pro | Fairphone Gen 6+ |
|---|---|---|
| Original/current price | Started at $999 | $649.99 |
| Display | 6.3″ OLED, 120 Hz, 2622×1206 | 6.31″ OLED, 120 Hz, approximately FHD+ |
| Processor | A18 Pro flagship | Snapdragon 7s Gen 4 midrange |
| Memory | 8 GB | 12 GB |
| Storage | 128 GB–1 TB | 256 GB |
| Expansion | None | microSD up to 2 TB |
| Cameras | 48 MP main, 48 MP ultrawide, 12 MP 5× telephoto, LiDAR | 50 MP main, 13 MP ultrawide, no telephoto |
| Battery | Sealed | User-replaceable, 4,415 mAh |
| Charging | Wired, 25 W MagSafe, Qi2 | 30 W wired only |
| Water resistance | IP68, 6 m/30 minutes | IP55 |
| Repairability | Difficult, paired components | Twelve replaceable modules |
| Software control | Locked bootloader, Apple-approved software | Unlockable/relockable bootloader, alternative operating systems |
| Support | Historically long, no fixed endpoint stated here | Promised through 2033 |
| AT&T integration | Complete | Basic service supported, important features missing |

Apple’s complete specification sheet is available [here](https://support.apple.com/en-us/121031). Fairphone’s U.S. listing is [here](https://us.fairphone.com/).

## What you lose

### 1. Considerably better cameras

This is probably the biggest hardware loss.

The iPhone has:

- A dedicated 5× optical telephoto camera
- A much better ultrawide camera
- Macro photography
- LiDAR
- Excellent stabilization
- ProRAW and advanced video formats
- More reliable low-light photography
- 4K video with polished stabilization and consistent color
- Camera Control button

The Fairphone has a capable main camera but only a 13 MP ultrawide and no telephoto lens. It should be adequate for documenting school, workouts and ordinary life, but the iPhone is a substantially better photo and video-production tool—particularly if you start that YouTube channel.

### 2. Flagship performance

The A18 Pro is much more powerful than the Snapdragon 7s Gen 4. You would notice this most in:

- Demanding games
- Emulation
- Video editing and exporting
- Computational photography
- Long-term responsiveness under increasingly demanding software
- High-performance creative applications

The Fairphone should remain comfortable for Obsidian, social media, LibreOffice-style document access, music, Garmin, maps, VPNs and ordinary applications. It simply is not a gaming or video-production flagship.

### 3. Complete AT&T feature support

This is the most concerning daily-life compromise.

Fairphone says normal AT&T cellular service is supported, but its current U.S. compatibility page says the Gen 6+ lacks:

- **Wi-Fi calling**
- **AT&T RCS**
- IR.94 carrier video calling
- LTE bands 14, 29 and 30
- mmWave 5G
- FirstNet
- Some carrier-specific features

It supports AT&T LTE bands 2, 4, 5, 12, 17, 26 and 66, and 5G n2, n5, n66 and n77. See [Fairphone’s AT&T disclosure](https://us.fairphone.com/carrier-compatibility).

The absence of Wi-Fi calling matters if your house, school or travel destinations have weak indoor service. The lack of AT&T RCS means your default texting experience may fall back to SMS/MMS instead of providing dependable high-resolution media, typing indicators and read receipts.

Your iPhone provides much more complete AT&T integration.

### 4. Apple communication features

You lose native access to:

- iMessage
- FaceTime
- AirDrop
- SharePlay
- NameDrop
- Apple’s Continuity features
- iCloud Shared Photo Library
- Apple-family location and purchase sharing

You can replace these with Signal, WhatsApp, Discord, LocalSend, Syncthing, Proton Drive and other cross-platform services—but friends and family must cooperate. There is no perfect independent replacement for iMessage when everyone around you uses iPhones.

Before switching, you must deregister iMessage so messages to your number do not disappear into Apple’s system.

### 5. Apple hardware integration

These stop working or become limited:

- **Apple Watch:** essentially unusable without an iPhone. Replace it with Garmin.
- **AirTags:** no proper Find My network management. Replace with a tracker compatible with your chosen Android arrangement, though most large tracker networks belong to Google or another major vendor.
- **AirPods:** basic Bluetooth audio and controls continue, but seamless pairing, Find My, automatic Apple-device switching, firmware management and some spatial-audio features are lost.
- Mac features such as Handoff, Universal Clipboard, iPhone Mirroring and Continuity Camera are lost.

### 6. Apple Pay and polished tap-to-pay

NFC hardware is present, but deGoogling complicates mobile payments.

On stock Fairphone Android, Google Wallet is the mainstream contactless-payment solution. If you refuse a Google account or install `/e/OS`, dependable bank-card tap-to-pay may be unavailable. Some bank applications also reject modified software.

The safest independent answer is carrying a physical contactless card.

### 7. Premium construction and protection

You move from:

- Titanium and glass to a repair-oriented plastic/modular construction
- IP68 to IP55
- Ceramic Shield to a more conventionally protected display
- A thinner 8.25 mm phone to a thicker approximately 9.6 mm phone
- Premium haptics and speakers to midrange components

IP55 handles rain and water jets, but it does **not** certify submersion. Dropping the Fairphone in a pool is a much larger concern.

### 8. Wireless charging and MagSafe

Fairphone has neither. You lose:

- MagSafe charging
- Qi/Qi2 charging
- Magnetic battery packs and stands without a special case
- Magnetic car-mount integration unless added through an accessory

You gain a removable battery, which is arguably more useful for longevity, but less convenient every night.

### 9. Emergency and location hardware

The iPhone provides a more mature emergency package, including satellite features in supported regions, Crash Detection and Apple’s Find My network. Fairphone does not provide a comparable integrated satellite-emergency system or ultra-wideband finding system.

That is a real safety downgrade for rowing trips, hiking or travel away from cellular coverage.

## What you gain

### 1. Actual physical ownership

You can personally replace:

- Battery
- Display
- USB-C port
- Main and ultrawide cameras
- Speaker
- Earpiece
- Back cover
- Other internal modules

The parts are designed to be replaced with ordinary tools rather than adhesives and serialized repair procedures. A worn battery no longer means scheduling a service appointment or replacing the phone.

### 2. Operating-system freedom

Fairphone officially lets you:

- Unlock the bootloader
- Install `/e/OS`
- Install LineageOS or other supported systems
- Return to official Fairphone OS
- Potentially relock the bootloader with appropriately signed and compatible software
- Download factory images
- Use standard Android platform tools

Fairphone explicitly describes bootloader freedom as part of device longevity. Its [official instructions](https://support.fairphone.com/hc/en-us/articles/10492476238865-How-to-unlock-and-re-lock-the-bootloader) are unusually supportive.

The iPhone gives you effectively none of this.

### 3. Google-account independence

On stock Fairphone OS, you can skip Google login and still use:

- Calls and SMS
- Cellular data and hotspot
- Bluetooth
- VPNs
- Camera and local storage
- Browser-based services
- Sideloaded applications
- F-Droid and Obtainium
- Aurora Store, subject to its current availability and policies
- Obsidian and Syncthing

Later, `/e/OS` can remove most direct Google components while using microG for some compatibility. That is much closer to the Linux-style ownership you want.

### 4. Real filesystem access and application choice

You gain:

- Easier local file management
- Installing software outside one mandatory store
- Alternative launchers and keyboards
- Replaceable default browser, assistant, dialer and messaging applications
- ADB access
- Automation tools
- Better Syncthing integration
- Termux and a capable command-line environment
- More direct interaction with Chiron and your Obsidian vault

Android still has sandboxing and security restrictions—it is not desktop Linux—but it is substantially less restrictive than iOS.

### 5. Expandable storage

A microSD card up to 2 TB is valuable for:

- Offline music
- Videos
- LibreOffice documents
- Obsidian attachments
- Garmin exports
- Camera archives
- Local maps
- Encrypted backups

You are no longer forced to select and permanently pay for storage at purchase.

### 6. Fingerprint unlocking

You gain a side-mounted fingerprint sensor. This can be more convenient than Face ID when wearing certain equipment, sitting at a desk or unlocking the phone without pointing it at your face.

You lose Apple’s exceptionally polished 3D Face ID; Fairphone’s face unlocking should not be treated as an equivalent biometric system.

### 7. Longer practical hardware life

Fairphone promises support through 2033 and sells replaceable components. More importantly, its design gives the phone a plausible life beyond official support because batteries, ports and operating systems can be changed.

That aligns extremely well with the Corsaya idea: the device serves your system instead of forcing your system to revolve around the vendor.

## Honest conclusion

The Fairphone Gen 6+ is **not an iPhone 16 Pro with the restrictions removed**. It is a different trade:

> You surrender flagship cameras, premium construction, complete AT&T integration and seamless consumer conveniences in exchange for repairability, expandable storage, software choice and genuine control.

For you, the major decision points are:

- If **AT&T Wi-Fi calling, excellent video and effortless family messaging** are essential, the Fairphone is currently too compromised.
- If **ownership, deGoogling, repairability and running your own workspace** matter more, it is the strongest philosophical and practical match.
- If you want freedom while losing as little iPhone functionality as possible, we should keep searching for a middle option. Fairphone sits near the freedom end of the spectrum, not the “zero-compromise flagship” middle.

I would not sell or trade the iPhone immediately. If you buy the Fairphone, keep the iPhone for the return period and test AT&T reception at home, school, crew practice and your normal travel routes before committing.

## Donovan

what would you recommend for me, still a normal high school senior

## Codex

For you specifically, I recommend **keeping the iPhone 16 Pro through the beginning of senior year while de-Apple-ing your services**, then reevaluating the Fairphone Gen 6+ after its first few months on AT&T.

That is less exciting than immediately switching, but it fits your actual situation better.

You currently need your phone to reliably handle:

- Family communication
- School messages and Google Classroom
- College applications and authentication codes
- Calendar reminders and deadlines
- Crew and fitness tracking
- Navigation and emergency communication
- Photos or video for a possible YouTube channel

The iPhone 16 Pro is already excellent at all of those. Selling it now for a newly released Fairphone—with no AT&T Wi-Fi calling or RCS—would introduce friction exactly when summer work, school and college applications are becoming important.

### What I would do

Keep the iPhone as a dependable communication appliance, but stop allowing Apple to own your underlying information:

- Move passwords to Bitwarden or KeePassXC.
- Move important files into your Obsidian/Chiron system.
- Use Proton Mail or another independent address for new personal accounts.
- Use Firefox instead of Safari.
- Build a CalDAV calendar and CardDAV contacts system rather than expanding dependence on iCloud.
- Export photos regularly to your Linux computer and local storage.
- Use Signal for people willing to adopt it.
- Choose Garmin instead of Apple Watch.
- Buy ordinary Bluetooth earbuds rather than AirPods.
- Avoid purchasing new Apple-only accessories.
- Keep school Google access isolated as a necessary connector, not your personal digital identity.

That turns the iPhone into a replaceable client of your workspace rather than the place where your life is stored.

### When I would reconsider Fairphone

Revisit the Gen 6+ around winter break or after your college applications are submitted. By then we should know:

- Whether AT&T activation is consistently reliable
- Whether calls and voicemail work correctly in real-world use
- Whether AT&T adds RCS or Wi-Fi calling
- Whether `/e/OS` is stable on the U.S. hardware
- Whether the bootloader can be safely relocked
- Whether replacement components remain readily available
- How its camera, battery and performance hold up in longer reviews

If those results are positive, the Fairphone becomes a much safer switch.

### If you insist on switching now

My recommendation would be:

1. **U.S. OnePlus 13 CPH2655 at approximately $500–600** — least disruptive transition, strongest hardware and officially approved by AT&T, despite OnePlus leaving America.
2. **Fairphone Gen 6+** — most freedom and repairability, but accept weaker cameras, no wireless charging, no AT&T Wi-Fi calling and no AT&T RCS.
3. **Keep the iPhone** — least freedom but by far the lowest operational risk.

I would personally choose option three for the next several months. Senior year is not the ideal moment to turn your only phone into an infrastructure experiment. Build Chiron and your vendor-independent data system first; then switching phones becomes much easier because the phone no longer owns anything essential.

## Donovan

i dont need to switch, just interested in switching, Apple gear for new phone (freedom focused, but still needs iPhone capabilities - Apple external hardware support) new watch (can get whenever) and earbuds (also whenever)

## Codex

That changes the recommendation substantially: **don’t treat this as an urgent replacement—build a portable device ecosystem first, then switch when the right phone is mature.**

Your ideal setup is:

- Freedom-focused phone
- Garmin watch
- Platform-neutral earbuds
- Obsidian/Chiron as the information layer
- Apple equipment retained wherever it still works
- Google and Microsoft used only for necessary services

### What Apple hardware survives an Android switch?

| Apple hardware/service | With Fairphone/Android |
|---|---|
| AirPods | Bluetooth audio works; Apple-specific configuration, Find My, automatic switching and some spatial features are lost |
| Apple Watch | Effectively incompatible; requires an iPhone |
| AirTags | Cannot properly configure or track them through Apple Find My |
| MagSafe stands/mounts | Work with a magnetic Fairphone case or adhesive ring |
| MagSafe charging | Fairphone cannot use it because it lacks wireless charging |
| USB-C chargers/cables | Generally reusable |
| Mac | Works through browser services, Syncthing, LocalSend and standard USB; Apple Continuity features disappear |
| Apple TV | Streaming apps still work, but AirPlay integration becomes less consistent |
| HomePods | Poor fit without an iPhone; heavily tied to Apple services |
| Apple Music | Android application available, though it still requires an Apple account |
| iCloud Mail/calendar | Can be accessed, but I would migrate away gradually |
| iMessage/FaceTime | No native Android support |
| Apple Card/Apple Cash | No proper Android support |

The Apple Watch is the only major piece that creates a hard dependency. AirPods are usable, just less intelligent.

### My recommended equipment path

**Phone: wait and watch the Fairphone Gen 6+.**

It is the best freedom-oriented candidate for you, but its current AT&T deficiencies keep it from being an automatic purchase. Give the American launch time to develop. If AT&T Wi-Fi calling and RCS improve—or user reports show you won’t miss them—it becomes compelling.

A phone like the OnePlus 13 has better iPhone-like hardware, but OnePlus’s American exit makes it less attractive as a future ecosystem foundation.

**Watch: Garmin Forerunner 570.**

You can buy this independently of the phone decision. It works with both iPhone and Android, tracks rowing and general fitness, and doesn’t trap your exercise history inside Apple Health. We should eventually make Chiron import Garmin FIT/TCX exports so your workspace owns the permanent record.

Choose the Forerunner 970 only if its extra navigation, maps and premium construction are genuinely worth the additional money. The 570 is sufficient for your crew and general fitness goals.

**Earbuds: Nothing Ear (3).**

They are ordinary Bluetooth earbuds with good codec support and do not bind you to Apple or Google. They work with your current iPhone, a future Fairphone and Linux. Their companion application adds configuration but isn’t required for basic listening.

Fairbuds are philosophically stronger because their batteries and components are replaceable, but Nothing Ear (3) is the safer recommendation if sound quality and active noise cancellation matter more than repairability.

### The ecosystem I’d build

The important move is making every new purchase phone-independent:

- Garmin instead of Apple Watch
- Neutral Bluetooth earbuds instead of deeper AirPods investment
- Bitwarden/KeePassXC instead of Apple Passwords
- Proton/CalDAV instead of iCloud-only mail and calendar
- Obsidian and Chiron instead of Apple Notes
- Syncthing or another open file system instead of iCloud Drive
- Physical NFC card instead of depending entirely on Apple Pay or Google Wallet
- Local photo archive instead of an iCloud-only library
- Signal alongside ordinary SMS
- USB-C and standard magnetic mounts rather than proprietary accessories

Then your eventual phone choice becomes much less consequential. You can keep enjoying the iPhone 16 Pro today while systematically ensuring that nothing prevents you from leaving tomorrow.

My current buying order would therefore be:

1. Garmin Forerunner 570 whenever you are ready to begin consistent fitness tracking.
2. Nothing Ear (3) when you need earbuds.
3. Continue monitoring the Fairphone Gen 6+ rather than buying immediately.
4. Reassess the phone after AT&T reports and `/e/OS` support mature.

That gives you freedom through **portability**, not merely through owning an unusual phone.

## Donovan

any other phones to monitor, or is Fairphone Gen 6+ the best choice? Not looking to swtich until either college or possibly before if a good opportunity presents itself.

## Codex

I’ll build a watchlist rather than force a single answer now. I’m filtering for credible future U.S./AT&T operation, bootloader or alternate-OS potential, repairability, and enough camera/performance quality to replace an iPhone without becoming a hobby project.

## Codex

Fairphone Gen 6+ is the best choice you could buy today for repairability and ownership, but it may not be the best choice by college. The most important phone for you to monitor is the forthcoming **2027 Motorola–GrapheneOS flagship**.

## Your watchlist

### 1. 2027 Motorola flagship with GrapheneOS

This is potentially your ideal phone.

Motorola and GrapheneOS are working on new flagship hardware expected in 2027. Reports indicate that the devices will be designed to satisfy GrapheneOS’s security requirements instead of merely allowing an unofficial ROM installation. Initial candidates are expected to resemble Motorola’s flagship Signature and Razr families, although the exact supported model has not been announced.

Why this could surpass Fairphone for you:

- Flagship processor and cameras
- Mainstream U.S. manufacturer and service network
- Strong likelihood of proper AT&T support
- GrapheneOS with verified boot and a relocked bootloader
- No required Google account
- Google Play can be installed as an ordinary sandboxed application only when needed
- Strong application compatibility without making Google a privileged system service
- Better security than most community ROMs
- Likely wireless charging, IP68 and other iPhone-class features

The tradeoff is that it probably won’t be modular or user-repairable like Fairphone, and early reporting says it could cost more than a Pixel—possibly conventional flagship pricing.

Important: existing Motorola phones will not retroactively gain GrapheneOS support. Do not buy an Edge 2026 or Razr 2026 expecting to install it later. [GrapheneOS partnership discussion](https://discuss.grapheneos.org/d/32656-motorola-partnership-announcement), [current reporting](https://arstechnica.com/gadgets/2026/08/motorolas-grapheneos-phones-will-launch-in-2027-priced-higher-than-pixels/).

This is the one I would wait for.

### 2. Fairphone Gen 6+ and its successor

Fairphone remains the benchmark for:

- Replaceable battery
- Twelve replaceable modules
- microSD storage
- Five-year warranty
- Support through 2033
- Official bootloader unlocking
- `/e/OS`, LineageOS and other alternatives
- Ethical manufacturing and material sourcing

Monitor whether the U.S. model gains:

- AT&T Wi-Fi calling
- AT&T RCS
- More complete AT&T band coverage
- Stable official `/e/OS` support for the U.S. variant
- Reliable bootloader relocking
- Better camera software
- Wider availability of spare parts

Also watch for a future Fairphone generation. Your iPhone remains capable enough that you do not need to buy the first U.S. Fairphone merely because it finally exists. [Fairphone U.S. store](https://us.fairphone.com/), [carrier limitations](https://us.fairphone.com/carrier-compatibility).

### 3. Nothing’s next fully supported U.S. phone

Nothing is worth monitoring, but not currently buying for your AT&T line.

Why it is interesting:

- Distinctive hardware
- Relatively clean Android interface
- Standard Bluetooth and USB-C ecosystem
- Bootloader modification is possible on some models
- More conventional cameras and performance than Fairphone
- Does not fundamentally require a Google account for telephone service

Why it is not ready:

- Several American devices have been sold through a “Beta Program.”
- Nothing explicitly warns that full compatibility is not guaranteed across U.S. carriers.
- AT&T’s approved list currently names only the older Nothing Phone 2.
- It is not intrinsically deGoogled.
- Custom-ROM support and long-term repairability are weaker than Fairphone.

Monitor the first Nothing flagship that receives normal U.S. retail distribution and explicit AT&T certification—not another beta-program import. [Nothing U.S. Beta Program](https://us.nothing.tech/pages/beta-program).

### 4. Future mainstream unlocked Motorola phones

Even without GrapheneOS, Motorola is a useful fallback because it sells directly through AT&T and the unlocked U.S. market. The Edge 2026 has wireless charging, a telephoto camera, IP68/IP69 protection and mainstream carrier integration.

However, the current Edge 2026 reportedly promises only two Android-version upgrades and three years of security updates. That is inadequate for a phone purchased with long-term ownership in mind. Its carrier-branded version is also likely to restrict bootloader unlocking.

Therefore:

- Monitor Motorola’s 2027 models.
- Prefer a factory-unlocked retail model.
- Do not buy the AT&T-branded version if bootloader freedom matters.
- Require at least five to seven years of security support.
- Wait for confirmed GrapheneOS compatibility rather than assuming it.

[Motorola Edge 2026](https://www.motorola.com/us/en/p/phones/motorola-edge/edge-2026/pmipmjr44mu), [AT&T listing](https://www.att.com/buy/phones/motorola-edge-2026.html).

## Phones I would not seriously consider for your primary line

- **Volla, SHIFTphone, Jolla, FuriPhone and Linux phones:** interesting projects, but inadequate evidence of complete AT&T support, application compatibility and ordinary American repair service.
- **Imported Oppo, Xiaomi or Chinese OnePlus models:** radio provisioning, warranty and bootloader problems.
- **PinePhone or Librem 5:** valuable Linux experiments, not dependable iPhone replacements for a student.
- **Current Nothing beta devices:** insufficient AT&T certainty.
- **Current Motorola bought specifically for a future ROM:** GrapheneOS support will require new 2027 hardware.
- **OnePlus 16:** no official U.S. launch is planned.

## My projected decision

If you switch before the 2027 Motorola launch:

> Fairphone Gen 6+, but only after verifying AT&T performance in your actual locations.

If you switch around college:

> First evaluate the 2027 Motorola–GrapheneOS flagship against whatever Fairphone offers at that point.

The likely final comparison will be:

| Priority | Likely winner |
|---|---|
| Security and privacy | Motorola + GrapheneOS |
| iPhone-like performance | Motorola + GrapheneOS |
| AT&T integration | Motorola, if officially certified |
| Repairability | Fairphone |
| Replaceable battery | Fairphone |
| Alternative operating-system variety | Fairphone |
| Google-free application compatibility | GrapheneOS |
| Long physical service life | Fairphone |

Because you are willing to wait, I would **not choose Fairphone conclusively yet**. Keep it as the current baseline, but place the 2027 Motorola–GrapheneOS phone at the top of your monitoring list. It has the best chance of delivering freedom without giving up as many iPhone capabilities.

## Donovan

i like the look of grapheneOS, open source is my jam, would this be a good phone for managing my projects outside of home, as well as functioning as a regular phone that won't be a hinderance rather than a great assist?

## Codex

I’ll separate what GrapheneOS can already do reliably from what remains unknown about the 2027 Motorola hardware. The operating system looks promising for your mobile workspace, but I don’t want to treat an unannounced phone as guaranteed.

## Codex

Yes—**GrapheneOS could be an excellent project-management phone for you while remaining a normal phone**, especially if the 2027 Motorola device delivers flagship hardware and proper AT&T certification.

Unlike many “privacy phones,” GrapheneOS is designed around application compatibility and daily usability. It is hardened Android, not a limited Linux-phone experiment. The qualification is that the Motorola hardware hasn’t been announced, so we cannot yet guarantee its cameras, AT&T support or desktop capabilities.

## How it could manage your projects

A GrapheneOS phone could serve as the mobile interface to Chiron and your Obsidian system:

- Read and edit your Obsidian vault.
- Capture quick notes, tasks, photos and voice recordings.
- Access Chiron through a web interface or future Android client.
- Review school assignments and calendar events.
- Use Git through Termux when necessary.
- SSH into your Linux computer or server.
- Run Syncthing or another synchronization system.
- Review GitHub issues and repositories.
- Edit ordinary documents and spreadsheets.
- Upload scans, receipts and class materials.
- Access Garmin training information.
- Connect through WireGuard or another VPN.
- Use a remote desktop when a task genuinely requires your home computer.

It would not replace your Linux computer for serious programming, long writing, LibreOffice work or vault restructuring. The right relationship is:

> Phone captures, retrieves, communicates and approves; your computer creates and administers.

That keeps the phone useful without trying to turn a six-inch screen into your entire workstation.

## A profile structure that fits you

GrapheneOS supports strongly isolated user profiles with separate applications, storage, contacts and encryption keys. You could organize it like this:

- **Personal:** Signal, phone, camera, Garmin, music and ordinary life.
- **School:** Google Classroom, school Gmail, Drive and authentication applications.
- **Corsaya:** Obsidian, Chiron, GitHub, Termux, calendar and project tools.
- **Restricted social:** Instagram, Discord, YouTube and any intrusive applications.
- **Private:** sensitive local material, kept logged out when not needed.

When a profile is ended, its applications stop running and its encryption keys are removed from active memory. That is much stronger separation than merely putting applications into folders.

GrapheneOS also lets you selectively expose contacts and files through Contact Scopes and Storage Scopes. Instagram could receive only the photographs you choose instead of your complete library, for example. [GrapheneOS features](https://grapheneos.org/features)

## Google access without Google ownership

Your school applications are likely to require Google components. GrapheneOS handles this unusually well:

- Google Play is not included by default.
- You can install it only inside the School profile.
- It runs as ordinary sandboxed applications without privileged system access.
- A Google account is optional unless a particular service requires login.
- Applications outside that profile cannot use or communicate with that Play installation.
- GrapheneOS’s own system services do not depend on Play Services.

That means your school can require Google Classroom without requiring Google to occupy the privileged core of your entire phone.

GrapheneOS reports near-complete Android application compatibility through sandboxed Play. It also supports Android Auto with explicitly selected additional permissions. [GrapheneOS usage guide](https://grapheneos.org/usage)

## Regular-phone behavior

On properly certified hardware, you should expect:

- Normal calling and SMS
- Cellular data and hotspot
- 5G, VoLTE and potentially Wi-Fi calling
- RCS through Google Messages and sandboxed Play, when supported by the carrier
- Bluetooth earbuds and Garmin watches
- Camera, maps and navigation
- VPNs
- Push notifications
- Banking and school applications in most cases
- Android Auto
- Fingerprint authentication
- Automatic background security updates
- Emergency calling

Some banking and authentication applications can still cause problems because they use crude custom integrity checks. GrapheneOS documents workarounds for many cases, but compatibility cannot be guaranteed for every bank. That should be tested during the phone’s return window.

## Why it could be more helpful than an iPhone

GrapheneOS would give you:

- More control over application installation
- Better filesystem access
- Per-application network permission
- Isolated identities through profiles
- Sandboxed Google access
- Termux, SSH and Git tools
- Better integration with Linux and Syncthing
- Sideloading without Apple’s approval
- A hardened open-source operating system
- A locked bootloader and verified boot after installation
- Automatic updates without turning the phone into an insecure custom-ROM project
- The ability to use Google applications selectively without granting Google system-level authority

This is more useful than freedom for its own sake. It would let the phone reflect the same architecture planned for Chiron: separate sources and identities, deliberate permissions and locally owned data.

## What could make it a hindrance

The phone would become a burden if you:

- Constantly change system components or root it.
- Install every application in a different profile without a coherent reason.
- Refuse sandboxed Play even when a required school application needs it.
- Attempt to run your entire Obsidian vault and development stack directly on the phone.
- Buy an unsupported international Motorola variant.
- Choose a carrier-branded version whose bootloader cannot be unlocked.
- Purchase before AT&T, GrapheneOS and Motorola publish exact compatibility information.

GrapheneOS specifically expects the bootloader to be relocked after installation. Running permanently unlocked is considered an incomplete and unsupported installation. This makes it much safer than the common “rooted custom ROM” approach. [GrapheneOS FAQ](https://grapheneos.org/faq)

## Purchase requirements for the future Motorola

Before I recommend buying it, I would verify:

1. Official GrapheneOS support for the exact model number.
2. Factory-unlocked U.S. hardware—not an AT&T-branded variant.
3. AT&T approval for VoLTE, Wi-Fi calling, RCS, visual voicemail and 5G.
4. Complete AT&T low-band and mid-band coverage.
5. At least five to seven years of firmware support.
6. Relockable bootloader with verified boot.
7. Working banking, Garmin, school and authentication applications.
8. Good cameras and video stabilization.
9. USB 3 and preferably DisplayPort output.
10. Repair availability in the United States.
11. Normal eSIM and emergency-calling behavior.
12. A return window long enough to test your real locations.

My judgment: **the forthcoming Motorola–GrapheneOS phone is currently the most promising future replacement for you.** It offers a better chance than Fairphone of matching the iPhone’s performance and carrier reliability, while giving you much stronger privacy, open-source software and project-management flexibility.

The smartest course is to keep the iPhone, develop Chiron as a device-independent workspace, and watch this Motorola launch closely. If the final hardware and AT&T support satisfy that checklist, it could become a great assistant rather than a technological hobby you must constantly maintain.

## Donovan

ok, think you can make a bit of a roadmap for chiron. before, I would read the entire codebase of the pytheas vault, if that's too much, I can wait until 2

## Codex

Yes. I’ll read the Pytheas vault and the actual Pytheas/Chiron repositories before drafting the roadmap, so it reflects what exists rather than the older planning notes. I’ll treat “entire codebase” as all source, configuration, tests, and architecture documentation; I’ll inventory generated assets and dependencies without wasting time line-reading vendored/build output. I won’t reorganize or edit existing vault files during this pass.

## Codex

The existing handoff already contains a sensible senior-year phase plan, but parts of its architecture description are stale—for example, it credits Chiron with SAT applications that were later removed. I’m now reconciling those plans against the current source trees and commit history before proposing a replacement roadmap.

## Codex

Yes. I can produce a proper roadmap, but I have not finished reading everything yet.

Current audit status:

- Inventoried all **316 files** in the Pytheas vault.
- Inspected the Pytheas repository’s **30 tracked source files / 8,896 lines**.
- Ran its complete test suite: **42/42 tests pass**.
- Reviewed the current Chiron commits and the relevant architecture, vault, task, calendar, classroom and workspace areas.
- Confirmed Chiron contains approximately **1,362 tracked files**, largely inherited from Odysseus.
- Confirmed the newest Chiron commit removed the SAT classroom applications, making several vault descriptions stale.

I would not line-read generated SAT screenshots, repeated briefings, bundled JavaScript libraries or Chiron’s inherited test fixtures. I will inventory those, but concentrate close reading on authored code and architecture.

## Draft Chiron roadmap

### Architectural division

Before adding features, establish permanent responsibilities:

| Component | Responsibility |
|---|---|
| **Obsidian** | Durable human-readable knowledge: notes, school materials, project documentation, journal ciphertext |
| **Chiron** | Main workspace interface: dashboard, search, calendar, assignments, documents, connectors and mobile access |
| **Host-side SQLite** | Structured operational state: tasks, deadlines, accounts, logs, knowledge progress and fitness data |
| **Pytheas** | Small experimental capability laboratory: voice, local actions, model routing and prototypes |
| **Codex/models** | Replaceable reasoning layer, never the sole owner of information |

The crucial decision is that **Chiron becomes the product, while Pytheas becomes its experimental workshop**. Maintaining two competing workspace applications will waste time.

### Phase 0 — Establish the truth

Before new development:

- Produce a current feature inventory for Pytheas and Chiron.
- Mark each feature as working, partial, stale or inherited-but-unused.
- Correct vault documentation that still claims Chiron contains the removed SAT applications.
- Establish how personal Chiron commits remain separate from upstream Odysseus.
- Record the minimum test and startup commands.
- Decide which Pytheas capabilities deserve migration into Chiron.
- Do not migrate a capability merely because it exists.

Deliverable: one authoritative architecture and status document.

### Phase 1 — Secure data foundation

Build the host-side database before another interface feature.

Initial tables should be limited to:

- `accounts`
- `connectors`
- `events`
- `tasks`
- `artifacts`
- `courses`
- `knowledge_state`
- `fitness_activities`
- `sync_runs`
- `audit_log`

Requirements:

- Database lives outside Chiron’s container.
- Automatic backup and tested restore.
- Every imported object records its source account.
- External identifiers remain separate from Chiron identifiers.
- Secrets remain in an OS keyring or restricted secret store—not SQLite or Obsidian.
- Migrations are versioned and tested.

Deliverable: the workspace can be rebuilt without losing its structured state.

### Phase 2 — Mobile-ready daily cockpit

Before copying Notion or Classroom, make Chiron useful every day:

- Today’s events
- Deadlines
- Three current priorities
- School assignments
- Quick capture
- Recently used project files
- Fitness summary
- Connector health
- Inbox of unprocessed information

Make it a responsive installable PWA, suitable for a future GrapheneOS phone. Remote access should initially use a private VPN such as WireGuard or Tailscale—not an openly exposed home server.

Deliverable: Chiron is genuinely useful from your phone away from home.

### Phase 3 — Accounts and connectors

Implement connectors as isolated accounts rather than one universal Google login:

- Personal Google
- School Google
- Future college Google or Microsoft account
- Independent mail/calendar account
- GitHub
- Garmin later

Each connector receives:

- Separate OAuth tokens
- Explicit scopes
- Read-only access first
- Last-successful-sync timestamp
- Revocation control
- Visible error state
- Import provenance

Start with calendars and assignments. Email sending, file mutation and calendar writing come later because they carry more risk.

Deliverable: Chiron can show information from multiple accounts without merging their identities or permissions.

### Phase 4 — School workspace

Model Google Classroom’s useful behavior without trying to reproduce Google itself:

- Course dashboard
- Subject pages
- Assignment list
- Due dates
- Materials and attachments
- Submission-status tracking
- Teacher announcements
- Links back to the authoritative school service

Documents should open through either:

- LibreOffice Writer
- LibreOffice Calc
- LibreOffice Impress
- Collabora in the browser, if a web editor becomes worthwhile

Use open formats where possible:

- `.odt`
- `.ods`
- `.odp`
- PDF for submission snapshots
- DOCX/XLSX/PPTX only when compatibility requires them

Deliverable: one subject can complete a full assignment cycle through Chiron before expanding to every class.

### Phase 5 — Obsidian bridge

Build the actual connection between structured state and durable notes:

- Tasks written in approved Markdown syntax enter SQLite.
- Calendar events appear in daily notes.
- Project dashboards link to relevant notes.
- Chiron search returns both structured records and vault documents.
- Every generated note declares its source and generation time.
- Small captures enter an inbox instead of becoming premature permanent notes.
- Notes graduate into permanent folders only after meeting a usefulness threshold.

A candidate permanent-note requirement:

- Clear title
- One-sentence purpose
- Source or provenance
- At least one meaningful link
- Enough content to support a future action, decision or retrieval

Deliverable: Obsidian and Chiron stop behaving like two separate systems.

### Phase 6 — Fitness and crew

- Import Garmin FIT/TCX files.
- Store workout measurements in SQLite.
- Keep reflections and training notes in Markdown.
- Track rowing sessions, erg tests and coach-provided plans.
- Never generate medical or weight-cut decisions.
- Compare scheduled training with completed training.
- Produce weekly trends without inventing coaching conclusions.

Deliverable: Garmin can disappear as a company without taking your training history with it.

### Phase 7 — Private journal broker

The journal should not rely on folder naming as its security boundary.

Build an encrypted store with two interfaces:

- Metadata interface: list, move, duplicate, rename, delete and back up.
- Content interface: unavailable to Chiron and AI unless you deliberately unlock a specific entry.

The encryption key should not be held continuously by the Chiron server.

Deliverable: Chiron can manage journal objects without reading their contents.

### Phase 8 — Retrieval and agent behavior

Only after the underlying information is trustworthy:

- Hybrid lexical and semantic search
- Related-note recommendations
- Project context packages
- Source citations for recalled facts
- Per-project agent permissions
- Draft-before-action workflow
- Audit log for every external write
- A mobile approval queue

The assistant should retrieve the minimum relevant material rather than ingesting the entire vault into every conversation.

Deliverable: ask “What is blocking Chiron?” or “What is due for AP Physics?” and receive a sourced answer.

### Phase 9 — Expansion

Only after daily use proves the foundation:

- Email triage and drafting
- Calendar writeback
- College-application workspace
- YouTube production pipeline
- Course/SRS engine
- Local voice control
- More advanced automations
- Optional local-model routing

## Immediate build order

For the beginning of senior year, I would narrow this to:

1. Finish the source and documentation audit.
2. Declare Chiron the workspace and Pytheas the capability lab.
3. Create the host-side database and backup process.
4. Build the mobile daily cockpit.
5. Connect one calendar account read-only.
6. Connect one school account read-only.
7. Implement one complete school subject.
8. Build the Obsidian task/event bridge.
9. Use it for two weeks before expanding.

The first success criterion should be concrete:

> For fourteen consecutive days, Chiron shows the correct schedule, deadlines and three current priorities on both your computer and phone without requiring manual duplication.

That is more valuable than immediately recreating every Notion, Classroom and Google Docs screen.

I haven’t saved this roadmap into the vault yet. This is the draft for your review; after the remaining code audit, I can turn it into a precise roadmap tied to current modules, tests and milestones.

## Donovan

add this roadmap, as well as this entire conversation into Obsidian ~/pytheas for now. I'm saving conversations manually now, unless you can remember to save them on the key word, finito. When we reorganize the Obsidian vaults, repo strucutre and the code folder structure, we will begin work.

## Codex

I’ll add three new notes under `pytheas`: the Chiron roadmap, a conversation archive, and the required prompt log. I’ll also make the one approved edit to the vault’s root instructions so **`finito`** means: save the current user/assistant conversation into `pytheas/Conversations/`, then commit and push the Pytheas vault.

One limitation: I cannot pull a platform-native verbatim export of messages that were compacted out of my active context. The archive will preserve the currently available transcript verbatim and label the earlier portion as a recovered summary, rather than pretending it is exact. Draft keyword text:

> **`finito`** — archive the current substantive user/assistant conversation in `pytheas/Conversations/` (exclude hidden instructions, internal reasoning, and tool logs), prompt-log it if not already logged, then commit and push the Pytheas vault. If earlier turns are unavailable after context compaction, label their reconstruction as a summary rather than verbatim.
