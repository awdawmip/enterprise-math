# Enterprise Math Unified Research Runtime

Status: `ACTIVE / CANONICAL CONTROL-PLANE RUNTIME / V1.2`  
Effective: `2026-08-25`  
Classification: `NO_NEW_MATHEMATICS`

Canonical machine:

- `research_runtime_state_machine.json`
- `tools/research_runtime_guard.py`
- `tools/research_runtime.py`
- `tools/active_turn_liveness.py`
- `tools/research_task_records.py`
- `tools/research_execution_records.py`
- `tools/research_dispatch.py`
- `tools/research_result_records.py`
- `tools/research_task_registry.py`
- `tools/check_task_registry_cutover.py`

Contracts and compatibility:

- `research_task_publication_contract.json` — V1 taskbook/shared-registry compatibility
- `research_task_publication_contract_v2.json` — immutable post-cutover publication
- `research_execution_contract.json` — task-generation to concrete execution binding
- `research_dispatch_contract.json` — merged registered/legacy dispatch
- `research_result_contract.json` — return/review/disposition chain
- `research_task_registry.json` — V1 compatibility mirror plus frozen scheduler cutover metadata
- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json` — the single taskbook template

## 1. Canonical control stack

The runtime answers:

`PARENT_OBJECTIVE -> TASK_REGISTRATION -> TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`.

Task existence, execution identity, live owner claim, session liveness and result disposition are different facts. The runtime is a projection of their authoritative sources; it is not a fourth independent persistent database.

## 2. Authenticated task existence

A caller cannot authorize a task by supplying a plausible registration object.

Freeze:

`CALLER_SUPPLIED_REGISTRATION_OBJECT != TASK_AUTHORITY`.

`UNKNOWN_TASK + FAKE_CLAIMABLE_STATE -> REJECT`.

Canonical post-cutover task existence is an immutable record:

`research_task_records/<task-id>/<publication-id>.json`.

`tools/research_runtime_guard.py` authenticates the task from repository state before delegating to `tools/research_runtime.py` and `tools/active_turn_liveness.py`.

A frozen legacy scheduler task is recognized only by an exact task ID in the frozen baseline. Legacy baseline status cannot be self-declared and cannot authorize a fresh redispatch.

## 3. Immutable publication transaction

The reusable taskbook format remains singular:

`templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`.

Post-cutover publication uses `tools/research_task_records.py`:

1. draft the taskbook;
2. `prepare` validates body, metadata, lineage/origin and policy in memory/temporary state;
3. policy PASS is written only after the validator succeeds;
4. `publish` requires the already prepared exact taskbook and does not rewrite it;
5. publication occurs only by exclusive creation of one immutable publication record.

No V2 `--replace` exists. A correction is a new immutable generation that explicitly names the publication ID it supersedes.

Freeze:

`TASKBOOK_PREPARED != TASK_PUBLISHED`.

`IMMUTABLE_PUBLICATION_RECORD_CREATED -> TASK_EXISTS`.

The V1 shared `research_task_registry.json` remains a compatibility mirror during migration and is not post-cutover publication authority.

## 4. Task -> execution binding

Publication does not decide who executes the task or which branch is used.

Before a registered CLAIM can become live, `tools/research_execution_records.py` creates an immutable execution intent:

`research_execution_records/<task-id>/<execution-record-id>.json`.

The intent pins:

- exact `task_id` and `publication_id`;
- exact taskbook blob;
- `claim_id`;
- `Researcher-ID`;
- `theorem_owner`;
- `execution_branch`;
- exact `execution_branch_base` commit;
- allowed output paths/prefixes;
- owner lease duration.

`theorem_owner` and `execution_branch` are typed separately even when a particular owner-generation uses the same branch name for both.

The distributed claim transaction is:

`CREATE/VERIFY BRANCH -> IMMUTABLE EXECUTION INTENT -> APPEND CLAIM TO ISSUE #240 -> FIRST VALID CLAIM WINS`.

The canonical reducer ignores a registered CLAIM that has no matching execution intent. Multiple losing intents may remain as provenance, but they do not become live owner claims.

## 5. One canonical dispatch view

`research_scheduler.json` is a frozen legacy task-definition baseline. `tools/research_scheduler.py` remains the legacy event-reduction primitive.

Canonical scheduling is:

`tools/research_dispatch.py`.

It merges:

- current immutable task publication records;
- the frozen legacy task baseline;
- matching immutable execution intents;
- Issue #240 runtime events;
- immutable result and Driver-review records.

If the same task ID exists in both the frozen legacy baseline and immutable publications, the immutable publication generation controls the definition.

