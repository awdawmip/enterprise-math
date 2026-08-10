# Enterprise Math / 进取数论共享研究面

状态：`ACTIVE / REQUIRED PREFLIGHT`  
生效：2026-08-09

目的：让每条研究路线共享一份紧凑的可复用数学、canonical executable/formal 资产、负向边界、活跃接口警报与实时路由。本文件是路由器，不替代精确定理文档或证明。

## 1. 强制预检

开展实质性的 L1/L2/L3 研究前：

1. 阅读本文件与 `research_common_surface.json`；
2. 阅读 `docs/RESEARCH_SCHEDULING_PROTOCOL.*`、`research_scheduler.json` 与实时 Dispatch Board Issue #240；
3. 阅读 `docs/RESEARCH_OWNER_ISOLATION.*`；
4. 阅读 `docs/PROBLEM_STATUS.*` 及相关 canonical theorem/result 文档；
5. 阅读 Research Relay Issue #82 中最新且相关的条目；
6. 在另起平行 theorem/tool 前检查重叠 Python/tests 与 root-imported Lean modules；
7. 若工作触及底层接口，阅读 `docs/FOUNDATION_STEWARD_PROTOCOL.*` 与 Foundation Problem Set Issue #164 中相关 `FQ-*`。

采用选择性读取。当前 branch 中没有，不等于整个项目没有。

## 2. 状态纪律

必须区分：

- `CANONICAL_MAIN`：在声明 scope 内已证明并进入 `main`；
- `LEAN_CHECKED_MAIN`：canonical 且实际被 root warning-fatal Lean build 覆盖；
- `PROVED_WIP_RELAY`：branch 已证明并带 provenance，但尚未 canonical；
- `EXECUTABLE_CHECKED`：精确 executable/finite validation，不等于单独证明；
- `COUNTEREXAMPLE / NEGATIVE_BOUNDARY`：可复用失败/不可能性结果；
- `CONJECTURAL`：研究目标。

source/test module 进入 `main` 不会自动把其所有数学或物理解释升级成 theorem。Scheduler claim/lease 只协调工作，不认证真值。

## 3. Canonical 知识通道

- `docs/THEOREMS.*`：原始 core 紧凑 theorem catalogue；
- `docs/PROBLEM_STATUS.*`：编号问题权威 router；
- canonical `docs/Pxxx_*.{en,zh-CN}.md`：现代 theorem 的精确陈述与假设；
- `EnterpriseMath.lean` 及其 import 的 `EnterpriseMath/**.lean`：root Lean-checked 子集；
- `research_common_surface.json`：机器可读 theorem/tool/formalization router；
- Research Relay Issue #82：跨路线 WIP、负向边界与 canonical consumption 通知；
- Foundation Problem Set Issue #164：已验证但尚未解决的底层问题；
- `research_scheduler.json` + Issue #240：仅用于 dispatch/lease/handoff。

## 4. 共享数学归属面

### A0 — primitive discrete state algebra

整数根/坍缩、basin/gap 坐标、quotient/remainder、scale lattice、signed state、typed descent、adjoint、commutation 与 fixed points。主要入口为 P001–P009 与 `docs/THEOREMS.*`。

Canonical 约定：

- `N = N_0 = {0,1,2,...}`；
- 正整数为 `N_{>0}`；
- 非平凡 primitive root/collapse 使用 `p >= 2`；
- 正指数代数使用 `p >= 1`，且 `R_1 = C_1 = id`。

### A1 — 确定性动力学与 functional kernels

History merge、fibers/kernel multiplicity、collision spectra、coalescence 与 stabilization。规范时间为：

`F_0=id`，`F_{t+1}=T_t o F_t`，因此对 `t>=1` 有 `F_t=T_{t-1} o ... o T_0`。

FQ-004 已 canonicalize 通用 functional 层。对确定性 `f:X->Y`，

`x ~_f y iff f(x)=f(y)`，且 `ker(f) subseteq ker(g o f)`。

State Pair 只是普通 `X x X`，不是新原语。

### A2 — observation 与 future-compatible quotient

Observation kernels、factorization、declared future signatures、predictive closure、operation-family compatibility、minimal repair 与 task-relative precision。P018/P023/P024 是主要 owner/consumer。

对声明的确定性未来语言 `W`，把所需输出打包为 `Sigma_W:X->S_W`；该语言下的 future-safe equality 是 `ker(Sigma_W)`。若当前 observation `O` 已包含在 signature 中，则

