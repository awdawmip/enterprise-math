# Enterprise Math Unified Task Publication Protocol

Status: `ACTIVE / CANONICAL TASK PUBLICATION / V2`

Canonical machine sources:

- `research_task_publication_contract_v2.json`
- `research_task_records/<task-id>/<publication-id>.json`
- `research_runtime_state_machine.json`
- `research_dispatch_contract.json`
- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`

Executable gates:

- `tools/research_task_records.py`
- `tools/check_task_registry_cutover.py`
- canonical control dispatch: `research_control_dispatch.py`

Legacy compatibility only:

- `research_task_publication_contract.json`
- `research_task_registry.json`
- `tools/research_task_registry.py`

The V1 shared-registry surface is read-only after cutover. It may audit/show historical compatibility state, but it must never create, publish, replace, or select new official work.

## 1. One post-cutover publication path

Every new or modified official task uses the immutable V2 transaction regardless of publisher role.

Allowed publishers:

- `RESEARCHER` — including ordinary task researchers and free researchers after the free-candidate audit boundary;
- `RESEARCH_DRIVER`;
- `FOUNDATION_STEWARD` for governance tasks.

Freeze:

`TASKBOOK_FILE != PUBLISHED_TASK`.

`HANDOFF_TEXT != PUBLISHED_TASK`.

`V1_REGISTRY_ROW != POST_CUTOVER_TASK_AUTHORITY`.

`OFFICIAL_POST_CUTOVER_TASK -> IMMUTABLE_V2_PUBLICATION_RECORD`.

`V2_PUBLICATION_RECORD_CREATED -> TASK_EXISTS`.

There is no Driver-only publication lane and no alternate shared-registry write path.

## 2. Publication authority and truth separation

A researcher may publish a new task without Driver approval after satisfying the same V2 machine gate.

Publication does **not** grant:

- Working Truth;
- Foundation status;
- canonical promotion;
- theorem truth;
- global priority authority;
- Driver authority.

Researcher-published tasks default to effective `P2 / MEDIUM`. Publisher priority/leverage requests remain provenance only until a separate authority changes effective portfolio rank.

## 3. Free-research publication

FREE Phase A remains blind and does not publish task agenda items while discovery is raw.

After Phase B, an audited free candidate in one of:

- `AUDITED_AXIOM_CANDIDATE`;
- `AUDITED_REPLACEMENT_CANDIDATE`;
- `EXACT_NEGATIVE_OBSTRUCTION`

may be published directly by the researcher through V2 while preserving:

- `origin_kind=FREE_AXIOM_CANDIDATE`;
- candidate id;
- audited candidate state;
- semantic lineage.

Publication still does not make the candidate Working Truth.

## 4. Valuable residue capture

A task researcher may publish a follow-up task at a semantic checkpoint when work exposes valuable unresolved residue.

Required data includes:

- parent objective;
- exact lineage;
- parent task when the new task is a continuation;
- exact unresolved frontier;
- first executable next action;
- `research_value`: why the work is worth preserving even if not immediately selected.

Publication is capture, not a task switch and not a reason to stop the current parent turn.

## 5. Mandatory V2 transaction

All new task publications use:

`templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`.

The five mandatory taskbook sections remain:

1. Mother question;
2. Frozen inputs and scope;
3. Hard target and required outputs;
4. Research value to preserve;
5. Success, kill, and return criteria.

Create a V2 draft:

```text
python tools/research_task_records.py new \
  --task-id <TASK_ID> \
  --title <TITLE> \
  --publisher-role <RESEARCHER|RESEARCH_DRIVER|FOUNDATION_STEWARD> \
  --parent-objective-id <PARENT_OBJECTIVE> \
  --origin-kind <ORIGIN> \
  --lineage <LINEAGE> \
  --output research_tasks/<FILE>.md
```

After filling the task-local content, prepare it. Preparation validates/normalizes the taskbook but does not create task authority:

```text
python tools/research_task_records.py prepare \
  --taskbook research_tasks/<FILE>.md \
  --publisher-role <ROLE> \
  --parent-objective-id <PARENT_OBJECTIVE>
```

Publish exactly one immutable generation:

```text
python tools/research_task_records.py publish \
  --taskbook research_tasks/<FILE>.md \
  --publisher-role <ROLE> \
  --publisher-id <Researcher-ID|Driver-ID|Steward-ID> \
  --research-value "<WHY THIS TASK MUST NOT BE LOST>"
