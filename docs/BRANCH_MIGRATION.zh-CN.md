# Enterprise Math / 进取数论分支迁移与研究连续性地图

状态：`ACTIVE MIGRATION PLAN / NON-DESTRUCTIVE`  
快照日期：`2026-08-09`  
架构分支基线：`main@9fe0eb4b9a5a635a029ca5c0d0b5211280aa0c2c`

## 1. 目的

本次迁移改变的是**未来研究应该在哪里继续**，而不是改写“以前研究在哪里发生”。

本方案不删除、不 force-move、不重写任何现有研究分支。新 continuation branch 从旧 head 原样建立，只表示未来研究有了新的归属；旧 branch 继续作为可审计的 provenance 对象存在。

由于若干长分支已经与当前 `main` 高度分叉，这些 continuation branch **不应整条直接并入 main**。未来规范集成必须从最新 main 建立 clean integration branch，对已筛选的成果做 semantic replay。

continuation branch 在拆分以后可以继续向前，而另一个 branch 可以有意停留在共同 split point。因此本地图同时记录**拆分 commit**与**当前研究 frontier**。

## 2. 本次已经完成的精确分支迁移与当前 frontier

### 2.1 原 P019 minimum-precision geometry / relation 混合分支

历史混合分支：

`research/p019-minimum-precision-lattice-geometry`

建立新归属时使用的共同 split commit：

`6b0a6160ed96d397c84bcb03926e5267256dfa99`

当时从同一个精确状态建立了两个 continuation branch：

- `research/core/relation-quotient`
- `research/p022-minimum-precision-geometry`

拆分以后立刻出现了一次真实的“归属测试”：历史混合分支又新增了三个提交，内容是 observation-aware minimum exact relation precision、relation-rank cost、operation/observation language refinement，没有新增 lattice geometry。因此这三个提交只被分流到 relation-state continuation，没有复制给 P022。

本快照下的当前 frontier：

- 历史混合分支：`research/p019-minimum-precision-lattice-geometry@3caa6a1cf8562747b12a808d1c2ade333280083d`
- A3 relation-state continuation：`research/core/relation-quotient@3caa6a1cf8562747b12a808d1c2ade333280083d`
- P022 geometry continuation：`research/p022-minimum-precision-geometry@6b0a6160ed96d397c84bcb03926e5267256dfa99`

这是本次迁移后第一个按照**数学归属**分流新增成果、而不是向两个后继分支同时复制的实例。

#### A3 工作继续在 `research/core/relation-quotient`

这一条路线的核心对象是 structured weighted integer relation-state，而不是一般 binary support relation。

以下内容在这里继续：

- capacity-weighted relation state `(m,C,Z)`，其中 `Z_ij=m_j c_i-m_i c_j`；
- 任意 partition quotient `Q_A` 与 `Z'=AZA^T`；
- partition kernel `K_A`、invisible-motion / state-fiber 同一性；
- relation rank、relation-scale quantum 与精确 refinement cost；
- exact present-state refinement data / Refinement Forest；
- 定义在 structured relation state 上的 linear operation / observation languages；
- coarsest observation refinement 与 stable-dynamics refinement；
- 给定 future task 所要求的 minimum exact relation precision；
- 作为 structured specialization 与 P018/P023 future-compatible quotient 做精确比较；
- 对 A4 提出明确 bridge questions，但不预设两个 relation 对象相同。

这里**暂时不要新增 P 编号**。先提炼数学接口、bridge hypotheses 与 prior-art boundary。

#### Geometry-owned 工作继续在 `research/p022-minimum-precision-geometry`

以下内容在这里继续：

- `A_p`、FCC/HCP/BCC 或其他 lattice candidates；
- primitive graph distance 与几何专属 shortest paths；
- finite balls/shells 与 coordinator counts；
- radial/quadratic distance observations 与 triangle/distance carry；
- spherical excavation 作为几何定理；
- isotropy/anisotropy tests 与几何专属 counterexamples；
- geometry-aware collapse。

P022 正式提升前，只把真正属于 geometry 的结果 semantic replay 到最新 main，并把历史 `P019_*` 资产重命名为规范 `P022_*`。不能把整个混合历史分支 wholesale merge 到主干。

### 2.2 P019 relation checkpoint 历史

此前暂停时创建的 checkpoint 保持不变：

- `checkpoint/p019-relation-quotient-20260809-0914@1bc0e4a3e96833a553bc52dc51ea88483bedf486`
- `research/p019-relation-quotient-continuation@1bc0e4a3e96833a553bc52dc51ea88483bedf486`

