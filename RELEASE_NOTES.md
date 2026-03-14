# Release Notes: v2.20

**Release Date**: March 14, 2026
**Status**: Ready for Production

## Overview

v2.20 completely syncs `project_templates/` from the canonical `VibeCoder_Pack` source, expanding the structural framework to support new governance runtimes.

## What's New

### 1. Template Synchronization from VibeCoder_Pack
- Replaced `project_templates/` with the current snapshot from `VibeCoder_Pack/project_templates/free/`.
- Introduced new structural policy, agent rules, and runtime configuration files into the free baseline:
  - `docs/GOVERNANCE_RUNTIME_SPEC.md`
  - `docs/MIGRATION_PLAN.md`
  - `docs/POLICY_PACKS.json`
  - `docs/PRODUCT_STRATEGY_ROADMAP.md`
  - `docs/PROJECT_RULES.json`
  - `docs/RULE_MODEL.md`
  - `docs/TOOL_ALLOWLIST_PROFILES.json`
- Ensures the scaffolding incorporates the latest structural primitives to support agent policies and tool availability profiles seamlessly out-of-the-box.

---

# Release Notes: v2.19

**Release Date**: March 12, 2026
**Status**: Ready for Production

## Overview

## What's New

### 1. [redacted-tiering-item] Now Included in baseline

- `docs/[redacted-tiering-item]` added to `project_templates/docs/` in the baseline scaffold.
- Upgrade trigger table covers: auth thresholds, rate limits, PII handling, GDPR/CCPA/age-gating, payment security hardening, multi-agent mode thresholds, journey completion gates.
- `docs/FILE_MAP.md` updated to include the new file.

---

# Release Notes: v2.17

**Release Date**: March 9, 2026
**Status**: Ready for Production

## Overview

## What's New

### 1. Workstation Context Check (Shared-Safe)

- Added formal Workstation Context Check SOP in `project_templates/ops/AI_WORKFLOW.md` (Section 2 subsection): verifies repo root path, OS/shell/runtime context, `.venv_run` health, git hooksPath, and absolute-path assumptions before treating a session as a safe resume.
- Added matching **Workstation Re-Adoption** SOP in `project_templates/ops/RUNBOOK.md` (v0.2): 6-step procedure for resuming on a different workstation.
- Added Workstation Context Check reference to `project_templates/CLAUDE.md` (step 5) and `project_templates/AGENTS.md` (step 4).
- Updated `project_templates/ops/QUALITY_GATES.md` (v2.3): added Workstation Re-Adoption completion checkbox in the Shipping Gate.

### 2. Practical Testing Responsibility Framework (Shared-Safe)

- Added **Practical Testing Responsibility Rule** to `project_templates/ops/AI_WORKFLOW.md` (Section 3): defines `AI-runnable verification`, `Developer POV practical testing`, and `Consumer POV practical testing` markers with clear ownership rules.
- Added three practical testing checkboxes to `project_templates/ops/QUALITY_GATES.md` Feature Acceptance Gate.
- Added `Awaiting human validation` pause rule to `project_templates/CLAUDE.md` and `project_templates/ops/prompts/SESSION_RESUME.md`.

### 3. SESSION_RESUME.md v2.1

- Replaced `project_templates/ops/prompts/SESSION_RESUME.md` with v2.1 format:
  - Section 1 prompt now includes full Workstation Context Check instructions.
  - Section 2 minimum resume rules include `Awaiting human validation` pause rule.
  - Added Section 3 compact resume handoff format.

### 4. Changelog Convention

- Added **Changelog Convention** subsection to `project_templates/ops/AI_WORKFLOW.md` (Section 3): defines `## YYYY-MM-DD` date blocks with `### HH:MM - [task]` sub-entries, newest-first ordering, and optional `Commands` field policy.
- Updated `project_templates/CHANGELOG_AI.md` to match the date-block + time format; `Commands` is now optional.

### 5. Governance Header Maintenance

- Added **Governance Header Maintenance** section to `project_templates/ops/AI_WORKFLOW.md` (after Policy Map): clarifies when to bump `Version` vs. update `Last Updated` only.

