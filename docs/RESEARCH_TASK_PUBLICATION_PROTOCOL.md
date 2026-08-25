# Enterprise Math Unified Task Publication Protocol

Status: `ACTIVE / CANONICAL TASK PUBLICATION / V1`

Canonical machine sources:

- `research_task_publication_contract.json`
- `research_task_registry.json`
- `research_runtime_state_machine.json`
- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`

Executable publication gate:

`tools/research_task_registry.py`

## 1. One publication path

Every official task uses the same publication transaction regardless of who creates it.

Allowed publishers:

- `RESEARCHER` — including ordinary task researchers and free researchers after the free-candidate audit boundary;
- `RESEARCH_DRIVER`;
- `FOUNDATION_STEWARD` for governance tasks.

Freeze:

`TASKBOOK_FILE != PUBLISHED_TASK`.

`HANDOFF_TEXT != PUBLISHED_TASK`.

`SCHEDULER_ENTRY != PUBLISHED_TASK` unless the task is either explicitly registered or covered by the frozen pre-cutover legacy baseline.

`OFFICIAL_NEW_TASK -> CANONICAL_TASK_REGISTRY_RECORD`.

There is no Driver-only publication lane and no free-form alternate task template.

## 2. Researcher publication authority

A researcher may publish a new task without Driver approval after satisfying the same machine publication gate.

Publication does **not** grant:

- Working Truth;
- Foundation status;
- canonical promotion;
- theorem truth;
- global priority authority;
- Driver authority.

Researcher-published tasks become claimable with default runtime rank `P2 / MEDIUM`. The publication record preserves any publisher priority/leverage request, and a Driver may later reprioritize it. An explicit user priority instruction controls over the default.

This lets researchers capture valuable follow-up work immediately without turning task creation into roadmap capture.

## 3. Free-research publication

FREE Phase A remains blind and does not publish task agenda items while discovery is still raw.

After Phase B, an audited free candidate in one of:

- `AUDITED_AXIOM_CANDIDATE`;
- `AUDITED_REPLACEMENT_CANDIDATE`;
- `EXACT_NEGATIVE_OBSTRUCTION`

may be published directly by the researcher as a registered task. Driver intake is no longer required merely to make the task exist.

The publication must preserve:

- `origin_kind=FREE_AXIOM_CANDIDATE`;
- candidate id;
- audited candidate state.

Publication still does not make the candidate Working Truth.

## 4. Valuable residue capture

A task researcher may publish a follow-up task at a semantic checkpoint when work reveals a valuable unresolved residue.

Required publication data includes:

- parent objective;
- exact lineage;
- parent task when the new task is a continuation;
- exact unresolved frontier;
- first executable next action;
- `research_value`: why the work is worth preserving even if it is not immediately selected.

Publishing the residue does not switch the current task and is not a reason to stop the current parent turn.

## 5. Mandatory template

All new task publications use:

`templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`.

The taskbook may contain additional task-local sections, but it must retain the publication fields and the five mandatory content sections:

1. Mother question;
2. Frozen inputs and scope;
3. Hard target and required outputs;
4. Research value to preserve;
5. Success, kill, and return criteria.

Recommended creation:

```text
python tools/research_task_registry.py new \
  --task-id <TASK_ID> \
  --title <TITLE> \
  --publisher-role <RESEARCHER|RESEARCH_DRIVER|FOUNDATION_STEWARD> \
  --parent-objective-id <PARENT_OBJECTIVE> \
  --origin-kind <ORIGIN> \
  --lineage <LINEAGE> \
  --output research_tasks/<FILE>.md
```

After task-local editing:

```text
python tools/research_task_registry.py publish \
  --taskbook research_tasks/<FILE>.md \
  --publisher-role <ROLE> \
  --publisher-id <Researcher-ID|Driver-ID|Steward-ID> \
  --parent-objective-id <PARENT_OBJECTIVE> \
  --research-value "<WHY THIS TASK MUST NOT BE LOST>"
```

Publication is complete only when:

`python tools/research_task_registry.py audit`

passes.

## 6. Orphan prevention

An orphan task is any post-cutover task-like object that can be mistaken for executable work but has no canonical registry record.

Examples include:

- an unregistered READY taskbook;
- an unregistered scheduler target;
- a handoff that names a new task but never registers it;
- a researcher note presented as an official task;
- a newly modified legacy taskbook redispatched without registry migration.

Freeze:

`UNREGISTERED_TASK -> NO_READY / NO_CLAIM / NO_EXECUTION`.

`UNREGISTERED_HANDOFF -> REGISTER_BEFORE_HANDOFF`.

`CURRENT_POLICY_PASS + NO_REGISTRY_RECORD -> CI_FAILURE`.

## 7. Legacy cutover

Pre-cutover tasks already present on canonical `main` are treated as `LEGACY_BASELINE_REGISTERED` for continuation of existing executions only.

They do not need bulk historical rewriting.

However:

`LEGACY_TASK + FRESH_REDISPATCH -> EXPLICIT_REGISTRY_RECORD`.

A new policy review or modification cannot use legacy status to bypass registration.

## 8. Runtime relationship

The unified runtime composes the task registry before owner/session execution.

Canonical order:

`PARENT_OBJECTIVE -> REGISTERED_TASK -> OWNER_CLAIM -> SESSION -> DURABLE_FRONTIER -> NEXT_ACTION -> TERMINAL_SCOPE -> FINAL_ALLOWED`.

Task registration controls whether a task exists as executable work. Owner lease controls who owns it. Session liveness controls whether the current conversation is alive. These are distinct controls.

Task publication is a SUBFLOW boundary. After a publication succeeds, return to the current parent objective rather than waiting for a user wake-up message.
