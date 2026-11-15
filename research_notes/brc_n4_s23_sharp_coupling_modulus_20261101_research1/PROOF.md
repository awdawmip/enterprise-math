# BRC N=4 / S23: sharp causal coupling modulus and strengthened 11D mesh certificate

2026-11-01 — AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED. Scope: six-source finite statistical S23 stopping-time model, NOT native P000 X6/time dynamics, NOT the unrestricted ten-label minimax.

## Frozen sources and quantifiers

Six sources AU0, AU1, AV, BU0, BU1, BV; six preparations; four stop times. The legal shared-control behavioral policy is
(a_A,a_B,b_U,b_AV,b_BV; c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV) in [0,1]^11.
First-stage index mapping A=(0,0,0,1,1,1); second-stage B=(2,2,3,2,2,4); third-stage C=(5,6,7,8,9,10). The U second-stage control is shared by AU and BU. One latent source has law

F(a,b,c) = (a, (1-a)b, (1-a)(1-b)c, (1-a)(1-b)(1-c)).

Prepared law p_i(theta)=sum_x M_ix F_x(theta), with positive row-stochastic BRC operator M=M20/20,

    M20=((10,10,0,0,0,0),(9,11,0,0,0,0),(0,0,20,0,0,0),
         (0,0,0,10,10,0),(0,0,0,2,18,0),(0,0,0,0,0,20)).

For any fixed row-stochastic common encoder E and any policy-independent finite decoder bank D_l, define q_li=(M E D_l)_i,
L_l(theta)=max_i TV(p_i(theta),q_li), G(theta)=min_l L_l(theta). The label is selected after learning theta but before observing stop time.

## Theorem A: causal source coupling

For two triples (a,b,c), (a',b',c'), put d_a=|a-a'|, d_b=|b-b'|, d_c=|c-c'| and
C = d_a + (1-max(a,a')) d_b + (1-max(a,a'))(1-max(b,b')) d_c.
For all real triples in [0,1]^3,

    TV(F(a,b,c),F(a',b',c')) <= C <= 1-(1-d_a)(1-d_b)(1-d_c).          (1)

Proof. Couple both stopped laws using the same three independent U[0,1] thresholds. The first stage decisions differ with probability d_a. The probability that both survive first stage is 1-max(a,a'); conditional on this the second decisions differ with probability d_b. The probability of joint survival through the second stage is (1-max(a,a'))(1-max(b,b')); conditional on this the third decisions differ with probability d_c. These three first-disagreement events are disjoint, and every disagreement of eventual stopping times must lie in their union. Their total probability is C, proving the TV coupling upper bound. Since max(a,a')>=d_a and max(b,b')>=d_b, C is at most the product bound. Note that C may strictly exceed true TV. QED.

## Theorem B: exact sharp uniform modulus of the prepared map

Let d_inf(theta,phi)=max_j |theta_j-phi_j|. For EVERY real epsilon in [0,1],

    sup_{d_inf(theta,phi)<=epsilon} max_{i=1..6} TV(p_i(theta),p_i(phi))
           = 1-(1-epsilon)^3.                                         (2)

Upper bound: each of the six sources traverses exactly three distinct causal parameters, each differing by at most epsilon. Apply (1) and the positivity/row sums of M to each prepared row. Attainment: choose theta=(0,...,0), phi=(epsilon,...,epsilon), including the same legal shared b_U control for both source groups. Then each latent source, and hence every prepared row, equals e4 at theta and equals
(epsilon,(1-epsilon)epsilon,(1-epsilon)^2 epsilon,(1-epsilon)^3)
at phi. Its TV from e4 equals 1-(1-epsilon)^3. Thus (2) is sharp for the prepared-law map for every real epsilon. QED.

The sharpness in (2) is NOT asserted for a particular decoder-bank risk G.

## Corollary C: exact source-aware 11D risk modulus and mesh bounds

With C_x(theta,phi) from (1), for any fixed encoder/bank,

    |G(theta)-G(phi)| <= max_i sum_x M_ix C_x(theta,phi)
                       <= 1-(1-d_inf(theta,phi))^3.                  (3)

For each l,i the TV metric reverse triangle inequality bounds changes in TV(p_i,q_li) by TV(p_i,p'_i); max_i and min_l preserve a common bound. Applying M yields (3).

For an axis-aligned parameter box Q, with widths h_j, define causal index set P(x)={A[x],B[x],C[x]},
omega_x(h)=1-prod_{j in P(x)}(1-h_j/2), and
Omega(Q)=max_i sum_x M_ix omega_x(h).
Rounding all free coordinates of any theta in Q to their nearest box endpoints yields a legal vertex v satisfying |theta_j-v_j|<=h_j/2. Thus

    0 <= sup_{theta in Q} G(theta) - max_{v vertex of Q} G(v) <= Omega(Q).   (4)

For uniform width h, Omega(Q)=1-(1-h/2)^3. The preceding linear mesh bound was 3h/2. Their strict difference for h>0 is 3(h/2)^2-(h/2)^3. For h=1/2, (4) gives 37/64 vs the earlier 3/4; for h=1/10 it gives 1141/8000 vs 3/20. The anisotropic Omega(Q) is at most the previous source-weighted sum bound.

IMPORTANT: (4) bounds the LOW (sampled-grid) underestimate, whereas the earlier min_l max_{corners} L_l upper certificate is separately sound. No finite-sample minimum of labels is automatically a full-box upper certificate. No improvement to the unrestricted ten-label minimax [1/2,2/3] (k=4,6) is claimed.

## Evidence and scientific boundaries

Run python VERIFY.py (stdlib Fraction) in this directory. The actual stdout is RUN_EVIDENCE.txt. It checks all 15,625 ordered pairs of the 125 3-stage parameter triples on {0,1/4,1/2,3/4,1}^3; all six prepared rows attain the sharp modulus at epsilon=1/7,1/3,1/2,3/4,1; three concrete pairs under the frozen 10-decoder bank from PR #1765 obey the source-aware and uniform bounds; two mesh widths improve strictly. Universal real results follow from proofs, not finite extrapolation.

BRC provenance: AU0/AU1 and BU0/BU1 remain distinct latent sources, followed by explicit M mixing; the six source labels are NOT P000 spatial axes. Separate hypotheses are required to transfer to native six-axis Cell and independent time, or to the S2 information-set model. No independent replication, formal verification or native scientific admission is represented.

Frozen inputs: GLOBAL_KNOWLEDGE_V1 main@50bd0cf9511f7730690d8c69b86ac37475e95115; Enterprise Math main@74d2253a036f31593a58f4c74eb73a707b6db3a7. Predecessor: PR #1765 commit f3890a2aa7548f533f7b805b946c01d69823e361 (fixed-nine three-atom 2/3 obstruction). Authenticated author login: awdawmip. Native research_authority_granted=false and owner query CONTROL_QUOTA, so no CLAIM, owner authority, Result or reviewer admission is asserted.

Next: apply the stronger certificate to a jointly redesigned ten-label bank that alters at least one of the frozen nine decoders; combine exact LOW rational witnesses, fixed-label UP cell covers, and Omega adaptive subdivision.