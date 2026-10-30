# F7 A6 fixed-scalar joint index–exponent spectrum

**AUTHOR_SIDE / EXPOSED_SHARED_CONTEXT / NOT_INDEPENDENT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.**
Corollary of this PR's fixed-four-channel classification and all-index Smith/exponent theorem, not an independent Driver review or a new native Result. The original F7 `GL4(Z)` no-go remains unchanged. No statement is made about arbitrary conserved scalar laws, native X6 geometry or the three-dimensional research slice.

Let `G=Z^4 ⊕ (Z/3)^2`, `C=[[1,1],[1,-1]]`, `D=diag(C,C)`, and `Q(w,t)=#supp(Dw)/2`. In the class of *injective* additive endomorphisms globally conserving this particular support scalar and splitting the elementary input into two outputs of scalar `1/2`, the proved structural form is
`F(w,t)=(Aw,Kw+Bt)`, `A=D P diag(k1,k2,k3,k4) D`,
where `P` is one of the 16 admissible split permutations, `ki` are nonzero integers, `K` is arbitrary modulo 3, and `B ∈ GL2(F3)`.

## Theorem — exact joint spectrum

Writing `I=[G:F(G)]` and `E=exp(G/F(G))`, the possible pairs are **exactly**
```
I = 16*m,    E = 4*L,    m >= 1,    L | m | L^4.
```
For every permissible pair, every one of the 16 split-permutation choices admits a realizing map by choosing suitable nonzero integer multipliers. For fixed index `I=16*m`, the sharp extremes are
```
E_min(16*m) = 4 * product_over_p^e||m p^ceil(e/4),
E_max(16*m) = 4*m,
```
with empty product 1 for `m=1`. These are arithmetic **existence** statements, not arbitrary-scalar or surjective-conservation claims.

## Proof (unrestricted, exact)

The prior all-index theorem establishes
```
I = 16*product_i |ki|,        E = 4*lcm_i |ki|.
```
Put `m=product_i |ki|` and `L=lcm_i |ki|`. For each prime `p`, set `ri=v_p(|ki|)`, `e=v_p(m)=sum_i ri`, and `t=v_p(L)=max_i ri`. Necessarily `t <= e <= 4*t`, exactly the divisibilities `L|m` and `m|L^4`.

Conversely, given `m,L` with these divisibilities, for each prime `p|m` choose `r1=t=v_p(L)` and distribute `e-t` across `r2,r3,r4` within `[0,t]` (possible because `0<=e-t<=3t`). All exponents at primes not dividing `m` are zero. The four integers `ki=product_p p^ri` then have product `m` and lcm `L`. Any split `P` with `K=0,B=I_2` gives the requested injection by the preceding classification. Independent prime allocations give the sharp minimum `t=ceil(e/4)` and maximum `t=e`, proving the formulas.

Example: `m=32`, index `I=512`, attainable exponents exactly `{16,32,64,128}`; `ki=(4,2,2,2)` attains the minimum, and `ki=(32,1,1,1)` the maximum.

## Finite cross-check and boundaries

A local exact regression enumerated every ordered positive quadruple with product `1<=m<=128` (**5,137 tuples**), compared the resulting lcm set with `L|m|L^4` for all **128** indices, and verified **221** distinct index–exponent witnesses using exact rational inverse denominators of an admissible split matrix. All checks passed. The finite regression is not the proof; the unrestricted result follows from the prime-valuation argument.

Frozen source: Result `RR-AA38973D56330E59D315` / Blob `3366edeae347e76b1f6a50bc45a6c6e4cd2dd472`. Contributor context is exposed and not independent; this file creates no formal Review, Reference, Synthesis, Follow-up or task publication. The source classification/exponent results in `TORSION_EXTENSION.md` and `FULL_SMITH_AND_EXPONENT.md` remain prerequisite and unadmitted.
