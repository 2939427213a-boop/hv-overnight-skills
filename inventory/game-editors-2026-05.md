# 游戏编辑器 in-engine AI copilot 清单（来源：腾讯 IEG 游戏技术扫描第 5 主题 + worldmodel/3D batch 经验）

> 这份清单是 hv-analysis-cloud routine 在云沙箱里的**唯一对象输入**——routine 不能读用户本地的 HTML 源，所有研究对象的最小信息都得在这里给齐。每条 brief 200-500 字，附 2-4 条权威来源 URL 让 routine 起手时不用瞎搜。
>
> 9 个对象都是**本批 fire 的对象**（2026-05-09 北京时间 13:00-21:00 顺次 fire），按 fire 顺序排。
>
> **本批 meta 定位（贯穿 9 篇 Phase 4）**：当 AI 进入引擎编辑器，谁最快锁定 moat？平台开放派（#1/#2/#3）vs 中国闭源大厂派（#4/#5/#6）vs 开源/区域派（#7/#8）vs 西方闭源 AAA 派（#9）。每篇要呼应这个 9-piece mosaic 四派坐标定位。
>
> **Scope 收紧**：仅 in-engine AI copilot（引擎/平台第一方或紧密整合），不含 Rosebud / Buildbox / GDevelop AI 这类端到端 game-gen 平台。

---

## ⭐ 1. Unity Muse + Unity AI 套件（BJ 13:00 / UTC 2026-05-09T05:00:00Z）

**类型**：产品（平台第一方 in-editor AI copilot 总集）
**主体**：Unity Technologies
**一句话定义**：Unity 把 AI 工具集中到 Muse 品牌伞下 + Sentis runtime ML，是平台向开发者输出"工具一站式"叙事的关键产品。

**关键信息**：
- Muse 套件包括：Chat（对话式编程）/ Sketch（2D 概念图）/ Texture（材质）/ Animate（动画）/ Behavior（行为树）/ Sprite（精灵图）
- Unity Sentis：runtime ML inference，让 ML 模型可在玩家设备实时跑
- 商业模式：Muse subscription $30/mo per seat
- 2024 年起作为 Unity 6（统一品牌升级）的卖点重点
- Unity 2024 大裁员（Runtime Fee 风波 + 高管换血）后的"AI 翻盘"叙事中心
- 与第三方 plugin（Inworld AI / Convai / Replica / Layer AI）形成生态层叠

**起手 URL**：
- Unity Muse 官方：https://unity.com/products/muse
- Unity Sentis：https://unity.com/products/sentis
- Unity 6 keynote：https://unity.com/releases/unity-6
- Unity AI strategy 公开材料 + 2024-2025 财报

**研究角度**：
- Muse 套件是平台第一方真"AI 整合品牌"，还是若干工具的 marketing 拼盘
- Sentis runtime ML 的技术差异化（vs Unreal NNE / WebGPU 直接跑）
- Unity Muse 的 ARPU 经济性（$30/mo × seat 能否回收开发投入）
- Unity Asset Store moat 在 AI 时代的可持续性 + Runtime Fee 后开发者信任修复

**重要差异化**：3D batch #9（Adobe Substance 3D + Firefly）已分析过 DCC 工作流嵌入 AI 的横向，本篇**聚焦 Unity 编辑器内 workflow 整合**——不重做单点 AI 模型质量评测，重点在 Muse 作为"品牌伞"的产品决策、Sentis 作为 runtime ML 的差异化定位、Unity 整体 AI 战略转型。

---

## ⭐ 2. Unreal Engine 5 AI 工具链（BJ 14:00 / UTC 2026-05-09T06:00:00Z）

**类型**：产品（引擎第一方 ML 工具集，不打统一品牌）
**主体**：Epic Games
**一句话定义**：Epic 没有 Muse 式品牌伞，把 ML 能力作为引擎原子能力下沉到核心模块——ML Deformer / Metahuman Animator / RealityScan / Verse-AI——再让开发者按需调用。

**关键信息**：
- ML Deformer：实时角色变形 ML，UE5 原生，代替昂贵的离线模拟
- Metahuman Animator：手机摄像头驱动表情捕捉，AI 自动 retarget
- RealityScan：手机扫物 → 3D 资产，整合到 UE 资产库
- Verse 语言（UEFN）：与 ChatGPT 等 LLM 集成，编辑器内 AI 编程辅助
- Substrate 材质系统：与 Texture Sets 等 AI 工作流深度集成
- 第三方生态：Convai for UE / Inworld for UE（NPC AI），Marketplace AI 插件
- Unreal Engine for Fortnite (UEFN)：UGC creator 端，AI 工具触达更广泛非专业用户

