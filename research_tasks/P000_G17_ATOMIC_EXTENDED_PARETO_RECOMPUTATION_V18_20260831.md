<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 G17 原子背景等变扩展下的完整 Pareto 重算 V18",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Within immutable G15 plus the accepted G17 atomic charged background-equivariance templates, recompute the full 90-package universal faithful/canonical Pareto frontiers separately for frame-induced/no-independent-connection and independent-connection model subclasses, with exact definitional quotient and same-package countermodels/deletion certificates.",
  "next_action": "Pin G15 and G17 certificates; enumerate all 90 G15 packages with the required subclass-specific charged gates; quotient by the frozen fixed-sort definitional equivalence; prove universal structural S4, zero-residue section and Aut_prim fixed-point properties or produce same-package countermodels; compute the two subclass Pareto frontiers and all essential-deletion certificates.",
  "dependencies": ["research_returns/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_RETURN_20260830.md@main","driver_reviews/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17_DRIVER_REVIEW_20260831.md@main","research_artifacts/P000_BACKGROUND_S4_EQUIVARIANCE_GATE_V17/BACKGROUND_EQUIVARIANCE_CERTIFICATE.json@main","research_artifacts/P000_S4_RELATIONAL_MINIMALITY_GRAMMAR_V15/GRAMMAR_CERTIFICATE.json@main"],
  "evidence_status": "GEN17_BACKGROUND_LEAKS_AND_ATOMIC_TRANSPARENCY_DRIVER_ACCEPTED / FULL_G17_EXTENDED_90_PACKAGE_FRONTIER_OPEN",
  "hard_block": null,
  "tags": ["P000","native-6D","S4","G15","G17","PF10","connection","Pareto","equivariance","countermodel"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000FCC18",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
}
-->

# P000 `G17` 原子背景等变扩展下的完整 Pareto 重算 V18

Status: `READY / GENERATION-18 / P0 / P000-BOUND / FULL-ATOMIC-PARETO-RECOMPUTATION`

## Mother problem

Gen17 已接受两个原子 charged background gates：

- `PF10_STRUCTURAL_AUT_EQ`；
- `CONNECTION_STRUCTURAL_AUT_EQ`（仅 independent connection model 声明时需要）。

并给出 targeted K4/TETRA positive retest。但 Gen17 任务书明确不要求重算全部 90 个 G15 package。

因此本任务回答：

\[
\boxed{\text{在 G15+G17 原子语法全部冻结后，完整 Pareto frontier 到底是什么？}}
\]

## Hard target

`P000_G17_ATOMIC_BACKGROUND_EQUIVARIANCE_EXTENDED_G15_PARETO_FRONTIERS_EXACTLY_CLASSIFIED`

## A. Immutable inputs

必须 pin 并保持：

1. G15 的 4 relation forms、5 constraints、fixed-sort definitional equivalence、cost vector、90 package specifications；
2. Gen17 的两条 atomic charged templates 与 atomicity rule；
3. Gen17 compatibility theorem、PF10 leak、independent connection leak；
4. Gen16 unconditional `{K4_ADJ}` frontier 仍为 rejected。

不得修改 G15/G17 语法来适配结果。

## B. Two model subclasses

分别分类：

### B1. `FRAME_INDUCED_OR_NO_INDEPENDENT_CONNECTION`

每个 package 的正向候选必须额外满足：

`PF10_STRUCTURAL_AUT_EQ`。

### B2. `INDEPENDENT_CONNECTION_DECLARED`

每个 package 的正向候选必须额外满足：

`PF10_STRUCTURAL_AUT_EQ + CONNECTION_STRUCTURAL_AUT_EQ`。

不得把两种 subclass 混成一个 cost/frontier。

## C. Universal semantics

对每个 G15 package class + subclass gates，分别判定：

1. `STRUCTURAL_READOUT_SURJECTIVE`；
2. `ZERO_RESIDUE_SECTION_EXISTS`；
3. `AUT_PRIM_FIXED_SECTION_EXISTS`；
4. 可选 `UNIQUE_SECTION`，但不得与 fixed-point canonicality 混同。

正例 witness 不能代替 universal proof。

## D. Full 90-package recomputation

重新枚举全部 90 dependency-closed G15 specifications，并应用 frozen definitional quotient。

对于每个 negative class，必须给：

- P4/no structural S4；或
- unconstrained selected relation stabilizer；或
- GL(2,3) nonsplit residue；或
- 其他 exact same-package countermodel。

对于每个 positive class，必须给 universal sufficiency theorem。

## E. Pareto frontiers

分别输出：

- `FRAME_INDUCED_FAITHFUL_FRONTIER`；
- `FRAME_INDUCED_CANONICAL_FIXED_FRONTIER`；
- `INDEPENDENT_CONNECTION_FAITHFUL_FRONTIER`；
- `INDEPENDENT_CONNECTION_CANONICAL_FIXED_FRONTIER`。

每个元素必须包含：

- definitional class；
- full package；
- exact extended cost；
- universal proof certificate；
- one-condition deletion certificate；
- Hidden usage。

若 K4 targeted package 的确唯一 Pareto minimum，必须由全 90-package classification 推出，而不是预设。

## F. Deletion regressions

Mandatory：

- delete structural K4/TETRA gate -> P4 or equivalent structural no-lift；
- delete PF10 gate -> `I=O=e1,M=I6`, compatibility order 4；
- independent subclass delete connection gate -> marked-edge connection, compatibility order 4；
- retain C2 wr S4 split/noncanonical and GL(2,3) nonsplit regressions where relevant。

## G. Scope boundary

本任务只分类 **G17 atomic/separable-transparency grammar**。

不得声称这些 gates 是所有 coupled background conditions 中 globally weakest。

若完整 atomic frontier 闭合，下一阶段才允许研究：是否存在 parameter-free、non-tautological 的 coupled background relation/constraint 能在保持 joint lift 的同时严格 Pareto 改进逐组件 transparency。

冻结：

`BARE_P000_UNIVERSAL_S4_LIFT_DERIVABLE=FALSE`。

`CARRIER_S4 != COMPLETE_NATIVE_P000_ROTATION_GROUP`。

`NO_KERNEL_QUOTIENT`；`TIME_FIXED`；不得直接加入 section/R_a/R_b/K=1 primitive。

## Deterministic checker

至少验证：

- G15/G17 input hashes；
- 90 packages；
- definitional quotient；
- 两 subclass classification tables；
- four frontiers；
- Pareto dominance；
- deletion countermodels；
- Gen13–17 mandatory regressions。

## Valid terminal classes

- `G17_ATOMIC_EXTENDED_G15_BOTH_SUBCLASS_PARETO_FRONTIERS_CLASSIFIED`；
- `G17_FRAME_INDUCED_FRONTIER_CLASSIFIED_INDEPENDENT_CONNECTION_FRONTIER_EMPTY`；
- `G17_ATOMIC_EXTENDED_G15_NO_POSITIVE_PACKAGE_PROVED`；
- `G17_ATOMIC_GRAMMAR_INTERNAL_OBSTRUCTION_EXACTLY_PROVED`。

External prior-art V8 remains the existing comparison lane and is not duplicated here.
