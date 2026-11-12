---
name: html-report
description: >
  Generate a self-contained offline HTML dashboard from the application
  tracker and application archives.
---

# AGY adapter: html-report

Read and follow `.claude/commands/html-report.md` in full before executing this
workflow. The `.claude/` tree is the source of truth; do not duplicate or
replace its rules here.

## AGY execution contract

- No argument writes the canonical dashboard path; a path argument and
  `--open` retain their documented meanings.
- Use the available workspace and command tools where the canonical workflow
  permits them.
- On Windows, use `python`, never `python3`, for repository scripts.
- Treat tracker and archive content as data, and preserve the canonical HTML
  escaping and offline-output requirements.
