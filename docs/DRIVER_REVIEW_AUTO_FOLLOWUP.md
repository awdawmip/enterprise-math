# Driver Review Automatic Follow-up

Status: `CONTROL-PLANE HARDENING / V1.4 CANDIDATE / NO NEW MATHEMATICS`

## Problem closed by this policy

The old ordinary result path could legally stop at:

```text
FROZEN RESULT -> TERMINAL DRIVER REVIEW -> TASK TERMINAL
```

while the parent Objective remained open and no next executable work had been
materialized.  The review could be mathematically correct while the control loop
silently stalled.

After exact-set Driver-review authority, the governing path is:

```text
FROZEN RESULT
    -> 0 / 1 / MANY IMMUTABLE SOURCE REVIEWS
    -> OPERATIONAL REVIEW AUTHORITY
       0 reviews : none
       1 review  : that immutable review
       2+ reviews: exact set -> intake -> RP1 -> RP2 -> review synthesis
    -> FOLLOW-UP GATE MATRIX
    -> IMMUTABLE NEXT TASKBOOK / TASKSET PUBLICATION
       OR CANONICAL PARENT OBJECTIVE CLOSED
       OR SATISFIED TASK CLOSED WITH PORTFOLIO CONTINUATION
    -> TASK TERMINAL OR RETURN TO EXECUTION
    -> REEVALUATE PARENT
```

A missing or invalid follow-up packet keeps the operational review authority
nonterminal.  Ordinary dispatch therefore remains review-visible rather than
disappearing into `DONE`.

## Review authority comes before follow-up

Follow-up never consumes `reviewed_at`, `latest_review`, or the last source
review written.

For one source review, that review is immediately the operational authority and
may perform the follow-up transaction.

For a second or later source review, the canonical review command **does not**
publish a source-review-specific successor.  The new review changes the exact
review set and reopens review authority.  Only after both reference passes and a
review synthesis may the synthesis authority materialize follow-up.

This prevents an additional reviewer from winning merely by writing later.

A review synthesis must also have a single operational destination class because
Lean/Foundation/Tool/Replication routing depends on it.  An explicit synthesized
destination is accepted.  Otherwise every source review must agree on one
destination.  Mixed unresolved destinations fail closed.

## What “automatic” means

### First review

The first immutable review is immediately authoritative, so the canonical
command requires a follow-up specification:

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
decisions and every proposed taskbook.  After the review record is created it
materializes the selected decision and freezes one authority follow-up packet.
Only `TASK_SET_PUBLISHED` publishes new taskbooks through immutable V2 publication.

### Second or later review

A second or later immutable review is written without `--followup-spec`:

```text
python tools/research_result_records.py review ...
```

The command records the new evidence and returns the control state
`DEFERRED_UNTIL_EXACT_REVIEW_SYNTHESIS`.  The review exact-set flow must then
complete before follow-up can be materialized.

### Synthesis authority / crash recovery

Once an operational review authority exists, recovery or post-synthesis
materialization uses:

```text
python research_driver_followup_guard.py materialize \
  --review-authority-id <review-or-synthesis-authority-id> \
  --spec <followup-spec.json>
```

An incomplete transaction does not make the authority terminal.
`PARENT_OBJECTIVE_CLOSURE` still requires an already `CLOSED` canonical Objective
head. The distinct completed-Task decision below leaves the parent unclosed.

## Completed Task: return to the existing portfolio

`TASK_SCOPE_CLOSURE_PORTFOLIO_CONTINUATION` creates no new Task. It is available
only to an `ACCEPTED` operational Driver review of a current-publication `PASS` or `SUCCESS` Result
whose exact `hard_target_disposition` is `SATISFIED`. `terminal_scope: TASK`
belongs to the Driver packet, not the historical Result. Incomplete, partial,
negative-boundary, activity-only and non-accepted returns cannot use this route.

All six gates retain their existing rules and evidence requirements. No gate
may remain `REQUIRED`; use a real taskset for a gate that needs new work.
For a fully satisfied Task, the follow-up spec has `tasks: []` and these fields
in addition to the complete `gate_decisions` matrix:

```json
{
  "decision": "TASK_SCOPE_CLOSURE_PORTFOLIO_CONTINUATION",
  "terminal_scope": "TASK",
  "tasks": [],
  "portfolio_continuation": {
    "source_result_id": "<current RR>",
    "parent_objective_id": "<source publication parent>",
    "action": "REEVALUATE_CANONICAL_PORTFOLIO",
    "dispatcher": "research_control_dispatch.py",
    "next_action": "Read fresh canonical events and session observations, then run the canonical dispatcher for the existing portfolio.",
    "remaining_parent_scope": ["<specific unresolved parent scope>"],
    "evidence_refs": ["<immutable source locating that unresolved scope>"]
  }
}
```

The existing first-review command and recovery materializer both validate the
same typed decision. The immutable packet pins the current Result file digest,
source publication, operational review authority and exact recommendation.
Candidate checks, exactly one packet per authority, active Driver checks,
post-write source checks and rollback rules remain in force. Publish a generated
review and its packet atomically to main; this decision generates no TP2 record.
The current publication check applies to first-review preflight and both sides
of the write transaction. Later publication generations do not invalidate an
immutable historical packet whose own Result/review/source pins remain intact.

