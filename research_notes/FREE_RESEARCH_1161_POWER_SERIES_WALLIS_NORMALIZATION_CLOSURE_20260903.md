# Free Research #1161 — power-series/Wallis normalization closure: `Pi_* = tau`

Status: `FREE_RESEARCH_RESULT / INTERNAL COMPLETION BRIDGE PROVED / ANALYTIC POWER-SERIES LAYER / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Cross-family source: `#1159` internal rotation-completion constant `tau`

## 0. Result

The previously open internal normalization bridge is now closed without elliptic integrals, classical circumference, or a target numerical value of pi:

\[
\boxed{\Pi_*=\tau}.
\]

Here

\[
\Pi_*=\frac{4M^2}{A_\infty}
\]

is the endogenous Gauss–Legendre completion defined by #1161, while `tau` is the independently defined #1159 boundary-completion constant obtained from finite rational determinant/Wallis data.

The proof is analytic at the power-series level. It is **not** an N0/native scalar promotion. The classical name `pi` remains a separate identification of `tau`.

## 1. A pi-free power series

Define

\[
F(z)=\sum_{n=0}^\infty c_n z^n,
\]

where

\[
c_n
=\left(\frac{(1/2)_n}{n!}\right)^2
=\frac{\binom{2n}{n}^2}{16^n}.
\]

Equivalently,

\[
c_0=1,
\qquad
\frac{c_{n+1}}{c_n}
=\left(\frac{n+1/2}{n+1}\right)^2.
\]

No gamma constant, elliptic integral, circle, or pi value is needed to define this series.

The coefficient recurrence gives the differential equation

\[
\boxed{
z(1-z)F''(z)+(1-2z)F'(z)-\frac14F(z)=0,
}
\]

with the unique analytic normalization `F(0)=1`.

Indeed, coefficient comparison gives

\[
(n+1)^2c_{n+1}=(n+1/2)^2c_n,
\]

so the analytic germ at `z=0` is uniquely determined by its constant term.

## 2. Exact finite coefficient/Wallis relation

Let the #1159 finite Wallis product be

\[
W_n=
\prod_{r=1}^n
\frac{(2r)^2}{(2r-1)(2r+1)}.
\]

Also put

\[
A_n^{\rm odd/even}
=
\prod_{r=1}^n\frac{2r-1}{2r}.
\]

Then

\[
c_n=(A_n^{\rm odd/even})^2.
\]

Moreover

\[
\begin{aligned}
\frac1{W_n}
&=
\prod_{r=1}^n
\frac{(2r-1)(2r+1)}{(2r)^2}\\
&=
(2n+1)(A_n^{\rm odd/even})^2.
\end{aligned}
\]

Therefore the exact finite bridge is

\[
\boxed{(2n+1)c_nW_n=1.}
\]

The #1159 result proves

\[
W_n\longrightarrow W_\infty=\tau/2.
\]

Hence

\[
\boxed{nc_n\longrightarrow\frac1\tau.}
\]

This is the only normalization input needed from the independent rotation/Wallis family.

## 3. Endpoint response of the power series from the Wallis limit

Differentiate termwise for `0<z<1`:

\[
F'(z)=\sum_{n\ge1}nc_nz^{n-1}.
\]

Because `nc_n -> 1/tau`, the elementary Abel limit gives

