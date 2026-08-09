# A3 Guard-Image Lattice Supplement 01 — Exact Branch Reachability for Rank-One Hidden Guards

Status: `RESEARCH WIP / EXACT INTEGER ARITHMETIC-LINE SOLVER`

## 1. Problem

The main note packages multi-guard hidden score geometry as

\[
L_G=W(K_A)\subseteq\mathbb Z^r.
\]

We already have:

- rank 0: all guards are visible;
- full rank `r`: every coarse fiber hits every strict orthant;
- partial rank cannot be summarized by rank alone.

This supplement solves the first complete nontrivial partial-rank case:

\[
\boxed{\operatorname{rank}L_G=1.}
\]

## 2. Canonical step of a rank-one lattice

Every rank-one integer subgroup can be written uniquely as

\[
L_G=\mathbb Z h,
\]

where `h` is chosen with first nonzero coordinate positive.

Given generators

\[
v_1,\ldots,v_d\in\mathbb Z^r,
\]

construct it by:

1. choose a nonzero `v`;
2. divide by the gcd of its coordinates to obtain a primitive direction `p`;
3. write every `v_i=t_i p` and set
   \[
   d=\gcd_i|t_i|;
   \]
4. return
   \[
   \boxed{h=d p.}
   \]

Only gcd and exact integer division are used.

## 3. A coarse fiber becomes an integer arithmetic line

Fix one fine representative of a coarse fiber and let its guard-score vector be

\[
g\in\mathbb Z^r.
\]

All guard scores in that fiber are exactly

\[
\boxed{g+t h,\qquad t\in\mathbb Z.}
\]

Branch reachability is therefore a one-integer problem rather than a high-dimensional state search.

## 4. A3-G06 — A threshold pattern is an integer interval

Each guard uses the binary threshold convention:

- `True`: score `>=0`;
- `False`: score `<0`, equivalently integer score `<=-1`.

For guard `j`, the score is

\[
g_j+t h_j.
\]

A requested truth value contributes either an integer lower bound or upper bound on `t`; if `h_j=0`, the base score decides whether the requirement is always satisfied or impossible.

Intersecting all bounds gives

\[
\boxed{
\{t\in\mathbb Z:\text{the branch pattern holds}\}
=[L,U]\cap\mathbb Z,
}
\]

with either side allowed to be unbounded. If `L>U`, the pattern is unreachable.

Hence

> **all branch reachability for rank-one hidden multi-guard systems has an exact single-integer interval representation.**

No fine-state enumeration or ILP solver is needed.

## 5. Equal rank does not imply equal patterns

Take base score `g=(0,0)`.

For diagonal step

\[
h=(1,1),
\]

the two guards move together.

For anti-diagonal step

\[
h=(1,-1),
\]

they move in opposite directions.

Both hidden image lattices have rank one, but their reachable threshold-pattern sets differ.

Thus the main-note negative boundary becomes executable:

\[
\boxed{
\text{partial hidden precision needs lattice direction, not only rank.}
}
\]

## 6. Consequence for piecewise quotients

Assume every affine branch already descends individually. In the rank-one case we do not need to compare all `2^r` branch effects.

For a given coarse state:

1. compute base guard scores `g`;
2. use `(g,h)` to compute the reachable branch-pattern set;
3. require equality only among the coarse effects of branches that are actually reachable.

This may need less precision than the full-rank regime because unreachable branch identities should not create a retention obligation.

The reachable set can depend on the coarse state's base scores `g`, so a general coarse piecewise program may need a state-dependent reachable-branch description rather than one global pattern mask.

## 7. Implementation

`guard_image_lattice.py` adds:

- `rank_one_lattice_step`;
- `guard_rank_one_step`;
- `rank_one_threshold_pattern_interval`;
- `rank_one_threshold_pattern_reachable`.

Tests compare the closed interval result against bounded arithmetic-line enumeration and preserve the diagonal/anti-diagonal same-rank/different-pattern counterexample.

## 8. Next

The remaining partial-hidden region is

\[
1<\operatorname{rank}L_G<r.
\]

The next target is rank two:

1. use an integer basis / Hermite normal form for a two-parameter affine lattice;
2. turn each sign pattern into two-dimensional integer half-plane feasibility;
3. seek a finite certificate for fixed guard dimension;
4. introduce general Presburger/ILP machinery only if needed, explicitly as prior-art tooling rather than new A3 ontology.
