# AI Workflow (Canonical Policy)

Version: 2.4
Last Updated: 2026-03-07
Owner: Project Lead

---

## Purpose

This file is the single source of truth for how AI agents and IDE assistants operate in this scaffold.

Applies to Claude Code, VS Code Copilot/Codex, and similar tools.

This workflow is security-first, privacy-first, production-minded, and not legal advice.

Version/date headers in governance files are informational. Do not treat them as freshness signals or skip a file because its header looks old.

## 0) Policy Map

- `ops/AI_WORKFLOW.md` is canonical.
- `AGENTS.md` is the universal scaffold router.
- `CLAUDE.md` and `.github/copilot-instructions.md` are tool-specific loaders and should stay thin.
- `.claude/settings.json` is the free-tier native enforcement layer.
- During active editing sessions, use the current working-tree versions of governance files; do not defer to older committed or remote copies.
- If any loader conflicts with this file, this file wins and the agent must stop and ask.

## 1) Scaffold Direction

- This scaffold is meant to help a user start a fresh AI-assisted project.
- Keep it generic, current, and free of creator-specific residue or carry-over history.
- Native loader support should reduce drift where supported, but markdown guidance remains the fallback.
- Optional tiering overlays under `guides/` may refine paid/free or entitlement boundary decisions when present.
- Optimize for token efficiency: centralize repeated instructions and keep tool-specific loaders lightweight.

## 2) Session Start (Hard Gate)

Before first code changes in a new feature or session:

1. Read `docs/FILE_MAP.md`.
2. Read this file.
3. If the task touches paid/free or entitlement boundaries and a local overlay exists, read `guides/TIERING_POLICY.local.md` or `guides/TIERING_POLICY.md`.
4. Read only the docs and source files required by the task.
5. If the session did not start with a governance-loading prompt, use `ops/prompts/SESSION_RESUME.md` Section 1 before feature work.
6. If governance files are missing, ask to create only missing files; do not overwrite existing governance files without approval.

### Context Discipline

- Do not preload the full codebase.
- Start with at most 3 source files unless the task clearly needs more.
- Expand in small batches and explain why.
- Read `CHANGELOG_AI.md` only when resuming or verifying recent work, and only the newest relevant entry.

### Required Read Triggers

- Feature, phase, public UX, entitlement, release QA, or architecture-impacting work: read `docs/ARCHITECTURE.md`, `docs/DECISIONS.md`, and `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md`.
- Paid access, legal, privacy, or policy wording work: read `docs/PRIVACY.md` and `docs/TERMS.md`.
- Local app/test work: prefer repo-local `.venv_run` and `python -m ...` commands. If a stale `.venv_run` path appears, use the reset SOP in `README.md` and `ops/RUNBOOK.md` rather than patching global Python.

### Dual-Lens Planning Gate

Before feature work, major enhancements, or phase/stage closeout, capture both perspectives in the plan:

1. `Technical Builder POV`
   - Implementation boundaries, constraints, non-goals.
   - Quality and security evidence expected before completion.
2. `User/Consumer POV`
   - Active journey variant.
   - Stage in focus and required outcome across `Discover`, `Acquire Access`, `Verify`, `Deliver`, `Study + Use`, and `Support + Recovery`.

Default to focused entry-point mode:

- Use full `Technical Builder POV` plus a lightweight `User/Consumer POV` anchor at the start.
- Expand to full journey mapping when public UX changes, entitlement or verification changes, phase closeout, or release QA begins.
- For narrow bugfix or doc-only work, a 1-2 line note per POV is enough.

Every feature or phase plan must include at least one concrete risk with mitigation.

## 3) Mandatory Operating Loop

Every task follows this loop:

1. Plan.
2. Execute small, reviewable diffs.
3. Verify with applicable quality gates.
4. Update impacted documentation.
5. Summarize verification evidence and residual risks.
6. Log the outcome in `CHANGELOG_AI.md`.

### Broad QA Rule

When running broad QA or pre-release checks, use two modes:

- `Discovery Only`: collect issues without changing code.
- `Fix After Approval`: fix only after the user approves the issue list.

Keep QA reports compact and actionable.

### Release And Journey Gates

