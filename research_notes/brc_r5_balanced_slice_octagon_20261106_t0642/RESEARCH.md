# R5: Exact time octagon, balanced-error equality slice, and pooling-residual hexagon

Date: 2026-11-06 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Mother problem and fixed sources

R5 seeks a strictly positive rational finite P/Q stopping tree with equal FULL_HIST and seedless LR four-observer convex hulls but different actual real-behavior images. Frozen scientific sources: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. The positive delta=1/4 kernel and four-observer affine lift are inherited from EM 57f7d654e5dd002567e0b0d333937e6e38f3b4cb, research_notes/brc_r5_scalar_nonlumpability_gate_20261106_t0343/RESEARCH.md; the immediately preceding fixed-flow result is EM dd2b5d8e2ec5d92b7efd01a951a86664507245bd. The earlier 80-halfspace four-dimensional hull certificate is an inherited, author-side dependency.

This is an auxiliary P/Q likelihood-ratio BRC observer, not a native Heartbeat X6 dynamics claim. The historical split and future declaration operations are retained in the FULL model, and pooling is performed only for the declared LR observation.

Let W=(e_P,e_Q,T_P,T_Q). The Q stop-ratio masses M_r satisfy sum M_r=1 and sum r*M_r=1. If t_r is the P-declaration probability at stopped ratio r, then e_Q=sum M_r*t_r and e_P=1-sum r*M_r*t_r.

## Theorem 1: the exact stopping-time octagon

In the inherited delta=1/4 model, both FULL_HIST and seedless LR realize exactly the same convex polygon H_T of real stopping-time pairs (T_P,T_Q). Its eight counterclockwise vertices are:

    (1,1)
    (483/160,221/80)
    (519/160,239/80)
    (613/160,293/80)
    (4,4)
    (559/160,293/80)
    (211/80,117/40)
    (203/80,113/40)

An exact halfspace description, with each LHS >= RHS, is:

    -282*T_P + 323*T_Q >= 41
    -160*T_P + 160*T_Q >= -41
    -216*T_P + 188*T_Q >= -139
      -2*T_P +     T_Q >= -4
       2*T_P -   3*T_Q >= -4
     236*T_P - 274*T_Q >= -179
      80*T_P -  80*T_Q >= -23
     146*T_P - 123*T_Q >= 23

Proof. Let g be root continuation, 0<=u_0,u_1<=g<=1, and V_j=(q3[0,j]*u_0+q3[1,j]*u_1)/2, with q3[0]=(13/20,1/5,3/20), q3[1]=(1/40,9/20,21/40); put 0<=X_j<=V_j. The stopped-time coordinates are affine:

    T_Q=1+g+(u_0+u_1)/2+X_0+X_1+X_2,
    T_P=1+g+(3*u_0+5*u_1)/8+X_0/2+X_1+3*X_2/2.

Every feasible flow can be realized by a seedless timing policy: at root use g, at time 2 use u_i/g if g>0 and zero otherwise, and at the shared time-3 ratio key j use X_j/V_j if V_j>0 and zero otherwise. FULL_HIST has the identical time projection by pooling its historical flows to X_j. The flow region is a compact convex polytope. Every randomized timing policy is a convex combination in occupation-mass coordinates of deterministic timing policies at the six timing nodes; conversely a convex combination of feasible deterministic flows remains feasible and reconstructs a randomized LR policy. Therefore H_T is the convex hull of the 64 deterministic timing images. Exact rational enumeration yields 26 distinct points and exactly the eight vertices above. The eight listed halfspaces are the primitive integer supporting inequalities of consecutive vertex pairs; all 64 points satisfy all eight. Hence they describe H_T exactly, including real randomized probabilities and boundary cases.

## Theorem 2: a globally shared balanced-error slice

For every (T_P,T_Q) in H_T and theta in [0,1], both FULL_HIST and seedless LR realize

    (e_P,e_Q,T_P,T_Q)=(1-theta,theta,T_P,T_Q).

Moreover,

    O4(FULL_HIST) intersect {e_P+e_Q=1}
      = O4(seedless LR) intersect {e_P+e_Q=1}
      = { (1-theta,theta,T_P,T_Q) : theta in [0,1], (T_P,T_Q) in H_T }.

