<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R012-A3A4-RELATION-GENESIS-CATEGORY-BOUNDARY",
  "title": "R012 A3/A4 Category Replanting and Relation Genesis",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Replant the core ideas of relation algebra, category theory and process theory into Enterprise Math's finite-state, precision, quotient, collapse, witness and forward-dynamics substrate; recover classical structure faithfully where it survives, identify exact new arithmetic or finite-resolution boundaries where it changes, and determine how much A3/A4 relation and object identity can be generated from lower-layer primitive dynamics rather than supplied exogenously.",
  "next_action": "Freeze canonical A3/A4 interfaces; reconstruct the strongest standard relational/categorical/process structures on top of Enterprise Math primitives without novelty pressure; classify exact reconstructions as successful prior-art rooting; then search for Enterprise-specific rigidity, carry, collapse, witness, future-language, or relation-genesis theorems and precise no-go boundaries.",
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
    "README.zh-CN.md",
    "README.md",
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
  "evidence_status": "CATEGORY_REPLANTING_RELATION_GENESIS_RESEARCH",
  "last_progress_ref": "Driver alignment to mature-mathematics replanting philosophy in README",
  "last_progress_at": "2026-08-10T21:01:00+08:00",
  "hard_block": null,
  "tags": ["R012", "A3", "A4", "relation", "category-theory", "process-theory", "replanting", "relation-genesis", "object-identity", "precision", "collapse", "prior-art", "foundation"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED"
}
-->

# R012 — A3/A4 范畴思想重新扎根与关系生成

Status: `READY / P0 / HIGH / FOUNDATION REPLANTING / NOT CANONICAL`

## 0. 任务哲学已经更新

本任务不再以“Enterprise Math 是否替代范畴论”为问题，也不把“发现 A3/A4 是既有范畴/关系结构”视为失败。

当前 README 的基础立场是：

> **成熟数学不是被进取数论排斥的旧世界，而是可以重新种在有限状态、显式精度、整数关系、collapse、witness 与前向演化土壤中的成熟思想。**

因此 R012 的正确目标是：

1. 沿着范畴论、关系代数、process theory 的**核心思想**重新构造；
2. 看哪些经典结构在 Enterprise Math 中原样恢复；
3. 看哪些结构因为 precision / quotient / collapse / future language / irreversible dynamics 而发生改变；
4. 看重新扎根后是否长出新的 exact boundary、rigidity、carry、witness、compression、no-go 或生成定理；
5. 再进一步追问：relation、correspondence、object identity 能否由 lower-layer primitive dynamics 内生生成。

完整恢复一个经典结构应标记为：

`ROOTING_SUCCESS / PRIOR_ART`

而不是失败。

只有恢复以后出现的新数学，才进入 Enterprise-Math-specific candidate 层。

方向可以激进，证据必须残酷。

Deep Research：**开启**。用途是查原始/权威范畴论、关系论、process theory、coalgebra、categorical quantum mechanics 等 prior art，帮助我们忠实重建并攻击自己的新结果；不是用文献替代内部推导。

---

# 1. 冻结并消费 canonical 输入

不要重做已经存在的 A3/A4 数学，只核准接口并消费。

## A3

Canonical relation coordinate：

\[
Z_{ij}=m_jc_i-m_ic_j.
\]

现有 A3 core 至少包含：

- weighted relation field；
- exact partition coarsening；
- relation lattice / reconstruction；
- relation quantum 与 primitive capacity；
- relation scale/carry；
- spanning-tree sparse relation lattice 后续结构。

## A4

Canonical finite correspondence core 至少包含：

- finite relation composition；
- converse；
- common-target structure；
- radius-family diagnostics；
- split-completeness；
- witness spectrum `W_k`；
- source-group spectrum `G_k`；
- total-function degeneration到 A1/P011 collision spectrum。

## 已有 bridges

A3/A4 bridge 已研究从 A3 relation threshold 生成 A4 support，以及 signed cancellation 使 coarse converse 失败的边界。

A4/P023 bridge 已研究：

\[
\Sigma_{(R,O)}(x)=\{O(y):(x,y)\in R\}
\]

以及 powerset compiler，把 raw relation words 编译成 deterministic support dynamics，同时明确丢失 path multiplicity、branch identity 与 intermediate definedness。

这些已有结果只作为输入，不重新命名成 R012 新发现。

---

# 2. 第一主线：沿范畴论核心思想重新建，而不是只做术语对照

