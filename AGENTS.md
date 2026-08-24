# Enterprise Math agent operating router

Status: `ACTIVE / STABLE EXECUTION ROUTER / V2.7`

`AGENTS.md` is a **current execution router**. It is **not** a theorem catalog, project history, old-route index, or archive.

## 1. Mode resolution

Current explicit user instruction controls scope.

Current research modes:

- `EM_FREE_RESEARCHER` -> `FREE_AXIOM_DISCOVERY`;
- explicit user task / Driver handoff / approved taskbook / scheduler dispatch -> `TASK_RESEARCH`;
- explicit Driver activation -> `RESEARCH_DRIVER`.

Exact role authority:

- `research_architecture.json`;
- `research_role_policy.json`;
- `research_identity_state_machine.json`.

## 2. Active-turn continuation liveness

Canonical contract:

- `active_turn_liveness.json`;
- `docs/ACTIVE_TURN_CONTINUATION_LIVENESS.md`.

Maintain:

`PARENT_USER_OBJECTIVE -> CURRENT_SUBFLOW -> NEXT_EXECUTABLE_ACTION`.

Freeze:

`SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE`.

`DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN`.

A semantic checkpoint, journal write, tool return, recoverable tool error, PR/branch metadata boundary, `PENDING_NONBLOCKING` state, Stage verdict, Driver verdict, progress update, publication completion, or local soft block is not a reason to wait for a user `继续` message when the parent objective remains open and an executable next step exists.

When the user's instruction means continue/keep going/do not stop/until satisfied/until no further progress/solve the blocker and continue, the parent continuation lease remains active until that criterion is met or the user revokes it.

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER` remains binding, but every Stage terminal verdict must be followed in the **same turn** by successor-gate/closure/portfolio evaluation.

## 3. Identity and mandatory final footer

Resolve visible role identity before substantive work:

- researcher -> `Researcher-ID`;
- Driver -> `Driver-ID`.

Identity registration is nonblocking.

Canonical final-response contract:

`final_response_identity_policy.json`.

Freeze:

`ACTIVE_ENTERPRISE_MATH_ROLE -> EVERY_ASSISTANT_FINAL_RESPONSE_ENDS_WITH_EXACTLY_ONE_ROLE_IDENTITY_MARKER`.

Exact final marker:

- `RESEARCH_DRIVER` -> `Driver-ID: <ID> / CONTROL_PLANE`;
- `RESEARCHER` with active task -> `Researcher-ID: <ID> / <TASK_ID>`;
- `RESEARCHER` in free mode -> `Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY`;
- other direct task-research fallback -> `Researcher-ID: <ID> / TASK_RESEARCH`.

Do not use `DIRECT` as a visible researcher scope. If `Global-Knowledge-Sync:` is also emitted, the role identity marker appears immediately before it.

## 4. FREE_AXIOM_DISCOVERY

FREE Phase A receives the **primitive substrate**, not the current-result catalog and not a suggestion menu.

Canonical substrate router:

`definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`.

The integrity shell is the default FREE Phase-A rigor surface:

`research_roles/EM_FREE_RESEARCHER_PHASE_A_INTEGRITY_SHELL.md`.

The full policies:

- `FOUNDATIONAL_LOGIC.md`;
- `native_semantics_admissibility.json`;

are triggered semantic reads. Do not preload their bodies in clean FREE Phase A merely to enforce rigor.

Before candidate freeze:

- do not preload the general current-result router;
- do not preload current task/route/coordination/recent-history context;
- do not inherit unrelated `WORKING_TRUTH`;
- do not let existing tools, representations, filenames or current research vocabulary choose the question;
- do not supply suggested questions or discovery-lens menus;
- use generic exclusion categories rather than naming hidden current results.

Freeze:

`FOUNDATION_FOR_DISCOVERY != CATALOG_OF_CURRENT_ACHIEVEMENTS`.

`NO_DEFAULT_DISCOVERY_LENS_MENU`.

Candidate lifecycle:

`research_axiom_candidate_state_machine.json`.

After the candidate/no-go packet is frozen, Phase B may open current/prior work and must include tool-coverage/dedup lookup before claiming a new reusable method.

FREE does not auto-select or CLAIM scheduler work. After a candidate reaches the required audited intake state, the FREE researcher may author and PUBLISH the derived task; it remains `PUBLISHED / NEEDS_REVIEW` until Driver review.

## 5. TASK_RESEARCH hot start

For a selected task:

1. this router if not already loaded;
2. **the exact task entry**;
3. the first exact dependency required to begin;
4. work;
5. expand only when a concrete dependency is triggered.

Soft routine source-read budget before substantive work: `<= 3`.

The Common Surface is a lookup, not a default preload.

## 6. Scheduler V2 — mandatory coordination path

Canonical machine contract:

- `research_scheduler_v2.json`;
- `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md`;
- `docs/RESEARCH_SCHEDULER_V2_QUICKSTART.md`;
- `tools/research_scheduler.py`.

When an action creates, dispatches, executes, returns, hands off, reviews, or recovers an official task, use scheduler V2. Do not manufacture runtime state by editing a taskbook.

Freeze:

`PUBLISH != READY`.

`RETURN != DONE`.

`LEASE_EXPIRY -> ORPHANED`.

`EXECUTABLE_TASKBOOK -> REGISTERED_TASK_ID`.

Operational lifecycle:

`PUBLISH -> PUBLISHED -> DRIVER DISPATCH REVIEW -> READY -> CLAIM/PROGRESS -> RETURN -> DRIVER RETURN REVIEW -> DONE`.

Only `READY`, `HANDOFF_READY`, and `CHANGES_REQUESTED` are claimable. `PUBLISHED`, `RETURNED`, and `ORPHANED` require Driver action first.

A Driver that published a task may not independently approve the same publication into READY. An executor may not review its own return into DONE.

Legacy scheduler events remain migration history; new work uses V2 events.

## 7. Universal tool reuse gate

Canonical policy:

- `tool_invocation_policy.json`;
- `docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md`;
- `enterprise_toolbox_registry.json`;
- `research_method_inventory.json`;
- `tools/enterprise_toolbox.py`.

For ordinary TASK_RESEARCH, RESEARCH_DRIVER, and shared Steward work, once the problem's information structure is understood and **before constructing a new general-purpose mechanism/tool/helper calculus**, perform current tool coverage lookup.

Freeze:

`UNDERSTAND_TASK_FIRST -> TOOL_LOOKUP_SECOND`.

`EXISTING_TOOL_COVERAGE -> REUSE_OR_COMPOSE_UNLESS_EXACT_SCOPE_GAP_IS_RECORDED`.

`NEW_TOOL_DIRECTION_REQUIRES_CONFIRMED_CAPABILITY_GAP`.

Outcomes:

- `REUSE_EXISTING_TOOL`;
- `COMPOSE_EXISTING_TOOLS`;
- `EXTEND_EXISTING_TOOL`;
- `CAPABILITY_GAP_CONFIRMED`;
- `NOT_APPLICABLE`.

### Discovery-firewall timing exception

Tool lookup is delayed when the controlling protocol explicitly declares a discovery information firewall and freeze point. This includes FREE Phase A and a Driver-reviewed blind-forward taskbook. Immediately after the declared freeze, current-tool dedup becomes mandatory before method-novelty claims.

## 8. GitHub/service routing

In ChatGPT/Project execution with connected GitHub available:

`CONNECTED_GITHUB_PLUGIN = PRIMARY_REMOTE_GITHUB_PATH`.

Use the connected GitHub capability for remote repository files, search, commits, branches, PRs, issues and allowed workflow/status operations. Do not use container networking to clone/fetch remote GitHub when the connected capability can perform the action.

Detailed rules:

`docs/GITHUB_INTERACTION_BUDGET.md`.

## 9. Working Truth

`WORKING_TRUTH` is TASK execution discipline after an explicit Driver/taskbook freeze accepted for execution.

It is not a FREE Phase-A premise and not raw-candidate status. An unreviewed PUBLISHED task is not Working Truth.

## 10. Evidence integrity

Never fabricate proof, computation, hashes, validation status, novelty, provenance or tool results.

Keep claim status exact. Finite enumeration/software success is not automatically theorem proof.

Load triggered semantic policies only when the claim requires them.

## 11. Candidate / task / continuation provenance

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`.

