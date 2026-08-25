# Enterprise Math Unified Research Runtime

Status: `ACTIVE / CANONICAL CONTROL-PLANE RUNTIME / V1`
Effective: `2026-08-25`
Classification: `NO_NEW_MATHEMATICS`

Canonical machine:

- `research_runtime_state_machine.json`
- `tools/research_runtime.py`

This runtime composes, rather than replaces, the existing scheduler, identity, taskbook and active-turn contracts.

## 1. Why this object exists

The runtime is the single control object that answers all of the following at once:

`PARENT_OBJECTIVE -> TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`

A role-specific contract may still own its own semantics, but no local terminal state may be interpreted as permission to end the whole research turn without passing through this runtime.

## 2. Canonical runtime object

Every nontrivial research/control turn should be representable as:

```json
{
  "parent_objective": {"objective_id": "...", "status": "OPEN"},
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

Not every route needs every value populated immediately, but the nine canonical fields themselves are not optional when the runtime object is materialized.

## 3. Two leases, never one

### Owner lease

The owner lease answers:

> Who still owns this task/branch/claim?

The existing scheduler `claim_lease_minutes` and `lease_until` are interpreted as **owner-lease** fields. A task-local 120-minute or 1440-minute claim remains legal as ownership policy.

It does **not** mean the current chat is alive.

### Session liveness

The session liveness clock answers:

> Is this exact conversation instance still making visible or durable progress?

Default stale window: **10 minutes**.

The clock may be renewed by visible/durable session progress or an explicit session heartbeat. It must not inherit the owner-lease duration.

Freeze:

`OWNER_LEASE != SESSION_LIVENESS`.

`LONG_OWNER_LEASE != LIVE_CONVERSATION`.

## 4. Session states

The runtime classifies the conversation as:

- `ACTIVE` — session is within the liveness window;
- `STALE_RECOVERABLE` — session is stale but its owner claim is still valid;
- `STALE_UNOWNED` — session is stale and the owner claim is no longer valid;
- `TERMINATED` — session was explicitly terminated.

Critical transition:

`SESSION_STALE + OWNER_LEASE_ACTIVE -> STALE_RECOVERABLE`.

Do not wait for owner-lease expiry merely because the old conversation died.

## 5. Stale adoption

When a replacement conversation sees `STALE_RECOVERABLE`, it must **adopt the existing owner claim** rather than issue a second claim.

Before adoption, verify all of:

1. exact `taskbook_source`;
2. exact `owner_branch`;
3. exact live `claim_id`;
4. refreshed remote `HEAD` against the durable frontier;
5. execution stamp;
6. durable outputs/checkpoints;
7. `durable_frontier_verified=true`.

Then:

`STALE_RECOVERABLE -> ADOPT_EXISTING_OWNER_CLAIM -> RESUME_FROM_DURABLE_FRONTIER`.

Adoption invariants:

- claim is not reissued;
- Researcher-ID is preserved;
- completed units are not replayed;
- resume at `CURRENT_UNFINISHED_UNIT`;
- if no unfinished unit remains, `REEVALUATE_PARENT`.

A mismatch in taskbook source, branch, claim, remote head, execution stamp or frozen durable frontier is a control error, not permission to guess.

## 6. Terminal scope

Exactly three semantic terminal scopes exist:

- `SUBFLOW`
- `TASK`
- `PARENT_OBJECTIVE`

Required transitions:

`SUBFLOW_COMPLETE -> REEVALUATE_PARENT`

`TASK_FROZEN -> REEVALUATE_PARENT`

`TASK_COMPLETE -> REEVALUATE_PARENT`

`PARENT_OBJECTIVE_COMPLETE -> PRE_FINAL`

A taskbook instruction such as “freeze and stop; do not open F6” is normally a **TASK terminal**, not proof that the parent Driver objective is complete. The researcher stops that task; the controlling loop then returns to the parent objective for review/routing.

Freeze:

`TASK_TERMINAL != PARENT_OBJECTIVE_TERMINAL`.

## 7. PRE_FINAL

The unified runtime delegates the base liveness decision to the existing canonical primitive:

`tools/active_turn_liveness.py`.

The runtime orchestration entry is:

`tools/research_runtime.py`.

Core rule:

`PARENT_OBJECTIVE_OPEN + EXECUTABLE_NEXT_ACTION -> FINAL_ALLOWED=false`.

Only runtime transitions whose liveness primitive returns one of the final-allowed outcomes may render a final response. `final_response_identity_policy.json` is evaluated **after** final permission; it cannot create permission by itself.

Therefore:

`RUNTIME_FINAL_ALLOWED_FALSE -> FINAL_CHANNEL_FORBIDDEN`.

## 8. Operator procedure for every researcher/Driver

At a meaningful boundary, use this order:

1. identify the parent user/Driver objective;
2. identify the exact current task and owner claim;
3. classify the current session independently from owner lease;
4. refresh/verify the durable frontier when recovery or handoff is involved;
5. identify the first unfinished unit;
6. materialize the next executable action;
7. classify any completion as `SUBFLOW`, `TASK`, or `PARENT_OBJECTIVE`;
8. for `SUBFLOW`/`TASK`, return to parent routing;
9. immediately before final, run the PRE_FINAL decision;
10. only if final is allowed, render the final response and identity footer.

Do not replace this with “the latest tool call succeeded”, “the task froze”, “the PR is ready”, “the scheduler lease is still live”, or “the user can send continue”. None is a parent-terminal proof.

## 9. Scheduler compatibility

`research_scheduler.json` remains the durable task/owner queue. Its current V1 lease remains supported.

Runtime interpretation:

- `LEASED + ACTIVE session` -> `KEEP_CURRENT_SESSION`;
- `LEASED + STALE_RECOVERABLE` -> `ADOPT_OWNER_CLAIM`;
- `LEASED + unknown session liveness` -> `VERIFY_SESSION_LIVENESS`;
- `NEEDS_DISPATCH` -> `CLAIM_NEW_OWNER`.

Thus `selection_policy.skip_live_leases=true` remains valid for actual live owner/session pairs, but an unverified or stale conversation is no longer silently treated as a live chat merely because the owner lease has time remaining.

## 10. Required regressions

The repository regression suite must exercise transitions, not only policy wording. At minimum:

- tool success + open parent + next action -> final rejected;
- subflow complete -> parent reevaluated;
- task frozen -> parent reevaluated;
- 1440-minute owner lease + 11-minute idle session -> `STALE_RECOVERABLE`;
- stale replacement preserves claim and Researcher-ID;
- stale replacement resumes the first unfinished unit without replay;
- mismatched recovery evidence is rejected;
- expired owner lease cannot be adopted;
- parent completion passes through PRE_FINAL before final rendering.

## 11. Enforcement boundary

The repository now contains an executable canonical control-plane runtime and transition regressions. A ChatGPT/product harness still has to invoke or faithfully implement the runtime decision to physically intercept a final-channel emission. Repository conformance must never be misreported as a product-level interceptor when the host runtime does not call it.
