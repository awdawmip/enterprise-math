# Enterprise Math Research Taskbook Authoring and Review

Status: `ACTIVE / CANONICAL TASKBOOK AUTHORING PROCESS / V5`
Effective: `2026-09-01`
Classification: `NO_NEW_MATHEMATICS`

Canonical machine sources:

- `research_task_publication_contract_v2.json`;
- `research_task_records/<task-id>/<publication-id>.json`;
- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`;
- `tools/research_task_records.py`;
- `docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md`.

Legacy compatibility only:

- `research_task_publication_contract.json`;
- `research_task_registry.json`;
- `tools/research_task_registry.py`.

The V1 shared-registry path is read-only after cutover. It may be inspected for historical compatibility but must not publish, replace or select new official work.

## 1. Purpose

A taskbook is the task-specific research contract. It is not itself task authority.

Freeze:

`TASKBOOK_FILE != PUBLISHED_TASK`.

`OFFICIAL_POST_CUTOVER_TASK -> IMMUTABLE_V2_PUBLICATION_RECORD`.

`UNREGISTERED_NEW_TASK -> NO READY / NO CLAIM / NO EXECUTION`.

A good taskbook fixes the mother question, exact inputs/scope, hard target, required outputs, research value, PASS/KILL/return criteria, origin and lineage. It does not bind one runtime conversation identity and does not promote truth.

## 2. One mandatory template

All new official tasks—Researcher, audited Free Researcher, Driver or Foundation Steward—start from:

`templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`.

Create a V2 draft with:

```text
python tools/research_task_records.py new \
  --task-id RS-... \
  --title "..." \
  --publisher-role <RESEARCHER|RESEARCH_DRIVER|FOUNDATION_STEWARD> \
  --parent-objective-id OBJ-... \
  --origin-kind <ORIGIN> \
  --lineage <LINEAGE> \
  --output research_tasks/<TASK>.md
```

Do not paste generic GitHub, CI, scheduler, liveness, identity or promotion policy into each taskbook. Inherit current repository policy and keep the taskbook task-local.

## 3. Origin and lineage

Allowed origins include:

- `DIRECT_USER_DIRECTION`;
- `DRIVER_ROADMAP`;
- `FREE_AXIOM_CANDIDATE`;
- `FOUNDATION_QUESTION`;
- `REPLAY_OR_INTEGRATION`;
- `MAINTENANCE`.

Allowed lineage classes are:

- `NEW_DIRECTION`;
- `CONTINUATION`;
- `REPLAY`;
- `INTEGRATION`;
- `MAINTENANCE`.

A free-discovery task preserves its exact audited candidate identity/state. Raw Phase-A candidates are not task-publication eligible.

`CONTINUATION` requires the exact parent task and a complete successor gate: new information gap, why the parent does not close it, discriminating outcomes, kill condition, alternative route/free exploration considered, and why a new task is better than same-task continuation or closure.

Freeze:

`PASS_IS_NOT_A_SUCCESSOR_TRIGGER`.

`RENAMING_DOES_NOT_RESET_LINEAGE`.

## 4. Five mandatory content sections

Every taskbook contains nonempty task-local sections for:

1. Mother question;
2. Frozen inputs and scope;
3. Hard target and required outputs;
4. Research value to preserve;
5. Success, kill and return criteria.

The task also carries a nonempty `parent_objective_id`, exact frontier and first executable `next_action`.

## 5. Prepare and publish through V2

Preparation validates and normalizes the taskbook but creates no authority:

```text
python tools/research_task_records.py prepare \
  --taskbook research_tasks/<TASK>.md \
  --publisher-role <ROLE> \
  --parent-objective-id <PARENT_OBJECTIVE>
```

Publish exactly one immutable generation:

```text
python tools/research_task_records.py publish \
  --taskbook research_tasks/<TASK>.md \
  --publisher-role <ROLE> \
  --publisher-id <Researcher-ID|Driver-ID|Steward-ID> \
  --research-value "<WHY THIS TASK MUST NOT BE LOST>"
```

A correction creates a new immutable generation and names the exact predecessor with:

```text
--supersedes-publication-id <PRIOR_PUBLICATION_ID>
```

No overwrite/replace operation exists.

After publication, run the canonical audits:

```text
python tools/research_task_records.py audit
python tools/check_task_registry_cutover.py
```

Researcher publication defaults to effective `P2 / MEDIUM` unless an explicit higher authority says otherwise. Requested priority remains provenance until Driver reprioritization.

Freeze:

`TASK_PUBLICATION != WORKING_TRUTH`.

`TASK_PUBLICATION != FOUNDATION_STATUS`.

`TASK_PUBLICATION != CANONICAL_PROMOTION`.

## 6. Remote-manual fallback

When local execution is unavailable but direct GitHub mutation is possible, follow the exact equivalent-preflight and CAS requirements in `docs/RESEARCH_TASK_PUBLICATION_PROTOCOL.md`.

Remote/manual transport is not a second semantic publication path. If equivalent V2 preflight cannot be reproduced, stop at a non-executable draft or handoff; do not fabricate task authority.

## 7. Publication and handoff are not PR gates

A taskbook/result becomes durable through a reachable branch or tag, immutable commit SHA and exact repository paths. V2 publication and Researcher handoff do not require opening a Pull Request, changing Draft/Ready state, waiting for CI or waiting for merge unless the exact task or an active Driver/integration decision explicitly requires that operation.

Freeze:

`DURABLE_HANDOFF != OPEN_PR`.

`TASK_PUBLICATION != PR_CREATION`.

`CI_PENDING_NONBLOCKING -> CONTINUE_PARENT_TASK`.

The default Researcher checkpoint is one batched branch/commit handoff. A PR is an optional review/integration surface, not the durable storage primitive.

## 8. Valuable side residue

A task researcher may publish valuable unresolved residue through the same V2 gate. Publication is capture, not task switching. After the subflow succeeds, resume the current parent objective in the same turn unless its real terminal rule has been met.

## 9. Identity and runtime separation

Publisher identity belongs to the immutable publication record. Execution Researcher-ID and winning CLAIM belong to runtime owner/session state. Reusable taskbooks remain execution-ID-free.

## 10. Legacy boundary

Already-owned compatible legacy executions may finish under their frozen authority. Fresh redispatch, modification or current-policy review of a legacy task requires explicit V2 migration.

Historical V1 files remain provenance and compatibility evidence only; they are not current publication authority.
