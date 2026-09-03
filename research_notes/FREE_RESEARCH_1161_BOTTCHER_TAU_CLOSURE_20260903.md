# Free Research #1161 — Böttcher phase / Wallis rotation phase closure

Status: `FREE_RESEARCH_RESULT / INTERNAL PHASE BRIDGE PROVED / ANALYTIC POWER-SERIES LAYER / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent issue: `#1161`
Dependencies:
- `FREE_RESEARCH_1161_BOTTCHER_ROTATION_PHASE_20260903.md`
- `FREE_RESEARCH_1161_BOTTCHER_RESPONSE_DERIVATIVE_ADDENDUM_20260903.md`
- `FREE_RESEARCH_1161_POWER_SERIES_WALLIS_NORMALIZATION_CLOSURE_20260903.md`

## 1. Result

For generalized AGM seed `a_0=1`, `b_0=x`, `0<x<1`, let

\[
\Theta_{\rm AGM}(x)
\]

be the normalized Böttcher rotation phase extracted from the AGM shape map, and let `tau` be the independently defined #1159 rotation boundary-completion constant.

Then

\[
\boxed{
\Theta_{\rm AGM}(x)
=
\tau\frac{F(x^2)}{F(1-x^2)}
}
\]

where

\[
F(z)=\sum_{n\ge0}\frac{\binom{2n}{n}^2}{16^n}z^n.
\]

Using the reciprocal-AGM identity proved in the power-series normalization closure,

\[
F(1-x^2)=\frac1{M(1,x)},
\]

this is equivalently

\[
\boxed{
\Theta_{\rm AGM}(x)
=
\tau
\frac{M(1,x)}{M(1,\sqrt{1-x^2})}.
}
\]

At the self-dual Gauss–Legendre seed `x=1/sqrt(2)`, the numerator and denominator AGM values agree, hence

\[
\boxed{\Theta_{\rm AGM}=\tau}.
\]

Together with the separately proved normalization closure `Pi_*=tau`, one obtains

\[
\boxed{\Pi_*=\Theta_{\rm AGM}=\tau}.
\]

No elliptic-integral representation or classical pi normalization is used in these equalities.

## 2. Derivative of the power-series ratio

Put

\[
Y_1(x)=F(1-x^2),
\qquad
Y_2(x)=F(x^2),
\]

and

\[
R(x)=Y_2(x)/Y_1(x).
\]

The power-series/Wallis normalization result proved that their Wronskian is

\[
W=Y_1Y_2'-Y_2Y_1'
=
\frac{2/\tau}{x(1-x^2)}.
\]

Therefore

\[
R'(x)
=
\frac{W}{Y_1^2}
=
\boxed{
\frac{2}{\tau x(1-x^2)F(1-x^2)^2}
}.
\]

## 3. Compare with the exact Böttcher response

The finite Böttcher/Wronskian result independently proved

\[
\Theta_{\rm AGM}'(x)
=
\frac{2M(1,x)^2}{x(1-x^2)}.
\]

Since

\[
M(1,x)=1/F(1-x^2),
\]

we have

\[
\boxed{
\Theta_{\rm AGM}'(x)
=
\frac{2}{x(1-x^2)F(1-x^2)^2}
=
\tau R'(x).
}
\]

Hence

\[
\Theta_{\rm AGM}(x)-\tau R(x)
\]

is constant on `(0,1)`.

## 4. Determine the integration constant without a classical period

### 4.1 `R(x) -> 0` as `x -> 0+`

The Wallis coefficient normalization proves

\[
F(z)\sim\frac1\tau\ln\frac1{1-z}
\]

as `z->1-`. Therefore

\[
F(1-x^2)\to\infty,
\qquad
F(x^2)\to1,
\]

and

\[
\boxed{R(x)\to0}.
\]

### 4.2 `Theta_AGM(x) -> 0` as `x -> 0+`

The exact derivative formula is positive, so `Theta_AGM(x)` is increasing in `x`. Hence its limit

\[
L:=\lim_{x\to0+}\Theta_{\rm AGM}(x)
\]

exists and is finite, with `L>=0`.

The normalized AGM ratio map is

\[
T(x)=\frac{2\sqrt{x}}{1+x}.
\]

The Böttcher phase shift law is exactly

\[
\boxed{
\Theta_{\rm AGM}(T(x))=2\Theta_{\rm AGM}(x).
}
\]

Since `T(x)->0` when `x->0`, taking limits gives

\[
L=2L.
\]

Thus

\[
\boxed{L=0}.
\]

Therefore both terms in the constant difference tend to zero, so the constant itself is zero.

This proves

\[
\boxed{
\Theta_{\rm AGM}(x)
=
\tau R(x)
=
\tau\frac{F(x^2)}{F(1-x^2)}.
}
\]

## 5. Self-dual point

Let

\[
x_*=1/\sqrt2.
\]

Then

\[
1-x_*^2=x_*^2=1/2,
\]

so

\[
F(x_*^2)=F(1-x_*^2).
\]

Hence

\[
\boxed{
\Theta_{\rm AGM}(x_*)=\tau.
}
\]

The independent #1161 power-series/Wallis Wronskian normalization already proved

\[
\Pi_* = \tau.
\]

Consequently

\[
\boxed{
\Pi_* = \Theta_{\rm AGM} = \tau
}
\]

at the standard Gauss–Legendre seed.

## 6. Complement law

The closed formula also gives an exact complementary-phase reciprocity. Put

\[
y=\sqrt{1-x^2}.
\]

Then

\[
\Theta_{\rm AGM}(x)
=
\tau\frac{F(x^2)}{F(y^2)},
\]

while

\[
\Theta_{\rm AGM}(y)
=
\tau\frac{F(y^2)}{F(x^2)}.
\]

Therefore

\[
\boxed{
\Theta_{\rm AGM}(x)\Theta_{\rm AGM}(\sqrt{1-x^2})
=
\tau^2.
}
\]

The self-dual point is the positive fixed point of this complement operation, forcing its phase to be exactly `tau`.

This is stronger and cleaner than the previously open stationarity criterion: the required complement structure has now been explicitly reconstructed at the analytic power-series layer.

## 7. Typing and remaining boundary

Closed:

- `PI_STAR_EQUALS_TAU = PROVED` at analytic power-series/internal-completion strength;
- `THETA_AGM_EQUALS_TAU = PROVED` at the standard self-dual seed;
- `THETA_AGM(x)=tau F(x^2)/F(1-x^2) = PROVED`;
- complementary phase product `=tau^2 = PROVED`.

Still not promoted to N0:

- the power-series function `F` is a derived analytic completion object;
- current Cell/path foundation still lacks an exact scalar iterated-root closure and canonical Cell-to-orientation quotient;
- `tau=classical pi` remains a separate #1159/classical identification layer.

Thus the #1161 local finite mechanism and its internal global normalization are closed, while N0-native promotion remains a distinct research problem.
