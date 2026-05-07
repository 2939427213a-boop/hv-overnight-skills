# 世界模型清单（来源：腾讯 IEG 游戏技术扫描 2026-04-19）

> 这份清单是 hv-analysis-cloud routine 在云沙箱里的**唯一对象输入**——routine 不能读用户本地的 HTML 源，所有研究对象的最小信息都得在这里给齐。每条 brief 200-500 字，附几条权威来源 URL 让 routine 起手时不用瞎搜。
>
> 8 个 Top 候选打 ⭐⭐⭐ 标记，是今晚批跑的对象。其余 27 条留作后续批次或主题研究的备料。

---

## ⭐⭐⭐ Top 8（今晚批跑）

### 1. World Labs / Marble

**类型**：产品（3D 世界生成）
**创始人**：Fei-Fei Li（前 Google AI 首席科学家、ImageNet 之母、斯坦福 HAI 联合主任）
**一句话定义**：把文字或图片输入生成可下载的 3D 环境，导出 Unity / Three.js / USDZ 工程而不是像素流。

**关键信息**：
- 2024-09 种子轮 $230M，估值 $10B；投资人 a16z + NEA + Marc Benioff + Geoffrey Hinton
- 2026-02 又一轮 $1B，加入 AMD / Autodesk / NVIDIA / Fidelity
- Marble 产品形态：每个世界 ~100MB 可下载，含 Chisel 编辑器（box 区域 + 文字 prompt 风格）
- 定价：免费（4 次）/ $20 / $35 / $95 月度
- Vision Pro / Quest 3 兼容
- 局限：只输出环境几何，没角色 rig / 骨骼 / 动画

**起手 URL**：
- 官网：https://www.worldlabs.ai/
- Marble 介绍：https://www.worldlabs.ai/blog/marble-world-model-3d-environments
- a16z 投资 announcement：https://a16z.com/announcement/

**研究角度**：可导出 vs 像素流的根本路线差异；游戏管线"环境生成"环节的真正可用性。

---

### 2. Tencent Hunyuan 套件（GameCraft 1/2 + HunyuanWorld 1.0 + Hunyuan3D Studio）

**类型**：产品套件（双轨布局）
**主体**：腾讯混元团队（IEG 与 PCG 协作）
**一句话定义**：腾讯把"世界模型"+"3D 资产生成"两条轨同时押注，是国内唯一双轨布局的玩家。

**关键产品**：
- **Hunyuan-GameCraft**：arXiv:2506.17201（2025-06），把鼠标/键盘输入统一进 camera 表达空间；100M+ AAA 游戏 clip 训练
- **Hunyuan-GameCraft 2**：arXiv:2511.23429（2025-11），auto-regressive 长视频 + 多 prompt 交互
- **HunyuanWorld-1.0**：2025-07 开源（WAIC 发布），文本/图像 → 可导航 3D 环境
- **Hunyuan3D Studio**：arXiv:2509.12815（2025-09），论文标题直接写 "End-to-End AI Pipeline for **Game-Ready** 3D Asset Generation"——"Game-Ready"是 Tencent 对游戏管线整合的明确信号

**起手 URL**：
- HunyuanWorld：https://github.com/Tencent/HunyuanWorld
- Hunyuan3D：https://github.com/Tencent/Hunyuan3D
- GameCraft 论文：https://arxiv.org/abs/2506.17201

**研究角度**：双轨为什么都做？game-ready 框架是真整合还是市场话术？Tencent 内部哪条管线先落地 AAA。

---

### 3. Decart + Etched / Oasis

**类型**：产品（神经游戏引擎）
**主体**：Decart（软件）+ Etched AI（硬件 ASIC）合作
**一句话定义**：把整个 Minecraft 游戏压进单张 H100 神经网络，浏览器实时可玩——"一个游戏 = 一个神经网络"。

**关键信息**：
- 2024-10-31 demo 上线，单 H100 360p/20fps/47ms per frame
- 79 小时 100 万独立用户
- 商业模式深度依赖 Etched 自家 Sohu Transformer ASIC（推理成本 10x 优势的承诺）—— Sohu 还没大规模商用
- Etched 融资细节稀疏，但 Sohu 是其旗舰产品

**起手 URL**：
- Oasis demo：https://www.oasis.decart.ai/
- Etched Sohu 介绍：https://www.etched.com/
- Decart 公告：https://decart.ai/

**研究角度**：神经游戏引擎是死路还是火种？Sohu ASIC 出货时间表。商业模型靠未问世硬件兜底的风险。

---

### 4. Odyssey Explorer

**类型**：产品（互动流式真实世界）
**创始人**：Oliver Cameron（前 Cruise 自动驾驶高管、Voyage CEO）
**一句话定义**：用自家 360° 背包相机采集真实世界视频训世界模型，对标 Genie / Sora 但走"自有数据 moat"路线。

