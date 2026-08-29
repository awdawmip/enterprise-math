<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-6D-AXIS-MIXING-ROTATION-GROUPOID",
  "title": "P000 六维进取空间的单轴混合旋转与切面胶合",
  "kind": "RESEARCH",
  "owner": "research/p000-6d-axis-mixing-rotation-groupoid",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Refine the accepted C2 complementary-block exchange into a genuinely finer native six-dimensional rotation structure that can mix individual visible and hidden axes or prove the exact obstruction, without importing unsupported classical metric or angle structure.",
  "next_action": "Starting from the accepted clone-product model as a regression only, define the weakest candidate generators that move less than an entire three-axis block, classify their legal domains and preserved Cell relations, and determine whether mixed three-axis observation slices arise as exact transported slices.",
  "dependencies": [
    "p000_reality_foundation.json@main",
    "research_returns/P000_6D_ROTATION_SLICE_TOMOGRAPHY_RETURN_20260829.md@main",
    "driver_reviews/P000_6D_ROTATION_SLICE_TOMOGRAPHY_DRIVER_REVIEW_20260829.md@main"
  ],
  "source_refs": [
    "research_tasks/P000_6D_ROTATION_SLICE_TOMOGRAPHY_20260829.md@main"
  ],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": "driver_reviews/P000_6D_ROTATION_SLICE_TOMOGRAPHY_DRIVER_REVIEW_20260829.md",
  "last_progress_at": "2026-08-29T01:13:30+00:00",
  "hard_block": null,
  "tags": [
    "MATHEMATICAL_CONTINUATION",
    "DRIVER_AUTO_FOLLOWUP",
    "P000",
    "6D-space",
    "axis-mixing",
    "rotation",
    "groupoid",
    "mixed-slice"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-6D-AXIS-MIXING-ROTATION-GROUPOID",
  "parent_objective_id": "OBJ-P000-ENTERPRISE-6D-ROTATION-TOMOGRAPHY",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P0006DAX",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-6D-ROTATION-SLICE-TOMOGRAPHY",
  "successor_gate": {
    "new_information_gap": "The accepted minimal model exposes hidden information only by swapping two whole three-axis blocks. It does not classify individual-axis mixing, mixed three-axis slices, or the native rotation structure beyond C2.",
    "why_parent_result_does_not_close_it": "The clone-product theorem is an exact existence construction, but its only nontrivial global rotation exchanges the complete visible and hidden factors. This does not determine the richer rotation geometry required by the P000 programme.",
    "discriminating_outcomes": [
      "Construct a nontrivial native group action that mixes individual axes across the two blocks while preserving an exact six-axis Cell relation.",
      "Construct the strongest partial-action/groupoid replacement with explicit legal domains and mixed-slice transitions.",
      "Prove an exact obstruction showing that finer axis mixing cannot be defined without adding new native incidence axioms."
    ],
    "kill_condition": "Any purported refinement that only renames or swaps the two three-axis blocks, or silently imports SO(6), Euclidean angles, a continuous metric, or an unproved mixed-slice structure, does not close the task.",
    "alternative_route_or_free_exploration_considered": "Closure at the minimal model was considered and rejected for the parent P000 geometry objective because the role of rotation remains underdetermined. Enlarging a finite census was also rejected because the missing object is structural.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The accepted task has a clean terminal theorem at minimal existence strength. A separate continuation preserves that theorem as a regression while isolating the strictly stronger rotation question."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 六维进取空间的单轴混合旋转与切面胶合

Status: `READY / DRIVER REVIEW FOLLOW-UP / P000-BOUND`

## Mother question

Assuming P000 unconditionally, can the accepted whole-block exchange rotation be refined to an exact native operation that mixes fewer than three axes at a time, thereby connecting visible and hidden coordinates more finely; and if not, what is the exact obstruction or partial-action/groupoid replacement?

## Frozen inputs and scope

P000 remains fixed: six native spatial dimensions, one time dimension, discrete Cell space, rotation as the primary geometric transformation, and three-axis geometry as a slice only.

The accepted result `RR-728A860D0C425719BCDB` is frozen only at `MINIMAL_TYPED_CLONE_PRODUCT_MODEL` strength. Preserve as regressions `X_6=C_A×C_B`, the complementary slice pair, the block exchange `rho`, the hidden-to-visible witness, the separation of phase/support/slice/observation, and the exact two-shot fixed-slice tomography theorem.

Do not assume that the clone product is canonical, that the hidden block must copy the visible block, that mixed slices exist, or that a Euclidean six-dimensional metric/angle table is available.

## Hard target and required outputs

Hard target: `P000_6D_INDIVIDUAL_AXIS_MIXING_ROTATION_OR_EXACT_OBSTRUCTION_CLASSIFIED`.

Required outputs: define the smallest generators changing less than an entire three-axis block; give exact legal domains and preserved native Cell relations; classify composition/inversion as a group, partial group action, groupoid, or exact no-go; determine whether any mixed three-axis slice can arise without assumption; exhibit a hidden-to-visible witness under the finer action or prove the obstruction; derive the observation/identifiability relation; and recover the accepted C2 two-shot model as an exact regression.

## Research value to preserve

The P000 programme treats rotation as the characteristic geometric operation. The minimal accepted model proves that hidden dimensions can become operational, but whole-block exchange is too coarse to reveal the genuine six-axis rotation structure. This task isolates the next structural layer without discarding the first exact tomography theorem.

## Success, kill, and return criteria

Success is a strictly finer native axis-mixing rotation structure with exact semantics, or a sharp obstruction theorem showing what additional native incidence axiom would be required.

Kill any construction that merely renames/swaps the two three-axis blocks, imports `SO(6)` or a classical metric/angle table as native truth, assumes mixed slices by declaration, or loses the accepted hidden-to-visible and two-shot regression facts.

If deterministic global mixing fails, return the strongest exact partial action/groupoid and its smallest obstruction witness.