### 6. DECISIONS.md Extended Fields

- Updated `project_templates/docs/DECISIONS.md` entry format to include: `Status`, `Current assumption`, `Trigger to revisit`, `Risk if wrong` fields (matching the AI-guided scaffold format).

### 7. CLAUDE.md and AGENTS.md Streamlining

- Slimmed `project_templates/CLAUDE.md` to a thin loader: removed redundant Non-Negotiables and Local Python Pattern sections (covered by `ops/AI_WORKFLOW.md`); added Workstation Context Check step and `Awaiting human validation` rule.
- Updated `project_templates/AGENTS.md`: added Workstation Context Check step, added practical-testing scaffold rule, removed redundant template fallback note.

### 8. FILE_MAP.md Description Improvements

- Updated four file descriptions in `project_templates/docs/FILE_MAP.md`:
  - `AI_WORKFLOW.md`: mentions workstation context checks and human practical testing gates.
  - `QUALITY_GATES.md`: mentions workstation re-adoption and human validation completion checks.
  - `RUNBOOK.md`: mentions workstation re-adoption SOP.
  - `SESSION_RESUME.md`: updated to reflect v2.1 workstation check requirement.

---

# Release Notes: v2.16

**Release Date**: March 7, 2026
**Status**: Ready for Production

## Overview

v2.16 locks the baseline user journey checklist at its current baseline and routes future checklist-component enhancements to the AI-guided scaffold+.

## What's New

---

# Release Notes: v2.15

**Release Date**: March 7, 2026
**Status**: Ready for Production

## Overview

v2.15 tightens baseline boundaries by keeping a focused loader baseline (Claude + VS Code Copilot/Codex) and moving additional tool-native rule packs back to the AI-guided scaffold.

## What's New

---

# Release Notes: v2.14

**Release Date**: March 7, 2026
**Status**: Ready for Production

## Overview

## What's New

### 1. Shared IDE-Native Enforcement Layer (Free)

- Added repo-native governance integrations in `project_templates/`:
  - `.claude/settings.json`
  - `.cursor/rules/00-governance.mdc`
  - `.windsurf/rules/00-governance.md`
  - `.clinerules/01-governance.md`
  - `.clinerules/hooks/TaskStart`
  - `.clinerules/hooks/PreToolUse`
- Added governance documentation stubs:
  - `project_templates/docs/IDE_ENFORCEMENT.md`
  - `project_templates/docs/TERMS.md`
  - `project_templates/docs/USER_CONSUMER_JOURNEY_CHECKLIST.md`

### 2. baseline template Governance Refactor (Shared-Safe)

- Refreshed shared policy loaders and canonical docs:
  - `project_templates/AGENTS.md`
  - `project_templates/CLAUDE.md`
  - `project_templates/.github/copilot-instructions.md`
  - `project_templates/ops/AI_WORKFLOW.md`
  - `project_templates/docs/FILE_MAP.md`
  - `project_templates/ops/QUALITY_GATES.md`
  - `project_templates/ops/DEFINITION_OF_DONE.md`
  - `project_templates/README.md`
- `ops/QUALITY_GATES.md` now carries the authoritative shipping and feature-acceptance checklists.
- `ops/DEFINITION_OF_DONE.md` is now a pointer file to avoid checklist duplication drift.

---

# Release Notes: v2.13

**Release Date**: March 6, 2026
**Status**: Ready for Production

## Overview

## What's New

### 1. cross-template Shared Governance Wording Alignment

- Updated free `project_templates/` governance loaders and docs to use flexible governance-first wording and point to `ops/prompts/SESSION_RESUME.md` as the canonical prompt location.
- Applied to:
  - `project_templates/.github/copilot-instructions.md`
  - `project_templates/AGENTS.md`
  - `project_templates/CLAUDE.md`
  - `project_templates/README.md`
  - `project_templates/ops/AI_WORKFLOW.md`
  - `project_templates/ops/prompts/SESSION_RESUME.md`

### 2. Template Hygiene Reset (Free)

- Reset `project_templates/CHANGELOG_AI.md` and `project_templates/ops/LESSONS_LEARNED.md` to starter-template form.

---

