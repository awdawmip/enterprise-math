# Enterprise Math Current Research Branch Ledger

Status: `CANONICAL OWNER-ISOLATION LEDGER / AUDITED WRITE SURFACE`  
Snapshot: `main@683d6baaec90f4d59a5c3a64c9d40a6f3a24a337`  
Date: 2026-08-09

This ledger records the current semantic write surface after the Architecture-v2 / Owner-Isolation migration. Git ancestry is evidence, not ownership: a branch may be far behind main and still be a valid isolated owner, while an old generation may be semantically exhausted even if its historical commits remain visible.

The governing rule is:

`owner research -> freeze exact payload -> fresh latest-main L4 replay -> full merge-state gates -> canonical main`.

L1/L2/L3 owners do not chase moving main. L4 is globally `NO NEW MATHEMATICS`.

## 1. Canonical state reached in this migration batch

The following reusable layers are already canonical on main:

- A2 k-ary operation-congruence / future-compatible quotient extension;
- A3 weighted relation-state / relation-lattice / integer-scale core;
- A4 finite correspondence / admissible-support / relational-spectrum core;
- the thin A3->A4 generated-support bridge B01-B06 slice;
- P021 finite causal-boundary core;
- P022 A_p/root-lattice geometry core;
- Owner-Isolation execution rules in `AGENTS.md`;
- scope-aware branch governance auditor.

Important canonical merges from the ordered compaction pass include:

- branch-ledger refresh: `87231d29`;
- Owner-Isolation AGENTS replay: `ca923d64`;
- thin A3/A4 bridge: `e8407882`;
- P021 causal-boundary core: `21c1ef66`;
- P022 A_p lattice core: `4a4a2fde`;
- concurrent E001 finite impulse-world integration: `683d6baa`.

## 2. Current active write surface: 11 branches

The target is not a universal fixed branch count. The current audited surface contains 11 branches whose theorem/application homes are genuinely distinct.

### 2.1 Program owners — 5

1. `program/p017-legendre`
   - current square-basin / Legendre frontier;
   - audited branch-side work is confined to `P017_*` / `p017_*` assets;
   - current active directional work remains WIP, not canonical theorem numbering.

2. `program/p018-precision-v2`
   - current precision-specific owner;
   - branch-side work is confined to P018 / precision partition-margin assets;
   - generic quotient theory remains A2/P023-owned.

3. `program/p021-causal-focusing-v3` — Draft PR #213
   - fresh generation from `main@683d6baa` after v2 causal-boundary promotion;
   - begins with `owner_manifest_p021_v3.json` only;
   - retains focusing observables, direction-orbit / causal-role structure, causal witness transport, finite causal spectra, and physically bounded application routes;
   - generic future quotient -> A2/P023; generic correspondence/witness algebra -> A4; generic precision response -> P018; physical validation policy -> P016.

4. `program/p022-geometry-v2`
   - A_p lattice core is already canonical;
   - HCP, Barlow stacking/coordination, geodesic multiplicity and related precision questions remain active same-owner geometry research;
   - `p022_*` source/test families and P022 bilingual registration are therefore legitimate owner assets, not `SCOPE_DRIFT` merely because they are not named `lattice_*`.

5. `program/p024-action-precision`
   - closed-form action-language / boundary-precision specialization owner;
   - generic quotient and adjunction mother theory remains upstream A2/P023/P008.

### 2.2 Cross-owner bridges — 3

1. `bridge/a3-a4-generated-support-v3`
   - current thin A3/A4 bridge;
   - first three-asset B01-B06 slice is canonical;
   - future bridge work must genuinely mention both A3 relation state and A4 correspondence/support.

2. `bridge/p017-p018-hard-core-v2`
   - active arithmetic/precision bridge;
   - audited branch-side files are confined to `p017_p018_*` theorem/test families;
   - current work includes hard-core root-channel, tail-resource and cubic ambiguity structures.

3. `bridge/a2-e001-material-markov`
   - active future-material specialization bridge;
   - branch-side files are confined to `material_future_*` code/tests;
   - generic quotient/minimization remains A2-owned, material meaning remains E001-owned.

### 2.3 E001 engineering owners — 3

1. `engineering/e001-material-impulse-v2` — PR #190
   - active finite impulse/momentum research beyond the already-canonical wall-world slice;
   - retains force activation, subquantum accumulation, precision re-entry and reversal-certificate questions.

2. `engineering/e001-material-pair-impulse` — PR #205
   - next bounded two-body generation after the canonical one-body wall impulse world;
   - equal-and-opposite delivered impulse, total integer momentum invariance and relative separation are the declared local problem.

3. `engineering/e001-material-multiaction-protocol` — PR #185
   - independent empirical/P023 adapter owner;
   - explicit measured action graph -> canonical future partition;
   - does not own generic P023 minimization.

## 3. Exhausted or frozen owner generations

The following refs are not current write points:

