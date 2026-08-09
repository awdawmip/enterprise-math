# Enterprise Math / 进取数论共享研究面

状态：`ACTIVE / REQUIRED PREFLIGHT`  
生效：2026-08-09  
目的：让每一条研究路线在开始新的 theorem line 前，都能看到同一份紧凑的可复用数学、可执行工具、负向边界、活跃接口警报、dispatch 状态与跨路线实时结果。

本文件是路由器，不替代正式证明。精确定理范围仍由 canonical result 文档控制；branch 上已证明结果在正式晋升前必须继续显式保持 WIP 身份。Scheduler 只协调工作，不会提升数学真值状态。

## 1. 强制预检

开始新的 L1/L2/L3 theorem line 前：

1. 阅读本共享研究面；
2. 阅读 `docs/RESEARCH_SCHEDULING_PROTOCOL.*`；
3. 阅读 `research_scheduler.json` 与实时 Research Dispatch Board Issue #240；
4. 阅读 `docs/RESEARCH_OWNER_ISOLATION.*`；
5. 阅读 `docs/PROBLEM_STATUS.*` 以及相关 canonical result 文档；
6. 阅读 Research Relay Issue #82 中最新且相关的条目；
7. 检查重叠的 executable specs/tests 与 root build 实际导入的 Lean 模块；
8. 若工作触及底层语言、公式、定理/工具接口，阅读 `docs/FOUNDATION_STEWARD_PROTOCOL.*` 与 Foundation Problem Set Issue #164 中相关 `FQ-*`；
9. 然后才判断工作属于母定理、特化、bridge、counterexample、tool、重复结果，还是基础问题回答。

采用选择性读取，不把整个仓库注入工作上下文。

## 2. 认识论/状态纪律

必须区分：

- `CANONICAL_MAIN`：在声明 scope 内已经证明并进入 `main`；
- `LEAN_CHECKED_MAIN`：canonical 且被实际 imported/warning-fatal Lean build 覆盖；
- `PROVED_WIP_RELAY`：branch 已证明并带 source provenance，但尚未 canonical；
- `EXECUTABLE_CHECKED`：有精确 executable/finite validation 支持，但不能单独替代证明；
- `COUNTEREXAMPLE / NEGATIVE_BOUNDARY`：可复用的不可能性/失败结果；
- `CONJECTURAL`：研究目标。

**canonical executable asset** 指已经把 source/test 资产集成进 `main`；它本身不自动把模块中体现的每一个数学陈述升级为 `PROVED`。同样，scheduler 的 claim/lease 只记录谁在工作，不代表已经证明了什么。

## 3. Canonical 知识通道

- `docs/THEOREMS.*`：原始 core 的紧凑 theorem catalogue；
- `docs/PROBLEM_STATUS.*`：编号问题的权威状态/router；
- canonical `docs/Pxxx_*.{en,zh-CN}.md`：现代 theorem families 的精确陈述与假设；
- `EnterpriseMath.lean` 及其实际 import 的 `EnterpriseMath/**.lean`：Lean-checked 子集；
- Research Relay Issue #82：带 source commit/relation class 的 branch 已证明 WIP 结果/反例；
- Foundation Problem Set Issue #164：经过最低验证、需要研究处理的底层问题；
- `research_scheduler.json` 与 Issue #240：仅用于实时 dispatch/lease/handoff 协调。

不能因为某结果或工具不在当前 branch 就推断“项目里未知”。

## 4. 全线路共享数学归属面

### A0 — primitive discrete state algebra

整数根/坍缩、basin/gap 坐标、quotient/remainder、scale factor 与 gcd/lcm lattice、signed state、typed descent、adjoint、commutation 与 fixed points。主要 canonical 入口：P001–P009 与 `docs/THEOREMS.*`。

Canonical 接口约定：

- `N = N_0 = {0,1,2,...}`；正整数记为 `N_{>0}`；
- 非平凡原始 root/collapse 使用 `p >= 2`；
- 精确正指数代数使用 `p >= 1`，并有 `R_1 = C_1 = id`。

### A1 — dynamics、kernels、collision、stabilization

