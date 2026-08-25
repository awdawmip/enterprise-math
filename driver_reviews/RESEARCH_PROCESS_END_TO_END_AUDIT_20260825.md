# Driver Review — Enterprise Math End-to-End Research Process Audit

Status: `AUDIT_COMPLETE / MATERIAL_CONTROL-GAPS_FOUND / CURRENT_FLOW_NOT_YET_END-TO-END-CLOSED`

Date: `2026-08-25`

Driver-ID: `EM-DVR-K7Q4N8 / CONTROL_PLANE`

Audit base:
`main@c28d8541deacaea6047d62d34e6778737cd1412f`

Classification:
`NO_NEW_MATHEMATICS / CONTROL-PLANE AUDIT`

## 1. Audit scope

This audit traces the entire research lifecycle rather than reviewing one policy file in isolation:

`USER/PARENT OBJECTIVE -> ROLE/IDENTITY -> TASK OR FREE DISCOVERY -> PUBLICATION/REGISTRATION -> DISPATCH -> OWNER CLAIM -> SESSION -> EVIDENCE/FRONTIER -> RETURN -> REVIEW -> PROMOTION/BACKFLOW -> CLOSURE/SUCCESSOR -> FINAL RESPONSE -> DURABLE KNOWLEDGE`

The audit cross-checked current router, role policy, identity state machine, free-candidate state machine, taskbook/publication contracts, canonical task registry, legacy scheduler and runtime tools, active-turn liveness, owner isolation, branch lifecycle, Foundation backflow, tool-reuse controls, return/review surfaces, and CI workflows.

## 2. Executive verdict

The research process has strong principles and several well-designed local controls, especially:

- explicit role separation;
- blind FREE Phase A and post-freeze dedup;
- task publication distinct from Working Truth and canonical promotion;
- owner lease distinct from session liveness;
- durable-frontier recovery instead of replay;
- continuation liveness and final-channel gate;
- exact task lineage and successor-gate requirements;
- legacy scheduler cutover protection;
- strong evidence-integrity language.

However, the current system is **not yet end-to-end closed**. The principal defect is that recently added task publication/registration is not operationally joined to dispatch, claim, runtime transition, review, closure, and promotion. Several older control surfaces still name the frozen scheduler as task-definition authority, use incompatible state vocabularies, or pin conversation-specific Driver identities into canonical policy.

Therefore the accurate system verdict is:

`LOCAL_CONTROLS_STRONG`

`END_TO_END_CONTROL_GRAPH_INCOMPLETE`

`NEW_RESEARCHER_PUBLISHED_TASK_PRESERVABLE_BUT_NOT_CANONICALLY_DISPATCHABLE`

`LEGACY_REGISTERED_TASK_EXECUTION_MAY_CONTINUE`

## 3. Severity model

- `P0`: can create orphaned, falsely executable, unclaimable, or authority-inconsistent work.
- `P1`: can lose provenance, permit divergent state, or make review/promotion non-reproducible.
- `P2`: increases operator error, ambiguity, duplicate work, or maintenance burden.

## 4. P0 findings — must be repaired before claiming full closure

### RP-AUD-001 — Publication and dispatch are disconnected

The canonical registry can publish a task as `CLAIMABLE`, but `tools/research_scheduler.py` loads and validates only the static task list in the frozen `research_scheduler.json`. A newly registered task is unknown to scheduler selection, claim, renewal, handoff, freeze, and completion operations.

Impact:

- `PUBLISHED/CLAIMABLE` does not imply actually claimable;
- researcher publication can preserve a task but cannot enter the canonical owner-lease lane;
- no single source can answer both “does this task exist?” and “who may execute it?”;
- the central user requirement—no orphan task—remains only partially achieved.

Required repair:

1. Build one combined dispatch view from registry records plus explicit legacy-baseline records.
2. Require every scheduler event to resolve to either a live registry record or a cryptographically verified legacy baseline task.
3. Add a temporary non-executable registry state until the bridge is live; do not label a task `CLAIMABLE` before dispatch compatibility is proven.
4. Add an end-to-end test: publish -> select -> claim -> renew -> handoff -> resume -> return -> close.

### RP-AUD-002 — Publication is not transactional

`tools/research_task_registry.py publish` mutates the taskbook before final validation, writes the registry, then mutates the taskbook again to add the registry pin. Audit failure or interruption can leave a taskbook that looks published without a registry record, or a registry record whose taskbook/pin was not finalized.

The registry is also rewritten as one unlocked JSON document. Concurrent publishers can overwrite one another. `--replace` replaces history instead of preserving an immutable event trail.

