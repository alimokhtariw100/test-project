#!/usr/bin/env python3
"""Validate and package one Agent Skill as skill.zip."""

from __future__ import annotations

import sys
import zipfile
from pathlib import Path

from quick_validate import validate_skill


MAX_SKILL_ZIP_BYTES = 25 * 1024 * 1024


def package_skill(skill_path: str | Path, output_dir: str | Path | None = None) -> Path:
    root = Path(skill_path).expanduser().resolve()
    valid, message = validate_skill(root)
    if not valid:
        raise SystemExit(f"Validation failed: {message}")
    print(message)

    destination = Path(output_dir).expanduser().resolve() if output_dir else Path.cwd()
    destination.mkdir(parents=True, exist_ok=True)
    output = destination / "skill.zip"
    if output.exists():
        output.unlink()

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in sorted(root.rglob("*")):
            if not file_path.is_file():
                continue
            arcname = file_path.relative_to(root.parent)
            archive.write(file_path, arcname)
            print(f"Added: {arcname}")

    size = output.stat().st_size
    if size > MAX_SKILL_ZIP_BYTES:
        output.unlink(missing_ok=True)
        raise SystemExit(
            f"Packaged skill exceeds 25 MiB ({size:,} bytes). Reduce bundled files."
        )

    print(f"Packaged: {output} ({size:,} bytes)")
    return output


def main() -> None:
    if len(sys.argv) not in {2, 3}:
        raise SystemExit("Usage: package_skill.py <skill-folder> [output-directory]")
    package_skill(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else None)


if __name__ == "__main__":
    main()
