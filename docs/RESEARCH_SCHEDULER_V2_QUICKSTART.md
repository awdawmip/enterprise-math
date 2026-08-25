# Scheduler V2 Quickstart / 状态机 V2 快速入口

Canonical task-runtime machine: `research_scheduler.json`  
Cross-layer research-control contract: `research_control_state_machine.json`  
Human protocol: `docs/RESEARCH_CONTROL_STATE_MACHINE.md`  
Runtime log: Issue `#240`  
Reducer: `tools/research_scheduler.py`  
Cross-layer validator: `tools/research_control.py`  
Event emitter: `tools/research_scheduler_event.py`

Scheduler V2 controls **task runtime**. The cross-layer state machine composes runtime with role/identity, task-local pre-math gates, information firewall, evidence state, Driver routing, axiom-admission/formalization/Foundation/benchmark/promotion gates and parent-objective liveness.

## Universal start / 所有人统一入口

1. Resolve role + visible identity.
2. Resolve the exact task/candidate/control object.
3. Classify the control profile (`STANDARD_RESEARCH`, `FREE_CANDIDATE_AUDIT`, `INDEPENDENT_AUDIT`, `AXIOM_ADMISSION_AUDIT`, `FORMALIZATION`, `FOUNDATION_DISPOSITION`, `INTEGRATION`, `BENCHMARK`, `MATHEMATICAL_PROMOTION`, `GOVERNANCE_MAINTENANCE`).
4. Materialize Scheduler V2 state for task work. If the taskbook declares a publication/liveness gate before mathematics, record it as `pre_math_gate` and do not start substantive mathematics until it is satisfied.
5. Respect the profile's information/evidence guards.
6. Use only legal events/transitions.
7. Before Driver closure, bind evidence class + method harvest + route disposition.
8. Re-evaluate the parent user objective; task `DONE` is not parent completion.

## Researcher / 研究员

- `领任务` -> `select` -> `CLAIM` -> work.
- Finish work with `SUBMIT`, never V2 `DONE`.
- Lease loss creates `ORPHANED`; resume with `ADOPT`, not ordinary `CLAIM`.
- Formalizers, independent auditors and axiom-admission auditors are task specializations and inherit additional cross-layer guards.
- `pre_math_gate=REQUIRED_UNSATISFIED` means complete the taskbook's branch/publication/liveness prerequisite first; it is not permission to reinterpret or weaken the task.

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

### Independent replication routing

Never model a fresh independent replication by returning the same task to `HANDOFF_READY`.

Use:

`PARK parent -> OPEN_INDEPENDENT_REPLICATION_CHILD -> distinct child taskbook/task_id -> PUBLISH -> cross-Driver APPROVE`.

The child task records its own blindness/independence provenance.

## Orphan / 孤儿

Every unregistered taskbook is visible as an orphan. An orphan is not auto-dispatchable. Inspect its refs, then `ADOPT`, `MIGRATE`, `SUPERSEDE`, or re-author/review/publish it.

This explicitly covers taskbooks created concurrently with the V2 cutover so live research cannot vanish during migration. Cross-layer guards apply to new events at/after `2026-08-25T10:50:39+08:00`; earlier Scheduler V2 events keep their historical replay semantics.

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
`ORPHANED != HANDOFF_READY`  
`INDEPENDENT_REPLICATION != SAME_TASK_HANDOFF`  
`AXIOM_ADMISSION_RECOMMENDATION != FOUNDATION_ACCEPTED`  
`ACCEPTED_RETURN -> METHOD_HARVEST + ROUTE_DISPOSITION`  
`PARENT_OPEN + NEXT_ACTION -> CONTINUE_IN_SAME_TURN`
