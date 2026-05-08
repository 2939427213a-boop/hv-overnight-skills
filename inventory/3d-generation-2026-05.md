# 3D 模型生成清单（来源：腾讯 IEG 游戏技术扫描 + world-models batch 2026-05-08 经验）

> 这份清单是 hv-analysis-cloud routine 在云沙箱里的**唯一对象输入**——routine 不能读用户本地的 HTML 源，所有研究对象的最小信息都得在这里给齐。每条 brief 200-500 字，附 2-4 条权威来源 URL 让 routine 起手时不用瞎搜。
>
> 9 个对象都是**今晚批跑的对象**（2026-05-09 北京时间 00:00-08:00 fire），按 fire 顺序排。

---

## ⭐ 1. Tencent Hunyuan3D Studio（BJ 00:00 / UTC 2026-05-08T16:00:00Z）

**类型**：产品（端到端 3D 资产管线）
**主体**：腾讯混元团队
**一句话定义**：腾讯混元 3D 资产线的"工作台"形态，对外宣称 game-ready，是世界模型套件之外的另一条独立轨。

**关键信息**：
- 论文标题直接写 "End-to-End AI Pipeline for **Game-Ready** 3D Asset Generation"，arXiv:2509.12815（2025-09）
- 演进链：Hunyuan3D 2.0（2025-01，arXiv:2501.12202）→ 2.5 → Studio → PolyGen 1.5（2025-07-08，业界第一个艺术级自回归 mesh 模型，端到端生成四边面）
- 双模型管线：Hunyuan3D-DiT（几何）+ Hunyuan3D-Paint（贴图），flow-based DiT
- Hunyuan3D-PolyGen 官方口径：建模时间减少 70%、拓扑整齐度提升 35%
- 开源 + 云端 API 双轨

**起手 URL**：
- GitHub：https://github.com/Tencent/Hunyuan3D
- Hunyuan3D 2.0 paper：https://arxiv.org/abs/2501.12202
- Hunyuan3D Studio paper：https://arxiv.org/abs/2509.12815
- HunyuanWorld（关联 world-models 套件）：https://github.com/Tencent/HunyuanWorld

**研究角度**：
- "Game-Ready" 框架是真整合还是话术
- 自回归 mesh / 四边面拓扑这一跳的工程意义
- IEG 美术管线对接的真实证据（vs 论文 / PR）
- 与 Tripo / Rodin 的横向对比集中在游戏管线落地能力

**重要差异化**：昨晚 `世界模型-HV-2026-05-08` 的 #2 已有「Tencent Hunyuan 套件」综合分析（覆盖 GameCraft + HunyuanWorld + Hunyuan3D Studio 套件级别）。本篇**聚焦 Hunyuan3D 资产线本身**：2.0 → 2.5 → Studio → PolyGen 1.5 的产品演进；只在必要时引用世界模型条线作对照，不要重写套件历史。

---

## ⭐ 2. ByteDance Seed3D 1.0（BJ 01:00 / UTC 2026-05-08T17:00:00Z）

**类型**：产品（单图原生 3D DiT）
**主体**：字节跳动 Seed 团队
**一句话定义**：字节最新的单图原生 3D 生成模型，明确"Embodied AI + 游戏"双路线，可直接进 NVIDIA Isaac Sim 做机器人仿真。

**关键信息**：
- Single-image DiT 架构，原生 3D 潜空间 + 扩散 Transformer
- 与 NVIDIA Isaac Sim 兼容是关键差异点（出生即对接机器人仿真）
- 字节系 3D 历史：MVDream（arXiv:2308.16512，2023-08）是中国厂商在多视图扩散赛道的第一次硬碰硬贡献
- 字节战略：Seedance 2.0（视频）+ Seed3D（3D）+ Seed* 一系列 foundation models

**起手 URL**：
- 字节 Seed 官方：https://seed.bytedance.com/
- MVDream paper：https://arxiv.org/abs/2308.16512
- Seed3D 公开材料（待 routine 自查）

**研究角度**：
- 字节为什么 Isaac Sim 优先（vs Hunyuan3D 的 game-ready）
- 是不是字节走了 Embodied AI 路线让游戏让位——这个判断对腾讯 IEG 的战略含义是什么
- 字节 MVDream 时代的多视图扩散经验如何延续到 Seed3D
- 字节内部 3D 路线（Seed3D）vs 视频路线（Seedance）的资源分配信号

---

## ⭐ 3. Microsoft TRELLIS / TRELLIS.2（BJ 02:00 / UTC 2026-05-08T18:00:00Z）

