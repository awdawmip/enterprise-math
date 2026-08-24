# Enterprise Math Research Scheduling Protocol

Status: `ACTIVE / CANONICAL SCHEDULING CONTRACT / V2`  
Effective: `2026-08-25`  
Machine contract: `research_scheduler_v2.json`  
Reducer / event emitter: `tools/research_scheduler.py`  
Runtime event log: GitHub Issue #240

## 1. Core invariant

Enterprise Math separates scientific work from control-plane authority:

> **any eligible role may publish a mature task; only reviewed tasks may execute; executors return results; Drivers independently close them; every abandoned task remains visible.**

Scheduler state coordinates task existence, dispatch, execution, review, handoff, and orphan recovery. It does not decide theorem truth or canonical mathematical promotion.

`TASKBOOK_FILE != RUNTIME_STATE_AUTHORITY`.

`PUBLISH != READY`.

`RETURN != DONE`.

`LEASE_EXPIRY != SILENT_HANDOFF`.

## 2. One task registry

Every official task must exist in scheduler V2.

There are two creation paths:

1. **V2 runtime publication** — a valid `PUBLISH` event creates the task immediately in state `PUBLISHED`;
2. **migration/bootstrap** — tasks that already existed before V2 are imported from the V1 seed registry or an explicit V2 bootstrap record.

A Markdown taskbook may describe a task, but it cannot create scheduler `READY`, `RETURNED`, `ORPHANED`, or `DONE` authority by itself.

CI runs registry-integrity checks. A taskbook claiming an executable state while its task ID is absent from the scheduler registry is an error.

## 3. Normal lifecycle

The normal lifecycle is:

```text
PUBLISH
  -> PUBLISHED / NEEDS_REVIEW
  -> REVIEW(stage=DISPATCH, verdict=ACCEPT)
  -> READY / NEEDS_DISPATCH
  -> CLAIM
  -> CLAIMED
  -> PROGRESS ...
  -> IN_PROGRESS
  -> RETURN
  -> RETURNED / NEEDS_REVIEW
  -> REVIEW(stage=RETURN, verdict=ACCEPT)
  -> DONE / COMPLETE
```

Other valid branches include:

```text
RETURNED -> REVIEW(RETURN, CHANGES_REQUESTED) -> CHANGES_REQUESTED -> CLAIM ...
PUBLISHED -> REVIEW(DISPATCH, CHANGES_REQUESTED) -> PUBLISHED
PUBLISHED -> REVIEW(DISPATCH, REJECT) -> REJECTED
active task -> HANDOFF -> HANDOFF_READY
active task -> HARD_BLOCK -> BLOCKED -> UNBLOCK -> HANDOFF_READY
active/legacy task -> ORPHAN -> ORPHANED -> RECOVER or REVIEW(RECOVERY) -> HANDOFF_READY
any nonterminal task -> SUPERSEDE (Driver-authorized in V2) -> SUPERSEDED
```

## 4. Publication

`PUBLISH` is task registration, not approval.

Allowed publisher roles are defined by `research_scheduler_v2.json` and currently include RESEARCHER, RESEARCH_DRIVER, STEWARD, and USER-originated control-plane publication.

A researcher may therefore publish a mature task without waiting for a Driver to author the taskbook. A FREE researcher remains excluded from automatic scheduler selection/CLAIM during autonomous Phase A; after its candidate has reached the required audited intake state, it may author and publish the derived task. The result is still only `PUBLISHED / NEEDS_REVIEW`.

A published task cannot be claimed until Driver dispatch review accepts it.

## 5. Driver cross-review

`REVIEW` is a scheduler event with three stages:

- `DISPATCH` — decide whether a `PUBLISHED` task becomes executable;
- `RETURN` — decide whether a `RETURNED` execution is complete;
- `RECOVERY` — decide how an `ORPHANED` task re-enters or exits the active portfolio.

