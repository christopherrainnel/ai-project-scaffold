# Governance Runtime Spec

> Starter runtime contract for generated governed projects.

## Purpose

This project uses the governed runtime workflow:
- `python -m gov scaffold`
- `python -m gov check`
- `python -m gov session`
- `python -m gov plan`
- `python -m gov verify`
- `python -m gov resume`

## Startup Chain

1. Read the active tool entry surface first when one exists.
2. Read `AGENTS.md`.
3. Read `docs/FILE_MAP.md`.
4. Read `ops/AI_WORKFLOW.md`.
5. Read only task-relevant docs after that.

## Fresh-State Rule

Project-facing docs must stay placeholder-led until the operator defines the project's actual scope, data model, legal posture, and release expectations.

## Closeout Rule

After completed governed work:
- run the relevant quality gates
- update `CHANGELOG_AI.md`
- update affected project docs deliberately
