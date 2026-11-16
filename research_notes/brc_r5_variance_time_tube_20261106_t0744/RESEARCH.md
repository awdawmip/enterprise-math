# R5: Sharp likelihood-ratio variance/time budget and a guaranteed real-image tube

Date: 2026-11-06 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Frozen science and scope

R5 asks for a strictly positive rational finite P/Q stopping tree whose FULL_HIST and seedless LR four-observer convex hulls agree but whose actual real-behavior images differ. The science pins remain GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e.

The exact four-stage delta=1/4 auxiliary P/Q model is inherited from EM 57f7d654e5dd002567e0b0d333937e6e38f3b4cb (scalar gate), and the exact common time octagon H_T from EM d648610de1a56f155d3a0d3caef37cd2ce0ca415 (time octagon). The earlier full four-dimensional hull certificate remains an author-side predecessor, not independently rerun. This P/Q likelihood-ratio histogram is an auxiliary typed BRC observer, not P000 native X6 dynamics.

Under Q, the bounded likelihood-ratio martingale R_t=dP/dQ starts at R_1=1. Time 2 ratios are (3/4,5/4), Q transition (1/2,1/2). Time 3 ratios are (1/2,1,3/2), Q rows (13/20,1/5,3/20) and (1/40,9/20,21/40). Time 4 ratios are (1/10,1,19/10); Q rows at j=0 and j=2 are (509,382,9)/900 and its reverse, respectively; at j=1 the rows for history i=0 and 1 are (47/180,43/90,47/180) and (67/162,14/81,67/162). All rows are strictly positive, stochastic, with their child's likelihood-ratio mean equal to the parent.

A seedless LR timing policy has root continuation g, time-2 continuations a_0,a_1, and shared time-3 ratio continuations z_0,z_1,z_2, all in [0,1]. Its stop tau lies in {1,2,3,4}; Q stopped-ratio masses M_r sum to one and satisfy sum_r r M_r=1. Write sigma2=sum_r M_r (r-1)^2 and T_Q=E_Q[tau].

## Theorem A. Exact sharp variance/time cost

For every seedless LR real-randomized timing policy, including boundaries,

    sigma2 >= (T_Q-1)/16.

The coefficient 1/16 is best possible and equality holds exactly when u_0=g*a_0=u_1=g*a_1=0 (so no continuation into time 3).

Proof. At a visited node, c=E_Q[(R_{t+1}-R_t)^2 | history] is a Q-conditional quadratic-variation cost. Direct substitution gives the exhaustive transition table:

    1 -> 2:             1/16
    2 -> 3 from i=0:    11/80
    2 -> 3 from i=1:    3/40
    3 -> 4, j=0 or 2:   1081/5000 (either history)
    3 -> 4, j=1, i=0:   423/1000
    3 -> 4, j=1, i=1:   67/100.

Every cost is at least 1/16; all costs beyond the first transition are strictly larger. Because R_t is a bounded Q-martingale and tau is a bounded stopping time, cross terms between different martingale increments have expectation zero, including with adapted continuation indicators. Therefore

    E_Q[(R_tau-1)^2]
      = E_Q[ sum_{s=1}^{tau-1} c_s(history_s) ]
      >= (1/16) E_Q[tau-1].

This identity also gives the equality characterization. If g=1,a_0=a_1=0, then tau=2 and M_{3/4}=M_{5/4}=1/2, so (T_Q,sigma2)=(2,1/16): the coefficient is sharp. QED.

## Theorem B. A quantitative common real-image tube

For every time pair (T_P,T_Q) in the exact seedless LR/FULL common octagon H_T, every theta in [0,1], and every real eta satisfying

    |eta| <= (5/72)*(T_Q-1)*min(theta,1-theta),

the four-observer vector

    W=(e_P,e_Q,T_P,T_Q)=(1-theta+eta,theta,T_P,T_Q)

is realizable by one legal seedless LR real-randomized policy. Hence the entire displayed tube is contained in both actual observation images. Whenever T_Q>1 and theta is strictly between zero and one, the slice has a positive-width two-dimensional error neighborhood. This strengthens the previously established balanced slice eta=0.

Proof. Choose any seedless LR timing flow realizing the prescribed time pair, using the inherited exact H_T reachability lemma. Let M_r be its stopped Q-ratio histogram. Ratios satisfy 1/10<=r<=19/10, so |r-1|<=9/10. Its variance obeys sigma2>=(T_Q-1)/16 by Theorem A.

If T_Q=1, no continuation occurred: sigma2=0 and the displayed bound forces eta=0. Declare P with common probability theta. Otherwise sigma2>0. Define

    b=-eta/sigma2;    t_r=theta+b*(r-1).

The bound on eta guarantees

    |b| <= (10/9)*min(theta,1-theta),

so 0<=t_r<=1 for every ratio (including zero-mass keys). This is seedless: the P-declaration probability t_r depends only on the current likelihood ratio. Martingale normalization gives

    e_Q=sum_r M_r*t_r = theta+b*(sum_r r M_r-1) = theta;
    e_P=sum_r r*M_r*(1-t_r)
       = 1-theta-b*(sum_r r^2*M_r-sum_r r*M_r)
       = 1-theta-b*sigma2=1-theta+eta.

The timing coordinates remain the prescribed (T_P,T_Q). QED.

An explicit rational boundary point: choose g=1,a_0=a_1=0, hence (T_P,T_Q)=(2,2) and M_{3/4}=M_{5/4}=1/2. With theta=1/2 and eta=5/144, take b=-5/9, t_{3/4}=23/36 and t_{5/4}=13/36. The nonbalanced real LR observation is exactly

    W=(77/144,1/2,2,2).

The sharpness assertion concerns the variance/time constant 1/16. The tube width 5/72 is a constructive sufficient inclusion, without any maximality assertion.

## Computational verification and open unit

The published VERIFY.py uses Python standard-library Fraction to check all conditional likelihood-ratio means and conditional quadratic-variation costs. It covers all 64 deterministic seedless LR timing parameter vectors (six binary timing keys), plus 640 seeded exact-rational random timing/declaration profiles including boundary values, and verifies the sharpness and nonbalanced tube witness. EXACT_OUTPUT.txt contains the executed output. Universal quantifiers are proved analytically above; finite random tests are model-specific regression evidence.

BRC reuse: retained carrier is the positive weighted Q stopped-ratio histogram M_r; the observer is (e_P,e_Q,T_P,T_Q) and a second moment. The proof uses its exact martingale observer and a ratio-local future declaration, rather than treating the LR quotient as path-wise reversible. For this auxiliary model, the precise reuse decision is REUSE_APPLIED (inherited exact model and time-octagon theorem).

R5's mother real-image difference remains open. Any proposed gap point in this specific delta=1/4 tree must lie outside the guaranteed tube, and in particular outside its balanced slice. The next scientific unit is an exact seven-variable fiber K(W) global minimum/maximum calculation for the predecessor scalar gate F=(A+B)J-X_1*(alpha*A+beta*B), on rational W in the inherited FULL hull outside this tube. A sign-definite F on all K(W) would witness nonattainability, while a sign crossing would reconstruct a seedless LR strategy. Formal ownership, CLAIM, Result and independent review remain separate from this author-side checkpoint.
