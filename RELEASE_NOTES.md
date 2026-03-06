# Release Notes: v2.13

**Release Date**: March 6, 2026
**Status**: Ready for Production

## Overview

v2.13 backports shared-safe governance/template updates from the latest Tier1 template snapshot while preserving free-tier friction boundaries.

## What's New

### 1. Cross-Tier Shared Governance Wording Alignment

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
- Confirmed free-tier boundaries remain intact: no `[redacted-tiering-item].md`, no `[redacted-tiering-item].md`, no `[redacted-tiering-item].md`, no `[redacted-tiering-item]`, and no bootstrap hard gates were introduced.

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
- Confirmed free-tier boundary remains unchanged (no Tier1 bootstrap artifacts added).

---

# Release Notes: v2.11

**Release Date**: March 5, 2026
**Status**: Ready for Production

## Overview

v2.11 aligns free template journey terminology and phase-close evaluation language with the latest VibeCoder_Pack governance model while preserving free-tier boundaries.

## What's New

### 1. Journey Language Alignment (Free Templates)

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
- Free-tier baseline now requires:
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

### 1. Two-Mode QA Boundary (Free + Tier1)

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

v2.7 clarifies repo boundary rules between free and Tier1 so cross-repo sync can remain deterministic.

## What's New

### 1. Tier Scope Clarification

- Added explicit `both` vs `free` vs `tier1` wording in documentation.
- Confirmed shared governance baseline remains aligned across both repos.

### 2. Alignment Handoff Classification

- Updated `REPO_ALIGNMENT_AGENT_HANDOFF.md` with scope (`free`, `tier1`, `both`) and applied/deferred status.
- Marked entitlement-runtime candidates as `tier1` future work until runtime modules exist.

---

# Release Notes: v2.6

**Release Date**: March 4, 2026
**Status**: Ready for Production

## Overview

v2.6 adds **multi-agent policy alignment** across all governance files. Free tier now explicitly documents single-agent default with optional Build -> Review flow. Limitation-awareness prompts ensure agents briefly note trade-offs when switching execution modes.

## What's New

### 1. Multi-Agent Policy (Free Tier)

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

- Added "Multi-Agent Support (Free Tier)" section to `guides/AI_Project_Workflow_Guide.md`.
- Added "When to Escalate to Tier1" subsection with signal/benefit table.

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

- ✅ Both repos (free + tier1) aligned on v2.5
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
  
- **ai-project-scaffold-tier1** (AI-guided, [redacted-tiering-item])
  - ✅ Generator updated (with tier1-specific features preserved)
  - ✅ .exe build hardened
  - ✅ v2.5 templates included ([redacted-tiering-item].md unaffected)

## 🐛 Known Limitations

- TOKEN_BUDGET rule is advisory (not enforced by generator) — requires agent discipline
- SESSION_RESUME.md requires manual invocation (no auto-trigger mechanism)
- Tier1 [redacted-tiering-item] unaffected by v2.5 (maintains backward compat)

## 📞 Support & Feedback

- Open issues on respective GitHub repos
- Contribute improvements via pull requests
- See CONTRIBUTING.md for guidelines
- Support via [GitHub Sponsors](https://github.com/sponsors/christopherrainnel) or [Patreon](https://www.patreon.com/posts/standard-one-tip-152177425?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link)

---

**Next Release Target**: v3.0 (Q3 2026) — Full automation of context-efficiency controls via MCP agent framework integration.

