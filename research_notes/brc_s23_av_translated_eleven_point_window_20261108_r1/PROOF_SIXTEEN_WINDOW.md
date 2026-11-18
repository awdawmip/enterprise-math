# S23/AV: exact translated sixteen-point ordering for 510 consecutive horizons

Date: 2026-11-08. Author-side exact mathematical proof, verification and independent review status as in parent PR #1777. Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Immediate predecessor: `PROOF.md` (translated eleven-point window) and `FIRST_OVERLAP_H9821806.md` (first sixteen-point block).

## Theorem

Put `u=(79,431)`, `d=|u|_1=510`, `w=(380295,2074774)`, `M=|w|_1=2455069`, `q_b=u+b*w`, `H3=2|q2|_1=9821296`, `T(h)=(h+1)(h+2)/2`; let `S_h={(v,j) in Z_{≥0}^2:v+j<=h}`, `theta(v,j)=rv-j`, `r=ln7/ln(10/7)`. The old integer readout is `L(v,j)=(2074774v-380295j,-v)` in lex order.

For **each integer 9,821,806 <= H <= 9,822,315**, set `a=H-H3`, `510<=a<=1019`, `z=d+a`, `t=M+z`, `s=2M+z`. The true increasing-theta ordering of `S_H` is the disjoint concatenation of these corrections to old integer-key order:

1. For each `x in S_(a-d)`, replace the following 16 consecutive old entries:
```text
[x+2w,x+w,x, x+q4,x+q3,x+q2,x+u+w,x+u,
 x+2q2,x+2u+3w,x+2u+2w,x+2u+w,x+2u,
 x+3u+4w,x+3u+3w,x+3u+2w]
```
by their exact true order using zero-based old indices
```text
[3,0,4,1,8,5,2,9,6,13,10,7,14,11,15,12].
```
Each 16-point correction contains 20 inverted point pairs.
2. For `x in S_a \ (S_(a-d) union (u+S_(a-d)))`, apply the parent eleven-point correction (`13` inversions).
3. For `x in S_z \ (S_a union (u+S_a))`, apply the parent six-point correction (`6` inversions).
4. For `y in S_t \ (S_z union (w+S_z))`, apply the parent four-point correction (`3` inversions).
5. For `b in S_s \ (S_t union (w+S_t))`, swap `[b,b+q2]` (`1` inversion).

All corrections are mutually disjoint, include every true inversion and induce the full correct strict ordering. Their exact operation counts are
```text
16 blocks = T(a-d)
11 blocks = T(a)-2T(a-d)
 6 blocks = T(z)-2T(a)+T(a-d)
 4 blocks = T(M+z)-2T(z)
 2 swaps  = M^2 = 6027363794761
```
and total inverted pairs are
```text
T(2M+z)+T(M+z)+T(z)+T(a).
```
Thus the existing floor-sum integer-key rank/select oracle has an O(1) (bounded, 16-entry) correction for every H in this finite window. At `H=9822315` the counts are `130305,260100,260100,3017438209270,6027363794761` in order above, giving `15079685970571` inverted pairs.

The window is sharp for this **disjoint sixteen-point** construction: at `H=H3+2d=9,822,316`, two 16-point blocks indexed by `0` and `u` intersect and require a larger merged component.

## Proof

The unimodular identity `det(u,w)=1` means a displacement has unique form `A*u+B*w`; its old first-key difference is `A`, its true difference `A*epsilon-B*eta` with `epsilon=79r-431`, `eta=2074774-380295r`. The exact rational logarithm enclosure establishes `3eta/2<epsilon<2eta`. Since `H<=H3+2d-1=4M+4d-1<5M+d` and `H<4M+5d`, no fifth-w displacement and no new inverted A=3,B=4 comparison occur. The complete inverted displacement types remain `(A,B)=(1,2),(1,3),(1,4),(2,4)`; their translation starts are respectively `S_s,S_t,S_z,S_a`.

For `x in S_(a-d)`, exactly three six-block starts `x,x+u,x+2u` are feasible. Since `d<=a<2d`, there is no longer chain, and different three-start chains cannot intersect (distinct chain bases in `S_(a-d)` differ in coordinate sum by less than d). The L fibers of keys `K(x),K(x)+1,K(x)+2,K(x)+3` supply consecutive blocks of sizes `3,5,5,3`; the neighboring extreme predecessor/successors are excluded by nonnegative coordinates or the H budget, because `d+a<=3d-1<<M`. The displayed sixteen offsets are precisely these consecutive positions. Sorting their affine values `Aepsilon-Beta` for `3/2<epsilon/eta<2` gives the stated fixed 16-index permutation, with 20 inversions (nine q2, six q3, three q4, two 2q2).

The remaining two-start chains of six blocks are indexed by `S_a\(S_(a-d) union (u+S_(a-d)))`, producing eleven-blocks. All other six-block starts in `S_z` are isolated. This follows from the exact overlap criterion: two six-point blocks share a lex position precisely when their starts differ by `u`; `S_z` has `z<3d<M`, so no longer nontrivial multiple-w difference fits. As in the preceding fiber proof, the remaining q3 comparisons form four-point blocks with starts `S_t\(S_z union (w+S_z))`, and the remaining q2 comparisons form isolated swaps with starts `S_s\(S_t union (w+S_t))`. All classes are disjoint and exhaust every inversion.

Because the start sets `S_(a-d)` and `u+S_(a-d)` are disjoint, the first two counts follow by subtraction. The six start family subtracts `S_a union (u+S_a)`, whose intersection is `u+S_(a-d)`, giving `T(z)-2T(a)+T(a-d)`. Since `z<M`, the four count is `T(M+z)-2T(z)`; the isolated count is the quadratic second difference `T(2M+z)-2T(M+z)+T(z)=M^2`. Weighting the counts by their inversions `20,13,6,3,1` simplifies to `T(2M+z)+T(M+z)+T(z)+T(a)`, equal to the sum over the four exact inverted translation classes. Hence the correction is complete. At `a=2d`, both 16 starts `0,u` become feasible and intersect. QED.

## Executed validation and scope

`VERIFY_SIXTEEN_WINDOW.py` uses `fractions.Fraction`; verifies the 16-point permutation throughout the **whole** strict interval `3/2<epsilon/eta<2` using rational sample points near its endpoints and the symbolic proof above; exhaustively sorts the entire triangular threshold set for *every* H in each corresponding scaled window for two unimodular models; confirms strict block contiguity, disjointness, complete true-order equality, inversion-count identities; checks actual 45-term rational logarithm bounds and endpoint integer counts. Actual stdout in `RUN_SIXTEEN_WINDOW.txt`. No enumeration of the full gigantic actual-H threshold set was performed.

BRC joint (1,4) count carrier and label-3 padding retained. Result is an auxiliary exact order/readout theorem, with native X6 and six-source/ten-label bridge preserved as distinct mathematical objectives; it is not a Result/Review promotion.

**Next:** at H=9822316 resolve the first collision of translated sixteen-blocks, likely a 21-point local interleaving, and test the exact finite-interval continuation. Independently continue full changed-gap prefix occupancy at H=2455579.
