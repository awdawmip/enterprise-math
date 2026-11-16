# Shared integer source errors after removing a common additive offset

Set J=(0,1,5), P=(455,−295,−25,185,−25,−295)/36, Sₐ=(Pₐ₊ⱼ) for j in J with indices modulo six. Write Q(v)=(max(v)−min(v))/2. Given all shared biases e,d, |e|≤M, |d|≤K and positive denominators, let N(M,K) be the earliest positive cutoff at which the true signature is the unique Q-nearest ideal signature for all subsequent positive cutoffs and all allowed (e,d). The source weights are (1,1,2,3,6), and the first weight-one source is marked. Everything below applies to this fixed auxiliary observer.

## Theorem

As M+K tends to infinity along any sequence of nonnegative integer budgets, let ρ be the unique positive root of

    ρ³ − 486Kρ − 5832M = 0.

Then N(M,K)=ρ+O(1) with an absolute implied constant. In particular N(M,0)=18∛M+O(1) and N(0,K)=9√(6K)+O(1).

## Proof

The unchanged rational generating functions for C and T at positive integer index q are z/[(1−z)³(1−z²)(1−z³)(1−z⁶)] and z²/[(1−z)⁴(1−z²)(1−z³)(1−z⁶)]. For v=1−z, their Laurent expansions are v⁻⁶(1/36+v/12+O(v²)) and v⁻⁷(1/36+v/18+O(v²)), respectively. Every pole away from z=1 has multiplicity at most two. Partial fractions then give

    C(q)=q⁵/4320+q⁴/144+O(q³),
    T(q)=q⁶/25920+11q⁵/8640+O(q⁴).

Here the second coefficients are constant across phases. Therefore, with A=q³/C and B=q³T/C²,

    A(q)=4320/q²−129600/q³+O(q⁻⁴),
    B(q)=720/q−19440/q²+O(q⁻³).

The bias relative to the clean residual is (eA−dB)/(1+d/C). For r≥cρ with any fixed c>0, the defining equation of ρ gives K=O(r²), M=O(r³). For q=r+j with j in J, the numerator is O(r) and d/C=O(r⁻³), so replacing the denominator by 1 incurs absolute error O(r⁻²), uniformly for any permitted e,d. For r large enough all denominators are positive. Subtract the common constant eA(r)−dB(r), expand each leading term in j/r, and retain the R749SRY bound R(q)−P(q)=O(1/q). The centered data have the form

    Yⱼ = Sₐ,ⱼ + common + j t + O(1/r),
    t = 720d/r² − 8640e/r³.

The O(1/r) is absolute and uniform for r≥ρ/2. In particular |t|≤F(r)=720K/r²+8640M/r³, achieved by e=−M,d=K with positive sign.

For true a and rival b write Δ=Sₐ−Sᵦ. With ideal affine errors t j the true spread (twice Q) is 5|t|. For t=σu, σ∈{−1,1} and u≥0, the rival ties or beats this exactly when for every ordered pair i,j of positions,

    Δᵢ−Δⱼ ≤ u[5−σ(Jᵢ−Jⱼ)].

Each coefficient on the right is nonnegative. A positive left side and zero coefficient make the rival unreachable on that ray. Otherwise the first tie is the maximum of zero and the six ordered difference ratios with positive coefficients (diagonal pairs add nothing). An exact 60-rival/sign enumeration in slope.py finds the first tie on the positive ray is u*=40/27, a=3,b=4; on the negative ray it is a=4,b=3, at the same u*. The first break for any other ordered pair is at least 5/2 on its sign. For a=3,b=4, Δ=(35/6,15/2,−35/6). Near u*, the rival's spread is 40/3−4u. The true minus rival spread is 9(u−u*). With sign and pair simultaneously reversed the same statement holds.

For the upper bound, the minimum rival advantage (rival spread minus true spread) for |t|≤u* is bounded below by c₁ min(1,u*−|t|) with c₁>0. This follows from the explicit unique first crossings with linear slope 9 at either end, and continuity of a finite minimum on each compact subinterval of the interior. An O(1/r) sup-norm perturbation of the data can change a difference of two spreads by at most O(1/r). The defining cubic yields F(ρ)=u* and ρ(−F′(ρ))∈[2u*,3u*]. For r∈[ρ,2ρ] the same derivative is bounded below in magnitude by an absolute positive constant times 1/ρ (each positive summand decreases by at most factor 16); hence taking r≥ρ+B with a sufficiently large absolute B absorbs the O(1/r) perturbation. For r≥2ρ there is a fixed strictly positive margin, completing the upper bound.

For the lower bound, choose r≡3 modulo 6 in [ρ−B−6,ρ−B]. The integer shared assignment e=−M,d=K realizes slope F(r). Its excess F(r)−u* is at least a constant times B/ρ and tends to zero as ρ grows. Hence the explicit 9(F−u*) strict rival advantage of phase 4 dominates the uniform O(1/r) perturbation by increasing B if necessary. This gives one failure at distance O(1) below ρ. Together the two bounds prove the claim.

Author-side derivation conditional on the finite model and the frozen clean-tail result. No independent review.

Frozen generating function and clean bound: https://github.com/awdawmip/enterprise-math/blob/38b09d4a6dcc81320226b8b689364cb0252f7a81/research_notes/portable_direct/2026-11-16_R749SSA_EXACT_JOINT_LATTICE_DECODER.md
