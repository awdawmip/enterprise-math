# Native Filament Coupled Selection External Novelty — V2 Preservation Audit Return

Task-ID: `RS-NATIVE-FILAMENT-COUPLED-SELECTION-EXTERNAL-NOVELTY-INDEPENDENT-REEXECUTION`

Publication-ID: `TP2-9568CDEA1071463F9532`

Researcher-ID: `EM-NFNOV2-5E9A31`

Claim-ID: `chatgpt-nfnov2-v2pres-20260902-1038-5e9a31`

Execution branch: `research/native-filament-v2-preservation-audit-em-nfnov2-5e9a31`

Execution base: `ac709e6d472c39b1b623905d85eb753d965a6567`

## Terminal verdict

`NEGATIVE_BOUNDARY`

Hard-target disposition:

`MATHEMATICAL_FRONTIER_AND_DURABLE_HANDOFF_STATE_PRESERVED__EXACT_TASK_IDENTITY_LINEAGE_PROVENANCE_PRESERVATION_REFUTED`

This is a control-surface preservation result only. It adds no mathematical theorem, no prior-art classification, no novelty claim, no historical-priority claim, no Working Truth, no Foundation status, and no canonical promotion.

## Scope actually audited

The preservation taskbook asks whether this exact legacy task can be represented on the immutable V2 surface without changing its mathematical meaning or durable frontier, while preserving exact identity, lineage, accumulated evidence, owner boundary, and next executable action without replaying completed work.

Accordingly this execution did **not** repeat the clean external literature search and did **not** inspect PR #627, the withheld source proofs/checkers, or the direct nonblind audit as novelty evidence. It compared only the durable task/control surfaces needed to test preservation.

Frozen surfaces used:

- original taskbook: `research_tasks/NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_INDEPENDENT_REEXECUTION_20260825.md`
- V2 preservation taskbook: `research_tasks/LEGACY_CONTROL_MIGRATION_RS_NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_INDEPENDENT_REEXECUTION_20260902.md`
- immutable publication: `research_task_records/RS-NATIVE-FILAMENT-COUPLED-SELECTION-EXTERNAL-NOVELTY-INDEPENDENT-REEXECUTION/TP2-9568CDEA1071463F9532.json`
- migration manifest: `control_plane/legacy_control_migration_manifest.json`
- archived legacy scheduler definition at `archive/legacy-control-plane-pre-v2-20260902:research_scheduler.json`
- current contracts: `research_taskbook_contract.json` and `control_plane/current_control_authority.json`

## What is preserved exactly or at the required durable strength

The following task-local mathematical/control invariants agree across the original task and the V2 publication/envelope:

| Field | Original | V2 | Audit |
|---|---|---|---|
| `task_id` | same exact identifier | same | PASS |
| `kind` | `RESEARCH` | `RESEARCH` | PASS |
| `owner` | `audit/native-filament-coupled-selection-independent-novelty-reexecution-20260825` | same | PASS |
| `priority` / effective priority | `P0` | `P0` | PASS |
| `leverage` / effective leverage | `HIGH` | `HIGH` | PASS |
| `frontier` | `NATIVE_FILAMENT_COUPLED_SELECTION_EXTERNAL_NOVELTY_INDEPENDENTLY_CLASSIFIED_WITH_PROVENANCE_CLEAN` | same | PASS |
| mathematical/non-novelty boundary | clean independent external novelty classification; absence of match is not novelty | retained in V2 next-action/body | PASS |
| taskbook binding | n/a | publication pins `sha1:c4090e3b8e49eb1a3a28585f559c6cc04ffb414d` | PASS |
| manifest identity | n/a | unique `ACTIVE_FRONTIER`, `ACTIVE`, `claimable=true`, legacy runtime `HANDOFF_READY` | PASS |

The publication's `taskbook_blob_sha1` equals the actual Git blob SHA-1 of the preservation taskbook, so the immutable record is correctly bound to the exact envelope bytes.

## Durable-state transition is legitimate, not a defect

The old static task definition says `base_state=READY` and asks the clean researcher to perform the external literature classification. That is the pre-execution definition.

The migrated publication records the later effective runtime state:

- `legacy_runtime_state = HANDOFF_READY`;
- `legacy_last_progress_ref` points to the frozen provenance-clean return on the completed research branch;
- V2 `next_action` is Driver review of that frozen return and explicitly forbids reinterpreting `NO_DIRECT_MATCH_FOUND` as historical priority.

Therefore `READY -> HANDOFF_READY` and the corresponding next-action change are a correct durable execution-state migration. Replaying the literature audit now would be the error.

## Exact-preservation counterexample

The preservation envelope itself states that exact task identity and lineage are to be preserved. That stronger claim is false on the frozen bytes.

### 1. Identity-lane drift

Original:

`identity_lane = NFNOV2`

V2 preservation envelope:

`identity_lane = NATIVE`

This does not change the theorem frontier, but it is not exact identity metadata preservation.

### 2. Origin drift

Original:

`origin_kind = DIRECT_USER_DIRECTION`

V2:

`origin_kind = MAINTENANCE`

The V2 wrapper provenance may be maintenance, but the same `task_id` now exposes wrapper origin in place of the task's original origin. No explicit dual-field distinction is provided.

### 3. Lineage drift

Original:

`task_lineage = CONTINUATION`

V2:

`task_lineage = MAINTENANCE`

This is semantically material under `research_taskbook_contract.json`: the active V7 contract has an explicit semantic anti-evasion rule for continuations and requires `parent_task_id` plus a complete `successor_gate`.

### 4. Parent loss

Original:

`parent_task_id = RS-NATIVE-FILAMENT-COUPLED-SELECTION-EXTERNAL-NOVELTY-AUDIT`

V2:

`parent_task_id = null`

Thus the original task ancestry is no longer represented in the canonical task-lineage field.

### 5. Successor-gate loss

The original taskbook contains the complete six-part continuation `successor_gate`, including the information gap, why the parent result did not close it, discriminating outcomes, provenance-contamination kill condition, alternative-route analysis, and why a separate clean re-execution was required.

The preservation envelope omits `successor_gate` entirely because it relabels the same task as `MAINTENANCE`.

This is the strongest preservation defect: a control-plane consumer reading only current V2 task semantics can no longer recover the continuation gate through the canonical fields.

### 6. Exact reference-set drift

The original `source_refs` include the pinned blind-audit Driver review

`driver_reviews/NATIVE_FILAMENT_COUPLED_SELECTION_INDEPENDENT_AUDIT_DRIVER_REVIEW_20260825.md@d4e3f8eca68bff1d8803b8eb74402fc6d69e7b5f`.

The preservation envelope instead adds the original taskbook as a source reference and does not retain that exact pinned review in `source_refs`. A related dependency is summarized textually, but the exact reference set is not preserved.

## Classification

The evidence supports the following exact split:

- **mathematical frontier preservation:** PROVED at the audited task fields;
- **owner / P0-HIGH priority preservation:** PROVED;
- **durable execution-state preservation:** PROVED;
- **exact task identity / lineage / provenance preservation:** REFUTED by explicit field witnesses;
- **novelty or historical priority:** NOT REOPENED;
- **old literature execution:** NOT REPLAYED.

Therefore the preservation task cannot truthfully return unconditional `PASS`.

## Recommended Driver action

Driver review should accept only the negative boundary above.

There are two clean repair choices, both requiring a new immutable V2 generation rather than editing the existing publication in place:

1. **Restore exact source lineage/provenance fields** in a superseding publication while separately recording cutover-wrapper provenance (for example in `migration_source`), retaining the correct durable `HANDOFF_READY` state and Driver-review next action; or
2. **Explicitly narrow the preservation contract** so it promises preservation only of mathematical frontier, owner boundary, accumulated durable state, and executable next action, while stating that publication-wrapper `origin_kind/task_lineage/identity_lane` intentionally replace source-task provenance and that the original lineage is recoverable only through pinned source references.

Until one of those is made explicit, the phrase “exact identity, lineage, ... preserved” is stronger than the current canonical bytes justify.

Do not respond by rerunning the literature audit. Do not use this result to weaken the already-frozen provenance-clean novelty classification or to make any historical-priority statement.
