# BRC non-split monic-cubic smallest-positive selector via specialized Sturm variation

Date: 2026-09-04
Mode: TASK_RESEARCH
Status: research candidate; no Foundation promotion in this note
Parent: WBRC-T59/T63; main-backed cubic smallest-real research PR #1212

## 1. Problem

The quadratic non-split selector tier T62/T63 shows that selector stability is fundamentally an interval-root-count observable, not a root-materialization problem.  The next fixed-degree case is one monic cubic competing cofactor.

Fix a declared rational Newton root

`r>0`

with declared multiplicity m, and let

`P(x)=x^3+a x^2+b x+c`,

with rational coefficients.  Assume the fixed-multiplicity guard

`P(r)!=0`.

Then r is the smallest positive root of `(x-r)^m P(x)` iff P has no distinct real root in the open interval `(0,r)`.

The goal is an exact degree-three Sturm observer that never materializes cubic roots.

## 2. Specialized monic-cubic Sturm invariants

Define

`A=a^2-3b`,
`B=a b-9c`,

and the cubic discriminant

`Delta=a^2 b^2 -4b^3 -4a^3 c -27c^2 +18abc`.

The derivative is

`P'(x)=3x^2+2a x+b`.

Polynomial division gives

`-rem(P,P')=(2A x+B)/9`.

Thus, after multiplying by the positive scalar 9, a Sturm-equivalent third polynomial is

`S2(x)=2A x+B`.

When `A!=0`, dividing P' by S2 gives

`-rem(P',S2)=9 Delta/(4A^2)`.

Hence after another positive rescaling, the final Sturm polynomial is simply

`S3=Delta`.

The exact identity behind this reduction is

`4aAB -4bA^2 -3B^2 = 9 Delta`.

Therefore the finite sign sequence is:

- if `A!=0`: `P, P', 2Ax+B, Delta`;
- if `A=0` and `B!=0`: `P, P', B`;
- if `A=0` and `B=0`: `P, P'`.

At every finite endpoint that is not a root of P, ordinary sign variation after deleting zeros is the exact Sturm variation.

## 3. Zero-root deflation is mandatory for smallest-positive semantics

The left endpoint is x=0.  If

`c=P(0)=0`,

then zero is a competing root but it is not positive and must not be counted.

For a simple zero root, merely deleting the first zero Sturm value happens to give the right-hand variation.  For a multiple zero root several consecutive Sturm polynomials may vanish at zero, so that shortcut is not generally valid.

The exact rule is:

> remove the full factor `x^nu` from P before counting roots in `(0,r)`.

For a monic cubic this reduces to:

- `c!=0`: keep the cubic;
- `c=0, b!=0`: divide by x and count roots of `x^2+a x+b`;
- `c=b=0, a!=0`: divide by `x^2` and count the root of `x+a`;
- `a=b=c=0`: P=`x^3`, so there is no positive competing root.

This is an exact semantic deflation, not a numerical perturbation.

## 4. WBRC-T65 candidate — cubic smallest-positive interval observer

Let `P_+(x)` denote P after full zero-root deflation.  Then, on the fixed-multiplicity stratum `P(r)!=0`,

`r is the smallest positive root`

iff

`N_(0,r)(P_+)=0`.

For a genuine cubic (`c!=0`), define

`V_3(x)=V(P(x), P'(x), 2A x+B, Delta)` when `A!=0`,

with the degenerate A/B truncations above and V deleting zero terms.

Then

`N_(0,r)(P)=V_3(0)-V_3(r)`.

For a deflated quadratic, use the T63 degree-two variation

`V_2(x)=V(Q(x),Q'(x),D_2)`.

For a deflated linear polynomial, use

`V_1(x)=V(L(x),1)`.

Thus the complete cubic-cofactor positive selector is a finite exact degree-dispatch Sturm observer.  No cubic or quadratic competing root is materialized.

## 5. Relation to main-backed cubic smallest-real research

The concurrent cubic smallest-real result uses a tighter closed criterion in terms of the cubic discriminant and derivatives at the declared root.  T65 is not intended to replace that criterion.

Its value is different:

- it handles the open positive interval `(0,r)` directly;
- it handles zero-root endpoint semantics by exact deflation;
- it exposes the specialized cubic Sturm sequence that can serve as the bridge to higher fixed degree.

The same specialized cubic variation can independently reproduce the smallest-real root count by comparing variation at `-infinity` and at r.

## 6. Exact validation plan

The dedicated checker must:

1. exhaust a rational cubic coefficient catalog `a,b,c` and positive rational roots r;
2. classify `P(r)=0` multiplicity collisions separately;
3. verify the algebraic identities for A/B/Delta and the specialized Sturm remainders;
4. compute the specialized cubic/deflated quadratic/linear open-interval count;
5. independently deflate the zero factor and compare against the repository's generic exact rational Sturm `_root_count` on `(0,r)`;
6. compare the same specialized cubic sequence with generic Sturm variation at rational endpoints for `c!=0`;
7. record `A=0`, `B=0`, `Delta=0`, `c=0`, repeated-root and irreducible/irrational-root cases;
8. include at least one one-parameter witness with a selector transition through the positive interval.

## 7. Hard boundaries

- MONIC_CUBIC_COFACTOR_ONLY.
- SMALLEST_POSITIVE interval semantics only in this theorem.
- ZERO_ROOT_IS_NOT_POSITIVE and must be exactly deflated when it is an endpoint factor.
- FIXED_MULTIPLICITY requires `P(r)!=0`.
- SPECIALIZED_CUBIC_STURM != GENERIC PARAMETRIC STURM/SUBRESULTANT CAD.
- DEGREE_DISPATCH_AFTER_ZERO_DEFLATION is part of the exact carrier.
- No cubic-root materialization is required.
- No complete Puiseux solver, generic multi-generator algebraic field, signed branch interference or infinite-state claim is made.

## 8. Next frontier

If this degree-three interval observer is stable, the next useful step is to unify the main-backed cubic smallest-real criterion and the T65 smallest-positive interval count into one `t0.weighted_brc_newton_cubic_selector` tool.  Only after that should a higher-degree symbolic subresultant sign-chamber mechanism be considered.
