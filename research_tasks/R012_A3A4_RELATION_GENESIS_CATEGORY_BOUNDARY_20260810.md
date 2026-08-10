<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY",
  "title": "R012 A3/A4 Relation Genesis and Categorical Boundary",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Determine whether canonical A3 weighted relation-state and A4 multivalued correspondence are merely arithmetic specializations of existing relation/category/process mathematics, or whether Enterprise Math has a genuinely stronger generative claim in which relation structure and object identity arise intrinsically from primitive finite dynamics rather than being supplied exogenously.",
  "next_action": "Freeze the exact canonical A3/A4 interfaces, construct the strongest faithful translation into standard relation/category/process-theory formalisms, classify what is pure prior-art language versus Enterprise-Math-specific arithmetic structure, then prove either a primitive-dynamics relation-genesis theorem or a no-go showing which additional primitive is mathematically necessary. Do not open the Bell/quantum-native branch until this boundary is resolved.",
  "dependencies": [
    {"target": "canonical A3 weighted relation-state core", "action": "CONSUME", "satisfied": true},
    {"target": "canonical A4 correspondence/support core", "action": "CONSUME", "satisfied": true},
    {"target": "canonical FQ-004 A1/A2 functional-kernel layering boundary", "action": "CONSUME", "satisfied": true},
    {"target": "A3/A4 generated-support bridge", "action": "INFORM", "satisfied": true},
    {"target": "A4/P023 relation-observable powerset bridge", "action": "INFORM", "satisfied": true},
    {"target": "R004 finite Bell/CHSH pressure-test return", "action": "INFORM", "satisfied": false}
  ],
  "source_refs": [
    "research_tasks/R012_A3A4_RELATION_GENESIS_CATEGORY_BOUNDARY_20260810.md",
    "research_common_surface.json",
    "src/enterprise_math/weighted_relation_field.py",
    "src/enterprise_math/relation_lattice.py",
    "src/enterprise_math/relation_scale.py",
    "src/enterprise_math/admissible_support.py",
    "src/enterprise_math/relational_spectrum.py",
    "PR #192 A3/A4 generated-support bridge",
    "PR #368 / #425 A4-P023 relation-observable bridge",
    "PR #302 R004 Bell/causal-identifiability pressure test",
    "external:enterprise_math_discussion.zip#sha256=8278b1af84b62b49d957cbc205aa8b90c5b786b3b7671350c61a8c263827d3f7"
  ],
  "evidence_status": "FOUNDATIONAL_POSITIONING_AND_GENERATIVITY_PRESSURE_TEST",
  "last_progress_ref": "driver review of independent external A3/A4 audit",
  "last_progress_at": "2026-08-10T19:30:00+08:00",
  "hard_block": null,
  "tags": ["R012", "A3", "A4", "relation", "correspondence", "category-theory", "process-theory", "relation-genesis", "object-identity", "prior-art", "foundation"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED"
}
-->

# R012 — A3/A4 关系生成与范畴定位

Status: `CANDIDATE RESEARCH HANDOFF / FOUNDATION POSITIONING / NOT CANONICAL`

## 0. 任务定位

本任务不问“Enterprise Math 有没有关系”，也不问“范畴论是否存在”。这两个问题都已经没有研究价值。

当前 canonical 架构已经明确：

- A3：结构化带权整数关系态、partition quotient/kernel、relation scale/rank、refinement memory；
- A4：多值 support/correspondence、composition、common targets、split-completeness、witness/group spectra；
- A1/A2 functional kernel 不自动等于 A3/A4；没有 reduction theorem 时必须保持分层。

本任务真正要回答两个更尖锐的问题：

> **Q1. 把 A3/A4 的术语全部剥掉以后，它们是否完全落入已有的 relation algebra / `Rel` / enriched relation / process-theory / categorical machinery，只剩一个算术实例？**

以及：

> **Q2. Enterprise Math 能否从更低层的 primitive finite dynamics 内生地产生 relation、correspondence 甚至 object identity，而不是把这些结构作为额外原语声明？**

只有 Q2 出现严格生成定理，或者 A3/A4 的整数约束产生标准框架没有自动给出的 sharp theorem，才可能形成真正的项目特异性。

