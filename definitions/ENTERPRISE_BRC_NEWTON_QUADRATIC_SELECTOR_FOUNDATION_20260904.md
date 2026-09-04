# Enterprise Math — BRC Non-Split Quadratic Newton Selector Foundation Addendum

Status: `CANONICAL ALL-RESEARCH FOUNDATION CANDIDATE / MAIN-BACKED RESEARCH / NON-SPLIT QUADRATIC SELECTOR`
Effective: `2026-09-04`
Parent: `ENTERPRISE_BRC_NEWTON_SELECTOR_CHAMBERS_FOUNDATION_20260904.md`
Evidence: PR #1208

## 1. Scope and prior art

This addendum extends WBRC-T60 beyond complete split-affine root inventories to the first genuinely non-split selector class: one monic quadratic competing factor.

Quadratic discriminants and root ordering are classical mathematics. No generic novelty claim is made. The Enterprise/BRC content is an exact selector state that:

- keeps the declared rational Newton root and multiplicity typed separately;
- decides smallest-real selector stability without solving the competing quadratic roots;
- works when the competing roots are complex, repeated, rational or irrational real;
- remains exact over rational-affine coefficient families.

This is not a general parametric Sturm/subresultant chamber theorem.

## 2. WBRC-T62 — non-split monic-quadratic smallest-real selector chamber

Fix a declared rational root `r` with multiplicity `m>=1` and edge representation

`E(y;lambda)=(y-r)^m Q(y;lambda)`,

where

`Q(y;lambda)=y^2+a(lambda)y+b(lambda)`

is monic quadratic.  In the affine-parameter application, `a,b` are rational-affine forms.

Fixed declared multiplicity requires

`R(lambda):=Q(r;lambda)=r^2+a(lambda)r+b(lambda) != 0`.

Define

`D(lambda)=a(lambda)^2-4b(lambda)`,

`L(lambda)=-a(lambda)-2r`,

`R(lambda)=r^2+a(lambda)r+b(lambda)`.

Then, on the fixed-multiplicity stratum, the declared root r is the smallest real root of E iff

`D<0 OR (L>0 AND R>0)`.

Equivalently, including the multiplicity guard,

`R!=0 AND [D<0 OR (L>0 AND R>0)]`.

### Proof without root materialization

If `D<0`, Q has no real roots.

If `D>=0`, the smaller competing root is formally

`x_-=(-a-sqrt(D))/2`.

The condition `x_->r` is equivalent to

`-a-2r > sqrt(D)`.

The left-hand side must be positive.  Squaring is therefore order-safe, and

`L^2-D=(-a-2r)^2-(a^2-4b)=4(r^2+ar+b)=4R`.

Hence `x_->r` iff `L>0 AND R>0`.  No numerical or symbolic square-root materialization is needed by the decision procedure.

Canonical ID: `WBRC-T62`.

## 3. Semi-algebraic parameter form

When `a(lambda)` and `b(lambda)` are rational-affine forms:

- D is a rational quadratic polynomial in the parameters;
- L is affine;
- R is affine.

Thus the exact non-split selector chamber is a low-degree semi-algebraic Boolean condition consisting of one quadratic inequality and affine inequalities/non-equalities.

This is the first promoted selector tier whose competitors need not be supplied as explicit root branches.

## 4. Exact one-parameter witness

For

`E_t(y)=(y+1)^2(y^2+t y+1)`,

with declared root `r=-1`, multiplicity two,

`D=t^2-4`,
`L=2-t`,
`R=2-t`.

Therefore, on fixed multiplicity `t!=2`, the smallest-real selector condition simplifies to

`t<2`.

The regimes are:

- `-2<t<2`: the quadratic competitors are complex, selector remains -1;
- `t=-2`: competing double root is +1, selector remains -1;
- `t<-2`: competing roots are positive real (usually irrational), selector remains -1;
- `t=2`: the quadratic becomes `(y+1)^2` and the declared multiplicity changes;
- `t>2`: a competing real root lies below -1, so the selector changes.

## 5. Discriminant-zero boundary

`D=0` is not by itself a selector boundary.

Examples at declared root `r=-1`:

- `Q=(y-1)^2`: `D=0`, competing double root is to the right, selector stable;
- `Q=(y+2)^2`: `D=0`, competing double root is to the left, selector unstable;
- `Q=(y+1)^2`: `D=0` and `R=0`, so declared multiplicity fails.

Therefore a discriminant-only rule is insufficient; the order data L and R are essential.

## 6. Relation to T59–T61

```text
T59 DECLARED SCHEDULE VALIDITY
    -> root/multiplicity/scale algebraically valid

T60/T61 COMPLETE SPLIT-AFFINE ROOT INVENTORY
    -> selector stability by affine root-order conditions

T62 MONIC QUADRATIC NON-SPLIT COFACTOR
    -> smallest-real selector stability from D,L,R without root splitting
```

T62 is a direct non-split extension of T60, not a replacement for T59 multiplicity validity.

## 7. Hard negative/scope boundaries

```text
MONIC_QUADRATIC_COFACTOR_ONLY
SMALLEST_REAL_ONLY
FIXED_MULTIPLICITY_REQUIRES_R_NOT_ZERO
D_ZERO != AUTOMATIC_SELECTOR_CHANGE
NO_ROOT_MATERIALIZATION_REQUIRED != GENERAL_FACTORING_ALGORITHM
QUADRATIC_CLOSED_FORM != GENERAL_PARAMETRIC_STURM_CHAMBER
AFFINE_COEFFICIENT_FAMILY != ARBITRARY_NONLINEAR_PARAMETERIZATION
T62 != COMPLETE_PUISEUX_OR_MULTIGENERATOR_SOLVER
```

Canonical negative IDs: `WBRC-N76..N83`.

## 8. Tool routing

No new top-level family is created. The companion subtool is

`t0.weighted_brc_newton_quadratic_selector`.

Production code provides:

- exact quadratic selector state `(a,b,r,D,L,R)`;
- fixed-multiplicity decision `R!=0`;
- exact smallest-real selector predicate;
- rational-affine quadratic selector-family evaluation;
- exact semi-algebraic chamber truth at rational parameter points;
- the algebraic identity `L^2-D=4R` as a checked invariant.

It does not compute or return the competing quadratic roots.

## 9. Validation

Main-backed PR #1208 verified:

- 405 rational `(a,b,r)` catalog points;
- 31 fixed-multiplicity collision points;
- 374 exact Sturm selector checks against the closed formula;
- 405 exact `L^2-D=4R` identity checks;
- 130 negative-discriminant points;
- both stable and unstable discriminant-zero cases (6 each);
- 232 positive-discriminant points, including 165 with irrational real competitors;
- a 33-point one-parameter witness with 24 stable, one collision and eight unstable points;
- 15 complex-competitor points and seven irrational-real stable witness points;
- exact affine-parameter regressions.

## 10. Next frontier

The next low-degree extension is the smallest-positive selector for a monic quadratic cofactor, using exact Sturm sign variation on `(0,r)`.  The higher-degree frontier remains a fixed symbolic Sturm/subresultant sign chamber rather than a generic CAD engine.
