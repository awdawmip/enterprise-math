# Enterprise Math Research Control State Machine V1

Status: `CANDIDATE CANONICAL CROSS-LAYER CONTROL / NO NEW MATHEMATICS`

Machine-readable contract: `research_control_state_machine.json`  
Task runtime submachine: `research_scheduler.json`  
Execution-liveness submachine: `active_turn_liveness.json`  
Cross-layer validator: `tools/research_control.py`  
Event emitter: `tools/research_scheduler_event.py`

## 1. What this machine is

Enterprise Math already has several valid local state machines: identity, role/mode, FREE candidate lifecycle, taskbooks, Scheduler V2, active-turn continuation and promotion. None of them should be duplicated.

This file defines their **composition**.

The operative state is a vector:

`ACTOR × OBJECT × RUNTIME × CONVERSATION × INFORMATION × EVIDENCE × ROUTING × PARENT`.

The point is to make questions such as the following decidable without relying on chat memory:

- what exact task/object is being acted on;
- whether that exact task is already durably complete, recoverable, unfinished, or genuinely never started before a new execution generation is created;
- who has authority to act;
- which task/generation is live;
- whether a task-local publication/liveness gate allows substantive mathematics to start;
- whether the executing conversation is actually alive or must be recovered;
- what the latest durable frontier is if a conversation stalls;
- whether the context is blind, statement-exposed or post-freeze;
- whether source and independent evidence are open/closed;
- whether an axiom-admission result is only a research recommendation or has actually reached Foundation disposition;
- whether a Driver verdict is still pending;
- whether formalization is admitted;
- whether a benchmark supports a performance claim;
- whether a successor gate is satisfied;
- whether the current task is locally done but the parent user objective is still open.

Scheduler V2 remains the source of truth for task-runtime state. The cross-layer machine does **not** invent a second scheduler. Conversation recovery uses the Scheduler's existing `ORPHAN -> ADOPT` path when a live claim must be released.

## 2. The one algorithm every role follows

For every substantive Enterprise Math action:

1. **Resolve the exact object first.** Identify task/candidate/control object, task id, origin, lineage, immutable taskbook ref, declared owner branch and expected return/evidence locations.
2. **Reconcile the durable frontier before a new execution generation.** Use durable repository/control evidence to classify the exact task as `VERIFIED_COMPLETE`, `IN_PROGRESS_RECOVERABLE`, `UNFINISHED`, or `NEVER_STARTED`. Do this before creating a new execution identity, owner branch, execution stamp, Scheduler `CLAIM`, Scheduler `ADOPT`, or direct rerun.
3. **Route the intake classification.** `VERIFIED_COMPLETE` is consumed, not re-executed. `IN_PROGRESS_RECOVERABLE` resumes the same durable frontier. `UNFINISHED` preserves valid evidence and restarts only the missing portion. Only `NEVER_STARTED` permits ordinary new dispatch.
4. **Resolve role + identity for the execution that is actually required.** Use the current role contract and identity state machine.
5. **Classify control profile.** Choose one of `STANDARD_RESEARCH`, `FREE_CANDIDATE_AUDIT`, `INDEPENDENT_AUDIT`, `AXIOM_ADMISSION_AUDIT`, `FORMALIZATION`, `FOUNDATION_DISPOSITION`, `INTEGRATION`, `BENCHMARK`, `MATHEMATICAL_PROMOTION`, `GOVERNANCE_MAINTENANCE`.
6. **Materialize runtime state.** For task work, reduce current Scheduler V2 events; do not infer runtime state from chat. If the taskbook declares a pre-math/publication liveness gate, record it as `pre_math_gate` before doing mathematics.
7. **Resolve conversation liveness.** A progress message is not a heartbeat. If the predecessor has no new verifiable action for 10 continuous minutes, rebuild the durable frontier and recover instead of waiting.
8. **Materialize information/evidence state.** Record firewall/freeze/source exposure plus source, independent, axiom-admission, Driver, formalization/benchmark/canonical state.
9. **Execute only an allowed transition.** Role permissions and profile guards both apply.
10. **Before Driver closure, bind evidence + routing.** Every accepted/narrowed return needs evidence class, method-harvest classification and explicit route disposition.
11. **Evaluate the parent objective.** `scheduler DONE`, Stage PASS, PR creation, checkpoint freeze, conversation replacement or remote pending never ends an open parent objective by itself.
12. **Persist changed control facts, then continue.** If the parent objective is open and an executable action exists, execute it in the same turn or recovering conversation.

For blind/independent work, step 2 reconciles existence/status/provenance metadata without reading mathematical source that the taskbook withholds before freeze.

## 3. Role-specific use

