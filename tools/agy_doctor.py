#!/usr/bin/env python3
"""Check local prerequisites and routing files used by Antigravity."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REQUIRED_FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    ".claude/skills/job-scraper/SKILL.md",
    ".claude/skills/upskill/SKILL.md",
    ".claude/commands/apply.md",
    ".claude/commands/interview.md",
    ".claude/commands/outcome.md",
    ".claude/commands/html-report.md",
    "tools/rank_state.py",
)
ADAPTERS = ("scrape", "rank", "apply", "interview", "outcome", "upskill", "html-report")
OPTIONAL_COMMANDS = ("bun", "lualatex", "xelatex")


def check_file(relative: str) -> bool:
    if (ROOT / relative).is_file():
        print(f"PASS file      {relative}")
        return True
    print(f"FAIL file      {relative}")
    return False


def check_adapter(name: str) -> bool:
    path = ROOT / ".agents" / "skills" / name / "SKILL.md"
    if not path.is_file():
        print(f"FAIL adapter   {name}: missing SKILL.md")
        return False
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n") or f"name: {name}\n" not in text:
        print(f"FAIL adapter   {name}: invalid frontmatter")
        return False
    print(f"PASS adapter   {name}")
    return True


def main() -> int:
    failures = sum(not check_file(path) for path in REQUIRED_FILES)
    failures += sum(not check_adapter(name) for name in ADAPTERS)

    if sys.version_info < (3, 10):
        print("FAIL runtime   Python 3.10+ is required")
        failures += 1
    else:
        print(f"PASS runtime   Python {sys.version_info.major}.{sys.version_info.minor}")

    for command in OPTIONAL_COMMANDS:
        resolved = shutil.which(command)
        if resolved:
            print(f"PASS optional  {command}: {resolved}")
        else:
            print(f"WARN optional  {command}: not found")

    if failures:
        print(f"agy_doctor: FAIL ({failures} required check(s))")
        return 1
    print("agy_doctor: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
