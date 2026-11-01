# BRC N=4 / S23: sharp six-third-stage box centers and four-group splitting obstruction

Research date: 2026-11-01. Classification: AUTHOR_ANALYTIC_PROOF / EXACT_INTEGER_V8_EXECUTED / UNREVIEWED / NOT_ADMITTED. This work continues the prior author-side observer-conditioning theorem at Enterprise Math PR #1765 commit c1f4d9375b5b32c584f19e240096e9804a97c968. It concerns only the frozen S23 finite probability model; P000 X6 and independent-time interpretation requires a separate faithful bridge.

## Model and hypotheses

There are six labelled positive BRC sources in this order: AU0, AU1, AV, BU0, BU1, BV. A source has four stopping probabilities

F(a,b,c) = (a, (1-a)b, (1-a)(1-b)c, (1-a)(1-b)(1-c)).

The six prepared laws are p_i = sum_x M_ix F_x, with the fixed, source-labelled observer matrix

20 M =
[10 10 0 0 0 0;
 9 11 0 0 0 0;
 0 0 20 0 0 0;
 0 0 0 10 10 0;
 0 0 0 2 18 0;
 0 0 0 0 0 20].

Freeze the first two stage variables a_A, a_B and the second stage variables b_U, b_AV, b_BV at any legal real values. The remaining six independent third-stage variables c_x vary in the rectangular box Q = product_x [ell_x,u_x], with 0 <= ell_x <= u_x <= 1. The six survival weights are

s = ((1-a_A)(1-b_U), (1-a_A)(1-b_U), (1-a_A)(1-b_AV), (1-a_B)(1-b_U), (1-a_B)(1-b_U), (1-a_B)(1-b_BV)).

Define nonnegative w_ix=M_ix s_x, interval midpoint m_x=(ell_x+u_x)/2, and observer halfwidth h_i = (1/2) sum_x w_ix (u_x-ell_x). Observations are prepared laws, not an unlabeled total that magically recovers source identities.

## Theorem 1: exact minimax on every third-stage rectangle

For each anchor z in Q, set R_Q(z)=sup_{c in Q} max_i TV(p_i(c),p_i(z)). Then for ALL real legal values, including degenerate survival weights and zero-width coordinates,

(1) TV(p_i(c),p_i(z)) = |sum_x w_ix (c_x-z_x)|.

(2) R_Q(z) = max_i [h_i + |sum_x w_ix(z_x-m_x)|].

(3) min_{z in Q} R_Q(z) = R_* = max_i h_i = (1/2) max_i sum_x M_ix s_x (u_x-ell_x).

(4) All optimal anchors are precisely the polytope of z in Q satisfying
    |sum_x w_ix(z_x-m_x)| <= R_* - h_i for all six i.
    The componentwise midpoint m is optimal.

(5) The exact prepared-law diameter of the box is
    D(Q) = sup_{c,d in Q} max_i TV(p_i(c),p_i(d))
         = max_i sum_x w_ix(u_x-ell_x) = 2 R_*.

Proof. Once a,b are frozen, varying c_x changes only source stop-3 and stop-4 probabilities by +s_x(c_x-z_x) and -s_x(c_x-z_x). After the positive source mixture, p_i(c)-p_i(z) is (0,0,T_i,-T_i), where T_i=sum_x w_ix(c_x-z_x); hence its total variation is |T_i|. Positivity of w makes the scalar sum_x w_ix c_x range between L_i=sum_x w_ix ell_x and U_i=sum_x w_ix u_x. Its maximum absolute distance to sum_x w_ix z_x is (U_i-L_i)/2 plus the absolute displacement of that anchor from (U_i+L_i)/2. This proves (2), with maximum over finitely many i commuting with the box supremum. The halfwidth is an unavoidable lower bound, and midpoint m simultaneously removes all displacements, proving (3) and (4). For the diameter, all-lower and all-upper box corners simultaneously realize the full nonnegative weight sums; no other pair can exceed their coordinate differences. This proves (5). No finite sampling or unproven minimax interchange is involved. QED.

Decoder-bank consequence. For any fixed common encoder and finite bank of fixed decoder laws q_i^l, define G(c)=min_l max_i TV(p_i(c),q_i^l). The triangle inequality and finite min/max Lipschitz properties imply

(6) sup_{c in Q} G(c) <= G(m) + R_*.

This is an exact local uncertainty-radius term. It need not be a tight bank-risk certificate for an arbitrary chosen bank.

