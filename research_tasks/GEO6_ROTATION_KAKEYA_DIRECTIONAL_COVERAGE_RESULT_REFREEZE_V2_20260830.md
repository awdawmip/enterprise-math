<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-ROTATION-KAKEYA-DIRECTIONAL-COVERAGE",
  "title": "GEO6 Rotation Kakeya Directional Coverage Result envelope re-freeze V2",
  "kind": "RESEARCH",
  "owner": "research/geo6-rotation-kakeya-directional-coverage",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Re-freeze the completed six-axis Kakeya negative boundary with a complete Result output manifest, preserving exactly the forest overlap theorem K6(r)=6r-5 and the dependent-direction cycle countermodel.",
  "next_action": "Reproduce the frozen return, checker and coverage certificate from the exact prior research head, create a fresh authorized execution record and NEW Result-ID, and pin return + checker + certificate + execution record with Git blob SHA-1 and SHA-256; do not alter the negative-boundary theorem.",
  "dependencies": [
    "TP2-46A7AB0834EC4AA32869",
    "RR-1EE9F0E97E13FBBD1742"
  ],
  "source_refs": [
    "PR #885@0da1238160fd8eb6a62d6fda1d051d7148539b19",
    "RR-1EE9F0E97E13FBBD1742@0da1238160fd8eb6a62d6fda1d051d7148539b19"
  ],
  "evidence_status": "MATHEMATICAL_PAYLOAD_RETAINED / RESULT_ENVELOPE_INCOMPLETE / ZERO_MATH_DRIFT_REFREEZE_REQUIRED",
  "last_progress_ref": "PR #885 / RR-1EE9F0E97E13FBBD1742",
  "last_progress_at": "2026-08-30T03:30:00+00:00",
  "hard_block": null,
  "tags": [
    "GEO6",
    "result-integrity",
    "envelope-refreeze",
    "maintenance",
    "zero-math-drift"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-ROTATION-KAKEYA-DIRECTIONAL-COVERAGE",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6KAKR2",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# GEO6 Rotation Kakeya Directional Coverage Result envelope re-freeze V2

Status: `READY / RESULT INTEGRITY MAINTENANCE / ZERO MATH DRIFT`

## Mother question

Can the already completed mathematical result `RR-1EE9F0E97E13FBBD1742` be re-frozen under a fresh authorized execution with a contract-complete immutable digest chain and no change to its theorem, countermodels, scope firewall, or unresolved residue?

## Frozen inputs and scope

The prior research head is `0da1238160fd8eb6a62d6fda1d051d7148539b19`. Preserve exactly: the independent six-axis forest-incidence proof; exact K6(r)=6r-5 for r>=2; nonuniqueness of extremizers; the dependent-direction triangle/cycle countermodel; carrier-S4 typing boundary; and the residue that mixed/refining native directions remain semantically open. The old Result remains immutable historical evidence and must not be edited. This maintenance task repairs evidence integrity only.

## Hard target and required outputs

Hard target: `RS-GEO6-ROTATION-KAKEYA-DIRECTIONAL-COVERAGE_RESULT_ENVELOPE_REFROZEN_WITH_COMPLETE_DIGEST_CHAIN_AND_ZERO_MATH_DRIFT`.

Required outputs: revision return, deterministic checker, exact coverage certificate, fresh execution record, and a NEW Result record whose output_manifest fixes every output with both digests.

A fresh Result-ID and truthful owner head are required.

## Research value to preserve

The mathematics has already passed Driver substantive inspection. The only blocking issue is an incomplete immutable Result envelope. Repairing the digest chain preserves the research while preventing an incomplete record from becoming canonical review authority.

## Success, kill, and return criteria

Success: a fresh execution yields a NEW Result-ID with the same mathematical payload and a complete digest chain. Kill the maintenance attempt if replay or byte comparison reveals theorem/checker/certificate drift; that would require substantive revision rather than integrity acceptance. Do not open a stronger mathematical successor from this maintenance execution.
