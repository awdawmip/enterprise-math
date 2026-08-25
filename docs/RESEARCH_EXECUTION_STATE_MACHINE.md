# Enterprise Math Research Execution State Machine

Status: `ACTIVE_CANONICAL_ON_MERGE / V1.4`

Machine authority: `research_execution_state_machine.json`.

This protocol applies to every concrete `TASK_RESEARCH` execution. It does not replace scheduler task state, Researcher-ID state, candidate maturity, theorem truth, Foundation status or canonical promotion.

## 1. Core rule

A valid task authority does **not** mean substantive work is ready.

Task authority may come from:

- `OFFICIAL_TASKBOOK`;
- `DIRECT_USER_TASK`;
- `SCHEDULER_TASK`;
- `DRIVER_DISPATCH_ENVELOPE`.

Every run normalizes to:

```json
{
  "task_id": "...",
  "authority_kind": "...",
  "authority_ref": "...",
  "execution_gates": []
}
```

Freeze:

`TASK_AUTHORITY_READY != EXECUTION_READY`.

`STATE_PERMISSION + ALL_GUARDING_GATES_SATISFIED -> ACTION_ALLOWED`.

Mathematical source reads/derivations are legal only after the concrete runtime reaches `EXECUTION_READY`, and later guarded actions remain blocked until their gates are satisfied.

## 2. Independent dimensions

Never collapse these into one status:

1. task authority / scheduler coordination;
2. concrete execution state and gate ledger;
3. role identity;
4. mathematical/candidate/canonical truth.

Examples:

- scheduler `CLAIMED` + execution `PRE_MATH_GATES_PENDING` => no mathematics yet;
- taskbook `READY` != `EXECUTION_READY`;
- `RETURN_ACCEPTED` means Driver accepted the run, not that a theorem/candidate is canonical;
- `DELIVERED_UNREVIEWED` means a direct-user task return was delivered without Driver review, not that Driver accepted or promoted it;
- a failed mandatory pre-math publication gate is an execution non-start, not a negative mathematical verdict.

## 3. State path

Typical startup with no pre-math gate:

`UNBOUND -> DISPATCH_READY -> CLAIMED -> IDENTITY_READY -> EXECUTION_READY -> IN_PROGRESS`.

With a pre-math gate:

`UNBOUND -> DISPATCH_READY -> CLAIMED -> IDENTITY_READY -> PRE_MATH_GATES_PENDING -> EXECUTION_READY -> IN_PROGRESS`.

The jump `PRE_MATH_GATES_PENDING -> IN_PROGRESS` is forbidden.

A durable handoff enters `HANDOFF_READY`, which pauses the run. The same conversation may resume the same execution only through `SAME_CONVERSATION_EXECUTION_RESUMED` after durable handoff and gate-ledger reconciliation. A genuinely new conversation binds a new execution instance.

A durable return enters `RETURNED`. From there:

- Driver-reviewed routes use `DRIVER_REVIEW_PENDING -> RETURN_ACCEPTED/RETURN_REJECTED`;
- a direct-user task with no applicable Driver review may use `RETURN_DELIVERED_WITHOUT_DRIVER_REVIEW -> DELIVERED_UNREVIEWED`.

`DELIVERED_UNREVIEWED` is terminal only for the execution instance. It promotes no mathematical truth.

## 4. Action classes

Control-relevant action classes are:

- `CONTROL_PLANE_READ`;
- `STARTUP_WRITE`;
- `MATHEMATICAL_SOURCE_READ`;
- `POST_FREEZE_SOURCE_READ`;
- `MATHEMATICAL_DERIVATION`;
- `CHECKPOINT_WRITE`;
- `VERDICT_FREEZE`;
- `RETURN_WRITE`;
- `DRIVER_REVIEW`.

`POST_FREEZE_SOURCE_READ` means reading a source class deliberately withheld until a named raw/independent/Phase-A freeze, such as current toolbox/prior-art/downstream comparison material opened only in Phase B.

It **inherits** the guards on `MATHEMATICAL_SOURCE_READ`, so a startup gate that blocks mathematical source reads also blocks post-freeze source reads. A later Phase-A-freeze gate may additionally guard only `POST_FREEZE_SOURCE_READ`, leaving already-authorized Phase-A sources readable.

`VERDICT_FREEZE` means selecting/freezing the primary/final terminal mathematical classification. A task that requires checker/audit/checkpoint X before its final verdict must guard `VERDICT_FREEZE`; guarding only `RETURN_WRITE` is too late.

## 5. Gate ledger

Every normalized execution gate begins `PENDING` and may become:

- `SATISFIED` — the declared evidence contract is met;
- `FAILED` — the gate failed and may not be silently bypassed.

An action is blocked when any unsatisfied gate guards that action **or an implied parent action class**.

### PRE_MATH

A `PRE_MATH` gate must guard:

- `MATHEMATICAL_SOURCE_READ`;
- `MATHEMATICAL_DERIVATION`.

Because of action implication it also blocks `POST_FREEZE_SOURCE_READ`.

### MID_EXECUTION

Use a MID gate for ordered in-task boundaries, especially:

- Phase-A/raw/independent freeze before `POST_FREEZE_SOURCE_READ`;
- checker/audit/materialization checkpoint before `VERDICT_FREEZE`.

### PRE_RETURN