\[
\boxed{(1-z)F'(z)\longrightarrow\frac1\tau}
\qquad(z\to1^-).
\]

For completeness, if `a_n=nc_n`, then for every epsilon choose `N` with

\[
|a_n-1/\tau|<\varepsilon
\]

for `n>=N`. Splitting the geometric sum into the first `N` terms and the tail proves

\[
(1-z)\sum_{n\ge1}a_nz^{n-1}\to1/\tau.
\]

A companion logarithmic asymptotic follows from

\[
F(z)-1=\sum_{n\ge1}\frac{nc_n}{n}z^n
\]

and

\[
\sum_{n\ge1}\frac{z^n}{n}=-\ln(1-z):
\]

\[
F(z)\sim\frac1\tau\ln\frac1{1-z}.
\]

Only the derivative limit will be needed for the Wronskian constant.

## 4. Gauss quadratic transformation from the same ODE

For `0<x<=1`, define

\[
q=\frac{1-x}{1+x}.
\]

The following identity is the exact quadratic transformation required by the AGM:

\[
\boxed{
F(1-x^2)
=
\frac{2}{1+x}F(q^2).
}
\]

It can be verified without elliptic integrals or any pi normalization as follows.

Set `z=1-x^2`, choose the positive analytic germ `x=sqrt(1-z)` at `z=0`, and define

\[
G(z)
=
\frac{2}{1+\sqrt{1-z}}
F\left(
\left(
\frac{1-\sqrt{1-z}}{1+\sqrt{1-z}}
\right)^2
\right).
\]

`G` is analytic at `z=0` and `G(0)=1`. Direct chain-rule substitution into the differential equation for `F` shows that `G` satisfies the same equation

\[
z(1-z)G''+(1-2z)G'-G/4=0.
\]

The analytic coefficient recurrence at `z=0` is unique once the constant term is fixed, so `G=F` near zero. Analytic continuation along the real interval `0<=z<1` yields the stated transformation.

This is a power-series/ODE proof of the quadratic transform. It does not use an elliptic-integral representation.

## 5. Exact identification with reciprocal AGM

Let

\[
x_0=x,
\qquad
x_{n+1}=\frac{2\sqrt{x_n}}{1+x_n}.
\]

For the AGM pair normalized by `a_0=1`, `b_0=x`, one has

\[
x_n=b_n/a_n
\]

and

\[
a_{n+1}=a_n\frac{1+x_n}{2}.
\]

Also

\[
1-x_{n+1}^2
=
\left(\frac{1-x_n}{1+x_n}\right)^2.
\]

Therefore the quadratic transformation gives

\[
F(1-x_n^2)
=
\frac{2}{1+x_n}F(1-x_{n+1}^2).
\]

Iterating,

\[
F(1-x^2)
=
\frac1{a_N}F(1-x_N^2).
\]

The AGM ratio satisfies `x_N -> 1`, hence `F(1-x_N^2)->F(0)=1`, while `a_N->M(1,x)`. Thus

\[
\boxed{
F(1-x^2)=\frac1{M(1,x)}.
}
\]

This is the exact reciprocal-AGM identity reconstructed from the finite AGM update and the pi-free power series.

## 6. Complementary solutions and their Wronskian

Define

\[
Y_1(x)=F(1-x^2),
\qquad
Y_2(x)=F(x^2).
\]

Direct substitution of `z=1-x^2` or `z=x^2` into the power-series differential equation shows that both solve

\[
\boxed{
x(1-x^2)Y''+(1-3x^2)Y'-xY=0.}
\]

Let

\[
W(x)=Y_1Y_2'-Y_2Y_1'.
\]

After division by `x(1-x^2)`, the coefficient of `Y'` is

\[
P(x)=\frac{1-3x^2}{x(1-x^2)}
=\frac{d}{dx}\ln[x(1-x^2)].
\]

Abel's Wronskian identity therefore gives

\[
\boxed{
W(x)=\frac{C}{x(1-x^2)}
}
\]

for one constant `C`.

## 7. The Wronskian constant from #1159 Wallis normalization

Take `x->0+`.

For `Y_1=F(1-x^2)`, the endpoint derivative limit from Section 3 gives

\[
x^2F'(1-x^2)\to1/\tau,
\]

hence

\[
Y_1'(x)
=-2xF'(1-x^2)
\sim-rac{2}{\tau x}.
\]

For `Y_2=F(x^2)`,

\[
Y_2(x)\to1,
\qquad
Y_2'(x)=2xF'(x^2)\to0.
\]

Also the logarithmic growth of `Y_1` is only `O(log(1/x))`, so

\[
Y_1Y_2'\to0.
\]

Consequently

\[
W(x)\sim\frac{2}{\tau x}.
\]

Therefore

\[
\boxed{C=2/\tau.}
\]

No classical value of pi has entered this calculation.

## 8. The same Wronskian constant from the #1161 self-dual response

Let

\[
x_*=1/\sqrt2,
\qquad
\sqrt{1-x_*^2}=x_*.
\]

By the reciprocal-AGM identity,

\[
Y_1(x_*)=Y_2(x_*)=1/M,
\]

where

\[
M=M(1,x_*).
\]

Differentiate with respect to `x`.

For `Y_1=1/M(1,x)`,

\[
Y_1'(x_*)=-M'/M^2.
\]

For

\[
Y_2(x)=1/M(1,\sqrt{1-x^2}),
\]

the complementary variable has derivative `-1` at the self-dual point, so

\[
Y_2'(x_*)=+M'/M^2.
\]

Hence

\[
W(x_*)=rac{2M'}{M^3}.
\]

Since `1-x_*^2=1/2`,

\[
C=x_*(1-x_*^2)W(x_*)
=
\frac{x_*M'}{M^3}.
\]

The previously proved #1161 self-dual response identity gives

\[
A_\infty=2x_*\frac{M'}M.
\]

Therefore

\[
C
=
\frac{A_\infty}{2M^2}.
\]

But

\[
\Pi_*=\frac{4M^2}{A_\infty},
\]

so

\[
\boxed{C=2/\Pi_*}.
\]

## 9. Internal completion equality

The same Wronskian constant has now been evaluated independently:

\[
C=2/\tau
\]

from the #1159 Wallis endpoint normalization, and

\[
C=2/\Pi_*
\]

from the #1161 self-dual AGM response.

Therefore

\[
\boxed{\Pi_*=\tau}.
\]

Equivalently, the previously open normalization identities are now proved:

\[
\boxed{A_\infty\tau=4M^2=H_\infty^2,}
\]

and

\[
\boxed{
\tau\sum_{n\ge0}2^n b_n(a_n-b_n)=M^2.
}
\]

## 10. What has and has not been closed

Closed at analytic power-series/result strength:

`AGM_ENDOGENOUS_COMPLETION Pi_* = INTERNAL_ROTATION_COMPLETION tau`.

This closure uses only:

- finite AGM recursion and its self-dual response identity;
- a rational-coefficient power series and its coefficient ODE;
- a quadratic transformation proved from that ODE/analytic coefficient uniqueness;
- the independently derived #1159 finite Wallis limit normalization.

Not used as premises:

- elliptic integral representations;
- classical circumference;
- the numerical or geometric value of pi;
- the classical Legendre relation.

Still not closed at N0/native strength:

- canonical Cell-to-orientation quotient;
- exact-scalar iterated positive-root closure from current Cell/path primitives;
- promotion of the power-series completion to native ontology.

The classical statement `Pi_*=pi` follows only after a separate accepted identification/name `tau=classical pi` from the #1159 completion layer.

## 11. Prior-art calibration

Hypergeometric quadratic transformations and classical AGM theory are established mathematics. DLMF §15.8 catalogs quadratic transformations of the Gauss hypergeometric function, and DLMF §19.8 records classical AGM quadratic transformations. No historical novelty is claimed for those ingredients.

The task-specific result here is the typed reconstruction and normalization route

`#1159 finite Wallis rotation constant tau -> power-series endpoint response -> complementary Wronskian -> #1161 self-dual AGM response -> Pi_*=tau`,

with elliptic integrals deliberately absent from the premises.
