# Enterprise Math Research Taskbook Authoring and Review

Status: `ACTIVE / CANONICAL TASKBOOK AUTHORING PROCESS / V5`
Effective: `2026-08-25`
Contract: `research_taskbook_contract.json`
Architecture: `research_architecture.json`
Execution lifecycle: `research_execution_state_machine.json`
Execution protocol: `docs/RESEARCH_EXECUTION_STATE_MACHINE.md`
Candidate lifecycle: `research_axiom_candidate_state_machine.json`

## Purpose

A taskbook is a **task-specific execution contract**. It is not a second copy of repository policy, a fixed runtime identity binding, a raw free-research candidate, or proof that a concrete execution already crossed its gates.

A good taskbook contains the mother question, frozen inputs/scope, task-local deliverables/evidence, PASS/KILL/return criteria, origin, lineage, machine-readable execution gates, and any narrow temporary policy override.

## 1. Declare task origin

Every new taskbook declares `origin_kind`:

- `DIRECT_USER_DIRECTION`;
- `DRIVER_ROADMAP`;
- `FREE_AXIOM_CANDIDATE`;
- `FOUNDATION_QUESTION`;
- `REPLAY_OR_INTEGRATION`;
- `MAINTENANCE`.

For `FREE_AXIOM_CANDIDATE`, include `origin_candidate_id` and an audited intake-eligible `origin_candidate_state`. A raw blind candidate may not be relabeled as Driver roadmap work. For `FOUNDATION_QUESTION`, include `origin_foundation_question_id`.

## 2. Choose task lineage

Every newly authored taskbook declares:

- `NEW_DIRECTION`;
- `CONTINUATION`;
- `REPLAY`;
- `INTEGRATION`;
- `MAINTENANCE`.

`CONTINUATION` requires `parent_task_id` plus a complete successor gate: new information gap, why the parent does not close it, discriminating outcomes, kill condition, alternatives considered, and why a new stage/task is preferable to same-task continuation or closure.

Freeze:

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

Stage 2+ is continuation semantics. Renaming does not reset lineage.

## 3. Generate

New direction:

```bash
python tools/research_taskbook.py new \
  --task-id RS-... \
  --title "..." \
  --kind RESEARCH \
  --priority P1 \
  --leverage HIGH \
  --lane R... \
  --origin-kind DRIVER_ROADMAP \
  --lineage NEW_DIRECTION \
  --output research_tasks/....md
```

Continuation adds:

```bash
--lineage CONTINUATION --parent-task-id RS-PARENT-...
```

A free-candidate task adds its audited candidate ID/state.

The generator writes runtime-policy inheritance and starts with:

```json
"execution_state_policy": "INHERIT_GLOBAL",
"execution_gates": []
```

`[]` is only an initial classification. Replace it with exact task-local gates when the task has ordered startup/source/checker/verdict/return conditions.

## 4. Classify every task-local execution condition

### A. Before mathematics

Any instruction equivalent to “before mathematics”, “before reading mathematical sources”, or “first create/push/verify X, then start” is a `PRE_MATH` gate:

```json
{
  "gate_id": "START",
  "phase": "PRE_MATH",
  "must_precede": [
    "MATHEMATICAL_SOURCE_READ",
    "MATHEMATICAL_DERIVATION"
  ],
  "evidence": {"kind": "..."}
}
```

`POST_FREEZE_SOURCE_READ` inherits the generic source-read startup guard automatically.

### B. Some sources withheld until a later freeze

If Phase A may read its whitelist but current toolbox/prior-art/downstream sources must stay hidden until a named raw/independent freeze, use a MID gate:

```json
{
  "gate_id": "PHASE-A-FREEZE",
  "phase": "MID_EXECUTION",
  "must_precede": ["POST_FREEZE_SOURCE_READ"],
  "evidence": {
    "kind": "FROZEN_RETURN_AND_CHECKER"
  }
}
```

This allows ordinary already-visible `MATHEMATICAL_SOURCE_READ` while keeping the delayed source class blocked.

### C. Checker/audit before final verdict

If the task says a checkpoint/checker/audit must precede the primary/final verdict, guard:

`VERDICT_FREEZE`.

Do not guard only `RETURN_WRITE`; that would permit the verdict to freeze too early.

### D. Final materialization before return

If final manifest/checker/remote-owner evidence must exist before the return is persisted, use `PRE_RETURN` and guard:

`RETURN_WRITE`.

## 5. Remote gate versus remote override

A task-local remote startup/checkpoint may intentionally require branch/file publication. If its prose matches `TB-REMOTE-RUNTIME`, declare both:

1. the execution gate — which controls **when** the action becomes legal;
2. a narrow `policy_review.temporary_overrides` entry — which authorizes the exceptional task-local remote behavior.

The override never satisfies or waives the execution gate.

## 6. Write only task-local content

Include:

- mother question;
- frozen inputs/assumptions/exclusions;
- exact outputs;
- task-local witnesses/discriminators;
- PASS/KILL/return criteria;
- exact ordered execution evidence.

Do not paste generic GitHub, scheduler, identity, promotion, liveness, candidate-lifecycle or successor policy into the body.

## 7. Automatic review

Run:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md
```

Review checks metadata, origin, lineage, Stage anti-evasion, successor gate, fixed identity, policy digest, runtime-sensitive directives and execution-gate schema.

On approval:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md --approve
```

Approval also invokes execution-state/gate audit.

Machine pass does not replace Driver semantic mapping: the Driver must still recognize equivalent prose requiring `POST_FREEZE_SOURCE_READ`, `VERDICT_FREEZE`, or `RETURN_WRITE` gates.

## 8. Single dispatch gate

Immediately before every official-taskbook dispatch/re-dispatch:

```bash
python tools/research_control_gate.py audit research_tasks/<task>.md
```

This is the canonical composite gate. It includes current taskbook policy and execution-state audit.

A taskbook passing dispatch is still not a concrete execution at `EXECUTION_READY`; runtime identity/startup gates remain.

## 9. Runtime startup

After dispatch the researcher resolves identity, instantiates all gates `PENDING`, satisfies every PRE_MATH gate, then enters `EXECUTION_READY`.

Later source/checker/verdict/return gates remain active and must be checked at the point of their guarded action.

## 10. Runtime identity lives outside the reusable taskbook

Manual relay may allocate a Researcher-ID separately:

```bash
python tools/research_identity.py allocate \
  --task RS-... \
  --role RESEARCHER \
  --lane R... \
  --dispatch-id <unique-dispatch-id>
```

Persist runtime identity in the dispatch/relay envelope and research return, not as fixed reusable taskbook metadata.

## 11. Policy digest

`research_taskbook_policy.json` lists inherited policy inputs. The authoring tool hashes their exact Git blob identities into `policy_review.policy_digest`.

When any inherited policy input changes, a previously reviewed taskbook remains historical but fails new dispatch until review refreshes its stamp.

Do not duplicate global policy text into taskbooks to simulate synchronization.