Freeze:

`REGISTERED_TASK + CLAIMABLE -> VISIBLE_TO_CANONICAL_SELECTION`.

`REGISTERED_CLAIM_WITHOUT_EXECUTION_INTENT -> IGNORE_EVENT`.

This eliminates the prior split where registry tasks could be marked claimable yet remain invisible to the actual scheduler.

## 6. Result-side loss prevention

Task preservation alone is insufficient. The result chain is:

`TASK_GENERATION -> EXECUTION_RECORD -> FROZEN_RESULT -> DRIVER_REVIEW -> DISPOSITION`.

Frozen returns are stored at:

`research_result_records/<task-id>/<result-id>.json`.

Driver reviews are independently stored at:

`research_result_reviews/<result-id>/<review-id>.json`.

The executor cannot self-promote the result merely by freezing it.

Required state semantics:

`FROZEN_RETURN + NO_DRIVER_REVIEW -> AWAITING_DRIVER_REVIEW`.

`AWAITING_DRIVER_REVIEW -> NOT_RESEARCHER_DISPATCHABLE`.

`RETURN_TO_OWNER / REQUEST_REVISION -> HANDOFF_READY`.

`TERMINAL_DRIVER_REVIEW -> COMPLETE`.

For immutable registered tasks, a `DONE` event is accepted only when it references the matching frozen result and that result has a terminal Driver disposition.

## 7. Owner lease is not session liveness

The execution intent and Issue CLAIM establish task ownership. They do not establish that the current conversation remains alive.

Freeze:

`OWNER_LEASE != SESSION_LIVENESS`.

Default session stale window remains 10 minutes.

`SESSION_STALE + OWNER_LEASE_ACTIVE -> STALE_RECOVERABLE`.

A replacement session verifies the taskbook source, branch, claim, remote HEAD, execution stamp and durable outputs, adopts the existing claim and Researcher-ID, and resumes the first unfinished unit. It does not replay completed work or issue a second claim.

## 8. Terminal scope

Exactly three semantic terminal scopes exist:

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

Publication is capture, not a current-task switch. Task/subflow terminality never silently closes the parent objective.

## 9. Authenticated PRE_FINAL

Canonical PRE_FINAL entrypoint:

`tools/research_runtime_guard.py`.

It authenticates task existence first, then delegates liveness to the pure runtime and `tools/active_turn_liveness.py`.

Freeze:

`PARENT_OBJECTIVE_OPEN + EXECUTABLE_NEXT_ACTION -> FINAL_ALLOWED=false`.

`AUTHENTICATED_RUNTIME_FINAL_ALLOWED_FALSE -> FINAL_CHANNEL_FORBIDDEN`.

A parent marked complete while runtime work remains is `CONTROL_STATE_INCONSISTENT`, not permission to final.

## 10. Operator procedure

For a new registered task:

1. publish one immutable task generation;
2. create/verify the execution branch from an exact base;
3. create one immutable execution intent with owner/output/identity scope;
4. append the CLAIM event;
5. use `tools/research_dispatch.py` for status and selection;
6. keep session liveness separate from the owner lease;
7. freeze the exact return and output manifest through `tools/research_result_records.py`;
8. wait in control-plane state `AWAITING_DRIVER_REVIEW`, not a researcher-dispatchable state;
9. create an immutable Driver review/disposition;
10. return TASK terminality to the parent objective;
11. invoke authenticated PRE_FINAL only at the parent boundary.

For legacy tasks, already-owned execution may continue; fresh redispatch requires immutable migration first.

## 11. Required regressions

Repository tests must prove behavior, not merely policy wording. Required cases include:

- forged registration cannot authorize an unknown task;
- registered and legacy tasks share one derived dispatch view;
- registered tasks are selectable without a row in the frozen scheduler file;
- registered CLAIM without execution intent is ignored;
- execution intent pins publication, Researcher-ID, branch/base, output scope and lease;
- immutable task publication cannot overwrite an earlier generation;
- placeholder/empty mandatory task sections cannot publish;
- frozen result without Driver review becomes `AWAITING_DRIVER_REVIEW`;
- registered DONE without a matching terminal reviewed result is ignored;
- terminal Driver review closes dispatch;
- return/review blob drift fails audit;
- stale adoption preserves claim identity;
- open parent plus executable action forbids final.

## 12. Enforcement boundary

The repository contains executable canonical publication, execution, dispatch, result and authenticated-runtime gates. A ChatGPT/product host still has to invoke or faithfully implement PRE_FINAL to physically intercept final-channel emission. Repository conformance must never be misreported as host-level enforcement.
