# P025 Supplement 09 — Exact Rank-Two Absorption Access by Integer Interval Intersection

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner: `program/p025-abc-support-collapse`  
Depends on: P025 Supplements 07–08  
Hard block: `NONE`

## 1. Scope

Supplements 07–08 reduced the absorption-optimal access radius to

\[
\nu
=\min\{\|x\|_\infty:
\alpha\cdot x=0,
\ \beta\cdot x=\pm d\},
\]

where

\[
d=\operatorname{cont}(\alpha\wedge\beta)>0.
\]

For general witness dimension this is an affine-lattice minimum problem.

This supplement solves it exactly when

\[
\boxed{\omega(abc)=3,}
\]

so the additive witness lattice has rank two.

The result uses only integer linear algebra and interval arithmetic. It removes cubic witness-ball enumeration from the exact reference path.

## 2. P025-T25 — the floor-attaining set is one primitive integer affine line

Assume there are exactly three prime coordinates and the Wronskian is non-degenerate on the additive witness lattice.

Let

\[
\alpha,\beta\in\mathbb Z^3
\]

be the primitive additive row and raw Wronskian row. Define the cross product

\[
c=\alpha\times\beta.
\]

Its coordinate content is

\[
\operatorname{cont}(c)=d,
\]

the positive Wronskian image generator from Supplement 04. Let

\[
\boxed{n_0=c/d}
\]

after fixing a global sign, so `n_0` is primitive.

Then

\[
\boxed{
\ker_{\mathbb Z}\alpha
\cap
\ker_{\mathbb Z}\beta
=
\mathbb Z n_0.
}
\]

Now let `x_0` be any integer witness satisfying

\[
\alpha\cdot x_0=0,
\qquad
\beta\cdot x_0=d.
\]

For example Supplement 08 supplies such an `x_0` constructively.

Then the complete positive-generator slice is

\[
\boxed{
\{x\in\mathbb Z^3:
\alpha\cdot x=0,
\beta\cdot x=d\}
=
x_0+\mathbb Z n_0.
}
\]

The negative-generator slice is its negation and has the same minimum `L_infinity` norm.

### Proof

Because `alpha,beta` have rational rank two, their common rational kernel is the line spanned by `alpha x beta`. Dividing by the content gives the primitive integer generator of the saturated integer kernel. If `x` and `x_0` both solve the inhomogeneous system, their difference lies in the common integer kernel, hence equals `k n_0` for a unique integer `k`. The converse is immediate. ∎

## 3. P025-T26 — exact radius feasibility is an integer interval intersection

Write

\[
x_0=(x_1,x_2,x_3),
\qquad
n_0=(n_1,n_2,n_3).
\]

For a candidate radius `B>=0`, a parameter `k in Z` is feasible exactly when

\[
|x_i+k n_i|\le B
\qquad(i=1,2,3).
\]

Each coordinate gives one integer interval `I_i(B)` for `k`:

- if `n_i>0`,
  \[
  \left\lceil\frac{-B-x_i}{n_i}\right\rceil
  \le k\le
  \left\lfloor\frac{B-x_i}{n_i}\right\rfloor;
  \]
- if `n_i<0`, equivalently with `m_i=-n_i>0`,
  \[
  \left\lceil\frac{x_i-B}{m_i}\right\rceil
  \le k\le
  \left\lfloor\frac{x_i+B}{m_i}\right\rfloor;
  \]
- if `n_i=0`, feasibility requires `|x_i|<=B` and imposes no parameter restriction.

Therefore

\[
\boxed{
B\text{ is feasible}
\iff
\bigcap_{i=1}^3 I_i(B)\cap\mathbb Z
\ne\varnothing.
}
\]

All endpoints are computed by floor/ceiling integer division.

## 4. P025-T27 — exact `nu` by finite binary search

Feasibility is monotone in `B`: if a parameter works at radius `B`, it also works at every larger radius.

A constructive Bezout witness `x_0` gives the finite upper bound

