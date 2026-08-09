# Enterprise Math / 进取数论分支迁移与研究连续性地图

状态：`ACTIVE MIGRATION PLAN / NON-DESTRUCTIVE`  
快照日期：`2026-08-09`  
架构分支基线：`main@9fe0eb4b9a5a635a029ca5c0d0b5211280aa0c2c`

## 1. 目的

本次迁移改变的是**未来研究应该在哪里继续**，而不是改写“以前研究在哪里发生”。

本方案不删除、不 force-move、不重写任何现有研究分支。新 continuation branch 从旧 head 原样建立，只表示未来研究归属发生了 namespace 迁移；旧 branch 继续作为可审计的 provenance 对象存在。

由于若干长分支已经与当前 `main` 高度分叉，这些 continuation branch **不应整条直接并入 main**。未来规范集成必须从最新 main 建立 clean integration branch，对已筛选的成果做 semantic replay。

## 2. 本次已经完成的精确分支迁移

### 2.1 原 P019 minimum-precision geometry / relation 混合分支

历史混合分支：

`research/p019-minimum-precision-lattice-geometry`

本次迁移读取到的仓库 branch head：

`6b0a6160ed96d397c84bcb03926e5267256dfa99`

该分支同时包含几何专属研究以及后来长出的更一般 relation/partition 理论。因此未来必须按**研究归属**分开，但共享历史不删除。

已经在同一个精确 head 上建立两个 continuation branch：

- `research/core/relation-quotient` @ `6b0a6160ed96d397c84bcb03926e5267256dfa99`
- `research/p022-minimum-precision-geometry` @ `6b0a6160ed96d397c84bcb03926e5267256dfa99`

#### 以下研究在 `research/core/relation-quotient` 继续

- capacity-weighted relation state `(m,C,Z)`；
- 任意 partition quotient `Q_A`；
- partition kernel `K_A` 以及 invisible-motion / state-fiber 的同一性；
- relation rank 与 relation scale；
- exact refinement memory / Refinement Forest 作为 present-state reconstruction 工具；
- 不依赖具体几何的 relation observations；
- 一般 witness/value/provenance 区别；
- 与 E001 admissible-support relations 的比较与合流；
- 针对给定未来 operation language，求最小 exact relation state。

此处**暂时不要新增 P 编号**。先把数学接口、最弱假设和 prior-art boundary 提炼清楚。

#### 以下研究在 `research/p022-minimum-precision-geometry` 继续

- `A_p`、FCC/HCP/BCC 或其他 lattice candidates；
- primitive graph distance 和几何专属 shortest-path 结构；
- finite balls/shells 与 coordinator counts；
- radial/quadratic distance observations 与 triangle/distance carry；
- spherical excavation 作为几何定理本身；
- isotropy/anisotropy 检验和几何专属反例；
- geometry-aware collapse。

P022 正式提升前，只把真正属于 geometry 的成果 semantic replay 到最新 main，并把历史 `P019_*` 文件重命名为规范 `P022_*`。禁止把整个混合历史分支直接并入主干。

### 2.2 P019 relation checkpoint 历史

此前暂停时创建的 checkpoint 保持不变：

- `checkpoint/p019-relation-quotient-20260809-0914` @ `1bc0e4a3e96833a553bc52dc51ea88483bedf486`
- `research/p019-relation-quotient-continuation` @ `1bc0e4a3e96833a553bc52dc51ea88483bedf486`

该 checkpoint 之后，原混合分支又继续推进到 `6b0a616...`。所以这两个 `1bc0e4a...` ref 是**历史审计锚**，不是当前研究前沿。不能为了“看起来整齐”而 force-update 它们，把这段推进历史抹掉。

### 2.3 历史 P019 黑洞分支 → P021

历史分支：

`research/p019-discrete-black-hole-horizon`

读取到的 head：

`e8d176b30e7e52ca75b2ae9467066ea4f8f5af6c`

已经在同一精确 head 上建立新续研分支：

`research/p021-causal-focusing` @ `e8d176b30e7e52ca75b2ae9467066ea4f8f5af6c`

以后 P021 研究在新分支继续。必须保留：

- causal boundary/horizon 构造；
- future-section expansion 与 focusing spectra；
- direction orbit 与 causal role；
- witness-level direction transport；
- 已经证明的“count/cardinality shadow 不等于未来精确复合所需 identity”边界。

如果某个陈述可以脱离物理解释，成为一般 quotient / witness-sufficiency 定理，则把母定理向上提炼到 A2/P023 或 relation core；P021 保留 direction/causal 特化。

物理主张继续位于数学模型下游，并受 P016 falsification contract 约束。

### 2.4 E001 工程分支 → 分离一般 relation 续研路线

当前 E001 分支：

`agent/e001-multires-collision`

读取到的 head：

`6e2dc72e46885c081278228838831cd87eb8167c`

该分支最初只是工程 collision pressure test，但后来同时长出了可复用数学：admissible support relation、common-target composition、relation spectra、support precision、以及 functional collapse 模型表达能力的边界。

已经在同一精确 head 上建立一般数学 continuation：

`research/core/admissible-support-relations` @ `6e2dc72e46885c081278228838831cd87eb8167c`

#### 以下内容继续在 `agent/e001-multires-collision`

- collision engine 实现；
- broad phase 与 adaptive refinement schedule；
- terminal oracle 对照；
- workload / CPU / materialization benchmark；
- 工程 certificate、失败分析与性能分析。

#### 以下内容继续在 `research/core/admissible-support-relations`

