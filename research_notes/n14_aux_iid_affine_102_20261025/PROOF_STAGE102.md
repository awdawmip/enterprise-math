# Stage102: exact real minimax interval with sharp right end (external iid N=14)

**Scientific classification:** AUTHOR exact-rational computation-assisted proof (two author-written checking implementations), not independent Research Driver review, not native Result/CLAIM, not a native P000/X6/BRC theorem. Frozen input: Stage101 PROOF_STAGE101.md and NEXT_TASK_PACKET_102.md at enterprise-math main@22a83b434187eb4fad90bdec903d91e7417ff4fc. Global Knowledge snapshot main@b034e5f7f3f65b3086830e7e3f8d53b28a382be4; P000 original blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc, startup projection matched.

## Mathematical statement

The observations X are iid with P=(1/8,1/24,5/6) and Q=(1/12,1/12,5/6). A randomized test can use the *complete ordered history* and must stop by tau<=14. Let eP=P(decide Q), eQ=Q(decide P), tP=E_P(tau), tQ=E_Q(tau), and V14(alpha)=min max(tP,tQ) subject to eP,eQ<=alpha. Stage101 established

    alpha101=152150366213667431/438244169232678912
    V101=44227501292577155/3423782572130304.

**Stage102 theorem (author calculation-assisted):** For *every real* delta with

    0<=delta<=eta102=48855870625/9700717287702528,

the exact optimum is

    V14(alpha101+delta)=V101-Gamma102*delta,
    Gamma102=187763606856/78169393.

The sharp right end of THIS supporting line is

    alpha102=2586593746940986327/7450150876955541504
    V102=751163408448101635/58204303726215168.

The same support line is unattainable at any alpha>alpha102. No later segment or native transfer is asserted.

## 1. Dual Bellman proof for arbitrary full ordered-history tests

Write v=(n,a,b) for the observation count state and L(v)=2^(a+b)/3^a for the prefix likelihood ratio Q/P. Fix

    K=lambdaQ=96424629120/78169393,
    lambdaP=91338977736/78169393=72+(8/9)K.

Define D(v) by backwards exact Fraction recursion: decide P costs K*L(v); decide Q costs lambdaP; continue costs 1+(1/8)D(n+1,a+1,b)+(1/24)D(n+1,a,b+1)+(5/6)D(n+1,a,b), omitted at n=14. D is the minimum of the available actions.

Conditional iid futures and prefix likelihood ratios depend only on v. Backwards induction over *all ordered histories*, including history-specific randomization, proves

    D(root)<=tP+lambdaP*eP+K*eQ.

The exact computation checks 680 states and every one of 1240 nonselected-action gaps: 1238 strictly positive, zero negative and only two equal-action pairs:

    A=(5,0,2): immediately decide Q vs continue;
    B=(12,0,1): immediately decide Q vs continue.

All others are strictly optimized. Exact dual root:

    D(root)=3626353483971594146819209007/4282160086838473289367552
           =V101+(lambdaP+K)*alpha101.

Thus for every alpha, V14(alpha)>=V101-Gamma102*(alpha-alpha101).

## 2. Verified ordered first-hit cones and suffix data

The strict-optimal prefix tree has exactly 10 genuine ordered first arrivals at A and 12 at B (binomial coefficients choose(5,2), choose(12,1)), with P and Q masses

    pA=625/62208, qA=625/15552,
    pB=48828125/725594112, qB=48828125/362797056.

**Disjointness is analytic, not an unchecked computational assumption.** The count b of symbol 1 cannot decrease. A has b=2 and B has b=1, hence A cannot precede B; B cannot precede A since depth 12>5. Therefore their ordered path cones are disjoint and there are no interaction/cross terms.

If we continue at the tie and use all later strict optimizers, the conditional suffix tuples (P-error,Q-error,P-extra-time,Q-extra-time,number of terminal ordered suffixes) are

    RA=(8102662423/8153726976,1489889/1289945088,1650008497/1019215872,145197871/107495424,685);
    RB=(63/64,1/144,9/8,13/12,5).

The independent ordered-prefix checker separately traversed 1,039,336 ordered prefix nodes with 692,903 terminal stopping paths for the start policy and 1,029,076 nodes with 686,063 paths for the end policy, confirming the exact endpoint errors, durations and first-hit masses without aggregating histories in its forward pass.

## 3. Feasible randomized primal equality for every real u

At the Stage101 endpoint policy, continue at A, decide Q with probability

    s101=1033425075169483/1228800000000000

at B (otherwise continue), and use strict minimizing actions elsewhere. Its exact outcome is

    (eP,eQ,tP,tQ)=(alpha101,alpha101,V101,449462455858132795/36520347436056576).

