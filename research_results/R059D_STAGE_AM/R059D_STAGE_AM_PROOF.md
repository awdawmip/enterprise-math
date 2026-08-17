# R059D Stage AM — Canonical BRC circle collapse and source/target non-isometry

Researcher-ID: `EM-R059D-AM-8E3C64`

Task: `RS-R059D-STAGE-AM-CANONICAL-BRC-CIRCLE-COLLAPSE-NONISOMETRY`

## 1. Frozen typing

The source and target are different mathematical objects.

The source object is the accepted orthogonal compatibility circle `C_perp(O,r)`. On the source side only, use the standard compatibility embedding

`iota(a,b)=(a+b/2,(sqrt(3)/2)b)`.

Then the source quadratic chart satisfies

`|iota(a,b)|^2=a^2+ab+b^2`.

This source metric is not the Enterprise target length.

The target is already fixed before Stage AM by AL: the canonical Enterprise native circle is the unique final-`ADM_E` fixed-length local-turn orbit. Its elementary circumference unit is one legal turn, and its circumference is the minimal turn period

`T_r=C_E(r)=C_N(r)`.

Stage AM never uses source geometry to choose this target.

## 2. Canonical radial-incidence BRC relation

Let the canonical target endpoint cycle relative to `O` be

`p_0,p_1,...,p_(T_r-1)`

in positive turn order and let

`e_k=(p_k,p_(k+1 mod T_r))`.

For a source point `x in C_perp(O,r)`, write `d=x-O` for its source radius ray. Define the closed-fiber relation

`(x,e_k) in R_BRC,r`

iff the source ray `d` lies in the closed positively oriented angular cone from `iota(p_k)` to `iota(p_(k+1))`.

At a source ray through a target vertex, the source point belongs to the two neighboring closed fibers. This is the correct relational tie semantics; no target selection depends on how such a tie might be single-valued.

The construction is canonical once the source compatibility chart and the already-canonical target orbit are frozen. It is an incidence comparison, not a resolver.

## 3. Strict cyclic order

For a first-sector canonical edge, the only primitive moves are the accepted symbols.

If `p=(a,b)`:

- symbol 1: `p'=(a,b+1)`, so `det(p,p')=a>0`;
- symbol 2: `p'=(a-1,b+1)`, so `det(p,p')=a+b>0`;
- symbol 3: `p'=(a-1,b)`, so `det(p,p')=b>0`.

The endpoint cases are covered by the symbol-2 axis join, where the determinant is also positive. Therefore every target edge subtends a strictly positive source angle.

The first sector advances strictly from one directed axis ray to the next. D6 transport copies the same statement through six sectors, and `R^6=id` returns to the first ray. Hence the closed angular intervals between consecutive target rays form one cyclic cover of the source circle.

Consequences:

1. every target turn has a nonempty source fiber;
2. every fiber is one connected closed source arc;
3. fiber interiors are pairwise disjoint;
4. neighboring fibers meet exactly at one target-vertex source ray;
5. non-neighbor fibers are disjoint;
6. the union of all fibers is the full source circle;
7. the fiber order is the target turn order;
8. the relation is D6 equivariant and translation covariant.

Because the source circle is continuous and the target turn set is finite for fixed integer `r`, the collapse is genuinely many-to-one.

## 4. Exact source-angle formula

Let consecutive target rays in one source-compatible sector be represented by

`p=(a,b)`, `q=(c,d)`.

In the source orthogonal compatibility embedding,

`cross(iota(p),iota(q))=(sqrt(3)/2)(ad-bc)`

and

`2 dot(iota(p),iota(q))=2ac+2bd+ad+bc`.

Write

`Delta_num=ad-bc > 0`

and

`D=2ac+2bd+ad+bc > 0`.

For the angular interval `Delta` between the two rays,

`tan(Delta)=sqrt(3)*Delta_num/D`.

The source arc measure of the corresponding fiber is

`mu_perp(F)=r*Delta`.

This formula is source-side only.

## 5. First exact failure of equal one-turn source arcs

