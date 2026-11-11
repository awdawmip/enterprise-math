# R5 — one common four-support transport has all three exact one-atom exits

Date: 2026-11-11 (Asia/Shanghai). Author-side exact constructive lemma; independent review and formal Source Result are pending.

## Frozen scientific model

Continue the pinned seven-likelihood auxiliary P/Q–BRC Blackwell observation fiber with scientific refs GLOBAL `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Current normative rules were read separately. The frozen model is the same as R5 PRs #2076, #2080, #2084 and #2085.

There are seven target labels i=0,...,6, four dynamic source ports j∈{1,2,3,5}, 28 labeled dynamic nonnegative masses x_(i,j), and 15 exact observation equations A x=b (rank 13), plus two fixed singleton arcs. Likelihood integers R=(2,10,15,20,25,30,38). The right-hand side b is reconstructed from the frozen positive reference E0, exactly specified in `VERIFY_COMMON_C_THREE_EXITS.py`. Target/source labels and all 15 observation equations are preserved without port collapse.

Masks at source port 3: A={1,3,4,6}, C={2,3,4,6}, B={2,3,4,5}. A six-arc signed atom H_j(v) places a three-label moment-null vector v on source 3 and -v on source j≠3. Each atom is in ker(A). A valid operation includes its full nonnegative line segment.

## Theorem: complete branching of the C→B one-atom final step, with a *single common starting transport*

Suppose a single nonzero six-arc atom changes positive source-3 mask C to B. It must modify targets 5 and 6; its third target cannot be 0 or 1 (zero at both endpoints), so necessarily it is exactly one of m∈{2,3,4}. This exhausts possible three-target supports for this mask change.

For each of these three possibilities, use source port 5 as compensator and set

`v_m(m)=-8; v_m(5)=38-R[m]; v_m(6)=R[m]-30`.

Then `sum v_m = sum_i R[i]v_m(i)=0` and each v_m has precisely three nonzero entries. The three exact alternatives are

| m | v_m at (m,5,6) | positive coefficient t_m from the common C |
|---|---|---|
| 2 | (-8,+23,-15) | 55429/33975844 |
| 3 | (-8,+18,-10) | 166287/67951688 |
| 4 | (-8,+13,-5) | 166287/33975844 |

All three **start at exactly the same fully labeled 28-component transfer X_C**, satisfy the same 15 observation equations, remain nonnegative on the full segment, and end with source-3 mask B. In particular, the third atom's target triple is not uniquely determined even when the exact starting transfer and compensator port are fixed.

The common C is reachable from an A-mask transfer by **two** exact six-arc operations with ports (1,2), first and second source-3 directions both (-23 at 1,+28 at 2,-5 at 6). The two positive coefficients are

`t1=1544855/475661816`, `t2=5306067/1902647264`.

Thus the same exact two-step history branches into three distinct three-step A→B histories, all with peak source-3 support 5 and compensator sequence (1,2,5).

### Exact common transfer (source-major order: j=1,2,3,5; target i=0,...,6 within each source)

```text
10022571/135903376,74268405/475661816,0,0,0,0,10022571/475661816,
0,122039541/1902647264,196521/67951688,0,0,0,26530335/1902647264,
0,0,11485487/67951688,377644447/2548188300,5499155/67951688,0,831435/33975844,
0,6092151/1902647264,0,0,680265/67951688,2161731/33975844,27135015/1902647264
```

The exact A-mask initial transfer and frozen E0 reference are in the self-contained verifier, not inferred from decimal reconstruction.

## Reusable necessary and sufficient local exit criterion

For an arbitrary *already feasible* C-mask transfer X in the fixed observation fiber and selected m∈{2,3,4}, let c=X_(6,3)>0. A single **source-5-compensated** C→B move along H_5(v_m) exists iff

```text
X_(m,3) > 8 c/(30-R[m])
X_(5,5) >= (38-R[m]) c/(30-R[m]).
```

Its coefficient is **forced** to be `t=c/(30-R[m])` by the requirement that target 6 end at zero. The first strict inequality keeps the common m-arc positive; the second weak inequality guarantees nonnegative compensator mass at target 5. All remaining affected arcs gain nonnegative mass or are unchanged. Therefore the inequalities are necessary and sufficient, and they define exact relatively open polyhedral exit regions of the C-face.

For the displayed single X_C, exact slack pairs (source-3 m, source-5 target 5) are

| m | source-3 slack | source-5 slack |
|---|---|---|
| 2 | 1514089/9707384 | 221716/8493961 |
| 3 | 46822621/364026900 | 166287/8493961 |
| 4 | 405509/9707384 | 0 |

In particular, the three exit regions have a **common** exact feasible point; m=4 lies on the source-5-target-5 boundary, while m=2 and 3 have strictly positive compensator slack. All three terminal transfers are different even though their source-3 positive target mask equals B.

## Proof and verification

The mask-support classification is immediate from the required two changed labels and the third coordinate being zero at both endpoints for targets 0 and 1. The kernel identity follows from the two exact zero moments. The local exit criterion follows by inspecting precisely six modified labeled arcs and the forced coefficient. The existential statements follow by substituting the 28 exact fractions above into the 15 frozen observation rows, the explicit two preparatory moves and the three alternatives; every check is implemented with Python standard-library `fractions.Fraction` in `VERIFY_COMMON_C_THREE_EXITS.py`.

Recorded verification is `EXACT_OUTPUT.txt`, ending `PASS_R5_EXACT_COMMON_C_THREE_BRANCH_ATOMIC_EXITS`. This is a finite, fully exact constructive/structural result within the auxiliary observer, not a native X6 motion claim or physical calibration. The old three-atom minimality result is a dependency, not reproved here.

## Relation to predecessor and next problem

PR #2085 proved compensator-port rigidity only for one **fixed** signed three-atom template whose final target is m=2. The present work changes the final target to m=3 and m=4 and proves an exact **three-way branching from one common predecessor state**; it does not claim the full three-atom port-diversity optimum.

A targeted exploratory LP search over the narrower template family (first two source-3 triples {1,2,k1}, {1,2,k2} with k1,k2∈{3,4,6}, third {m,5,6} with m∈{2,3,4}, each of 27 ordered compensator assignments) tested 567 cases. Six positive solutions were observed, all with k1=k2=6, m∈{2,3,4}, and compensators (1,2,5) or (2,1,5). This is **exploratory numerical screening only**; no exhaustive rational infeasibility certificate is claimed for the other 561 cases.

Next: build exact certificates for the 561 screened cases or find a counterexample outside this restricted first-two-triples family; ultimately determine whether an arbitrary three-atom A→B path can use at most two different compensator ports. Retain the full labeled observer and endpoint positivity, and separate signed target-template coverage from source-port feasibility.
