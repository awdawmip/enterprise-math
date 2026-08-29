<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "title": "P000 混合三轴切面与状态级 S4 旋转提升 / Z2 holonomy 障碍 V5",
  "kind": "RESEARCH",
  "owner": "research/p000-l1-native-carrier-contact-bridge",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "foundation_level": "P000_ROOT_AXIOM_BOUND",
  "p000_required": true,
  "frontier": "Construct the three mixed native K4-star slices and a state-level lift of accepted FCC S4 generators after freezing the accepted star/complement and Z2-holonomy obstructions, or prove the exact native obstruction/minimal additional state extension.",
  "next_action": "Treat J_A={1,2,3}, J_B={1,4,5}, J_C={2,4,6}, J_D={3,5,6} as observation windows only; construct or refute geometric native structures on J_B,J_C,J_D, then lift a=(BCD), b=(AB) and classify exact S4 closure versus hidden Z2/cocycle/extension/groupoid residue.",
  "dependencies": [
    "research_returns/P000_L1_NATIVE_FCC_CARRIER_BRIDGE_V2_RETURN_20260829.md@main",
    "driver_reviews/P000_NATIVE_FCC_STRICT_BRIDGE_GEN2_DRIVER_REVIEW_20260829.md@main",
    "driver_reviews/P000_FCC_SIX_LINE_ROTATION_ALGEBRA_DRIVER_REVIEW_20260829.md@main"
  ],
  "evidence_status": "GEN2_STRICT_BRIDGE_DRIVER_ACCEPTED / POST_REVIEW_CANONICAL_FOLLOWUP / MATHEMATICAL_SCOPE_IDENTICAL_TO_V4",
  "hard_block": null,
  "tags": ["P000","native-6D","FCC","S4","mixed-slice","Z2-holonomy","state-lift","group-extension","groupoid","rotation"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000NATFCC5",
  "origin_kind": "DRIVER_REVIEW_FOLLOWUP",
  "task_lineage": "REVISION",
  "parent_task_id": "RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE",
  "successor_gate": {
    "new_information_gap": "The accepted Gen2 return proves only a strict axis/readout bridge and exact obstructions for the old clone-product rotation and global chart orientation. It leaves mixed native star-slice geometry and state-level S4 lifting open.",
    "why_parent_result_does_not_close_it": "RR-A8EDE17557A1C30BC189 freezes MIXED_NATIVE_STAR_SLICE_GEOMETRY_AND_STATE_LEVEL_S4_LIFT_NOT_PROVED.",
    "discriminating_outcomes": [
      "construct all mixed native star slices and exact state-level S4 lift",
      "derive the minimal nontrivial state extension/cocycle/groupoid needed for the lift",
      "prove an exact native obstruction and minimal missing axiom/data"
    ],
    "kill_condition": "Do not redo K4/S4, reuse old whole-factor rho as the lift, ignore accepted Z2 holonomy, declare mixed windows geometric by fiat, or quotient native state through carrier readout.",
    "alternative_route_or_free_exploration_considered": "The star/complement theorem kills direct reuse of the clone-product C2 route; extra carrier word enumeration is downstream-only. Mixed native slice gluing plus state-level lift/obstruction is the remaining high-leverage route.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "Generation 5 is the post-review canonical publication of the mathematically unchanged V4 scope; V4 was materialized before the immutable review timestamp and therefore cannot satisfy the governed post-review follow-up rule."
  }
}
-->

# P000 混合三轴切面与状态级 S4 旋转提升 / Z2 holonomy 障碍 V5

Status: `READY / GENERATION-5 / P0 / P000-BOUND / POST-REVIEW-CANONICAL`

数学内容继承 V4，不扩大也不削弱。唯一硬目标：

`P000_MIXED_NATIVE_STAR_SLICES_AND_STATE_LEVEL_ROTATION_LIFT_OR_EXACT_OBSTRUCTION_CLASSIFIED`。

冻结：K4/S4、axis-type beta、star/complement obstruction、旧 C2 no-intertwiner、四 chart Z2 loop holonomy=-1、FCC/HCP 6/3 regression 均不得重做。

必须：构造或否定 `J_B,J_C,J_D` 的 native geometric slice；构造/否定 `tilde R_a,tilde R_b`；检查 `a^3,b^2,(ab)^4` 在 native state 的严格闭合或 hidden residue；若 holonomy 强迫附加状态，只允许加入 exact obstruction 所需的最小 Z2/orientation/incidence/support state，并严格分类其 algebra（S4 / extension / cocycle / groupoid / exact no-go）。

禁止把 chart sign 当 native negative axis，禁止用 carrier kernel quotient native state，禁止 SO(6) 偷渡，禁止经典秩降维。
