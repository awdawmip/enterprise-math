# Seven positions and the first non-smooth contribution to numerator noise

Use seven consecutive positions j=0,...,6 and their three overlapping forward fourth differences, with weight vector (1,−4,6,−4,1). For each true phase a, the ideal vector Sₐ is the triple (Gₐ,Gₐ₊₁,Gₐ₊₂), where G=Δ⁴P=(20,20,20,−100,140,−100), cyclically indexed. The distance is the usual maximum norm on these three components. The minimum separation between distinct Sₐ is 120, as verified by the 15 pairwise distances. The formula concerns one shared integer numerator error e, |e|≤M, and zero denominator errors. It grants exact invariance to every common additive cubic in the position j by the definition of Δ⁴.

**Theorem.** Let N(M,0) be the least integer such that for every greater or equal integer starting index r and all allowed e, the observed three-component vector is uniquely nearest to S_{r mod 6}. Then

    N(M,0)=(51840 M)^(1/6)+O(1).

**Proof.** In the frozen source count C(q)= [z^q] z/[(1−z)³(1−z²)(1−z³)(1−z⁶)], let C₀ be the polynomial part produced by the pole at z=1. All other poles have multiplicity ≤2, so C(q)=C₀(q)+hₐq+O(1), a=q mod 6. Only the non-unit double-pole partial fractions contribute to h. In real rational form these terms are

    −1/[192(z+1)²] − (z+1)/[54(z²+z+1)²].

The first gives leading periodic slope −(−1)^a/192. For the second use (1+z)(1−z)²=1−z−z²+z³ and denominator (1−z³)²; its slope is −1/81 for a≡0 mod 3, and 1/162 otherwise. This yields

    5184h = (−91,59,5,−37,5,59).

Consequently A(q)=q³/C(q)=A₀(q)+αₐ/q⁶+O(q⁻⁷), where A₀=q³/C₀ and α=−4320²h=(327600,−212400,−18000,133200,−18000,−212400). Here C₀(q)=q⁵/4320+O(q⁴). For the rational smooth part, Δ⁴A₀(q)=518400/q⁶+O(q⁻⁷), since A₀(q)=4320q⁻²+q⁻³U(1/q) for an analytic U and the fourth derivative of q⁻² is 120q⁻⁶. On the bounded stencil the cyclic oscillation has a genuine fourth difference, contributing Δ⁴αₐ/q⁶+O(q⁻⁷). Thus Δ⁴A(r)=Vₐ/r⁶+O(r⁻⁷), with

    V=518400+Δ⁴α=(1036800,1036800,1036800,−2073600,4147200,−2073600)
      =25920(G+20).

At the three consecutive stencil starts, replacing (r+j)⁻⁶ by r⁻⁶ gives the same uniform remainder. With K=0 the exact source bias in Y(q) is eA(q). Combining the frozen clean bound R(q)−P(q)=O(1/q) with |e|=O(r⁶) gives

    observed vector = Sₐ + t V⃗ₐ + O(1/r),
    t=e/r⁶,      V⃗ₐ=(Vₐ,Vₐ₊₁,Vₐ₊₂)=25920(Sₐ+20·1).

The critical distance must be determined on each signed ray of the actual phase direction V⃗ₐ. For a competitor b set δ=Sₐ−Sᵦ and H=max_i|V⃗ₐ,ᵢ|. Let t=σu, u≥0. A rival ties or beats the truth exactly when the six inequalities

    sδᵢ ≤ u[H−sσV⃗ₐ,ᵢ],    i=1,2,3,    s=−1,+1

all hold. The coefficients on the right are nonnegative. Reject a ray if a zero coefficient has positive left side; otherwise its first tie is the maximum of zero and the ratios with positive denominators. The adjacent exact rational checker fourth_error.py evaluates the 60 ordered sign/phase pairs. Over both signs and all phases the first tie occurs at u*=1/51840 on the negative ray. On the positive ray every first tie is at least 1/8640. The negative ray for true phase 2 and rival 0 crosses strictly. Its three residuals relative to S₀ are (−1036800u, −120+2073600u, 120−4147200u); near u* the rival distance is 120−2073600u. The true distance is 4147200u, hence the strict advantage of the rival is 6220800(u−u*).

For |t|<u* all competitors have strictly larger distance. Because the finite family of distance gaps are piecewise linear in t, their minimum is at least a positive absolute multiple of min(1,u*−|t|) on [−u*,u*]: each potentially zero endpoint has a left boundary segment with positive slope in the inward direction, since a constant zero segment would contradict strict success in the interior. The uniform O(1/r) perturbation changes each distance gap by O(1/r). Let ρ=(51840M)^(1/6). For r≥ρ/2 the underlying expansion is uniform; M/ρ⁶=u* and ρ(−F′(ρ))=6u* for F(r)=M/r⁶. Therefore r≥ρ+B with a sufficiently large absolute B guarantees success. On [ρ,2ρ] this follows from the derivative lower bound of order 1/ρ; for r≥2ρ the margin remains strictly positive. Conversely choose r≡2 mod 6 in [ρ−B−6,ρ−B], e=−M. Then F(r)−u* dominates the O(1/r) error and the strict rival advantage forces a failure. This proves the result.

This is a common numerator-only theorem with no denominator noise. Budgets K on the scale of r⁵ may significantly modify the denominator factor or its positivity and require another argument. Author-side derivation and exact arithmetic checks, no external review.

Frozen C(q) generating function and clean-tail predecessor: https://github.com/awdawmip/enterprise-math/blob/38b09d4a6dcc81320226b8b689364cb0252f7a81/research_notes/portable_direct/2026-11-16_R749SSA_EXACT_JOINT_LATTICE_DECODER.md

## Exact global thresholds at M=K=2, with both count errors present

The maximum norm for three adjacent fourth differences is used throughout. For the seven raw samples sharing both errors, the sharp threshold is **17**. The last failure is at r=16, true phase 4, rival 0, with e=d=−2 everywhere. Directly comparing all 25 shared error pairs for each finite cutoff and checking the infinite tail proves the upper bound. For fully independent positions, the sharp threshold is **395**. The last failure at r=394 also compares phase 4 against phase 0. Alternating (e,d)=(−2,+2),(+2,−2) from offset 0 through offset 6 is one strict witness. Its true and rival distances are respectively about 61.35758 and 60.72091.

To verify all independent assignments, let H be the three-row fourth-difference matrix, and S the codeword. For a true phase a and a rival b, the failure condition is equivalent to the existence of a row h and sign σ with all six inequalities
     
    τ (Hᵢ y − S_b,i) ≤ σ (Hₕ y − S_a,h), for all i and τ∈{−1,+1}.

Necessity follows by choosing an extremal true residual. Conversely the right-hand side is at most the actual true distance. The inequalities are linear in the seven raw readings. Interval extrema for each left-minus-right over independent coordinate ranges give exact safe exclusions. Splitting over the finite legal reading sets is exhaustive whenever exclusions alone do not suffice. For 395≤r≤1349 only 398,399,400 escape the scalar half-gap check in the separate second implementation; all signed rival tests are excluded at their root boxes for those three cutoffs. For q≥1350 its mod-six Newton certificates directly establish |Y(q)−P(q)|<3 for all shifts and errors, hence each fourth-difference coordinate errs by <48<60. The two independent implementations produce the same distances and sharp threshold.

Run from this directory:

    python cubic_drift_common.py
    python seven_independent_certificate.py
    python seven_independent.py
    python fourth_error.py

Budget notation in the sharp sixth-root theorem above sets K=0; K=2 in these finite calculations.
