<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "GOV-T6-SHAPE-MOMENT-PERSISTENT-LINE-DRIVER",
  "title": "Persistent Line Driver: T6 Shape-Moment Exact Threshold",
  "kind": "GOVERNANCE",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "The T6 shape-moment line has a claimable mathematical continuation prepared around the exact frontier T6<=2332: p>=29 eliminated, p=23 globally eliminated, p=19 vertical orders 0-8 eliminated, with p=19 order 9 as the first unfinished unit. The line requires persistent review, bounded task routing, durable handoff, and integration so replacement researchers can continue without predecessor chat state.",
  "next_action": "Assume persistent line responsibility for the T6 threshold program. Consume the current research task and dossier, route one bounded researcher to the first unfinished p=19 order-9 unit, audit each returned exact certificate incrementally, update the dossier, and publish or split only the next justified bounded task when the mathematical frontier changes. Preserve closed-work pins and route any theorem/counterexample to independent review or formalization as appropriate.",
  "dependencies": [],
  "source_refs": [
    "research_artifacts/T6_SHAPE_MOMENT_PERSISTENT_LINE_DRIVER_20260909/dossier.md",
    "research_task_records/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/",
    "https://github.com/awdawmip/chatgpt-global-knowledge/commit/047b47aedbd129d5fb2c2a0af136704f5d802592",
    "https://github.com/awdawmip/chatgpt-global-knowledge/commit/8cdc2272e4d75859002686222dc81d3974a26b1c"
  ],
  "evidence_status": "USER_DELEGATED_PERSISTENT_LINE_DRIVER_HANDOFF",
  "last_progress_ref": "https://github.com/awdawmip/chatgpt-global-knowledge/commit/8cdc2272e4d75859002686222dc81d3974a26b1c",
  "last_progress_at": "2026-09-06T08:47:32+08:00",
  "hard_block": "PERSISTENT_REVIEW_AND_SUCCESSOR_ROUTING_FOR_T6_LINE",
  "tags": [
    "T6",
    "persistent-driver",
    "research-orchestration",
    "BRC",
    "durable-handoff"
  ],
  "claim_lease_minutes": 180,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "GOV-T6-SHAPE-MOMENT-PERSISTENT-LINE-DRIVER",
  "parent_objective_id": "EM-T6-SHAPE-MOMENT-EXACT-THRESHOLD",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "T6DRV",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:b3d44e7cb736426e48b7994d280192f2f48ddde306af1d7ad80db2012c00864b",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Persistent Line Driver: T6 Shape-Moment Exact Threshold

Status: `READY / PUBLISHED_REGISTERED`

## Mother question

How should the \(T_6\) shape-moment resolution line be carried from its current exact frontier to a validated theorem or counterexample while preserving continuity across short-lived researchers and replacement conversations?

This is a line-management and evidence-integration task. It does not itself grant mathematical truth to any returned result.

## Frozen inputs and scope

The delegated line is the exact degree-6 shape-moment threshold problem with parent objective `EM-T6-SHAPE-MOMENT-EXACT-THRESHOLD`.

The current durable mathematical frontier is:

- exact \(T_1,\ldots,T_5 = 6,20,105,301,941\);
- exact \(L=360\) degree-6 witness/minimum 2332;
- maximal \(p\ge29\) eliminated below 2332;
- maximal \(p=23\) globally eliminated;
- maximal \(p=19\) vertical orders 0 through 8 eliminated;
- first unfinished mathematical unit: \(p=19\) vertical order 9, then orders 10-12 if necessary.

The primary execution task is `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`. The persistent line dossier is `research_artifacts/T6_SHAPE_MOMENT_PERSISTENT_LINE_DRIVER_20260909/dossier.md`.

The Driver must preserve exact theorem strength and source pins. Ordinary line review, task splitting, successor selection, replication/formalization routing, and source integration belong to this line. Escalate to the portfolio Owner only for a genuine cross-line conflict, authority change, major reprioritization, or a decision that changes the parent objective.

## Hard target and required outputs

Hard target: `PERSISTENT_T6_LINE_WITH_RESTART_FREE_SUCCESSOR_HANDOFF`.

Maintain the line until one of the mathematical terminal outcomes is independently supported: exact \(T_6=2332\), or an exact cheaper collision.

Required Driver outputs:

1. Maintain the line dossier with accepted frontier, unresolved obligations, exact immutable evidence, current task/publication identifiers, and the smallest next unit.
2. Route bounded research work from the existing frontier rather than replaying closed layers.
3. Audit each new result incrementally against the previous accepted ledger; preserve rejected or partial results as provenance without silently turning them into accepted mathematics.
4. When the frontier changes, continue the same task if appropriate; otherwise publish a justified bounded successor or split a genuinely independent subproblem.
5. Require durable proof/checker material before a short-lived researcher finishes when later reuse is expected.
6. Route important terminal claims to an independent reviewer or formalization path when that materially increases confidence, especially if the line Driver contributed to the proof construction.
7. Keep the state-machine frontier sufficient for a replacement Driver or researcher to resume without hidden predecessor conversation state.
8. Update the dossier after every accepted semantic change, not after mere execution noise.

## Research value to preserve

The line contains expensive exact enumerations and saturated-lattice certificates that should never be reconstructed merely because a conversation ended. A persistent Driver turns those artifacts into a cumulative review ledger and keeps the mathematical work modular: researchers solve bounded units, while the line retains the proof architecture and selects the next true bottleneck.

This also protects the user's methodological requirement that full integer and small-prime composite structure remain visible. The Driver must prevent a successor from accidentally reverting to prime-only or total-only observers that erase the valuation information already shown to be decisive.

## Success, kill, and return criteria

Success for this Driver task is a durable line state in which the terminal mathematical result has been independently audited, the exact evidence is bound, and no unresolved line-local obligation remains.

Kill or redirect any action that:
- restarts a verified-complete layer without a demonstrated integrity defect;
- treats a new researcher as if it inherited hidden predecessor context;
- publishes speculative stage chains before their predecessor gate is resolved;
- weakens a global statement to a support-local computation without recording the remaining rescue channels;
- confuses a task publication or dossier update with theorem acceptance.

If the current Driver is replaced, return the dossier and immutable task identifiers as the handoff. The replacement begins from the smallest recorded unfinished unit and does not need the current conversation.
