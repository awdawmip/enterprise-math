# Scheduler V2 Quickstart / 状态机 V2 快速入口

Canonical task-runtime machine: `research_scheduler.json`  
Cross-layer research-control contract: `research_control_state_machine.json`  
Execution-liveness contract: `active_turn_liveness.json`  
Human protocol: `docs/RESEARCH_CONTROL_STATE_MACHINE.md`  
Runtime log: Issue `#240`  
Reducer: `tools/research_scheduler.py`  
Cross-layer validator: `tools/research_control.py`  
Event emitter: `tools/research_scheduler_event.py`

Scheduler V2 controls **task runtime**. The cross-layer state machine composes runtime with role/identity, task-local pre-math gates, information firewall, evidence state, Driver routing, axiom-admission/formalization/Foundation/benchmark/promotion gates, parent-objective liveness, durable-frontier intake reconciliation, and stale-conversation recovery.

## Universal start / 所有人统一入口

1. Resolve the exact task/candidate/control object and immutable taskbook ref.
2. **Before creating a new execution identity/branch/stamp or claiming an existing task, reconcile its durable frontier.** Check the declared owner branch, execution stamp, expected return/result/manifest locations, Scheduler state, PR/review state and persisted checker/build evidence as allowed by the task's information firewall.
3. Classify the predecessor exactly once as `VERIFIED_COMPLETE`, `IN_PROGRESS_RECOVERABLE`, `UNFINISHED`, or `NEVER_STARTED`.
4. Route by classification: consume complete work; resume the same recoverable frontier; preserve valid evidence and restart only missing work; or dispatch normally only when never started.
5. Resolve role + visible identity only for the execution that is actually required.
6. Classify the control profile (`STANDARD_RESEARCH`, `FREE_CANDIDATE_AUDIT`, `INDEPENDENT_AUDIT`, `AXIOM_ADMISSION_AUDIT`, `FORMALIZATION`, `FOUNDATION_DISPOSITION`, `INTEGRATION`, `BENCHMARK`, `MATHEMATICAL_PROMOTION`, `GOVERNANCE_MAINTENANCE`).
7. Materialize Scheduler V2 state for task work. If the taskbook declares a publication/liveness gate before mathematics, record it as `pre_math_gate` and do not start substantive mathematics until it is satisfied.
8. Resolve conversation liveness from **verifiable actions**, not progress prose. If a predecessor conversation has no new verifiable action for 10 minutes, recover from its durable frontier instead of waiting for it.
9. Respect the profile's information/evidence guards and use only legal transitions.
10. Before Driver closure, bind evidence class + method harvest + route disposition; then re-evaluate the parent objective because task `DONE` is not parent completion.

The intake check is narrow and task-specific. For blind/independent work, inspect status/provenance metadata without reading withheld mathematical content before the declared freeze.

## Researcher / 研究员

- `领任务` -> `select` -> reconcile durable frontier -> only `NEVER_STARTED` may `CLAIM(frontier_class=NEVER_STARTED, frontier_ref=...)` -> work.
- `VERIFIED_COMPLETE` -> consume the frozen result; do not create a new researcher identity or rerun mathematics.
- `IN_PROGRESS_RECOVERABLE` / `UNFINISHED` -> recover through the same durable frontier; if Scheduler state is `ORPHANED`, use `ADOPT(frontier_class=..., recovery_ref=...)`.
- Finish work with `SUBMIT`, never V2 `DONE`.
- Lease loss creates `ORPHANED`; resume with `ADOPT`, not ordinary `CLAIM`.
- Formalizers, independent auditors and axiom-admission auditors are task specializations and inherit additional cross-layer guards.
- `pre_math_gate=REQUIRED_UNSATISFIED` means complete the taskbook's branch/publication/liveness prerequisite first; it is not permission to reinterpret or weaken the task.
- Persist a resume-capable checkpoint at meaningful phase boundaries; do not leave more than one semantic phase only in chat-local state.

Canonical emitter examples now bind intake evidence:

`python tools/research_scheduler_event.py claim --task-id <TASK> --execution-id <ID> --claim-id <CLAIM> --frontier-ref <TASKBOOK_OR_RECONCILIATION_REF> --at <ISO8601>`

`python tools/research_scheduler_event.py adopt --task-id <TASK> --execution-id <ID> --claim-id <CLAIM> --frontier-class IN_PROGRESS_RECOVERABLE --recovery-ref <DURABLE_FRONTIER_REF> --at <ISO8601>`

## FREE researcher / 自由研究员

FREE discovery itself stays outside automatic dispatch. After the declared freeze, a FREE researcher may publish a concrete next-task proposal:

`publish-proposal -> REVIEW_PENDING`.

It cannot become `READY` until a different Driver reviews the publication and binds an approved immutable taskbook ref.

## Driver / 驾驶员

