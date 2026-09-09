<!-- ENTERPRISE_MATH_TASK_V1
{
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P2",
  "leverage": "MEDIUM",
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCHER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "EM-FREE-F6D046-RAMANUJAN-GEOMETRY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "task_id": "RS-EMF6D046-R107-PPAV-THETA-JACOBIAN",
  "title": "P46 principalizations: global ppav classes and genus-4 Jacobian test",
  "frontier": "After R106 resolves the full local unitary action, the unresolved global question is whether the three C3 principalizations yield one or three unmarked principally polarized abelian fourfold classes and whether any lies in the smooth genus-four Jacobian locus.",
  "next_action": "Use the exact R106 orbit result to construct the global principal polarization classes, then compute theta/Schottky-Igusa data or an equivalent exact genus-four Jacobian criterion. If a Jacobian occurs, produce an explicit curve or certifying modular data; otherwise isolate the exact obstruction.",
  "dependencies": ["RS-EMF6D046-R106-TWO-ADIC-HERMITIAN-UNITARY"],
  "source_refs": [
    "research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md",
    "task:RS-EMF6D046-R106-TWO-ADIC-HERMITIAN-UNITARY"
  ],
  "evidence_status": "R105_HANDOFF_PLUS_R106_REQUIRED",
  "last_progress_ref": "research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md",
  "last_progress_at": "2026-09-09T10:21:00+08:00",
  "hard_block": "GLOBAL_PPAV_ORBITS_AND_GENUS4_JACOBIAN_CRITERION",
  "tags": ["EM-FREE-F6D046", "P46", "ppav", "theta", "Schottky-Igusa", "genus4", "Jacobian", "principalization"],
  "registry_key": "RS-EMF6D046-R107-PPAV-THETA-JACOBIAN",
  "identity_lane": "RF6D107",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-EMF6D046-R106-TWO-ADIC-HERMITIAN-UNITARY",
  "successor_gate": {
    "new_information_gap": "R106 can determine the local unitary orbit of the three principalization lines, but local orbit equivalence does not decide global unmarked ppav isomorphism or membership in the smooth genus-four Jacobian locus.",
    "why_parent_result_does_not_close_it": "The global polarization class and theta/Schottky data are not encoded by the local two-adic permutation action alone.",
    "discriminating_outcomes": "Either the three principalizations collapse to one global ppav class or remain three classes; for each resulting class, theta/Schottky data either prove a smooth genus-four Jacobian realization or give an exact obstruction.",
    "kill_condition": "Stop any route that treats indecomposability alone as a genus-four Jacobian criterion or that identifies ppav classes solely from the local C3 action.",
    "alternative_route_or_free_exploration_considered": "An explicit genus-four curve search and a Schottky-Igusa/theta-constant computation are independent routes; use whichever yields exact certification first and cross-check when feasible.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The input changes from local integral lattice automorphisms to global principal polarizations and theta geometry, requiring different invariants and a distinct acceptance criterion."
  }
}
-->

# P46 principalizations: global ppav classes and genus-4 Jacobian test

Status: `READY / CONTINUATION AFTER R106 / PUBLISHED_REGISTERED`

## 0. Entry point and dependency

Read `research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md` first, then consume task `RS-EMF6D046-R106-TWO-ADIC-HERMITIAN-UNITARY` and its exact output. Do not infer global ppav equivalence before the full local unitary action is certified.

## 1. Hard target

Decide the global unmarked ppav orbit of the three R105 principalizations and determine whether any resulting ppav lies in the smooth genus-four Jacobian locus.

Required outputs:

1. Decide exactly whether the three principalizations define one or three global unmarked ppav isomorphism classes; if a more refined outcome is mathematically forced, prove why it is compatible with the R106 action.
2. For each global class, compute exact theta data, Schottky-Igusa data, or another rigorous genus-four Jacobian criterion.
3. If a smooth Jacobian occurs, give an explicit genus-four curve or equivalent certifying construction and identify its polarization class.
4. If none occurs, identify the exact modular/theta obstruction.
5. Separate geometric indecomposability from the stronger Jacobian condition.

## 2. Frozen exclusions

The canonical Weil-restriction product polarization is already integrally separated from every Prym principalization; it must not be relabeled as the desired smooth Jacobian. Numerical theta recognition without certification is insufficient.

## 3. Return criterion

Return a global ppav orbit theorem together with a rigorous Jacobian/non-Jacobian classification, or freeze the first exact theta/Schottky datum still missing.
