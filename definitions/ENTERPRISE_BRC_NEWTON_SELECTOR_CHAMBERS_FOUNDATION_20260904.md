# Enterprise Math — BRC Split-Affine Newton Selector Chambers Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION CANDIDATE / MAIN-BACKED RESEARCH / COMPLETE-SPLIT SELECTOR CERTIFICATES`
Effective: `2026-09-04`
Parent: `ENTERPRISE_BRC_NEWTON_SCHEDULE_STRATA_FOUNDATION_20260904.md`
Evidence: PR #1206

## 1. Scope and prior art

This addendum closes the WBRC-T59 root-selector gap for a typed certificate class in which the complete real-root inventory of a Newton edge is explicitly represented by one fixed declared rational root plus finitely many rational-affine real-root branches.

Root ordering and affine half-space geometry are classical mathematics. No generic novelty claim is made. The Enterprise/BRC content is the exact selector lease:

- T59 still certifies declared root/multiplicity/scale validity;
- a complete split-affine root certificate supplies the entire real-root inventory;
- smallest-real and smallest-positive selectors then reduce to exact affine order conditions;
- selector-value stability and declared multiplicity stability remain separately typed at root-collision hyperplanes.

This is not a general parametric Sturm/subresultant theorem.

## 2. Complete split-affine real-root certificate

Let `lambda=(lambda_1,...,lambda_d)` be rational parameters. Fix a declared rational root `r` with declared multiplicity `m>=1`.

A complete split-affine selector certificate consists of:

- the fixed root `r` and multiplicity `m`;
- finitely many rational-affine root branches `h_j(lambda)` with positive multiplicities `m_j`;
- exact degree accounting showing that the displayed root factors exhaust the polynomial degree;
- a nonzero overall scalar factor on the parameter set under discussion.

Semantically,

`E(y;lambda)=c(lambda)(y-r)^m product_j (y-h_j(lambda))^(m_j)`.

For a fixed-multiplicity schedule, root collisions

`h_j(lambda)=r`

are excluded.  The product coefficients need not remain affine when several moving roots are multiplied; the split certificate is an additional typed representation, not a replacement for the T59 affine-coefficient carrier.

## 3. WBRC-T60 — smallest-real selector chamber

Within the fixed-multiplicity split certificate, the declared root `r` is the smallest real root iff

`h_j(lambda)>r`

for every j.

Therefore the selector-stable set is an intersection of strict rational affine half-spaces.  Its only root-order boundaries are the affine collision hyperplanes

`h_j(lambda)=r`.

For

`E_t(y)=(y+1)^2(y-t)`,

the declared root `r=-1` is double for `t!=-1` and is the smallest real root iff

`t>-1`.

At `t=-1` the selector value may still equal `-1`, but the declared multiplicity changes from two to three. For `t<-1`, the smallest real selector changes to `t`.

Canonical ID: `WBRC-T60`.

## 4. WBRC-T61 — smallest-positive selector chamber

Assume `r>0`. Within the fixed-multiplicity split certificate, `r` is the smallest positive real root iff every other branch satisfies

`h_j(lambda)<=0 OR h_j(lambda)>r`.

Hence the selector-stable set is a finite Boolean combination of rational affine order inequalities. It can be disconnected and non-convex even when every root branch is affine.

For

`F_t(y)=(y-1)^2(y-t)`,

the declared root `r=1` is double for `t!=1` and is the smallest positive root iff

`t<=0 OR t>1`.

For `0<t<1`, the selector changes to `t`. At `t=1`, the declared multiplicity changes. At `t=0`, the selector remains 1 because zero is not a positive root.

Canonical ID: `WBRC-T61`.

## 5. Multi-parameter chambers

For

`E_(u,v)(y)=(y+1)^2(y-u)(y-v)`,

the fixed root `-1` is the smallest real root exactly on

`u>-1 AND v>-1`.

For

