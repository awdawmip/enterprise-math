# Enterprise Math agent operating router

Status: `ACTIVE / STABLE EXECUTION ROUTER / V2.9`

`AGENTS.md` is a **current execution router**. It is not a theorem catalog, project history, old-route index, or archive.

## 1. Mode resolution

Current explicit user instruction controls scope.

Current research roles/modes:

- `EM_FREE_RESEARCHER` -> `FREE_AXIOM_DISCOVERY`;
- explicit user task / registered task / taskbook / scheduler dispatch -> `TASK_RESEARCH`;
- explicit Driver activation -> `RESEARCH_DRIVER`;
- explicit Foundation Steward activation/maintenance -> `FOUNDATION_STEWARD`.

Exact role authority:

- `research_architecture.json`;
- `research_role_policy.json`;
- `research_identity_state_machine.json`;
- `foundation_steward.json` when Steward authority is active.

## 2. Active-turn continuation liveness

Canonical contract:

- `active_turn_liveness.json`;
- `docs/ACTIVE_TURN_CONTINUATION_LIVENESS.md`.

Maintain:

`PARENT_USER_OBJECTIVE -> CURRENT_SUBFLOW -> NEXT_EXECUTABLE_ACTION`.

Freeze:

`SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE`.

`DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN`.

A semantic checkpoint, journal write, tool return, recoverable tool error, PR/branch metadata boundary, `PENDING_NONBLOCKING`, Stage/Driver verdict, task publication, progress update, or local soft block is not a reason to wait for `继续` when the parent remains open and an executable next step exists.

When the user says continue/keep going/do not stop/until satisfied/until no further progress/solve blocker and continue, the parent continuation lease remains active until that criterion is met or revoked.

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER` remains binding, but every Stage terminal verdict receives same-turn successor-gate/closure/portfolio evaluation.

### Unified runtime gate

Canonical runtime:

- `research_runtime_state_machine.json`;
- `tools/research_runtime_guard.py`;
- `tools/research_runtime.py`;
- `docs/RESEARCH_RUNTIME_STATE_MACHINE.md`.

Preserve one coherent runtime view:

`PARENT_OBJECTIVE -> TASK_REGISTRATION -> TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> CURRENT_UNFINISHED_UNIT -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`.

Freeze:

`OWNER_LEASE != SESSION_LIVENESS`.

`SESSION_STALE + OWNER_LEASE_ACTIVE -> STALE_RECOVERABLE`.

`SUBFLOW_COMPLETE -> REEVALUATE_PARENT`.

`TASK_FROZEN -> REEVALUATE_PARENT`.

A stale replacement conversation verifies taskbook source, owner branch, live claim, remote HEAD, execution stamp and durable outputs, then adopts the existing claim and resumes the first unfinished unit. Do not re-claim or replay durable work.

Scheduler `claim_lease_minutes` / `lease_until` is owner lease only. It does not prove conversation liveness.

Canonical control dispatch is recovery-aware:

`STALE_SESSION + VALID_OWNER_CLAIM -> ADOPT_EXISTING_CLAIM -> OTHERWISE_FRESH_DISPATCH`.

Do not infer `NO_TASK` / `NO_DISPATCH` merely because the fresh selector returns no `NEEDS_DISPATCH` task. If fresh task/lane selection is empty while a valid owner lease remains and session liveness is unknown, first verify the latest independently observable conversation response or durable execution progress. Stale means adopt the existing winning CLAIM through `tools/research_runtime_guard.py adopt`; active means preserve that owner. Never manufacture a second CLAIM merely to recover a stale conversation.

Immediately before final-channel output, evaluate PRE_FINAL through `tools/research_runtime_guard.py`; `tools/active_turn_liveness.py` remains the primitive liveness evaluator.

`PARENT_OBJECTIVE_OPEN + EXECUTABLE_NEXT_ACTION -> FINAL_ALLOWED=false`.

`RUNTIME_FINAL_ALLOWED_FALSE -> FINAL_CHANNEL_FORBIDDEN`.

### Unified task publication / orphan prevention

Canonical post-cutover task-publication surfaces:

- `research_task_publication_contract_v2.json`;
- `research_task_records/<task-id>/<publication-id>.json`;
- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`;
- `tools/research_task_records.py`;
- `tools/research_dispatch.py`.

`research_task_registry.json` and `tools/research_task_registry.py` are V1 compatibility surfaces, not new publication authority. `research_scheduler.json` is a frozen legacy task-definition baseline, not a new publication path.

Every new official task—Researcher, free Researcher after audit, Driver, or Foundation Steward—uses the **same taskbook template and immutable publication transaction**.

Freeze:

`TASKBOOK_FILE != PUBLISHED_TASK`.

`OFFICIAL_NEW_TASK -> CANONICAL_TASK_REGISTRY_RECORD -> IMMUTABLE_TASK_PUBLICATION_RECORD`.

`UNREGISTERED_NEW_TASK -> NO READY / NO CLAIM / NO EXECUTION`.

`RESEARCHER_MAY_PUBLISH_TASK_WITHOUT_DRIVER_APPROVAL`.

