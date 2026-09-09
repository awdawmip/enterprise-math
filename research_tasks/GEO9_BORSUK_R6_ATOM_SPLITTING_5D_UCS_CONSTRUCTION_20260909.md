<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO9-BORSUK-R6-ATOM-SPLITTING-5D-UCS-CONSTRUCTION",
  "title": "GEO9 Borsuk R6 atom-splitting and five-dimensional UCS construction",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "BLOCKED",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The frozen GEO8 evidence proves that unions of whole Lassak atoms cannot compress 33 to 32 and that the simplest center-fixed untruncated R6 hypercube-facet port fails. The first genuine escape is to split/redraw atoms or construct new truncation/UCS geometry in the five-dimensional projection, but this continuation may execute only after a current-generation GEO8 Result is Driver-accepted.",
  "next_action": "After the persistent line Driver binds a Driver-accepted current-generation Result for the stable GEO8 task and republishes this same Task-ID as READY, construct and certify a continuous R6 atom-splitting/truncation/UCS scheme aiming at <=32 pieces, or prove an exact obstruction for the explicitly enlarged template.",
  "dependencies": [{"task_id":"RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE","required_artifact":"Driver-accepted current-generation immutable Result"}],
  "source_refs": [
    "research_task_records/RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE/TP2-75A6C3F81E2D094B67CF.json",
    "research_result_records/RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE/RR-68BA014D54542DA7221C.json",
    "research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/r4_to_r6_transfer_audit_20260902.json",
    "research_artifacts/GEO8_BORSUK_R6_LASSAK_33_COMPRESSION_PRESSURE/lassak_r6_exact_obstruction_20260902.json",
    "research_notes/GEO8_BORSUK_R6_COMPLETE_RELEASE_AND_DRIVER_HANDOFF_20260909.md"
  ],
  "evidence_status": "BLOCKED_ON_CURRENT_GENERATION_GEO8_DRIVER_ACCEPTANCE / WHOLE_ATOM_ROUTE_ALREADY_EXACTLY_OBSTRUCTED / NEW_CONTINUOUS_GEOMETRY_REQUIRED",
  "last_progress_ref": "RR-68BA014D54542DA7221C",
  "last_progress_at": "2026-09-02T07:52:11+00:00",
  "hard_block": {
    "missing_object": "Driver-accepted current-generation Result for RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE",
    "owner": "GV-GEO8-BORSUK-R6-PERSISTENT-LINE-DRIVER",
    "necessity": "The successor must consume a current operationally reviewable GEO8 boundary rather than the superseded Gen1 publication.",
    "unblock_condition": "The persistent line Driver binds a current-generation ACCEPTED review and republishes this same Task-ID in a READY superseding generation without weakening the mathematical gate."
  },
  "tags": ["GEO9","Borsuk","R6","atom-splitting","truncation","UCS","continuous-geometry","5D-projection"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO9-BORSUK-R6-ATOM-SPLITTING-5D-UCS-CONSTRUCTION",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-BORSUK-R6-UPPER-BOUND-PRESSURE-20260902",
  "parent_objective_generation_id": "OG-1302C0D2A19AF22098E8",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GEO9BORSUKR6",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "CONTINUATION",
  "parent_task_id": "RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE",
  "successor_gate": {
    "new_information_gap": "GEO8 blocks every coarsening by unions of the original 33 atoms and one naive center-fixed cone port, but it leaves genuine atom splitting, truncation, movable/multiple apices, non-hypercubic directions, multiple UCS representatives, and five-dimensional normal/orbit geometry unclassified.",
    "why_parent_result_does_not_close_it": "The parent boundary is a restricted-template obstruction, not a global lower bound and not a classification of enlarged R6 truncation/UCS templates.",
    "discriminating_outcomes": ["B6_CONSTRUCTIVE_UPPER_BOUND_AT_MOST_32_WITH_UNIVERSAL_CONTINUOUS_CERTIFICATE","ENLARGED_ATOM_SPLITTING_5D_UCS_TEMPLATE_CANNOT_BEAT_33","EXACT_MINIMAL_R6_GEOMETRIC_LEMMA_FOR_LE32_ISOLATED"],
    "kill_condition": "Stop any claimed universal improvement without global coverage and strict-diameter proof for every part; stop any replay of whole-atom merging already killed by K33; finite samples, Monte Carlo, local floating-point optima, or graph coloring alone are not a universal Euclidean theorem.",
    "alternative_route_or_free_exploration_considered": "Closing the R6 upper-bound Objective, direct attack on b(6)=7, and unrelated free exploration were considered. This task is preserved because GEO8 identifies a precise surviving structural escape adjacent to the best retained constructive bound, but it remains blocked until the current-generation parent boundary is accepted.",
    "why_new_stage_or_task_is_better_than_same_task_or_closure": "The new task changes the admissible construction class from whole-atom coarsening to atom splitting/truncation/UCS geometry and therefore has distinct continuous hypotheses, certificates, and failure modes."
  },
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b","review_state":"PASS","temporary_overrides":[]}
}
-->

