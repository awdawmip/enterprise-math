# Enterprise Math Unified Research Runtime

Status: `ACTIVE / CANONICAL CONTROL-PLANE RUNTIME / V1`
Effective: `2026-08-25`
Classification: `NO_NEW_MATHEMATICS`

Canonical machine:

- `research_runtime_state_machine.json`
- `tools/research_runtime.py`
- `tools/active_turn_liveness.py`
- `tools/research_task_registry.py`
- `tools/check_task_registry_cutover.py`

Task publication/registry:

- `research_task_publication_contract.json`
- `research_task_registry.json`
- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`
- `docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md`

This runtime composes, rather than replaces, identity, taskbook, registered-task publication, legacy owner scheduling and active-turn contracts.

## 1. Canonical control object

The runtime answers at once:

`PARENT_OBJECTIVE -> TASK_REGISTRATION -> TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`.

No local terminal state, scheduler row, handoff, taskbook file or chat-only idea may be interpreted as a new executable official task outside this runtime.

## 2. Registered-task gate

Task existence is explicit runtime state.

Freeze:

`TASKBOOK_FILE != PUBLISHED_TASK`.

`OFFICIAL_NEW_TASK -> CANONICAL_TASK_REGISTRY_RECORD`.

`UNREGISTERED_NEW_TASK -> NO READY / NO CLAIM / NO EXECUTION`.

Every new task published by a researcher, Driver or Foundation Steward uses the same publication template and is written to `research_task_registry.json` through `tools/research_task_registry.py` or an exact equivalent transaction.

Researchers may publish claimable tasks without Driver approval. Researcher publication defaults to effective `P2 / MEDIUM`; the publisher request is preserved, while Driver portfolio reprioritization remains separate authority.

Publication does not grant Working Truth, Foundation status, theorem truth, canonical promotion or Driver authority.

FREE Phase A remains non-agenda discovery. A free researcher may publish a task only after Phase-B audit has produced an eligible audited candidate/negative-obstruction state. Driver intake is not required merely to preserve that task.

A task researcher may publish a valuable side residue without switching or terminating the current task. The publication record must preserve `parent_objective_id`, exact lineage, frontier, next action and `research_value`.

Task publication is a `SUBFLOW`; after success the runtime returns to the current parent objective.

## 3. Legacy scheduler cutover

`research_scheduler.json` is now a **frozen legacy task-definition baseline** for existing executions. Its frozen Git blob is recorded in `research_task_registry.json` and verified by:

`tools/check_task_registry_cutover.py`.

Freeze:

`LEGACY_SCHEDULER_RUNTIME_EVENTS_MAY_CONTINUE`.

`LEGACY_SCHEDULER_DEFINITION_FILE_MAY_NOT_PUBLISH_NEW_TASKS`.

`NEW_OR_MODIFIED_TASK -> RESEARCH_TASK_REGISTRY`.

Issue/runtime owner events may continue for already-existing scheduler tasks. But editing `research_scheduler.json` to add or materially modify a task is no longer an official publication path and fails CI until the task is migrated/published through the registry.

Legacy pre-cutover tasks may continue their already-existing execution. Fresh redispatch, modification or current-policy re-review requires explicit registry migration.

This prevents the old scheduler from remaining a hidden second task registry.

## 4. Canonical runtime object

Every nontrivial task execution/control turn should be representable as:

```json
{
  "parent_objective": {"objective_id": "...", "status": "OPEN"},
  "task_registration": {"registry_key": "...", "state": "REGISTERED_OR_LEGACY_BASELINE_REGISTERED"},
  "task": {
    "task_id": "...",
    "status": "ACTIVE",
    "taskbook_source": "...",
    "owner_branch": "..."
  },
  "owner_claim": {
    "claim_id": "...",
    "researcher_id": "...",
    "owner_lease_until": "..."
  },
  "session": {
    "session_id": "...",
    "last_activity_at": "..."
  },
  "durable_frontier": {
    "remote_head": "...",
    "execution_stamp": "...",
    "durable_outputs": []
  },
  "current_unfinished_unit": "...",
  "next_action": {"description": "...", "executable": true},
  "terminal_scope": null,
  "final_allowed": false,
  "control": {}
}
```

## 5. Two leases, never one

The owner lease answers who owns the task/branch/claim. Scheduler `claim_lease_minutes` and `lease_until` are owner-lease fields only.

The session clock answers whether this exact conversation is still making visible or durable progress.

Default stale window: **10 minutes**.

Freeze:

`OWNER_LEASE != SESSION_LIVENESS`.

`LONG_OWNER_LEASE != LIVE_CONVERSATION`.

## 6. Session states and stale adoption

The runtime classifies the conversation as:

- `ACTIVE`;
- `STALE_RECOVERABLE`;
- `STALE_UNOWNED`;
- `TERMINATED`.

Critical transition:

`SESSION_STALE + OWNER_LEASE_ACTIVE -> STALE_RECOVERABLE`.

A replacement conversation verifies taskbook source, owner branch, live claim id, refreshed remote HEAD, execution stamp, durable outputs and durable-frontier integrity, then adopts the existing owner claim rather than issuing a second claim.

`STALE_RECOVERABLE -> ADOPT_EXISTING_OWNER_CLAIM -> RESUME_FROM_DURABLE_FRONTIER`.

Adoption preserves claim/Researcher-ID, does not replay completed units, resumes at the first unfinished unit, and reevaluates the parent when no unfinished unit remains.

## 7. Terminal scope

Exactly three semantic terminal scopes exist:

- `SUBFLOW`;
- `TASK`;
- `PARENT_OBJECTIVE`.

Required transitions:

`SUBFLOW_COMPLETE -> REEVALUATE_PARENT`.

`TASK_PUBLISHED -> REEVALUATE_PARENT`.

`TASK_FROZEN -> REEVALUATE_PARENT`.

`TASK_COMPLETE -> REEVALUATE_PARENT`.

`PARENT_OBJECTIVE_COMPLETE -> PRE_FINAL`.

`TASK_TERMINAL != PARENT_OBJECTIVE_TERMINAL`.

Task/subflow completion clears obsolete local execution frontier before parent routing, except task publication: publication preserves the current task frontier because it is capture, not a task switch.

## 8. PRE_FINAL

The runtime delegates base liveness to `tools/active_turn_liveness.py`; orchestration entry is `tools/research_runtime.py`.

Core rule:

`PARENT_OBJECTIVE_OPEN + EXECUTABLE_NEXT_ACTION -> FINAL_ALLOWED=false`.

`RUNTIME_FINAL_ALLOWED_FALSE -> FINAL_CHANNEL_FORBIDDEN`.

A parent marked complete while unfinished runtime work remains is `CONTROL_STATE_INCONSISTENT`, not permission to final.

## 9. Operator procedure

At a meaningful boundary:

1. identify the parent objective;
2. verify current task registration before READY/CLAIM/execution;
3. ensure a new task came through the unified publication template/registry, not the frozen scheduler file;
4. identify task and owner claim;
5. classify session independently from owner lease;
6. verify durable frontier for recovery/handoff;
7. identify first unfinished unit and next action;
8. classify terminal scope;
9. return SUBFLOW/TASK terminals to parent routing;
10. immediately before final, run PRE_FINAL;
11. only then render final response and identity footer.

Do not substitute “taskbook exists”, “scheduler row exists”, “handoff exists”, “tool call succeeded”, “task froze”, “PR is ready”, “lease is live”, or “the user can send continue”.

## 10. Scheduler compatibility

For existing legacy tasks:

- owner/runtime events remain valid;
- `LEASED + ACTIVE session` -> `KEEP_CURRENT_SESSION`;
- `LEASED + STALE_RECOVERABLE` -> `ADOPT_OWNER_CLAIM`;
- `LEASED + unknown session liveness` -> `VERIFY_SESSION_LIVENESS`.

For post-cutover new/modified tasks:

- `UNREGISTERED` -> register before dispatch;
- `REGISTERED/CLAIMABLE` -> eligible for claim;
- direct scheduler-file task addition -> cutover audit failure.

Task registration, owner lease and session liveness are distinct controls.

## 11. Required regressions

The repository tests transitions, not only wording. Required cases include:

- researcher can publish a registered claimable task without Driver approval;
- raw free-research candidate cannot publish a task;
- current-policy dispatchable task without registry record fails orphan audit;
- legacy scheduler definition drift fails cutover audit;
- publication cannot grant Working Truth or canonical promotion;
- unregistered new task cannot execute;
- tool success + open parent + next action -> final rejected;
- task publication returns to parent without switching current task;
- task frozen -> parent reevaluated;
- 1440-minute owner lease + 11-minute idle session -> `STALE_RECOVERABLE`;
- stale adoption preserves claim/identity and does not replay completed work;
- mismatched recovery evidence is rejected;
- parent completion passes PRE_FINAL only when runtime work is actually exhausted.

## 12. Enforcement boundary

The repository contains executable canonical runtime, registered-task publication, cutover/orphan guards and transition regressions. A ChatGPT/product harness still has to invoke or faithfully implement these decisions to physically intercept final-channel emission. Repository conformance must never be misreported as a product-level interceptor when the host runtime does not call it.
