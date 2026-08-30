<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 S4 冻结语法内的 Pareto 最小正向关系包分类 V16",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Within the accepted G15 finite grammar/equivalence/cost/envelope, classify the Pareto-minimal downstream packages that universally force faithful S4 splitting and, separately, an Aut_prim-fixed canonical section; prove sufficiency/necessity relative to the frozen semantics with deletion countermodels or redundancy certificates.",
  "next_action": "Consume the exact G15 catalog without modification; quotient by fixed-sort parameter-free mutual definability; enumerate the 90 dependency-closed package specifications; for each candidate positive package prove universal model-class sufficiency or produce a countermodel; compute faithful and canonical Pareto frontiers separately; attach one-condition deletion witnesses and retain P4, GL(2,3), C2 wr S4, K4 and tetra regressions.",
  "dependencies": ["research_returns/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15_RETURN_20260830.md@main","driver_reviews/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15_DRIVER_REVIEW_20260830.md@main","research_artifacts/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15/GRAMMAR_CERTIFICATE.json@main"],
  "evidence_status": "GEN15_GRAMMAR_EQUIVALENCE_COST_ENVELOPE_DRIVER_ACCEPTED / PARETO_POSITIVE_PACKAGE_CLASSIFICATION_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","S4","Pareto","relational-grammar","canonical-section","countermodel","no-quotient"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000FCC16",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
}
-->

# P000 `S4` 冻结语法内的 Pareto 最小正向关系包分类 V16

Status: `READY / GENERATION-16 / P0 / P000-BOUND / PARETO-CLASSIFICATION`

## Mother problem

Gen15 已冻结有限语法 `G15`：4 个 candidate relation forms、5 个 intrinsic constraint templates、fixed-sort parameter-free definitional equivalence、显式 Pareto cost，以及 90 个 dependency-closed package specifications。

现在第一次可以严格问：

\[
\boxed{\text{在 G15 内，哪些最小关系包真正强制 faithful / canonical }S_4\text{？}}
\]

## Hard target

`P000_G15_PARETO_MINIMAL_FAITHFUL_AND_CANONICAL_S4_RELATIONAL_PACKAGES_EXACTLY_CLASSIFIED`

## A. Grammar immutability gate

不得修改 Gen15 的 relation/constraint catalog、参数政策、equivalence policy、cost vector 或 envelope。若发现 G15 自相矛盾，只能返回 exact obstruction，不得边算边改语法。

## B. Universal semantics, not witness matching

对每个 package class，必须区分：

- `HAS_POSITIVE_WITNESS`；
- `UNIVERSALLY_FORCES_SPLIT`；
- `UNIVERSALLY_FORCES_AUT_FIXED_SECTION`。

K4/tetra 的正例不能单独证明 universal sufficiency。必须在冻结模型语义下证明全称结论，或给一个同 package 的反例。

## C. Faithful frontier

对所有 90 个 dependency-closed packages，在 definitional quotient 后分类：

1. readout 是否被强制为 surjective S4；
2. zero-residue lift locus `Z(q)` 是否在所有 admitted models 中非空；
3. 因而 faithful section 是否 universally exists。

所有 Pareto-minimal faithful packages 必须给：sufficiency proof + 每个条件删除后的 countermodel 或 redundancy proof。

## D. Canonical frontier

对 faithful packages 进一步计算声明的 primitive-preserving automorphism action：

\[
Aut_{prim}(M)\curvearrowright Sec(q).
\]

分类哪些 package universally force fixed point；若要求 uniqueness，必须另列，不得与 fixed-point canonicality 混同。

`C2 wr S4` 的 16 sections / two 8-orbits / no kernel-fixed section 是 mandatory negative regression。

## E. Countermodel discipline

优先复用：

- P4 no-lift；
- GL(2,3) nonsplit；
- C2 wr S4 split/noncanonical；
- K4 canonical；
- tetra incidence canonical。

若这些不足以删除某条件，构造 G15-envelope 内的新 exact countermodel。不得用超出 grammar 的 predicate 破坏候选 package。

## F. Pareto output

最终分别输出：

- `FAITHFUL_PARETO_FRONTIER`；
- `CANONICAL_FIXED_POINT_PARETO_FRONTIER`；
- 可选 `UNIQUE_SECTION_PARETO_FRONTIER`。

每个 frontier 元素必须包含 exact cost vector、definitional class、sufficiency certificate、deletion witnesses、是否使用 Hidden sort。

若 frontier 为空，必须 exact prove empty；若多个 incomparable minima，全部保留。

## G. Boundary

`BARE_P000_UNIVERSAL_S4_LIFT_DERIVABLE=FALSE` 仍冻结。

本任务只是在 **G15 downstream grammar** 内寻找足够条件，不得把胜出 package 自动提升为 P000 root axiom。

禁止 kernel quotient、carrier/native identity collapse、直接加入 section/R_a/R_b/K=1 primitive；time fixed。

## Deterministic checker

至少验证：

- G15 hash/catalog regression；
- 90 package specifications；
- definitional quotient；
- universal/countermodel classification table；
- Pareto dominance/frontier；
- one-condition deletion certificates；
- all Gen12–15 regressions。

## Valid terminal classes

- `G15_PARETO_MINIMAL_FAITHFUL_AND_CANONICAL_S4_PACKAGES_CLASSIFIED`；
- `G15_FAITHFUL_FRONTIER_CLASSIFIED_CANONICAL_FRONTIER_EMPTY`；
- `G15_NO_UNIVERSALLY_SUFFICIENT_POSITIVE_PACKAGE_IN_FROZEN_ENVELOPE_PROVED`；
- `G15_GRAMMAR_INTERNAL_OBSTRUCTION_EXACTLY_PROVED`。

External prior-art lane remains `RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT / TP2-2F8C6A1D9E7043B5C812 / Generation 8` and is not duplicated here.
