# F7 A6 — singular torsion conservation blind spots and nonsplit residuals

**2026-10-31 · AUTHOR_SIDE / EXPOSED_SHARED_CONTEXT / NOT_INDEPENDENT / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE.** Supplement to Draft PR #1753. Frozen F7 Result `RR-AA38973D56330E59D315` (Git blob `3366edeae347e76b1f6a50bc45a6c6e4cd2dd472`) and reversible `GL4(Z)` no-go remain unchanged. This is an auxiliary F6 carrier theorem, with no native X6 or three-dimensional-slice transfer.

**Setup.** Let `G=Z^4⊕T`, `T=(Z/3)^2`, `C=[[1,1],[1,-1]]`, `D=diag(C,C)`, and `Q(w,t)=#supp(Dw)/2`. Require global `Q(F(w,t))=Q(w,t)` and marked output-slot balance `1/2+1/2` for free input `e=(1,0,0,0)`. The fixed scalar has the inherited unary R/J/S invariances and strict old-projection positivity. The frozen F7 packet does not impose operator equivariance on `F`.

## Theorem A — all maps, including non-injective torsion blocks

Every **additive endomorphism** with these two conditions, without assuming injectivity, has the unique form

`F(w,t)=(Aw, Kw+Bt mod 3)`, `A=D P diag(k1,k2,k3,k4) D`,

where `P` is one of the 16 channel permutations splitting the first two marked channels between output slots, each `ki∈Z\{0}`, `K∈M(2×4,F3)` is arbitrary and **`B∈M(2,F3)` is arbitrary, including singular matrices**. These conditions force free-coordinate injectivity, but not full-group injectivity. With `r=rank_F3(B)`,

`ker(F)={0}⊕ker(B)`, `|ker F|=3^(2-r)`,
`[G:F(G)]=16*(∏|ki|)*3^(2-r)`.

At minimal free index 16, `B` of ranks 0,1,2 occurs in exactly 1,32,48 choices. With 16 split permutations, 16 signs and 3^8 torsion couplings, the numbers of distinct maps are respectively **1,679,616 / 53,747,712 / 80,621,568**. Full indices are respectively **144 / 48 / 16**; kernel sizes are **9 / 3 / 1**. This counts endomorphisms in the fixed presentation, not physical equivalence classes.

*Proof.* Any homomorphism from finite torsion to `Z^4` vanishes, giving the displayed block form. Since `Q` vanishes on the free part only at zero, conservation forces `A` to be injective. Set `L=D Z^4`; each `2e_i` belongs to `L`. For `T_0=DAD^(-1)`, conservation forces every column to have exactly one nonzero entry; injectivity forces four different output rows. Thus `T_0=P diag(λ_i)`. The marked balance makes `P` split the two first channels. Because `A=(1/2)D P diag(λ_i)D`, each split 2×2 slot block has integer entries `±λ_i/2`, so `λ_i=2ki` for nonzero integers `ki`. Conversely `DA=2P diag(ki)D` preserves all four support indicators and the split. The kernel of `F` is precisely `ker B`, since `A` is injective. For each free image `Aw`, attainable torsion outputs form `Kw+BT`; every free cokernel class therefore has `3^(2-r)` torsion cosets. The finite rank and parameter counts give the stated multiplicities.

## Theorem B — exact torsion residual extension and nonsplit family

For every map above there is a short exact sequence

`0 → T/BT → G/F(G) → Z^4/AZ^4 → 0.`

It splits as finite abelian groups when `3∤det A`. When `3|det A`, the torsion coupling can change the full cokernel **even with exactly the same free matrix, scalar and kernel size**.

Take any split `P`, `A0=DPD` (determinant ±16), `A=3A0`, `B=0`, and arbitrary `K` of rank `s∈{0,1,2}` over F3. Then

`[G:F(G)]=16*3^6=11664`, `|ker F|=9`, and

`G/F(G) ≅ (Z/2)^2 ⊕ Z/4 ⊕ (Z/9)^s ⊕ (Z/3)^(6-2s).`

Thus `s=0` gives exponent 12 and a split extension; **`s=1` or `s=2` gives exponent 36 and a genuinely nonsplit extension**.

*Proof.* Any `(0,t)` in `F(G)` must have `Aw=0`, hence `w=0`, proving exactness at the torsion subgroup. Coprime primary components split. For this family, `A0` is invertible over the 3-local integers because its determinant is ±16. The 3-primary presentation is therefore equivalent to generators `x_1,...,x_4,y_1,y_2` with `3x_i+∑_j K_{ji}y_j=0` and `3y_j=0`. Bringing `K` to rank normal form pairs `s` free order-3 generators with `s` torsion order-3 generators, replacing each pair by a cyclic order-9 generator; the rest stay order 3. This gives `(Z/9)^s⊕(Z/3)^(6-2s)`. At 2, multiplying the free map by 3 is invertible, and `A0` has Smith factors `(1,2,2,4)` (minors have determinantal divisors 1,2,4,16). This yields `(Z/2)^2⊕Z/4`. The 9-torsion for `s>0` rules out splitting because a split 3-primary group here would be `(Z/3)^6`.

## Exact finite regression and boundary

A local deterministic `sympy`-integer-Smith checker produced **PASS**: 16 split permutations; 3,888 bounded scalar-conservation cases; 2,916 6×8 presentation-index cases across all 81 torsion B matrices in selected free/coupling families; and 81 K-family 3-primary decomposition cases covering ranks 0/1/2. Finite checks are regression evidence, not the universal proof. Local artifact `check_singular_torsion.py` SHA256 `477b8130492f38ea8cc39c6bdc70d3db20f80cdd35192ac58ad2c21164c9912a`; `CHECK_RESULT.json` SHA256 `e2689aab7e41b43b0512d109aeaa904d1131de84fb5518d3ecccdd0e7281547f`.

This identifies a typed **scalar-conservation blind spot**: the auxiliary scalar cannot certify torsion preservation or the full residual quotient. The result is confined to this explicit fixed scalar, finite torsion and F7 A6 relaxation. It does not change original reversible F7, prove a native X6 physical claim, or perform Source-native Review/Reference/Synthesis/Follow-up/Task publication. Eligible follow-up is an exact-set, contribution-independent Driver review under current Source session/DA.
