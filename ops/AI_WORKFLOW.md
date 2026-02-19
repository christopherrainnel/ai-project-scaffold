# AI Workflow (Canonical Policy)
Version: 1.0
Last Updated: 2026-02-19
Owner: Project Lead

## Purpose
This file is the canonical governance policy for this repository and must be followed by any AI agent or IDE assistant (VS Code, Cursor, Windsurf, others).

## Session Start: Audit Rule
On opening this workspace (or first task):
1) Verify required governance scaffold exists (see "Scaffold Checklist").
2) If missing items exist, ask:
   "This workspace is missing governance scaffold items. Do you want me to install the missing pieces (recommended) or skip (for small/simple projects)?"
3) If approved: create missing items only. Do not overwrite existing files unless user approves a diff.
4) If a required file exists, do not overwrite it. Only propose updates via diff and request approval.
5) At least once per major milestone, run the Workspace Governance Audit prompt.

## Operating Mode (Required)
1) Plan first (short, step-by-step). Name the files to be changed.
2) Make small, reviewable edits. Avoid unrelated reformatting.
3) Run quality gates (lint/test/build) if available.
4) Summarize: what changed, why, how verified, risks, and next check.
5) Log the work in `CHANGELOG_AI.md`.

## Safety Rules (Non-Negotiable)
- Secrets: never request, paste, store, or echo secrets (keys, tokens, passwords).
- `.env`: never read or modify `.env`. Only update `.env.example`.
- Terminal: never run destructive commands; require explicit approval for any command execution.
- Data: never request customer PII or sensitive internal data; request redacted/sanitized samples.

## Dependency Discipline
- Do not add dependencies unless justified (why needed, alternatives considered).
- Pin versions and update lockfiles immediately.
- Run vulnerability checks if available (e.g., npm audit/pip-audit) when dependencies change.

## Anti-Drift Control
Before implementing changes:
- Read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
- If proposed work conflicts with recorded decisions, stop and ask.

## Scaffold Checklist
Required paths:
- ops/* (all governance files)
- ops/prompts/*
- docs/ARCHITECTURE.md
- docs/DECISIONS.md
- CHANGELOG_AI.md
- .env.example