- functional collapse 与 relational collapse 的区别；
- radius-indexed admissible relation family；
- common-target relation composition；
- split-completeness 与 atomic counterexample；
- MAY/MUST support semantics，作为 P018 precision 的 relation 输入；
- `W_k` witness spectrum 与 `G_k` group/event spectrum；
- total function graph 下 `W_k=G_k=J_k` 的退化定理；
- pair graph 无法恢复的 higher-order common-target structure；
- 防止任意 support-intersection graph 变成“万能本体”的 admissibility constraints。

两个分支在 split point 以前共享全部历史。split 以后，一般定理应先在 core branch 中发展，再由 E001 消费，不能各自复制成两套实现和两套术语。

## 3. 这次刻意不改名的活跃路线

### 3.1 P018

当前活跃路线继续保持：

`agent/p018-critical-grid` / PR #68；其记录的 verified research head 为 `948e2dd452ccbd3e33e81586f566715c094f5551`。

P018 继续拥有 precision interpretation、pair/kernel precision structure、defect/response、precision-time filtration 和 precision-specific dynamic closure。

以后如果准备再加入一个“一般 predictive closure”定理，必须先和 P023 逐条比对。若 P023 已经给出严格更一般的 operation-language 陈述，P018 只增加 precision specialization/corollary。

### 3.2 P023

当前分支继续保持：

`research/p023-composition-safe-collapse`

PR 记录的 head：

`3601235fd87cc8dcb961599155ff9500a4e67d52`

这个名称已经符合它正在形成的通用职责：future-compatible quotient、factorization/congruence、minimal repair、operation-family closure。它要进入规范主干仍然必须独立完成最新 main semantic replay 和全部 gates。

### 3.3 P017

P017 继续作为压力测试项目，已接受成果按小步 integration 进入 main。本次不批量改名现有 `agent/p017-*`、`agent/legendre-*`、`integration/p017-*` 分支。

以后 P017 遵循：

- square-basin 专属约束继续归 P017；
- 一旦发现 prime/Legendre 假设可以删除，就把一般定理提升到相应 reusable home；
- 一旦证明两个 P017 路线只是同一对象的不同坐标，就只维护一个规范陈述，另一条降为 representation/corollary；
- 历史 stale PR 只有在 equivalence audit 确认真正独有的数学都已接住以后，才关闭。

### 3.4 规范 P019/P020

规范 `P019` 始终是 collapse-word stabilization；`P020` 始终是 well-founded finite stabilization。本迁移文件中的任何 branch move 都不会改变这两个规范含义。

## 4. 研究员续研表

| 研究主题 | 继续工作的 branch | 紧接着的问题 |
|---|---|---|
| 一般 relation / partition quotient | `research/core/relation-quotient` | 对一个声明好的 future operation/observation language，最小 exact relation state 是什么？ |
| Minimum-precision geometry | `research/p022-minimum-precision-geometry` | 把 relation-generic 工具抽离后，哪些几何结果仍然真正属于 P022？ |
| Causal focusing / 黑洞应用 | `research/p021-causal-focusing` | 加入物理解释以前，哪些 witness identities 是数学上不可删除的？ |
| Admissible supports / common-target relations | `research/core/admissible-support-relations` | 什么样的 generated support axioms 足够强、能产生非平凡定理，同时又不会万能到能表示任何图？ |
| E001 工程 | `agent/e001-multires-collision` | 在不改变精确语义的情况下，结构上减少 exact work 能否稳定转化为实现层性能收益？ |
| P018 precision calculus | `agent/p018-critical-grid` | 与 P023 比较后，剩余哪些结果是真正 precision-specific？ |
| P023 quotient safety | `research/p023-composition-safe-collapse` | 能否用一个干净的一般定理同时覆盖 unary predictive closure、finite operation families 与 minimal repair？ |
| P017 pressure test | 从最新 main 新建当前 P017 research branch | lower-band descent 或 resource coupling 能否给出真正新的 deterministic bound，而不是再一次坐标改写？ |

## 5. 跨分支同步规则

这些长分支之间不要靠反复 wholesale merge 来“同步”。

一个可复用成果应按下面步骤集成：

1. 在真正拥有该定理的 continuation branch 中证明/审计；
2. 记录最初发现该结构的 source branch/commit；
3. 从**最新 main** 新建 clean integration branch；
4. 只 replay 归属定理、可执行规格、测试、双语 prose 与 provenance records；
5. 应用 corollary 单独提交，或至少使用清晰分隔的 commits；
6. 来源 research branch 可以继续保留历史 local numbering 与实验资产。

这样可以避免历史 ledgers 或 stale bilingual manifest 在合并时覆盖并行进入主干的新成果。

## 6. No-delete / no-orphan 保证

只有下列条件全部满足以后，历史 branch 或 open PR 才可以标记 superseded：

- 每个独有 proved statement 都已经有新归属，或者已被明确 counterexample 否定；
- 独有 executable tests/counterexamples 已迁移，或者有明确理由记录为退休；
- prior-art/source lineage 已带过去；
- 旧研究员下一步应该进入哪个 branch 已明确写出；
- 新路线仍能恢复回旧 commit 的 provenance 链。

在此之前，历史分支全部保留。

## 7. 下一轮迁移任务

下一轮架构工作不应继续自动制造更多 branch alias，而应该：

1. 把两个新 relation-core continuation 逐定理比较；
2. 建立统一 concept-lineage matrix，并给每条关系标记 `same / strict generalization / specialization / independent / conflict`；
3. 找到能够从最新 main clean replay 的最小 relation-core integration slice；
4. 只有完成上述审计后，才判断这个可复用 core 应该获得新 numbered problem、保持 non-numbered library module，还是未来进入 `FOUNDATIONS`。
