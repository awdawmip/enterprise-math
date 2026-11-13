# PREFIX-755-R6 — Exact Bernstein-coefficient certificate for Gamma-clock stochastic monotonicity

Date: 2026-11-13 (Asia/Shanghai). Predecessor: PREFIX-754-R6, with mathematical dependency to PREFIX-712.
Scientific pin: awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d.
Scientific scope: external two-coordinate Gamma(max) auxiliary observer, using the 189-layer BRC stopped-survivor recurrence printed in research_notes/portable_direct/PREFIX754_R6_INDEPENDENT_GRID_REPLAY.py. This is not a native X6 spatial model.
Evidence status: AUTHOR_EXACT_INTEGER_FINITE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.

## Research question and exact results

PREFIX-712/753/754 use coordinatewise monotonicity of the mean and raw second moment of an independent Gamma-clock maximum to extend endpoint inequalities to closed parameter cells. This note gives an **exact integer certificate plus a continuous-parameter proof** of that analytic premise, without depending on the approximate 384×384 scan.

**Theorem 755.1 — symmetric normalized Bernstein coefficient criterion.**
For each integer 0<=n<=188, let a[n,k]>=0 be the number of surviving binary paths of length n with k successes (zero outside 0<=k<=n). Put

    b[n,k] = a[n,k] / binom(n,k).

If b[n,k]=b[n,n-k] for all k, and b[n,k+1]>=b[n,k] for 0<=k<floor(n/2), then

    S_n(p) = sum_{k=0}^n a[n,k] p^k (1-p)^(n-k)

is nondecreasing for **every real p in [0,1/2]**. If some displayed adjacent inequality is strict, S_n is strictly increasing on the full interval.

**Theorem 755.2 — finite frozen-BRC certificate.**
For the exact 189-layer frozen width predicate and stopped-count recursion, all the conditions of Theorem 755.1 hold at every n=0,...,188. The final row n=189 is identically zero. The standalone verifier checks:

| Exact finite predicate | Number |
|---|---:|
| Symmetry equalities a[n,k]=a[n,n-k] | 17,955 |
| Bernstein normalized cross-product inequalities | 8,836 |
| Strict inequalities | 4,511 |
| Equalities among the cross-products | 4,325 |
| Rows with a strict inequality (n=25,...,188) | 164 |
| Nonzero a[n,k] among rows n=0,...,188 | 9,529 |
| Nonzero entries in row n=189 | 0 |

All comparisons are exact arbitrary-precision integer comparisons; the checker enumerates the full declared finite domain. Therefore S_n(p) is nondecreasing on [0,1/2] for all n=0,...,188 and strictly increasing for n=25,...,188.

**Corollary 755.3 — conditional Gamma stochastic order and monotone moments.**
Let N_p be the bounded stopped count with P(N_p>n)=S_n(p) and 1<=N_p<=189. Conditional on N_p=m, let T_p have distribution Gamma(m,1). Then, for all real 0<=p1<=p2<=1/2 and t>=0,

    P(T_p1>t) <= P(T_p2>t).

With two independent such clocks T_p and T_z, write Y(p,z)=max(T_p,T_z). Both

    mu(p,z) = E[Y(p,z)]
    M2(p,z) = E[Y(p,z)^2]

are coordinatewise nondecreasing on [0,1/2]^2 and strictly increasing in any coordinate that increases strictly while the other remains fixed. This is the exact analytic stochastic-order premise used by the earlier Gamma cell-certificate proofs.

## Proof of Theorem 755.1 (all real parameters)

Fix n and let m=floor(n/2). For j=1,...,m define delta_j=b[n,j]-b[n,j-1]>=0. Symmetry and telescoping give

    b[n,k] = b[n,0] + sum_{j=1}^m delta_j * 1{j<=k<=n-j}.

Indeed, the included increments count the steps from the nearest endpoint to k, truncated at the central index. If K is Binomial(n,p), then

    S_n(p) = b[n,0] + sum_{j=1}^m delta_j * H_nj(p),

where H_nj(p)=P(j<=K<=n-j). Termwise differentiation of this finite polynomial yields the exact binomial-tail telescoping identity

    H'_nj(p) = n * binom(n-1,j-1) *
       [ p^(j-1)(1-p)^(n-j) - p^(n-j)(1-p)^(j-1) ].

Here n-j>=j and, on [0,1/2], 1-p>=p. The bracket is nonnegative throughout and is strictly positive for 0<p<1/2. Since all delta_j>=0, S'_n(p)>=0; if some delta_j>0, it is >0 on (0,1/2). Continuity extends the strict order to the closed interval. For n=0 or n=1 the sum is empty and S_n is constant. QED.

## Exact finite proof of Theorem 755.2

