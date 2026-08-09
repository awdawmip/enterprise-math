# Enterprise Math Current Research Branch Ledger

Status: `MIGRATION LEDGER / AUDITED SUBSET`  
Initial audit baseline: `main@fbd95bc3d119c2429d3e83825b5cd44cd044e501`  
Current recheck baseline: `main@c8aae69491fe50b107ca98b5777b9653be9f9aaf`  
Date: 2026-08-09

This ledger records critical refs already checked through Git compare, exact blob comparison, PR metadata, or theorem/path semantic audit. `ahead/behind` values are governance signals only; actual absorption follows `RESEARCH_BRANCH_LIFECYCLE` semantic audit.

## 1. Confirmed `ABSORBED`

### 1.1 Mechanical absorption: `ahead(main)=0`

| Branch | Result | Action |
|---|---|---|
| `agent/e001-material-foundation` | ahead=0 | provenance only |
| `agent/p017-multiplicative-resource-capacity` | ahead=0 | provenance only |
| `research/p018-all-power-quotient-basin-final` | ahead=0 | provenance only |
| `research/p023-composition-safe-collapse` | ahead=0 | provenance only |
| `research/p023-safe-selector-semigroup` | ahead=0 | provenance only |
| `research/e002-horizon-saturation-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-precision-locked-actuation-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-precision-native-hysteresis-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-predictive-quotient-compiler-v2` | ahead=0 | absorbed E002 generation |
| `research/e002-vector-actuation-v2` | ahead=0 | absorbed E002 generation |

### 1.2 Semantic absorption: different ancestry, same assets on main

`research/e002-task-observable-v2` still reports `ahead=2`, but this audit confirmed:

- `docs/E002_TASK_RELATIVE_OBSERVABLE_SUPPLEMENT_05.en.md` is the exact same blob on main;
- `src/enterprise_math/precision_task_observable.py` is the exact same blob on main;
- `tests/test_precision_task_observable.py` is the exact same blob on main.

Its ahead commits therefore do not represent unique mathematics. State: `ABSORBED / SEMANTIC`; **do not create a duplicate integration replay**.

Conclusion: the old E002 v2 generation has left the active research surface. Future E002 work should start from current main on a short task/program branch.

## 2. Synchronization shells actually closed

### PR #56 — `Sync canonical main into P018 Stage 9`

State: `CLOSED / PROVENANCE`.

Reason: synchronization-only PR with no new mathematics; Architecture v2 replaces wholesale sync with latest-main semantic replay.

### PR #85 — `A3 dependency sync into relation-support bridge`

State: `CLOSED / PROVENANCE`.

Reason: dependency-only owner→bridge synchronization; latest-main semantic replay replaces this pattern.

## 3. Zero-risk closure audit of old PRs

The following old heads were recomputed against current main. They still contain unique mathematics and therefore **must not be closed yet**:

| PR / Branch | ahead | behind | Current decision |
|---|---:|---:|---|
| #22 `research/p005-multibase-scale-algebra` | 3 | 372 | `SEMANTIC_REPLAY_AUDIT_REQUIRED` |
| #21 `agent/legendre-basin-aggregate` | 4 | 372 | `SEMANTIC_REPLAY_AUDIT_REQUIRED` |
| #23 `agent/legendre-mirror-separation` | 6 | 372 | `SEMANTIC_REPLAY_AUDIT_REQUIRED` |
| #54 `research/p018-centered-prime-radius` | 35 | 317 | `REPLAY_REQUIRED` |
| #65 `research/p017-rough-window-recursion` | 20 | 262 | `REPLAY_REQUIRED` |

Important boundary: old P017 history contains cases where a later route reused the **same Supplement filename** for different mathematics. For example, historical `LEGENDRE_PRESSURE_TEST_SUPPLEMENT_06` and current-main Supplement 06 are not the same blob/theorem family. **Filename equality is not absorption evidence.**

## 4. P018

### `agent/p018-critical-grid` / PR #68

Current scale: roughly `ahead=121`, with more than one hundred behind commits; changed files span pair/kernel, coalescence, context separation, operation congruence, predictive closure, transport, reusable interface, quotient basin, and Supplements 12–26.

State: `REPLAY_REQUIRED / FROZEN`.

Do not append Supplement 27+ to #68.

Replay routing:

- general A2/P023 future-compatible quotient / congruence / minimal repair → core owner;
- P018 precision-specific pair/kernel/context-depth/transport → `program/p018-precision-v2`;
- quotient-basin/factor/proof specializations → P018 application layer.

### Small historical P018 branches

| Branch | Unique scale | State |
|---|---:|---|
| `research/p018-graded-precision` | 5 commits | replay audit |
| `research/p018-proof-certificates` | 6 commits | replay audit |
| `research/p018-factor-precision` | 5 commits | replay audit |
| `research/p018-centered-prime-radius` | 35 commits | replay audit |

Treat them and #68 as source history; do not rebase the old trees.

## 5. A3 / A4

### `research/core/relation-quotient`

State: `REPLAY_REQUIRED / FROZEN`.

The tree now has hundreds of ahead/behind commits and mixes relation-state, guard, causal, geometry, and other assets.

Target owner: `core/a3-relation-state-v2`; replay only A3 structured relation-state / partition quotient / kernel / guard-image / task-derived relation precision.

### `research/core/admissible-support-relations`

State: `ACTIVE_OWNER -> MIGRATE TO core/a4-admissible-support-v2`.

It still contains unique admissible-support/common-collapse assets; the new owner should no longer inherit E001 engineering history.

### `research/core/relation-support-bridge` / PR #83

State: `REPLAY_REQUIRED / FROZEN`.

Target: `bridge/a3-a4-v2`, retaining bridge theorems only. General witness/count/shadow/equitability mathematics must be assigned to an L1 owner.

## 6. P017

P017 remains a program owner, but historical stage refs no longer all remain active.

Audited examples:

| Branch | ahead | behind | Action |
|---|---:|---:|---|
| `agent/p017-lower-band-root-overlap` | 6 | 148 (earlier audit) | small semantic replay |
| `agent/p017-full-core-crt-stacked` | 6 | 96 (earlier audit) | small semantic replay |
| `agent/p017-multiplicative-resource-capacity` | 0 | — | absorbed |
| `agent/legendre-basin-aggregate` | 4 | 372 | replay audit |
| `agent/legendre-mirror-separation` | 6 | 372 | replay audit |
| `research/p017-rough-window-recursion` | 20 | 262 | replay audit |

Future P017 research should run from `program/p017-legendre` or a short latest-main task branch.

## 7. E001 / E002 contact stack

Current stack: PR #101 → #108 → #113.

State: short `ACTIVE_BRIDGE` chain.

Allow the current T38–T42 pressure test to finish, then:

1. lift general future-language quotient/gcd/semigroup mathematics to A2/P023;
2. keep the contact specialization in E001/E002;
3. create one latest-main clean replay;
4. archive #101/#108/#113.

## 8. E001 engineering/material

- PR #70: `PROVENANCE + REPLAY SOURCE`; stop adding general mathematics there;
- PR #95: `PROVENANCE / REVIEW UNIQUE DELTA`;
- PR #114/#115: current-main clean replay; preferred future pattern.

## 9. P021 / P022

Historical PR #48/#50 remain provenance sources and must not be wholesale merged.

- P021 → `program/p021-causal-focusing-v2`: replay only causal/direction-specific results;
- P022 → `program/p022-geometry-v2`: replay only lattice/metric/balls/radial/distance-carry; route generic A3 machinery away.

## 10. Architecture

Old PR #81 / `chore/research-architecture-v1`: `SUPERSEDED BY V2 REPLAY`.

New PR #121 / `chore/research-architecture-v2`: current-main two-parent synchronization, carrying the A0–A5 mathematical ownership axis, L0–L5 Git lifecycle, and this ledger.

Close #81 after #121 passes gates.

## 11. Next migration batch

1. run real gates on #121;
2. archive E002 v2 refs as semantically absorbed, with no duplicate replay;
3. create the `program/p018-precision-v2` semantic replay manifest;
4. freeze #68 and build a source→owner map;
5. create A3/A4 v2 owners plus a thin bridge;
6. audit old P017 stages theorem by theorem;
7. clean replay P021/P022;
8. remove absorbed branch refs / convert checkpoints to tags.

## 12. Target active surface

Keep roughly 8–12 long-lived writable refs. Git/PR/tag history stores provenance; branch refs represent only the live research frontier or short-lived transport work.
