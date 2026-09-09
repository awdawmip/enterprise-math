<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GV-GEO9-BORSUK-R6-UPPER-BOUND-FINAL-INTEGRATION",
  "title": "GEO9 Borsuk R6 upper-bound final integration and Objective disposition",
  "kind": "GOVERNANCE",
  "owner": "governance",
  "base_state": "BLOCKED",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "The R6 upper-bound Objective can be closed, parked, or continued only after the current-generation GEO8 boundary is Driver-accepted, the enlarged atom-splitting/5D-UCS task has a Driver-accepted exact Result, and the continuous certificate has an accepted independent audit.",
  "next_action": "After all declared evidence gates are satisfied, integrate only compatible accepted claims, update the retained b(6) interval if and only if a universal theorem changes it, and issue one explicit Objective disposition: CLOSED, PARKED/NO_EXECUTABLE_ROUTE, or OPEN_WITH_EXPLICIT_NEW_INFORMATION_GAP_AND_JUSTIFIED_TASKSET.",
  "dependencies": [
    {"task_id":"RS-GEO8-BORSUK-R6-LASSAK-33-COMPRESSION-PRESSURE","required_artifact":"Driver-accepted current-generation Result"},
    {"task_id":"RS-GEO9-BORSUK-R6-ATOM-SPLITTING-5D-UCS-CONSTRUCTION","required_artifact":"Driver-accepted immutable Result"},
    {"task_id":"RS-GEO9-BORSUK-R6-CONTINUOUS-CERTIFICATE-INDEPENDENT-AUDIT","required_artifact":"Driver-accepted independent audit Result"}
  ],
  "source_refs": ["research_notes/GEO8_BORSUK_R6_COMPLETE_RELEASE_AND_DRIVER_HANDOFF_20260909.md"],
  "evidence_status": "BLOCKED_ON_CURRENT_GEO8_ACCEPTANCE_PLUS_ACCEPTED_GEO9_CONTINUATION_PLUS_ACCEPTED_INDEPENDENT_AUDIT / FINAL_PORTFOLIO_DISPOSITION_ONLY",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": {
    "missing_object": "Accepted current-generation GEO8 Result, accepted GEO9 atom-splitting/5D-UCS Result, and accepted independent continuous-certificate audit",
    "owner": "GV-GEO8-BORSUK-R6-PERSISTENT-LINE-DRIVER",
    "necessity": "Final Objective disposition must synthesize accepted current authority, not task specifications, raw Results, or finite candidate evidence.",
    "unblock_condition": "The persistent line Driver binds all three accepted evidence objects and republishes this same Task-ID READY for final integration."
  },
  "tags": ["GEO9","Borsuk","R6","final-integration","governance","objective-disposition"],
  "claim_lease_minutes": 360,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "GV-GEO9-BORSUK-R6-UPPER-BOUND-FINAL-INTEGRATION",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-BORSUK-R6-UPPER-BOUND-PRESSURE-20260902",
  "parent_objective_generation_id": "OG-1302C0D2A19AF22098E8",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "GEO9B6INT",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "INTEGRATION",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b","review_state":"PASS","temporary_overrides":[]}
}
-->

# GEO9 Borsuk R6 upper-bound final integration and Objective disposition

## Mother question

Given the final accepted evidence from the current GEO8 boundary, the enlarged GEO9 construction/obstruction, and an independent continuous-certificate audit, what is the strongest compatible six-dimensional Borsuk upper-bound statement the project may retain, and should the R6 upper-bound Objective close, park, or continue?

## Frozen inputs and scope

This GOVERNANCE task is `BLOCKED`. It may become READY only after all three declared evidence gates are satisfied.

Consume only Driver-accepted exact Results/reviews. Do not integrate raw taskbooks, unreviewed Results, finite candidate searches, or a historical superseded publication as if they were current mathematical authority. Preserve the distinction between Euclidean theorem, finite certificate, project-local template obstruction, and any P000 comparison. Change the retained interval only by a theorem whose hypotheses cover the universal Euclidean `R^6` Borsuk problem.

## Hard target and required outputs

Hard target: `BORSUK_R6_UPPER_BOUND_LINE_FINAL_INTEGRATION_AND_OBJECTIVE_DISPOSITION_COMPLETE`.

Bind the accepted current-generation GEO8 Result/review, accepted GEO9 atom-splitting/5D-UCS Result/review, and accepted independent audit Result/review. Build a compatibility matrix of claims, hypotheses, sources and exclusions. Update the retained `b(6)` interval only if a universal continuous theorem justifies it. If only template obstructions survive, retain `7<=b(6)<=33` unless another accepted source changes it. Issue one Objective generation with exactly one disposition: `CLOSED`, `PARKED/NO_EXECUTABLE_ROUTE`, or `OPEN_WITH_EXPLICIT_NEW_INFORMATION_GAP`. If OPEN, publish only the minimal genuinely justified taskset. Update the persistent line dossier.

## Research value to preserve

Final integration prevents individually useful negative results from being mistaken for a solution, and prevents a genuine universal improvement from being diluted by task-local wording. It is the single point where the project decides what changed in the actual six-dimensional Borsuk frontier and whether more work remains justified.

## Success, kill, and return criteria

Success requires a source-complete portfolio disposition and updated dossier. `CLOSED` is allowed only when the Objective's real closure criteria are met; `PARKED` when no executable evidence-based route remains but the mathematics is open; `OPEN` requires an explicit new information gap and bounded justified taskset.

Kill integration that upgrades K33 or another restricted-template obstruction to `b(6)>=33`, changes the upper bound from computation alone, skips the independent audit gate, publishes stages solely because prior stages passed, or discards provenance/equality caveats. Publication of this task does not authorize Objective closure before the hard block is cleared.
