# R043 — Native Surface Frontier Reconstruction / Markov Carrier Checkpoint

Status: `SEMANTIC_CHECKPOINT / BOUNDED_G0_RECONSTRUCTION_POSITIVE / GLOBAL_STATIONARY_OPEN`  
Researcher-ID: `EM-R043-8C2F71`  
Task: `RS-R043-NATIVE-SURFACE-FRONTIER-RECONSTRUCTION-MARKOV-CARRIER`  
Taskbook source: `41afbdf37f70b1fc484f7a49bc68880826ead31d`  
Frozen R041 owner head: `688661e76255b3e86df6d5c69695f2932b650740`  
Frozen R039 owner head: `c484fb85385b8498982aaa939171957588c836d7`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`

## 0. Executive verdict

R043 does **not** promote `G0` to a global stationary Markov theorem, and it does **not** find a counterexample. The exact checkpoint is:

1. `G0` is injective on every frozen-symmetry cluster class through `N<=8` in both FCC and HCP, including cross-`N` comparison. Hence on that bounded source domain `G0` determines `B3`, `B4`, and every fixed finite Boolean future because it determines the entire source cluster class.
2. This bounded injectivity is not upgraded to arbitrary `N`.
3. The rooted question `G0 + action -> successor G0` has no split in all strong-invariant scans through `N=8`; strict exact rooted gates pass completely through FCC `N<=7` and HCP `N<=6`, plus HCP `N=8` strict stabilizer holdouts. A global structural extension theorem remains open.
4. A new exact carrier strictly below full `M3` is proved: retain `G0`, the shared-future incidence sets `I_z=N(z)∩L0`, and only the `L1-L1` edges whose endpoints can be coexposed by one current action. This **coexposure carrier** reconstructs exact successor `G0` and therefore exact current `B3`.
5. The coexposure carrier is one-successor / `B3` exact, not yet recursively closed as the same fixed-form state.

The mother-question has therefore moved from “does `G0` obviously miss L1 correlation?” to “why are realizable native weighted frontiers so rigid, and does that rigidity hold for every finite FCC/HCP cluster?”

---

## 1. Frozen results consumed without reopening

R043 treats the following as frozen.

From R039:

- native surface is the contact cut;
- `S(C)=sum_{x in F(C)} k_C(x)`;
- reduced `R2bar` is a frontier-profile bag and loses relational correlation at higher future depth;
- the frozen FCC/HCP animal atlases and their symmetry conventions are inherited.

From R041:

- `R2bar -> B2` exactly;
- `R2bar -/-> B3`, first bounded collision size `N=6` in both frozen worlds;
- `M3`, the weighted induced graph on `L0 union L1`, exactly reconstructs successor `R2bar`, hence `M3 -> B3`;
- more generally `M_h` through `L_{h-2}` is an exact horizon-indexed recursively executable Boolean carrier;
- preliminary weighted-frontier-only `G0` search had no collision through FCC `N<=7`, HCP `N<=6`, with no theorem claim.

No frozen theorem was recomputed, re-owned, weakened, or promoted by R043.

---

## 2. Candidate `G0`

The taskbook state is

```text
G0(C) = (S(C), weighted induced contact graph on F(C)),
weight(x)=k_C(x).
```

Because `S=sum_x k(x)` by the frozen frontier handshake, separately serialized `S` is algebraically redundant once all vertex weights are retained. R043 keeps the taskbook name and equivalence; this is only a storage observation.

---

## 3. R043-T1 — complete bounded `G0` injectivity through `N<=8`

An independent engine reimplements the frozen FCC/HCP contact graphs and frozen symmetry canonicalization, then constructs the weighted frontier graph.

The collision sieve uses a necessary invariant for weighted-graph isomorphism:

- frontier vertex and edge counts;
- attachment-weight histogram;
- `(weight, frontier-degree)` histogram;
- 12-round canonical color refinement;
- color-pair edge histogram.

This invariant is only a bucket filter. Exact weighted graph isomorphism is separately implemented. The rigorous implication used for the bounded injectivity result is only

```text
weighted graph isomorphism => equal safe invariant.
```

Thus if every realized state has a unique safe invariant, no exact weighted-graph collision exists in that domain.

Exact frozen atlas counts:

| N | FCC classes | HCP classes |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 4 | 9 |
| 4 | 20 | 57 |
| 5 | 131 | 460 |
| 6 | 1,211 | 4,641 |
| 7 | 12,734 | 50,353 |
| 8 | 144,158 | 575,375 |
| **total N<=8** | **158,260** | **630,898** |

Cross-size `G0` sieve:

```text
FCC N<=8: 158,260 states / 158,260 unique invariant buckets / 0 duplicate.
HCP N<=8: 630,898 states / 630,898 unique invariant buckets / 0 duplicate.
```

Therefore, under each frozen world quotient,

```text
G0(C) ~= G0(D), |C|,|D|<=8
  => C,D are the same frozen symmetry class.
