# Enterprise Math Unified Research Runtime

Status: `ACTIVE / CANONICAL CONTROL-PLANE RUNTIME / V1.1`  
Effective: `2026-08-25`  
Classification: `NO_NEW_MATHEMATICS`

Canonical machine:

- `research_runtime_state_machine.json`
- `tools/research_runtime_guard.py`
- `tools/research_runtime.py`
- `tools/active_turn_liveness.py`
- `tools/research_task_records.py`
- `tools/research_dispatch.py`
- `tools/research_result_records.py`
- `tools/research_task_registry.py`
- `tools/check_task_registry_cutover.py`

Compatibility and contracts:

- `research_task_publication_contract.json` — V1 taskbook/publication compatibility
- `research_task_publication_contract_v2.json` — immutable publication transaction
- `research_task_registry.json` — V1 compatibility mirror and frozen scheduler cutover metadata
- `research_dispatch_contract.json`
- `research_result_contract.json`
- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`

## 1. Canonical stack

The runtime answers:

`PARENT_OBJECTIVE -> TASK_REGISTRATION -> TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`.

The crucial V1.1 change is that `TASK_REGISTRATION` is no longer trusted merely because a caller supplied a plausible object. `tools/research_runtime_guard.py` authenticates the task against repository state before delegating to the pure runtime.

Freeze:

`CALLER_SUPPLIED_REGISTRATION_OBJECT != TASK_AUTHORITY`.

`UNKNOWN_TASK + FAKE_CLAIMABLE_STATE -> REJECT`.

## 2. Post-cutover task publication

Reusable taskbooks still use the single mandatory taskbook template:

`templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`.

The post-cutover publication transaction is now immutable:

1. draft taskbook;
2. `tools/research_task_records.py prepare` performs normalization and machine review;
3. preparation may mark policy PASS only after lint actually succeeds;
4. `tools/research_task_records.py publish` does **not** rewrite the taskbook;
5. official task existence begins when one immutable record is exclusively created at:

`research_task_records/<task-id>/<publication-id>.json`.

There is no overwrite/`--replace` publication. A corrected generation must explicitly name the exact prior `publication_id` it supersedes.

Therefore:

`TASKBOOK_PREPARED != TASK_PUBLISHED`.

`IMMUTABLE_PUBLICATION_RECORD_CREATED -> TASK_EXISTS`.

`SHARED_TASKS_ARRAY != POST_CUTOVER_TASK_AUTHORITY`.

The historical `research_task_registry.json` remains a compatibility mirror while V1 readers are being retired.

## 3. Legacy scheduler cutover

`research_scheduler.json` remains frozen at its recorded Git blob. It is a legacy definition baseline, not a new-publication path.

`tools/research_scheduler.py` remains the legacy event-reduction primitive.

The canonical scheduling entrypoint is now:

`tools/research_dispatch.py`.

It merges:

- immutable post-cutover task records;
- frozen legacy task definitions;
- Issue #240 runtime events;
- immutable result/Driver-review state.

If a task ID exists in both the legacy baseline and immutable records, the immutable registered definition controls.

Freeze:

`REGISTERED_TASK + CLAIMABLE -> VISIBLE_TO_CANONICAL_SELECTION`.

This closes the prior gap where registry publication could make a task “claimable” while the actual scheduler could not see it.

## 4. Result-side loss prevention

Task preservation alone is insufficient. V1.1 adds an immutable result chain:

`TASK -> FROZEN_RESULT -> DRIVER_REVIEW -> DISPOSITION`.

Frozen returns are recorded at:

`research_result_records/<task-id>/<result-id>.json`.

Driver reviews are separately recorded at:

`research_result_reviews/<result-id>/<review-id>.json`.

The two records are deliberately separate so an executor cannot self-promote a result merely by freezing it.

Required semantics:

`FROZEN_RETURN + NO_DRIVER_REVIEW -> AWAITING_DRIVER_REVIEW`.

`AWAITING_DRIVER_REVIEW -> NOT_RESEARCHER_DISPATCHABLE`.

`TERMINAL_DRIVER_REVIEW -> COMPLETE`.

`RETURN_TO_OWNER / REQUEST_REVISION -> HANDOFF_READY`.

For an immutably registered task, a `DONE` event is accepted only when it names the matching frozen result and that result has a terminal Driver disposition.

## 5. Two leases, never one

Owner lease and conversation/session liveness remain distinct.

`OWNER_LEASE != SESSION_LIVENESS`.

A long task/scheduler lease does not prove that the current conversation is alive.

Default session stale window remains 10 minutes.

`SESSION_STALE + OWNER_LEASE_ACTIVE -> STALE_RECOVERABLE`.

Stale adoption preserves the existing claim and Researcher-ID after durable-frontier verification; it does not replay completed work.

## 6. Terminal scope

Exactly three semantic terminal scopes remain:

- `SUBFLOW`
- `TASK`
- `PARENT_OBJECTIVE`

Required transitions:

`TASK_PUBLISHED -> REEVALUATE_PARENT`.

`SUBFLOW_COMPLETE -> REEVALUATE_PARENT`.

`TASK_FROZEN -> REEVALUATE_PARENT`.

`TASK_COMPLETE -> REEVALUATE_PARENT`.

`PARENT_OBJECTIVE_COMPLETE -> PRE_FINAL`.

`TASK_TERMINAL != PARENT_OBJECTIVE_TERMINAL`.

## 7. Authenticated PRE_FINAL

Canonical PRE_FINAL entrypoint:

`tools/research_runtime_guard.py`.

It first authenticates task existence from:

- an immutable task publication record; or
- an exact frozen legacy task ID for an already-owned continuation.

Only then does it delegate:

`tools/research_runtime.py -> tools/active_turn_liveness.py`.

Freeze:

`PARENT_OBJECTIVE_OPEN + EXECUTABLE_NEXT_ACTION -> FINAL_ALLOWED=false`.

A parent marked complete while runtime work remains is `CONTROL_STATE_INCONSISTENT`.

## 8. Legacy execution boundary

Legacy tasks may continue only as already-owned executions. A caller cannot turn the frozen baseline into fresh dispatch authority merely by sending:

`{"state":"LEGACY_BASELINE_REGISTERED"}`.

For legacy execution/adoption the authenticated runtime requires a real task ID from the frozen baseline and an existing owner claim. Fresh redispatch requires immutable migration.

## 9. Operator procedure

At a meaningful control boundary:

1. resolve the exact task ID;
2. authenticate task publication/legacy status;
3. use `tools/research_dispatch.py`, not the frozen scheduler file, for selection/status;
4. keep owner lease separate from session liveness;
5. freeze return evidence through `tools/research_result_records.py` when task research ends;
6. keep the task in `AWAITING_DRIVER_REVIEW` until an immutable Driver review/disposition exists;
7. return SUBFLOW/TASK terminals to the parent objective;
8. invoke authenticated PRE_FINAL only at the parent boundary.

## 10. Required regressions

Repository regressions must prove behavior, not merely policy text:

- forged registration cannot authorize an unknown task;
- registered tasks enter the same dispatch view as legacy tasks;
- immutable task publication cannot overwrite a prior generation;
- placeholders/empty mandatory sections cannot publish;
- publish cannot self-mark PASS before machine lint;
- frozen result without Driver review becomes `AWAITING_DRIVER_REVIEW`;
- registered `DONE` without matching reviewed result is ignored;
- terminal Driver review closes dispatch;
- return/review blob drift fails audit;
- stale adoption preserves claim identity;
- open parent plus executable action forbids final.

## 11. Enforcement boundary

This repository now contains an authenticated canonical runtime entrypoint and result-side closure, but a product host still has to invoke or faithfully implement PRE_FINAL to physically intercept final-channel emission. Repository conformance must not be misreported as host-level enforcement.