A Driver publication cannot be approved into `READY` by the same Driver-ID. A research execution cannot be reviewed into `DONE` by its executor identity. Review evidence is recorded by `review_ref` and remains in `review_history`.

`REVIEW` controls workflow state only. Mathematical/canonical promotion remains governed by its own evidence and promotion contracts.

## 6. Claims and progress

A `CLAIM` is a renewable execution lease. Only `READY`, `HANDOFF_READY`, and `CHANGES_REQUESTED` are claimable.

- `HEARTBEAT` renews a lease without claiming scientific progress;
- `PROGRESS` renews and records a meaningful checkpoint;
- `HANDOFF` deliberately releases a claim and requires a concrete next action;
- `RETURN` releases a claim and submits the result for Driver review;
- a V2 executor never emits `DONE`.

A second claim cannot preempt a live lease.

## 7. Orphans are first-class state

When a live lease expires, V2 does **not** silently rewrite the task as `HANDOFF_READY`.

The reducer creates a durable derived orphan record preserving, when available:

- orphan time and reason;
- claim ID;
- actor and Researcher-ID;
- last progress reference;
- last known next action.

The effective state becomes:

`ORPHANED / ORPHANED`.

An explicit `ORPHAN` event may additionally record discovered branch, last commit, source reference, discovering actor, and exact reason. Orphan history survives recovery.

An orphan is not automatically selected. A Driver records `RECOVER` or `REVIEW(stage=RECOVERY, ...)` before it becomes `HANDOFF_READY` again.

## 8. Hard blocks remain exceptional

Only a complete record may stop a route:

```text
HARD_BLOCK:
  missing_object: <exact theorem/data/experiment/artifact>
  owner: <route or external source>
  necessity: <why no meaningful independent next step exists>
  unblock_condition: <precise condition that resumes work>
```

CI, review, scheduler tooling, moving `main`, or lack of downstream acknowledgement are not mathematical hard blocks.

## 9. Deterministic automatic selection

When TASK_RESEARCH has no user-selected task, the reducer considers only tasks with `dispatch_state=NEEDS_DISPATCH`.

It prefers:

1. `HANDOFF_READY`;
2. `CHANGES_REQUESTED`;
3. fresh `READY`;

then priority, leverage, oldest progress, and stable task ID. `PUBLISHED`, `RETURNED`, `ORPHANED`, `BLOCKED`, terminal states, and live leases are never auto-selected.

FREE_AXIOM_DISCOVERY does not enter this automatic selection path.

## 10. Runtime event schema

New events use:

`ENTERPRISE_MATH_SCHEDULER_EVENT_V2`.

The event log is append-only. The reducer accepts legacy V1 events for migration/history. In particular, a historical V1 `DONE` remains grandfathered rather than rewriting append-only history. No new V1 `DONE` should be emitted after V2 activation.

Use the emitter commands rather than hand-writing JSON where practical:

```text
python tools/research_scheduler.py emit-publish ...
python tools/research_scheduler.py emit-review ...
python tools/research_scheduler.py emit-claim ...
python tools/research_scheduler.py emit-progress ...
python tools/research_scheduler.py emit-handoff ...
python tools/research_scheduler.py emit-return ...
python tools/research_scheduler.py emit-orphan ...
python tools/research_scheduler.py emit-recover ...
```

The emitted JSON is appended to Issue #240 by the available connected GitHub/control-plane path.

## 11. Required checks

Repository/control-plane maintenance must pass:

```text
python tools/research_scheduler.py validate
python tools/research_scheduler.py registry-integrity
```

The unit-test suite pressure-tests publication, independent review, execution return, lease expiry, orphan persistence, recovery, selection, legacy migration, and hidden-task detection.

## 12. Research remains parallel

The V2 state machine does not serialize mathematical research globally. It serializes only conflicting execution leases and required review transitions for the same task.

Ownership remains unique; knowledge remains shared; independent research remains parallel; canonical promotion remains a separate bounded lifecycle.
