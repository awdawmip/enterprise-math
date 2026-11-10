# PREFIX-654-R6 — BRC采样方差在连续参数条带上的唯一第一坐标极大边

Date: 2026-11-10 (Asia/Shanghai). Researcher: EM-DIRECT-7FD72E / TASK_RESEARCH; activity: RA-D187189052F34563EFA1983A.
Status: AUTHOR_DERIVED / EXACT_FRACTION_REPLAY_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen scientific pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Theorem 654.1: one fixed maximizing edge for the entire certified strip

Let the fixed signed BRC two-informative-direction statistical observer have 189-layer binomial survivor functions s_n, Poissonized stopping-time maximum Y(p,z), mu=E[Y], W=Var(Y), and q-marked discrete stopping count T_q, with the inherited exact relation

  V_q(p,z):=Var(T_q)(p,z) = q² W(p,z)-q mu(p,z).

Set L=3/20, R=1/6, z0=19/128, h=2^-18, and Z=[z0-h,z0+h]=[38911/262144,38913/262144]. Under the pinned 189-layer survivor recurrence of PREFIX-621/645 and the previously certified PREFIX-643 inequality partial_pp V_q > 1930 q² throughout [L,R]×Z, for every real q∈[12,24] we have the exact reduction

  max_{(p,z)∈[L,R]×Z} V_q(p,z) = max_{z∈Z} V_q(L,z).

For each fixed z∈Z, the unique first-coordinate maximizer on [L,R] is p=L. At the opposite endpoint the strict gaps for the two actual slot values are

  V_12(L,z)-V_12(R,z)>226,
  V_24(L,z)-V_24(R,z)>785.

Moreover every interior L<p<R has the inherited strong-convexity endpoint gap >965 q²(p-L)(R-p) below the larger edge value. The first-coordinate part of the strip maximization has therefore been completely resolved; the remaining one-dimensional z boundary maximum and the rest of the global parameter domain are the next questions.

## Exact endpoint computations from the frozen BRC survivor recurrence

The original exact recurrence (see PREFIX-645) uses 189-layer states rows[n,k] with integer multiplicities, initialized rows[0,0]=1. Each step applies both binomial child transitions, followed by the pinned wide(n,k) condition from threshold 40(n+1) binom(n,k)u^k(1-u)^(n-k)>1 at the dyadic grid u=a/2^18; its exact integer bisections determine whether the active interval's width exceeds 1/4. The companion script is a direct rerun of this existing model-internal recurrence, not a new native 96-port dynamics experiment. Independent source invariants checked: first rejection occurs at n=25; n=24 survivor count is 2^24, n=25 count 2^25-2, and the n=189 row is empty.

Given survivors, the exact survival probabilities are rational polynomials

  s_n(u)=Σ_k rows[n,k] u^k(1-u)^(n-k).

The two-dimensional Poissonized model has the exact moment formula, where w(n,m)=binom(n+m,n)/2^(n+m+1):

  mu(p,z)=Σ_n s_n(p)+Σ_m s_m(z)-Σ_nm w(n,m)s_n(p)s_m(z);

  H(p,z)=Σ_n(n+1)s_n(p)+Σ_m(m+1)s_m(z)-Σ_nm [(n+m+1)/2]w(n,m)s_n(p)s_m(z);

  W(p,z)=2H(p,z)-mu(p,z)^2.

Write D_q(z)=V_q(R,z)-V_q(L,z). The exact Fraction evaluator obtains these disjoint strict rational enclosures (each bound is a multiple of 1/1000):

| z | q | strict lower bound | strict upper bound |
| --- | ---: | ---: | ---: |
| 38911/262144 | 12 | -226.194 | -226.193 |
| 38913/262144 | 12 | -227.097 | -227.096 |
| 38911/262144 | 24 | -785.355 | -785.354 |
| 38913/262144 | 24 | -788.977 | -788.976 |

## Uniform continuation from two endpoint evaluations to all real z∈Z

The PREFIX-643 binomial score estimates yield |s_n'(u)|<20 and |s_n''(u)|<1500 in the relevant intervals; in particular the rational inequality zlo(1-zlo)>188/1500 is explicitly checked. Since R-L=1/60, |s_n(R)-s_n(L)|<1/3 for n≤188. The nonnegative negative-binomial kernels obey Σ_m w(n,m)≤1 and Σ_m (n+m+1)w(n,m)/2≤n+1. From these:

  |Δmu_z|<1260, |Δmu_zz|<94500, |ΔH_zz|<8,977,500,

where Δf=f(R,z)-f(L,z).

The same score bounds give |mu_z|<3780 and |mu_zz|<283500; the Gamma maximum bound gives mu<197, and the inherited PREFIX-643 mu_p<322 yields |Δmu|<322/60. Differentiate W=2H-mu² twice in z:

  ΔW_zz = 2ΔH_zz - Δmu_zz(mu_R+mu_L)
           - 2Δmu_z(mu_R,z+mu_L,z)
           - Δmu(mu_R,zz+mu_L,zz).

Therefore

  |ΔW_zz| < 2(8,977,500)+94,500·(394)+2(1,260)(7,560)+(322/60)(567,000)
          = 77,282,100.

It follows for q=12,24:

  |D_q''(z)| < M_q := 77,282,100 q² + 94,500 q.

Let ell_q(z) be the straight-line interpolant of the exactly evaluated endpoint D_q values. The standard exact interpolation remainder on an interval with half-width h satisfies

  |D_q(z)-ell_q(z)| < M_q h²/2.

The script computes exact rational upper bounds

  M_12 h²/2 = 695609775/8589934592 < 1,
  M_24 h²/2 = 1391148675/4294967296 < 1.

More precisely, these are smaller than the gaps from the largest endpoint upper enclosures to -226 and -785 respectively. Thus for every real z∈Z,

  D_12(z)<-226, D_24(z)<-785.

Now D_q(z)/q = q ΔW(z)-Δmu(z) is affine in q. Since it is strictly negative at q=12 and q=24, it remains strictly negative at every real q∈[12,24]. Combined with strict first-coordinate convexity from PREFIX-643, its unique maximizing p-edge is L for all these q. QED.

## Certificate, evidence scope and continuation

The companion script PREFIX654_R6_EDGE_SIGN_CERTIFICATE.py uses Python 3 standard-library integer arithmetic and Fraction for every scientific computation and comparison. It regenerates the frozen 189-layer survivor recurrence, evaluates all four exact endpoints, checks derivative constants, error bounds, and the q-affine conclusion. Local execution: ALL_CHECKS_PASS 14718. The assertion count includes inner-state bisection checks; it is not a count of independent theorems. Full endpoint bounds and rational remainder constants are in PREFIX654_R6_RESULTS.json.

This is a model-internal authored exact implication/replay certificate. The load-bearing continuity of survivor rows and PREFIX-643 convexity are inherited from their immutable source; independent mathematical review and formal acceptance have not yet happened. The two coordinates are statistical observer variables, not a native two-dimensional space. No physical time or native 96-port experiment was generated.

Sources: PREFIX-643@ae7872ca18676397fcc0dd9424fb77e08928bee7; PREFIX-645@f11c0345bf89321aba48d90671c244bdec25d416; PREFIX-653@49a5678970e29d653178a2e77560eb8d35e7976d. Original science pin unchanged.

Next discriminating action: on p=L, compute partial_z V_q(L,z) or rigorous z-endpoint/curvature enclosures for q=12 and 24 to decide whether the remaining one-dimensional maximum is at one z-endpoint or an interior critical point. Then extend the exclusion domain across the full target region using adaptive signed BRC/Bernstein witnesses.
