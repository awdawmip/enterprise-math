# Enterprise Math Research Taskbook Authoring and Review

Status: `ACTIVE / CANONICAL TASKBOOK AUTHORING PROCESS / V4`
Effective: `2026-08-25`
Contract: `research_taskbook_contract.json`
Architecture: `research_architecture.json`
Execution lifecycle: `research_execution_state_machine.json`
Execution protocol: `docs/RESEARCH_EXECUTION_STATE_MACHINE.md`
Candidate lifecycle: `research_axiom_candidate_state_machine.json`

## Purpose

A taskbook is a **task-specific execution contract**. It is not:

- a second copy of repository operating policy;
- a runtime conversation identity binding;
- a raw free-research candidate;
- a way to erase where a selected question came from;
- automatic evidence that a previous successful stage deserves another stage;
- evidence that a concrete execution has already crossed its startup gates.

A good taskbook contains the mother question, frozen inputs/scope, task-local deliverables/evidence, PASS/KILL/return criteria, **origin**, **lineage**, machine-readable **execution gates**, and any narrow temporary policy override.

## 1. Declare task origin

Every new taskbook declares `origin_kind`:

- `DIRECT_USER_DIRECTION`;
- `DRIVER_ROADMAP`;
- `FREE_AXIOM_CANDIDATE`;
- `FOUNDATION_QUESTION`;
- `REPLAY_OR_INTEGRATION`;
- `MAINTENANCE`.

This prevents a selected task from losing its provenance as it moves into execution.

### Free-candidate origin

If `origin_kind=FREE_AXIOM_CANDIDATE`, the taskbook must include:

- `origin_candidate_id`;
- `origin_candidate_state`.

The state must already be one of the audit/intake-eligible states defined by `research_taskbook_contract.json`.

A raw blind candidate may not become a taskbook by simply being relabeled `DRIVER_ROADMAP`.

### Foundation-question origin

If `origin_kind=FOUNDATION_QUESTION`, include `origin_foundation_question_id`.

## 2. Choose task lineage

Every newly authored taskbook declares one of:

- `NEW_DIRECTION`;
- `CONTINUATION`;
- `REPLAY`;
- `INTEGRATION`;
- `MAINTENANCE`.

Origin and lineage are different: a task can originate in a free candidate and still be a continuation of a later research task, or originate in the Driver roadmap and be a genuinely new direction.

### Continuation gate

`CONTINUATION` means a parent result exposed a genuinely new information gap.

It requires:

- `parent_task_id`;
- `new_information_gap`;
- `why_parent_result_does_not_close_it`;
- `discriminating_outcomes`;
- `kill_condition`;
- `alternative_route_or_free_exploration_considered`;
- `why_new_stage_or_task_is_better_than_same_task_or_closure`.

Freeze:

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

Stage numbering, recent success, momentum, unused ideas in a return report, or “there is more to explore” do not satisfy the gate.

Any task explicitly named **Stage 2 or later** is continuation semantics by construction and the machine audit requires `task_lineage=CONTINUATION`.

Renaming the next unresolved layer to avoid the word “Stage” does not make it a new direction when the parent result remains a necessary research premise/motivation. Driver semantic review must preserve lineage even where a lexical checker cannot infer it.

If the frontier still belongs to the mother question, prefer `CONTINUE_SAME_TASK`. If no new discriminating gap remains, close/park/return to exploration rather than manufacturing another stage.

## 3. Generate

New Driver-roadmap direction:

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

Continuation:

```bash
python tools/research_taskbook.py new \
  --task-id RS-...-STAGE2-... \
  --title "... Stage 2 ..." \
  --lane R... \
  --origin-kind DRIVER_ROADMAP \
  --lineage CONTINUATION \
  --parent-task-id RS-PARENT-... \
  --output research_tasks/....md
```

Task opened from an audited free candidate:

```bash
python tools/research_taskbook.py new \
  --task-id RS-... \
  --title "..." \
  --origin-kind FREE_AXIOM_CANDIDATE \
  --origin-candidate-id AX-... \
  --origin-candidate-state AUDITED_AXIOM_CANDIDATE \
  --lineage NEW_DIRECTION \
  --output research_tasks/....md
```

The continuation skeleton intentionally leaves `successor_gate` incomplete. Driver review cannot approve it until all fields are filled.

The generator writes Driver/identity-policy metadata, execution-state inheritance, `execution_gates=[]`, and a `policy_review` block initially marked:

`PENDING_DRIVER_REVIEW`.

`execution_gates=[]` is only a starting classification. The Driver must replace it with exact gate objects when the task body contains any startup/publication/source/firewall gate.

The generator never assigns a fixed runtime Researcher-ID.

## 4. Declare execution gates

Every new or re-dispatched taskbook carries:

```json
"execution_state_policy": "INHERIT_GLOBAL",
"execution_gates": []
```

Use `[]` only when the task truly has no task-local execution gate.

Any instruction of the form “before mathematics”, “before reading mathematical sources”, “first create/push/verify X, then start”, or equivalent must be represented as a machine-readable gate. A standard pre-math gate looks like:

```json
{
  "gate_id": "UNIQUE-ID",
  "phase": "PRE_MATH",
  "must_precede": [
    "MATHEMATICAL_SOURCE_READ",
    "MATHEMATICAL_DERIVATION"
  ],
  "evidence": {
    "kind": "DURABLE_EVIDENCE_KIND",
    "path": "optional/exact/path"
  }
}
```

