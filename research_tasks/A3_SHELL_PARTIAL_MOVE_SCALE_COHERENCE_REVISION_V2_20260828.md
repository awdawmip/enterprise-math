<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION",
  "title": "A3 外壳递归部分动作的跨尺度一致性与径向缺陷修订",
  "kind": "RESEARCH",
  "owner": "research/a3-shell-partial-move-scale-coherence-revision",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Repair the state-level scale square after an exact counterexample showed that frame-only double-coset phase does not detect scale-dependent support shift of partial shell moves.",
  "next_action": "Define the actual scale-indexed partial actions and restrictions, replay the frozen n=2 g=(23) interior-marker counterexample, and derive the strongest support/domain-aware radial defect or exact impossibility theorem before revisiting dependent scale observables.",
  "dependencies": [
    "driver_reviews/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_DRIVER_PREMERGE_REVIEW_20260828.md@main",
    "research_returns/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_RETURN_20260828.md@main"
  ],
  "source_refs": [
    "scripts/check_a3_recursive_shell_alignment_tomography.py@main"
  ],
  "evidence_status": "DRIVER_FINAL_REJECTED_PARENT_PASS / EXACT_H4_COUNTEREXAMPLE / VERIFIED_H1_H3_SUBRESULTS_PRESERVED / FIXED_H_ALGEBRA_SIDE_RESULT_ONLY",
  "last_progress_ref": "driver_reviews/A3_RECURSIVE_SHELL_ALIGNMENT_TOMOGRAPHY_DRIVER_PREMERGE_REVIEW_20260828.md",
  "last_progress_at": "2026-08-28T08:28:42+00:00",
  "hard_block": null,
  "tags": ["A3","recursive-shell","revision","partial-move","scale-coherence","radial-defect","groupoid"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-A3-SHELL-PARTIAL-MOVE-SCALE-COHERENCE-REVISION",
  "parent_objective_id": "OBJ-A3-RECURSIVE-SHELL-ALIGNMENT-AND-BULK-OBSERVATION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "A3SCR",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-A3-RECURSIVE-SHELL-ALIGNMENT-TOMOGRAPHY",
  "successor_gate": {
    "new_information_gap": "The parent result's H4 iff criterion is false: identical adjacent frame aligners can have identity double-coset defect while different scale supports make the two nested-state paths disagree.",
    "why_parent_result_does_not_close_it": "The parent checker tested compressed frame classes rather than the two state-level paths; the fixed-subgroup side result repairs only compressed-label composition.",
    "discriminating_outcomes": [
      "Prove a support/domain-aware exact coherence criterion for the state-level scale square.",
      "Prove that no frame-only quotient can classify the square and give the strongest exact relation or groupoid replacement.",
      "Derive a minimal support-transition obstruction that completely explains failure of descent."
    ],
    "kill_condition": "Any candidate depending only on the adjacent frame double coset, without evaluating actual scale-indexed partial actions and restrictions, is non-closing.",
    "alternative_route_or_free_exploration_considered": "Closing the route, enlarging the finite census, and treating the fixed-subgroup algebra as sufficient were considered; the explicit state-level counterexample isolates partial-move scale coherence as the smaller decisive frontier.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent generation contains a merged false H4 PASS claim, so a separate revision generation preserves verified subresults while giving the counterexample an explicit regression boundary."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b78f85af4629ddb714870c44535ad0393418dbc3bebe06da142a90c0c6b9075e",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# A3 外壳递归部分动作的跨尺度一致性与径向缺陷修订

Status: `PUBLISHED_REGISTERED / CONTINUATION / H4 REVISION`

## Mother question

What exact object classifies the actual comparison between align-then-restrict and restrict-then-align when a legal shell move has scale-dependent partial support?

## Frozen inputs and scope

Preserve the verified A3 shell census, 24-frame sign-twisted action, residual-stabilizer alignment analysis, and depth-1 shielding/depth-2 first-coupling facts from the parent package. Do not restart those units unless a direct dependency failure is proved.

Freeze the Driver regression at adjacent scales 3 and 2 with the same aligner \(g=(23)\), pointer targets \(a_k=(k,-k,0,0)\), compatible shell markers \(p_k=R_g^{-1}a_k\), and interior marker \(p=(1,-1,0,0)\in S_1\). The scale-3 depth-2 action fixes \(p\), while the scale-2 depth-2 action sends it to \((-1,0,1,0)\); these are not equivalent under \(H=\{e,(12)\}\), although the adjacent frame double-coset defect is the identity class.

The fixed-subgroup double-coset/pair-groupoid theorem may be reused only as a compressed special case after its hypotheses are matched.

## Hard target and required outputs

Hard target: `A3_PARTIAL_MOVE_SCALE_COMMUTATION_AND_RADIAL_DEFECT_EXACTLY_CLASSIFIED`.

Required outputs are: exact scale-indexed partial action and restriction definitions; a proof or refutation of operation descent; deterministic replay of the frozen counterexample; the strongest correct support/domain-aware radial defect or no-go theorem; an exact projection statement for any fixed-subgroup quotient; re-audit of dependent scale observables; and a checker that evaluates both state-level paths themselves.

## Research value to preserve

The central phenomenon is that a nominally identical rotation can penetrate to different radial depth after resizing the observed world. Correctly separating frame phase from support/domain transport can turn recursive shell alignment into a genuine boundary-to-bulk diagnostic rather than a coordinate-only normalization.

## Success, kill, and return criteria

Success requires an exact state-level classification of the scale square with the frozen counterexample handled correctly. Kill any frame-only repair that ignores support/domain shift, any checker that tests only group multiplication, and any larger census that leaves the state-level commutation defect unresolved. If no compact invariant survives, return the strongest exact relation/groupoid formulation and the smallest collision witness preventing further compression.
