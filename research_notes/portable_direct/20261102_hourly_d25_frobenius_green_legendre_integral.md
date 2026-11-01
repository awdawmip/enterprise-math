# D25 — Frobenius-compensated Legendre Green identity

Date: 2026-11-02 (Asia/Hong_Kong). Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. TASK_RESEARCH portable author-side lineage: chatgpt-research-hourly-enterprise-math-20260923, separate from maintenance. Frozen scientific pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged).

Evidence status: AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. This is external arithmetic auxiliary work, neither the native X6 object nor native H0/B0 experiment.

## 1. Whole-polynomial theorem

Fix a prime p >= 7 with p = 6r+1, n = 2r = (p-1)/3. Put

- Y_p(z) = sum_{k=0}^{p-1} (1/6)_k (1/3)_k z^k/(k!)^2;
- Z_p(z) = P_n(sqrt(1-z)) = 2F1(-r,r+1/2;1;z) exactly over Q, with P_n(1)=1. Since n is even, Z_p belongs to Z_(p)[z];
- D_p(z) = (Y_p(z)-Z_p(z))/p, which is p-integral coefficientwise by the previously proved Y_p = Z_p mod p;
- f_p(x) = D_p(1-x^2) mod p;
- I_n(x) = integral from 0 to x of P_n(t)^2 dt, a polynomial with p-unit denominators because deg P_n^2 = 2n < p-1.

**Theorem (G).** The following identity holds in the entire polynomial ring F_p[x]:

(1-x^2) [ P_n(x) f_p'(x) - P_n'(x) f_p(x) ]
 = [ I_n(x) - x^p/(2n+1) ]/9.                  (G)

The Frobenius term x^p/(2n+1) has nonzero coefficient -1/[9(2n+1)] = -1/3 mod p. It is part of the exact theorem.

**Proof.** Define the common hypergeometric differential operator

L = z(1-z) d²/dz² + (1-3z/2)d/dz - 1/18.

The exact coefficient recurrence for the truncated original series gives

L Y_p = -(p-5/6)(p-2/3)u_{p-1} z^p,

where u_{p-1} = (1/6)_{p-1}(1/3)_{p-1}/((p-1)!)² has valuation v_p(u_{p-1})=2. Thus L Y_p is 0 mod p². The exact terminating Legendre-series parameters (-r,r+1/2) satisfy

(-r)(r+1/2) = 1/18 - p(p+1)/36,

and therefore L Z_p = -p(p+1)Z_p/36 exactly. Subtracting and dividing by p yields L D_p = Z_p/36 mod p. Under z=1-x² this is

[(1-x²)d²/dx² -2x d/dx + n(n+1)] f_p = P_n(x)/9 mod p,

using n(n+1)=-2/9 in F_p. P_n obeys the corresponding homogeneous Legendre equation. Lagrange's identity implies that

G'(x) = P_n(x)^2/9,

where G=(1-x²)(P_n f_p'-P_n'f_p). Both P_n and f_p are even, hence G is odd. Since deg f_p <= 2(p-1), deg G <= 2p+n-1 < 3p. Also I_n'=P_n² and deg I_n=2n+1 <p. The derivative kernel on odd polynomials of this degree is exactly the span of x^p; thus G = I_n/9 + b x^p for a constant b. The polynomial identity G(1)=0 and classical Legendre orthogonality I_n(1)=1/(2n+1) force b=-1/[9(2n+1)]. QED.

**Diagnostic interpretation.** In characteristic p, integrating the Green derivative without recording the Frobenius kernel would erase a nonzero, evaluation-visible source. Retaining x^p as a separate port repairs the information loss exactly.

## 2. CM specialization and next arithmetic criterion

Now let p mod 24 be 13 or 19, and choose t in F_{p²} with t²=1/2. Consume the already established CM(-24) selector P_n(t)=0 and its simple-zero certificate P_n'(t) !=0. Since (2/p)=-1, t^p=-t. Parity gives the following elements of F_p:

E_p=P_n'(t)/t (a unit); J_p=I_n(t)/t;
H_p=Z_p(1/2)/p mod p (Legendre polynomial p-adic carry);
a_0=Y_p(1/2)/p mod p; d_0=(theta Y_p)(1/2) mod p.

Every quotient by p above is taken in Z_(p) before reduction. H_p is distinct from the earlier original truncated-Gauss low-band binomial carry.