```

This is a bounded reconstruction theorem only. The inherited HCP 24-representative crystallographic-completeness caveat remains an L4 audit item.

### Bounded future corollary

Because `G0` determines the complete source cluster class on the bounded domain,

```text
G0 -> B3,
G0 -> B4,
and G0 -> B_h for every fixed finite h
```

on source states `N<=8`. This is a domain-injectivity corollary, not a stationary update theorem.

---

## 4. Rooted action gate: `G0 + action -> successor G0`

Abstract source-state injectivity is insufficient: a single `G0` can have automorphisms, and two abstractly equivalent frontier actions could conceivably lead to different successor frontiers. R043 therefore audits rooted action classes separately.

### FCC strict exact gate

Complete through every FCC state with `N<=7`:

```text
states:                           14,102
rooted exact-isomorphism checks:  18,774
nontrivial exact root orbits:      16,784
successor exact-isomorphism checks:18,774
splits:                            0
```

At FCC `N=8`, all 144,158 states pass the stronger successor-invariant split sieve with zero split.

### HCP gate

Strict exact rooted checking is complete through HCP `N<=6` (5,170 combined atlas states) with zero split. At HCP `N=8`:

```text
strong successor-invariant scan:
  states: 575,375
  splits: 0

strict stabilizer holdout:
  states: 5,000
  nontrivial color buckets: 1,361
  buckets crossing frozen ambient-stabilizer orbits: 0
