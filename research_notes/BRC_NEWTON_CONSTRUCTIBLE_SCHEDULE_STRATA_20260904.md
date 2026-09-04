# BRC Newton constructible schedule strata under affine perturbation

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T57/T58

## 1. Problem

WBRC-T58 gives exact finite-horizon observability for a **frozen** Newton schedule.  The missing bridge is to determine when a declared schedule remains algebraically valid after the coefficients are perturbed.

For multiple roots this is not ordinary open-neighborhood stability.  Multiplicity and contact order are defined by exact vanishing conditions, so the natural parameter regions are constructible strata cut out by affine equalities and non-equalities.

This note proves the rational-affine version of that statement.

## 2. Affine rational Newton family

Let `lambda=(lambda_1,...,lambda_d)` be rational parameters.  Let a finite Newton jet have fixed rational-valuation scales `sigma` and polynomial layers

`P_sigma(x;lambda)`

whose coefficients are affine rational forms in lambda.

Fix a declared rational root `x0` and multiplicity `r>=2` for the scale-one layer.  For every strict scale sigma and Taylor order k define the affine form

`A_(sigma,k)(lambda) = P_sigma^(k)(x0;lambda)/k!`.

For `k<r`, the contact order is

`q_sigma(lambda) = min{k<r : A_(sigma,k)(lambda) != 0}`,

with no Newton candidate from sigma when all such forms vanish.

Therefore the finite collection of hyperplanes

`A_(sigma,k)=0`

stratifies parameter space into finitely many zero/nonzero patterns on which every contact order q_sigma is constant.

## 3. Piecewise-constant Newton scale

On one such contact stratum, every candidate scale

`theta_sigma = sigma^(1/(r-q_sigma))`

is constant in the exact rational-prime-valuation carrier.  Hence the selected Newton scale

`theta = max_sigma theta_sigma`

is also constant on that stratum.

Thus Newton-scale changes can occur only when one of the finitely many relevant affine Taylor forms crosses its zero hyperplane.

This is stronger and more precise than saying the scale is 'locally stable': at a multiple-root locus the valid stratum can have positive codimension and need not contain any ordinary open ball.

## 4. Edge polynomial remains affine on a fixed scale stratum

Fix a contact stratum and its selected theta.  The residual scale-one edge receives exactly those Taylor atoms satisfying

`sigma theta^(k-r)=1`.

Its coefficients are therefore finite sums of the affine forms A_(sigma,k), so the edge polynomial

`E_theta(y;lambda)`

still has affine rational coefficient forms.

For a declared rational edge root `y0` and declared multiplicity `m`, the condition

`ord_(y0) E_theta = m`

is exactly

`E_theta^(j)(y0;lambda)=0` for `0<=j<m`,

and

`E_theta^(m)(y0;lambda) != 0`.

These are again finitely many affine rational equalities/non-equalities.

Hence a one-step declared rational-root Newton schedule is valid on a rational constructible parameter stratum.

## 5. Finite schedule induction

Once one declared step is fixed, the scheduled substitution is linear in the coefficient state by WBRC-T58.  Linear substitution preserves affine dependence on the original parameters.

Therefore the same argument iterates:

> for any finite declared schedule of rational roots, positive multiplicities and fixed rational-valuation Newton scales, the parameter set on which every contact order, selected scale and declared root multiplicity is algebraically valid is a finite Boolean combination of rational affine equalities and non-equalities.

Equivalently, finite rational-root Newton schedule validity is constructible in the affine parameter space.

This theorem validates a frozen schedule on its exact stratum.  It does not yet certify that a separate global root-selector rule continues to choose the same root among all possible roots.

## 6. Exact three-parameter witness

Consider

`J_s(x;u,v,w) = (x-1)^2`

` + (1/2)^s [u + 2(x-1)]`

` + (1/4)^s [v + 2(x-1)]`

` + (1/8)^s 2`

` + (1/16)^s w`.

Take the first declared root `x0=1` with multiplicity `r=2`.

The `(1/2)` layer has Taylor data

`A_(1/2,0)=u`,
`A_(1/2,1)=2`.

Hence:

- if `u != 0`, its contact is q=0 and its candidate scale is `sqrt(1/2)`;
- if `u = 0`, its contact is q=1 and its candidate scale is `1/2`.

All other candidate scales are <=1/2.  Therefore

`theta_1 = sqrt(1/2)` iff `u!=0`,

and

`theta_1 = 1/2` iff `u=0`.

On the stratum `u=0`, the first edge is

`E_1(y)=y^2+2y+v`.

Thus `y0=-1` is a double root iff

`v=1`.

On the sub-stratum `u=0, v=1`, the first residual strict layers combine to

- scale `1/2`: `2(y+1)`;
- scale `1/4`: constant `w`.

At the declared second root `y0=-1`, both give candidate scale `1/2`, so

`theta_2=1/2`.

The second edge is

`E_2(z)=z^2+2z+w`.

Thus the next declared root `z0=-1` is double iff

`w=1`.

The complete two-rescaling schedule stratum is therefore exactly

`u=0, v=1, w=1`.

## 7. Non-open boundary is exact

At `(u,v,w)=(0,1,1)` the two-step declared schedule is valid.  But for every nonzero rational epsilon, however small,

`u=epsilon`

changes the first contact order from 1 to 0 and changes the first Newton scale from

`1/2`

to

`sqrt(1/2)`.

Therefore the schedule-valid set is not an ordinary open neighborhood of the witness point.

## 8. Relation to T58

T58 says a frozen schedule yields exact linear future observability.

The present result says when that same declared schedule is algebraically valid over an affine perturbation family.  Inside the constructible stratum, the T58 frozen substitutions coincide with valid Newton steps using the declared roots/multiplicities/scales.

The remaining selector frontier is narrower:

> certify that the upstream root-selection rule itself chooses the same root on the whole constructible stratum.

That may require exact isolation/order/sign information beyond affine derivative constraints.

## 9. Hard boundaries

- CONSTRUCTIBLE_SCHEDULE_STRATUM != OPEN_STABILITY_NEIGHBORHOOD.
- DECLARED_ROOT_VALIDITY != GLOBAL_ROOT_SELECTOR_STABILITY.
- AFFINE_RATIONAL_PARAMETER_FAMILY != ARBITRARY NONLINEAR PARAMETERIZATION.
- RATIONAL_DECLARED_ROOTS != GENERAL ALGEBRAIC MULTI-GENERATOR ROOTS.
- FIXED FINITE SCHEDULE != COMPLETE PUISEUX SOLVER.
- ALGEBRAIC CHARACTERISTIC COEFFICIENT CANCELLATION != SIGNED BRANCH-MASS INTERFERENCE.

## 10. Next frontier

The next exact step is selector stability: attach rational isolating intervals/order conditions to the constructible schedule stratum and certify that the same selected root remains isolated and preferred throughout the parameter region.
