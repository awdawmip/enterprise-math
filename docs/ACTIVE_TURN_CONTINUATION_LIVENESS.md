# Enterprise Math Active-Turn Continuation Liveness

Status: `ACTIVE / CANONICAL EXECUTION-LIVENESS CONTRACT / CANDIDATE UPDATE`
Effective: `2026-08-25`
Scope: `FREE_AXIOM_DISCOVERY / TASK_RESEARCH / RESEARCH_DRIVER / FOUNDATION_STEWARD / GitHub-publication subflows / cross-conversation recovery`

## Core invariant

Maintain an explicit execution stack:

`PARENT_USER_OBJECTIVE -> CURRENT_SUBFLOW -> NEXT_EXECUTABLE_ACTION`.

Freeze:

`SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE`.

`DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN`.

`STALE_CONVERSATION != WAITING_WORKER`.

`BEFORE_NEW_EXECUTION_GENERATION -> RECONCILE_DURABLE_FRONTIER`.

A model must not require the user to send `继续`, `continue`, `完成了`, or an equivalent wake-up message when that message supplies no new information and the next action is already determined by the current objective and evidence.

A model must also not keep an open parent objective blocked merely because an earlier conversation appears to be executing it. Once that conversation has produced no new **verifiable action** for 10 continuous minutes, recovery is from durable state, not from trust in the old chat.

## What counts as verifiable liveness

The liveness clock is refreshed by a new externally checkable action that materially advances the objective, for example:

- a new tool or compute result;
- a branch, commit, PR, issue comment, taskbook, return, execution stamp or checker/build result;
- a validated state-machine transition;
- a resume-capable checkpoint with an explicit next action.

The following do **not** refresh verified liveness:

- progress prose by itself;
- saying that work will continue;
- passive waiting;
- repeating an earlier result;
- asserting that another conversation is still working without new evidence.

Progress text is observability. It is never a lease heartbeat by itself.

## Durable frontier

A **durable frontier** is the newest externally verifiable state from which a replacement conversation can resume without trusting stale chat claims.

Preferred sources, in order of usefulness, are:

1. owner branch + commit SHA;
2. taskbook `path@immutable-source-sha`;
3. frozen `research_return` / evidence artifact;
4. PR state and changed-file set;
5. accepted Scheduler Issue #240 event;
6. execution stamp or semantic checkpoint;
7. persisted checker/build/test evidence tied to source refs.

Conversation-local scratch reasoning, uncommitted edits and assistant progress messages are **not** sufficient durable frontiers.

Operationally, do not carry more than one meaningful semantic phase exclusively inside a conversation. At phase boundaries, persist reusable evidence and a concrete next action whenever a write path is available.

## Pre-execution frontier reconciliation

Before creating a new researcher execution identity, owner branch, execution stamp, Scheduler `CLAIM`, Scheduler `ADOPT`, or direct rerun for an existing exact task, reconstruct its durable frontier first. This is a narrow task-specific intake check, not a universal repository preflight.

Resolve the exact task id, immutable taskbook ref, declared owner branch and expected return/evidence locations, then classify exactly one:

- `VERIFIED_COMPLETE` — durable evidence already satisfies the assigned objective. Consume the frozen result; do not create another execution generation or redo mathematics.
- `IN_PROGRESS_RECOVERABLE` — a valid frontier exists. Resume/ADOPT from it and preserve valid evidence.
- `UNFINISHED` — execution began but the durable result is incomplete. Preserve what is valid and restart only the missing portion.
- `NEVER_STARTED` — no substantive durable execution began. Normal dispatch is allowed.

Freeze:

`VERIFIED_COMPLETE -> CONSUME_NOT_REDISPATCH`.

`IN_PROGRESS_RECOVERABLE -> TAKEOVER_SAME_DURABLE_FRONTIER`.

`UNFINISHED -> RESTART_ONLY_MISSING_WORK`.

`NEVER_STARTED -> NORMAL_DISPATCH`.

A stale conversation or ordinary continuation is not itself a fresh independent replication. Create a new clean independent child only when the controlling independence protocol explicitly requires a distinct run.

For blind/independent work, this intake reconciles status/provenance metadata without reading withheld mathematical content before the declared freeze.

## Cross-conversation stale recovery

If an active conversation has no new verifiable action for **10 continuous minutes**, classify that conversation as stale for control purposes. Do not wait for it to finish and do not ask the user to keep it alive.

Reconstruct the durable frontier, then assign exactly one recovery class:

- `VERIFIED_COMPLETE` — durable evidence proves the assigned objective already completed; consume it and do not redo the work.
- `IN_PROGRESS_RECOVERABLE` — a valid branch/checkpoint/frontier exists and the remaining step can be resumed.
- `UNFINISHED` — execution began, but the durable frontier is incomplete or insufficient; preserve valid evidence and restart only the missing portion.
- `NEVER_STARTED` — dispatch/claim existed but no substantive durable execution began.

For `IN_PROGRESS_RECOVERABLE`, if Scheduler V2 still shows a live task claim, a Driver or SYSTEM may emit an early `ORPHAN` with reason `STALE_CONVERSATION_NO_VERIFIABLE_ACTION_10M` and an evidence/recovery ref, then the recovering execution uses `ADOPT` with a fresh execution identity and `recovery_ref`.

This early stale-conversation orphaning does **not** wait for the ordinary task lease to expire. The ordinary claim lease protects against accidental duplicate dispatch; it is an upper bound on ownership, not a requirement to wait on a dead chat for its full duration.

