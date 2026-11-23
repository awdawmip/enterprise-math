# R284GI — sharp capacity extends to q >= 4u-2

Date 2026-11-24 Asia/Shanghai. Author proof with exact rational branch verification; NOT_REVIEWED. Informed portable research, same frozen four-phase binary fixed-tag model as R284GH; no shared CLAIM. P000 and ACTIVE worldview unchanged. This is an auxiliary Boolean residual observer problem, not a native geometry computation.

## Result

For integers u>=2 and q>=4u-2, n_min(q,u)=4q+8u+2. The previous u=1, q>=2 result covers the u=1 boundary separately. R284GH already proves q>=4u-1, so only q=4u-2 needs new obstruction. The repeated Gray upper construction remains unchanged.

## 1. Two-heavy necessity: use the discrete u threshold

Reuse the six necessary disjunctions of R284GG: two opposite stable separations, four R284GE adjacent no-rollback conditions, with the original seven normalized nonconstant patterns. The six families are constructed explicitly in the checker. Opposite graph K2,2 requires at least one edge mass >=2q+2u+1, incident pair mass >=3q+2u+1, or total four-edge mass >=4q+2u+1. Adjacent source groups G require some nonempty subset S of groups with sum of masses >= (|S|+1)q+4u+1. Both statements retain exact source incidence.

For width <=4q+8u+1 and two nonheavy types from {3,5,6}, impose x_p<=2q+2u-1 for the selected pair, q>=4u-2 and u>=2. This real relaxation is infeasible, even though GH's earlier relaxation with u>=1 had a fractional solution at u=1.5. Integer u>=2 allows the stronger domain; no further integrality argument is necessary for the disjunctions.

The companion script explicitly branches over all children of each necessary disjunction until an infeasible branch is established. Every stopped branch has a nonnegative rational multiplier vector c satisfying c^T A=0 and c^T b=-1 for rows Ax<=b. SciPy proposes candidates; Fraction checks the exact identities, not a floating infeasibility claim. A missing proof or feasible full branch raises an assertion. Both source group incidence and opposite K2,2 incidence are reconstructed from the actual phase bits. Actual local run (Python, SciPy/HiGHS; assertions enabled):
(3,5): 1063 verified leaves, maximum denominator 53
(3,6): 785 verified leaves, maximum denominator 53
(5,6): 1525 verified leaves, maximum denominator 53
Total 3373. No bound on q or u. Script regenerates rather than embeds the exact certificate data.

## 2. Two-heavy obstruction at q=4u-2

Write width n=4q+k, k<=8u+1. Two heavy multiplicities are 2q+a,2q+b with a,b>=2u; all other columns total R=k-a-b<=4u+1=q+3. Constants are harmless by the previous normalization argument.

Use GE: sum_e (N_e-q)_+ >= q+4u+1, where N_e are source-group sizes. For disjoint residual groups of total mass M, their overflow is at most (M-q)_+.

Pair {3,6}: on edges 0 and 1 each respective heavy is alone in its changing source group. Other groups contribute at most 3; hence a,b>=4u-2 and R<=5<=q (u>=2). Now residual groups cannot overflow. The same inequalities force a,b>=4u+1, contradicting k<=8u+1.

Pairs {3,5},{5,6}: a is the offset of nonalternating heavy g; b is offset of alternating heavy h=5. On two edges where only h is heavy and changes, h shares a source group with distinct residual types r1,r2 (multiplicities of 1,4 for {3,5}; 2,7 for {5,6}). GE and the residual overflow bound imply
    b+max(r_i,R-q)>=4u+1, i=1,2.
If b<=4u-3, then 4u+1-b>=4>R-q, so r1+r2>=2(4u+1-b). Since k=a+b+R<=8u+1, b>=a+1>=2u+1. If b>=4u-2, the same lower bound b>=2u+1 holds because u>=2. Thus R<=4u, R-q<=2.