**起手 URL**：
- Unreal Engine 5 官方：https://www.unrealengine.com/
- Metahuman Creator：https://www.unrealengine.com/en-US/digital-humans
- ML Deformer 文档：https://dev.epicgames.com/documentation/en-us/unreal-engine/ml-deformer-overview
- State of Unreal 2024/2025 keynote

**研究角度**：
- Epic 的"ML as native engine module"路线 vs Unity 的"Muse 品牌伞"，两种产品哲学谁更可持续
- Verse + AI 编程辅助的真实可用性（vs Cursor / Copilot for game dev）
- UEFN 在 UGC creator 端的 AI 工具触达 vs Roblox Studio AI 的对比
- UE Marketplace 的 AI 工具生态健康度

**重要差异化**：Metahuman 动画细节（动捕 / lip-sync / facial AI）将留给后续动画批 specifically 分析，本篇**聚焦 in-editor procedural + scripting + asset 三类 AI**，把 Metahuman Animator 当作一个章节而非主角；同时把 Verse + AI 编程辅助 vs Unity Muse Chat 做正面对照。

---

## ⭐ 3. Roblox Studio AI（BJ 15:00 / UTC 2026-05-09T07:00:00Z）

**类型**：产品（UGC 平台第一方 in-editor AI 总集）
**主体**：Roblox Corporation
**一句话定义**：Roblox 把 AI 全栈嵌入 Studio：Code Assist 写 Lua / Material Generator 出材质 / Texture Generator 出贴图 / Avatar Auto Setup 自动绑骨 / Studio AI Assistant 总管，目标是让"任何人都能 ship game"。

**关键信息**：
- Code Assist：Lua 自动补全 + 上下文感知，2023 推出，2024 升级
- Material Generator：text-to-PBR 材质，2024 RDC 演示
- Texture Generator：text-to-3D-texture 直接贴到 mesh
- Avatar Auto Setup：自动 rig + skin，UGC creator 不用懂 3D 技术
- Studio AI Assistant：自然语言改 Studio 项目，"Build me a forest" 直接生成场景
- 商业模式：免费给 creator，平台从 Robux 流水抽成
- 200M+ MAU，60% < 16 岁，UGC creator 端门槛是核心战略变量
- Roblox 2024-2025 财报里 AI 是核心增长叙事

**起手 URL**：
- Roblox Creator Hub：https://create.roblox.com/
- RDC 2024 keynote AI 部分：https://corp.roblox.com/newsroom
- Code Assist 文档：https://create.roblox.com/docs/code-assist
- Studio AI Assistant 公告 / Roblox 财报 AI 表态

**研究角度**：
- Roblox Studio AI 是"普通用户也能造游戏"的真 UX 突破，还是只够做 prototype
- Avatar Auto Setup 跟 3D batch 的 mesh-gen 模型有何分工
- 200M MAU + AI 助手 = UGC 内容供给雪球可能性
- Roblox AI infra 自建程度（自训 model 还是接 API），毛利率影响

**重要差异化**：3D batch 已扫过 Avatar Auto Setup 背后的 mesh-gen 技术细节，本篇**不重做 mesh 模型评测**，聚焦 Studio AI 套件作为"UGC creator 端到端编辑器闭环"——从 idea 到 ship 的 UX 路径、各 AI 模块如何衔接、Roblox 的 200M MAU 与 AI 工具能力的化学反应、平台经济的二阶效应。

---

## ⭐ 4. 腾讯 GiiNEX（BJ 16:00 / UTC 2026-05-09T08:00:00Z）

**类型**：产品（IEG 自研 AI 引擎工具链，定位"内部能力"非外部产品）
**主体**：腾讯 IEG（Interactive Entertainment Group）AI Lab + 引擎团队
**一句话定义**：GiiNEX 是 IEG 在 AI 与游戏引擎接合层做的工具栈，对外不是"产品"而是"内部能力"——procedural content / agent NPC / 编辑器副驾驶 / 美术流水线，定位类似育碧 La Forge。

**关键信息**：
- 2023-2024 IEG 公开过 GiiNEX 在 PCG（procedural content generation）方向的进展
- 腾讯 AI Lab + 王者荣耀团队（天美） + 光子工作室群有联合产出
- 与 Hunyuan 套件的关系：Hunyuan 偏内容生成模型层（文 / 图 / 3D / 视频 / 世界），GiiNEX 偏引擎工具集成层
- 公开演讲：CGDC（中国游戏开发者大会）2024 / GDC China 上的腾讯 session
- 内部产品（《王者荣耀》《和平精英》《暗区突围》等）的工具链落地证据有限
- IEG 内部"PCG / Agent / Asset / QA"四象限工具链逐步成型

