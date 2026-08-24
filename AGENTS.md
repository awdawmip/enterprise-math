# Enterprise Math agent operating router

Status: `ACTIVE / STABLE EXECUTION ROUTER / V2.8`

`AGENTS.md` is a **current execution router**. It is not a theorem catalog, project history, old-route index, or archive.

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

## 1A. Unified task/review claim fast path

Canonical work-state control plane:

- `research_work_state_machine.json`;
- `tools/research_work_state.py`.

A generic researcher request such as `领任务` / `领取任务` is explicit scheduler intent, not an invitation to ask the user for a task id.

Freeze:

`GENERIC_TASK_CLAIM_INTENT -> SELECT_HIGHEST_ELIGIBLE_TASK -> CLAIM -> START_TASK`.

FREE Phase A is excluded from automatic task dispatch.

A Driver request such as `领审核` / `领取审核` is explicit review-queue intent.

Freeze:

`GENERIC_REVIEW_CLAIM_INTENT -> SELECT_HIGHEST_ELIGIBLE_REVIEW -> REVIEW_CLAIM -> START_REVIEW`.

The task-issuing Driver has no exclusive review lock:

`TASK_ISSUER != REQUIRED_REVIEWER`.

Prefer cross-Driver review when a comparable pending review exists; same-Driver review remains a labeled fallback, not a blocker.

A Driver-approved dispatchable taskbook is published to the shared work state in the same turn:

`TASKBOOK_DISPATCH_PASS -> SAME_TURN_TASK_PUBLISH`.

A completed research task returns to the shared work state rather than through the user:

`RESEARCH_DONE -> SAME_TURN_REVIEW_REQUEST`.

The user need not relay task ids, review ids, return prompts, logs, or review targets between conversations.

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

## 4. FREE_AXIOM_DISCOVERY

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

## 5. TASK_RESEARCH hot start

For a selected task:

1. this router if not already loaded;
2. the **exact task entry**;
3. the first exact dependency required to begin;
4. work;
5. expand only when a concrete dependency is triggered.

Soft routine source-read budget before substantive work: `<= 3`.

The Common Surface is a lookup, not a default preload.

## 6. Universal tool reuse gate

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
- a TASK research taskbook that explicitly requires blind-forward / source-whitelist isolation until a named raw candidate/no-go freeze.

Before that declared freeze, the current toolbox/method catalog is hidden as a discovery prior and its tool names must not be exposed merely to enforce reuse. The researcher obeys the exact task-local whitelist/firewall.

Immediately after the declared freeze, the same lookup becomes mandatory before method-novelty claims or a new tool continuation. The frozen result is preserved even when it collides with an existing tool; deduplication is classification, not retroactive steering.

An ordinary TASK may not self-declare blindness simply to skip the reuse gate. The exception must come from the controlling role/task contract.

The lookup is selective rather than a universal preload: query by the actual need. When a local checkout is available, `python tools/enterprise_toolbox.py coverage <need>` searches curated tool families, harvested methods and the current executable Python surface without importing modules.

## 7. GitHub/service routing

In ChatGPT/Project execution with the connected GitHub capability available:

`CONNECTED_GITHUB_PLUGIN = PRIMARY_REMOTE_GITHUB_PATH`.

Use the GitHub connector/plugin for remote repository files, search, commits, branches, PRs, issues and allowed workflow/status operations.

Do **not** use ChatGPT/container networking to clone GitHub, fetch raw GitHub URLs, or reproduce remote GitHub access when the connected capability can perform the action.

A pre-existing local checkout may be used for actual local execution/tests. It is not the fallback transport for remote synchronization.

Do not repeatedly retry or report a known unavailable local GitHub network route. A remote-access problem is surfaced only when the connected GitHub route itself cannot complete a required action.

Detailed remote rules:

`docs/GITHUB_INTERACTION_BUDGET.md`.

## 8. Working Truth

`WORKING_TRUTH` is TASK execution discipline after an explicit Driver/taskbook freeze.

It is not a FREE Phase-A premise and not raw-candidate status.

## 9. Evidence integrity

Never fabricate proof, computation, hashes, validation status, novelty, provenance or tool results.

Keep claim status exact. Finite enumeration/software success is not automatically theorem proof.

Load triggered semantic policies only when the claim requires them:

- `FOUNDATIONAL_LOGIC.md` / `foundational_logic.json` — foundation-facing inverse/recovery reasoning;
- `native_semantics_admissibility.json` — native/intrinsic/base-world claims;
- geometry/refoundation policy — geometry/refoundation tasks.

## 10. Candidate / task / continuation provenance

`RAW_AXIOM_CANDIDATE != WORKING_TRUTH != CANONICAL_FOUNDATION`.

A task opened from FREE discovery preserves audited candidate origin/ID/state.

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

A continuation requires a genuine new information gap, discriminating outcomes, kill condition, and explicit consideration of closure/another owner/free exploration.

Exact taskbook contract:

- `research_taskbook_contract.json`;
- `research_taskbook_policy.json`;
- `docs/RESEARCH_TASKBOOK_AUTHORING_AND_REVIEW.md`;
- `tools/research_taskbook.py`.

## 11. Remote liveness

`RESEARCH_HOT_PATH > REMOTE_PREFLIGHT`.

Do not perform universal scheduler/Issue/PR/CI/tree preflight.

Do not poll CI/review/status merely to wait for change.

Do not chase moving `main` without a concrete action.

Tool/scheduler/CI availability is not a mathematical `HARD_BLOCK`.

`REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED`.

## 12. Triggered control surfaces

Load only when relevant:

- unified work-state/scheduler/Relay/Foundation surfaces for actual coordination actions;
- Driver contract + continuity for actual Driver portfolio decisions;
- Common Surface for exact cross-owner theorem/tool/conflict lookup;
- toolbox registry/method inventory for actual method selection or method-harvest/dedup;
- current native router for current-result/generation lookup;
- test/Lean diagnostics for actual diagnosis;
- owner-isolation/promotion policy for actual publication/promotion work.

## 13. Persistence and publication

L1/L2/L3 research is remote-silent between semantic checkpoints by default.

`REMOTE_SILENT` describes repository traffic, **not conversational inactivity**.

Journal, Driver Continuity, source task/result files and source `main` have distinct roles.

Current source `main` is canonical only after applicable gates.

## 14. Promotion liveness

`READY_PR != PROMOTION_LANE_LEASE`.

Mathematical L4 is one bounded active promotion attempt at a time.

Strict `NO_NEW_MATHEMATICS` governance maintenance uses the separate bounded protocol in:

`docs/GOVERNANCE_MAINTENANCE_LIVENESS.md`.

## 15. Current-only hot path

Normal startup files describe **current behavior/current authority only**.

Historical/provenance material is retrieved only when the task explicitly needs history/provenance/comparison.
