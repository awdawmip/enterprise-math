# Enterprise Math agent operating router

Status: `ACTIVE / STABLE EXECUTION ROUTER / V2.10`

`AGENTS.md` is a **current execution router**. It is not a theorem catalog, project history, old-route index, or archive.

## 1. Mode resolution

Current explicit user instruction controls scope.

Current research modes:

- `EM_FREE_RESEARCHER` -> `FREE_AXIOM_DISCOVERY`;
- explicit user task / Driver handoff / approved taskbook / Scheduler V2 `CLAIM` or `ADOPT` -> `TASK_RESEARCH`;
- explicit Driver activation -> `RESEARCH_DRIVER`.

Exact role authority:

- `research_architecture.json`;
- `research_role_policy.json`;
- `research_identity_state_machine.json`.

## 1A. Scheduler V2 control plane

Canonical runtime authority:

- `research_scheduler.json`;
- `docs/RESEARCH_SCHEDULING_PROTOCOL.en.md`;
- `docs/RESEARCH_SCHEDULER_V2_QUICKSTART.md`;
- `tools/research_scheduler.py`;
- `tools/research_scheduler_event.py`;
- live Research Dispatch Board Issue #240.

For an actual coordination action, materialize current Scheduler V2 state before routing. Do not infer task state from chat memory, a taskbook filename, an open PR, or the historical branch ledger.

Before **any new execution generation** for an exact task — including a direct user reissue, new researcher identity, owner-branch start, execution stamp, Scheduler `CLAIM`, or orphan `ADOPT` — reconcile the durable frontier first. Resolve the exact task id/taskbook ref, declared owner branch, expected return/evidence paths and available durable branch/commit/manifest/checker state; then classify exactly one of `VERIFIED_COMPLETE`, `IN_PROGRESS_RECOVERABLE`, `UNFINISHED`, or `NEVER_STARTED`.

Freeze:

`TASKBOOK_POLICY_PASS != SCHEDULER_READY`.

`PUBLISH != READY`.

`SUBMIT != DONE`.

`LEASE_EXPIRY -> ORPHANED`, not silent `HANDOFF_READY`.

`ORPHANED -> ADOPT`, not ordinary `CLAIM`.

`BEFORE_REISSUE -> RECONCILE_DURABLE_FRONTIER`.

`VERIFIED_COMPLETE -> CONSUME_NOT_REDISPATCH`.

`IN_PROGRESS_RECOVERABLE -> RESUME_SAME_DURABLE_FRONTIER`.

`UNFINISHED -> PRESERVE_VALID_EVIDENCE_AND_RESTART_ONLY_MISSING_WORK`.

`NEVER_STARTED -> NORMAL_DISPATCH`.

`PUBLISHER != PUBLICATION_REVIEWER` and `EXECUTOR != RETURN_REVIEWER`.

Generic intent routing is machine-defined in `research_scheduler.json`:

- generic researcher task claim -> select highest eligible `NEEDS_DISPATCH`, reconcile the exact durable frontier, emit `CLAIM(frontier_class=NEVER_STARTED, frontier_ref=...)` only if it is genuinely never started, resolve identity, start;
- generic Driver review claim -> select highest eligible non-self `NEEDS_REVIEW`, emit `REVIEW_CLAIM`, start review;
- researcher/FREE task publication -> `PUBLISH -> REVIEW_PENDING`; a different Driver must `APPROVE` before runtime `READY`;
- orphan recovery -> inspect `ORPHAN_RECOVERY`, rebuild the durable frontier, then `ADOPT` only `IN_PROGRESS_RECOVERABLE`/`UNFINISHED` work with recovery provenance;
- stalled-conversation recovery -> rebuild the durable frontier, classify the predecessor, release a stale live claim if needed, then `ADOPT`/resume recoverable work or consume the verified-complete result.

FREE Phase A remains outside automatic scheduler claiming. After the relevant discovery freeze, a FREE researcher may publish a concrete proposal into `REVIEW_PENDING`; this does not grant Working Truth, dispatch authority, or self-approval.

V2 direct `DONE` is forbidden. Execution finishes with `SUBMIT`; scheduler completion requires a different Driver's `REVIEW` verdict.

A stale conversation or ordinary continuation is **not** itself a fresh independent replication. A new clean independent child is created only when the controlling independence protocol explicitly requires a distinct run.

## 2. Active-turn continuation liveness

Canonical contract:

- `active_turn_liveness.json`;
- `docs/ACTIVE_TURN_CONTINUATION_LIVENESS.md`.

Maintain:

