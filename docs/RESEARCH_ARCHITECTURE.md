# Enterprise Math Research Architecture V2

Status: `ACTIVE / CANONICAL GOVERNANCE / V2.6`
Date: `2026-08-28`
Driver-ID: `EM-DVR-K7Q4N8`

Machine contracts:

- `research_architecture.json` — role/research semantics;
- `control_plane/current_control_authority.json` — narrow control precedence for publication/dispatch/tool reuse/liveness;
- `research_runtime_state_machine.json`;
- `research_task_publication_contract_v2.json`;
- `research_dispatch_contract.json`;
- `active_turn_liveness.json`;
- `research_axiom_candidate_state_machine.json`.

FREE substrate: `definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`
Task publication: `docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md`
Promotion liveness: `docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`

For fields covered by `control_plane/current_control_authority.json`, that narrow precedence plus the named exact machine contract controls over stale V1 compatibility wording in older documents. This does not alter mathematical/role authority outside those control fields.

## 1. Four research functions plus non-research control maintenance

### FREE_AXIOM_DISCOVERY

`PRIMITIVE SUBSTRATE -> SELF-GENERATED QUESTION -> FROZEN CANDIDATE -> PHASE-B AUDIT`.

FREE receives primitive substrate, not current achievements or a suggestion menu. Raw Phase-A discovery does not publish task agenda. After Phase-B audit, an eligible audited candidate may publish an immutable V2 task without Driver intake.

### TASK_RESEARCH

Executes a selected explicit/registered mother question. A task researcher may publish valuable side residues through V2 without switching the current task.

### RESEARCH_DRIVER

Owns portfolio reprioritization, de-duplication, continuation/closure, Working Truth activation, Foundation/replication routing and promotion. Driver uses the same V2 task publication transaction as researchers; Driver authority is not required merely to make a task exist.

### FOUNDATION_STEWARD

Maintains/verifies shared definitions/interfaces/status/tools and may publish governance tasks through V2. Task publication never auto-promotes Foundation truth.

### CONTROL_PLANE_MAINTENANCE

Maintains dispatch/liveness/CI/authority/control surfaces when explicitly requested. It is not a research identity and grants no theorem review, Driver, Steward, Working Truth or promotion authority.

## 2. Canonical runtime stack

Every research role preserves:

`PARENT_OBJECTIVE -> TASK_REGISTRATION -> TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`.

Freeze:

`OFFICIAL_POST_CUTOVER_TASK -> IMMUTABLE_V2_PUBLICATION_RECORD`.

`UNREGISTERED_NEW_TASK -> NO READY / NO CLAIM / NO EXECUTION`.

`OWNER_LEASE != SESSION_LIVENESS`.

`SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE`.

`DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN`.

The following do not terminate the parent by themselves: task publication, tool return, recoverable error, checkpoint/journal write, Stage/Driver verdict, branch/PR boundary, `PENDING_NONBLOCKING`, or progress update.

Open-ended continuation survives these subflows until the parent criterion is met or revoked.

## 3. Immutable V2 task publication / orphan prevention

All new or modified post-cutover tasks use:

- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`;
- `tools/research_task_records.py`;
- immutable `research_task_records/<task-id>/<publication-id>.json`.

Allowed publishers: `RESEARCHER`, `RESEARCH_DRIVER`, `FOUNDATION_STEWARD`.

`research_task_registry.json` and `tools/research_task_registry.py` are V1 read-only compatibility/audit surfaces, not post-cutover publication authority.

Freeze:

`TASKBOOK_FILE != PUBLISHED_TASK`.

`RESEARCHER_MAY_PUBLISH_TASK_WITHOUT_DRIVER_APPROVAL`.

`TASK_PUBLICATION != WORKING_TRUTH`.

`TASK_PUBLICATION != FOUNDATION_OR_CANONICAL_PROMOTION`.

Every V2 publication preserves a nonempty `parent_objective_id`, `research_value`, exact frontier/next action, origin/lineage and immutable taskbook identity.

Researcher-published tasks default to effective `P2 / MEDIUM`; publisher rank requests remain provenance and Driver portfolio reprioritization remains separate.

Publication is a `SUBFLOW`: after V2 audit PASS, return to the current parent objective.

Pre-cutover scheduler/taskbook state remains legacy baseline for existing compatible executions only. Fresh redispatch, modification or current-policy re-review requires V2 migration.

## 4. Canonical live dispatch

Canonical live routing is:

`research_control_dispatch.py`.

It composes fault-isolated runtime views, stale-owner recovery, ordinary fresh selection and active-cohort lane selection.

`tools/research_dispatch.py` is the ordinary **fresh selector**, not the whole live routing decision.

`tools/research_lane_dispatch.py` is the active-cohort lane selector.

Freeze:

`STALE_SESSION + VALID_OWNER_CLAIM -> ADOPT_SAME_CLAIM`.

`FRESH_SELECTOR_EMPTY + VALID_OWNER_LIVENESS_UNKNOWN -> VERIFY_SESSION_LIVENESS`.

`NO_DISPATCH` is valid only after stale-recoverable owner scopes and fresh targets are both excluded.

## 5. FREE Phase-A information regime

Freeze:

`FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS`.

`NO_DEFAULT_DISCOVERY_LENS_MENU`.

FREE Phase A loads only primitive substrate, exact primitives actually needed, protected relevant worldview and integrity/typing rules. Current task/route/history, downstream achievements, other-branch Working Truth, suggestion menus and project-tool/representation convenience are not discovery priors.

After candidate freeze, current/prior context becomes Phase-B audit material.

## 6. Candidate lifecycle

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`.

