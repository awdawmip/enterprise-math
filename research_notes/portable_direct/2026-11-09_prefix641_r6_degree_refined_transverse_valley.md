# PREFIX-641-R6 — Degree-refined mixed derivative bound; fourfold widening of the unique BRC variance-valley strip

Date: 2026-11-09 (Asia/Shanghai). Frozen scientific input: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.
Independent TASK_RESEARCH mathematical note; no claim of shared-task ownership or mathematical admission.

## Model and exact new theorem

Retain the finite signed two-information-direction BRC statistical observer defined in PREFIX-621/622, with the 189-layer first-stop survivor polynomials s_n and N=189, n=0,...,188. The underlying 96-port native graph is an unchanged frozen dependency. Let mu(p,z) denote the mean of the maximum of two unit-rate informative Poisson stopping times, W(p,z) its variance, and F_q(p,z)=W(p,z)-mu(p,z)/q for real 12<=q<=24.

**Theorem 641.1 (global improved mixed-curvature bound).** For all (p,z) in [0,1]^2 and q>=12,
  |partial_z partial_pp F_q(p,z)| <= K_new = 1,146,545,169,525.
Furthermore |partial_z partial_p mu| <= C=2,250,360. In comparison, PREFIX-636 used K_old=5,933,858,212,800 and |partial_z partial_p mu|<=6,680,016.

**Theorem 641.2 (fourfold wider two-parameter valley).** Let I=[3/20,1/6], z0=19/128 and h=2^(-26). On the entire rectangle R=I x [z0-h,z0+h], for every real 12<=q<=24,
  273 < partial_p mu < 322,
  10000 < partial_pp F_q < 65200.
For each (q,z) in the specified set, F_q(.,z) has one and only one critical point c(q,z) in I, its unique global minimizer there. It is real analytic locally and decreases strictly as q increases. For the actual BRC observer slots q=12 and q=24,
  91/521600 < c(12,z)-c(24,z) < 161/120000.
For t=1/q and Phi(t,z)=min_{p in I}(W(p,z)-t mu(p,z)),
  273^2/65200 < -partial_tt Phi < 322^2/10000.
The second-parameter halfwidth grows by exactly four compared with PREFIX-640 (2^(-28)).

## Proof: degree-refined survivor estimates

The coefficients of every s_n in its degree-n Bernstein expansion belong to [0,1]. Hence for p in [0,1],
  0<=s_n(p)<=1; |s_n'(p)|<=n; |s_n''(p)|<=2n(n-1).
These inequalities follow directly from the first and second Bernstein differences; they preserve each term's degree n instead of replacing every degree by 188.

Let w(n,m)=binom(n+m,n)/2^(n+m+1). Its probability generating function is (2-x)^(-(n+1)); therefore sum_{m>=0} w=1, sum w*m=n+1, and sum w*m*(n+m+1)/2=(n+1)(n+2). The finite truncation m<=188 preserves all the corresponding nonnegative upper bounds.

PREFIX-622 supplies alpha_n(z)=1-sum_{m=0}^{188}w(n,m)s_m(z) and beta_n(z)=n+1-sum_{m=0}^{188}(n+m+1)w(n,m)s_m(z)/2. Therefore 0<=alpha_n<=1, 0<=beta_n<=n+1, |alpha'_n|<=n+1, |beta'_n|<=(n+1)(n+2).
Using
  mu=sum_m s_m(z)+sum_n alpha_n(z)s_n(p),
  U=mu_p=sum_n alpha_n s_n',
  U2=mu_pp=sum_n alpha_n s_n'',
  J2=H_pp=sum_n beta_n s_n'',
the exact finite sums yield:
  A=sum_n n=17766 >= |U|,
  B=2 sum_n n(n-1)=4429656 >= |U2|,
  C=sum_n n(n+1)=2250360 >= |U_z|,
  D=2 sum_n n(n-1)(n+1)=631225980 >= |U2_z|,
  E=sum_m m+sum_n(n+1)=35721=N^2 >= |mu_z|,
  J=2 sum_n n(n-1)(n+1)(n+2)=96451329744 >= |J2_z|,
  0<=mu<=2N=378.
All sums run over n=0,...,188. The moment expression W=2H-mu^2 implies
  partial_pp F_q = 2(J2-U^2-mu U2)-U2/q
and, by differentiation in z,
  |partial_z partial_pp F_q| <= 2[J+2AC+EB+2ND]+D/q.
For every q>=12, the right-hand side is at most
  K_new=2[J+2AC+EB+2ND]+D/12=1146545169525.
This proves Theorem 641.1 by finite exact algebra.

## Proof: integration and valley uniqueness

PREFIX-639 supplies, on I at z=z0 and for 12<=q<=24, the exact coefficient-certified inequalities 274<mu_p<321 and 27100<F_q,pp<48100. For h=1/67108864 the new certificate checks
  C*h=281295/8388608 < 1,
  K_new*h=1146545169525/67108864 < 17100.
Integrating the mixed derivative bounds from z0 to any z with |z-z0|<=h gives the strict envelopes in Theorem 641.2.

PREFIX-631 already certifies F_q,p(3/20,z)<0<F_q,p(1/6,z) for all q>=12 and the larger z range [37/256,39/256], containing this strip. Continuity, the intermediate-value theorem and the strict positivity of F_q,pp imply exactly one interior minimizer c(q,z). Implicit differentiation yields
  c_q=-mu_p/(q^2 F_q,pp)<0.
Integrating over 12<=q<=24 gives
  (273/65200)*(1/12-1/24) < c(12,z)-c(24,z)
    < (322/10000)*(1/12-1/24),
which reduces to 91/521600 < gap < 161/120000.
At the optimizer Phi_t=-mu and -Phi_tt=mu_p^2/F_q,pp, giving the curvature inequalities. QED.

## Verification, scope, next experiment

The companion exact integer/Fraction certificate computes six finite sums, the derivative envelope, rational margins, valley-gap constants and consequences in 24 assertions; execution on 2026-11-09 produced ALL_CHECKS_PASS 24. It tests the new derivation and its implications assuming the pinned PREFIX-622, PREFIX-631 and PREFIX-639 source statements. It does not recompute the original 96-port graph or the predecessor Bernstein recurrence.

Next: replace the remaining global survivor derivative envelopes by interval-restricted Bernstein controls in z, with degree-sensitive weighted coefficients, aiming to certify positivity of F_q,pp across z in [37/256,39/256]. A failure of a coarse coefficient cell should trigger subdivision or a precise signed witness, rather than a broad negative conclusion.

Immutable predecessor sources:
- PREFIX-631: enterprise-math@cab564fd9a112feed4a5a1fac0ee5556ebe7d7b6
- PREFIX-622: first-stop moment identity, preserved in the PREFIX-639 source reference chain
- PREFIX-639: enterprise-math@6acbf4f472a48d846859a71a31af243808961cff
- PREFIX-640: enterprise-math@facf6129b795befc119802daf29f30bd1e9680d1
