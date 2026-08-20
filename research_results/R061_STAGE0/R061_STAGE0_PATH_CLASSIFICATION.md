# R061 Stage 0 — Path Class Classification

## Answer to WHAT_FINITE_PATH_CLASS_IS_CANONICALLY_GENERATED_BY_THE_LINE_FORMULA?

For fixed `(a,b)`, `Lambda(a,b)` generates exactly:

`ALL DIRECTED COORDINATE-MONOTONE TWO-POSITIVE-GENERATOR WORDS`

in the abstract `N_0^2` chart, from formal displacement `(0,0)` to `(a,b)`,
using only `+X` and `+Y`.

This class is finite and has size `binom(a+b,a)`.

It is minimum-jump only in the restricted directed graph whose only moves are
`+X,+Y`. That restricted statement is tautological and is not a theorem about
the full native circle-cell carrier.

## It is not all carrier minimum-jump paths

The current foundation retains the triangular nearest-center carrier and
explicitly preserves the classical carrier direction relation as a carrier
relation, while forbidding its use as a native vector/metric identity.

Let the three unit nearest-center carrier translations along the positive
direction families be `t1,t2,t3`. Then, at the carrier incidence level,

`t1+t2+t3=0`.

So

`-t3=t1+t2`.

For a selected start cell and target displacement `(a,b)` in the `t1,t2`
coordinates, the full nearest-neighbor carrier permits steps

`±(1,0), ±(0,1), ±(1,1)`,

where `(1,1)` is the inverse-third-family move `-t3`.

For `a,b>=0`, the carrier graph distance is therefore

`d_jump((0,0),(a,b))=max(a,b)`.

Proof: each nearest-neighbor step changes either coordinate by at most one, so
at least `max(a,b)` steps are necessary. If `a>=b`, take `b` diagonal
`(1,1)` steps and `a-b` `(1,0)` steps; the case `b>=a` is symmetric.

Hence for every interior branch `a,b>0`,

`max(a,b) < a+b`.

The shuffle words are not carrier graph geodesics.

Smallest positive interior witness:

`(a,b)=(1,1)`, `N=2`.

`Lambda(1,1)={X1X2,X2X1}` uses two center transitions, whereas one
nearest-center inverse-third-family move `-X3` reaches the same carrier center.

## It is not all simple native paths

Even before resolving origin incidence, the full triangular carrier has many
simple detours and cross-sector paths that use directions outside `{+X,+Y}`.
The shuffle fiber includes none of them.

The unrestricted walk class is infinite because loops may be inserted.

## Canonicality verdict

`PATH_CLASS_TYPED_FINITE_AND_CANONICAL = false`.

More precisely:

- `TYPED_FINITE = true` at the formal two-generator level;
- `NATIVE_CANONICAL = not established`;
- if the downstream combinatorial realization is "retain all minimum-jump
  center paths after the target cell is selected", the shuffle fiber is
  exactly wrong on every nondegenerate interior branch.

No replacement native line formula is frozen here. The carrier geodesic
formula above is a falsification diagnostic only, because native Enterprise
length is not graph jump count and the origin-to-cell realization remains
unresolved.
