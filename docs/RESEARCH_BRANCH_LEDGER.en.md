# Enterprise Math Research Branch Snapshot

Status: `CANONICAL ADVISORY SNAPSHOT / NOT LIVE DISPATCH AUTHORITY`  
Snapshot base: `main@fc81a15a0fc7a76d1d2b44e7d9a41b699863ef22`  
Date: 2026-08-09

This document is an audited **ownership/provenance snapshot**. It is deliberately not the live scheduler and must not be refreshed for every branch-head or `main` movement.

Live execution authority is, in order:

1. explicit current user instruction;
2. `branch_governance_overrides.json` for writable owner/bridge state and scope;
3. `research_scheduler.json` for durable task definitions;
4. Research Dispatch Board Issue #240 for claims, leases, progress, handoff and blocks;
5. `docs/RESEARCH_COMMON_SURFACE.*` / `research_common_surface.json` for reusable canonical theorem/tool routing.

`ahead/behind` is a Git signal, never a proof of mathematical ownership or novelty.

## 1. Current long-lived research surface

At this snapshot the machine owner registry has 13 long-lived `ACTIVE_OWNER` / `ACTIVE_BRIDGE` routes.

| Home | Writable route | Class | Scheduler task |
|---|---|---|---|
| A3 | `core/a3-relation-lattice-v3` | L1 owner | `RS-A3-RELATION-LATTICE` |
| A3 ↔ A4 | `bridge/a3-a4-generated-support-v3` | L3 bridge | `RS-A3-A4-GENERATED-SUPPORT` |
| P017 ↔ P018 | `bridge/p017-p018-hard-core-v2` | L3 bridge | `RS-P017-P018-ANALYTIC-MASS` |
| A2 ↔ E001 | `bridge/a2-e001-material-markov` | L3 bridge | `RS-A2-E001-MATERIAL-MARKOV` |
| P017 | `program/p017-legendre` | L2 owner | `RS-P017-GLOBAL-CAPACITY` |
| P018 | `program/p018-precision-v2` | L2 owner | `RS-P018-TERNARY-CARRY` |
| P021 | `program/p021-causal-focusing-v3` | L2 owner | `RS-P021-FOCUSING-DIRECTION` |
| P022 | `program/p022-geometry-v2` | L2 owner | `RS-P022-OBSERVATION-HISTORY` |
| P024 | `program/p024-action-precision` | L2 owner | `RS-P024-HIGHER-ACTION-PRECISION` |
| P025 | `program/p025-abc-support-collapse` | L2 owner | `RS-P025-WITNESS-PRECISION` |
| E001 impulse | `engineering/e001-material-impulse-v2` | L2 owner | `RS-E001-IMPULSE-V2` |
| E001 contact network | `engineering/e001-material-contact-network` | L2 owner | `RS-E001-CONTACT-NETWORK` |
| E001 measurement | `engineering/e001-measurement-area-refinement` | L2 owner | `RS-E001-MEASUREMENT-REFINEMENT` |

The owner-registry and scheduler coverage sets are equal at this snapshot. A scheduler task may be `BACKLOG`, `READY`, `HANDOFF_READY`, leased, blocked or complete at runtime; **do not copy runtime state into this file**. Read Issue #240 instead.

## 2. Canonical compaction already achieved

The following reusable layers/slices are already on `main`; their historical validation/replay branches are not current owners:

- A2/P023 generic descent, future-compatible quotient and finite-arity operation congruence;
- first clean A3 weighted relation-state / relation-lattice / relation-scale core;
- first clean A4 admissible-support / relational-spectrum core;
- thin A3→A4 generated-support/cancellation executable bridge;
- P021 finite causal-boundary executable core;
- P022 `A_p` root-lattice executable core;
- P022 geodesic-multiplicity and HCP executable core (L4 #262, `main@fc81a15a...`);
- P018 centered-prime-radius executable remainder from historical #54 (L4 #270);
- canonical E001 wall/pair impulse and other explicitly promoted application slices.

Canonical executable presence does not by itself upgrade every encoded statement to `PROVED`; theorem/proof status remains controlled by canonical theorem documents, Lean coverage and Relay/provenance.

## 3. Provenance and absorbed generations

Examples of branches/PR generations that have left the writable research surface include:

- historical P018 long tree `agent/p018-critical-grid` / PR #68;
- A2/A3/A4 v2 owner generations after their selected cores were promoted;
- P021 v2 after causal-boundary promotion;
- E001 one-body impulse-world, pair-impulse and multi-action generations after their L4 promotions;
- E002 v2 generations whose payloads are mechanically or semantically absorbed;
- obsolete whole-main synchronization PRs;
- validation/publication shadows such as P005 #22 and P022 geodesic validation #220 once exact payloads were canonical.

Closing a PR or deleting a branch ref does not delete mathematical provenance: discovery commits, closed PR discussion, lineage and replay manifests remain available.

## 4. Historical trees still requiring semantic replay

The current machine registry retains these as `REPLAY_REQUIRED` rather than writable owners:

- `research/core/relation-quotient` — historical mixed A3 source;
- `research/core/relation-support-bridge` — historical broad A3/A4 source after B01–B06 extraction;
- `bridge/a3-a4-v2` — obsolete broad bridge generation;
- `engineering/e001-material-state-cost` — stacked E001 application branch with upstream A2/E001 dependency.

`REPLAY_REQUIRED` means: preserve history, stop growing the mixed historical tree, classify each remaining result by theorem home, and publish selected still-unique payload through fresh L4. It does **not** mean wholesale merge/rebase.

## 5. Semantic absorption rule

A branch is absorbed exactly when no branch-owned semantic asset is still missing from `main`.

Two common proofs:

1. mechanical: `ahead(main)=0`;
2. semantic: different ancestry, but theorem/doc/code/test/lineage assets are exact, equivalent, or strictly generalized on `main`, with no unique specialization/counterexample left.

Path/name equality is not enough. Historical P017/P018 work reused supplement numbers and filenames for different mathematics; content/theorem audit controls.

## 6. Owner isolation and promotion

L1/L2/L3 owners may legitimately lag moving `main`. They must not whole-tree merge/rebase/copy `main` merely for currency.

Canonical publication is:

`owner/bridge research -> freeze exact payload -> one L4 integration -> shared-surface delta or explicit N/A -> applicable gates -> one final current-main combination gate -> main -> provenance`.

L4 carries **NO NEW MATHEMATICS**. If replay discovers a new theorem, return it to the proper owner first.

Unrelated `main` movement during validation does not create a new replay generation. Inspect the actual intervening delta, reconcile genuine overlap in the same integration line, then perform one final combination gate.

## 7. Scheduler and Foundation boundaries

Scheduler state coordinates work; it does not prove theorems or promote canonical truth.

Foundation questions are owned by Foundation Problem Set Issue #164. Research answers require independent steward verification before any Foundation integration. Active tool/interface alerts remain active until explicitly resolved; a scheduler task ID alone is not evidence that the corresponding mathematical/interface question has been answered.

## 8. Maintenance rule for this snapshot

Refresh this ledger only when the **long-lived ownership/provenance topology** changes materially, for example:

- a new long-lived owner/bridge is registered;
- an owner generation becomes provenance;
- a historical mixed tree is fully accounted for;
- the promotion/control-plane contract itself changes.

Do not refresh it merely because:

- `main` advanced;
- an owner head advanced;
- a lease changed hands;
- CI/review state changed;
- a short task/integration branch appeared.

For live dispatch, always read the machine owner registry, scheduler config and Issue #240.