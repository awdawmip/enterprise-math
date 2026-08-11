<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R031-LARGE-SCALE-PI-COLLAPSE-DIVERGENCE-ATLAS",
  "title": "R031 Large-Scale Pi Collapse Divergence Atlas and Machine-Field Crossover",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_STRESS_TEST",
  "frontier": "Use large-scale pi computations and circle-derived quantities to compare IEEE binary64's implicit dyadic precision field against exact big-integer/rational Enterprise collapse fields beyond 10^36, and determine when directional collapse creates stable discrete futures that are invisible to ordinary floating arithmetic.",
  "next_action": "Build exact scaled-pi and large-circle benchmark channels, measure binary64 ULP versus p-th-power basin gaps, inject collapse policies inside multiple pi algorithms rather than only at final output, sweep magnitude/exponent/policy, and return crossover laws, divergence phase maps, formula-consistency tests, and minimal counterexamples.",
  "dependencies": [
    {
      "target": "EnterpriseMath/Arithmetic/IntegerRoot.lean",
      "action": "CONSUME_EXACT_PTH_POWER_BASIN_CHARACTERIZATION",
      "satisfied": true
    },
    {
      "target": "RS-R025-MULTILAYER-COLLAPSE-POLICY-DYNAMICS-ATLAS",
      "action": "REUSE_POLICY_AND_PRECISION_TOWER_DEFINITIONS_WHERE_COMPATIBLE_WITHOUT_INHERITING_ITS_CONCLUSIONS",
      "satisfied": true
    },
    {
      "target": "R026 owner head 54219b11eae891f40013c081cad0b0e3034db7c5",
      "action": "USE_ONLY_AS_CLASSICAL_TARGET_CALIBRATION_AND_NEGATIVE_CONTROL_NOT_AS_FOUNDATIONAL_ARBITER",
      "satisfied": true
    }
  ],
  "source_refs": [
    "User correction on 2026-08-12: collapse research should allow intentionally different futures rather than score only agreement with continuous mathematics",
    "EnterpriseMath/Arithmetic/IntegerRoot.lean",
    "R025 exact multi-layer collapse policy model",
    "R026 classical solved-problem calibration as a limited comparison surface",
    "IEEE binary64 spacing/ULP as the conventional machine-precision comparison field"
  ],
  "evidence_status": "LARGE_SCALE_COLLAPSE_DIVERGENCE_AND_CROSSOVER_GATE",
  "last_progress_ref": "User proposed starting at 10^36-scale pi/circle arithmetic to compare double precision with Enterprise collapse futures and different collapse directions",
  "last_progress_at": "2026-08-12T07:22:00+08:00",
  "hard_block": null,
  "tags": [
    "R031",
    "pi",
    "large-number",
    "binary64",
    "ulp",
    "collapse-field",
    "directional-collapse",
    "precision-crossover",
    "p-th-power",
    "discrete-future"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R031",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:a03b06c1c6d29ca2776592fd12aa77406f45a21afb8fc1a8431b25cd41963c77",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R031 — Large-Scale Pi Collapse Divergence Atlas and Machine-Field Crossover

Status: `READY / P0 / FOUNDATIONAL STRESS TEST / LARGE-SCALE DISCRETE FUTURES / NOT CANONICAL`

## 1. 母问题

本任务不把“越接近连续高精度数学越正确”作为唯一评分标准。

进取数论的核心研究对象之一恰恰是：在有限精度和显式取舍下，不同坍缩政策可以产生与连续数学不同、但内部稳定、可复现、可分析的未来。

因此本任务问：

> 当绝对尺度从普通机器范围推进到 `10^36`、`10^48`、`10^72`、`10^100` 乃至更大时，IEEE binary64 自身的可表示数格点已经抹掉多少 p-th-power collapse-field 结构？在 exact big-integer/rational 表示中，DOWN / UP / NEAREST / FAR / stochastic / residual 等政策又会形成怎样的方向性偏移、分叉、重汇合、稳定数字前缀和算法依赖？

π 不是因为“连续 π 是裁判”而被选中，而是因为它同时提供：

- 一个稳定无量纲常数；
- 多种结构完全不同的计算算法；
- 圆周、面积、polygon bounds 等几何通道；
- 可以任意放大绝对尺度而保持宏观定义不变的测试场。

最终目标是建立：

**Large-Scale Collapse Divergence Atlas / 大数坍缩分歧图谱**。

---

## 2. 第一原则：把 binary64 也当作一种坍缩场

不要把普通双精度当作“连续数学本身”。

对任意有限 magnitude，binary64 只允许落在一个离散 dyadic lattice 上，默认 round-to-nearest 只是对这个 lattice 的一种选择政策。

为一个正数 `x` 定义：

- `ulp64(x)`：x 附近相邻 binary64 representable values 的间距；
- `F64(x)`：包围 x 的上下两个 binary64 lattice anchors；
- `phase64(x)`：x 在该 machine cell 中的位置。

因此比较对象不是：

`continuous mathematics vs strange collapse`

而是：

`dyadic machine collapse field vs Enterprise p-power collapse field vs arbitrary-precision reference coordinates`。

任意精度 reference 负责记录差异，不自动拥有“未来必须和它相同”的裁判权。

---

## 3. Enterprise p-th-power field

对 integer-scaled state `N` 与 `p>=2`：

`k=floorRoot_p(N)`

`L=k^p`

`U=(k+1)^p`

`G_p(N)=U-L`

`d=N-L`

`phi=d/G_p(N)`。

必须用 exact integer arithmetic 得到 `k,L,U,G,d`。

至少比较：

- `p = 2,3,4,5,6,8,10,12,16`；
- 必要时自适应扩大到更高 p；
- exact powers 必须保留 fixed-point behavior。

---

## 4. 关键新量：Machine/Collapse Resolution Ratio

定义：

`chi_p(N) = ulp64(N) / G_p(N)`。

解释：

- `chi_p < 1`：machine lattice 比 p-power anchor gap 更细；
- `chi_p ~= 1`：进入 crossover；
- `chi_p > 1`：一个 binary64 cell 已经跨越多个 p-power basins；
- `chi_p >> 1`：普通双精度在这个尺度上看不见大量 Enterprise collapse-field 局部结构。

对 fixed p 和大 N，攻击渐近候选：

`G_p(N) ~ p*N^(1-1/p)`，

从而

`chi_p(N) ~ epsilon64 * N^(1/p) / p`

（常数因 IEEE exponent cell 位置而有局部跳变）。

必须区分 exact local ULP 与渐近 envelope。

### 冻结 sanity target

以

`N_36 = floor(pi * 10^36)`

为初始 sanity point。

Driver 先验小算例显示：

- binary64 ULP 在该数量级约 `5.9e20`；
- square-field gap 约 `3.54e18`；
- 因而一个 binary64 step 约跨 `1.6e2` 个 square basins；
- cubic-field gap 则远大于 binary64 ULP。

研究员必须独立 exact 重算，不把这些数字当作证明输入。

寻找每个 p 的 crossover magnitude 和 staircase corrections，并确认 `10^36` 是否处在 p=2 已跨越、p>=3 尚未跨越的分区。

---

## 5. Magnitude sweep

至少使用 scale exponents：

`d = 12,16,20,24,30,32,36,40,48,64,72,96,100,128,150,192,256,300`。

定义：

`M_d = 10^d`

`Pi_d = floor(pi*M_d)`

并同时记录 nearest/ceiling integer encodings。

加入 `d=400,1000` 作为 arbitrary-precision-only regime，明确记录 binary64 已无法直接承载相应绝对值时发生的是 representation absence/overflow，而不是一个伪造的数值误差。

每个 d 记录：

- binary64 lower/upper representable anchors；
- exact ULP；
- 每个 p 的 `L,U,G,d,phi`；
- `chi_p`；
- 一个 machine cell 覆盖多少完整/部分 p-power basins；
- normalized gap `G/M_d`；
- directional-collapse normalized displacement。

---

## 6. Policy family

至少运行：

1. `DOWN`
2. `UP`
3. `NEAREST`
4. `FAR`
5. `PRNG_50_50`
6. `DISTANCE_WEIGHTED_STOCHASTIC`
7. `RESIDUAL_ONLY`
8. `ANCHOR_PLUS_RESIDUAL`
9. `FIELD_PHASE`
10. `ALL_ENDPOINTS` support baseline where the observable is set-valued

但本任务不假定哪一种“应该”回到连续 reference。

对每种 policy 记录：

- signed displacement；
- absolute displacement；
- normalized displacement；
- basin phase；
- direction-change count；
- future trajectory hash/signature；
- stable decimal/binary prefix length；
- policy pair separation；
- whether distinct policies later recoalesce；
- whether algorithm/channel changes the long-run policy ordering。

---

## 7. 三个 π 通道

只在最终 π 上做一次 rounding 不够。本任务必须区分三种完全不同的实验。

### Channel A — static scaled-pi field probe

直接对 high-precision `Pi_d` 做 machine-field / p-power-field resolution analysis。

目的：建立纯表示层 crossover atlas。

### Channel B — internal-collapse π algorithms

至少使用两种结构显著不同、能够独立高精度交叉验证的 π 算法，例如：

- Gauss-Legendre / AGM family；
- Chudnovsky or another rapidly convergent independent family。

在 fixed-point integer/rational state 中运行，并在明确 primitive boundaries 或 iteration boundaries 注入 collapse policy。

必须同时运行：

- collapse only at iteration boundary；
- collapse after selected nonlinear primitives；
- no-collapse arbitrary-precision reference。

目的不是只看最终 error，而是看：

- 第一次 policy divergence 在哪一层发生；
- divergence 是否随后扩大、缩小、翻向或 recoalesce；
- 哪些 digits/macroscopic ratios 在不同 future 中仍稳定；
- 同一 policy 在不同 π 算法上是否产生同一种 effective future。

如果 policy effect 强烈依赖算法结构，应记录 `ALGORITHM_RELATIVE_COLLAPSE`，不得强行解释成唯一自然常数。

### Channel C — large-circle geometry

使用 `R=10^d` 及附近扰动半径构造：

- circumference channel；
- area channel；
- polygon lower/upper-bound channel；
- 可行时加入 integer-lattice circle count / discrete-area channel。

从各通道恢复 effective pi：

`pi_C = C/(2R)`

`pi_A = A/R^2`

以及 polygon/discrete estimates。

核心观察：同一 collapse policy 是否保持跨公式一致，还是产生系统性的 formula defect。

定义：

`formula_defect = max pairwise distance among effective-pi channels under the same policy/scale`。

这比单纯对 continuous pi 的绝对误差更重要。

---

## 8. 必须攻击的候选规律

### H1 — binary64 itself is a collapse system

Machine rounding can be represented as endpoint selection on a scale-dependent dyadic field。

### H2 — machine-vs-p-field crossover law

For fixed p, `chi_p(N)` eventually grows like `N^(1/p)` up to dyadic staircase factors, so machine cells eventually cover multiple p-power basins。

### H3 — p=2 around 10^36 is already sub-machine structure

At `Pi_36`, square basins are substantially finer than binary64 spacing while at least the next several higher-p fields remain coarser。

### H4 — intrinsic-vs-machine granularity opposition

For fixed p, relative p-field gap `G_p(N)/N` decreases roughly like `N^(-1/p)`, while binary64 relative spacing remains order `2^-52`; therefore large scale can make the intrinsic field relatively smoother yet simultaneously make machine arithmetic blind to its local anchors。

### H5 — directional future separation

DOWN and UP may define persistent lower/upper future families rather than mere symmetric numerical error; test monotonic ordering and minimal counterexamples。

### H6 — macro agreement / micro divergence

Different policies may disagree strongly in field coordinates while sharing a long stable prefix in recovered π. Measure the stable-prefix law as scale increases。

### H7 — policy-specific effective constants

Under repeated internal collapse, an algorithm/policy pair may approach a stable effective value or interval distinct from the arbitrary-precision reference. Distinguish convergence, oscillation, periodicity, drift and nonconvergence。

### H8 — formula coherence

A meaningful collapse regime may preserve bounded or vanishing `formula_defect` across circumference/area/polygon channels even when its effective π differs from the continuous reference. Kill this if channel dependence remains macroscopic。

### H9 — scale covariance and power-factor effects

Changing `M` by exact p-th powers may preserve or predictably transform field phase/trajectory; non-p-power scale factors may alter them. Re-test rather than inheriting R025 conclusions。

### H10 — residual as one possible future, not protected information

Residual-only trajectories are allowed to produce genuinely different futures. Do not reject them solely because anchor reconstruction is impossible. Instead classify whether the resulting future has its own stable law, scale covariance or geometric consistency。

### H11 — irreversible information loss is an intended observable

Measure which distinctions disappear after each collapse and whether downstream macroscopic observables become simpler/stabler because of that loss. Do not score every irreversible loss as an error by definition。

### H12 — crossover dimension

Test whether `(magnitude d, exponent p, policy)` naturally partitions into regimes where machine precision dominates, Enterprise field dominates, or both are comparable; seek a low-dimensional phase boundary rather than a case list。

---

## 9. “不同未来”必须成为一级数据，而不是 error column

每一次实验至少输出两个并列视角：

### Reference-relative view

- difference from arbitrary-precision reference；
- stable digit prefix；
- absolute/relative deviation。

### Intrinsic-collapse view

- exact anchor sequence；
- exact residual/phase sequence；
- direction sequence；
- basin-index trajectory；
- recoalescence events；
- cycle/attractor/stabilization signatures；
- cross-formula consistency；
- scale covariance；
- state/work cost。

Reference-relative error 不得覆盖 intrinsic-collapse classification。

---

## 10. Binary64 comparator must be honest

不要简单说“double 只有 16 位所以失败”。

必须实际提取每个 scale 附近的：

- predecessor；
- representable value；
- successor；
- exact ULP；
- rounding direction；
- exponent transition discontinuities。

比较：

- binary64 default nearest；
- directed-down/up machine anchors where implemented exactly by bit/nextafter logic；
- exact arbitrary precision；
- Enterprise field policies。

必须区分 relative precision 与 absolute field resolution。

---

## 11. 大数以后继续扩展

`10^36` 是起点，不是结论。

如果 `p=2` 的 crossover 已在更低 scale 发生，则向上下各扩至少 6 个 decade checkpoints，定位 transition window。

对每个 p 自动估计 crossover scale，再在预测点附近密集采样。

对于 binary64 overflow 以后的规模，只继续 exact big-number Enterprise/reference channels，并记录 conventional machine representation 的断点，不做虚假的 extrapolated float。

---

## 12. ECC / finite-field route

用户明确提出 residual/collapse 思想可能更适合 ECC/finite-field arithmetic。

本任务只做一个**非攻击性数学接口说明**：

- 记录 finite-field / modular state 天然以 residue class 组织；
- 列出后续可验证的 point-addition / scalar-multiplication correctness、coordinate growth、field reduction、representation cost benchmark contract；
- 不把 ECC benchmark 混入 π 大数主实验，以免把有限域闭合语义与大尺度 real/fixed-point collapse 混成一个结果。

如果 R031 证明 large-scale field-resolution/collapse-future framework有辨识力，向 Driver 建议单独的 finite-field/ECC calibration task。

---

## 13. 数据产物

至少交付：

1. `R031_LARGE_SCALE_PI_COLLAPSE_REPORT.md`；
2. `R031_MACHINE_FIELD_CROSSOVER.json`；
3. `R031_PI_POLICY_DIVERGENCE.json`；
4. `R031_FORMULA_COHERENCE.json`；
5. exact experiment runner；
6. focused tests；
7. compact CSV/columnar export for plotting；
8. scale × p × policy phase atlas；
9. minimal counterexamples for every killed H1-H12 claim；
10. strongest surviving theorem candidates；
11. explicit recommendation on whether large-scale collapse deserves a new foundational lane。

Keep raw traces reproducible but do not explode source artifacts with unnecessary full dumps; store compact sufficient data and deterministic regeneration when possible。

---

## 14. 成功标准

成功不要求某个 policy 更接近 continuous pi。

成功至少满足其一：

- 找到 exact machine-field / p-field crossover law；
- 找到稳定的 direction-dependent future regime；
- 找到跨 π algorithms / circle formulas 保持的 collapse invariant；
- 找到 scale/exponent phase transition；
- 找到 residual-only or field-coordinate attractor/cycle/scaling law；
- 或证明这些现象严重 algorithm-relative，从而精确限制“自然坍缩”的主张。

优先正向返回：

`LARGE_SCALE_COLLAPSE_PHASE_STRUCTURE_FOUND / MACHINE_FIELD_CROSSOVER_CLASSIFIED / DIRECTIONAL_FUTURES_MEASURED / NOT_CANONICAL`

若没有统一结构但数据仍清楚：

`LARGE_SCALE_COLLAPSE_ALGORITHM_RELATIVE / NO_UNIVERSAL_DIRECTION / CROSSOVER_ATLAS_FROZEN / NOT_CANONICAL`

若大数层只复现普通 rounding 且无额外结构：

`LARGE_SCALE_COLLAPSE_NO_NEW_STRUCTURE / MACHINE_PRECISION_EXPLAINS_OBSERVED_EFFECTS / NOT_CANONICAL`

---

## 15. Driver-facing return

最终必须直接回答：

1. `10^36` 为什么特别或其实并不特别？
2. 在 `10^36`、`10^48`、`10^72`、`10^100` 上，binary64 一个 machine cell 分别覆盖多少 p=2,3,4... collapse basins？
3. 哪个 `(scale,p)` 是精确 crossover？
4. DOWN/UP/NEAREST/FAR 在大数内部迭代中是简单误差方向，还是形成稳定不同未来？
5. residual-only 是否出现可重复的吸引子、标度或公式一致性？
6. 同一 policy 在 Gauss-Legendre 与 Chudnovsky 中是否得到相同宏观结构？
7. circumference/area/polygon recovered pi 是否形成一致的 policy-specific effective constant/interval？
8. 大数 collapse-field 结构是否提供 binary64 无法表达的有效状态分辨率？
9. 下一步应该进入 finite-field/ECC、离散几何、物理大尺度，还是停止 foundational escalation？
