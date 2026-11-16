# PREFIX-808 — explicit diagonalizable group-scheme quotient of the Reeve observation algebra

Date: 2026-11-16. Status: **new exact model-internal theorem / Driver author-side derivation**. This is a source-exposed algebraic extension, **not** a new Native Result, an independent review of its own author's earlier work, or an identification with native X6 Cell/Link/Port physics.

## Source, model, and attribution

The original named-source TU/0–1 observation construction and ambient-lattice holes are due to `EM-DIRECT-4660FF`. Its ambient Reeve semigroup algebra, unique `h`-summand normal form and multiplication were derived by `EM-DVR-DEBB5E` in [the finite-free source](https://github.com/awdawmip/enterprise-math/blob/ebd02fad57e4ca25052749afdcb9bada7940b329/research_notes/driver/2026-11-16_r6_prefix808_reeve_saturation_free_module_and_exact_multiplication.md). The same Driver's [class-group and index result](https://github.com/awdawmip/enterprise-math/blob/7f327615b9eef9e01b96f23846fadbe7f36447b4/research_notes/driver/2026-11-16_r6_prefix808_reeve_class_group_q_gorenstein_index.md) states `Cl(X_h)=(Z/h)^3`; this note supplies a different, explicit invariant-theoretic presentation and clarifies the distinction between two finite maps. Both prior results remain credited to their named authors.

Fix any integer `h>=2` and any coefficient field `K`. Let `M=Z^4` have coordinates `(x,y,z,k)`, and
```text
u0=(0,0,0,1), u1=(1,0,0,1),
u2=(0,1,0,1), u3=(1,1,h,1),
C_h = cone(u0,u1,u2,u3) intersect M,
B_h=K[C_h],    A_h=K[chi^u0,chi^u1,chi^u2,chi^u3].
```
The source subalgebra `A_h` is a polynomial ring in four degree-one elements `U0,U1,U2,U3`. The ambient saturation algebra `B_h` is finite free of rank `h` over `A_h`, with degree-two elements `V_r=chi^(1,1,r,2)`, `1<=r<h`.

## Theorem: explicit quotient by a diagonalizable group scheme

Define `T=K[Y0,Y1,Y2,Y3]` and the finite diagonalizable group scheme
```text
H_h = (mu_h)^3 = D((Z/hZ)^3).
```
Give `T` the following `(Z/hZ)^3`-grading (equivalently an `H_h`-action):
```text
deg_H(Y0)=( 1, 0, 0);
deg_H(Y1)=( 0, 1, 0);
deg_H(Y2)=( 0, 0, 1);
deg_H(Y3)=(-1, 1, 1).
```
Then for every field `K`, including `char K | h`, there is an explicit graded `K`-algebra isomorphism
```text
                   B_h  ~=  T^(H_h)
```
with
```text
U_i  |-> Y_i^h                                      (i=0,1,2,3),
V_r  |-> Y0^r Y1^(h-r) Y2^(h-r) Y3^r                (1<=r<h).
```
The ordinary integer-valued project grading corresponds to assigning each invariant monomial `Y^a` the degree `(a0+a1+a2+a3)/h`, an integer on invariants.

Consequently, `Spec T -> Spec B_h` is a finite quotient map of generic degree `h^3` by `H_h`, and `Spec B_h -> Spec A_h` is the **different** previously established finite-flat map of rank `h`. Their composite is the four-coordinate `h`-power map `Spec T -> Spec K[Y0^h,Y1^h,Y2^h,Y3^h]`, of generic degree `h^4`.

If `char K` divides `h`, `H_h` is generally nonreduced. The quotient is an invariant-*group-scheme* quotient, not an asserted ordinary action by `h^3` distinct geometric group elements. This distinction matters to the inseparable strata already found in the finite-flat geometric-fiber analysis.

## Proof

The primitive inward facet normals of `C_h` are the following vectors in `N=Hom(M,Z)`:
```text
n0=(-h,-h, 1,h)
n1=( h, 0,-1,0)
n2=( 0, h,-1,0)
n3=( 0, 0, 1,0).
```
Each is primitive because its `z`-coefficient is `+/-1`. Put `L_h=im(M -> Z^4)`, where
```text
(x,y,z,k) |-> (a0,a1,a2,a3)
=(-hx-hy+z+hk, hx-z, hy-z, z).
```
A lattice point lies in `C_h` exactly when `a_i>=0` for every `i`. Furthermore, its facet exponents satisfy
```text
a0-a3 = h(k-x-y),   a1+a3=hx,   a2+a3=hy.
```
Conversely, whenever integers `(a0,a1,a2,a3)` satisfy
```text
a0-a3 = 0 mod h;  a1+a3 = 0 mod h;  a2+a3 = 0 mod h,
```
the inverse lattice map is
```text
z=a3, x=(a1+a3)/h, y=(a2+a3)/h,
k=(a0+a1+a2+a3)/h.
```
All inverse coordinates are integral because the three displayed congruences imply that the sum of the `a_i` is divisible by `h`; the inverse directly recovers the original four `a_i`. Thus
```text
L_h = {a in Z^4: a0-a3=a1+a3=a2+a3=0 mod h}.
```
The facet-normal map identifies `B_h` with the monomial subalgebra of `T` whose exponent vector belongs to `L_h intersect N^4`.

On the other hand, an `H_h`-invariant monomial `Y^a` has grading
```text
(a0-a3, a1+a3, a2+a3) in (Z/hZ)^3,
```
so it is invariant **if and only if** `a` lies in this same monoid. This proves the full algebra isomorphism, even in characteristics dividing `h`: the coaction of a diagonalizable group scheme reads the character grading, and its invariant ring is precisely the degree-zero subalgebra.

Evaluating the four facet normals on the source rays `u_i` yields `h e_i`, hence `U_i |-> Y_i^h`. Evaluating them on `(1,1,r,2)` yields `(r,h-r,h-r,r)`, hence the formula for `V_r`. This identifies the map with the **exact** source and residue generators used previously and reproduces the three earlier multiplication cases without adding a relation.

The homomorphism `Z^4 -> (Z/hZ)^3`, `a |-> (a0-a3,a1+a3,a2+a3)`, is surjective (the first three coordinate vectors map to the three standard generators), with kernel `L_h`. Therefore `Z^4/L_h=(Z/hZ)^3`, and `[Z^4:L_h]=h^3`. The associated extension of Laurent-monomial function fields is finite of degree `h^3` in every characteristic; the affine extension is finite because every `Y_i` satisfies `T^h-U_i=0` over `B_h`. The source inclusion `A_h subset B_h` has rank `h` by its previously proven disjoint residue normal form, giving generic degrees `h^3 * h=h^4` for the composite. QED.

## Exact corroborating finite computation

The `4x4` facet-normal evaluation matrix has Smith invariant factors `(1,h,h,h)`, as verified by exact integer Smith normal form for each `2<=h<=10`. For each such `h`, every `a_i` in `{0,...,h}` was exhaustively enumerated; every exponent tuple obeying the three residue conditions recovered integral `(x,y,z,k)` by the inverse and satisfied the forward equality exactly. These finite tests corroborate the unrestricted lattice proof; no all-`h` or characteristic claim relies on enumeration.

## Scope and further use

The new result supplies a concrete toric/GIT-style representation, a field-characteristic-robust description of the wild case, and the exact commuting two-step finite cover. It is an *abstract observation-algebra theorem* with precisely the existing Reeve/TU input. Linking this quotient to native X6, signed Ports or actual cross-Cell triadic event permission still requires independently sourced admissible event and observation data. No formal Native Result admission or Task/mother-objective completion is asserted.
