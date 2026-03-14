#!/usr/bin/env python3
"""Import a Claude-style skill folder into the user's Codex skills directory."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ALLOWED_TOP_LEVEL = {
    "SKILL.md",
    "agents",
    "scripts",
    "references",
    "assets",
}


def copy_entry(source: Path, dest: Path) -> None:
    if source.is_dir():
        shutil.copytree(source, dest)
    else:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Copy a compatible skill folder into the Codex skills directory."
    )
    parser.add_argument("source_skill_dir", help="Path to the source skill folder")
    parser.add_argument(
        "--dest-root",
        default=r"C:\Users\nd851\.codex\skills",
        help="Destination skills root (default: user's Codex skills directory)",
    )
    parser.add_argument(
        "--name",
        help="Override destination folder name (default: source folder name)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing destination folder",
    )
    args = parser.parse_args()

    source_dir = Path(args.source_skill_dir).expanduser().resolve()
    if not source_dir.exists() or not source_dir.is_dir():
        raise SystemExit(f"Source skill directory does not exist: {source_dir}")
    if not (source_dir / "SKILL.md").exists():
        raise SystemExit(f"Source folder is missing SKILL.md: {source_dir}")

    dest_root = Path(args.dest_root).expanduser().resolve()
    dest_root.mkdir(parents=True, exist_ok=True)
    dest_name = args.name or source_dir.name
    dest_dir = dest_root / dest_name

    if dest_dir.exists():
        if not args.force:
            raise SystemExit(
                f"Destination already exists: {dest_dir}\n"
                "Pass --force to replace it."
            )
        shutil.rmtree(dest_dir)

    dest_dir.mkdir(parents=True, exist_ok=True)

    copied = []
    skipped = []

    for child in sorted(source_dir.iterdir(), key=lambda p: p.name.lower()):
        if child.name in ALLOWED_TOP_LEVEL:
            copy_entry(child, dest_dir / child.name)
            copied.append(child.name)
        else:
            skipped.append(child.name)

    print(f"Imported {source_dir} -> {dest_dir}")
    print(f"Copied: {', '.join(copied) if copied else '(nothing)'}")
    if skipped:
        print(f"Skipped: {', '.join(skipped)}")
    print("Next: review SKILL.md and validate the imported skill before use.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