方向可以激进，证据必须残酷。

---

# 1. 必须冻结的 canonical 输入

不要重做以下数学，只核准接口并消费：

## A3

Canonical relation coordinate：

\[
Z_{ij}=m_jc_i-m_ic_j.
\]

现有 A3 core 包含：

- weighted relation field；
- exact partition coarsening；
- relation lattice / reconstruction；
- relation quantum 与 primitive capacity；
- relation scale/carry；
- spanning-tree sparse relation lattice 后续结构。

## A4

Canonical finite correspondence core 包含：

- finite relation composition；
- converse；
- common-target structure；
- radius-family diagnostics；
- split-completeness；
- witness spectrum `W_k`；
- source-group spectrum `G_k`；
- total-function degeneration到 A1/P011 collision spectrum。

## 已有 bridge

A3/A4 bridge 已研究从 A3 relation threshold 生成 A4 support，以及 cancellation 导致 coarse converse 失败的边界。

A4/P023 bridge 已研究：

\[
\Sigma_{(R,O)}(x)=\{O(y):(x,y)\in R\}
\]

以及 powerset compiler，把 raw relation words 编译成 deterministic support dynamics，但明确丢失 path multiplicity、branch identity 和 intermediate definedness。

本任务不得把这些已有桥重新命名成新发现。

---

# 2. 第一主问题：最强 categorical reduction

目标不是找“像不像范畴论”，而是构造**最强可能的严格翻译**。

至少比较：

- category `Rel`：对象为集合、态射为 binary relations、组合为 relational composition；
- allegory / relation algebra；
- quantale / weighted relation / enriched-category 表述；
- spans / profunctors / distributors（若适用）；
- symmetric monoidal / dagger process theories；
- categorical quantum mechanics 中 sets-and-relations、stochastic maps 与 operational models 的位置。

对 A3 与 A4 分别建立 translation table：

```text
Enterprise object
-> standard categorical/relation object
-> exact preservation
-> information lost
-> extra arithmetic constraint
```

必须检查：

1. A4 composition/converse/common-target 是否只是 `Rel` 中普通组合/反向；
2. A4 witness spectrum 是否只是 path/witness multiplicity 的标准 enrichment；
3. A3 的 `Z_ij` 是否只是 state vector 的 antisymmetric pair-observable / linear image；
4. relation lattice 是否只是 integer lattice / incidence / Smith-type structure；
5. relation scale 是否只是一个 valuation/filtration/graded structure；
6. A3→A4 threshold support 是否只是一个 functor / forgetful map / support map；
7. A4→P023 powerset compiler 是否就是 subset construction / relational image 的标准确定化。

如果完整 reduction 成立，明确标：

`GENERIC_STRUCTURE_IS_PRIOR_ART`

不要试图保住“新术语”。

---

# 3. 需要的 verdict：替代、实例、还是生成层？

不要使用“Enterprise Math 替代范畴论”这种模糊说法。

范畴论首先是一种高层结构语言，本任务要分类 A3/A4 与它的关系：

### Class C0 — RENAMING ONLY

A3/A4 的核心对象、定理和组合全部是标准结构的直接改名，没有独立算术内容。

### Class C1 — ARITHMETIC SPECIALIZATION

一般结构是 prior art，但 integer/floor/collapse/scale 约束产生新的 sharp special theorem、index、rigidity、no-go 或 executable classification。

### Class C2 — GENERATED SUBTHEORY

存在一个从 Enterprise Math primitive dynamics 到 relation/process structure 的明确生成函子/closure，A3/A4 不是独立输入，而是 lower-layer dynamics 的派生层。

### Class C3 — STRICT EXTRA STRUCTURE

即使放进成熟 categorical language，仍有不能由 generic categorical axioms 自动推出的 Enterprise-specific primitive/constraint，并且它产生可检验的新数学结果。

最终必须给出准确等级，而不是宣传性结论。

---

# 4. 第二主问题：Relation Genesis

当前最大的结构风险是：

> A3/A4 如果只是先给一个 relation，再研究 relation，那么“关系优先”并没有被 lower-layer primitive dynamics 导出。

因此要求从 A0/A1/A2 可用对象出发，尝试产生 relation。

