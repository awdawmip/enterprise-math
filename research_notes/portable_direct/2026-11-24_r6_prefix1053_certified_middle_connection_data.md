# PREFIX-1053 — Certified rational connection data at the critical point 16

Date 2026-11-24. Parent PREFIX-1052. AUTHOR_CONDITIONAL_ANALYTIC_PROOF / EXACT_RATIONAL_CHECKED / NOT_REVIEWED.

## Scope and immutable inputs

Frozen P000 V5 f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json; retain Stage46 signed W=J12−6I12, incoming −e1, bidirectional exclusion of Link {0,e1}, exactly one outgoing negative step, full native X6 Cell–terminal-port–grade, branch identity, sign, multiplicity and provenance. This note only evaluates an inherited auxiliary scalar ODE connection certificate, without a new phase sample, pi calculation, native evolution or classical comparison experiment. NATIVE_ATTRIBUTION_PENDING_BRC_REVALIDATION. Mother B_fix,odd(32) in {19,20} remains open.

Actual immutable reads:
- PREFIX-1052 de0250c78a0952c5b282623dacedce81c47bad90:research_notes/portable_direct/2026-11-24_r6_prefix1052_exact_critical_connection_and_middle_analytic_branch.md (ODE, critical connection, existence of analytic background and cusp coefficient).
- PREFIX-1051 3e6750ea4c429cab0758e35b6292d2bcb59a1da0:research_notes/portable_direct/PREFIX1051_R6_CRITICAL_TAIL_CHECK.py (upper scaled recurrence and critical tail certificate).

Use the normalized middle analytic functions f=F/c, v=V/c from PREFIX-1052; c is its positive inherited upper-edge coefficient. At t=y−16, f(16+t)=sum_{j=0}^3 Q_j R_j(t), where [t^i]R_j=delta_ij for 0<=i<=3. On the right the physical density is c[f+(27/2)t^(3/2) C16(t)], and U'= (y−6)rho.

## Main result

The following closed rational intervals enclose the exact connection data (divide all displayed integer endpoints by 10^6):
| quantity | lower numerator | upper numerator |
|---|---:|---:|
| Q0 | 326281872 | 326281873 |
| Q1 | -73882460 | -73882459 |
| Q2 | 2998263 | 2998264 |
| Q3 | -148957 | -148956 |
| v(16) | -24327338758 | -24327338757 |

The internally computed common Q error bound is < 1e-8 (diagnostic 3.58910e-16); the v error bound < 1e-7 (diagnostic 3.80073e-13). The integer endpoints above are calculated by exact floor/ceiling, not by rounding diagnostic floats. This supplies all five real initial parameters for the middle branch (four free analytic density jets and one primitive constant), without inferring the missing native observer correspondence.

## 1. Uniform tail via inverse convolution (new tool)

Let a_j(y) be the six coefficients in PREFIX-1052, A_j(t)=a_j(16+t), and alpha=0 or 3/2. Write a local solution as t^alpha sum b_n t^n and d_n=5^n b_n. Then for n>=4 (analytic) or n>=1 (cusp):
W_k(n)=5^k sum_{j=0}^5 [t^(k−4+j)] A_j(t) (n−k+alpha)_j,
where (x)_j is falling factorial and k=0..7. The recurrence is sum W_k(n)d_(n−k)=0, with out-of-range negative coefficients zero. Let l_k be the leading-coefficient ratio −LC(W_k)/LC(W_0) for k>=1. Exact expansion gives
1−sum l_k z^k=(1+5z/12)(1+5z/16)^5(1−z/4).
Hence the causal inverse convolution has absolute sum <=
K=1/[(7/12)(11/16)^5(3/4)].
This preserves the signed recurrence structure instead of demanding sum|l_k|<1.

Set N=300, D(z)=sign(LC(W_0)) W_0(N+z). Every coefficient of D is positive. For each k, e_k=max_{0<=j<=5} |[z^j]sign(LC(W_0))(-W_k(N+z)−l_k W_0(N+z))|/[z^j]D. Therefore |−W_k(n)/W_0(n)−l_k|<=e_k for every real n>=N. Exact coefficient comparison gives K e<1, e=sum e_k, for both alpha values.

For any finite prefix of the tail let M be its maximum modulus and B=max_{N−7<=n<N}|d_n|. Extend the tail by zero before N. Its forcing under the limiting convolution is bounded by (sum|l_k|+e)B+eM, including contributions across the initial boundary. Causal inversion yields M<=K[(sum|l_k|+e)B+eM]. Since the bound is independent of the finite prefix, for every n>=N,
|d_n|<=T=K(sum|l_k|+e)B/(1−Ke).
This is an all-order bound, not a sampled tail. It also applies to other finite-width rational recurrences whose limiting polynomial has a summable causal inverse and an explicit perturbation margin.

