# Enterprise Math Research Scheduler V2

Status: `ACTIVE / UNIFIED RESEARCH CONTROL PLANE`
Effective: `2026-08-24`
Machine config: `research_scheduler_v2.json`
Reducer/CLI: `tools/research_scheduler.py`
Runtime event log: GitHub Issue #240
Owner registry: `branch_governance_overrides.json`
Taskbook inventory: `research_tasks/*.md`

## 1. Core invariant

Every research task must be visible to the scheduler before it can disappear, execute, or close.

The registry is the union of:

1. V2 `PUBLISH` / `REGISTER_ORPHAN` events;
2. every taskbook discovered under `research_tasks/*.md`;
3. the read-only V1 static seed in `research_scheduler.json` during migration.

A taskbook file is not dispatch authority. A taskbook with no scheduler history is automatically visible as `ORPHANED`, never silently ignored and never auto-dispatched. During migration only, a pre-V2 taskbook that already has a genuine V1 runtime event is treated as `LEGACY_EVENT_REGISTERED_TASKBOOK` so its historical CLAIM/HANDOFF/DONE chain can replay instead of being falsely orphaned.

The scheduler controls workflow only. It does not prove a theorem, promote canonical mathematics, or replace Foundation/Steward gates.

## 2. Normal lifecycle

New work:

`PUBLISH -> PENDING_REVIEW -> REVIEW(DISPATCH, APPROVE) -> READY -> CLAIM -> CLAIMED/IN_PROGRESS -> RETURN -> RETURNED -> REVIEW(RETURN, APPROVE) -> DONE`

Interrupted work:

`CLAIMED/IN_PROGRESS -> HANDOFF -> HANDOFF_READY -> CLAIM`

Hard dependency:

`CLAIMED/IN_PROGRESS -> HARD_BLOCK -> BLOCKED -> UNBLOCK -> HANDOFF_READY`

Orphan recovery:

`lease expiry | ORPHAN | unregistered taskbook | REGISTER_ORPHAN -> ORPHANED -> ADOPT or REVIEW(ORPHAN_RECOVERY, APPROVE) -> HANDOFF_READY`

`REJECTED`, `SUPERSEDED`, and `DONE` are terminal workflow states.

## 3. Publication is open; dispatch authority is not

Any Enterprise Math researcher, including `EM_FREE_RESEARCHER`, may register a task by publishing it into the scheduler.

`PUBLISH` always creates `PENDING_REVIEW`. It never creates `READY`.

This preserves scientific freedom without allowing a researcher to self-approve a roadmap item, bypass candidate maturity, or silently create an official dispatchable taskbook.

A Driver may also publish. If a Driver is the publisher, that same Driver cannot perform the `DISPATCH` approval for that publication. A different Driver-ID is required.

## 4. Cross-review is part of the state machine

A V2 worker cannot close its own task with `DONE`.

The worker uses `RETURN`. The task becomes `RETURNED / NEEDS_REVIEW`.

Only a valid Driver `REVIEW` event may decide the return:

- `APPROVE` -> `DONE`;
- `REVISE` -> `HANDOFF_READY` with a concrete `next_action`;
- `REJECT` -> `REJECTED`.

For `DISPATCH` review, a research task must have a concrete owner that is currently `ACTIVE_OWNER` or `ACTIVE_BRIDGE`. The state machine rejects approval, adoption, and claim against inactive owners.

## 5. Orphans are durable workflow objects

Silent abandonment is never converted invisibly to ordinary handoff.

When a live claim lease expires, the reducer records an orphan-history entry containing the prior claim, actor/researcher identity, progress pointer, next action, expiry time and reason, then moves the task to `ORPHANED`.

Other orphan sources are also first-class:

- a taskbook present in the repository but absent from V2 registration;
- a historical branch/return discovered without a scheduler task, registered with `REGISTER_ORPHAN`;
- explicit `ORPHAN` by a coordinator/agent.

`ORPHANED` is never selected by normal dispatch. Recovery requires Driver adoption/review or explicit supersession. `ADOPT` and `REVIEW(ORPHAN_RECOVERY, APPROVE)` may also supply `assigned_owner`; this is the correct way to recover work whose former owner is retired, invalid, or `taskbook/unassigned`.

