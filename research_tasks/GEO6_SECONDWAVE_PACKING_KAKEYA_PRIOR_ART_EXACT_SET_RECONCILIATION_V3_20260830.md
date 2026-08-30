<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS",
  "title": "GEO6 second-wave Packing/Kakeya prior-art exact-set reconciliation V3",
  "kind": "RESEARCH",
  "owner": "research/geo6-secondwave-packing-kakeya-prior-art-synthesis",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Reconcile the exact set of two independently frozen Results on superseded publication TP2-3B14908767F248123B62, RR-830A587B1588DFB21AB1 and RR-4DC6467AD05A1E3CA824, and freeze one writer-conformant current Result without selecting by timestamp or silently discarding either claim/source matrix.",
  "next_action": "Compare both historical Results claim-by-claim and source-by-source; preserve their shared four-selector no-successor boundary, explicitly resolve every classification or source difference, create one unified matrix plus source manifest and deterministic reconciliation checker, then freeze a fresh execution and NEW Result-ID with complete dual-digest output bindings.",
  "dependencies": ["TP2-4BE16D83EC2AA855C5B1", "RR-830A587B1588DFB21AB1", "RR-4DC6467AD05A1E3CA824", "RR-547A186EBDE5EE6CD8A3", "RR-EC0502A82AD5DC3995F4"],
  "source_refs": ["PR#937", "PR#950", "research/geo6-secondwave-packing-kakeya-prior-art-em-g6pa2-4a7d2c", "research/geo6-secondwave-packing-kakeya-prior-art-synthesis-em-g6pa2-7a84c2"],
  "evidence_status": "PARALLEL_RESULT_EXACT_SET_REQUIRED / BOTH_OLD_PUBLICATION_RESULTS_RETAINED / CURRENT_GEN2_SINGLE_RESULT_REPLAY_INSUFFICIENT",
  "last_progress_ref": "RR-4DC6467AD05A1E3CA824",
  "last_progress_at": "2026-08-30T11:25:34+00:00",
  "hard_block": null,
  "tags": ["GEO6", "Packing", "Kakeya", "prior-art", "exact-set", "parallel-result", "maintenance", "integration"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6PA2R3",
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

# GEO6 second-wave Packing/Kakeya prior-art exact-set reconciliation V3

Status: `READY / MAINTENANCE + INTEGRATION / EXACT-SET`

## Mother question

What is the single exact source-backed prior-art boundary for the accepted Packing/Kakeya second wave when the superseded generation-1 publication produced two independently frozen Results, and which four P000 semantic selectors survive after reconciling the complete Result set rather than choosing one branch by timestamp?

## Frozen inputs and scope

The exact historical Result set is `{RR-830A587B1588DFB21AB1, RR-4DC6467AD05A1E3CA824}` on superseded publication `TP2-3B14908767F248123B62`. Both are immutable evidence. Neither may be silently preferred, edited, or discarded. The current generation-2 repair `TP2-4BE16D83EC2AA855C5B1` is superseded by this task because it was authored before the second parallel Result became visible and therefore targets only one member of the exact set.

Freeze the shared semantic boundary unless exact source comparison disproves it: `NONOVERLAP_SELECTOR`, `TRANSLATION_FOLNER_SELECTOR`, `PHYSICAL_REFINEMENT_SELECTOR`, and `MIXED_DIRECTION_SELECTOR` remain unresolved; no currently accepted P000/Full-Cell datum has been identified as a resolver; `NO_MATERIAL_MATCH` is not a novelty certificate.

## Hard target and required outputs

Hard target: `GEO6_SECONDWAVE_PACKING_KAKEYA_PRIOR_ART_EXACT_SET_RECONCILED_AND_WRITER_CONFORMANT`.

Required outputs:

1. a two-Result exact-set comparison table covering every claim row, external source, formal hypothesis comparison, classification label and kill decision;
2. one unified claim/source matrix that records agreements and every genuine disagreement explicitly;
3. one source manifest identifying provenance from both historical branches;
4. one deterministic checker that verifies Result-set membership, reconciliation totals, selector set and no-successor guard;
5. a fresh execution record and NEW Result-ID using canonical typed Result enums;
6. a complete output manifest with Git blob SHA-1 plus SHA-256 for return, checker, unified matrix, source manifest and fresh execution record.

## Research value to preserve

The value is not another literature search. It is the exact-set synthesis needed to prevent concurrency from turning source history into an arbitrary winner. Preserve every supported antecedent and kill decision, while producing one operational prior-art boundary that the parent GEO6 objective can safely consume.

## Success, kill, and return criteria

Success requires explicit reconciliation of both historical Results and a writer-conformant new Result. If the two matrices differ only in granularity or source choice, preserve that distinction in the audit trail and freeze a justified unified classification. If a substantive classification conflict exists, return it as an exact unresolved discrepancy rather than forcing consensus.

Kill any execution that selects a Result by timestamp, ignores one historical branch, reopens classical finite Packing/Kakeya mathematics, infers novelty from search absence, changes the four shared selectors without exact evidence, or publishes native selector mathematics. This task is the final control-plane reconciliation before objective-level semantic-selector synthesis.