不要停在“这个对象像哪个范畴对象”的 translation table。

至少沿下列核心思想逐层重建：

## 2.1 Object / process / morphism

研究 Enterprise Math 中什么应扮演：

- object；
- morphism / process；
- identity；
- composable boundary；
- source / target；
- object state 与 relation state 的关系。

重要问题：object 是否必须先给定，还是可以由稳定 process/history class 生成？

## 2.2 Composition and associativity

从 A1/A4 现有 composition 出发，区分：

- total composition；
- partial/guarded composition；
- relation composition；
- witness-sensitive composition；
- quotient/coarse composition；
- finite-horizon future-language composition。

研究 associativity 在哪些表示层上原样成立，在哪些 collapse/observation 后需要额外 sufficient state。

特别寻找：

> fine composition associative，但 coarse representation 因遗失 witness / legality / branch state 而无法形成同样的 associative effective process algebra。

若出现 exact minimal repair，优先记录。

## 2.3 Identity and idempotent structure

研究：

- identity process 在有限精度世界中的意义；
- collapse idempotent 与 categorical idempotent 的关系；
- quotient / retract / splitting 是否自然出现；
- stable image 是否可成为 generated object。

不要把标准 idempotent splitting 冒充新理论；重点找 Enterprise-specific integer/collapse specialization。

## 2.4 Functoriality / naturality

测试已有 scale projection、quotient projection、A3→A4 support、A4→P023 powerset compiler 是否形成严格 functorial/natural 结构。

要求区分：

- literal functoriality；
- only-after-quotient functoriality；
- partial/legality-sensitive functoriality；
- witness-reflecting functoriality；
- failure of naturality caused by lost precision。

优先寻找 exact naturality criterion 与 minimal repair。

## 2.5 Universal properties

不要只把已有对象贴上 categorical 名字。

对 project-native constructions 主动问：

- coarsest future-safe quotient 是否有 universal property；
- minimal repair 是否可表成 reflection/coreflection；
- generated relation closure 是否有 free / initial / terminal 性质；
- powerset compiler 是否只是标准 construction，还是 Enterprise restrictions 选出特殊子结构；
- relation lattice / sparse tree coordinates 是否对应某种 universal representation problem。

如果只是经典 universal property，标 prior art；如果 integer/precision 条件给出更强 sharp property，再单独记录。

## 2.6 Monoidal / parallel composition

如果两个独立 state/process 并行组合，研究 product/tensor-like structure：

- 独立 future languages 如何组合；
- precision requirement 是否简单 product，还是会出现 interaction-generated repair；
- witness/support 是否出现不可由 marginals 恢复的 joint relation state；
- collapse 是否对 parallel composition 保持兼容。

这可能是未来物理最重要的入口之一，但本任务先做有限 exact mathematics，不直接宣称量子理论。

---

# 3. 第二主线：最强标准数学重建与 prior-art 定位

至少比较：

- `Rel`；
- relation algebra / allegory；
- enriched relation / quantale / quantaloid；
- spans / profunctors / distributors（适用时）；
- category / functor / natural transformation；
- idempotent / quotient / reflective constructions；
- symmetric monoidal / dagger process theories；
- coalgebra / behavioral equivalence；
- categorical quantum mechanics 中 sets-and-relations、stochastic/process models。

对每个重建对象建立紧凑矩阵：

```text
core idea
→ Enterprise primitive realization
→ exact reconstruction theorem
→ required precision/state
→ information lost under collapse
→ standard prior-art owner
→ Enterprise-specific residue (if any)
```

如果完全重建，标：

`EXACT_RECONSTRUCTION / ROOTING_SUCCESS / PRIOR_ART`

不要为了创新而改写经典定理。

---

# 4. 结果分类：不再用“重命名失败”作为主 verdict

每个研究块分别分类，而不是强迫整个 R012 只有一个标签。

### R0 — EXACT_RECONSTRUCTION

经典 category/relation/process structure 在 Enterprise Math 中严格重现。

这是基础扎根成功，但不是新数学。

### R1 — ARITHMETIC / PRECISION SPECIALIZATION

一般结构属于 prior art，但 integer/floor/root/collapse/scale/future-language 约束产生新的 sharp special theorem、index、carry、rigidity、compression 或 no-go。

### R2 — GENERATED SUBTHEORY

存在明确的 lower-layer primitive dynamics → relation/process/category structure 的生成 construction；A3/A4 某部分成为派生层，而非额外输入。

