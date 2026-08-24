# Enterprise Math Research Scheduling Protocol

Status: `ACTIVE / CANONICAL SCHEDULING CONTRACT / V2`
Effective: `2026-08-24`
Machine config: `research_scheduler_v2.json`
Reducer/CLI: `tools/research_scheduler.py`
Runtime event log: GitHub Issue #240
Full state-machine contract: `docs/RESEARCH_SCHEDULER_V2.md`

## 1. Scheduling invariant

Research remains parallel by default. Canonical promotion is serialized only where repository consistency requires it. `defer`, `consume`, review, CI, and moving `main` are not research blockers. Only a complete four-field `HARD_BLOCK` may place a task in `BLOCKED`.

## 2. Every task is registry-visible

The V2 registry is the union of V2 `PUBLISH`/`REGISTER_ORPHAN` events, all discoverable `research_tasks/*.md` taskbooks, and the read-only V1 static seed during migration.

A taskbook that exists but was never registered is therefore visible as `ORPHANED`; it is never silently missing and never directly dispatchable.

## 3. Lifecycle

`PUBLISH -> PENDING_REVIEW -> REVIEW(DISPATCH, APPROVE) -> READY -> CLAIM -> CLAIMED/IN_PROGRESS -> RETURN -> RETURNED -> REVIEW(RETURN, APPROVE) -> DONE`

Unfinished sessions use `HANDOFF -> HANDOFF_READY`.

Lease expiry, explicit `ORPHAN`, unregistered taskbooks, and externally recovered branch/return work become durable `ORPHANED` entries. Recovery requires Driver `ADOPT` or `REVIEW(ORPHAN_RECOVERY)`.

## 4. Open publication, separated approval

Researchers, including FREE researchers, may `PUBLISH` a task into `PENDING_REVIEW`. Publication never creates `READY` and does not bypass candidate maturity, provenance, official taskbook, or roadmap gates.

Drivers may publish too, but a Driver cannot DISPATCH-review a task published by that same Driver-ID.

## 5. Cross-review is machine-enforced

A V2 worker cannot emit a valid `DONE`. Completed work must `RETURN`, then a Driver review decides `APPROVE -> DONE`, `REVISE -> HANDOFF_READY`, or `REJECT -> REJECTED`.

RESEARCH tasks may be released, adopted, and claimed only under a currently registered `ACTIVE_OWNER/ACTIVE_BRIDGE` owner.

## 6. Claims are leases

A second claim cannot preempt a live lease. `HEARTBEAT` and `PROGRESS` renew it; `HANDOFF` releases it. Expiry creates an auditable orphan record instead of silently becoming an ordinary handoff.

## 7. Correct role usage

Researchers/FREE: `PUBLISH`, `CLAIM`, `HEARTBEAT`, `PROGRESS`, `RETURN`, `HANDOFF`, complete `HARD_BLOCK`.

Drivers: `REVIEW(DISPATCH|RETURN|ORPHAN_RECOVERY)`, `ADOPT`, `SUPERSEDE`, deterministic dispatch/review routing, subject to self-review separation.

Runtime state changes belong in Issue #240 as events; do not edit static files to impersonate runtime transitions.

## 8. Commands

```bash
python tools/research_scheduler.py validate
python tools/research_scheduler.py snapshot --events events.jsonl
python tools/research_scheduler.py audit-registry --events events.jsonl
python tools/research_scheduler.py select --events events.jsonl
python tools/research_scheduler.py select-review --events events.jsonl --reviewer-id EM-DVR-ABC123
python tools/research_scheduler.py emit ...
```

Prefer `emit` to hand-written event JSON.

## 9. Workflow truth is not theorem truth

Scheduler `DONE` closes workflow only. It does not itself establish theorem truth, novelty, canonical status, Foundation acceptance, or L4 promotion.

## 10. V1 migration

`research_scheduler.json` remains a read-only legacy seed; V1 events remain replayable so historical state is not erased. New runtime behavior is V2 only. See `docs/RESEARCH_SCHEDULER_V2.md` for the full machine contract.
