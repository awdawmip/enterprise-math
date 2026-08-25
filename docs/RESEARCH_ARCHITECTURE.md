# Enterprise Math Research Architecture V2

Status: `ACTIVE / CANONICAL GOVERNANCE / V2.5`
Date: `2026-08-25`
Driver-ID: `EM-DVR-A4319A`
Machine contracts:

- `research_architecture.json`;
- `active_turn_liveness.json`;
- `research_execution_state_machine.json`;
- `research_axiom_candidate_state_machine.json`.

FREE substrate: `definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`
Execution protocol: `docs/RESEARCH_EXECUTION_STATE_MACHINE.md`
Promotion liveness: `docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`

## 1. Four functions

### FREE_AXIOM_DISCOVERY

`PRIMITIVE SUBSTRATE -> RESEARCHER GENERATES ITS OWN QUESTION -> FROZEN CANDIDATE -> PHASE-B AUDIT`.

FREE receives primitive substrate, not the current-achievement catalog or a suggestion/lens menu.

### TASK_RESEARCH

Executes a selected mother question from the user, Driver, scheduler, Foundation intake or audited-candidate transition under one concrete execution lifecycle.

Task authority is not execution readiness. Every run normalizes its authority and task-local gates, resolves identity, and reaches `EXECUTION_READY` before mathematical source reads/derivations.

### RESEARCH_DRIVER

Owns portfolio routing, candidate intake, de-duplication, task creation, Working Truth activation, continuation/closure, execution-review decisions and promotion.

### FOUNDATION_STEWARD

Maintains/verifies shared definitions, interfaces, status and reusable tools; raw discovery is not automatic Foundation input.

## 2. Active-turn execution stack

Every role preserves:

`PARENT_USER_OBJECTIVE -> CURRENT_SUBFLOW -> NEXT_EXECUTABLE_ACTION`.

Freeze:

`SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE`.

`DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN`.

The following do not terminate the parent objective by themselves:

- tool return;
- recoverable tool error with an available alternative;
- semantic checkpoint/journal write;
- Stage verdict or route closure;
- Driver verdict;
- branch/PR/publication boundary;
- `PENDING_NONBLOCKING` state;
- progress update.

When a user instruction establishes open-ended continuation (`continue`, `do not stop`, `until no further progress`, `until satisfied`, `solve blocker and continue`, or equivalent), that continuation lease survives all subflow boundaries until the parent completion criterion is met or the user revokes it.

Detailed current contract:

`docs/ACTIVE_TURN_CONTINUATION_LIVENESS.md`.

## 3. TASK_RESEARCH execution lifecycle

Allowed task-authority kinds:

- `OFFICIAL_TASKBOOK`;
- `DIRECT_USER_TASK`;
- `SCHEDULER_TASK`;
- `DRIVER_DISPATCH_ENVELOPE`.

All normalize to:

`task_id + authority_kind + authority_ref + execution_gates`.

Freeze:

`TASK_AUTHORITY_READY != EXECUTION_READY`.

`STATE_PERMISSION + ALL_GUARDING_GATES_SATISFIED -> ACTION_ALLOWED`.

For an official taskbook, the exact taskbook revision first passes the composite dispatch gate. A direct user task does not require an artificial taskbook; its current task-local constraints are normalized directly into the execution ledger. Scheduler `CLAIMED` is coordination only and never means `EXECUTION_READY`. A Driver envelope cannot waive taskbook gates when it points to a taskbook.

Every declared gate begins `PENDING`; an action listed in `must_precede` is blocked until that gate becomes `SATISFIED` from its required evidence.

A `PRE_MATH` gate blocks both mathematical source reads and derivations. A `PRE_RETURN` gate can still block `RETURN_WRITE` after the run is already `IN_PROGRESS`.

A failed mandatory startup/publication gate is an execution non-start, not a mathematical rejection.

When continuity becomes unreliable, enter `RECOVERY_REQUIRED` and reconstruct the last legal state and gate ledger from durable evidence.

## 4. FREE Phase-A information regime

Freeze:

`FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS`.

`NO_DEFAULT_DISCOVERY_LENS_MENU`.

FREE Phase A loads only the primitive-substrate router, exact primitive files actually needed, relevant protected worldview facts, and necessary integrity/typing rules.

