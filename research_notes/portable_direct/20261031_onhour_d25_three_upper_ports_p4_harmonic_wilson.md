# D25: fourth-order upper-three-port harmonic and Wilson source theorem

**2026-10-31; AUTHOR-SIDE / CLASSICAL ALGEBRA PROVED / FINITELY CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**
Mother: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Scientific Source pin **c47e13e4aba0e006366f989d6334d443f6333ae3** remains unchanged. Research logical lane chatgpt-research-onhour-enterprise-math-20260923; distinct from maintenance chatgpt-hourly-enterprise-math-20260921.

## Original sources and previously consumed frontier

For prime p>3, put a_k=(2k)!(3k)!/[216^k(k!)^5], b_k=(4k)!/[2304^k(k!)^4], A_p=Σ(6k+1)a_k, B_p=Σ(8k+1)b_k, all k=0,...,p−1. Work in Z_(p) throughout. The conjecture A_p−2B_p+pχ_{−3}(p)≡0 mod p⁴ is NOT proved here.

Consume the exact six source-valuation bands and signed ports D_{r,p}=Σ_{k∈I_r}[(6k+1)a_k−2(8k+1)b_k], and the previously PROVED reflected top port D_{5,p}≡p³U_p mod p⁴ (proof in project commit abca20f33ef41943d70135000f27a7af3ed802e0, research_notes/portable_direct/20261031_onhour_d25_affine_p4_six_ports_upper_reflection.md). No repetition of its proof.

## Lemma 1: p² block-factorial unit law

For p≥5, 0≤q≤3, 0≤r<p, and H_r=Σ_{j=1}^r 1/j with H_0=0,
**(qp+r)!/p^q ≡ q!((p−1)!)^q r!(1+qpH_r) mod p².**

Proof: remove multiples p,2p,...,qp, whose product is p^q q!. Each of q full nonmultiple blocks has product (p−1)!∏_{t=1}^{p−1}(1+jp/t)≡(p−1)!(1+jpH_{p−1})≡(p−1)! mod p², as H_{p−1}≡0 mod p. The partial block is r!∏_{t=1}^r(1+qp/t)≡r!(1+qpH_r). Multiply. All harmonic denominators are p-units. Let W_p=((p−1)!+1)/p∈Z reduced mod p; then ((p−1)!)²≡1−2pW_p mod p².

## Theorem 2: explicit I4 penultimate port

I4={integer k:0≤k<p, 2p≤3k, 4k<3p}. For k∈I4 define r₂=2k−p, r₃=3k−2p, r₄=4k−2p, all in [0,p), and the typed normalized sources

Y_k=−2r₂!r₃!/[216^k(k!)^5] mod p,
X_k=2r₄!/[2304^k(k!)^4]·(1+2p(H_{r₄}−W_p)) mod p².

**a_k≡p³Y_k mod p⁴, b_k≡p²X_k mod p⁴,**
and
**D_{4,p}≡p³Σ_{I4}(6k+1)Y_k−2p²Σ_{I4}(8k+1)X_k mod p⁴.**

Proof: the exact factorial valuations are (3,2), with floors for (2k)!, (3k)!, (4k)! equal to (1,2,2). In a_k/p³ only mod p is needed; the factor is 1!2!((p−1)!)³≡−2. In b_k/p² retain mod p²: 2!((p−1)!)²(1+2pH_{r₄})≡2(1+2p(H_{r₄}−W_p)). Apply Lemma 1; k!, 216 and 2304 are p-units. Restoring original weights proves the termwise and summed congruences.

The Wilson-source contribution to D4 is exactly +8p³W_p Σ_{I4}(8k+1)r₄!/[2304^k(k!)^4] mod p⁴. It cannot in general be erased. For the *coarser* scalar mod p, D4/p²≡−4Σ_{I4}(8k+1)r₄!/[2304^k(k!)^4] mod p; this precision-specific quotient is not a native-state equivalence.

## Theorem 3: exact I3 port

