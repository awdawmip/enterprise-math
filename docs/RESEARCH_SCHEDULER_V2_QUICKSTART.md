# Scheduler V2 Quickstart / 状态机 V2 快速入口

Canonical task-runtime machine: `research_scheduler.json`  
Cross-layer research-control contract: `research_control_state_machine.json`  
Human protocol: `docs/RESEARCH_CONTROL_STATE_MACHINE.md`  
Runtime log: Issue `#240`  
Reducer: `tools/research_scheduler.py`  
Cross-layer validator: `tools/research_control.py`  
Event emitter: `tools/research_scheduler_event.py`

Scheduler V2 controls **task runtime**. The cross-layer state machine composes runtime with role/identity, information firewall, evidence state, Driver routing, formalization/Foundation/benchmark/promotion gates and parent-objective liveness.

## Universal start / 所有人统一入口

1. Resolve role + visible identity.
2. Resolve the exact task/candidate/control object.
3. Classify the control profile (`STANDARD_RESEARCH`, `FREE_CANDIDATE_AUDIT`, `INDEPENDENT_AUDIT`, `FORMALIZATION`, `FOUNDATION_DISPOSITION`, `INTEGRATION`, `BENCHMARK`, `MATHEMATICAL_PROMOTION`, `GOVERNANCE_MAINTENANCE`).
4. Materialize Scheduler V2 state for task work.
5. Respect the profile's information/evidence guards.
6. Use only legal events/transitions.
7. Before Driver closure, bind evidence class + method harvest + route disposition.
8. Re-evaluate the parent user objective; task `DONE` is not parent completion.

## Researcher / 研究员

- `领任务` -> `select` -> `CLAIM` -> work.
- Finish work with `SUBMIT`, never V2 `DONE`.
- Lease loss creates `ORPHANED`; resume with `ADOPT`, not ordinary `CLAIM`.
- Formalizers and independent auditors are task specializations and inherit additional cross-layer guards.

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

### Independent replication routing

Never model a fresh independent replication by returning the same task to `HANDOFF_READY`.

Use:

`PARK parent -> OPEN_INDEPENDENT_REPLICATION_CHILD -> distinct child taskbook/task_id -> PUBLISH -> cross-Driver APPROVE`.

The child task records its own blindness/independence provenance.

## Orphan / 孤儿

Every unregistered taskbook is visible as an orphan. An orphan is not auto-dispatchable. Inspect its refs, then `ADOPT`, `MIGRATE`, `SUPERSEDE`, or re-author/review/publish it.

This explicitly covers taskbooks created concurrently with the V2 cutover so live research cannot vanish during migration.

## Control checks / 控制检查

`python tools/research_scheduler.py validate`

`python tools/research_scheduler.py registry --events <exported-events.jsonl>`

`python tools/research_control.py validate-spec`

`python tools/research_control.py template <CONTROL_PROFILE>`

`python tools/research_control.py validate-events <events.jsonl>`

For an explicit composed snapshot:

`python tools/research_control.py validate-snapshot <snapshot.json>`

The invariants to remember are:

`PUBLISH != READY`  
`SUBMIT != DONE`  
`SCHEDULER_DONE != THEOREM_TRUTH`  
`SCHEDULER_DONE != PARENT_USER_OBJECTIVE_COMPLETE`  
`ORPHANED != HANDOFF_READY`  
`INDEPENDENT_REPLICATION != SAME_TASK_HANDOFF`  
`ACCEPTED_RETURN -> METHOD_HARVEST + ROUTE_DISPOSITION`  
`PARENT_OPEN + NEXT_ACTION -> CONTINUE_IN_SAME_TURN`