Current task/route/history, downstream achievements, other-branch Working Truth, success/failure catalogs, suggested questions/lens menus, ambient recent-project context, and tool/representation convenience are not discovery priors.

After candidate freeze, current/prior context becomes Phase-B audit/comparison material.

## 5. Candidate lifecycle

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`.

`DISCOVERY_IN_PROGRESS -> BLIND_CANDIDATE_FROZEN -> PHASE_B_AUDIT -> CLASSIFICATION -> DRIVER_INTAKE`.

Tasks created from free discovery preserve candidate origin/ID/audited state.

`TASK_ORIGIN_AND_LINEAGE_CANNOT_BE_ERASED_BY_RENAMING`.

## 6. Working Truth

Working Truth activates only after explicit Driver/taskbook freeze. It is not a FREE Phase-A premise, raw-candidate state or Phase-B dedup prior.

## 7. Stage / successor rule

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

A continuation requires a genuine new information gap, discriminating outcomes, kill condition, and explicit consideration of closure/another owner/free exploration.

Stage 2+ is continuation semantics; renaming does not reset lineage.

But:

`STAGE_TERMINAL_VERDICT -> SAME_TURN_SUCCESSOR_GATE_EVALUATION`.

The Driver immediately evaluates continue-same-task, justified successor, route closure plus another portfolio action, FREE exploration, or parent completion. Local stage/route closure is not automatically parent-goal closure.

## 8. Scheduler / Foundation / portfolio

Scheduler is TASK exploitation infrastructure, not FREE question selection and not an execution-readiness authority.

`SCHEDULER_CLAIMED != EXECUTION_READY`.

Raw discovery does not auto-enter Foundation backflow.

Recent route success is not itself roadmap evidence. No numeric exploration quota is imposed.

## 9. Independence and evidence

A clean blind-discovery claim requires a clean pre-generation context and frozen substrate/worldview snapshot.

`DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE`.

Independent runs do not share candidate packets or a common suggestion menu before freeze.

For TASK independence/replication, a task-local pre-math/source firewall must be encoded as an execution gate and satisfied before the forbidden source read/derivation can occur.

## 10. Read performance

`SMALLEST_SUFFICIENT_ROLE_PACKET > UNIVERSAL_PRELOAD`.

FREE:

`ROLE -> PRIMITIVE SUBSTRATE -> NEEDED PRIMITIVES -> DISCOVERY`.

TASK:

`AGENTS -> EXACT TASK AUTHORITY -> NORMALIZE EXECUTION SPEC -> IDENTITY -> PRE_MATH GATES -> EXECUTION_READY -> FIRST MATHEMATICAL DEPENDENCY -> WORK -> TRIGGERED EXPANSION`.

The soft pre-work read budget applies to control-plane/task-authority reads. It never overrides a task-local pre-math mathematical-source firewall.

## 11. Remote / publication liveness

`REMOTE_SILENT` describes repository activity, not conversational inactivity.

`CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK`.

`CHECKPOINT_PERSISTED -> RESUME_PARENT_TASK`.

`PUBLICATION_COMPLETE -> RESUME_PARENT_TASK`.

GitHub/publication subflows follow the bounded current protocols and then return to the parent objective in the same turn when it remains open.

A task-declared remote `PRE_MATH` publication/liveness gate is different from generic remote preflight: it is an explicit legality condition for that concrete execution and must be satisfied or the run is classified non-start/recovery/redispatch.

## 12. Promotion

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 remains one bounded active promotion attempt at a time. Strict `NO_NEW_MATHEMATICS` governance maintenance uses a separate bounded attempt and cannot change theorem/native-definition/evidence/ownership semantics.

Execution `RETURN_ACCEPTED` is also not canonical truth promotion.

## 13. Persistence / truth

- journal = event provenance, not theorem truth;
- Driver Continuity = routing only, no implicit default route;
- execution return/acceptance = concrete-run validity, not theorem/candidate truth;
- exact mathematical canonical truth = gated source `main`;
- semantic checkpoints persist state but do not by themselves end an active parent user objective.

## 14. Turn termination

A turn ends only when the parent objective is complete, the user explicitly asks to stop/pause/wait, or no executable next action remains because of a genuine safety/authorization/missing-user-data/unavoidable-external-event/platform limitation.

Before using a blocking terminal condition, exhaust independent/downstream-safe work and return the strongest current result.

Never use `WAITING_FOR_CONTINUE` when `continue` would add no information.
