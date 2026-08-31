<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-PHYSICAL-REFINEMENT-SUPPORT-TRANSPORT-CORE",
  "title": "GEO6 Physical Refinement and Support Transport Core",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Derive or refute a typed physical P000 scale-refinement map from native locality/refinement and classify support transport across that map, without substituting abstract Q17 refinement or finite graph covering.",
  "next_action": "Define the weakest physical Cell-refinement morphism compatible with current native locality, then test existence/functoriality and whether Cell×Support incidence transports coherently; use exact countermodels before escalating structure.",
  "dependencies": ["RR-35C4FE925E9C12E53604"],
  "source_refs": ["research_returns/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS_RETURN_20260831.md","research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/selector_atlas.json","research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/accepted_resolver_manifest.json"],
  "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
  "last_progress_ref": "RR-35C4FE925E9C12E53604",
  "last_progress_at": "2026-08-31T02:47:19+00:00",
  "hard_block": null,
  "tags": ["GEO6","DRIVER_AUTO_FOLLOWUP","MATHEMATICAL_CONTINUATION","GEO6_REFINEMENT_CORE"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-PHYSICAL-REFINEMENT-SUPPORT-TRANSPORT-CORE",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GEO6_REFINEMENT_CORE",
  "origin_kind": "DRIVER_ROADMAP",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
  "successor_gate": {
    "new_information_gap": "The atlas proves LOCALITY_REFINEMENT -> PHYSICAL_REFINEMENT and PHYSICAL_REFINEMENT/SUPPORT_RELATION -> REFINEMENT_TRANSPORT dependencies but no typed physical refinement map exists in accepted evidence.",
    "why_parent_result_does_not_close_it": "Without the refinement morphism, four downstream selector contracts cannot be evaluated rather than merely labeled unresolved.",
    "discriminating_outcomes": ["PHYSICAL_REFINEMENT_AND_SUPPORT_TRANSPORT_PROVED","PHYSICAL_REFINEMENT_OBSTRUCTED_WITH_MINIMAL_EXTRA_DATUM","SUPPORT_TRANSPORT_OBSTRUCTED_AFTER_REFINEMENT"],
    "kill_condition": "If the only candidate is abstract effectivity refinement, graph covering, or external Euclidean scaling without native semantics, freeze the obstruction and stop.",
    "alternative_route_or_free_exploration_considered": "Separate locality/refinement and support-transport tasks would duplicate the same morphism typing. The atlas's prerequisite DAG shows one shared core is the minimal route.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The integration atlas is complete; this successor isolates its load-bearing refinement prerequisite as a theorem/countermodel problem."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:10ec4f937324069d7af8d77a52c244389ac4cccd957e3685c14c6fe8b8fd367c","review_state":"PASS","temporary_overrides":[]},
  "parent_objective_generation_id": "OG-BB398D541DDECF58D19E"
}
-->

# GEO6 Physical Refinement and Support Transport Core

Status: `READY / P0 / GEO6 DRIVER FOLLOW-UP`

## Mother question

Does the current native Cell language determine any genuine physical scale-refinement map, and if so what support data transports canonically across it?

## Frozen inputs and scope

Freeze `RR-35C4FE925E9C12E53604`: Q17 abstract refinement is not physical Cell refinement, finite graph cover is not physical scale refinement, and Full-Cell frame transport is not Mahler support transport. Preserve current P000 typing and do not import classical Euclidean scaling, convex polarity, or volume without an explicit map.

## Hard target and required outputs

Hard target: `GEO6_PHYSICAL_REFINEMENT_SUPPORT_TRANSPORT_CORE_EXACTLY_CLASSIFIED`.

Required outputs: (1) typed source/target Cell systems and refinement morphism candidates; (2) existence/nonexistence and composition laws; (3) induced or obstructed support-relation transport; (4) exact selector dispositions for LOCALITY_REFINEMENT_SELECTOR, PHYSICAL_REFINEMENT_SELECTOR, REFINEMENT_TRANSPORT_SELECTOR and the refinement prerequisite of MIXED_DIRECTION_SELECTOR; (5) countermodels for any unforced identification; (6) deterministic checker for finite components only.

## Research value to preserve

Preserve the distinction between combinatorial refinement and physical scale. A useful result may be a no-go that isolates the exact extra datum needed for transport.

## Success, kill, and return criteria

Success requires a typed refinement/transport theorem or exact obstruction with the smallest missing datum. Kill any route that calls Q17 refinement, graph subdivision/cover, or coordinate rescaling 'physical refinement' by naming alone. Do not infer Mahler polarity/volume semantics. Return one durable Result.
