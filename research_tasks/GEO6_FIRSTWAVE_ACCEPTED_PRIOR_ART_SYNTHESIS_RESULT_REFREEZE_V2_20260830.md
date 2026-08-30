<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-FIRSTWAVE-ACCEPTED-PRIOR-ART-SYNTHESIS",
  "title": "GEO6 第一波 prior-art synthesis Result envelope re-freeze V2",
  "kind": "RESEARCH",
  "owner": "research/geo6-firstwave-accepted-prior-art-synthesis",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Re-freeze the completed 19-claim first-wave GEO6 prior-art synthesis with a complete Result manifest that includes the return, checker, exact claim-source matrix and a fresh execution record, with zero mathematical drift.",
  "next_action": "Reproduce the frozen audit from PR #922 / branch head bf9c6bf53d0762aa9cc762f3dfc08eed20469bd4, preserve all 19 claim classifications and selector residues, create a fresh execution record and NEW Result-ID, and bind every output with Git blob SHA-1 plus SHA-256.",
  "dependencies": [
    "RR-F4C8092F1AC6678344DF",
    "PR-922"
  ],
  "source_refs": [
    "research/geo6-firstwave-prior-art-synthesis-em-g6pa-9c72f1@bf9c6bf53d0762aa9cc762f3dfc08eed20469bd4",
    "research_returns/GEO6_FIRSTWAVE_ACCEPTED_PRIOR_ART_SYNTHESIS_RETURN_20260830.md@branch:research/geo6-firstwave-prior-art-synthesis-em-g6pa-9c72f1",
    "research_artifacts/GEO6_FIRSTWAVE_ACCEPTED_PRIOR_ART_SYNTHESIS/claim_source_matrix.json@branch:research/geo6-firstwave-prior-art-synthesis-em-g6pa-9c72f1"
  ],
  "evidence_status": "MATHEMATICAL_AUDIT_RETAINED / RESULT_MANIFEST_INCOMPLETE / CLAIM_MATRIX_AND_EXECUTION_RECORD_MISSING_FROM_MANIFEST",
  "last_progress_ref": "PR #922 / RR-F4C8092F1AC6678344DF",
  "last_progress_at": "2026-08-30T07:22:08+00:00",
  "hard_block": null,
  "tags": [
    "GEO6",
    "prior-art",
    "result-integrity",
    "maintenance",
    "revision"
  ],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-FIRSTWAVE-ACCEPTED-PRIOR-ART-SYNTHESIS",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6PAR2",
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

# GEO6 第一波 prior-art synthesis Result envelope re-freeze V2

Status: `READY / INTEGRITY MAINTENANCE / ZERO MATH DRIFT`

## Mother question

Can the already completed GEO6 first-wave prior-art synthesis be re-frozen as a contract-complete Result without changing any claim classification, source comparison, no-novelty guard, or surviving P000 semantic selector?

## Frozen inputs and scope

The mathematical payload is fixed by PR `#922`, Result `RR-F4C8092F1AC6678344DF`, and branch head `bf9c6bf53d0762aa9cc762f3dfc08eed20469bd4`. Preserve exactly the 19 audited claims/obstructions and the counts `3 EXACT_DUPLICATE / 10 STRICT_ANTECEDENT / 3 ADJACENT_METHOD / 3 NO_MATERIAL_MATCH`. Preserve the rule `NO_MATERIAL_MATCH != NOVELTY_CERTIFICATE`. Preserve the surviving selector residue exactly: `CONTACT_SELECTOR`, `LOCALITY_REFINEMENT_SELECTOR`, `ROTATION_CLOSURE_SELECTOR`, `TRANSLATION_ACTION_SELECTOR`. This is integrity maintenance only.

## Hard target and required outputs

Hard target: `GEO6_FIRSTWAVE_PRIOR_ART_SYNTHESIS_REFROZEN_WITH_COMPLETE_DIGEST_CHAIN_AND_ZERO_MATH_DRIFT`.

Freeze a NEW Result-ID under a fresh execution record. The output manifest must include at least:
1. the revision return;
2. the deterministic checker;
3. the exact `claim_source_matrix.json`;
4. the fresh execution record;
with `path + Git blob SHA-1 + SHA-256` on every row. The return must also carry its top-level SHA-256 pin.

## Research value to preserve

The completed audit removed unsupported novelty pressure and isolated four genuinely semantic P000 selectors. Those conclusions are useful and must not be recomputed or weakened merely because the old Result envelope omitted two outputs.

## Success, kill, and return criteria

Success is a zero-mathematical-drift Result whose return/checker/matrix content reproduces the frozen audit and whose execution/result chain passes the current Result contract. Kill any attempt to change the 19 classifications, infer novelty from no-match rows, or open selector mathematics from this maintenance execution. If any source artifact cannot be reproduced truthfully, return `PROVENANCE_FAILURE` instead of silently substituting new mathematics. After a valid repaired Result is frozen, Driver review decides whether any selector task is justified.