**类型**：产品 / 学术开源（原生 3D DiT 基础设施）
**主体**：Microsoft Research
**一句话定义**：用 Structured LATent (SLAT) 表示 + Rectified Flow Transformer，把稀疏 3D 网格和密集多视图视觉特征统一到一个潜空间，是被广泛 fine-tune 的开源底座。

**关键信息**：
- TRELLIS：arXiv:2412.01506（2024-12），CVPR 2025 Spotlight，最大 2B 参数
- 数据：Objaverse-XL 等 500K 物体训练
- 输出三种格式：Radiance Fields、3D Gaussians、mesh
- TRELLIS.2：引入 O-Voxel 表示，4B 参数；进一步提升几何质量
- Microsoft Research 在 3D 赛道稳占学术输出位（vs 大厂自家产品化路线）

**起手 URL**：
- TRELLIS paper：https://arxiv.org/abs/2412.01506
- TRELLIS GitHub：https://github.com/microsoft/TRELLIS
- TRELLIS.2 公开材料

**研究角度**：
- 学术开源底座的影响力（被 Tripo / Meshy / Hunyuan3D 等谁 fine-tune 引用了？）
- TRELLIS.2 的 O-Voxel 工程意义
- Microsoft 不出商业 3D 产品但持续放学术论文的战略目的（vs Edify / Hunyuan3D 的产品化）

---

## ⭐ 4. NVIDIA Edify 3D（BJ 03:00 / UTC 2026-05-08T19:00:00Z）

**类型**：产品（合规授权数据 + 商业 API）
**主体**：NVIDIA（与 Shutterstock 合作）
**一句话定义**：与 Shutterstock 合作授权数据训练，定位企业 / 影视，**合规优先**。

**关键信息**：
- 与 Shutterstock 数据合作，是少数明确"训练数据来源合规"的商业 3D 模型
- 企业 / 影视市场，不直接对游戏小工作室
- NVIDIA Cosmos（世界模型）官方表态明确不优先做游戏——Edify 在 3D 上是否一致
- Shutterstock 数据生态被 NVIDIA 拉拢，是行业首例授权数据 3D 模型

**起手 URL**：
- NVIDIA Edify：https://www.nvidia.com/en-us/ai/edify/
- Shutterstock × NVIDIA 合作公告
- NVIDIA Picasso（Edify 母平台）介绍

**研究角度**：
- 训练数据合规性的未来（vs Adobe Firefly 的 Adobe Stock 路径）
- Shutterstock 数据生态被 NVIDIA 拉拢，对 Getty / Adobe 的连锁反应
- 企业合规优先 vs 创业公司"先用数据再说"的两种打法
- Edify 在 NVIDIA 整体 AI 战略里的位置（vs Cosmos 世界模型 / Picasso 平台）

---

## ⭐ 5. Google DeepMind CSM（BJ 04:00 / UTC 2026-05-08T20:00:00Z）

**类型**：产品 + 收购整合（image/text/sketch → game-engine ready）
**主体**：Common Sense Machines → Google DeepMind（2026-01-24 收购）
**一句话定义**：Google 通过收购回到 3D 牌桌——CSM 12-17 人工程团队并入 DeepMind，输出 game-engine ready 资产。

**关键信息**：
- 2026-01-24 Google 收购 CSM 公告，12-17 人团队并入 DeepMind
- CSM 原产品：image / text / sketch → game-engine ready 输出
- Google 在 3D 赛道此前缺位（vs Genie 自研的世界模型路线 / DreamFusion 论文血缘）
- 收购被视为行业整合信号（"AI-acquihire 时代"标志事件之一）

**起手 URL**：
- Google 收购公告：（routine 自查 2026-01-24 前后官方博客）
- CSM 原网站：https://www.csm.ai/
- Google DeepMind 3D 相关材料

**研究角度**：
- 收购整合战略意义：Google 为什么不自研 3D 而走收购？
- CSM 的 game-engine ready 输出能力是真还是宣传
- Google 在 3D 赛道的"通过收购回到牌桌"逻辑（vs Genie 自研的世界模型路线）
- 12-17 人团队规模意味着什么——是 IP / 技术收购还是全栈能力收购

---

## ⭐ 6. VAST / Tripo 3.0 + Tripo Studio（BJ 05:00 / UTC 2026-05-08T21:00:00Z）

**类型**：产品（产品化最彻底的中国独角兽）
**主体**：VAST（北京）
**一句话定义**：累计服务 700+ 企业客户（含腾讯游戏、网易），累计生成 3000 万+ 模型，号称 200B 参数级，"估值和累计融资全球第一"。

