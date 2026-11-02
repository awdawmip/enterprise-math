# D25: original 216 Cauchy-truncation and p-adic joint carry (2026-11-02)

**AUTHOR-DERIVED / EXACT-PROVED (Theorems A-B) / 107-PRIME EXACT CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7, frozen scientific source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Mother D25 remains Δ_p-R_p≡0 mod p for p mod24=13,19, equivalently the original signed 216 target S_p≡p mod p^3. This is an independent author-side modulo-p² bridge, not a native Source checkpoint or Result.

## External source and formal coefficient theorem

Roman Le Lan, *Series for 1/pi arising from Cauchy product*, arXiv:2604.03327v2 (2026-04-10), Eq. (3.2): https://arxiv.org/html/2604.03327v2. Euler's hypergeometric transformation and Clausen's square give the exact Q[[z]] identity

    P(z)=Σ_{n≥0} a_n z^n
        =(1-z)^(-1/2) Σ_{m≥0} binom(2m,m)^2 binom(3m,m)(z/108)^m,
    a_n=Σ_{k=0}^n binom(-1/3,k)binom(-1/6,k)binom(-2/3,n-k)binom(-5/6,n-k).

Le Lan proves an analytic 1/pi series; the distinct finite p-adic claim C_p≡-p(-6/p) mod p² is explicitly **Conjecture 1** there. No unproved p-adic identity is imported.

For any prime p=6r+1≥7 define p-integral coefficients and original 216 series:

    A_m=binom(2m,m)^2 binom(3m,m)/216^m
       =(1/2)_m(1/3)_m(2/3)_m/((m!)^3 2^m);
    B_j=binom(2j,j)/8^j;
    S_p=Σ_{m=0}^{p-1}(6m+1)A_m;
    C_p=Σ_{n=0}^{p-1}(3n-1)a_n/2^n
       =Σ_{m+j<p}(3(m+j)-1)A_m B_j.

The last equality is exact in Q, preserving the original Cauchy index pair (m,j).

## Theorem A — exact triangular cutoff and conditional CM transfer

Let F=Σ_{m<p}A_m, F1=Σ_{m<p}mA_m, B=Σ_{j<p}B_j, B1=Σ_{j<p}jB_j.
Define J0=Σ_{m,j<p; m+j≥p}A_m B_j and J1=Σ_{m,j<p; m+j≥p}(m+j)A_m B_j; H=3J1-J0.
The following identities are exact in Q:

    C_{p,0}=Σ_{n<p}a_n/2^n=BF-J0,
    C_{p,1}=Σ_{n<p}n a_n/2^n=B F1+B1 F-J1,
    C_p=3 C_{p,1}-C_{p,0}
       =(-B+3B1)F+3BF1-H.                            (A)

Proof: expand the Cauchy triangle into its p×p rectangle and its omitted high-index triangular complement, once for weight 1 and once for weight m+j. This directly proves all three identities.

Modulo p, the polynomial Σ_{j<p}(1/2)_j z^j/j! equals (1-z)^((p-1)/2). Evaluated at z=1/2:

    B≡ε, B1≡ε/2 (mod p), ε=(2/p).

**If** the original 216 CM double-zero premise F≡F1≡0 mod p holds, (A) implies

    C_p≡(ε/2) S_p-H (mod p²).                       (B)

On the D25 classes p mod24 in {13,19}, ε=-1, hence C_p≡-S_p/2-H mod p². The double-zero premise is separately checked over the finite computation range; a universal use requires its source proof.

## Theorem B — exact one-carry reduction in the p² observer

By Legendre's valuation formula for prime p=6r+1, the original coefficients obey

    v_p(A_m)=0 on [0,2r], =1 on [2r+1,3r],
             =2 on [3r+1,4r], =3 on [4r+1,p-1],
    v_p(B_j)=0 on [0,3r], =1 on [3r+1,p-1].

Consequently, every term of J0 or J1 outside 1≤m≤2r and p-m≤j≤p-1 is divisible by p². For 1≤s≤2r, Wilson's theorem gives

    binom(2p-2s,p-s)/p≡-2/[s binom(2s,s)] (mod p),
    B_{p-s}/p≡-1/[4sB_s] (mod p).                   (R)