### R3 — STRICT EXTRA STRUCTURE

成熟 categorical language 能描述它，但 generic categorical axioms 不自动给出 Enterprise Math 的额外 arithmetic/precision constraint；该 constraint 产生新的可检验数学。

### R4 — REQUIRES NEW PRIMITIVE

某个需要的 relation/process capability 无法从当前 lower layers 导出，且有严格 no-go 指出缺失的最小 primitive。

最终允许混合分类，例如：

`A4 composition = R0; A3 scale carry = R1; relation genesis = R2 candidate; phase semantics = R4`。

---

# 5. 第三主线：Relation Genesis

README 的“重新扎根”不意味着所有 relation 必须由 A0 自动生成；但如果能够生成，这是非常高价值结果。

从 A0/A1/A2 可用对象出发测试：

## 5.1 History merge

\[
x\sim_t y \iff F_t(x)=F_t(y).
\]

它天然产生 equivalence/kernel。

研究它能否进一步产生：

- direction；
- weight；
- asymmetry；
- multivaluedness；
- witness multiplicity；
- relation scale。

若不能，给最小 no-go。

## 5.2 Future-language generated relation

由：

\[
\Sigma_W(x)
\]

研究 behavioral equivalence / preorder / simulation / bisimulation，以及这些结构在 P023 future-safe quotient 中如何重现。

特别寻找 future language 扩张时 relation 如何 refinement，以及是否形成自然 filtration。

## 5.3 Transition-incidence genesis

从 primitive transition：

\[
x\to y
\]

的 occurrence / multiplicity / cost / merge / legality 产生 relation。

要求明确回答：direction、weight、sign、composition、witness、scale 分别从哪里来。

## 5.4 A3-specific genesis

检验：

\[
Z_{ij}=m_jc_i-m_ic_j
\]

究竟是：

- pair observable；
- exterior/difference construction；
- invariant；
- coordinate transformation；
- dynamically generated relation；
- 或真正需要额外 relation state。

必须区分：

`relation explicitly represented`

与

`relation dynamically generated / ontically independent`。

---

# 6. 第四主线：Object Identity Genesis

把“对象是历史稳定模式”数学化，而不是哲学化。

测试：

- fixed/stable classes；
- recurrent components；
- eventual behavioral equivalence；
- idempotent image/splitting；
- minimal future-safe quotient；
- process-history equivalence class。

目标是构造最小 finite model，使 object identity 不是任意 label，而是由 process/dynamics 稳定产生。

然后判断：

1. 是否只是标准 automata / coalgebra / dynamical-system quotient 的 R0 重建；
2. precision/collapse 是否产生新的 R1 边界；
3. relation 与 object 谁先生成；
4. 是否存在循环定义；
5. 是否需要 primitive event/incidence layer。

正结果和 no-go 都有价值。

---

# 7. Process-first 是研究入口，不是默认创新声明

现有 process theory 已经非常成熟。

因此：

```text
object → system
relation → morphism
composition → composition
```

若严格恢复，就是 `R0 / ROOTING_SUCCESS / PRIOR_ART`。

这不是需要回避的结论。

R012 真正继续追问的是：

> 同一个 process/category 核心思想，在有限信息、explicit precision、many-to-one collapse、future-safe quotient、witness retention 和 irreversible dynamics 条件下，会不会产生成熟理论通常无需显式区分的新资源与边界？

项目特异性优先寻找：

- precision-dependent composability；
- quotient-dependent associativity/descent；
- witness-preserving vs support-only morphism；
- irreversible idempotent/collapse structure；
- naturality failure and minimal repair；
- integer lattice/index/carry；
- generated relation/object theorem。

---

# 8. A3/A4 与量子表达能力：只做信息门槛

不要在 R012 重做 Bell/CHSH 主研究。

只回答：当前 relation/correspondence coefficient/state type 能否原则上承载：

- Boolean support；
- path/witness multiplicity；
- probability weight；
- signed weight；
- phase-sensitive amplitude-like data；
- contextual measurement relation。

若 Boolean support 或 witness count 不足，寻找最小 collision：

> 两个状态在当前 A4 可见层完全相同，但某个 phase/interference-sensitive future observation 不同。

这应输出 expressivity boundary，不要立即发明“Quantum A4”。

如果未来需要 richer coefficient/enrichment，应把它作为 proposal candidate 返回 Driver。

---

# 9. README 新数学相思想与 R012 的边界

