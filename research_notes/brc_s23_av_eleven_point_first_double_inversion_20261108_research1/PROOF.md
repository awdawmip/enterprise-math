# Exact first doubled-q2 inversion: eleven-point cascade at H=9,821,296

Date: 2026-11-08. Status: author-side proof, exact arithmetic checker executed, independent review pending.
Scientific freeze: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Immediate predecessor: exact third-window proof at `f7270feef39c905792a1e10a8c612fa72dcfaa86`, `research_notes/brc_s23_av_six_point_interleaving_window_20261108_research1/`.
S23/AV joint-count (1,4) two-point auxiliary observer with label-3 padding; same population and readout.

## Theorem

Use `S_H={(v,j) in Z>=0^2:v+j<=H}`, `theta(v,j)=rv-j`, `r=ln7/ln(10/7)`. Define
```
u=(79,431), |u|_1=510; w=(380295,2074774), M=|w|_1=2455069,
q2=u+2w, q3=u+3w, q4=u+4w,
H0=|q2|_1=4910648, H1=|q3|_1=7365717, H2=|q4|_1=9820786,
H3=2|q2|_1=9821296.
L(v,j)=(2074774v-380295j,-v), lexicographic.
epsilon=theta(u)>0, eta=-theta(w)>0, 3eta/2<epsilon<2eta.
T(n)=(n+1)(n+2)/2, n>=0.
```
At the **exact single horizon `H=H3=9,821,296`**, the increasing true-threshold order of `S_H` is obtained from the old integer `L` order by the following pairwise-disjoint finite local operations.

**One eleven-point merge.** Eleven consecutive lexicographic entries
```
[2w,w,0,q4,q3,q2,u+w,u,2q2,2u+3w,2u+2w]
```
are replaced by the exact increasing true-order entries
```
[q4,2w,q3,w,2q2,q2,0,2u+3w,u+w,2u+2w,u].
```
This merges the two overlapping six-point blocks whose starting points are `0` and `u` and adds the newly feasible `2q2` inverted comparison. The merged block contains **13** inverted point pairs.

**Remaining disjoint operations.** For every `x in S_510 \ {0,u}`, apply the six-point interleaving of the predecessor theorem. For each `y in S_(M+510) \ (S_510 union (w+S_510))`, apply its four-point rotation. For each `a in S_(2M+510) \ (S_(M+510) union (w+S_(M+510)))`, apply its isolated `q2` adjacent swap. All other entries are unchanged.

The exact counts are
```
eleven-point blocks = 1,
six-point blocks = T(510)-2 = 130814,
four-point blocks = T(M+510)-2T(510) = 3014937534358,
isolated swaps = M^2 = 6027363794761,
total inverted point pairs = T(2M+510)+T(M+510)+T(510)+1
                           = 15072177182732.
```
Thus a preexisting exact floor-sum rank/select oracle for `L` gains the correct true order at `H3` by one eleven-element lookup and a constant number of integer triangle-membership tests, including the earlier six/four/pair maps.

## Proof

**1. All inverted differences.** Since `det(u,w)=1`, a displacement `d=A*u+B*w` has first integer key difference `A` and true threshold difference `Aepsilon-Beta`. After reversing endpoints take `A>0`. If `B<=1` signs agree. For `B>=2`, the nonnegative coordinate sum is `510A+MB<=H3=4M+1020`, hence `B<=4`. By `3eta/2<epsilon<2eta`, the only pairs `(A,B)` producing negative true sign are `(1,2),(1,3),(1,4),(2,4)`; `(2,4)` is newly feasible only at `H3`. The exact rational verifier independently checks this bounded classification. The first three classes translate by `q2,q3,q4`, and the last by `2q2` starting only at the origin.

**2. Eleven consecutive lex slots.** In the `K=0` fiber the last three points are `2w,w,0`; the `K=1` fiber consists precisely of `q4,q3,q2,u+w,u` (as `u-w` and `u+5w` are infeasible); the first three points of `K=2` fiber are `2q2,2u+3w,2u+2w`. The three successive keys are consecutive integers, hence all eleven old entries are consecutive. Relative to `theta(0)`, their true increments, when reordered as asserted, are
```
epsilon-4eta < -2eta < epsilon-3eta < -eta
< 2epsilon-4eta < epsilon-2eta < 0
< 2epsilon-3eta < epsilon-eta < 2epsilon-2eta < epsilon.
```
Every strict inequality follows from `3eta/2<epsilon<2eta`. Counting the inversions of the displayed finite permutation gives 13, exactly the six `q2`, four `q3`, two `q4` and one `2q2` comparisons.

**3. Complete partition of all remaining corrections.** At `H3`, the six-point block starting set is `S_510`. The offset sets of two such blocks can intersect only if their starts differ by the smallest positive lattice displacement `u`: differences involving `w` have coordinate sum at least `M>510`, and relevant cross-key positive differences other than `u` have even larger sum. With nonnegative starts in `S_510`, `x+u in S_510` holds exactly when `x=0`. Thus the **only** overlapping six-block starts are `0,u`; their union has eleven distinct points, and the new `2q2` inverted pair belongs to it. All other six-blocks are disjoint. The extremal neighboring-fiber argument from the predecessor theorem applies verbatim to four-block starts outside `S_510 union (w+S_510)` and to isolated swaps outside `S_(M+510) union (w+S_(M+510))`. These sets are disjoint from one another and the merged block. Every inverted comparison listed in step 1 lies in exactly one such operation; no additional inverted comparison exists.

**4. Counts and certificate.** Set differences in step 3 have sizes `T(510)-2`, `T(M+510)-2T(510)` and `T(2M+510)-2T(M+510)+T(510)=M^2`. Each block contributes respectively 13, 6, 3 or 1 inversions, giving the total formula. Complete exact scaled-model sorting tests and strict rational endpoint checks in `VERIFY_ONSET.py` corroborate these algebraic steps. QED.

## Evidence and next unit

`VERIFY_ONSET.py` uses only Python 3 standard-library exact fractions. It constructs rigorous logarithm bounds, verifies the complete feasible inversion-class list at H3, exhaustively compares the entire small scaled model at H=24 (325 thresholds) and a second model H=48 (1225 thresholds), then checks giant-H eleven-point inequalities and all counting formulas. Its actual stdout is in `RUN_EVIDENCE.txt`.

The P000/ACTIVE X6 worldview, frozen S23/AV science and joint relation observer preservation remain as selected. This is an exact auxiliary threshold **ordering** theorem. Independent units: global prefix occupancy at H=2455579, and the next threshold ordering horizon H=9821297 (multiple translated double-q2 pairs). Formal owner/CLAIM and independent mathematical review remain Source-controlled.
