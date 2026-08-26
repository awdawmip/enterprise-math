# P017 — A6 Order-4 Geometric B-Spline Cross-State Package

Status: `PROVED_WIP EXPLICIT TAIL + RECIPROCAL-WINDOW CONSTANT / NOT FULL BILINEAR CONSTANT / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_A6_FIVE_NINTH_ROOT_EDGE_PACKAGE_20260826.md`;
- `docs/P017_P2_EXPLICIT_BSPLINE_BALANCED_PACKAGE_20260825.md`;
- `docs/P017_P2_EXPLICIT_RECIPROCAL_SUM_LEMMA_20260825.md`;
- `docs/P017_P2_CENTERED_INCIDENCE_SPECTRAL_FRONTIER_20260826.md`;
- `docs/P017_P2_FINITE_SPLICE_MOBIUS_KERNEL_CENSUS_20260826.md`.

Purpose: after the physical-space residual energy and same-state Mobius core have been compressed, minimize the explicit smoothing cost paid by the irreducible cross-state sector. This note does not yet propagate constants through the full Cauchy quadruple sum or Rosser-Iwaniec factorization.

---

## 1. Freeze a low-order explicit smoothing

Keep the live root-edge values

\[
\theta=\frac{4999}{10000},
\qquad
 d=\frac59,
\qquad
 D=X^d.
\]

Use the order-4 compact B-spline from the existing explicit smoothing family:

\[
f_{4,y}(t)=4a^{-3}u_a^{*4}(t),
\qquad
 a=y/4,
\]

so

\[
\widehat f_{4,y}(\xi)
=y\left(\frac{\sin(\pi a\xi)}{\pi a\xi}\right)^4.
\]

Freeze the Fourier cutoff exponent

\[
\boxed{\eta=\frac1{40}.}
\]

For the cross-state factor split choose

\[
\boxed{
\mu=\frac{161777}{360000},
\qquad
\nu=\frac{4247}{40000},
}
\]

that is

\[
M=X^\mu,
\qquad
N=X^\nu.
\]

Exactly,

\[
\mu+\nu=\frac59=d.
\]

These values are obtained by balancing the explicit-cutoff diagonal and trivial off-diagonal exponents while keeping a materially stronger Fourier tail.

---

## 2. Source-Lemma-4 admissibility remains comfortable

Retain the already-used source parameter

\[
\varepsilon=\frac1{200}.
\]

The original sufficient conditions have exact positive margins.

### A2

\[
\theta-6\varepsilon-\mu
=
\boxed{\frac{7387}{360000}}
\approx0.0205194.
\]

### A3

\[
1-(\mu+2\nu)
=
\boxed{\frac{121777}{360000}}
\approx0.3382694.
\]

### A4

\[
\frac52\theta-\frac12-4\varepsilon-(\mu+2\nu)
=
\boxed{\frac{24487}{360000}}
\approx0.0680194.
\]

Thus lowering the B-spline order and moving the factor split does not push the packet against the source admissibility walls.

---

## 3. Exact structural powers with the explicit cutoff

The explicit B-spline replay gives the diagonal square-root saving

\[
\delta_{\rm diag}
=
\frac{\theta-\eta-\mu}{2},
\]

and the trivial off-diagonal square-root saving

\[
\delta_{\rm off}
=
\frac12\left[
\mu
-2(d-\theta)
-\frac{1-\theta}{2}
-\frac52\eta
\right].
\]

For the frozen values,

\[
\boxed{
\delta_{\rm diag}
=
\delta_{\rm off}
=
\frac{9187}{720000}
\approx0.0127597.
}
\]

For order `p=4`, the Fourier tail saving relative to the natural interval scale is

\[
\delta_{\rm tail}
=3\eta-(d-\theta)
=
\boxed{\frac{1741}{90000}}
\approx0.0193444.
\]

So the low-order package deliberately gives the tail more power room than the diagonal/off-diagonal terms.

---

## 4. Narrow geometric blocks make the order-4 tail cheap

Use geometric blocks of ratio

\[
\boxed{\rho=\frac65}
\]

as in the explicit reciprocal-sum lemma:

\[
M<m\le\rho M,
\qquad
N<n\le\rho N.
\]

For one such block put

\[
H=\frac{\rho^2MN}{y}X^\eta.
\]

