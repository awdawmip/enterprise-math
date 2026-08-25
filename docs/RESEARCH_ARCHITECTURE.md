# Enterprise Math Research Architecture V2

Status: `ACTIVE / CANONICAL GOVERNANCE / V2.5`
Date: `2026-08-25`
Driver-ID: `EM-DVR-K7Q4N8`

Machine contracts:

- `research_architecture.json`;
- `research_runtime_state_machine.json`;
- `research_task_publication_contract.json`;
- `research_task_registry.json`;
- `active_turn_liveness.json`;
- `research_axiom_candidate_state_machine.json`.

FREE substrate: `definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`
Task publication: `docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md`
Promotion liveness: `docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`

## 1. Four functions, one task registry

### FREE_AXIOM_DISCOVERY

`PRIMITIVE SUBSTRATE -> SELF-GENERATED QUESTION -> FROZEN CANDIDATE -> PHASE-B AUDIT`.

FREE receives primitive substrate, not current achievements or a suggestion menu. Raw Phase-A discovery does not publish task agenda. After Phase-B audit, an eligible audited candidate may be published directly by the free researcher into the common task registry without Driver intake.

### TASK_RESEARCH

Executes a selected registered/explicit mother question. A task researcher may publish valuable side residues into the same registry without switching the current task.

### RESEARCH_DRIVER

Owns portfolio reprioritization, de-duplication, continuation/closure, Working Truth activation, Foundation/replication routing and promotion. Driver uses the same task publication template as researchers; Driver authority is not required merely to make a task exist.

### FOUNDATION_STEWARD

Maintains/verifies shared definitions/interfaces/status/tools and may publish governance tasks through the same registry. Task publication never auto-promotes Foundation truth.

## 2. Canonical runtime stack

Every role preserves:

`PARENT_OBJECTIVE -> TASK_REGISTRATION -> TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`.

Freeze:

`OFFICIAL_NEW_TASK -> CANONICAL_TASK_REGISTRY_RECORD`.

`UNREGISTERED_NEW_TASK -> NO READY / NO CLAIM / NO EXECUTION`.

`OWNER_LEASE != SESSION_LIVENESS`.

`SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE`.

`DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN`.

The following do not terminate the parent by themselves: task publication, tool return, recoverable error, checkpoint/journal write, Stage/Driver verdict, branch/PR boundary, `PENDING_NONBLOCKING`, or progress update.

Open-ended continuation survives these subflows until the parent criterion is met or revoked.

## 3. Unified task publication / orphan prevention

All new official tasks use:

- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`;
- `tools/research_task_registry.py`;
- `research_task_registry.json`.

Allowed publishers: `RESEARCHER`, `RESEARCH_DRIVER`, `FOUNDATION_STEWARD`.

Freeze:

`TASKBOOK_FILE != PUBLISHED_TASK`.

`RESEARCHER_MAY_PUBLISH_TASK_WITHOUT_DRIVER_APPROVAL`.

`TASK_PUBLICATION != WORKING_TRUTH`.

`TASK_PUBLICATION != FOUNDATION_OR_CANONICAL_PROMOTION`.

Every registry record requires a `parent_objective_id` and `research_value`, preserving why the unresolved work matters even when not immediately selected.

Researcher-published tasks default to effective `P2 / MEDIUM`; publisher priority requests remain visible and Driver portfolio reprioritization remains separate.

A publication is a `SUBFLOW`: after registry audit PASS, return to the current parent objective.

Pre-cutover taskbooks/scheduler work remain legacy baseline for existing executions only. Fresh redispatch, modification or current-policy re-review requires explicit registry migration.

## 4. FREE Phase-A information regime

Freeze:

`FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS`.

`NO_DEFAULT_DISCOVERY_LENS_MENU`.

FREE Phase A loads only primitive substrate, exact primitives actually needed, protected relevant worldview and integrity/typing rules. Current task/route/history, downstream achievements, other-branch Working Truth, suggestion menus and tool/representation convenience are not discovery priors.

After candidate freeze, current/prior context becomes Phase-B audit material.

## 5. Candidate lifecycle

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`.

