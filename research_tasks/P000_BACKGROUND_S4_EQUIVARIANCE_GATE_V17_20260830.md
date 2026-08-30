<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 零成本背景的 S4 兼容门与有成本等变增强 V17",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Classify the zero-cost background symmetry leak exposed by Gen16: prove the exact compatibility/stabilizer bound on the S4 readout image, inventory PF10/frame/connection/other retained background components that can reduce the image, determine which full-S4 equivariance conditions are derivable versus genuinely new charged downstream assumptions, and freeze the minimal charged background-symmetry extension required before any positive G15 Pareto theorem can be recomputed.",
  "next_action": "Keep G15 immutable. Define per-background compatibility subsets of carrier S4; prove im(q) lies in their intersection; construct independent leak countermodels for PF10 and any other retained background components; test derivability of full equivariance from accepted structure; if not derivable, define and cost the weakest intrinsic equivariance templates without mentioning the desired section itself.",
  "dependencies": ["research_returns/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15_RETURN_20260830.md@main","driver_reviews/P000_G15_PARETO_MINIMAL_S4_PACKAGES_V16_DRIVER_REVIEW_20260830.md@main","research_tasks/P000_G15_PARETO_MINIMAL_S4_PACKAGES_V16_20260830.md@main"],
  "evidence_status": "GEN16_OFFICIAL_K4_FRONTIER_REFUTED / G15_EMPTY_POSITIVE_FRONTIERS_AT_DRIVER_AUDIT_STRENGTH / BACKGROUND_EQUIVARIANCE_GATE_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","S4","PF10","background-equivariance","stabilizer","connection","symmetry-leak","no-quotient"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000FCC17",
  "origin_kind": "DRIVER_REVIEW_REVISION",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
}
-->

# P000 零成本背景的 `S4` 兼容门与有成本等变增强 V17

Status: `READY / GENERATION-17 / P0 / P000-BOUND / BACKGROUND-SYMMETRY-FIRST`

## Mother problem

Gen15 冻结 G15，但把 framed/PF-10 模型中的若干已接受结构计为零成本背景。Gen16 的正式正向 frontier 结果被如下反例击穿：在保持全部 G15 关系/约束不变时，非均匀 PF-10 轴 profile 可以把 carrier `S4` readout 压到真子群。

因此现在必须先回答：

\[
\boxed{\text{哪些零成本背景数据本身在控制可实现的 }S_4\text{ readout？}}
\]

只有这个门被精确关闭后，才允许给 G15 增加有成本的等变约束并重新计算正向 frontier。

## Hard target

`P000_ZERO_COST_BACKGROUND_S4_COMPATIBILITY_GATE_AND_MINIMAL_CHARGED_EQUIVARIANCE_EXTENSION_EXACTLY_CLASSIFIED`

## A. Freeze G15 and Gen16 audit boundary

不得修改 G15 的 4 relation forms、5 constraint templates、definitional equivalence、cost vector 或 finite envelope。

冻结：

`G15_CURRENT_UNIVERSAL_POSITIVE_FRONTIERS = EMPTY_AT_DRIVER_AUDIT_STRENGTH`。

`PF10_I=O=e1, M=I6` 是 mandatory no-surjectivity regression。

不得重新声称 `{K4_ADJ}` 在现有语义下 universal sufficient。

## B. Background inventory

从当前 accepted downstream source 中逐项列出 enriched automorphism 必须保持的零成本背景。至少审计：

1. PF-10 local `I/O/M` tensor；
2. per-Cell frame `f_x` 的 typed role；
3. frame-induced transport `T_xy=f_y o f_x^-1`；
4. independent retained connection（若模型声明）；
5. retained native adjacency valuation；
6. retained star/overlap/gluing data at其 accepted scope；
7. 任何 Gen15 漏列但实际上进入 `Aut_prim(M)` 定义的 background field。

必须区分：

- `PURE_GAUGE_PRESENTATION`；
- `DERIVED_AUTOMATICALLY_EQUIVARIANT`；
- `CONTENTFUL_SYMMETRY_LEAK_SOURCE`；
- `OPTIONAL_IF_MODEL_DECLARED`。

## C. Exact compatibility-set theorem

对每个 background component `B`，定义 carrier `S4` 中的兼容集合

\[
Compat_B\subseteq S_4,
\]

其元素是那些在 frozen axis action 下至少存在一个合法的 `B`-preserving typed lift 的 carrier permutations。

若 `B` 纯粹是 AxisType-indexed tensor，可退化为普通 stabilizer `Stab_{S4}(B)`。

必须证明：

\[
\boxed{im(q)\subseteq\bigcap_B Compat_B.}
\]

