# Enterprise Math Current Research Branch Ledger

Status: `CANONICAL MIGRATION LEDGER / AUDITED STATE`  
Snapshot: `main@7ca013f461716e0f9d3050e26970d598ef20ff8b`  
Date: 2026-08-09

This ledger records the current **ownership topology and audited migration state**. Exact live branch heads may move after this snapshot; use the read-only branch governance auditor for current ancestry/scope data. `ahead/behind` alone is never a mathematical absorption proof.

The governing documents are:

- `RESEARCH_ARCHITECTURE`: A0–A5 mathematical ownership;
- `RESEARCH_BRANCH_LIFECYCLE`: L0–L5 branch lifecycle;
- `RESEARCH_SCHEDULING_PROTOCOL`: parallel research / serialized promotion;
- `RESEARCH_COMMON_SURFACE`: shared research knowledge;
- `RESEARCH_OWNER_ISOLATION`: owners research, L4 integrations transport;
- `branch_governance_overrides.json` + `tools/audit_branch_lifecycle.py`: ancestry and scope-drift audit.

## 1. Canonical reusable homes already on `main`

### A2 — observation / future-compatible quotient

Canonical main now includes:

- P023 fiber/descent, minimal repair, operation-family refinement, word semantics, and coarsest compatible quotient;
- the finite-arity extension in `EnterpriseMath/Quotient/OperationCongruence.lean`.

`core/a2-future-quotient-v2` remains a research owner/source, not a rolling mirror of main. P024/material/contact specializations are not A2-owned files merely because they consume A2.

### A3 — structured relation state

Canonical main includes the first clean A3 core:

- `weighted_relation_field.py`;
- `relation_lattice.py`;
- `relation_scale.py`;
- their regression suites and replay provenance.

This core owns the capacity-weighted signed relation state, partition coarsening, primitive capacity shift, relation quantum, and relation-scale carry. `core/a3-relation-state-v2` remains the owner/source for further A3 research.

### A4 — admissible support / correspondence

Canonical main includes the first clean A4 core:

- `admissible_support.py`;
- `relational_spectrum.py`;
- self-contained finite-relation regression suites and replay provenance.

A4 owns finite correspondence composition/common-target structure, the split-completeness boundary, witness spectrum `W_k`, source-group spectrum `G_k`, and exact total-function degeneration to P011. `core/a4-admissible-support-v2` remains the owner/source for further A4 research.

## 2. Current long-lived research owners

| Home | Current owner | Current role |
|---|---|---|
| A2 | `core/a2-future-quotient-v2` | Generic quotient/factorization/compatibility extensions beyond canonical P023 |
| A3 | `core/a3-relation-state-v2` | Structured relation-state, partition kernel/selector extensions |
| A4 | `core/a4-admissible-support-v2` | Correspondence/support, witness and relation-algebra extensions |
| P017 | `program/p017-legendre` | Consecutive-square/Legendre pressure test; active discovery frontier |
| P018 | `program/p018-precision-v2` | Precision-specific pair/kernel/defect/transport and proof applications |
| P021 | `program/p021-causal-focusing-v2` | Causal/focusing application owner; first causal-boundary slice validated at owner level |
| P022 | `program/p022-geometry-v2` | Intrinsic geometry owner; A_p lattice core plus active HCP/Barlow routes |
| P024 | `program/p024-action-precision` | Closed-form action-language / threshold / boundary-pullback specialization program |

Owners may legitimately be behind `main`. They MUST NOT whole-tree synchronize moving main merely to stay current.

## 3. Active bridge topology

### A3 ↔ A4

Current thin generation:

`bridge/a3-a4-generated-support-v3`

First slice is intentionally limited to three assets:

- generated A4 support from canonical A3 `Z_ij`;
- regression tests;
- replay manifest.

It consumes canonical A4 relation/common-target operations rather than duplicating them. Historical B07+ metric/frontier/count/equitability work remains unpromoted until owner classification is complete.

Historical umbrella PR #83 is provenance/replay source only.

### P017 ↔ P018