In (R), all displayed inverted factors are p-units. Define finite, source-tagged carry observers

    K0(p)=-Σ_{m=1}^{2r} A_m Σ_{s=1}^m [1/(4s B_s)] (mod p),
    K1(p)=-Σ_{m=1}^{2r} A_m Σ_{s=1}^m [(m-s)/(4s B_s)] (mod p).

By retaining j=p-s and reducing m+j=p+m-s modulo p in the unique one-carry range, **unconditionally for every p=6r+1 prime**:

    J0≡pK0,  J1≡pK1,  H≡p(3K1-K0) (mod p²).       (C)

Under the separate CM premise, (B) becomes the explicit source-preserving comparison

    C_p≡-S_p/2-p(3K1-K0) (mod p²)                 (D)

for p mod24=13,19. These are exact theorems with the stated hypotheses, not fitted transfers.

## Distinct new finite conjectures and execution

Author-side Python standard library checker d25_cauchy_carry_bridge_20261102.py checks 13 coefficients in Q (n=0..12), and every one of the 107 primes ≤3000 in classes 13/19 (53 + 54), computing the full original p×p Cauchy triangle via moment prefixes, both high-index moments, independent reflected carry kernel, the CM premise and both original 216/Sun sums modulo p², all by integer arithmetic. Its actual output is d25_cauchy_carry_bridge_20261102.log. On **that exact finite domain**, all checks PASS and the following distinct candidate congruences hold:

    K0=0, K1=-1/2 mod p; hence H/p=-3/2 mod p;
    F=0 mod p²;
    S_p=C_p=p mod p²;
    C_{p,0}=0, 3 C_{p,1}=p mod p².

These remain **unproved universally**. The two K moments are stronger information than their combination. Exact sample (p; K0,K1,H/p,C_{p,1} mod p²):

    13:   0, 6,   5, 117
    19:   0, 9,   8, 247
    37:   0, 18, 17, 925
    43:   0, 21, 20, 1247
    61:   0, 30, 29, 2501
    373:  0, 186,185,92877
    1171: 0, 585,584,914551

If K0=0 and K1=-1/2 and the CM premise are proved for all target primes, then (D) implies C_p≡-S_p/2+3p/2 (mod p²): establishing either the original S_p≡p (mod p²) or the independent Sun/Le Lan finite C_p≡p (mod p²) would establish the other. The stronger original D25 p³ problem stays open.

BRC: carrier = ordered (m,j), original exact A_m/B_j, signed weight, index-sum and triangular cutoff, p-adic valuation, retained J0/J1. The reduction (C) is certified only for the declared mod-p² readout, with original source provenance; no native X6 physical or dynamical equivalence is asserted. Next research: independently prove/disprove the two moment identities K0=0 and K1=-1/2 using finite-field hypergeometric/character sums or genuine WZ certification, then connect to original signed p³ transfer. The 2026-11-02 previously completed PF boundary p^6 and Frobenius jet results are inputs, not repeated claims.

## Operational scope / recovery

Research logical lane chatgpt-research-hourly-enterprise-math-20260923; maintenance lane chatgpt-hourly-enterprise-math-20260921 not used. GitHub bridge issue #6637 read-only recovery COMPLETE/SUCCEEDED, historical session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94, no pending/run/unopened own claim; issue #6638 continuation COMPLETE/FAILED with exact UPSTREAM_CODE_REVIEW_REQUIRED (original request hourly-d25-continuation-20261101T1530p0800-r11). Direct native em_control_result for historical bridge request was CONTROL_REQUEST_NOT_FOUND, so GitHub original receipt is retained as historical evidence only. Current native em_status 0.6.11: control CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active jobs 5/5. Existing support issue #1558 owns real control repair; native 373 H0/B0 #1559 remains outstanding. No new native session, CLAIM, authorized OPEN, Source checkpoint, Result/freeze/review, or mathematics admission. The historical Research ID is not silently transferred to another actual dialogue. Project GitHub artifact is neutral author-side portable evidence; role registration and Source publication remain pending. Preserve all frozen pins, P000/ACTIVE worldview, and existing scheduler and notifications.