明确哪些 `Compat_B` 必为 subgroup，哪些在 groupoid/partial-domain 情形仅是可组合兼容集，禁止无证明地统一叫 stabilizer subgroup。

## D. PF-10 leak classification

冻结六轴作用 `rho:S4->Sym(6)`。

对 PF-10：

\[
P_x=(I_x,O_x,M_x)
\]

精确定义 `Stab_{S4}(P_x)` 或跨 Cell orbit 的 typed compatibility law。

必须复核：

`I=O=e1, M=I6`

的 stabilizer order 为 4，从而阻止 `S4` surjectivity。

进一步分类：

- full PF-10 `S4` invariance；
- orbitwise equivariance under Cell action；
- weaker generator-only conditions；
- 哪些是 necessary，哪些在 declared model 中 sufficient。

## E. Connection / holonomy leak independence

先令 PF-10 取完全 `S4`-symmetric 数据，再主动寻找 connection/holonomy 能否独立杀死某个 carrier generator。

若能，构造 exact independent countermodel。

若不能，证明在相应 accepted connection semantics 下其 equivariance 自动由 frame/background law 推出。

必须保持：

`STANDARD_FLATNESS != TRIVIAL_GLOBAL_HOLONOMY`。

非平坦 holonomy 不是自动 obstruction；问题是其在 lift 下是否满足 equivariance/conjugacy law。

## F. Derivable versus charged conditions

对每个需要 full-`S4` compatibility 的 background condition，分类为：

1. `DERIVED_FROM_ACCEPTED_STRUCTURE`；
2. `NOT_DERIVABLE_COUNTERMODEL_EXISTS`；
3. `DERIVABLE_ONLY_UNDER_EXPLICIT_MODEL_SUBCLASS`。

已有 PF-10 非均匀 countermodel 强烈提示其 full equivariance 在当前强度下不可导；必须正式证明，不得只凭直觉。

## G. Minimal charged extension

若存在不可导的 symmetry leak source，定义新的**有成本 downstream constraint template**。要求：

- 不得写成 `there exists an S4 section`；
- 不得直接加入 `R_a,R_b`；
- 必须是对已有 background field 的 intrinsic equivariance/preservation 条件；
- 给出 relation/constraint typing；
- 给出 Gen15 cost vector 的扩展坐标或明确为什么沿用 global-constraint coordinate；
- 做 one-condition deletion countermodel。

优先考虑拆分而不是一个总包：例如 `PF10_S4_EQ`, `CONNECTION_S4_EQ`。若多个独立 leak source 存在，允许得到 incomparable minimal charged packages。

## H. Positive-gate sufficiency test

在所有必要 background equivariance gates 加入后，重新测试最弱结构（优先 `{K4_ADJ}` 与 `TETRA_CA`）是否真的 universal force：

- readout surjectivity；
- zero-residue section existence；
- `Aut_prim` fixed-point canonicality。

本任务不要求完整重算所有 90 个旧 package；若 background gate 一旦固定后剩余 Pareto frontier 仍需大规模枚举，可发布后续 generation。

## I. Boundary

`BARE_P000_UNIVERSAL_S4_LIFT_DERIVABLE=FALSE` 保持冻结。

任何新 equivariance constraint 都是 P000 下游模型条件，不得偷升为 root axiom。

禁止 kernel quotient、carrier/native identity collapse、直接 section primitive；time fixed。

## Deterministic checker / certificate

至少覆盖：

- frozen G15 hash regression；
- background inventory machine record；
- `im(q) <= intersection Compat_B` finite witnesses；
- PF10 `e1` stabilizer order 4；
- symmetric-PF10 regression；
- connection independent leak or automatic-equivariance certificate；
- derivability countermodels；
- charged-template deletion tests；
- Gen12–16 mandatory regressions。

## Valid terminal classes

- `BACKGROUND_S4_COMPATIBILITY_INTERSECTION_THEOREM_AND_LEAK_SOURCES_CLASSIFIED`；
- `MINIMAL_CHARGED_BACKGROUND_EQUIVARIANCE_CONSTRAINTS_CLASSIFIED`；
- `PF10_ONLY_LEAK_SOURCE_AND_MINIMAL_EQUIVARIANCE_GATE_CLASSIFIED`；
- `MULTIPLE_INDEPENDENT_BACKGROUND_LEAK_SOURCES_AND_PARETO_GATES_CLASSIFIED`；
- `BACKGROUND_EQUIVARIANCE_GRAMMAR_OBSTRUCTION_EXACTLY_PROVED`。

External prior-art V8 remains the existing comparison lane; do not duplicate it.
