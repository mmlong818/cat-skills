# Everything Claude Code Porting Notes

Use this note when the source repository is [`affaan-m/everything-claude-code`](https://github.com/affaan-m/everything-claude-code).

## What The Repo Is

`everything-claude-code` is a large collection of Claude Code oriented material: commands, hooks, agents, output styles, MCP setup notes, and many skills. It is not a single portable skill.

## Good Import Targets

Start with skill folders whose value is mainly:

- a strong `SKILL.md` workflow
- local helper scripts
- reusable references
- templates or assets

These usually adapt cleanly with wording and path fixes.

## Higher-Risk Targets

Treat these as partial references, not direct imports:

- command-centric folders that assume Claude slash commands
- setup flows that depend on `.claude/` conventions
- automation that depends on Claude-specific hooks or agents
- skills that mostly wrap external installers instead of providing reusable workflow knowledge

## Suggested Workflow For This Repo

1. Make a local checkout or extract a ZIP.
2. Run `python scripts/list_claude_skills.py <repo-path>`.
3. Read only the `SKILL.md` files for the user-relevant candidates.
4. Import one target skill at a time with `python scripts/import_skill.py <source-skill-dir>`.
5. Rewrite imported instructions so they mention Codex paths, tools, and constraints instead of Claude Code ones.

## Specific Recommendation

If the user gives only the top-level repo URL and does not name a specific skill, do not import the whole repository. Pick or propose one narrow Codex-native skill that solves the user's immediate need.
