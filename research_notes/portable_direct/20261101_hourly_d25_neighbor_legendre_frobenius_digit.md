# D25: adjacent Legendre-degree normalization of the Frobenius first digit

Date: 2026-11-01. TASK_RESEARCH logical lane: chatgpt-research-hourly-enterprise-math-20260923. Parent task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).
Status: AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE_NOT_RUN.

## Deduplication and scope

The distinct on-hour Research lane already published the all-prime beta CM mod-p selector, using the original quadratic Frobenius polynomial factorization, at commit 2e52f3dfc171e3b0621084a3eb88a48377c3b000, path research_notes/portable_direct/20261101_onhour_d25_beta_modp_quadratic_factorization.md. This work **consumes, and does not re-credit**, that beta selector. It also uses the hourly lane's prior Hasse/CM(-24) Legendre theorem (99bc54f51e5e351a3109e7843b4dfd57481f53ba) and existing Jacobi small-core and rational-to-Frobenius coordinate lemmas. New here is the explicit **adjacent Legendre degree** normalization of the original beta derivative and the resulting scalar factorization of its first Frobenius coordinate carry.

## Exact theorem

For every prime p=8t+5 congruent to 13 mod 24, let n=(p-1)/4=2t+1, m=(p+1)/2, lambda=1/9, s^2=2, x=2s/3, and q_p(9)=(9^(p-1)-1)/p. All quantities involving p-adic division are formed in the p-local integers before reducing modulo p. Define
\[
F_p(z)=\sum_{k=0}^{p-1}\frac{(1/8)_k(3/8)_k}{(k!)^2}z^k.
\]
Then
\[
\boxed{F'_p(\lambda)\equiv -\frac98 P_{n-1}(x)\pmod p,\qquad
P_{n-1}(x)\in\mathbb F_p^\times.} \tag{N1}
\]
Furthermore, because the already-proved mod-p beta selector ensures both quotients exist,
\[
\boxed{\frac{F_p(\lambda^p)}p-\frac{F_p(\lambda)}p
 \equiv\frac{q_p(9)}8 P_{n-1}(x)\pmod p.} \tag{N2}
\]
Thus the first digits at the two coordinates are equal **if and only if** q_p(9)=0 mod p, equivalently to 3^(p-1)=1 mod p^2; no unproved p^2 beta vanishing is assumed for this equivalence. The still-open second-digit statement is exactly equivalent to
\[
\boxed{F_p(\lambda)\equiv0\pmod{p^2}\ \Longleftrightarrow\
 F_p(\lambda^p)/p\equiv (q_p(9)/8)P_{n-1}(x)\pmod p.} \tag{N3}
\]
(N3) is a proof target, NOT an all-prime proof of either side.

## Complete algebraic derivation

Use the previously proved p-modular Jacobi factorization F_p(z)=(1-z)^m Q_t(z), where
\[
Q_t(z)={}_2F_1(-t,5t+4;1;z).
\]
Since 5t+4=t+3/2+p/2, this equals S_t(z)={}_2F_1(-t,t+3/2;1;z) in F_p[z]. For n=2t+1, the exact rational polynomial identity
\[
P_n(X)=X\,S_t(1-X^2)
\]
follows by substituting P_n(X)=XS(1-X^2) into Legendre's ODE; the resulting ODE has hypergeometric parameters (-t,t+3/2;1), and S(0)=1. At the CM point x^2=8/9=1-lambda the already established Legendre selector gives P_n(x)=0, hence Q_t(lambda)=0. Differentiate x^2=1-z:
\[
Q_t'(\lambda)=-P_n'(x)/(2x^2),\quad
F_p'(\lambda)=-\tfrac12(1-\lambda)^{m-1}P_n'(x).
\]
As m-1=(p-1)/2 and (8/9)^((p-1)/2)=(2/p)=-1 for p=5 mod 8, F_p'(lambda)=P_n'(x)/2. The exact Legendre identity
\[
(1-x^2)P_n'(x)=n(P_{n-1}(x)-xP_n(x))
\]
reduces at the CM zero, where 1-x^2=lambda=1/9, to P_n'(x)=9nP_{n-1}(x). Since n=-1/4 mod p, (N1) follows. P_n'(x) is a unit because Legendre's ODE at x^2=8/9 has unit leading coefficient and deg P_n=n<p: P_n and P_n' cannot both vanish at x. Because n-1 is even, P_{n-1}(x) is a scalar F_p unit rather than an unexamined extension-field branch.

For (N2), the exact identity lambda^p=lambda/(1+p q_p(9)) yields lambda^p-lambda=-p lambda q_p(9) mod p^2. Taylor to first order gives [F_p(lambda^p)-F_p(lambda)]/p=-lambda q_p(9)F'_p(lambda) mod p. Insert (N1) and lambda=1/9, proving (N2). The p-local condition q_p(9)=0 mod p is equivalent to 3^(p-1)=1 mod p^2 since 9^(p-1)=(3^(p-1))^2 and p is odd. Rearranging (N2) proves (N3).

## Executed exact evidence

The companion standard-library Python reproducer recomputes original Pochhammer coefficients modulo p^2 and Legendre polynomials via a separate three-term recurrence. All 53 primes p<=3000, p=13 mod 24 pass N1 and N2. At p=13,37,61,109,373 respectively:
- P_(n-1)(x) mod p: 3,16,1,77,333
- F'_p(lambda) mod p: 8,19,37,36,45
- q_p(9) mod p: 3,36,26,93,229
- [F_p(lambda^p)-F_p(lambda)]/p mod p: 6,35,49,64,347.

For these same 53 finite samples F_p(lambda) is zero mod p^2, but a finite check does not close the general conjecture. No native H0/B0, semilinear Frobenius, X6 experiment, SOURCE checkpoint, claim/open, formal Result or independent admission is represented as executed.

BRC composition: retains the two s-conjugate branches, original finite Gauss coefficient source, the p-valuation, rational and Frobenius observation coordinates and q_p(9). Compression to an even scalar P_(n-1) is justified only for this first-digit coordinate-difference observer, **not** for the p^2 signed quadratic tail, original 216-sum, or native six-dimensional state. P000 ACTIVE and the frozen scientific pin remain intact.

Next smallest scientific obligation: derive the original F_p(lambda^p)/p from the previously separated two-port quadratic cutoff / signed high-index source with a proven Dwork or finite WZ normalization, and determine whether its value always matches (q_p(9)/8)P_(n-1)(x). Preserve the unproved p^2 conjecture and all native evidence obligations; control recovery remains in project issue #1558 and the original p=373 H0/B0 experiment in #1559.