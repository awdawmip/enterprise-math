# Free Research #1161 addendum — finite Böttcher-response derivative and self-dual stationarity bridge

Status: `FREE_RESEARCH_ADDENDUM / EXACT FINITE DERIVATIVE IDENTITY / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent: `FREE_RESEARCH_1161_BOTTCHER_ROTATION_PHASE_20260903.md`

## 1. Generalized aspect ratio and finite phase

Let

\[
a_0=1,\qquad b_0=x,\qquad 0<x<1,
\]

and iterate the arithmetic–geometric mean. Define

\[
s_n(x)=\frac{a_n(x)-b_n(x)}{a_n(x)+b_n(x)}.
\]

The finite Böttcher-phase approximant is

\[
\Theta_n(x)=2^{-n}\ln\frac4{s_n(x)}.
\]

## 2. Reuse the finite Wronskian invariant

Set

\[
W_n=a_nb_n'-b_na_n'.
\]

The separate self-dual response result proved the exact finite identity

\[
\boxed{
x(1-x^2)W_n
=2^n a_nb_n(a_n^2-b_n^2).
}
\]

No limiting derivative is needed for this statement.

## 3. Exact finite phase derivative

Differentiate

\[
s_n=\frac{a_n-b_n}{a_n+b_n}.
\]

One obtains

\[
s_n'
=
-\frac{2W_n}{(a_n+b_n)^2}.
\]

Therefore

\[
-\frac{s_n'}{s_n}
=
\frac{2W_n}{a_n^2-b_n^2}.
\]

Since

\[
\Theta_n'=-2^{-n}\frac{s_n'}{s_n},
\]

substitution of the Wronskian invariant gives the complete cancellation

\[
\boxed{
\Theta_n'(x)
=
\frac{2a_n(x)b_n(x)}{x(1-x^2)}.
}
\]

This holds at every finite AGM depth.

## 4. Limiting phase response

On any compact subinterval of `(0,1)`, the AGM convergence is uniform and the finite derivative formula has the pointwise limit

\[
\boxed{
\Theta_{\rm AGM}'(x)
=
\frac{2M(x)^2}{x(1-x^2)},
}
\]

where

\[
M(x)=\operatorname{AGM}(1,x).
\]

Thus the derivative of the Böttcher rotation phase is itself an exact squared-AGM-scale response density.

At the self-dual point

\[
x_*=1/\sqrt2,
\qquad
1-x_*^2=x_*^2=1/2,
\]

this reduces to

\[
\boxed{
\Theta_{\rm AGM}'(x_*)
=\frac{4M(x_*)^2}{x_*}.
}
\]

## 5. First global bridge becomes a local stationarity condition

The separate self-dual defect/response theorem gives

\[
\Pi_*
=\frac{2M(x_*)^3}{x_*M'(x_*)}.
\]

Therefore

\[
\Pi_*=\Theta_{\rm AGM}(x_*)
\]

is equivalent to

\[
\frac{\Theta_{\rm AGM}'(x_*)}{\Theta_{\rm AGM}(x_*)}
=2\frac{M'(x_*)}{M(x_*)}.
\]

Equivalently,

\[
\boxed{
\left.
\frac{d}{dx}
\left(
\frac{\Theta_{\rm AGM}(x)}{M(x)^2}
\right)
\right|_{x=x_*}
=0.
}
\]

So the first open global completion equality has been reduced to a local self-dual stationarity/symmetry statement for the ratio

\[
\Theta_{\rm AGM}/M^2.
\]

## 6. Why this is structurally useful

The standard seed is the fixed point of the positive complementary involution

\[
x\longmapsto\sqrt{1-x^2}.
\]

Therefore a future proof that

\[
\Theta_{\rm AGM}(x)/M(x)^2
\]

is invariant under this complement operation would automatically force the required derivative to vanish at `x=1/sqrt(2)` and hence prove

\[
\Pi_*=\Theta_{\rm AGM}.
\]

Such complement invariance is **not proved here**. It is now a sharply typed bridge target rather than an implicit appeal to the classical elliptic Legendre relation.

If, in addition, the separate bridge `Theta_AGM=tau` to the #1159 rotation-completion phase is established, the full internal completion chain closes.

## 7. Frozen scope

`FINITE_THETA_DERIVATIVE = 2 a_n b_n/[x(1-x^2)] = PROVED`.

`LIMIT_THETA_DERIVATIVE = 2 M(x)^2/[x(1-x^2)] = DERIVED_ON_INTERIOR`.

`PI_STAR_EQUALS_THETA_AGM <=> SELF_DUAL_STATIONARITY_OF_THETA_OVER_M_SQUARED = PROVED_EQUIVALENCE`.

`COMPLEMENT_INVARIANCE_OF_THETA_OVER_M_SQUARED = OPEN`.

`THETA_AGM_EQUALS_TAU = OPEN`.

`CLASSICAL_ELLIPTIC_LEGENDRE_RELATION = NOT_USED_AS_PREMISE`.
