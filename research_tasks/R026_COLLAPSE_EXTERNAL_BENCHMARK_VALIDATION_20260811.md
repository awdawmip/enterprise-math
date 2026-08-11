<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R026-COLLAPSE-EXTERNAL-BENCHMARK-VALIDATION",
  "title": "R026 Solved-Problem Validation of Collapse Modes and Residual-Field Iteration",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_CALIBRATION",
  "frontier": "Test Enterprise Math collapse semantics against already-solved mathematical, numerical, physical, and engineering problems with known ground truth, so that downward/upward/nearest/stochastic/BRC projection and residual-field iteration can be distinguished by actual utility rather than internal elegance.",
  "next_action": "Build a common benchmark harness, freeze exact/reference solvers for each benchmark family, map each collapse mode into the same observable contract, run favorable and hostile cases, and return a capability matrix showing where each collapse idea is equivalent to known methods, genuinely useful as a representation/execution tool, or actively harmful.",
  "dependencies": [
    {
      "target": "RS-R025-MULTILAYER-COLLAPSE-POLICY-DYNAMICS-ATLAS",
      "action": "CONSUME_COLLAPSE_POLICY_DEFINITIONS_AND_PRECISION_EXPERIMENT_SCHEMA",
      "satisfied": true
    },
    {
      "target": "R021/R023 BRC Boolean-support semantic core",
      "action": "CONSUME_NO_RESURRECTION_AND_EXACT_SUPPORT_BOUNDARIES",
      "satisfied": true
    },
    {
      "target": "R014 representation-resource methodology",
      "action": "CHARGE_STATE_METADATA_WORK_AND_RECONSTRUCTION_HONESTLY",
      "satisfied": true
    }
  ],
  "source_refs": [
    "Euclidean algorithm / Euclidean remainder descent as classical solved arithmetic baseline",
    "LAPACK/Netlib iterative refinement and backward-error/residual methodology",
    "Netlib/PETSc multigrid restriction-residual-correction methodology",
    "NIST data-acquisition quantization and measurement-resolution studies",
    "classical projected/alternating-projection and operator-splitting convex benchmarks",
    "exact/reference harmonic-oscillator and one-dimensional conservation benchmarks",
    "R025 collapse policies and residual-collapse proposal"
  ],
  "evidence_status": "SOLVED_PROBLEM_EXTERNAL_CALIBRATION_GATE",
  "last_progress_ref": "User proposed validating collapse ideas on already-solved mathematics, physics, and engineering problems before further foundational commitment",
  "last_progress_at": "2026-08-11T21:46:00+08:00",
  "hard_block": null,
  "tags": [
    "R026",
    "collapse-validation",
    "residual-collapse",
    "benchmark",
    "euclidean-algorithm",
    "iterative-refinement",
    "multigrid",
    "quantization",
    "projection",
    "oscillator",
    "engineering-calibration"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R026",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R026 — Solved-Problem Validation of Collapse Modes and Residual-Field Iteration

Status: `READY / P0 / FOUNDATIONAL_CALIBRATION / EXTERNAL GROUND-TRUTH BENCHMARK / NOT CANONICAL`

## 1. 母问题

进取数论当前已经拥有若干不同的坍缩解释：

- 向下端点投影；
- 向上端点投影；
- 就近/就远端点投影；
- 50/50 与按距离无偏的随机端点选择；
- BRC / 多世界 exact support；
- 余量坍缩：保留 `n - anchor` 或到坍缩场的距离并继续迭代；
- 场几何状态：不把绝对位置当唯一状态，而保留 basin address / gap / phase / residual 等局部坐标。

本任务不继续从体系内部论证哪一个“更自然”。它要问：

> 当这些思想被放进人类已经解决、答案或误差理论已经明确的问题里，它们分别会带来什么真实价值？

目标不是证明所有问题都适合坍缩，而是建立一张**能力/失效地图**。

如果一个模式只是已有算法的重新命名，要明确 rooting；如果一个模式在某类问题中能给出更小状态、更低工作、更强不变量或更自然的多层结构，则冻结这个 specialization；如果一个模式破坏收敛、守恒或最优性，则把失败边界当成结果。

---

## 2. 统一实验纪律

每个 benchmark 都必须同时提供：

1. `REFERENCE_SOLVER`：经典精确解、解析解、高精度解或公认稳定算法；
2. `GROUND_TRUTH_OBSERVABLE`：最终答案、误差、守恒量、最优值、可行性、轨迹或已知复杂度；
3. `COLLAPSE_ADAPTER`：明确说明坍缩作用在什么对象上；
4. `STATE_ACCOUNTING`：主状态、residual、branch token、precision、cache、metadata 全部计费；
5. `KILL_TEST`：至少一个预计该坍缩模式会输的 hostile case；
6. `ROOTING`：与经典方法同构/近似时要明确指出，而不是改名宣称新算法。

每项结果至少报告：

- correctness / final error；
- iterations；
- arithmetic work proxy；
- state dimension / bytes；
- residual norm or field distance；
- bias / variance when stochastic；
- invariant violation；
- convergence or termination depth；
- reconstruction cost；
- sensitivity to precision and problem conditioning。

---

## 3. 必须比较的 Enterprise collapse families

定义统一候选族：

### C0 — DOWN_PROJECTION

落到声明场中的下方 anchor。

### C1 — UP_PROJECTION

落到上方 anchor / conservative enclosure。

### C2 — NEAREST_PROJECTION

落到最近 anchor。

### C3 — FAR_PROJECTION

落到最远端点，用作 adversarial/extremal control。

### C4 — UNIFORM_ENDPOINT_RANDOM

两个端点等概率。

### C5 — UNBIASED_DISTANCE_RANDOM

端点概率按距离选择，使单步期望在可证明条件下保持原状态。

### C6 — RESIDUAL_COLLAPSE

`state -> state - selected_anchor` 或对应约束/方程 residual；下一轮以 residual 为主要推进对象。

### C7 — ANCHOR_PLUS_RESIDUAL

不丢信息，保留 `(anchor,residual)`；研究是否存在更低成本的分层计算。

### C8 — FIELD_COORDINATE

保留 basin/field address、gap、phase、distance 等任务相关局部坐标，而非全绝对坐标。

### C9 — BRC_SUPPORT

当前信息不足时保留 exact alternative support；只在目标语义是 Boolean/result support 时允许无损 union recoalescence。

不是每个 benchmark 都要求所有 C0–C9 有意义；无意义的 adapter 必须标成 `TYPE_MISMATCH`，不能硬套。

---

## 4. Benchmark A — Euclidean GCD / classical remainder descent

这是余量思想的第一校准场，但必须防止“因为长得像就宣布成功”。

给定正整数 `a >= b > 0`，经典 Euclidean step：

`a = q*b + r`, `0 <= r < b`,

然后 `(a,b) -> (b,r)`。

任务：

1. 把 quotient/bulk 与 residual 分解映射到 Enterprise `anchor + residual` 语言；
2. 对比普通 `%` remainder、下 anchor residual、nearest multiple residual、balanced/signed remainder；
3. 比较 termination depth、coefficient growth、signed-state burden；
4. 测试 Fibonacci worst cases；
5. 对 extended GCD 同时检查 Bezout coefficient reconstruction；
6. 明确哪些只是 Euclidean-domain prior art，哪些可能给出更一般 collapse-field design principle。

核心问题：

> “余量作为下一状态”究竟是 p-th-power field 的特殊新结构，还是 Euclidean descent 的更一般模板？

成功不等于比经典 GCD 更快；如果能够抽出一个跨不同 field 的 well-founded residual descent criterion，也算高价值结果。

---

## 5. Benchmark B — quantization / ADC / fixed-point rounding

这是区分 DOWN / UP / NEAREST / RANDOM / UNBIASED 的最干净工程基准。

构造可精确控制的输入：

- uniform ramp；
- constant offset；
- sinusoid；
- slowly varying signal；
- adversarial values clustered near thresholds。

对每种 policy 测量：

- mean error / bias；
- mean squared error；
- max error；
- cumulative-sum drift；
- spectral distortion where appropriate；
- repeated-quantization drift；
- precision-bit scaling。

必须单独验证：

- `NEAREST` 是否在其经典 MSE 目标上占优；
- `DOWN` 是否产生系统负偏；
- `UP` 是否产生系统正偏；
- `50/50` 是否只在 basin midpoint 才无偏；
- distance-weighted stochastic rule 是否在明确条件下保持期望；
- residual/error-feedback state 能否消除长期积分漂移。

这条 benchmark 的意义是：如果一种坍缩在量化领域只是标准 rounding/stochastic rounding/error feedback，则要诚实 rooting；但其成功/失败模式可以反过来校准 Enterprise collapse policy。

---

## 6. Benchmark C — numerical summation / lost-detail compensation

选择 exact-integer or high-precision ground truth 的长序列求和。

基线：

- naive finite-precision sum；
- pairwise sum；
- compensated/Kahan-like error carry；
- exact rational/integer accumulator where feasible。

Enterprise adapters：

- 每步直接投影后丢 detail；
- `(coarse sum, residual)` 双状态；
- residual-only correction channel；
- stochastic unbiased rounding。

测量：

- absolute/relative error；
- error growth with sequence length；
- cancellation-heavy sequences；
- monotone positive sequences；
- state cost；
- correction work。

关键问题：

> `anchor + residual` 是否只是 compensated arithmetic 的重述，还是能给出更通用的 collapse bookkeeping law？

---

## 7. Benchmark D — linear systems and iterative refinement

使用可控 condition number 的小/中型线性系统 `Ax=b`，reference 用高精度/可靠 direct solve。

经典 refinement 结构：

`x_k -> residual r_k=b-Ax_k -> solve correction d_k -> x_(k+1)=x_k+d_k`。

测试：

1. low-precision coarse solve + high-precision residual；
2. coarse solve + quantized residual；
3. residual as primary iteration state；
4. anchor+residual split of solution vector；
5. nearest/down/stochastic quantization of correction；
6. ill-conditioned hostile matrices。

输出：

- forward error；
- backward error；
- residual norm；
- convergence depth；
- precision schedule；
- failure threshold versus conditioning。

核心判定：

如果 residual-collapse 语言自然复现 iterative refinement，它应被归类为 `ROOTING_SUCCESS / RESIDUAL_CORRECTION_PATTERN`；只有额外的可复用 theorem/tool residue 才属于 Enterprise specialization。

---

## 8. Benchmark E — multigrid / coarse-to-fine residual correction

选择有解析解或高精度离散解的一维/二维 Poisson boundary-value problem。

必须比较：

- fine-grid relaxation baseline；
- coarse restriction without residual correction；
- residual restriction + coarse correction + prolongation；
- Enterprise down/up/nearest state restriction variants；
- explicit residual-state multilevel representation；
- optional BRC support only where a genuine set-valued uncertainty is present。

记录每个 level：

- error norm；
- residual norm；
- high/low-frequency error decomposition if feasible；
- state count；
- smoothing work；
- correction work；
- convergence factor。

这是检验“多层全部往下坍缩”与“下去只处理 residual，再把 correction 带回来”是否本质不同的核心工程题。

---

## 9. Benchmark F — convex projection / feasibility

使用解析 ground truth 或可高精度验证的简单 convex sets：

- interval/box；
- halfspaces；
- intersecting disks/balls；
- simple quadratic objective over a box；
- two-set alternating projection cases。

测试：

- nearest projection；
- one-sided/down enclosure；
- far projection hostile control；
- residual/displacement vector作为下一状态；
- alternating projections；
- BRC when active constraint identity is unresolved。

测量：

- feasibility residual；
- objective gap；
- distance to exact solution set；
- iteration count；
- cycling/nonconvergence；
- active-set information burden。

此 lane 主要用于回答：

> “到坍缩场的距离”是否更像 residual/constraint violation，而不是一个自然数特有概念？

---

## 10. Benchmark G — harmonic oscillator finite-precision physics

用简谐振子作为已解物理基准：解析解已知，总机械能在理想连续模型中守恒。

不要求宣称任何新的物理理论；这里只把它作为数值/状态表示压力测试。

比较同一积分器下不同 collapse/quantization policies：

- down；
- up；
- nearest；
- unbiased stochastic；
- anchor+residual error-feedback；
- variable precision schedule。

测量：

- phase error；
- amplitude error；
- energy drift；
- long-horizon bias；
- variance；
- precision dependence。

如果向下策略持续耗散、向上持续注能、nearest 降低局部误差、unbiased stochastic 把系统漂移转成方差，这些都是非常有辨识力的 calibration results。

---

## 11. Benchmark H — one-dimensional collision / conservation test

使用解析可解的两体一维碰撞作为第二个物理校准题。

在 exact real/rational reference 之外，对碰撞前后速度/冲量施加不同有限精度 collapse policy。

检查：

- total momentum error；
- kinetic energy error for elastic case；
- restitution constraint；
- systematic bias over repeated collisions；
- residual impulse bookkeeping 是否能够精确守恒某个量；
- BRC support 与 actual physical uncertainty 是否被正确区分。

任何为了保持某一守恒量而偷偷把丢失信息藏进免费 metadata 的实现都判失败。

---

## 12. Benchmark I — rasterization / accumulated geometric error

加入一个非常离散的工程基准：在整数像素格上逼近给定直线/斜率，ground truth 为连续直线与离散像素选择准则。

比较：

- 每步只看绝对坐标重新取整；
- nearest pixel；
- down/up directional rasterization；
- accumulated residual/error state；
- phase-only / distance-to-grid state。

测量：

- max geometric deviation；
- endpoint error；
- step isotropy；
- integer operation count；
- state size。

这个 benchmark 用来测试一个非常强的猜想：

> 在某些离散动力学中，真正需要迭代的不是绝对坐标，而是“距离下一条离散边界还有多少”的 residual/phase。

若结果仅重现经典 incremental rasterization/error-accumulator 思想，要明确 prior-art rooting。

---

## 13. 必须设置的 hostile controls

至少包括：

1. nearest 应天然占优的单步平方误差任务；
2. down 应天然占优的安全下界/不超调任务；
3. up 应天然占优的 conservative upper enclosure 任务；
4. residual 不足以决定未来的 path-dependent system；
5. same residual but different anchor 导致不同 future 的反例；
6. stochastic unbiased but variance unacceptable 的任务；
7. BRC support exact but multiplicity/provenance observable 导致 carrier 不足的任务。

这些 controls 的目标是阻止“一个坍缩模式包打天下”的错误结论。

---

## 14. 统一价值分类

每个 collapse family × benchmark 的最终格子必须落在以下之一：

- `DOMINATES_REFERENCE_ON_DECLARED_RESOURCE_AXIS`；
- `PARETO_ALTERNATIVE`；
- `EQUIVALENT_TO_KNOWN_METHOD`；
- `USEFUL_COORDINATE_ONLY`；
- `SEMANTICALLY_EXACT_BUT_NO_RESOURCE_GAIN`；
- `APPROXIMATE_ONLY`；
- `BIASED_BUT_USEFUL_FOR_ONE_SIDED_GOAL`；
- `FAILS_CONVERGENCE_OR_INVARIANT`；
- `TYPE_MISMATCH`。

“漂亮”不是价值分类。

---

## 15. 特别关注的跨领域候选规律

主动寻找但不要预设：

### H1 — Residual-State Principle

当问题具有 exact decomposition

`state = solved/coarse component + residual`

并且 future correction 能主要通过 residual factorize 时，residual 可能是比 absolute state 更自然的迭代坐标。

### H2 — Anchor Necessity Boundary

存在问题使相同 residual 配不同 anchor 产生不同未来；此时 residual-only 不完整，至少需要 `(anchor,residual)`。

### H3 — Projection/Correction Duality

“直接把 state 投影到 coarse field”与“保留 coarse anchor，只迭代 residual/correction”是两种资源配置，而非同一算法。

### H4 — Directional Bias Law

down/up 的系统方向性在多步系统里对应可测的耗散/注入、under/over enclosure 或 conservative bias。

### H5 — Unbiasedness Is Not Stability

零期望误差不推出低方差、长期稳定、守恒或收敛。

### H6 — Field-Distance Sufficiency

某些增量/局部系统的 future 可以通过 distance/phase 坐标 factorize，从而无需完整绝对位置；另一些系统会被最小反例杀死。

---

## 16. 实现与数据要求

建立统一 benchmark runner，建议：

`experiments/r026_collapse_external_benchmarks.py`

每个 benchmark 独立 adapter，但输出同一 schema。

机器结果至少包含：

- benchmark id；
- exact/reference method；
- collapse family；
- precision；
- problem size/condition parameters；
- initial state；
- terminal state；
- residual history summary；
- correctness/error metrics；
- invariant metrics；
- work/state-cost metrics；
- classification；
- prior-art/rooting note。

随机实验必须固定 seed，并把期望/方差性质与单次轨迹分开。

---

## 17. Required artifacts

返回至少：

1. `docs/R026_COLLAPSE_EXTERNAL_BENCHMARK_REPORT.md`；
2. `experiments/r026_collapse_external_benchmarks.py`；
3. focused tests；
4. machine-readable results JSON/CSV；
5. `R026_CAPABILITY_MATRIX.json`；
6. `R026_PRIOR_ART_ROOTING.md`；
7. 每个 benchmark 的 ground-truth contract；
8. hostile-control counterexample packet；
9. strongest surviving cross-domain law candidates；
10. 对 Driver 的明确结论：哪些 collapse ideas 应继续投资，哪些只保留为特殊模式，哪些应该降级或淘汰。

---

## 18. Return classes

允许并鼓励混合结论。

首选高价值返回：

`COLLAPSE_EXTERNAL_CALIBRATION_COMPLETE / RESIDUAL_STATE_REGIME_CLASSIFIED / POLICY_SPECIALIZATIONS_FROZEN / PRIOR_ART_ROOTED / NEW_TOOL_RESIDUE_ISOLATED / NOT_CANONICAL`

如果主要只是经典方法重述：

`ROOTING_SUCCESS / MOST_COLLAPSE_MODES_MAP_TO_KNOWN_NUMERICAL_OR_ENGINEERING_PATTERNS / LIMITED_ENTERPRISE_RESIDUE / NOT_CANONICAL`

如果余量坍缩跨领域明显 survives：

`RESIDUAL_COLLAPSE_CROSS_DOMAIN_TOOL_CANDIDATE / ANCHOR_NECESSITY_BOUNDARY_CLASSIFIED / RESOURCE_ADVANTAGE_DEMONSTRATED / NOT_CANONICAL`

如果 residual-only 被广泛杀死：

`RESIDUAL_ONLY_TOO_COARSE / ANCHOR_PLUS_RESIDUAL_REQUIRED / FIELD_DISTANCE_NOT_GENERAL_STATE / NOT_CANONICAL`

最重要的验收问题：

> 在已经知道正确答案的人类问题上，哪一种坍缩让我们用更合适的状态、更少的信息或更清楚的多尺度结构得到正确结果？

如果答案是“没有”，也必须如实冻结。