A task opened from FREE discovery preserves audited candidate origin/ID/state.

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

A continuation requires a genuine new information gap, discriminating outcomes, kill condition, and explicit consideration of closure/another owner/free exploration.

Exact taskbook contract:

- `research_taskbook_contract.json`;
- `research_taskbook_policy.json`;
- `docs/RESEARCH_TASKBOOK_AUTHORING_AND_REVIEW.md`;
- `tools/research_taskbook.py`.

Taskbook policy PASS permits PUBLISH; only scheduler Driver review creates READY.

## 12. Remote liveness

`RESEARCH_HOT_PATH > REMOTE_PREFLIGHT`.

Do not perform universal scheduler/PR/CI/tree preflight. Do not poll merely to wait for change. Do not chase moving `main` without a concrete action.

But when an actual scheduler action is required, use V2 and leave the task in a valid registered state before the control subflow ends.

`REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED`.

## 13. Triggered control surfaces

Load only when relevant:

- scheduler V2 surfaces for actual publish/claim/return/review/orphan actions;
- Driver contract + continuity for actual Driver portfolio decisions;
- Foundation surfaces for actual Foundation routing;
- Common Surface for exact cross-owner theorem/tool/conflict lookup;
- toolbox registry/method inventory for actual method selection or harvest/dedup;
- current native router for current-result/generation lookup;
- test/Lean diagnostics for actual diagnosis;
- owner-isolation/promotion policy for actual publication/promotion work.

## 14. Persistence and publication

L1/L2/L3 research is remote-silent between semantic checkpoints by default.

`REMOTE_SILENT` describes repository traffic, not conversational inactivity.

Journal, Driver Continuity, source task/result files and source `main` have distinct roles.

Current source `main` is canonical only after applicable gates.

## 15. Promotion liveness

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 is one bounded active promotion attempt at a time. Strict `NO_NEW_MATHEMATICS` governance maintenance uses the separate bounded protocol in:

`docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`.

## 16. Current-only hot path

Normal startup files describe **current behavior/current authority only**. Historical/provenance material is retrieved only when the task explicitly needs it.
