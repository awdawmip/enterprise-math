<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-FIRSTWAVE-ACCEPTED-PRIOR-ART-SYNTHESIS",
  "title": "GEO6 first-wave prior-art Result schema repair V3",
  "kind": "RESEARCH",
  "owner": "research/geo6-firstwave-accepted-prior-art-synthesis",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Re-freeze the completed 19-claim first-wave GEO6 prior-art synthesis through the current canonical Result writer, changing only invalid typed Result metadata while preserving the return, checker, claim-source matrix, 3/10/3/3 classifications and four selector residues with zero mathematical drift.",
  "next_action": "Replay generation-2 evidence, create a fresh execution record and NEW Result-ID, use canonical typed fields exactly (SUCCESS, RESULT_ONLY, NOT_APPLICABLE, NONBLIND_DISCLOSED), and bind return + checker + matrix + fresh execution record with Git blob SHA-1 and SHA-256.",
  "dependencies": ["TP2-364C8C41A848FB12F86E", "RR-0C87FC289FDC9FD77641"],
  "source_refs": ["research/geo6-firstwave-prior-art-refreeze-v2-em-g6par2-e385c3@b14d9629e2c1d7139847bc3c503aae9e796e94d5"],
  "evidence_status": "MATHEMATICAL_PAYLOAD_RETAINED / COMPLETE_DIGEST_CHAIN / RESULT_TYPED_ENUM_INVALID",
  "last_progress_ref": "RR-0C87FC289FDC9FD77641",
  "last_progress_at": "2026-08-30T08:56:00+00:00",
  "hard_block": null,
  "tags": ["GEO6", "prior-art", "result-schema", "maintenance", "zero-math-drift"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-FIRSTWAVE-ACCEPTED-PRIOR-ART-SYNTHESIS",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6PAR3",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {"policy_set": "research_taskbook_policy.json", "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c", "review_state": "PASS", "temporary_overrides": []}
}
-->

# GEO6 first-wave prior-art Result schema repair V3

Status: `READY / MAINTENANCE / ZERO-MATH-DRIFT`

## Mother question
Can the completed first-wave prior-art synthesis be frozen as a writer-conformant Result without changing any mathematical or literature classification?

## Frozen inputs and scope
Freeze generation-2 result `RR-0C87FC289FDC9FD77641` as immutable historical evidence. Its return, checker, matrix, 19 claim rows, totals `3 EXACT_DUPLICATE / 10 STRICT_ANTECEDENT / 3 ADJACENT_METHOD / 3 NO_MATERIAL_MATCH`, rule `NO_MATERIAL_MATCH != NOVELTY_CERTIFICATE`, and selector residues `CONTACT_SELECTOR`, `LOCALITY_REFINEMENT_SELECTOR`, `ROTATION_CLOSURE_SELECTOR`, `TRANSLATION_ACTION_SELECTOR` are frozen. The diagnosed defect is only that `method_harvest` used noncanonical free text instead of one allowed enum.

## Hard target and required outputs
Hard target: `GEO6_FIRSTWAVE_PRIOR_ART_RESULT_V3_WRITER_CONFORMANT_WITH_ZERO_MATH_DRIFT`.

Freeze a NEW Result-ID with a fresh execution record and exact canonical typed fields: `terminal_verdict=SUCCESS`, `method_harvest=RESULT_ONLY`, `independence_status=NOT_APPLICABLE`, `source_exposure_status=NONBLIND_DISCLOSED`. The manifest must bind return, checker, exact claim-source matrix and fresh execution record with Git blob SHA-1 plus SHA-256.

## Research value to preserve
Preserve the completed source-backed prior-art boundary so it can become canonical review authority without repeating research or altering the selector map.

## Success, kill, and return criteria
Success is a writer-conformant zero-mathematical-drift Result whose checker/matrix classifications reproduce generation 2 exactly. Kill on any classification drift, selector drift, source-matrix drift or theorem strengthening. Do not open selector mathematics or any stronger successor from this maintenance lane.
