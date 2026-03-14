# Claude 技能导入

这是 `import-claude-skills` 的中文说明版。

## 这个技能是做什么的

把 Claude Code 风格的技能仓库，筛选、检查并迁移成 Codex 可用的技能，而不是整仓照搬。

## 核心价值

- 快速发现外部仓库里有哪些 skill
- 只导入真正有价值的部分
- 规避 Claude 专属规则直接照搬后的失效问题

## 推荐流程

1. 先准备本地仓库或解压目录
2. 扫描里面的 `SKILL.md`
3. 只查看和当前目标相关的 skill
4. 判断是否依赖 `.claude/`、slash commands、hooks 等专属能力
5. 只复制 `SKILL.md`、`scripts`、`references`、`assets` 等核心内容
6. 再改造成 Codex 版本
