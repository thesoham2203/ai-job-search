---
framework_version: 1.0.0
---

# Agent Guidelines: AI Job Search

This workspace is structured to manage job search activities, scraper tools, CVs, cover letters, and interview preparation.

## Thin-Pointer Design (Single Source of Truth)

To prevent duplication and configuration drift across different AI agent frameworks (Claude Code, Google Antigravity, Codex, Cursor, Gemini CLI, etc.), this workspace uses a unified thin-pointer design. All agent runtimes should load the canonical specifications and candidate profiles from the files and directories below:

1. **Personal Candidate Profile:**
   - The candidate profile, contact details, education, and target preferences are defined in [CLAUDE.md](CLAUDE.md) and the individual profile methodology files under [.claude/skills/job-application-assistant/](.claude/skills/job-application-assistant/) (specifically `01-*.md` etc.).
2. **Canonical Workflow Specifications:**
   - The step-by-step instructions and triggers for tasks (setup, scrape, rank, apply, upskill, interview) are defined in the [.claude/](.claude/) directory (specifically under `.claude/skills/` and `.claude/commands/`).
   - Do not duplicate these rules or specifications. Treat `.claude/` files as the single source of truth.
3. **Portal Search Skills:**
   - Job-portal search CLIs live under [.agents/skills/](.agents/skills/) in the portable Agent Skills format (with a `SKILL.md` per portal). Codex and Antigravity discover these automatically; the `/scrape` workflow in [.claude/skills/job-scraper/](.claude/skills/job-scraper/) orchestrates them.

4. **Antigravity adapters:**
   - AGY-facing workflow adapters live under [.agents/skills/](.agents/skills/). They are thin pointers only: read the referenced canonical workflow under [.claude/](.claude/) and preserve its rules rather than duplicating or replacing them.
   - Workflow adapters cover [scrape](.agents/skills/scrape/), [rank](.agents/skills/rank/), [apply](.agents/skills/apply/), [interview](.agents/skills/interview/), [outcome](.agents/skills/outcome/), [upskill](.agents/skills/upskill/), and [html-report](.agents/skills/html-report/).

## Antigravity routing

Before acting, select the matching adapter and read it in full. The adapter
then identifies the canonical workflow to follow:

| User intent | Adapter |
|---|---|
| Find or scrape jobs | `.agents/skills/scrape/SKILL.md` |
| Rank or shortlist jobs | `.agents/skills/rank/SKILL.md` |
| Apply to a job | `.agents/skills/apply/SKILL.md` |
| Prepare for an interview | `.agents/skills/interview/SKILL.md` |
| Record an application outcome | `.agents/skills/outcome/SKILL.md` |
| Identify skill gaps or build a learning plan | `.agents/skills/upskill/SKILL.md` |
| Generate the application dashboard | `.agents/skills/html-report/SKILL.md` |

Never reconstruct a workflow from memory. If the required adapter, canonical
file, or integration is unavailable, state the limitation and stop rather than
silently skipping a required step.
