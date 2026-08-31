<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
  "title": "GEO6 objective semantic-selector synthesis current-head revalidation V2",
  "kind": "RESEARCH",
  "owner": "research/geo6-objective-semantic-selector-synthesis",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "Revalidate the completed Generation-1 twelve-selector synthesis against the current canonical control plane after duplicate Gen17 review reconciliation, preserving selector mathematics unless newly canonical ACCEPTED P000/Full-Cell evidence forces an explicit status change.",
  "next_action": "Use RR-35C4FE925E9C12E53604 as frozen source evidence; replace superseded resolver review IDs by current canonical review authority, scan all canonical ACCEPTED P000/Full-Cell review+Result pairs added or changed after snapshot 228446b2d797372b2d18503116f612ba03701184 through the fresh execution base, refresh the resolver manifest/snapshot, and emit a new writer-conformant Result without publishing successors.",
  "dependencies": [
    "RR-35C4FE925E9C12E53604",
    "DR-61B4E8C29A705FD31746",
    "TP2-D6A41E9C3B705F821847",
    "RR-547A186EBDE5EE6CD8A3",
    "RR-B5DB25EC13BF1C42DC9B",
    "RR-EC0502A82AD5DC3995F4"
  ],
  "source_refs": [
    "research_returns/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS_RETURN_20260831.md",
    "research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/selector_atlas.json",
    "research_artifacts/GEO6_OBJECTIVE_SEMANTIC_SELECTOR_SYNTHESIS/accepted_resolver_manifest.json",
    "driver_reviews/GEO6_OBJECTIVE_SELECTOR_SYNTHESIS_GEN1_CURRENT_HEAD_AUDIT_20260831.md",
    "research_result_reviews/RR-985AEE277DE45AFCC9D8/DR-61B4E8C29A705FD31746.json",
    "research_task_records/RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE/TP2-D6A41E9C3B705F821847.json"
  ],
  "evidence_status": "GEN1_MATH_COMPLETE / CURRENT_AUTHORITY_MANIFEST_STALE / CURRENT_HEAD_REVALIDATION_REQUIRED",
  "last_progress_ref": "RR-35C4FE925E9C12E53604",
  "last_progress_at": "2026-08-31T02:47:19+00:00",
  "hard_block": null,
  "tags": ["GEO6", "objective-integration", "semantic-selector", "maintenance", "current-head", "resolver-authority", "zero-math-drift"],
  "claim_lease_minutes": 240,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
  "parent_objective_id": "OBJ-EXTERNAL-GEOMETRY-STRUCTURAL-TRANSFER-20260830",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "G6OBJSYN2",
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

# GEO6 objective semantic-selector synthesis current-head revalidation V2

Status: `READY / P0 / MAINTENANCE + CURRENT-HEAD REVALIDATION`

## Mother question

Does the completed Generation-1 selector synthesis remain exactly valid under the **current canonical control plane**, after duplicate Gen17 review reconciliation and subsequent P000/Full-Cell progress, and what is the current exact accepted-resolver authority for every selector?

This task is not permission to redo the geometry program and is not permission to publish successor mathematics. It repairs the current-authority layer of a completed objective-integration Result.

## Frozen source mathematics

Source Result: `RR-35C4FE925E9C12E53604`.

Preserve the following unless current canonical ACCEPTED evidence forces a documented change:

- twelve original selector identities;
- all 66 unordered selector-pair relations;
- no proven `SAME_SELECTOR` pairs;
- prerequisite DAG structure and six-root compression;
- Generation-1 baseline status counts `0 RESOLVED / 3 PARTIALLY_CONSTRAINED / 9 UNRESOLVED / 0 DUPLICATE`;
- recommendation cap of at most three successor candidates;
- no mechanical twelve-selector fan-out;
- no Working Truth, Foundation, canonical, or novelty promotion.

If any pair relation, DAG edge, selector status, or recommendation must change, the return must identify the exact newly canonical ACCEPTED datum and give the type/hypothesis map that forces the change. Silent drift is forbidden.

## Mandatory canonical-authority repair

Generation 1 cites superseded duplicate review:

`RR-985AEE277DE45AFCC9D8 / DR-6D2A91F4C8E3057B1246`.

Current canonical authority is:

