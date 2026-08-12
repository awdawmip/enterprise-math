# R041 — Compact R3 / One-Layer-Shaved Operational Cone Extension

Status: `SEMANTIC_CHECKPOINT_EXTENSION / COMPACT_R3_POSITIVE / NOT_CANONICAL`  
Researcher-ID: `EM-R041-7C3A91`  
Task: `RS-R041-NATIVE-SURFACE-HORIZON-QUOTIENT-CALCULUS`  
Parent R041 checkpoint: `10e1b62491b8fbf954aa49233304638a33a01c34`  
Frozen R039 dependency: Draft PR #524 head `c484fb85385b8498982aaa939171957588c836d7`  
CI: `CI_NOT_REQUIRED_FOR_RESEARCH`

## 0. Verdict

The first R041 checkpoint reduced R039's full exterior cone `J_h` to an activation-pruned `K_h`. This extension proves a stronger horizon-indexed structural reduction for the declared Boolean branch-aware surface language:

```text
J_h -> K_h -> M_h -> B_h,
```

where, for `h>=2`, `M_h(C)` retains only

1. current `S(C)`;
2. the weighted induced native contact graph on
   `L0(C) union ... union L_{h-2}(C)`;
3. weight `k_C(x)` on `L0` and zero on deeper retained layers;
4. no explicit layer tags.

So the entire R039 deepest layer `L_{h-1}` and every incident edge can be omitted. For `h=3`, compact R3 is only the weighted induced graph on `L0 union L1`.

A second result locates the first reduced-R2 operational debt:

```text
R2bar -> B2 exact,
R2bar -/-> B3 first at N=6 in both frozen worlds.
```

For the R039 FCC CE6 pair, `T1,T2,T3` and `B2` are equal, but `B3` differs; terminal support differs only at `T4`. Recursive execution debt therefore appears one horizon earlier than terminal-answer debt in that exact witness.

---

## 1. R041-T4 — `R2bar` determines Boolean `B2`

R039 stores each current frontier candidate as

```text
Pbar_C(x)=(k_x,A_x),
```

with `A_x(j)` counting adjacent current-frontier cells in attachment bin `j`; `R2bar(C)` is the multiset of these profiles.

From first coordinates reconstruct

```text
H_C(k)=# {x in F(C): k_C(x)=k},
S(C)=sum_k k H_C(k).
```

For a first profile `(k_x,A_x)`, R039's exact reduced update is

```text
H' = H - e_{k_x} - A_x + shift_{+1}(A_x)
     + (12-k_x-sum_j A_x(j)) e_1,
S' = S + 12 - 2k_x.
```

Boolean `B1(C+x)` needs only `S'` and the support of `H'`. Therefore every branch `(k_x,B1(C+x))`, and hence `B2(C)`, is determined by `R2bar(C)`.

Thus

```text
R2bar(C)=R2bar(D) => B2(C)=B2(D).
```

This strengthens the frozen R039 use of `R2bar` from two-step terminal sufficiency to Boolean operational depth-two sufficiency. It is still far from minimal: at FCC `N=5`, `R2bar` has `131` classes while `B2` has `69` and `T2` only `18`.

Bounded executable check: `R2bar -> B2` agrees with the independent recursive oracle in FCC and HCP through `N<=4`.

---

## 2. R041-T5 / CE5 — first R2 operational debt is B3

R039 established no `R2bar` collisions through `N<=5`; first collisions occur at `N=6`.

### FCC N=6

Collision-group sizes are

```text
2,2,3.
```

Within every group:

```text
T3 class count = 1,
B3 class count = group size.
```

Hence all first FCC `R2bar` collisions are fully split by `B3`, although exact three-step terminal support still recoalesces each group.

For the frozen R039 CE6 pair

```text
C=((0,0,0),(0,0,2),(0,1,-1),(1,-1,4),(1,0,1),(1,0,3))
D=((0,0,0),(0,0,2),(0,1,-1),(0,1,1),(1,0,3),(1,1,-2)),
```

R041 obtains

```text
same R2bar
B2(C)=B2(D)
T1={68,70,72}
T2={72,74,76,78,80,82}
T3={76,78,80,82,84,86,88,90,92}
B3(C)!=B3(D).
```

R039's frozen `T4` supports are

```text
C: {82,84,86,88,90,92,94,96,98,100,102}
D: {80,82,84,86,88,90,92,94,96,98,100,102}.
```