**关键信息**：
- 2025-06 Pre-A+ 数千万美元，北京市 AI 产业基金领投
- 2025 推出 Tripo Studio 工作台（不仅是 API，是企业客户工作流）
- 累计 700+ 企业客户：含腾讯游戏、网易（公开披露）
- 累计 3000 万+ 模型生成
- TripoSR（与 Stability AI 联合，arXiv:2403.02151，2024-03）开源 + Tripo 3.0 闭源的双轨

**起手 URL**：
- Tripo 官网：https://www.tripo3d.ai/
- TripoSR paper：https://arxiv.org/abs/2403.02151
- Tripo Studio 介绍页

**研究角度**：
- 中国独角兽全球化路线（vs Meshy 美国 + Sequoia / GGV 的另一种路线）
- 号称 200B 参数级是不是营销（参数级 vs 模型质量的关系）
- Tripo Studio 工作台是否真把企业客户绑死
- 累计 3000 万+ 模型的真实利用率（活跃 vs 一次性试用）
- TripoSR 开源 + Tripo 3.0 闭源的双轨策略

---

## ⭐ 7. Deemos Tech / Rodin Gen-2（BJ 06:00 / UTC 2026-05-08T22:00:00Z）

**类型**：产品（保真度第一档）
**主体**：Deemos Tech（ShanghaiTech 学术背景）
**一句话定义**：BANG 架构，10B 参数，专业创作者市场，业内公认保真度第一档。

**关键信息**：
- BANG 架构（Branch-Aware-Native-Geometry，部分公开）
- 10B 参数，专业向；用户社群对其保真度评价最高
- ShanghaiTech 学术背景
- 部分英文媒体描述其与字节跳动有研究渊源，**但两者并非母子公司关系**——routine 必须澄清这个常见误解
- 具体融资轮次信息暂缺，需 routine 调研

**起手 URL**：
- Rodin 官网：https://hyperhuman.deemos.com/
- Deemos 公开材料
- BANG 架构相关 paper（routine 自查）

**研究角度**：
- BANG 架构的工程创新点
- 保真度第一档的代价（速度、价格、商业化路径）
- 与字节研究渊源的传闻 vs 独立公司事实——澄清行业常见误解
- 专业创作者市场是不是死路（vs Tripo 的企业客户路线 / Meshy 的轻量级路线）

---

## ⭐ 8. Meshy 5（BJ 07:00 / UTC 2026-05-08T23:00:00Z）

**类型**：产品（多范式集成 + UI 友好）
**主体**：Meshy（旧金山）
**一句话定义**：text-to-3D + image-to-3D + texture 多范式集成，业内公认 UI 最友好；3D 打印 + 轻量游戏 + AR 三个非 AAA 渠道渗透最深。

**关键信息**：
- 累计约 $52M 融资（builtinSF / 测评博客来源，需 routine 在 Crunchbase 交叉验证）
- Sequoia / GGV 主要投资方
- 多范式集成：不押注单一技术路线，而是把 LRM / 多视图扩散 / 原生 3D DiT 都集成
- 渗透市场：3D 打印社区 + Roblox / Unity 中小工作室 + AR 创作者
- 不冲 AAA 路线（这是 Meshy 的明确战略选择）

**起手 URL**：
- Meshy 官网：https://www.meshy.ai/
- 测评 / 用户反馈
- 融资来源（builtinSF / Crunchbase 交叉）

**研究角度**：
- UI 友好如何转化为渗透深度
- 3D 打印 + 轻量游戏 + AR 三个非 AAA 渠道的累积是不是更稳的市场
- 为什么 Meshy 不冲 AAA 路线（战略放弃 vs 能力不足）
- 多范式集成 vs 单一技术路线（Tripo / Rodin 押注一种）的工程取舍

---

## ⭐ 9. Adobe Substance 3D + Firefly（BJ 08:00 / UTC 2026-05-09T00:00:00Z）

**类型**：产品（DCC 厂反向 AI 嵌入）
**主体**：Adobe（Substance 3D 套件 + Firefly 模型族）
**一句话定义**：老牌 DCC 厂在材质 / 贴图层面做 AI 嵌入——**不直接生成 mesh**，但进入 IEG 美术管线最深。

**关键信息**：
- Substance 3D 套件：Painter / Sampler / Designer / Stager，已是行业标准
- Firefly 训练数据：Adobe Stock 授权数据，合规护城河
- AI 嵌入位置：Substance Sampler 的图像→材质、Firefly Generative Match、Substance Painter 的 AI 助手
- 不生成 mesh，专攻 PBR / 纹理 / 材质
- 与 Autodesk 系统性收编动捕（在 03_animation 报告里）形成"DCC 双雄反向收编"主题

**起手 URL**：
- Adobe Substance 3D：https://www.adobe.com/products/substance3d.html
- Adobe Firefly：https://www.adobe.com/products/firefly.html
- Substance + AI 公开材料

