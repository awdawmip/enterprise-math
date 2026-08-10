# Enterprise Math Branch Compression Audit — 2026-08-11

Status: `FIRST_REVIEW_COMPLETE / RETIREMENT_NOT_AUTHORIZED`

Purpose: first-pass semantic/lifecycle audit of the full GitHub branch surface before branch retirement. This audit may authorize bounded L4 harvest/promotion, but **does not authorize changing a source branch to `ABSORBED/PROVENANCE`, closing its historical PR, or deleting its ref**. Those actions require a fresh independent second review.

## 1. Frozen audit scope

- Repository: `awdawmip/enterprise-math`
- Full branch census: **492 refs total, including `main`**; **491 non-main refs**.
- First-pass deep-comparison base: `4859bc5a15c58b7487ec65430c977d3a7d5debbe`.
- Census source: five paginated GitHub branch-list pages covering the complete branch ref surface available during the audit.
- Machine owner registry at audit start: 14 `ACTIVE_OWNER/ACTIVE_BRIDGE`, 4 `REPLAY_REQUIRED`, 9 `PROVENANCE`, 9 `ABSORBED`.

The frozen base is intentional. `main` moved during the audit; unrelated movement was not chased. Actual L4 promotions use their own one-time current-main admission and final merge-time checks.

## 2. Retirement safety rule

First review may assign the internal audit markers below. They are **not new formal lifecycle states**:

- `RETIRE_REVIEW_PENDING` — strong retirement candidate; lifecycle unchanged until second review.
- `PROMOTION_READY_SURFACE_SYNC_REQUIRED` — bounded mature payload, but shared-surface registration or another final promotion gate remains.
- `HARVEST_REQUIRED` — branch may contain unique mathematics; select/rehome payload before retirement can be considered.
- `KEEP_ACTIVE` — current generation has a bounded unabsorbed frontier.
- `SECOND_REVIEW_CLEANUP_CANDIDATE` — operational/provenance ref that may be removable after independent proof of recoverable provenance and no unique payload.

A second reviewer must independently inspect current `main`, the frozen/source head, source PR/provenance, semantic uniqueness, and destination coverage. Only explicit second-review approval may authorize lifecycle change or ref deletion.

## 3. Registered active/replay branches — first review

| Branch | First-review disposition | Evidence / rationale |
|---|---|---|
| `core/a3-relation-lattice-v3` | `PROMOTION_READY_SURFACE_SYNC_REQUIRED` | Clean four-file A3 generation (`relation_tree_lattice`, `relation_zero_total_orbit` + tests), source head `a9c5d25e...`; requires common-surface sync before canonical merge. |
| `bridge/a3-a4-generated-support-v3` | `RETIRE_REVIEW_PENDING` | Mechanical branch delta is essentially the already-canonical first A3→A4 bridge slice plus manifest; any future bridge work should start only from a new bounded cross-owner question. |
| `bridge/p017-p018-hard-core-v2` | `HARVEST_REQUIRED` | Very large generation (~277 ahead commits in frozen compare); no wholesale merge. Distill only genuinely cross-owner arithmetic/precision payload. |
| `bridge/a2-e001-material-markov` | `RETIRE_REVIEW_PENDING` | Scheduler is `BACKLOG` / `ACTIVE_BRIDGE_NO_SELECTED_FRONTIER`; generic future-quotient work is A2/P023-owned, material-only work is E001-owned. |
| `program/p017-legendre` | `KEEP_ACTIVE` | Bounded P017-specific unabsorbed modules/docs/tests remain. |
| `program/p018-precision-v2` | `KEEP_ACTIVE` | Bounded P018 precision-specific WIP remains. |
| `program/p021-causal-focusing-v3` | `RETIRE_REVIEW_PENDING` | Current branch delta is only the v3 owner manifest; scheduler frontier can open a fresh generation when new P021-local mathematics starts. |
| `program/p022-geometry-v2` | `HARVEST_REQUIRED` | Huge multi-slice generation (~469 ahead commits in frozen compare); many slices are already canonical. Freeze and distill, never wholesale merge. |
| `program/p024-action-precision` | `RETIRE_REVIEW_PENDING` | Current branch delta is only replay manifest; canonical P024 assets already live on `main`; future higher-dimensional action work can use a fresh generation. |
| `program/p025-abc-support-collapse` | `HARVEST_REQUIRED` | Large generation (~109 ahead commits); requires semantic slicing by P025-local vs A2/A4-owned mathematics. |
| `research/r004-causal-identifiability-v1` | `KEEP_ACTIVE` | FQ-007 research package remains a bounded active Foundation-facing frontier. |
| `engineering/e001-material-impulse-v2` | `HARVEST_REQUIRED` | Broad generation (~51 ahead commits) spanning several impulse/force/work/capacity slices; freeze and distill. |
| `engineering/e001-material-contact-network` | `PROMOTION_READY_SURFACE_SYNC_REQUIRED` | Clean six-file owner generation (incidence/Gram, cycle kernel, rank duality + tests); shared-surface registration required before merge. |
| `engineering/e001-measurement-area-refinement` | `RETIRE_REVIEW_PENDING` | Exact four-file measured-polyline refinement slice is already canonical via PR #264; scheduler is `BACKLOG` / frozen previous generation. |
| `research/core/relation-quotient` | `HARVEST_REQUIRED` | Very large historical mixed A3 tree (~712 ahead / ~716 behind in frozen compare); selected replay only. |
| `research/core/relation-support-bridge` | `HARVEST_REQUIRED` | Historical mixed A3/A4/P019 tree (~209 ahead); B01–B06 already moved to thin v3 bridge, remaining results require owner-by-owner harvest. |
| `bridge/a3-a4-v2` | `RETIRE_REVIEW_PENDING` | Historical broad bridge now mechanically close to replay-manifest-only state; thin v3 replaced its live role. |
| `engineering/e001-material-state-cost` | `RETIRE_REVIEW_PENDING` | Generic `material_future_precision` module/test already canonical. The two remaining unique application assets were harvested through PR #451 and merged at `main@9730c385115440f49b03f3de9d1cf2509682737b`. |

