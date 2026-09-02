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

After publication, fresh execution uses one authenticated Issue #240 CLAIM envelope and routes through `research_control_dispatch.py`. CI is a backstop, not publication authorization, and does not keep a chat turn alive.

The completed pre-V2 task migration is recorded in `control_plane/legacy_control_migration_manifest.json`; old publication surfaces are not present on `main`.