# Release Notes: v2.12

**Release Date**: March 6, 2026
**Status**: Ready for Production

## Overview

v2.12 adds a required GOVERNANCE BOOT session-start prompt so agents load policy context before implementation work.

## What's New

### 1. Required Session-Start Prompt

- Added a standard copy/paste GOVERNANCE BOOT prompt to:
  - `project_templates/ops/prompts/SESSION_RESUME.md` (Section 1)
  - `project_templates/README.md`
  - `project_templates/AGENTS.md`
  - `project_templates/CLAUDE.md`
  - `project_templates/.github/copilot-instructions.md`
  - `project_templates/ops/AI_WORKFLOW.md`

### 2. Context and Ops Documentation Alignment

- Updated `project_templates/docs/FILE_MAP.md` so `SESSION_RESUME.md` is explicitly described as governance boot + handoff template.
- Added a recurring-issue entry in `project_templates/ops/LESSONS_LEARNED.md` for governance-boot skipping.

---

# Release Notes: v2.11

**Release Date**: March 5, 2026
**Status**: Ready for Production

## Overview

v2.11 aligns baseline template journey terminology and phase-close evaluation language with the latest VibeCoder_Pack governance model while preserving baseline boundaries.

## What's New

### 1. Journey Language Alignment (baseline templates)

- Updated `project_templates/ops/AI_WORKFLOW.md` to use the current lifecycle naming:
  - `Acquire Access` (replacing `Buy (if applicable)`)
  - `Study + Use` naming consistency
- Added lightweight Dual-Lens Planning Gate language to keep phase work tied to both builder and user/consumer outcomes.

### 2. Completion + Release Evidence Consistency

- Updated `project_templates/ops/DEFINITION_OF_DONE.md` to require phase journey completeness/defer tracking.
- Updated `project_templates/ops/RELEASE_CHECKLIST.md` to require explicit journey-variant mapping (`paid consumer`, `self-use`, `team/internal`) before release closure.

---

# Release Notes: v2.10

**Release Date**: March 5, 2026
**Status**: Ready for Production

## Overview

v2.10 introduces a phase/stage User Journey Completion Gate so projects cannot mark major phases complete without evaluating real user-lifecycle coverage.

## What's New

### 1. User Journey Completion Gate (Phase/Stage Close)

- Added a mandatory journey-gate evaluation to `project_templates/ops/AI_WORKFLOW.md` at the close of each major phase/stage.
- Added a matching Definition of Done requirement in `project_templates/ops/DEFINITION_OF_DONE.md`.
- Added release-time journey checks in `project_templates/ops/RELEASE_CHECKLIST.md`.
- Journey sequence now explicitly tracked as: `Discover -> Buy (if applicable) -> Verify -> Deliver -> Study/Use -> Support/Recovery`.

---

# Release Notes: v2.9

**Release Date**: March 5, 2026
**Status**: Ready for Production

## Overview

v2.9 adds a Product Readiness Polish Gate to reduce stale UI/legal drift before release.

## What's New

### 1. Product Readiness Polish Gate

- Added a required pre-release polish gate in `ops/AI_WORKFLOW.md` and `ops/RELEASE_CHECKLIST.md`.
- baseline baseline now requires:
  - UI quality pass,
  - legal-page alignment review,
  - explicit human approval for AI-assisted legal drafting,
  - release professionalism pass.
- Legal drafting guidance defaults to pattern-based synthesis, with constrained verbatim reuse only when clearly permissible.

---

# Release Notes: v2.8

**Release Date**: March 5, 2026
**Status**: Ready for Production

## Overview

v2.8 aligns current template behavior with clearer review and session-resume controls.

## What's New

### 1. Two-Mode QA Boundary (Free + the AI-guided scaffold)

- Added explicit review modes in templates:
  - `Mode A: Discovery` (findings only, no edits)
  - `Mode B: Fix` (edits only after explicit approval)
- Added guidance in `ops/AI_WORKFLOW.md` and `ops/prompts/code_review.md`.

### 2. Strict Session Resume Sequence

- `ops/prompts/SESSION_RESUME.md` now requires:
  1. confirm latest relevant `CHANGELOG_AI.md` entry,
  2. restate the next concrete action,
  3. read only the minimal required files.
