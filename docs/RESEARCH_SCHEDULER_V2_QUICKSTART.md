# Enterprise Math Scheduler V2 — Role Quickstart

Status: `ACTIVE / OPERATIONAL QUICKSTART`
Machine contract: `research_scheduler_v2.json`
CLI: `tools/research_scheduler.py`

This file is the shortest operational path for **every** Enterprise Math role that needs to create, review, execute, return, hand off, or recover a task.

## The rule to remember

```text
PUBLISH != READY
RETURN != DONE
ORPHANED != HANDOFF_READY
```

Only the V2 reducer determines runtime state.

## Researcher / TASK_RESEARCH

To execute an existing task:

```text
READY/HANDOFF_READY/CHANGES_REQUESTED
  -> emit-claim
  -> work
  -> emit-progress as meaningful checkpoints occur
  -> emit-handoff if unfinished and deliberately releasing
  -> emit-return when the declared task frontier is complete
```

Never emit V2 `DONE`. After RETURN, a Driver reviews the result.

To propose a genuine new task, author a current-policy taskbook, bring its policy review to PASS, then `emit-publish`. The task is only PUBLISHED until Driver review.

## FREE researcher

Do not use the scheduler to choose the Phase-A question and do not auto-claim tasks.

After candidate freeze + required Phase-B audit/maturity, you may author the derived taskbook and `emit-publish` yourself. You do not need a Driver to write it for you.

Publication gives `PUBLISHED / NEEDS_REVIEW`, not READY.

## Driver

For a published task:

```text
PUBLISHED -> REVIEW stage=DISPATCH
```

Accept -> READY; request changes -> remains PUBLISHED; reject -> REJECTED.

If you were the Driver publisher, another Driver-ID must perform the accepting DISPATCH review.

For a returned task:

```text
RETURNED -> REVIEW stage=RETURN
```

Accept -> DONE; changes requested -> CHANGES_REQUESTED.

Do not accept your own execution return.

For an orphan:

```text
ORPHANED -> RECOVER or REVIEW stage=RECOVERY
```

Preserve orphan history; never rewrite it away.

## Steward

A Steward may publish a mature governance/research task where policy permits, but publication still enters PUBLISHED and cannot bypass Driver dispatch review unless another explicit canonical lifecycle owns that governance state.

## User-originated task

An explicit user task may override automatic task selection. If it becomes a persistent official Enterprise Math task rather than a one-turn direct instruction, register it through PUBLISH or an explicit migration/bootstrap record.

## Event generators

```text
python tools/research_scheduler.py emit-publish --taskbook <path> --publisher-role <ROLE> --publisher-id <ID> --actor <actor>
python tools/research_scheduler.py emit-review --task-id <TASK> --review-stage DISPATCH --verdict ACCEPT --reviewer-id <DRIVER-ID> --review-ref <ref> --actor <actor>
python tools/research_scheduler.py emit-claim --task-id <TASK> --claim-id <claim> --actor <actor>
python tools/research_scheduler.py emit-progress --task-id <TASK> --claim-id <claim> --progress-ref <ref> --next-action <action> --actor <actor>
python tools/research_scheduler.py emit-handoff --task-id <TASK> --claim-id <claim> --progress-ref <ref> --next-action <action> --actor <actor>
python tools/research_scheduler.py emit-return --task-id <TASK> --claim-id <claim> --return-ref <ref> --actor <actor>
python tools/research_scheduler.py emit-orphan --task-id <TASK> --orphan-reason <reason> --discovered-by <ID> --source-ref <ref> --actor <actor>
python tools/research_scheduler.py emit-recover --task-id <TASK> --driver-id <DRIVER-ID> --review-ref <ref> --next-action <action> --actor <actor>
```

Append emitted events to the configured runtime scheduler event log in creation order.

## Before declaring the control plane healthy

Run:

```text
python tools/research_scheduler.py validate
python tools/research_scheduler.py registry-integrity
python -m unittest tests.test_research_scheduler -v
```

`registry-integrity` must report zero executable taskbooks invisible to the scheduler.

## What the state machine does not do

Scheduler `DONE` is workflow completion, not automatic theorem truth, novelty, Foundation admission, or canonical promotion. Those remain separate evidence/promotion questions.
