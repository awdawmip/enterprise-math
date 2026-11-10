# D25 / W216 — finite Clausen square gives a uniform *exact double root* in both CM classes

Date 2026-11-10 (Asia/Hong_Kong). TASK_RESEARCH `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`. Logical Research lane `chatgpt-research-onhour-enterprise-math-20260923`, separate from maintenance. **AUTHOR_SIDE / EXACT_DEPENDENCY_COMPOSITION / PROVED_CONDITIONAL_ON_ACCEPTED_CM0_SIMPLE / COMPUTATION_CHECKED / UNREVIEWED / NOT_ADMITTED / NATIVE_NOT_RUN.**

This is the **second substantive unit of the same run**. It closes the previously open double-zero condition in the author's newly proved `W_(p²)` row first-jet formula, directly using the **already frozen/accepted** CM0 and SIMPLE theorems instead of independently re-proving them. Prior note: `20261110_onhour_d25_W216_two_digit_firstjet_row_compression.md`.

## Theorem: precise multiplicity two over F_p

For every prime `p=6m+1>3`, define polynomials in `F_p[z]`
`
B_m(z) = sum_(n=0)^m ((1/6)_n (1/3)_n)/(n!)² * z^n
       = sum_(n=0)^m binom(m,n)binom(2m,n) z^n  (mod p),

A_p(z) = sum_(k=0)^(p-1) ((1/2)_k (1/3)_k (2/3)_k)/(k!)³ * z^k.
`
Every denominator for these finite coefficient ranges is a p-unit. Then the **polynomial identity**
`
               A_p(z) = B_m(z)^2  in F_p[z]                 (C)
`
holds, coefficient by coefficient, for every `p=6m+1>3`.

**Proof of (C).** Consume the exact rational formal Clausen identity, already used by the frozen source's original signed cutoff:
`
[{}_2F_1(1/6,1/3;1;z)]^2
       = {}_3F_2(1/2,1/3,2/3;1,1;z).
`
The identity may equivalently be established by taking the symmetric square of the Gauss equation
`
z(1-z)y'' + (1-3z/2)y' - y/18 = 0
`
and checking that its square solves the third-order coefficient recurrence corresponding to `theta³-z(theta+1/2)(theta+1/3)(theta+2/3)`, with constant term 1. For all degrees k<p its rational coefficient identity has p-unit denominators and is valid in `F_p`. At `p=6m+1`, `(1/6)_(m+1)` contains the factor `p/6`, so every `{}_2F_1` coefficient of degree greater than m and less than p vanishes mod p. Likewise `(1/3)_(2m+1)` contains `p/3`, so each `{}_3F_2` coefficient beyond 2m and below p vanishes mod p. The finite square has degree at most 2m, matching every coefficient in `A_p`. Moreover `1/6≡-m, 1/3≡-2m (mod p)`, giving the binomial expression. QED.

Set `z0=1/2`, and use the frozen accepted `CM0: B_m(z0)=0` and `SIMPLE: B_m'(z0)≠0 (mod p)`, both proved in `research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md` at the original scientific source pin **for every prime p≡13 or 19 (mod24)**. Then (C) implies
`
A_p(z0)=0;      A_p'(z0)=0;       A_p''(z0)=2 B_m'(z0)^2 ≠0 (mod p).
`
Thus `z0=1/2` is **exactly a double root of the full finite W216 coefficient polynomial `A_p` in F_p[z] for all target primes in both residue classes**. This is a uniform theorem (conditional only on the explicit previously accepted CM0 and SIMPLE provenance), not a finite-prime extrapolation.

## Exact signed-moment certificate and carry-preserving composition

The original W216 coefficients in the previous row theorem are `a_k=c_k 2^{-k}`, where `c_k=[z^k]A_p(z)`. Define `F_j=\sum_(k=0)^(2m) k^{\underline j} a_k`, with `k^{\underline j}` the falling factorial; `F0,F1` agree with the previous row theorem. From the exact polynomial square at `z0=1/2`:
`
F0=A_p(z0)= B_m(z0)^2 = 0 (mod p),

F1=(z d/dz A_p)(z0)
  = 2 z0 B_m(z0) B_m'(z0) = 0 (mod p),

F2=(z² d²/dz² A_p)(z0)
  = 2 z0² B_m'(z0)^2
  = (1/2) B_m'(1/2)^2 != 0 (mod p).
`
**This identifies the first surviving grade-0 moment at order two**, retaining the derivative observer otherwise erased by total-only projection. It also proves the hypotheses of the row corollary from the preceding author-side theorem.

Using exactly the author's earlier all-row identity, with the accepted first-digit `W_p≡p (mod p²)` to eliminate high rows,
`
W_(p²) ≡ F0*L0 + p*F1*L1 + p*(F0+3F1)*L2 (mod p²),
`
we now obtain **for every prime p≡13,19 (mod24)**:
`
                       W_(p²) ≡ 0 (mod p²).               (T)
`
This is a new **uniform conditional-on-accepted-source algebraic composition** connecting the original signed two-digit sum to exact CM double-root and first-jet carry structure. It is the source-level input for the *next* nonzero digit-block obstruction. Neither (T) nor the finite checks proves `W_(p²)-p W_p=0 (mod p^6)` or the original all-prime `W_p=p (mod p³)`; those higher-precision questions remain research.

**BRC observer audit:** the compression from the full `a_k` population to `(F0,F1)` is justified for the stated mod-p² weighted row operation by the exact row factorization, while the nonzero `F2` is deliberately retained for the next order. The finite quadratic polynomial and root are auxiliary classical algebra, not native X6 coordinates or a native H0/B0 Frobenius certificate. Resolution: `COMPOSE_APPLIED`, provenance CM0/SIMPLE preserved.

## Independent reproducibility

The accompanying pure-Python finite checker directly builds `B_m(z)` and `A_p(z)` via **separate** rational coefficient recurrences mod p, checks every coefficient of the square in `F_p[z]`, and computes `M=B_m(1/2)`, `N=(z B_m')(1/2)`, `F0,F1,F2`. For all 80 primes `p<=1000, p≡1(mod6)`, the coefficientwise identity passed. For **all 45 target primes** `p<=1000, p≡13,19(mod24)`, M=0, N≠0, F0=F1=0, `F2=2N²≠0`; exact finite witnesses include:
- p13: N=7, F2=7;
- p19: N=1, F2=2;
- p373: N=294, F2=173.

These tests independently detect implementation errors; the universal proof uses the source's exact CM0/SIMPLE and the coefficientwise formal Clausen identity.

## Durable next frontier

The uniform double-zero obstruction in the preceding note is **now resolved**, and future work should **not** re-prove it. Next scientifically discriminating unit: derive a row expansion at modulus p³ or p⁴ and identify the coefficient of the newly nonzero second moment `F2` in the original signed `W_(p²)-pW_p` defect. The ultimate original `Delta_p-R_p=0 mod p` task remains active with its original frozen scalar observer and Clausen cutoff, and the independent native H0/B0 issue #1559 remains OPEN/PENDING_OWNER/NOT_RUN for original p373 `[X]U mod139129`, rank, semilinear eta, signed kappa and independent replication.

Source native role status remains unchanged: own recovery_status `SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED`; no own winning CLAIM/open run or formal Source checkpoint. Source continuation `onhour11-20261110-1304-existing-continuation` was read as SUCCEEDED. This note is author-side unreviewed mathematics and not an admitted Result.
