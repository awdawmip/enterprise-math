# R061 Stage 0 — Exact Noncommutative Path-Lift Theorem

Task: `RS-R061-STAGE0-ENTERPRISE-LINE-FORMULA-ALGEBRAIC-PATH-LIFT-VALIDATION`

## Status

`NONCOMMUTATIVE_COEFFICIENT_LIFT_EXACT = true`

This result is purely formal. It does not by itself identify a word with a
native circle-cell trajectory.

## Theorem

Let `u,v` be central commuting markers and let `X,Y` be free noncommuting
letters. For `a,b in N_0`,

`Lambda(a,b)=[u^a v^b](uX+vY)^(a+b)`

is exactly the sum of every word of length `a+b` containing exactly `a`
copies of `X` and exactly `b` copies of `Y`, each with coefficient one.

Therefore

`|Lambda(a,b)| = binom(a+b,a) = binom(a+b,b)`.

## Proof

Expand the product as `a+b` ordered factors. At each factor choose either
`uX` or `vY`. A choice is uniquely encoded by the subset `S` of positions at
which `uX` was selected.

Because `u,v` commute with the free letters, the marker monomial is

`u^|S| v^(a+b-|S|)`.

The coefficient extraction `[u^a v^b]` retains exactly the subsets of size
`a`. Each such subset produces one ordered free word. Two different subsets
differ at a first position and hence produce different free words. Conversely
every word with `a` copies of `X` determines its unique `X`-position subset.
Thus occurrence is bijective and multiplicity is one.

## Formal endpoint map

Define

`End_formal(w)=(#X(w),#Y(w))`.

For every `w in Lambda(a,b)`,

`End_formal(w)=(a,b)`.

Abelianization sends all words in the fiber to the same commutative monomial
`X^a Y^b`, but no two distinct words are identified in the free associative
algebra.

Using only the native sector metric,

`L_E(End_formal(w))^2=a^2+b^2`.

Thus if `(a,b) in D_N`, every formal word lies above squared native coordinate
length `N`.

## Deterministic validation

Every pair `(a,b)` with `a+b<=22` was explicitly enumerated. Across all 276
pairs this materialized exactly

`8,388,607`

free words. For every pair:

- count equals `binom(a+b,a)`;
- no duplicate free word occurs;
- every word has the required endpoint counts.

Global explicit-word digest:

`572562117dbc2ba388543fbbeaa73bd26359ef47c26ef7ff31314ee92b318f93`.

For all `a+b<=512`, a compressed Pascal/DAG recurrence was checked exactly
against Python integer `binom`; mismatch count is zero.

## Scope limit

`End_formal` is a displacement/count map in the free two-generator chart.
It is not yet an absolute native cell-center address from `O_E`, because
`O_E` is not a cell and the start-incidence/affine address map is not supplied
by the current foundation.
