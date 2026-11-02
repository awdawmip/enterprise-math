# D25: Exact half-pair carrier and p^6 even-harmonic boundary lift

Date: 2026-11-02 (Asia/Hong_Kong). Scope: portable, author-derived arithmetic of the original 216/2304 Picard–Fuchs endpoint boundary quotient. **AUTHOR-DERIVED / EXACT-PROVED / FINITE-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.**

Frozen Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. Prior source: research_notes/portable_direct/20261102_hourly_d25_pf_harmonic_seventh_digit_residual.md, which establishes the original exact ratio E_A/E_B=(16/3)(32/3)^(p-1) W_1/W_3 and the p^4 harmonic observation. This note adds a different precision and an exact half-range carrier; it preserves the prior source and all native-task constraints.

## Definitions and exact half-pair factorization

For every odd prime p and integer r, put W_r(p)=∏_{j=1}^{p-1}(rp+j). For p≥7 all factors appearing below are p-adic units. Define Q_p=W_1(p)/W_3(p)∈Z_(p)^× and h=(p-1)/2.

**Theorem A (exact rational identity).**

Q_p = ∏_{j=1}^{h} [(j²-pj-2p²)/(j²-pj-12p²)].

**Proof.** Pair j with p-j in the full product ∏(j+p)/(j+3p). The pair equals [(j+p)(2p-j)]/[(j+3p)(4p-j)] = (j²-pj-2p²)/(j²-pj-12p²). Each denominator is a unit modulo p, and the product runs through every index exactly once. QED.

This is a literal half-range reindexing of the complete composite-block carrier, not an erasure of its source. In particular every original (j,p-j) joint pair and the original pair operation can be recovered from the displayed factors and p.

## Sixth-power precision with two even harmonic ports

Write H_m(p)=∑_{j=1}^{p-1}j^{-m}∈Z_(p). The coefficient 65/2 is interpreted in Z_(p). For every prime p≥7,

**Theorem B.**

Q_p ≡ 1 + 5 p² H_2(p) + (65/2) p⁴ H_4(p)   (mod p^6).

Since H_2(p)≡H_4(p)≡0 (mod p), there is the exact next-source-digit consequence

(Q_p - 1 - 5p²H_2(p))/p^5 ≡ (65/2)·(H_4(p)/p)   (mod p).

**Proof.** All factors 1+rp/j lie in 1+pZ_p. The p-adic logarithm of their quotient is convergent. Modulo p^6 (p≥7 makes denominators for orders 1,...,5 invertible), the logarithmic series gives

L=log Q_p ≡ -2pH_1+4p²H_2-(26/3)p³H_3+20p⁴H_4-(242/5)p⁵H_5   (mod p^6).

The permutation j↦p-j yields, at the precisions needed,

2H_1 ≡ -pH_2-p²H_3-p³H_4-p⁴H_5   (mod p^5),

2H_3 ≡ -3pH_4-6p²H_5   (mod p^3).

Substitution gives

L ≡ 5p²H_2+(65/2)p⁴H_4-(122/5)p⁵H_5   (mod p^6).

Since p-1 does not divide 2,4,5 when p≥7, finite-field power sums imply H_2≡H_4≡H_5≡0 mod p (with H_5 also vanishing for p=7). Therefore the final H_5 term is 0 modulo p^6, and L has p-adic valuation at least 3. Its square is 0 modulo p^6. Exponentiating proves the formula. H_4/p is p-integral, so subtracting and dividing by p^5 proves the displayed residue. QED.

### Boundary transfer and observer scope

Combining with the previously *proved exact* D25 endpoint boundary ratio yields, for every prime p≥7,

E_A/E_B ≡ (16/3)(32/3)^(p-1)[1+5p²H_2+(65/2)p⁴H_4]   (mod p^6).

The p^6 quotient is a boundary/Picard–Fuchs observer. The half-pair carrier is a lossless arithmetic reindexing; the even-harmonic truncation is valid for the stated p^6 quotient observer only. The 216/2304 weighted signed sums and original CM-jet/Clausen/resonance data remain distinct inputs to the still-open D25 transfer problem. No claim of S_p-T_p≡0 mod p³ follows from a boundary-only identity.

### Exact execution evidence

The Python standard-library checker d25_block_pair_p6_20261102.py independently constructs Q from (i) the full W_1/W_3 product and (ii) the half-range paired factors, evaluates H_2 to precision p^4 and H_4 to precision p² and checks the formula and quotient-of-difference modulo p. All 427 primes 7≤p≤3000 passed (full p^6 modular integer arithmetic, no floating point). Selected exact certificates (p, (Q-1)/p³ mod p, (Q-1-5p²H_2)/p⁵ mod p, H_2/p mod p, H_4/p mod p):

(7,3,2,2,2), (13,8,0,12,5), (19,12,5,10,6), (37,19,0,26,0), (373,95,347,19,223), (1171,99,1015,254,932).

The p=373 third-digit block certificate 95 agrees with the predecessor. The new sixth-digit correction is 347 mod 373; it is calculated from the p-adic H_4 port, not fitted to the original sum. The data are finite exact checks separate from the proof.

## Continuation and native authorization

Frozen mother target: Δ_p-R_p≡0 mod p for p mod24∈{13,19}, equivalently the original signed 216 sum goal on the pinned source scope. This note completes the p^6 boundary-quotient subunit. Next discriminating scientific action: build/test a **source-labeled, non-scalar local CM-jet transfer** that consumes the exact boundary quotient (with its now-proven half-pair carrier) and the original 13/19 resonance and half-range signed compensator; test the resulting prediction against the original S_p-T_p mod p³ at p=13,19,37,373 before making a general conjecture.

As checked in this run, native Gateway v0.6.11 still reported code_review_required (UPSTREAM_CODE_REVIEW_REQUIRED), research_authority_granted=false, executor_binding_configured=false and active job quota 5/5. Its read-only continuation #6637 and definitively failed #6638 are preserved as historic receipts; no source CLAIM, OPEN, checkpoint, freeze, admission or independent review is claimed by this note. Control recovery remains assigned to existing Issue #1558 and original native H0/B0 experiment to #1559. P000, active worldview and frozen scientific pins were not modified.
