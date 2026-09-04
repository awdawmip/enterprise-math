# Primitive Dirichlet spectral zeta moments and Jordan totients

Status: `FREE_RESEARCH / EXACT FINITE ARITHMETIC MOMENT HIERARCHY / NOT_FOUNDATION`
Date: `2026-09-04`
Researcher: `EM-FREE-W59A / FREE_AXIOM_DISCOVERY`
Issue: `#1159`
Depends on the divisor/primitive spectral decomposition.

## 1. Finite reciprocal spectral moments

For integer `M>=1`, let the nonzero finite Dirichlet roots be

\[
u_{1,M},\ldots,u_{M-1,M}.
\]

For `s>=1`, define

\[
\boxed{
Z_s(M):=
\sum_{k=1}^{M-1}\frac1{u_{k,M}^s}.
}
\tag{PSZ-1}
\]

This is a finite sum over the native spectrum.

## 2. Exact reciprocal elementary symmetric sums

The normalized characteristic continuant is

\[
H_M(u)
:=\frac{D_{M-1}(u)}M
=
\prod_{k=1}^{M-1}
\left(1-\frac{u}{u_{k,M}}\right).
\]

The finite continuant coefficient formula gives

\[
H_M(u)
=
\sum_{j=0}^{M-1}
(-1)^j
\frac{1}{M}\binom{M+j}{2j+1}
u^j.
\]

The central-factorial identity rewrites the coefficient as

\[
\frac{1}{M}\binom{M+j}{2j+1}
=
\frac{
\prod_{r=1}^{j}(M^2-r^2)
}{(2j+1)!}.
\]

Comparing with the root product therefore gives the exact reciprocal elementary symmetric sum

\[
\boxed{
e_j\left(
\frac1{u_{1,M}},\ldots,\frac1{u_{M-1,M}}
\right)
=
\frac{
\prod_{r=1}^{j}(M^2-r^2)
}{(2j+1)!}.
}
\tag{PSZ-2}
\]

For `j>=M`, the right side vanishes because the product contains `M^2-M^2`, agreeing with the finite number of roots.

Thus the reciprocal spectral symmetric functions are themselves central-factorial polynomials in `M^2`.

## 3. Newton recursion implies polynomial spectral zeta moments

Let

\[
E_j(M):=
\frac{
\prod_{r=1}^{j}(M^2-r^2)
}{(2j+1)!}.
\]

Newton identities give, for every `s>=1`,

\[
\boxed{
Z_s(M)
-E_1(M)Z_{s-1}(M)
+E_2(M)Z_{s-2}(M)
-\cdots
+(-1)^{s-1}E_{s-1}(M)Z_1(M)
+(-1)^s sE_s(M)=0.
}
\tag{PSZ-3}
\]

Since `E_j(M)` is a degree-`j` polynomial in `M^2`, induction gives

\[
\boxed{
Z_s(M)
=c_{s,0}+c_{s,1}M^2+\cdots+c_{s,s}M^{2s}
}
\tag{PSZ-4}
\]

with rational coefficients `c_(s,r)`.

The empty spectrum at `M=1` gives

\[
Z_s(1)=0,
\]

so

\[
c_{s,0}=-\sum_{r=1}^{s}c_{s,r}.
\]

## 4. First three full-spectrum moments

Newton recursion gives

\[
\boxed{
Z_1(M)=\frac{M^2-1}{6}.
}
\tag{PSZ-5}
\]

For the second moment,

\[
\boxed{
Z_2(M)
=\frac{(M^2-1)(2M^2+7)}{180}
=\frac{2M^4+5M^2-7}{180}.
}
\tag{PSZ-6}
\]

For the third,

\[
\boxed{
Z_3(M)
=\frac{(M^2-1)(8M^4+29M^2+71)}{7560}
=\frac{8M^6+21M^4+42M^2-71}{7560}.
}
\tag{PSZ-7}
\]

These formulas require no trigonometric sum identities; they come directly from finite continuant coefficients and Newton identities.

## 5. Primitive reciprocal moments

For `d>1`, define the primitive denominator-`d` moment

\[
\boxed{
Z_s^{\rm prim}(d)
:=
\sum_{\substack{1\le r<d\\\gcd(r,d)=1}}
\frac1{u_{r,d}^s}.
}
\tag{PSZ-8}
\]