Here `CANONICAL_TASK_REGISTRY_RECORD` is the compatibility name for the current immutable task-publication generation; it does not restore the V1 shared registry as write authority.

A researcher-published task defaults to effective `P2 / MEDIUM`; publication may record a requested rank, but Driver portfolio reprioritization remains separate authority.

Publication never grants Working Truth, Foundation status, theorem truth, canonical promotion, or Driver authority.

Every published task carries a nonempty `parent_objective_id` and `research_value` explaining why the work must not be lost.

FREE Phase A cannot publish task agenda. After Phase-B audit, an eligible `AUDITED_AXIOM_CANDIDATE`, `AUDITED_REPLACEMENT_CANDIDATE`, or `EXACT_NEGATIVE_OBSTRUCTION` may be published directly by the free researcher while preserving candidate provenance.

A task researcher may publish a valuable side residue without switching the current task. Publication is a SUBFLOW; after success return to the current parent objective.

Legacy tasks may continue already-owned executions, but fresh redispatch/modification requires explicit immutable migration.

### Canonical low-burden dispatch

Canonical live control routing is `research_control_dispatch.py` over the existing fresh selectors and runtime guard:

- ordinary fresh task selection: `tools/research_dispatch.py`;
- active-cohort fresh lane selection: `tools/research_lane_dispatch.py`;
- stale valid-owner adoption: `tools/research_runtime_guard.py adopt`;
- immutable registered task definitions;
- frozen legacy scheduler baseline;
- Issue #240 runtime events;
- result/review state.

The control router must distinguish `OWNER_LEASE` from `SESSION_LIVENESS`. A fresh-selector miss is not a terminal dispatch verdict until stale-owner recovery has been excluded. Unknown liveness with a valid owner lease routes to `VERIFY_SESSION_LIVENESS`, not `NO_DISPATCH`.

For a new registered execution:

`VALIDATE_CURRENT_PUBLICATION -> CREATE_OR_VERIFY_BRANCH -> ONE_CLAIM -> RESEARCH`.

For stale-session recovery:

`VERIFY_STALE_SESSION -> VERIFY_WINNING_CLAIM_AND_DURABLE_FRONTIER -> ADOPT_SAME_CLAIM -> RESUME`.

The single Issue #240 CLAIM is the execution envelope. Do not require a second pre-claim execution-record write, PR, merge, CI wait, or status poll.

Live registered events are authenticated from the **same GitHub comment's server metadata**: comment ID orders events, server `created_at` supplies the event/lease clock, server author records provenance, and `updated_at` detects edits. Body `actor/at` are descriptive only. Edited event comments do not rewrite runtime history; append a new correction event instead.

## 3. Identity and mandatory final footer

Resolve visible identity before substantive work:

- Researcher -> `Researcher-ID`;
- Driver -> `Driver-ID`;
- Foundation Steward -> `Steward-ID`.

Identity registration is nonblocking. Publisher identity is persisted in the publication record; reusable taskbooks do not freeze execution identity.

Canonical final-response contract: `final_response_identity_policy.json`.

Freeze:

`ACTIVE_ENTERPRISE_MATH_ROLE -> EVERY_ASSISTANT_FINAL_RESPONSE_ENDS_WITH_EXACTLY_ONE_ROLE_IDENTITY_MARKER`.

Exact marker:

- `RESEARCH_DRIVER` -> `Driver-ID: <ID> / CONTROL_PLANE`;
- `FOUNDATION_STEWARD` -> `Steward-ID: <ID> / FOUNDATION_STEWARD`;
- `RESEARCHER` with active task -> `Researcher-ID: <ID> / <TASK_ID>`;
- free researcher -> `Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY`;
- direct fallback -> `Researcher-ID: <ID> / TASK_RESEARCH`.

Do not use `DIRECT` as a visible researcher scope. If `Global-Knowledge-Sync:` is emitted, identity appears immediately before it.

## 4. FREE_AXIOM_DISCOVERY

FREE Phase A receives the **primitive substrate**, not the current-result catalog and not a suggestion menu.

Canonical substrate router: `definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`.

Before candidate freeze:

- do not preload the general current-result router;
- do not preload task/route/coordination/recent-history context;
- do not inherit unrelated `WORKING_TRUTH`;
- do not let tools, representations, filenames or current vocabulary choose the question;
- do not supply suggested questions or discovery-lens menus;
- use generic exclusion categories rather than naming hidden current results.

Freeze:

`FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS`.

`NO_DEFAULT_DISCOVERY_LENS_MENU`.

Candidate lifecycle: `research_axiom_candidate_state_machine.json`.

After candidate/no-go freeze, Phase B may open current/prior work and must run tool-coverage/dedup before method-novelty claims. Eligible audited candidates may then be published as tasks without Driver intake merely to preserve the work.

## 5. TASK_RESEARCH hot start

For a selected task:

1. this router if not already loaded;
2. the **exact task entry**;
3. verify it is immutably registered or covered by an already-owned legacy continuation;
4. load the first exact dependency required to begin;
5. work and expand only when a concrete dependency triggers.

Soft routine source-read budget before substantive work: `<= 3`.