```

Singleton sanity check:

```text
FCC: one abstract rooted action orbit of size 12; one successor-G0 class.
HCP: two rooted action orbits of size 6+6; two successor-G0 classes of size 6+6.
```

Hence HCP basal/interlayer action type is already encoded in singleton `G0`; it is not a missing external slot label at this size.

No rooted split was found. Nevertheless the arbitrary-`N` implication

```text
G0(C), action-class -> G0(C+x)
```

remains `OPEN`: bounded gates are evidence, not a structural extension proof.

---

## 5. Pair-overlap audit

For

```text
O2(x,y)=#{z in L1 : z~x and z~y},
```

R043 tested whether one realized `G0` can contain abstractly pair-equivalent frontier pairs with different `O2` values. Exact pair-root audits found no split in:

```text
FCC N=6:  1,211 states / 1,119 exact pair-root checks
FCC N=7: 12,734 states / 2,972 exact pair-root checks
HCP N=6:  4,641 states / 1,420 exact pair-root checks
```

This does not prove global reconstructibility of `O2`, nor pairwise sufficiency if a future true `G0` collision is found.

---

## 6. R043-T2 — exact coexposure carrier below full `M3`

Let

```text
F=L0(C),
L1=next exterior layer.
```

For `z in L1`, define

```text
I_z=N(z) intersect F.
```

For action `x in F`, the newly exposed cells are exactly

```text
W_x={z in L1 : x in I_z}.
```

Retain only those actual `L1-L1` edges whose endpoints can be exposed together by at least one current action:

```text
E_co={zq in E(L1) : I_z intersect I_q != empty}.
```

Define

```text
X3(C)=G0(C)+{I_z : z in L1}+E_co.
```

### Exact update theorem

Given `X3(C)` and action `x`:

```text
F'=(F-{x}) union W_x.
```

Weights are

```text
k'(y)=k(y)+1_{y~x}    for old y in F-{x},
k'(z)=1               for z in W_x.
```

Successor-frontier edges split into:

1. old-old: inherited from `G0` after deleting `x`;
2. old-new: `z--y` exactly when `y in I_z-{x}`;
3. new-new: exactly `E_co` restricted to `W_x`.

For class 3, if `z,q in W_x`, then `x in I_z intersect I_q`. Hence every actual edge between simultaneously exposed new cells satisfies the coexposure condition and is retained. Conversely every retained actual edge with both endpoints in `W_x` is a successor-frontier edge.

Therefore, globally in both frozen contact worlds,

```text
X3(C), x -> exact G0(C+x).
```

This is a set/combinatorial proof and is independent of bounded atlas size.

### Dead-edge pruning theorem

If an actual `L1-L1` edge `zq` satisfies

```text
I_z intersect I_q = empty,
```

then no single current action exposes both endpoints. Such an edge is invisible in every immediate successor `G0`; it is theorem-level dead information for the one-successor query and may be deleted.

Thus `X3 <= M3`, with strict inequality whenever dead `L1-L1` edges exist.

---

## 7. R043-T3 — `X3 -> B3`

Frozen R041 proves `G0=M2 -> B2`. R043 proves `X3,x -> G0(C+x)` for every first action. Therefore

```text
X3(C) -> B3(C)
```

exactly in the frozen addition-only Boolean language.

This is the R043 global exact carrier result. It is not yet proved recursively updateable as `X3(C+x)`: child coexposure may import information outside the parent's stored `L1`. Therefore it is classified as an exact one-successor / `B3` repair, not a stationary carrier.

---

## 8. Carrier Pareto

Singleton shared-future structures:

```text
FCC singleton:
  |F|=12, |L1|=42
  |I_z| histogram={1:12,2:24,4:6}
  E01=84
  E11 full=96, coexposed=96, pruned=0

HCP singleton:
  |F|=12, |L1|=44
  |I_z| histogram={1:18,2:18,3:2,4:6}
  E01=84
  E11 full=108, coexposed=102, pruned=6
```

HCP therefore already contains triple shared-future incidence at the singleton, whereas FCC singleton does not. This is a structural difference, not yet a proof of different minimal residual order.

Full `N=7` edge Pareto:

| world | states | avg M3 edges | avg X3 edges | pruned E11 | % E11 pruned | % all M3 edges pruned |
|---|---:|---:|---:|---:|---:|---:|
| FCC | 12,734 | 599.290 | 590.612 | 110,496 | 3.476% | 1.448% |
| HCP | 50,353 | 618.189 | 600.346 | 898,455 | 6.651% | 2.886% |

Aggregate details:

```text
FCC N=7:
  M3 vertices=1,849,366
  E00=1,414,386
  E01=3,038,168
  E11 full=3,178,799
  E11 coexposed=3,068,303
  states with pruning=12,731/12,734
  max pruned E11/state=19

HCP N=7:
  M3 vertices=7,469,384
  E00=5,602,798
  E01=12,015,928
  E11 full=13,508,938
  E11 coexposed=12,610,483
  states with pruning=50,353/50,353
  max pruned E11/state=31
