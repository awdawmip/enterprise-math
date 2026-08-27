# Driver Review — P022 Parallel Publication Authority Resolution

Status: `DRIVER_CONTROL_PLANE_FINAL / PUBLICATION_FORK_RESOLVED / KEEP_PARALLEL_AND_SELECT_OPERATIONAL`

Date: `2026-08-27`

Driver-ID: `EM-NTIRF-6C5A1E / DRIVER`

Task: `RS-P022-OBSERVATION-HISTORY`

Live-main audit base before resolution: `cc0106285c579998747c3e777c11c35a3304a274`

Resolution commit: `82c0b71cf91644e6c18a3d2311bd3d374cf4475d`

## 1. Control-plane finding

The live task registry contained three simultaneously active generation-1 publication heads for the same task id:

- `TP2-DE338F269CA11E9BC01B` — arithmetic-core replay;
- `TP2-D78DBA0243911E0363FA` — forced-midpoint fallback replay;
- `TP2-2346F5D3E731ED56DB0A` — composite Franel escape replay.

Under `tools/research_task_records.py`, `current_records()` rejects more than one unresolved head for a task id. Therefore this was a real publication-authority fork, not merely a display-layer duplication.

The generation-aware result shim in `tools/research_result_records.py` first resolves the operational publication and then reduces result state for that publication. Consequently an explicit operational binding is also necessary to prevent the already-terminal arithmetic-core result from obscuring the intended next P022 replay frontier.

## 2. Evidence relation

Reference pass 1: all three publications survive as immutable research evidence. They are not duplicate byte-identical publications and none is rejected on mathematical-content grounds.

Reference pass 2: their routing roles are different.

- `TP2-DE338F269CA11E9BC01B` already produced `RR-8323CFDCB99F7832F51F`, accepted at exact-reduction scope. It is terminal evidence for that publication lineage, not the next live P022 frontier.
- `TP2-D78DBA0243911E0363FA` is an earlier and narrower forced-midpoint fallback replay.
- `TP2-2346F5D3E731ED56DB0A` is the later composite Franel escape replay. The accepted P022 arithmetic-core Driver review explicitly identifies it as the existing active continuation and routes the fixed residual kernel into that line.

## 3. Resolution

`research_task_publication_resolutions.json` now binds:

`RS-P022-OBSERVATION-HISTORY -> TP2-2346F5D3E731ED56DB0A`

as the unique operational publication.

The compatibility reducer field `quarantined_publication_ids` contains:

- `TP2-DE338F269CA11E9BC01B`;
- `TP2-D78DBA0243911E0363FA`.

Per the registry compatibility note, this is not a mathematical quarantine or rejection. Both are retained parallel publications and remain immutable, referenceable evidence.

## 4. Mathematical scope preserved

No mathematical verdict is changed by this control-plane repair.

`RR-8323CFDCB99F7832F51F` remains accepted only as:

`EXACT_BOUNDARY_REDUCTION / FIXED_TERMINATING_KERNEL`.

It does not prove all-parameter nonvanishing, complete P022 observability, or Foundation truth.

The P022 parent objective remains open.

## 5. Driver disposition

`PUBLICATION_AUTHORITY = ONE_VALUED`.

`OPERATIONAL_PUBLICATION = TP2-2346F5D3E731ED56DB0A`.

`TERMINAL_ARITHMETIC_CORE_RESULT = PRESERVED`.

`P022_PARENT_OBJECTIVE = OPEN`.

`NEXT_CONTROL_PLANE_ACTION = CONTINUE_REVIEW_QUEUE_OR_ALLOW_VALID_CLAIM_ON_OPERATIONAL_PUBLICATION`.