For 0<=u<=1, decide Q at A with probability u, continue otherwise. At B decide Q with probability s, continue otherwise. Set

    XA=pA*(1-RA.Perror)=31915345625/507227047723008,
    YA=qA*RA.Qerror=931180625/20061226008576,
    EB=pB*(1-RB.Perror)=48828125/46438023168,
    HB=qB*RB.Qerror=48828125/52242776064.

By disjointness, the error perturbations are EXACT, without omitted cross terms:

    eP-alpha101=XA*u+EB*(s-s101),
    eQ-alpha101=-YA*u-HB*(s-s101).

Equality eP=eQ is equivalent to

    s=s101-h*u, h=(XA+YA)/(EB+HB)=1437504293/26112000000.

Both probabilities are legal throughout u in [0,1], since

    s(1)=16418222843481211/20889600000000000 >0.

The common error is

    eP=eQ=alpha101+eta102*u,
    eta102=XA-EB*h=48855870625/9700717287702528 >0.

Every randomized action is a Bellman minimizer, hence the dual identity is attained:

    tP+lambdaP*eP+K*eQ=D(root).
    tP=V101-Gamma102*eta102*u.

The difference tP-tQ is affine in u because the cones are disjoint, with strictly positive endpoint values:

    u=0: 66892673788070575/109561042308169728;
    u=1: 400265986153999925/620845906412961792.

Consequently max(tP,tQ)=tP over *every real* u in [0,1]. Put delta=eta102*u to prove the whole exact minimax interval.

## 4. Sharpness of this supporting line

The space of finite-horizon randomized ordered-history tests is compact, so an optimum is attained. If any alpha>alpha102 attained the displayed line, the positive multipliers force eP=eQ=alpha and action-by-action Bellman equality at all reached histories. There are only the two tie states A and B. Across ordered histories within each count state, Q/P ratio and the conditional iid suffix outcomes are identical, so any history-specific tie choices can be replaced, with no change in either error or duration, by their first-arrival P-mass-weighted average probabilities u,s. The two tie cones are disjoint. Error equality forces s=s101-h*u, with 0<=u<=1. Thus alpha=alpha101+eta102*u<=alpha102, contradiction. Right sharpness follows.

## 5. Actual verification and reproducibility

Actual **locally executed** programs (same author, differently implemented):
- CHECKER_STAGE102.py: exact rational bottom-up DP for 680 states/1240 comparisons; suffixes, ordered first-hit masses by P/Q-weighted forward propagation, baseline/end/interior policies, rational certificates.
- INDEPENDENT_ORDERED_STAGE102.py: independently written top-down dynamic Bellman plus a full ordered-prefix DFS, independent exact endpoint outcomes/first-hit counts and tP>tQ.
- STAGE103_DUAL_SCAN.py: fixed-policy affine gaps on [K103,K102] to identify the next **dual-only** candidate.

The source code, exact JSON certificates, complete proof and manifest are in the corresponding attached Stage102 reproducible research packet. The full locally executed packet has 680 Bellman states, 1240 nonselected comparisons, 1238 positive, two exact ties, zero negative; both author checkers passed. No independent mathematical reviewer, formal verification, Source-native Researcher role, native Result or P000 transfer is claimed.

## 6. Next genuinely open research unit

On the same pencil lambdaP=72+(8/9)K and on the post-kink Stage102 policy, exact affine gap calculations on both endpoints yield

    K103=152847928260/128768917,
    C103=(6,2,3): continue vs decide Q.

The 1240 fixed-policy gaps are nonnegative throughout [K103,K102]; there is no earlier kink on this **specific** dual pencil. This is a dual-only candidate, NOT a Stage103 primal proof. Next: compute genuine C103 and B ordered first-hit masses, suffix distributions, feasible error balancing, global Bellman equality and right sharpness.

## 7. Source and permission scope

Current GitHub connector identity: awdawmip. Native control read returned CONTROL_QUOTA; an actual native em_session_start attempt returned STATIC_READONLY_SCOPE_DENIED, operation_sent=false. These are native permission results, not a GitHub content-writing failure and not evidence of no active owner. This note is a plain author research checkpoint and cannot substitute formal CLAIM/Result or independent review. Native P000 X6 space, time, three-dimensional slices and residual provenance remain protected; the auxiliary iid theorem has no established native embedding/readout/preservation map. BRC-native arithmetic is not invoked in this external iid exact-rational calculation.

**Scientific state:** STAGE102_AUTHOR_EXACT_AFFINE_PROVED / REAL_INTERVAL_AND_RIGHT_SHARPNESS / TWO_AUTHOR_CHECKS_PASS / STAGE103_DUAL_ONLY / NATIVE_REVIEW_PENDING.