**关键信息**：
- 2024 种子轮 $27M
- 2024-11 A 轮 $18M
- 2024-12 Pixar 联合创始人 Ed Catmull 加入董事会——电影行业进入互动叙事的关键信号
- 不用公网数据训练，完全自采（vs Genie/Sora 的互联网视频数据）
- 定位：Hollywood 电影美学 + 游戏交互的交汇

**起手 URL**：
- 官网：https://odyssey.systems/
- Catmull 加入：https://odyssey.systems/blog/

**研究角度**：自采数据 moat 在视频生成时代是否真站得住？film + interactive 的市场到底在哪？Catmull 的实际作用是顾问 vs 战略。

---

### 5. Google DeepMind Genie 3 / Project Genie

**类型**：产品/平台（行业最高水位标杆）
**主体**：Google DeepMind
**一句话定义**：从一张图生成可探索的 3D 互动世界，720p/24fps 几分钟一致性，支持"边玩边用文字改世界"——但还不能商用。

**关键信息**：
- Genie 1：arXiv:2402.15391（2024-02），200k 小时无标签 2D 平台游戏视频训练
- Genie 2：2024-12-04 blog，3D + 1 分钟一致性
- Genie 3：2025-08-05 blog，30k+ 小时游戏视频训练，720p/24fps 持续几分钟，支持 "promptable world events"
- Project Genie：2026 早期美国小规模实验性 rollout（Google Ultra 订阅）
- 没有完整技术 report，参数规模未公开
- 实际不能 runtime 用：无确定性、无网络同步、无防作弊

**起手 URL**：
- Genie 3 blog：https://deepmind.google/discover/blog/genie-3-a-new-frontier-for-world-models/
- Project Genie：https://blog.google/technology/google-deepmind/project-genie/
- arXiv Genie 1：https://arxiv.org/abs/2402.15391

**研究角度**：Genie 3 是 demo 还是产品？Project Genie 商业路径在哪？AGI 营销话术 vs 工程现实。

---

### 6. NVIDIA Cosmos（World Foundation Model Platform）

**类型**：产品（平台）
**主体**：NVIDIA
**一句话定义**：通用世界模型平台，主推机器人/自动驾驶/工业仿真，**官方明确不优先做游戏**。

**关键信息**：
- 2025-01 CES 大会发布
- 2025-03 GTC 详细展示
- 三件套架构：Cosmos Predict / Cosmos Reason / Cosmos Transfer
- 训练数据：20M 小时视频
- 定位为通用世界理解平台，下游适配 Tesla/Toyota/Waymo 等
- 不做游戏的官方表态明确

**起手 URL**：
- Cosmos 官网：https://www.nvidia.com/en-us/ai/cosmos/
- 技术博客：https://blogs.nvidia.com/blog/cosmos-world-foundation-models/

**研究角度**：NVIDIA 不做游戏的真实原因（vs 公开理由）；Cosmos 之于机器人 ≈ Tesla 自家芯片之于 FSD 这个类比成不成立；通用平台 vs 垂直产品的护城河。

---

### 7. Sora 2 (OpenAI) vs Yann LeCun 物理批评

**类型**：产品 + 公开争议
**主体**：OpenAI / Sora 团队
**一句话定义**：从 Sora 1 的物理失败（篮球穿过篮筐、玻璃自动复原）到 Sora 2 的修补——"视频生成是不是世界模型"成为 LeCun 与 Altman 公开论战的焦点。

**关键信息**：
- Sora 1：2024-02 技术博客 "Video Generation Models as World Simulators"，引发"理解物理 vs 模仿物理"争议
- Sora 2：2025-09-30 发布，明确修补 Sora 1 的物理失败 case（篮球反弹、cookies 不复原、玻璃不还原）
- LeCun 多次公开批评："会生成视频不等于理解世界"，主张 V-JEPA 而非 diffusion
- OpenAI 商业策略：Sora 走订阅，对 prosumer / 影视市场，**没有进游戏**

**起手 URL**：
- Sora 2 announcement：https://openai.com/index/sora-2/
- Sora 1 技术博客：https://openai.com/index/video-generation-models-as-world-simulators/
- LeCun on V-JEPA：https://ai.meta.com/blog/v-jepa-yann-lecun-ai-model-video-joint-embedding-predictive-architecture/

**研究角度**：Sora 是不是世界模型这件事的语义之争 vs 工程之争；OpenAI 不进游戏的真实理由；V-JEPA 路线是不是真比 diffusion 更接近世界理解。

---

### 8. 昆仑万维 Matrix-Zero

**类型**：产品（3D 场景 + 互动世界）
**主体**：昆仑万维（Kunlun Group）
**一句话定义**：国内除腾讯外，唯一另一家在做"世界模型 + 游戏管线整合"的厂商，但资源体量比腾讯小一个量级。

**关键信息**：
- 产品名 Matrix-Zero
- 主打 3D 场景生成 + 互动世界
- 母公司昆仑万维转型 AI 后的多个尝试之一（同期还有 SkyMusic / 天工大模型 / SkyReels）
- 信息密度比 Tencent 套件低，公开 paper 少
- 战略意义大于技术意义：作为"中国厂商对照组"看 Tencent

