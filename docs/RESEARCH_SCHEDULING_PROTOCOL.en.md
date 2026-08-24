# Enterprise Math Research Scheduling Protocol V2

Status: `ACTIVE / CANONICAL CONTROL PLANE / V2`
Effective cutover: `2026-08-24T16:00:00+08:00`
Runtime board: GitHub Issue `#240`
Machine: `research_scheduler.json`
Reducer: `tools/research_scheduler.py`
Event helper: `tools/research_scheduler_event.py`

## 1. One control plane

Every research task identity must be visible to Scheduler V2. A taskbook is not allowed to remain invisible merely because it was created or executed outside Issue #240.

The registry is the union of:

- the frozen V1 static registry, retained as historical provenance;
- every task-like artifact under `research_tasks/`;
- V2 `PUBLISH`, `MIGRATE`, and `ORPHAN` events.

A pre-V2 taskbook that is already represented by accepted historical scheduler events keeps that historical runtime meaning. A pre-V2 taskbook that lacks a reliable accepted runtime history is registered as `ORPHANED`, not silently re-dispatched. A V2 task can be created dynamically by `PUBLISH` even before its taskbook is merged to `main`.

## 2. Canonical lifecycle

New work uses:

`PUBLISH -> REVIEW_PENDING -> REVIEW_CLAIM -> APPROVE -> READY -> CLAIM -> IN_PROGRESS -> SUBMIT -> RETURN_REVIEW -> REVIEW_CLAIM -> REVIEW -> DONE`

Return-to-work branches are explicit:

`REVIEW(RETURN_TO_RESEARCH) -> HANDOFF_READY`

Abandonment is explicit:

`CLAIM lease expires -> ORPHANED -> ADOPT -> CLAIMED`

`DONE` is not a valid V2 event. Direct claimant completion is forbidden.

## 3. Publication authority

Researchers, Drivers, and Foundation Stewards may publish a task proposal. Publication never makes the proposal dispatchable.

In particular:

`FREE RESEARCHER PUBLISH -> REVIEW_PENDING`, never `READY`.

A dispatchable task requires a current cross-Driver publication review and an immutable Driver-approved taskbook ref. The publisher may not approve the same task.

## 4. Cross-Driver review

All V2 publication approvals and execution-return reviews require a review lease:

`REVIEW_CLAIM -> APPROVE/REJECT` or `REVIEW_CLAIM -> REVIEW`.

The state machine rejects:

- publisher reviewing the same publication;
- executor reviewing the same return;
- unclaimed review verdicts.

`REVIEW` routes work. It is not theorem truth or canonical source promotion.

## 5. Orphan ledger

An orphan is a first-class state, not a hidden lease reset. The durable record retains the task ID, reason, prior claim/execution identity, last progress ref, next action, time, and recovery/evidence ref when available.

An `ORPHANED` task cannot be ordinary-claimed. Recovery must use `ADOPT` with a recovery ref.

Taskbooks found outside the old static scheduler are registered as orphans unless valid pre-V2 runtime history or a V2 event explains their state.

## 6. V1 retirement

Historical `ENTERPRISE_MATH_SCHEDULER_EVENT_V1` events before the cutover remain replayable. V1 events at or after cutover are ignored. New work must use `ENTERPRISE_MATH_SCHEDULER_EVENT_V2`.

Historical V1 `DONE` remains historical completion authority only. It does not create a V2 self-completion path.

## 7. Normal user/agent operations

Use the reducer rather than guessing state:

```bash
python tools/research_scheduler.py validate
python tools/research_scheduler.py registry --events events.jsonl
python tools/research_scheduler.py select --events events.jsonl --kind ANY
python tools/research_scheduler.py select-review --events events.jsonl --reviewer-id EM-DVR-XXXXXX
```

Use the event helper rather than hand-writing event JSON:

```bash
python tools/research_scheduler_event.py publish-taskbook research_tasks/TASK.md --taskbook-ref research_tasks/TASK.md@<sha> --publisher-id <ID> --publisher-role RESEARCH_DRIVER --at <ISO8601>
python tools/research_scheduler_event.py publish-proposal --task-id <TASK> --title <TITLE> --publisher-id <ID> --publisher-role RESEARCHER --frontier <F> --next-action <N> --at <ISO8601>
python tools/research_scheduler_event.py review-claim --task-id <TASK> --reviewer-id <DRIVER> --review-claim-id <ID> --at <ISO8601>
python tools/research_scheduler_event.py claim --task-id <TASK> --execution-id <ID> --claim-id <ID> --at <ISO8601>
python tools/research_scheduler_event.py submit --task-id <TASK> --execution-id <ID> --claim-id <ID> --return-ref <path@sha> --at <ISO8601>
```

The emitted JSON object is appended as one Issue #240 comment.

## 8. Generic intents

A generic request to claim research work means: materialize the current V2 registry, select the highest eligible `NEEDS_DISPATCH` task, claim it, resolve identity, and start.

A generic Driver request to claim a review means: select the highest eligible `NEEDS_REVIEW` item that is not self-review, claim the review lease, and start.

The user is not the routing bus and does not need to copy task IDs or return payloads between conversations.

## 9. Migration-only event

`MIGRATE` is Driver-only and exists solely to import work already live outside V2 at cutover. It requires an exact migration ref and target state. It must not be used to bypass normal publication or cross-review for post-cutover tasks.

## 10. Truth boundary

`SCHEDULER_DONE != THEOREM_TRUTH`.

`REVIEW_DONE != CANONICAL_MAIN`.
