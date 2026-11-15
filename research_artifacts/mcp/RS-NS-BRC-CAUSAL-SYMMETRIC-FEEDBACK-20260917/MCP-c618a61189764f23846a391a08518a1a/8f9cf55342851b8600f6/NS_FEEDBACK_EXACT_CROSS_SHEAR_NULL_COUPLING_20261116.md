# Exact same-frequency cross-shear cancellation for the causal NS linearization

Date: 2026-11-16 (Asia/Shanghai)
Task: RS-NS-BRC-CAUSAL-SYMMETRIC-FEEDBACK-20260917 / TP2-8C2E04B5D6F90123BC45
Status: exact restricted author derivation, independent review pending
Scope: classical mean-zero divergence-free Navier–Stokes on the normalized torus T^3=(R/2πZ)^3. This is a localized symmetric-convection identity, not a general causal-inverse or arbitrary-data regularity theorem.

## Proposition (nontrivial heat shear with an exact uncoupled linear perturbation)

Fix ν>0 and m∈Z_{>0}. Let f(x)=A cos(mx)+B sin(mx) and g(y)=C cos(my)+D sin(my), with real coefficients. Define F(t,x)=exp(-νm²t)f(x), G(t,y)=exp(-νm²t)g(y) and

v(t,x)=F(t,x_1)e_2,   h(t,x)=G(t,x_2)e_1.

Then v is an exact Navier–Stokes solution with pressure constant. Moreover h is an exact solution of the full *homogeneous linearized equation about v*:

∂_t h - νΔh + P[(v·∇)h+(h·∇)v]=0,  h(0)=g(x_2)e_1.

In fact the symmetric convection coupling vanishes identically after the Leray projection:

P[(v·∇)h+(h·∇)v] ≡0.

Therefore the causal linearized propagator U_v(t,0) agrees with free heat evolution on this specified initial datum:
U_v(t,0)[g(x_2)e_1] = exp(-νm²t)g(x_2)e_1.

## Proof

All fields are real, smooth, periodic, mean-zero and divergence-free. Their spatial heat eigenvalues are -m². For v, (v·∇)v=F∂_2(F e_2)=0, so v solves the unforced NS equation.

For the linearized pair, the *two ordered terms before projection* are
(v·∇)h=F G' e_1,
(h·∇)v=G F' e_2.
Since F''=-m²F and G''=-m²G, put Φ=-F'G'/m². Then
∂_1Φ=F G',   ∂_2Φ=G F',   ∂_3Φ=0.
Thus their sum is ∇Φ and its Leray projection is zero. Since ∂_t h-νΔh=0, the asserted exact propagator action follows by uniqueness for the classical linearized IVP.

## Source-preserving Fourier witness: cancellation before absolute values

Take p=(σm,0,0), q=(0,τm,0), k=p+q, with σ,τ∈{±1}. For complex Fourier coefficients v_p=α_σ e_2 and h_q=β_τ e_1 the raw symmetric contribution to output k is
iα_σβ_τ[(τm)e_1+(σm)e_2] = iα_σβ_τ στ k.
Its Leray projection P_k is zero for *each ordered input pair* when the two convection terms are added. Yet for nonzero α_σβ_τ each individual projected term has magnitude |α_σβ_τ| m / sqrt(2) and the triangle sum is sqrt(2)|α_σβ_τ|m >0.

Any unitary helical decomposition on k⊥ preserves the exact zero after summing the two terms. A positive absolute-before-pair majorant sees a nonzero artificial contribution. The two terms carry different directional provenance and must be retained until the output projection / signed sum is performed.

## Significance and remaining question

The result is an exact nonzero-reference, nonzero-perturbation, all-time cancellation family in the *linearized* NS dynamics. It supplies a regression witness for a time-ordered, helical/Waleffe symmetric-feedback implementation: it must recover zero coupling for these p,q pairs and exact free-heat propagation for h. It does not bound the operator norm for arbitrary h and v, nor improve the existing global all-mode inverse estimate by itself.

Next discriminate whether one can extend such cancellations to a nontrivial invariant mode family with multiple A3 reference waves, tracking ordered p,q, time exponents, helicity and output projection before absolute majorization. Preserve previously published causal inverse, polarization and orthogonal-response results, and seek independent verification.