候选来源可以测试，但不得预设成功：

## 4.1 History-merge genesis

\[
x\sim_t y
\iff
F_t(x)=F_t(y).
\]

它天然产生 equivalence/kernel。

问题：

- 这是否最多停留在 A1/A2 functional-kernel 层？
- 什么额外数据才能升级成有方向、有权、非对称、多值的 A3/A4 relation？
- 是否存在 no-go：仅靠 deterministic functional kernels 无法生成 generic A3/A4 structure？

## 4.2 Future-language genesis

由 future signature：

\[
\Sigma_W(x)
\]

产生 behavioral relation。

检查它究竟是 equivalence、preorder、simulation、bisimulation，还是能自然生成 A3/A4 richer relation。

## 4.3 Transition-incidence genesis

从 primitive transitions：

\[
x\to y
\]

的 occurrence / multiplicity / cost / merge structure 构造 pair relation。

要求回答：

- direction 从哪来？
- weight 从哪来？
- sign 从哪来？
- composition law 从哪来？
- relation scale 从哪来？

## 4.4 A3-specific genesis

检验 canonical

\[
Z_{ij}=m_jc_i-m_ic_j
\]

究竟是：

- primitive relation；
- 从单体 state/capacity 派生的 pair observable；
- 一个坐标变换；
- 某个 universal invariant；
- 或某种 exterior/difference construction 的整数特例。

如果它只是从 `m,c` 派生，则必须诚实区分：

> “relation is represented explicitly”

与

> “relation is ontologically primitive / dynamically generated”。

---

# 5. 第三主问题：Object Identity Genesis

外部审核提出：

> 对象不一定先存在；对象可以是历史稳定模式。

这必须数学化，而不是哲学口号。

至少比较并测试以下候选：

- fixed points；
- attractor/stable classes；
- eventual behavioral equivalence；
- recurrent components；
- idempotent splittings；
- minimal future-safe quotients；
- process-history equivalence classes。

目标：

构造一个最小有限系统，使“对象身份”不是初始标签，而是由 dynamics 生成的稳定 equivalence/class。

然后问：

1. 这种 object genesis 是否只是标准 automata / coalgebra / dynamical-system quotient；
2. 它是否与 A3/A4 relation state 相容；
3. object 与 relation 谁先生成；
4. 是否出现循环定义：要定义 dynamics 已经先需要 object/action labels；
5. 是否需要一个真正更底层的 primitive event/incidence layer。

寻找最小 no-go 或最小 positive construction。

---

# 6. Process-first 不是默认创新

必须主动攻击以下叙述：

> “我们从过程出发，所以不同于集合论/范畴论。”

现有 process theories / categorical quantum mechanics 本来就可以把 systems/processes/interactions 作为基本组织语言。

所以如果 R012 的唯一结果只是：

```text
object -> process
relation -> morphism
composition -> composition
```

则 verdict 应是 prior art / reformulation，而不是 Foundation breakthrough。

项目特异性必须落在：

- primitive arithmetic constraints；
- finite-resolution compatibility；
- irreversible many-to-one laws；
- generated relation/object theorem；
- exact integer rigidity/no-go；
- 或后续物理可区分预测。

---

# 7. A3/A4 与量子能力：本任务只做门槛，不做 Bell 主研究

不要在 R012 重新做 CHSH 表或 Bell 定理。

R004 已经有 finite rational Bell target：

\[
|S|=14/5>2
\]

以及 measurement-dependence cost pressure test。

R012 只回答一个 prerequisite：

> **当前 A3/A4 relation/correspondence 的信息类型是否原则上足以承载 phase-sensitive / interference-sensitive semantics？**

至少区分：

- Boolean support；
- witness multiplicity；
- probability weight；
- signed weight；
- complex/amplitude-like phase data；
- contextual measurement relation。

如果 Boolean relation / powerset support 在信息论上不够，给出最小 collision counterexample：两个量子/干涉候选状态拥有相同 A4 support 和相同 witness-count 层，但未来 phase-sensitive observation 不同。

不要因此立刻发明“quantum A4”。只形成后续任务的必要输入。

---

# 8. 最重要的负结果候选

优先尝试证明或反驳：

### Candidate N1

