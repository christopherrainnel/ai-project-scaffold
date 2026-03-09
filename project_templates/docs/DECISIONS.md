# Decisions Log

Version: 0.1
Last Updated: {{DATE}}

> Record every significant decision here. AI agents check this before proposing changes.
> If a proposed change conflicts with a recorded decision, the agent must stop and ask.

## Entry Format

```
### YYYY-MM-DD — [Short title]
**Decision**: What was decided.
**Status**: Decided | Deferred
**Why**: The reasoning behind it.
**Current assumption**: (if Deferred) What we assume for now.
**Trigger to revisit**: When to re-evaluate.
**Risk if wrong**: (optional) Impact if this decision turns out to be wrong.
**Alternatives considered**: What else was evaluated.
**Tradeoffs**: What you gain and what you give up.
```

---

### {{DATE}} — Governance scaffold adopted

**Decision**: Use a standardized governance scaffold for AI-assisted development.
**Status**: Decided
**Why**: Reduce architectural drift, improve auditability, enforce secure defaults from day one.
**Current assumption**: N/A
**Trigger to revisit**: N/A
**Alternatives considered**: Ad-hoc instructions per project; no governance at all.
**Tradeoffs**: Small upfront setup time; large reduction in long-term risk and rework.

---

<!-- Add new decisions above this line, newest first -->