`精确相等 subseteq ker(Sigma_W) subseteq ker(O)`。

Difference/defect/critical-grid 或其他压缩坐标，只有在所需当前/未来输出能够通过它 factorize 后，才可替代状态信息。

#### P023 合法性敏感的部分操作商 — `CANONICAL_MAIN + EXECUTABLE_CHECKED / NOT LEAN-CHECKED`

FQ-006 把 declared-future 接口从全定义确定性操作扩展到有限确定性部分操作

`F_a : D_a -> X`。

只有当两个状态对每个声明生成元都具有相同的 **enabledness/定义域成员关系**，并且动作可执行时其目标落入同一 quotient class，quotient class 才可以把它们合并。迭代 signature

`q_(t+1)(x) = (q_t(x), (enabled_a(x), next_class_a(x))_a)`

会单调细化初始 observation，在有限 `X` 上稳定，并得到与整个部分操作族兼容的最粗细化。深度 `t` 的 partition 恰好等于所有长度不超过 `t` 的声明动作词之合法性敏感 observation signature 相等关系；由于所有前缀也都属于这些动作词，prefix legality 同时被保留。

若所有 `D_a=X`，该构造在 partition-label 重命名意义下精确退化为现有 P023 全操作族闭包。

Canonical 资产：

- `docs/P023_PARTIAL_OPERATION_QUOTIENT_SUPPLEMENT_08.en.md`
- `docs/P023_PARTIAL_OPERATION_QUOTIENT_SUPPLEMENT_08.zh-CN.md`
- `src/enterprise_math/partial_operation_quotient.py`
- `tests/test_partial_operation_quotient.py`

只有在显式区分且 absorbing 时，吸收态 `UNDEFINED` sink 才可作为**验证表示**。它不是新的 Enterprise Math world state；未区分的 sink 会错误合并 enabled 与 disabled behavior。Partial transition systems、automata/behavioral equivalence、sink totalization 与有限 partition refinement 均属于前人数学；这里不提出一般原创性主张。

#### P018↔P023 有界 quotient-root action basis — `LEAN_CHECKED_MAIN`

PR #249 / `main@c9b39069917c32b8a02a1bbdf6297ca5e43c9438`。

对 `O_a(q)=R_r(floor(q/a))` 在精确状态 `0,...,N` 上，一个正 action set 分离全部精确状态，当且仅当它包含全部 `b<=N` 的正 `r`-power-free 整数；这些 actions 因而构成按包含关系唯一的最小 separating set。局域规律为

`O_a(q-1) != O_a(q) iff q=a*t^r`

其中 `t` 为正整数。

Canonical 资产：

- `EnterpriseMath/Quotient/RootAdjacentBoundary.lean`
- `EnterpriseMath/Quotient/PowerFreeActionBasis.lean`
- `src/enterprise_math/p018_p023_power_free_action_basis.py`
- `tests/test_p018_p023_power_free_action_basis.py`
- `docs/PRIOR_ART_P018_P023_POWER_FREE_ACTION_BASIS.en.md`
- `docs/PRIOR_ART_P018_P023_POWER_FREE_ACTION_BASIS.zh-CN.md`
- 独立 source/lineage sidecars。

边界：power-free arithmetic 与通用 distinguishing/Test-Cover/minimal-language machinery 属于前人数学；精确 packaging 的历史新颖性仍未验证。**future-safe state precision 与最小 future-action-language complexity 是不同资源。**

#### P018 centered-prime-radius 层 — `CANONICAL_MAIN + EXECUTABLE_CHECKED`

PR #270 / `main@b48019603c3c39332be97a5769e811f33d884296`。

资产：

- `src/enterprise_math/centered_prime_radius.py`
- `tests/test_centered_prime_radius.py`

这是已经建立的 P018 Stage-8 near-diagonal factor-proof slack 的 elementary centered-coordinate 重写。在其明确的 left-prime 与 size-range 假设下，相关最小正对称 prime radius 等于 `proof_slack+1`，shell state 可由平方差定位。它**不**声称每个中心都存在对称素数对，也不证明 Goldbach 类命题。

### A3 — structured relation-state algebra

核心对象为 `Z_ij=m_j*c_i-m_i*c_j`，并包含 partition quotient/kernel、relation scale/rank 与 refinement structure。