**起手 URL**：
- 腾讯 AI Lab：https://ai.tencent.com/ailab/
- 腾讯 IEG 官网：https://www.tencent.com/zh-cn/business/ieg.html
- GDC China / CGDC GiiNEX 演讲（待 routine 自查）
- Hunyuan 系列 paper（关联 cross-reference）

**研究角度**：
- GiiNEX 与 Hunyuan 套件在腾讯内部的产品边界与协同机制
- IEG 内部不同工作室（天美 / 光子 / 北极光 / 魔方）对 GiiNEX 的接受度与落地场景
- 腾讯做"AI 引擎工具栈"的战略定位——是要替代 Unity/Unreal 还是补充
- GiiNEX 对外开放路径（UGC / 第三方厂商授权）的可能性

**重要差异化**：worldmodel batch #2「Tencent Hunyuan 套件」已综合分析过 GameCraft + HunyuanWorld + Hunyuan3D Studio 的世界模型 / 3D 模型层，本篇**不重做 Hunyuan 模型层**，聚焦 GiiNEX 作为"in-editor AI agent + 工具集"的产品形态、IEG 内部分发路径、与外部对手（Unity Muse / Unreal AI 工具链 / Roblox Studio AI）的横向比较。

---

## ⭐ 5. 网易伏羲 + NeoX/Messiah AI 工具链（BJ 17:00 / UTC 2026-05-09T09:00:00Z）

**类型**：产品（自研 AI Lab + 自研引擎 双轨工具链，多工作室共用）
**主体**：网易伏羲实验室 + 网易雷火 NeoX 引擎团队 + 网易 Messiah 引擎团队
**一句话定义**：网易在伏羲实验室（AI Lab）+ 自研引擎（NeoX/Messiah）双轨建立"AI in-editor"能力，以《逆水寒》《永劫无间》《一梦江湖》《光遇》等产品为试验田。

**关键信息**：
- 伏羲 Lab：2017 年成立，定位"游戏中的 AI"，发表过 NPC AI / 美术风格迁移 / 关卡程序生成等论文
- NeoX 引擎：网易自研，《逆水寒》《一梦江湖》《天谕》《忘川风华录》等使用
- Messiah 引擎：《永劫无间》使用，已对外授权部分能力
- 公开 case：《逆水寒》"智能 NPC"（GPT 接入 NPC 对话），2023 引发讨论
- 美术 AI：网易内部公开过原画风格迁移 / 一致性生成工具
- 学术输出：SIGGRAPH / NeurIPS / GDC / ChinaJoy 论文与演讲级别证据
- 商业化路径：内部使用为主，部分能力以 SaaS / API 形式对外（伏羲游戏 AI 平台）

**起手 URL**：
- 网易伏羲：https://fuxi.163.com/
- 网易雷火（NeoX）：https://leihuo.163.com/
- 《逆水寒》智能 NPC 公开报道（2023-2024）
- SIGGRAPH 网易 paper / GDC 网易 session（待 routine 自查）

**研究角度**：
- 网易"伏羲 + NeoX/Messiah"的工具链是真整合还是 PR
- 《逆水寒》智能 NPC 在生产环境的实际可用性（vs demo），玩家长期接受度
- 网易 vs 腾讯 vs 米哈游 三家"AI in-editor"路线的差异
- Messiah 引擎对外授权 + AI 工具链是否一并打包，与 Unreal 在中国市场的竞争

**重要差异化**：本篇**聚焦 NeoX/Messiah 编辑器侧 AI 工具**，不深入伏羲 Lab 的纯学术 paper（如纯 NLP / RL 论文），重点关注与编辑器内开发者工作流相关的 in-editor copilot 部分，并与 #4 GiiNEX 对照"中国大厂自研引擎 + AI 工具"的路径差异。

---

## ⭐ 6. 米哈游 自研引擎 AI tooling（BJ 18:00 / UTC 2026-05-09T10:00:00Z）

**类型**：产品（封闭自研 toolchain + 内部 AI tooling，公开度最低）
**主体**：米哈游（HoYoverse / Cognosphere）
**一句话定义**：米哈游不公开命名引擎，但《原神》《崩坏：星穹铁道》《绝区零》《崩坏3》共享一套以 Unity 为基础高度定制的内部 toolchain，AI tooling 嵌在其中——公开资料极少，需基于公开演讲 / 招聘 JD / 业内访谈 + 论文发表推断。

