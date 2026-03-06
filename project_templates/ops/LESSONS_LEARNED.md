# Lessons Learned

> Log recurring mistakes and their fixes here. Only add entries that are likely to happen again.
> Keep entries short and actionable. This is not a general journal — it is a reference for avoiding repeat errors.

## Format

```
### YYYY-MM-DD — Short title
**Problem**: What went wrong.
**Root cause**: Why it happened.
**Fix**: What resolved it.
**Prevention**: How to avoid it next time.
```

---

<!-- Add entries below this line -->

### 2026-03-06 - Governance boot skipped at session start
**Problem**: Agent started implementation without loading required governance context.
**Root cause**: Session began with task-only prompting and no explicit governance boot instruction.
**Fix**: Added a required session-start prompt across loaders, workflow, README, and SESSION_RESUME.
**Prevention**: Require the GOVERNANCE BOOT prompt before implementation in every new session.
