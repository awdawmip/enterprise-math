# R5: Endpoint-inclusive five-parameter variable-kappa Blackwell prism

Date: 2026-11-08. Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Frozen model and provenance

This is directed, author-side research in the fixed seven-node P/Q-BRC terminal observer with ordered likelihood ratios r=(1/10,1/2,3/4,1,5/4,3/2,19/10). The retained observer is (e_P,e_Q,T_P,T_Q) for every randomized seven-node terminal declaration. The mother problem is whether all legal FULL_HIST flows have pointwise equivalent legal seedless LR realizations.

Predecessor: PR #1813, immutable scientific commit fc02be651e79f82db987c4160a07f87815691ad9, especially its RESEARCH.md and VERIFY_R5_ENDPOINT_MIXED.py. Scientific pins from that work are global a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e. The present proof uses that frozen seven-node scientific input family. Current P000 and behavior rules were read independently; this mathematical model is an explicitly typed terminal observer, not a physical equivalence assertion about all native X6 history.

## All-real new theorem

For every real tuple

    0 ≤ t ≤ 1/50,          0 ≤ p ≤ 77/152,
    17/2112 ≤ q ≤ 1,       0 ≤ theta ≤ 1,
    0 ≤ kappa ≤ 19/20,

let the lawful FULL_HIST flow x=(g,a,b,u,v,w,z) be

    x=(1, t, 1,
       (13t/40+1/80)p,
       9 kappa/40 + t theta/10,
       (3t/40+21/80)q,
       t theta/10).

Then the explicit target

    y=(1, 0, 1,
       u+23t/160,
       v+37t/80,
       w-17t/160,
       0)

is lawful and seedless. There is a nonnegative 7×7 declaration-independent Blackwell matrix Q with target rows i and source columns j, satisfying for every i,j=0,...,6:

    sum_j Q[i,j] = M_i(y),
    sum_i Q[i,j] = M_j(x),
    sum_i r_i Q[i,j] = r_j M_j(x).

Here M is the exact Q-node mass map below. Also T_P(y)=T_P(x), T_Q(y)=T_Q(x). Consequently the terminal declaration under both P and Q and both expected stopping times are preserved exactly, for every randomized seven-node terminal declaration.

For every real h in [0,1], the interpolant (1-h)x+hy has the same four observables, with valid Blackwell kernel (1-h)Q+h diag(M(y)).

The source history residual is R=(9t/10)(theta-kappa). The family contains strictly positive, strictly negative, and zero residual mixed-side flows.

## Proof I: capacities, seedless identity, and times

The source is lawful by its physical-parameter definitions. The target has a'=z'=0 and hence satisfies the seedless LR relation 9b'z'=4a'(v'-z') exactly. Its required bounds are

    0 ≤ u'=(13t/40+1/80)p+23t/160 ≤ 1/80,
    0 ≤ w'=(3t/40+21/80)q-17t/160 ≤ 21/80,
    0 ≤ v'=9 kappa/40+t(theta/10+37/80) ≤ 9/40.

The first two follow by monotonic extrema in t,p,q. The last uses the exact boundary identity

    9(19/20)/40 + (1/50)(1/10+37/80) = 9/40.

Thus κ=19/20 is an exact capacity face for this *chosen target* over the whole displayed box. It is not asserted as a global seedless infeasibility result.

For any f=(g,a,b,u,v,w,z),

    T_P(f)=1+g+3a/8+5b/8+u/2+v+3w/2;
    T_Q(f)=1+g+(a+b)/2+u+v+w.

Their changes x→y vanish identically:

    T_Q(y)-T_Q(x)=t(-1/2+23/160+37/80-17/160)=0;
    T_P(y)-T_P(x)=t(-3/8+23/320+37/80-51/320)=0.

## Proof II: exact transfer and all-real multiaffinity

The frozen seven-node Q-mass laws are

    M0=509u/900+47z/180+67(v-z)/162+w/100
    M1=13a/40+b/80-u
    M2=(g-a)/2
    M3=1-g+a/10+9b/40-v+191(u+w)/450+43z/90+14(v-z)/81
    M4=(g-b)/2
    M5=3a/40+21b/80-w
    M6=u/100+47z/180+67(v-z)/162+509w/900.

For each t=1/50 and each of the 16 combinations of p∈{0,77/152}, q∈{17/2112,1}, theta∈{0,1}, kappa∈{0,19/20}, the original four sparse support patterns from PR #1813 reconstruct a *unique strictly positive rational* Blackwell Q solving all 7 target-row, 7 source-Q-column, and 7 source-P-column equations. The 16 kernels have 192 positive edges in total; the minimum edge over all endpoints is exactly 17/800000. A standalone Fraction-only exact checker is included in VERIFY_KAPPA_PRISM.py and rebuilds every matrix from support and equations, rather than reading fitted floats.

At t=0, for all 16 remaining parameter corners, x=y and the Q mass diagonal is a valid identity kernel.

Set normalized parameters

    lambda=50t; beta=152p/77;
    gamma=(q-17/2112)/(1-17/2112);
    epsilon=theta; xi=20kappa/19.

The product weights for (lambda,beta,gamma,epsilon,xi)∈[0,1]^5 are nonnegative and sum to 1. Both x and y are separately affine in all five parameters (the only products tp, tq, t theta are multiaffine). So x,y, all Q-node masses, the two stopping times and the 21 kernel constraints exactly interpolate from their 32 corner values. The nonnegative combination of the 32 corner Blackwell matrices therefore gives a valid transfer everywhere in the real five-parameter box. All target rows retain a'=z'=0, so the seedless identity is stable under this interpolation. This proves the theorem for all real parameters, including irrational interior points and boundaries.

## Local execution evidence and its scope

Two distinct Fraction-only computational formulations were exercised, one using an explicit 32-corner checker and one reusing the earlier PR #1813 supports with the additional kappa variable. The first actually returned:

    EXACT_16_T_ZERO_IDENTITY_CORNERS_PASS
    EXACT_16_T_POSITIVE_CORNERS_PASS 192 POSITIVE_EDGES MIN_EDGE 17/800000
    EXACT_151_INTERIOR_INTERPOLATION_CHECKS_PASS
    AUTHOR_PROVED_R5_ALL_REAL_FIVE_PARAMETER_KAPPA_PRISM

The published standalone verifier is a directly extended, complete Fraction-only version of the predecessor's checker. Execute it using python3 VERIFY_KAPPA_PRISM.py. The all-real result follows from exact 32-vertex rational certificates plus algebraic multiaffinity; 151 rational interior points are regression checks. Author-side proof only; independent review and formal admission remain separate.

## Next mathematical unit

First test the remaining boundary corner (t,p,q,theta,kappa)=(1/50,77/152,17/2112,1,1) with a new legal seedless target (possibly positive a'); the displayed a'=0 target saturates at κ=19/20. Then separately enlarge p beyond 77/152 and q below 17/2112, which hit the current target's exact capacity faces. A suitable second chart may overlap the current five-parameter prism. Preserve previous verified certificates and the exact 4-observable mother objective.

Control: GitHub author awdawmip. No formal Task CLAIM, Result, Review, independent acceptance or native identity is inferred from Git publication. The service-issued session/activity, if obtained, must be recorded from the actual native receipt.
