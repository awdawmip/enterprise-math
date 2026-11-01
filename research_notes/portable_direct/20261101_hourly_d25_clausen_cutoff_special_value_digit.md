# D25 — low-band reflection formula for first Clausen cutoff digit at original z=1/2

Date 2026-11-01, TASK_RESEARCH portable author-side, lane `chatgpt-research-hourly-enterprise-math-20260923`. Task `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`, publication `TP2-B6F4FC938FF94941C1B7`, frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3` unchanged. Status `AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING`. Consume prior finite Clausen and three-level cutoff lemmas without recrediting.

## All-primes exact special-value reduction

Fix any prime p≥7, p≡1 (mod 6), r=(p−1)/6, and set

`u_n=(1/6)_n(1/3)_n/(n!)²`,
`Y_p(z)=sum_(0≤n<p) u_n z^n`,
`U_p(z)=sum_(0≤n<p) (1/2)_n(1/3)_n(2/3)_n/(n!)³ z^n`,
`K_p(z)=Y_p(z)²−U_p(z)`,
`theta=z d/dz`, `W_p(z)=(6theta+1)U_p(z)`.

The finite cutoff `K_p` is supported in degrees p,...,2p−2. Define a short sequence in Z_(p) reduced modulo p:

`c_0=1/10`,
`c_d=c_(d−1) · 18 d²/[(6d+5)(3d+2)]` for 1≤d<r.

All displayed denominators are p-units in these ranges. Define the explicit low-band moment

`C_p = sum_(j=0)^(r−1) (6j+1)/2^j · sum_(i=j+1)^r u_i c_(i−j−1) (mod p)`.

**Theorem (first omitted special-value digit, all p≡1 mod6):**

`[(6theta+1)K_p](1/2) ≡ p² C_p (mod p³)`.

Consequently, at the ORIGINAL 216 evaluation coordinate z=1/2,

`W_p(1/2) ≡ [(6theta+1)Y_p(z)²]_(z=1/2) − p² C_p (mod p³)`.

This is a general arithmetic reduction, not a proof that W_p(1/2)≡p mod p³.

**Proof.** Previous exact coefficient valuation gives for n≥p+r, `v_p([z^n]K_p)≥3`; these degrees vanish modulo p³ after multiplying by 6n+1 and 2^(−n). For n=p+j, 0≤j<r, the only summands in `k_(p+j)=sum u_i u_(p+j−i)` with total p-valuation 2 are symmetric pairs with low index j+1≤i≤r (valuation 0) and high index p+j−i>s=(p−1)/3 (valuation 2). Thus

`k_(p+j)/p² ≡ 2 sum_(i=j+1)^r u_i · [u_(p+j−i)/p²] (mod p)`.

By Wilson's already established high endpoint `u_(p−1)/p²≡1/10`. Put d=i−j−1, so p+j−i=p−1−d. Reversing the exact u-ratio gives

`[u_(p−1−d)/p²] ≡ c_d (mod p)`,

because `u_(p−1−d)/u_(p−d) ≡ d²/[(d+5/6)(d+2/3)] = 18d²/[(6d+5)(3d+2)] (mod p)`. This gives the short sum for every low-band coefficient. Finally at z=1/2, Fermat's congruence `2^(−p)≡1/2 (mod p)` cancels the factor of 2 from symmetric pairs, leaving exactly `C_p`. QED.

## Concrete nonzero/zero witnesses and information conservation

Exact modular calculation at p=13 gives C_p=0; p=19 gives 12; p=37 gives 11; p=373 gives 196 (each mod p). Hence the signed high-index cutoff is **not universally negligible modulo p³**: p=19 gives an explicit nonzero effect, while p=13 exhibits an accidental cancellation. The formula isolates the entire first omitted digit using only u_i for 0≤i≤r and a reversed high-band endpoint sequence. It avoids evaluating the entire high-degree cutoff when only the p² correction is required.

BRC `COMPOSE_APPLIED`: indexed two-port coefficient provenance, p-valuations and the exact future operation (6theta+1) at 1/2 determine this compression; it is *not* safe to discard K entirely or promote a special zero sample into a universal law. Combining with the contemporaneous Hadamard Gauss bridge requires its class-specific precision (two lost digits for 13 mod24, one for 19 mod24). These are classical p-adic observations, not a native X6 or H0/B0 experimental result.

Validation: a separate exact modular implementation built u_n mod p³, reconstructed **all** omitted K_p coefficients and evaluated the full weighted cutoff at 1/2, then compared with C_p. PASS 80/80 primes p≤997, p≡1 mod6, plus independent p=373 check. Computation supports, but does not replace, the all-primes proof above.

**Next**: compose this low-band special-value moment with the exact nonlocal (1/6,1/3)→(1/8,3/8) Hadamard source intertwiner and the original signed Delta_p−R_p/Frobenius ports. Test a precise finite-trace identity relating W_p(1/2) to the 2304 Gauss special point 1/9. A coefficientwise Gauss bridge alone does not fix the two distinct evaluation points.

Native status: Gateway 0.6.11 control code review remains blocked. Historical Research lane recovery #6637 and continuation failure #6638 preserve original receipts; #1558 holds control repair, #1559 original H0/B0. No current native CLAIM/run/Source checkpoint, mathematical review or theorem admission is claimed.