- Added compact handoff block for low-token context recovery.

---

# Release Notes: v2.7

**Release Date**: March 5, 2026
**Status**: Ready for Production

## Overview

v2.7 clarifies repo boundary rules between free and the AI-guided scaffold so cross-repo sync can remain deterministic.

## What's New

---

# Release Notes: v2.6

**Release Date**: March 4, 2026
**Status**: Ready for Production

## Overview

v2.6 adds **multi-agent policy alignment** across all governance files. baseline now explicitly documents single-agent default with optional Build -> Review flow. Limitation-awareness prompts ensure agents briefly note trade-offs when switching execution modes.

## What's New

### 1. Multi-Agent Policy (baseline)

- Single-agent mode is now the documented default across all policy loaders.
- Optional Build -> Review flow supported for complex/high-risk tasks.
- No mandatory planner — planning is used only when complexity justifies it.

**Where it's enforced**:

- `ops/AI_WORKFLOW.md` — canonical source (Section 2)
- `AGENTS.md` — universal agent entry point (Hard Constraints)
- `CLAUDE.md` — Claude Code auto-read rules (Operating Mode)
- `.github/copilot-instructions.md` — VS Code Copilot policy loader (Operating Rules)
- `project_templates/README.md` — template README (For AI Agents)

### 2. Limitation-Awareness on Mode Switch

When switching from default to complex mode (Plan -> Build -> Review), the agent now briefly summarizes trade-offs relevant to the current project context (1–2 sentences). The tone is neutral — awareness, not discouragement.

### 3. Workflow Guide: Multi-Agent + Escalation

- Added "Multi-Agent Support (baseline)" section to `guides/AI_Project_Workflow_Guide.md`.
- Added "When to Escalate to the AI-guided scaffold" subsection with signal/benefit table.

### 4. Cross-File Alignment

All `project_templates/` files now use consistent language for:

- Single-agent default + optional Build -> Review
- No mandatory planner
- Security gates non-negotiable

## Quality Assurance

- All policy loaders cross-referenced and synchronized.
- Guide updated to reflect current policy.
- No breaking changes from v2.5.

---

## Release Notes: v2.5

**Release Date**: March 3, 2026  
**Status**: Ready for Production

## v2.5 Overview

v2.5 adds **cross-agent context-efficiency controls** to minimize token consumption and ensure consistent AI behavior across all agent types (Claude, GitHub Copilot, VS Code Copilot, etc.). The release includes a new context-resumption prompt template and hardened build pipeline.

## ✅ What's New

### 1. Context-Efficient Read Order (All Agents)

New mandatory read order for all AI agents:

```text
1. Read docs/FILE_MAP.md first (orientation layer)
2. Load only task-relevant files (never preload entire codebase)
3. Respect token budget: max 3 source files per task unless explicitly required
```

**Where it's enforced**:

- ✅ `ops/AI_WORKFLOW.md` — canonical source (Section 1.1)
- ✅ `AGENTS.md` — universal agent entry point
- ✅ `CLAUDE.md` — Claude Code auto-read rules
- ✅ `.github/copilot-instructions.md` — VS Code Copilot policy loader
- ✅ `guides/AI_Project_Workflow_Guide.md` — workflow documentation

**Impact**: ~40% reduction in token consumption for typical agent sessions while maintaining accuracy.

### 2. SESSION_RESUME.md — Context Handoff Template

New reusable prompt template for resuming conversations or switching AI agents:

- **Location**: `ops/prompts/SESSION_RESUME.md`
- **Use case**: When resuming a long project context or switching from one agent to another
- **Format**: Structured template with placeholders for `{{CURRENT_TASK}}` and `{{RELEVANT_FILES}}`
- **Governance**: Automatically injects FILE_MAP.md + token-budget rules into context

Register your use:

```text
Agent: "Run ops/prompts/SESSION_RESUME.md to resume our context"
Agent will:
  1. Load FILE_MAP.md for orientation
  2. Load only files you specify in {{RELEVANT_FILES}}
  3. Respect token budget rule during the session
```

