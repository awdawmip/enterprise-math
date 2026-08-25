# Enterprise Math Research Taskbook Authoring and Review

Status: `ACTIVE / CANONICAL TASKBOOK AUTHORING PROCESS / V4`
Effective: `2026-08-25`
Contract: `research_taskbook_contract.json`
Publication contract: `research_task_publication_contract.json`
Registry: `research_task_registry.json`
Mandatory template: `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`
Publication tool: `tools/research_task_registry.py`
Architecture: `research_architecture.json`
Candidate lifecycle: `research_axiom_candidate_state_machine.json`

## Purpose

A taskbook is the **task-specific research contract**. It is not the object that makes a task officially exist.

Freeze:

`TASKBOOK_FILE != PUBLISHED_TASK`.

A task becomes official only after the unified publication gate writes its canonical registry record and the registry audit passes.

A good taskbook contains mother question, frozen inputs/scope, hard target/deliverables, research value, PASS/KILL/return criteria, **origin** and **lineage**. It does not bind a runtime conversation identity or promote truth.

## 1. One mandatory publication template

All new official tasks—researcher, free researcher after audit, Driver, or Foundation Steward—start from:

`templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`.

Recommended generator:

```bash
python tools/research_task_registry.py new \
  --task-id RS-... \
  --title "..." \
  --publisher-role RESEARCHER \
  --parent-objective-id OBJ-... \
  --origin-kind DIRECT_USER_DIRECTION \
  --lineage NEW_DIRECTION \
  --output research_tasks/....md
```

Use `RESEARCH_DRIVER` or `FOUNDATION_STEWARD` in `--publisher-role` when appropriate. There is no separate Driver-only official task template.

The legacy `tools/research_taskbook.py` remains available as a parser/linter for historical taskbooks, but its old `new/review --approve` path is **not** the canonical publication gate.

## 2. Declare task origin

Every new taskbook declares one of:

- `DIRECT_USER_DIRECTION`;
- `DRIVER_ROADMAP`;
- `FREE_AXIOM_CANDIDATE`;
- `FOUNDATION_QUESTION`;
- `REPLAY_OR_INTEGRATION`;
- `MAINTENANCE`.

### Free-candidate origin

If `origin_kind=FREE_AXIOM_CANDIDATE`, include `origin_candidate_id` and `origin_candidate_state`.

Raw Phase-A candidates cannot publish tasks. After Phase-B audit, the allowed task-publication states are:

- `AUDITED_AXIOM_CANDIDATE`;
- `AUDITED_REPLACEMENT_CANDIDATE`;
- `EXACT_NEGATIVE_OBSTRUCTION`.

A researcher may publish directly from those audited states **without Driver intake merely to make the task exist**. Driver/Steward intake remains separate for portfolio rank, Working Truth, replication/Foundation and promotion decisions.

A raw candidate may not be relabeled `DRIVER_ROADMAP` to bypass provenance.

### Foundation-question origin

If `origin_kind=FOUNDATION_QUESTION`, include `origin_foundation_question_id`.

## 3. Choose task lineage

Every newly authored taskbook declares:

- `NEW_DIRECTION`;
- `CONTINUATION`;
- `REPLAY`;
- `INTEGRATION`;
- `MAINTENANCE`.

`CONTINUATION` requires `parent_task_id` and a complete successor gate:

- `new_information_gap`;
- `why_parent_result_does_not_close_it`;
- `discriminating_outcomes`;
- `kill_condition`;
- `alternative_route_or_free_exploration_considered`;
- `why_new_stage_or_task_is_better_than_same_task_or_closure`.

Freeze:

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

Stage 2+ is continuation semantics. Renaming does not reset lineage.

## 4. Write the five mandatory content sections

Every new publication contains at least:

1. Mother question;
2. Frozen inputs and scope;
3. Hard target and required outputs;
4. Research value to preserve;
5. Success, kill, and return criteria.

The `research_value` section must explain why this unresolved work is worth preserving even if the portfolio does not execute it immediately.

