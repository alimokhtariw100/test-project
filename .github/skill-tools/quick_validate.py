#!/usr/bin/env python3
"""Validate the required structure and SKILL.md frontmatter for one Agent Skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ALLOWED_FRONTMATTER_KEYS = {"name", "description"}


def validate_skill(skill_path: str | Path) -> tuple[bool, str]:
    root = Path(skill_path)
    if not root.is_dir():
        return False, f"Skill directory not found: {root}"

    skill_md = root / "SKILL.md"
    if not skill_md.is_file():
        return False, "SKILL.md not found"

    content = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        return False, "SKILL.md must start with valid YAML frontmatter"

    try:
        frontmatter = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return False, f"Invalid YAML frontmatter: {exc}"

    if not isinstance(frontmatter, dict):
        return False, "Frontmatter must be a YAML mapping"

    unexpected = set(frontmatter) - ALLOWED_FRONTMATTER_KEYS
    if unexpected:
        return False, f"Unexpected frontmatter keys: {', '.join(sorted(unexpected))}"

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not name.strip():
        return False, "Frontmatter name is required"
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        return False, "Frontmatter name must use lowercase hyphen-case"
    if name != root.name:
        return False, "Frontmatter name must match the skill directory name"
    if len(name) > 64:
        return False, "Frontmatter name exceeds 64 characters"

    if not isinstance(description, str) or not description.strip():
        return False, "Frontmatter description is required"
    if len(description) > 1024:
        return False, "Frontmatter description exceeds 1024 characters"
    if "<" in description or ">" in description:
        return False, "Frontmatter description cannot contain angle brackets"

    openai_yaml = root / "agents" / "openai.yaml"
    if not openai_yaml.is_file():
        return False, "agents/openai.yaml not found"

    if len(content.splitlines()) > 500:
        return False, "SKILL.md exceeds the 500-line control-plane guideline"

    return True, "Skill is valid"


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: quick_validate.py <skill_directory>")
        return 2
    valid, message = validate_skill(sys.argv[1])
    print(message)
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
