#!/usr/bin/env python3
"""Initialize a new Agent Skill directory."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


SKILL_TEMPLATE = """---
name: {name}
description: TODO: describe what the skill does and when it should be used.
---

# {title}

TODO: replace this template with the final instructions.
"""


def validate_name(name: str) -> None:
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise SystemExit(
            "Skill name must use lowercase letters, digits, and single hyphens only."
        )
    if len(name) > 64:
        raise SystemExit("Skill name must be 64 characters or fewer.")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_name")
    parser.add_argument("--path", required=True)
    args = parser.parse_args()

    validate_name(args.skill_name)
    root = Path(args.path).expanduser().resolve() / args.skill_name
    if root.exists():
        raise SystemExit(f"Skill directory already exists: {root}")

    root.mkdir(parents=True)
    (root / "references").mkdir()
    (root / "scripts").mkdir()
    (root / "assets").mkdir()
    (root / "agents").mkdir()

    title = " ".join(part.capitalize() for part in args.skill_name.split("-"))
    (root / "SKILL.md").write_text(
        SKILL_TEMPLATE.format(name=args.skill_name, title=title), encoding="utf-8"
    )
    (root / "scripts" / "example.py").write_text(
        "#!/usr/bin/env python3\nprint('replace or remove me')\n", encoding="utf-8"
    )
    (root / "references" / "README.md").write_text(
        "Replace or remove this reference.\n", encoding="utf-8"
    )
    (root / "assets" / "README.txt").write_text(
        "Replace or remove this asset.\n", encoding="utf-8"
    )
    (root / "agents" / "openai.yaml").write_text(
        f'interface:\n  display_name: "{title}"\n', encoding="utf-8"
    )

    print(f"Initialized skill at {root}")


if __name__ == "__main__":
    main()
