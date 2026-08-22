# Enterprise Math Research Taskbook Authoring and Review

Status: `ACTIVE / CANONICAL TASKBOOK AUTHORING PROCESS / V3`
Effective: `2026-08-22`
Contract: `research_taskbook_contract.json`
Architecture: `research_architecture.json`
Candidate lifecycle: `research_axiom_candidate_state_machine.json`

## Purpose

A taskbook is a **task-specific execution contract**. It is not:

- a second copy of repository operating policy;
- a runtime conversation identity binding;
- a raw free-research candidate;
- a way to erase where a selected question came from;
- automatic evidence that a previous successful stage deserves another stage.

A good taskbook contains the mother question, frozen inputs/scope, task-local deliverables/evidence, PASS/KILL/return criteria, **origin**, **lineage**, and any narrow temporary policy override.

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

The generator also writes Driver/identity-policy metadata and a `policy_review` block initially marked:

`PENDING_DRIVER_REVIEW`.

It never assigns a fixed runtime Researcher-ID.

## 4. Write task-local content

Include only what is different about this task:

- mother question;
- frozen inputs/assumptions/exclusions;
- exact mathematical/executable/formal outputs;
- task-local witnesses/discriminators;
- PASS/KILL/return criteria.

Do not paste generic GitHub, scheduler, identity, promotion, liveness, Working Truth, candidate-lifecycle or successor-gate policy prose into the body. Those rules are inherited from repository policy.

If the task came from free discovery, Phase-B audit and Driver intake must already be complete and the candidate provenance remains in metadata.

## 5. Automatic audit

Run:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md
```

The audit checks:

- required metadata;
- task origin;
- free-candidate/Foundation provenance when applicable;
- task lineage;
- Stage-2+ anti-evasion;
- continuation successor gate;
- forbidden fixed runtime identity;
- stale policy digest;
- policy-sensitive runtime directives;
- generic policy restatement;
- temporary-override schema.

A machine pass does not replace Driver mathematical/semantic judgment. In particular, a semantically continuous route can still be misnamed to evade a lexical Stage check; the Driver must reject that misclassification.

## 6. Temporary overrides

If a task must intentionally differ from inherited policy, record a narrow item in:

`policy_review.temporary_overrides`.

Required fields:

- `conflict_id`;
- `scope`;
- `reason`;
- `replacement_behavior`;
- `expires_when`.

An override cannot silently weaken theorem truth, safety, authorization, owner isolation, candidate maturity, task-origin provenance, successor-stage requirements or canonical-promotion rules.

## 7. Driver approval

After findings are resolved:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md --approve
```

This refreshes the current policy digest and sets:

`policy_review.review_state = PASS`.

For a continuation, approval means the Driver accepted the **new information gap and route choice**, not merely the parent PASS.

## 8. Dispatch gate

Immediately before dispatch/re-dispatch:

```bash
python tools/research_taskbook.py audit research_tasks/<task>.md --dispatch
```

A taskbook is dispatchable only when this passes.

Historical taskbooks may remain unstamped or lack newer origin/lineage fields. They are preserved as provenance. A new dispatch under current policy requires current review and the missing current metadata.

## 9. Runtime identity lives outside the taskbook

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

## 10. Policy changes invalidate old stamps automatically

`research_taskbook_policy.json` lists the inherited policy inputs. The authoring tool hashes them into the taskbook policy digest.

When architecture/role/Driver/foundation semantics change:

1. the digest changes;
2. existing stamped taskbooks remain historical artifacts;
3. another dispatch fails until current Driver review refreshes the stamp;
4. only still-live taskbooks need re-review.

Do not copy global policy text into every taskbook to keep it “in sync”. The digest is the synchronization mechanism.

An already-running frozen research execution is not retroactively erased by a policy update; the new policy governs subsequent control-plane actions/re-dispatch according to its scope.

## Design separation

Repository policy answers:

> How does Enterprise Math research operate?

The axiom-candidate packet answers:

> What was independently discovered before the control plane selected it?

The taskbook origin/lineage answers:

> Why does this selected task exist, and what did it come from?

The taskbook body answers:

> What exact selected question is this researcher executing?

The dispatch envelope answers:

> Which concrete researcher conversation is executing it now?

Keeping these layers separate prevents route anchoring, provenance laundering, stale identity, duplicated rules and automatic stage cascades.
