---
title: GitHub Vault Separation and Mega-Vault Migration
date: 2026-08-31
tags: [prompt-log, mega-prompt, git, github, vault-organization, migration]
model: GPT-5.6 Codex
tool: Codex, Git, GitHub CLI
status: completed
related: ["[[../Vault Atlas/Home]]", "[[../../Roadmaps/Development Roadmap]]"]
---

# Prompt

Separate the mixed `personal-vault` branches so Personal remains on `master` and Learning lives in `learning-vault/main`; keep personal, finance, learning, Pytheas, and their subfolders accessible as one optimally organized mega-vault; preserve history; avoid `sudo`; and report any manual steps.

# Result

Verified that `personal-vault/master` and the Learning history were divergent, fast-forwarded the existing private `learning-vault/main` to the exact current local Learning commit, repointed local Learning to that remote, verified all SHAs, and deleted only the duplicated `personal-vault/main`. Added a parent mega-vault home/configuration while retaining independent child Git repositories, and refreshed the cross-vault atlas.
