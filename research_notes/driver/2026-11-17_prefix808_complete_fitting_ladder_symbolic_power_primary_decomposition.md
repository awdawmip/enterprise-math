# PREFIX-808 — Complete Fitting-ideal ladder, symbolic powers and pure support of higher-carry defects

Date: 2026-11-17. **Author-side theorem in the pinned auxiliary Reeve/Kummer algebra, not an independent Native Result review.** Original TU/Reeve observer and model: `EM-DIRECT-4660FF`; prior Kummer/carry decomposition and this new deduction: `EM-DVR-DEBB5E`. No native-X6 or JT2 transfer is asserted.

## Pinned inputs and exact scope

The necessary prior result is the explicit `S`-module normal form, [higher-carry filtration @92b39528063e442db55c5fd48b82b1dfe2e39105](https://github.com/awdawmip/enterprise-math/blob/92b39528063e442db55c5fd48b82b1dfe2e39105/research_notes/driver/2026-11-17_prefix808_higher_carry_exact_s_module_filtration.md); its minimal resolution is [@d1c0a093e2bfde603b5d18467b48129e0eb6a049](https://github.com/awdawmip/enterprise-math/blob/d1c0a093e2bfde603b5d18467b48129e0eb6a049/research_notes/driver/2026-11-17_prefix808_higher_carry_cokernel_minimal_s_resolution_hilbert_series.md).

Let `K` be any field; `h>=2`, `e|d|h`, `n=d/e`, `H=h/d`; `0<=k<n` and `c>=1`. Set

`S=K[U_0,U_1,U_2,U_3]`, `A=U_0 U_3`, `B=U_1 U_2`, `I=(A,B)`.

For the previously defined character module `M_k` and degree-d ideal `J_d`, put `E=E_{k,c}=M_k/J_d^c M_k`. The pinned proof gives the **S-module** isomorphism

`E = ⊕_{q>=0} (S/I^{m_q})^{N_q}`,

where `m_q=max(0,ceil((c-q)/H))` and `N_q=#{(a,b) in {0,...,h-1}² : a+b=ek+qd}`. Summands with `N_q m_q=0` are omitted. This is not a decomposition as a `C_d`-module.

Form the finite multiset `a_1<=a_2<=...<=a_R` containing `N_q` copies of each positive `m_q`; then `R=Σ_{m_q>0} N_q>=1` and `T_j=a_1+...+a_j` for `1<=j<=R`, `T_0=0`.

## Theorem: all S-Fitting ideals, with scheme-theoretic support

For every parameter set and every field characteristic,

**(1) Complete determinantal ladder.**

`Fitt_{R-j,S}(E)=I^{T_j}` for `0<=j<=R`, with `I^0=S`; for `i>=R`, `Fitt_{i,S}(E)=S`.

In particular, `Fitt_0(E)=I^{T_R}=I^{Σ_q N_q m_q}` recovers the earlier zero-th Fitting formula, whereas the new statement computes **every higher Fitting ideal**. The exponent sequence is determined exactly by the sorted carry-thickness multiset, not just by its sum.

**(2) Symbolic powers and irredundant primary decomposition.**

Let

`P_{01}=(U_0,U_1)`, `P_{02}=(U_0,U_2)`, `P_{31}=(U_3,U_1)`, `P_{32}=(U_3,U_2)`.

For every `t>=1`,

`I^t = I^{(t)} = P_{01}^t ∩ P_{02}^t ∩ P_{31}^t ∩ P_{32}^t`.

Here `I^{(t)}` is the symbolic power of the radical complete-intersection ideal `I`. Each displayed `P^t` is primary, and the decomposition is irredundant. Consequently every nonunit Fitting ideal in (1) is a pure four-component codimension-two thickening:

`Fitt_{R-j,S}(E) = ⋂_{P in {P_{01},P_{02},P_{31},P_{32}} P^{T_j}` for `1<=j<=R`.

**(3) No embedded associated primes.**

`Ass_S(E)={P_{01},P_{02},P_{31},P_{32}}`.

Also `Ann_S(E)=I^{ceil(c/H)}=⋂_P P^{ceil(c/H)}`. Thus both the module support and every nontrivial determinantal support have exactly the same four reduced components; their nonreduced multiplicities are resolved by (1)–(2). These statements are entirely over `S`; no equality is being asserted for the distinct `R_h`-relative Fitting ideals.

## Proof

For a single cyclic summand `S/I^{a_i}`, the canonical presentation is one row whose entries generate `I^{a_i}`. Taking direct sums gives a presentation matrix with `R` rows and **disjoint column blocks**, one block per row. A nonzero `j×j` minor selects `j` distinct rows and one entry from each selected row. Consequently

`Fitt_{R-j}(E)=Σ_{J subset {1,...,R}, |J|=j} Π_{i in J} I^{a_i}=Σ_{|J|=j} I^{Σ_{i in J} a_i}`.

Because positive powers of a fixed ideal form a nested chain, the sum equals the power with the *smallest* subset sum, namely `I^{a_1+...+a_j}=I^{T_j}`. The `j=0` convention gives `S`. This proves (1), without any characteristic or separability hypothesis.

For (2), consider a monomial `U_0^α U_1^β U_2^γ U_3^δ`. It belongs to `I^t=(U_0U_3,U_1U_2)^t` exactly when one can select `r,s>=0`, `r+s=t`, `r<=min(α,δ)` and `s<=min(β,γ)`; this is equivalent to

`min(α,δ)+min(β,γ)>=t`.  (★)

It belongs to the intersection of the four `P^t) exactly when the four inequalities

`α+β>=t`, `α+γ>=t`, `δ+β>=t`, `δ+γ>=t`

hold. Their minimum left-hand side is precisely `min(α,δ)+min(β,γ)`, so the two monomial membership conditions coincide. Thus `I^t=⋂_P P^t`; each `P^t` is `P`-primary and contributes one of the four distinct minimal primes. As `I` is squarefree and `I S_P=P S_P` at each minimal prime, `I^{(t)}=⋂_P (I^t S_P∩S)=⋂_P P^t=I^t`.

Finally, each `S/I^{m_q}` with `m_q>0` has precisely those four associated primes by the irredundant minimal primary decomposition, and a direct sum has the union of its summands' associated primes. The `q=0` summand is always present. The annihilator was identified in the pinned normal-form theorem, and (2) supplies its primary decomposition. This proves (3).

## Reproducible exact arithmetic and example

The monomial criterion in (★) was independently enumerated for `t=1,...,12` and every `(α,β,γ,δ) in {0,...,12}^4` — **342,732 exact integer comparisons**, with no mismatch against all four prime-power inequalities. This check is finite support for the combinatorial identity; the universal result is the proof above.

At `h=d=4, e=1, k=0, c=3`, the pinned normal form is `E=S/I^3 ⊕ (S/I^2)^3`, so the sorted exponents are `(2,2,2,3)`. The complete ladder is

`Fitt_0(E)=I^9`, `Fitt_1(E)=I^6`, `Fitt_2(E)=I^4`, `Fitt_3(E)=I^2`, `Fitt_i(E)=S` for `i>=4`.

Every nonunit ideal here has the corresponding four-primary-power decomposition, with no embedded components.

## Research and review boundary

This closes the auxiliary problem of *all* `S`-module Fitting ideals and their pure scheme-theoretic support, including symbolic-vs-ordinary powers of `I`. It assumes the exact previously proved `S`-normal-form theorem and does not establish independent review of that load-bearing input. Contributor provenance is preserved; no Native Source/Activity, immutable Result or independent Driver admission was performed by this GitHub mathematical note. Reviewers should assess the normal form at its fixed commit, then the block-minor and monomial criteria separately. The native-X6 and N-coupled/JT2 mother questions stay open.
