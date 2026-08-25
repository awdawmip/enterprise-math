# Enterprise Math Research Execution State Machine

Status: `ACTIVE_CANONICAL_ON_MERGE / V1.3`

Canonical machine-readable authority: `research_execution_state_machine.json`.

This protocol applies to every concrete `TASK_RESEARCH` execution. It also governs Driver recovery/review of those executions. It does **not** replace scheduler task state, Researcher-ID state, axiom-candidate maturity, theorem truth, or Foundation/canonical promotion.

## 1. The one rule everyone must remember

A valid task authority does **not** mean substantive work is ready.

Task authority can come from an approved taskbook, a current direct user task, a scheduler task, or a Driver dispatch envelope. In every case, mathematical source reads/derivations are legal only after the concrete runtime state reaches:

`EXECUTION_READY`

and the requested action is not blocked by an unsatisfied execution gate.

If the task declares any `PRE_MATH` execution gate, the required route is:

`TASK_AUTHORITY_READY -> CLAIMED -> IDENTITY_READY -> PRE_MATH_GATES_PENDING -> EXECUTION_READY -> IN_PROGRESS`

The jump

`PRE_MATH_GATES_PENDING -> IN_PROGRESS`

is forbidden.

## 2. Four independent dimensions

Do not collapse these into one status word:

1. **Task authority / scheduler state** — what authorizes the selected work and who may work it.
2. **Execution state** — whether this concrete run is legally allowed to start/continue/freeze a verdict/return.
3. **Identity state** — whether the conversation has a valid Researcher-ID/Driver-ID.
4. **Mathematical/candidate truth state** — whether a theorem, obstruction, axiom candidate or canonical artifact has been reviewed/promoted.

Examples:

- scheduler `CLAIMED` + execution `PRE_MATH_GATES_PENDING` => **no mathematics yet**;
- taskbook `READY` + execution `IDENTITY_READY` => **still no mathematics if a PRE_MATH gate is pending**;
- execution `RETURN_ACCEPTED` => Driver accepted the return as a valid run, but no theorem/candidate promotion follows automatically;
- a failed publication stamp before mathematics => `NONSTART_TERMINAL`, **not** a negative mathematical verdict.

## 3. Normalize task authority first

Every concrete `TASK_RESEARCH` execution starts by normalizing one allowed authority source into:

```json
{
  "task_id": "...",
  "authority_kind": "...",
  "authority_ref": "...",
  "execution_gates": []
}
```

Allowed `authority_kind` values:

- `OFFICIAL_TASKBOOK`;
- `DIRECT_USER_TASK`;
- `SCHEDULER_TASK`;
- `DRIVER_DISPATCH_ENVELOPE`.

Rules:

- `OFFICIAL_TASKBOOK` requires the exact revision to pass `python tools/research_control_gate.py audit <taskbook>` before entering `DISPATCH_READY`.
- `DIRECT_USER_TASK` does not require manufacturing a taskbook. The current instruction is authority; explicit task-local startup/process/verdict/return constraints are normalized into `execution_gates` before substantive work.
- `SCHEDULER_TASK` is task authority/coordination only. A scheduler claim never means `EXECUTION_READY`.
- A `DRIVER_DISPATCH_ENVELOPE` cannot waive an official taskbook audit or gate if the envelope points to that taskbook.

A normalized direct/scheduler/envelope spec can be machine-checked with:

```bash
python tools/research_execution_state.py audit-spec \
  --spec-json '{"task_id":"...","authority_kind":"DIRECT_USER_TASK","authority_ref":"conversation:...","execution_gates":[]}' \
  --authority-body 'current task instruction when prose-gate detection is needed'
```

## 4. Every declared gate has a runtime ledger entry

Every normalized `execution_gates` entry becomes a concrete runtime gate initially in:

`PENDING`.

A gate may become:

- `SATISFIED` — its declared durable evidence contract has been met;
- `FAILED` — the gate failed and may not be silently bypassed.

An action is legal only when **both** are true:

1. the current execution state permits the action class;
2. every gate whose `must_precede` contains that action is `SATISFIED`.

Therefore `EXECUTION_READY` is necessary but not always sufficient. For example, a task can be `IN_PROGRESS` while a checker/audit gate still blocks `VERDICT_FREEZE`, or while a final materialization gate blocks `RETURN_WRITE`.

## 5. Action classes researchers must distinguish

The machine uses these control-relevant action classes:

- `CONTROL_PLANE_READ`;
- `STARTUP_WRITE`;
- `MATHEMATICAL_SOURCE_READ`;
- `MATHEMATICAL_DERIVATION`;
- `CHECKPOINT_WRITE`;
- `VERDICT_FREEZE`;
- `RETURN_WRITE`;
- `DRIVER_REVIEW`.

`VERDICT_FREEZE` means selecting/freezing the task's primary/final/terminal mathematical classification. If the task says “checker/audit/checkpoint X must happen before the final verdict”, that condition must guard `VERDICT_FREEZE`; merely guarding `RETURN_WRITE` is too late.

Researchers may continue any other state/gate-allowed work while a verdict gate is pending, but must not announce/freeze the terminal verdict until every gate guarding `VERDICT_FREEZE` is satisfied.

## 6. Mandatory startup protocol for researchers

For every task execution:

1. Read only the task authority and control-plane/startup material permitted before mathematics.
2. Normalize the concrete execution spec and all explicit task-local gates.
3. Resolve/allocate the required role identity.
4. Instantiate every declared gate as `PENDING`.
5. If there is no `PRE_MATH` gate, classify startup as `EXECUTION_READY` only after task authority and identity are ready.
6. If any `PRE_MATH` gate exists, enter `PRE_MATH_GATES_PENDING`.
7. Satisfy every PRE_MATH gate exactly as declared and verify the required durable evidence.
8. Only then enter `EXECUTION_READY` and read mathematical sources / perform mathematical derivations.
9. Before every later guarded action, including `VERDICT_FREEZE` and `RETURN_WRITE`, check the gate ledger again.

A chat claim, intention, screenshot without the required repository evidence, local-only file, or “I already completed it” statement does not satisfy a durable gate when the gate requires durable/remote evidence.

## 7. Official taskbook fields

Every new or re-dispatched taskbook must carry:

```json
"execution_state_policy": "INHERIT_GLOBAL",
"execution_gates": []
```

Use `[]` only when there truly is no task-local execution gate.

A gate has the minimum form:

```json
{
  "gate_id": "UNIQUE-ID",
  "phase": "PRE_MATH",
  "must_precede": [
    "MATHEMATICAL_SOURCE_READ",
    "MATHEMATICAL_DERIVATION"
  ],
  "evidence": {
    "kind": "DURABLE_EVIDENCE_KIND"
  }
}
```

Taskbooks may add exact branch/path/hash/required-field constraints inside `evidence`.

Phase rules:

- `PRE_MATH` must guard both `MATHEMATICAL_SOURCE_READ` and `MATHEMATICAL_DERIVATION`;
- `MID_EXECUTION` guards later actions such as `VERDICT_FREEZE` when the task declares an ordered checkpoint;
- `PRE_RETURN` must guard `RETURN_WRITE`.

The machine audit also recognizes obvious task-local prose such as “before mathematics” / “开始数学前”. If that prose exists but no machine-readable `PRE_MATH` gate is declared, the authority/gate audit fails with `EX-PREMATH-UNDECLARED`.

Semantic Driver/taskbook review remains responsible for mapping equivalent task-local phrases such as “before final verdict” into a `VERDICT_FREEZE` gate even when a lexical checker cannot infer them safely.

## 8. Mandatory Driver protocol

Before official-taskbook dispatch/re-dispatch:

- audit the taskbook against current taskbook policy;
- audit its execution-state metadata/gates;
- use the single composite command `python tools/research_control_gate.py audit <taskbook-path>`;
- bind a runtime identity outside the reusable taskbook when manual dispatch requires it.

For direct/scheduler/envelope tasks, ensure the current authority is normalized into the same execution spec/gate schema; do not manufacture a taskbook merely to enter the state machine.

On return:

- review the durable return/evidence, not the conversation’s self-reported status;
- verify the concrete gate ledger is complete;
- verify any task-declared verdict-before-checker chronology via the `VERDICT_FREEZE` gate;
- classify the execution result separately from mathematical truth/promotion;
- after `RETURN_ACCEPTED`, evaluate closure/successor routing under the existing liveness and lineage contracts.

On stalled or ambiguous conversations:

`... -> RECOVERY_REQUIRED`

Then reconstruct the last legal state **and gate ledger** from durable authority/evidence. Resume only from an evidenced legal frontier. If no safe frontier exists, use `REDISPATCH_REQUIRED`.

## 9. F5A regression rule

The following historical failure mode is permanently guarded:

> A researcher reports completion, but a mandatory pre-math remote branch/stamp is absent.

The execution must **not** be classified `EXECUTION_READY`, `IN_PROGRESS`, `RETURN_ACCEPTED`, or `CLOSED`. It is a startup/liveness failure and must end in `NONSTART_TERMINAL` or a recovery/redispatch path.

## 10. Machine checks

Validate the machine:

```bash
python tools/research_execution_state.py validate-machine
```

Audit official-taskbook execution metadata:

```bash
python tools/research_execution_state.py audit-taskbook research_tasks/<TASK>.md
```

Ask whether the bare state permits an action:

```bash
python tools/research_execution_state.py check-action \
  --state PRE_MATH_GATES_PENDING \
  --action MATHEMATICAL_SOURCE_READ
```

Expected result: `BLOCKED_BY_STATE`.

Ask the authoritative task-aware question, including satisfied gate IDs:

```bash
python tools/research_execution_state.py check-task-action \
  --taskbook research_tasks/<TASK>.md \
  --state IN_PROGRESS \
  --action VERDICT_FREEZE \
  --satisfied-gates GATE-A,GATE-B
```

This combines state permission with the task’s gate ledger. If an unsatisfied gate guards the action, the result is `BLOCKED: <gate-id>`.

Check a state transition and its required evidence:

```bash
python tools/research_execution_state.py next-state \
  --state PRE_MATH_GATES_PENDING \
  --event PRE_MATH_GATES_SATISFIED \
  --evidence-json '{"durable_evidence_refs_for_all_pre_math_gates":["commit:..."],"remote_verification_if_required_by_gate":"verified"}'
```

Boolean pass fields such as `dispatch_audit_pass`, `action_within_task_scope`, `return_write_action_guard_pass` and `execution_gate_ledger_complete` must be literal `true`; a false/non-boolean placeholder cannot fake a transition.

## 11. Handoff and recovery

A durable handoff is terminal for the current execution instance unless the same conversation is explicitly resumed. A genuinely new conversation performs identity bootstrap again and binds a new execution instance; it may consume the previous durable handoff as its frontier.

Neither a tool call, progress message, checkpoint, CI state nor scheduler `DONE` terminates the parent user objective by itself. `active_turn_liveness.json` remains authoritative for same-turn continuation and successor evaluation.