### Task researcher

Normal fresh execution:

`READY/HANDOFF_READY -> DURABLE_FRONTIER_RECONCILIATION -> NEVER_STARTED -> CLAIM(frontier_ref) -> PROGRESS* -> SUBMIT`.

Recovery execution:

`ORPHANED -> DURABLE_FRONTIER_RECONCILIATION -> IN_PROGRESS_RECOVERABLE/UNFINISHED -> ADOPT(recovery_ref) -> PROGRESS* -> SUBMIT`.

If the reconciliation result is `VERIFIED_COMPLETE`, stop execution setup and consume the durable return/result. Do not allocate another researcher identity, branch, execution stamp, or mathematical rerun.

Never emit V2 `DONE`. Never self-review. A hard block must name a genuinely missing object/dependency, its owner, necessity and unblock condition. If the taskbook requires a branch/publication stamp, source freeze, or another explicit pre-math gate, substantive mathematics is forbidden until `pre_math_gate=SATISFIED`.

Once execution is actually required, create the earliest supported durable execution stamp/claim before a long research phase. At meaningful phase boundaries, persist reusable evidence and a concrete next action; do not carry more than one meaningful semantic phase only in chat-local state.

### FREE researcher

Phase A stays outside automatic claiming. Preserve blindness until candidate/no-go freeze. After freeze, a concrete proposal may be published only to `REVIEW_PENDING`; that publication is not Working Truth and is not dispatchable authority.

### Independent auditor / replicator

This is a `RESEARCHER` task specialization, not a new authority role.

The task must declare its information firewall. Clean independence requires a distinct execution context when the protocol claims independent replication. Source proofs/checkers withheld by the taskbook stay withheld until the named freeze.

**Do not use same-task handoff to represent a new independent replication.** If a Driver decides a new independent run is needed, the parent review is parked and a **distinct child task id/taskbook** is opened with fresh provenance and an explicit independence/firewall protocol.

A stale-conversation recovery or ordinary continuation is not automatically a fresh independent replication. Recovery resumes the same durable task frontier unless the audit protocol separately requires a new clean child context.

### Axiom-admission auditor

This is a `RESEARCHER` task specialization with profile `AXIOM_ADMISSION_AUDIT`.

Its job is to classify whether a proposed rule is model-relative, conservative/admissible, restricted-admissible, deferred, rejected, invalid, or unsupported at the audited level. It may recommend admission, but it **cannot itself change Foundation** and it cannot mark the rule canonical. If a Driver accepts or narrows an admission recommendation, the only valid semantic path is `ROUTE_TO_FOUNDATION` with a concrete route ref and `foundation_status=PENDING` until a Foundation Steward disposes it.

For tasks such as current CBRC F5A that require a publication-liveness stamp before mathematics, `pre_math_gate=REQUIRED_UNSATISFIED` is a hard local execution gate, not a reason to reinterpret the mathematics.

### Formalizer

This is a `RESEARCHER` task specialization with profile `FORMALIZATION`.

Formalization may start only after Driver admission, frozen/corrected source mathematics, and closure of any required independent evidence. `NO_NEW_MATHEMATICS` is binding. If Lean or another proof kernel exposes a statement/interface mismatch, return it to the Driver. Never weaken a theorem, change the accepted universe, add an unreviewed hypothesis or insert an axiom merely to pass the build.

### Driver

Drivers own task publication/review, return review, route disposition, method harvest, successor gating, formalization admission, Foundation routing, promotion routing, exact-task reissue reconciliation, and control-plane release of an evidenced stale execution claim.

Before reissuing an explicit task, the Driver must reconcile its durable frontier even when the prior execution never reached Issue #240. A completed owner branch/return is authority to consume, not permission to dispatch a duplicate.

For every accepted/narrowed return, record:

- `evidence_class`;
- `method_harvest`;
- `route_disposition`;
- route/successor/child refs when applicable.

A Driver verdict is a routing event, not parent-objective completion. A Driver acceptance of an axiom-admission audit is still only a routing decision until Foundation Steward disposition.

When a predecessor chat has produced no verifiable action for 10 minutes, the Driver must reconstruct the durable frontier before touching its claim. If a live Scheduler claim must be released, use `ORPHAN` with reason `STALE_CONVERSATION_NO_VERIFIABLE_ACTION_10M` and a concrete evidence/recovery ref; the replacement execution uses `ADOPT` with a fresh execution identity, a recoverable/unfinished frontier classification, and `recovery_ref`.

### Foundation Steward

Steward disposition may change the Foundation semantic gate. Until that gate is explicitly resolved, canonical mutation and gated downstream formalization remain blocked. Steward verification does not automatically promote a theorem.

