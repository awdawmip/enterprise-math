<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-NATIVE-RELATION-SELECTOR-CORE",
  "title": "GEO6 Native Relation Selector Core",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Determine the minimum typed native relation primitives that distinguish contact/readout, non-overlap/exclusion, and Cell×Support incidence without importing carrier identity or complete adjacency.",
  "next_action": "Freeze explicit native type signatures for contact/readout, exclusion/non-overlap and Cell×Support incidence; test exact conversions and countermodels first, then classify which of CONTACT_SELECTOR, NONOVERLAP_SELECTOR and SUPPORT_RELATION_SELECTOR can be resolved or must remain independent.",
  "dependencies": ["RR-35C4FE925E9C12E53604"],
  "source_refs": ["research_returns/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS_RETURN_20260831.md","research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/selector_atlas.json","research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/accepted_resolver_manifest.json"],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": "RR-35C4FE925E9C12E53604",
  "last_progress_at": "2026-08-31T02:47:19+00:00",
  "hard_block": null,
  "tags": ["GEO6","DRIVER_AUTO_FOLLOWUP","MATHEMATICAL_CONTINUATION","GEO6_RELATION_CORE"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-NATIVE-RELATION-SELECTOR-CORE",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GEO6_RELATION_CORE",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
  "successor_gate": {
    "new_information_gap": "The objective audit leaves CONTACT, NONOVERLAP and SUPPORT_RELATION as distinct roots/overlaps without a common typed relation core.",
    "why_parent_result_does_not_close_it": "The audit classifies their relationship but does not supply the native conversion theorems or separating countermodels required to resolve the selectors.",
    "discriminating_outcomes": ["NATIVE_RELATION_CONVERSIONS_PROVED_WITH_EXACT_SCOPE","NATIVE_RELATION_SELECTORS_PROVED_INDEPENDENT","MIXED_RELATION_CORE_PARTIAL_WITH_SMALLEST_GAP"],
    "kill_condition": "If the proposed shared primitive merely re-encodes complete adjacency or assumes the target relation by definition, reject it and freeze the countermodel.",
    "alternative_route_or_free_exploration_considered": "Three independent selector tasks were considered; the accepted atlas shows overlap and shared typing obligations, so a common root task is lower-duplication and more discriminating.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The parent integration task is terminal as an atlas. This successor changes from classification of evidence to proving the missing native relation semantics."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]},
  "parent_objective_generation_id": "OG-BB398D541DDECF58D19E"
}
-->

# GEO6 Native Relation Selector Core

Status: `READY / P0 / GEO6 DRIVER FOLLOW-UP`

## Mother question

What is the weakest native relation language in which contact/readout, non-overlap/exclusion, and Cell×Support incidence can be compared without silently identifying them?

## Frozen inputs and scope

Freeze the accepted GEO6 selector atlas `RR-35C4FE925E9C12E53604`, including the exact partial CONTACT constraint and the kill list. Carrier S4, PF-10 channel labels, classical packing contact, and untyped Full-Cell readouts are comparison evidence only unless an explicit native type map is proved. Do not reopen the active P000-L1 rotation/native-lift frontier.

## Hard target and required outputs

Hard target: `GEO6_NATIVE_RELATION_SELECTOR_CORE_EXACTLY_CLASSIFIED`.

Required outputs: (1) native sort/signature definitions for the three relation families; (2) proofs of any valid implication/equivalence and explicit typed countermodels for invalid conversions; (3) an exact disposition for CONTACT_SELECTOR, NONOVERLAP_SELECTOR, and SUPPORT_RELATION_SELECTOR; (4) a prerequisite update for SELF_DUAL_IDENTIFICATION_SELECTOR, COMPLEXITY_FUNCTIONAL_SELECTOR, and REFINEMENT_TRANSPORT_SELECTOR; (5) deterministic finite certificates only where the finite domain is explicitly complete; (6) no novelty inference.

## Research value to preserve

Preserve the GEO6 insight that similar-looking geometric notions may live on different native sorts. The point is minimum typed information, not relabeling classical contact or exclusion as native structure.

## Success, kill, and return criteria

Success requires a typed theorem/countermodel package that resolves at least one declared implication boundary and freezes the smallest remaining information gap. Kill any route that uses complete adjacency, named Euclidean axes, classical packing constants, or an untyped identification of readout/contact with exclusion/support. Return a durable Result and do not self-publish a successor.
