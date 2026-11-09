# PREFIX-635-R6 — Exact strong-convexity certificate and unique BRC variance valleys on a fixed central slice

Date: 2026-11-09 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_INTEGER_INTERVAL_CHECKED / UNREVIEWED / NOT_ADMITTED. Independent direct TASK_RESEARCH note; no formal CLAIM/Result/Review implied. Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.

## Statement and scope

Use the finite signed two-information-direction statistical first-passage observer of PREFIX-621/622 and its thinned native action sampler. The original 96-port native graph is a frozen dependency, not rerun here. Fix the exact slice p2=19/128 and set I0=[4/25,161/1000]. As in PREFIX-634, let Y be the maximum of the two unit-rate informative Poisson stopping times, mu(p)=E[Y], W(p)=Var(Y), and F_q(p)=W(p)-mu(p)/q. The native-time variance satisfies V_q=q² F_q for q=12,24; the same analytic interpolating objective is defined for every real q in [12,24].

**Theorem 1 (uniform certified local strict convexity).** For every p in I0 and real 12<=q<=24,

~~~text
300 < mu'(p) < 310
23000 < F_q''(p) < 50000
~~~

For each such q there is exactly one stationary point c(q) in I0; it is the unique minimizer of F_q on I0. The branch q -> c(q) is real analytic on the interior of [12,24] and strictly decreasing:

~~~text
-310/(23000*q^2) < c'(q) < -300/(50000*q^2)
~~~

**Theorem 2 (refined exact native separation).** For q=12,24 the unique central-slice minimizers satisfy

~~~text
168247/1048576 < c(12) < 168248/1048576
167883/1048576 < c(24) < 167884/1048576
363/1048576 < c(12)-c(24) < 365/1048576
~~~

The final interval has width 2/1048576. Integrating the analytic derivative additionally gives 1/4000 < c(12)-c(24) < 31/55200; the dyadic interval is sharper.

## Proof and exact finite certificate

For each 0<=n<=188 let s_n(p) be the first-passage survival polynomial in Bernstein form

~~~text
s_n(p) = sum_{k=0}^n c[n,k]*binom(n,k)*p^k*(1-p)^(n-k)
c[n,k] = row[n][k]/binom(n,k).
~~~

The exact survivor recurrence of PREFIX-621 supplies row[n][k]. Its first derivative has Bernstein coefficients n*(c[n,k+1]-c[n,k]), and its second derivative has coefficients n*(n-1)*(c[n,k+2]-2*c[n,k+1]+c[n,k]). The certificate reconstructs all 189 layers by PREFIX-621's dyadic strict-integer primitive test (DEN=2^18 and 40*(n+1) threshold), checks first stop at 25, and extinction by layer 189.

Put w(n,m)=binom(n+m,n)/2^(n+m+1) and fix p2=19/128. The exact moment reduction of PREFIX-622/632 gives

~~~text
mu(p) = sum_m s_m(p2) + sum_n alpha_n*s_n(p)
alpha_n = 1-sum_m w(n,m)*s_m(p2)
beta_n = (n+1)-sum_m ((n+m+1)/2)*w(n,m)*s_m(p2)
U=mu'=sum_n alpha_n*s_n'; U2=mu''=sum_n alpha_n*s_n''
J=H'=sum_n beta_n*s_n'; J2=H''=sum_n beta_n*s_n''
W=2H-mu^2
F_q' = 2*(J-mu*U)-U/q
F_q'' = 2*(J2-U^2-mu*U2)-U2/q.
~~~

The companion script forms exact dyadic coefficients for all 189 alpha_n,beta_n. The underlying arithmetic uses Python integers and Fraction; every certificate interval endpoint is an outward-rounded multiple of 2^-116. Rational de Casteljau subdivision and the Bernstein convex-hull property enclose each survivor polynomial and its first two derivatives. Four adjacent rational subintervals partition I0. Exact integer assertions verify 300<U<310 and 23000<F_q''<50000 at q=12 and q=24 throughout all four patches. Since F_q'' is affine in t=1/q, these strict bounds hold for every intermediate real q.

The certificate bounds F_q' at the two endpoints of I0, giving a strict negative sign at 4/25 and a strict positive sign at 161/1000 for q=12,24. Linearity in t extends the signs to q in [12,24]. By the intermediate value theorem and positive second derivative, exactly one critical point occurs in I0 and it is a strict minimum. The analytic implicit function theorem gives

~~~text
c'(q)=-mu'(c(q))/(q^2*F_q''(c(q))).
~~~

This proves the derivative bounds. Outward-rounded dyadic point evaluations give strictly negative and positive derivative signs at the respective endpoints of the two rational root isolations. Subtraction proves the 363/1048576 and 365/1048576 separation bounds, entirely using integer and rational comparisons.

## Reproduction and evidence

Run python PREFIX635_R6_STRICT_LOCAL_VALLEY_CERTIFICATE.py using Python 3 standard library. Local execution on 2026-11-09 returned ALL_CHECKS_PASS; floored display summaries were min_F_second 23162, max_F_second 49139 and mu_prime_envelope 303 306. Assertions retain the exact 2^-116 interval bounds. PREFIX635_R6_RESULTS.json captures the exact parameter ranges, dyadic root brackets, and certificate scope. The original 96-port graph remains the unchanged frozen scientific dependency.

## Next discriminating problem

Certify F_q''>0 on the larger interval [3/20,1/6], uniformly for p2 in [37/256,39/256], by adaptive two-variable Bernstein subdivision. This would upgrade the central-slice unique local valleys to uniqueness of the earlier full-interval minimizers. Continue the separate full two-dimensional global maximum variance question. 