I3={integer k:0≤k<p, 2k≥p, 3k<2p}. For k∈I3 define s₂=2k−p, s₃=3k−p, s₄=4k−2p in [0,p), and

C_k=s₂!s₃!/[216^k(k!)^5]·(1+p(H_{s₂}+H_{s₃}−2W_p)) mod p²,
F_k=2s₄!/[2304^k(k!)^4]·(1+2p(H_{s₄}−W_p)) mod p².

**a_k≡p²C_k and b_k≡p²F_k mod p⁴**, hence
**D_{3,p}≡p²Σ_{I3}[(6k+1)C_k−2(8k+1)F_k] mod p⁴.**

Proof: the factorial valuation pair is (2,2), with floors (1,1,2). For a_k/p² the two complete unit blocks contribute ((p−1)!)²≡1−2pW_p, and two partial blocks contribute (1+pH_{s₂})(1+pH_{s₃}); for b_k/p² the factor is 2!((p−1)!)²(1+2pH_{s₄}). Apply Lemma 1 and restore the original signed weights. Individual normalized coefficients are proved, not merely aggregate agreement.

## Corollary: three lower ports remain (equivalence, NOT proof)

Combine Theorems 2–3 with the previously established reflected I5:

pχ_{−3}(p)+Σ_{r=0}²D_{r,p}
≡ −p² Σ_{I3}[(6k+1)C_k−2(8k+1)F_k]
+2p²Σ_{I4}(8k+1)X_k
−p³[U_p+Σ_{I4}(6k+1)Y_k] mod p⁴.

This is *equivalent* to the original unproved affine p⁴ conjecture and retains exact signed sources. It is not a proof that the displayed equality holds. No natural source is dropped by asserting cancellation from the final scalar.

## Exact finite execution and witnesses

Independent standard-library Python script d25_affine_p4_three_upper_ports_harmonic_20261031.py was executed on all 194 primes 5≤p≤1200, checking 17,789 individual I3 and 8,894 individual I4 terms of the factorial/harmonic prediction against original a,b coefficient recurrences modulo p⁴. Original integer-binomial definitions independently crosschecked both ports for p=5,7,11,13,19,37,67,373. **All assertions PASSED**; finite verification does not substitute for the universal algebraic proof above.

|p|D3 mod p⁴|D4 mod p⁴|D3/p² mod p²|D4/p² mod p²|
|--:|--:|--:|--:|--:|
|13|1521|2366|9|14|
|19|21660|50179|60|139|
|67|399521|7379916|89|1644|
|373|4941444693|9470511030|35517|68070|

At p=373, W_p=224 and D4/p²=184 mod 373; dropping W_p from its p⁴ formula changes the observed p³ coefficient by −2·224·184≡1 mod 373. This is a classical arithmetic carry, not a native H0/B0 Frobenius coefficient.

## Open obligation and real control status

The p⁴ affine bridge and weaker D25 universal target A_p≡p mod p³ for p≡13,19 mod 24 remain OPEN. Next direct proof action: seek a *joint finite WZ/CM transform for original coupled low I0–I2* with the precise upper three-port boundary. I2 normalized coefficient expansion through p³ is admissible only as a substep of that elimination.

The native same-original-class p=373 divided-power H0/B0, semilinear Frobenius, rank, odd signed Green/Hesse and κ benchmark is **NOT EXECUTED**, support issue awdawmip/enterprise-math#1559 OPEN / PENDING_OWNER on last read. A scalar modular regression is not a replacement. Own-lane recovery awdawmip/kimi-query-bridge#6632 did not prove a current CLAIM/run; original dispatch request research-onhour-20261031-0205-dispatch-r15 in #6633 received **UPSTREAM_CODE_REVIEW_REQUIRED**. Preserve original request; do not reissue rejected mutation, borrow maintenance identity or assert Research-Activity/Source checkpoint/Result/independent review from this author-side file. Preserve P000, ACTIVE worldview and frozen Source pin.