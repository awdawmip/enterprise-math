# Enterprise Math Active-Turn Continuation Liveness

Status: `ACTIVE / CANONICAL EXECUTION-LIVENESS CONTRACT`
Effective: `2026-08-22`
Scope: `FREE_AXIOM_DISCOVERY / TASK_RESEARCH / RESEARCH_DRIVER / FOUNDATION_STEWARD / GitHub-publication subflows`

## Core invariant

Maintain an explicit execution stack:

`PARENT_USER_OBJECTIVE -> CURRENT_SUBFLOW -> NEXT_EXECUTABLE_ACTION`.

Freeze:

`SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE`.

`DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN`.

A model must not require the user to send `继续`, `continue`, `完成了`, or an equivalent wake-up message when that message supplies no new information and the next action is already determined by the current objective and evidence.

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
- one route becoming locally blocked while independent/downstream-safe work remains.

After any such boundary, return immediately to the parent objective and execute the next available action in the same turn.

## Parent-goal continuation lease

When the user's instruction semantically means `continue`, `keep going`, `do not stop`, `until no further progress`, `until satisfied`, `solve the blocker and continue`, or otherwise defines a multi-step completion criterion, record an implicit:

`CONTINUATION_LEASE = ACTIVE_UNTIL_PARENT_CRITERION_MET_OR_USER_REVOKES`.

A stage, route, checkpoint, PR, or publication subflow cannot consume that lease.

If one route closes while the parent objective remains open, the controller must evaluate the next highest-leverage executable route in the same turn. It may close the local route without automatically opening a semantic successor, but it must not equate local closure with parent completion.

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

## Remote/tool rule

`REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED`.

`CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK`.

`CHECKPOINT_PERSISTED -> RESUME_PARENT_TASK`.

`TOOL_RESULT_RECEIVED -> RESUME_PARENT_TASK`.

When a tool path fails but a supported alternative exists, switch to that route without waiting for user confirmation unless authorization/safety requires it.

## Allowed terminal conditions

A turn may stop only when at least one holds:

1. the current parent user objective is actually complete;
2. the user explicitly asked to stop, pause, review only, or wait for their next instruction;
3. no executable next step remains within current capabilities because a genuine safety, authorization, missing-user-data, or unavoidable external-event dependency blocks the parent objective;
4. a platform/tool limit makes further action impossible in the current turn.

Before using 3 or 4, exhaust independent/downstream-safe work and return the strongest current result. Do not output a passive `WAITING_FOR_CONTINUE` state.

## User-visible liveness

Progress updates are observability, not synchronization barriers.

After a commentary/progress update, execution continues automatically unless the task is terminal under the conditions above.

For long tool chains, keep the user informed at the normal platform cadence while continuing work.

## Minimal state test

Before ending any nontrivial turn, ask internally:

`PARENT_OBJECTIVE_COMPLETE?`

If no:

`IS_THERE_AN_EXECUTABLE_NEXT_ACTION?`

If yes, execute it now.
