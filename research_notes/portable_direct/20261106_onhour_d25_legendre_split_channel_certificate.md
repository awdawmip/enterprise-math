# D25 — Legendre two-channel observer certificate
2026-11-06 · TASK_RESEARCH author-side · AUTHOR-PROVED finite-field algebra / 611-prime FINITE-VERIFIED / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CM.

Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance conversation. Mother target Delta_p-R_p=0 (mod p), p≡13,19 (mod24), OPEN. Native p373 H0/B0 #1559 NOT_RUN.

## Algebraic statements and proofs

For prime p=6m+1>3, F_m(z)=sum_{n=0}^m binom(m,n)binom(2m,n)z^n in F_p[z], theta=z d/dz. Previously verified signed Clausen certificate (not new): a_n=sum_{i+j=n}d_i d_j with d_n=(1/6)_n(1/3)_n/[2^n(n!)^2], S_p=sum_{n<p}d_n, T_p=sum_{n<p}n d_n, K_p=S_p+12T_p, and W_p≡S_p K_p-2p^2 J_p (mod p^3), where J_p retains the NONZERO signed triangular cutoff. Further S_p≡F_m(1/2), T_p≡theta F_m(1/2) (mod p).

**Theorem A (quadratic Legendre transform).** In F_p[z],
F_m(z)=P_{2m}(sqrt(1-z)), where P_j are classical Legendre polynomials. RHS is a polynomial in z independent of the square-root sign. Proof: Legendre's differential equation gives over Q the terminating hypergeometric identity P_{2m}(sqrt(1-z)) = 2F1(-m,m+1/2;1;z). For n<=m<p, denominators n! are p-units, and m+1/2 ≡ -2m (mod p) since p=6m+1. The coefficients reduce to (-m)_n(-2m)_n/(n!)^2 = binom(m,n)binom(2m,n); both polynomials terminate at n=m.

**Theorem B (two coupled signed observers).** Take u^2=1/2 in Fpbar, E_k=P_{2k}(u), O_k=P_{2k+1}(u)/u; both belong to F_p. E_0=O_0=1 and for 0<=k<m,
 E_{k+1}=((4k+3)O_k/2-(2k+1)E_k)/(2k+2);
 O_{k+1}=((4k+5)E_{k+1}-(2k+2)O_k)/(2k+3).
Every denominator is nonzero mod p in this range. By (1-u^2)P'_{2m}(u)=2m(P_{2m-1}(u)-u P_{2m}(u)),
 S_p≡E_m, T_p≡m(E_m-O_{m-1}), K_p≡2O_{m-1}-E_m (mod p).
Here 12m≡-2 mod p. These are algebraic identities, not statistical observations.

**Theorem C (squarefree).** F_m has simple roots in the algebraic closure Fpbar, and neither 0 nor 1 is a root. F_m(0)=1; F_m(1)=binom(3m,m)≠0 since 3m<p. Its hypergeometric equation is
 z(1-z)F''+[1-(1-3m)z]F'-2m^2F=0.
At a double root z0 not in {0,1}, this equation and successive derivatives force every coefficient in the Taylor expansion at z0 to vanish, because deg F_m=m<p; contradiction. In particular, if E_m=0, theta F_m(1/2)≠0 and O_{m-1}≠0.

**Corollary (conditional first-digit inversion).** On primes where the accepted frozen first-digit premise W_p≡p (mod p^2) applies, the signed Clausen identity yields S_p K_p≡p (mod p^2). Exactly one of S_p,K_p vanishes mod p. If E_m=0, (S_p/p)*2O_{m-1}≡1 (mod p). If K_p=0, E_m*(K_p/p)≡1 (mod p). Quotients are taken only for factors known divisible by p. This preserves signed and valuation observers, not just the product.

## Exact finite evidence and observer state

The Python standard-library checker independently computes the binomial polynomial, Legendre pair recurrence, and original Gauss coefficients modulo p^2. It passed all 611 primes 7<=p<=10007, p≡1 (mod6), 0 assertion failures.

For 312 primes (2/p)=-1 (p≡13,19 mod24): E_m=0, K_p≠0, (S_p/p)*K_p=1 (modp). For 299 primes (2/p)=+1 (p≡1,7 mod24): K_p=0, E_m≠0, S_p*(K_p/p)=1 (modp). The *uniform quadratic-character channel selection* remains OPEN; these are bounded finite observations, not an all-prime theorem.

Concrete p | chi2 | E | Oprev | K | divided factor | inverse-product:
7 | +1 | 2 | 1 | 0 | K/p=4 | 1
13 | -1 | 0 | 3 | 6 | S/p=11 | 1
19 | -1 | 0 | 6 | 12 | S/p=8 | 1
31 | +1 | 21 | 26 | 0 | K/p=3 | 1
373 | -1 | 0 | 272 | 171 | S/p=24 | 1

BRC: COMPOSE_APPLIED. Sufficient carrier for current modular observer is (p,m,(2/p),E_m,O_{m-1},S modp^2,K modp^2,J modp); collapsing to S*K erases which channel carries the first digit and the independently signed nonzero J_p. No claim about native Frobenius or higher precision follows.

**Next smallest unit:** prove/refute the uniform quadratic-character selector by finite-field Jacobi-sum or CM relation, then use the previously verified nonzero J_p to prove (S_p/p)K_p≡1+2p J_p (mod p^2) on the target classes. Fixed original-class H0/B0 [X]U mod139129, semilinear Frobenius, eta/kappa and independent replication in #1559 remain NOT_RUN/PENDING_OWNER. Author-side preservation grants no Source CLAIM/Result/admission.

Evidence companion: d25_legendre_coupled_observer_20261106.py and 20261106_onhour_d25_legendre_split_channel_results.json.