Suppose a=2u. For opposite phases 0 and 2, only g among the two heavies differs. No single differing type reaches 2q+2u+1: g has exactly 2q+2u and residual sizes <=4u. A four-vertex cut is impossible because the total differing mass is <=2q+k-b<=2q+6u<4q+2u+1 for q=4u-2,u>=2. Thus a three-vertex cut must separate, requiring two incident types with sum >=3q+2u+1. Residual mass alone <=4u is too small, so it must include g and one residual type of size >=q+1=4u-1. Also 2q+k-b>=3q+2u+1 gives b<=2u+2. Then each distinct r_i>=4u+1-b>=2u-1>R-q. Even the largest residual type leaves at least 2u-1 mass in a different residual type, so its size is <=4u-(2u-1)=2u+1<4u-1. Contradiction; a>=2u+1.

If b=2u+1, then R<=4u-1, R-q<=1; both r_i>=2u and R>=4u, contradiction. Therefore b>=2u+2 and R<=4u-2=q.

## 3. One-extra-omission extension of GF diagonal barrier

Take edge 0->1 for {3,5}, or 1->2 for {5,6}. Both heavies change and their four phase projections are the four distinct binary pairs. Set
    T_g=a+R-2u=k-b-2u <=4u-1=q+1,
    T_h=b+R-2u=k-a-2u <=4u=q+2.
Both thresholds are positive. If T_h<=q+1, GF already applies. Otherwise T_h=q+2 (so k=8u+1,a=2u+1). Follow the write order until either threshold is first hit.

If h is first, fewer than T_g<=q+1 g-attempts have occurred; omit all of them and apply the GF witness with h as the successful group. If g is first, at most q+1 h-attempts have occurred. Omit all except at most one, and let all g and residual attempts succeed. The third phase j differing from source i on g alone is 2 for {3,5}, 3 for {5,6}. As in GF, correct up to q untouched g-coordinates in source history and up to q-R additional g-coordinates in comparison history. Correct all residual mismatches in comparison history (at most R), giving remaining g-distance <=2u by T_g. The possible one successful h-attempt is an extra comparison mismatch; correct it in comparison history. This is legal because:
- the comparison last-change group of h is distinct from g's (at j=2, g last=0,h last=1; at j=3, g last=1,h last=2);
- when R<=q-1, the h group has room for the extra correction;
- when R=q, k<=8u+1, a>=2u+1,b>=2u+2 force a=2u+1,b=2u+2,k=8u+1. The two r_i inequalities then imply r1,r2>=2u-1 (R-q=0). One of them is outside the h group: type 4 has last edge 3 at phase 2; type 7 has last edge 0 at phase 3. Thus at least one residual column is outside the h group, leaving room for one h correction even when every residual coordinate needs correction.

Every source history and comparison history used here respects the last-change budgets in the exact R284FM stable product. The current prefix uses at most q omissions. After all corrections the prefix is at Hamming distance <=2u from a stable third-phase state. Their noisy read sets intersect, violating correctness. This holds for every order, and exhausts both alternating-heavy cases.

Together with section 1 and the unchanged Gray upper bound, the claimed sharp capacity follows. The new ingredient is to preserve the comparison-phase residual source groups instead of charging the extra h-mismatch against the entire residual mass.

## Evidence and remaining boundary

- GH theorem and its exact assumptions: c3617898cea2157702d79e68ee0117cd333cd310:research_notes/portable_direct/R284GH_SHARP_BOUNDARY_Q4U_MINUS1_20261124.md
- GG source groups and six disjunctions: 1d92030a09b96f41661247bc2bae837ed8ff1899:research_notes/portable_direct/R284GG_exact_general_u_certificate.py
- GF witness and frozen lineage: 85801535d3b34cca713f28703b4984baf80975f3:research_notes/portable_direct/R284GF_UNIFORM_TWO_HEAVY_DIAGONAL_BARRIER_20261124.md
- GE exact rollback theorem: a112519ea319ef0e0bdf10ee01d817e10fd3dcd5:research_notes/portable_direct/R284GE_EXACT_ADJACENT_ROLLBACK_CAPACITY_20261124.md
- New executable certificate checker: 7eeeb2cd7354b165335d1ad22bceceeb8294f95c:research_notes/portable_direct/R284GI_q4u_minus2_checker.py. Actual local run verified 3373 rational certificates. This computation checks section 1; sections 2-3 are written arguments, not an independent numerical simulation or formal Review.
Next question: q=4u-3 for integer u>=2. Check nonheavy relaxation on the correct discrete domain, then use per-source comparison slack (not aggregate R alone) for extra-omission witnesses. Do not infer the sharp boundary from a relaxation failure.