The complete length-`M` spectrum is the disjoint union of primitive denominator classes, hence

\[
\boxed{
Z_s(M)
=
\sum_{\substack{d\mid M\\d>1}}
Z_s^{\rm prim}(d).
}
\tag{PSZ-9}
\]

Additive Möbius inversion gives

\[
\boxed{
Z_s^{\rm prim}(d)
=
\sum_{e\mid d}
\mu(d/e)Z_s(e).
}
\tag{PSZ-10}
\]

## 6. Jordan-totient transform theorem

Insert the polynomial expansion (PSZ-4) into (PSZ-10). For `d>1`,

\[
\sum_{e\mid d}\mu(d/e)=0,
\]

so the constant term disappears. For every `r>=1`,

\[
\sum_{e\mid d}\mu(d/e)e^{2r}
=J_{2r}(d),
\]

where `J_k` is the Jordan totient.

Therefore

\[
\boxed{
Z_s^{\rm prim}(d)
=
\sum_{r=1}^{s}
c_{s,r}J_{2r}(d).
}
\tag{PSZ-11}
\]

This is the general primitive spectral zeta/Jordan-totient dictionary.

## 7. First primitive formulas

From (PSZ-5),

\[
\boxed{
Z_1^{\rm prim}(d)
=\frac{J_2(d)}6.
}
\tag{PSZ-12}
\]

From (PSZ-6),

\[
\boxed{
Z_2^{\rm prim}(d)
=\frac{2J_4(d)+5J_2(d)}{180}.
}
\tag{PSZ-13}
\]

From (PSZ-7),

\[
\boxed{
Z_3^{\rm prim}(d)
=\frac{8J_6(d)+21J_4(d)+42J_2(d)}{7560}.
}
\tag{PSZ-14}
\]

Examples:

- `d=3`: primitive roots are `1,3`, so `Z_1^prim=1+1/3=4/3`; `J_2(3)/6=8/6=4/3`.
- `d=4`: primitive roots are `2-sqrt2,2+sqrt2`, whose reciprocal sum is `2`; `J_2(4)/6=12/6=2`.

## 8. Arithmetic interpretation

The product-level primitive mass law is multiplicative/Möbius:

\[
P_d=\prod_{e\mid d}e^{\mu(d/e)}.
\]

The reciprocal-moment hierarchy is its additive spectral-zeta counterpart:

\[
Z_s^{\rm prim}(d)
=\sum_{e\mid d}\mu(d/e)Z_s(e).
\]

Thus the same finite divisor filtration yields two complementary arithmetic readouts:

```text
primitive product mass
   -> prime-power dichotomy

primitive reciprocal zeta moments
   -> Jordan totients J_2, J_4, ...
```

## 9. Generating-function viewpoint

Since

\[
H_M(u)
=
\prod_k(1-u/u_k),
\]

formally near `u=0`,

\[
\boxed{
-\log H_M(u)
=
\sum_{s=1}^{\infty}
\frac{Z_s(M)}s u^s.
}
\tag{PSZ-15}
\]

Likewise, if `Psi_d` is the normalized primitive denominator factor,

\[
\boxed{
-\log\Psi_d(u)
=
\sum_{s=1}^{\infty}
\frac{Z_s^{\rm prim}(d)}s u^s.
}
\tag{PSZ-16}
\]

Equation (PSZ-11) therefore says that the logarithmic germ of each primitive spectral factor is governed by Jordan totients.

This suggests a finite spectral analogue of arithmetic Euler-factor expansions without importing a continuous spectral operator.

## 10. Research consequence

Freeze:

`RECIPROCAL_ELEMENTARY_SPECTRUM = CENTRAL_FACTORIAL_POLYNOMIALS`.

`FULL_SPECTRAL_ZETA_s(M) = POLYNOMIAL_IN_M^2`.

`PRIMITIVE_SPECTRAL_ZETA_s(d) = JORDAN_TOTIENT_TRANSFORM`.

The first exact dictionary is

`Z_1^prim = J_2/6`,

with higher moments given by the same universal Newton coefficients applied to `J_4,J_6,...`.