# GEO9 Borsuk R6 atom-splitting and five-dimensional UCS construction

## Mother question

Can a genuinely enlarged six-dimensional Lassak-derived construction—one allowed to split/redraw old atoms and use new five-dimensional truncation/UCS geometry—produce a rigorous universal partition into at most 32 strictly smaller-diameter pieces, or can that enlarged construction class itself be exactly obstructed?

## Frozen inputs and scope

This task is `BLOCKED`. It must not execute until the persistent line Driver binds a Driver-accepted current-generation Result for the stable GEO8 task.

Consume rather than replay the frozen negative information: whole-atom coarsening has incompatibility graph `K_33`; cap-sector distance squared is `1`; sector-sector strict-interior distance squared is at least `15/13`; and the center-fixed untruncated 12 hypercube-facet cone port has a uniform `10/7` witness.

Allowed new freedoms are atom splitting/repartition, wall redrawing, lens truncation, movable or multiple apices, non-hypercubic directions, multiple UCS representatives, and new five-dimensional normal/orbit systems. This is external Euclidean `R^6`; no P000-native metric is inferred.

## Hard target and required outputs

Hard target: `BORSUK_R6_ATOM_SPLITTING_5D_UCS_LE32_CERTIFICATE_OR_ENLARGED_TEMPLATE_OBSTRUCTION`.

Return one exact outcome: a universal `b(6)<=32` or stronger continuous certificate; an exact `<=32` obstruction for a clearly enlarged atom-splitting/5D-UCS template; or the exact minimum missing R6 geometric lemma.

A positive theorem must cover every bounded unit-diameter subset of `R^6` after normalization and prove every piece has strict diameter `<1`. An obstruction must quantify over the full frozen enlarged parameter family. Required artifacts are the exact construction/template, theorem dependency graph, source manifest, global coverage/diameter proof, exact finite or symbolic checks, adversarial equality/boundary audit, BRC applicability statement, fresh execution record, and immutable Result.

## Research value to preserve

K33 has already killed the obvious compression route. The remaining value lies in changing the geometry. A universal 32-part construction improves the retained bound; a rigorous enlarged-template no-go identifies the next genuinely missing ingredient instead of merely reporting an unsuccessful search.

## Success, kill, and return criteria

Success requires one exact terminal outcome with complete continuous proof obligations. BRC is first-line only on an exact discrete branch/recoalescence carrier such as provenance-labeled split atoms or finite UCS choices; state its population, observer, provenance and future-operation horizon. BRC alone is not a proof of continuous Euclidean coverage or strict diameter without an exact bridge.

Kill finite-sample, point-cloud, Monte Carlo, local floating-point, or graph-coloring substitutes for a universal theorem; replay of the already killed whole-atom route; loss of split-piece provenance needed by coverage; or upgrade of a template obstruction to `b(6)>=33`. Do not publish a successor from the Researcher lane.
