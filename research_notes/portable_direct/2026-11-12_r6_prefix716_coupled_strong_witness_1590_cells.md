# PREFIX-716-R6 — Correct Gamma coupling + stronger feasible witness: 1,590 new exclusion cells

Date: 2026-11-12 (Asia/Shanghai). Parent: PREFIX-675. Frozen science: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d. Source interfaces: PREFIX-710/712/713/714/715. Grade: AUTHOR_EXACT_CHECKED / UNREVIEWED / NOT_ADMITTED.

This is the auxiliary two-parameter BRC statistical observer D=[0,1/2]^2, not a native X6 plane or slice. For independent completion clocks T_p|N_p=k ~ Gamma(k,1), put Y=max(T_p,T_z), mu=E[Y], M2=E[Y^2], W=M2-mu^2, and f_t=W-t mu (t=1/q). The 189-row frozen BRC count kernel yields the correct Gamma maximum moments from PREFIX-710.

## Theorem 716.1 (targeted certified area)

Relative to PREFIX-714's exact disjoint union of 137,278 certified 384x384 cells, the new checker certifies 795 distinct upper-triangular cells and their 795 exchanges, no prior overlap. For every real q>=2, a global maximizer of V_q=q^2 f_(1/q) is strictly outside these 1,590 additional closed cells. Thus at least

  (137278+1590)/147456 = 138868/147456 = 34717/36864 = 94.1758897569...%

of D is strictly excluded. On each of the newly certified cells the normalized objective gap against the feasible e_A=(0,149/1000) is strictly greater than 745380/1000000, hence the unscaled V_q gap is greater than (745380/1000000)q^2.

## Exact proof

For a rectangle R=[a,h] define delta=mu(h)-mu(a)>=0 and B=M2(h)-M2(a)>=0. Reuse the proven coordinatewise frozen survival order and the exact Gamma influence coefficient ratios I_n(v),J_n(v) of PREFIX-713. They furnish C_R>0 so that with d=mu(x)-mu(a), for each x in R:

  0<=d<=delta, 0<=M2(x)-M2(a)<=min(B,C_R*d).

Consequently for every t>=0:

  f_t(x)<= E_R(t)
   := W(a)-t*mu(a) + max_(0<=d<=delta) [min(B,C_R*d)-(2mu(a)+t)d-d^2].

The finite exact maximization evaluates d=0, d=delta, d=min(delta,B/C_R), and d=(C_R-2mu(a)-t)/2 if inside the first segment. The correct Gamma clock is essential, not the maximum of stopping counts from the invalid PREFIX-709 shortcut.

**Endpoint lemma.** E_R(t) is a supremum of affine functions of t and hence convex. For any feasible fixed witness e, L_e(t)=f_t(e) is affine, so L_e-E_R is concave. Strict positivity at both t=0 and t=1/2 establishes strict positivity for all real t in [0,1/2]. The checker applies this to e_A; PREFIX-713 proves from exact frozen moments that W(e_A)-W(e_0)>5224/100000 and mu(e_0)-mu(e_A)>5474/10000 for e_0=(0,3/20).

## Finite computation and novelty accounting

The script constructs 189 integer survivor rows (9,529 nonzero units), the rational Gamma kernel and exact 384-axis lattice. It deterministically selects 1,066 off-diagonal fine cells from -3..+4 neighborhoods of 11 known coupled coarse seeds and -3..+3 neighborhoods of ten previously known multi-comparator fine seeds. It removes the 90 exact PREFIX-713 coupled cells and the 20 exact PREFIX-714 multi-comparator cells; it also rejects any cell passing PREFIX-712's old fixed-e_0 fine-cell certificate. A certified PREFIX-712 coarse parent implies that fine-cell certificate for all its children by monotonicity and nesting of the moment corner bounds. Hence every retained cell is new relative to the inherited union.

The script tests E_R(0) and E_R(1/2) against exact e_A moments with Python Fraction, retains exactly 795 distinct pairs i<j with positive margins, verifies the strict minimum bound and compact-list SHA256 01ee0b393803fbdfe9b7b27bd80a1f50d5ebcd5ef3fc5a0b3bd115c0c13c33db. The attached JSON contains the complete 795-index list. Reflection gives 1,590 disjoint new ordered cells. Each (i,j) denotes the closed cell [i/768,(i+1)/768] x [j/768,(j+1)/768]. Boundary intersections have zero area.

The author locally executed an equivalent exact-integer/Fraction checker, reproducing 795, 1,590, the strict gap floor and the final rational fraction. The published program generates its own full JSON when run. Remote CI execution and independent mathematical review are pending. Reuse decision: COMPOSE_APPLIED. Existing P000, frozen scientific source and the objective/observer distinction remain unchanged.

## Next discriminating unit

The remaining uncertified area corresponds to at most 8,588 fine-cell equivalents. Scan these selectively with the same coupled envelope and other exact feasible witnesses; retain only new disjoint exclusions. Then isolate local stationary points or produce Bernstein/derivative certificates to resolve the PREFIX-675 global optimizer, not only its candidate-area reduction. Source storage here is an author checkpoint, not a formal Task CLAIM, Result, Review or Foundation promotion.
