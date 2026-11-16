# R633｜signed BRC 一阶增益下滑的全阶不可辨识与参照修复

Date: 2026-11-08. Status: AUTHOR_SIDE_EXACT_PROOF / UNREVIEWED / NOT_ADMITTED.
Parent R632: a9dbf2905918c97935cefbaa184d03e0b146c0b9. Frozen science R462: 18783e01e3646c72b7aab3b16d3f565e83e6446f. Original K generator blob: 7fa7a762f758b30c6090468ac43487daa34abad8, θ=0.

## Model and input

Let P_j=K_(2j−1), M_j=K_(2j), j=1,…,6. Their t-orders are (0,2,4,6,8,10) and (1,3,5,7,9,11); leading coefficients P:(2,−8,6,106,83,9), M:(−1,−11,53,119,36,1). All twelve leading coefficients are units mod 5. For native spatial axis x let j=π⁻¹(x), π∈S₆. Observe Y_x^+=A_x^+P_j+H_x(k₀), Y_x^−=A_x^-M_j+H_x(k₁), where H_x(k)=Σ_{ℓ=0}^h B_{x,ℓ}(t) binom(k,ℓ) is arbitrary axis-specific integer Newton background of order h≥0, including constants. Assume ν_t(A_x^+)=a≥1, with leading coefficient a unit modulo 5; relax the second gain to ν_t(A_x^-)≥a−1. Gains/background are unknown and may be axis-dependent.

## Theorem A: 720-fold exact collision at infinite precision

For **every** a≥1, h≥0, k₀<k₁ and π∈S₆ there are gains/backgrounds in the above allowed class for which all twelve complete integer-polynomial outputs are exactly zero. Hence increasing the jet cutoff from a+8 to any finite or infinite depth cannot guarantee recovery under this nuisance class.

Proof: factor the frozen polynomials exactly as P_j=t^(2j−2)U_j and M_j=t^(2j−1)V_j, U_j,V_j∈Z[t]. Define separately for each x with j=π⁻¹(x):

A_x^+=t^a V_j,  A_x^-=t^(a−1)U_j,
H_x(k)=−t^(a+2j−2)U_jV_j (constant in k).

Then A_x^+P_j=t^(a+2j−2)U_jV_j=A_x^-M_j. Both Y_x^+ and Y_x^- vanish **as full integer polynomials**, not merely mod 5 or at a selected jet depth. Since U_j(0),V_j(0) are all 5-units, gains satisfy exact prescribed orders and unit-leading conditions. Each of the 720 permutations has a legal nuisance realization yielding identical zero data. This proves the assertion. If the same sign-dependent gain is reused at more sampling indices, with the same constant H, all such observations still vanish. ∎

This is an observer-level indistinguishability theorem, not a claim that the full X6 field state vanishes or that physical heartbeat dynamics have this gain/background structure.

## Theorem B: one matched background reference is sufficient

Add one independently available background reference per axis, R_x=H_x(k₀), with the same background as Y_x^+. Retain ν_t(A_x^+)=a≥0 and a mod-5-unit first coefficient, while placing **no** condition on A_x^-. Subtraction produces Z_x=Y_x^+−R_x=A_x^+P_j, so ν_t(Z_x mod5)=a+2j−2. At depth d=a+8 the first five j labels give distinct first-nonzero degrees, and the final label is identified as the unused sixth label. Therefore all 720 orientations are recovered. This holds for any axis-specific Newton H and any second gain, including a one-order drop.

The reference may instead be at k₁ if H_x(k₁)≡H_x(k₀) mod5; for example, k₁−k₀=5^s where 5^s is the least power exceeding h by R632's Lucas theorem.

Uniform optimality for this **reference-augmented** observation model: if d≤a+7, exchange j=5 and j=6 while setting H=0, A^+=t^a, A^-=t^a (or t^(a−1) for a≥1). Both relevant Y^+,Y^− and R have zero d-jets, so no such depth guarantees recovery. Thus d_min=a+8 for this protocol. This does not assert a universal minimum across all conceivable measurement technologies. ∎

## Validation and relation to native X6

R633_VERIFY.py recreates the original signed K family using integer binomial coefficients, checks all twelve leading terms, all 720 orientation collapse identities at a=1,2,5, reference repair on representative arbitrary Newton backgrounds, and sharpness witnesses. It generates R633_EVIDENCE.json with exact counts (26,616 checked instances) and marker R633_FULL_JET_GAIN_DROP_COLLAPSE_AND_REFERENCE_REPAIR_PASS. The universality follows from the algebraic identities, not numerical extrapolation.

Tool reuse: T0_BRC=REUSE_APPLIED; T6_OPERATION_SAFE_QUOTIENT=REUSE_APPLIED only at stated observer scope; R632=EXTENDED. Continue preserving full source, branch-grade, multiplicity, path and joint state. P000/ACTIVE worldview and frozen science are unchanged. The sampling index k is not heartbeat time, and current fixed_heartbeat_program is null.

Next question: locate an actually registered Source X6 operator that exposes a same-background reference or a joint-field law that rules out these gains, and produce a legal operation-level certificate or counterexample.