Evaluating (G) at t gives

D_p(1/2) = -2[ J_p + (2n+1)^(-1) ]/(9E_p) mod p.

Hence

a_0 = H_p - 2[ J_p + (2n+1)^(-1) ]/(9E_p) mod p,   (F1)
d_0 = -E_p/4 mod p.                                    (F2)

Here (2n+1)^(-1)=3 mod p. Combining (F1)-(F2) with the previously established first weighted digit equivalence W_p(1/2)=p mod p² iff 12a_0 d_0=1 mod p gives the **new necessary and sufficient criterion**

W_p(1/2)=p mod p²  iff  9 E_p H_p = 2J_p+3 mod p.   (C)

The right-hand side of (C) is currently an **open universal arithmetic identity**, not a proved consequence of the CM selector. This theorem replaces three separate original first-digit source summands by one exact Legendre carry, a finite integral, and its essential Frobenius correction.

## 3. Exact verification

Code: research_notes/portable_direct/d25_green_frobenius_20261102.py, using only integer modular arithmetic and exact factorial-based Legendre coefficients. Two independent checks were executed locally:

1. The entire coefficientwise polynomial (G) was checked at p = 7, 13, 19, 37, 61, 109, 373: seven PASS, including Frobenius monomial coefficient at x^p.
2. The CM-special-value formula (F1) was checked against the original truncated Pochhammer sum for all 45 primes <= 997 in classes 13/19 mod 24, after inspecting all 80 primes <= 997 satisfying p=1 mod 6: 45 PASS. The first-digit condition also held for all 45, a *finite* observation only.

Selected witnesses (p; H_p, D_p(1/2), J_p, E_p, a_0), all entries modulo p:

13: (2,9,0,11,11);
19: (4,4,12,15,8);
37: (9,14,14,15,23);
61: (25,60,16,11,24);
109: (62,16,56,34,78);
373: (46,351,322,316,24).

The coefficient of x^p in (G) equals -1/3 mod p; the exact checker confirms values 2,4,6,12,20,36,124 respectively for the seven whole-polynomial primes.

These tests corroborate the proved polynomial theorem but do not establish (C) for all primes. No Lean check, original native experiment or independent mathematical review was performed.

## 4. Actual BRC application, evidence status and continuation

BRC reuse: COMPOSE_APPLIED, pairing the exact signed p-local difference (Y-Z)/p, Green-Wronskian response, Legendre-square integral and Frobenius port, with explicit CM field descent to F_p. Population: the declared p≡1 mod6 primes; observers: coefficients and the evaluation at t; future operations: differentiation, integration degree<p, Frobenius, evaluation, p-adic lift and the weighted mod p²/p³ comparison. The precise kernel x^p is invisible under differentiation but nonzero under evaluation at t. Thus collapsing the derivative kernel is **not** observer-safe for this operation. This does not claim a native X6 realization or broader compression optimum.

Consumed prior D25 work without recrediting: the Legendre reduction, the cubic-Hasse CM selector, the signed Clausen cutoff and Hensel/weighted first-digit criterion (research_notes/portable_direct/20261101_hourly_d25_cm24_cubic_hasse_selector_unweighted_p2.md and 20261101_hourly_d25_legendre_hensel_observer_inverse.md).

**Next executable mathematical unit:** obtain a general CM/character-sum or exact WZ certificate proving or refuting 9 E_p H_p = 2J_p+3 for all p≡13,19 mod24. If it holds, move to the established second weighted digit formula retaining actual integer carry and signed high-tail correction C_p. Frozen mother goal A_p=p mod p³ for these classes remains OPEN. The original same-class native 373 H0/B0 experiment belongs to #1559 and remains not executed.

**Control:** historical Research-lane recovery issue awdawmip/kimi-query-bridge#6637 was read-only SUCCEEDED, with no own run/claim in that 2026-11-01 snapshot; exact continuation #6638 was terminal FAILED: UPSTREAM_CODE_REVIEW_REQUIRED. Control support Enterprise Math #1558 has a reviewed-map parity candidate but no verified production deployment. No new native role-bound call, CLAIM, OPEN, Source checkpoint, freeze, Result, review or admission was made during this portable result. Preserve old session and neutral staging; distinguish logical Research lineage from maintenance. P000, ACTIVE worldview, frozen input and existing timer settings remain unchanged.