**Deterministic-kernel no-go**：仅从有限 deterministic maps 的 kernel/future-kernel 闭包，不能生成任意非对称、多值 A4 correspondence；必须额外引入 transition incidence / witness / branching primitive。

### Candidate N2

**Pair-observable boundary**：如果 A3 relation `Z_ij` 完全由 single-object data `(m_i,c_i)` functorially 决定，则 A3 本身不是独立 ontic degree of freedom；需要额外 relation state 才能表示同一 marginals 下不同 relational worlds。

构造两个 world：所有单体 state 相同，但 relation state 不同。若 canonical A3 无法表示，记录 expressivity boundary。

### Candidate N3

**Support-phase no-go**：纯 Boolean A4 correspondence及其 powerset future compiler不能区分某类具有同 reachable support 但不同 interference outcome 的状态，因此 quantum-native semantics 若存在必须提升 coefficient/witness structure。

这些 negative results 即使成立，也不是“Enterprise Math 失败”；它们精确告诉我们下一原语在哪里。

---

# 9. 最重要的正结果候选

### Candidate P1 — Relation genesis universal construction

找到一个 lower-layer object `D`（primitive transition/history/future language），并构造：

\[
G(D)=R_D
\]

使 relation：

- 不是任意外加；
- 对 dynamics 同构/重标号自然；
- composition/refinement 行为可证明；
- canonical A3/A4 是某个 specialization 或 quotient。

若 `G` 满足 universal property，优先抽象。

### Candidate P2 — Arithmetic categorical specialization

即使 generic category/relation structure全是 prior art，也证明某个 A3/A4 integer constraint 对应一个特殊子范畴/富集结构，并推出 generic category theory 不自动给出的 exact index、rigidity、scale 或 carry theorem。

这是完全合法的项目贡献。

---

# 10. Lean / executable 状态审计

当前 Common Surface 的 root Lean import 列表中没有 A3/A4 专属模块。

本任务先审计：

- A3/A4 是否已有未 root-registered Lean；
- 哪些 canonical Python theorem 最值得 first Lean target；
- categorical reduction 是否可以直接复用 mathlib `Relation`, `CategoryTheory`, `Quiver`, `Rel` 相邻 API，而不是自建一整套类别框架。

优先 formalization 候选应是小 theorem / no-go，不是先搭“Enterprise Category Theory”。

---

# 11. Prior-art discipline

这是一个 prior-art 本身就是研究对象的任务，因此允许从较早阶段做定向文献检查。

重点检查：

- `Rel` / allegories / relation algebras；
- enriched categories / quantaloids；
- spans/profunctors；
- process theories；
- categorical quantum mechanics；
- coalgebra / behavioral equivalence；
- automata minimization；
- dynamical systems / attractor quotients；
- relational quantum models；
- weighted/multirelations。

必须区分：

1. generic mathematical framework；
2. Enterprise Math exact arithmetic specialization；
3. 真正由 primitive finite dynamics 导出的 relation-genesis theorem。

没有第三项，不得用“重新定义数学对象”作为新颖性结论。

---

# 12. 最终交付

必须至少输出：

1. `A3_A4_CATEGORICAL_REDUCTION_MATRIX.md`
2. `A3_A4_RELATION_GENESIS_THEOREMS.md`
3. `A3_A4_OBJECT_IDENTITY_GENESIS.md`
4. `A3_A4_PRIOR_ART_POSITIONING.md`
5. `A3_A4_QUANTUM_EXPRESSIVITY_GATE.md`
6. executable / Lean evidence（如形成稳定 theorem）

最终 verdict 必须从下面选：

- `RENAMING_ONLY`
- `ARITHMETIC_SPECIALIZATION`
- `GENERATED_SUBTHEORY`
- `STRICT_EXTRA_STRUCTURE`
- 或精确的混合分类。

并回答：

> **Enterprise Math 与范畴论的正确关系到底是什么：替代、实例、内部生成的子理论，还是携带额外算术/动力学结构的模型？**

以及：

> **当前 A3/A4 的 relation 到底是输入进去的，还是已经能够由 lower-layer primitive dynamics 生成？**

如果答案是不够，明确指出缺失的最小 primitive，不要用哲学措辞掩盖。
