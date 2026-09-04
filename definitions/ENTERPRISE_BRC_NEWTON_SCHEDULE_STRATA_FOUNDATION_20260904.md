# Enterprise Math — BRC Newton Constructible Schedule Strata Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION CANDIDATE / MAIN-BACKED RESEARCH / AFFINE-PARAMETER SCHEDULE VALIDITY`
Effective: `2026-09-04`
Parent: `ENTERPRISE_BRC_NEWTON_OBSERVER_LATTICE_FOUNDATION_20260904.md`
Evidence: PR #1204

## 1. Scope and prior art

This addendum upgrades WBRC-T58 from a frozen declared schedule to an exact description of rational-affine parameter values on which that declared schedule remains algebraically valid.

Hyperplane arrangements, constructible sets and affine linear algebra are classical mathematics. No generic novelty claim is made. The Enterprise/BRC content is the exact schedule-validity typing attached to rational-valuation Newton jets:

- affine Taylor coefficients determine contact-order strata;
- Newton candidate scales are constant on those strata;
- fixed-scale edge coefficients remain affine;
- rational declared root/multiplicity constraints remain affine equalities/non-equalities;
- frozen scheduled substitution preserves affine dependence, so the construction iterates for any finite declared rational-root schedule.

This is not a root-selector stability theorem.

## 2. WBRC-T59 — affine constructible schedule validity

Let `lambda=(lambda_1,...,lambda_d)` be rational parameters. Let a finite Newton jet have fixed rational-valuation scales `sigma` and polynomial layers

`P_sigma(x;lambda)`

whose coefficients are affine rational forms in lambda.

Fix a declared rational root `x0` and positive multiplicity `r`. For each strict layer and Taylor order define

`A_(sigma,k)(lambda)=P_sigma^(k)(x0;lambda)/k!`.

For `k<r`, the contact order is the first k for which this affine form is nonzero. Hence the finite family of hyperplanes

`A_(sigma,k)=0`

stratifies parameter space into finitely many zero/nonzero patterns on which every contact order is constant.

On each such stratum every candidate scale

`theta_sigma=sigma^(1/(r-q_sigma))`

is constant in the exact rational-prime-valuation scale carrier, so the selected Newton scale is constant as well.

Fix one such selected scale theta. The residual scale-one edge receives exactly the Taylor atoms satisfying

`sigma theta^(k-r)=1`.

Therefore each edge coefficient is a finite sum of affine rational forms and is itself affine in lambda.

For a declared rational edge root `y0` and declared multiplicity m, validity is exactly

`E_theta^(j)(y0;lambda)=0` for `0<=j<m`,

and

`E_theta^(m)(y0;lambda)!=0`.

These are finitely many affine equalities/non-equalities. Thus one declared rational-root Newton step is valid on a rational constructible parameter stratum.

Because a frozen scheduled Newton substitution is linear in the coefficient state by WBRC-T58, affine dependence on the original parameters is preserved after every valid declared step. Inductively:

> any finite declared rational-root Newton schedule has a schedule-valid parameter set that is a finite Boolean combination of rational affine equalities and non-equalities.

Canonical ID: `WBRC-T59`.

## 3. Exact witness

Main-backed PR #1204 used

`J_s=(x-1)^2 +(1/2)^s[u+2(x-1)] +(1/4)^s[v+2(x-1)] +(1/8)^s 2 +(1/16)^s w`.

At the declared root `x0=1`, multiplicity 2:

- `u!=0` gives first contact q=0 on the `(1/2)` layer and first Newton scale `sqrt(1/2)`;
- `u=0` gives q=1 and first Newton scale `1/2`.

On `u=0`, the first edge is

`E_1(y)=y^2+2y+v`,

so the declared root `y=-1` is double iff `v=1`.

On `u=0,v=1`, the next selected scale is again `1/2`, and the second edge is

`E_2(z)=z^2+2z+w`,

so the next declared root `z=-1` is double iff `w=1`.

The complete two-rescaling declared schedule stratum is exactly

`u=0, v=1, w=1`.

The same witness proves the valid set need not be open: every nonzero rational perturbation `u=epsilon` changes the first scale from `1/2` to `sqrt(1/2)`.

## 4. Decision tree after T58

```text
FROZEN DECLARED NEWTON SCHEDULE ONLY
    -> WBRC-T58

RATIONAL-AFFINE PARAMETER FAMILY + DECLARED RATIONAL ROOTS/MULTIPLICITIES/SCALES
    -> WBRC-T59 constructible schedule-valid stratum

NEED TO PROVE THE SAME GLOBAL ROOT-SELECTOR RULE CHOOSES THE SAME ROOT
    -> SELECTOR-STABILITY FRONTIER
```

## 5. Hard negative/scope boundaries

```text
CONSTRUCTIBLE_SCHEDULE_STRATUM != OPEN_STABILITY_NEIGHBORHOOD
DECLARED_ROOT_VALIDITY != GLOBAL_ROOT_SELECTOR_STABILITY
AFFINE_RATIONAL_PARAMETER_FAMILY != ARBITRARY NONLINEAR PARAMETERIZATION
RATIONAL_DECLARED_ROOTS != GENERAL MULTI-GENERATOR ALGEBRAIC ROOTS
FINITE_SCHEDULE_VALIDITY != COMPLETE_PUISEUX_SOLVER
AFFINE_EQUALITY/NON-EQUALITY STRATUM NEED NOT BE CONVEX OR OPEN
ALGEBRAIC CHARACTERISTIC CANCELLATION != SIGNED BRANCH-MASS CANCELLATION
```

Canonical negative IDs: `WBRC-N61..N67`.

## 6. Tool routing

No new top-level family is created. The companion subtool is

`t0.weighted_brc_newton_schedule_strata`.

Production code provides:

- exact rational affine forms and affine polynomials;
- affine Taylor forms at a declared rational root;
- exact contact order at a rational parameter point;
- exact selected Newton scale at a parameter point;
- affine edge polynomial for a fixed Newton scale;
- exact declared rational-root multiplicity constraint forms;
- exact affine scheduled Newton substitution preserving parameter dependence;
- evaluation of affine jets/states at rational parameter points.

It does not choose a global preferred root among multiple roots.

## 7. Validation

PR #1204 verified:

- 125 rational parameter points;
- 625 symbolic scale/edge checks against production `rational_newton_step`;
- 154 affine residual-state checks against production;
- all eight contact zero-pattern strata of the three-parameter witness;
- 25 points with first scale `1/2` and 100 with `sqrt(1/2)`;
- five first declared double-root points and one complete two-step schedule point;
- exact edge derivative constraints;
- 126 checks freezing the non-open boundary.

## 8. Next frontier

The next exact frontier is **root-selector stability**. One must augment the T59 constructible validity stratum with exact root-isolation/order conditions proving that the upstream selector itself continues to choose the same root throughout the parameter region.
