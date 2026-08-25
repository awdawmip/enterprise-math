# Enterprise Math Unified Research Runtime

Status: `ACTIVE / CANONICAL CONTROL-PLANE RUNTIME / V1`
Effective: `2026-08-25`
Classification: `NO_NEW_MATHEMATICS`

Canonical machine:

- `research_runtime_state_machine.json`
- `tools/research_runtime.py`
- `tools/active_turn_liveness.py`
- `tools/research_task_registry.py`

Task publication/registry:

- `research_task_publication_contract.json`
- `research_task_registry.json`
- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`
- `docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md`

This runtime composes, rather than replaces, the scheduler, identity, taskbook, task-publication and active-turn contracts.

## 1. Why this object exists

The runtime is the single control object that answers all of the following at once:

`PARENT_OBJECTIVE -> TASK_REGISTRATION -> TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`

A role-specific contract may still own its own semantics, but no local terminal state and no unregistered task-like artifact may be interpreted as executable work outside this runtime.

## 2. Registered-task gate

Task existence is now explicit runtime state.

Freeze:

`TASKBOOK_FILE != PUBLISHED_TASK`.

`OFFICIAL_NEW_TASK -> CANONICAL_TASK_REGISTRY_RECORD`.

`UNREGISTERED_NEW_TASK -> NO READY / NO CLAIM / NO EXECUTION`.

Every new task published by a researcher, Driver or Foundation Steward uses the same publication template and is written to `research_task_registry.json` through `tools/research_task_registry.py` or an exact equivalent transaction.

Researchers may publish claimable tasks without Driver approval. Researcher publication defaults to runtime rank `P2 / MEDIUM`; a publisher request is preserved, and Driver portfolio reprioritization remains separate authority. Publication does not grant Working Truth, Foundation status, theorem truth, canonical promotion or Driver authority.

FREE Phase A remains non-agenda discovery. A free researcher may publish a task only after Phase-B audit has produced an audited candidate/negative-obstruction state allowed by the candidate lifecycle. Driver intake is not required merely to register that task.

A task researcher may publish a valuable side residue without switching or terminating the current task. The publication record must preserve `parent_objective_id`, exact lineage, frontier, next action and `research_value`.

Legacy pre-cutover tasks may continue existing executions under baseline compatibility, but any fresh redispatch or current-policy re-review requires explicit registration.

Task publication is a `SUBFLOW`; after it succeeds the runtime returns to the current parent objective.

## 3. Canonical runtime object

Every nontrivial research/control turn should be representable as:

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

## 4. Two leases, never one

### Owner lease

The owner lease answers who still owns the task/branch/claim. Existing scheduler `claim_lease_minutes` and `lease_until` are **owner-lease** fields. Long owner leases remain legal ownership policy.

They do **not** mean the current chat is alive.

### Session liveness

The session clock answers whether this exact conversation is still making visible or durable progress.

Default stale window: **10 minutes**.

Freeze:

`OWNER_LEASE != SESSION_LIVENESS`.

`LONG_OWNER_LEASE != LIVE_CONVERSATION`.

## 5. Session states

The runtime classifies the conversation as:

- `ACTIVE`;
- `STALE_RECOVERABLE`;
- `STALE_UNOWNED`;
- `TERMINATED`.

Critical transition:

`SESSION_STALE + OWNER_LEASE_ACTIVE -> STALE_RECOVERABLE`.

Do not wait for owner-lease expiry merely because the old conversation died.

## 6. Stale adoption

When a replacement conversation sees `STALE_RECOVERABLE`, it adopts the existing owner claim rather than issuing a second claim.

Before adoption, verify taskbook source, owner branch, live claim id, refreshed remote HEAD, execution stamp, durable outputs and durable-frontier integrity.

Then:

`STALE_RECOVERABLE -> ADOPT_EXISTING_OWNER_CLAIM -> RESUME_FROM_DURABLE_FRONTIER`.

Adoption preserves the claim and Researcher-ID, does not replay completed units, resumes at the first unfinished unit, and reevaluates the parent when no unfinished unit remains.

## 7. Terminal scope

Exactly three semantic terminal scopes exist:

- `SUBFLOW`
- `TASK`
- `PARENT_OBJECTIVE`

Required transitions:

`SUBFLOW_COMPLETE -> REEVALUATE_PARENT`

`TASK_PUBLISHED -> REEVALUATE_PARENT`

`TASK_FROZEN -> REEVALUATE_PARENT`

`TASK_COMPLETE -> REEVALUATE_PARENT`

`PARENT_OBJECTIVE_COMPLETE -> PRE_FINAL`

Freeze:

`TASK_TERMINAL != PARENT_OBJECTIVE_TERMINAL`.

## 8. PRE_FINAL

The runtime delegates base liveness to `tools/active_turn_liveness.py`; orchestration entry is `tools/research_runtime.py`.

Core rule:

`PARENT_OBJECTIVE_OPEN + EXECUTABLE_NEXT_ACTION -> FINAL_ALLOWED=false`.

`RUNTIME_FINAL_ALLOWED_FALSE -> FINAL_CHANNEL_FORBIDDEN`.

## 9. Operator procedure

At a meaningful boundary:

1. identify parent objective;
2. verify current task registration before READY/CLAIM/execution;
3. identify task and owner claim;
4. classify session independently from owner lease;
5. verify durable frontier when recovery/handoff is involved;
6. identify first unfinished unit and next executable action;
7. classify terminal scope;
8. return SUBFLOW/TASK terminals to parent routing;
9. immediately before final, run PRE_FINAL;
10. only then render final response and identity footer.

Do not replace this with “taskbook exists”, “handoff exists”, “scheduler entry exists”, “tool call succeeded”, “task froze”, “PR is ready”, “lease is live”, or “the user can send continue”.

## 10. Scheduler compatibility

`research_scheduler.json` remains the durable legacy task/owner queue. For post-cutover tasks, registration is a prerequisite to scheduling/claim.

Runtime interpretation:

- `UNREGISTERED new task` -> register before dispatch;
- `REGISTERED/CLAIMABLE` -> eligible for claim;
- `LEASED + ACTIVE session` -> `KEEP_CURRENT_SESSION`;
- `LEASED + STALE_RECOVERABLE` -> `ADOPT_OWNER_CLAIM`;
- `LEASED + unknown session liveness` -> `VERIFY_SESSION_LIVENESS`;
- `NEEDS_DISPATCH` -> `CLAIM_NEW_OWNER` only after registration gate.

Task registration, owner lease and session liveness are distinct controls.

## 11. Required regressions

The repository tests transitions, not only policy wording. Required cases include:

- researcher can publish a registered claimable task without Driver approval;
- raw free-research candidate cannot publish a task;
- current-policy dispatchable task without registry record fails orphan audit;
- publication cannot grant Working Truth or canonical promotion;
- unregistered new task cannot execute;
- tool success + open parent + next action -> final rejected;
- task frozen -> parent reevaluated;
- 1440-minute owner lease + 11-minute idle session -> `STALE_RECOVERABLE`;
- stale adoption preserves claim/identity and does not replay completed work;
- mismatched recovery evidence is rejected;
- parent completion passes PRE_FINAL.

## 12. Enforcement boundary

The repository contains executable canonical control-plane runtime, task-publication registry and transition regressions. A ChatGPT/product harness still has to invoke or faithfully implement these decisions to physically intercept a final-channel emission. Repository conformance must never be misreported as a product-level interceptor when the host runtime does not call it.
