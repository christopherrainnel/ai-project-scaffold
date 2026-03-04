# AI Workflow (Canonical Policy)

Version: 2.0
Last Updated: {{DATE}}
Owner: Project Lead

---

## Purpose

This file is the **single source of truth** for how AI agents and IDE assistants operate in this repository.

Applies to: Claude Code, Cursor, VS Code Copilot, Windsurf, and any other AI-assisted tool.

This workflow is **security-first, privacy-first, and production-minded**. It is not legal advice.

---

## 1) Session Start (Hard Gate)

Before first code changes in a new feature/session:

1. Confirm governance scaffold completeness (Section 10).
2. Read local tiering overlay if present: `guides/TIERING_POLICY.local.md` (fallback: `guides/TIERING_POLICY.md`).
3. Ask the minimum discovery questions needed to avoid building the wrong thing (see `ops/STANDARDS_BASELINE.md`).
4. Choose execution mode: direct Build -> Review for simple work, or add a short plan + risk register for complex/high-risk work.
5. If governance files are missing, ask to create missing files only; do not overwrite without approval.

If no local tiering file exists, continue normally without failing.

### Context-Efficient Read Order (All Agents)

At the start of each task/session:

1. Read `docs/FILE_MAP.md` first for project orientation.
2. Read governance/policy files only as needed for the task.
3. Fetch only task-relevant source files; do not preload the full codebase.

Token budget rule:

- Never load more than 3 source files per task unless explicitly required by the user or task complexity.
- If more files are needed, expand in small batches and justify why.

---

## 2) Standard Operating Loop

Every task follows one of these modes:

1. **Default (simple work): Build -> Review -> Log**
2. **Complex/high-risk work: Plan -> Build -> Review -> Log**

When switching to the complex mode, briefly note the trade-off for the current task (1–2 sentences, e.g., "Adding a plan step — expect a slightly longer cycle for this change" or "Review pass adds value here because the edit spans multiple modules"). Keep the tone neutral; the goal is awareness, not discouragement.

In both modes:

- Keep diffs small and focused.
- Run applicable quality gates.
- Update impacted docs.
- Include verification evidence and residual risks.
- Update `CHANGELOG_AI.md`.

### Two-Mode QA Boundary (Code Review Tasks)

When the user asks for a review, default to **Mode A: Discovery**.

- Mode A (Discovery): analyze and report findings only. Do not edit files.
- Mode B (Fix): apply fixes only after explicit user approval.

For review responses, list findings first (ordered by severity) with file and line references, then open questions/assumptions, then optional change summary.

---

## 3) Non-Negotiable Rules

1. **No mandatory planner**: use a short plan + risk register only for complex/high-risk tasks.
2. **Security gates before shipping**: CI must fail on configured and applicable checks in `.github/workflows/ci.yml` (lint/format/typecheck/tests, vulnerability scan, secret scan, and basic SAST).
3. **No secrets in code**: never commit secrets, tokens, API keys, private URLs.
4. **Least privilege by default**: explicit roles/permissions and deny-by-default.
5. **Minimize and protect data**: collect minimum data; use encryption in transit and managed encryption at rest.
6. **Payments**: never handle raw card data; use hosted checkout/tokenization only.
7. **AI safety controls**: treat user input as hostile; guard against prompt injection; use tool allowlists and confirmation for sensitive actions.
8. **Legal baseline required**: align with official sources and record effective dates; never claim certification/compliance.

---

## 4) Security & Privacy Baseline

- Never read/modify `.env`; update `.env.example` only.
- Use input validation at every boundary.
- Apply secure headers where applicable (CSP, HSTS, frame protections, MIME protections).
- Implement rate limiting and abuse controls for public endpoints.
- Do not log PII/secrets.
- Define retention and deletion process in `docs/PRIVACY.md`.

---

## 5) AI Feature Baseline (When AI Is Used)

- Keep system/tool instructions isolated from user content.
- Require explicit confirmation for destructive or external actions.
- Restrict tool execution by allowlist.
- Redact sensitive data before sending to model providers.
- Store metadata or hashes where possible instead of full prompt/response logs.

---

## 6) Dependency & Supply Chain Discipline

- Add dependencies only with rationale.
- Pin versions and maintain lockfiles.
- Enable dependency vulnerability scanning.
- Enable secret scanning in pre-commit and CI.
- Generate SBOM when feasible.

---

## 7) Anti-Drift Control

Before implementation:

1. Read `docs/ARCHITECTURE.md` and `docs/DECISIONS.md`.
2. If change conflicts with documented decisions, stop and ask.
3. Log new architecture decisions in `docs/DECISIONS.md`.

---

## 8) High-Risk Fail-Safe

If the feature involves children, health data, regulated industry requirements, or direct payment handling:

1. Pause implementation.
2. Propose a safer reduced MVP scope.
3. Require legal/compliance review and DPIA/PIA-style assessment.
4. Resume only after minimization controls are documented.

---

## 9) Definition of Done

Use `ops/DEFINITION_OF_DONE.md` and `ops/QUALITY_GATES.md`.

A task is complete only when applicable checks pass and required docs are updated.

---

## 10) Scaffold Checklist

Required governance files:

```text
CLAUDE.md
AGENTS.md
CHANGELOG_AI.md
.env.example
.gitignore
.github/copilot-instructions.md
.github/workflows/ci.yml
.github/ISSUE_TEMPLATE/01-bug-report.yml
.github/ISSUE_TEMPLATE/02-feature-request.yml
.github/ISSUE_TEMPLATE/config.yml
.github/PULL_REQUEST_TEMPLATE.md
.github/CODEOWNERS
.github/BRANCH_PROTECTION.md
docs/ARCHITECTURE.md
docs/DECISIONS.md
docs/FILE_MAP.md
docs/PRIVACY.md
docs/THREAT_MODEL.md
ops/AI_WORKFLOW.md
ops/SECURITY_POLICY.md
ops/DATA_CLASSIFICATION.md
ops/DEPENDENCY_POLICY.md
ops/QUALITY_GATES.md
ops/DEFINITION_OF_DONE.md
ops/RUNBOOK.md
ops/STANDARDS_BASELINE.md
ops/RELEASE_CHECKLIST.md
ops/LESSONS_LEARNED.md
ops/prompts/feature_request.md
ops/prompts/SESSION_RESUME.md
ops/prompts/bug_report.md
ops/prompts/refactor_request.md
ops/prompts/code_review.md
```
