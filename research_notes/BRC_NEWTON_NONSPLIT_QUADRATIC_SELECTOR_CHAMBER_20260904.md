# BRC non-split monic-quadratic smallest-real selector chamber

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T59/T60

## 1. Problem

WBRC-T60 closes smallest-real selector stability when the complete real-root inventory is already split into rational-affine root branches.  The next selector problem is genuinely non-split: the competing roots may be irrational or complex and should not need to be explicitly solved.

The first exact non-split class is a monic quadratic cofactor.

## 2. Quadratic-cofactor setup

Fix a declared rational root `r in Q` of multiplicity `m>=1`.  Consider an edge polynomial represented as

`E(y;lambda) = (y-r)^m Q(y;lambda)`,

where

`Q(y;lambda)=y^2+a(lambda)y+b(lambda)`

and `a,b` are rational-affine parameter forms.

For fixed declared multiplicity require

`Q(r;lambda) != 0`.

Define

`D(lambda)=a(lambda)^2-4b(lambda)`,

`L(lambda)=-a(lambda)-2r`,

`R(lambda)=Q(r;lambda)=r^2+a(lambda)r+b(lambda)`.

D is quadratic in the parameters, while L and R are affine.

## 3. WBRC-T62 candidate — exact non-split smallest-real chamber

The declared root r is the smallest real root of E exactly when Q has no real root below r.

If `D<0`, Q has no real roots, so r is automatically the smallest real root.

If `D>=0`, the smaller quadratic root is

`x_- = (-a-sqrt(D))/2`.

Without evaluating the square root, the condition `x_->r` is equivalent to

`L>0 AND R>0`.

Proof: `x_->r` iff

`-a-2r > sqrt(D)`.

The left side must be positive.  Squaring is then order-safe, and

`L^2-D = (-a-2r)^2-(a^2-4b) = 4(r^2+ar+b)=4R`.

Therefore, on the fixed-multiplicity stratum `R!=0`,

`r is the smallest real root`

iff

`D<0 OR (L>0 AND R>0)`.

This is a genuine non-split selector chamber: no factorization or quadratic-root materialization is required.

## 4. Semi-algebraic complexity

If a and b are affine parameter forms, the chamber is a Boolean combination of:

- one quadratic inequality `D<0`;
- one affine inequality `L>0`;
- one affine inequality `R>0`;
- the fixed-multiplicity noncollision condition `R!=0`.

Thus the first non-split extension of T60 is semi-algebraic but still exact and low-degree.

The discriminant boundary `D=0` is not automatically a selector boundary.  A double competing root can be born to the right of r without changing the selected root.  Conversely, if the quadratic vertex lies to the left of r, crossing `D=0` can create a new smaller real root without any split-affine branch representation.

## 5. One-parameter non-split witness

Take

`Q_t(y)=y^2+t y+1`,

`E_t(y)=(y+1)^2 Q_t(y)`,

with declared root `r=-1` of multiplicity two.

Then

`D=t^2-4`,
`L=2-t`,
`R=2-t`.

Hence, for fixed multiplicity `t!=2`, the selector condition becomes

`t^2-4<0 OR (2-t>0)`

which simplifies exactly to

`t<2`.

The regimes are:

- `-2<t<2`: Q has no real roots, so -1 is selected;
- `t=-2`: Q=(y-1)^2, competing double root is to the right, selector unchanged;
- `t<-2`: Q has two positive real roots (usually irrational), selector unchanged;
- `t=2`: Q=(y+1)^2 collides with the declared root and changes multiplicity;
- `t>2`: Q has a real root below -1, so the selector changes.

This example includes complex competitors, repeated competitors and irrational real competitors without ever solving them.

## 6. Exact Sturm regression

At a rational parameter point, the chamber theorem can be verified independently using the existing exact rational Sturm machinery on Q:

- choose a rational Cauchy bound B beyond all roots;
- because fixed multiplicity gives Q(r)!=0, r is a valid interval endpoint;
- count roots of Q in `(-B,r)` exactly;
- the declared root r is smallest real iff this root count is zero.

The research checker exhausts a finite rational `(a,b,r)` catalog and compares this exact Sturm predicate with the closed chamber formula.

## 7. Relation to T59/T60

- T59 certifies the declared root/multiplicity/scale schedule validity.
- T60 gives selector stability when all competing real roots are explicitly split affine branches.
- The present quadratic-cofactor theorem removes that split requirement for one monic quadratic competing factor.

It is therefore the first exact non-split selector tier.

## 8. Hard boundaries

- MONIC_QUADRATIC_COFACTOR != GENERAL PARAMETRIC POLYNOMIAL.
- SMALLEST_REAL only; smallest-positive requires interval root counts on `(0,r)` and is a separate theorem.
- `R=Q(r)!=0` remains a required fixed-multiplicity condition.
- DISCRIMINANT_ZERO != AUTOMATIC SELECTOR CHANGE.
- CLOSED CHAMBER FORMULA != GENERAL PARAMETRIC STURM/SUBRESULTANT CAD.
- No floating square root is required or permitted by the exact theorem.
- No complete Puiseux solver, multi-generator algebraic field, signed branch interference or infinite-state claim is made.

## 9. Next frontier

Two natural continuations are now sharply separated:

1. derive the corresponding exact smallest-positive chamber for a monic quadratic cofactor using the explicit quadratic Sturm sign sequence on `(0,r)`;
2. generalize from degree two to a fixed symbolic Sturm/subresultant sign chamber for higher-degree non-split cofactors.
