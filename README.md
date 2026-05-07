# hv-overnight-skills

Source repo for **Anthropic Routines** to clone read-only when running 横纵分析 (HV-analysis) overnight as cloud batches. **Not for human use directly**——本地交互会话用本地的 `~/.claude/skills/hv-analysis`。

## Why public

Anthropic Routines 的 `sources.git_repository` 字段**不携带 user 的 GitHub 凭证**。私有 repo 会撞 401。所以本 repo 只能 public。私人研究笔记应当独立维护（不要进 references/），下游 routine 通过 inventory + sibling SKILL 拿到方法论即可。

## Layout

```
.claude/skills/
├── hv-analysis-cloud/    # cloud-tailored HV skill (no PDF, no checkpoints, writes /tmp + Notion)
├── munger-perspective/   # Charlie Munger 思维框架
├── musk-perspective/     # Elon Musk first-principles
└── jobs-perspective/     # Steve Jobs taste/简化
inventory/
└── world-models-2026-04.md   # 35+ world-model objects with briefs + URLs
```

## How a Routine uses this

```jsonc
job_config.ccr.session_context.sources = [
  { git_repository: { url: "https://github.com/2939427213a-boop/hv-overnight-skills" } }
]
```

Sandbox boots:

1. clone repo → cwd
2. Claude Code auto-discovers `.claude/skills/` → 4 skills become invokable via Skill tool
3. routine prompt tells agent to:
   - read `inventory/world-models-2026-04.md`
   - invoke `hv-analysis-cloud` skill
   - push result to Notion via the connector that's already auto-attached to sandbox
4. find Notion tool name dynamically: it's `mcp__<connector_uuid>__notion-create-pages` — connector_uuid is namespaced even when `mcp_connections.name` is set explicitly. Don't hardcode.

## How to run a new batch

1. Append new objects' briefs to `inventory/world-models-2026-04.md` (200-500 chars + 2-4 starting URLs each)
2. `git push origin main`
3. Compose 1 RemoteTrigger create body per object (use prior `.routine-bodies.json` as template):
   - `name`: `[#N] <对象>_HV-overnight`
   - `run_once_at`: stagger 1h apart, time in UTC (北京时间 - 8h)
   - `sources`: this repo URL
   - `mcp_connections`: Notion connector (uuid `ab597b4a-b429-421d-948d-ac4d323ca978`)
   - `events[0].data.message.content`: prompt referencing object name + Notion parent page_id
4. `RemoteTrigger.action="create"` for each
5. Sleep

## Modifying

- Read-only at runtime; updates push from local Mac
- Never put secrets here; routines clone unauthenticated, repo is public
- `.routine-bodies.json` (operational details) is gitignored — keep it local

## Provenance

- `hv-analysis-cloud`：本地 `hv-analysis` skill (by 数字生命卡兹克 Khazix) 的云端变体，删 user checkpoint 和 PDF 生成，加 Notion push 阶段
- `*-perspective`：`nuwa-skill` 框架的人格 skill 模板
