# Driver Review Automatic Follow-up

Status: `CONTROL-PLANE HARDENING / NO NEW MATHEMATICS`

## Problem closed by this policy

The old ordinary result path allowed

```text
FROZEN RESULT -> TERMINAL DRIVER REVIEW -> TASK TERMINAL
```

without proving that the Driver had materialized the next executable work under
the still-open parent Objective. That made a Driver stall machine-legal: the
review could be correct, the task could be terminal, and yet no next taskbook
existed.

The new post-cutover path is:

```text
FROZEN RESULT
    -> DRIVER REVIEW
    -> FOLLOW-UP GATE MATRIX
    -> IMMUTABLE NEXT TASKBOOK / TASKSET PUBLICATION
       OR CANONICAL PARENT OBJECTIVE CLOSED
    -> TASK TERMINAL
    -> REEVALUATE PARENT
```

A missing follow-up packet keeps the reviewed result nonterminal. The ordinary
dispatch projection therefore remains in `AWAITING_REVIEW`; it cannot disappear
into `DONE`.

## What "automatic" means

The Driver does not merely write prose saying "next do X". In the same review
subflow the Driver supplies one machine-readable follow-up specification and runs:

```text
python research_driver_followup.py materialize \
  --review-id <DR-...> \
  --spec <followup-spec.json>
```

The materializer preflights the gate decisions and taskbooks, publishes the
taskbook(s) through the existing immutable V2 publication mechanism, and then
writes one immutable follow-up packet pinning those exact publication IDs.

If the parent Objective is genuinely complete, the zero-task exception is
allowed only after the canonical Objective head is already `CLOSED`.

## Mandatory gate matrix

Every governed Driver review explicitly decides all of:

1. `MATHEMATICAL_CONTINUATION`
2. `LEAN_FORMALIZATION`
3. `EXTERNAL_PRIOR_ART_DUPLICATION`
4. `INDEPENDENT_REPLICATION`
5. `INTEGRATION_OR_TOOL_HARVEST`
6. `ADVERSARIAL_AUDIT`

Each gate is exactly one of:

- `REQUIRED` — publish at least one task with the matching role;
- `SATISFIED_BY_REVIEWED_RESULT` — pin exact evidence refs showing the reviewed
  package already closed the gate;
- `NOT_REQUIRED` — give a nonempty task-specific reason.

Additional hard rules:

- every `ACCEPTED` result must run or publish external prior-art/duplication work;
- an accepted `L4` destination must run or publish the Lean/formalization gate;
- a tool-bearing result must run or publish integration/tool-harvest work;
- `REQUEST_REPLICATION` must publish an independent-replication task.

The gate list is deliberately extensible by a later contract generation, but a
review may not silently omit a gate from the current exact set.

## Lean tasks

A Lean follow-up should pin the accepted theorem/result and must state the exact
formal target. When full formal closure is required, the taskbook should retain
the normal no-`sorry` / no-`admit` / no-custom-axiom boundary, warning-fatal
build/check command, theorem-source blob provenance and regression guards.

If the reviewed result is already fully Lean-checked, the Driver does **not**
publish a pointless second Lean task. It marks `LEAN_FORMALIZATION` as
`SATISFIED_BY_REVIEWED_RESULT` and pins the existing theorem/build evidence.

## External prior-art / duplication tasks

An accepted result may not turn "we did not search" into an implicit novelty
claim. The external task should at minimum record:

- search date and search surfaces;
- task-specific queries;
- candidate papers/repos/results;
- exact duplicate vs partial antecedent vs adjacent method vs no material match;
- source links/identifiers sufficient for audit.

"No material match found" is evidence about the search, not a theorem of
novelty.

## Relation to the successor gate

This policy does **not** repeal:

```text
PASS_OR_DONE_IS_NOT_ITSELF_A_SUCCESSOR_TRIGGER
```

A Driver review now has a duty to materialize the next control action, but every
new task whose semantics are `CONTINUATION` still must pass the existing
`successor_gate`:

- genuine new information gap;
- why the parent result does not close it;
- discriminating outcomes;
- kill condition;
- alternative route/free exploration considered;
- why a new stage/task is better than closure or continuing the same task.

This prevents the anti-stall rule from becoming an infinite "PASS -> invent
another stage" generator.

## Revision and negative-result behavior

A nonterminal review still needs an explicit next control action. A revision can
be published as a new immutable generation of the same task using an explicit
`supersedes_publication_id` and a new taskbook path. A rejected/no-go result under
an open parent Objective normally publishes the alternative route, adversarial
audit, replication, or other concrete next task selected by the Driver.

## Parallel results

Terminal parallel synthesis does not bypass this barrier. If a reviewed result
inside the terminal evidence set is post-cutover and its follow-up packet is
missing/invalid, the task remains nonterminal until the review follow-up is
materialized.

## Compatibility

Reviews before `2026-08-27T09:19:00+00:00` are historical immutable evidence and
are not retroactively forced to create tasks. New reviews at or after the
cutover are governed.

This timestamp is a compatibility bridge, not the final actor-authentication
design. The separate active-Driver-authorization hardening should eventually
replace timestamp-only cutover classification with source-backed Driver
authority.

## Core invariant

```text
DRIVER_REVIEW_COMPLETE
!=
CONTROL_LOOP_CONTINUATION_COMPLETE

POST_CUTOVER_DRIVER_REVIEW
-> FOLLOWUP_TASKSET_READY_OR_PARENT_OBJECTIVE_CLOSED
-> TASK_TERMINAL
```
