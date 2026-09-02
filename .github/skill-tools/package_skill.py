#!/usr/bin/env python3
"""Validate and package one Agent Skill as skill.zip."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

from quick_validate import validate_skill

MAX_SKILL_ZIP_BYTES = 25 * 1024 * 1024


def package_skill(skill_path: Path, output_dir: Path) -> Path:
    skill_path = skill_path.resolve()
    output_dir = output_dir.resolve()

    valid, message = validate_skill(skill_path)
    if not valid:
        raise ValueError(message)
    print(message)

    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "skill.zip"
    if output_file.exists():
        output_file.unlink()

    with zipfile.ZipFile(output_file, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(skill_path.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(skill_path.parent))
                print(f"Added: {path.relative_to(skill_path.parent)}")

    archive_size = output_file.stat().st_size
    if archive_size > MAX_SKILL_ZIP_BYTES:
        output_file.unlink(missing_ok=True)
        raise ValueError(
            f"Packaged skill exceeds the 25 MiB limit: {archive_size} bytes"
        )

    print(f"Packaged: {output_file} ({archive_size} bytes)")
    return output_file


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_path", type=Path)
    parser.add_argument("output_dir", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()
    package_skill(args.skill_path, args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