P017/P018 bridge work may continue where hypotheses genuinely require both square-basin arithmetic and P018 quotient/root structure. Such results remain L3 and must not become a second P017 or P018 owner.

## 4. Validated owner slices not yet canonical

### P021 first slice

`program/p021-causal-focusing-v2` has an owner-level green checkpoint for:

- replay manifest;
- `causal_boundary.py`;
- `test_causal_boundary.py`.

The PR is Draft by design after validation. Canonical promotion requires a future fresh L4 replay from then-current main.

### P022 current owner

P022 is actively advancing within one theorem home. The owner currently combines:

- replayed A_p/root-lattice geometry;
- HCP/geodesic multiplicity and Barlow-stacking research.

This is legal same-owner growth, not cross-home scope drift. Canonical promotion should freeze and replay selected validated slices separately rather than merge the whole moving owner.

## 5. Confirmed provenance / superseded integration history

The following classes must not return to the active owner surface:

- historical P018 #68 long tree: replay/provenance source only;
- historical A3/A4 #83 bridge tree: replay/provenance source only;
- historical P021 #48 and P022 #50 umbrellas: provenance until unique assets are fully classified;
- obsolete whole-main synchronization PRs such as #56, #85 and #123: closed by Owner-Isolation;
- superseded Architecture v1 #81: replaced by canonical Architecture v2;
- polluted/stale integration vehicles: kept as provenance, not merge vehicles;
- old A2/A3/A4 validation/release PRs once their exact payload was absorbed canonically.

Deleting a branch ref is optional cleanup; mathematical provenance is carried by commits, closed PRs, lineage and manifests.

## 6. Semantic absorption rule

`ahead(main)=0` is a sufficient mechanical absorption signal, but not necessary.

A branch with different commit ancestry may still be `ABSORBED` when theorem/doc/code/test assets are already on main as exact blobs or an explicitly audited equivalent/generalized canonical result. E002 task-observable history is the canonical example.

Conversely, a path or filename collision is not absorption. Historical P017/P018 branches reused Supplement numbers and filenames for different mathematics; theorem/content audit controls.

## 7. Scope-drift rule

Owner purity and ancestry are separate dimensions.

A branch is `SCOPE_DRIFT` when its branch-side changes contain unrelated theorem homes because another owner or whole main was synchronized into it. Live migration reproduced this defect on A2, A3, A4 and a lifecycle-tooling L4 branch.

Recovery preserves history and restores the current tree to the declared owner/integration asset set. It does not force-rewrite history.

The canonical auditor now measures branch-side changes from merge-base to owner head and compares them with declared allowed paths/prefixes.

## 8. Promotion pipeline

For L1/L2/L3 work:

`owner research -> freeze exact payload -> fresh L4 from latest main -> replay owner-only assets -> final combination gates -> main`.

Only L4 must chase current main. Owner branches do not.

A multi-owner L4 release is exceptional and allowed only when every included payload was independently validated first and the combined release is explicit/auditable.

## 9. Next compaction batches

1. finish the three-asset A3↔A4 bridge validation, then promote it through a fresh L4 if selected;
2. promote the validated P021 causal-boundary slice when its program boundary/prior-art note is ready;
3. split P022 canonical promotion into bounded slices instead of waiting for the entire active geometry owner to stop moving;
4. audit old P017/P018 PRs by theorem/blob equivalence and close only genuinely absorbed histories;
5. route generic P024 adjoint/stabilization formalizations upward to A0/A1 while P024 keeps only action-language specializations;
6. continue retiring pure synchronization PRs and stale integration vehicles;
7. keep E001 engineering/material owners separate from reusable A2/A3/A4 mathematics.

## 10. Target active surface

Long-lived writable refs should remain approximately:

- A2 / A3 / A4 core owners;
- P017 / P018 / P021 / P022 / P024 program owners;
- bounded E001 engineering/material owners;
- 0–2 genuinely thin bridges.

`integration/*` and short `agent/*` branches are transport/execution refs and should exit after their task. Historical discovery remains recoverable without remaining an active branch.