`DISCOVERY_IN_PROGRESS -> BLIND_CANDIDATE_FROZEN -> PHASE_B_AUDIT -> CLASSIFICATION`.

From `AUDITED_AXIOM_CANDIDATE`, `AUDITED_REPLACEMENT_CANDIDATE`, or `EXACT_NEGATIVE_OBSTRUCTION`, a researcher may publish an immutable V2 task while preserving `origin_kind=FREE_AXIOM_CANDIDATE`, candidate ID/state and semantic lineage.

Driver/Steward intake remains a separate later decision for portfolio rank, Working Truth, Foundation/replication and promotion.

`TASK_ORIGIN_AND_LINEAGE_CANNOT_BE_ERASED_BY_RENAMING`.

## 7. Working Truth

Working Truth activates only after explicit Driver freeze or exact task semantics that explicitly grant the execution premise. Mere V2 task publication is not an activation event.

## 8. Tool lookup and actual reuse

Once TASK semantics are understood—and after any explicit discovery firewall freeze—run the reuse gate before inventing new general machinery.

`TOOL_COVERAGE_LOOKUP != TOOL_USE`.

A relevant match must receive explicit reuse resolution under `tool_invocation_policy.json`, including as appropriate:

- `REUSE_APPLIED`;
- `REUSE_EXECUTED`;
- `COMPOSE_APPLIED`;
- `REUSE_IDENTIFIED_EXECUTION_UNAVAILABLE`;
- `EXTEND_EXISTING_TOOL`;
- `CAPABILITY_GAP_CONFIRMED`;
- `NOT_APPLICABLE`.

Environment inability to execute an adequate existing implementation is not itself a mathematical capability gap.

FREE Phase A hides current project-tool vocabulary as a discovery prior; Phase B opens toolbox/method context for audit/dedup/reuse.

## 9. Stage / successor rule

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

A continuation requires a genuine new information gap, discriminating outcomes, kill condition, `parent_task_id`, and explicit consideration of closure/another owner/free exploration.

Stage 2+ is continuation semantics; renaming does not reset lineage.

`STAGE_TERMINAL_VERDICT -> SAME_TURN_SUCCESSOR_GATE_EVALUATION`.

## 10. Scheduler / Foundation / portfolio

Canonical control dispatch is TASK exploitation infrastructure, not FREE Phase-A question selection. New post-cutover work must have V2 authority before CLAIM.

Raw discovery does not auto-enter Foundation backflow, and task publication does not auto-promote Foundation truth.

Foundation Steward research handoffs use V2 task publication plus `research_control_dispatch.py`; they do not publish new work by editing `research_scheduler.json`.

Recent route success is not itself roadmap evidence. Registered capture does not imply immediate selection.

## 11. Independence and evidence

A clean blind-discovery claim requires clean pre-generation context and frozen substrate/worldview snapshot.

`DISCOVERY_EVIDENCE != INDEPENDENT_VALIDATION_EVIDENCE`.

Independent runs do not share candidate packets or a suggestion menu before freeze. Publishing a task does not create independence.

## 12. Read performance and control-plane efficiency

`SMALLEST_SUFFICIENT_ROLE_PACKET > UNIVERSAL_PRELOAD`.

FREE: `ROLE -> PRIMITIVE SUBSTRATE -> NEEDED PRIMITIVES -> DISCOVERY`.

TASK: `AGENTS -> EXACT TASK -> FIRST DEPENDENCY -> WORK -> TRIGGERED EXPANSION`.

Control-plane work uses the cooperative soft watchdog in `active_turn_liveness.json`:

- normally 2–3 control tool calls per inspection cycle before recomputation;
- sufficient evidence stops diagnostic expansion;
- same error signature collapses to one root cause;
- user status/direction messages preempt nonessential diagnostics;
- `READ_SNAPSHOT != WRITE_AUTHORITY`;
- long mathematical computation with semantic progress is not control-plane no-progress.

## 13. Remote / publication liveness

`REMOTE_SILENT` describes repository activity, not conversational inactivity.

`CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK`.

`CHECKPOINT_PERSISTED -> RESUME_PARENT_TASK`.

`PUBLICATION_COMPLETE -> RESUME_PARENT_TASK`.

Task publication, GitHub publication and checkpoint subflows return to the parent objective in the same turn when it remains open.

## 14. Promotion

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 remains one bounded active promotion attempt at a time. Strict `NO_NEW_MATHEMATICS` governance maintenance uses a separate bounded maintenance attempt and cannot smuggle mathematical claim changes.

## 15. Persistence / truth

- immutable V2 task records = post-cutover task existence/provenance;
- `research_task_registry.json` = V1 compatibility mirror only;
- taskbook = task-local research content;
- Issue #240 = sparse runtime ownership/control events;
- immutable result/review records = terminal provenance;
- journal = event provenance, not theorem truth;
- Driver Continuity = routing summary, not task existence or theorem evidence;
- canonical mathematical truth = gated source `main`.

## 16. Turn termination

A turn ends only when the parent objective is complete, the user explicitly asks to stop/pause/wait, or no executable next action remains because of genuine safety/authorization/missing-user-data/unavoidable-external-event/platform limitation.

Before a blocking terminal, exhaust independent/downstream-safe work and return the strongest result.

Never use `WAITING_FOR_CONTINUE` when `continue` would add no information.