`RR-985AEE277DE45AFCC9D8 / DR-61B4E8C29A705FD31746 / ACCEPTED`.

The Gen2 resolver manifest must use the current canonical review and must verify that every other cited resolver review remains present and `ACCEPTED` at the declared execution snapshot.

## Current P000-L1 no-duplicate boundary

Current active owner for immediate rotation/mixed native-lift continuation is:

`RS-P000-L1-NATIVE-CARRIER-CONTACT-BRIDGE / TP2-D6A41E9C3B705F821847 / generation 18 / P0 / ACTIVE`.

Open research PR #1013 / `RR-7FED4A83F3922D37319D` is **context only** unless, by the Gen2 execution snapshot, it has received an immutable canonical Driver review with `disposition=ACCEPTED`. An open PR or raw Result cannot alter selector status.

The Gen2 return must identify the current operational publication head for this lineage and preserve the no-duplicate gate if it remains active.

## Current-head delta scan

Starting after frozen snapshot:

`228446b2d797372b2d18503116f612ba03701184`

scan through the fresh execution base for every newly added, removed, superseded, reconciled, or replaced canonical `ACCEPTED` P000/Full-Cell review+Result pair that could touch any of the twelve selector contracts.

For each delta candidate record:

1. Result-ID;
2. current canonical Review-ID;
3. review disposition;
4. selector(s) potentially affected;
5. exact type/hypothesis map;
6. disposition: `FULL_RESOLVER / PARTIAL_CONSTRAINT / TYPE_MAP_REJECTED / CONTEXT_ONLY`.

Deleted duplicate review IDs must not remain in the final resolver manifest.

## Hard target and required outputs

Hard target:

`GEO6_OBJECTIVE_SELECTOR_SYNTHESIS_CURRENT_HEAD_REVALIDATED_WITH_CANONICAL_RESOLVER_AUTHORITY_AND_ZERO_UNEXPLAINED_MATH_DRIFT`

Required outputs:

1. a revalidation return that compares Gen1 snapshot to the fresh execution snapshot;
2. a current `accepted_resolver_manifest_v2.json` containing only current canonical review authority;
3. a `selector_atlas_v2.json` preserving or explicitly revising every selector status, pair relation, DAG edge and recommendation;
4. a current-head delta manifest covering all relevant accepted-review changes since the Gen1 snapshot;
5. a deterministic checker verifying:
   - all twelve selectors;
   - 66 unordered pairs;
   - current review-ID existence/disposition;
   - absence of superseded `DR-6D2A91F4C8E3057B1246` from current authority;
   - canonical `DR-61B4E8C29A705FD31746` binding to `RR-985AEE277DE45AFCC9D8`;
   - current P000-L1 publication head/no-duplicate gate;
   - exact before/after status counts and any justified drift;
   - recommendation count `<=3`;
6. a fresh execution record;
7. a NEW Result-ID with complete dual-digest bindings for return, checker, atlas v2, resolver manifest v2, delta manifest and execution record.

## Success conditions

Success is either:

### A. Zero semantic drift

Current canonical evidence changes only authority IDs/control-head routing, and the Gen1 mathematics remains:

`0 RESOLVED / 3 PARTIAL / 9 UNRESOLVED / 0 DUPLICATE`, six roots, same three bounded recommendations.

or:

### B. Explicit accepted-evidence drift

One or more statuses/relations/recommendations change because a newly canonical `ACCEPTED` datum satisfies an exact selector obligation. Every change must be source-bound and type-mapped.

Both are valid outcomes.

## Kill rules

Kill the execution if it:

- reuses a removed/superseded review ID as current authority;
- counts open PR #1013 or any raw/unreviewed Result as accepted resolver evidence;
- chooses a current task head by timestamp rather than publication supersession/current record state;
- redoes classical prior-art searches already closed by the three GEO6 prior-art reviews;
- changes selector math without a newly canonical accepted datum and exact type map;
- publishes successor tasks from the Researcher lane;
- treats unresolved/no-match status as novelty.

## Driver handoff

Return one current-head, writer-conformant Gen2 Result. If Driver accepts it, the Driver may then decide whether to publish the same bounded successor set, a smaller changed set, revise the parent Objective, or close it. Until that review, no GEO6 selector successor mathematics is authorized.