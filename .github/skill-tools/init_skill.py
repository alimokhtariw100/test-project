#!/usr/bin/env python3
"""Initialize a new Agent Skill directory from a minimal template."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def validate_name(name: str) -> None:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError(
            "Skill name must use lowercase letters, digits, and single hyphens only."
        )
    if len(name) > 64:
        raise ValueError("Skill name must be 64 characters or fewer.")


def title_case(name: str) -> str:
    return " ".join(part.capitalize() for part in name.split("-"))


def initialize(name: str, output_root: Path) -> Path:
    validate_name(name)
    skill_dir = output_root.resolve() / name
    if skill_dir.exists():
        raise FileExistsError(f"Skill directory already exists: {skill_dir}")

    skill_dir.mkdir(parents=True)
    (skill_dir / "scripts").mkdir()
    (skill_dir / "references").mkdir()
    (skill_dir / "assets").mkdir()
    (skill_dir / "agents").mkdir()

    skill_md = f"""---
name: {name}
description: TODO describe what this skill does and when it should be used.
---

# {title_case(name)}

## Instructions

TODO replace this template with the finished skill instructions.
"""
    (skill_dir / "SKILL.md").write_text(skill_md, encoding="utf-8")
    (skill_dir / "agents" / "openai.yaml").write_text(
        f'interface:\n  display_name: "{title_case(name)}"\n', encoding="utf-8"
    )
    (skill_dir / "scripts" / "example.py").write_text(
        '#!/usr/bin/env python3\nprint("replace or remove this example")\n',
        encoding="utf-8",
    )
    (skill_dir / "references" / "README.md").write_text(
        "# Replace or remove this example reference\n", encoding="utf-8"
    )
    (skill_dir / "assets" / "README.txt").write_text(
        "Replace or remove this example asset.\n", encoding="utf-8"
    )
    print(f"Initialized skill at {skill_dir}")
    return skill_dir


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_name")
    parser.add_argument("--path", required=True, type=Path)
    args = parser.parse_args()
    initialize(args.skill_name, args.path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