`PARENT_USER_OBJECTIVE -> CURRENT_SUBFLOW -> NEXT_EXECUTABLE_ACTION`.

Freeze:

`SUBFLOW_COMPLETE != USER_OBJECTIVE_COMPLETE`.

`DETERMINISTIC_NEXT_STEP_EXISTS -> CONTINUE_IN_SAME_TURN`.

`PROGRESS_PROSE != VERIFIED_LIVENESS`.

`TASK_CLAIM_LEASE != CONVERSATION_LIVENESS_LEASE`.

`NEW_EXECUTION_GENERATION -> DURABLE_FRONTIER_RECONCILIATION_FIRST`.

A semantic checkpoint, journal write, tool return, recoverable tool error, PR/branch metadata boundary, `PENDING_NONBLOCKING` state, Stage verdict, Driver verdict, progress update, publication completion, or local soft block is not a reason to wait for a user `继续` message when the parent objective remains open and an executable next step exists.

When the user's instruction semantically means continue/keep going/do not stop/until satisfied/until no further progress/solve the blocker and continue, the parent continuation lease remains active until that parent criterion is met or the user revokes it.

A predecessor conversation with **10 continuous minutes and no new verifiable action** is stale for control purposes even if its ordinary Scheduler task claim lease has not expired. Do not wait for that chat or treat progress prose as a heartbeat. Rebuild the durable frontier from externally verifiable branch/commit/taskbook/return/PR/Scheduler/checker evidence, then classify exactly one of `VERIFIED_COMPLETE`, `IN_PROGRESS_RECOVERABLE`, `UNFINISHED`, or `NEVER_STARTED`.

For a stale live task claim, Driver/SYSTEM may use Scheduler V2 `ORPHAN` with reason `STALE_CONVERSATION_NO_VERIFIABLE_ACTION_10M` and a concrete recovery/evidence ref before the ordinary claim lease expires; a replacement execution resumes with `ADOPT` and a fresh execution identity. `VERIFIED_COMPLETE` work is consumed, not re-executed.

Freeze:

`10_MIN_NO_VERIFIABLE_ACTION -> DURABLE_FRONTIER_RECOVERY`, not `WAIT_FOR_24H_TASK_LEASE`.

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER` remains binding, but every Stage terminal verdict must be followed in the **same turn** by successor-gate/closure/portfolio evaluation. Closing one route does not close the parent user objective.

Before ending a nonterminal turn, if the parent objective is incomplete and another executable action exists, execute it now.

## 3. Identity and mandatory final footer

Resolve the visible role identity before substantive work, but for an existing task do not create a new execution identity until durable-frontier reconciliation says a new/recovery execution is actually required:

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

For a selected or explicitly reissued task:

1. this router if not already loaded;
2. the **exact task entry/taskbook ref**;
3. reconcile the declared owner branch, execution stamp, expected return/evidence paths and other durable frontier for that exact task;
4. classify `VERIFIED_COMPLETE / IN_PROGRESS_RECOVERABLE / UNFINISHED / NEVER_STARTED`;
5. consume completed work, recover the same frontier, restart only missing work, or create a new execution only according to that classification;
6. load the first exact dependency required to continue;
7. work;
8. expand only when a concrete dependency is triggered.

Soft routine source-read budget before substantive work: `<= 3`; the durable-frontier intake check is control-plane reconciliation, not permission to preload hidden mathematical source beyond the task's information firewall.

For a blind/independent task, reconcile existence/status metadata without reading withheld mathematical content before its freeze. Recovery must preserve the task's blindness protocol.

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

Do not perform universal scheduler/Issue/PR/CI/tree preflight. For an actual scheduler coordination action, however, current V2 materialized state is the authority and must be read before mutation. For an explicitly selected/reissued task, the narrow durable-frontier intake reconciliation is mandatory and is not the prohibited universal preflight.

Do not poll CI/review/status merely to wait for change. A concrete promotion/merge/control decision may inspect current status as its evidence gate; `PENDING_NONBLOCKING` then returns control to other executable work.

Do not chase moving `main` without a concrete action.

Tool/scheduler/CI availability is not a mathematical `HARD_BLOCK`.

`REMOTE_SUBFLOW_TERMINATED != PARENT_TASK_TERMINATED`.

A stale predecessor chat is not remote liveness. Once the 10-minute no-verifiable-action threshold is met, recover from durable state rather than continuing to wait on that chat.

## 12. Triggered control surfaces

Load only when relevant:

- Scheduler V2/Relay/Foundation surfaces for actual coordination actions;
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
