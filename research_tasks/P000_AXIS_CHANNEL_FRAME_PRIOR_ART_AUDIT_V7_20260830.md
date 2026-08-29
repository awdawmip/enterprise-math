<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT",
  "title": "P000 Axis-Channel Frame/Torsor/Connection 外部先例审计 V7",
  "kind": "RESEARCH",
  "owner": "research/p000-6d-rotation-prior-art-audit",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Audit external antecedents for the Gen9/Gen10 symmetry-breaking problem: definability under automorphism groups, S6 torsors, frame fields/principal bundles, discrete graph connections, parallel transport, gauge freedom, loop holonomy, and equivalence between a global/per-cell frame and seed-frame-plus-connection presentations; separate standard mathematics from P000-specific Cell/axis/channel typing and no-quotient semantics.",
  "next_action": "Search authoritative model theory/group actions, principal-bundle/torsor, graph connection/discrete gauge and local-system literature. Map each Gen9/Gen10 claim to exact duplicate, partial antecedent, adjacent method or no material match. Explicitly test whether the five-anchor lower bound is merely orbit-stabilizer bookkeeping and whether AXIS_CHANNEL_FRAME is a standard trivialization/frame object.",
  "dependencies": [
    "research_returns/P000_FULL_CELL_AXIS_HANDLE_REALIZATION_V9_RETURN_20260829.md@main",
    "driver_reviews/P000_FULL_CELL_AXIS_HANDLE_V9_DRIVER_REVIEW_20260830.md@main",
    "research_returns/P000_CROSS_BLOCK_NATIVE_PRODUCT_PRIOR_ART_AUDIT_V6_RETURN_20260829.md@main",
    "driver_reviews/P000_CROSS_BLOCK_PRODUCT_PRIOR_ART_V6_DRIVER_REVIEW_20260830.md@main"
  ],
  "evidence_status": "GEN9_DEFINABILITY_OBSTRUCTION_ACCEPTED / PRODUCT_BLOCK_PRIOR_ART_V6_CLOSED / FRAME_CONNECTION_PRIOR_ART_OPEN",
  "hard_block": null,
  "tags": ["P000","prior-art","definability","automorphism","torsor","frame","principal-bundle","connection","gauge","holonomy"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-6D-ROTATION-PRIOR-ART-DUPLICATION-AUDIT",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P0006DPA7",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE"
}
-->

# P000 Axis-Channel Frame/Torsor/Connection 外部先例审计 V7

Status: `READY / GENERATION-7 / P1 / PRIOR-ART / P000-BOUND`

## Hard target

`P000_AXIS_CHANNEL_FRAME_CONNECTION_EXTERNAL_DUPLICATION_BOUNDARY_CLASSIFIED`

## Mandatory claim map

至少审计：

1. 结构在 automorphism group 下不可区分时，canonical definable choice 不存在的标准模型论/群作用结论；
2. Gen9 `S6` local presentation orbit 与 stabilizer 计数，特别是 `(6-k)!` 和 five-anchor lower bound 是否只是标准 orbit-stabilizer / base-size 现象；
3. 一个六元素无标号 local channel set 的 frame 是否标准等价于一个 `S6`-torsor 的 trivialization；
4. per-Cell frame field 与 one seed frame + edge connection 的标准 bundle/local-system 对应；
5. graph/discrete connection、parallel transport、path composition、loop holonomy；
6. gauge change 下 connection/frame/passage observable 的变换与 invariant；
7. flat connection 与 globally consistent frame field 的等价条件/限制；
8. partial actions / groupoids / inverse semigroups 与 frame/connection 的关系；
9. framed local matrix `M_x` 通过 `f_x` 转写成 axis-labeled matrix `PASS_x` 是否属于标准 change-of-frame / conjugation；
10. P000-specific no-quotient、opaque Cell identity、native axis typing 与 carrier readout separation 是否有 exact external duplicate。

逐条标记：`EXACT_DUPLICATE / PARTIAL_ANTECEDENT / ADJACENT_METHOD / NO_MATERIAL_MATCH`。

## Evidence rules

- 记录检索日期、数据库/搜索面、exact queries、authoritative sources；
- 优先专著、标准教材、正式论文；
- 明确区分 abstract mathematical object 与 P000 interpretation；
- `NO_MATERIAL_MATCH != NOVELTY`；
- 不因文献没有“P000”字样而判新颖；
- 不重复 V6 已关闭的 Cartesian product / wreath-product / maximal-imprimitive 审计，除非用于 frame 问题的必要背景。

## Required synthesis

最终必须回答：

\[
\boxed{\text{Gen9/Gen10 中哪些结构只是经典 torsor/frame/connection 数学，哪些剩余约束才真正是 P000-specific？}}
\]

并对任何未来 novelty statement 给出允许强度上限。
