# Enterprise Math Active-Turn Continuation Liveness

Status: `ACTIVE / CANONICAL EXECUTION-LIVENESS CONTRACT / V2`
Effective: `2026-08-25`
Scope: `FREE_AXIOM_DISCOVERY / TASK_RESEARCH / RESEARCH_DRIVER / FOUNDATION_STEWARD / GitHub-publication subflows`
Executable evaluator: `tools/active_turn_liveness.py`

## Core invariant

Maintain an explicit execution stack:

`PARENT_USER_OBJECTIVE -> CURRENT_SUBFLOW -> NEXT_EXECUTABLE_ACTION`.

Freeze:

`SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE`.

`DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN`.

`PARENT_INCOMPLETE + EXECUTABLE_NEXT_ACTION -> FINAL_FORBIDDEN`.

The last rule is **independent of continuation-lease state**. A user does not need to have said `继续` for base liveness to apply. The continuation lease strengthens persistence across multi-step boundaries; it is not the prerequisite for continuing ordinary unfinished work.

A model must not require the user to send `继续`, `continue`, `完成了`, or an equivalent wake-up message when that message supplies no new information and the next action is already determined by the current objective and evidence.

## Canonical PRE_FINAL guard

Before ending any nontrivial turn, evaluate the canonical state using the decision semantics implemented in:

`tools/active_turn_liveness.py`.

The evaluator returns exactly one of:

- `FINAL_ALLOWED`;
- `FINAL_ALLOWED_WITH_BLOCKER`;
- `FINAL_ALLOWED_WITH_LIMIT`;
- `EXECUTE_NEXT_ACTION`;
- `SWITCH_STRATEGY`;
- `RECOMPUTE_PARENT_STATE`;
- `CONTROL_STATE_INCONSISTENT`.

Only the first three permit a final response.

The PRE_FINAL decision order is:

1. if the parent objective is complete -> `FINAL_ALLOWED`;
2. if the user explicitly requested stop/pause/review-only/wait -> `FINAL_ALLOWED`;
3. if one or more executable next actions exist -> final is forbidden;
4. if the selected action repeated without any state change, do not retry it unchanged: switch to a supported alternative when one exists, otherwise recompute parent routing once;
5. a parent-level blocker or platform/tool limit permits final only after all independent/downstream-safe work is exhausted and no executable next action remains;
6. if the parent remains incomplete, no executable action exists, no terminal blocker exists, and a parent-state recomputation changes nothing -> `CONTROL_STATE_INCONSISTENT` rather than silent termination or infinite retry.

## Blocked subflow is not blocked parent

Freeze:

`BLOCKED_SUBFLOW != BLOCKED_PARENT`.

A single reproduction route, PR, CI run, reviewer, unavailable helper, or other subflow can be blocked while the parent objective remains executable through another route.

A blocked subflow becomes a terminal parent blocker only when:

`NO_EXECUTABLE_INDEPENDENT_OR_DOWNSTREAM_SAFE_WORK_REMAINS`.

Therefore:

`LOCAL_BLOCK + OTHER_EXECUTABLE_WORK -> EXECUTE_NEXT_ACTION`.

## Loop-safety

The liveness contract must not repair premature stopping by creating infinite retries.

Freeze:

`IDENTICAL_ACTION + IDENTICAL_STATE + NO_PROGRESS -> DO_NOT_REPEAT_UNCHANGED`.

Transition rules:

- supported alternative exists -> `SWITCH_STRATEGY`;
- no alternative selected yet -> `RECOMPUTE_PARENT_STATE` once;
- recomputation leaves the same parent state and no alternative/blocker appears -> `CONTROL_STATE_INCONSISTENT`.

A repeated no-progress action has zero automatic identical retries under this guard.

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

The lease is **not** required for the base rule `unfinished parent + executable action -> continue`. It only makes the persistence condition explicit across multiple local completion boundaries.

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
3. no executable next step remains within current capabilities because a genuine safety, authorization, missing-user-data, or unavoidable external-event dependency blocks the **parent** objective, and independent/downstream-safe work has been exhausted;
4. a platform/tool hard limit makes **all** further action impossible in the current turn after independent/downstream-safe work has been exhausted.

Before using 3 or 4, exhaust independent/downstream-safe work and return the strongest current result. Do not output a passive `WAITING_FOR_CONTINUE` state.

## User-visible liveness

Progress updates are observability, not synchronization barriers.

After a commentary/progress update, execution continues automatically unless the task is terminal under the conditions above.

For long tool chains, keep the user informed at the normal platform cadence while continuing work.

## Regression contract

The repository tests must cover at least these cases:

- parent incomplete + executable next action + **no continuation lease** -> `EXECUTE_NEXT_ACTION`;
- parent incomplete + executable next action + active continuation lease -> `EXECUTE_NEXT_ACTION`;
- checkpoint/PR/journal/Driver verdict does not create terminal state by itself;
- blocked subflow + other executable work -> continue;
- true parent blocker + no remaining executable safe work -> `FINAL_ALLOWED_WITH_BLOCKER`;
- hard platform/tool limit + no remaining executable safe work -> `FINAL_ALLOWED_WITH_LIMIT`;
- explicit user stop -> `FINAL_ALLOWED`;
- repeated identical no-progress action + alternative -> `SWITCH_STRATEGY`;
- repeated identical no-progress action + no alternative -> one `RECOMPUTE_PARENT_STATE`;
- same state after that recomputation -> `CONTROL_STATE_INCONSISTENT`.

## Enforcement boundary

This repository contract and helper are the canonical Enterprise Math control-plane evaluator and regression guard. They can be invoked directly where a local checkout/runtime is available, or their decision table can be implemented by the caller.

They do **not** by themselves intercept the ChatGPT product runtime. A product/runtime caller must invoke or faithfully implement the same PRE_FINAL decision in order to physically block a final response. Do not claim runtime enforcement merely because the repository test passes.