## 4. Completed first-pass semantic harvest

### E001 state-cost historical tree

Frozen source: `engineering/e001-material-state-cost@99537ae04c1f1c84dfb8beb4219d9faa4e24aa4d`.

Already canonical/upstream-owned and therefore **not replayed**:

- `src/enterprise_math/material_future_precision.py`
- `tests/test_material_future_precision.py`

Unique application-only assets replayed through L4 PR #451:

- `experiments/e001_treloar_state_precision_benchmark.py`
- `tests/test_e001_material_state_pareto.py`

PR #451 merged at `9730c385115440f49b03f3de9d1cf2509682737b` with `NO NEW MATHEMATICS`. Common-surface delta was explicitly `N/A` because the promotion introduced no new stable shared API/theorem/tool family.

The source branch remains unchanged pending second review.

## 5. Existing registered provenance/absorbed generations

All registry entries already marked `PROVENANCE` or `ABSORBED` are `SECOND_REVIEW_CLEANUP_CANDIDATE` for branch-ref cleanup, **not automatically deleted**. Second review must verify that provenance remains recoverable from PR/tag/lineage/main and that no branch contains a unique semantic asset.

Registered `PROVENANCE` set at audit start:

- `agent/p018-critical-grid`
- `research/core/admissible-support-relations`
- `core/a2-future-quotient-v2`
- `core/a3-relation-state-v2`
- `core/a4-admissible-support-v2`
- `program/p021-causal-focusing-v2`
- `engineering/e001-material-impulse-world`
- `engineering/e001-material-pair-impulse`
- `engineering/e001-material-multiaction-protocol`

Registered `ABSORBED` set at audit start:

- `research/e002-horizon-saturation-v2`
- `research/e002-precision-locked-actuation-v2`
- `research/e002-precision-native-hysteresis-v2`
- `research/e002-predictive-quotient-compiler-v2`
- `research/e002-vector-actuation-v2`
- `research/e002-task-observable-v2`
- `research/p023-composition-safe-collapse`
- `research/p023-safe-selector-semigroup`
- `research/p018-all-power-quotient-basin-final`

## 6. Unregistered branch refs — full-census routing

The branch census contains hundreds of historical refs not represented as current owner entries. First review covered these by namespace/lifecycle class rather than performing hundreds of redundant semantic re-proofs.

### Operational short-lived namespaces

Refs under short-lived operational namespaces such as `agent/`, `integration/`, `validation/`, `checkpoint/`, `maintenance/`, `chore/`, and `ci/` are `SECOND_REVIEW_CLEANUP_CANDIDATE` **only when** the second review confirms their PR/task is complete, payload is canonical or superseded, and provenance is recoverable. Their namespace alone is never sufficient for deletion.

The merged `integration/e001-state-cost-harvest-20260811` ref is included in this cleanup queue; it is not deleted by first review.

### Unregistered mathematical namespaces

Unregistered refs under `core/`, `program/`, `research/`, `bridge/`, or `engineering/` are **not** presumed stale. They require `HARVEST_REQUIRED` or supersession proof before cleanup. In particular, a branch missing from the current owner registry is not evidence that its mathematics is absent or absorbed.

This rule is how the 492-ref census avoids both failure modes: preserving every stale executor ref forever, and deleting undiscovered mathematics merely because control-plane metadata moved on.

## 7. Second-review contract

The next scheduler claimant must perform an independent retirement review. For every proposed branch retirement, record:

1. source branch + exact head SHA;
2. current-main SHA used by the second review;
3. source PR/tag/lineage provenance;
4. branch-owned semantic assets;
5. relation to main: `SAME`, `STRICT_GENERALIZATION_ON_MAIN`, `SPECIALIZATION`, `UNIQUE`, or `CONFLICT`;
6. whether any selected replay is still required;
7. whether the theorem/program owner still has a live frontier and, if so, whether it should continue on a fresh generation;
8. final verdict: `APPROVE_RETIRE`, `REJECT_RETIRE`, `HARVEST_REQUIRED`, or `KEEP_ACTIVE`.

Only `APPROVE_RETIRE` authorizes a later bounded mutation of `branch_governance_overrides.json`, corresponding scheduler task state, stale PR closure, and branch-ref deletion. The second review must not infer approval from this first-pass document.

## 8. Priority order for second review

Review in this order:

1. completed L4 / validation / agent refs whose task is already canonical;
2. registered `ABSORBED` / `PROVENANCE` refs;
3. named strong candidates from Section 3;
4. `PROMOTION_READY_SURFACE_SYNC_REQUIRED` source generations after their payload is canonical;
5. large `HARVEST_REQUIRED` trees only after selected payloads are classified/replayed.

Do not chase moving `main`, poll CI, or wholesale merge any historical tree merely to complete retirement review.

## 9. First-review conclusion

The GitHub branch problem is primarily **ref lifecycle debt**, not a need to merge mathematical owners together. The correct compression path is:

`semantic harvest -> L4/main -> independent second review -> lifecycle transition/ref cleanup`.

No source branch was retired or deleted during this first review.
