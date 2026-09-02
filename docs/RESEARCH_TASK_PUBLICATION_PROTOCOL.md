# CANONICAL TASK PUBLICATION / V2

Status: `ACTIVE / CURRENT ONLY`

An official task exists only after one immutable publication record is written under `research_task_records/<task-id>/<publication-id>.json` and pins the exact taskbook blob.

Canonical surfaces:

- `research_task_publication_contract_v2.json`;
- `templates/RESEARCH_TASK_PUBLICATION_TEMPLATE.json`;
- `tools/research_task_records.py`;
- `research_control_dispatch.py`.

Typical flow:

```text
python tools/research_task_records.py prepare ...
python tools/research_taskbook.py audit research_tasks/<TASK>.md
python tools/research_task_records.py publish ...
python tools/research_task_records.py audit
```

Publication requires publisher identity, `parent_objective_id`, `research_value`, lineage/origin review, exact taskbook blob, and a conflict-safe immutable record write. It creates no execution claim and grants no mathematical truth, Working Truth, Foundation status, canonical promotion, or Driver authority.

## Mandatory taskbook body

Every new or revised publication must contain these exact nonempty sections before the immutable record is written:

1. `Mother question`;
2. `Frozen inputs and scope`;
3. `Hard target and required outputs`;
4. `Research value to preserve`;
5. `Success, kill, and return criteria`.

Exact byte-pinned compatibility adapters may preserve a finite pre-canonical publication whose semantics already exist under older headings or the immutable record's `research_value` field. Such an adapter is not a publication path and cannot authorize a new malformed taskbook, change an immutable task record, grant authority, or waive any non-section integrity error.

## Remote/manual GitHub transport fallback

When the local publication CLI cannot be executed, a direct GitHub contents/commit transaction is permitted only as an alternative transport for the same canonical preflight. It must validate the exact taskbook envelope and all five mandatory body sections, compute and pin the exact Git blob, bind the exact predecessor when revising a task, reject unresolved publication forks, preserve publisher/lineage fields, and use conflict-safe CAS/non-force semantics.

Direct GitHub publication is therefore a **transport fallback**, not a semantic or validation fallback.

Freeze:

`LOCAL_PUBLICATION_TOOL_UNAVAILABLE != PREFLIGHT_OPTIONAL`.

`REMOTE_MANUAL_RECORD_WRITE != CANONICAL_PUBLISH_UNLESS_EQUIVALENT_PREFLIGHT_PASSES`.

`REFERENCE_INTEGRITY_IS_BACKSTOP_NOT_PUBLICATION_AUTHORIZATION`.

If canonical-equivalent preflight cannot be completed, the output may be retained only as a non-executable draft or handoff; it is not a published task and may not enter READY, CLAIM, or execution.

After publication, fresh execution uses one authenticated Issue #240 CLAIM envelope and routes through `research_control_dispatch.py`. CI is a backstop, not publication authorization, and does not keep a chat turn alive.

The completed pre-V2 task migration is recorded in `control_plane/legacy_control_migration_manifest.json`; old publication surfaces are not present on `main`.