原混合分支后来先推进到 `6b0a616...`，再推进到 `3caa6a1...`。所以这两个 `1bc0e4a...` ref 是**历史审计锚**，不是当前研究前沿。不能 force-update 它们来掩盖中间发生过的研究推进。

### 2.3 历史 P019 黑洞分支 → P021

历史分支：

`research/p019-discrete-black-hole-horizon`

迁移 head：

`e8d176b30e7e52ca75b2ae9467066ea4f8f5af6c`

新 continuation：

`research/p021-causal-focusing@e8d176b30e7e52ca75b2ae9467066ea4f8f5af6c`

以后 P021 工作在新分支继续。必须保留：

- causal boundary/horizon constructions；
- future-section expansion 与 focusing spectra；
- direction orbits 与 causal roles；
- witness-level direction transport；
- 已经证明的 cardinality shadow 与未来精确 composition 所需 identity 之间的区别。

如果某个陈述已经脱离 causal/physical interpretation，成为一般 quotient 或 witness-sufficiency theorem，先与 A2/P023 比较，不能再建立一套平行一般理论。P021 保留 direction/causal applications 与发现 provenance。

物理主张继续位于数学模型下游，并受 P016 falsification requirements 约束。

### 2.4 E001 工程分支 → A4 admissible-support continuation

本快照下 E001 branch 及 split/current head：

`agent/e001-multires-collision@6e2dc72e46885c081278228838831cd87eb8167c`

A4 continuation 从同一精确状态建立，目前也仍在：

`research/core/admissible-support-relations@6e2dc72e46885c081278228838831cd87eb8167c`

E001 分支里已经包含两类不同资产，未来归属不同。

#### 以下内容继续在 `agent/e001-multires-collision`

- collision engine implementation；
- broad phase 与 adaptive refinement schedule；
- terminal oracle comparison；
- workload/CPU/materialization benchmarks；
- engineering certificates、negative results 与 performance analysis。

#### A4 工作继续在 `research/core/admissible-support-relations`

这一条路线的核心对象是有限多值 support/correspondence `R⊆X×Z`，不是 A3 structured integer field。

以下内容在这里继续：

- functional collapse 与 relational collapse；
- radius-indexed admissible support families `R_r`；
- relation composition 与 common-target relations；
- relational subadditivity 与 split-completeness boundary；
- MAY/MUST support semantics，作为 P018 precision 的输入；
- `W_k` witness spectra 与 `G_k` group/event spectra；
- total function graph 下精确的 `W_k=G_k=J_k` degeneration；
- pair graph 无法恢复的 higher-order common-target structure；
- 防止 unconstrained universal support graphs 的 admissibility constraints；
- 只有在明确 generator/factorization 被证明以后，才建立与 A3 的 bridge theorem。

两个分支在 split point 以前共享历史。split 以后，一般 A4 theorem 应在 A4 branch 发展，再由 E001 消费，不能在 engineering modules 中复制一份理论。

### 2.5 A3 与 A4 禁止无证明重新合并

本轮架构审计已经确认，“relation”在 A3 与 A4 中表示两个不同对象：

- A3：与 capacities/totals 和 partition quotient 配套的 structured weighted integer relation-state `Z_ij=m_jc_i-m_ic_j`；
- A4：描述 allowed target states 的有限 binary support/correspondence `R⊆X×Z`。

当前关系是 `COMPOSABLE_INDEPENDENT`，不是一个已经统一的 relation theory。桥梁必须是定理，不能是命名决定。

## 3. 本次刻意不改名的活跃路线

### 3.1 P018

当前活跃路线继续保持：

`agent/p018-critical-grid@948e2dd452ccbd3e33e81586f566715c094f5551` / PR #68。

P018 继续拥有 precision interpretation、pair/kernel precision structure、defect/response、precision-time filtration 与 precision-specific dynamic closure。

定理级审计现在给出了更强的去重规则：

- P018 T160–T168 与 P023 T03–T07 是同一个 finite-unary mother theorem family；
- P023 T10–T14 是 finite operation-family strict generalization；
- 未来一般 extensions 通过 P023/A2 继续；
- P018 只新增 precision-specific consequences 与 applications。

### 3.2 P023

当前分支保持：

`research/p023-composition-safe-collapse@3601235fd87cc8dcb961599155ff9500a4e67d52`

P023 继续作为 future-compatible quotient、factorization/congruence、operation-family closure 与 minimal repair 的候选一般归属。它的 one-step/minimal-repair 路线与 predictive closure 相关，但不是同一个问题。

进入规范主干前仍必须完成 latest-main clean replay 与普通仓库 gates。

### 3.3 P017

P017 继续作为 pressure-test program，已经接受的成果按小步 integration 进入 main。本次不批量改名 `agent/p017-*`、`agent/legendre-*`、`integration/p017-*` 历史。

