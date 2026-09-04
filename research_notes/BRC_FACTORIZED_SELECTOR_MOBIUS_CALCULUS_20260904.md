# BRC factorized selector certificates and root-support Möbius calculus

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parents: WBRC-T57/T58 observer leases, WBRC-T59 schedule strata, WBRC-T60--T63 selector chambers, main-backed PRs #1217--#1220, PR #1236

## 1. Problem

The current selector line can certify a declared Newton root using several exact factor types:

- explicitly split affine real-root branches;
- one non-split monic quadratic cofactor;
- one non-degenerate cubic cofactor;
- an arbitrary fixed rational polynomial through a Sturm root-rank signature.

A mixed edge polynomial is often naturally supplied in factored form,

\[
P(x)=c\prod_{i=1}^n F_i(x)^{m_i},
\qquad c\ne0,\quad m_i\ge1.
\]

Expanding this product before selector analysis is unnecessary and can be actively harmful: permanent repeated factors make the nominal resultant `Res(P,P')` identically zero.  The factorization should therefore be treated as typed state rather than discarded.

This note extracts the exact compositional laws for three different observers:

1. Boolean interval emptiness / selector safety;
2. distinct-root count;
3. multiplicity-counted root count.

These observers require different quotients and different parameter-event sets.

All polynomial gcd, inclusion-exclusion, resultant and Sturm facts used here are classical prior art.  The BRC result is the explicit observer-typed composition interface and its safe information-loss boundaries.

## 2. Product root support is a Boolean union

For any real interval or subset `I`,

\[
Z_I(P)=Z(P)\cap I
=igcup_{i=1}^n Z(F_i)\cap I.
\]

The scalar `c` and the positive exponents `m_i` do not affect this support identity.

Therefore

\[
\boxed{
P\text{ has no root in }I
\iff
F_i\text{ has no root in }I\quad\forall i.
}
\]

For a declared positive root `r`, take `I=(0,r)`; for a smallest-real selector, take `I=(-\infty,r)`.

If the declared root is represented separately as `(x-r)^m`, fixed declared multiplicity additionally requires

\[
\boxed{F_i(r)\ne0\quad\forall i.}
\]

Thus a mixed split/quadratic/cubic/Sturm certificate is composed by conjunction without expanding the factors.

Define the failing-factor support

\[
\mathcal U_I=(\,i:Z_I(F_i)\ne\varnothing\,).
\]

Then the product is selector-safe exactly when `U_I` is empty.  Keeping `U_I` also identifies which factor supplies a counterexample.

## 3. One-shot quotient versus factor-local contextual signature

For one final Boolean query, the vector of factor safety bits

\[
s=(s_1,\ldots,s_n)\in\{0,1\}^n
\]

may be collapsed to

\[
\boxed{S=\bigwedge_i s_i.}
\]

That one bit is sufficient for the one-shot observer.

It is not contextually sufficient when later operations may replace individual factors.  For each `i`, a context may replace every factor except `i` by a certified safe factor.  The resulting product safety is exactly `s_i`.  Hence all coordinates are observable under factor-local contexts:

\[
\boxed{
\text{arbitrary factor-local replacement lease}
\Longrightarrow
(s_1,\ldots,s_n)\text{ is the minimal Boolean signature.}
}
\]

Equivalently, the failing support `U_I` is the contextual signature.  This is a direct instance of the T6/T57 principle that minimality is relative to the declared future-operation lease.

## 4. Distinct-root count requires all-order intersections

Let

\[
N_I(F)=\#\bigl(Z(F)\cap I\bigr)
\]

count distinct real roots in `I`.

For every nonempty subset `S` of factor indices,

\[
\bigcap_{i\in S}Z(F_i)=Z\!\left(\gcd_{i\in S}F_i\right).
\]

Finite inclusion-exclusion therefore gives the exact root-support Möbius formula