Fix W=2^18. The integer predicate printed by the frozen replay is

    inside(n,k,x) :=
       40*(n+1)*binom(n,k)*x^k*(W-x)^(n-k) > W^n.

The exact integer-bisection width predicate wide(n,k) is symmetric in k and n-k, with the same strict W/4 endpoint tests as the published PREFIX-754 independent replay. Define

    a[0,0]=1,
    a[n,k]=1{wide(n,k)}*(a[n-1,k]+a[n-1,k-1]), n=1,...,189.

The accompanying program completely reconstructs all rows through n=189. For every n<=188 and k=0,...,n it checks

    a[n,k] == a[n,n-k].

For every k=0,...,floor(n/2)-1 it checks the equivalent integer inequality

    a[n,k+1]*binom(n,k) >= a[n,k]*binom(n,k+1).

Both binomial factors are positive; thus each checked inequality is exactly b[n,k+1]>=b[n,k]. The combinatorial scope counts are

    sum_{n=0}^{188}(n+1)=17955;
    sum_{n=0}^{188}floor(n/2)=8836.

The independent run returns ALL_CHECKS_PASS PREFIX755-R6, 4511 strict adjacent comparisons, and 9529 nonzero positions before the empty final row. No floating-point values, random samples, numerical derivative estimates, or unstated parameter grid are used in these tests. These exhaustive exact integer checks establish the stated premises, and Theorem 755.1 proves the continuum consequence. QED.

## Proof of Gamma stochastic and moment transfer

For integer m>=1, the Erlang/Gamma survival function is

    P(Gamma(m,1)>t)=exp(-t)*sum_{n=0}^{m-1} t^n/n!.

Condition on N_p and exchange finite sums:

    P(T_p>t)=exp(-t)*sum_{n=0}^{188} S_n(p)*t^n/n!.

Every S_n(p) is nondecreasing; for t>0 S_25(p) is strictly increasing. Therefore the entire survival function is nondecreasing (strict for t>0 when p increases strictly).

Put H_p(t)=P(T_p>t). Independence gives

    P(Y(p,z)>t)=H_p(t)+H_z(t)-H_p(t)*H_z(t)
                =1-(1-H_p(t))*(1-H_z(t)).

For each finite t>0, H_p(t)<1. Thus this survival function is strictly increasing with either parameter when that parameter increases strictly. The standard layer-cake identities for nonnegative random variables yield

    E[Y]=integral_0^infinity P(Y>t) dt,
    E[Y^2]=2*integral_0^infinity t*P(Y>t) dt.

Their integrals are finite because the Gamma shapes are bounded by 189. Both expectations inherit strict coordinatewise monotonicity. QED.

The exact frozen Gamma cross-kernel and moment identities also follow directly from the survival integral:

    C_nm=binom(n+m,n)/2^(n+m+1);
    D_nm=(n+m+1)*C_nm;
    mu(p,z)=sum_n S_n(p)+sum_m S_m(z)-sum_nm C_nm*S_n(p)*S_m(z);
    M2(p,z)=2*sum_n (n+1)*S_n(p)+2*sum_m (m+1)*S_m(z)
            -sum_nm D_nm*S_n(p)*S_m(z).

Here integral_0^infinity exp(-2t)*t^(n+m)/(n!m!) dt=C_nm and twice the same integrand with factor t yields D_nm. This verifies the previously used analytic kernel within its original Gamma-mixture assumptions.

## Consequence, verification and open problem

For every closed rectangular cell [a,h] and every continuous point x inside it, the proved coordinate monotonicity gives

    mu(x)>=mu(a),  M2(x)<=M2(h),
    Var(Y(x))=M2(x)-mu(x)^2 <= M2(h)-mu(a)^2.

This discharges the *stochastic-order analytic premise* of the PREFIX-712/753/754 endpoint comparison, independently of their full-grid numerical certification and binary64/BLAS error model. **New certified geometry: zero cells**; the previously author-reported 140662/147456 historical union remains a separate counting claim.

Reproduction: run PREFIX755_R6_BERNSTEIN_MONOTONE_GAMMA_CHECK.py with Python >=3.10, standard library only. Its output was actually checked in this research turn; PREFIX755_R6_BERNSTEIN_MONOTONE_GAMMA_RESULTS.json records the asserted counts. All model arithmetic in this certificate is exact integer arithmetic. Formal independent review and project admission remain open.

Next useful unit: use the analytic order certificate with an exact comparator to attempt one of PREFIX-752's 6794 previously uncovered fine cells, counting each physical fine cell after deduplication; independently evaluate the numerical IEEE/BLAS premises of PREFIX-754. Preserve any active shared TASK owner/CLAIM and the immutable scientific pin.