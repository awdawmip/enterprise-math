# D25 — finite Clausen square and harmonic second jet for the original-216 integer shadow

Date: 2026-11-05 (+08); role: TASK_RESEARCH, portable author-side evidence; logical lane: chatgpt-research-hourly-enterprise-math-20260923.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3.
**Status:** AUTHOR-PROVED exact finite-ring formula / 94-prime exact check / UNREVIEWED / NOT_ADMITTED. The six-port W216 decomposition is inherited, not credited again.

## New theorem

For every prime p=6n+1 >=7, all values below lie in Z_(p). Let

    Q_n(z)=sum_{k=0}^{2n}(-1)^k binom(2n,k)binom(3n,k)binom(4n,k) z^k,
    G_n(z) = _2F_1(-n,-2n;1-p/2;z)  [terminating at k=n],
    H_k = sum_{j=1}^k 1/j,    H_k^(2) = sum_{j=1}^k 1/j^2,
    w_k = (6k+1)(-1)^k 2^(-k) binom(2n,k)binom(3n,k)binom(4n,k),
    U_1=sum w_k H_k,  U_11=sum w_k H_k^2,  U_2=sum w_k H_k^(2),
    G=G_n(1/2), J=(z d/dz G_n(z))|_(z=1/2).

Write the previously defined integer shadow as
    C_n=sum_{k=0}^{2n}(6k+1)(-1)^k 2^(2n-k)binom(2n,k)binom(3n,k)binom(4n,k),
    S_n=2^(-2n) C_n.

Then the following is an **exact general algebraic congruence**:

    S_n ≡ G(G+12J) - (3p/2)U_1 - (p^2/8)(9U_11+5U_2)  (mod p^3).          (1)

In particular, S_n ≡ G(G+12J) (mod p). The signed observer (1+6z d/dz) and both harmonic correction ports are retained; this formula re-expresses only the shadow S_n, rather than replacing the five A–E valuation/parameter ports needed for the W216 LIFT readout.

## Proof

Apply the classical terminating Clausen identity to a=-n,b=-2n:

    G_n(z)^2 = _3F_2(-2n,-3n,-4n;1-p/2,1-p;z).

For k<=2n, the ratio of the coefficient on the right to that of Q_n is

    R_k = product_{j=1}^k (1-p/(2j))^(-1)(1-p/j)^(-1).

Every j<=2n<p, and both terminating denominator products are p-units. Expanding finite logarithms in Z_(p) gives

    log R_k ≡ (3p/2)H_k + (5p^2/8)H_k^(2)  (mod p^3),
    R_k ≡ 1+(3p/2)H_k+(p^2/8)(9H_k^2+5H_k^(2))  (mod p^3).

Thus G_n(z)^2 equals Q_n(z) plus the first and second harmonic corrections coefficientwise modulo p^3. Apply 1+6z d/dz at z=1/2. The left is G^2+12GJ; Q_n gives S_n; the correction terms give U_1,U_11,U_2. Rearrangement proves (1) for every stated prime.

This is also an exact observer-safe factorization at the first p-adic digit: the two factors G and G+12J are individually retained. The composite-indexed conjecture (6n+1)|C_n remains separately open; its arithmetic cannot be inferred from this prime-local denominator argument.

## Exact computation

An independent exact modular implementation of G,J by the recurrence

    g_(k+1)=g_k (k-n)(k-2n)/[(k+1)(2k+2-p)], g_0=1

and an independent integer-binomial evaluation of S_n,U_1,U_11,U_2 gave **94/94 PASS** for all primes 7<=p<=1200 with p=1(mod6). A separate exact rational coefficient comparison of Clausen confirmed n=1,2,3.

| p | G mod p | (G+12J) mod p | S mod p^3 | 3U_1/2 mod p^2 | (9U_11+5U_2)/8 mod p |
|---:|---:|---:|---:|---:|---:|
| 7 | 2 | 0 | 147 | 24 | 5 |
| 13 | 0 | 6 | 442 | 160 | 5 |
| 19 | 0 | 12 | 5491 | 360 | 3 |
| 31 | 21 | 0 | 5704 | 206 | 7 |
| 37 | 0 | 29 | 26862 | 1251 | 32 |
| 73 | 14 | 0 | 9855 | 1219 | 18 |
| 373 | 0 | 171 | 15521276 | 56842 | 189 |

**New branch observation:** across the checked primes, when (2/p)=-1 (p=13,19 mod24), G vanishes mod p; when (2/p)=+1 (p=1,7 mod24), G+12J vanishes mod p. This **factor-selection pattern is conjectural for general primes**; the proven identity (1) does not rely on it.

## BRC/provenance and next action

Carry: ordered k, signed binomial coefficient, p-adic valuation, harmonic 1/2 jets, G,J, original normalization 1/2, observer 1+6z d/dz and declared future W216 readout. The usual arithmetic polynomial Q_n is a restricted observer, not a claim about full native X6 state, original H0/B0 CM module, crystalline Frobenius, eta or kappa.

Next: combine (1) with the already proven signed six-port W216=S+p(A+B)+p^2(C+D+E), derive and test a smaller exact cancellation certificate for W216-p modulo p^3, and look for a proof or exact counterexample to the (2/p) factor-selection rule. The frozen mother objective Delta_p-R_p remains open, as does the original-class p373 H0/B0 [X]U modulo 139129 experiment and independent review.

At checkpoint: original native Source frontier stays intact; author-side GitHub artifact is not a new native CLAIM, OPEN, canonical Source checkpoint or mathematical admission. Fresh exact continuation request em-hourly20-20261105-1825-continuation succeeded on Source 12bf9098eeb895079bfc5aedccb90fee45947fd6, preserving SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED and NO_LIVE_CLAIM; canonical route REGISTER_NEW_SESSION_AND_CLAIM_CURRENT_PUBLICATION; execution_authorized=false.