## 6. Role permissions

### Researcher / FREE researcher

Allowed:

- `PUBLISH` a task proposal into `PENDING_REVIEW`;
- `CLAIM` a `READY/HANDOFF_READY` task;
- `HEARTBEAT`, `PROGRESS`;
- `RETURN` finished work for review;
- `HANDOFF` unfinished work;
- `HARD_BLOCK` only with the complete four-field contract.

Forbidden by the reducer:

- self-transition to `READY`;
- V2 `DONE`;
- Driver `REVIEW`;
- orphan adoption/supersession without Driver identity.

### Research Driver

Allowed:

- all coordination publication actions;
- `REVIEW` for `DISPATCH`, `RETURN`, `ORPHAN_RECOVERY`;
- `ADOPT` orphaned work;
- `SUPERSEDE` stale/replaced work;
- deterministic `select-review` and dispatch routing.

The Driver may not self-review its own Driver-published task into `READY`.

### System/reducer

May derive deterministic state only, including lease-expiry orphaning. It has no mathematical promotion authority.

## 7. Exact event schemas

V2 events use:

`"schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V2"`

The canonical event log is Issue #240, in GitHub comment order. V1 events remain replayable during migration so historical claims and completions do not disappear.

Use the CLI to emit well-formed JSON instead of hand-writing events whenever possible.

Examples:

```bash
python tools/research_scheduler.py emit publish \
  --taskbook research_tasks/EXAMPLE.md \
  --publisher-id EM-FREE-ABC123 \
  --publisher-role RESEARCHER \
  --at 2026-08-24T20:00:00+08:00

python tools/research_scheduler.py emit review \
  --task-id RS-EXAMPLE \
  --review-kind DISPATCH --verdict APPROVE \
  --reviewer-id EM-DVR-ABC123 \
  --review-ref driver_reviews/EXAMPLE.md \
  --assigned-owner program/example \
  --at 2026-08-24T20:05:00+08:00

python tools/research_scheduler.py emit claim \
  --task-id RS-EXAMPLE --claim-id claim-001 \
  --actor agent --at 2026-08-24T20:06:00+08:00

python tools/research_scheduler.py emit return \
  --task-id RS-EXAMPLE --claim-id claim-001 \
  --return-ref research_returns/EXAMPLE_RETURN.md \
  --actor agent --at 2026-08-24T21:00:00+08:00

python tools/research_scheduler.py emit adopt \
  --task-id RS-ORPHAN \
  --reviewer-id EM-DVR-ABC123 \
  --review-ref driver_reviews/ORPHAN_RECOVERY.md \
  --assigned-owner program/example \
  --next-action "resume from frozen evidence" \
  --at 2026-08-24T21:05:00+08:00
```

For a branch/return that exists without a scheduler task, use `emit register-orphan` with a recovered task payload and evidence references.

## 8. Inspection commands

```bash
python tools/research_scheduler.py validate
python tools/research_scheduler.py snapshot --events events.jsonl
python tools/research_scheduler.py audit-registry --events events.jsonl
python tools/research_scheduler.py select --events events.jsonl
python tools/research_scheduler.py select-review --events events.jsonl --reviewer-id EM-DVR-ABC123
```

`validate` checks V2 config plus the V1 migration seed and scans the taskbook inventory. `snapshot` shows every registered/discovered task. `audit-registry` exposes orphaned tasks and invalid event groups.

## 9. Migration invariant

`research_scheduler.json` remains a read-only V1 seed until its legacy tasks have naturally been replaced or superseded. It is no longer the canonical runtime scheduler.

Canonical runtime authority after V2 activation is:

`research_scheduler_v2.json + taskbook inventory + Issue #240 V2/V1 event replay + owner registry`.

There is no post-V2 self-review exception. The direct bootstrap repair authorized on 2026-08-24 is a one-time migration act only.

## 10. CI / repository integrity

The quality workflow runs the full unit test suite and `python tools/research_scheduler.py validate`.

A scheduler change that breaks task discovery, owner coverage, review separation, orphan persistence, lease exclusivity, or migration replay must fail before it is treated as a valid control-plane change.
