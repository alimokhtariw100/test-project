#!/usr/bin/env python3
"""Validate a local Agent Skill folder."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}


def validate_skill(skill_path: str | Path) -> tuple[bool, str]:
    root = Path(skill_path)
    skill_md = root / "SKILL.md"
    if not root.is_dir():
        return False, f"Skill folder not found: {root}"
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

    unexpected = set(frontmatter) - ALLOWED_FRONTMATTER
    if unexpected:
        return False, f"Unexpected frontmatter keys: {', '.join(sorted(unexpected))}"

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not name.strip():
        return False, "Frontmatter requires a non-empty string name"
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        return False, "Skill name must be lowercase hyphen-case"
    if len(name) > 64:
        return False, "Skill name is longer than 64 characters"
    if root.name != name:
        return False, f"Directory name '{root.name}' must match skill name '{name}'"

    if not isinstance(description, str) or not description.strip():
        return False, "Frontmatter requires a non-empty string description"
    if len(description) > 1024:
        return False, "Description is longer than 1024 characters"
    if "<" in description or ">" in description:
        return False, "Description cannot contain angle brackets"

    body = content[match.end():].strip()
    if not body:
        return False, "SKILL.md body is empty"

    agents_file = root / "agents" / "openai.yaml"
    if not agents_file.is_file():
        return False, "agents/openai.yaml not found"
    try:
        agent_config = yaml.safe_load(agents_file.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return False, f"Invalid agents/openai.yaml: {exc}"
    if not isinstance(agent_config, dict) or not isinstance(agent_config.get("interface"), dict):
        return False, "agents/openai.yaml must contain an interface mapping"
    if not agent_config["interface"].get("display_name"):
        return False, "agents/openai.yaml requires interface.display_name"

    missing_references: list[str] = []
    for reference in re.findall(r"`(references/[^`]+)`", content):
        if not (root / reference).is_file():
            missing_references.append(reference)
    if missing_references:
        return False, "Missing referenced files: " + ", ".join(sorted(set(missing_references)))

    placeholders = ["TODO:", "replace or remove me", "Replace or remove this"]
    for file_path in root.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in {".md", ".txt", ".yaml", ".yml", ".py"}:
            text = file_path.read_text(encoding="utf-8")
            for placeholder in placeholders:
                if placeholder in text:
                    return False, f"Placeholder text remains in {file_path.relative_to(root)}"

    return True, "Skill is valid"


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: quick_validate.py <skill-folder>")
    valid, message = validate_skill(sys.argv[1])
    print(message)
    raise SystemExit(0 if valid else 1)


if __name__ == "__main__":
    main()
