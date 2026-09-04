# BRC split-affine root-selector chambers

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T59

## 1. Problem

WBRC-T59 certifies when a finite declared rational-root Newton schedule is algebraically valid in a rational-affine parameter family.  It deliberately does not prove that a global root-selector rule continues to choose the same root among all roots.

The fully general parametric selector problem can require Sturm/subresultant sign chambers and is a separate algebraic task.  There is, however, an exact and reusable intermediate case:

> the real roots of the relevant Newton edge are supplied by a complete split certificate consisting of one fixed declared rational root and finitely many rational-affine real-root branches.

In this case selector stability is pure affine order geometry.

## 2. Complete split-affine real-root certificate

Let `lambda=(lambda_1,...,lambda_d)` be rational parameters.  Fix a declared rational root `r in Q` with declared multiplicity `m>=1`.

Assume an exact complete real-root factorization

`E(y;lambda) = c(lambda) (y-r)^m product_j (y-h_j(lambda))^(m_j)`

where:

- every `h_j(lambda)` is a rational affine form;
- every multiplicity `m_j` is a positive integer;
- `c(lambda)` is nonzero on the parameter set under discussion;
- the displayed factors account for the complete polynomial degree, so there are no hidden roots;
- the fixed-multiplicity schedule stratum excludes `h_j(lambda)=r` for every j.

The coefficient family need not itself remain affine after multiplying several moving factors.  The split certificate is an additional typed representation, not a replacement for the T59 affine-coefficient representation.

## 3. Smallest-real selector chamber

Within the fixed-multiplicity stratum, the declared root r is the smallest real root exactly when

`h_j(lambda) > r`

for every j.

Hence the selector-stable set is an intersection of strict rational affine half-spaces.

The selector can change only on a root-order collision hyperplane

`h_j(lambda)=r`.

For a single moving branch `h(lambda)=t`, the family

`E_t(y)=(y+1)^2(y-t)`

has declared root `r=-1` of multiplicity two for `t!=-1`, and `-1` is the smallest real root exactly when

`t>-1`.

At `t=-1` the multiplicity changes to three; for `t<-1` the selector changes to t.

## 4. Smallest-positive selector chamber

Assume the declared root satisfies `r>0`.  Within the fixed-multiplicity stratum, r is the smallest **positive** real root exactly when every other affine branch satisfies

`h_j(lambda) <= 0  OR  h_j(lambda) > r`.

Thus the selector-stable set is a finite Boolean combination of rational affine order inequalities.  It need not be connected or convex.

For

`F_t(y)=(y-1)^2(y-t)`

with declared root `r=1` of multiplicity two for `t!=1`, the smallest-positive selector chooses 1 exactly when

`t<=0  OR  t>1`.

For `0<t<1` it chooses t.  At `t=1` the declared multiplicity changes.  The point `t=0` is allowed: zero is not a positive root, so the smallest positive root remains 1.

## 5. Multi-parameter chambers

For the complete split family

`E_(u,v)(y)=(y+1)^2(y-u)(y-v)`,

the fixed root `-1` is the smallest real root exactly on

`u>-1 AND v>-1`,

excluding the collision lines `u=-1` and `v=-1` from the fixed-multiplicity stratum.

For

`F_(u,v)(y)=(y-1)^2(y-u)(y-v)`,

the fixed root 1 is the smallest positive root exactly when

`(u<=0 OR u>1) AND (v<=0 OR v>1)`,

again with the collision lines `u=1`, `v=1` excluded from the fixed-multiplicity stratum.

This gives a disconnected selector-stable set even though every root branch is affine.

## 6. Relation to T59

T59 provides an exact constructible set on which the declared Newton root, multiplicity and scale are algebraically valid.

If, on that set, one can additionally provide a complete split-affine real-root certificate for the relevant edge, then intersecting the T59 validity set with the order conditions above upgrades declared-root validity to actual selector stability for either:

- `SMALLEST_REAL_ROOT`; or
- `SMALLEST_POSITIVE_REAL_ROOT`.

This closes the T59 selector gap only for the split-affine certificate class.

## 7. Exact verification interface

A certificate checker needs only:

1. the declared fixed rational root r and multiplicity m;
2. a finite list of affine root branches h_j and multiplicities m_j;
3. exact verification that the factorization degree is complete at the representation level;
4. exact noncollision tests h_j(lambda)!=r at the parameter point or region;
5. exact affine comparisons against r and, for the positive selector, against zero.

No floating root computation is needed.

At individual rational parameter points, the factorized polynomial can also be materialized exactly and its distinct real-root count checked by the existing rational Sturm machinery as a regression against hidden-root mistakes.

## 8. Hard boundaries

- COMPLETE_SPLIT_AFFINE_CERTIFICATE is required; T59 alone does not imply it.
- SPLIT_SELECTOR_CHAMBER != GENERAL PARAMETRIC STURM/SUBRESULTANT CHAMBER.
- SELECTOR_VALUE_STABILITY != MULTIPLICITY_STABILITY at collision hyperplanes; T59 schedule validity must still be intersected.
- SMALLEST_REAL and SMALLEST_POSITIVE are distinct selector semantics.
- ZERO_ROOT is not a positive root.
- AFFINE_ROOT_BRANCHES != AFFINE_POLYNOMIAL_COEFFICIENTS when several moving factors are multiplied.
- No complete Puiseux solver, multi-generator algebraic coefficient field, signed branch interference or infinite-state claim is made.

## 9. Next frontier

After this split certificate class, the next genuinely new selector problem is a non-split rational-affine edge family.  There the natural exact route is a parametric Sturm/subresultant sign chamber: root counts and root order remain constant while the relevant signed subresultant/endpoint-evaluation data avoid zero.