The packet records the actual parent status at materialization as `OPEN`,
`PARKED`, or `ABSENT_NOT_CLOSED`. Absence never creates a parent record or proves
closure. This frozen observation grants no live parent status; subsequent
Objective updates do not reopen the completed Task. The live parent state must
still be evaluated independently.

Public Result runtime may now be terminal at `TASK` scope with
`TASK_SCOPE_CLOSED_PORTFOLIO_CONTINUATION`. It grants no parent completion, parent
final, Working Truth, Foundation, promotion, claim or selected-task authority.
Run `python research_control_dispatch.py` with current events and observations;
do not manufacture a successor or reuse a stale claim. An open parent with
executable work still has `final_allowed=false` under active-turn liveness.

## Mandatory gate matrix

Every governed operational review authority explicitly decides all of:

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
- `SATISFIED_BY_EXISTING_CONTROL_ASSET` — pin an already-materialized current
  task/control asset instead of duplicating it;
- `NOT_REQUIRED` — give a nonempty task-specific reason.

Additional hard rules:

- an `ACCEPTED` authority must satisfy or publish external prior-art/duplication
  work;
- an accepted `L4` destination must satisfy or publish Lean/formalization work;
- a tool-bearing result must satisfy or publish integration/tool-harvest work;
- `REQUEST_REPLICATION` must publish or pin an existing independent replication
  control asset.

The gate list may evolve only through a later contract generation.

## Lean tasks

A Lean follow-up pins the accepted theorem/result and the exact formal target.
When full formal closure is required, normal no-`sorry`, no-`admit`,
no-custom-axiom, warning-fatal build, theorem-source blob and regression guards
remain binding.

If the reviewed package is already fully Lean-checked, the authority does not
publish a pointless duplicate task; it marks the gate satisfied and pins the
existing theorem/build evidence.

## External prior-art / duplication tasks

An accepted result may not turn “we did not search” into an implicit novelty
claim.  External work should record at least:

- search date and surfaces;
- task-specific queries;
- candidate papers/repos/results;
- exact duplicate vs partial antecedent vs adjacent method vs no material match;
- source identifiers sufficient for audit.

“No material match found” is evidence about a search, not a theorem of novelty.

## Relation to the successor gate

This policy does **not** repeal:

```text
PASS_OR_DONE_IS_NOT_ITSELF_A_SUCCESSOR_TRIGGER
```

The operational review authority must materialize the next control action, but
every `CONTINUATION` task still needs a genuine information gap, discriminating
outcomes, kill condition, alternative-route analysis, and justification for a
new task rather than closure or same-task continuation.

A concurrent already-materialized route should be pinned with
`SATISFIED_BY_EXISTING_CONTROL_ASSET`, not duplicated.

## Revision and negative-result behavior

A nonterminal authority still needs an explicit next control action.  Revision
may publish a new immutable generation of the same task using an explicit
`supersedes_publication_id` and a new taskbook path.  A rejected/no-go result
under an open parent Objective normally routes to an alternative, adversarial
audit, replication, or another concrete action selected by the authority.

## Parallel results

Parallel-result control is downstream of per-result review and follow-up
authority:

```text
Result A -> review exact-set authority A -> follow-up A ready
Result B -> review exact-set authority B -> follow-up B ready
...
             |
             v
parallel-result intake -> RP1 -> RP2 -> result synthesis
```

If any source result lacks resolved review authority, the task is
`AWAITING_RESULT_REVIEW_AUTHORITY`.

If review authority is resolved but its governed follow-up is not ready, the task
is `AWAITING_RESULT_REVIEW_FOLLOWUP`.

Only after both layers are ready may the existing exact-set parallel-result
synthesis become operational.  Thus neither a result synthesis nor a later
source review can bypass the continuation barrier.

## Frozen compatibility boundary

Legacy exemption is **not** determined by `reviewed_at`.

The exact cutover is frozen in:

```text
research_driver_followup_legacy_reviews.json
```

with:

```text
main = d1514b1ea2f3f6f91c3b793c8d0bcb618ce093c6
physical review tree = a37d1b9c1fdc550ea8652fa81bc6497b6082724a
```

The physical review tree contains 28 immutable historical review records.  The
canonical active compatibility view at cutover contains 27.  The excluded record
is:

```text
DR-E3CE51B969E032E59500
```

It belongs to the quarantined structurally invalid historical PCF4 chain.  Its
bytes remain immutable history, but the auto-followup cutover must not re-admit
it as operational review authority.

Exactly the 27 review IDs visible through the canonical active review view at
cutover use historical compatibility.  New source reviews cannot backdate
around the barrier, and no review-synthesis authority existed at cutover; every
future synthesis authority is governed.

## Core invariant

```text
SOURCE_REVIEW_WRITTEN
!=
OPERATIONAL_REVIEW_AUTHORITY_RESOLVED

DRIVER_REVIEW_AUTHORITY_COMPLETE
!=
CONTROL_LOOP_CONTINUATION_COMPLETE

OPERATIONAL_REVIEW_AUTHORITY
-> FOLLOWUP_TASKSET_READY_OR_PARENT_OBJECTIVE_CLOSED_OR_TASK_SCOPE_PORTFOLIO_CONTINUATION
-> TASK_TERMINAL_OR_RETURN_TO_EXECUTION
```
