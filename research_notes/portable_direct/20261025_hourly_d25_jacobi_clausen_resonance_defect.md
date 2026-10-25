# D25/LIFT — Clausen denominator resonance and its source-preserving weighted defect

Date 2026-10-25, TASK_RESEARCH portable proof; UNREVIEWED / NOT_ADMITTED / NO_NEW_NATIVE_CHECKPOINT. Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Logical Research lane chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

## Precise new mathematical question

A full-source Jacobi Green pairing introduces no independent reflected-tail observation (consumed result in this run's original_cross_green_factorization_no_go.md). Instead, compare the terminating Jacobi 2F1 with its genuine **Clausen-compatible** denominator and track the first p-adic denominator-parameter defect. Unlike a mere self-Wronskian, this comparison involves a second, explicitly identifiable 3F2 source. The resulting exact signed observer identity is a source-preserving bridge, not a proof of the original D25 supercongruence.

Fix p=6m+1>=7 prime, theta=z d/dz, and finite rational polynomials

\[
U(z)={}_2F_1(-m,-2m;1;z)=\sum_{n=0}^{m}u_nz^n,\quad
u_n=\frac{(-m)_n(-2m)_n}{(n!)^2},
\]
\[
C(z)={}_2F_1(-m,-2m;1-p/2;z),\quad
T(z)={}_3F_2(-2m,-4m,-3m;1-p/2,1-p;z).
\]

Because -m is a nonpositive integer, C terminates at degree m; T terminates at degree 2m. All denominators up to their actual support are p-local units. Define the explicitly signed, parameter-sensitive harmonic observer

\[
\mathcal H(z)=\sum_{n=0}^{m}u_n H_n z^n,\quad H_n=\sum_{j=1}^n1/j,\quad H_0=0.
\]

**Theorem A (exact rational Clausen identity plus first p-adic resonance defect).**
By the classical Clausen identity with parameters a=-m,b=-2m and c=a+b+1/2=1-p/2, over Q[z]

\[
\boxed{C(z)^2=T(z).}
\]

Further, coefficientwise in Z_(p)[z],

\[
\boxed{C(z)\equiv U(z)+\frac p2\mathcal H(z)\pmod{p^2}},
\quad
\boxed{T(z)-U(z)^2\equiv pU(z)\mathcal H(z)\pmod{p^2}.}
\]

These polynomial equalities hold for ALL primes p=6m+1>=7. This is the *corrected* Clausen identity for denominator c=1: squaring U itself and silently substituting Clausen's c=1-p/2 would erase the harmonic source defect.

**Theorem B (signed weighted observer, conditional inert point).**
Let \(\mathcal O=1+6\theta\) act on the actual polynomials *before* evaluation, z0=1/2. For all such primes

\[
\boxed{\mathcal O T-\mathcal O(U^2)\equiv p\mathcal O(U\mathcal H)\pmod{p^2}.}
\]

For p≡13,19 (mod24), consume (without re-proving) the previously accepted D25 first-digit input U(z0)≡0 modp. Then

\[
\boxed{T(z_0)\equiv U(z_0)^2\equiv0\pmod{p^2}},
\]
yet
\[
\boxed{
[\mathcal OT-\mathcal O(U^2)]_{z=z_0}
\equiv 6p(\theta U)(z_0)\mathcal H(z_0)\pmod{p^2}.
}
\]

In particular, the weighted observation can retain a first p-adic digit that the unweighted inert value destroys. This is exactly an observed BRC signed-amplitude/derivative source port, not a positive-mass surrogate.

## Proof and arithmetic scope

The terminating Clausen identity is the specialization of

\[
{}_2F_1(a,b;a+b+\tfrac12;z)^2
={}_3F_2(2a,2b,a+b;a+b+\tfrac12,2a+2b;z).
\]

At a=-m,b=-2m, the denominator 2a+2b=-6m=1-p has no zero in the finite 3F2 support n<=2m. No analytic continuation or infinite-tail assumption is needed: the identities are rational polynomials.

For 0<=n<=m, the p-unit product satisfies

\[
\frac1{(1-p/2)_n}
=\frac1{n!}\prod_{j=1}^n(1-p/(2j))^{-1}
\equiv\frac1{n!}(1+(p/2)H_n)\pmod{p^2}.
\]

This gives the first congruence; squaring yields T=U²+pU H modulo p²; applying the linear operator \(\mathcal O\) respects p-local coefficients and the z-degree (no z^p=z substitution). At the inert point p|U, the ordinary value of U H is divisible p, but
\(\theta(U\mathcal H)=(\theta U)\mathcal H+U(\theta\mathcal H)\)
has potentially nonzero first term. This proves the signed weighted identity and its strict conditional scope.

## Exact checker and examples

Adjacent standalone Python reproducer 20261025_hourly_d25_jacobi_clausen_parameter_resonance_check.py. Exact rational coefficientwise identity C²=T checked for p=7,13,19,31,37,43. Two independent modular recurrences for C and T and another for U checked the coefficientwise defect and point/weighted observer for 35 primes p=1 mod6, 7<=p<=373, plus 1327 (36/36 PASS). The code uses only integer modular arithmetic and Fraction. These are author tests, not independent mathematical review.

- p=13, modulo 169: U(1/2)=91, T(1/2)=0, O(U²)=39, OT=156; difference 117=13·9, while (theta U)(1/2)=7 mod13 and H(1/2)=3 mod13.
- p=19, modulo 361: U(1/2)=114, T(1/2)=0, O(U²)=285, OT=57; difference 133=19·7, while theta U=1, H=17 modulo 19.
- p=373, modulo 139129: U(1/2)=126820, T(1/2)=0, O(U²)=121225 and OT=132415; difference 11190=373·30.

## What this does and does not solve

This T is a deliberately **p-deformed and degree-2m terminating** 3F2, with top parameters (-2m,-4m,-3m) and denominators (1-p/2,1-p). It is NOT the original D25 3F2 with top (1/2,1/3,2/3), denominators (1,1), and cutoff p-1. Both agree modulo p within actual support, but their second-digit differences require numerator/denominator jets and high-rank source extraction. In particular the theorem does NOT prove the uniform D25 congruence, or furnish authenticated same-original-class CM H0/B0, [X]U mod p², original Frobenius or kappa. Native CM still NOT_RUN.

BRC resolution COMPOSE_APPLIED: exact coefficient-source identity, signed harmonic denominator jet and differential observer are preserved. The scalar inert value is a lawful quotient only for unweighted evaluation; it is not safe under the declared future theta observation. No native X6 geometry or p-adic experimental substitution is inferred.

## Next exact action

Derive a **source-preserving first-order parameter-translation bridge from the full original 3F2** (all ranks n<p, with p-adic source layers) to the resonant terminating Clausen T. Below rank n<=2m, take the harmonic numerator/denominator jet; in ranks 2m<n<=3m, recover the source coefficient from the derivative of the terminating top parameter -2m, rather than setting the original p-divisible tail to zero. Preserve weighted 1+6theta and the original signed cutoff. Then seek an all-prime telescoper for the target congruence. Father objective D25/LIFT/JT2 OPEN; historical native checkpoint/claim/contribution history unchanged, and this portable author proof is not predecessor completed research. Current native continuation returned CONTROL_QUOTA, Issue #1558 remains support owner. Original research scheduler and notifications unchanged.
