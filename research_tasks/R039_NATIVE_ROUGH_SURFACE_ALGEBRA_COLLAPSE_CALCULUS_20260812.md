<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R039-NATIVE-ROUGH-SURFACE-ALGEBRA-COLLAPSE-CALCULUS",
  "title": "R039 Native Rough Surface Algebra and Collapse Calculus",
  "kind": "RESEARCH",
  "owner": "program/p022-geometry-v2",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_GEOMETRY_COLLAPSE",
  "frontier": "Starting from a single FCC/HCP cell and using only native local incidence/contact/stacking relations, build an exact rough-surface/interface calculus before any metricization, radius, equidistance or Euclidean area is introduced; then classify which algebraic collapses of that interface preserve which future surface operations and observables.",
  "next_action": "Freeze a metric-free native interface state, exhaustively enumerate small connected clusters from one cell, derive exact boundary-update laws and minimal-boundary sequences, then construct a quotient/collapse ladder from full interface incidence to local type spectra, frontier-contact profiles and scalar surface counts, with minimal counterexamples for every unsafe collapse.",
  "dependencies": [
    {
      "target": "R038 Driver semantic correction: ROOT_DISTANCE_IS_READOUT_NOT_NATIVE",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "R033 owner head c2aa1758c6cf8f194d8b4493b90c903a2dfcd048",
      "action": "TEST_AS_PROPAGATION_SPECIFIC_BASELINE_ONLY",
      "satisfied": true
    },
    {
      "target": "R034 owner head 674fb8717d753cd36fd83b061c869d79e8875b31",
      "action": "CONSUME_PROPAGATION_RELATIVE_GEOMETRY_DISTINCTION",
      "satisfied": true
    },
    {
      "target": "R023/R023I future-safe quotient and BRC semantic core",
      "action": "TEST_FOR_SURFACE_COLLAPSE_SPECIALIZATION_WITHOUT_REOWNING_GENERIC_THEORY",
      "satisfied": true
    }
  ],
  "source_refs": [
    "User correction: native FCC/HCP does not contain a primitive global equidistance relation; graph distance is a chosen readout/propagation semantics",
    "User continuation: a rough surface can exist before a sphere; study its composition and then its relation to algebraic collapse, starting from one cell",
    "R033 boundary-type data only as conditional shortest-path evidence, not as native sphere ontology",
    "R034 propagation-relative geometry and observable-memory hierarchy",
    "R023/R023I future-safe quotient and Branch-Recoalescence Collapse semantics"
  ],
  "evidence_status": "NATIVE_INTERFACE_AND_SURFACE_COLLAPSE_FOUNDATION_GATE",
  "last_progress_ref": "Driver/user reframe: replace native sphere/equidistance with metric-free inside/outside interface and study the exact information-loss ladder of surface descriptions.",
  "last_progress_at": "2026-08-12T14:28:00+08:00",
  "hard_block": null,
  "tags": [
    "R039",
    "fcc",
    "hcp",
    "barlow",
    "native-interface",
    "rough-surface",
    "boundary-alphabet",
    "isoperimetric",
    "collapse",
    "quotient",
    "future-relative-precision",
    "brc",
    "one-cell-seed"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R039",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R039 — Native Rough Surface Algebra and Collapse Calculus

Status: `READY / P0 / NATIVE INTERFACE / ROUGH SURFACE / COLLAPSE CALCULUS / NOT CANONICAL`

## 0. 母问题

本任务从一个比“球是什么”更低层的问题开始：

> **如果 FCC/HCP/Barlow 世界的原生结构只有胞元及其局部接触/关联，那么一个由若干胞元组成的区域与外部之间的“粗糙表面”能否在完全不引入中心、半径、等距、最短路、欧氏面积的条件下被 exact 定义、枚举、演化与压缩？这些压缩与进取数论中的代数坍缩/未来相对精度是什么关系？**

本任务的第一原则：

`native surface != sphere surface`。

本任务禁止在 native 阶段偷偷引入：

- root distance；
- graph radius；
- shortest-path shell；
- Euclidean radius；
- equal-distance class；
- `4*pi*r^2` / `4*pi*r^3/3`；
- 任何把“离理想球多远”作为粗糙度定义的量。

允许从一个 seed cell 开始生长，但 seed 只是构造 provenance，不得被升级为全局径向坐标或中心语义。最终 cluster 分类必须 quotient 掉纯平移/允许的晶格对称，而不能把“离 seed 几步”当作 native label。

---

## 1. 任务内状态机

`READY`
→ taskbook 可领取。

`CLAIMED`
→ 执行身份绑定；先冻结 native relation schema，不得先写球/半径公式。

`IN_PROGRESS / NATIVE_INTERFACE_FROZEN`
→ 已定义 cluster、inside/outside cut、boundary half-edge/face incidence、frontier cell 及局部 slot 标识；无 metricization。

`IN_PROGRESS / SMALL_CLUSTER_EXHAUSTED`
→ 已从 1 个胞元开始完成小 N connected cluster 的 exact 枚举、对称归约、边界统计和最小反例搜索。

`IN_PROGRESS / COLLAPSE_LADDER_BUILT`
→ 已建立至少 4 层 surface representation quotient，并为每层列出 preserves / does-not-preserve / future horizon / minimal counterexample。

`IN_PROGRESS / ISOPERIMETRIC_DYNAMICS_BUILT`
→ 已得到固定胞元数下的 exact minimal-boundary 数据、局部 addition/removal law、greedy/BRC/all-branch 对照与可证明边界。

`HANDOFF_READY`
→ 若未完成，必须留下 frozen definitions、已枚举范围、最小 counterexample、当前 collapse ladder 和唯一 next_action。

`SEMANTIC_CHECKPOINT`
→ 能回答“原生粗糙表面是什么、如何由局部类型组成、哪些代数坍缩对哪些表面未来是安全/不安全的”。

`DONE / RETURNED`
→ 返回 exact interface calculus、small-cluster atlas、collapse hierarchy、future-safety matrix、isoperimetric/dynamics results、kill tests 和后续 theorem/Foundation 建议。

---

## 2. Native substrate：只允许局部关系

分别建立 exact FCC 和 ideal HCP/Barlow 局部接触模型。

### 2.1 Cell/contact graph

每个胞元有 12 个 native contact slots。

允许使用 exact integer/combinatorial coordinates 作为实现工具，但必须把“坐标实现”与“native relation content”区分：

- native：cell identity、contact slot、adjacency、stacking/local type；
- implementation-only：用于去重/对称归约的整数坐标；
- forbidden-native：global radius、root distance、Euclidean norm。

### 2.2 Cluster

一个有限 cluster：

`C subset V`

要求默认 connected，但必须明确 connectivity 是通过 native adjacency 定义，而不是距离球。

### 2.3 Native interface / cut

定义 oriented boundary contact set：

`delta(C) = {(u,v): u in C, v notin C, u~v}`。

若实现使用 contact slots，则优先保留：

`delta_slot(C) = {(u,slot): neighbor(u,slot) notin C}`。

这是本任务的第一原生“表面”对象。

其 scalar size：

`S(C)=|delta(C)|`。

注意：`S(C)` 已经是对完整 boundary incidence 的一次 scalar collapse；它不是 native surface 的全部信息。

---

## 3. 从 1 个胞元开始：exact small-cluster atlas

必须实际从：

`N=1`

开始增长并枚举所有 connected clusters，至少在一个可行的 exact reference range 内做到 exhaustive。

目标优先：

- FCC 至少 `N<=10`；
- HCP 至少 `N<=10`；
- 如果组合爆炸，给 canonicalization + frontier growth + pruning 的 exact certificate，并保证至少 `N<=8` exhaustive；
- 再做更大 N 的 targeted/branch-and-bound/ILP/DP 采样，但不得把采样冒充 exhaustive。

### 3.1 Canonicalization 规则

禁止只按 abstract induced graph isomorphism 去重，如果两个 embedding 未来的可扩展环境不同。

必须 quotient by：

- global translation；
- 该 world 实际允许的 point/space-group symmetry；
- HCP/Barlow 的合法 phase equivalence（若确实存在）。

必须保留 embedding-sensitive future structure。

### 3.2 必须检查的 sanity states

对 degree-12 contact graph：

单胞：

`N=1, E_int=0, S=12`。

两个相邻胞：

`N=2, E_int=1, S=22`。

三胞至少要出现：

- chain/path-like cluster；
- 3-cycle/triangle cluster（如果 frozen FCC/HCP contact model 中存在）。

并验证它们的 boundary size 是否由内部 adjacency 数区别。

这些 sanity checks 只用于抓实现错误，不得代替全枚举。

---

## 4. 第一条 exact surface algebra

设 `E_int(C)` 为 cluster 内部 native contact 数。

对 12-regular contact graph，独立证明：

`S(C)=12|C|-2E_int(C)`。

这是本任务的基线 identity。

### 4.1 单胞增加 law

对外部 frontier cell `x notin C`，定义：

`k_C(x)=#{u in C: u~x}`。

若 `C' = C union {x}`，则独立证明：

`Delta S = S(C')-S(C)=12-2k_C(x)`。

不要把 `k` 叫 curvature；先冻结为：

`native attachment degree / local interface incidence count`。

### 4.2 单胞删除 law

对 `x in C`，若删除后仍满足 declared connectivity requirement，推导对应 exact `Delta S`，并明确所需内部邻接数/桥接信息。

### 4.3 Boundary update identity

优先给出不经过 scalar `S` 的 exact set-level update：

`delta(C union {x})`

如何由：

- 原 `delta(C)`；
- `x` 与 `C` 的 contact incidence；
- `x` 的外部 contact slots

局部更新。

这将作为“full information”参考语义。

---

## 5. Rough surface alphabet

对每个 boundary cell `u in C`，定义局部 exposed-contact mask：

`m_C(u) subset {1,...,12}`。

按 world 的真实局部 symmetry quotient 得到 finite local surface type：

`tau_C(u)`。

建立：

`N_tau(C)=#{u in boundary cells: tau_C(u)=tau}`。

必须分别研究：

- FCC local surface alphabet；
- HCP-A/HCP-B local surface alphabet；
- Barlow generic local environment 如有必要。

禁止用“normal vector”“curvature”“radius”来定义类型；那些只能作为后验 readout。

检查：

1. surface alphabet 是否有限；
2. smallest N where multiple alphabets/compositions appear；
3. FCC/HCP 是否在很小 N 已可由 native surface composition 区分；
4. 相同 `S(C)` 是否可对应不同 `N_tau(C)`；
5. 相同 `N_tau` 是否仍可有不同 boundary adjacency/correlation。

---

## 6. Frontier state：表面未来的真正局部语言

定义 frontier：

`F(C)={x notin C: exists u in C, u~x}`。

对每个 `x in F(C)` 记录：

`k_C(x)`。

第一层 frontier profile：

`H_C(j)=#{x in F(C): k_C(x)=j}`。

必须研究：

- `H_C` 是否足够预测所有 possible one-step `Delta S` support；
- `max k_C(x)` 是否足够做 one-step greedy surface descent；
- `H_C` 是否不足以预测 two-step future；
- 最小两个 clusters：`H_C=H_D` 但 two-step surface futures 不同。

如果 `H_C` 不足，逐步加入：

- frontier-frontier adjacency；
- shared-boundary-cell incidence；
- second-order overlap/correlation；
- local surface type to frontier incidence。

目标不是无限加信息，而是寻找最小 future-safe state。

---

## 7. Algebraic collapse ladder

必须明确构造一组 quotient / collapse maps。

推荐至少包含：

### Q0 — full cluster / full native incidence

保留 embedding-sensitive cluster 和完整 contact structure。

### Q1 — full interface + frontier incidence

丢掉深层 interior，但保留 boundary cut、frontier cells、boundary-to-frontier incidence 以及必要的 frontier correlations。

### Q2 — local surface-type multiset

保留 `N_tau(C)`，丢掉类型之间的空间关联。

### Q3 — frontier attachment histogram

保留 `H_C(j)`，丢掉 candidate 之间的关联。

### Q4 — coarse algebraic tuple

例如：

`(|C|, E_int(C), S(C))`。

由于 `S=12N-2E`，要标明其中哪些坐标是冗余的。

### Q5 — scalar surface only

只保留：

`S(C)`。

### Q6 — optional roughness excess

在 `S_min(N)` 已经 exact 定义/计算后：

`rho(C)=S(C)-S_min(|C|)`。

注意：`rho` 不能在 `S_min` 未定义前使用，也不能借欧氏球作 reference。

---

## 8. Collapse 必须按 future language 判定，而不是按“信息越多越好”

对每个 quotient `Q_i`，定义至少以下 future languages：

### U0 — 当前表面读数

只问 `S(C)`。

### U1 — 指定候选 cell 的一次 add/remove 后 `S`

测试 quotient 是否能在给定操作参数下精确更新。

### U1* — 任意允许 one-step addition 的 `Delta S` support

只问所有可能下一步表面变化集合。

### Ubest1 — one-step 最优表面下降

问：

`min_{x in F(C)} S(C union {x})`

或等价 `max k_C(x)`。

### Uh — h-step surface future

对 `h=2,3,...`，记录所有可达 surface-value support，或最小 achievable surface。

### Uiso — fixed-N minimal boundary

问 `S_min(N)` 及 minimizer class。

对每个 `(Q_i,U)` 必须返回：

- `SAFE_EXACT`；
- `SAFE_FOR_OBSERVABLE_ONLY`；
- `UNSAFE_MINIMAL_COUNTEREXAMPLE`；
- `OPEN`。

禁止仅凭直觉说“这个 summary 应该够”。

---

## 9. Relation to Enterprise algebraic collapse

本任务必须把 rough-surface compression 与已有代数坍缩语义真正对齐，而不是只做类比。

### 9.1 Quotient / future-safe relation

对 representation `Q`，测试：

`Q(C)=Q(D)`

是否推出所声明 future language 下的 observable equality/support equality。

这与 future-relative precision / safe operation 的关系必须写成 exact implication。

### 9.2 NO_RESURRECTION boundary

寻找最小 `C,D`：

- 在某个 coarse quotient 下相同；
- 后续某个合法 surface operation 将它们区分。

明确：一旦 quotient 抹掉 correlation，后续如果没有 residual/branch support，不得假装可恢复。

### 9.3 BRC / all-branch surface growth

从一个 cluster `C` 对所有允许 frontier additions 分支：

`C -> {C union {x}: x in F(C)}`。

研究：

- 在只关心 `S` / `S_min` / future support 时哪些 branches 可以 recoalesce；
- multiplicity 是否重要；
- Boolean reachable-support 是否足够；
- 哪些 quotient 后提前 recoalesce 会破坏 two-step/h-step future。

不要把 BRC 术语强行套入；只有 exact reachable-support 语义吻合时才使用。

### 9.4 Residual / anchor+residual candidates

测试是否存在小 residual 可以修补 coarse surface quotient，例如：

- `S + frontier histogram`；
- `surface type multiset + overlap residual`；
- `N + roughness + small defect code`。

比较 acquisition/storage cost 与 future horizon。

---

## 10. Fixed-volume minimal surface：无半径的 native droplet

定义：

`S_min^W(N)=min{S(C): C connected cluster in world W, |C|=N}`。

以及 minimizer set：

`M_W(N)=argmin_{|C|=N} S(C)` modulo allowed world symmetries。

这不是“球”。工作术语用：

`native minimal-surface droplet` / `原生最小表面团`。

必须实际计算小 N exact sequence，并寻找：

1. FCC/HCP 的 `S_min(N)` 第一次不同的 N；
2. minimizer 是否唯一 modulo symmetry；
3. 多个 minimizer 是否具有不同 boundary alphabets；
4. greedy `max k` growth 是否总能生成 global minimizer；
5. 若不能，给最小 greedy trap；
6. BRC/all-additions 是否可以在有限 branch budget 下恢复 global minimizer support。

### 10.1 Equivalent internal-edge maximization

利用：

`S(C)=12N-2E_int(C)`

证明 fixed-N minimization 等价于：

`max E_int(C)`。

这给出纯代数/图论的 isoperimetric formulation，不需要 radius。

---

## 11. Roughness：只相对 native optimum

当且仅当 `S_min(N)` 已定义时，定义：

`rho(C)=S(C)-S_min(N)`。

研究：

- `rho` 的 parity / attainable values；
- one-cell addition/removal 对 `rho` 的 exact change；
- 是否存在 local defect alphabet 控制小 `rho`；
- 相同 `rho` 的 clusters 是否未来行为不同；
- `rho` 作为 collapse coordinate 的 future-safety boundary。

禁止定义：

“roughness = 到连续球面的距离”。

---

## 12. Growth policies：表面演化与“方向性坍缩”只做后验比较

在 exact all-branch reference 建立以后，才允许比较局部策略：

- `SURFACE_DOWN`: 每步选最大 `k_C(x)`，即时最小化 `Delta S`；
- `SURFACE_UP`: 每步选最小 `k_C(x)`；
- ties 下保留 all ties / deterministic tie-break / branch support；
- 可加入随机策略作为 diagnostic。

问题：

1. local DOWN 是否等于 global minimal-surface path？
2. 哪个最小 N 首次分叉？
3. DOWN/UP 是否产生不同稳定 boundary alphabets？
4. BRC 保留 all-tie/all-endpoint 时是否能 recoalesce 到相同 `S_min` observable？

这只是与旧 collapse-direction 思想的桥，不得反过来定义 native surface。

---

## 13. 必须攻击的 hypotheses

### H1 — Native interface exactness

`delta(C)` 可在无 metric/radius 条件下 exact 定义和局部更新。

### H2 — Boundary handshake identity

`S(C)=12N-2E_int(C)` exact。

### H3 — Local attachment law

`Delta S=12-2k_C(x)` exact。

### H4 — Finite native surface alphabet

FCC/HCP boundary local mask 在真实 local symmetry quotient 后形成有限 alphabet。

### H5 — Scalar surface insufficiency

存在最小 `C,D`：

`S(C)=S(D)`

但 one-step 或 two-step surface futures 不同。

### H6 — Frontier histogram one-step sufficiency / two-step insufficiency

测试 `H_C(j)` 是否恰好刻画 one-step `Delta S` support，但不足以刻画 two-step future。

### H7 — Local-type multiset correlation debt

相同 `N_tau` 的 clusters 是否仍可因 type adjacency/correlation 不同而拥有不同 future。

### H8 — Fixed-volume native droplet law

`S_min(N)` 与 minimizer family 可在不引入 radius 的条件下建立 exact small-N atlas，并可能具有可识别渐近/递推结构。

### H9 — Greedy DOWN trap

即时最小 `Delta S` 的 greedy growth 是否可能错过 global `S_min(N)`；优先寻找最小反例。

### H10 — Collapse precision ladder

随着 future horizon `h` 增长，安全 quotient 所需信息单调增加或至少不减少；若不成立，给反例并解释原因。

### H11 — Small residual repairs coarse surface state

是否存在低成本 residual 使 `S` 或 `H_C` 对更长 horizon 重新 future-safe。

### H12 — FCC/HCP native-surface memory

在不使用 root distance 的 small-cluster/minimal-surface 问题中，FCC/HCP stacking memory 第一次在哪个 N/哪个 observable 出现。

### H13 — Sphere not required

整个 native interface/isoperimetric calculus 是否可在零 radius、零 pi 输入下闭合；任何 Euclidean comparison 必须是后验读数。

---

## 14. Exact experiments

必须有 executable exact reference。

### 14.1 数据对象

至少输出：

- canonical cluster ID；
- N；
- internal contact count `E_int`；
- full boundary size `S`；
- boundary cell-mask/type spectrum；
- frontier size；
- attachment histogram `H_C(k)`；
- one-step reachable `S` support；
- two-step reachable `S` support；
- minimizer flag / roughness `rho`（若 `S_min` 已知）。

### 14.2 Integer-only theorem-critical path

contact membership、cluster enumeration、boundary counts、canonicalization signature 和 future support 必须用 exact integer/combinatorial logic。

禁止 theorem-critical floating point。

### 14.3 Independent cross-check

对随机/targeted small clusters，用至少两种独立方法交叉：

- handshake formula `12N-2E`；
- direct cut-edge count。

任何 mismatch 立即冻结为 implementation bug，不能继续推导。

---

## 15. Minimal counterexample atlas

必须专门输出一个 counterexample table，至少寻找：

1. same `S`, different boundary type spectrum；
2. same `S`, different one-step future support；
3. same `H_C`, different two-step future；
4. same `N_tau`, different future because correlation lost；
5. greedy DOWN first failure；
6. premature branch recoalescence first failure；
7. FCC/HCP first native-surface distinction without root radius。

每个 counterexample 必须给 exact cluster encoding 和最小性说明（在已 exhaust 的 N 区间内）。

---

## 16. Prior-art rooting

独立发现阶段完成后，再有界查 prior art。

重点但不限于：

- edge-isoperimetric problem on lattices/periodic graphs；
- lattice animals / polycubes / close-packed clusters；
- Wulff constructions 与 crystalline surface energy；
- discrete minimal surfaces；
- cluster expansion / surface tension；
- quotient automata / Markov sufficient state / lumpability（只在 future-state 语义真正一致时）。

不得因为经典 edge-isoperimetric prior art 已存在，就否定本任务关于：

`native interface representation + collapse ladder + future-safety + BRC/residual precision`

的项目内组合价值。

同样不得把已有结果重新宣称为 Enterprise Math 新定理。

---

## 17. 允许的最强返回类

可能的正结果包括：

`NATIVE_INTERFACE_CALCULUS_FOUND`

`BOUNDARY_HANDSHAKE_LAW_CONFIRMED`

`FINITE_SURFACE_ALPHABET_FOUND`

`NATIVE_ISOPERIMETRIC_DROPLET_SEQUENCE_FOUND`

`SURFACE_COLLAPSE_PRECISION_LADDER_FOUND`

`SCALAR_SURFACE_FUTURE_INSUFFICIENCY_FOUND`

`FRONTIER_HISTOGRAM_ONE_STEP_SUFFICIENT_TWO_STEP_INSUFFICIENT`

`SURFACE_CORRELATION_DEBT_FOUND`

`SMALL_RESIDUAL_REPAIRS_SURFACE_COLLAPSE`

`GREEDY_SURFACE_DOWN_TRAP_FOUND`

`SURFACE_BRC_RECOALESCENCE_LAW_FOUND`

`FCC_HCP_NATIVE_SURFACE_MEMORY_FOUND`

`METRIC_FREE_SURFACE_CALCULUS_CLOSED`

也允许负结果：

`LOCAL_MASK_ALPHABET_INSUFFICIENT_IMMEDIATELY`

`NO_LOW_COST_SURFACE_COLLAPSE_FOUND`

`FIXED_VOLUME_MINIMIZER_NOT_STRUCTURALLY_STABLE`

`FCC_HCP_NATIVE_SURFACE_UNIVERSAL_IN_TESTED_RANGE`

`SURFACE_COLLAPSE_DOES_NOT_MAP_CLEANLY_TO_EXISTING_QUOTIENT_SEMANTICS`

负结果必须给 minimal witness。

---

## 18. 最终必须回答

最终报告必须直接回答以下问题：

1. **不定义距离时，一个 FCC/HCP cluster 的原生粗糙表面究竟是什么？**
2. **从 1 个胞元开始，表面状态第一次在哪个 N 出现非平凡分叉？**
3. **`S=|delta C|` 丢掉了哪些对未来真正有用的信息？**
4. **哪一个最小 surface representation 足以支持 one-step / two-step / h-step growth？**
5. **这种 representation hierarchy 是否就是一个 future-relative algebraic collapse lattice？**
6. **fixed-volume minimal-boundary droplet 是否可以完全不靠半径定义？**
7. **FCC/HCP stacking memory 是否在这种 metric-free surface calculus 中仍然可见？第一次在哪？**
8. **从 rough surface 到 area/normal/curvature/radius/sphere 的后续读取链中，第一次真正发生 scalar collapse 的位置在哪里？**

最终优先形成：

`native relation -> interface incidence -> local surface alphabet -> frontier future state -> algebraic quotient/collapse -> minimal-surface dynamics -> optional smooth/Euclidean readout`

而不是：

`continuous sphere -> discretize -> compare error`。