Freeze:

`10_MIN_STALE_CHAT + RECOVERABLE_DURABLE_FRONTIER -> TAKEOVER_NOW`.

`TASK_LEASE_NOT_EXPIRED != MUST_WAIT_FOR_STALE_CHAT`.

`TAKEOVER -> REBUILD_FROM_DURABLE_FRONTIER`, never `TAKEOVER -> TRUST_OLD_CHAT_SUMMARY`.

## Parent-goal continuation lease

When the user's instruction semantically means `continue`, `keep going`, `do not stop`, `until no further progress`, `until satisfied`, `solve the blocker and continue`, or otherwise defines a multi-step completion criterion, record an implicit:

`CONTINUATION_LEASE = ACTIVE_UNTIL_PARENT_CRITERION_MET_OR_USER_REVOKES`.

A stage, route, checkpoint, PR, publication subflow, conversation stall, or conversation replacement cannot consume that lease.

If one route closes while the parent objective remains open, the controller must evaluate the next highest-leverage executable route in the same turn. It may close the local route without automatically opening a semantic successor, but it must not equate local closure with parent completion.

## Start and checkpoint rule

Before entering a long substantive research phase:

1. resolve the exact task/object and immutable taskbook ref;
2. reconcile its durable frontier and classify `VERIFIED_COMPLETE / IN_PROGRESS_RECOVERABLE / UNFINISHED / NEVER_STARTED`;
3. stop execution setup and consume the result if `VERIFIED_COMPLETE`;
4. otherwise resolve the role/identity for the execution that is actually required;
5. create/bind the earliest supported durable execution stamp or accepted runtime claim plus owner branch/taskbook ref as required;
6. record the first concrete next action.

After a meaningful phase produces reusable evidence, persist the changed knowledge/control facts and next action before moving deep into the next phase whenever possible.

If the conversation fails later, the recovery target is therefore the latest durable phase boundary, not the beginning of the task.

## Non-terminal boundaries

The following are **not** turn-stop conditions by themselves:

- a tool call returning successfully;
- a tool call returning a recoverable error with another supported route available;
- a journal write or semantic checkpoint;
- branch/PR creation or metadata refresh;
- `mergeable`, CI, review, scheduler, or other `PENDING_NONBLOCKING` state;
- a research Stage PASS/FAIL/closure;
- a Driver verdict;
- a progress update to the user;
- publication completion;
- one route becoming locally blocked while independent/downstream-safe work remains;
- a predecessor conversation becoming stale when durable recovery is possible.

After any such boundary, return immediately to the parent objective and execute the next available action in the same turn or recovering conversation.

## Stage and Driver rule

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER` remains binding.

However:

`STAGE_TERMINAL_VERDICT -> SAME_TURN_SUCCESSOR_GATE_EVALUATION`.

The Driver must immediately decide one of:

- continue the same task;
- open a justified successor under the successor gate;
- close the route and move to another selected portfolio action;
- return to FREE exploration when that is the best information-producing move;
- conclude the parent user objective if its actual completion criterion is met.

Do not stop merely after writing “no next Stage opened”.

For stale recovery, the Driver also owns the control-plane act of releasing a still-live Scheduler claim when the 10-minute stale condition is evidenced. This is recovery governance, not mathematical authorship.

## Remote/tool rule

`REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED`.

`CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK`.

`CHECKPOINT_PERSISTED -> RESUME_PARENT_TASK`.

`TOOL_RESULT_RECEIVED -> RESUME_PARENT_TASK`.

`OTHER_CONVERSATION_APPEARS_RUNNING + 10_MIN_NO_VERIFIABLE_ACTION -> REBUILD_DURABLE_FRONTIER_AND_RECOVER`.

When a tool path fails but a supported alternative exists, switch to that route without waiting for user confirmation unless authorization/safety requires it.

## Allowed terminal conditions

A turn may stop only when at least one holds:

1. the current parent user objective is actually complete;
2. the user explicitly asked to stop, pause, review only, or wait for their next instruction;
3. no executable next step remains within current capabilities because a genuine safety, authorization, missing-user-data, or unavoidable external-event dependency blocks the parent objective;
4. a platform/tool limit makes further action impossible in the current turn.

Before using 3 or 4, exhaust independent/downstream-safe work and return the strongest current result. Do not output a passive `WAITING_FOR_CONTINUE` or `WAITING_FOR_OTHER_CONVERSATION` state when recovery is possible.

## User-visible liveness

Progress updates are observability, not synchronization barriers and not verified-action heartbeats.

After a commentary/progress update, execution continues automatically unless the task is terminal under the conditions above.

For long tool chains, keep the user informed at the normal platform cadence while continuing work. Prefer progress messages that follow a real tool/checkpoint advance so the visible state tracks durable reality.

## Minimal state test

Before starting/restarting an exact task, ask internally:

`WHAT_IS_THE_DURABLE_FRONTIER?`

Then classify it. Do not dispatch until that classification is complete.

Before ending any nontrivial turn, ask internally:

`PARENT_OBJECTIVE_COMPLETE?`

If no:

`IS_THERE_AN_EXECUTABLE_NEXT_ACTION?`

If yes, execute it now.

If no only because another conversation supposedly owns the work:

`HAS_THAT_CONVERSATION PRODUCED A NEW VERIFIABLE ACTION WITHIN 10 MINUTES?`

If no, reconstruct the durable frontier, classify it, release/recover the stale execution as needed, and continue here.
