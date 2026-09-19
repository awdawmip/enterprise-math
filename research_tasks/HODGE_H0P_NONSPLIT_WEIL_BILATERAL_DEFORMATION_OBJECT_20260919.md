<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT",
  "title": "Hodge H0P — Non-split Weil bilateral deformation object",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "frontier": "A pure nonzero Weil Chern-character candidate is available only as an unreviewed special-fibre checkpoint, while the known direct-sum and cone constructions retain at least seven first-order obstruction directions; no actual object has yet been shown to deform through all nine Weil directions.",
  "next_action": "Construct the smallest mixed torsion/derived candidate with effective maps on both obstruction sides, compute its full Atiyah–Kodaira–Spencer obstruction map over all nine Weil deformation directions, and decide positive full-rank cancellation versus an exact family-level no-go.",
  "dependencies": [
    "RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3"
  ],
  "source_refs": [
    "research_returns/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_RETURN_20260902.md",
    "research_result_records/RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT/RR-65EB865C14B89B964BB9.json",
    "research_returns/HODGE_H0O_NONSPLIT_WEIL_INTERMEDIATE_SUPPORT_FM_EXCEPTIONAL_CH3_RETURN_20260903.md",
    "research_result_records/RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3/RR-FB3CF77C4F611FDED79B.json",
    "research_task_records/RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3/TP2-853EE36ED78FF34CC992.json",
    "research_notes/HODGE_WEIL_BILATERAL_DEFORMATION_FRONTIER_20260919.md"
  ],
  "evidence_status": "CHAT_DERIVED_UNREVIEWED_CHECKPOINT / SOURCE_H0O_NEGATIVE_BOUNDARY_PRESERVED",
  "last_progress_ref": "research_notes/HODGE_WEIL_BILATERAL_DEFORMATION_FRONTIER_20260919.md",
  "hard_block": null,
  "tags": [
    "HODGE",
    "WEIL_SIXFOLD",
    "NONSPLIT",
    "DEFORMATION",
    "ATIYAH_KODAIRA_SPENCER"
  ],
  "claim_lease_minutes": 120,
  "registry_key": "RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT",
  "identity_lane": "HODGEH0P",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3",
  "successor_gate": {
    "new_information_gap": "H0O isolates seed conservation for its declared Fourier–Mukai family, but the surviving frontier is an actual algebraic/derived object whose nonzero Weil component deforms through all nine target directions rather than only as a Hodge class.",
    "why_parent_result_does_not_close_it": "The parent result is a conservation/negative-boundary statement and does not decide whether a mixed torsion or genuinely two-sided derived object can cancel the full first-order obstruction while preserving a nonzero Weil class.",
    "discriminating_outcomes": [
      "Construct one explicit object with nonzero Weil class and zero first-order obstruction on all nine directions.",
      "Prove a precise no-go theorem for the declared mixed candidate class.",
      "Return a strictly delimited partial obstruction classification that identifies the remaining unmapped directions."
    ],
    "kill_condition": "Kill the declared construction family if every admissible candidate has a rigorously verified nonzero obstruction on at least one Weil direction or loses the nonzero Weil component under the required two-sided coupling.",
    "alternative_route_or_free_exploration_considered": "Direct cycle deformation, broader correspondence kernels, and independent free exploration were considered; this task is preferred first because it attacks the obstruction bottleneck already exposed by H0O with a falsifiable finite-dimensional map.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The new candidate class lies outside H0O's frozen family and terminal-alternative repair scope, so extending H0O would blur a completed negative boundary with genuinely new mathematics."
  },
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "last_progress_at": "2026-09-19",
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "HODGE_SPECIAL_OPEN_FRONTIER_ALGEBRAICITY_MECHANISM",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:98ee2981553fb4eeaf5bd8599513719ee2ac987fae875e9c5daf8a3e2156f3cf",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Hodge H0P — Non-split Weil bilateral deformation object

Status: `READY / PUBLISHED_REGISTERED / TASK_TERMINAL_SCOPE`

## 0. Mother question

On the same very-general non-split Weil-type abelian sixfold target with discriminant class `[-3]`, can one construct an actual algebraic or perfect derived object whose codimension-three Chern character has nonzero exceptional Weil component and whose complete first-order deformation obstruction vanishes in all nine Weil deformation directions?

## 1. Frozen inputs and scope

Preserve the H0N exceptional projector and the H0O seed-conservation boundary only at the strength actually established in their source records. Treat the 2026-09-19 bilateral-deformation note as an unreviewed research checkpoint, not as accepted theorem evidence. The declared search space is mixed torsion/derived objects that can provide effective maps on both obstruction sides; simple direct-sum stabilization by torsion-free auxiliary objects is outside the positive route unless a new calculation changes the relevant Hom vanishing. Do not infer the full Hodge conjecture, non-algebraicity, or very-general transport from first-order calculations alone.

## 2. Hard target and required outputs

Produce one exact candidate family and compute the full Atiyah–Kodaira–Spencer obstruction map for the nine-dimensional Weil deformation space. A positive return must exhibit a nonzero exceptional Weil component and zero first-order obstruction in all nine directions for the same object, with explicit Ext/Yoneda data sufficient for independent reproduction. A negative return must prove a family-level no-go with the candidate class and hypotheses stated exactly. Preserve all finite-dimensional matrices, ranks, intersection numbers, and object definitions needed to reproduce the decision.

## 3. Research value to preserve

This task targets the first bottleneck not already removed by H0O: converting a cohomological special class or virtual difference into one actual deformable object. Either a nine-direction cancellation or a clean no-go sharply changes the viable route to algebraicity and prevents repeated searches inside families that only enlarge parameter count without changing obstruction geometry.

## 4. Success, kill, and return criteria

SUCCESS requires one actual object with nonzero exceptional Weil component and verified vanishing of its complete first-order obstruction on all nine Weil directions. NEGATIVE_BOUNDARY requires a theorem-level no-go for the declared candidate class. PARTIAL requires an exact residual obstruction subspace together with a justified next bottleneck. Stop this task before any higher-order or very-general algebraization claim; those belong to a later task only after the positive first-order condition is independently confirmed.
