<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS",
  "title": "GEO6 second-wave Packing/Kakeya prior-art Result envelope repair V2",
  "kind": "RESEARCH",
  "owner": "research/geo6-secondwave-packing-kakeya-prior-art-synthesis",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Re-freeze the completed 18-claim Packing/Kakeya prior-art synthesis with a complete Result manifest, preserving exactly the 3/11/1/3 classifications and four surviving selectors while adding the omitted claim-source matrix and fresh execution record to the dual-digest chain.",
  "next_action": "Replay PR #937 / RR-830A587B1588DFB21AB1 without literature or mathematical drift, create a fresh execution record and NEW Result-ID, and bind return + checker + exact claim-source matrix + execution record with Git blob SHA-1 and SHA-256 using current canonical typed Result enums.",
  "dependencies": ["TP2-3B14908767F248123B62", "RR-830A587B1588DFB21AB1"],
  "source_refs": ["research/geo6-secondwave-packing-kakeya-prior-art-em-g6pa2-4a7d2c@d39910150303bd943c5b5055264da2c1184a223b"],
  "evidence_status": "MATHEMATICAL_PAYLOAD_RETAINED / RESULT_MANIFEST_INCOMPLETE / MATRIX_AND_EXECUTION_OMITTED",
  "last_progress_ref": "RR-830A587B1588DFB21AB1",
  "last_progress_at": "2026-08-30T09:05:51+00:00",
  "hard_block": null,
  "tags": ["GEO6", "Packing", "Kakeya", "prior-art", "result-integrity", "maintenance"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6PA2R2",
  "origin_kind": "MAINTENANCE",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {"policy_set": "research_taskbook_policy.json", "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c", "review_state": "PASS", "temporary_overrides": []}
}
-->

# GEO6 second-wave Packing/Kakeya prior-art Result envelope repair V2

Status: `READY / MAINTENANCE / ZERO-MATH-DRIFT`

## Mother question
Can the completed Packing/Kakeya prior-art synthesis be frozen with the complete immutable output chain required by the current Result contract?

## Frozen inputs and scope
Freeze `RR-830A587B1588DFB21AB1` and PR #937 as immutable source evidence. Preserve exactly 18 classifications: `3 EXACT_DUPLICATE / 11 STRICT_ANTECEDENT / 1 ADJACENT_METHOD / 3 NO_MATERIAL_MATCH`, the rule that no-match is not novelty, and the surviving selectors `NONOVERLAP_SELECTOR`, `TRANSLATION_FOLNER_SELECTOR`, `PHYSICAL_REFINEMENT_SELECTOR`, `MIXED_DIRECTION_SELECTOR`. No currently accepted P000/Full-Cell resolver was identified and that conclusion must not drift.

## Hard target and required outputs
Hard target: `GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_RESULT_REFROZEN_WITH_COMPLETE_DIGEST_CHAIN_AND_ZERO_MATH_DRIFT`.

Freeze a NEW Result-ID with a fresh execution record and canonical typed fields. The output manifest must contain the revision return, deterministic checker, exact claim-source matrix and fresh execution record, with Git blob SHA-1 plus SHA-256 on every row.

## Research value to preserve
Preserve the completed antecedent classification and selector isolation so the geometry objective can synthesize only genuinely unresolved native semantics after all audit envelopes are valid.

## Success, kill, and return criteria
Success requires exact replay of all 18 rows, counts and selector residues with a complete dual-digest chain. Kill on any claim reclassification, selector change, unsupported novelty inference or mathematical strengthening. Do not publish a native selector successor from this maintenance lane.
