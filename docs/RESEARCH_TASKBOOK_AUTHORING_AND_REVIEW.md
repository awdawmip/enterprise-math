# Enterprise Math Research Taskbook Authoring and Review

Status: `ACTIVE / CANONICAL TASKBOOK AUTHORING PROCESS / V4`
Effective: `2026-08-24`
Contract: `research_taskbook_contract.json`
Policy set: `research_taskbook_policy.json`
Runtime control plane: `research_scheduler.json`
Runtime protocol: `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md`

## 1. Layer separation

A taskbook is the task-specific execution contract. It is not a runtime claim, a fixed researcher identity, a scheduler state, a review lease, theorem truth, or canonical promotion authority.

Freeze:

`TASKBOOK_POLICY_REVIEW_PASS != SCHEDULER_READY`.

The layers are:

`TASKBOOK CONTENT -> POLICY REVIEW -> PUBLISH -> CROSS-DRIVER APPROVAL -> CLAIM -> EXECUTION -> SUBMIT -> CROSS-DRIVER RETURN REVIEW`.

## 2. Required origin and lineage

Every new taskbook declares `origin_kind` and `task_lineage` according to `research_taskbook_contract.json`.

A FREE-derived task preserves its audited candidate provenance. A continuation preserves parent identity and a complete successor gate. Stage numbering, momentum, or parent PASS does not justify a successor.

## 3. Authoring

Use:

```bash
python tools/research_taskbook.py new ...
```

Then write only task-local mother question, frozen inputs/scope, required outputs, PASS/KILL/return criteria, and any narrow temporary override.

Do not copy generic scheduler, GitHub, identity, liveness, promotion, Working Truth, or successor policy into the task body.

## 4. Policy review

Run:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md --approve
python tools/research_taskbook.py audit research_tasks/<task>.md --dispatch
```

The policy digest is computed from `research_taskbook_policy.json`. Scheduler V2 is a policy input. When the scheduler contract changes, old taskbook stamps become stale before redispatch.

## 5. Publication is mandatory

A taskbook PASS does not create a live queue item by itself.

After the taskbook has an immutable repository ref, publish it to Scheduler V2:

```bash
python tools/research_scheduler_event.py publish-taskbook \
  research_tasks/<task>.md \
  --taskbook-ref research_tasks/<task>.md@<commit-sha> \
  --publisher-id <ID> \
  --publisher-role RESEARCH_DRIVER \
  --at <ISO8601>
```

Append the emitted JSON as one Issue #240 comment.

The result is `REVIEW_PENDING`, never `READY`.

## 6. Cross-Driver publication approval

A different Driver claims the publication review and either approves or rejects it. The state machine rejects publisher self-review.

Only `APPROVE` with an immutable Driver-approved taskbook ref creates runtime `READY`.

Manual chat relay may transport the packet, but cannot bypass `PUBLISH -> REVIEW_CLAIM -> APPROVE`.

## 7. FREE researcher publication

FREE Phase A remains outside automatic task dispatch. But a FREE researcher may publish a concrete proposed task without pretending it is already Driver-approved:

```bash
python tools/research_scheduler_event.py publish-proposal ... --publisher-role RESEARCHER ...
```

This creates `REVIEW_PENDING`. It grants no Working Truth and no dispatch authority. Driver taskbook authoring/intake and cross-Driver approval remain necessary before `READY`.

## 8. Runtime identity

Taskbooks remain free of fixed runtime `researcher_id`, `driver_id`, and `execution_id`.

Runtime identity is bound by V2 `CLAIM` or `ADOPT`. Direct/manual identity allocation remains a transport fallback but must be reflected in the state machine.

## 9. Completion and review

Execution never closes with V2 `DONE`.

The executor emits `SUBMIT` with an immutable return ref. Scheduler state becomes `RETURN_REVIEW`.

A different Driver obtains `REVIEW_CLAIM` and emits `REVIEW`. The executor cannot review their own return.

Accepted routing verdicts may close the scheduler task, return it to research, park it, route it onward, or reject it. Scheduler completion is not automatic theorem truth or source promotion.

## 10. Orphans

Any taskbook discovered outside the live V2 registry is visible as `ORPHANED` unless pre-V2 runtime history or an explicit migration event explains it.

Lease expiry also creates `ORPHANED` with durable provenance. An orphan resumes via `ADOPT`, not ordinary `CLAIM`.

## 11. Correct current flow

`new/edit -> policy review -> audit PASS -> PUBLISH -> different Driver APPROVE -> CLAIM -> work -> SUBMIT -> different Driver REVIEW`.

This is the only normal post-cutover dispatch path.
