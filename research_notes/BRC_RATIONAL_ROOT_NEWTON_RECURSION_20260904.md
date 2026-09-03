# BRC rational-root Newton recursion over prime-valuation scales

Status: `RESEARCH / CANDIDATE / FINITE CHARACTERISTIC JET`
Date: 2026-09-04
Parent Foundation: `WBRC-T49..T51`

## 1. Scope

This note continues the multiple-root frontier left by `WBRC-T51` without introducing a general algebraic-number field or complete Newton-Puiseux solver.

Newton polygons, Puiseux series, transseries and valuation methods are classical mathematics. No generic novelty claim is made. The Enterprise/BRC contribution studied here is the exact typed closure of the already finite positive-rational characteristic jet under repeated Newton rescaling **as long as every selected translated edge root remains rational**.

## 2. Exact scale group

Let

\[
\mathcal S_{\rm rad}=\mathbb Q_{>0}^{\times}\otimes_{\mathbb Z}\mathbb Q.
\]

Represent an element by finitely many rational prime valuations

\[
s=\prod_p p^{\alpha_p},\qquad \alpha_p\in\mathbb Q.
\]

This representation is exact and finite.

Operations are coordinatewise:

\[
v_p(st)=v_p(s)+v_p(t),
\qquad
v_p(s^{1/d})=\frac1d v_p(s).
\]

Comparison is root-free.  For `s,t` choose the least common multiple `N` of all valuation denominators in `s/t`; then

\[
s<t\iff s^N<t^N,
\]

and `s^N,t^N` are ordinary positive rationals.

Thus all Newton candidate scales created by repeated integer roots of positive-rational characteristic bases can be stored and ordered without evaluating radicals.

## 3. Rational Newton jets

A finite rational Newton jet is a finite map

\[
\mathcal J=\{\sigma\mapsto P_\sigma(x)\},
\qquad
\sigma\in\mathcal S_{\rm rad},\ P_\sigma\in\mathbb Q[x],
\]

with top scale `1`.

Formally for integer asymptotic index `s`,

\[
J_s(x)=\sum_\sigma \sigma^sP_\sigma(x).
\]

This is a typed scale expansion; intermediate radical scales need not be materialized numerically.

The characteristic jet produced by `WBRC-T50/T51` is the initial case, where every strict scale is rational.

## 4. One exact recursive Newton step

Assume the scale-one polynomial `P_1(x)` has a selected rational root `x_0` of multiplicity `r>=2`.

For every strict layer `sigma<1`, let

\[
q_\sigma=\operatorname{ord}_{x_0}P_\sigma.
\]

Only layers with `q_sigma<r` participate in the next Newton edge.  Their candidate scales are

\[
\theta_\sigma=\sigma^{1/(r-q_\sigma)}\in\mathcal S_{\rm rad}.
\]

Let

\[
\theta=\max_\sigma\theta_\sigma.
\]

Substitute

\[
x=x_0+\theta^s y
\]

and divide by the leading factor `theta^(rs)`.

Taylor expansion gives the exact finite residual jet

\[
\widetilde J_s(y)
=
\sum_{\sigma,k}
\left(\sigma\theta^{k-r}\right)^s
\frac{P_\sigma^{(k)}(x_0)}{k!}y^k.
\]

By construction every new scale satisfies

\[
\sigma\theta^{k-r}\le1,
\]

and equality occurs exactly on the first Newton edge.

Therefore the new jet again has:

- finite support in `S_rad`;
- rational polynomial coefficients;
- a scale-one edge polynomial.

This proves **rational-root closure of one Newton step**.

## 5. Iterated rational-root closure

If the selected root of the new scale-one edge polynomial is again rational and multiple, the same construction may be repeated.

Hence any finite chain of rational selected Newton roots stays entirely inside

\[
\boxed{\text{finite }\mathbb Q[x]\text{-coefficient jets over }\mathcal S_{\rm rad}.}
\]

No general termination claim is made.  If a selected edge root is irrational, translating by it generally moves coefficients into an algebraic extension; that is a separate frontier.

## 6. Direct-versus-recursive second-edge identity

Suppose the original characteristic jet is

\[
P_s(z)=\sum_\eta \eta^sG_\eta(z),
\]

with rational selected root `z_0` of multiplicity `r_1`.

Let the first scale be `theta_1`, first edge selected rational root `y_0`, and first-edge root multiplicity `r_2`.

The recursive two-step construction equals the direct substitution

\[
z=z_0+\theta_1^s\bigl(y_0+\theta_2^s x\bigr)
\]

followed by division by

\[
\theta_1^{r_1s}\theta_2^{r_2s}.
\]

For an original Taylor monomial of order `k` and the subsequent binomial order `j`, the direct residual scale is

\[
\boxed{
\eta\,\theta_1^{k-r_1}\theta_2^{j-r_2}.
}
\]

The coefficient is

\[
\frac{G_\eta^{(k)}(z_0)}{k!}
\binom{k}{j}y_0^{k-j}.
\]

Grouping equal prime-valuation scales yields exactly the recursively produced second residual jet.

## 7. BRC-realizable two-step witness

Consider the positive-rational two-state moment family

\[
A_s=
\begin{pmatrix}
1+a^s & b^s\\
c^s & 1+a^s
\end{pmatrix},
\qquad
1>a>\sqrt{bc}>a^2>0.
\]

The limiting critical matrix is

\[
K=I_2,
\]

so `z_0=1` is a double selected root.

The first Newton scale is

\[
\theta_1=a,
\]

and the first edge polynomial is

\[
E_1(y)=(y+1)^2.
\]

Thus the selected first-edge root is the rational double root

\[
y_0=-1.
\]

The second Newton scale is

\[
\boxed{
\theta_2=\frac{\sqrt{bc}}a.
}
\]

It may be irrational even though all original branch weights are rational.  Its prime valuations are nevertheless rational and finite.

For example

\[
a=\frac12,\quad b=\frac13,\quad c=\frac15
\]

give

\[
\theta_2=\frac2{\sqrt{15}},
\]

encoded exactly by

\[
v_2=1,\quad v_3=v_5=-\frac12.
\]

The second edge polynomial is

\[
E_2(x)=x^2-1,
\]

and the Perron branch selects `x=-1`.

## 8. Repeated rational-root witness

With two common diagonal layers,

\[
A_s=(1+a^s+b^s)I_2+
\begin{pmatrix}0&c^s\\d^s&0\end{pmatrix},
\]

choose rational weights so that

\[
a>b>\sqrt{cd}>\max(a^2,\ldots).
\]

Then the first edge and second edge may both be translated by the rational double root `-1`; the third scale is determined by the radical ratio associated with `cd`.

This supplies an explicit BRC family on which the rational-root recursion advances beyond the first Newton edge.

## 9. Hard boundaries

Freeze:

```text
NEWTON_SCALE_CARRIER = FINITE_PRIME_VALUATIONS_WITH_RATIONAL_EXPONENTS
RATIONAL_SELECTED_ROOT -> COEFFICIENT_FIELD_REMAINS_Q
IRRATIONAL_SELECTED_ROOT -> ALGEBRAIC_COEFFICIENT_FIELD_REQUIRED
RATIONAL_ROOT_RECURSION != COMPLETE_PUISEUX_SERIES
SCALE_EXACTNESS != FLOATING_RADICAL_MATERIALIZATION
FIRST_NEWTON_EDGE_T51 != FULL_NEWTON_RECURSION
```

The next algebraic frontier is not scale comparison.  It is exact arithmetic in the coefficient field after an irrational selected edge root.