**关键信息**：
- 引擎基础：Unity HDRP / URP 高度定制，不像网易腾讯从零自研引擎
- 公开 AI 工具线索：HoYoLab 美术 AI 工具、AI 检索式 QA tooling 在 ChinaJoy / Unite 演讲提及过
- 米哈游 Cognosphere 是海外子公司，研发主力仍在上海
- 招聘 JD 透露：AI 美术（一致性生成 / 风格化）/ AI QA（自动化游戏测试）/ AI NPC（部分 demo）三条线
- 米哈游 IP 商业模型 vs 工具开放化：高度封闭，AI 工具几乎不外售，与腾讯网易"对外授权"路线相反
- 与腾讯网易最大差异：米哈游基于 Unity，AI 工具是 Unity 之上的 layer，理论上可受 Unity Muse 影响
- 米哈游研究院 SIGGRAPH / Eurographics 论文（如风格化渲染、动画方向）

**起手 URL**：
- 米哈游官网：https://www.mihoyo.com/
- HoYoverse：https://www.hoyoverse.com/
- Unite Shanghai 米哈游 session / GDC 米哈游 talks（待 routine 自查）
- 米哈游招聘 JD（boss 直聘 / 拉勾 / LinkedIn）+ SIGGRAPH 米哈游 paper

**研究角度**：
- 米哈游用 Unity 而非自研引擎对 AI 工具策略的根本影响
- 米哈游 in-editor AI 与外部 Unity Muse 的关系（自家 layer + Muse 共用？或排斥 Muse）
- 米哈游一致性美术 AI 是核心竞争力还是辅助生产
- 国内三大厂（米哈游 / 腾讯 / 网易）AI 工具路径差异的战略含义

**重要差异化**：公开资料有限，prompt 必须强调"已知 vs 推测"边界——不能根据招聘 JD 单方信息断言产品形态，所有"我们听说"型证据要标注来源 + 不确定度。Phase 4 三视角投票里特别要求 Munger 的 "Show me the evidence" 立场，明确划界哪些是确证哪些是合理推测。

---

## ⭐ 7. Godot 4 + AI 插件生态（BJ 19:00 / UTC 2026-05-09T11:00:00Z）

**类型**：产品（开源引擎 + 社区主导 AI 插件生态）
**主体**：Godot Foundation + 社区开发者
**一句话定义**：Godot 4.x 第一方对 AI 抱保守立场（不像 Unity Muse 那样品牌包装），AI 能力主要靠社区 plugin——但作为"开源引擎对 AI 工具化的态度"是关键参照锚。

**关键信息**：
- Godot Foundation 立场：对 AI 工具不排斥但不推动，保持引擎核心精简
- 社区 plugin 头部：Godot AI Studio、EditorAI、LLM Helper、Godot OpenAI integration
- 与 GDScript / C# 的集成路径：plugin 通常以 EditorPlugin 形式注入 IDE
- 商业模式：开源免费，社区 plugin 多数也免费
- 2024-2025 Godot 4.3 / 4.4 对 AI 的官方表态
- Godot 在 indie / educational 市场的渗透 vs Unity 的份额
- Godot 离开 Unity 浪潮（2023 Unity Runtime Fee 风波）后用户增长
- Godot AssetLib 上 AI 相关 plugin 的下载与维护活跃度

**起手 URL**：
- Godot 官网：https://godotengine.org/
- Godot Asset Library：https://godotengine.org/asset-library/asset
- Godot Foundation AI 政策表态（GitHub issue / proposal / blog）
- 头部 AI plugin GitHub repos（搜 Godot + AI / LLM / Editor）

**研究角度**：
- 开源引擎为什么对 AI 工具集成保守（社区治理 / IP 担忧 / 资源限制）
- Godot 社区 AI plugin 生态健康度（活跃 contributor / 维护频率）
- Godot 是不是会成为"AI 工具友好但不主推"的清流派
- Indie / educational market 对 in-editor AI 的需求强度，与 Roblox Studio AI 的端用户对照

---

## ⭐ 8. Cocos Creator + CocosAI（BJ 20:00 / UTC 2026-05-09T12:00:00Z）

**类型**：产品（国产手游 / Web 跨端引擎 + AI 工具链）
**主体**：Cocos（雅基软件）
**一句话定义**：Cocos Creator 是国产手游 / 小游戏 / Web 游戏头部引擎，2024 起推 CocosAI 服务（含 AI 美术、AI 编程辅助、AI runtime ML），定位"中国本土 Unity Muse"。

