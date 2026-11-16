# Four consecutive samples remove a quadratic trend

Use the frozen five-source residual Y at J=(0,1,2,3), with |e|≤M and |d|≤K fixed across all four positions. Use the forward third difference L(Y)=−Yᵣ+3Yᵣ₊₁−3Yᵣ₊₂+Yᵣ₊₃. For P=(455,−295,−25,185,−25,−295)/36, define Sₐ,j=Pₐ₊ⱼ with indices modulo six. The ideal scalar codes 36L(Sₐ) for a=0,…,5 are (−1080,−360,360,1080,−2520,2520). Their minimum gap is 20 in the unscaled readout. A positive scalar error exceeding 10 at phase 0 makes phase 1 strictly closer than the truth.

## Uniform shared-source threshold

Let N₃(M,K) be the least cutoff from which the scalar nearest-code decoder returns the true phase uniquely at every integer and for all permitted common integer biases (positive denominators). As M+K→∞, let ρ>0 be the unique positive root of

    ρ⁵ − 432Kρ − 10368M = 0.

Then N₃(M,K)=ρ+O(1), with an absolute additive constant uniform in the proportions of the separate budgets. In particular N₃(M,0)=(10368M)^(1/5)+O(1) and N₃(0,K)=(432K)^(1/4)+O(1).

For the proof, split the exact generating functions of the frozen C,T at their pole z=1 from the contributions of the non-unit poles. The resulting smooth polynomials C₀(q),T₀(q) have degrees 5 and 6 respectively, with leading coefficients 1/4320,1/25920. All other poles have multiplicity at most two, so at integer q the differences C−C₀,T−T₀ are O(q), including on all six residue classes. For q sufficiently large, write

    A₀(q)=q³/C₀=q⁻²[4320+O(1/q)],
    B₀(q)=q³T₀/C₀²=q⁻¹[720+O(1/q)].

Both bracketed terms are analytic functions of 1/q near zero. For the true A,B defined with C,T, |A−A₀|=O(q⁻⁶) and |B−B₀|=O(q⁻⁵), by subtraction using C,C₀ comparable to q⁵. For all r≥ρ/2 and j=0,...,3, q=r+j, we have |e|=O(r⁵), |d|=O(r⁴), and denominators remain positive once ρ is large. The exact added bias (eA−dB)/(1+d/C) differs uniformly by O(1/r) from the real-rational profile

    D₀(q)=(eA₀−dB₀)/(1+d/C₀).

Indeed the numerator error is O(r⁻¹), and d(1/C−1/C₀)=O(r⁻⁵) multiplies a numerator O(r³), giving O(r⁻²).

To include the nonlinear denominator correction, put q=rx, h=1/r, E=e/r⁵ and D=d/r⁴. On 1≤x≤2, for h small and E,D bounded, we may write C₀(q)=q⁵W(1/q), A₀=q⁻²U(1/q), B₀=q⁻¹V(1/q), for analytic functions W,U,V, with W(0)=1/4320,U(0)=4320,V(0)=720. Thus D₀(rx)=r³G(x,h,E,D), where

    G=[E x⁻²U(h/x)−D x⁻¹V(h/x)]/[1+h D x⁻⁵/W(h/x)].

The denominator stays bounded away from zero, uniformly. At h=0 the profile G equals 4320 E x⁻²−720 D x⁻¹. The difference G(x,h,E,D)−G(x,0,E,D) is h times a smooth function whose first three x derivatives are uniformly bounded, by the mean-value integral in h on the compact parameter domain. Therefore the third derivative with respect to q of D₀(q)−(4320 e/q²−720 d/q) is O(r⁻¹): the profile residual is O(r²) and every q derivative supplies r⁻¹. The forward third difference is the integral of the third derivative over [0,1]³, with shift the sum of its three coordinates. The preceding discrepancy and the O(1/r) clean R(q)−P(q) bound remain O(1/r) under the fixed third difference. Finally Δ³q⁻²=−24r⁻⁵+O(r⁻⁶) and Δ³q⁻¹=−6r⁻⁴+O(r⁻⁵), giving uniformly

    L(Y)−L(Sₐ)=−103680e/r⁵+4320d/r⁴+O(1/r).

Write F(r)=103680M/r⁵+4320K/r⁴. F(ρ)=10, and 40≤ρ[−F′(ρ)]≤50. Throughout [ρ,2ρ], the negative derivative remains bounded below by an absolute multiple of 1/ρ; beyond 2ρ there is a fixed positive gap to 10. Thus r≥ρ+B implies success for a sufficiently large universal B. Below, take r≡0 mod 6 within [ρ−B−6,ρ−B], e=−M,d=K. The actual positive drift F(r)+O(1/r) exceeds 10 for B large enough, so phase 1 is strictly closer. This supplies the reverse bound N₃≥ρ−O(1).

## Exact limit for cancelling cubic trends on the six distinct phases

At j=0,...,5 one checks

    Pⱼ−Pⱼ₊₁=−(5/6)(2j−5)(2j²−10j+5).

If a decoder with any subset of these six labelled positions is invariant under adding every cubic polynomial in the position j, it must identify ideal phase 0 with ideal phase 1. The argument holds for any invariant map, including a nonlinear map or several outputs. It rules out reading exact phase from this quotient of these six samples. It does not rule out longer stencils with distinct integer positions beyond 5: the right-hand side is a cubic interpolation on these six integers, while the left-hand side is periodic. Shared integer source biases also form a narrower error family than all additive cubics.

Frozen source for C,T and clean tail: https://github.com/awdawmip/enterprise-math/blob/38b09d4a6dcc81320226b8b689364cb0252f7a81/research_notes/portable_direct/2026-11-16_R749SSA_EXACT_JOINT_LATTICE_DECODER.md

Author-side proof audit against the frozen model and predecessor bounds. No external review.
