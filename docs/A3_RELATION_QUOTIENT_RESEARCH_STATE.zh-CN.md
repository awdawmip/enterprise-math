# A3 Relation Quotient — 研究归属与续研协议

状态：`ACTIVE RESEARCH OWNER NOTE`  
分支：`research/core/relation-quotient`  
架构归属：`A3 — Partition relation-state algebra`

## 1. 归属

本分支是 capacity-weighted partition relation-state 的通用研究归属。

核心对象：

\[
Z_{ij}=m_jc_i-m_ic_j,
\qquad
Z=cm^T-mc^T.
\]

以及：

- partition quotient `Z' = A Z A^T`；
- partition kernel `K_A={eta:A eta=0}`；
- relation rank / relation quantum / refinement memory；
- weighted collision observations `E^(s)`；
- 给定 future operation/observation language 的 exact relation precision。

## 2. 与历史 P019 混合分支的关系

历史分支 `research/p019-minimum-precision-lattice-geometry` 及其中 `P019_*` 文档保留为 discovery provenance，不删除、不 force-move、不重写历史。

从本说明生效后：

- A3 不再新增 `P019_MINIMUM_PRECISION_LATTICE_GEOMETRY_SUPPLEMENT_*`；
- 新的一般 relation-state 数学统一使用 `A3_*` 文档名；
- 历史 `P019_*` 文件只有在修正事实错误时才修改，不继续作为命名主线；
- canonical P019 的编号含义由 source `main` / `PROBLEM_STATUS` 决定，历史 relation 文件与 canonical P019 属于 `NAME_COLLISION_ONLY`。

## 3. 与其他研究节点的边界

### A2 / P023

一般 future-compatible quotient、operation-family closure、behavioral/future equivalence 与 minimal repair 的母定理归 A2/P023。

A3 只维护：

- weighted relation-state 上的特化定理；
- partition/capacity 的整数闭式；
- A3-specific exact solver / counterexample / precision consequence。

若 A3 结果去掉 weighted-relation 假设后仍成立，应通过 Research Relay 向 A2/P023 上提，不在本分支复制一套母定理。

### A4

A4 admissible-support/correspondence 与 A3 是不同对象。A3↔A4 只通过已证明 bridge 使用，不按术语合并。

### A5 / P022

lattice、primitive adjacency、balls/shells、geometry-specific filling/interpolation 与物理空间候选归 P022/A5。

A3 可以接收几何产生的 partition/observation，但不在本分支继续扩展 FCC/HCP/A_p 物理几何本体。

## 4. 共享机制

跨路线同步使用 GitHub Issue #82 `Research Relay: cross-branch theorem and finding bus`，不通过反复 whole-branch merge 同步。

开始新的通用定理线前：

1. 检查当前 branch head 与 source `main`；
2. 阅读与 A3/A2/A4/A5 相关的最新 Relay；
3. 先分类 `SAME_MOTHER / STRICT_GENERALIZATION / SPECIALIZATION / GENERATOR / COMPOSABLE_INDEPENDENT / CONFLICT / NAME_COLLISION_ONLY`；
4. 只有真正需要搬运资产时做 dependency/corollary/semantic replay。

重要 generalization、bridge、关键反例或 precision/witness obligation 必须回流 Relay。

## 5. 集成纪律

本分支长期 diverged 是允许的。不要为了“看起来同步”反复 merge `main`。

规范集成仍采用：

`owner branch audit -> Relay/lineage -> latest-main clean integration branch -> semantic replay minimal slice`。

历史研究文件不是 canonical theorem status。

## 6. 当前续研前沿

当前已经有：

- integer linear/affine dynamics 的 exact partition descent；
- linear observation-aware minimum exact partition；
- task-derived relation rank / quantum precision profile。

下一阶段只推进 A3-specific 的难点：

> **predicate-controlled / piecewise integer dynamics 中，允许 hidden branch identity 不可见、但 coarse output 仍完全相同时，求 exact quotient 条件。**

首先处理完整整数格上的 binary linear-threshold affine map；目标是区分：

- guard 必须显式 descend 的情形；
- guard 可以完全擦除、因为不同 branch 在 coarse quotient 上具有相同效果的情形；
- exactness 对 partition refinement 可能出现的负边界。