So the pair gives the strict ladder

```text
same R2bar -> same B2 -> same T3,
but different B3, and only later different T4.
```

### HCP N=6

The first HCP `R2bar` collisions are four pairs. Their `(T3 classes,B3 classes)` pattern is

```text
(1,2), (1,1), (1,2), (1,1)
```

up to group ordering. Two pairs expose the same B3-before-terminal debt; two survive `B3`.

One exact split pair is

```text
C=((0,0,0),(0,1,0),(1,1,0),(1,2,0),(1,3,0),(2,3,0))
D=((0,0,0),(0,1,0),(1,1,0),(2,1,0),(2,2,0),(3,2,0)),
```

with

```text
same R2bar
B2 equal
T2={74,76,78,80,82}
T3={80,82,84,86,88,90,92}
B3 different.
```

Because there are no R2 collisions through `N<=5`, `N=6` is bounded-minimal for this failure in both worlds. The inherited HCP symmetry-completeness caveat remains.

Interpretation: `R2bar` stores local frontier profiles as a bag but loses the identity/correlation structure required to update the whole bag after a chosen first action.

---

## 3. R041-T6 — compact R3 needs only `L0 union L1`

Define `M3(C)` as current `S` plus the weighted induced contact graph on `L0 union L1`.

Choose `x in L0`. The successor frontier is exactly

```text
F(C+x)=(L0-{x}) union (N(x) intersect L1).
```

For old frontier `y`,

```text
k_{C+x}(y)=k_C(y)+1_{y~x};
```

for newly exposed `y in L1`,

```text
k_{C+x}(y)=1.
```

All adjacencies among successor-frontier vertices are already edges of the stored `L0 union L1` induced graph. Hence `M3` reconstructs the exact successor `R2bar(C+x)` for every first action. R041-T4 then yields exact successor `B2`, so `M3` yields exact current `B3`.

Exact checks:

```text
successor-R2 reconstruction:
  FCC all states through N<=4: PASS
  HCP all states through N<=3: PASS

M3 -> B3 direct bounded comparison:
  FCC 26 states through N<=4: PASS
  HCP 69 states through N<=4: PASS
```

---

## 4. R041-T7 — general one-layer-shaved family `M_h`

For every fixed `h>=2`, retain `S` and the weighted induced graph on

```text
L0 union ... union L_{h-2}.
```

### Layer reconstruction

`L0` is exactly the positive-weight set. Deeper retained layers are graph-distance layers from `L0`; explicit tags are redundant.

### Child containment

After choosing `x in L0`, every vertex needed by child `M_{h-1}` lies in the parent retained set. Indeed, a child layer-`r` cell (`r<=h-3`) lies at contact distance at most `r+1` from `C union {x}`; if reached through `x`, appending `x~C` puts its old exterior depth at most `r+1<=h-2`.

### Exact update

The child frontier is

```text
L0'=(L0-{x}) union (N(x) intersect L1),
```

with weights

```text
k'(y)=k(y)+1_{y~x}  for old frontier y,
k'(y)=1             for new L1 frontier y,
S'=S+12-2k(x).
```

Breadth-first expansion inside the retained parent graph reconstructs child layers through `L'_{h-3}` and their induced edges. Therefore

```text
M_h(C), x -> M_{h-1}(C union {x})
```

without querying omitted `L_{h-1}` cells.

### Base h=2

`M2` is only the weighted current frontier graph. For each chosen `x`, the exact number of newly exposed omitted-L1 cells is recovered from 12-regularity:

```text
b_x=12-k_x-deg_{L0}(x).
```

They all have successor attachment count 1, so exact `B1` follows.

Induction gives

```text
M_h(C) -> B_h(C)
```

for all fixed `h>=2` in the frozen addition-only Boolean language.

This is a horizon-indexed Markov family (`M_h -> M_{h-1}` as remaining horizon decreases), not a claimed stationary universal state. No claim is made yet for multiplicity/provenance semantics, deletion, unbounded horizon, or minimality.

Validation includes canonical-oracle equality at `h=2,3` and an independent raw non-symmetry-quotiented singleton oracle at `h=4` for both worlds.

---

## 5. Exact singleton cost slice

For the one-cell cluster:

| world | h | M vertices | M edges | J vertices | J edges |
|---|---:|---:|---:|---:|---:|
| FCC | 2 | 12 | 24 | 54 | 204 |
| FCC | 3 | 54 | 204 | 146 | 648 |
| FCC | 4 | 146 | 648 | 308 | 1476 |
| HCP | 2 | 12 | 24 | 56 | 216 |
| HCP | 3 | 56 | 216 | 152 | 684 |
| HCP | 4 | 152 | 684 | 322 | 1560 |

Thus at `h=3`, relative to full `J3`, `M3` removes about 63% of vertices and 68% of induced edges in both exact singleton fixtures.

For FCC singleton shells,

```text
|L_r|=10(r+1)^2+2,
|E(J_h)|=20h^3+12h^2+4h-12,
```

and `M_h` has exactly the vertex/edge size of `J_{h-1}`. Under the frozen HCP implementation,

```text
|L_r|=floor(21(r+1)^2/2)+2,
|E(J_h)|=(21/2)h(h+1)(2h+1)-18h^2-6h-3ceil(h/2)-12,
```

again with `M_h` equal in size to `J_{h-1}` on the singleton slice.

This is a concrete state-size/horizon Pareto improvement, not just a qualitative compression statement.

---

## 6. Stronger kill test: is L1 necessary at all for B3?

Let `G0(C)` retain only the weighted induced current-frontier graph `L0`, i.e. structurally the same object as `M2` but asked to predict `B3`.

It omits exactly the suspicious correlations:

- shared `L1` future cells between different current candidates;
- new-frontier adjacency after the first action;
- the full successor-R2 identity structure.

No theorem says `G0 -> B3`.

A bounded diagnostic search nevertheless found **no weighted-frontier-graph isomorphism collision** through

```text
FCC N<=7 (12,734 classes at N=7),
HCP N<=6 (4,641 classes at N=6).
```

WL hashing was used only as an isomorphism-invariant bucket filter; any non-singleton bucket would have been checked by exact weighted graph isomorphism. No non-singleton bucket occurred at the stated terminal levels.

This is not proof of sufficiency. It instead creates a new reconstruction frontier: either the weighted native frontier graph determines much more of the embedding than expected, or the first counterexample lies beyond the present atlas / needs deliberate construction.

---

## 7. BRC and hypothesis update

For Boolean operational futures:

```text
same R2bar => safe recoalescence through B2,
same R2bar =/=> safe recoalescence through B3.
```

The FCC CE6 pair additionally has same `T3` but different `B3`, so equality of a three-step terminal answer set is insufficient for branch-conditioned continuation.

Hypothesis dispositions:

- H1: nested-language refinement proved; raw exact-h slogan false.
- H2: strengthened by same-T3/different-B3 witness.
- H3/H4: strengthened from `J_h/K_h` to one-layer-shaved `M_h` for Boolean operational futures.
- H5: R2 correlation hierarchy now exact at B2/B3 boundary, first collision size N=6 in both worlds.
- H6: `COMPACT_R3_EXISTS` positive — `M3=L0 union L1` is exact and strictly smaller than `J3/K3`.
- H7: Boolean surface BRC specialization advanced; multiplicity/provenance matrix pending.
- H8: exact singleton `M_h`/`J_h` storage law gives a concrete Pareto slice.

---

## 8. Validation and next frontier

Focused test file:

```text
Ran 13 tests in 27.350s
OK
```

Additional bounded holdouts:

```text
M2 -> B2: FCC 26 states / HCP 69 states through N<=4: PASS
M3 -> B3: FCC 26 states / HCP 69 states through N<=4: PASS
```

All theorem-critical operations are integer/combinatorial. No CI/workflow status was queried.

Next research order:

1. kill or prove weighted-frontier-only `G0 -> B3`;
2. if killed, isolate the first missing `L0-L1` overlap/shared-future-cell correlation;
3. test pairwise overlap summaries before retaining explicit full `L1`;
4. compare first failure order in FCC/HCP;
5. then complete Boolean/multiplicity/provenance BRC and serialized-size/update-cost Pareto matrices.

Current mother-question answer:

> For the native addition-only Boolean surface world, finite-h future precision admits an exact horizon-indexed behavioral kernel and a recursively executable carrier whose explicit exterior depth is only `h-1`, not `h`. The first proved R2 debt is relational update structure: the R2 bag is exact for B2 but not B3.