`DISCOVERY_IN_PROGRESS -> BLIND_CANDIDATE_FROZEN -> PHASE_B_AUDIT -> CLASSIFICATION`.

From `AUDITED_AXIOM_CANDIDATE`, `AUDITED_REPLACEMENT_CANDIDATE`, or `EXACT_NEGATIVE_OBSTRUCTION`, a researcher may publish a registered task while preserving `origin_kind=FREE_AXIOM_CANDIDATE`, candidate ID and audited state.

Driver/Steward intake remains a separate later decision for portfolio rank, Working Truth, Foundation/replication and promotion.

`TASK_ORIGIN_AND_LINEAGE_CANNOT_BE_ERASED_BY_RENAMING`.

## 6. Working Truth

Working Truth activates only after explicit Driver freeze or exact task semantics that explicitly grant the execution premise. Mere registered publication is not an activation event.

## 7. Stage / successor rule

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

A continuation requires a genuine new information gap, discriminating outcomes, kill condition, `parent_task_id`, and explicit consideration of closure/another owner/free exploration.

Stage 2+ is continuation semantics; renaming does not reset lineage.

`STAGE_TERMINAL_VERDICT -> SAME_TURN_SUCCESSOR_GATE_EVALUATION`.

## 8. Scheduler / Foundation / portfolio

Scheduler is registered TASK exploitation infrastructure, not FREE Phase-A question selection. New post-cutover work must be registered before READY/CLAIM.

Raw discovery does not auto-enter Foundation backflow, and registered task status does not auto-promote Foundation truth.

Recent route success is not itself roadmap evidence. Registered capture does not imply immediate selection.

## 9. Independence and evidence

A clean blind-discovery claim requires clean pre-generation context and frozen substrate/worldview snapshot.

`DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE`.

Independent runs do not share candidate packets or a suggestion menu before freeze. Publishing a task does not create independence.

## 10. Read performance

`SMALLEST_SUFFICIENT_ROLE_PACKET > UNIVERSAL_PRELOAD`.

FREE: `ROLE -> PRIMITIVE SUBSTRATE -> NEEDED PRIMITIVES -> DISCOVERY`.

TASK: `AGENTS -> EXACT REGISTERED TASK -> FIRST DEPENDENCY -> WORK -> TRIGGERED EXPANSION`.

## 11. Remote / publication liveness

`REMOTE_SILENT` describes repository activity, not conversational inactivity.

`CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK`.

`CHECKPOINT_PERSISTED -> RESUME_PARENT_TASK`.

`PUBLICATION_COMPLETE -> RESUME_PARENT_TASK`.

Task publication, GitHub publication and checkpoint subflows return to the parent objective in the same turn when it remains open.

## 12. Promotion

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 remains one bounded active promotion attempt at a time. Strict `NO_NEW_MATHEMATICS` governance maintenance uses a separate bounded governance-maintenance attempt and cannot change theorem/native-definition/evidence/ownership semantics or use the governance-maintenance lane to smuggle mathematical claim changes.

## 13. Persistence / truth

- `research_task_registry.json` = canonical task existence/orphan prevention;
- taskbook = task-local research content;
- journal = event provenance, not theorem truth;
- Driver Continuity = routing summary, not task existence or theorem evidence;
- canonical mathematical truth = gated source `main`.

## 14. Turn termination

A turn ends only when the parent objective is complete, the user explicitly asks to stop/pause/wait, or no executable next action remains because of genuine safety/authorization/missing-user-data/unavoidable-external-event/platform limitation.

Before a blocking terminal, exhaust independent/downstream-safe work and return the strongest result.

Never use `WAITING_FOR_CONTINUE` when `continue` would add no information.
