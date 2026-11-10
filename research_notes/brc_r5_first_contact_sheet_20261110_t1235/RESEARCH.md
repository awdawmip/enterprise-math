# R5: a genuine interior 14-edge wall with 15-edge chambers on both sides

Date: 2026-11-10 (Asia/Shanghai). Mode: author-side exact research, not a formal Result or independent review. Scientific pins unchanged: GLOBAL `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. Exact predecessor: Draft PR #1950 at `c8a0ade3904507cf4dda38bfa888bdb490b1ea87`, especially `research_notes/brc_r5_two_facet_20261110_t1140/VERIFY.py` and `VERIFY_FIRST_14_CONTACT.py`. Earlier ten forced-edge certificates: PR #1939. BRC branches are the 30 specified statistical transport arcs, **not** spatial X6 axes; P000 and ACTIVE world assumptions are preserved.

## Theorem — local two-sided phase stratification at the first contact

Write `R=49948501046391/3920403670319950000`, `x=(-1,1,1,-1,-1,-1,-1,1)`, `z_c=R*x`, and use the frozen eight-parameter physical-affine family `p(z)=p0+P*(tstar+z)`. Let `N(z)` be the minimum number of strictly positive allowed Blackwell transfer arcs over **all** nonnegative solutions of the full 21-row martingale marginal system.

Set the primitive integral normal
```
n = (34101,-293725,-85599,42525,937899,293725,85599,-3287440)
```
and the affine seven-dimensional hyperplane `H={z:n·(z-z_c)=0}`.

**There exists an open eight-dimensional neighborhood U of z_c**, entirely inside the original physical legal and Blackwell feasible domain, such that:
```
for every z in U intersect H:       N(z)=14;
for every z in U outside H:         N(z)=15.
```
The 14-edge locus in U is one genuine codimension-one sheet in the *interior* of the physical legal region, not merely a boundary of physical capacities. Both neighboring sides contain feasible 15-edge physical points. This strengthens the predecessor's exact isolated 14-edge first-contact witness to a local dimensional classification. It does not assert a global 13/14/15 classification.

## Proof and exact finite classification

The 10 forced arcs from PR #1939 are `F=((0,0),(0,1),(0,2),(2,2),(3,3),(4,3),(4,5),(5,5),(6,5),(6,6))`. At z_c take the strictly positive 14-edge support `F+S` with `S=((2,1),(3,2),(0,3),(1,5))`; the predecessor checked all full 21 equations and physical inequalities. Its 15-row reduced column matrix has exact rank 14; its 14 masses are strictly positive, the smallest being `16932541854726549/313632293625596000000`. All nonstructural physical slacks are strictly positive; the smallest is `3836062555208901/156816146812798000000`. Its `mu_1` is also strictly positive. Therefore a sufficiently small real ball about z_c preserves physical legality and all 14 original masses on any perturbation for which their 14-column system remains solvable.

Let `C` be the 15-by-30 exact reduced column matrix, `L` a five-row left annihilator of the ten forced columns, `V=L*C_other` the 5-by-20 quotient columns, `q(z)` the quotient requirement, and `T` the 15-by-8 derivative of the reduced physical right-hand side. The previous first-contact normal is `w=(0,-25,1,1,1)`, with
```
w*q(z_c) = 0
w*L*T = (421/800,-11749/2592,-9511/7200,21/32,
         11579/800,11749/2592,9511/7200,-41093/810)
n = 64800*(w*L*T).
```
An independent exact enumeration of all `binom(20,4)=4845` four-extra-arc subsets shows: **4817** quotient column spans omit `q(z_c)`; exactly **28** contain it, every corresponding 15-row 14-column matrix has rank 14, and each has precisely the **same** physical normal `n`. Among those 28 unique 14-edge solutions, **12** have all 14 masses strictly positive; the remaining 16 contain negative coefficients. Thus all 14-edge support spans passing through the contact occupy H. Since there are only finitely many supports and all 4817 other spans are closed and omit `q(z_c)`, a common open neighborhood excludes them. The predecessor's strict forced-edge duals continue to apply locally. The exhaustive `binom(20,3)=1140` quotient rank exclusions at z_c show no <=13-edge transfer there; the same finite-closed-set argument gives a smaller open neighborhood excluding all such supports. On H, the positive `F+S` 14-edge solution extends continuously; therefore every sufficiently near z in H has N=14.

For points off H, add to the original 14-edge basis either the arc `(5,1)` (positive side) or `(1,1)` (negative side). The respective 15-by-15 matrices have rank 15. Their last coefficients are exactly
```
E_(5,1)(z) = (w*q(z))/5     when n·(z-z_c)>0;
E_(1,1)(z) = -(w*q(z))/15   when n·(z-z_c)<0.
```
They are positive on their named sides. The other 14 coefficients are continuous with positive values at z_c, so both 15-edge bases remain positive in a sufficiently small common neighborhood. This proves feasibility and N=15 on each side, using the same finite support exclusions.

## New exact rational witnesses and reproducibility

A nonzero tangent vector to H is
```
h=(11749/2592,421/800,0,0,0,0,0,0).
```
At the distinct point `z'=z_c+10^-12*h`, the original 14-edge support still solves all 21 Blackwell equations, all physical capacities are satisfied, and the minimum strictly positive transfer mass equals `16932541854726549/313632293625596000000`. A newly executed exact integer rank test excludes all 1140 <=13 support candidates at this nontrivial point.

For the two transverse rational points `z_+=z_c+10^-12*e_0`, `z_-=z_c-10^-12*e_0`, exact 15-edge solutions exist with additional arcs and masses
```
z_+: (5,1) has mass 421/4000000000000000;
z_-: (1,1) has mass 421/12000000000000000.
```
All remaining 14 masses and nonstructural physical slacks are strictly positive at both points. The quotient normal sees both positive and negative admissible additional branches: this is an *internal sparsity wall*, not the Blackwell feasibility boundary.

The accompanying `VERIFY_SHEET.py` recomputes all 4,845 quartet rank tests with exact fraction-free integer elimination and classifies their positive solutions and normal; it also recomputes 1,140 triple exclusions at the distinct tangent point and tests all 21 original equations, physical capacities and both transversal 15-edge solutions. `EXACT_OUTPUT.txt` is the actual stdout of that script executed under Python/SymPy locally. Its dependency `../brc_r5_two_facet_20261110_t1140/VERIFY.py` is pinned by the parent commit above. Other earlier claims, including the ten forced-edge dual proofs, retain their source and review status.

## Next smallest scientific unit

Find the nearest points on H where one of the 14 positive masses vanishes or the forced-edge dual certificates cease to apply, and test the resulting candidates for 13-edge realizations. Separately classify the 12 positive 14-edge bases and their transitions inside H, preserving branch identity and the complete physical observer.