`F_(u,v)(y)=(y-1)^2(y-u)(y-v)`,

the fixed root 1 is the smallest positive root exactly on

`(u<=0 OR u>1) AND (v<=0 OR v>1)`.

The second set is generally disconnected. This is a selector-semantic distinction, not an implementation artifact.

## 6. T59 composition rule

The exact composition is:

```text
T59 DECLARED SCHEDULE VALIDITY STRATUM
+ COMPLETE SPLIT-AFFINE REAL-ROOT CERTIFICATE
+ T60/T61 AFFINE ORDER CONDITIONS
    -> ACTUAL SELECTOR STABILITY IN THE CERTIFICATE CLASS
```

T60/T61 do not replace T59 multiplicity conditions. A collision may preserve the selector value while invalidating the declared multiplicity/schedule.

## 7. Decision tree after T59

```text
NEED ONLY DECLARED ROOT/MULTIPLICITY/SCALE VALIDITY
    -> WBRC-T59

COMPLETE SPLIT-AFFINE REAL-ROOT CERTIFICATE + SMALLEST-REAL SELECTOR
    -> WBRC-T60

COMPLETE SPLIT-AFFINE REAL-ROOT CERTIFICATE + SMALLEST-POSITIVE SELECTOR
    -> WBRC-T61

NON-SPLIT PARAMETRIC EDGE / HIDDEN ROOT ORDERING
    -> PARAMETRIC STURM-SUBRESULTANT FRONTIER
```

## 8. Hard negative/scope boundaries

```text
COMPLETE_SPLIT_AFFINE_CERTIFICATE_IS_REQUIRED
SPLIT_SELECTOR_CHAMBER != GENERAL_PARAMETRIC_STURM_CHAMBER
SELECTOR_VALUE_STABILITY != DECLARED_MULTIPLICITY_STABILITY
SMALLEST_REAL_SELECTOR != SMALLEST_POSITIVE_SELECTOR
ZERO_ROOT_IS_NOT_POSITIVE
AFFINE_ROOT_BRANCHES != AFFINE_POLYNOMIAL_COEFFICIENTS
T60_T61_DO_NOT_REPLACE_T59_SCHEDULE_VALIDITY
FINITE_SPLIT_SELECTOR_CERTIFICATE != COMPLETE_PUISEUX_OR_MULTIGENERATOR_SOLVER
```

Canonical negative IDs: `WBRC-N68..N75`.

## 9. Tool routing

No new top-level family is created. The companion subtool is

`t0.weighted_brc_newton_selector_chambers`.

Production code provides:

- typed split-affine root branches with multiplicities;
- complete degree accounting for a declared fixed root and branch inventory;
- exact fixed-multiplicity noncollision checks at rational parameter points;
- exact smallest-real and smallest-positive selector predicates;
- affine order atoms/clauses and selector chamber predicates;
- exact materialization of the factorized polynomial at rational parameter points for regression/certificate checks.

It does not infer a split factorization from arbitrary polynomial coefficients.

## 10. Validation

Main-backed PR #1206 verified:

- a 49-point two-parameter smallest-real grid with 36 fixed-multiplicity points, 13 collisions and 16 stable points;
- a 49-point two-parameter smallest-positive grid with 36 fixed-multiplicity points, 13 collisions and 25 stable points;
- 98 exact Sturm real-root inventory checks total across the two grids;
- 196 selector-order checks across the two grids;
- 11 explicit zero-root boundary points for smallest-positive semantics;
- a 25-point one-parameter sweep through the `t=-1`, `t=0`, and `t=1` boundaries;
- exact affine threshold-form regression.

## 11. Next frontier

The next genuinely new selector problem is a non-split rational-affine edge family. The natural exact route is a parametric Sturm/subresultant sign chamber: root counts and order remain fixed while the relevant subresultant, leading-coefficient and endpoint-evaluation signs avoid zero.
