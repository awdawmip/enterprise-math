# Exact translated eleven-point interleaving window after the first doubled-q2 inversion

Date: 2026-11-08. Status: author-side exact mathematical proof with executed finite-model tests; independent review pending.
Frozen scientific source: `awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Parent: PR #1777, `research_notes/brc_s23_av_eleven_point_first_double_inversion_20261108_research1/PROOF.md` at the PR head read on 2026-11-08.
Object: two-point S23/AV auxiliary likelihood-sign observer, joint (1,4) count carrier retained with label-3 padding.

## Definitions
Let `S_h={(v,j) in Z^2_{≥0}:v+j<=h}`, `theta(v,j)=rv-j`, `r=ln(7)/ln(10/7)`. Put
```text
u=(79,431); d=|u|_1=510
w=(380295,2074774); M=|w|_1=2455069
q2=u+2w; q3=u+3w; q4=u+4w
H0=d+2M=4910648; H1=d+3M=7365717
H2=d+4M=9820786; H3=2d+4M=9821296
L(v,j)=(2074774v-380295j,-v) (lexicographic order)
epsilon=79r-431; eta=2074774-380295r
T(n)=(n+1)(n+2)/2 (n>=0)
```
The rigorous rational enclosure used in the predecessor establishes `3eta/2<epsilon<2eta`. In particular all threshold values are distinct.

## Theorem (510 consecutive horizons)

For every integer **9821296 <= H <= 9821805**, let `a=H-H3` and `z=d+a`, so `0<=a<d=510` and `z<M`. Let `t=M+z`, `s=2M+z`. The exact increasing-theta order of all points in `S_H` is obtained from the old integer-key L order by the following **mutually disjoint** local permutations:

1. **Eleven-point translated cascade**, for each `x in S_a`. In the 11 consecutive L positions
```text
[x+2w, x+w, x, x+q4, x+q3, x+q2,
 x+u+w, x+u, x+2q2, x+2u+3w, x+2u+2w]
```
place, respectively, the following exact true-order values:
```text
[x+q4, x+2w, x+q3, x+w, x+2q2, x+q2,
 x, x+2u+3w, x+u+w, x+2u+2w, x+u].
```
2. **Remaining six-point interleavings**, for `x in S_z \ (S_a union (u+S_a))`, by
```text
[x+2w,x+w,x,x+q4,x+q3,x+q2]
 -> [x+q4,x+2w,x+q3,x+w,x+q2,x].
