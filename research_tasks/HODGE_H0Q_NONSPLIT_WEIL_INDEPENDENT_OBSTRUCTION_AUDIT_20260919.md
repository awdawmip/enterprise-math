<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-HODGE-H0Q-NONSPLIT-WEIL-INDEPENDENT-OBSTRUCTION-AUDIT",
  "title": "Hodge H0Q — Independent audit of the bilateral Weil obstruction frontier",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "frontier": "The 2026-09-19 special-fibre projector, graph-combination, Ext-dimension and bilateral-obstruction claims are durable only as an unreviewed checkpoint and must be independently reproduced before they can support later transport.",
  "next_action": "Independently reconstruct the projector identities, special-fibre graph calculations, Ext/Hom dimensions, obstruction-naturalness lemma and rank bounds from source definitions; issue PASS, PARTIAL, or FAIL with explicit counter-calculation where applicable.",
  "dependencies": [
    "RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT"
  ],
  "source_refs": [
    "research_returns/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_RETURN_20260902.md",
    "research_result_records/RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT/RR-65EB865C14B89B964BB9.json",
    "research_returns/HODGE_H0O_NONSPLIT_WEIL_INTERMEDIATE_SUPPORT_FM_EXCEPTIONAL_CH3_RETURN_20260903.md",
    "research_result_records/RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3/RR-FB3CF77C4F611FDED79B.json",
    "research_task_records/RS-HODGE-H0O-NONSPLIT-WEIL-INTERMEDIATE-SUPPORT-FM-EXCEPTIONAL-CH3/TP2-853EE36ED78FF34CC992.json",
    "research_notes/HODGE_WEIL_BILATERAL_DEFORMATION_FRONTIER_20260919.md",
    "research_tasks/HODGE_H0P_NONSPLIT_WEIL_BILATERAL_DEFORMATION_OBJECT_20260919.md"
  ],
  "evidence_status": "INDEPENDENT_REPLICATION_REQUIRED",
  "last_progress_ref": "research_notes/HODGE_WEIL_BILATERAL_DEFORMATION_FRONTIER_20260919.md",
  "hard_block": "Do not certify downstream very-general transport from the checkpoint without independent reproduction.",
  "tags": [
    "HODGE",
    "WEIL_SIXFOLD",
    "INDEPENDENT_AUDIT",
    "EXT",
    "OBSTRUCTION"
  ],
  "claim_lease_minutes": 120,
  "registry_key": "RS-HODGE-H0Q-NONSPLIT-WEIL-INDEPENDENT-OBSTRUCTION-AUDIT",
  "identity_lane": "HODGEH0Q",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-HODGE-H0P-NONSPLIT-WEIL-BILATERAL-DEFORMATION-OBJECT",
  "successor_gate": {
    "new_information_gap": "The new bilateral-obstruction calculations were produced in the same research line and have not yet received an independent derivation from the underlying geometric definitions.",
    "why_parent_result_does_not_close_it": "A positive or negative H0P construction cannot by itself supply independence for the projector, Ext, Hom, naturality, and obstruction-rank premises that later transport would consume.",
    "discriminating_outcomes": [
      "Independent reproduction agrees with every premise needed downstream.",
      "One or more claims fail and a corrected frontier is supplied.",
      "Some claims reproduce while others remain unresolved and are explicitly quarantined from downstream use."
    ],
    "kill_condition": "Kill downstream use of any checkpoint claim that cannot be reproduced from exact source definitions or whose stated rank/dimension changes under an independent calculation.",
    "alternative_route_or_free_exploration_considered": "Embedding the check inside H0P was considered, but a separate audit task is preferable because the user explicitly requested an independent verification path and hidden reliance on the constructing argument must be minimized.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The task has a different epistemic role from H0P: it validates or rejects the reusable premises rather than searching for another candidate object."
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

# Hodge H0Q — Independent audit of the bilateral Weil obstruction frontier

Status: `READY / PUBLISHED_REGISTERED / TASK_TERMINAL_SCOPE`

## 0. Mother question

Which parts of the current non-split Weil special-fibre and bilateral-deformation checkpoint survive an independent reconstruction from the underlying geometry, and which claims must be corrected before any later task may use them?

## 1. Frozen inputs and scope

Use the H0N/H0O source records and the 2026-09-19 frontier note as evidence to be checked, not as conclusions to be assumed. Re-derive the short exceptional projector formula, the signed graph combination, the stated intersection pairings, Ext and Hom dimensions, the obstruction-naturalness implication, and the common allowed deformation subspace. Maintain reviewer independence from the H0P candidate-construction argument wherever the same premise is under audit.

## 2. Hard target and required outputs

Return a claim-by-claim audit ledger with exact definitions, derivations or executable finite checks, and a disposition of PASS, PARTIAL, or FAIL for every premise that H0R would need. Any disagreement must include the corrected formula, dimension, rank, or hypothesis. The audit must distinguish cohomological Hodge persistence from deformation of an actual algebraic or derived object and must not convert a virtual K-class calculation into existence of a flat family.

## 3. Research value to preserve

The next route is unusually sensitive to small rank, sign, and naturality errors. An independent ledger prevents a plausible but incorrect special-fibre calculation from becoming a hidden premise in a very-general-fibre argument and preserves reusable verified pieces even if one component fails.

## 4. Success, kill, and return criteria

SUCCESS requires independent reproduction of every premise explicitly marked as needed for the next transport stage, or a corrected replacement set with the same role. FAIL on a premise blocks that premise from downstream use and returns the corrected frontier to the parent objective. PARTIAL must list exactly which statements remain usable. This task does not itself prove the existence of a deformable object or any higher-order algebraization.
