# Code Review (Agent Task)

## Scope

What files or modules should be reviewed?
- Files:
- Focus area (security / performance / readability / all):

## Review Checklist

- [ ] No hardcoded secrets or credentials
- [ ] Error handling is present and meaningful
- [ ] No unused imports, variables, or dead code
- [ ] Functions are focused (single responsibility)
- [ ] Naming is clear and consistent
- [ ] Edge cases are handled (null, empty, unexpected input)
- [ ] Dependencies added are justified and version-pinned

## What to Flag

- Security risks (injection, exposed secrets, missing validation)
- Performance issues (unnecessary loops, missing pagination, large payloads)
- Maintainability concerns (deeply nested logic, magic numbers, unclear naming)
- Missing tests for critical paths

## Output Format

For each issue found:
```
File: <path>
Line: <number>
Severity: critical | warning | suggestion
Issue: <description>
Fix: <recommended change>
```
