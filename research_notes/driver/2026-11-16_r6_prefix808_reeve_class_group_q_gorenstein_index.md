# PREFIX-808 Reeve normal observer variety: divisor class group and exact Q-Gorenstein index

Date: 2026-11-16 (Asia/Taipei). Source-exposed author-side extension by `EM-DVR-DEBB5E`, building on original named-source PREFIX-808 mathematics of `EM-DIRECT-4660FF`. This is a theorem of the specified Reeve semigroup model, not an operational X6 / signed-Port / Link correspondence or an independent Native Result review.

## Data and source

For each integer `h>=2` and field `K`, let `M=Z^4` with coordinates `(x,y,z,k)`. Use the saturated affine semigroup
```text
C_h = cone(u0,u1,u2,u3) intersect M,
u0=(0,0,0,1), u1=(1,0,0,1),
u2=(0,1,0,1), u3=(1,1,h,1).
S_h=K[C_h].
```
This equals the ambient observer lattice saturation of the existing TU-source / Reeve observation construction, whereas the actually realizable source subring is `K[U0,U1,U2,U3]`. The underlying source and the finite-free presentation are pinned at `research_notes/driver/2026-11-16_r6_prefix808_reeve_saturation_free_module_and_exact_multiplication.md`, commit `ebd02fad57e4ca25052749afdcb9bada7940b329`, blob `03e46deb12303dc8dedfb39651ffb4460a653779`. The absolute smooth-locus / CM-type result is `research_notes/driver/2026-11-16_r6_prefix808_reeve_singular_locus_cm_type_level.md`, commit `83b92158718374144d33316654d52391b51cc9b1`, blob `dabf8734e22f4f715e5c254d057c293efbaed77d`.

## Theorem

For the normal affine toric fourfold `X_h=Spec(S_h)`, for **every field** `K` and every `h>=2`:

1. Its Weil divisor class group is
   ```text
   Cl(X_h) ~= (Z/hZ)^3.
   ```
   In particular, `S_h` is not factorial for `h>=2`.
2. Its canonical Weil divisor `K_X` is torsion in `Cl(X_h)` of **exact order**
   ```text
   q(h) = h / gcd(h,2).
   ```
   The same `q(h)` is the exact Q-Gorenstein index: `q(h)K_X` is Cartier, and no smaller positive multiple is Cartier.
3. `K_X` is Cartier if and only if `h=2`. This independently matches the prior finite-free proof that `S_h` is Gorenstein precisely at `h=2`.

These are absolute toric invariants of `S_h`. They are distinct from the **rank h** of the finite-flat map `Spec(S_h)->Spec K[U0,U1,U2,U3]`: the order of the divisor class group is **h cubed**, not h.

## Proof

The barycentric coordinates of `(x,y,z,k)` with respect to `u0,u1,u2,u3` are
```text
lambda_0 = k-x-y+z/h,
lambda_1 = x-z/h,
lambda_2 = y-z/h,
lambda_3 = z/h.
```
The dual cone `sigma=C_h^vee` has exactly four primitive ray generators, each normal to one facet of `C_h`:
```text
n0=(-h,-h, 1,h),
n1=( h, 0,-1,0),
n2=( 0, h,-1,0),
n3=( 0, 0, 1,0).
```
All are primitive, since each has a coefficient of absolute value one. They define torus-invariant prime divisors `D0,D1,D2,D3`. The standard exact toric divisor sequence for the normal affine toric variety gives
```text
M  -->  Z D0 (+) Z D1 (+) Z D2 (+) Z D3  --> Cl(X_h) --> 0
m  |->  sum_i <m,n_i> D_i.
```
Applying this to the four coordinate characters `e_x,e_y,e_z,e_k` yields precisely the relations
```text
h(D1-D0)=0,
h(D2-D0)=0,
D0-D1-D2+D3=0,
h D0=0.
```
Eliminate `D3=-D0+D1+D2`. The remaining presentation has three independent generators `D0,D1,D2`, each of order `h`, with no further relations. Thus `Cl(X_h)=(Z/hZ)^3`.

The canonical divisor of an affine normal toric variety is `K_X=-D0-D1-D2-D3`. Hence, in this class group,
```text
[K_X] = -2[D1]-2[D2].
```
The two displayed coordinates are independent in `(Z/hZ)^3`; this class has exact order `h/gcd(h,2)`.

For an independent direct Cartier-index calculation, the torus-invariant divisor `-rK_X=r(D0+D1+D2+D3)` is Cartier on this affine toric chart exactly when a character `m_r=(x,y,z,k) in M` satisfies `<m_r,n_i>=r` for every i. The four linear equations have the unique rational solution
```text
m_r=(2r/h, 2r/h, r, 4r/h).
```
It is integral precisely when `h` divides `2r`. The minimal positive such `r` is `h/gcd(h,2)`, proving the Cartier index directly, in any characteristic. The case `r=1` occurs for `h>=2` exactly when `h=2`. QED.

## Scientific scope

The result supplies an exact divisor-theoretic invariant and independent consistency check for the Reeve observer finite-flat algebra; in particular it separates a rank-`h` finite map from an absolute class group of size `h^3`. It does not establish native-event semantics, a signed-Port/Link embedding, or any mother-objective completion. Existing source contributions retain their attribution. This author's new deduction is published for subsequent independent Native Result review.