```

This representation saves edges but no `L0 union L1` vertices.

Independent coordinate-level exact-update checks:

```text
FCC: 200 states / 6,780 actions / 0 mismatch
HCP: 100 states / 2,942 actions / 0 mismatch
```

The proof, not these bounded checks, is the theorem-critical justification.

---

## 9. Negative control: hidden one-step touch is not a tiny rooted stencil

A tempting proof route says every old frontier vertex touched by a newly exposed `L1` cell must lie in a small rooted graph-radius around the chosen action inside current `G0`. That geometric shortcut fails already at `N=7`.

FCC witness:

```text
C=((0,0,0),(0,0,2),(0,1,-1),(0,1,3),(0,3,-1),(1,0,1),(1,2,-1))
x=(0,4,0)
z=(0,3,1) in L1, z~x
y=(0,2,2) in F, y~z
d_G0(x,y)=4.
```

HCP witness:

```text
C=((0,0,0),(0,1,0),(0,1,1),(1,0,3),(1,1,2),(1,1,4),(2,0,2))
x=(1,-1,0)
z=(1,-1,1) in L1, z~x
y=(2,-1,2) in F, y~z
d_G0(x,y)=4.
```

This kills only the naive radius-3 touch assumption. It does not by itself rule out a globally constrained predictor that infers the distant incidence from other `G0` structure.

---

## 10. Minimal hidden-correlation residual status

Because no exact `G0` collision is known, R043 cannot honestly call pair overlap, triple/hypergraph identity, or slot identity **necessary**.

For rooted state `(G0,x)`, define the **successor-extension orbit** as the rooted-automorphism quotient of the extension adding `W_x` together with its incidences to old frontier vertices and its internal edges. Any exact rooted updater must distinguish rooted states whenever these successor-extension orbits differ.

Thus the current formal location of possible debt is

```text
rooted successor-extension orbit.
```

`X3` is a concrete global sufficient realization/upper bound of these one-action residuals. Pair-overlap and hypergraph quotients remain possible further compressions; no current witness proves one irreducible.

---

## 11. Kernel / BRC ledger

Proved or bounded-safe:

```text
frozen R041: ker(R2bar) subseteq ker(B2) globally.
frozen R041: ker(R2bar) not subseteq ker(B3), bounded-minimal N=6 witnesses.
R043 bounded: ker(G0) is diagonal on each frozen N<=8 source atlas.
R043 global: ker(X3) subseteq ker(B3).
```

Not proved:

```text
global ker(G0) subseteq ker(B3);
global suffix-safe recoalescence under repeated G0 updates;
any multiplicity/provenance/probability analogue of the Boolean claims.
```

---

## 12. Hypothesis ledger

| Hypothesis | R043 status | Reason |
|---|---|---|
| H1 `G0_B3_SUFFICIENCY` | `BOUNDED_POSITIVE / GLOBAL_OPEN` | injective through N<=8; no arbitrary-N proof |
| H2 `G0_RECURSIVE_CLOSURE` | `STRONGLY_SUPPORTED / OPEN` | no rooted split in exact/strong gates |
| H3 `FRONTIER_STATIONARY_MARKOV` | `OPEN` | fixed-form global recursive theorem absent |
| H4 `PAIR_OVERLAP_REPAIR` | `NOT_TRIGGERED / NOT_PROVED` | G0 not killed |
| H5 `HYPERGRAPH_DEBT` | `SUFFICIENT_STRUCTURE, NOT LOWER_BOUND` | `I_z` is part of exact X3, necessity unproved |
| H6 `INTERIOR_FORGETFULNESS` | `STRENGTHENED_FOR_B3` | X3 ignores deeper data for current B3 |
| H7 `FCC_HCP_RECONSTRUCTION_SPLIT` | `QUANTITATIVE_SPLIT / ORDER_SPLIT_OPEN` | HCP has more dead edges/triple singleton incidence |
| H8 `FIXED_STATE_VS_HORIZON_GROWTH` | `OPEN` | R041 M_h remains only proved arbitrary-h family |

---

## 13. Mandatory negative controls

- bounded no-collision is not promoted to theorem;
- safe invariant is not treated as exact isomorphism;
- abstract graph equivalence is kept distinct from ambient embedding symmetry;
- pairwise overlap is not assumed to reconstruct triple/hypergraph structure;
- `B3` exactness is not promoted to all-horizon stationarity;
- terminal/query sufficiency is kept distinct from recursive Markov closure;
- Boolean support is not promoted to multiplicity/provenance/probability;
- FCC evidence is not transferred to HCP;
- no norm, radius, curvature, or Euclidean smooth-surface semantics enters the theorem path.

---

## 14. Evidence package and validation

Checkpoint files:

```text
SEMANTIC_CHECKPOINT.md
RESULTS.json
frontier_reconstruction_engine.py
test_frontier_reconstruction_engine.py
```

The independent engine contains frozen contact/canonicalization, `G0`, a safe collision invariant, dependency-free exact weighted graph isomorphism with optional root, exact Boolean `B_h` oracle, coexposure residual/update logic, and the locality-negative-control helper.

Focused tests:

```text
Ran 6 tests in 0.056s
OK
```

The dependency-free exact graph checker was additionally cross-checked against NetworkX on random FCC/HCP rooted and unrooted comparison samples with agreement. No CI/workflow status was queried.

---

## 15. Mandatory return answers

### 1. Is weighted current frontier sufficient for `B3`?

**Exactly yes on the complete frozen atlas `N<=8` in both FCC and HCP; globally unresolved.** Bounded injectivity of `G0` is stronger than a direct B3 check but cannot be extrapolated to arbitrary `N`.

### 2. Can `G0` recursively update itself?

**No counterexample found; no global proof.** Strict exact rooted gates pass through FCC `N<=7` and HCP `N<=6`, with full `N=8` strong-invariant scans and HCP stabilizer holdouts showing no split. Global `G0 + action -> successor G0` remains the primary open theorem candidate.

### 3. If not, what is the first missing correlation?

**Not determined because `G0` has not failed.** Formally any debt lives in the rooted successor-extension orbit. Shared-future incidence plus coexposed `L1` edges is globally sufficient. Pairwise, triple/hypergraph, and slot identity are not yet proved necessary.

### 4. How much smaller is the practical repair than `M3`?

`X3` keeps the same `L0 union L1` vertices but deletes immediately dead `L1-L1` edges. On the full `N=7` slice it removes 1.448% of all `M3` edges in FCC and 2.886% in HCP (3.476% and 6.651% of `E11`, respectively). This is a rigorous sufficient upper-bound repair, not an information-theoretic minimum.

### 5. Do FCC and HCP differ in reconstruction debt?

**Quantitatively yes; minimal residual order remains open.** HCP has more dead `L1-L1` structure and singleton triple shared-future incidence. Neither world has a `G0` failure through `N<=8`.

### 6. Must future precision grow with horizon, or is there a fixed stationary carrier?

**Open.** Frozen R041 `M_h` is still the proved arbitrary-h exact family. R043 provides much stronger evidence for `G0` reconstruction rigidity but not the global recursive closure needed for a stationary theorem.

### 7. Which interior information can be permanently collapsed?

For current Boolean `B3`, everything beyond `G0` plus the coexposure part of `L1` can be forgotten; dead `L1-L1` edges and deeper interior provenance do not enter the exact one-successor update. For arbitrary unbounded continuation, permanent collapse of all deep interior provenance is not proved: whatever is needed to reconstruct the next successor-extension/coexposure structure must continue through the boundary state unless global `G0` closure is established.

---

## 16. Next exact frontier

Do not spend the next cycle merely extending the no-collision atlas by one `N` unless needed to kill a structural candidate.

Highest-value continuation:

1. prove or kill the extension property that every rooted automorphism/isomorphism of a realizable `G0` preserves the rooted successor-extension orbit;
2. search deliberate boundary-preserving local surgeries, especially hidden shared-future shortcuts between frontier vertices far apart in `G0`;
3. on the first real `G0` collision, immediately compare `O2`, slot-orbit augmentation, shared-future hypergraph, and `X3` on the same witness;
4. test whether `X3` admits a fixed-form recursive update or necessarily imports parent `L2` information;
5. keep multiplicity/provenance outside the theorem until separately audited.

Current frontier:

> `G0` is an unexpectedly strong bounded reconstruction code, but stationary closure is unproved. If `G0` ever fails, the exact one-action debt lives in the rooted successor-extension orbit; shared-future incidence plus only coexposed `L1` edges is already a global exact `B3` repair strictly below full `M3`.
