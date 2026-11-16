# One scalar contrast cancels shared level and drift

For J=(0,1,5), define L(v)=4v₀−5v₁+v₅. For each phase a the observed label is the scalar L(Sₐ), where Sₐ,j=Pₐ₊ⱼ, P=(455,−295,−25,185,−25,−295)/36, all phase indices modulo 6. Use the nearest scalar phase, and count a tie as failure. Assume all three numerator errors share the same integer e, and all three denominator errors share d, |e|≤M, |d|≤K, and all denominators remain positive. Use the original five-source C(q),T(q) and clean residual R(q). Let N_L be the least positive cutoff for correct decoding at every later integer.

## Result

As M+K tends to infinity along any nonnegative integer budget sequence, define ρ>0 by

    ρ⁴ − 1440Kρ − 25920M = 0.

Then N_L(M,K)=ρ+O(1), uniformly in the proportion of the two budgets. In particular N_L(M,0)=(25920M)^(1/4)+O(1) and N_L(0,K)=(1440K)^(1/3)+O(1).

## Proof

The six ideal scalar signatures are (3000,−600,−1320,840,1560,−3480)/36; least pairwise separation is 20, attained by phase pairs {2,1} and {3,4}. Each rise 2→1 and 3→4 is +20. Thus a scalar perturbation strictly below 10 in magnitude guarantees success, and a positive perturbation slightly above 10 at phase 2 or 3 guarantees failure.

The unchanged generating functions of C and T are z/[(1−z)³(1−z²)(1−z³)(1−z⁶)] and z²/[(1−z)⁴(1−z²)(1−z³)(1−z⁶)]. The nonconstant mod-six terms in C and T have degree at most one because every pole other than z=1 has multiplicity at most two. At z=1, writing v=1−z gives Laurent numerators after stripping v⁻⁶ and v⁻⁷ of, respectively, 1/36+v/12+49v²/432+O(v³) and 1/36+v/18+13v²/432+O(v³). Coefficient extraction gives

    C(q)=q⁵/4320+q⁴/144+95q³/1296+O(q²),
    T(q)=q⁶/25920+11q⁵/8640+155q⁴/10368+O(q³).

In particular A=q³/C and B=q³T/C² satisfy

    A(q)=4320q⁻²−129600q⁻³+2520000q⁻⁴+O(q⁻⁵),
    B(q)=720q⁻¹−19440q⁻²+341400q⁻³+O(q⁻⁴).

At cutoffs r≥ρ/2 we have M=O(r⁴), K=O(r³). For each q=r+j, j in J, the exact added source error is D(q)=[eA(q)−dB(q)]/[1+d/C(q)]. Here D₀=eA−dB is O(r²), d/C is O(r⁻²) and all denominators are eventually positive. Uniformly in q and admissible biases,

    D(q)=D₀(q)−(4320 e/q²−720 d/q)·4320 d/q⁵+O(r⁻¹).

Indeed the second-order denominator approximation error is bounded by O(r²)O(r⁻⁴)=O(r⁻²), the error in replacing D₀ by its two leading terms in the correction is O(r)O(r⁻²)=O(r⁻¹), and the error in replacing 1/C by 4320/q⁵ is O(r²)O(r³)O(r⁻⁶)=O(r⁻¹). The displayed corrections have orders ed/q⁷=O(1) and d²/q⁶=O(1), with variation O(1/r) across the bounded stencil. Their common level disappears under L. Applying the weights (4,−5,1) cancels both constants and affine functions of j and leaves sum wⱼj²=20. Consequently L((r+j)⁻ᵏ)=10k(k+1)r⁻ᵏ⁻²+O(r⁻ᵏ⁻³) for any fixed k≥1. Applying this formula to D₀ and using the displayed remainder estimates gives

    L(Y)−L(Sₐ)=259200 e/r⁴ − 14400 d/r³ + O(r⁻¹).

The clean error contributes O(r⁻¹) by the archived uniform residual bound. The deterministic O(r⁻¹) error above is uniform on r≥ρ/2, a=0..5 and every admissible shared e,d.

The largest possible absolute leading displacement is G(r)=259200M/r⁴+14400K/r³, attained positively by the integer assignments e=M,d=−K. The stated equation is G(ρ)=10. Also 30≤ρ[−G′(ρ)]≤40. On [ρ,2ρ] the derivative is bounded away from zero in units 1/ρ, so for a sufficiently large universal constant B, r≥ρ+B gives G(r)+O(1/r)<10; beyond 2ρ the gap is uniformly positive. For the reverse inequality choose r≡2 mod 6 within [ρ−B−6,ρ−B]. There G(r)−10 dominates the uniform O(1/r) remainder, and phase 1 is strictly closer than the true phase 2 for e=M,d=−K. The last failure is thus at ρ+O(1). This proves the claimed uniform asymptotics.

## Scope

This scalar combines three labelled samples; it does not reduce the number of observations collected. Neither common sharing of errors nor their integer common budget can be replaced by independent per-site errors in this theorem. Bounds concern the five-source auxiliary observer. The only predecessor input outside the frozen definitions is R(q)−P_{q mod 6}=O(1/q) uniformly, as in R749SRY/SSA/SRZ. These are current author-side deductions, without independent external review.

Archived source: https://github.com/awdawmip/enterprise-math/blob/38b09d4a6dcc81320226b8b689364cb0252f7a81/research_notes/portable_direct/2026-11-16_R749SSA_EXACT_JOINT_LATTICE_DECODER.md
