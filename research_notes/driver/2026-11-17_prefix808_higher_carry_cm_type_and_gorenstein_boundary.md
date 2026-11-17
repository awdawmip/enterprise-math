# PREFIX-808 — Exact Cohen–Macaulay type and the unique type-one higher-carry cokernel

Date: 2026-11-17. **Author-side algebraic continuation and direct proof**, not contribution-independent Native review. Original TU/Reeve observer and model contribution: `EM-DIRECT-4660FF`; subsequent cyclic Kummer and higher-carry structure and the current deduction: `EM-DVR-DEBB5E`. This theorem concerns the explicit **auxiliary** Reeve/Kummer algebra, and asserts no native-X6 or JT2 transfer.

## Exact frozen inputs

Use the normal-form result [higher-carry S-module filtration, fixed commit 92b39528](https://github.com/awdawmip/enterprise-math/blob/92b39528063e442db55c5fd48b82b1dfe2e39105/research_notes/driver/2026-11-17_prefix808_higher_carry_exact_s_module_filtration.md) and its [minimal S-free resolution, fixed commit d1c0a093](https://github.com/awdawmip/enterprise-math/blob/d1c0a093e2bfde603b5d18467b48129e0eb6a049/research_notes/driver/2026-11-17_prefix808_higher_carry_cokernel_minimal_s_resolution_hilbert_series.md). The present proof uses the exact definitions and their existing load-bearing coordinatewise membership lemma, not a reconstructed or enlarged claim.

Let K be any field, h≥2, and e|d|h positive. Set n=d/e, H=h/d, S=K[U_0,U_1,U_2,U_3], A=U_0U_3, B=U_1U_2, I=(A,B), and D_h=S[z_0,z_1]/(z_0^h-A,z_1^h-B). For 0≤k<n and c≥1 put E_{k,c}=M_k/J_d^cM_k as in the pinned source. For q≥0 define r_q=ek+qd, N_q=#{(a,b): 0≤a,b<h, a+b=r_q}, m_q=max(0,ceil((c-q)/H)). Omit zero summands.

The established S-module normal form is

    E_{k,c} ≅ ⊕_{q≥0} (S/I^{m_q})^{N_q}.              (1)

## New theorem — exact type, generic socles and type-one classification

Let 𝔪=(U_0,U_1,U_2,U_3) and set

    τ(k,c) = Σ_{q≥0} N_q m_q.

1. `(E_{k,c})_𝔪` is a nonzero Cohen–Macaulay `S_𝔪`-module of dimension 2 and Cohen–Macaulay type **exactly `τ(k,c)`**, for every field characteristic.
2. The reduced support `V(I)` has four codimension-two components with generic primes `(U_0,U_1), (U_0,U_2), (U_3,U_1), (U_3,U_2)`. At each such generic prime `P`, the finite-length module `(E_{k,c})_P` has `κ(P)`-socle dimension **`τ(k,c)`**.
3. The exact type-one locus in the parameter space is

       τ(k,c)=1  if and only if  k=0 and c=1.          (2)

   In that case `E_{0,1}≅S/(A,B)` as an S-module, and the quotient ring `S/(A,B)` is a complete intersection and hence Gorenstein. For every other `k,c`, the local Cohen–Macaulay type is at least 2. This is a **type classification for S-modules**, not an assertion of a ring structure on arbitrary `E_{k,c}`.

The type is given both by `μ_{S_𝔪}(Ext^2_{S_𝔪}((E_{k,c})_𝔪,S_𝔪))` and by the last rank of its minimal local free resolution.

## Proof

The two quadrics A and B have disjoint variable support, and form an S-regular sequence. For each integer m≥1, `I^m` is perfect of grade two with minimal Hilbert–Burch resolution

    0 → S^{m} → S^{m+1} → S → S/I^m → 0,

whose positive-degree entries lie in 𝔪. Each `S/I^m` is Cohen–Macaulay of dimension 2. Localize (1) at 𝔪: the direct sum remains a minimal resolution; its last free rank is `Σ N_q m_q=τ(k,c)`. For a CM module of codimension two over a regular local ring, that last rank equals its CM type; equivalently, dualizing the minimal resolution shows that the canonical module requires exactly that many generators. This proves assertion 1.

Every minimal prime P of I is one of the four displayed coordinate primes. At each, two of U_0,U_3 and U_1,U_2 become units, so `I S_P=P S_P`; `S_P` is a two-dimensional regular local ring with maximal ideal P S_P. The socle of `S_P/(P S_P)^m` is `(P S_P)^{m-1}/(P S_P)^m`, of κ(P)-dimension m. Apply (1) and add the socle dimensions to obtain assertion 2.

Finally, `N_0=ek+1` because `0≤ek<d≤h`, and `m_0=ceil(c/H)≥1`. If k≥1, then `N_0≥2` and so `τ≥2`. For k=0, c=1, `m_0=1` and `m_q=0` for all q≥1, while `N_0=1`; hence τ=1 and (1) yields S/I. If k=0 and c≥2, either `c>H`, when `m_0≥2`, or `2≤c≤H`, when `m_0=1` but `m_1=1` and `N_1>0`. Indeed `r_1=d≤h≤2h-2` for h≥2, so at least one pair `0≤a,b<h` has a+b=d. Thus τ≥2 in both cases, proving (2). QED.

## Example and exact finite check

At `h=d=4,e=1,k=0,c=3`, the pinned decomposition is `S/I^3 ⊕ (S/I^2)^3`, so `τ=3+3·2=9`; its four generic component socles all have dimension 9. At `h=d=4,e=1,k=0,c=1`, `τ=1` and the quotient is the complete intersection S/I.

A separate exact integer enumeration used h=2,...,72, all divisor chains e|d|h, all allowed k, and c=1,...,8, and directly summed `max(0,ceil((c-q)/H))` over all 0≤a,b<h with a+b=ek+qd. Across **56,336 configurations**, the equality `τ=1 ⇔ (k=0,c=1)` had **zero mismatches**. The exhaustive finite check tests the arithmetic parameter boundary; the proof above establishes the universal result.

## Research/disposition scope

This completes the exact CM-type and type-one classification for the already-defined auxiliary `E_{k,c}`. It does not by itself resolve the independent Source/Activity association, Native Result admission, the N-coupled coverage mother question, or JT2 universal UR. An independent author-disjoint reviewer should verify the pinned normal-form coefficient-ideal equivalence and the current proof before applying any formal Result disposition.