确定性 history merge、fiber/kernel multiplicity、collision spectra、coalescence 与 well-founded stabilization。规范时间接口：

`F_0 = id`，`F_{t+1} = T_t o F_t`；等价地，对 `t >= 1`，`F_t = T_{t-1} o ... o T_0`。

主要入口：P010、P011、P019、P020。

### A2 — observation 与 future-compatible quotient

Observation factorization、predictive/future closure、有限 operation-family compatibility、minimal repair 与 task-relative precision。P018/P023/P024 是主要入口。finite-arity quotient operation-congruence extension 已 canonical；其 Lean 资产为 `EnterpriseMath/Quotient/OperationCongruence.lean`，只有被 root build 实际导入时才可声称对应部分 Lean-checked。

### A3 — structured relation-state algebra

核心对象：`Z_ij = m_j*c_i - m_i*c_j`，并包括 partition coarsening `Z' = A Z A^T`、relation scale/rank 与 refinement structure。

已经进入 `main` 的 canonical executable core：

- `weighted_relation_field.py`；
- `relation_lattice.py`；
- `relation_scale.py`；
- 对应 canonical regression suites。

这些模块是全线路共享 executable specifications。任何仍只存在于 research branch/Relay 的 theorem statement，在单独 canonicalize 前仍保持 WIP。

### A4 — admissible support / correspondence algebra

Finite multivalued relation、converse/composition、common-target structure、radius-indexed support、split-completeness boundary、MAY/MUST semantics 与 witness/group spectra。

已经进入 `main` 的 canonical executable core：

- `admissible_support.py`；
- `relational_spectrum.py`；
- 对应 canonical regression suites。

A3→A4 executable bridge `a3_a4_support_bridge.py` 也已进入 `main`；其 theorem/proof 状态仍由 canonical result/Relay provenance 控制，不能仅凭 module 存在自动升级。

### A5 — intrinsic discrete geometry

P012 给出**连通无向简单图**上的 canonical 普通度量基础。Canonical 工具包括 `geometry.py`，以及已经进入 `main` 的 P022 `A_p` / root-lattice executable core `lattice_geometry.py` 与其 regression suite。

P022 仍为 `OPEN / ACTIVE RESEARCH`；当前 canonical executable slice 覆盖整数 `A_p` graph distance、quadratic separation、collapsed radial distance、shell/ball counts 与 distance-carry probes。更广的 lattice candidates、HCP/Barlow 与跨 owner 接口继续开放。

**活跃接口警报：** `FQ-20260809-005` 正在判断稳定导出的 `geometry.graph_distance` 应收窄到 P012 无向 metric 定义域，还是应与更一般的 directed shortest-walk helper 分层。在解决前，非对称 adjacency 输入不得直接引用 P012 的 metric symmetry。

### P021 — causal-boundary specialization

已经进入 `main` 的 canonical executable core：

- `causal_boundary.py`；
- `test_causal_boundary.py`。

它复用 P018 observation/refinement machinery，并拥有有限图 + 整数 expansion boundary 的 program-specific 特化。更广的 causal focusing、方向/witness 复合及物理解释继续开放。

### E001 — 有限材料冲量应用特化

以下八文件 slice 已作为 canonical executable application machinery 进入 `main`：

- `material_impulse_accounting.py` + regression；
- `material_impulse_world_1d.py` + regression；
- `material_impulse_tick_order.py` + regression；
- `material_impulse_wall_world_1d.py` + regression。

这组资产可复用于 retained-detail 冲量精确记账、离散动量漂移、显式 tick-order 比较以及 contact/wall-world 实验。它**不是**通用 mechanics/material theorem，也不会仅凭进入 `main` 就完成物理模型验证。尤其 `OUTWARD` 动量不能被悄悄等同于物理 `REBOUND`；更丰富事件仍需要 contact history / transmission state。

## 5. 所有路线都必须知道的高价值负向边界

