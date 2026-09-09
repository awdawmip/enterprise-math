<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GV-PCF7-STATEMENT-CORRECTION-DRIVER-REVIEW",
  "title": "PCF7 statement-correction Driver review gate",
  "kind": "GOVERNANCE",
  "owner": "governance",
  "base_state": "BLOCKED",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "PCF7's main polynomial-prefix obstruction is preserved, but terminal acceptance is blocked until the current statement-correction task freezes a replacement Result that repairs only the zero-probe sentence and binds exact evidence bytes.",
  "next_action": "After a current-generation PCF7 correction Result exists, refresh its exact bytes, review only the authorized zero-probe/evidence delta, record ACCEPTED or the narrowest revision disposition, and preserve the polynomial-prefix theorem, L=N classification and PCF2 benchmark boundary unchanged.",
  "dependencies": [
    {
      "task_id": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION",
      "required_artifact": "current-generation immutable correction Result"
    }
  ],
  "source_refs": [
    "research_task_records/RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION/TP2-1C146C521C5946742C17.json",
    "research_result_reviews/RR-A9A5ADD3931B3F3EDFAB/DR-8183213860B7A72A2BD3.json",
    "research_artifacts/PCF_PERSISTENT_LINE_DRIVER_20260909/dossier.md"
  ],
  "evidence_status": "BLOCKED_ON_CURRENT_PCF7_CORRECTION_RESULT / EXACT_DELTA_DRIVER_REVIEW_REQUIRED",
  "last_progress_ref": "research_result_reviews/RR-A9A5ADD3931B3F3EDFAB/DR-8183213860B7A72A2BD3.json",
  "last_progress_at": "2026-09-02T12:56:00+00:00",
  "hard_block": {
    "missing_object": "current-generation PCF7 statement-correction Result",
    "owner": "RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION",
    "unblock_condition": "A current-generation immutable Result exists for the statement-correction task."
  },
  "tags": [
    "PCF",
    "PCF7",
    "driver-review",
    "governance",
    "statement-correction"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "GV-PCF7-STATEMENT-CORRECTION-DRIVER-REVIEW",
  "parent_objective_id": "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION",
  "parent_objective_generation_id": "OG-AA2BAD92F59DC97880C7",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "PCF7DRV",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# PCF7 statement-correction Driver review gate

Status: `BLOCKED / PUBLISHED_REGISTERED / DRIVER EXACT-DELTA REVIEW`

## Mother question

Does the current PCF7 correction Result repair exactly the false zero-probe statement while preserving every accepted part of the polynomial-prefix failure theorem and its complexity boundary?

## Frozen inputs and scope

This task is blocked until `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION` / `TP2-1C146C521C5946742C17` has a current-generation immutable Result.

The review consumes the original PCF7 Result `RR-A9A5ADD3931B3F3EDFAB`, its `REQUEST_REVISION` review `DR-8183213860B7A72A2BD3`, and the new correction Result. The only authorized mathematical delta is:

- zero fixed probe: `gcd(N,0)=N`;
- nonzero fixed probe whose prime support is avoided: gcd `1`;
- neither case yields a proper factor.

The Driver must preserve the frozen polynomial-prefix infinite balanced-family obstruction, exact worst-case proper-split probability `0` for the declared campaign model, `L=N` recurrence classification, T1–T5 and the sealed PCF2 benchmark boundary. No universal factoring lower bound or new algorithm is under review.

## Hard target and required outputs

Hard target:

`PCF7_CORRECTION_EXACTLY_REVIEWED_AND_TERMINAL_DISPOSITION_RECORDED`

Required Driver outputs:

1. refresh and bind the exact current correction Result bytes at the review write boundary;
2. check the before/after statement audit and checker/certificate consistency;
3. decide `ACCEPTED` only if the mathematical delta is limited to the zero-probe sentence and evidence refresh;
4. otherwise issue the narrowest exact revision disposition without reopening already-proved parts;
5. update the persistent PCF dossier and review ledger with the immutable review identifier and remaining obligations.

## Research value to preserve

A small false sentence can contaminate an otherwise useful negative theorem if it is silently ignored. A dedicated Driver gate closes that defect without making the whole PCF7 proof pay another full research cycle.

It also gives downstream portfolio synthesis one clean terminal PCF7 object rather than a conversation-level assurance that the error was harmless.

## Success, kill, and return criteria

Success is a terminal Driver disposition on the current correction Result at exact corrected scope.

Reject or request revision if the Result changes the campaign model, the polynomial-prefix theorem, the `L=N` calculation, the sealed benchmark, or the no-global-lower-bound guard.

Do not broaden this review into a new factorization task. The post-audit portfolio gate owns successor selection.