\[
\boxed{
N_I(P)
=
\sum_{\varnothing\ne S\subseteq[n]}
(-1)^{|S|+1}
N_I\!\left(\gcd_{i\in S}F_i\right).
}
\]

The positive exponents `m_i` again disappear because this observer counts support, not multiplicity.

### Pairwise-coprime collapse

If every pair of factors is coprime over `Q[x]`, equivalently every pairwise resultant is nonzero, then their complex root sets are disjoint and

\[
\boxed{N_I(P)=\sum_iN_I(F_i).}
\]

Without that guard, single-factor counts are generally insufficient.

### Genuine third-order witness

Take

\[
F_1=x(x-1),\quad
F_2=x(x-2),\quad
F_3=x(x-3)
\]

on `I=(-1,4)`.

Then

\[
\sum_iN_I(F_i)=6,
\]

all three pairwise gcds equal `x`, so the pairwise correction is `3`, while the triple gcd is also `x`, contributing `1` back.  The product has roots

\[
\{0,1,2,3\}
\]

and hence

\[
\boxed{6-3+1=4.}
\]

Stopping at pairwise corrections gives `3`, so a full distinct-root observer can have genuine higher-order intersection data.

## 5. Multiplicity-counted roots remain additive

Let

\[
M_I(F)
\]

count real roots in `I` with algebraic multiplicity.  Then product multiplicities add at every root, including shared roots, and therefore

\[
\boxed{
M_I(P)=\sum_{i=1}^n m_iM_I(F_i).
}
\]

No coprimality or cross-resultant condition is required.

This sharply separates the observers:

- Boolean emptiness is conjunction;
- multiplicity count is a weighted sum;
- distinct count is a union size and requires gcd-Möbius corrections when factors overlap.

## 6. Factorized parameter-event hierarchy

Let each factor vary polynomially with one rational parameter `t`:

\[
F_i=F_i(t,x).
\]

For an open interval `(u,v)`, define a per-factor event polynomial

\[
E_i^{\rm bool}(t)
=
\operatorname{Res}_x(F_i,\partial_xF_i)
F_i(t,u)F_i(t,v).
\]

The nominal resultant also records degree drops.  On a connected parameter interval where every `E_i^{bool}` is nonzero, each factor's interval-emptiness state is constant.  Consequently

\[
\boxed{
E_{\rm bool}(t)=\prod_iE_i^{\rm bool}(t)
}
\]

is sufficient for constancy of product selector safety.

Cross-factor resultants are not needed for that Boolean observer: a collision between roots of two already-unsafe factors cannot create or destroy the statement that the union is empty.

For the exact distinct-root count, collisions matter.  A sufficient event polynomial is

\[
\boxed{
E_{\rm dist}(t)
=
E_{\rm bool}(t)
\prod_{i<j}\operatorname{Res}_x(F_i,F_j).
}
\]

Away from its zero set, all factors are internally squarefree, endpoint-free and pairwise root-disjoint; distinct counts therefore add and remain constant.

The classical product identity explains the extra factors.  Up to a nonzero convention-dependent scalar/sign,