- `core/a2-future-quotient-v2` — fully absorbed, observed `ahead=0`; future A2 mother-theorem work should start a new generation from then-current main.
- `core/a3-relation-state-v2` — fully absorbed, observed `ahead=0`; start a new A3 generation only when new owner work exists.
- `core/a4-admissible-support-v2` — fully absorbed, observed `ahead=0`; start a new A4 generation only when needed.
- `program/p021-causal-focusing-v2` — causal-boundary slice promoted; PR #182 closed `PROMOTED / PROVENANCE`; v3 is active.
- `engineering/e001-material-impulse-world` — frozen source PR #194; the eight-file wall-world slice is canonical in `main@683d6baa`.

Do not fast-forward these old generations merely to make them look current. Their historical shape is provenance.

## 4. Replay-required or stacked sources

These branches contain useful history but are not current theorem homes:

- `research/core/relation-quotient` — broad historical A3 source; replay by owner only.
- `research/core/relation-support-bridge` — broad historical A3/A4 source; B01-B06 has been promoted through the thin bridge, while B07-B58 must be rehomed to A4/A5/A2/P021 as appropriate.
- `bridge/a3-a4-v2` — old broad bridge generation; no longer active.
- `engineering/e001-material-state-cost` — stacked benchmark/application; it carries `material_future_precision` from the A2/E001 bridge and must later replay only its unique benchmark/test assets after the bridge is canonical.

## 5. Semantic audit of selected historical PRs

### 5.1 Closed as absorbed

- PR #22 P005 multi-base scale algebra — `ABSORBED / SEMANTIC`.
  - canonical P005 covers scale-factor compatibility, projection composition, multi-base order, gcd/lcm diamond and the explicit nonunique refinement witness;
  - the historical state-only refinement criterion is a specialization of canonical P023 fiber constancy/descent.

- PR #23 P017 transverse mirror support — `ABSORBED / STRICT_GENERALIZATION`.
  - canonical `p017_mirror.py`, `p017_mirror_incidence.py` and tests retain the historical support/incidence results and add stronger resource/coprimality structure.

- PR #65 P017 rough-window/high-band route — `ABSORBED / STRICT_GENERALIZATION`.
  - core cofactor/rough assets and Supplements 06-08 survive on main;
  - the current high-band implementation/test/provenance layer strictly extends the historical resource results.

### 5.2 Must remain open as research/provenance

- PR #21 — `PARTIAL ABSORPTION / CORRECTED / DEPENDENCY-BLOCKED WIP`, Draft.
  - old L023 is subsumed by canonical L039;
  - old L024 was corrected by L041, which requires anchor survival and supplies a counterexample to the unqualified statement;
  - only the L025 four-support graph-tail aggregate remains noncanonical;
  - historical CI failed because `basin_aggregate.py` imports missing `enterprise_math.four_support`; therefore L025 is unvalidated WIP, not a replay-ready result.

- PR #54 — `SPECIALIZATION / STILL-UNIQUE REPRESENTATION / UNVALIDATED DRAFT`.
  - centered-prime radius is a near-diagonal two-candidate specialization of the later general cofactor-window calculus;
  - `centered_prime_radius.py`, its tests, the conditional identity `rho(k+1)=sigma(k)+1`, and the `k=10` boundary counterexample are still not represented as their own canonical coordinate layer;
  - no replay until current-head validation, numbering reconciliation and prior-art audit.

## 6. Scope-audit corrections in this snapshot

The scope-aware audit exposed two metadata errors and one lifecycle improvement:

1. P022 was falsely narrow in the old override. `p022_hcp_*`, `p022_barlow_*`, `p022_geodesic_*`, their tests, and P022 bilingual registration are legitimate same-owner assets.
2. The new `bridge/a3-a4-generated-support-v3` must replace the old v2 bridge as the active A3/A4 bridge.
3. A2/A3/A4 v2 refs are exhausted generations, not permanent write points. Canonical theorem homes live on main; create a new generation only when new owner mathematics actually resumes.

At the snapshot, P017, P018, P021-v3, P022, P024 and all three active bridge families show no cross-home scope pollution under their declared paths. E001's active owner branches are separated by impulse, pair-impulse and empirical-protocol roles; the state-cost branch is intentionally marked stacked/replay-required.

## 7. Canonical promotion protocol

For every active owner or bridge:

1. research locally on the owner generation without whole-main synchronization;
2. relay reusable results to affected routes;
3. freeze the exact payload selected for publication;
4. create a fresh L4 branch from then-current main;
5. replay only the frozen owner-owned payload;
6. run quality, bilingual-sync, reference-integrity, and Lean when applicable on the exact merge state;
7. merge only that L4;
8. close or freeze the exhausted source generation when its remaining branch-side payload is fully accounted for.

A moving main is not a research stop condition. It matters only at the final L4 combination gate.

## 8. How to use this ledger

Before new work:

- use `AGENTS.md` for execution rules;
- use `RESEARCH_COMMON_SURFACE` for reusable theorem/tool discovery;
- use this ledger for owner/ref routing;
- use `branch_governance_overrides.json` with `tools/audit_branch_lifecycle.py` for machine scope classification;
- use PR/commit provenance for historical details.

Do not infer theorem ownership from branch age, ahead/behind counts, or filename history alone.