Required repair:

- validate a staged copy first;
- perform compare-and-swap against expected registry blob/version;
- commit taskbook and registry as one publication transaction or use an append-only publication event followed by deterministic materialization;
- never expose `PUBLISHED_REGISTERED` before the transaction commits;
- preserve superseded records and publication events rather than destructive replacement.

### RP-AUD-003 — Runtime trusts caller assertions instead of canonical state

`tools/research_runtime.py` accepts caller-supplied dictionaries/booleans for registration, legacy status, owner-claim validity, branch agreement, session freshness, and durable frontier. It does not itself resolve the canonical registry, taskbook source pin, frozen legacy baseline, Issue #240 events, remote branch HEAD, or execution stamp.

Impact:

- the machine can report a coherent state from fabricated or stale inputs;
- `LEGACY_BASELINE_REGISTERED` is assertable rather than proven;
- terminal registry states can be treated as merely “registered” without an execution-state distinction;
- runtime completion does not automatically update registry lifecycle.

Required repair:

- separate pure evaluator from canonical resolver;
- make production entrypoint load and verify source data itself;
- distinguish `EXISTS`, `EXECUTABLE`, `CLAIMABLE`, `ACTIVE`, `REVIEW`, and `TERMINAL` registration classes;
- make runtime transitions emit durable events that materialize registry state.

### RP-AUD-004 — One universal runtime incorrectly requires a task for taskless modes

The unified runtime is declared for `TASK_RESEARCH`, `FREE_AXIOM_DISCOVERY`, `RESEARCH_DRIVER`, and shared Steward work, but its canonical model unconditionally requires `TASK_REGISTRATION` and `TASK`.

FREE Phase A and pure Driver/Steward control-plane work can legitimately begin from a parent objective without an official task. The present model either forces synthetic/fake tasks or makes those modes formally invalid.

Required repair:

Use a tagged root object:

`PARENT_OBJECTIVE -> {REGISTERED_TASK | FREE_DISCOVERY_SESSION | CONTROL_PLANE_SESSION}`

Only the registered-task branch should require task registration and owner claim. All branches should converge at durable frontier, next action, terminal scope, and final gate.

### RP-AUD-005 — Canonical policies contain conversation-specific Driver identity

Multiple canonical machine/policy surfaces pin `EM-DVR-K7Q4N8`, while `research_architecture.json` also contains `EM-DRIVER-01`. This conflicts with the role policy that Driver activation is explicit, current-conversation scoped, and not inferred by default.

The identity state machine points to `projects/enterprise-math/CHATGPT_RESEARCH_IDENTITIES.json` in GLOBAL_KNOWLEDGE_V1, but that canonical path was not present during this audit.

Impact:

- a past session identity appears to authorize future sessions;
- multiple Driver identifiers create split authority;
- publisher identity cannot be validated against the declared registry;
- canonical documents become stale whenever the active Driver changes.

Required repair:

- remove all concrete active IDs from canonical policy;
- use placeholders such as `RESOLVED_DRIVER_ID`;
- maintain one real identity registry with stable conversation/execution handle separate from visible role marker;
- validate publisher/reviewer IDs against it;
- keep session activation evidence outside canonical timeless policy.

## 5. P1 findings — provenance and lifecycle integrity

### RP-AUD-006 — State vocabularies diverge

The publication registry uses states including `REGISTERED_DRAFT`, `AUDIT_FAILED`, `CLAIMABLE`, `RETURNED_FOR_REVIEW`, `PARKED`, and `SUPERSEDED`. The scheduling protocol still uses `BACKLOG`, `READY`, `CLAIMED`, `IN_PROGRESS`, `DONE`, `REVIEW`, and `FROZEN`. Foundation backflow and branch lifecycle use additional incompatible terms.

Required repair:

Define one canonical lifecycle and explicit projections for task existence, execution, review, promotion, and branch state. Do not reuse one field for all dimensions.

Recommended factorization:

- `registration_state`;
- `execution_state`;
- `review_state`;
- `promotion_state`;
- `branch_state`;
- `terminal_reason`.

### RP-AUD-007 — Authority declarations still point to the frozen scheduler

`research_common_surface.json`, scheduling/branch-lifecycle documents, and `foundation_backflow.json` still name `research_scheduler.json` as current task-definition/dispatch authority or require synchronization among taskbook, scheduler, and Issue #240. This contradicts the new canonical registry and frozen scheduler cutover.

Required repair:

Freeze one authority matrix:

- task existence/content pin: task registry + taskbook;
- owner lease/runtime event: Issue #240 or successor event store;
- branch truth: remote branch HEAD + owner-scope contract;
- review verdict: review registry/event;
- promotion truth: bounded promotion-lane event;
- canonical mathematics: gated main.

Then make all prose and machine surfaces derive from this matrix.

### RP-AUD-008 — Return and review are prose, not lifecycle transactions

Research returns and Driver reviews contain strong human reasoning, exact hashes, verdicts, and scope boundaries, but there is no universal machine-readable return/review schema that transitions the task to `RETURNED_FOR_REVIEW`, records reviewer independence, closes/reopens the task, releases owner lease, triggers method harvest, or opens a successor gate.

Required repair:

Add:

- `research_return.schema.json`;
- `research_review.schema.json`;
- immutable return/review event IDs;
- exact task/registry/source/branch/commit links;
- verdict, accepted scope, rejected scope, evidence level, independence declaration, method-harvest result, successor verdict, and terminal transition.

### RP-AUD-009 — Promotion/backflow lacks one machine owner and idempotent transition

Promotion rules are strong in prose (`READY_PR != PROMOTION_LANE_LEASE`, bounded L4, no automatic Foundation promotion), but no dedicated promotion state machine/registry was found that prevents duplicate promotion, proves lease ownership, or atomically joins review acceptance, PR/commit, main integration, status update, and Foundation backflow.

Required repair:

Create an idempotent promotion transaction keyed by accepted result ID. A result may have at most one active promotion lease and one canonical promotion event per scope/version.

### RP-AUD-010 — Parent objective and candidate references are not integrity-checked

Task publication requires a nonempty `parent_objective_id`, but there is no canonical objective registry or foreign-key validation. Candidate IDs and audited candidate states are carried as strings without a canonical candidate record store. Existing mathematical `lineage.json` records source/novelty lineage, not operational parent-objective/task/candidate/review lineage.

Required repair:

Create a lightweight objective/candidate graph or append-only event index and validate:

- parent objective exists;
- continuation parent task exists;
- candidate exists and is in the stated audited state;
- no lineage cycle;
- no duplicate active task for the same unresolved frontier unless explicitly independent replication.

### RP-AUD-011 — Branch scope isolation is detectable but not routinely enforced

`tools/audit_branch_lifecycle.py` can identify branch scope drift using path allowances, but normal PR CI does not run a task-aware branch-scope check. Static `branch_governance_overrides.json` is another manual authority surface and is not joined to registry publication IDs or owner events.

Required repair:

At PR time, derive allowed paths from the registered task/owner contract, compare against the exact base, reject unexplained cross-owner changes, and require expiring machine-readable overrides.

### RP-AUD-012 — CI lacks one golden-path integration test

Current CI has useful unit, reference-integrity, bilingual, and scheduler-cutover checks. It does not exercise the full lifecycle against one fixture repository/event stream. Consequently locally correct components can remain globally disconnected.

Required repair:

Add a hermetic golden-path suite and negative paths for:

- orphan publication;
- concurrent publication conflict;
- unregistered scheduler event;
- stale owner but live session and live owner but stale session;
- recovery without replay;
- return/review close;
- successor without gate;
- duplicate promotion;
- FREE raw candidate publication rejection and audited candidate publication success.

## 6. P2 findings — quality and operator-error reduction

### RP-AUD-013 — Mandatory template placeholders can survive publication

The publication template has mandatory sections, but current publication audit does not prove that placeholders were replaced with substantive content. The publisher can potentially satisfy nonempty checks with template text.

Repair: reject known placeholders, require minimum structured fields, and validate first executable action/kill condition enough to prevent blank boilerplate.

### RP-AUD-014 — Researcher priority override is specified but not implemented

The contract says explicit user priority controls, while the publication code unconditionally clamps researcher publication to `P2 / MEDIUM` and exposes no verified user-override path.

Repair: require an exact user-instruction evidence reference and persist both requested and effective priority plus the authority that set the effective value.

### RP-AUD-015 — Publisher role/origin combinations are not fully validated

The `new` command defaults `origin_kind=DRIVER_ROADMAP` even when the publisher is a researcher. Publisher ID is checked only for nonemptiness, not registry membership or role compatibility.

Repair: role-aware defaults and an allowed publisher-role × origin-kind matrix.

### RP-AUD-016 — `TB-META` findings are ignored during publication

The publication tool filters out taskbook findings with code `TB-META`. That can allow a task to publish despite missing or contradictory mandatory metadata.