A `PRE_RETURN` gate must guard `RETURN_WRITE`.

A chat claim, intention, local-only unverified file or self-report does not satisfy a gate that requires durable/remote evidence.

## 6. Task-authority rules

### Official taskbook

The exact revision must first pass:

```bash
python tools/research_control_gate.py audit research_tasks/<TASK>.md
```

Taskbook `READY` is only dispatchability, not runtime readiness.

### Direct user task

Do not manufacture an artificial taskbook. The current instruction is authority. Normalize every explicit startup/process/source-visibility/verdict/return constraint into the runtime execution spec before substantive work.

Machine-check the normalized spec when useful:

```bash
python tools/research_execution_state.py audit-spec \
  --spec-json '{"task_id":"...","authority_kind":"DIRECT_USER_TASK","authority_ref":"conversation:...","execution_gates":[]}' \
  --authority-body 'the current task instruction'
```

### Scheduler task

Scheduler `CLAIMED/IN_PROGRESS/DONE` coordinates work only. Normalize the scheduler-selected task and its task-local gates into this execution machine; scheduler state never means `EXECUTION_READY` or theorem truth.

### Driver dispatch envelope

The envelope may bind task authority/identity. If it points to an official taskbook, it cannot waive the taskbook composite audit or execution gates.

## 7. Mandatory researcher startup

For every TASK run:

1. resolve the task authority;
2. normalize the execution spec and all explicit task-local gates;
3. resolve/allocate Researcher-ID;
4. instantiate every gate `PENDING`;
5. if any PRE_MATH gate exists, enter `PRE_MATH_GATES_PENDING`;
6. satisfy and verify every PRE_MATH gate;
7. only then reach `EXECUTION_READY` and begin mathematical source reads/derivation;
8. before any guarded later action, check the gate ledger again.

The machine detects obvious prose such as “before mathematics” / “开始数学前”. An official taskbook or supplied authority body that contains such a directive but declares no PRE_MATH gate fails with `EX-PREMATH-UNDECLARED`.

Semantic review remains responsible for equivalent language and for mapping phase-specific source firewalls to `POST_FREEZE_SOURCE_READ` and pre-verdict checkpoints to `VERDICT_FREEZE`.

## 8. Recovery

When chat/runtime continuity becomes unreliable:

`... -> RECOVERY_REQUIRED`.

Reconstruct the last legal state **and gate ledger** from durable authority/evidence only. Resume requires both a durable frontier reference and `execution_gate_ledger_reconciled=true`. If no safe frontier exists, use `REDISPATCH_REQUIRED`.

Do not infer completion from chat self-report.

## 9. Driver review

The Driver checks execution legality before mathematical acceptance:

- authority kind/spec;
- startup gate evidence;
- any Phase-A source-visibility freeze;
- any checker/audit gate before `VERDICT_FREEZE`;
- final `RETURN_WRITE` gate;
- durable return;
- recovered gate ledger when continuity failed.

Then classify execution status separately from mathematical/candidate/canonical status.

## 10. F5A regression guard

Historical failure mode:

> researcher reports completion but mandatory pre-math remote branch/stamp evidence is absent.

The run must not become `EXECUTION_READY`, `IN_PROGRESS`, `RETURN_ACCEPTED`, `DELIVERED_UNREVIEWED` or `CLOSED`. It is a startup/liveness failure and must follow non-start/recovery/redispatch.

## 11. Machine checks

Validate machine:

```bash
python tools/research_execution_state.py validate-machine
```

Audit official-taskbook execution metadata:

```bash
python tools/research_execution_state.py audit-taskbook research_tasks/<TASK>.md
```

Check bare state permission:

```bash
python tools/research_execution_state.py check-action \
  --state PRE_MATH_GATES_PENDING \
  --action MATHEMATICAL_SOURCE_READ
```

Check state + task gate ledger:

```bash
python tools/research_execution_state.py check-task-action \
  --taskbook research_tasks/<TASK>.md \
  --state IN_PROGRESS \
  --action POST_FREEZE_SOURCE_READ \
  --satisfied-gates START-GATE,PHASE-A-FREEZE
```

or:

```bash
python tools/research_execution_state.py check-task-action \
  --taskbook research_tasks/<TASK>.md \
  --state IN_PROGRESS \
  --action VERDICT_FREEZE \
  --satisfied-gates START-GATE,CHECKER-GATE
```

Check transition evidence:

```bash
python tools/research_execution_state.py next-state \
  --state PRE_MATH_GATES_PENDING \
  --event PRE_MATH_GATES_SATISFIED \
  --evidence-json '{"durable_evidence_refs_for_all_pre_math_gates":["commit:..."],"remote_verification_if_required_by_gate":"verified"}'
```

Pass booleans such as `dispatch_audit_pass`, `action_within_task_scope`, `execution_gate_ledger_reconciled`, `return_write_action_guard_pass`, `execution_gate_ledger_complete` and `parent_objective_or_successor_gate_evaluated` must be literal `true` where required.

## 12. Parent-objective liveness

Execution-state completion is not automatically parent-objective completion. A tool call, checkpoint, handoff, scheduler `DONE`, PR state or Driver verdict cannot terminate an open parent objective by itself.

`active_turn_liveness.json` remains authoritative for same-turn continuation and successor/closure evaluation.