Do not paste generic GitHub, scheduler, identity, promotion, liveness or registry policy prose into the task body; inherit current repository policy.

## 5. Optional structural lint

Before publication, legacy taskbook tooling can still lint origin/lineage/conflicts:

```bash
python tools/research_taskbook.py audit research_tasks/<task>.md
```

This is a lint, not publication and not Driver approval.

## 6. Publish

After task-local content is complete:

```bash
python tools/research_task_registry.py publish \
  --taskbook research_tasks/<task>.md \
  --publisher-role RESEARCHER \
  --publisher-id EM-... \
  --parent-objective-id OBJ-... \
  --research-value "<why this task must not be lost>"
```

Publication transaction:

`NORMALIZE_TEMPLATE -> POLICY/ORIGIN/LINEAGE GATE -> REGISTRY RECORD -> TASKBOOK BLOB PIN -> ORPHAN AUDIT -> CLAIMABLE`.

A researcher does not need Driver approval for this publication transaction.

Researcher-published tasks receive effective rank `P2 / MEDIUM` by default while preserving the publisher's requested priority/leverage. Driver can later reprioritize the portfolio. An explicit user priority instruction controls over the default.

Freeze:

`TASK_PUBLICATION != WORKING_TRUTH`.

`TASK_PUBLICATION != FOUNDATION_STATUS`.

`TASK_PUBLICATION != CANONICAL_PROMOTION`.

## 7. Central registry and orphan prevention

Publication is complete only after:

```bash
python tools/research_task_registry.py audit
```

passes.

`research_task_registry.json` is the canonical task-existence surface.

For new/post-cutover work:

`NO REGISTRY RECORD -> NO READY / NO CLAIM / NO EXECUTION`.

A handoff, scheduler row, chat message or taskbook file cannot substitute for the registry record.

Every registered task includes:

- publisher role and identity;
- parent objective;
- taskbook path and pinned blob;
- origin/lineage;
- claimability/rank;
- research value;
- exact no-Working-Truth/no-promotion flags.

## 8. Valuable side-residue capture

A TASK researcher may publish a new valuable residue discovered during current work.

This is **capture**, not automatic task switching.

Publish the residue with exact parent objective/lineage/research value, then resume the current parent objective in the same turn unless its own completion rule says otherwise.

## 9. Temporary overrides

Task-local overrides remain narrow and explicit under `policy_review.temporary_overrides` with `conflict_id`, `scope`, `reason`, `replacement_behavior`, and `expires_when`.

An override cannot bypass the registry, free-candidate maturity, continuation gate, theorem truth, safety, owner isolation, terminal scope, stale-adoption integrity or promotion gates.

## 10. Dispatch identity lives outside the taskbook

Only after registered publication may a Driver-mediated relay allocate an execution Researcher-ID:

```bash
python tools/research_identity.py allocate \
  --task RS-... \
  --role RESEARCHER \
  --lane R... \
  --dispatch-id <unique-dispatch-id>
```

Publisher identity belongs to the registry record. Execution Researcher-ID belongs to owner/session runtime state. The reusable taskbook remains execution-ID-free.

## 11. Legacy cutover

Pre-cutover taskbooks/scheduler work remain `LEGACY_BASELINE_REGISTERED` for existing executions only; no bulk rewrite is required.

But:

`LEGACY TASK + FRESH REDISPATCH / MODIFICATION / CURRENT-POLICY REVIEW -> EXPLICIT REGISTRY MIGRATION`.

A policy update does not erase an already-running frozen execution, but all subsequent new publication/redispatch actions use the current registry contract.

## Design separation

- repository policy = how research operates;
- candidate packet = what was independently discovered;
- taskbook = exact research contract;
- task registry = whether the task officially exists and why it must be preserved;
- owner/session runtime = who executes it now and whether that conversation is alive;
- Driver portfolio = reprioritization/closure/Working Truth/promotion decisions;
- source `main` = gated canonical truth.

Keeping these layers separate prevents orphan tasks, provenance laundering, stale identity, duplicated rules and automatic stage cascades.
