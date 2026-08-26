# Enterprise Math Unified Research Runtime

Status: `ACTIVE / CANONICAL CONTROL-PLANE RUNTIME / V1.2`  
Effective: `2026-08-26`  
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

The runtime also inherits the GitHub interaction budget:

> **Research remains the hot path. Control records are sparse semantic-boundary persistence, not per-step research telemetry.**

Between genuine publication/checkpoint/result/review boundaries, this runtime adds no routine repository write, CI poll, review poll, moving-main chase, or scheduler heartbeat requirement.

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

Task publication is a semantic checkpoint. It may be batched with the taskbook publication commit; it does not create a requirement for routine research-time writes afterwards.

## 4. Task -> execution binding without a second pre-claim write

Publication does not decide who executes the task or which branch is used.

For new registered executions, the **Issue #240 CLAIM itself is the execution authorization envelope**. One CLAIM carries or resolves:

- exact `task_id` and current `publication_id`;
- `claim_id`;
- `Researcher-ID` or the information needed to derive it deterministically;
- `theorem_owner`;
- `execution_branch`;
- exact `execution_branch_base` commit;
- allowed output paths/prefixes;
- owner lease duration.

The taskbook blob is resolved from the immutable publication record rather than duplicated by the caller.

`theorem_owner` and `execution_branch` are typed separately even when a particular owner-generation uses the same branch name for both.

Freeze:

`REGISTERED_CLAIM = EXECUTION_AUTHORIZATION_ENVELOPE`.

`NO_SEPARATE_REMOTE_EXECUTION_RECORD_WRITE_REQUIRED_BEFORE_CLAIM`.

The preferred distributed claim transaction is:

`VALIDATE CURRENT PUBLICATION -> CREATE/VERIFY BRANCH -> APPEND ONE CLAIM ENVELOPE TO ISSUE #240 -> FIRST VALID CLAIM WINS`.

A registered CLAIM with a stale publication ID or incomplete owner/branch/output envelope is ignored. No PR, merge, CI wait, heartbeat, or second GitHub write is required merely to make the CLAIM valid.

`research_execution_records/<task-id>/<execution-record-id>.json` remains the immutable durable-provenance form used by result freezing. It may be materialized locally after CLAIM and batched with the first genuine durable checkpoint or final return. Historical pre-claim execution-intent records remain compatible but are not the preferred path.

## 5. One canonical dispatch view

`research_scheduler.json` is a frozen legacy task-definition baseline. `tools/research_scheduler.py` remains the legacy event-reduction primitive.

Canonical scheduling is:

`tools/research_dispatch.py`.

It merges:

- current immutable task publication records;
- the frozen legacy task baseline;
- Issue #240 runtime events, including self-contained registered CLAIM envelopes;
- compatible immutable execution records when already present;
- immutable result and Driver-review records.

If the same task ID exists in both the frozen legacy baseline and immutable publications, the immutable publication generation controls the definition.

Freeze:

`REGISTERED_TASK + CLAIMABLE -> VISIBLE_TO_CANONICAL_SELECTION`.

`REGISTERED_CLAIM_WITH_STALE_OR_INCOMPLETE_EXECUTION_ENVELOPE -> IGNORE_EVENT`.

This eliminates both prior splits: registry tasks can no longer be invisible to the real scheduler, and claim validity no longer depends on a second pre-claim repository publication.

## 6. Result-side loss prevention

Task preservation alone is insufficient. The durable result chain is:

`TASK_GENERATION -> CLAIM_ENVELOPE -> EXECUTION_RECORD_AT_DURABLE_CHECKPOINT -> FROZEN_RESULT -> DRIVER_REVIEW -> DISPOSITION`.

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

The execution/result record files are intended to be created in the same publication batch as the durable return/checkpoint whenever possible; they are not separate conversational stop points.

## 7. Owner lease is not session liveness

The valid Issue CLAIM establishes task ownership. A compatible execution record preserves durable provenance. Neither establishes that the current conversation remains alive.

Freeze:

`OWNER_LEASE != SESSION_LIVENESS`.

Default session stale window remains 10 minutes.

`SESSION_STALE + OWNER_LEASE_ACTIVE -> STALE_RECOVERABLE`.

A replacement session verifies the taskbook source, branch, claim, remote HEAD, execution stamp and durable outputs, adopts the existing claim and Researcher-ID, and resumes the first unfinished unit. It does not replay completed work or issue a second claim.

No routine heartbeat is required merely to keep an actively progressing research conversation legitimate; visible/durable progress and stale-recovery semantics remain distinct from owner-lease duration.

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

1. publish one immutable task generation at the task-publication checkpoint;
2. create/verify the execution branch from an exact base;
3. append one self-contained CLAIM envelope; do **not** make a separate pre-claim repository commit/PR merely for execution intent;
4. begin research after the CLAIM validates;
5. between semantic checkpoints, research locally/remotely-silent with zero governance-only heartbeat/CI polling requirements;
6. at the first genuine durable checkpoint or final return, materialize the matching execution record together with the research artifact when durable provenance is needed;
7. freeze the exact return and output manifest through `tools/research_result_records.py` in that same bounded publication batch when practical;
8. enter control-plane state `AWAITING_DRIVER_REVIEW`, not a researcher-dispatchable state;
9. create an immutable Driver review/disposition together with the actual Driver review artifact;
10. return TASK terminality to the parent objective;
11. invoke authenticated PRE_FINAL only at the parent boundary.

For legacy tasks, already-owned execution may continue; fresh redispatch requires immutable migration first.

## 11. Required regressions

Repository tests must prove behavior, not merely policy wording. Required cases include:

- forged registration cannot authorize an unknown task;
- registered and legacy tasks share one derived dispatch view;
- registered tasks are selectable without a row in the frozen scheduler file;
- incomplete or stale registered CLAIM envelope is ignored;
- a complete registered CLAIM becomes live **without** a pre-claim execution-record repository write;
- a compatible historical execution intent may still authorize its matching CLAIM;
- execution provenance pins publication, Researcher-ID, branch/base, output scope and lease before result freeze;
- immutable task publication cannot overwrite an earlier generation;
- placeholder/empty mandatory task sections cannot publish;
- frozen result without Driver review becomes `AWAITING_DRIVER_REVIEW`;
- registered DONE without a matching terminal reviewed result is ignored;
- terminal Driver review closes dispatch;
- return/review blob drift fails audit;
- stale adoption preserves claim identity;
- open parent plus executable action forbids final;
- ordinary execution introduces no governance-only heartbeat, CI-poll, or second pre-claim persistence requirement.

## 12. Enforcement boundary

The repository contains executable canonical publication, execution, dispatch, result and authenticated-runtime gates. A ChatGPT/product host still has to invoke or faithfully implement PRE_FINAL to physically intercept final-channel emission. Repository conformance must never be misreported as host-level enforcement.
