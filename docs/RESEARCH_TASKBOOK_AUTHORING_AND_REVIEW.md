# Enterprise Math Research Taskbook Authoring and Review

Status: `ACTIVE / CANONICAL TASKBOOK AUTHORING PROCESS / V2`
Effective: `2026-08-22`
Contract: `research_taskbook_contract.json`
Architecture: `research_architecture.json`

## Purpose

A taskbook is a **task-specific execution contract**. It is not:

- a second copy of repository operating policy;
- a runtime conversation identity binding;
- a raw free-research candidate;
- automatic evidence that a previous successful stage deserves another stage.

A good taskbook contains only the mother question, frozen inputs/scope, task-local deliverables/evidence, PASS/KILL/return criteria, lineage, and any narrow temporary policy override.

## 1. Choose task lineage first

Every newly authored taskbook declares one of:

- `NEW_DIRECTION`;
- `CONTINUATION`;
- `REPLAY`;
- `INTEGRATION`;
- `MAINTENANCE`.

This is control-plane provenance, not mathematical truth.

### Continuation gate

`CONTINUATION` means the new task exists because a parent result exposed a genuinely new information gap.

It therefore requires:

- `parent_task_id`;
- `new_information_gap`;
- `why_parent_result_does_not_close_it`;
- `discriminating_outcomes`;
- `kill_condition`;
- `why_new_stage_or_task_is_better_than_same_task_or_closure`.

Freeze:

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

Stage numbering, recent success, momentum, unused ideas in a return report, or “there is more to explore” do not satisfy the gate.

If the frontier still belongs to the mother question, prefer `CONTINUE_SAME_TASK`. If no new discriminating gap remains, close/park/return to exploration rather than manufacturing another stage.

## 2. Generate

New direction:

```bash
python tools/research_taskbook.py new \
  --task-id RS-... \
  --title "..." \
  --kind RESEARCH \
  --priority P1 \
  --leverage HIGH \
  --lane R... \
  --lineage NEW_DIRECTION \
  --output research_tasks/....md
```

Continuation:

```bash
python tools/research_taskbook.py new \
  --task-id RS-... \
  --title "..." \
  --lane R... \
  --lineage CONTINUATION \
  --parent-task-id RS-PARENT-... \
  --output research_tasks/....md
```

The continuation skeleton intentionally leaves `successor_gate` incomplete. Driver review cannot approve it until those fields are filled.

The generator also writes Driver/identity-policy metadata and a `policy_review` block initially marked:

`PENDING_DRIVER_REVIEW`.

It never assigns a fixed runtime Researcher-ID.

## 3. Write task-local content

Include only what is different about this task:

- mother question;
- frozen inputs/assumptions/exclusions;
- exact mathematical/executable/formal outputs;
- task-local witnesses/discriminators;
- PASS/KILL/return criteria.

Do not paste generic GitHub, scheduler, identity, promotion, liveness, Working Truth or successor-gate prose into the body. Those rules are inherited from repository policy.

If the task came from a free-research axiom candidate, the candidate must already have passed Phase-B audit and Driver intake under `research_axiom_candidate_state_machine.json`. Do not turn a raw blind candidate directly into a dispatchable taskbook.

## 4. Automatic audit

Run:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md
```

The audit checks:

- required metadata;
- task lineage;
- continuation successor gate;
- forbidden fixed runtime identity;
- stale policy digest;
- policy-sensitive runtime directives;
- generic policy restatement;
- temporary-override schema.

A machine pass does not replace Driver mathematical judgment.

## 5. Temporary overrides

If a task must intentionally differ from inherited policy, record a narrow item in:

`policy_review.temporary_overrides`.

Required fields:

- `conflict_id`;
- `scope`;
- `reason`;
- `replacement_behavior`;
- `expires_when`.

An override cannot silently weaken theorem truth, safety, authorization, owner isolation, candidate maturity, successor-stage requirements or canonical-promotion rules.

## 6. Driver approval

After findings are resolved:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md --approve
```

This refreshes the current policy digest and sets:

`policy_review.review_state = PASS`.

For a continuation, approval also means the Driver has explicitly accepted the successor information gap—not merely the parent PASS.

## 7. Dispatch gate

Immediately before dispatch/re-dispatch:

```bash
python tools/research_taskbook.py audit research_tasks/<task>.md --dispatch
```

A taskbook is dispatchable only when this passes.

Historical taskbooks may remain unstamped or lack newer lineage fields. They are preserved as provenance. A new dispatch under current policy requires current review.

## 8. Runtime identity lives outside the taskbook

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

## 9. Policy changes invalidate old stamps automatically

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

The taskbook answers:

> What exact selected question is this researcher executing, and why does this task exist?

The dispatch envelope answers:

> Which concrete researcher conversation is executing it now?

The axiom-candidate packet answers:

> What was independently discovered before the control plane selected it?

Keeping these layers separate prevents route anchoring, stale identity, duplicated rules and automatic stage cascades.
