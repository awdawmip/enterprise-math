# PREFIX-643-R6 — Binomial score localization expands the signed-BRC variance valley strip 146-fold

Date: 2026-11-09 (Asia/Shanghai). Mode: independent TASK_RESEARCH. Frozen science pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Status: AUTHOR_DERIVED / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Model and precise predecessors

The object is the frozen signed two-information-direction BRC first-stop *statistical observer* of PREFIX-621/622. Its surviving row counts satisfy 0<=row[n,k]<=binom(n,k), n=0,...,188, and all rows vanish by layer N=189. Accordingly, s_n(u)=sum_k rho(n,k) binom(n,k)u^k(1-u)^(n-k) with 0<=rho(n,k)<=1. These are randomized binomial event probabilities. Let Y be the maximum of two independently stopped unit-rate informative Poisson clocks; mu=E[Y], W=Var(Y), F_q=W-mu/q. Actual slots use q=12 and q=24.

Write I=[3/20,1/6], Z=[37/256,39/256], z0=19/128. Two immutable inherited results are needed: PREFIX-631 certifies F_q,p(3/20,z)<0<F_q,p(1/6,z) over z in Z, q>=12; PREFIX-639 certifies, at z=z0 for all p in I and real 12<=q<=24,
  274 < mu_p < 321,    27100 < F_q,pp < 48100.
The original native 96-port graph is not re-executed.

## Lemma 643.1 — score bounds for all randomized binomial events

If S_n(u)=E_u[r(K)], K~Bin(n,u), 0<=r(k)<=1, 0<u<1, then
  |S_n'(u)| <= sqrt(n/[u(1-u)])/2,
  |S_n''(u)| <= n/[u(1-u)].

Proof: write L=(K-nu)/[u(1-u)] and L'=-K/u^2-(n-K)/(1-u)^2. Finite differentiation gives S'=E[rL] and S''=E[r(L^2+L')]. Both L and L^2+L' have zero expectation because the binomial probabilities sum to one. If EX=0 and 0<=r<=1, |E[rX]|<=E|X|/2. Since E L^2=n/[u(1-u)] and E|L'|=n/[u(1-u)], Cauchy–Schwarz and the triangle inequality yield both formulas.

For n<=188 and u in I or Z, u(1-u)>=alpha=(37*219)/256^2=8103/65536. Exact check 188<4*20^2*alpha proves |s_n'(u)|<20. For p in I, p(1-p)>=51/400 and 188<1500*(51/400), hence |s_n''(p)|<1500 throughout the rectangle.

## Lemma 643.2 — much smaller localized mixed derivative

From the PREFIX-622 moment identities, with w(n,m)=binom(n+m,n)/2^(n+m+1), n,m ranging over 0,...,188,
  mu=sum_n s_n(p)+sum_m s_m(z)-sum_nm w(n,m)s_n(p)s_m(z),
  H=sum_n(n+1)s_n(p)+sum_m(m+1)s_m(z)
    -sum_nm [(n+m+1)/2] w(n,m)s_n(p)s_m(z),
  W=2H-mu^2.
For each n, the nonnegative extended weights (all m>=0) satisfy sum_m w(n,m)=1 and sum_m [(n+m+1)/2]w(n,m)=n+1 (negative-binomial mean m=n+1). Truncation only decreases the positive weight sums, and all 0<=s_n<=1. The score bounds imply, everywhere p in I,z in Z,
  |mu_p|<=A=3780,
  |mu_pp|<=B=283500,
  |mu_pz|<=C=75600,
  |mu_ppz|<=D=5670000,
  |mu_z|<=E=3780,
  |H_ppz|<=J=538650000.

For clarity, J=20*1500*sum_{n=0}^{188}(n+1) and the other numbers are 189 times the indicated score factors. The bound |mu_z|<=3780 uses the symmetric representation and weights.

The actual two stopping times are bounded pathwise by their respective Nth unit-rate Poisson arrival times X,Z', independently Gamma(N,1). Therefore Y<=max(X,Z'). With V=X/(X+Z')~Beta(N,N), integration of the symmetric beta density by parts gives
  E max(X,Z')=N+N*binom(2N,N)/4^N.
At N=189, the exact integer inequality N*binom(2N,N)<8*4^N shows mu<197 (the exact gamma maximum is about 196.7511962765).

Differentiating F_q=2H-mu^2-mu/q twice in p and once in z gives
  |F_q,ppz| <= 2[J+2AC+EB+mu*D]+D/q
             < 2[J+2AC+EB+197D]+D/12
             = K=6,598,084,500
for every p in I,z in Z,q>=12. This localized bound improves the earlier full-square PREFIX-642 K=920,566,268,685 by more than 139-fold, with a distinct declared domain.

## Theorem 643.3 — extended strip and unique minimizers

Let h=2^-18. For all p in I, z in [z0-h,z0+h] and real q in [12,24],
  273 < mu_p(p,z) < 322,
  1930 < F_q,pp(p,z) < 73270.

Proof: integrate the derivative bounds from the center z0. The exact companion certificate verifies C*h=4725/16384<1 and K*h=1649521125/65536<25170. Adding/subtracting these errors to the PREFIX-639 center Bernstein controls establishes both strict inequalities everywhere in the rectangle.

By the endpoint signs of PREFIX-631 and F_q,pp>0, each fixed pair (q,z) has precisely one interior global minimizer c(q,z) over I. Its implicit derivative for t=1/q is c_t=mu_p/F_q,pp>0, equivalently c_q=-mu_p/(q^2 F_q,pp)<0. Integrating over the t interval [1/24,1/12], whose length is 1/24, gives
  273/(24*73270) < c(12,z)-c(24,z) < 322/(24*1930).
For Phi(t,z)=min_{p in I}[W(p,z)-t mu(p,z)], the envelope/implicit formula Phi_tt=-mu_p(c,z)^2/F_q,pp(c,z) gives
  273^2/73270 < -Phi_tt < 322^2/1930.

The new transverse half-width h=2^-18 is exactly 1024/7 times the PREFIX-642 half-width 7/2^28: approximately 146.29-fold greater. All statements refer to the fixed signed statistical observer and its explicitly inherited prior evidence, not a new 96-port native run.

## Verification and continuation

An executable Python-stdlib Fraction certificate checks 28 exact equalities/inequalities (score constants, beta/Gamma cap, mixed constant, strip, curvature and optimizer implications). Local run on 2026-11-09 returned ALL_CHECKS_PASS 28. This is an exact rational implication certificate: it consumes PREFIX-621/622 survivor/moment identities and PREFIX-631/639 previously established analytic/finite certificates. It is not an independent mathematical review.

Next discriminating unit: compute restricted bivariate Bernstein coefficients of F_q,pp over I×Z for q=12 and 24. Subdivide any negative coefficient rectangles; an exact negative *function value*, if found, is a sign-changing witness. The parent objective remains the two-parameter global variance maximum.

Provenance: PREFIX-631@cab564fd9a112feed4a5a1fac0ee5556ebe7d7b6; PREFIX-639@6acbf4f472a48d846859a71a31af243808961cff; PREFIX-642@d7da5bc5c36a7a498607ceea77567aa0211208cd. Formal task CLAIM/Result/Review not created.
