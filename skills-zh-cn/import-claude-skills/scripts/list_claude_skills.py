#!/usr/bin/env python3
"""List SKILL.md-based skills inside a Claude-style repository."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FRONTMATTER_RE = re.compile(
    r"^---\s*\n(?P<body>.*?)\n---\s*\n", re.DOTALL
)


def extract_field(frontmatter: str, field: str) -> str:
    pattern = re.compile(rf"^{re.escape(field)}:\s*(.+?)\s*$", re.MULTILINE)
    match = pattern.search(frontmatter)
    if not match:
        return ""
    value = match.group(1).strip()
    return value.strip("\"'")


def parse_skill(skill_md: Path) -> tuple[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return skill_md.parent.name, ""
    frontmatter = match.group("body")
    name = extract_field(frontmatter, "name") or skill_md.parent.name
    description = extract_field(frontmatter, "description")
    return name, description


def discover(repo_path: Path) -> list[Path]:
    return sorted(
        p for p in repo_path.rglob("SKILL.md")
        if ".git" not in p.parts and "__pycache__" not in p.parts
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Discover SKILL.md-based skills in a local repository."
    )
    parser.add_argument("repo_path", help="Path to a local repo or extracted archive")
    args = parser.parse_args()

    repo_path = Path(args.repo_path).expanduser().resolve()
    if not repo_path.exists():
        raise SystemExit(f"Repository path does not exist: {repo_path}")

    skills = discover(repo_path)
    if not skills:
        print("No SKILL.md files found.")
        return 0

    for skill_md in skills:
        name, description = parse_skill(skill_md)
        rel_dir = skill_md.parent.relative_to(repo_path)
        print(f"{name}\t{rel_dir}")
        if description:
            print(f"  {description}")

    print(f"\nFound {len(skills)} skill(s) in {repo_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
