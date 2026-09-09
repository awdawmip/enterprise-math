<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-DRIVER-PRIME-FUSION-F2-REVISION-REVIEW-INTEGRATION",
  "title": "Driver Prime Fusion F2 revision review and integration",
  "kind": "GOVERNANCE",
  "owner": "driver/governance/prime-fusion-f2-revision-review-integration",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The F2-L04 same-task repair is frozen as RR-80665B86477BADFB81AD on immutable head 72e8c6adc0a9887ddfda9c0bd763f76ff08ba2a3. It replaces the fake primality-storing field certificate with structural IsField(ZMod) predicates and a genuine field-to-prime converse, while preserving the accepted T7/T8 boundary.",
  "next_action": "Review the replacement F2 Result against the prior theorem-spec defect, verify structural fieldness, field-to-prime edge conditions, fixed Gaussian/Eisenstein labels, no theorem weakening, and the pinned warnings-fatal Lean evidence. If accepted, integrate F2 at T7/T8 scope and close the local formalization task; otherwise return an exact same-task correction. Do not create F3 from this governance task.",
  "dependencies": [
    "TP2-7C31E9A4D5B6082F14CE",
    "RR-80665B86477BADFB81AD"
  ],
  "source_refs": [
    "git:awdawmip/enterprise-math@72e8c6adc0a9887ddfda9c0bd763f76ff08ba2a3:research_result_records/RS-PRIME-FUSION-F2-LEAN-RECONSTRUCTION-DUAL-PRIME-FORMALIZATION/RR-80665B86477BADFB81AD.json",
    "git:awdawmip/enterprise-math@72e8c6adc0a9887ddfda9c0bd763f76ff08ba2a3:research_returns/PRIME_FUSION_F2_LEAN_RECONSTRUCTION_DUAL_PRIME_FORMALIZATION_RETURN_20260903.md",
    "git:awdawmip/enterprise-math@c16084e34d5e1e0392ab5dd6684891aa039a772a:research_task_records/RS-PRIME-FUSION-F2-LEAN-RECONSTRUCTION-DUAL-PRIME-FORMALIZATION/TP2-7C31E9A4D5B6082F14CE.json"
  ],
  "evidence_status": "F2_REPLACEMENT_RESULT_FROZEN / SAME_TASK_REVISION / DRIVER_REVIEW_REQUIRED",
  "last_progress_ref": "git:awdawmip/enterprise-math@72e8c6adc0a9887ddfda9c0bd763f76ff08ba2a3:research_result_records/RS-PRIME-FUSION-F2-LEAN-RECONSTRUCTION-DUAL-PRIME-FORMALIZATION/RR-80665B86477BADFB81AD.json",
  "last_progress_at": "2026-09-03T02:31:50+00:00",
  "hard_block": null,
  "tags": [
    "Driver",
    "Prime-Fusion",
    "F2",
    "Lean",
    "review",
    "integration",
    "T7",
    "T8"
  ],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-DRIVER-PRIME-FUSION-F2-REVISION-REVIEW-INTEGRATION",
  "parent_objective_id": "OBJ-PRIME-FUSION-MACHINE-CHECKED-THEOREM-PACKAGE",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "DRV-PFF2",
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

# Driver Prime Fusion F2 revision review and integration

Status: `READY / DRIVER-PUBLISHED GOVERNANCE`

## Mother question

Does the frozen F2 replacement Result now close the exact theorem-spec defect identified in the first Driver review, so that Driver can accept and integrate the T7/T8 Lean layer at its original scope without manufacturing a new F3 research stage?

## Frozen inputs and scope

The research task remains `RS-PRIME-FUSION-F2-LEAN-RECONSTRUCTION-DUAL-PRIME-FORMALIZATION / TP2-7C31E9A4D5B6082F14CE`. The current replacement Result is `RR-80665B86477BADFB81AD` at immutable head `72e8c6adc0a9887ddfda9c0bd763f76ff08ba2a3`.

The prior defect was narrow: the first L04 certificate encoded modulus primality inside its definition and therefore did not prove field structure implies primality. The replacement claims to use structural `IsField (ZMod N)` and `IsField (ZMod C)` predicates, to derive primality through finite characteristic under explicit edge conditions, and to preserve the fixed Gaussian/Eisenstein channel labels.

Preserve all previously accepted T7/T8 mathematics, the no-sorry/no-admit/no-custom-axiom boundary, and the pinned warnings-fatal build requirement. This control task may accept, return, or integrate that exact layer. It may not absorb T9 or T12-T15 and may not turn a local formalization closeout into a new mathematical theorem.

## Hard target and required outputs

Hard target: `PRIME_FUSION_F2_REVISED_RESULT_REVIEWED_AND_T7_T8_FORMALIZATION_INTEGRATED_OR_EXACTLY_RETURNED`.

Required Driver outputs:

1. Verify the immutable replacement Result and its source/return bindings.
2. Compare the revised L04 declarations to the original accepted T8 quotient/field requirement, not merely to the first rejected implementation.
3. Verify that fieldness is structurally stated independently of modulus primality and that the converse proves the required prime modulus facts with all nontriviality edge conditions explicit.
4. Check that fixed Gaussian/Eisenstein projections and channel order are preserved in both directions.
5. Verify the reported warnings-fatal Lean evidence and axiom boundary at the frozen revision.
6. If all obligations pass, issue an exact accepted disposition and integrate only the T7/T8 F2 layer.
7. If any obligation fails, return the smallest same-task correction and preserve all unaffected accepted declarations.

## Research value to preserve

F2 is a proof-kernel closure task, not a discovery route. The value is a machine-checked representation of already accepted T7/T8 mathematics with no circular certificate and no channel-label loss. A durable Driver closeout prevents this nearly finished formalization from remaining stranded simply because the original researcher session ended.

## Success, kill, and return criteria

Success is exact Driver acceptance plus integration at T7/T8 scope, or an exact nonterminal return identifying the smallest remaining theorem-spec or proof-engineering defect.

Kill any attempt to accept the replacement solely because it builds, to hide primality in a renamed predicate, to weaken the accepted source theorem, to erase channel attachment, or to start F3/T9/T12-T15 from this governance task. A later research stage requires its own independently justified successor gate.
