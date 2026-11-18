# S23/AV: 20 further exact capacity plateaux, indices 201–220

Date: 2026-11-08 (Asia/Shanghai). Status: **author-side exact-rational finite proof certificate**, pending independent review and any formal task admission. Scientific input is frozen at `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`. This is the two-point S23/AV joint-count auxiliary observer, not a six-source native observation bridge.

## Statement

In the frozen iid experiment with one-step laws `P0=(1/2,1/4,1/4)` and `P1=(5/7,1/4,1/28)` on labels (1,3,4), retain joint counts of labels 1 and 4 with neutral label-3 padding. Let `T_h={10^j/7^s:0<=j<=s<=h}`. Define `N(h)` as the minimum common padded observation length for which an attainable prefix score falls in **every open threshold cell**, including the two exterior cells.

Let `r=log(7)/log(10/7)`, `epsilon=79r-431`, `d=2074774-380295r`, and
`a_i=floor(i*d/epsilon)`,
`V_i=380295*i+79*a_i`,
`K_i=2074774*i+431*a_i`,
`H_i=V_i+510`,
`M_i=K_i+V_i-(V_(i-1)+1)`.

**For every integer i with 201 <= i <= 220, and every integer h with V_(i-1)+511 <= h <= V_i+510,**

```
N(h)=M_i.
```

In particular, for all **7,606,769 consecutive integer horizons** `76,068,754 <= h <= 83,675,522`, the staircase is determined exactly by the 20 rows below. Its twentieth new interval is `83,295,228 <= h <= 83,675,522` and has `N(h)=456,885,742`. The first new interval has `N(h)=417,460,295`. The union connects immediately to the previously certified i=200 endpoint `h=76,068,753`.

## Complete finite index certificate

| i | H_i | M_i | Narrow directions | Complete critical cells |
|---:|---:|---:|---:|---:|
| 201 | 76449048 | 417460295 | 62 | 19615 |
| 202 | 76829422 | 419535579 | 62 | 19780 |
| 203 | 77209717 | 421610274 | 62 | 19950 |
| 204 | 77590091 | 423685558 | 62 | 20120 |
| 205 | 77970465 | 425760763 | 62 | 20290 |
| 206 | 78350760 | 427835458 | 62 | 20460 |
| 207 | 78731134 | 429910742 | 64 | 20820 |
| 208 | 79111429 | 431985437 | 64 | 20991 |
| 209 | 79491803 | 434060721 | 64 | 21165 |
| 210 | 79872098 | 436135416 | 64 | 21339 |
| 211 | 80252472 | 438210700 | 64 | 21513 |
| 212 | 80632846 | 440285905 | 64 | 21687 |
| 213 | 81013141 | 442360600 | 64 | 21862 |
| 214 | 81393515 | 444435884 | 66 | 22238 |
| 215 | 81773810 | 446510579 | 66 | 22416 |
| 216 | 82154184 | 448585863 | 66 | 22594 |
| 217 | 82534558 | 450661068 | 66 | 22772 |
| 218 | 82914853 | 452735763 | 66 | 22950 |
| 219 | 83295227 | 454811047 | 66 | 23130 |
| 220 | 83675522 | 456885742 | 68 | 23517 |

Every row is independently executed by `VERIFY_201_220.py` using the exact `check(i)` from the earlier same-branch `research_notes/brc_s23_av_plateau20_20261108_r1/VERIFY_PLATEAUX20_200.py`, whose baseline Git blob is `261d7e22da0e62d667009cb50acfe77ac4e35c3f` at commit `19730a65ae527ed19cda441ccc0ed31b9d6f2639`.

## Proof

The preceding theorem `research_notes/brc_s23_av_scaled_gap_sturmian_jumps_20261108_research1/PROOF.md` at immutable commit `85b53d06d6ba775e516c566c1d79828b6ca9bb1f` gives the **exact lower bound** `N(V_(i-1)+511)>=M_i` for each integer i. We reuse that proven result with its original domain and frozen inputs.

For the **upper bound**, fix each one of the twenty indices separately and set `H=H_i,M=M_i`. The finite symbolic certificate from `PLATEAUX20_200.md`, `VERIFY_PLATEAUX20_200.py` is valid for any particular integer i satisfying all its asserted preconditions: it first proves a strict `10^-26` enclosure for the logarithm ratio by 45-term rational atanh series with rigorous remainder. Its `enc(A,B)` transforms any integer affine form of r to adverse rigorous integer lower/upper bounds.

With the unimodular basis `U=(79,431), W=(11,60)`, every possible outgoing threshold displacement having width in `(0,epsilon)` is classified by a bounded nonzero coefficient `b` from the exact estimate `|b|<epsilon*(H+79)`. For each `b`, the `(a,b)` strip has at most one admissible integer a; the checker tests it and verifies triangle embeddability and width-order comparisons by exact integer bounds. The maximum actually embeddable narrow-direction count across these twenty endpoints is 68; no unenumerated b remains in the asserted finite bound.

For every translated witness `(K_s,V_s)`, `s=1,...,i`, the checker proves `0<K_s-rV_s<epsilon`. It partitions all integer left endpoints `(v,j)` in the main region `0<=v<=V_i, j>=0, v+j<=H` at the exact cuts for `v<=V_s`, `j<=K_s`, `v+j>=K_s+V_s-M` and for all narrow-displacement feasibility predicates. Each resulting critical cell is a product of integer intervals for `v,j,z=v+j`. A cell is nonempty **if and only if** `max(v_lo+j_lo,z_lo)<=min(v_hi+j_hi,z_hi)`; the checker inspects every such feasible cell and verifies at least one strictly inside-cell translated prefix of length <=M. The largest such complete finite collection in this batch has 23,517 cells (index 220), and **none are uncovered**.

For the remaining top 510 rows, the predecessor's exact `gamma=eta-epsilon` gap lemma supplies the short translated witness `(K_i+371+431m,V_i+68+79m)` for an admissible `m in {1,...,6}`; `VERIFY_PLATEAUX20_200.py` tests all six offsets with strict integer inequalities and the budget bound. Both exterior unbounded cells are checked by explicit prefixes using the rigorous floor bounds of `H/r` and `rH`. Thus `N(H_i)<=M_i` for each checked i. By nesting of threshold sets and monotonicity of N(h), the lower bound at the start and upper bound at the end establish the equality for each full integer interval.

The program output `RUN_EVIDENCE.txt` records each i and the finite coverage statistics; it finishes with `PASS_S23_AV_PLATEAUX_201_TO_220`. Actual validation re-used a locally reproduced, semantically identical copy of the previous `check(i)` implementation; the published wrapper calls the exact upstream repository file at runtime. This pins the dependency rather than duplicating its underlying code.

## Scope and open work

This is a finite 20-index exact-rational certificate under the previously established soundness lemma and lower-bound theorem; no untested i is inferred. The result is an author-side mathematical proof in Draft PR #1777. Native Heartbeat/X6 P000 ontology is preserved as project assumptions, and no auxiliary-to-native transfer is inferred.

Next: test i=221 onward, identify first uncovered critical cell if any and classify its exact integer v/j/(v+j) range and blocking displacements; alternatively study a uniform-in-i proof of this finite partition mechanism with bit-cost and source-bridge accounting.