```
3. **Remaining four-point rotations**, for `y in S_t \ (S_z union (w+S_z))`, by
```text
[y+w,y,y+q3,y+q2] -> [y+q3,y+w,y+q2,y].
```
4. **Remaining isolated adjacent swaps**, for `b in S_s \ (S_t union (w+S_t))`, by
```text
[b,b+q2] -> [b+q2,b].
```
Every other threshold keeps its L position. An existing exact floor-sum rank/select query for L can be corrected with O(1) local triangle-membership tests and a finite 11-element lookup, independent of `|S_H|`.

The numbers of local operations and total inverted point pairs are exactly:
```text
eleven blocks = T(a)
six blocks    = T(z)-2T(a)
four blocks   = T(M+z)-2T(z)
pair swaps    = M^2 = 6027363794761
inverted pairs = T(2M+z)+T(M+z)+T(z)+T(a)
```
This block decomposition is sharp at the right boundary: at `H=H3+d=9821806`, the translated eleven blocks indexed by `x=0` and `x=u` overlap; the disjoint eleven-block rule requires a further merger.

## Proof

**1. Exhaustive inverted-displacement classification.** Because `det(u,w)=1`, every integer displacement is uniquely `A*u+B*w`. The first integer key changes by `A`, while true theta changes by `A*epsilon-B*eta`. Reverse endpoints so `A>0`. For `B<=1` signs agree, whereas for `B>=2` the displacement has nonnegative coordinates and requires `d*A+M*B<=H<=H3+d-1`. Consequently `B<=4`; if `B=4` then `A<=2`. Since `3eta/2<epsilon<2eta`, the **only** reversed displacement types are `(A,B)=(1,2),(1,3),(1,4),(2,4)`. Their translates start respectively in `S_s,S_t,S_z,S_a`. All other comparisons are correctly ordered by L (including first-key ties, ordered by -v).

**2. All eleven positions are consecutive.** For `x in S_a`, `|x|_1<=a<d<<M`. The last three entries of the L fiber of key `K(x)` are `x+2w,x+w,x` because `x-w` is infeasible. The whole next fiber of key `K(x)+1` consists of `x+q4,x+q3,x+q2,x+u+w,x+u`: neither `x+u-w` nor `x+u+5w` is feasible in the current window. The first three entries of key `K(x)+2` are `x+2q2,x+2u+3w,x+2u+2w`; `x+2u+5w` is infeasible. These three integer keys are consecutive, so the displayed 11 positions are consecutive. Their true theta order follows from
```text
epsilon-4eta < -2eta < epsilon-3eta < -eta
< 2epsilon-4eta < epsilon-2eta < 0
< 2epsilon-3eta < epsilon-eta < 2epsilon-2eta < epsilon.
```
One eleven block contains exactly 13 inversions: the 12 q2/q3/q4 inversions of two overlapping six-blocks plus the new doubled-q2 inversion.

**3. Disjointness.** Six-point starts form `S_z=S_(d+a)`, with `d<=z<2d` and `z<M`. Distinct six-blocks can intersect only if their starts differ by `u` (the only positive adjacent-key displacement fitting in `S_z-S_z`); this happens exactly for starts `x` and `x+u` with `x in S_a`. Hence these pairs assemble into `T(a)` pairwise disjoint eleven blocks. Removing `S_a union (u+S_a)` leaves disjoint six blocks. The same extremal-fiber argument from the predecessor gives the four-block and isolated-pair start sets in the theorem; all their positions are disjoint from the eleven/six blocks and one another. Every reversed comparison in step 1 belongs to exactly one listed block, hence the resulting sequence agrees with every pairwise true comparison.

**4. Counts.** There are `T(a)` eleven-block starts, and `T(z)-2T(a)` remaining six starts. As `z<M`, the sets `S_z` and `w+S_z` are disjoint, giving `T(M+z)-2T(z)` four blocks. The q2-start set has size `T(2M+z)`; after removing covered starts, the remaining isolated pairs number `T(2M+z)-2T(M+z)+T(z)=M^2`. A six/four/pair block contributes respectively 6/3/1 inverted pairs, an eleven block contributes 13. Thus the total is
```text
13T(a)+6(T(z)-2T(a))+3(T(M+z)-2T(z))+M^2
 = T(2M+z)+T(M+z)+T(z)+T(a),
```
the exact sum of inversions of all four displacement classes. QED.

## Independent executable checks and limits

`VERIFY.py` uses `fractions.Fraction` and the 45-term atanh rational enclosure for r; it checks the complete large-integer displacement classification, the endpoint operation/inversion counts, and **exhaustively compares the entire corrected order** against exact rational true sorting in three scaled unimodular models, for every horizon in each scaled window. The second model has `u=(2,1),w=(5,3),r=61/105`; choosing `M>2d` preserves the structural gap to the next positive displacement. `RUN_EVIDENCE.txt` records actual stdout and SHA-256 digests.

This is a fully stated auxiliary threshold-order theorem. It preserves the joint (1,4) relation and the label-3 padding; the S23 six-source/ten-label mother observation mapping, observer capacity `N(H)`, native X6 geometry and formal Result/Review acceptance remain separate tasks.

## Next
At `H=9821806`, analyze the first overlap of translated eleven-blocks and derive the next finite merger/rank correction. In parallel, complete the global changed-gap occupancy at `H=2455579`, independently of the threshold-ordering result.