## 4. Publication approval is two gates, not one

Taskbook content gate:

`python tools/research_taskbook.py audit <taskbook> --dispatch`

Runtime gate:

`PUBLISH -> different Driver REVIEW_CLAIM -> APPROVE -> READY`.

New `APPROVE` events must bind both:

- `taskbook_audit=PASS`;
- current `policy_digest=sha256:...`;
- immutable `taskbook_ref`;
- `review_ref`.

This prevents a cross-Driver runtime approval from silently bypassing the taskbook policy gate.

## 5. Return review is a semantic routing gate

New `REVIEW` events carry four mandatory fields:

- `review_ref`;
- `evidence_class`;
- `method_harvest`;
- `route_disposition`.

Additional guards:

- `RETURN_TO_RESEARCH` -> `CONTINUE_SAME_TASK`;
- `OPEN_CONTINUATION` requires `successor_gate_ref` and a distinct route/task ref;
- `ROUTE_TO_FOUNDATION`, `ROUTE_TO_FORMALIZATION`, `ROUTE_TO_PROMOTION` require the concrete route ref;
- independent replication uses `PARK + OPEN_INDEPENDENT_REPLICATION_CHILD`, with distinct child task id/ref and independence protocol;
- `REQUEST_INDEPENDENT_REPLICATION` as a new same-task Scheduler verdict is forbidden after the cross-layer cutover;
- an accepted `ADMIT_RECOMMENDED` / `RESTRICTED_ADMISSION_RECOMMENDED` axiom audit routes to Foundation; it does not mutate Foundation in place.

## 6. Profile guards for the current research portfolio

### Prime Fusion F1 / formalization

Profile `FORMALIZATION`: corrected/frozen package + closed independent evidence + Driver admission are prerequisites. A source-repair-required state cannot enter formalization.

### Native-prime companion replay and CBRC F5R

Profile `INDEPENDENT_AUDIT`: firewall and freeze state are first-class control fields. A blind audit cannot close before raw freeze and cannot claim clean independence from the source execution context if it reused that context.

### CBRC F5A branch-ontology axiom admission

Profile `AXIOM_ADMISSION_AUDIT`: preserve the taskbook whitelist/firewall and its publication-liveness pre-math gate. The research verdict may recommend unrestricted or restricted admission, but only a Driver may route that recommendation to Foundation, and only a Foundation Steward may dispose the Foundation status. `canonical_status=CANONICAL` is illegal in the research-audit profile.

### FQ010 scale-role decision

Profile `FOUNDATION_DISPOSITION`: pending Steward disposition blocks canonical mutation and downstream formalization admission.

### Valley / third-sector computational claims

Profile `BENCHMARK`: structural theorem status is separate from performance status. Positive performance claims require benchmark PASS, fair baseline and complete cost accounting. Partial/negative evidence cannot be relabeled L4.

### Prime Fusion package repair/integration

Profile `INTEGRATION`: package freeze is illegal while mandatory source repair or required independent evidence remains open.

### Mathematical L4 promotion

Profile `MATHEMATICAL_PROMOTION`: canonical mutation is downstream of a bounded promotion attempt. `IN_ATTEMPT`/`MERGED` states require an attempt ref, current-main snapshot, conflict audit ref and frozen candidate head. `canonical_status=CANONICAL` is illegal until `promotion_status=MERGED`.

### Scheduler/control-plane repair

Profile `GOVERNANCE_MAINTENANCE`: `NO_NEW_MATHEMATICS`; use current-main conflict audit and the bounded governance-maintenance lane.

## 7. Pre-execution durable-frontier reconciliation

Task runtime registration and exact-task execution are separate questions. Scheduler state can say a task is dispatchable while repository evidence already proves that a prior execution completed it or left a recoverable frontier.

Therefore, before any **new execution generation**, resolve the exact task id/taskbook and inspect only the durable surfaces needed to answer whether prior work exists. Preferred evidence includes the declared owner branch/head, execution stamp, frozen return/result, manifest, PR/review state, Scheduler runtime event, and persisted checker/build evidence.

The only legal intake classes are:

- `VERIFIED_COMPLETE`: consume and route/review the durable result. `CLAIM`, `ADOPT`, new owner branch, new execution stamp and duplicate mathematics are forbidden.
- `IN_PROGRESS_RECOVERABLE`: preserve the durable frontier and resume it. Use Scheduler `ADOPT` when the runtime state is orphaned.
- `UNFINISHED`: preserve valid evidence, explicitly release/requeue incomplete execution as needed, and restart only the missing part.
- `NEVER_STARTED`: ordinary `CLAIM` and fresh execution setup are allowed.

