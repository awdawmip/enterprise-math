# Native Enterprise primitive-ray classification for the maximal 105 gate

Status: `FREE_RESEARCH_EXACT_FINITE_CLASSIFICATION / NOT_CANONICAL_FOUNDATION`

Date: `2026-08-23`

Researcher-ID: `EM-FREE-NEPS-239A6D`

Parent: `NATIVE_ENTERPRISE_C3_BOUQUET_ROOT_PROFILE_20260823.md`

## 1. Problem

For a primitive native ray `(u,v,0)`, `gcd(u,v)=1`, let its three cyclic quadratic label lanes be

`F0(m)=B_{(u+v)m}+v*m`,

`F1(m)=F0(m)+(u+v)m`,

`F2(m)=F0(m)+2(u+v)m`.

For q in `{3,5,7}`, call q a saturated gate when for every nonzero `m mod q` at least one `Fk(m)` is zero mod q.

The maximal small-prime gate means simultaneous saturation at 3,5,7, hence gate product 105.

## 2. Exact finite direction classification

The gate condition depends only on `(u,v) mod q`. Exhaustive exact enumeration of the q^2 residue pairs gives:

### q=3

The saturated nonzero direction pairs are

`(0,1),(0,2),(1,0),(1,1),(2,0),(2,2)`.

Equivalently, excluding `(0,0)`,

`u*v*(u-v)=0 mod 3`.

In projective language the saturated directions are

`[1:0], [0:1], [1:1]`;

the only projective direction that fails is `[1:-1]`.

### q=5

The saturated pairs are exactly

`(a,a)`, `a in {1,2,3,4}`.

Equivalently

`u=v !=0 mod5`, or `[u:v]=[1:1] in P^1(F_5)`.

### q=7

The saturated pairs are exactly

`(a,a)`, `a in {1,2,3,4,5,6}`.

Equivalently

`u=v !=0 mod7`, or `[u:v]=[1:1] in P^1(F_7)`.

These tables are finite exact classifications, not statistical searches.

## 3. Closed form for primitive maximal-gate rays

For primitive `(u,v)`, simultaneous 3,5,7 saturation is therefore equivalent to

`35 | (u-v)`,

`gcd(u*v,35)=1`,

`3 | u*v*(u-v)`.

The primitive assumption already prevents both u and v from being divisible by the same prime.

Thus the complete maximal-gate family is an arithmetic family of integer lifts of the equal-coordinate projective direction modulo 5 and modulo 7, with the three allowed q=3 directions.

## 4. Minimum-complexity theorem

The equal-coordinate primitive ray `(1,1)` has complexity

`u+v=2`

and satisfies the maximal gate.

If a positive primitive maximal-gate ray is not equal-coordinate, then

`u-v` is a nonzero multiple of 35,

so

`|u-v|>=35`.

The least possible positive sum is therefore at least 37. Equality is attained exactly, up to swap, by

`(u,v)=(1,36)` and `(36,1)`.

Both satisfy the mod3 gate because one coordinate is divisible by 3.

Hence:

`(1,1) = UNIQUE MINIMUM-COMPLEXITY MAXIMAL-GATE RAY`,

and

`NEXT MAXIMAL-GATE COMPLEXITY = 37`.

This proves the earlier bounded-census gap without relying on the census.

## 5. Geometric interpretation

The strongest possible three-quadratic small-prime gate selects the native sector bisector internally:

- modulo 5, saturation forces the equal-coordinate direction;
- modulo 7, saturation again forces the equal-coordinate direction;
- modulo 3, the equal-coordinate direction is one of only three surviving projective directions.

Therefore the native equal-coordinate ray is not selected merely because it is visually symmetric. It is the least positive integer lift of the unique common saturated projective direction at the two load-bearing moduli 5 and 7.

The higher-complexity maximal-gate rays are congruence lifts of this same finite-field direction rather than new low-complexity geometric competitors.

## 6. Boundary

The finite modular enumeration and CRT consequences are elementary classical arithmetic. The Enterprise-specific research statement is the selection provenance:

`NATIVE C3 RAY DIRECTION`

`-> CYCLIC QUADRATIC LABEL ORBIT`

`-> MAXIMAL ROOT-SATURATION REQUIREMENT`

`-> [u:v]=[1:1] mod 5 and mod 7`

`-> EQUAL-COORDINATE NATIVE BISECTOR AS UNIQUE MINIMAL INTEGER LIFT`.
