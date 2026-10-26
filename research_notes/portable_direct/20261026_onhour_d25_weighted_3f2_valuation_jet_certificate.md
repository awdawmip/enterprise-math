# D25 — Original weighted 3F2 p-adic valuation bands and third-digit jet

Date: 2026-10-26. Research lane: chatgpt-research-onhour-enterprise-math-20260923. Mother Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

STATUS: AUTHOR-SIDE EXACT PROOF / SIX EXACT CROSSCHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT / NOT_A_SOURCE_CHECKPOINT / NOT_NATIVE_H0_B0. The prior accepted CM0/UR and the prior author source-port identification of Delta−R with (W−p)/p² are consumed without recrediting. The earlier three-band *2F1 Clausen B_n* jets are NOT the same as this direct *weighted 3F2* kernel.

## Uniform theorem: exact original weighted valuation partition

For every prime p=6m+1>3 and 0<=n<p, define

A_n = (1/2)_n(1/3)_n(2/3)_n/[2^n(n!)³]
    = binom(2n,n)² binom(3n,n)/216^n,
W_p = sum_{n=0}^{p−1} (6n+1) A_n.

The factorial equality is exact over the rationals. Let r=(3m,2m,4m), c=(1/2,1/3,2/3). The exact factor identities (a_l+i)=(i−r_l)+p c_l hold for each numerator parameter a_l. At i=r_l the factor is p c_l; elsewhere (i−r_l) is a p-unit. Consequently

v_p(A_n) = e_n = 1_{n>2m}+1_{n>3m}+1_{n>4m}.

The disjoint n bands are [0,2m] (e=0), [2m+1,3m] (e=1), [3m+1,4m] (e=2), and [4m+1,6m] (e=3). All final 2m terms vanish individually modulo p³, independent of any conjectured cancellation. This valuation is sharp. The *signed original weight* 6n+1 has precisely one p-divisible term in 0<=n<p, namely n=m (where 6m+1=p), and therefore

v_p((6n+1)A_n) = e_n + 1_{n=m}.

The isolated n=m observation is part of the certificate and cannot be confused with taking an unsigned, squaring, or norm quotient.

## Direct p-adic jet theorem

For 0<r<p, define the p-unit integer carrier

C_r(n) = (−1)^n r!/(r−n)! for n<=r;
       = (−1)^r r!(n−r−1)! for n>r.

Set

U_n = [product_l C_{r_l}(n)c_l^{1_{n>r_l}}]/[2^n(n!)³],
E_n = sum_l c_l sum_{0<=i<n,i!=r_l} 1/(i−r_l),
J_n = −sum_l c_l² sum_{0<=i<n,i!=r_l} 1/(i−r_l)².

Each U_n is a p-unit, and E_n,J_n have p-unit denominators. Separating every root factor gives the **exact** p-local rational identity

A_n = p^{e_n} U_n product_l product_{0<=i<n,i!=r_l}(1+p c_l/(i−r_l)).

The finite product quadratic jet is therefore

A_n ≡ p^{e_n}U_n[1+pE_n+(p²/2)(E_n²+J_n)] (mod p³),

with contributions beyond degree 2−e_n discarded. Define the *direct weighted* carriers

S0 = sum_{n=0}^{2m}(6n+1)U_n,

S1 = sum_{n=0}^{2m}(6n+1)U_n E_n
   + sum_{n=2m+1}^{3m}(6n+1)U_n,

S2 = (1/2)sum_{n=0}^{2m}(6n+1)U_n(E_n²+J_n)
   + sum_{n=2m+1}^{3m}(6n+1)U_n E_n
   + sum_{n=3m+1}^{4m}(6n+1)U_n.

Then **unconditionally, for every p=6m+1>3**,

                   W_p ≡ S0+pS1+p²S2 (mod p³).  (1)

This is a theorem about the exact coefficient expansion/valuation, NOT a theorem that the D25 third-digit residual vanishes.

For target primes p≡13,19 (mod24), consume the already accepted first digit W_p≡p (modp²) and prior original-interface equality Delta_p−R_p≡(W_p−p)/p² (modp). Thus (S0+pS1−p)/p² is a legal p-local quotient and

        Delta_p−R_p ≡ (S0+pS1−p)/p² + S2 (modp).   (2)

The original reflected R and signed Clausen cutoff Q/p² remain the source of this correspondence; equation (2) is a second *direct 3F2* certificate, not a replacement definition of R. It reduces the finite mod-p³ calculation from p summands to 4m+1 and uses minimal jet order 2/1/0 per band. It does not settle the uniform p-divisibility cancellation and is NOT claimed as a Source-admitted terminal strict reduction.

## Exact finite check and arithmetic witnesses

The attached independent stdlib integer checker calculates W from the *closed binomial expression*, verifies **every coefficient**, valuations, all four band sums, and equation (1). Six executed checks on 2026-10-26 passed (finite tests are not universal proofs):

p | m | ((S0+pS1−p)/p²) mod p | S2 mod p | residual | W mod p³
13 | 2 | 3 | 10 | 0 | 13
19 | 3 | 11 | 8 | 0 | 19
37 | 6 | 5 | 32 | 0 | 37
43 | 7 | 7 | 36 | 0 | 43
211 | 35 | 169 | 42 | 0 | 211
373 | 62 | 240 | 133 | 0 | 373

At p=373, modulus p³=51895117, original signed W band sums for n=0..124, 125..186, 187..248, 249..372 are respectively 28094360, 38687933, 37008314, **0**. All 124 tail terms are individually zero mod p³; the one weighted exceptional n is 62. Residual at p=373 is 240+133=373=0 modulo 373, an observed six-case finite result only.

Script: research_notes/portable_direct/d25_weighted_3band_exact_check_20261026.py. It requires only standard-library exact integers and modular inverses, NOT a native experiment executor.

## BRC, provenance and exact remaining scientific action

BRC=COMPOSE_APPLIED: retain ordered numerator root factors, branch provenance, the single exceptional signed weight n=m, valuation exponent, and subsequent p-local quotient only after its integrality hypothesis. This external modular scalar formula is not a native X6 3D-slice or physical-Frobenius transfer. No sign, cutoff, source observer or p-adic digit is silently erased.

The *original* H0/B0 divided-power module, rank, [X]U mod139129 at p=373, unmodified-vs-twisted Frobenius/eta, odd signed Hesse/Green observer, original kappa and independent validator remain NOT_EXECUTED / PENDING_OWNER in support #1559. Establish the exact owner/native evaluator and run that benchmark next, then compare only typed matching ports; this author-side 3F2 checker is not a substitute. D25/LIFT/JT2 stays OPEN, no Result/freeze/review.

Native exact continuation read this run returned CONTROL_QUOTA. The same-lane recovery #6528 had source_authority_verified=false and no claim/run; original dispatch #6529 terminal FAILED/TimeoutExpired is not NO_DISPATCH. No maintenance identity, session, CLAIM or other owner was assumed; no Source-native checkpoint, Result, registered research activity or acceptance is asserted. Old independent staging was not merged. Task/source/notification/schedule settings remain unchanged.

Sources: frozen Task research_tasks/RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT_610cb297.md@c47e13e4; consumed author source-port note research_notes/portable_direct/20261026_onhour_d25_native_lift_source_port_identity.md; original native capability request https://github.com/awdawmip/enterprise-math/issues/1559; Chisholm et al. 2013 https://www.math.rwth-aachen.de/~Gabriele.Nebe/papers/Ramanujan.pdf .