<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R046-ENGINEERING-SUCCESS-INVERSION-PI-CONSTRAINT-ATLAS",
  "title": "R046 Engineering-Success Inversion: Pi Constraint Atlas and Minimal Success Kernel",
  "kind": "RESEARCH",
  "owner": "program/foundational-logic-engineering-inversion",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_METHOD / PI / ENGINEERING_INVERSION",
  "frontier": "Invert the engineering success of classical pi-bearing mathematics into a definition-stripped set of empirical/operational constraints, identify which appearances are merely shared-definition descendants, and isolate the smallest cross-domain success kernel that a native theory would have to explain without importing classical definitions into its premises.",
  "next_action": "Build a provenance- and dependency-aware engineering-success atlas first; do not design or select a native collapse policy until the independent target constraints and their classical-definition dependencies have been separated.",
  "dependencies": [
    {
      "target": "FOUNDATIONAL_LOGIC.md + foundational_logic.json @ main",
      "action": "CONSUME_ENGINEERING_SUCCESS_INVERSION_AS_TOP_LEVEL_METHOD",
      "satisfied": true
    },
    {
      "target": "native_semantics_admissibility.json V3 @ main",
      "action": "CONSUME_NO_OUTPUT_COPYING_AND_FOUNDATION_CALIBRATION_SEPARATION",
      "satisfied": true
    },
    {
      "target": "R045 Draft PR #533 head 60f5798192da90982b66d5a1bbad47e43798050b",
      "action": "CONSUME_C05_C06_REPAIR_BOUNDARY_WITHOUT_REOPENING_NATIVE_PI",
      "satisfied": true
    }
  ],
  "source_refs": [
    "Engineering success of continuous mathematics is evidence to explain, not a license to inherit its definitions",
    "R045: bare metric-free N0 does not yet type a native-pi candidate class",
    "R038 conditional/readout pi-family remains valid evidence at its declared later strata"
  ],
  "evidence_status": "ENGINEERING_SUCCESS_INVERSION_AND_CONSTRAINT_EXTRACTION",
  "last_progress_ref": "Foundational logic V1 and Native-Semantics Gate V3 activated on main; R045 C05/C06 repair returned on Draft PR #533.",
  "last_progress_at": "2026-08-12T21:30:00+08:00",
  "hard_block": null,
  "tags": [
    "R046",
    "engineering-success-inversion",
    "pi",
    "effective-theory",
    "constraint-atlas",
    "explanatory-compression",
    "foundation-calibration-separation",
    "definition-leakage"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R046",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R046 — Engineering-Success Inversion: Pi Constraint Atlas and Minimal Success Kernel

Status: `READY / P0 / FOUNDATIONAL ENGINEERING INVERSION / NOT CANONICAL`

## 0. 母问题

连续数学在工程上长期成功，这是事实性证据；但本任务不把其定义继承到底层。

本任务只问：

> **经典数学中那些通常由 `pi`、圆、周期、旋转、积分归一化等结构统一表达的工程成功，去掉经典定义之间的相互借用后，究竟剩下多少彼此独立的现实约束？这些约束的最小共同核心是什么？**

目标不是证明 classical pi，也不是定义 native pi，而是先建立一个足够干净的 target surface，使后续 native theory / collapse 可以被要求“解释成功”，而不是“复制定义”。

核心反问题：

```text
observed engineering success
        ↓ strip inherited definitions / conventions
independent operational constraints
        ↓ dependency quotient
minimal success kernel
        ↓ only in a later task
candidate native explanations / collapse mechanisms
```

本任务停在 `minimal success kernel`。不得为了尽快得到 native collapse 而跳过 constraint extraction。

---

## 1. Frozen semantic boundary

消费但不重做 R045：

- bare metric-free relational N0 尚未声明 native-pi candidate class；
- `pi` 的 existence / uniqueness / role / nonexistence 在 bare N0 均不能被直接假定；
- 经典几何、metric、periodic phase、Fourier/Gaussian/integral normalization 等若被使用，只能作为 effective-theory / engineering-side 描述或待剥离依赖；
- R038 已得到的 later-stratum readout 数学可以作为历史样本，但不能当作底层结论。

### 1.1 两个严格分开的输入面

**Engineering evidence side** 可以记录：

- 实际工程协议；
- 控制量与测量量；
- 工作尺度；
- 误差/容差包络；
- 经典理论如何表达该成功；
- 该表达中 pi 出现的位置。

**Native explanatory side** 在本任务中保持空白，不预置：

- center；
- distance / equidistance；
- radius；
- circle/sphere primitive；
- angle/radian primitive；
- Euclidean measure；
- continuum point set；
- classical pi value；
- 任何为复现 output 而专门抄入的等价定义。

本任务不是让 researcher 选择 collapse，而是先把未来 collapse 要解释的 target 做干净。

---

## 2. 第一主攻：建立 Engineering-Success Atlas

至少覆盖以下**候选来源族**，允许经 prior-art/engineering audit 后合并、拆分或删除：

1. **round-object / rotational mechanical engineering**：圆形构件、旋转件、滚动/传动/加工/测量中 classical pi-bearing 关系；
2. **periodic phase / oscillation / signal engineering**：周期、角频率、相位闭合、谐振中 `2pi` 类表达；
3. **Fourier / spectral normalization**：频域/波数/变换规范中 pi 的出现；
4. **diffusion / Gaussian / heat / noise normalization**：连续概率密度、扩散核、热核等工程模型中的 pi；
5. **wave / boundary-value / modal engineering**：边界条件、波导/谐振/模态中与 pi 相关的稳定预测；
6. **area/volume/flow/capacity readouts of nominally round geometries**：作为与 1 不同的 observable family 检查，避免把同一几何定义重复计票。

对每个候选成功项必须生成一行 typed record：

```text
success_id
engineering_domain
physical_or_engineering_protocol
controlled_inputs
measured_outputs
scale_regime
tolerance_or_error_envelope
classical_effective_formula
where_pi_appears
classical_definitions_required
unit_or_coordinate_conventions_required
upstream_mathematical_dependencies
empirical_independence_from_other_rows
what_survives_after_definition_stripping
status
sources
```

### 2.1 不把“公式用了 pi”当作独立成功

一个 success row 必须对应可区分的工程/实验约束，而不是仅仅某个教材公式。

如果两个 row 的成功实际上来自同一个 upstream continuum theorem、同一个几何定义或同一个单位约定，必须在 dependency graph 中连起来，后续 quotient 时不能算成两个独立证据。

---

## 3. 第二主攻：Definition-Stripping

对每一行经典成功，逐层删除：

1. 纯符号/单位约定；
2. classical definition；
3. 由同一 classical definition 直接推出的重复结果；
4. continuum-specific representation；
5. 只在特定坐标/normalization convention 下出现的 pi 因子。

保留最弱的 operational statement，例如：

```text
给定某种可重复工程操作和输入控制，
某组输出在某尺度内满足某种稳定的无量纲关系 / 闭合关系 / 相位关系 / 误差包络。
```

这里“无量纲”“闭合”等词如果仍依赖额外定义，也必须继续展开其 measurement protocol；不得用抽象词掩盖未剥离的结构。

### 3.1 Pi-role classification

每个 pi appearance 至少归入以下之一，若不够则扩展 taxonomy：

- `PURE_CONVENTION_OR_COORDINATE_NORMALIZATION`；
- `DESCENDANT_OF_CLASSICAL_GEOMETRIC_DEFINITION`；
- `DESCENDANT_OF_PERIODIC_PHASE_DEFINITION`；
- `CONTINUUM_MEASURE_OR_INTEGRAL_NORMALIZATION`；
- `SPECTRAL_TRANSFORM_NORMALIZATION`；
- `CROSS_DOMAIN_OPERATIONAL_REGULARITY`；
- `UNRESOLVED_MIXED_ORIGIN`。

目标是防止把“同一个 classical pi 定义在多个公式里出现”误认成独立证据。

---

## 4. 第三主攻：构造 dependency quotient

把 atlas 看成有向依赖图：

```text
classical definitions / conventions / theorems
        ↓
engineering prediction rows
        ↓
observed success constraints
```

对 success rows 做 quotient：如果两行在移除同一 upstream definition/theorem 后只剩同一个 operational constraint，则合并为一个 evidence class。

必须区分：

- `same formula family`；
- `same classical definition descendant`；
- `same engineering apparatus`；
- `empirically independent protocol`；
- `mathematically independent effective-theory route`。

最终返回：

```text
RAW_SUCCESS_COUNT
DEFINITION_STRIPPED_COUNT
DEPENDENCY_QUOTIENT_COUNT
CROSS_DOMAIN_INDEPENDENT_COUNT
```

这些计数本身不是重点；重点是给出可审计的 quotient witness。

---

## 5. 第四主攻：最小 Engineering-Success Kernel

从 quotient 后 evidence classes 中寻找一个尽可能小的集合 `K_eng`，使它满足：

1. 跨至少三个真正不同的 engineering protocol families；
2. 不能由一个共享的 classical definition 直接同时生成；
3. 每项都有现实的 scale/tolerance 语义；
4. 任意未来 native theory 若声称“解释 classical pi 的工程成功”，至少必须解释 `K_eng`；
5. 删除 kernel 中任意一个成员，应明确失去哪一类独立解释压力。

不要假定 `K_eng` 一定唯一。允许返回 Pareto family：

```text
minimal cardinality
minimal shared-definition debt
maximal cross-domain coverage
maximal empirical independence
```

### 5.1 Explanatory Compression score 只作排序，不作真理定义

可以提出一个透明的候选指标，例如：

```text
explained independent constraints
---------------------------------
native assumptions + imported effective definitions
```

但本任务没有 native candidate，因此只允许定义**未来评价协议**，不得虚构数值排名。

---

## 6. 强制 adversarial controls

必须至少攻击以下错误路线：

### A. `PI_FREQUENCY_IS_EVIDENCE`
公式里 pi 出现次数多，不代表独立现实证据多。

### B. `SHARED_DEFINITION_DOUBLE_COUNT`
圆周、面积、体积、转动等若通过同一个 classical geometric primitive 直接联系，不能自动算成多个 independent constraints。

### C. `RADIANS_AS_PHYSICS`
`2pi` 出现在相位/角频率表示中，必须区分单位/参数化约定与真正可测闭合关系。

### D. `FOURIER_NORMALIZATION_AS_NATIVE_CONSTANT`
不同 Fourier convention 可移动 `2pi` 因子；必须剥离 convention 后再判断剩余 physical constraint。

### E. `GAUSSIAN_NORMALIZATION_AS_NATIVE_PI`
连续积分 normalization 的 pi 不能未经分析就当成底层证据。

### F. `OUTPUT_COPYING`
不得从“经典工程上圆很好用”直接把 circle/radius/equidistance 放进未来 native premise。

### G. `ONE_NUMBER_FIT`
未来某个 native model 即使产生接近 `3.14159...` 的数，也不能凭这一点宣称解释成功；必须覆盖 cross-domain kernel。

---

## 7. 与 cell / collapse 线的接口

本任务只定义下一任务要解释的 constraints，不指定 cell growth 的正确规则。

但必须输出一个 machine-readable `NATIVE_EXPLANATION_INTERFACE`，格式至少包含：

```text
constraint_id
allowed_native_inputs = UNSPECIFIED
forbidden_imported_effective_definitions
required_observable_protocol
required_scale_range
required_tolerance
composition_requirements
cross_constraint_shared_state_allowed?
```

下一任务可以让多个 native collapse / growth candidates 接口化地尝试解释 `K_eng`。

如果 R046 发现 classical pi 的工程成功其实分裂成多个彼此无共同 operational core 的 evidence families，也必须如实返回；不得强行制造统一常数。

---

## 8. Required deliverables

至少返回：

1. `R046_ENGINEERING_SUCCESS_ATLAS.json`；
2. `R046_CLASSICAL_DEPENDENCY_GRAPH.json`；
3. `R046_DEFINITION_STRIPPED_CONSTRAINTS.json`；
4. `R046_DEPENDENCY_QUOTIENT.json`；
5. `R046_MINIMAL_SUCCESS_KERNEL.json`；
6. `R046_NATIVE_EXPLANATION_INTERFACE.json`；
7. `R046_PRIOR_ART_AND_ENGINEERING_SOURCES.md`；
8. `R046_REPORT.md`；
9. 至少一组 leakage/double-counting adversarial tests 或 checker。

所有来源要区分：

- empirical/engineering evidence；
- standard/classical mathematical derivation；
- convention/normalization；
- prior-art interpretation；
- R046-new decomposition/quotient。

---

## 9. Candidate hypotheses

全部允许被杀。

### H1 `SMALL_SUCCESS_KERNEL`
classical pi-bearing engineering success 在 definition stripping 和 dependency quotient 后，存在一个远小于 raw formula family 的 cross-domain success kernel。

### H2 `PI_APPEARANCE_MOSTLY_DEPENDENT`
大量 pi appearance 并非独立证据，而是少数 shared definitions / continuum normalizations 的后代。

### H3 `CROSS_DOMAIN_RESIDUAL_SURVIVES`
剥离 convention 和 shared definitions 后，仍存在至少两个或三个真正跨域的 operational constraints，需要某个共同底层结构解释。

### H4 `NO_SINGLE_PI_ROLE`
经典 pi 在不同工程域中的 role 可能并不统一；统一常数可能属于 effective-theory compression，而不是单一 native primitive。

### H5 `ENGINEERING_SUCCESS_KERNEL_SUFFICIENT_FOR_NEXT_CALIBRATION`
可以形成一个不包含 classical definition leakage 的 target interface，供下一任务比较 native collapse/growth candidates。

---

## 10. 成功 / kill / return 分类

优先返回以下之一：

`ENGINEERING_SUCCESS_KERNEL_FOUND / DEFINITION_STRIPPED_CROSS_DOMAIN_CONSTRAINTS_FROZEN / NEXT_NATIVE_EXPLANATION_TASK_READY / NOT_CANONICAL`

或：

`PI_ENGINEERING_SUCCESS_DECOMPOSES_INTO_MULTIPLE_NONUNIFIED_FAMILIES / NO_SINGLE_SUCCESS_KERNEL / NEXT_TASK_MUST_BE_MULTI_TARGET / NOT_CANONICAL`

或：

`CLASSICAL_PI_SUCCESS_MOSTLY_DEFINITION_OR_CONVENTION_DEPENDENT / INDEPENDENT_ENGINEERING_RESIDUAL_SMALL / NOT_CANONICAL`

允许发现更小的新对象并替换 `K_eng` 语言。

---

## 11. Driver return boundary

本任务完成时必须明确回答：

1. 多少 classical pi-bearing success 是同一 shared definition 的重复后果？
2. 去掉这些重复后，剩下哪些真正独立 engineering constraints？
3. 是否存在 small cross-domain success kernel？
4. 哪些 pi appearance 只是 convention/normalization？
5. 下一轮 native collapse/growth candidate 到底必须解释什么，而不是必须复现什么定义？

本任务不得宣称已经找到 native pi 或正确 collapse；它只负责把**要解释的工程成功**变成干净、最小、可审计的 target surface。