Since `mn<=rho^2 MN`, the order-4 Fourier tail satisfies

\[
|r_{\rm tail}(mn)|
\le
C_4
\left(
\frac{mn}{\rho^2MN X^\eta}
\right)^3,
\qquad
C_4=\frac{512}{3\pi^4}.
\]

If `M,N>=1000`, then the number of integers in a ratio-`rho` block is at most `(rho-1)M+1`, and every such integer is at most `rho M`. Hence

\[
\sum_{M<m\le\rho M}m^3
\le
\rho^3\left(\rho-1+\frac1{1000}\right)M^4,
\]

and similarly for `n`.

After multiplying the two sums, the `rho^6` factor cancels the cutoff denominator. Therefore the total Fourier tail of one bounded-coefficient geometric block is at most

\[
\boxed{
C_4
\left(\frac15+\frac1{1000}\right)^2
D X^{-3\eta}.
}
\]

Using only the elementary inequality `pi>3`,

\[
C_4<\frac{512}{243},
\]

so the completely elementary block constant is

\[
\boxed{
\frac{512}{243}
\left(\frac{201}{1000}\right)^2
=
\frac{35912}{421875}
<0.085125.
}
\tag{O4-tail-constant}
\]

Relative to `y`, the block tail is therefore

\[
\boxed{
\frac{|R_{\rm tail}^{\rm block}|}{y}
<
\frac{35912}{421875}
X^{-1741/90000}.
}
\]

At the conservative Tier-A splice

\[
X_0=K_0^2,
\qquad
K_0=116009280740973308,
\]

exact integer exponentiation certifies

\[
\boxed{
\frac{35912}{421875}
X_0^{-1741/90000}
<\frac{19}{1000}=0.019.
}
\tag{O4-splice-tail}
\]

This is a natural-interval-scale statement for one factorable geometric block. It is not yet a direct subtraction from the source-normalized main coefficient `G_*`; the final count normalization and the number/grouping of factorable blocks remain separate bookkeeping.

---

## 5. The explicit reciprocal m-sum constant 15 is legal far below the splice

The existing explicit reciprocal-sum lemma on a ratio-`6/5` block states

\[
\left|
\sum_{M<m\le(6/5)M}e(t/m)
\right|
\le15\sqrt{t/M}
\]

provided

\[
\rho^{4/3}M^{5/3}\le t\le M^3/2.
\]

For the present `mu,nu,eta`, the lower-frequency exponent margin is

\[
1-2\nu-\frac53\mu
=
\boxed{\frac{41777}{1080000}}
\approx0.0386824.
\]

Thus the lower edge follows from

\[
X^{41777/1080000}\ge\rho^{10/3},
\]

or equivalently

\[
X\ge
\left(\frac65\right)^{3600000/41777}.
\]

The exponent `3600000/41777` is approximately `86.172`, so this threshold is only of order `10^7`, astronomically below the Tier-A splice.

The corresponding upper-frequency margin is

\[
3\mu-(d+1+\eta-\theta-\nu)
=
\boxed{\frac{67259}{180000}}
\approx0.373661.
\]

Hence the upper edge is even less restrictive.

Therefore the already-frozen explicit reciprocal constant `15` is fully legal throughout the finite scale relevant to this order-4 a6 package.

---

## 6. What remains expensive

This calculation removes two suspected sources of the finite constant problem:

1. the literal-Mobius same-state internal core is at most `13` at the splice;
2. the order-4 B-spline tail of one narrow factorable block is below `0.019 y` there;
3. the terminal reciprocal `m`-sum has the explicit constant `15` in a frequency window that opens long before the splice.

The remaining unresolved constant is therefore sharply localized to

\[
\boxed{
\text{Cauchy aggregation of }(n_1,n_2,h_1,h_2)
+
\text{Rosser/Iwaniec factorization multiplicity}
}
\]

on the cross-state centered sector.

The next task is not to increase the B-spline order. It is to group the equation

\[
k=h_1n_2-h_2n_1
\]

arithmetically before paying the constant `15`, and to avoid charging the generic factorization multiplicity to the same-state sector already removed by the P017 kernel census.

No full finite analytic threshold, no P2-in-every-square theorem, and no Legendre theorem is claimed here.
