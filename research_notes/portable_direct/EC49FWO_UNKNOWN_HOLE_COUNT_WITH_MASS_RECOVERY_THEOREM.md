# EC49FWO — Unknown CRT hole count is recoverable with total support mass

**Date:** 2026-11-22 (Asia/Shanghai). **Lineage:** BRC16943, EC49FWN at 730033aac844f0e1f09b1762a4b7957bd78d8d29 (three-hole inverse and unknown-count complement counterexample). **Status:** AUTHOR_PROVED / EXACT_INTEGER_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED.

## Theorem — total-mass augmented exact CRT inverse

Let n,q>=1 be coprime positive integers, q odd, and let U⊆Z/n, V⊆Z/q be *nonempty* Boolean supports. Define W=U×V⊆Z/(nq) under the fixed indexed CRT identification. Both factors and the number of holes h=q−|V| are unknown. The observer supplies the **indexed** reflection defects

Δ_W(a,b)=|W △ ((a,b)−W)|, for every a mod n, b mod q, and the **total mass** N=|W|>0.

Define K_S(c)=#{(x,y)∈S²:x+y=c} (ordered pair-sum multiplicity), so that K_S(c)=|S∩(c−S)|. Then the data determine uniquely:

1. Both factor cardinalities u=|U|, v=|V|, hence the *unknown hole count* h=q−v.
2. The **entire positional Boolean support V**, hence every excluded position, for any odd q.
3. The shorter factor's indexed pair-sum vector K_U and its full reflection defect spectrum Δ_U(a)=2(u−K_U(a)).

No restriction to one, two or three holes is required. The original U membership can remain ambiguous when n is even (as in the frozen ten-cycle spectrum collisions).

### Exact reconstruction

From N,Δ_W, compute

K(a,b)=N−Δ_W(a,b)/2=K_U(a)K_V(b).

Let B(b)=Σ_a K(a,b)=u² K_V(b) and A(a)=Σ_b K(a,b)=v² K_U(a). For the discrete Fourier transform hat f(χ)=Σ_x f(x)overline{χ(x)} on Z/q, write

L(B)=Σ_{χ∈(Z/q)^} |hat B(χ)|.

Then the exact, scale-fixed cardinality formulas are

u=L(B)/(qN),     v=N/u.

The right side is provably a positive integer for inputs in this model. Recover

K_V(b)=B(b)/u²,

1_V(x) = K_V(2x mod q) mod 2,

K_U(a)=A(a)/v²,

Δ_U(a)=2(u−K_U(a)).

The Fourier expression is an algebraic identity, not a recommendation to evaluate approximate complex roots numerically. An entirely **integer-only exact implementation** enumerates positive divisors u|N, retains u<=n and v=N/u<=q, tests whether B/u² is integral, decodes the candidate V by the parity rule, and checks the candidate convolution and factorization. Exactly one u,V,K_U passes when the observer comes from the stipulated nonempty product model.

### Proof

**Factorization.** CRT reflection maps act componentwise. Consequently K(a,b)=K_U(a)K_V(b) and the marginals satisfy B=u² K_V and A=v² K_U, because Σ_c K_S(c)=|S|².

**Scalar rigidity of Boolean self-convolution.** For a finite abelian group G, any nonempty S,T⊆G and λ>0, if K_T=λ K_S pointwise, then λ=1, |T|=|S|, and K_T=K_S. Indeed Fourier convolution gives hat K_S(χ)=hat 1_S(χ)^2. Parseval for real Boolean 1_S yields

Σ_χ |hat K_S(χ)| = Σ_χ |hat 1_S(χ)|² = |G||S|.

It follows that |T|=λ|S|, while summing K_T=λ K_S over G gives |T|²=λ|S|². Nonemptiness forces λ=1.

**Cardinality and factor autocorrelation uniqueness.** Suppose U',V' with the same fixed group sizes yield the same N,Δ_W. Then their K matrices agree. Taking a nonzero K_U(a0) row shows K_{V'}=λ K_V for a positive scalar λ; scalar rigidity forces K_{V'}=K_V and |V'|=|V|. The row identity then gives K_{U'}=K_U, and similarly |U'|=|U|. For the explicit formula, hat B=u² hat 1_V²; Parseval gives L(B)=u² qv=q u N. Hence u=L(B)/(qN).

**Odd-factor positional support recovery.** For odd q, each ordered pair (x,y) with x≠y cancels modulo two against (y,x) in K_V(b). The remaining diagonal contributions satisfy 2x=b. Since doubling is bijective on Z/q, K_V(2x) mod2=1_V(x) for each x. This recovers V and its complement. The remaining formulas follow from the marginals. QED.

### Scope and information preservation

The fixed factor lengths, CRT label coordinates, nonempty Boolean product hypothesis, total support mass and **all indexed center defects** are inputs. The theorem treats the auxiliary CRT observation; it is not a proof of any moving-Farey transition or a projection-safe replacement for a native BRC joint observer under future dynamics. It removes the prior unknown-hole-number obstruction precisely when the mass observer is supplied.

The EC49FWN spectrum-only complement example remains valid: for U=Z/10, V={2,7} and its complement in Z/11, every indexed defect agrees, but the total masses differ (20 versus 90). Distinct U supports may still share the same K_U: for A={0,2,3,4,7} and B={0,1,3,4,6}, K_A=K_B in Z/10; their products with the same V cannot be distinguished by (Δ_W,N). Thus no original-U recovery is asserted.

### Verification

Run the companion Python verifier and compare the saved JSON output. Tests use only exact integer operations. Exhaustive: every nonempty U⊆Z/4 and V⊆Z/5 (465 products) and V⊆Z/7 (1,905 products), with each reconstructed from (N,Δ). Also four n=10,q=11 cases with 1,2,3,9 unknown holes; direct collision witnesses for spectrum-only complement ambiguity and irrecoverability of the original U. This verifies those finite domains; the mathematical proof covers arbitrary coprime n,q with odd q.

### Next scientific question

Determine the **least additional observer** beyond Δ_W (possibly weaker than exact total mass N) that removes unknown-hole-count ambiguity for the frozen P10/CRT family, while preserving exact signed-position distinctions relevant to a specified native moving-Farey successor. The frozen native update/observation source remains to be identified and read before making a dynamic sufficiency claim.