- `领审核` -> `select-review` -> `REVIEW_CLAIM`.
- Publication review: `APPROVE` or `REJECT`.
- `APPROVE` must bind `taskbook_audit=PASS` + current `policy_digest` + immutable taskbook ref + review ref.
- Return review: `REVIEW` with verdict + `evidence_class` + `method_harvest` + `route_disposition`.
- A Driver cannot review a task they published or a return they executed.
- Use `MIGRATE` only for cutover/pre-V2 work already live outside V2.
- An accepted axiom-admission recommendation does not change Foundation. Route it with `ROUTE_TO_FOUNDATION` and keep Foundation status pending until Steward disposition.
- If an execution chat is stale for 10 minutes with no new verifiable action, reconstruct the durable frontier first. If Scheduler still holds its claim, Driver/SYSTEM may `ORPHAN` it early with reason `STALE_CONVERSATION_NO_VERIFIABLE_ACTION_10M`; the event must bind `evidence_ref` or `recovery_ref`, and a recovering execution then `ADOPT`s from that frontier.
- Before reissuing any explicit task, run the same durable-frontier reconciliation even if the previous run never reached Issue #240. A completed owner branch/return is authority to consume, not permission to dispatch a duplicate.

### Independent replication routing

Never model a fresh independent replication by returning the same task to `HANDOFF_READY`.

Use:

`PARK parent -> OPEN_INDEPENDENT_REPLICATION_CHILD -> distinct child taskbook/task_id -> PUBLISH -> cross-Driver APPROVE`.

The child task records its own blindness/independence provenance. Stale recovery by itself is not a fresh independent replication.

## Stale conversation / 卡住对话

A conversation is stale for control purposes after **10 continuous minutes without a new verifiable action**. Progress messages alone do not count.

Recovery algorithm:

`REBUILD DURABLE FRONTIER -> CLASSIFY -> RELEASE STALE CLAIM IF NEEDED -> ADOPT/RESUME OR CONSUME COMPLETE RESULT -> CONTINUE PARENT OBJECTIVE`.

Classification is exactly one of:

- `VERIFIED_COMPLETE` — durable result already proves completion; do not redo;
- `IN_PROGRESS_RECOVERABLE` — resume from latest valid checkpoint;
- `UNFINISHED` — preserve valid evidence and restart only the missing portion;
- `NEVER_STARTED` — release and dispatch normally.

The ordinary Scheduler task lease is 1440 minutes. It is **not** a 24-hour waiting period for a dead conversation. Evidenced 10-minute conversation staleness may trigger an early Driver/SYSTEM `ORPHAN` before lease expiry.

A stale chat is never an authority source. Branches, commits, taskbooks, returns, PRs, accepted runtime events, execution stamps and persisted checker/build evidence are.

## Orphan / 孤儿

Every unregistered taskbook is visible as an orphan. An orphan is not auto-dispatchable. Inspect its refs, then `ADOPT`, `MIGRATE`, `SUPERSEDE`, or re-author/review/publish it.

This explicitly covers taskbooks created concurrently with the V2 cutover so live research cannot vanish during migration. Cross-layer guards apply to new events at/after `2026-08-25T10:50:39+08:00`; pre-execution reconciliation fields apply to new `CLAIM`/`ADOPT` events at/after `2026-08-25T12:00:00+08:00`. Earlier Scheduler events keep their historical replay semantics.

## Control checks / 控制检查

`python tools/research_scheduler.py validate`

`python tools/research_control.py validate-spec`

Safe registry/materialization entrypoint:

`python tools/research_control.py registry --events <exported-events.jsonl>`

The wrapper validates the versioned cross-layer event contract first, then invokes the canonical Scheduler V2 reducer. Direct `python tools/research_scheduler.py registry ...` is reserved for low-level reducer/debug use.

`python tools/research_control.py template <CONTROL_PROFILE>`

`python tools/research_control.py validate-events <events.jsonl>`

For an explicit composed snapshot:

`python tools/research_control.py validate-snapshot <snapshot.json>`

The invariants to remember are:

`PUBLISH != READY`  
`SUBMIT != DONE`  
`SCHEDULER_DONE != THEOREM_TRUTH`  
`SCHEDULER_DONE != PARENT_USER_OBJECTIVE_COMPLETE`  
`PRE_MATH_GATE_UNSATISFIED != MATH_ALLOWED`  
`BEFORE_REISSUE -> RECONCILE_DURABLE_FRONTIER`  
`VERIFIED_COMPLETE -> CONSUME_NOT_REDISPATCH`  
`CLAIM -> FRONTIER_CLASS_NEVER_STARTED + FRONTIER_REF`  
`ADOPT -> RECOVERABLE/UNFINISHED + RECOVERY_REF`  
`ORPHANED != HANDOFF_READY`  
`INDEPENDENT_REPLICATION != SAME_TASK_HANDOFF`  
`AXIOM_ADMISSION_RECOMMENDATION != FOUNDATION_ACCEPTED`  
`ACCEPTED_RETURN -> METHOD_HARVEST + ROUTE_DISPOSITION`  
`PROGRESS_PROSE != VERIFIED_LIVENESS`  
`10_MIN_STALE_CHAT != WAIT_24H_TASK_LEASE`  
`STALE_CHAT -> DURABLE_FRONTIER_RECOVERY`  
`PARENT_OPEN + NEXT_ACTION -> CONTINUE_IN_SAME_TURN_OR_RECOVERING_CONVERSATION`
