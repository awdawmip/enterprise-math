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

Publication requires publisher identity, `parent_objective_id`, `research_value`, lineage/origin review, exact taskbook blob, and a conflict-safe immutable record write. The canonical writer also persists the prepared taskbook's `identity_lane`, `source_refs`, `dependencies`, `evidence_status`, `successor_gate`, separate `migration_source`, and `parent_objective_generation_id` when present. Migration provenance must not replace source-backed task identity, lineage, parentage, successor-gate, or source-reference semantics.

Every executable publication body contains nonempty current sections:

- `Mother question`;
- `Frozen inputs and scope`;
- `Hard target and required outputs`;
- `Research value to preserve`;
- `Success, kill, and return criteria`.

Publication creates no execution claim and grants no mathematical truth, Working Truth, Foundation status, canonical promotion, or Driver authority.

## Remote/manual GitHub transport fallback

Direct GitHub publication is therefore a **transport fallback**, not a semantic or validation fallback.

Freeze:

`LOCAL_PUBLICATION_TOOL_UNAVAILABLE != PREFLIGHT_OPTIONAL`.

`REMOTE_MANUAL_RECORD_WRITE != CANONICAL_PUBLISH_UNLESS_EQUIVALENT_PREFLIGHT_PASSES`.

`REFERENCE_INTEGRITY_IS_BACKSTOP_NOT_PUBLICATION_AUTHORIZATION`.

When the local canonical publication command cannot be executed, an authorized remote/manual writer must perform an equivalent preflight before creating the immutable record. It must:

1. parse the exact taskbook frontmatter and body;
2. require the five canonical body sections above with nonempty, non-placeholder payloads;
3. run the current taskbook policy audit and require machine `PASS`;
4. pin the exact taskbook Git blob;
5. preserve source-backed identity, origin, lineage, parent task, complete successor gate and source references, while storing migration-wrapper provenance separately;
6. require the exact `supersedes_publication_id` for every revision;
7. fail closed rather than selecting a publication from an unresolved fork;
8. use compare-and-swap/non-force mutation semantics;
9. create no executable publication when equivalent preflight cannot be performed.

If equivalent preflight is unavailable, the only valid output is a non-executable draft or handoff. A later green CI run may detect a defect, but cannot retroactively authorize an invalid publication.

After publication, fresh execution uses one authenticated Issue #240 CLAIM envelope and routes through `research_control_dispatch.py`. CI is a backstop, not publication authorization, and does not keep a chat turn alive.

The completed pre-V2 task migration is recorded in `control_plane/legacy_control_migration_manifest.json`; old publication surfaces are not present on `main`. Known schema-valid semantic-preservation faults are removed from operational selection by `research_task_semantic_integrity_quarantines.json` until an authorized superseding generation repairs them.