**研究角度**：
- DCC 厂"加固"vs 创业公司"颠覆"的两种路径
- Substance 3D 在 IEG 美术管线里的既有装机量（材质环节进入 AAA 最深）
- Firefly 训练数据的 Adobe Stock 合规护城河（vs NVIDIA Edify 的 Shutterstock 路径）
- 与 Autodesk 收编动捕（Radical / Wonder Dynamics）形成的 DCC 双雄反向收编主题

**重要差异化（避免错位横向对比）**：
- Substance 3D + Firefly **不直接生成 mesh**，是材质 / 贴图 / PBR / 纹理层的 AI 嵌入。
- 横向对比维度**不**是「产品 A 的 mesh vs 产品 B 的 mesh」，而是 **DCC 工作流里 AI 嵌入的位置 / 深度 / 数据合规**：vs Autodesk 收编路径、vs NVIDIA Edify 数据授权路径、vs 创业公司"颠覆 mesh 生成"路径。
- 重点：Adobe Stock 训练数据的合规护城河、Substance Sampler 的图像→材质路径、IEG 美术管线里 Substance 的既有装机量。

---

## 备料（27 条，今晚不跑，留作后续批次素材）

### 第一梯队补充
- **Meta 3D Gen / AssetGen / TextureGen**（arXiv:2407.02445, 2024-07）：PBR 原生生成，研究项目未产品化
- **Stability AI TripoSR / SF3D**：LRM 衍生开源线
- **Wonder3D / SyncDreamer / Zero123 系列**：多视图扩散学术血缘

### 第二梯队补充
- **Luma Labs Genie**：LRM + 四边面，已边缘化（优先级让位 Dream Machine）
- **Kaedim**：2023 The Verge 信任危机案例，反面教材
- **CSM** 已纳入 #5
- **Anything World**：AI 绑骨 / 动画
- **3DFY.ai**：程序化 3D 库
- **Polycam AI**：手机扫描

### 第三梯队 / 周边
- **Sloyd**（参数化程序生成）、**Spline AI**（网页 / UI 3D）、**Masterpiece X**（VR 草模→3D）、**Alpha3D**（电商物品扫描）、**Blockade Labs**（360 Skybox）

### 学术原点
- **DreamFusion**（arXiv:2209.14988, 2022-09）+ Magic3D（arXiv:2211.10440, 2022-11）+ Point-E（arXiv:2212.08751, 2022-12）+ GET3D：四篇 2022 H2 奠基
- **LRM**（arXiv:2311.04400, 2023-11）：把时间从小时压到秒
- **MeshAnything v1 / v2**（arXiv:2406.10163 / arXiv:2408.02555）：自回归 mesh 学术原点（PolyGen 谱系）
- **InstantMesh**（腾讯 arXiv:2404.07191, 2024-04）：多视图 + 稀疏视图 LRM 串联

### 中国厂商补充
- **腾讯 InstantMesh / Hunyuan3D-PolyGen**：自家学术线
- **阿里 3D 系列**：信息密度低，待 routine 调研
- **昆仑万维 Matrix-Zero**：已在 world-models batch（含 3D 场景生成线）

---

## 后续主题研究备选（4-5 小时一份，单 routine 1h 跑不完）

### A. 五跳范式演进史
横向收敛：DreamFusion → MVDream → LRM → TRELLIS / Hunyuan3D-DiT → MeshAnything / PolyGen
关键问题：每一跳为什么不可避免？下一跳会是什么？

### B. 自回归 mesh / 四边面拓扑专题
单主题：MeshAnything v1/v2 + Hunyuan3D-PolyGen 1.5 + 后续工作
关键问题：自回归 mesh 是不是把"AI 3D 进游戏管线"的最后一公里走通的钥匙？

### C. 3D 训练数据合规性专题
横向收敛：NVIDIA Edify (Shutterstock) + Adobe Firefly (Adobe Stock) + Kaedim 信任危机 + 创业公司"先用再说" + 中国厂商不公开数据来源
关键问题：合规护城河会不会吃掉创业公司？数据生态站队会怎么演变？

### D. DCC 双雄反向收编主题
横向收敛：Adobe Substance + Firefly（材质 / 贴图）vs Autodesk 收编 Radical + Wonder Dynamics（动捕）
关键问题：DCC 厂的"加固"vs 创业公司"颠覆"——哪种笑到最后？

---

> *维护说明*：以后用户给新源（HTML / PDF / Notion 页面），把对应对象 brief 加入"备料区"，需要纳入下一批跑的就移到 ⭐ 段。每条 brief 控制在 200-500 字 + 2-4 条起手 URL，不要太长，云端 routine 自己会去 web 调研补全。
