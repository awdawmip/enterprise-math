# BRC Sturm-signature root-rank selector state

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T59/T60/T61 and low-degree non-split selector research

## 1. Goal

The low-degree selector program now has two kinds of results:

1. **closed chamber formulas** for split-affine roots and low-degree non-split cofactors;
2. exact Sturm machinery already used as an independent root-count oracle.

The next reusable layer is to expose the Sturm information itself as a typed BRC selector state for arbitrary finite degree.

This is not a new Sturm theorem.  The project value is an exact observer interface that unifies smallest-real and smallest-positive selection without materializing roots.

## 2. Polynomial and squarefree semantics

Let

\[
P(x)\in\mathbb Q[x]
\]

be nonconstant.  Selector ordering depends on the locations of distinct real roots, not on their multiplicities inside the competing cofactor.

Let

\[
\widetilde P=P/\gcd(P,P')
\]

be the squarefree part, and form the ordinary Sturm sequence

\[
S_0=\widetilde P,
\quad
S_1=\widetilde P',
\quad
S_{i+1}=-\operatorname{rem}(S_{i-1},S_i)
\]

until the sequence terminates.

Positive rescaling of sequence members does not affect the selector state below.

## 3. Finite sign signature

For a rational probe `x` with

\[
P(x)\ne0,
\]

define the finite probe sign list by evaluating every Sturm member and deleting zero evaluations:

\[
\operatorname{sgn}_x(S)
=
\bigl(\operatorname{sgn}S_i(x)\bigr)_{S_i(x)\ne0}.
\]

Let

\[
V_x(S)
\]

be the number of sign changes in this list.

At negative infinity no root isolation is needed.  If `d_i=deg S_i` and `ell_i=lc(S_i)`, then

\[
\boxed{
\operatorname{sgn}S_i(-\infty)
=
(-1)^{d_i}\operatorname{sgn}(\ell_i).
}
\]

Hence the negative-infinity variation

\[
V_{-\infty}(S)
\]

is a finite exact function of degrees and leading-coefficient signs.

The **Sturm selector signature** at `x` is therefore finite data:

\[
\boxed{
\Sigma_P(x)
=
\bigl((d_i,\operatorname{sgn}\ell_i,\operatorname{sgn}S_i(x))\bigr)_i.
}
\]

## 4. Root-rank theorem

Define

\[
\nu_P(x)
=
\#\{\alpha\in\mathbb R:\ P(\alpha)=0,\ \alpha<x\},
\]

counting distinct real roots.

For every non-root rational probe `x`, Sturm's theorem gives

\[
\boxed{
\nu_P(x)=V_{-\infty}(S)-V_x(S).
}
\]

Thus `Sigma_P(x)` is a complete exact observer state for the pointwise real-root rank.

No root approximation or algebraic-number materialization is required.

## 5. Smallest-real readout

Let `r` be a declared rational root of the full Newton edge while the competing cofactor `P` satisfies

\[
P(r)\ne0.
\]

Then

\[
\boxed{
\text{declared }r\text{ is smaller than every real competitor}
\iff
\nu_P(r)=0.
}
\]

This subsumes the low-degree smallest-real selector formulas at the pointwise level.

The low-degree formulas remain valuable because they compress the full Sturm signature into fewer discriminant/derivative/order forms and expose explicit parameter chambers.

## 6. Right-rank at zero

For smallest-positive selection, define

\[
\nu_P(0^+)
=
\#\{\alpha\in\mathbb R:P(\alpha)=0,\ \alpha\le0\}.
\]

If

\[
P(0)\ne0,
\]

then

\[
\nu_P(0^+)=\nu_P(0).
\]

If zero is a root, write

\[
P(x)=x^kQ(x),
\qquad
k\ge1,
\qquad
Q(0)\ne0.
\]

Distinct-root semantics imply

\[
\boxed{
\nu_P(0^+)=\nu_Q(0)+1.
}
\]

The multiplicity `k` of the zero root does not change the selector count.

## 7. Smallest-positive readout

Let

\[
r>0,
\qquad
P(r)\ne0.
\]

Then the declared positive root `r` is smaller than every positive competitor iff there is no competing real root in `(0,r)`.

Equivalently,

\[
\boxed{
\text{smallest-positive safe}
\iff
\nu_P(r)=\nu_P(0^+).
}
\]

This formula is degree-independent.

## 8. Observer interpretation

The full polynomial contains much more information than a pointwise selector needs.

For the observer

\[
P\mapsto\nu_P(x),
\]

the exact semantic state may be compressed to the finite Sturm sign/degree signature `Sigma_P(x)`, and even further to the integer rank once no additional probe is required.

This is another observer-relative safe quotient in the sense of the T56-T58 program:

- one probe -> one rank integer is enough;
- many future interval/probe queries require more of the Sturm state;
- recovering explicit root values or polynomial provenance requires stronger state.

No absolute minimality beyond the declared observer is claimed.

## 9. Independent factorized validation family

To avoid merely re-calling the same root-count routine, validation uses products of mutually root-disjoint factors whose rank contributions are known independently.

Use distinct factors from a library containing:

- rational linear factors `(x-r)`;
- positive-discriminant irreducible-over-Q quadratics with two irrational real roots;
- negative-discriminant quadratics with no real roots.

For a rational probe `x` that is not a root of the product:

- each linear factor contributes `1` iff its rational root is `<x`;
- a real quadratic factor contributes rank `0/1/2` from its exact sign/derivative position;
- a complex quadratic contributes `0`.

Because the factor root sets are disjoint, the product rank is the sum of factor ranks.

This gives an independent exact comparator for degrees up to six without numerical root solving.

Repeated-factor regressions separately verify that squarefree Sturm semantics count a repeated competing root only once.

## 10. Higher-degree witness

A useful non-split degree-five example is

\[
P(x)=(x^2+1)(x^2-x-1)(x-2).
\]

It has exactly three real roots:

- the two irrational roots of `x^2-x-1`;
- the rational root `2`.

At `r=1`, exactly one real root lies below `1`, and exactly one lies at or below zero, so

\[
\nu_P(1)=\nu_P(0^+)=1.
\]

Hence `r=1` is safe for a smallest-positive observer even though the cofactor has degree five and contains irrational real roots.

## 11. Parametric boundary

This theorem is **pointwise exact**.

If polynomial coefficients depend on parameters, a full selector chamber requires controlling:

- degree drops in the Sturm/subresultant chain;
- signs of leading coefficients;
- signs of probe evaluations;
- zero-resultant/discriminant boundaries.

A supplied fixed-degree subresultant/Sturm template can turn those into semi-algebraic sign cells, but this note does not claim an automatic CAD or symbolic chamber decomposition engine.

## 12. Hard boundaries

- POINTWISE_STURM_SIGNATURE != PARAMETRIC_CAD.
- DISTINCT_ROOT_RANK does not retain root multiplicity of the competing cofactor.
- ROOT_RANK != EXPLICIT_ROOT_VALUES.
- ONE_PROBE_RANK is not sufficient for arbitrary future probe queries.
- ZERO_ROOT contributes one to `nu(0+)` regardless of multiplicity.
- No complete Puiseux solver, generic multi-generator algebraic field, signed branch interference, or infinite-state claim is made.
