# Enterprise Math Research Taskbook Authoring and Review

Status: `ACTIVE / CANONICAL TASKBOOK AUTHORING PROCESS / V4`
Effective: `2026-08-23`
Contract: `research_taskbook_contract.json`
Architecture: `research_architecture.json`
Candidate lifecycle: `research_axiom_candidate_state_machine.json`
Tool policy: `tool_invocation_policy.json`

## Purpose

A taskbook is a task-specific execution contract. It is not:

- a second copy of repository operating policy;
- a runtime conversation identity binding;
- a raw free-research candidate;
- a way to erase task origin or lineage;
- automatic evidence that a successful parent deserves another stage.

A good taskbook contains the mother question, frozen inputs/scope,
deliverables/evidence, PASS/KILL/return criteria, origin, lineage and any narrow
temporary override.

## 1. Required inherited-policy markers

Every newly authored or re-reviewed dispatchable taskbook carries:

- `final_response_identity_policy = INHERIT_GLOBAL`;
- `tool_invocation_policy = INHERIT_GLOBAL`.

These compact fields solve the strict taskbook-only last mile.

The identity field exposes that every final response needs the global role
footer. The tool field exposes that ordinary TASK work must understand the task
first, then look up existing tools before inventing a general mechanism.

Neither field copies the full policy into the mathematical body.

For an explicit blind-forward/source-whitelist task, tool names remain hidden
until the taskbook's named freeze point. Immediately after freeze, the normal
dedup lookup becomes mandatory. The inheritance field does not weaken the
firewall and does not preload a discovery menu.

## 2. Declare task origin

Every new taskbook declares `origin_kind`:

- `DIRECT_USER_DIRECTION`;
- `DRIVER_ROADMAP`;
- `FREE_AXIOM_CANDIDATE`;
- `FOUNDATION_QUESTION`;
- `REPLAY_OR_INTEGRATION`;
- `MAINTENANCE`.

For `FREE_AXIOM_CANDIDATE`, include `origin_candidate_id` and an intake-eligible
`origin_candidate_state`. A raw blind candidate may not be laundered into
`DRIVER_ROADMAP`.

For `FOUNDATION_QUESTION`, include `origin_foundation_question_id`.

## 3. Choose task lineage

Every new taskbook declares:

- `NEW_DIRECTION`;
- `CONTINUATION`;
- `REPLAY`;
- `INTEGRATION`;
- `MAINTENANCE`.

`CONTINUATION` requires:

- `parent_task_id`;
- `new_information_gap`;
- `why_parent_result_does_not_close_it`;
- `discriminating_outcomes`;
- `kill_condition`;
- `alternative_route_or_free_exploration_considered`;
- `why_new_stage_or_task_is_better_than_same_task_or_closure`.

Freeze:

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

Any task explicitly named Stage 2 or later is continuation semantics. Renaming
the next unresolved layer does not reset lineage.

## 4. Generate

Example:

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

The generator writes:

- Driver/task authority;
- identity inheritance;
- tool-invocation inheritance;
- origin and lineage;
- a policy-review stamp marked `PENDING_DRIVER_REVIEW`.

It never writes a fixed runtime Researcher-ID.

## 5. Write task-local content

Include only task-specific material:

- mother question;
- inputs/assumptions/exclusions;
- outputs;
- witnesses/discriminators;
- PASS/KILL/return criteria.

Do not paste generic GitHub, scheduler, identity, promotion, liveness, tool
catalog, Working Truth, candidate-lifecycle or successor-gate prose into the
body. These rules are inherited through policy and digest.

If the task came from free discovery, Phase-B audit and Driver intake must
already be complete and the provenance remains in metadata.

## 6. Automatic audit

Run:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md
```

The audit checks:

- required metadata;
- identity-footer inheritance;
- tool-invocation inheritance;
- origin and provenance;
- lineage and Stage-2+ anti-evasion;
- successor gate;
- forbidden fixed runtime identity;
- stale policy digest;
- policy-sensitive directives;
- generic policy restatement;
- temporary-override schema.

A machine pass does not replace Driver semantic judgment.

## 7. Temporary overrides

Record a narrow override under:

`policy_review.temporary_overrides`.

Required fields:

- `conflict_id`;
- `scope`;
- `reason`;
- `replacement_behavior`;
- `expires_when`.

An override cannot silently weaken theorem truth, safety, authorization,
ownership, candidate maturity, origin, successor rules, role identity visibility
or post-freeze tool dedup.

## 8. Driver approval

After findings are resolved:

```bash
python tools/research_taskbook.py review research_tasks/<task>.md --approve
```

This refreshes the current digest and sets
`policy_review.review_state = PASS`.

## 9. Dispatch gate

Immediately before dispatch/re-dispatch:

```bash
python tools/research_taskbook.py audit research_tasks/<task>.md --dispatch
```

Historical taskbooks remain provenance artifacts. A new dispatch under current
policy requires current metadata and a fresh stamp.

## 10. Runtime identity lives outside the taskbook

For a new Driver-mediated researcher conversation:

```bash
python tools/research_identity.py allocate \
  --task RS-... \
  --role RESEARCHER \
  --lane R... \
  --dispatch-id <unique-dispatch-id>
```

The reusable taskbook remains runtime-ID-free.

## 11. Policy changes invalidate old stamps

`research_taskbook_policy.json` lists inherited inputs. The authoring tool
hashes them into the taskbook policy digest.

A change to `final_response_identity_policy.json`,
`tool_invocation_policy.json`, the taskbook contract, or another policy input
makes prior stamps stale for redispatch. Running frozen work is not
retroactively erased.

## Design separation

Repository policy answers how research operates.

The candidate packet answers what was independently discovered.

Taskbook origin/lineage answers why the selected task exists.

The taskbook body answers what exact selected question is executed.

The dispatch envelope answers which concrete researcher conversation executes
it.

The registry/inventory/executable router answers which reusable machinery is
already available at the role-appropriate time.