```

A correction is a new generation and must name the exact prior publication when applicable:

```text
--supersedes-publication-id <PRIOR_PUBLICATION_ID>
```

No V2 overwrite/replace operation exists.

Publication integrity is checked by:

```text
python tools/research_task_records.py audit
python tools/check_task_registry_cutover.py
```

### 5A. Chat / remote-manual fallback

A chat environment may have GitHub write access while lacking a local checkout or the ability to execute `tools/research_task_records.py`. That limitation does **not** create a second publication path and does not permit hand-authoring a V2 record from incomplete metadata.

Freeze:

`LOCAL_PUBLICATION_TOOL_UNAVAILABLE != PREFLIGHT_OPTIONAL`.

`REMOTE_MANUAL_RECORD_WRITE != CANONICAL_PUBLISH_UNLESS_EQUIVALENT_PREFLIGHT_PASSES`.

`REFERENCE_INTEGRITY_IS_BACKSTOP_NOT_PUBLICATION_AUTHORIZATION`.

Before any direct GitHub/manual creation of a V2 publication record, the publisher must reproduce the canonical transaction boundary over the exact current source snapshot:

1. refresh the target `main`/branch immediately before the mutation; an earlier read snapshot is not write authority;
2. verify the taskbook uses canonical `ENTERPRISE_MATH_TASK_V1` frontmatter and its `task_id` matches the intended immutable record;
3. verify all five canonical body sections above are present, nonempty, and contain no unresolved placeholders;
4. verify nonempty `parent_objective_id`, `research_value`, `frontier`, `next_action`, origin/lineage fields, and current machine-policy review binding required by the canonical publication tool;
5. compute and pin the exact current taskbook Git blob; never publish against an assumed or stale taskbook body;
6. resolve the exact current publication generation immediately before a revision. If a revision is intended, `supersedes_publication_id` must name the exact prior generation. An unresolved publication fork is fail-closed and cannot be bypassed by manually choosing a head;
7. construct only the same immutable record shape and authority flags that the canonical V2 tool would permit. If equivalent preflight/build semantics cannot be reproduced, stop at a non-executable draft/handoff; do not create task authority;
8. use CAS/non-force write semantics where supported and refresh the target blob/head again if concurrent state changed;
9. after creation, verify the record/taskbook binding and allow the ordinary strict publication/reference gates to check the result. Passing a later CI gate cannot retroactively authorize a write whose preflight was skipped.

Direct GitHub publication is therefore a **transport fallback**, not a semantic or validation fallback.

## 6. Orphan prevention

An orphan task is any post-cutover task-like object that can be mistaken for executable work but lacks exact immutable V2 publication authority.

Examples include:

- an unpublished READY taskbook;
- a handoff naming a new task without a V2 publication record;
- a new scheduler target created outside immutable publication;
- a modified legacy taskbook offered for fresh dispatch without migration.

Freeze:

`UNREGISTERED_TASK -> NO_READY / NO_CLAIM / NO_EXECUTION`.

`UNREGISTERED_HANDOFF -> PUBLISH_V2_BEFORE_HANDOFF`.

## 7. Legacy boundary

`research_scheduler.json` is a frozen legacy definition baseline for already-existing compatible executions only.

`research_task_registry.json` and `tools/research_task_registry.py` are V1 compatibility/audit surfaces only.

Freeze:

`LEGACY_SCHEDULER_RUNTIME_EVENTS_MAY_CONTINUE`.

`LEGACY_SCHEDULER_DEFINITION_FILE_MAY_NOT_PUBLISH_NEW_TASKS`.

`NEW_OR_MODIFIED_TASK -> IMMUTABLE_V2_PUBLICATION`.

`LEGACY_TASK + FRESH_REDISPATCH / MODIFICATION / CURRENT-POLICY REVIEW -> V2_MIGRATION_REQUIRED`.

## 8. Runtime and dispatch relationship

Canonical order:

`PARENT_OBJECTIVE -> TASK_REGISTRATION -> TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`.

For ordinary/lane fresh selection, `tools/research_dispatch.py` and `tools/research_lane_dispatch.py` are selectors. They are not the top-level control entrypoint.

Canonical live routing is:

`research_control_dispatch.py`.

It applies stale-session recovery before concluding that fresh dispatch is empty.

Task publication is a semantic SUBFLOW checkpoint. After publication succeeds, return to the current parent objective without routine CI/review polling or a user wake-up message.