For t=4, q=4/5. For every derivative k<=4 the omitted series terms are bounded in absolute sum by fac*T*q^N*(N+2)^4/(18/100), fac=1 or 8 for alpha=0 or 3/2. Indeed the falling factorial magnitude <=(n+2)^4 and q*((N+3)/(N+2))^4<82/100. The integral from 0 to 4 of (10+t) times the series has tail <=56*fac*T*q^N/(1−q). The finite prefix uses exact fractions. Diagnostics of the uniform local error: R0 2.95139e-134, R1 2.16234e-132, R2 4.33887e-130, R3 7.59632e-129, cusp 2.60532e-132. All are less than 1e-12.

## 2. Upper connection data

Reuse the exact upper Frobenius recurrence and fixed-point residual propagation of PREFIX-1051 at scale 20, through n=2999, with integer scale 10^800. The maximum certified finite coefficient error is <10^-200. The transformed terminal estimate is checked again: H<162/10^10. The inherited all-order polynomial bound gives |20^n b_n|<=H for n>=3000. For n>=300 use T_up=max(H, max_{300<=n<3000} certified absolute coefficient bound). At x=16 use q=4/5, fac=64 and the same derivative bound as above, with a sign (−1)^k for y derivatives. The primitive at y=20 equals
U(20)/c=sum (20^n b_n) q^n *64*(256/(n+7/2)−480/(n+5/2)).
Its tail <=64*736*T_up*q^300/(1−q). The maximum of the derivative and integral bounds plus 10^-180 covers also the finite directed fixed-point residual (300 terms, each bounded by 10^-200 times the displayed factors). Actual upper uniform error diagnostic 9.20074e-23 < 1e-12. This relies on the previously published half-line contraction certificate; no new upper positivity claim.

## 3. Certified connection solve

At y=20 form a 4x4 matrix from derivative orders 0..3 of R_j at t=4 and right-hand side from the corresponding upper density derivatives minus (27/2) cusp derivatives. Round finite rational evaluations downward on a 10^-20 grid, giving A0,b0; define eta=max local error+10^-20 per matrix entry, eb=upper error+(27/2)cusp error+10^-20 per right-hand entry. Invert A0 exactly, with infinity norm L of its inverse. The checker establishes 4L eta<1; hence the true matrix is invertible by the Neumann estimate. Qhat=A0^-1 b0, and
||Q−Qhat||_infty <= L(eb+4eta||Qhat||_infty)/(1−4L eta).
The existence of the full five-derivative connection is inherited from PREFIX-1052; only the first four equations are needed after invertibility is certified. The fifth equation was not independently certified in this run.

For v(16), subtract the integrated cusp and analytic contributions from U(20)/c. If I_j are finite approximations to integral_0^4 (10+t)R_j(t)dt, the propagated error is upper error+(27/2)cusp error+sum_j[Qerror*|I_j|+(|Qhat_j|+Qerror)*localerror_j]. All operations determining interval endpoints use exact integers/fractions/SymPy rational algebra. The diagnostic decimal displays have no role in the proof.

Actual executed checker printed:
upper tail 9.200737205950476e-23
cusp tail 2.6053200309579212e-132
local tails [2.951388464367777e-134, 2.1623366427899384e-132, 4.338873183316759e-130, 7.596322821748232e-129]
Q [326.2818729281318, -73.8824590268895, 2.9982633656930924, -0.1489562626513123]
qe 3.5890963967247877e-16
V16 -24327.338757711383; ve 3.8007284649517813e-13
PREFIX1053_CONNECTION_CERTIFICATE_PASSED

## 4. Control and next problem

Current owner read r6-20261124-1150-leased-observe-v1 was RUNNING/NATIVE_RUNNER at last observation. Historical registered identity EM-DIRECT-780BBE / RA-0ABD84561C86E53067DB0322 inherited from PREFIX-1052; current logical-session execution binding not established. No new CLAIM, PROGRESS, review or protected Activity mutation. This standalone auxiliary proof is retained separately from formal task authority.

Next: propagate the above certified rational initial box into the middle branch using the analytic recurrence at 16, re-center before radius 12, use the proven removability at 4, and certify the contrast 5g/c=4(Hf)'−2Pf+12(11+y)v by a continuous interval polynomial certificate or locate a negative witness. No middle-wide positivity claimed yet. Existing upper-band certificate stays in force.