**起手 URL**：
- 昆仑万维官方介绍：https://www.kunlun.com/
- 天工/SkyReels 系列 paper（关联）

**研究角度**：小厂打世界模型 game-ready 的可行性；Matrix-Zero vs Hunyuan 套件的资源对比；昆仑万维的 SkyReels 视频生成线和 Matrix-Zero 是同一管线还是分离。

---

## 备料区（27 条，今晚不跑，留作后续批次/主题研究素材）

### 视频生成系（弱游戏相关性）
- **Sora 2**（已纳入 #7）
- **OpenAI Sora**（被 Sora 2 替代）
- **Runway Gen-3 / Gen-4 / Gen-4.5**：影视/特效市场，2024-2025 多次发布
- **Luma Dream Machine**：消费级视频
- **阿里 Wan 2.x**：开源视频生成，HF 趋势榜常客；阿里"开源策略"研究主题
- **字节 Seedance 2.0**：UGC/网红创作
- **快手 Kling O1 / 2.6**：UGC
- **MiniMax Hailuo**：消费视频
- **生数 Vidu Q3**：UGC

### RL 世界模型谱系（学术线）
- **Schmidhuber 1990**：FKI-126-90，"Making the World Differentiable"，理论原点
- **Ha & Schmidhuber 2018**："World Models" (arXiv:1803.10122)，模板论文
- **Dreamer V1**：arXiv:1912.01603 (2019)
- **Dreamer V2**：arXiv:2010.02193 (2020)，离散潜变量、Atari 55 游戏
- **Dreamer V3**：arXiv:2301.04104 (2023)，Minecraft diamond 无演示提取
- **Dreamer 4**：arXiv:2509.24527 (2025-09)，**离线视频训练**——对游戏 NPC 训练有直接落地价值
- **MuZero**：arXiv:1911.08265 (Nature 2020)，决策相关而非感知
- **DIAMOND**：arXiv:2405.12399 (NeurIPS 2024 Spotlight)，CS:GO 神经引擎，**RL world model 与互动神经引擎收敛点**
- **DayDreamer**：arXiv:2206.14176

### 互动/生成神经引擎
- **GameNGen** (Google)：arXiv:2408.14837 (2024-08)，DOOM 实时神经仿真，47ms/frame
- **The Matrix** (阿里 + UHK + UWaterloo)：arXiv:2412.03568 (2024-12)，无限长度 + 帧级实时控制，含 Forza Horizon 5 + Cyberpunk 2077 训练数据
- **UniSim**：arXiv:2310.06114

### 3D 资产生成
- **HunyuanWorld 1.0**（已纳入 #2）
- **Hunyuan3D Studio**（已纳入 #2）
- **World Labs Marble**（已纳入 #1）

### 自动驾驶世界模型（平行宇宙，技术血缘相同）
- **Wayve GAIA / GAIA-2**：arXiv:2503.20523 (2025-03)
- **Waabi Copilot4D**：自动驾驶卡车仿真，2024 B 轮 $200M（NVIDIA + Uber + Volvo）

### 硬件层
- **Etched Sohu Transformer ASIC**：是 Decart Oasis 的硬件依赖，单独看也值得一份分析（候选 #9 替补）

---

## 后续主题研究备选（4-5 小时一份，单 routine 一晚跑不完）

### A. 神经游戏引擎是不是死路？
横向收敛：Oasis (Decart+Etched) + GameNGen (Google) + DIAMOND (CS:GO) + Genie 3。
关键问题：runtime 可用性？硬件 economics？防作弊？商业模式？

### B. 中国厂商世界模型双轨布局对比
横向收敛：腾讯（Hunyuan 套件）+ 阿里（Wan + The Matrix）+ 昆仑万维 (Matrix-Zero) + 字节快手（视频系）。
关键问题：开源策略 vs 闭源；游戏内部使用 vs 外部输出；与海外 Genie / Sora / Marble 的差距。

### C. Dreamer 4 离线训 NPC 路线落地评估
单产品：但需要交叉评估数据可获得性 / 工程复杂度 / 与 Tencent / 网易等大厂内部 NPC 训练 pipeline 的兼容性。
关键问题：玩家录像数据合规性？训出的 NPC 在线服性能？vs 当前 RL/IL pipeline 的真实优势。

### D. AV 世界模型对游戏的启示
横向收敛：Wayve + Waabi + Tesla FSD（最相关）。
关键问题：传感器先验 vs 文本先验；闭环仿真 vs 开环视频生成；同源技术为何在 AV 商业化领先于游戏。

---

> *维护说明*：以后用户给新源（HTML / PDF / Notion 页面），把对应对象 brief 加入"备料区"，需要纳入下一批跑的就移到 Top N 段。每条 brief 控制在 200-500 字 + 2-4 条起手 URL，不要太长，云端 routine 自己会去 web 调研补全。