For remote publication/liveness gates, include exact branch/path/required-field constraints in `evidence`. If the task body necessarily contains a policy-sensitive remote directive such as `push`, also declare the narrow `TB-REMOTE-RUNTIME` temporary override. The override authorizes that task-local remote behavior; it does **not** waive or satisfy the execution gate.

## 5. Write task-local content

Include only what is different about this task:

- mother question;
- frozen inputs/assumptions/exclusions;
- exact mathematical/executable/formal outputs;
- task-local witnesses/discriminators;
- PASS/KILL/return criteria;
- task-specific execution gate details where needed.

Do not paste generic GitHub, scheduler, identity, promotion, liveness, Working Truth, candidate-lifecycle or successor-gate policy prose into the body. Those rules are inherited from repository policy.

If the task came from free discovery, Phase-B audit and Driver intake must already be complete and the candidate provenance remains in metadata.

## 6. Automatic review

Run:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md
```

The review checks the ordinary taskbook contract. On `--approve`, the tool also invokes execution-state/gate auditing.

Checks include:

- required metadata;
- task origin;
- free-candidate/Foundation provenance when applicable;
- task lineage;
- Stage-2+ anti-evasion;
- continuation successor gate;
- forbidden fixed runtime identity;
- execution-state inheritance;
- execution-gate schema and PRE_MATH coverage;
- stale policy digest;
- policy-sensitive runtime directives;
- generic policy restatement;
- temporary-override schema.

A machine pass does not replace Driver mathematical/semantic judgment. In particular, a semantically continuous route can still be misnamed to evade a lexical Stage check; likewise a task-local startup requirement can be omitted from `execution_gates` unless the Driver cross-checks the body.

## 7. Temporary overrides

If a task must intentionally differ from inherited policy, record a narrow item in:

`policy_review.temporary_overrides`.

Required fields:

- `conflict_id`;
- `scope`;
- `reason`;
- `replacement_behavior`;
- `expires_when`.

An override cannot silently weaken theorem truth, safety, authorization, owner isolation, candidate maturity, task-origin provenance, successor-stage requirements, execution gates or canonical-promotion rules.

## 8. Driver approval

After findings are resolved:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md --approve
```

This refreshes the current policy digest, sets:

`policy_review.review_state = PASS`,

and refuses approval if the execution-state/gate audit is invalid.

For a continuation, approval means the Driver accepted the **new information gap and route choice**, not merely the parent PASS.

## 9. Single dispatch gate

Immediately before every dispatch/re-dispatch run exactly:

```bash
python tools/research_control_gate.py audit research_tasks/<task>.md
```

This is the canonical composite gate. It covers the current taskbook policy audit **and** execution-state/gate audit.

A taskbook is dispatchable only when this passes.

Historical taskbooks may remain unstamped or lack newer origin/lineage/execution fields. They are preserved as provenance. A new dispatch under current policy requires current review and the missing current metadata.

## 10. Runtime startup after dispatch

A taskbook passing dispatch is still not the same as a concrete execution reaching `EXECUTION_READY`.

The researcher must resolve identity and then:

- if there is no `PRE_MATH` gate, classify startup and enter `EXECUTION_READY`;
- if any `PRE_MATH` gate exists, remain `PRE_MATH_GATES_PENDING` until all required durable evidence is verified.

Only `EXECUTION_READY` / `IN_PROGRESS` permit `MATHEMATICAL_SOURCE_READ` and `MATHEMATICAL_DERIVATION`.

## 11. Runtime identity lives outside the taskbook

For Driver-mediated manual relay into a new researcher conversation:

```bash
python tools/research_identity.py allocate \
  --task RS-... \
  --role RESEARCHER \
  --lane R... \
  --dispatch-id <unique-dispatch-id>
```

Persist the resulting Researcher-ID in the dispatch/relay envelope and receiving research return metadata.

The reusable taskbook remains runtime-ID-free.

Scheduler CLAIMs and direct task entry use their own identity bootstrap. Driver conversations expose Driver-ID, not Researcher-ID.

## 12. Policy changes invalidate old stamps automatically

`research_taskbook_policy.json` lists the inherited policy inputs. The authoring tool hashes them into the taskbook policy digest.

When architecture/role/Driver/execution/foundation semantics change:

1. the digest changes;
2. existing stamped taskbooks remain historical artifacts;
3. another dispatch fails until current Driver review refreshes the stamp;
4. only still-live taskbooks need re-review.

Do not copy global policy text into every taskbook to keep it “in sync”. The digest is the synchronization mechanism.

An already-running frozen research execution is not retroactively erased by a policy update; the new policy governs subsequent control-plane actions/re-dispatch according to its scope.

## Design separation

Repository policy answers:

> How does Enterprise Math research operate?

The execution state machine answers:

> What may this concrete run legally do **now**, and what durable evidence is required to move next?

The axiom-candidate packet answers:

> What was independently discovered before the control plane selected it?

The taskbook origin/lineage answers:

> Why does this selected task exist, and what did it come from?

The taskbook body answers:

> What exact selected question is this researcher executing?

The dispatch envelope answers:

> Which concrete researcher conversation is executing it now?

Keeping these layers separate prevents route anchoring, provenance laundering, stale identity, duplicated rules, pre-math gate bypass and automatic stage cascades.
