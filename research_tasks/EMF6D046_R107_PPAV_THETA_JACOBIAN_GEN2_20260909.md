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

## 0. Mother question

After the full local unitary action is known, do the three R105 principalizations define one or three global unmarked principally polarized abelian fourfolds, and does any resulting ppav lie in the smooth genus-four Jacobian locus?

## 1. Frozen inputs and scope

Read `research_notes/EM_FREE_F6D046_R105_STATE_MACHINE_HANDOFF_20260909.md` first, then consume the exact output of `RS-EMF6D046-R106-TWO-ADIC-HERMITIAN-UNITARY`.

The canonical Weil-restriction product polarization is already integrally separated from every Prym principalization and cannot be relabeled as the desired smooth Jacobian. Local two-adic equivalence is not global ppav isomorphism. An indecomposable principally polarized fourfold is not automatically a genus-four Jacobian.

## 2. Hard target and required outputs

Hard target: `GLOBAL_PPAV_ORBITS_AND_GENUS4_JACOBIAN_CRITERION`.

1. Decide exactly whether the three principalizations define one or three global unmarked ppav isomorphism classes; if a different refined outcome is forced, prove it against the R106 action and global descent data.
2. For each global class, compute exact theta data, Schottky-Igusa data, or another rigorous genus-four Jacobian criterion.
3. If a smooth Jacobian occurs, give an explicit genus-four curve or equivalent certifying construction and identify its polarization class.
4. If none occurs, identify the exact modular/theta obstruction.
5. Separate geometric indecomposability, ppav isomorphism, and Jacobian membership throughout the proof.

## 3. Research value to preserve

The R105/R106 route resolves the arithmetic local carrier of the three principalizations but cannot by itself decide global polarization geometry. This task isolates the genuinely global Schottky/theta layer and prevents a local `C3` orbit from being overinterpreted as a global Jacobian theorem.

A positive result would produce a new explicit genus-four Jacobian realization inside the same isogeny class; a negative result would identify the exact theta obstruction and close the principalization branch without ambiguity.

## 4. Success, kill, and return criteria

Success is a global ppav orbit theorem together with a rigorous Jacobian/non-Jacobian classification for every resulting class.

Kill any route that treats indecomposability alone as a genus-four Jacobian criterion, infers global ppav equivalence solely from the local `C3` action, or relies on uncertified numerical theta recognition.

An explicit genus-four curve search and a Schottky-Igusa/theta-constant computation are independent routes; use whichever yields exact certification first and cross-check when feasible. Return the theorem or the first exact theta/Schottky datum still missing.
