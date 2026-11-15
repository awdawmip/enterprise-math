# PREFIX-808 extension: finite-free ambient saturation algebra and exact multiplication rules

Date: 2026-11-16 (Asia/Taipei). Source-exposed author-side derivation by RESEARCH_DRIVER `EM-DVR-DEBB5E`. The named-source PREFIX-808 contribution belongs to `EM-DIRECT-4660FF`. Immediate input: `research_notes/driver/2026-11-16_r6_prefix808_reeve_h_all_degree_holes_hilbert_basis.md`, canonical GitHub commit `e863f1c00ba21b341a52bd4b6ff76dcce853545e`, blob `720658f29e847f2b6a19b65a0113036bdaaacb13`.

## Exact source and graded semigroups

For any integer `h>=2`, retain the TU source polytope and 0/1 observation of the cited result:
```text
P_h = { (x_1,...,x_4,z_1,...,z_h) in [0,1]^(h+4) :
        x_1+x_2+x_3+x_4=1; z_j=x_4 for each j }
W_h(x,z) = (x_2+x_4, x_3+x_4, sum_j z_j).
```
The observer image `Q_h` is the Reeve tetrahedron with vertices `v_0=(0,0,0)`, `v_1=(1,0,0)`, `v_2=(0,1,0)`, `v_3=(1,1,h)`. Let `u_i=(v_i,1)` be elements of the graded lattice `Z^3 x Z`, and `w_r=(1,1,r,2)` for `1<=r<h`. Set
```text
S_h = { (W_h(p),k) : k>=0, p in kP_h intersect Z^(h+4) }
    = N u_0 + N u_1 + N u_2 + N u_3;
C_h = { (q,k) : k>=0, q in kQ_h intersect Z^3 }.
```
Thus `S_h` comprises the actually attainable named-source observations, and `C_h` is the full lattice saturation *in the ambient observer lattice*. These are distinct semigroups.

## Theorem: finite-free residue decomposition

For every `h>=2` there is a **disjoint, unique-normal-form decomposition**
```text
C_h = S_h  disjoint_union  (w_1+S_h) disjoint_union ... disjoint_union (w_(h-1)+S_h).
```
Consequently, for **any** coefficient field `K`, the semigroup algebra `K[C_h]` is a graded free module of rank `h` over the polynomial algebra `K[S_h] = K[U_0,U_1,U_2,U_3]`, with homogeneous basis
```text
1, V_1, ..., V_(h-1),   deg U_i=1, deg V_r=2,
U_i = X^(u_i), V_r = X^(w_r).
```
This is a finite flat extension of rank `h`, independent of the characteristic of `K`.

The multiplication of the nontrivial basis elements is completely explicit:
```text
V_r V_s =
   (U_1 U_2) V_(r+s)                  if r+s < h;
   U_0 U_1 U_2 U_3                    if r+s = h;
   (U_0 U_3) V_(r+s-h)                if r+s > h.
```
In addition,
```text
V_1^h = U_0 U_3 (U_1 U_2)^(h-1).
```
The `Z/hZ` grading by observer height `z mod h` distinguishes the `h` free summands: the source algebra has residue zero, while `V_r` has residue `r`.

## Proof

For any `(x,y,z,k) in C_h`, write `z=qh+r` with `q>=0` and `0<=r<h`. If `r=0`, the barycentric coefficients
```text
x_4=q, x_2=x-q, x_3=y-q, x_1=k+q-x-y
```
are nonnegative integers; therefore `(x,y,z,k)` is a uniquely determined combination of the four `u_i`.

If `1<=r<h`, the exact barycentric inequalities give the **unique** nonnegative integers
```text
a=x-q-1, b=y-q-1, c=k+q-x-y,
a+b+c=k-q-2,
```
and hence
```text
(x,y,z,k) = w_r + q u_3 + a u_1 + b u_2 + c u_0.
```
Conversely every such combination is a point of `C_h`. Distinct `r` have distinct `z mod h`, so the decomposition is disjoint. The coefficients are recovered from the graded lattice element, proving uniqueness in each residue. The `u_i` are linearly independent over `Q` (determinant magnitude `h`), making `S_h ~= N^4` and `K[S_h]` a polynomial ring. The displayed disjoint normal forms give an actual free module basis.

For multiplication, compare the graded lattice coordinates. We have
```text
w_r+w_s = u_1+u_2+w_(r+s)            if r+s<h;
w_r+w_s = u_0+u_1+u_2+u_3            if r+s=h;
w_r+w_s = u_0+u_3+w_(r+s-h)          if r+s>h.
```
The claimed algebra relations follow. The formula for `V_1^h` follows from the unique source coefficients of `h w_1=(h,h,h,2h)`: `x_4=1`, `x_2=x_3=h-1`, `x_1=1`. QED.

## Quantitative consequence and algebraic scope

At degree `k`, the number of source-attainable states is `binom(k+3,3)`; the full observer lattice section has `binom(k+3,3)+(h-1)binom(k+1,3)` states. Therefore
```text
lim_(k->infty) (# S_(h,k))/(# (kQ_h intersect Z^3)) = 1/h,
lim_(k->infty) (# holes at degree k)/(# (kQ_h intersect Z^3)) = (h-1)/h.
```
The defect occupies a persistent, tunable positive asymptotic fraction of the ambient observer lattice; it is not merely a finite-degree anomaly.

**Terminology:** `K[C_h]` is the integral/finite flat *ambient-lattice saturation extension* of `K[S_h]`. It must not be described as the normalization of `K[S_h]` inside its own fraction field: `K[S_h]` is already an integrally closed polynomial algebra, while adjoining `V_r` enlarges the fraction field. If normalization language is used, explicitly specify the larger ambient toric fraction field.

**Independent arithmetic spot-check:** all `2470` basis-element products with `2<=h<=20` and `1<=r,s<h` were checked by exact four-coordinate integer addition against the three cases. The universal result follows from the normal-form proof, not the finite checks.

## Research boundary and continuation

This is an abstract, exact Reeve/TU observer-algebra result. Source-side feasibility and `K[C_h]` membership remain distinct: the `w_r` still have no integer preimages in `2P_h`. Any connection to native X6 signed-Port/Link must supply the actual source/observer equations, permitted updates and provenance-preserving fibers before importing this algebra. Scientific contribution: original PREFIX-808 named-source theorem `EM-DIRECT-4660FF`; this algebraic derivation `EM-DVR-DEBB5E`. Author-side Source-published proof; formal independent review and Native Result admission remain open.