Canonical executable core：

- `src/enterprise_math/weighted_relation_field.py`
- `src/enterprise_math/relation_lattice.py`
- `src/enterprise_math/relation_scale.py`

这些是可复用 executable specifications。更广的历史 A3 theorem claim 保持其真实 WIP/canonical 状态。除非存在显式 reduction theorem，A3 不等同于普通 functional-kernel membership。

### A4 — admissible support / correspondence algebra

有限多值 relation、composition/converse、common-target structure、split-completeness、MAY/MUST support 与 witness/group spectra。

Canonical executable core：

- `src/enterprise_math/admissible_support.py`
- `src/enterprise_math/relational_spectrum.py`
- `src/enterprise_math/a3_a4_support_bridge.py`（首个 A3→A4 executable bridge slice）。

A4 multivalued correspondence 不能被悄悄等同于一个确定性 functional kernel，也不能等同于一个部分确定性操作族。

### A5 — intrinsic discrete geometry

P012 给出**连通无向简单图**上的普通 metric 基础。P022 仍为 `OPEN / ACTIVE RESEARCH`；canonical executable geometry 不代表整个 program 已解决。

Canonical P022 families：

- `src/enterprise_math/lattice_geometry.py` + `tests/test_lattice_geometry.py`：精确 `A_p`/root-lattice graph distance、quadratic separation、radial collapse、shell/ball counts 与 distance-carry probes；
- PR #262 / `main@fc81a15a0fc7a76d1d2b44e7d9a41b699863ef22`：
  - `src/enterprise_math/p022_geodesic_multiplicity.py`
  - `tests/test_p022_geodesic_multiplicity.py`
  - `src/enterprise_math/p022_hcp_geometry.py`
  - `tests/test_p022_hcp_geometry.py`
- PR #288 / `main@aec7f625e48eb8f93ba701ba57686a9e225efd17`：
  - `src/enterprise_math/p022_barlow_stacking.py`
  - `tests/test_p022_barlow_stacking.py`；
- PR #292 / `main@04a3baa2f47981a752e4fbaa50c9166a06690d36`：
  - `src/enterprise_math/p022_barlow_precision.py`
  - `tests/test_p022_barlow_precision.py`；
- PR #296 / 当前 L4：
  - `src/enterprise_math/p022_barlow_growth.py`
  - `tests/test_p022_barlow_growth.py`。

PR #262 给出 `A_p` 与 simple-cubic geometry 的精确有限/组合 geodesic-multiplicity observable，以及整数坐标 ABAB HCP contact graph：degree 12、精确 graph distance/shells，并以独立算法交叉检查 shortest-path counts。通用非负 witness-count/correspondence algebra 属于 A4/A2；P022 拥有 geometry specialization。这里没有偷偷引入浮点 Euclidean sphere-center 模型。

PR #288 把 close-packed executable 层推广到 periodic Barlow stacking：periodic contact graph、精确 graph distance/geodesic multiplicity、FCC/HCP reconstruction，以及针对声明的 root-to-target-layer distance/geodesic-count query 的**累计 interface-sign-count**压缩。

PR #292 加入对应的 task-relative precision 边界。对一个选定 target layer，`(abs(k), delta_k)` 可精确恢复两类 effective interface-sign counts，从而恢复声明的 root-to-layer distance/geodesic-count language 所需的 vertical witness polynomial；同一 imbalance 也可由该 polynomial 的一阶矩恢复。这不是 whole-history sufficiency：完整 prefix-imbalance trajectory 严格更丰富，并可重建 literal stacking word。

PR #296 在上述精确 precision normal form 上加入 periodic-growth 层。对长度为 `L`、period drift 为 `D` 的周期 sign pattern，executable layer 从 prefix imbalance 给出精确 shell-total geodesic formulas，并由

`(lambda - 2)^(2L) = 2^(L+|D|)`

给出精确正增长常数，同时构造按 period blocks 得到的 universal eventual C-finite annihilator/recurrence class。该 annihilator 可能不是 minimal。因而，相同 period length 与相同 absolute drift 会强制相同的 class-level growth equation 和 universal recurrence space，但**不**强制相同有限 shell-total sequence 或 phase：有限周期 cancellation 仍可不同。Coordination-observable 与 observation-history theory 仍在本次 promotion 之外。

