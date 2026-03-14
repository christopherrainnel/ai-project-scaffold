# File Map

## Root Files

| File | Purpose |
|---|---|
| `README.md` | Project overview and starter rules |
| `AGENTS.md` | Universal AI-agent entrypoint |
| `CLAUDE.md` / `GEMINI.md` | Tool-specific loaders |
| `CHANGELOG_AI.md` | AI change history |
| `.env.example` | Environment template |
| `.gitignore` | Git exclusions |

## IDE And Governance

| Path | Purpose |
|---|---|
| `.claude/`, `.cursor/`, `.windsurf/`, `.clinerules/` | Native IDE governance surfaces |
| `.vscode/` | Recommended VS Code baseline |
| `.githooks/pre-commit.advisory` | Optional local advisory hook |
| `.github/` | CI and contribution templates |

## Docs

| Path | Purpose |
|---|---|
| `docs/ARCHITECTURE.md` | System design |
| `docs/DECISIONS.md` | Decision log |
| `docs/FILE_MAP.md` | Plain-English index |
| `docs/GOVERNANCE_RUNTIME_SPEC.md` | Starter runtime contract for governed workflow |
| `docs/IDE_ENFORCEMENT.md` | IDE enforcement layout |
| `docs/MIGRATION_PLAN.md` | Placeholder migration path |
| `docs/POLICY_PACKS.json` | Starter structured policy-pack set |
| `docs/PRIVACY.md` | Privacy and data handling |
| `docs/PRODUCT_STRATEGY_ROADMAP.md` | Placeholder project roadmap |
| `docs/RULE_MODEL.md` | Starter rule-layer explanation |
| `docs/TEMPLATE_TIERING_POLICY.md` | Local starter-tier policy placeholder |
| `docs/TERMS.md` | Operating terms |
| `docs/THREAT_MODEL.md` | Threats and mitigations |
| `docs/TOOL_ALLOWLIST_PROFILES.json` | Starter tool-allowlist profile set |
| `docs/[redacted-tiering-item]` | Escalation triggers |
| `docs/USER_CONSUMER_JOURNEY_CHECKLIST.md` | Journey-stage release checklist |

## Operations

| Path | Purpose |
|---|---|
| `ops/AI_WORKFLOW.md` | Canonical workflow |
| `ops/SESSION_RESUME.md` | Canonical restart and resume handoff |
| `ops/QUALITY_GATES.md` | Required verification steps |
| `ops/SECURITY_POLICY.md` | Security rules |
| `ops/DATA_CLASSIFICATION.md` | Data-sensitivity guidance |
| `ops/DEPENDENCY_POLICY.md` | Dependency rules |
| `ops/RUNBOOK.md` | Operations and recovery notes |
| `ops/LESSONS_LEARNED.md` | Recurring issues and fixes |
| `ops/prompts/` | Bug, feature, refactor, and review prompt templates |

## Scripts

| Path | Purpose |
|---|---|
| `scripts/local_preflight_advisory.py` | Optional warning-first local preflight |