For `r=1`, each D6 sector consists of one turn, so all six source angular fibers are equal by D6.

For `r=2`, the canonical sector is `22`; its two fibers are reflection paired and both have tangent signature `sqrt(3)/3`.

For `r=3`, the canonical sector is still the straight word

`222`.

Consider its first two target turns.

### Edge 0

`p=(3,0)`, `q=(2,1)`.

Then

`Delta_num=3`, `D=15`,

so

`tan(Delta_0)=sqrt(3)/5`.

### Edge 1

`p=(2,1)`, `q=(1,2)`.

Then

`Delta_num=3`, `D=13`,

so

`tan(Delta_1)=3sqrt(3)/13`.

Since

`1/5 != 3/13`

and both angles lie strictly between `0` and one source sixth-turn, the source angles are unequal:

`Delta_0 != Delta_1`.

Both target turns are the same primitive target symbol `2` and both have native target turn weight one. Therefore source arc length is not determined by the target one-turn state.

This is a local obstruction. It does not use any comparison between the numerical values of source and target circumference constants.

## 6. Metric nondescend

Suppose source arc measure descended to a target-local one-turn metric at radius `r`. Then there would exist a common source arc unit `lambda(r)` such that

`mu_perp(F_k)=lambda(r)`

for every elementary target turn `e_k`.

The exact `r=3` witness contradicts this.

Therefore

`SOURCE_EQUIDISTANCE_ARC_METRIC_DOES_NOT_DESCEND_THROUGH_CANONICAL_BRC`.

The BRC relation preserves cyclic order, D6 symmetry, translation covariance and radius-class compatibility, but it does not preserve source arc density per target turn.

## 7. Circumference versus turn period

The source circumference functional is the total source arc measure around `C_perp(O,r)`.

The target circumference functional is the minimal legal-turn period `T_r` of the canonical Enterprise fixed-length orbit.

The BRC relation says every source arc is accounted for and every target turn is represented. It does not say all source fibers have equal arc measure. Since equal-fiber descent fails, BRC compatibility alone cannot identify the source circumference functional with the target turn-period functional under one fixed local unit.

Thus

`SOURCE_ARC_CIRCUMFERENCE_IS_NOT_A_BRC_INVARIANT`.

A hypothetical extra isometry axiom assigning one common normalized source arc unit to every target turn would force the source and target circumference/diameter constants to coincide. That is an additional axiom, not part of BRC, and its equal-fiber premise is false.

## 8. Distinct realizations

At fixed finite integer `r`:

- the source circle has a continuous point state space;
- the target circle has a finite number `T_r` of elementary turns;
- each target turn has a nontrivial source arc fiber;
- the bridge is therefore many-to-one;
- source arc length does not descend to the target turn metric;
- target canonicality was already proved independently by AL.

Hence the two circles are not merely two coordinate charts of one metric circle.

They are distinct realizations connected by a non-isometric BRC collapse:

`ORTHOGONAL_CONTINUOUS_CIRCLE_AND_ENTERPRISE_NATIVE_CIRCLE_ARE_DISTINCT_REALIZATIONS_CONNECTED_BY_NONISOMETRIC_BRC_COLLAPSE`.

## 9. Typed constants

Define source-only

`kappa_perp = Circ_perp(O,r)/(2r)`.

Standard source mathematics may call this source constant `pi_source`. It remains source typed.

The target constant remains the previously proved native constant

`kappa_E^2=12`, `kappa_E>0`,

with

`kappa_E=lim_(r->infinity) T_r/(2r)`.

Stage AM does not identify `kappa_perp` with `kappa_E`, does not use the source constant to tune the target, and proves no new theorem about the algebraicity of the standard real number pi.

## 10. Runtime and semantic firewall

The target remains the AL canonical orbit. No AM construction:

- chooses or retunes the target from source arc error;
- redefines Enterprise length as source distance;
- reintroduces source Q as target membership;
- assumes source circumference equals target period;
- uses standard pi numerics as a target-selection signal.

Finite replay validates the bridge implementation only. The coverage/fiber and non-isometry statements above are symbolic.