- Before public-facing release, run a polish pass covering UX clarity, accessibility basics, legal/runtime doc alignment, and support language.
- Before phase or release sign-off, evaluate the active user or consumer journey using `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md`.
- Required stages are `Discover`, `Acquire Access`, `Verify`, `Deliver`, `Study + Use`, and `Support + Recovery`.
- If any in-scope stage is not complete, record the gap, owner, and target sequence in `CHANGELOG_AI.md`.

### Session Boundary And Multi-Agent Use

Start a new session when scope or context becomes noisy, especially when:

- more than 5 implementation phases are planned,
- more than 4 files are actively changing,
- scope expands beyond one vertical slice,
- the agent is re-reading the same context or re-deciding settled choices.

Before ending a session, leave a compact handoff with objective, completed items, next action, blockers, and touched files.

Multi-agent mode is optional. Recommend it only for multi-domain work, 4 or more files, risky releases, or repeated missed review findings. The user must explicitly approve activation.

## 4) Non-Negotiable Rules

1. Plan before feature code: no feature implementation without a short plan and risk register.
2. Never read or modify `.env`; update `.env.example` only.
3. Never commit or expose secrets, private URLs, keys, or tokens.
4. Never run destructive commands without explicit user approval.
5. Never add dependencies without rationale, version pinning, and lockfile updates.
6. Treat governance files as protected; do not overwrite them without a diff and approval.
7. CI must block shipping when applicable lint, format, typecheck, tests, dependency scan, secret scan, basic SAST, or build checks fail.
8. Use least privilege, deny-by-default access, rate limits, and abuse controls for public surfaces.
9. Never handle raw card data; use hosted checkout or tokenization only.
10. For legal, security, or policy guidance, use current official sources and concrete dates when relevant.
11. Never claim certification or compliance without proof; use wording such as "aligned with" or "informed by".

## 5) Supporting Docs And Control Surfaces

- **Security and privacy**: follow `ops/SECURITY_POLICY.md`. Validate input at every boundary, apply secure headers, never log secrets or PII, reflect retention in `docs/PRIVACY.md`.
- **AI safety**: isolate system prompts from user content, treat user input as hostile, require confirmation for destructive actions, prefer tool allowlists, redact sensitive data before sending to providers.
- **Dependencies**: follow `ops/DEPENDENCY_POLICY.md`. Pin versions, keep lockfiles aligned, run dependency and secret scanning in CI.
- **Acceptance gates**: `ops/QUALITY_GATES.md` is the authoritative checklist file. `ops/DEFINITION_OF_DONE.md` is a pointer and should not duplicate the checklists.
- **Release readiness**: use `ops/RELEASE_CHECKLIST.md` for release execution details.
- **Anti-drift**: read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md` before design-affecting work. If the task conflicts with recorded decisions, stop and ask. Record new decisions in `docs/DECISIONS.md`.
- **High-risk fail-safe**: if the task touches children, health data, regulated requirements, or direct payment handling, pause, reduce scope, and require documented review before resuming.

## 6) Closeout Requirements

- Use the checklists in `ops/QUALITY_GATES.md`.
- After every task, update `CHANGELOG_AI.md`.
- Update `ops/LESSONS_LEARNED.md` if the issue is likely to recur.
- Update `docs/PRIVACY.md`, `docs/TERMS.md`, `docs/THREAT_MODEL.md`, `ops/RUNBOOK.md`, and `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md` when the change affects those areas.

## 7) Governance Scaffold Completeness

Required coverage (verify these exist; do not recreate without checking first):

- Entry points: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `CHANGELOG_AI.md`, `.env.example`.
- Core docs under `docs/`: `FILE_MAP`, `ARCHITECTURE`, `DECISIONS`, `PRIVACY`, `TERMS`, `THREAT_MODEL`, `USER_CONSUMER_JOURNEY_CHECKLIST`.
- Ops docs under `ops/`: `AI_WORKFLOW`, `SECURITY_POLICY`, `DATA_CLASSIFICATION`, `DEPENDENCY_POLICY`, `QUALITY_GATES`, `DEFINITION_OF_DONE`, `RUNBOOK`, `STANDARDS_BASELINE`, `RELEASE_CHECKLIST`, `LESSONS_LEARNED`, and prompt files under `ops/prompts/`.
- Native enforcement in free tier: `.claude/settings.json`.
- CI and contribution: `.github/workflows/ci.yml`, issue templates, PR template, `CODEOWNERS`, branch-protection guidance.
