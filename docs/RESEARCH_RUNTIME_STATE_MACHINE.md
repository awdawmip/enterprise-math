# Enterprise Math Runtime State Machine

Status: `ACTIVE / CANONICAL / V2`

The live runtime is current-only. Task definitions come from immutable V2 task-publication records, runtime ordering comes from `research_runtime_policy_v2.json`, and authenticated Issue #240 comments are reduced by `tools/research_runtime_reducer.py`.

## Live chain

`PARENT_OBJECTIVE -> IMMUTABLE_TASK_PUBLICATION -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`

Canonical tools:

- `research_control_dispatch.py` — recovery-aware top-level router;
- `tools/research_dispatch.py` — fresh task selector;
- `tools/research_lane_dispatch.py` — active-cohort lane selector;
- `tools/research_lane_claims.py` — exact lane-claim ownership and conflict surface;
- `tools/research_cohort_runtime.py` — exact cohort/lane runtime ownership surface;
- `tools/research_runtime.py` — parent/session/final state machine;
- `tools/research_runtime_reducer.py` — pure authenticated-event reducer;
- `tools/research_runtime_guard.py` — repository-backed execution/adoption/final guard;
- `tools/research_task_records.py` — immutable task publication;
- `tools/research_execution_records.py` and `tools/research_result_records.py` — durable execution/result records;
- `tools/active_turn_liveness.py` — session-liveness primitive.

## Invariants

`UNPUBLISHED_TASK -> NO READY / NO CLAIM / NO EXECUTION`.

`AUTHENTICATED_ISSUE_240_EVENT_ONLY -> RUNTIME_MUTATION`.

`OWNER_LEASE != SESSION_LIVENESS`.

`SESSION_STALE + OWNER_LEASE_ACTIVE -> ADOPT_EXISTING_CLAIM_AFTER_DURABLE_FRONTIER_VERIFICATION`.

`PARENT_OBJECTIVE_OPEN + EXECUTABLE_NEXT_ACTION -> FINAL_ALLOWED=false`.

The archived pre-V2 state is provenance, not a runtime fallback. Exact source bytes are pinned in `control_plane/legacy_control_migration_manifest.json` and preserved on `archive/legacy-control-plane-pre-v2-20260902`.
