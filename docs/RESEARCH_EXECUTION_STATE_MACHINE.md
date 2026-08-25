# Enterprise Math Research Execution State Machine

Status: `ACTIVE_CANONICAL_ON_MERGE`

Canonical machine-readable authority: `research_execution_state_machine.json`.

This protocol applies to every concrete `RESEARCHER` task execution. It also governs Driver recovery/review of those executions. It does **not** replace scheduler task state, Researcher-ID state, axiom-candidate maturity, theorem truth, or Foundation/canonical promotion.

## 1. The one rule everyone must remember

A taskbook being `READY`, a scheduler item being `CLAIMED`, or a researcher saying “done” does **not** mean mathematics may start or that the execution is complete.

For a concrete execution, mathematics is legal only after the runtime state reaches:

`EXECUTION_READY`

If the task declares any `PRE_MATH` execution gate, the required route is:

`CLAIMED -> IDENTITY_READY -> PRE_MATH_GATES_PENDING -> EXECUTION_READY -> IN_PROGRESS`

The jump

`PRE_MATH_GATES_PENDING -> IN_PROGRESS`

is forbidden.

## 2. Four independent dimensions

Do not collapse these into one status word:

1. **Scheduler task state** — who may work and whether a task is leased/queued.
2. **Execution state** — whether this concrete run is legally allowed to start/continue/return.
3. **Identity state** — whether the conversation has a valid Researcher-ID/Driver-ID.
4. **Mathematical/candidate truth state** — whether a theorem, obstruction, axiom candidate or canonical artifact has been reviewed/promoted.

Examples:

- scheduler `CLAIMED` + execution `PRE_MATH_GATES_PENDING` => **no mathematics yet**;
- execution `RETURN_ACCEPTED` => Driver accepted the return as a valid run, but no theorem/candidate promotion follows automatically;
- a failed publication stamp before mathematics => `NONSTART_TERMINAL`, **not** a negative mathematical verdict.

## 3. Mandatory startup protocol for researchers

For every task execution:

1. Read only the taskbook and control-plane/startup material permitted before mathematics.
2. Resolve/allocate the required role identity.
3. Read the taskbook frontmatter fields:
   - `execution_state_policy`;
   - `execution_gates`.
4. If `execution_gates` contains no `PRE_MATH` gate, classify startup as `EXECUTION_READY` only after the taskbook itself passed dispatch audit and identity is ready.
5. If any `PRE_MATH` gate exists, enter `PRE_MATH_GATES_PENDING`.
6. Satisfy every PRE_MATH gate exactly as declared and verify the required durable evidence.
7. Only then enter `EXECUTION_READY` and read mathematical sources / perform mathematical derivations.

A chat claim, intention, screenshot without the required repository evidence, local-only file, or “I already completed it” statement does not satisfy a durable gate.

## 4. Mandatory taskbook fields

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

## 5. Mandatory Driver protocol

Before dispatch:

- audit the taskbook against current taskbook policy;
- audit its execution-state metadata/gates;
- bind a runtime identity outside the reusable taskbook when manual dispatch requires it.

On return:

- review the durable return/evidence, not the conversation’s self-reported status;
- classify the execution result separately from mathematical truth/promotion;
- after `RETURN_ACCEPTED`, evaluate closure/successor routing under the existing liveness and lineage contracts.

On stalled or ambiguous conversations:

`... -> RECOVERY_REQUIRED`

Then reconstruct the last legal state from durable repository evidence only. Resume only from an evidenced legal frontier. If no safe frontier exists, use `REDISPATCH_REQUIRED`.

## 6. F5A regression rule

The following historical failure mode is permanently guarded:

> A researcher reports completion, but a mandatory pre-math remote branch/stamp is absent.

The execution must **not** be classified `EXECUTION_READY`, `IN_PROGRESS`, `RETURN_ACCEPTED`, or `CLOSED`. It is a startup/liveness failure and must end in `NONSTART_TERMINAL` or a recovery/redispatch path.

## 7. Machine checks

Validate the machine:

```bash
python tools/research_execution_state.py validate-machine
```

Audit task execution metadata:

```bash
python tools/research_execution_state.py audit-taskbook research_tasks/<TASK>.md
```

Ask whether an action is legal in a state:

```bash
python tools/research_execution_state.py check-action \
  --state PRE_MATH_GATES_PENDING \
  --action MATHEMATICAL_SOURCE_READ
```

Expected result: `BLOCKED`.

Check a transition and its required evidence:

```bash
python tools/research_execution_state.py next-state \
  --state PRE_MATH_GATES_PENDING \
  --event PRE_MATH_GATES_SATISFIED \
  --evidence-json '{"durable_evidence_refs_for_all_pre_math_gates":["commit:..."],"remote_verification_if_required_by_gate":"verified"}'
```

## 8. Handoff and recovery

A durable handoff is terminal for the current execution instance unless the same conversation is explicitly resumed. A genuinely new conversation performs identity bootstrap again and binds a new execution instance; it may consume the previous durable handoff as its frontier.

Neither a tool call, progress message, checkpoint, CI state nor scheduler `DONE` terminates the parent user objective by itself. `active_turn_liveness.json` remains authoritative for same-turn continuation and successor evaluation.
