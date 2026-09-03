# BRC selected-root evaluation algebra for algebraic-base Newton recursion

Status: `RESEARCH / CANDIDATE / EXACT SELECTED-ROOT COEFFICIENT CARRIER`
Date: 2026-09-04
Parents: `WBRC-T51`, PR #1186 rational-root Newton recursion

## 1. Purpose and prior-art boundary

This note continues the BRC Newton hierarchy after the selected critical root itself becomes irrational algebraic.

Algebraic-number arithmetic, quotient algebras, real-root isolation and Newton-Puiseux theory are classical. No generic novelty claim is made. The Enterprise/BRC question is narrower:

> How little new exact state is needed to continue a finite characteristic Newton jet when the base selected root is algebraic, but the next translated Newton root is rational?

A full algebraic-number field is unnecessary for this step.

## 2. Selected-root evaluation state

Let

\[
p(x)\in\mathbb Q[x]
\]

and let `alpha` be a particular real root selected exactly by a rational isolating interval and the existing Sturm selector.

A coefficient is represented by a rational polynomial

\[
g(x)\in\mathbb Q[x]
\]

with semantics

\[
\boxed{[g]_{\alpha}:=g(\alpha).}
\]

For bounded storage, `g` may be reduced modulo `p`; this preserves evaluation because `p(alpha)=0`.  The representation need not be injective when `p` is reducible.  Equality is semantic:

\[
[g]_\alpha=[h]_\alpha
\iff
(g-h)(\alpha)=0,
\]

and is decided by the existing selected-root gcd/Sturm test rather than by polynomial-remainder equality.

Thus this is deliberately a **selected-root evaluation algebra**, not a claim that `Q[x]/(p)` is the minimal field of `alpha`.

## 3. Exact operations needed by Newton recursion

The following are exact without factoring `p`:

\[
[g]_{\alpha}+[h]_{\alpha}=[g+h]_{\alpha},
\]

\[
[g]_{\alpha}[h]_{\alpha}=[gh]_{\alpha},
\]

and rational scalar multiplication.

Zero testing uses

\[
[g]_{\alpha}=0
\]

iff the selected root belongs to the common zero set of `p` and `g`; the existing selector/gcd/Sturm machinery decides this exactly.

For a nonzero coefficient, its sign is exact: refine the isolating interval of `alpha` until `g` has no zero in the interval, then evaluate at any rational midpoint.

No division is required merely to form Taylor coefficients, contact orders, Newton edge polynomials or rational translations.

## 4. Polynomials in a Newton variable

Let

\[
E(y)=\sum_j [g_j]_{\alpha}y^j.
\]

For rational `y0`,

\[
E(y_0)=\left[\sum_j g_j(x)y_0^j\right]_{\alpha}
\]

is again a selected-root evaluation coefficient.

Therefore exact vanishing order at a rational translated root is computable by repeated differentiation in `y` and selected-root zero tests.

This is precisely what later Newton edges need as long as each translated selected root remains rational.

## 5. Algebraic-base Newton closure with rational translated roots

Let the characteristic jet be

\[
J_s(z)=\sum_{\sigma}\sigma^sG_\sigma(z),
\qquad G_\sigma\in\mathbb Q[z],
\]

with scales in the rational-valuation carrier

\[
\mathcal S_{\rm rad}=\mathbb Q_{>0}^{\times}\otimes_{\mathbb Z}\mathbb Q.
\]

Suppose the scale-one polynomial has selected algebraic root `alpha` of multiplicity `r>=2`.

For every layer, the Taylor coefficient

\[
\frac{G_\sigma^{(k)}(\alpha)}{k!}
\]

is stored exactly as the selected-root coefficient

\[
\left[\frac{G_\sigma^{(k)}(x)}{k!}\right]_{\alpha}.
\]

The contact order `q_sigma` is determined by exact selected-root zero tests. Candidate scales and the first Newton scale are computed exactly in `S_rad`, exactly as in `WBRC-T51`.

After substitution

\[
z=\alpha+\theta^s y,
\]

the residual jet has finite `S_rad` support and polynomial coefficients in the selected-root evaluation algebra.

If the chosen edge root `y0` is rational, translating

\[
y=y_0+\vartheta^s u
\]

again uses only addition/multiplication by rational numbers and selected-root zero tests. Therefore:

\[
\boxed{
\text{algebraic base selected root + rational later selected roots}
\Rightarrow
\text{exact finite Newton recursion without a general algebraic field.}
}
\]

## 6. Systematic 4-state BRC realization

Let

\[
B\in M_2(\mathbb N_0)
\]

be irreducible with irrational Perron root `rho`, and put

\[
K=\operatorname{diag}(B,B).
\]

The selected critical root

\[
\alpha=\rho^{-1}
\]

is irrational and has multiplicity two in

\[
p_K(z)=\det(I-zB)^2.
\]

Let

\[
C=B^2.
\]

Since the Perron eigenvalue of `C` is `rho^2`, a perturbation `B+epsilon C` has Perron eigenvalue

\[
\rho+\epsilon\rho^2.
\]

Therefore its reciprocal root has derivative exactly `-1` at `epsilon=0`, independent of the algebraic value of `rho`.

### First rational double edge root

Use the 4-state finite exponential matrix jet

\[
A_s=
\begin{pmatrix}
B+\eta^s C&0\\
0&B+\eta^s C
\end{pmatrix},
\qquad 0<\eta<1.
\]

Both critical blocks shift identically, so after scaling around `alpha` by `eta^s`, the first edge polynomial has the selected double root

\[
\boxed{y_0=-1.}
\]

The base selected root is irrational, but the translated edge root is rational.

### Second rational edge root

Add a smaller off-diagonal coupling

\[
\tau^s
\begin{pmatrix}
0&C\\
C&0
\end{pmatrix},
\qquad
\eta^2<\tau<\eta.
\]

In the symmetric Perron sector the eigenvalue is exactly

\[
\rho+\rho^2(\eta^s+\tau^s).
\]

Hence after the first translation `y=-1`, the second Newton scale is

\[
\boxed{\vartheta=\tau/\eta}
\]

and the Perron-selected second edge root is again

\[
\boxed{u_0=-1.}
\]

Thus the exact recursion advances through an irrational base root and at least two rational translated roots.

### Two common shifts before splitting

With common diagonal scales

\[
\eta_1^sC+\eta_2^sC
\]

and off-diagonal `tau^s C`, where

\[
1>\eta_1>\eta_2>\tau>\eta_1^2,
\]

the first two translated selected roots are both the rational double root `-1`; the third edge performs the block splitting.

## 7. Direct-versus-recursive identity

For one algebraic base root `alpha` and rational later roots `y0,u0`, repeated Taylor/binomial substitution can be performed in two ways:

1. recursively in the selected-root evaluation algebra;
2. directly from each original rational polynomial `G_sigma(z)`, keeping every Taylor coefficient as a polynomial in the symbolic root variable `x`, and only at the end evaluating at `alpha` semantically.

The two finite jets must agree coefficientwise **at the selected root**, i.e. every difference polynomial must vanish at `alpha` by the exact gcd/Sturm test.

This avoids any numerical approximation of `alpha`.

## 8. Why this is not a full algebraic-number field

The selected-root evaluation algebra is sufficient for:

- addition and multiplication;
- Taylor coefficients;
- rational translations;
- exact zero/equality tests;
- exact sign tests after interval refinement;
- contact-order Newton recursion.

It does not yet claim general inversion. If an edge-selected root is itself irrational, the next translation introduces a second algebraic generator and the coefficient state generally leaves the single selected-root evaluation algebra.

That is the next boundary.

## 9. Frozen boundaries

```text
SELECTED_ROOT_EVALUATION_COEFFICIENT = POLYNOMIAL_EVALUATED_AT_EXACT_SELECTED_ROOT
REPRESENTATIVE_MOD_P != MINIMAL_FIELD_ELEMENT
ZERO_TEST = GCD_PLUS_SELECTED_ROOT_ISOLATION
SIGN_TEST = ROOT_INTERVAL_REFINEMENT
ALGEBRAIC_BASE_ROOT + RATIONAL_TRANSLATED_ROOTS -> EXACT_RECURSION_SUPPORTED
IRRATIONAL_TRANSLATED_ROOT -> MULTI_GENERATOR_ALGEBRAIC_COEFFICIENT_FRONTIER
NO_GENERAL_INVERSION_CLAIM
NO_GENERIC_ALGEBRAIC_NUMBER_CAS
NO_COMPLETE_PUISEUX_SOLVER
```
