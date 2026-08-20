# R061 Stage 0 — Third-Axis / Cross-Sector Completeness Audit

## Status

`THIRD_AXIS_COMPLETENESS_PASS = false`

Smallest positive interior carrier counterexample:

`N=2`, `(a,b)=(1,1)`.

## Carrier-only derivation

Let `t1,t2,t3` be the three positive unit nearest-center direction
translations in the triangular carrier. The current foundation expressly
preserves

`t1+t2+t3=0`

as a **carrier presentation relation only**, while forbidding its use as a
native vector identity or native length formula.

Therefore

`-t3=t1+t2`.

Because center adjacency is undirected and nearest-center spacing is one, the
move from a center `C` to `C-t3` is one allowed nearest-center/overlap move.
The same carrier center is obtained by two positive active-axis translations:

`C+t1+t2`.

Thus, after any valid start cell has been selected,

- shuffle fiber for `(1,1)`:
  `{X1X2, X2X1}`;
- a legitimate nearest-center realization omitted by the shuffle:
  `{-X3}`.

No carrier Euclidean distance is used as native length. The native endpoint
branch still has `L_E^2=1^2+1^2=2`.

## General result

Using `(t1,t2)` coefficient coordinates, the six nearest-center carrier moves
are

`±(1,0), ±(0,1), ±(1,1)`.

Hence for `a,b>=0`:

`d_carrier_jump((0,0),(a,b))=max(a,b)`.

If `a>=b`, every geodesic has `a-b` moves `(1,0)` and `b` moves `(1,1)`
(`-t3`) in arbitrary order, so the geodesic count is

`binom(a,b)`.

If `b>=a`, symmetrically it has `b-a` moves `(0,1)` and `a` inverse-third
moves, count `binom(b,a)`.

For every `a,b>0`, these are strictly shorter than the `a+b` shuffle words.

## Interpretation

This does not create a native negative number axis. `-t3` denotes the reverse
direction of an undirected nearest-center carrier edge in the third direction
family. It is a cell-transition fact, not a native coordinate/vector
identification.

Therefore the proposed two-positive-generator shuffle cannot simultaneously
be claimed to be:

- all nearest-center realizations;
- all carrier minimum-jump realizations;
- or the complete native line fiber unless a new canonical rule explicitly
  excludes these third-family paths and proves why that exclusion is native.

The current task supplies no such rule, and the older downstream principle
that combinatorial realizations retain all minimizers points in the opposite
direction.

The counterexample is preserved rather than patched.