## Theorem 2: optimal four-group bisection is necessary and sufficient

Now set a_A=a_B=1/4 and b_U=b_AV=b_BV=1/3, so all six s_x=1/2; start from Q=[0,1]^6. Theorem 1 gives R_*=1/4 and D(Q)=1/2. Every h_i=1/4. The midpoint m=(1/2)^6 is the UNIQUE minimizing anchor because (4) requires M(z-m)=0, and M is invertible: the AU two-by-two block determinant is 1/20, BU determinant 2/5, and AV/BV rows are singleton identities.

For a chosen subset S of the six third-stage axes, bisect each selected interval ONCE and choose either child, leaving all other intervals uncut. Define the integer entries n_ix=20 M_ix. Each resulting child has exact optimal radius

(7) R(S)= (1/160) max_i sum_x n_ix (2 - 1_{x in S}).

The radius strictly improves below 1/4 IF AND ONLY IF S intersects each of four groups: {AU0,AU1}, {AV}, {BU0,BU1}, {BV}. Thus one, two or three coordinate bisections cannot reduce the worst-observer optimal radius AT ALL. Four bisections are necessary and sufficient. Among four-axis choices, the UNIQUE best set is S={AU1,AV,BU1,BV} (zero-index mask 54), attaining

(8) R(S)=30/160=3/16.

The three other four-group-transversal selections have exact radii 31/160, 38/160 and 38/160, respectively. The minima over all subsets of size k=0,1,2,3,4,5,6 (in units 1/160) are 40,40,40,40,30,30,20.

Proof. A prepared row supported in a source group that S misses retains full unit c-width, so that row still forces radius (1/2)(1/2)=1/4. Conversely, once S hits all four source groups, the strictly positive weights of every supported source in the relevant rows make every row width strictly smaller than one. Any four-element transversal contains AV and BV and one member each of AU and BU. Substitution in (7) for these four possibilities yields the enumerated exact numerators; the six-count result is the finite 64-subset evaluation of (7). Both child choices have the same width, so the result holds for EVERY child box. QED.

The first three splits can still reduce source-level uncertainty, but a global worst-observer score remains on a plateau. This is a concrete reason not to rely on myopic one-axis radius improvement for this BRC cover.

## Theorem 3: every single observer-row deletion erases a lawful distinction

The full six-by-six observer matrix M is invertible. For row j removed, the following d_j directions in labelled c-coordinates are invisible to ALL five retained rows but visible to the omitted row:

d_0=(11,-9,0,0,0,0), d_1=(1,-1,0,0,0,0),
d_2=(0,0,1,0,0,0), d_3=(0,0,0,9,-1,0),
d_4=(0,0,0,1,-1,0), d_5=(0,0,0,0,0,1).

Direct integer multiplication gives M_i d_j=0 for every retained i!=j, and M_j d_j !=0. With fixed first/second controls as above, the two legal six-control policies c=(1/2)^6 and c'=(1/2)^6+d_j/32 stay in [0,1]^6. Their five retained prepared laws coincide exactly; the deleted law differs. Therefore no one-row deletion is lossless for the declared target of preserving ALL SIX original prepared laws or any future observation capable of reading the deleted law. A narrower observer-horizon equivalence is not excluded; the claim is explicitly observer/future-operation typed. This extends the earlier one-AU-row witness to ALL six possible omissions without claiming an external physical no-go theorem. QED.

## Exact validation and research boundary

The committed VERIFY.js contains precisely the verifier executed in V8 during this author turn. Its safe-integer arithmetic evaluates 15,625 legal grid policies and 93,750 direct-row total-variation identities; all 64 bisection subsets with 64 vertices and six rows each (24,576 direct TV checks); the sharp four-split optimum; and all six erased-row directions. The numerical grid checks correct encoding of the frozen rational face; the all-real box theorem is analytic. Full 64-subset enumeration is an exact exhaustive finite proof only of the discrete split-selection claim.

BRC reuse decision: REUSE_APPLIED — existing labelled positive-mixture, local TV and observer-fiber methods at the pinned preceding PR; no new general-purpose tool-family novelty or new Foundation admission claimed. The unrestricted 11D ten-label minimax remains bounded as previously by 1/2 <= R_beh(k,10) <= 2/3 (k=4,6). P000 native X6 and independent-time transfer, S2 information-set scope, live Owner/CLAIM, and independent mathematical review are separate obligations.
