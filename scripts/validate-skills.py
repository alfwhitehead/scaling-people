#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md against the klick-management contract.

Contract (see docs/superpowers/specs/2026-05-27-klick-management-skill-library-design.md
and the plan's §C5):
  - File exists, non-empty.
  - YAML frontmatter present, parses, has `name` and `description`.
  - `name` matches parent directory name.
  - `description` is 20-400 chars.
  - Body has the required headings for its type (router / stub / built sub-skill).
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROUTER_SLUGS = {
    "operating-principles",
    "org-foundations-and-planning",
    "hiring",
    "team-development",
    "feedback-and-performance",
    "manager-self",
}

BUILT_SUBSKILL_HEADINGS = ("## Mode", "## Rubric", "## Draft-mode intake", "## Artifact", "## Source")
ROUTER_HEADINGS = ("## Sub-skills", "## Source")
STUB_MARKER = "> **Stubbed.**"
STUB_HEADINGS = ("## Source",)


def parse_frontmatter(content: str) -> dict[str, str] | None:
    if not content.startswith("---\n"):
        return None
    end = content.find("\n---\n", 4)
    if end < 0:
        return None
    block = content[4:end]
    result: dict[str, str] = {}
    for line in block.split("\n"):
        if ":" in line:
            k, _, v = line.partition(":")
            result[k.strip()] = v.strip()
    return result


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    rel = skill_md.relative_to(skill_dir.parent.parent)

    if not skill_md.exists():
        return [f"{rel}: missing SKILL.md"]

    content = skill_md.read_text()
    if not content.strip():
        return [f"{rel}: empty file"]

    fm = parse_frontmatter(content)
    if fm is None:
        return [f"{rel}: missing or malformed YAML frontmatter"]

    if "name" not in fm:
        errors.append(f"{rel}: frontmatter missing `name`")
    elif fm["name"] != skill_dir.name:
        errors.append(f"{rel}: frontmatter name '{fm['name']}' != directory name '{skill_dir.name}'")

    if "description" not in fm:
        errors.append(f"{rel}: frontmatter missing `description`")
    else:
        desc = fm["description"]
        if len(desc) < 20:
            errors.append(f"{rel}: description too short ({len(desc)} chars, min 20)")
        if len(desc) > 400:
            errors.append(f"{rel}: description too long ({len(desc)} chars, max 400)")

    # Body heading checks
    if skill_dir.name in ROUTER_SLUGS:
        required = ROUTER_HEADINGS
        kind = "router"
    elif STUB_MARKER in content:
        required = STUB_HEADINGS
        kind = "stub"
    else:
        required = BUILT_SUBSKILL_HEADINGS
        kind = "built sub-skill"

    for h in required:
        if h not in content:
            errors.append(f"{rel} ({kind}): missing required heading '{h}'")

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    skills_dir = repo_root / "skills"
    if not skills_dir.is_dir():
        print(f"ERROR: skills directory not found at {skills_dir}", file=sys.stderr)
        return 1

    all_errors: list[str] = []
    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir() and not p.name.startswith("."))
    for skill_dir in skill_dirs:
        all_errors.extend(validate_skill(skill_dir))

    if all_errors:
        print(f"FAIL: {len(all_errors)} validation error(s) across {len(skill_dirs)} skill(s):")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print(f"OK: {len(skill_dirs)} skill(s) validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
