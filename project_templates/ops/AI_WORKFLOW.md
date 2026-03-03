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
2. Ask the minimum discovery questions needed to avoid building the wrong thing (see `ops/STANDARDS_BASELINE.md`).
3. Produce a short implementation plan plus a risk register.
4. If governance files are missing, ask to create missing files only; do not overwrite without approval.

### Context-Efficient Read Order (All Agents)

At the start of each task/session:

1. Read `docs/FILE_MAP.md` first for project orientation.
2. Read governance/policy files only as needed for the task.
3. Fetch only task-relevant source files; do not preload the full codebase.

Token budget rule:

- Never load more than 3 source files per task unless explicitly required by the user or task complexity.
- If more files are needed, expand in small batches and justify why.

---

## 2) Mandatory Operating Loop

Every task follows this loop:

1. **Plan** — scope, files, tests, risks.
2. **Execute** — small diffs only, no unrelated reformatting.
3. **Verify** — run applicable quality gates.
4. **Document** — update docs impacted by the change.
5. **Summarize** — include verification evidence and residual risks.
6. **Log** — update `CHANGELOG_AI.md`.

---

## 3) Non-Negotiable Rules

1. **Plan before code**: no feature implementation without a short plan + risk register.
2. **Security gates before shipping**: CI must fail on lint/format/typecheck, tests, vulnerability scan, secret scan, and basic SAST.
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

```
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
