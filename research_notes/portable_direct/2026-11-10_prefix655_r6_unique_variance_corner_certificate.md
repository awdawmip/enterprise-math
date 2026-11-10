# PREFIX-655-R6 — Exact unique variance-maximizing corner on the certified BRC rectangle

Date: 2026-11-10 (Asia/Shanghai). Mode: independent TASK_RESEARCH. Status: AUTHOR_DERIVED / EXACT_RATIONAL_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Problem and inherited frontier

For the frozen signed two-informative-direction 189-layer BRC first-stop statistical observer, write Y(p,z) for the maximum of the two Poissonized first-stop times, mu=E[Y], H=E[Y^2]/2, W=Var(Y)=2H-mu^2, and V_q(p,z)=Var(T_q)=q^2 W(p,z)-q mu(p,z). The actual observed slot values are q=12,24; the inherited analytic interpolation uses real q in [12,24].

Let I=[L,R]=[3/20,1/6], z0=19/128, h=2^-18, and Z=[z0-h,z0+h]=[38911/262144,38913/262144].

PREFIX-643 proves strict p-convexity of V_q on I x Z. PREFIX-654 establishes that for every real q in [12,24] and z in Z the unique maximizing first-coordinate edge is p=L. The remaining question is to maximize z -> V_q(L,z).

## Theorem 655.1: exact resolution of the two-dimensional compact strip

For every real q in [12,24], the function V_q has precisely one global maximizer on I x Z:

    (p*,z*)=(3/20,38911/262144).

More strongly, for all z in Z,

    dV_12(L,z)/dz < -9476,
    dV_24(L,z)/dz < -31590,

and dV_q(L,z)/dz<0 for every real q in [12,24].

At the two actual slot values the attained maxima obey strict rational bounds:

    47425.459 < max_{I x Z} V_12 < 47425.460,
    192190.134 < max_{I x Z} V_24 < 192190.135.

All comparisons are exact rational bounds for the frozen statistical observer.

## Proof: score derivatives and mean cap

Let the frozen survivor rows be rho(n,k) binomial coefficients (0<=n<=188). Define s_n(u)=sum_k rows[n,k]u^k(1-u)^(n-k). PREFIX-643's randomized-binomial score lemma gives |s_n'(u)|<20 and |s_n''(u)|<1500 on Z: the certificate checks zlo(1-zlo)>188/1500 and 188<4*20^2*zlo(1-zlo).

The exact PREFIX-622/645 moment sums are

    mu = sum_n s_n(p) + sum_m s_m(z) - sum_{n,m} w(n,m)s_n(p)s_m(z)
    H  = sum_n (n+1)s_n(p) + sum_m (m+1)s_m(z)
         - sum_{n,m} (n+m+1) w(n,m)s_n(p)s_m(z)/2
    w(n,m)=binom(n+m,n)/2^(n+m+1).

The nonnegative negative-binomial kernels satisfy sum_n w(n,m)=1 and sum_n (n+m+1)w(n,m)/2=m+1. Hence the coefficient of each s_m(z) in mu lies in [0,1], and its coefficient in H lies in [0,m+1]. Consequently

    |mu_z| < 189*20=3780,
    |mu_zz| < 189*1500=283500,
    |H_zz| < 1500*sum_{m=0}^{188}(m+1)=26932500.

An exact independent evaluation of the frozen recurrence at (L,z0) gives 103<mu(L,z0)<104. Integrating |mu_z| over |z-z0|<=h yields

    mu(L,z)<104+3780*h<105.

Differentiate W=2H-mu^2 twice:

    W_zz=2H_zz-2(mu_z)^2-2mu mu_zz.

Therefore throughout Z at p=L,

    |W_zz| < 2*26932500+2*3780^2+2*105*283500
           = 141976800.

Thus for every q>0,

    |V_q,zz(L,z)| < M_q=141976800 q^2+283500 q.

## Proof: exact center derivative and signed transfer

The companion Fraction program reconstructs all 189 survivor rows via the frozen integer bisection threshold, differentiates the exact rational survival polynomials, evaluates mu,H,mu_z,H_z, and forms V_q,z=q^2(2H_z-2mu mu_z)-q mu_z. It checks first rejection at n=25, intact rows through n=24, and extinction by n=189.

Its strict center-derivative enclosures are

    -87480.764 < V_12,z(L,z0) < -87480.763,
    -343577.977 < V_24,z(L,z0) < -343577.976.

The exact curvature transport margins are

    M_12*h = 1278003825/16384 < 78004,
    M_24*h = 2555795025/8192 < 311987.

The mean value theorem therefore gives for all z in Z:

    V_12,z(L,z)<-87480+78004=-9476,
    V_24,z(L,z)<-343577+311987=-31590.

For each fixed z, V_q,z(L,z)/q=q W_z(L,z)-mu_z(L,z) is affine in q. Strict negativity at q=12,24 entails strict negativity throughout [12,24]. Therefore z -> V_q(L,z) is strictly decreasing, with its unique maximum at z=zlo. PREFIX-654 supplies the unique maximizing p-coordinate L at every z. Combining them yields the stated unique corner, with endpoint variance enclosures obtained by the same exact moment evaluator. QED.

## Verification and provenance

The companion code uses Python 3 standard-library arbitrary-size integers and Fraction. Direct local execution of the 189-layer replay and 21 named exact assertions returned ALL_CHECKS_PASS 21. The certificate computes exact rational moment/derivative and corner-variance intervals; it does not use floating-point comparisons. No original native 96-port dynamics was rerun; scientific inputs are unchanged.

Load-bearing predecessor files:
- PREFIX-643, source commit ae7872ca18676397fcc0dd9424fb77e08928bee7 (strict p-convexity and score bound).
- PREFIX-654, current pinned source version 429849fc4985a5e3b475f09b1d446ab853a15b1b, research_notes/portable_direct/2026-11-10_prefix654_r6_single_variance_edge_strip.md (unique maximizing first-coordinate edge).
- Original 189-layer recurrence and moment identities are inherited from PREFIX-621/622/645.

BRC reuse resolution: REUSE_APPLIED (existing signed-survivor, score, moment-kernel, and first-coordinate convexity interfaces), with a new exact z-derivative endpoint certificate. This does not introduce a new native state or tool family.

## Remaining mother objective

The full two-parameter global variance maximum remains open beyond I x Z. Next: use this explicit unique maximizing corner as a certified baseline in a rigorous exclusion cover of the remaining target region; extend via adaptive Bernstein/score rectangles and compare all possible boundary maxima. Do not extrapolate this strip theorem beyond its displayed domain. Formal task CLAIM/Result/Review and independent admission are not implied by artifact persistence.
