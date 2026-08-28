# Driver Review Automatic Follow-up

Status: `CONTROL-PLANE HARDENING / V1.3 CANDIDATE / NO NEW MATHEMATICS`

## Problem closed by this policy

The old ordinary result path allowed

```text
FROZEN RESULT -> TERMINAL DRIVER REVIEW -> TASK TERMINAL
```

without proving that the Driver had materialized the next executable work under
the still-open parent Objective. That made a Driver stall machine-legal: the
review could be correct, the task could be terminal, and yet no next taskbook
existed.

The new path is:

```text
FROZEN RESULT
    -> DRIVER REVIEW
    -> FOLLOW-UP GATE MATRIX
    -> IMMUTABLE NEXT TASKBOOK / TASKSET PUBLICATION
       OR CANONICAL PARENT OBJECTIVE CLOSED
    -> TASK TERMINAL
    -> REEVALUATE PARENT
```

A missing or invalid follow-up packet keeps the reviewed result nonterminal. The
ordinary dispatch projection therefore remains in `AWAITING_REVIEW`; it cannot
disappear into `DONE`.

## What "automatic" means

The canonical Driver review command itself carries the follow-up specification:

```text
python tools/research_result_records.py review \
  --result-id <RR-...> \
  --driver-id <EM-DVR-...> \
  --disposition <...> \
  --review-path <driver review markdown> \
  --destination-class <...> \
  --followup-spec <followup-spec.json>
```

Before writing the immutable review, the command preflights the six gate
decisions and every proposed taskbook. After the review record is created it
immediately publishes the follow-up taskbook(s) through the immutable V2 task
publication mechanism and freezes one follow-up packet pinning the exact
publication IDs.

If a process dies after the immutable review write but before the follow-up
transaction finishes, recovery uses:

```text
python research_driver_followup_guard.py materialize \
  --review-id <review-id> \
  --spec <followup-spec.json>
```

That recovery path does not make an incomplete review terminal; the result stays
in `AWAITING_DRIVER_REVIEW` until the packet is valid.

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

The gate list may evolve only through a later contract generation; a review may
not silently omit a current gate.

## Lean tasks

A Lean follow-up pins the accepted theorem/result and states the exact formal
target. When full formal closure is required, the taskbook retains the normal
no-`sorry` / no-`admit` / no-custom-axiom boundary, warning-fatal build/check
command, theorem-source blob provenance and regression guards.

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

Terminal parallel synthesis does not bypass governed result reviews. Existing
parallel-evidence validation already requires at least one review per result
before a multi-result terminal synthesis; if any governed latest review inside
the terminal evidence set lacks its follow-up packet, task terminality is
revoked until the packet is materialized.

A future synthesis-specific checkpoint can harden the separate case where an
entirely new synthesis is performed only over legacy-reviewed evidence. That is
not allowed to weaken the present per-review barrier.

## Frozen compatibility boundary

Legacy exemption is **not** determined by `reviewed_at`.

The exact pre-policy review-ID set is frozen in:

```text
research_driver_followup_legacy_reviews.json
```

It is pinned to:

```text
main = 00c3c8143ca38410df7ed0de64158a3d33e3c67b
review tree = 41a57a0c838d944ac61908fcdb200d425ef89b18
```

Only the 12 review IDs present in that baseline use historical reduction. Every
other review is governed, even if a caller writes an old `reviewed_at`. Thus a
new Driver review cannot backdate itself around the follow-up barrier.

## Core invariant

```text
DRIVER_REVIEW_COMPLETE
!=
CONTROL_LOOP_CONTINUATION_COMPLETE

NEW_DRIVER_REVIEW
-> FOLLOWUP_TASKSET_READY_OR_PARENT_OBJECTIVE_CLOSED
-> TASK_TERMINAL
```
