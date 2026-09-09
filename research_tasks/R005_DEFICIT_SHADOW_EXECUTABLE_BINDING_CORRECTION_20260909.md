<!-- ENTERPRISE_MATH_TASK_V1
{
  "priority": "P1",
  "leverage": "HIGH",
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "parent_objective_id": "OBJ-R005-PRIME-ALGORITHM-LAB-RELAY-20260909",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "claim_lease_minutes": 360,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  },
  "title": "R005 deficit-shadow executable binding correction",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "frontier": "The Sep-3 R005-A DSI handoff reduces q=78553 to a finite exact-916 gap-shadow obligation, but the committed scanner has a metadata typo and malformed coverage diagnostic, and the validation transcript/manifest do not bind executable final repository bytes.",
  "next_action": "Repair only the scanner and evidence bindings, add a real positive attested-catalog regression path, rerun final-byte validation, and freeze a new correction Result without changing DSI mathematics or extending the q=78553 frontier.",
  "dependencies": [],
  "source_refs": [
    "git:awdawmip/enterprise-math@f9e2a611b45631c43effce36b7300c6f9a56b77b:docs/R005A_P2_DEFICIT_SHADOW_INVERSION_20260902.md",
    "git:awdawmip/enterprise-math@f9e2a611b45631c43effce36b7300c6f9a56b77b:experiments/r005a_p2_gap_shadow_inversion.py",
    "research_activity_records/RA-PR1140-P8H4Q2-20260909.json"
  ],
  "evidence_status": "DRIVER_BLOCKING_REVIEW_FOUND_EXECUTABLE_BYTE_DEFECT / DSI_MATHEMATICS_NOT_REOPENED",
  "last_progress_ref": "research_activity_records/RA-PR1140-P8H4Q2-20260909.json",
  "last_progress_at": "2026-09-09T05:57:46+00:00",
  "hard_block": null,
  "tags": ["R005", "maintenance", "deficit-shadow", "executable-binding", "q78553"],
  "identity_lane": "R005FIX1",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "task_id": "RS-R005-DEFICIT-SHADOW-EXECUTABLE-BINDING-CORRECTION",
  "registry_key": "RS-R005-DEFICIT-SHADOW-EXECUTABLE-BINDING-CORRECTION"
}
-->

# R005 deficit-shadow executable binding correction

## Mother question

Can the Sep-3 deficit-shadow package be made internally auditable at the exact stored-byte level while leaving the DSI mathematics and certified frontier unchanged?

## Frozen inputs and scope

Freeze DSI1/DSI2/DSI3, the q=78553 constants, the gap-start band `[1291005053866735,1294364244470160]`, and the certified frontier `k <= 2822453183433`. Reproduce and repair the undefined `metada` reference and malformed coverage diagnostic in the stored scanner. Do not obtain the full 916-gap catalogue or claim q=78553 closure here.

## Hard target and required outputs

Hard target: `R005_DEFICIT_SHADOW_EXECUTABLE_BINDING_CORRECTED_AND_REVALIDATED`.

Return a syntactically valid fail-closed scanner; a regression that reaches `completeness_attestation=true` and exercises coverage/max-gap/positive scanner logic; exact final-byte syntax and focused regression evidence; regenerated transcript and manifest hashes; and a new immutable correction Result pinning the final source revision and unchanged mathematical boundary.

## Research value to preserve

The DSI reduction collapses a huge seam scan to sparse gap shadows. Repairing delivery integrity preserves that structural work without forcing a successor researcher to reconstruct the mathematics or trust stale validation evidence.

## Success, kill, and return criteria

Success requires the final stored scanner to parse and execute, the positive attested path to be tested, and the transcript/manifest/Result to bind those same bytes. Return `REVISION_REQUIRED` for remaining delivery defects and `MATHEMATICAL_SCOPE_DRIFT` if the repair changes DSI semantics. Stop when the corrected package is frozen; q=78553 seam closure belongs to a separate task.