以后遵循：

- square-basin/least-factor/resource-specific constraints 继续归 P017；
- 证明允许时移除 prime/Legendre 假设并把 mother theorem 向上提炼；
- 一旦证明两条路线只是同一对象的不同坐标，只维护一个 canonical statement，另一条保留为 representation/corollary；
- historical stale PR 只有在 equivalence audit 确保所有独有数学已被接住以后才关闭。

### 3.4 规范 P019/P020

规范 `P019` 始终是 collapse-word stabilization；`P020` 始终是 well-founded finite stabilization。历史 `P019_*` geometry/relation 文件只属于命名碰撞，不获得规范 P019 的 theorem ownership。

## 4. 研究员续研表

| 研究主题 | 继续工作的 branch | 紧接着的问题 |
|---|---|---|
| A3 structured relation-state / partition quotient | `research/core/relation-quotient` | 证明 A3 task-derived linear relation precision 到一般 A2/P023 future-compatible quotient language 的精确 bridge；然后检验哪些 A4 support query 可以 factor through 它。 |
| P022 minimum-precision geometry | `research/p022-minimum-precision-geometry` | 从 split point clean replay geometry-only theorem stack，并明确去掉所有 A3-generic machinery 后还剩哪些真正的 radial/distance 几何结果。 |
| P021 causal focusing / 黑洞应用 | `research/p021-causal-focusing` | 在增加物理解释以前，把 causal/direction-specific witness identities 与已经一般化的 P023 quotient-sufficiency rule 分开。 |
| A4 admissible supports / common-target correspondence | `research/core/admissible-support-relations` | 寻找非平凡 admissibility axioms，并精确判断哪些 A4 observables 由 geometry 生成，或能 factor through A3 state。 |
| E001 engineering | `agent/e001-multires-collision` | 在不改变精确语义的情况下，判断 reduced exact work 是否能稳定转化为实现层性能收益；保留负 benchmark 证据。 |
| P018 precision calculus | `agent/p018-critical-grid` | 停止重复 unary closure mother theorem；围绕 P023 一般 core 继续推进 precision-specific kernel/time/defect/repair consequences。 |
| P023 quotient safety | `research/p023-composition-safe-collapse` | 合并 unary duplicate，把 operation-family closure 保留为一般推广，并继续 minimal-repair / arithmetic sufficiency 研究。 |
| P017 pressure test | 从 latest main 新建当前 P017 branch | 寻找真正新的 deterministic lower-band/resource coupling，而不是新的坐标改写。 |

## 5. 跨分支同步规则

长分支之间不要靠反复 wholesale merge 来“同步”。

一个可复用成果应按下面步骤集成：

1. 在真正拥有该 theorem 的 continuation branch 中证明/审计；
2. 记录最初暴露该结构的 source branch/commit；
3. 先将它与既有定理分类为 `same`、`strict generalization`、`specialization`、`independent` 或 `conflict`；
4. 从**latest main** 新建 clean integration branch；
5. 只 replay mother theorem、executable specification、tests、双语 prose 与 provenance records；
6. application corollaries 单独提交，或至少使用清晰分隔的 commits；
7. 来源 research branch 可以继续保留历史 local numbering 与 experiments。

这样可以防止 stale ledger / manifest 覆盖并行进入主干的新成果。

## 6. No-delete / no-orphan 保证

只有下列条件全部满足以后，historical branch 或 open PR 才可以标记 superseded：

- 每个 unique proved statement 都已有新 owner，或者已被 explicit counterexample 否定；
- unique executable tests/counterexamples 已保留，或者有记录清楚的退休理由；
- prior-art/source lineage 已带过去；
- 旧研究员下一步应进入的 branch 已明确写出；
- 新路线仍可恢复回旧 commit 的 provenance 链。

在此之前，历史分支全部保留。

## 7. 下一轮迁移任务

定理级 concept-lineage matrix 已经建立在 `docs/CONCEPT_LINEAGE.*`。因此下一轮工作不再是“比较两个 relation core 并把它们合并”。审计已经证明它们不同。

下一步是：

1. 正式化 A3→A2/P023 specialization bridge；
2. 在不预设等价的前提下寻找受限 A3↔A4 bridge theorem；
3. 提炼独立于历史 P019/P022 命名的最小 clean A3 integration slice；
4. 提炼独立于 E001 engineering 的最小 clean A4 integration slice；
5. 等这些 reusable dependencies 清楚以后，再 replay P022 与 P021；
6. 只有这些 slices 通过 prior-art 与 integration review 后，才决定是否需要新 numbered problem 或 `FOUNDATIONS` 身份。