- coarse equality/support/cardinality 不自动保留后续 composition；
- A3 signed relation data 在 quotient 时可能 cancellation，因此 coarse support 不能证明 universal fine support；
- pairwise/common-target cardinality 可能丢失 multi-step composition 需要的 witness identity；
- geometry-only contact/collision fact 可能不足以唯一选择 response；
- 对一个 future language 安全的 quotient，面对更丰富语言可能失效；
- 普通 metric claim 必须满足其 graph/weight hypotheses；directed/asymmetric structure 不能悄悄继承 symmetry；
- E001 engineering transition/result 不能仅因其 executable slice 已 canonical 就提升为通用物理定律；
- 文件名相同、Git ancestry 或 `ahead(main)>0` 都不能证明存在新数学；
- Galois connection、semigroup、numerical semigroup、partition refinement 等成熟结构继续属于 prior art。

## 6. 全线路共享 executable 工具面

所有路线都可以复用 canonical executable assets；发现 branch 不产生独占权。

`src/enterprise_math/` 下的重要 Python 工具族包括：

- A0/A5 primitives：`core.py`、`division.py`、`scale_algebra.py`、`signed.py`、`typed_scale.py`、`geometry.py`、`lattice_geometry.py`；
- A2：`composition_safe_collapse.py`、precision/predictive/future-signature modules，以及 action-language/clearance/guard/boundary specializations；
- A3：`weighted_relation_field.py`、`relation_lattice.py`、`relation_scale.py`；
- A4：`admissible_support.py`、`relational_spectrum.py`；
- A3→A4：`a3_a4_support_bridge.py`；
- P021：`causal_boundary.py`；
- P017：mirror/cofactor/Legendre pressure-test modules；
- E001 application：`material_impulse_accounting.py`、`material_impulse_world_1d.py`、`material_impulse_tick_order.py`、`material_impulse_wall_world_1d.py` 及对应 tests。

`src/enterprise_math/__init__.py` 只导出紧凑 stable subset。未导出的 module 仍可能是 canonical internal executable specification；把它当 stable API 前先检查 scope/provenance。

Lean：

- `EnterpriseMath.lean` 是 root import surface；
- `EnterpriseMath/**.lean` 保存 formalization assets；
- 只有实际被 imported/warning-fatal build 覆盖的 statement 才能标记 `LEAN_CHECKED_MAIN`。

Validation/reconstruction/governance tools：

- `tests/`：exact regression/counterexample suites；
- `experiments/`：bounded pressure tests 与 engineering probes；
- `tools/check_bilingual_pairs.py`：bilingual gate；
- `tools/check_references.py`：reference-integrity gate；
- `tools/research_scheduler.py`：实时 dispatch/lease/handoff 状态机辅助工具；它只协调执行，不认证 theorem truth。

Executable checks 服务于 discovery/falsification/regression，不能独立把 claim 升级为 `PROVED`。

## 7. 传播、dispatch 与非阻断规则

出现可复用结果时：

1. 若其他 active route 可能受益，立即 Relay；
2. downstream action 标为 `INFORM`、`CONSUME`、`TEST` 或 `HARD_DEPENDENCY`；
3. 标明 mother-theorem owner/relation class；
4. canonical promotion 后按需要更新 status/result routing 与本共享面；
5. 新的可复用 executable tool family 在这里登记；
6. 除非存在完整 `HARD_BLOCK`，不等待 consumer ACK。

研究并行，canonical promotion 串行；`defer` 是路由，不是 blocker。Issue #240 上的 claim 是可续期 execution lease；若本会话无法继续，必须 HANDOFF 回 scheduler，不能让路线静默无人负责。Scheduler 事件（`CLAIM`、`HEARTBEAT`、`PROGRESS`、`HANDOFF`、`HARD_BLOCK`、`UNBLOCK`、`DONE`、`SUPERSEDE`）只用于协调执行。

## 8. 底层维护

机械性或已经由 canonical 证据唯一决定的底层漂移，由 foundation steward 直接修复。真正尚未解决的数学/接口选择，只验证到足够成立后进入 Issue #164，并交由其他研究员调查。

当前活跃 foundation questions：

- `FQ-20260809-004` —— 跨路线回流提出的 candidate minimal State/Pair/kernel → future-safe precision foundation interface；
- `FQ-20260809-005` —— stable `graph_distance` API 定义域与 P012 普通 metric theorem 定义域之间的接口选择。

FQ-001 至 FQ-003 的 canonical 约定仍按上文执行。