The Common Surface is a lookup, not a default preload.

Do not preload the entire dispatch board. One canonical task selection/claim boundary is sufficient until a real coordination event requires another lookup.

## 6. Universal tool reuse gate

Canonical policy:

- `tool_invocation_policy.json`;
- `docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md`;
- `enterprise_toolbox_registry.json`;
- `research_method_inventory.json`;
- `tools/enterprise_toolbox.py`.

For ordinary `TASK_RESEARCH`, `RESEARCH_DRIVER`, and shared Steward work, once the problem structure is understood and **before constructing a new general-purpose mechanism/tool/helper calculus**, perform current tool coverage lookup.

Freeze:

`UNDERSTAND_TASK_FIRST -> TOOL_LOOKUP_SECOND`.

`EXISTING_TOOL_COVERAGE -> REUSE_OR_COMPOSE_UNLESS_EXACT_SCOPE_GAP_IS_RECORDED`.

`NEW_TOOL_DIRECTION_REQUIRES_CONFIRMED_CAPABILITY_GAP`.

Outcomes: `REUSE_EXISTING_TOOL`, `COMPOSE_EXISTING_TOOLS`, `EXTEND_EXISTING_TOOL`, `CAPABILITY_GAP_CONFIRMED`, `NOT_APPLICABLE`.

Do not create a new tool family merely because the mechanism appears under another route/domain/name. Every Driver/Steward-accepted return receives method-harvest classification.

### Discovery-firewall timing exception

Tool lookup is delayed for FREE Phase A and explicit task-local blind-forward/source-whitelist protocols until their declared freeze. Immediately after freeze, dedup becomes mandatory before method-novelty or new-tool continuation claims.

## 7. GitHub/service routing

`CONNECTED_GITHUB_PLUGIN = PRIMARY_REMOTE_GITHUB_PATH`.

Use connected GitHub capability for remote repository files, commits, branches, PRs, issues and workflow/status operations. Do not use container networking to duplicate GitHub access when the connector supports the action.

Detailed rules: `docs/GITHUB_INTERACTION_BUDGET.md` and `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md`.

## 8. Working Truth

`WORKING_TRUTH` is TASK execution discipline only after an explicit Driver freeze or exact task semantics that grant the premise.

Mere task registration/publication does not activate Working Truth.

It is not a FREE Phase-A premise and not raw-candidate status.

## 9. Evidence integrity

Never fabricate proof, computation, hashes, validation status, novelty, provenance, registry state or tool results. Finite enumeration/software success is not automatically theorem proof.

Load triggered semantic policies only when needed:

- `FOUNDATIONAL_LOGIC.md` / `foundational_logic.json`;
- `native_semantics_admissibility.json`;
- geometry/refoundation policy for relevant tasks.

## 10. Candidate / task / continuation provenance

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`.

A task from FREE discovery preserves audited candidate origin/ID/state.

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

A continuation requires a genuine information gap, discriminating outcomes, kill condition, and consideration of closure/another owner/free exploration.

Exact task/publication contracts:

- `research_taskbook_contract.json`;
- `research_taskbook_policy.json`;
- `research_task_publication_contract_v2.json`;
- `research_task_records/`;
- `docs/RESEARCH_TASKBOOK_AUTHORING_AND_REVIEW.md`;
- `docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md`.

## 11. Remote liveness

`RESEARCH_HOT_PATH > REMOTE_PREFLIGHT`.

Do not run universal scheduler/Issue/PR/CI/tree preflight, poll CI merely to wait, chase moving main, or emit periodic scheduler heartbeats without a concrete coordination need.

Session-liveness verification is targeted control recovery, not a periodic heartbeat: perform it when a stale adoption is being considered or when fresh dispatch is empty and a live owner lease would otherwise be mistaken for terminal `NO_DISPATCH`.

Between genuine semantic checkpoints, default added governance operations are zero.

Tool/scheduler/registry/CI availability is not a mathematical `HARD_BLOCK`.

`REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED`.

## 12. Triggered control surfaces

Load only when relevant:

- task records/canonical dispatch/Relay/Foundation for actual coordination;
- Driver contract + continuity for portfolio decisions;
- Common Surface for exact cross-owner theorem/tool/conflict lookup;
- toolbox/method inventory for method selection/harvest;
- current native router for current-result lookup;
- test/Lean diagnostics for actual diagnosis;
- owner-isolation/promotion policy for publication/promotion work.

## 13. Persistence and publication

L1/L2/L3 research is remote-silent between semantic checkpoints by default.

`REMOTE_SILENT` describes repository traffic, **not conversational inactivity**.

Immutable task records carry task existence; taskbooks carry task content; Issue #240 carries sparse ownership/coordination events; result/review records carry terminal provenance; Driver Continuity carries routing summary; source main carries gated canonical truth. These roles must not be conflated.

## 14. Promotion liveness

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 is one bounded active promotion attempt at a time. Strict `NO_NEW_MATHEMATICS` maintenance follows `docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`.

## 15. Current-only hot path

Normal startup files describe current behavior/current authority only. Historical/provenance material is loaded only when explicitly needed.
