# Free Research #1161 addendum — derivative-limit audit for the power-series normalization closure

Status: `FREE_RESEARCH_ADDENDUM / RIGOR AUDIT CLOSED / NOT WORKING_TRUTH / NOT FOUNDATION`
Date: `2026-09-03`
Researcher: `EM-FREE-G61R8`
Parent: `FREE_RESEARCH_1161_POWER_SERIES_WALLIS_NORMALIZATION_CLOSURE_20260903.md`

## 1. Audit target

The normalization proof uses the self-dual response identity

\[
A_\infty
=4x(1-x^2)\frac{M'(x)}{M(x)}
\]

at `x=1/sqrt(2)`.

The finite algebra gives

\[
J_n=4x(1-x^2)\frac{a_n'}{a_n}
\]

and independently proves

\[
J_n\to A_\infty
\]

at the self-dual seed.

To justify the displayed limiting derivative identity rigorously, it remains to prove

\[
\frac{a_n'}{a_n}\to\frac{M'}M.
\]

Pointwise convergence `a_n->M` alone is not sufficient for that conclusion, so this addendum supplies the missing estimate.

## 2. Exact AGM invariance at finite depth

Let

\[
x_n=b_n/a_n.
\]

Because the AGM common limit is invariant under each arithmetic/geometric step and homogeneous,

\[
\boxed{
M(1,x)=a_n(x)M(1,x_n(x)).
}
\]

This identity is exact at every finite `n`.

The power-series closure has already proved

\[
M(1,y)=\frac1{F(1-y^2)}.
\]

Since `F` is analytic at zero with `F(0)=1`, the logarithmic derivative

\[
L(y):=\frac{\partial_yM(1,y)}{M(1,y)}
\]

is bounded on some interval `[y_0,1]`.

## 3. Exact finite derivative of the normalized ratio

The previously proved finite Wronskian identity is

\[
x(1-x^2)W_n
=2^n a_nb_n(a_n^2-b_n^2),
\]

where

\[
W_n=a_nb_n'-b_na_n'.
\]

Since

\[
x_n'=(b_n/a_n)'=W_n/a_n^2,
\]

we obtain

\[
\boxed{
x_n'
=
\frac{2^n x_n a_n^2(1-x_n^2)}{x(1-x^2)}.
}
\]

## 4. The ratio derivative tends to zero without using `Pi_*=tau`

The normalized cone shape is

\[
s_n=\frac{1-x_n}{1+x_n}.
\]

The earlier purely algebraic shape contraction, proved before the normalization closure, gives a double-exponential bound of the form

\[
s_n\le q^{2^n}
\]

for one fixed `0<q<1` at the standard seed (and analogous compact-subinterval bounds for nearby `x`).

Also

\[
1-x_n^2
=(1-x_n)(1+x_n)
=s_n(1+x_n)^2
\le4s_n.
\]

Therefore

\[
2^n(1-x_n^2)\to0.
\]

The sequences `a_n` and `x_n` are bounded, while the initial denominator `x(1-x^2)` is fixed and positive. Hence the exact formula above yields

\[
\boxed{x_n'\to0.}
\]

This step uses only the already-proved AGM shape contraction, not the later equality `Pi_*=tau`, so there is no circularity.

## 5. Convergence of logarithmic derivatives

Differentiate the exact finite-depth invariance

\[
\log M(1,x)
=
\log a_n(x)+\log M(1,x_n(x)).
\]

Then

\[
\frac{M'(x)}{M(x)}
=
\frac{a_n'}{a_n}
+L(x_n)x_n'.
\]

As `n->infinity`,

\[
x_n\to1,
\]

so `L(x_n)` remains bounded, while

\[
x_n'\to0.
\]

Consequently

\[
\boxed{
\frac{a_n'}{a_n}
\longrightarrow
\frac{M'}M.
}
\]

## 6. Self-dual response identity is now fully justified

At the self-dual seed `x=1/sqrt(2)`, the finite defect/response invariant proves

\[
J_n\to A_\infty.
\]

Together with

\[
J_n=4x(1-x^2)\frac{a_n'}{a_n}
\]

and the derivative convergence just established,

\[
\boxed{
A_\infty
=4x(1-x^2)\frac{M'}M
=2x\frac{M'}M
}
\]

at `x=1/sqrt(2)`.

Therefore the Wronskian evaluation used in the proof of

\[
\Pi_*=\tau
\]

has no unproved derivative-interchange step remaining.

## 7. Scope

`FINITE_TO_LIMIT_LOG_DERIVATIVE_CONVERGENCE = PROVED`.

`SELF_DUAL_A_INFINITY_RESPONSE_FORMULA = RIGOROUSLY CLOSED`.

`PI_STAR_EQUALS_TAU PROOF_DEPENDENCY_GAP = CLOSED`.
