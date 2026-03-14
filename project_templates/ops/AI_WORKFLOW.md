# AI Workflow (Canonical Policy)

Version: 1.0
Last Updated: 2026-03-13

## Purpose

This is the canonical AI workflow for the free starter template.
It defines the safe, maintainable baseline for AI-assisted delivery.

## Startup Chain

1. Enter through the active tool surface.
2. Read `AGENTS.md`.
3. Read `docs/FILE_MAP.md`.
4. Read this file.
5. Read only task-triggered docs after that.

## Working Rules

- Plan before code.
- Execute small, reviewable diffs.
- Never read or modify `.env`; update `.env.example` only.
- Never expose secrets, keys, tokens, or private URLs.
- Never run destructive commands without explicit approval.
- Treat governance files as protected.
- Use repo-local runtime commands and environments when applicable.

## Required Read Triggers

- Architecture, feature, release, or UX work -> `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md`
- Privacy, legal, or policy work -> `docs/PRIVACY.md`, `docs/TERMS.md`
- Local app/test work -> repo-local environments plus `python -m ...` commands where applicable

## Operating Loop

1. Plan.
2. Execute small changes.
3. Run applicable quality gates.
4. Update affected documentation.
5. Summarize verification evidence and residual risks.
6. If tracked project files changed, log the outcome in `CHANGELOG_AI.md`; otherwise use lightweight closeout unless a durable policy or product decision changed.

## Closeout

- Use `ops/QUALITY_GATES.md` as the authoritative checklist.
- Update `ops/LESSONS_LEARNED.md` for recurring issues.
- No-change research, audit, inspection, or advisory tasks do not need local history-log edits unless they changed a durable repo policy or decision.
- Update privacy, terms, threat model, runbook, and journey docs when affected.
