# Enterprise Math Current Research Branch Ledger

Status: `MIGRATION LEDGER / AUDITED SUBSET`  
Audit baseline: `main@fbd95bc3d119c2429d3e83825b5cd44cd044e501`  
Date: 2026-08-09

This ledger is not intended to remain a permanently hand-maintained truth source. It records the critical refs verified in the current migration through Git compare/PR metadata and provides the initial classification for a later automated ledger.

State definitions are in `RESEARCH_BRANCH_LIFECYCLE`.

## 1. Confirmed `ABSORBED`

The following branches were verified with `ahead(main)=0`, meaning current main already contains all of their commits:

| Branch | Result | Action |
|---|---|---|
| `agent/e001-material-foundation` | ahead=0 | provenance only; no longer an active owner |
| `agent/p017-multiplicative-resource-capacity` | ahead=0 | archive branch ref |
| `research/p018-all-power-quotient-basin-final` | ahead=0 | archive; consume all-power results from main |
| `research/p023-composition-safe-collapse` | ahead=0 | archive; continue P023 only from current main |
| `research/p023-safe-selector-semigroup` | ahead=0 | archive |
| `research/e002-horizon-saturation-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-precision-locked-actuation-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-precision-native-hysteresis-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-predictive-quotient-compiler-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-vector-actuation-v2` | ahead=0 | absorbed E002 generation |

After provenance is recoverable through PR/lineage/tag, stale PRs should be closed and branch refs removed.

## 2. E002 generation tail

`research/e002-task-observable-v2`:

- `ahead=2`
- `behind=64`

State: small `REPLAY_REQUIRED` delta.

Action: create a latest-main `integration/e002-task-observable-current`, replay only the two unabsorbed task-observable commits and their theorem/doc/test/lineage assets, pass gates, then retire the old E002 v2 family.

## 3. P018

### `agent/p018-critical-grid` / PR #68

Audit:

- `ahead=121`
- `behind=146`
- changed files span pair/kernel, coalescence, context separation, operation congruence, predictive closure, transport, reusable interface, quotient basin, and Supplements 12–26.

State: `REPLAY_REQUIRED / FROZEN`.

Do not append Supplement 27+ to PR #68.

Replay routing:

- general future-compatible quotient / congruence / minimal repair → A2/P023 core owner;
- precision-specific pair/kernel/context-depth/transport → `program/p018-precision-v2`;
- quotient-basin/factor/proof specializations → P018 application layer.

### Small historical P018 branches

| Branch | ahead | behind | State |
|---|---:|---:|---|
| `research/p018-graded-precision` | 5 | 337 | `REPLAY_REQUIRED` |
| `research/p018-proof-certificates` | 6 | 336 | `REPLAY_REQUIRED` |
| `research/p018-factor-precision` | 5 | 335 | `REPLAY_REQUIRED` |

Do not rebase or merge these old histories. Replay their unique mathematics together with selected #68 assets onto latest main.

## 4. A3 / A4

### `research/core/relation-quotient`

Audit: hundreds of ahead/behind commits; the tree now mixes relation-state, guard, causal, geometry, and other assets.

State: `REPLAY_REQUIRED / FROZEN`.

Target owner: `core/a3-relation-state-v2`.

Replay only A3 structured relation-state / partition quotient / kernel / guard-image / task-derived relation precision.

### `research/core/admissible-support-relations`

Still owns unique admissible-support/common-collapse material.

State: `ACTIVE_OWNER`, but should migrate to `core/a4-admissible-support-v2` so that future A4 work no longer inherits E001 engineering history.

### `research/core/relation-support-bridge` / PR #83

Highly diverged and now owns many staged-support/count/witness/equitability/semantic-shadow results.

State: `REPLAY_REQUIRED / FROZEN`.

Target: `bridge/a3-a4-v2` containing true bridge theorems only. Independently reusable witness/count/shadow theorems must move to a named L1 owner.

### PR #85 `A3 dependency sync into relation-support bridge`

State: `OBSOLETE SYNC PATTERN`.

The v2 lifecycle forbids long-lived wholesale synchronization PRs as a bridge-maintenance mechanism. Replace with semantic replay.

## 5. P017

P017 remains a program owner, but historical `agent/legendre-*` and `integration/p017-*` refs should not all remain active.

Audited samples:

| Branch | ahead | behind | Action |
|---|---:|---:|---|
| `agent/p017-lower-band-root-overlap` | 6 | 148 | small semantic replay |
| `agent/p017-full-core-crt-stacked` | 6 | 96 | small semantic replay |
| `agent/p017-multiplicative-resource-capacity` | 0 | 198 | `ABSORBED` |

New P017 research should run from `program/p017-legendre` or a short task branch from latest main rather than leaving every stage as a permanent ref.

## 6. E001 / E002 contact stack

Current stack:

- PR #101 `predictive Boolean-contact quotient bridge`;
- PR #108 `symmetric contact action-family gcd quotient`;
- PR #113 `contact semigroup versus group-completion precision`.

This is a temporary bridge chain, not three permanent owners.

State: `ACTIVE_BRIDGE` until the current T38–T42 pressure test closes.

Then:

1. lift general future-language quotient/gcd/semigroup mathematics to A2/P023;
2. retain the contact specialization in E001/E002;
3. create one clean latest-main replay PR;
4. archive #101/#108/#113.

## 7. E001 engineering/material

### PR #70 historical E001 collision

State: `PROVENANCE + REPLAY SOURCE`.

Engineering workloads/benchmarks remain E001-owned. General support/correspondence mathematics has moved toward A4. Do not expand generic theory on #70.

### PR #95 stacked material response

State: `PROVENANCE / REVIEW FOR UNIQUE DELTA`.

A current-main clean replay now exists for material foundation/validation. Audit #95 only for unique material-response probe assets not replayed elsewhere; close it once no unique delta remains.

### PR #114 / #115

These illustrate the desired model: clean current-main replay, small delta, explicit boundary.

## 8. P021 / P022

Historical PR #48/#50 remain provenance sources and must not be wholesale merged.

- P021 target owner: `program/p021-causal-focusing-v2`, clean replay of causal/direction-specific results; lift generic witness-sufficiency upward.
- P022 target owner: `program/p022-geometry-v2`, replay only lattice/metric/balls/radial/distance-carry results; do not carry A3 generic relation machinery.

## 9. Architecture

Old PR #81 / `chore/research-architecture-v1`:

State: `SUPERSEDED BY V2 REPLAY`.

The current `chore/research-architecture-v2` replays the mathematical ownership rules from latest main and adds the Git lifecycle contract. Close #81 after v2 gates pass.

## 10. First migration batches

1. merge architecture v2 + lifecycle + ledger;
2. close clearly obsolete sync/provenance PRs, starting with #56/#85, then audit PRs whose heads are `ahead=0`;
3. replay the two unique `e002-task-observable-v2` commits;
4. create `program/p018-precision-v2` and freeze #68;
5. create A3/A4 v2 owners plus a thin bridge;
6. replay small P017 deltas;
7. clean replay P021/P022;
8. remove absorbed branch refs.

## 11. Target active surface

Keep roughly 8–12 long-lived writable refs. Everything else should be a short-lived agent/integration ref or provenance in Git/PR/tag history, not another apparent current owner.