Proof. Implement the chosen time pair with the LR flow from Theorem 1. Independently declare P with the common probability t_r=theta at all stopped ratios. Because both total Q stop mass and total P stop mass equal one, e_Q=theta and e_P=1-theta. Conversely, a FULL observation satisfying e_P+e_Q=1 has theta=e_Q in [0,1] and an attainable time pair, giving exactly the claimed reconstruction. This is a global equality of the entire balanced slice, not a fixed-flow approximation.

## Theorem 3: two-mode loss and exact hexagon

At any fixed FULL timing flow, let J denote its central history-dependent terminal coefficient and J_LR its shared-ratio pooling coefficient. Define epsilon=J-J_LR. Keep the same probabilities t_r of declaring P at every stopped ratio in FULL and in its pooled LR policy. The stop-time coordinates are identical. The only Q stopped-ratio mass change is epsilon*(1,-2,1) at the ratios (1/10,1,19/10). Writing t_-,t_0,t_+ for their declaration probabilities:

    Δe_Q = epsilon*(t_- - 2*t_0 + t_+),
    Δ(e_P+e_Q) = (9/10)*epsilon*(t_- - t_+).

If epsilon != 0, the two full four-observer outputs under this same-flow and same-declaration pooling coincide if and only if t_-=t_0=t_+.

As (t_-,t_0,t_+) range over [0,1]^3, the complete residual set in (Δe_P,Δe_Q) is the centrally symmetric hexagon

    epsilon*conv{ +/-(-1/10,1), +/-(2,-2), +/-(-19/10,1) }.

The hexagon has exact area (27/5)*epsilon^2. Both coordinate magnitudes are at most 2*abs(epsilon), sharply. Using the earlier exact sharp bound abs(epsilon)<=19/1800 gives a uniform residual area bound 361/600000 and sharp coordinate bound 19/900 for this particular same-declaration pooling comparison.

Proof. Direct substitution into the two error definitions gives the identities. The linear map from (t_-,t_0,t_+) has columns epsilon*a, epsilon*b, epsilon*c with a=(-1/10,1), b=(2,-2), c=(-19/10,1), and a+b+c=0. The eight binary cube images are the origin twice and the six distinct outer points +/-epsilon*a, +/-epsilon*b, +/-epsilon*c. Their convex hull is the entire image zonotope, and all three absolute pairwise determinants equal 9/5, so its area is 3*(9/5)*epsilon^2. When epsilon!=0, vanishing of the two independent displayed differences forces t_-=t_+ and t_0=(t_-+t_+)/2, hence all three equal. The prior bound on epsilon is attained by the previously identified extreme historical split; the choices (t_-,t_0,t_+)=(1,0,1) and (0,1,0) attain the coordinate bounds.

## Exact evidence, scope, next problem

VERIFY.py uses standard-library Fraction, enumerates all 64 deterministic timing policies, checks 26 distinct points, the eight exact vertices and their facet inequalities, and verifies 600 reproducible rational FULL profiles (including 0/1 boundary probabilities). Each profile checks stopped-ratio mass, total P/Q normalization, model pooling, the two exact defect modes and the balanced declaration slice. The hexagon area and sharp upper bound are rational identities. Actual executed output: PASS_EXACT_R5_BALANCED_SLICE_TIME_OCTAGON_RESIDUAL_HEXAGON; see EXACT_OUTPUT.txt. The theorems are analytical plus complete finite polygon enumeration; randomized trials are regression checks.

The R5 mother question remains open. Next, use the exact eight time facets to stratify candidate rational W in the inherited FULL hull. The entire e_P+e_Q=1 slice is now proved common and may be set aside in image-gap searches. For e_P+e_Q != 1, form the seven-variable global fiber K(W) from the earlier affine stop-mass lift, certify global min/max of F=(A+B)*J-X_1*(alpha*A+beta*B), and either produce a sign-definite real-image counterexample or an explicit LR reconstruction. Formal owner/CLAIM and independent Driver review remain separate from this portable author-side proof.