**关键信息**：
- Cocos Creator 3.x：跨端（iOS / Android / Web / 小程序 / 主机）引擎
- CocosAI Cloud（2024）：text-to-image / text-to-3D / 美术风格化 一站式 API
- 小程序 / 微信生态深度集成是 Cocos 的差异化护城河
- 中国手游 / 小游戏头部市占率（vs Unity 中国版团结引擎）
- 与 Unity 中国版（团结引擎）的关系：直接竞争 + 局部互补
- Cocos Lite + Cocos Service 的开发者服务平台
- Cocos 国际化：日韩 / 东南亚的进展

**起手 URL**：
- Cocos 官网：https://www.cocos.com/
- CocosAI 服务页：https://www.cocos.com/cocos-ai
- Cocos 开发者大会 2024 keynote
- 国内小游戏 / 手游使用 Cocos 的产品案例（搜 ChinaJoy / 微信小游戏 top）

**研究角度**：
- Cocos 的"区域市场 moat"（中国手游 / 小游戏）能否在 AI 时代延续
- CocosAI 作为本土 Muse 平替的差异化（价格 / 中文支持 / 接入门槛）
- Cocos vs Unity 中国版（团结引擎）在 AI 工具上的竞争走向
- 小程序 / 微信生态对 in-editor AI 的特殊需求（包大小 / 审核 / 性能）

**重要差异化**：本篇**聚焦中国本土手游 / 小游戏 / Web 引擎语境**，不要套美式 SaaS 商业模型，要理解中国开发者对 in-editor AI 工具的实际接受度与付费习惯，并与 #1 Unity Muse 形成全球巨头 vs 中国本土 对照。

---

## ⭐ 9. Ubisoft La Forge + EA SEED/Frostbite AI tooling（BJ 21:00 / UTC 2026-05-09T13:00:00Z）

**类型**：产品（西方 AAA 自研引擎 + 内部 AI 实验室双对比）
**主体**：Ubisoft La Forge AI Lab + Electronic Arts SEED Lab + Frostbite 引擎团队
**一句话定义**：西方两大 AAA 厂商各自的内部 AI 工具线——Ubisoft La Forge 偏 R&D 学术输出，EA SEED 偏前沿 demo，二者都不像 Unity/Roblox 那样 productize，但作为"闭源 AAA 自研引擎 + AI"的代表性样本。

**关键信息**：
- Ubisoft La Forge：2017 年蒙特利尔成立，与 McGill / 满地可学界深度合作；公开 paper 涵盖动捕 AI、PCG、QA 自动化
- EA SEED（Search for Extraordinary Experiences Division）：EA 前沿研究部门，《战地》《FIFA》《极品飞车》等基于 Frostbite 引擎
- Frostbite 引擎：EA 内部使用，封闭程度高；AI 工具不外售
- Ubisoft Snowdrop / Anvil 引擎：La Forge 部分成果落地《刺客信条》《全境封锁》生产管线
- 公开 demo：La Forge 的 ZooBuilder（动物 AI 动画）、SEED 的 Halcyon 渲染器、Project Halcyon、PICA PICA 等
- 与中国闭源大厂（腾讯 / 网易 / 米哈游）的对照锚
- Ubisoft 曾推出 Ghostwriter（NPC 台词 AI 生成工具）的公开 case

**起手 URL**：
- Ubisoft La Forge：https://www.ubisoft.com/en-us/studios/montreal/la-forge
- EA SEED：https://www.ea.com/seed
- La Forge 论文与项目列表：https://www.ubisoft.com/en-us/studios/montreal/la-forge/research-publications
- SIGGRAPH / GDC La Forge / SEED 演讲

**研究角度**：
- 西方 AAA 闭源派 vs 中国闭源大厂派的 AI 工具差异（学术开源 vs PR demo vs 生产落地）
- 为什么西方大厂不做 productize（生态 / 商业模型 / 工具复杂度 / 反垄断风险）
- Ubisoft La Forge / EA SEED 的工具是否真的进入生产管线（vs 学术 paper）
- 9-piece mosaic 里西方 AAA 自研派与平台开放派、中国闭源大厂派、开源/区域派的优劣对比

**重要差异化**：本篇是 9-piece mosaic 的最后一块，Phase 4 必须做**全 9 对象的四派坐标合集回顾**——本对象（西方 AAA 闭源派）的位置 + 与平台开放派、中国闭源大厂派、开源/区域派的优劣对比，给读者一个"who wins which moat"的总结判断。