\[
\operatorname{Res}_x\!\left(\prod_iF_i,
\partial_x\prod_iF_i\right)
=
\prod_i\operatorname{Res}_x(F_i,F_i')
\prod_{i<j}\operatorname{Res}_x(F_i,F_j)^2.
\]

Thus the expanded-product discriminant carries cross-collision events even when the Boolean selector does not need them.

## 7. Collision observer witness

Set

\[
F_1(t,x)=x-(2+t),
\qquad
F_2(t,x)=x-(2-t),
\]

and observe the open interval `(0,4)`.

The per-factor endpoint events occur only at `t=\pm2`; hence `E_bool` is nonzero at `t=0`.

But

\[
\operatorname{Res}_x(F_1,F_2)=2t.
\]

At `t=0`, the two factor roots collide at `x=2`:

- Boolean selector safety is unsafe on both sides and at the collision;
- multiplicity-counted root count remains `2`;
- distinct-root count changes from `2` to `1` at the event point.

Therefore the cross resultant is:

\[
\boxed{
\text{irrelevant to Boolean emptiness,}
\quad
\text{irrelevant to multiplicity count,}
\quad
\text{necessary for exact distinct support.}
}
\]

This is an observer-typed event boundary, not a contradiction between event polynomials.

## 8. Permanent multiplicity must stay typed

If the expanded family contains a permanent repeated factor,

\[
P(t,x)=F(t,x)^2G(t,x),
\]

then

\[
\operatorname{Res}_x(P,P')\equiv0.
\]

The generic expanded resultant is therefore useless as an event polynomial even though the moving support of `F` and `G` may be perfectly regular.

The repair is not to perturb away the multiplicity.  It is to retain the factorized state

\[
\bigl((F,2),(G,1)\bigr)
\]

and build support/selector events from the primitive factor carriers while keeping exponents as separate multiplicity data.

This is exactly the general BRC discipline:

\[
\boxed{
\text{do not discard declared type and then try to reconstruct it from an aggregated carrier.}
}
\]

## 9. Exact regression

The dedicated checker verifies:

- `1,275` factorized interval samples;
- `2,550` Boolean selector conjunction checks;
- `1,275` exact gcd-Möbius reconstructions using `12,975` subset terms;
- `750` pairwise-coprime additive samples;
- `525` non-coprime samples, including `325` actual failures of naïve distinct-count additivity;
- `840` multiplicity-additivity samples, including `456` shared-root cases;
- the explicit `6-3+1=4` third-order intersection witness;
- the one-shot-AND versus factor-local contextual-minimality distinction on all `2^5` safety vectors;
- the two-factor collision event, the three-factor resultant product identity and the permanent-repetition resultant failure.

All checks use exact integers/Fractions, polynomial gcds, Sturm counts and Sylvester resultants.  No floating root approximation is used.

## 10. Relationship to earlier selector work

PR #1217 already used products of mutually root-disjoint factors as an independent regression source for arbitrary-degree Sturm ranks.  The present result extracts what that test did not state:

- the exact product safety conjunction without a disjointness assumption;
- the all-order subset-gcd Möbius formula when root supports overlap;
- the multiplicity-count observer that remains additive through collisions;
- the different parameter-event polynomials required by Boolean, distinct-support and multiplicity observers;
- the contextual minimality of the full factor safety vector under factor-local replacement.

PR #1236's four-chamber quadratic interval theorem becomes one factor-level certificate inside this composition calculus rather than a competing global method.

## 11. Hard boundaries

- FACTORIZED CERTIFICATE requires a supplied verified factorization; no factorization algorithm is claimed.
- SELECTOR SAFETY CONJUNCTION does not recover distinct-root counts.
- DISTINCT ROOT COUNT is not additive without root-disjointness or Möbius corrections.
- PAIRWISE CORRECTIONS are not always complete; higher-order gcd intersections may contribute.
- MULTIPLICITY COUNT is not the same observer as distinct support.
- CROSS RESULTANTS are observer-dependent events, not universally mandatory.
- EXPANDED RESULTANT may vanish identically under permanent multiplicity.
- FACTOR LABEL PROVENANCE is lost if only the final safety bit is retained.
- This is finite rational-polynomial exact algebra, not a generic factorization engine, multi-parameter CAD, complete Puiseux solver, signed branch-interference theory or infinite-state theorem.

## 12. Next frontier

The next controlled extension is an exact **factor-certificate compiler** that accepts a mixed list of split-linear, quadratic-four-chamber and general Sturm factors, emits:

1. the one-shot selector bit;
2. the failing-factor support;
3. optional distinct-root Möbius data;
4. the observer-appropriate one-parameter event polynomial.

A second frontier is sparse intersection compression: identify when the subset-gcd Möbius tower can be represented by the intersection poset rather than all `2^n-1` subsets.
