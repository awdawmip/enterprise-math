# Enterprise Math — BRC Exact Newton Recursion Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION CANDIDATE / MAIN-BACKED RESEARCH / EXACT SCALE+SELECTED-ROOT COEFFICIENTS`
Effective: `2026-09-04`
Parent: `ENTERPRISE_BRC_REDUCIBLE_CRITICAL_JET_FOUNDATION_20260903.md`
Evidence: PR #1186, PR #1188

## 1. Scope and prior art

This addendum transports the main-backed continuation of `WBRC-T51` beyond the first Newton edge.

Newton polygons, Puiseux expansions, valuations and algebraic-number arithmetic are classical mathematics. No generic novelty claim is made. The Enterprise/BRC content is the typed exact carrier needed by the finite positive-rational characteristic jet:

- Newton scales live in a finite rational-prime-valuation group;
- rational translated roots preserve rational polynomial coefficients;
- an irrational **base** selected root does not yet require a full algebraic-number field: coefficients may be stored as rational polynomials evaluated at that exact selected root;
- an irrational **translated** root remains a separate multi-generator algebraic frontier.

## 2. WBRC-T52 — rational-root Newton recursion closure

Define the scale carrier

\[
\boxed{\mathcal S_{\rm rad}=\mathbb Q_{>0}^{\times}\otimes_{\mathbb Z}\mathbb Q.}
\]

Represent a scale by finite rational prime valuations

\[
s=\prod_p p^{\alpha_p},\qquad \alpha_p\in\mathbb Q.
\]

Multiplication adds valuations and integer roots divide valuations. To compare two scales, choose a common denominator `N` for the valuation exponents of their quotient and compare the ordinary positive rationals `s^N` and `t^N`.

Let a finite Newton jet be

\[
J_s(x)=\sum_\sigma \sigma^sP_\sigma(x),
\qquad P_\sigma\in\mathbb Q[x].
\]

If the scale-one polynomial has a selected rational root `x0` of multiplicity `r>=2`, and

\[
q_\sigma=\operatorname{ord}_{x_0}P_\sigma<r,
\]

the candidate scale is

\[
\theta_\sigma=\sigma^{1/(r-q_\sigma)}.
\]

For maximal `theta`, substitute `x=x0+theta^s y` and divide by `theta^(rs)`. The residual jet again has finite support in `S_rad` and coefficients in `Q[y]`:

\[
\boxed{
\widetilde J_s(y)=
\sum_{\sigma,k}
(\sigma\theta^{k-r})^s
\frac{P_\sigma^{(k)}(x_0)}{k!}y^k.
}
\]

Therefore any finite chain of **rational selected translated roots** stays in the same exact carrier. No termination theorem is asserted.

The recursive two-step construction agrees exactly with one-shot substitution. Main-backed PR #1186 verified 66 targeted second-edge BRC families, including 34 with genuinely non-rational radical scales, plus a three-step family. The old coarse 2/3-state catalog contained zero natural second-edge samples; this is preserved as an occurrence boundary, not hidden.

Canonical ID: `WBRC-T52`.

## 3. WBRC-T53 — selected-root evaluation algebra

Let `alpha` be an exact real root selected by the existing integer/rational polynomial + rational isolating interval state. A coefficient is represented by

\[
\boxed{[g]_\alpha:=g(\alpha),\qquad g\in\mathbb Q[x].}
\]

Representatives may be reduced modulo a known polynomial vanishing at `alpha`, but this representation need not be injective when that polynomial is reducible. Equality is semantic:

\[
[g]_\alpha=[h]_\alpha
\iff
(g-h)(\alpha)=0.
\]

The existing selected-root gcd/Sturm machinery decides zero/equality exactly. For a nonzero `g(alpha)`, sign is decided by refining the isolating interval until `g` has no root inside and evaluating at a rational midpoint.

Addition, multiplication and rational scalar multiplication are exact and require no factorization or field inversion.

For a Newton-variable polynomial

\[
E(y)=\sum_j[g_j]_\alpha y^j,
\]

and rational `y0`, evaluation and repeated differentiation in `y` remain selected-root evaluation coefficients, so exact contact order at `y0` is decidable.

Hence a finite characteristic jet with algebraic base selected root `alpha` may be Newton-expanded exactly; if subsequent translated selected roots remain rational, recursion continues with:

- scale support in `S_rad`;
- coefficients in the selected-root evaluation algebra;
- exact zero/sign/contact tests;
- no floating evaluation of `alpha`.

### Semantic-zero-first law

A polynomial representative may be nonzero in `Q[x]` while satisfying `g(alpha)=0`. Therefore:

\[
\boxed{
\text{SELECTED-ROOT SEMANTIC ZERO TEST MUST PRECEDE NEWTON SCALE ORDERING.}
}
\]

Main-backed PR #1188 caught this boundary in its first implementation and then verified the corrected rule.

### Systematic irrational-base realization

For irreducible integer `2x2` matrix `B` with irrational Perron root, let

\[
K=\operatorname{diag}(B,B),\qquad C=B^2.
\]

The selected root `alpha=1/rho(B)` is irrational and double. A common `eta^s C` perturbation in both blocks gives rational double first-edge root `-1`; a smaller off-diagonal `tau^s C` perturbation with `eta^2<tau<eta` gives a second rational selected edge root `-1`.

PR #1188 verified 22 irrational-base block families, 2,854 recursive/direct semantic coefficient checks, and 22 three-edge irrational-base families.

Canonical ID: `WBRC-T53`.

## 4. Exact decision tree after T51

Freeze:

```text
FIRST_NEWTON_EDGE_SELECTED_ROOT_RATIONAL
    -> WBRC-T52

BASE_SELECTED_ROOT_ALGEBRAIC + LATER_TRANSLATED_ROOTS_RATIONAL
    -> WBRC-T53

TRANSLATED_SELECTED_ROOT_IRRATIONAL
    -> MULTI_GENERATOR_ALGEBRAIC_COEFFICIENT_FRONTIER
```

`T53` does not claim that an arbitrary irrational translated root can be absorbed into the same single-root coefficient algebra.

## 5. Hard negative/scope boundaries

```text
RATIONAL_VALUATION_SCALE != FLOATING_RADICAL
OLD_COARSE_CATALOG_ZERO_SECOND_EDGE != NONEXISTENCE_THEOREM
SELECTED_ROOT_POLYNOMIAL_REPRESENTATIVE_NONZERO != VALUE_AT_ROOT_NONZERO
Q[x]/(p) REPRESENTATIVE != MINIMAL_ALGEBRAIC_FIELD
SELECTED_ROOT_EVALUATION_ALGEBRA != GENERAL_INVERSION_FIELD
IRRATIONAL_TRANSLATED_ROOT != SUPPORTED_SINGLE_ROOT_RECURSION
RATIONAL_ROOT_RECURSION != COMPLETE_PUISEUX_SERIES
FINITE_POSITIVE_RATIONAL_SCOPE_ONLY
```

Canonical negative IDs: `WBRC-N36..N41`.

## 6. Tool routing

No new top-level tool family is created. The companion T0 subtool is

`T0_BRC / t0.weighted_brc_newton_recursion`.

Production code provides:

- finite rational-valuation scale arithmetic and exact comparison;
- rational-coefficient Newton jets and rational-root Newton steps;
- selected-root evaluation coefficients with exact semantic zero/equality/sign tests;
- algebraic-base first Newton step and rational translated-root continuation.

No general algebraic factorization, inversion field, floating radical or complete Puiseux engine is included.
