# Enterprise Math agent operating router

Status: `ACTIVE / STABLE EXECUTION ROUTER / V2.9`

`AGENTS.md` is a **current execution router**. It is not a theorem catalog, project history, old-route index, or archive.

## 1. Mode resolution

Current explicit user instruction controls scope.

Current research modes:

- `EM_FREE_RESEARCHER` -> `FREE_AXIOM_DISCOVERY`;
- explicit user task / Driver handoff / approved taskbook / scheduler dispatch -> `TASK_RESEARCH`;
- explicit Driver activation -> `RESEARCH_DRIVER`.

Exact role/execution authority:

- `research_architecture.json`;
- `research_role_policy.json`;
- `research_identity_state_machine.json`;
- `research_execution_state_machine.json`.

For `TASK_RESEARCH`, task authority and execution readiness are separate. A valid direct user task, approved taskbook, scheduler task, or Driver dispatch envelope may establish task authority; none of them by itself means substantive work is authorized.

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

When the user's instruction semantically means continue/keep going/do not stop/until satisfied/until no further progress/solve the blocker and continue, the parent continuation lease remains active until that parent criterion is met or the user revokes it.

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER` remains binding, but every Stage terminal verdict must be followed in the **same turn** by successor-gate/closure/portfolio evaluation. Closing one route does not close the parent user objective.

Before ending a nonterminal turn, if the parent objective is incomplete and another executable action exists, execute it now.

## 3. Identity and mandatory final footer

Resolve the visible role identity before substantive work:

- researcher -> `Researcher-ID`;
- Driver -> `Driver-ID`.

Identity registration is nonblocking.

Canonical final-response contract:

`final_response_identity_policy.json`.

Freeze:

`ACTIVE_ENTERPRISE_MATH_ROLE -> EVERY_ASSISTANT_FINAL_RESPONSE_ENDS_WITH_EXACTLY_ONE_ROLE_IDENTITY_MARKER`.

This applies even to short status replies, readiness/completion receipts, handoffs, blocked/no-go conclusions, refusals, and ordinary research answers. Commentary/progress/tool-call messages are not final responses and do not need the footer.

Exact final marker:

- `RESEARCH_DRIVER` -> `Driver-ID: <ID> / CONTROL_PLANE`;
- `RESEARCHER` with an active task -> `Researcher-ID: <ID> / <TASK_ID>`;
- `RESEARCHER` in free mode without a task -> `Researcher-ID: <ID> / FREE_AXIOM_DISCOVERY`;
- other direct task-research fallback -> `Researcher-ID: <ID> / TASK_RESEARCH`.

Do not use `DIRECT` as a visible researcher scope. Registration state `REGISTER_PENDING` never suppresses the marker.

If `Global-Knowledge-Sync:` is also emitted, the role identity marker appears immediately before it and the sync line remains last.

## 4. TASK_RESEARCH execution-state gate

Canonical contract:

- `research_execution_state_machine.json`;
- `docs/RESEARCH_EXECUTION_STATE_MACHINE.md`;
- `tools/research_execution_state.py`.

Every concrete `TASK_RESEARCH` run normalizes its task authority into one execution spec:

`task_id + authority_kind + authority_ref + execution_gates`.

Allowed task-authority kinds are:

- `OFFICIAL_TASKBOOK`;
- `DIRECT_USER_TASK`;
- `SCHEDULER_TASK`;
- `DRIVER_DISPATCH_ENVELOPE`.

Freeze:

`TASK_AUTHORITY_READY != EXECUTION_READY`.

`STATE_PERMISSION + ALL_GUARDING_GATES_SATISFIED -> ACTION_ALLOWED`.

Before any mathematical source read or mathematical derivation:

1. resolve the concrete task authority;
2. normalize explicit task-local startup/process/source-visibility/verdict/return constraints into `execution_gates`;
3. resolve Researcher-ID;
4. if any `PRE_MATH` gate exists, enter `PRE_MATH_GATES_PENDING`;
5. satisfy and verify every PRE_MATH gate;
6. reach `EXECUTION_READY`;
7. only then begin substantive mathematics.

A taskbook `READY`, scheduler `CLAIMED`, Driver relay, direct task acceptance, or chat statement “done” never skips these steps.

Every normalized gate starts `PENDING`. An action remains blocked until every gate whose `must_precede` guards that action is `SATISFIED`, even if the current state otherwise permits it.

Special ordered actions:

- `POST_FREEZE_SOURCE_READ` = read sources deliberately withheld until a named raw/independent/Phase-A freeze. It inherits the generic `MATHEMATICAL_SOURCE_READ` startup guard and may also be blocked by a later Phase-A-freeze gate.
- `VERDICT_FREEZE` = freeze/select the task's primary/final terminal mathematical classification. A checker/audit required before final verdict must guard this action.
- `RETURN_WRITE` = persist the final return. A final materialization/checker gate must guard this action.

A failed mandatory pre-math publication/liveness gate is an **execution non-start**, not a mathematical rejection.

`HANDOFF_READY` pauses a same-conversation execution. Resume the same execution only after reconciling the durable handoff and gate ledger. A new conversation binds a new execution instance.

A direct-user task that has no applicable Driver-review step may end as `DELIVERED_UNREVIEWED`; this means only that the execution return was delivered, not that Driver accepted or mathematical truth was promoted.

If chat/runtime continuity becomes unreliable, enter `RECOVERY_REQUIRED` and reconstruct the last legal state **and gate ledger** from durable evidence. Do not infer execution completion from chat text.

## 5. FREE_AXIOM_DISCOVERY

FREE Phase A receives the **primitive substrate**, not the current-result catalog and not a suggestion menu.

Canonical substrate router:

`definitions/00_FREE_AXIOM_DISCOVERY_SUBSTRATE.md`.

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

After the candidate/no-go packet is frozen, Phase B may open current/prior work and must include the tool-coverage/dedup lookup before claiming a new reusable method.

## 6. TASK_RESEARCH hot start

For a selected task:

1. this router if not already loaded;
2. the **exact task authority** (current user instruction, taskbook, scheduler task, or Driver envelope) and execution-control metadata only;
3. normalize/validate the execution spec and resolve identity;
4. satisfy all `PRE_MATH` gates and reach `EXECUTION_READY`;
5. read the first exact currently-visible mathematical dependency required to begin;
6. work;
7. if the task has a blind/source-whitelist phase boundary, freeze the declared Phase-A/raw/independent artifact before any `POST_FREEZE_SOURCE_READ`;
8. expand only when a concrete dependency or satisfied source-visibility gate permits it.

Soft routine source-read budget before substantive work: `<= 3` **control-plane/task-authority reads**. A task-local `PRE_MATH` firewall overrides this budget and forbids mathematical-source reads until the gate is satisfied.

The Common Surface is a lookup, not a default preload.

For an official taskbook, Driver dispatch/re-dispatch uses the single composite gate:

`python tools/research_control_gate.py audit research_tasks/<task>.md`.

For a direct user/scheduler/Driver-envelope task without an official taskbook, normalize the current authority into the runtime spec and validate it with `tools/research_execution_state.py audit-spec`, supplying the authority body when prose-gate detection is needed.

## 7. Universal tool reuse gate

Canonical policy:

- `tool_invocation_policy.json`;
- `docs/ENTERPRISE_TOOL_INVOCATION_PROTOCOL.md`;
- `enterprise_toolbox_registry.json`;
- `research_method_inventory.json`;
- `tools/enterprise_toolbox.py`.

For ordinary `TASK_RESEARCH`, `RESEARCH_DRIVER`, and shared Steward work, once the problem's information structure is understood and **before constructing a new general-purpose mechanism/tool/helper calculus**, perform a current tool-coverage lookup.

Freeze:

`UNDERSTAND_TASK_FIRST -> TOOL_LOOKUP_SECOND`.

`EXISTING_TOOL_COVERAGE -> REUSE_OR_COMPOSE_UNLESS_EXACT_SCOPE_GAP_IS_RECORDED`.

`NEW_TOOL_DIRECTION_REQUIRES_CONFIRMED_CAPABILITY_GAP`.

The coverage outcome is one of:

- `REUSE_EXISTING_TOOL`;
- `COMPOSE_EXISTING_TOOLS`;
- `EXTEND_EXISTING_TOOL`;
- `CAPABILITY_GAP_CONFIRMED`;
- `NOT_APPLICABLE`.

Do not create a new tool family merely because the same mechanism appears under another historical name, route, application domain or filename. Use aliases, specializations, domain facades or subtools.

Every Driver/Steward-accepted research return must receive a method-harvest classification so reusable methods flow back into the shared inventory instead of remaining hidden in route-local artifacts.

### Discovery-firewall timing exception

Tool lookup is delayed when the controlling research protocol explicitly declares a discovery information firewall and a freeze point.

This includes:

- FREE Phase A;
- a TASK research taskbook that explicitly requires blind-forward / source-whitelist isolation until a named raw candidate/no-go/independent freeze.

For TASK_RESEARCH, such delayed sources are represented as `POST_FREEZE_SOURCE_READ` and remain machine-blocked until the declared freeze gate is satisfied.

Before that declared freeze, the current toolbox/method catalog is hidden as a discovery prior and its tool names must not be exposed merely to enforce reuse. The researcher obeys the exact task-local whitelist/firewall.

Immediately after the declared freeze, the same lookup becomes mandatory before method-novelty claims or a new tool continuation. The frozen result is preserved even when it collides with an existing tool; deduplication is classification, not retroactive steering.

An ordinary TASK may not self-declare blindness simply to skip the reuse gate. The exception must come from the controlling role/task contract.

The lookup is selective rather than a universal preload: query by the actual need. When a local checkout is available, `python tools/enterprise_toolbox.py coverage <need>` searches curated tool families, harvested methods and the current executable Python surface without importing modules.

## 8. GitHub/service routing

In ChatGPT/Project execution with the connected GitHub capability available:

`CONNECTED_GITHUB_PLUGIN = PRIMARY_REMOTE_GITHUB_PATH`.

Use the GitHub connector/plugin for remote repository files, search, commits, branches, PRs, issues and allowed workflow/status operations.

Do **not** use ChatGPT/container networking to clone GitHub, fetch raw GitHub URLs, or reproduce remote GitHub access when the connected capability can perform the action.

A pre-existing local checkout may be used for actual local execution/tests. It is not the fallback transport for remote synchronization.

Do not repeatedly retry or report a known unavailable local GitHub network route. A remote-access problem is surfaced only when the connected GitHub route itself cannot complete a required action.

Detailed remote rules:

`docs/GITHUB_INTERACTION_BUDGET.md`.

## 9. Working Truth

`WORKING_TRUTH` is TASK execution discipline after an explicit Driver/taskbook freeze.

It is not a FREE Phase-A premise and not raw-candidate status.

## 10. Evidence integrity

Never fabricate proof, computation, hashes, validation status, novelty, provenance or tool results.

Keep claim status exact. Finite enumeration/software success is not automatically theorem proof.

Load triggered semantic policies only when the claim requires them:

- `FOUNDATIONAL_LOGIC.md` / `foundational_logic.json` — foundation-facing inverse/recovery reasoning;
- `native_semantics_admissibility.json` — native/intrinsic/base-world claims;
- geometry/refoundation policy — geometry/refoundation tasks.

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

## 12. Remote liveness

`RESEARCH_HOT_PATH > REMOTE_PREFLIGHT`.

Do not perform universal scheduler/Issue/PR/CI/tree preflight.

Do not poll CI/review/status merely to wait for change.

Do not chase moving `main` without a concrete action.

Tool/scheduler/CI availability is not a mathematical `HARD_BLOCK`.

`REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED`.

A task-declared remote `PRE_MATH` gate is different: it is an explicit execution-legality prerequisite for that concrete run, not generic remote preflight and not a mathematical hard dependency.

## 13. Triggered control surfaces

Load only when relevant:

- execution-state protocol for every concrete `TASK_RESEARCH` startup/recovery/action-gate decision;
- scheduler/Relay/Foundation surfaces for actual coordination actions;
- Driver contract + continuity for actual Driver portfolio decisions;
- Common Surface for exact cross-owner theorem/tool/conflict lookup;
- toolbox registry/method inventory for actual method selection or method-harvest/dedup;
- current native router for current-result/generation lookup;
- test/Lean diagnostics for actual diagnosis;
- owner-isolation/promotion policy for actual publication/promotion work.

## 14. Persistence and publication

L1/L2/L3 research is remote-silent between semantic checkpoints by default.

`REMOTE_SILENT` describes repository traffic, **not conversational inactivity**.

Journal, Driver Continuity, source task/result files and source `main` have distinct roles.

Current source `main` is canonical only after applicable gates.

## 15. Promotion liveness

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 is one bounded active promotion attempt at a time.

Strict `NO_NEW_MATHEMATICS` governance maintenance uses the separate bounded protocol in:

`docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`.

## 16. Current-only hot path

Normal startup files describe **current behavior/current authority only**.

Historical/provenance material is retrieved only when the task explicitly needs history/provenance/comparison.
