# D25/LIFT: exact fifth-digit tail-vanishing criterion (nonblind auxiliary lemma)

2026-10-25 | PORTABLE NONBLIND DERIVATION | UNREVIEWED / NOT_ADMITTED | REGISTER_PENDING / NO_NATIVE_CLAIM / NO_DRIVER_DA / NO_FORMAL_REVIEW.

## Exact source and attribution

Source at this audit: `awdawmip/enterprise-math@ac9ec4f8065d21239ec9f3d76e9b15924bea65ae`.
Original author input: `research_notes/portable_direct/20261025_offphase_d25_lifted_frobenius_p5_compressed_fifth_digit.md` (author formula and 79-prime check). Frozen D25 scientific source pin `c47e13e4aba0e006366f989d6334d443f6333ae3`; task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`. Parent objective `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`. This addendum does not take another owner's claim or re-credit the old WZ/factorization proof.

## Lemma: complete conditional p^5 vanishing locus

Let `p >= 13` be prime, `p ≡ 1 (mod 6)`. In the author's notation, let

`T_p(p)=∏_{j=1}^{p-1}(1+p/j)=binom(2p-1,p-1)`,
`Θ_p=(∑_{j=1}^{p-1} 1/j²)/p ∈ Z_(p)`, and
`E_p=(T_p(p)²-1)L_p(p)`.

The original fifth-digit computation established `L_p(p) ≡ p·ℓ₁ (mod p²)` and
`T_p(p) ≡ 1-p³Θ_p (mod p⁵)`, with `ℓ₁=752427/3942400`.
Consequently,

`E_p ≡ -2p⁴ Θ_p ℓ₁ (mod p⁵)`.

**Exact criterion:**
`E_p ≡ 0 (mod p⁵)` if and only if
`p ∈ {13,109}` **or** `binom(2p-1,p-1) ≡ 1 (mod p⁴)`.
For any other admissible prime failing this binomial congruence, `v_p(E_p)=4`.
The binomial condition is the usual Wolstenholme-prime congruence; the lemma does not classify the primes satisfying it.

**Independent elementary product-to-harmonic bridge:** Set `h_r=Σ_{j=1}^{p-1}j^{-r}` in `Z_(p)`. For `1<=r<p-1`, finite-field power sums imply `h_r≡0 (mod p)`; in particular `h_2,h_4∈pZ_(p)`.
Pairing `j` and `p-j` gives `2h_3 ≡ -3p h_4 (mod p²)`, hence `h_3∈p²Z_(p)`; it also gives `2h_1 ≡ -p h_2-p²h_3-p³h_4 (mod p⁴)`.
Expanding the logarithm of the finite product yields `log T=ph_1-(p²/2)h_2+(p³/3)h_3-(p⁴/4)h_4 ≡ -p²h_2 (mod p⁵)`.
Since `v_p(p²h_2)>=3`, exponentiation gives `T≡1-p²h_2=1-p³Θ_p (mod p⁵)`. This proof is elementary but the subsequent L-tail normalization is inherited from the original source.

**Proof:** Factor the *exact rational* normalization as
`ℓ₁=(3²·13·59·109)/(2¹¹·5²·7·11)`.
For admissible p, denominator primes are excluded and 59 is not 1 modulo 6, leaving exactly 13 and 109 as numerator factors. At every other admissible p, ℓ₁ is a p-adic unit, so the first displayed congruence vanishes iff `Θ_p ≡ 0 (mod p)`. Since `T_p(p) ≡ 1-p³Θ_p (mod p⁵)`, this is equivalent to `binom(2p-1,p-1) ≡ 1 (mod p⁴)`. Otherwise the coefficient of p⁴ is nonzero, establishing exact valuation 4. QED.

**Scope:** This only refines the inherited arithmetic fifth-digit compression observer. It does not derive the original five-port WZ factorial identity, validate a true same-class H0/B0/CM/DP semilinear Frobenius representative, alter P000, or claim an admitted theorem. The original statement's “not uniformly zero modulo p⁵” is correct; the new lemma sharpens its prime-dependent exception boundary.

## Arithmetic check / provenance

A separately implemented, nonblind Python integer-modular check at this turn evaluated the rational A-transfer to sufficient p³ precision and the T/R factors against the compressed p⁵ prediction on **206/206** primes `13 <= p < 3000, p ≡ 1 (mod 6)`. It found a nonzero p⁴ tail coefficient on 204 and zero at exactly p=13 and p=109 within that finite range; it separately checked `Σj^-2 ≡ 0 (mod 16843²)` for p=16843. The original 79-prime regression, equations and WZ bridge belong to the prior author; this new check is **nonblind** and cannot satisfy contributor-independent Driver review. The 206-prime observation does not prove all later non-numerator primes nonexceptional.

## Next legal action

For real review, obtain current legally activated Driver DA and the exact frozen Result/current review set via current operation_contract; preserve all earlier passes and the complete contribution ledger. An independent reviewer must distinguish this disclosed author-exposed deduction from a clean-blind review. Do not publish a duplicate fifth-digit Task. The next D25 mother-target gap remains the true original-class normalized H0/B0/CM/DP representative and Frobenius bridge. If no own native session, hold REGISTER_PENDING / SYNC_DEBT; this neutral Source note is **not** a session checkpoint, Result, Review, Reference, Synthesis or Follow-up.