**活跃接口警报 — FQ-20260809-005：**稳定导出的 `geometry.graph_distance` 接受一般 adjacency mapping，而 P012 普通 metric theorem 假设连通无向简单图。在研究答案经 steward 验证前，对非对称 adjacency 输入不得引用 P012 metric symmetry。

### P021 — causal-boundary specialization

Canonical executable core：

- `src/enterprise_math/causal_boundary.py`
- `tests/test_causal_boundary.py`

它复用 P018 observation/refinement machinery，并拥有有限图 + 整数 expansion causal-boundary 特化。更广的 causal focusing、witness/direction composition 与物理解释继续开放。

## 5. 共享 E001 application 工具与边界

### 有限 material-impulse world

Canonical executable family：

- `src/enterprise_math/material_impulse_accounting.py`
- `src/enterprise_math/material_impulse_world_1d.py`
- `src/enterprise_math/material_impulse_tick_order.py`
- `src/enterprise_math/material_impulse_wall_world_1d.py`
- 对应四个 regression 文件。

可复用于 retained-detail impulse accounting、momentum drift、tick-order comparison 与 wall-world tests。它不是通用 mechanics/material theorem；尤其 `OUTWARD` momentum 不自动等于物理 `REBOUND`。

### 精确 measured-polyline refinement

PR #264 canonical 资产：

- `src/enterprise_math/material_measurement_area_refinement.py`
- `src/enterprise_math/material_measurement_refinement_variation.py`
- `tests/test_material_measurement_area_refinement.py`
- `tests/test_material_measurement_refinement_variation.py`

这些工具精确量化向已声明整数 stress-strain polyline 加入**新真实测量点**时发生的变化；它们不插值缺失样本，也不恢复未知连续 constitutive curve。

### Residual result-conservation slice

PR #274 / `main@12500185f4c222ae49816e7b844e36a82e3ac8fe` 已 canonicalize：

- `src/enterprise_math/material_alias_stability.py` + `tests/test_material_alias_stability.py`：有限永久 response/anisotropy alias horizon；horizon 前 visibility 可非单调；
- `src/enterprise_math/material_boundary_shell_growth.py` + `tests/test_material_boundary_shell_growth.py`：固定深度 `K` 时，`R_{n,K}(d)=d^n-(d-K)^n` 的精确离散次数为 `n-1`，而完整 coarse box 为 `n` 次；
- `src/enterprise_math/material_phase_saturation.py` + `tests/test_material_phase_saturation.py`：endpoint-clearance sum `C>=2d-1` 后 interaction phases 饱和为 `2(d-1)`，新增 displacement 只增加 transmission phases；
- `src/enterprise_math/material_layered_kinematics.py` + `tests/test_material_layered_kinematics.py`：**COMPARATOR-NEGATIVE**——即使 undeformed rational product 交换，两层 staged finite projection 的顺序结果也最多可差一个 returned-budget quantum。

这些都是有限整数/application result，不是 probability law、hidden continuum、laminate constitutive law 或通用 material physics。

## 6. 高价值负向边界

所有路线必须知道：

- 精确状态相等、当前观测相等与声明 future-safe 相等不同，除非假设证明它们重合；
- 压缩坐标在没有 factorization/sufficiency 时不是动力学完备状态；
- future-safe state precision != 最小 future-action-language complexity；
- 对声明的部分 action language，disabledness/定义域成员关系本身就是未来行为，不能被悄悄解释成 identity；
- absorbing `UNDEFINED` sink 只有在显式区分且 absorbing 时才是等价验证表示；它不是新的 ontic state；
- coarse equality/support/cardinality 不保证后续 composition 或 witness identity；
- A3 signed relation data 在 quotient 时可能 cancellation；
- geometry-only collision/contact fact 可能不足以确定唯一 response；
- 对一种 future language 安全的 quotient，对更丰富语言可能失效；
- 普通 metric claim 必须满足 P012 graph hypotheses；
- 相同 periodic Barlow `(L,|D|)` growth/recurrence class 不决定有限 shell-total sequence 或 phase；
- finite measured-polyline refinement 不会揭示未测量 continuum；
- engineering code 进入 `main` 不会自动成为通用物理定律；
- Git ancestry/同名文件不证明新数学或 semantic absorption；
- function kernels、Galois connections、semigroups、partial transition systems、automata distinguishability、Test Cover、power-free arithmetic、numerical semigroups、partition refinement 等均属于 prior art。