New post-cutover `CLAIM` events bind `frontier_class=NEVER_STARTED` plus `frontier_ref`. New `ADOPT` events bind `frontier_class=IN_PROGRESS_RECOVERABLE|UNFINISHED` plus `recovery_ref`.

This rule applies equally to explicit user reissues that bypass automatic Scheduler selection. Direct instruction selects the task; it does not erase durable prior execution.

Freeze:

`EXPLICIT_REISSUE != BLIND_RESTART`.

`BEFORE_REISSUE -> RECONCILE_DURABLE_FRONTIER`.

`VERIFIED_COMPLETE -> CONSUME_NOT_REDISPATCH`.

## 8. Conversation liveness and takeover

The control plane distinguishes **task ownership lease** from **conversation liveness**.

Current Scheduler V2 task claim lease: `1440 minutes`.

Conversation stale threshold: `10 minutes without a new verifiable action`.

These clocks serve different purposes. The 24-hour task lease prevents accidental duplicate dispatch. It does not authorize the system to wait 24 hours for a dead chat.

A verifiable action is a new external/tool/compute/control result that materially advances the objective. Progress prose by itself does not count.

After 10 minutes of no verifiable action, rebuild the durable frontier from branch/commit, taskbook immutable ref, return/evidence, PR, Scheduler Issue #240 accepted event, execution stamp, or persisted checker/build evidence. Never use stale chat prose as the sole recovery authority.

Classify exactly one:

- `VERIFIED_COMPLETE`: consume the durable result; duplicate execution is forbidden.
- `IN_PROGRESS_RECOVERABLE`: preserve the frontier, release the stale live claim if necessary, `ADOPT` with a fresh execution identity, continue only the remainder.
- `UNFINISHED`: preserve valid evidence, explicitly orphan/requeue, restart only the missing portion.
- `NEVER_STARTED`: release the stale assignment and dispatch normally.

A stale-conversation `ORPHAN` must carry a durable `evidence_ref` or `recovery_ref`; the timeout alone is not authority to preempt work.

Freeze:

`10_MIN_NO_VERIFIABLE_ACTION + DURABLE_FRONTIER -> RECOVER_NOW`.

`24H_TASK_LEASE != WAIT_24H_FOR_STALE_CHAT`.

`TAKEOVER != NEW_INDEPENDENT_REPLICATION` unless a separate independence protocol requires a clean child execution.

## 9. Cutover and orphan rule

A taskbook discovered outside V2 registration is not silently READY. It appears as `ORPHANED`.

Cross-layer review-event guards take effect at `2026-08-25T10:50:39+08:00`. Pre-execution reconciliation fields for `CLAIM`/`ADOPT` take effect at `2026-08-25T12:00:00+08:00`. Earlier Scheduler events retain their historical replay semantics. Do not rewrite historical events merely to add newer audit fields.

This is intentional and covers work created concurrently with the V2 cutover. A Driver must reconcile it explicitly:

- `MIGRATE` for already-live cutover work;
- `ADOPT` for genuine orphan recovery after durable-frontier classification;
- `ORPHAN(reason=STALE_CONVERSATION_NO_VERIFIABLE_ACTION_10M)` for an evidenced dead execution chat that still owns a live claim;
- `SUPERSEDE` for dead/stale work;
- or re-author/review/publish it through the ordinary V2 gate.

No live task is allowed to disappear merely because it was issued during a control-plane migration or its original chat stopped responding.

## 10. Mandatory checks

Static machine:

`python tools/research_scheduler.py validate`

`python tools/research_control.py validate-spec`

To avoid hand-building the state vector:

`python tools/research_control.py template <CONTROL_PROFILE>`

Safe default for an exported Scheduler event stream:

`python tools/research_control.py registry --events <events.jsonl>`

This command first enforces the versioned cross-layer event guards and only then materializes the canonical Scheduler V2 registry. Direct `python tools/research_scheduler.py registry ...` is a low-level reducer/debug path and should not be the ordinary coordination entry point.

For validation only:

`python tools/research_control.py validate-events <events.jsonl>`

For a materialized cross-layer snapshot:

`python tools/research_control.py validate-snapshot <snapshot.json>`

The validator is a guard over the existing submachines. A PASS never proves mathematics; it proves only that the control state is internally admissible.

## 11. Nonterminal rule

Always end the control decision with:

`PARENT_USER_OBJECTIVE -> CURRENT_SUBFLOW -> NEXT_EXECUTABLE_ACTION`.

If the parent objective is open and the next executable action is known, continue now. Do not turn `DONE`, `PASS`, freeze, publication, review, PR/CI pending, a progress update, or a stale predecessor conversation into a user wake-up barrier.
