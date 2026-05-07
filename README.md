# hv-overnight-skills

Source repo for **Anthropic Routines** to clone read-only when running 横纵分析 (HV-analysis) overnight. **Not for human use directly**——本地交互会话用本地的 `~/.claude/skills/hv-analysis`。

## Layout

```
.claude/skills/
├── hv-analysis-cloud/    # cloud-tailored HV skill (no PDF, no checkpoints, writes to /tmp + Notion)
├── munger-perspective/   # Charlie Munger 思维框架
├── musk-perspective/     # Elon Musk first-principles
└── jobs-perspective/     # Steve Jobs taste/简化
inventory/
└── world-models-2026-04.md   # 35+ world-model objects with briefs + URLs
```

## How a Routine uses this

```
job_config.ccr.session_context.sources = [
  { git_repository: { url: "https://github.com/2939427213a-boop/hv-overnight-skills" } }
]
```

When the routine starts, the sandbox `cwd` is the cloned repo root. Claude Code auto-discovers `.claude/skills/` and the 4 skills become invokable. The routine prompt then tells the agent to:

1. Read `inventory/world-models-2026-04.md` to find the assigned object's brief
2. Invoke `/hv-analysis-cloud "<对象名>"` to run the full Phase 1-7 flow
3. Push the result Notion page via `mcp__claude_ai_Notion__notion-create-pages`

## Modifying

- This repo is read-only at routine runtime. Updates happen by pushing from local Mac.
- Never put secrets here; routines clone unauthenticated.

## Provenance

- `hv-analysis-cloud` is a cloud variant of `hv-analysis` skill by 数字生命卡兹克 (Khazix), modified to remove user checkpoints and PDF generation.
- `*-perspective` skills are example templates from the `nuwa-skill` framework.