## 7. Root Lean import index

`EnterpriseMath.lean` 是 canonical root build。机器索引必须与下列 imports 精确一致：

- `EnterpriseMath/Arithmetic/CollapseCommutation.lean`
- `EnterpriseMath/Arithmetic/CollapseGap.lean`
- `EnterpriseMath/Arithmetic/IntegerRoot.lean`
- `EnterpriseMath/Arithmetic/RootMultiplicativity.lean`
- `EnterpriseMath/Dynamics/HistoryMerge.lean`
- `EnterpriseMath/Order/ReductiveCompositionStabilization.lean`
- `EnterpriseMath/Order/WellFoundedStabilization.lean`
- `EnterpriseMath/Precision/Carry.lean`
- `EnterpriseMath/Precision/CompositionSafeCollapse.lean`
- `EnterpriseMath/Precision/QuotientBasin.lean`
- `EnterpriseMath/Precision/QuotientCoalescence.lean`
- `EnterpriseMath/Quotient/OperationCongruence.lean`
- `EnterpriseMath/Quotient/PowerFreeActionBasis.lean`
- `EnterpriseMath/Quotient/RootAdjacentBoundary.lean`
- `EnterpriseMath/Quotient/RootFutureClosure.lean`
- `EnterpriseMath/Scale/Compatibility.lean`
- `EnterpriseMath/State/CriticalGrid.lean`

只有实际被这些模块覆盖的 statement 才能标记 `LEAN_CHECKED_MAIN`。

## 8. Repository operational tools

所有 `tools/*.py` 都是共享 operational infrastructure，必须同时进入 machine/human index：

- `tools/audit_branch_lifecycle.py`
- `tools/check_bilingual_pairs.py`
- `tools/check_references.py`
- `tools/check_research_common_surface.py`
- `tools/research_scheduler.py`

`tools/check_research_common_surface.py` 只做机械检查：registered path 存在性、root-Lean imports 精确一致、repository-tool membership 精确一致、active-FQ 集合一致、active-alert 有效性。它不证明数学，也不判断语义复用价值。

`tests/` 支持 regression/counterexample；`experiments/` 支持 bounded pressure tests。二者都不会自动把 claim 升成 `PROVED`。

## 9. 传播与 canonical-promotion contract

可复用结果出现时：

1. Relay 时记录 source、最弱假设、relation class、owner，并给出 `INFORM`、`CONSUME`、`TEST` 或 `HARD_DEPENDENCY`；
2. 除非存在完整 `HARD_BLOCK`，研究保持并行；
3. canonical L4 promotion 时更新 `docs/RESEARCH_COMMON_SURFACE.*` 与 `research_common_surface.json`，或明确说明 shared-surface delta 为 `N/A`；
4. 登记可复用 executable-family paths；
5. `EnterpriseMath.lean` root import 与 `tools/*.py` membership 变化必须在同一 PR 同步 machine/human exact indexes；
6. 只做一次 current-main final combination gate；验证期间 `main` 的无关推进不生成新 replay generation。

`tools/check_research_common_surface.py` 强制其中可机械判定的部分；语义 scope 仍由 steward/reviewer 判断。

## 10. Foundation stewardship

FQ-001 至 FQ-004 与 FQ-006 已 canonicalized。目前 active foundation questions 为：

- `FQ-20260809-005` —— stable `graph_distance` API 定义域与 P012 ordinary-metric theorem 定义域。
- `FQ-20260810-007` —— 研究是否存在一个最弱的项目原生有限 causal/relational primitive，使任意有限预采样在操作上可被证伪；若不存在，则证明当前 Foundation 需要额外物理/因果公理才能区分在线生成与有限 latent completion。

FQ-006 在不改变 FQ-004 actual-state / observation / future-safe 分层的前提下，为 P023 增加合法性敏感的部分确定性未来语言；它也不把 A4 multivalued correspondence 压缩成 partial function model。

FQ-007 路由到 clean owner `research/r004-causal-identifiability-v1` 与 durable task `RS-R004-CAUSAL-IDENTIFIABILITY`。历史 R004 PR #302 仅作为 evidence/provenance；Bell locality 与 measurement independence 是压力测试限制，不是 Foundation 公理，也不是项目原创主张。

Steward 直接修机械漂移，但不替研究员选择尚未解决的研究答案。FQ 回报必须先经 steward 验证，才能 canonicalize。
