<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION",
  "title": "P000 six-axis Johnson–Plücker Result schema repair V3",
  "kind": "RESEARCH",
  "owner": "research/p000-six-axis-johnson-plucker-decomposition",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "Generation 2 completed the missing Pfaffian/Hodge mathematics and preserved the Johnson/index-24 structure, but its frozen Result RR-99F9C977CDB5EF762F42 uses a noncanonical method_harvest value and therefore cannot satisfy the current immutable Result registry audit.",
  "next_action": "A fresh one-shot researcher must preserve the generation-2 mathematical content with zero mathematical drift, replay the exact checker/regression evidence, and freeze a NEW Result-ID through the current canonical Result writer using only valid typed Result enums and a complete dual-digest output manifest.",
  "dependencies": [
    "TP2-FDC95F823029B5829F3B",
    "RR-99F9C977CDB5EF762F42",
    "driver-review-comment-5467874656"
  ],
  "source_refs": [
    "research/p000-six-axis-johnson-plucker-revision-v2-em-p000jp2-d2c2ae@bc78abf5f4d2d4e2e698ed19e0f6e873456861f2",
    "research_returns/P000_SIX_AXIS_JOHNSON_PLUCKER_DECOMPOSITION_REVISION_V2_RETURN_20260830.md@sha1:23436a14dc08491c84fa35bfcf9c8d6dd140cc38",
    "research_result_records/RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION/RR-99F9C977CDB5EF762F42.json@sha1:38d4e955842f438b4a79d51fce4e95ed8f21f12a"
  ],
  "evidence_status": "GEN2_MATHEMATICS_DRIVER_RECHECKED / RESULT_TYPED_ENUM_REPAIR_REQUIRED / ZERO_MATH_DRIFT",
  "hard_block": null,
  "tags": ["P000","Johnson","Plucker","Pfaffian","Hodge","result-schema","revision"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION",
  "parent_objective_id": "OBJ-P000-SIX-AXIS-REPRESENTATION-ARITHMETIC",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "P000JP3",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-P000-SIX-AXIS-JOHNSON-PLUCKER-DECOMPOSITION",
  "successor_gate": {
    "new_information_gap": "The generation-2 mathematical obligations are complete, but the immutable Result record stores method_harvest outside the current canonical enum, so the result chain is not operationally valid.",
    "why_parent_result_does_not_close_it": "RR-99F9C977CDB5EF762F42 is immutable and must not be edited; terminal Driver acceptance requires a writer-conformant NEW Result record bound to a fresh execution.",
    "discriminating_outcomes": [
      "zero-drift replay succeeds and a writer-conformant Result is frozen",
      "replay detects mathematical or artifact drift and forces a substantive narrower return",
      "current writer rules expose another exact evidence-chain defect that blocks acceptance"
    ],
    "kill_condition": "No theorem strengthening or weakening merely to repair metadata; do not change P000 typing, the characteristic-aware Pfaffian/Hodge boundary, Q_orb, the index-24 splitting, or any prior immutable Result bytes.",
    "alternative_route_or_free_exploration_considered": "Closing would discard a mathematically complete revision; unrelated exploration would evade a pure result-integrity defect. A fresh writer-conformant re-freeze is the smallest safe action.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The prior execution identity is one-shot and its Result is immutable, so a new publication generation is required for a fresh execution to create a valid Result envelope without rewriting history."
  },
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# P000 six-axis Johnson–Plücker Result schema repair V3

## Mother question

Can the mathematically completed generation-2 Johnson–Plücker revision be re-frozen with zero mathematical drift as a Result that is fully valid under the current canonical typed Result registry?

## Frozen inputs and scope

Freeze generation-2 publication `TP2-FDC95F823029B5829F3B`, branch head `bc78abf5f4d2d4e2e698ed19e0f6e873456861f2`, Result `RR-99F9C977CDB5EF762F42`, its return/checker/regression artifact, and Driver review comment `5467874656` as immutable input. Preserve the exact generation-2 mathematical boundary: integral and half polarization conventions, rank `6`, real signature `(3,3)`, coefficient-ring and characteristic-2 behavior, Hodge sectors/orientation law, Johnson `1+3+2`, `Q_orb`, index-24 splitting and `rho`. Preserve all P000/native-dimension/Full-Cell firewalls.

## Hard target and required outputs

Hard target:

`P000_JOHNSON_PLUCKER_REVISION_V3_WRITER_CONFORMANT_RESULT_WITH_ZERO_MATH_DRIFT`.

Required outputs:

1. replay or independently recheck the exact generation-2 checker and regression table;
2. preserve the generation-2 theorem statements unless exact replay finds a real contradiction;
3. use a fresh execution identity and freeze a NEW Result-ID through the current canonical Result writer;
4. use only canonical typed Result enums, including `terminal_verdict=SUCCESS` when the zero-drift replay passes and a valid `method_harvest` value chosen honestly from the current enum;
5. use valid current `independence_status` and `source_exposure_status` values;
6. pin the return, checker, every certificate/artifact and the fresh execution record with Git blob SHA-1 plus SHA-256;
7. make no downstream mathematical successor claim from the researcher lane.

## Research value to preserve

The generation-2 mathematics closes the original Pfaffian/Hodge gap and preserves the exact rational-versus-integral Johnson structure. This task prevents a metadata typing error from either discarding that result or being silently normalized into authority without a writer-conformant immutable chain.

## Success, kill, and return criteria

Success requires a NEW writer-conformant Result whose mathematical delta from generation 2 is `NONE`, whose exact checker/regression replay passes, and whose complete manifest validates under current Result rules. If replay finds substantive drift, return the exact smallest discrepancy instead of forcing zero drift. Kill any attempt to mutate earlier Results, weaken the P000 firewall, identify the four-label exterior facade with native dimensionality, or invent a downstream theorem merely to justify another stage. Return the NEW Result for Driver review.