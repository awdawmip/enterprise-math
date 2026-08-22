# Enterprise Math Research Architecture V2

Status: `ACTIVE / CANONICAL GOVERNANCE / V2.4`
Date: `2026-08-22`
Driver-ID: `EM-DVR-K7Q4N8`
Machine contracts:

- `research_architecture.json`;
- `active_turn_liveness.json`;
- `research_axiom_candidate_state_machine.json`.

FREE substrate: `definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`
Promotion liveness: `docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`

## 1. Four functions

### FREE_AXIOM_DISCOVERY

`PRIMITIVE SUBSTRATE -> RESEARCHER GENERATES ITS OWN QUESTION -> FROZEN CANDIDATE -> PHASE-B AUDIT`.

FREE receives primitive substrate, not the current-achievement catalog or a suggestion/lens menu.

### TASK_RESEARCH

Executes a selected mother question from the user, Driver, scheduler, Foundation intake or audited-candidate transition.

### RESEARCH_DRIVER

Owns portfolio routing, candidate intake, de-duplication, task creation, Working Truth activation, continuation/closure and promotion.

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

## 3. FREE Phase-A information regime

Freeze:

`FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS`.

`NO_DEFAULT_DISCOVERY_LENS_MENU`.

FREE Phase A loads only the primitive-substrate router, exact primitive files actually needed, relevant protected worldview facts, and necessary integrity/typing rules.

Current task/route/history, downstream achievements, other-branch Working Truth, success/failure catalogs, suggested questions/lens menus, ambient recent-project context, and tool/representation convenience are not discovery priors.

After candidate freeze, current/prior context becomes Phase-B audit/comparison material.

## 4. Candidate lifecycle

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`.

`DISCOVERY_IN_PROGRESS -> BLIND_CANDIDATE_FROZEN -> PHASE_B_AUDIT -> CLASSIFICATION -> DRIVER_INTAKE`.

Tasks created from free discovery preserve candidate origin/ID/audited state.

`TASK_ORIGIN_AND_LINEAGE_CANNOT_BE_ERASED_BY_RENAMING`.

## 5. Working Truth

Working Truth activates only after explicit Driver/taskbook freeze. It is not a FREE Phase-A premise, raw-candidate state or Phase-B dedup prior.

## 6. Stage / successor rule

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

A continuation requires a genuine new information gap, discriminating outcomes, kill condition, and explicit consideration of closure/another owner/free exploration.

Stage 2+ is continuation semantics; renaming does not reset lineage.

But:

`STAGE_TERMINAL_VERDICT -> SAME_TURN_SUCCESSOR_GATE_EVALUATION`.

The Driver immediately evaluates continue-same-task, justified successor, route closure plus another portfolio action, FREE exploration, or parent completion. Local stage/route closure is not automatically parent-goal closure.

## 7. Scheduler / Foundation / portfolio

Scheduler is TASK exploitation infrastructure, not FREE question selection.

Raw discovery does not auto-enter Foundation backflow.

Recent route success is not itself roadmap evidence. No numeric exploration quota is imposed.

## 8. Independence and evidence

A clean blind-discovery claim requires a clean pre-generation context and frozen substrate/worldview snapshot.

`DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE`.

Independent runs do not share candidate packets or a common suggestion menu before freeze.

## 9. Read performance

`SMALLEST_SUFFICIENT_ROLE_PACKET > UNIVERSAL_PRELOAD`.

FREE:

`ROLE -> PRIMITIVE SUBSTRATE -> NEEDED PRIMITIVES -> DISCOVERY`.

TASK:

`AGENTS -> EXACT TASK -> FIRST DEPENDENCY -> WORK -> TRIGGERED EXPANSION`.

## 10. Remote / publication liveness

`REMOTE_SILENT` describes repository activity, not conversational inactivity.

`CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK`.

`CHECKPOINT_PERSISTED -> RESUME_PARENT_TASK`.

`PUBLICATION_COMPLETE -> RESUME_PARENT_TASK`.

GitHub/publication subflows follow the bounded current protocols and then return to the parent objective in the same turn when it remains open.

## 11. Promotion

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 remains one bounded active promotion attempt at a time. Strict `NO_NEW_MATHEMATICS` governance maintenance uses a separate bounded attempt and cannot change theorem/native-definition/evidence/ownership semantics.

## 12. Persistence / truth

- journal = event provenance, not theorem truth;
- Driver Continuity = routing only, no implicit default route;
- exact mathematical canonical truth = gated source `main`;
- semantic checkpoints persist state but do not by themselves end an active parent user objective.

## 13. Turn termination

A turn ends only when the parent objective is complete, the user explicitly asks to stop/pause/wait, or no executable next action remains because of a genuine safety/authorization/missing-user-data/unavoidable-external-event/platform limitation.

Before using a blocking terminal condition, exhaust independent/downstream-safe work and return the strongest current result.

Never use `WAITING_FOR_CONTINUE` when `continue` would add no information.