\[
\nu\le\|x_0\|_\infty.
\]

Hence binary search on the finite integer interval

\[
0\le B\le\|x_0\|_\infty
\]

using P025-T26 returns the exact optimum

\[
\boxed{
\nu
=
\min_{k\in\mathbb Z}
\|x_0+k n_0\|_\infty.
}
\]

The number of radius checks is logarithmic in the constructive upper bound, and each check intersects at most three integer intervals.

This is exact arithmetic; no float optimization or bounded witness-ball enumeration is required.

## 5. `1+242=243` revisited

For

\[
1+242=243,
\]

Supplement 08 supplied the constructive floor witness

\[
x_0=(-405,11,1215).
\]

The primitive common-kernel direction is

\[
\boxed{n_0=(4,0,-11).}
\]

Thus every positive-generator witness is

\[
(-405,11,1215)+k(4,0,-11).
\]

At radius `26`, the three coordinate constraints have empty integer intersection.

At radius `27`, their intersection is exactly

\[
\boxed{k=108.}
\]

This gives

\[
\boxed{x=(27,11,27)}
\]

and therefore

\[
\boxed{\nu=27.}
\]

The previous cubic enumeration is unnecessary.

## 6. Calibration examples

### `2+3=5`

\[
n_0=(2,3,5),
\qquad
\nu=2.
\]

The direct Bezout certificate is already optimal.

### `2+7=9`

\[
n_0=(4,3,14),
\qquad
\nu=5,
\]

again matching the simple Bezout certificate.

### `1+242=243`

The same exact algorithm compresses an upper bound `1215` down to the true `27` without searching the ambient cube.

## 7. Architectural meaning

This stage separates three kinds of computation:

\[
\boxed{
\text{minor gcd}
\to
\text{arithmetic floor }d
\to
\text{one floor witness }x_0
\to
\text{affine kernel direction }n_0
\to
\text{exact minimum access radius }\nu.
}
\]

The important point is that each step discards a different kind of uncertainty:

- the minor gcd settles **which Wronskian scale is attainable**;
- the Bezout witness settles **existence of a preimage**;
- the affine direction settles **all alternative preimages**;
- the interval intersection settles **which preimage has minimum task cost**.

A certificate pipeline can therefore be exact and finite without identifying all witnesses.

## 8. Relation to mature mathematics

For three variables, solving two independent integer linear equations reduces to an affine rank-one lattice, and minimizing a convex norm on that line is standard integer optimization / closest-lattice-point territory.

P025 claims no novelty for:

- cross products and primitive integer kernels;
- one-dimensional lattice cosets;
- interval feasibility;
- binary search over a monotone integer predicate.

The project-specific object under study is the resulting **certificate access precision** attached to the abc/Pasten witness language.

## 9. Executable assets

Added:

- `src/enterprise_math/abc_absorption_rank2.py`
  - primitive common-kernel direction;
  - exact parameter interval for a radius;
  - monotone finite feasibility test;
  - exact binary-search solver for `nu` when `omega(abc)=3`.
- `tests/test_abc_absorption_rank2.py`
  - exact directions for three working triples;
  - exact optima for `2+3=5`, `2+7=9`, and `1+242=243`;
  - sharp infeasibility at radius `26` and singleton feasibility at `27` for the last example.

The Bezout regression was also updated to consume this exact affine solver instead of repeating a cubic witness-ball scan.

## 10. Next frontier

No hard block exists. Continue with:

1. derive a closed or near-closed modular formula for the minimizing parameter `k` rather than binary-searching the radius;
2. specialize the rank-two solver to structured families such as `1+qr=p^m` and identify explicit formulas for `nu`;
3. compare `nu` with the first successive minimum of the additive witness lattice and with Pasten's Geometry-of-Numbers bounds;
4. search for a family where the naive Bezout certificate / exact `nu` ratio grows without bound;
5. lift the affine-line idea to `omega(abc)>3` using quotient lattices while preserving the distinction between existence and minimum access precision.