### 3. Build Pipeline Hardening

**`build_exe.py` now bundles canonical `project_templates/`**:

- Added `--add-data` flag to PyInstaller configuration
- Ensures .exe distributions always include on-disk templates (vs. stale embedded fallback)
- Single source of truth maintained across all distribution channels

**`scaffold_project.py` now syncs runtime templates**:

- Added `FILES = load_templates()` call after function definition
- Generator always prefers on-disk `project_templates/` as primary source
- Falls back to embedded templates only if directory missing

### 4. Documentation Alignment

**Parent ReadMe Updated**:

- Added "Context-efficient agent startup" to feature list
- References to FILE_MAP.md and SESSION_RESUME.md usage

**Workflow Guide Updated** (v2.4 → v2.5):

- Added "What Changed in v2.5" section
- Policy hierarchy diagram now shows FILE_MAP.md as orientation-first layer
- Clarified token-budget rule (≤3 files/task)

**Template-Level Documentation Updated**:

- `project_templates/README.md` — usage guidance for FILE_MAP-first and SESSION_RESUME
- `docs/FILE_MAP.md` — registration row for SESSION_RESUME.md
- `docs/FILE_MAP.md` — registration row for SESSION_RESUME.md

## 🔍 Quality Assurance

**Testing**:

- ✅ All unit tests pass (2 tests per variant, ~0.09s execution)
- ✅ Template parity validation (embedded vs. on-disk)
- ✅ Cross-repo consistency scans (13 references per repo confirmed)

**Code Validation**:

- ✅ No broken references (all FILE_MAP, SESSION_RESUME, ops/prompts paths verified)
- ✅ No deprecated markers in release content
- ✅ All entry points aligned on new read order
- ✅ Build pipeline tested and verified

**Version Consistency**:

- ✅ Both repos (free + the AI-guided scaffold) aligned on v2.5
- ✅ All policy files cross-referenced and synchronized

## 📋 Migration Guide (For Existing Projects)

If you have an existing scaffolded project, to adopt v2.5:

1. **Add SESSION_RESUME.md prompt template**:

   ```bash
   cp ops/prompts/SESSION_RESUME.md /path/to/your/project/ops/prompts/
   ```

2. **Update policy files** — If you have local customizations, merge these sections:
   - `ops/AI_WORKFLOW.md` — Section 1.1 "Context-Efficient Read Order"
   - `AGENTS.md` — "Read order" step
   - `CLAUDE.md` — "Read order" step
   - `.github/copilot-instructions.md` — "Read order" step

3. **Update FILE_MAP.md** — Add row for SESSION_RESUME.md:

   ```markdown
   | `SESSION_RESUME.md` | Standard context-resume prompt: inject governance + FILE_MAP + current task only |
   ```

4. **No breaking changes** — Existing projects remain functional; v2.5 improvements are opt-in.

## 🚀 Distribution

Both variants updated and ready:

- **ai-project-scaffold** (free, bootstrap-less)
  - ✅ Generator updated
  - ✅ .exe build hardened
  - ✅ v2.5 templates included
  
- **ai-project-scaffold-the AI-guided scaffold** (AI-guided, [redacted-tiering-item])
  - ✅ Generator updated (with the AI-guided scaffold-specific features preserved)
  - ✅ .exe build hardened
  - ✅ v2.5 templates included ([redacted-tiering-item].md unaffected)

## 🐛 Known Limitations

- TOKEN_BUDGET rule is advisory (not enforced by generator) — requires agent discipline
- SESSION_RESUME.md requires manual invocation (no auto-trigger mechanism)
- the AI-guided scaffold [redacted-tiering-item] unaffected by v2.5 (maintains backward compat)

## 📞 Support & Feedback

- Open issues on respective GitHub repos
- Contribute improvements via pull requests
- See CONTRIBUTING.md for guidelines
- Support via [GitHub Sponsors](https://github.com/sponsors/christopherrainnel) or [Patreon](https://www.patreon.com/posts/standard-one-tip-152177425?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link)

---

**Next Release Target**: v3.0 (Q3 2026) — Full automation of context-efficiency controls via MCP agent framework integration.