Repair: no blanket suppression; explicitly classify only truly publication-owned fields and validate them after normalization.

### RP-AUD-017 — Subflow continuation has no frame stack

The runtime treats publication as a subflow, but completion clears current unfinished unit/next action rather than restoring a saved parent frame. Nested publication, tool lookup, validation, or review subflows can lose the parent frontier.

Repair: use a stack of frames with parent objective, current unit, next action, and durable checkpoint.

### RP-AUD-018 — Tool registry and method inventory overlap without strong reconciliation

Tool reuse policy is conceptually strong, but `enterprise_toolbox_registry.json` and `research_method_inventory.json` are separate mutable catalogs. Coverage lookup uses keyword scoring and can incorrectly declare a capability gap for synonyms. Registration/harvest writes are unlocked and not tied to an accepted return/review event.

Repair:

- one canonical method/tool identity graph;
- semantic aliases and exact capability predicates;
- accepted-review foreign key for harvest;
- CAS/append-only updates;
- CI reconciliation.

### RP-AUD-019 — Hot-start documentation remains internally inconsistent

AGENTS says Common Surface is lookup-only, routine pre-math reads should normally be at most three, and remote/scheduler preflight is triggered rather than universal. Older Common Surface and scheduling documents still mandate broad preflight reads and live Issue/scheduler checks.

Repair: generate secondary documents from the canonical hot-path contract or enforce a precedence banner and CI drift check.

### RP-AUD-020 — Bilingual sync checks pairs, not semantic equivalence

The bilingual workflow verifies synchronized paired-file changes. It does not prove that English and Chinese policies express the same authority/state semantics.

Repair: for control-plane documents, prefer one machine source with generated bilingual views, and validate that both views cite the same schema/version/authority matrix.

## 7. What is safe now

The following may continue:

- existing pre-cutover task executions verified against the frozen legacy baseline;
- explicit user-selected task work with a valid existing owner branch and claim;
- FREE Phase A discovery under its blind firewall;
- task publication for **preservation**, provided operators do not confuse registry `CLAIMABLE` with scheduler-dispatchable;
- current evidence, scope, and continuation discipline;
- current final-response liveness gate.

## 8. Immediate operational restrictions

Until RP-AUD-001 through RP-AUD-005 are repaired:

1. Do not represent a newly registry-published task as canonically dispatchable solely because its registry state is `CLAIMABLE`.
2. Do not create synthetic official tasks merely to run FREE or Driver control-plane sessions.
3. Do not rely on a hard-coded Driver ID in policy as activation evidence.
4. Do not infer task closure from a prose return/review alone; verify owner lease, registry/task state, branch, durable outputs, and successor decision separately.
5. Do not allow direct edits to the frozen scheduler to serve as a workaround.

## 9. Required repair order

### Gate A — Safe task existence and dispatch

Close RP-AUD-001, 002, 003, 004, and 005.

Exit criterion:

`NEW_TASK_PUBLISH -> CANONICAL_SELECT -> CLAIM -> SESSION_START -> VERIFIED_RUNTIME_STATE`

must pass end to end without manual alternate authority.

### Gate B — Return/review/closure

Close RP-AUD-006, 007, 008, 010, 012, 016, and 017.

Exit criterion:

`ACTIVE_TASK -> DURABLE_RETURN -> INDEPENDENT_REVIEW -> {REOPEN | CLOSE | PARK | SUPERSEDE} -> OWNER_RELEASE -> PARENT_REEVALUATION`

must be one auditable transaction chain.

### Gate C — Promotion/Foundation and portfolio quality

Close RP-AUD-009, 011, 013–015, 018–020.

Exit criterion:

accepted results can be promoted exactly once, branch scope is enforced, method harvest is evidence-linked, and all secondary control surfaces derive from one authority matrix.

## 10. Final Driver judgment

The earlier unified task-publication repair was directionally correct and materially improved orphan prevention, but it completed only the **task-existence** segment. It did not yet close the complete research control loop.

The system should not be described as “100% able to carry all research control tasks” until the three repair gates above pass end to end.

Final verdict:

`RESEARCH_PROCESS_AUDIT = COMPLETE`

`CRITICAL_GAPS = 5 P0`

`MAJOR_GAPS = 7 P1`

`IMPROVEMENT_GAPS = 8 P2`

`FULL_END_TO_END_CLOSURE = false`

`NEXT_CONTROL_OBJECTIVE = GATE_A_SAFE_TASK_EXISTENCE_AND_DISPATCH`