当前 README 允许：普通有限分辨率区域以 Enterprise Math 为主要底层，而奇点/极端高混乱度区域可能进入真正连续数学相。

R012 **不负责研究奇点内部，也不负责建立连续数学相理论**。

但可以记录一个接口问题：

> 如果 relation/category/process structure 在有限精度域中成功重建，哪些结构可能跨越未来的离散—连续数学相边界，哪些依赖 finite precision 而不能直接延拓？

除非出现非常直接的 theorem，否则只作为 `proposal_candidates`，不要扩张 R012 scope。

---

# 10. 优先 negative / positive candidates

## Negative N1 — deterministic-kernel generation limit

仅由 deterministic map kernels/future kernels 是否不能生成 generic asymmetric multivalued A4 correspondence？

若是，给最小 no-go 与所缺 primitive。

## Negative N2 — pair-observable boundary

如果 A3 `Z_ij` 完全由单体 `(m_i,c_i)` 决定，能否表示“相同 marginals、不同 relational world”？

若不能，给 exact expressivity boundary。

## Negative N3 — support-phase boundary

纯 Boolean/support compiler 是否无法保存 phase-sensitive future distinction？

## Positive P1 — generated relation construction

寻找 lower-layer object `D` 与自然 construction：

\[
G(D)=R_D
\]

要求 relation 非任意外加，且对重标号、composition、refinement 有可证明行为。

## Positive P2 — categorical precision specialization

寻找成熟 category/process theorem 在加入 explicit precision/collapse 后出现的新 exact boundary。

## Positive P3 — universal property of future-safe repair

检验 P023 coarsest future-safe quotient/minimal repair 是否能获得有用 categorical universal property，并进一步产生 project-specific finite/integer specialization。

---

# 11. Lean / executable

不要先搭“Enterprise Category Theory”大框架。

优先：

- 小型 exact finite models；
- minimal counterexamples；
- small universal-property theorem；
- naturality/descent criterion；
- generated relation no-go；
- precision-dependent composition witness。

先审计 mathlib 的 `Relation` / `CategoryTheory` / `Quiver` / functor / quotient 等已有 API，能复用就复用。

Formalization 必须服从 theorem maturity，不为了形式化而制造新 ontology。

---

# 12. Prior-art discipline

Deep Research 优先查原论文、作者材料、标准专著/权威文献，重点覆盖：

- categories / functors / natural transformations / universal properties；
- `Rel`, relation algebra, allegory；
- enriched categories / quantales / quantaloids；
- spans / profunctors；
- process theories；
- coalgebra / behavioral equivalence；
- automata minimization；
- categorical quantum mechanics；
- weighted/multirelations；
- idempotent splitting / quotient / reflective constructions。

External mathematics = prior art。

研究纪律：

> **Deep Research 用来校准、攻击和定位我们的重建，不用来替 Enterprise Math 产生结果。**

---

# 13. 文档纪律

不要产生五六份独立 MD。

默认交付只需要：

1. 一个主研究报告 / handoff，包含 reconstruction matrix、relation genesis、object identity、quantum expressivity、prior-art positioning；
2. 一个 machine-readable reconstruction/result matrix（JSON 优先）；
3. 必要的 executable / Lean / tests。

如果发现多个后续方向，集中写进一个 `proposal_candidates` 区块，不自行生成新的 taskbook。

Artifact creation 本身不是 progress。

---

# 14. 最终必须回答

最终报告必须分别回答：

### A. 什么经典范畴/关系/process 核心思想已经成功在 Enterprise Math 中重建？

这些标 `R0 / ROOTING_SUCCESS / PRIOR_ART`。

### B. 哪些重建因为 integer / precision / collapse / witness / future language 出现了新 sharp structure？

这些才进入 `R1/R3` candidate。

### C. 当前 A3/A4 relation 有多少是输入结构，有多少能由 lower-layer dynamics 生成？

### D. object identity 能否由 process/history stable pattern 生成？

### E. 当前 A3/A4 对 phase-sensitive / contextual future language 的表达能力边界在哪里？

### F. 下一步最值得继续重新扎根的 1–3 个成熟数学核心思想是什么？

最终总判断不再问“Enterprise Math 是否替代范畴论”。

正确的问题是：

\[
\boxed{
\text{范畴论的核心思想在 Enterprise Math 的新地基上重新生长后，哪些结构原样恢复，哪些结构改变，又长出了什么新的数学？}
}
\]
