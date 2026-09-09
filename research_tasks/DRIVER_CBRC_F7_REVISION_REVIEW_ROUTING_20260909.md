<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-DRIVER-CBRC-F7-REVISION-REVIEW-ROUTING",
  "title": "Driver CBRC F7 revised no-go review and routing",
  "kind": "GOVERNANCE",
  "owner": "driver/governance/cbrc-f7-revision-review-routing",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The F7 same-task theorem repair is frozen as RR-AA38973D56330E59D315 at immutable head 80df6ad5686052c784a8d3e69a4c6b9451a1db7a. It retracts the false standalone Lemma 3.3 and replaces it with an A0/J-aware block-rank classification while preserving the proposed F7 no-go verdict.",
  "next_action": "Review the revised F7 proof at its exact repaired obligations: retraction consistency, block-rank exhaustion, finite-index saturation/integration, period descent through accepted F4, hub cases, all-rank-one determinant/J-conjugacy classification, and ablations. If accepted, integrate and close F7 at the exact no-go strength, then evaluate any successor separately. If not, return the smallest same-task proof defect. Do not open F8 from this control task.",
  "dependencies": [
    "TP2-6F3A8C21D4B7095E1F62",
    "RR-AA38973D56330E59D315"
  ],
  "source_refs": [
    "git:awdawmip/enterprise-math@80df6ad5686052c784a8d3e69a4c6b9451a1db7a:research_result_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/RR-AA38973D56330E59D315.json",
    "git:awdawmip/enterprise-math@80df6ad5686052c784a8d3e69a4c6b9451a1db7a:research_returns/COHERENT_BRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_CLASSIFICATION_REVISION_20260903.md",
    "git:awdawmip/enterprise-math@c16084e34d5e1e0392ab5dd6684891aa039a772a:research_task_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/TP2-6F3A8C21D4B7095E1F62.json"
  ],
  "evidence_status": "F7_REPLACEMENT_RESULT_FROZEN / OLD_LEMMA_RETRACTED / DRIVER_REVIEW_REQUIRED / NO_FRESH_BLIND_AUDIT_CLAIM",
  "last_progress_ref": "git:awdawmip/enterprise-math@80df6ad5686052c784a8d3e69a4c6b9451a1db7a:research_result_records/RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION/RR-AA38973D56330E59D315.json",
  "last_progress_at": "2026-09-03T03:32:00+00:00",
  "hard_block": null,
  "tags": [
    "Driver",
    "CBRC",
    "F7",
    "review",
    "no-go",
    "routing",
    "proof-repair"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-DRIVER-CBRC-F7-REVISION-REVIEW-ROUTING",
  "parent_objective_id": "COHERENT_BRC_WORKING_EXTENSION",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "DRV-CBRCF7",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "NEW_DIRECTION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:dd425305887871866cb2f0894885ff38359639e2de7750fa45e8c584e19feae4",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Driver CBRC F7 revised no-go review and routing

Status: `READY / DRIVER-PUBLISHED GOVERNANCE`

## Mother question

Does the revised F7 return now supply a theorem-level proof of the claimed rank-two no-go after explicitly retracting the false standalone period/quadratic lemma, and what exact route should follow if that repaired proof is accepted or returned?

## Frozen inputs and scope

The research task remains `RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION / TP2-6F3A8C21D4B7095E1F62`. The repaired frozen Result is `RR-AA38973D56330E59D315` at immutable head `80df6ad5686052c784a8d3e69a4c6b9451a1db7a`.

The first return's standalone Lemma 3.3 is not reusable theorem evidence. The revised return explicitly retracts it, supplies a counterexample to that standalone statement, and claims a replacement proof that uses the actual A0/J constraints and an exhaustive block-rank analysis. Review the replacement proof on its own merits.

Preserve the original clean-blind raw freeze only as provenance of the original model. The repaired execution is source-exposed after that freeze and does not claim a fresh blind-audit pass. Do not manufacture such a label during review.

## Hard target and required outputs

Hard target: `CBRC_F7_REVISED_NO_GO_RESULT_EXACTLY_REVIEWED_AND_ROUTE_CLOSED_OR_RETURNED`.

Required Driver outputs:

1. Verify the replacement Result/return bindings and the explicit retraction of the old standalone lemma.
2. Check that the A0/J-aware block-rank case split is exhaustive and does not assume the desired selector/no-go conclusion.
3. Verify finite-index saturation and discrete quadratic integration wherever used, including the exact integrality hypotheses.
4. Verify the nonzero-period descent through the previously accepted F4 theorem at the precise interface consumed.
5. Check rank-two/rank-one hub cases and the all-rank-one determinant plus integral J-conjugacy classification.
6. Confirm that the ten ablations remain genuine boundary witnesses and are not used as finite substitutes for the infinite theorem.
7. If the repaired proof passes, accept and integrate F7 only at `F7_NO_BALANCED_RANK_TWO_MIXING_EXISTS` strength and close the F7 task scope.
8. If any proof obligation fails, return the smallest same-task correction and retain every unaffected repaired component.

## Research value to preserve

F7 tests whether the minimal rank-two extension can support the frozen balanced-mixing semantics. The repaired return may close that question, but only if the replacement infinite proof survives review. A dedicated Driver task prevents both failure modes: losing a potentially valid no-go because the original proof had one false lemma, or accepting the same verdict without checking the genuinely new proof.

## Success, kill, and return criteria

Success is an exact accepted or nonterminal Driver disposition for `RR-AA38973D56330E59D315`, with source integration and a durable smallest-next-unit handoff.

Kill any attempt to reuse the retracted standalone lemma, to promote bounded ablations into proof, to label the repair as a fresh clean-blind execution, or to publish F8 merely because F7 passes. Any F8 or alternative CBRC route requires a separate successor decision after the F7 disposition.
