# R5: an open triangle of fixed C→B endpoint pairs requiring exactly three BRC atoms

Date: 2026-11-11 (Asia/Shanghai). Evidence tier: author-side exact rational theorem + reproducible finite cut checker; independent Source Result/Review pending.

## Frozen observer, predecessor, and research question

Scientific pins unchanged: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. The P/Q–BRC Blackwell auxiliary observer has target indices `i=0,...,6`, dynamic source ports `j in {1,2,3,5}`, 28 nonnegative variable masses, two fixed singleton arcs, likelihood integers `R=(2,10,15,20,25,30,38)`, and an exact rank-13 dynamic linear observation matrix of 15 rows. All work is in one frozen fiber `F={x>=0:Ax=b}`.

Source-3 support masks are `C={2,3,4,6}` and `B={2,3,4,5}`. A primitive six-arc BRC atom on source 3 and compensator source `j in {1,2,5}` is `H_j(v)`, where `v` has exactly three target entries and `sum(v)=sum(R_i*v_i)=0`; the source-3 part is `v`, the compensator part `-v`.

Exact predecessor: [R5 common C triple exits](https://github.com/awdawmip/enterprise-math/blob/b69383e8665eb0fa71041356b63191661f5d7392/research_notes/brc_r5_common_c_three_exits_20261111/RESEARCH.md) and [robust interior witness](https://github.com/awdawmip/enterprise-math/blob/7d15d533afd60df2fd48382eb397b38ca32cf48e/research_notes/brc_r5_robust_triple_exit_interior_20261111/RESEARCH.md), especially the exact `Z` and its three one-atom terminal states `Y_2,Y_3,Y_4` on the interior of the B-face. This paper adds an **endpoint-specific** minimum atomic-distance theorem, distinct from the earlier A→B face-to-face distance of three.

## Main theorem: relatively open two-simplex with exact distance three

Let `Z in relint(F_C)` be the exact rational interior point constructed in predecessor PR #2091; let `c=Z_(6,3)>0`. For `m in {2,3,4}` define a source-3 atom vector
```
v_m(m)=-8,    v_m(5)=38-R[m],    v_m(6)=R[m]-30,
v_m(other targets)=0;
t_m=c/(30-R[m]) > 0.
```
Take all three atoms compensated on source 5 and set `Y_m=Z+t_m H_5(v_m)`. The predecessor's exact positive witness gives `Y_m in relint(F_B)` for every `m`.

For nonnegative barycentric weights `lambda=(lambda_2,lambda_3,lambda_4)` with sum one, define `Y(lambda)=sum_m lambda_m Y_m`.

**Theorem.** The three points `Y_2,Y_3,Y_4` are affinely independent, so they span a genuine two-simplex inside `relint(F_B)`. Every `Y(lambda)` can be reached from the *same fixed* `Z` by at most three legal six-arc BRC operations with `peak_source3<=5`. Moreover, throughout the nonempty relative-open weight region
```
lambda_2+lambda_3+lambda_4=1,
lambda_m>0,
max_m abs(lambda_m-1/3)<1/6,
```
the endpoint-specific atomic distance is **exactly three**, even if the two hypothetical operations were permitted to choose arbitrary compensator ports and target triples. In particular, the equal-weight endpoint `Y_bar=(Y_2+Y_3+Y_4)/3` has atomic distance exactly three from `Z`.

### Constructive upper bound

Run the three operations `lambda_m*t_m H_5(v_m)` in any order, for `m=2,3,4`. All losses occur on source-3 target `m`, source-3 target 6 and source-5 target 5, and are monotone; all increases are monotone. Since the final state is the positive convex combination of `Y_m`, every intermediate state is nonnegative and preserves `Ax=b`. The source-3 support on the open segments is contained in `{2,3,4,5,6}`, hence the peak is five. The terminal positive mask is exactly B; every terminal allowed arc is positive by convexity of the three predecessor interior witnesses. The three vertices are affinely independent because the target-`m` component of `Y_m-Z` is nonzero for its own `m` and zero for the other two.

For `lambda=(1/3,1/3,1/3)`, the normalized source-3 difference is the exact rational vector (target labels 0 through 6):
```
(Y_bar - Z)_(i,3) / c = (0, 0, -8/45, -4/15, -8/15, 89/45, -1).
```
It has five strictly nonzero target components at `S={2,3,4,5,6}`.

### Exact universal two-atom obstruction by a 30-cut classification

An atom on any compensator port projects on source 3 to one three-target null vector for both `sum` and `R`-weighted moment. Since all seven `R_i` differ, a nonzero such vector has three **nonzero** entries.

If the five-target difference `d` were a sum of at most two such atom vectors, their two three-target supports must have union exactly `S`, hence intersect at precisely one shared target `r in S`; the four remaining targets partition into two unique pairs. (A disjoint six-target union would have an uncancelled nonzero target outside S; a smaller union cannot cover S.) If `p,q` are the two targets unique to one atom, the moment-null condition forces the necessary **pair cut**
```
d_p*(R[p]-R[r]) + d_q*(R[q]-R[r]) = 0.
```
Using `D_i=45*d_i/c`, the nonzero integer values at the barycenter, grouped by shared target `r` and all six choices of `{p,q} subset S\{r}`, are:
```
r=2: -300, 1275,-1095, 1095,-1275, 300
r=3:  -80,  930, -770,  770, -930,  80
r=4:  140,  525, -505,  505, -525,-140
r=5:  240,  240, -240,  240, -240,-240
r=6:  400,  496, -528,  528, -496,-400
```
Thus all `5*binom(4,2)=30` necessary cuts are nonzero. This excludes *every* two-atom decomposition, with no reference to a particular compensator, atom ordering, intermediate supports or nonnegativity relaxation. Combined with the three-step construction, the exact minimum is three.

### Quantitative relative-open persistence of the obstruction

For general barycentric weights the source-3 delta `d(lambda)/c` is linear in `lambda`. Each of the 30 pair-cut expressions is a linear form `L(lambda)=sum_m a_m*lambda_m`. Direct exact-rational evaluation of those coefficients yields
```
min_over_30 [abs(L(1/3,1/3,1/3)) / sum_m abs(a_m)] = 1/6.
```
By the triangle inequality, if `max_m abs(lambda_m-1/3)<1/6`, then every `L(lambda)` stays nonzero. Those weights are strictly positive. Consequently a full relative-open 2D neighborhood of the equal-weight point has exact endpoint-specific distance three.

## Verification and limits

`VERIFY.py` reconstructs the predecessor's exact `Z` from its rational `C`, a six-arc repair, the 13-pivot positive C-face witness and a rational convex combination; checks the 15 exact observation equalities and each intermediate transfer; derives the rational barycenter vector; exhausts all 30 pair cuts and verifies the uniform radius `1/6`. `EXACT_OUTPUT.txt` stores an actual Python `fractions.Fraction` run. Finite completeness follows from the five-nonzero-support argument above. The theorem concerns the frozen **auxiliary positive-mass observation fiber** and uses BRC atoms with labeled branches and signed move directions, not a new native Heartbeat/X6 physical evolution claim.

## Stronger result: exact distance on the entire closed two-simplex

The preceding open-region theorem admits a **complete extension**. In fact, for every set of barycentric weights `lambda_2,lambda_3,lambda_4 >=0` summing to one, the exact minimal number of allowed six-arc BRC atoms between the fixed `Z` and `Y(lambda)` is

| Barycentric stratum | Minimum number of atoms |
| --- | ---: |
| Three vertices (one weight equals 1) | **1** |
| Any open edge (exactly two weights positive) | **2** |
| Strict interior with `lambda_2=3*lambda_4` | **2** |
| All other strict interior points | **3** |

All upper-bound constructions stay in the original frozen fiber, use only compensator source 5, and keep `peak_source3 <=5`; all lower bounds allow any compensator and intermediate supports.

### Why there is exactly one exceptional interior line

The five-support obstruction proof above provides 30 exact pair-cut affine linear forms in the three weights. A nonzero linear form `L(lambda)=a_2*lambda_2+a_3*lambda_3+a_4*lambda_4` can vanish for **strictly positive** weights iff its coefficients have both positive and negative signs. Exhaustive exact sign classification of all 30 necessary cuts yields just two such cases:

```
shared target r=3, unique pair {2,4}:
    (a_2,a_3,a_4)=(8/3,0,-8)
shared target r=3, complementary unique pair {5,6}:
    (a_2,a_3,a_4)=(-8/3,0,8)
```

Both define precisely `lambda_2=3*lambda_4`. Every other cut retains a strict sign throughout the barycentric interior and therefore cannot vanish there. Because the pair-cut is also **sufficient for a two-triple source-3 algebraic decomposition** (subtract its three-target moment-null component; the remainder is the complementary moment-null triple), this is the unique possible interior two-atom locus at the source-3 level. We now show actual **nonnegative full-fiber realization** on this line.

### Explicit exact two-atom bridge for the exceptional line

Write `lambda=(3s,1-4s,s)` with `0<s<1/4`. First use the already verified one-atom exit at vertex `lambda=(0,1,0)`:

```
Z -> P = Y_3 = Z + (c/5)*H_5({3:-4,5:+9,6:-5})
```

The exact prior witness and current checker establish that `P` lies in the relative interior of the B-face, with all 25 allowed dynamic arcs strictly positive. The remaining difference factorizes as

```
Y(3s,1-4s,s)-P
   = (8*c*s/5)*H_5({2:-1,3:+2,4:-1}).
```

This is an identity affine in `s`, checked algebraically at the two rational endpoints `s=0` and `s=1/4` in the checker, so it holds identically for all `0<=s<=1/4`. The terminal state is a convex combination of the three interior B-face endpoints and is therefore nonnegative and strictly positive on allowed B arcs. The segment from `P` to this terminal is nonnegative by convexity, and its source-3 support stays B (four positive targets). The first segment has peak five. Thus exactly two atoms suffice on this exceptional line. One atom is impossible there because all five components `{2,3,4,5,6}` of the source-3 delta are nonzero.

At each triangle vertex, its predecessor defining atom yields the upper bound of one and the endpoint differs from Z, giving equality. On an open edge the delta has four nonzero source-3 targets (the two selected m-labels plus 5 and 6), excluding one atom, while the two selected defining atoms provide a legal path. In the strict interior away from `lambda_2=3*lambda_4`, all 30 pair cuts are nonzero, so the existing three-step path is optimal.

This proves a complete exact **one / two / three** endpoint-distance stratification of the two-dimensional simplex. Notably, the one-atom distance between the two *faces* coexists with an open family of fixed C-interior to B-interior endpoint pairs at distance three.

## Validation and next question

The updated `VERIFY.py` now checks the classification of 30 affine cut signs, uniquely identifies the two complementary `r=3` cases, reconstructs the exceptional-line first endpoint `P` in the relative interior of B, and verifies the exact affine two-atom identity at `s=0,1/4` plus additional rational interior tests. `EXACT_OUTPUT.txt` records an actual standard-library `Fraction` execution, including `PASS_R5_EXACT_COMPLETE_C_TO_B_SIMPLEX_DISTANCE_STRATIFICATION`.

Next, classify endpoint-specific distances for **arbitrary** pairs `(X,Y)` in the full 12D `C/B` faces (not only this two-simplex from Z), and separately resolve the unrestricted three-atom A→B compensator-port diversity question. The present result preserves the frozen P/Q–BRC science and does not claim a native X6 dynamics theorem.

Provenance: author-side mathematical contribution only. No prior task CLAIM is displaced and formal Source Result plus independent review remain pending.
