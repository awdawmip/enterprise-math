# X6 determinant-41 exact minimum: the p=13 centered shape recurs at a second prime

Status: `RESEARCH_NOTE / DURABLE FRONTIER / NONCANONICAL / NOT_FOUNDATION / NOT_WORKING_TRUTH`
Date: `2026-09-08`
Scope: `Enterprise Math / P000 X6 / centered metric-shape recurrence / prime-index geometry`
Parents:
- `research_notes/x6_gram_common_depth_shape_quotient_determinant_curves_20260908.md`
- `research_notes/x6_p13_exact_minimum_saturated_ternary_self_gluing_20260908.md`
Exact finite certificate:
- `research_notes/certificates/x6_p41_shape_recurrence_exact_certificate_20260908.cpp@9e5c10b939a2be2278f9f1e3a020a97dfcdd7f7b`
EM source snapshot before theorem write: `awdawmip/enterprise-math@9e5c10b939a2be2278f9f1e3a020a97dfcdd7f7b`

## 0. Theorem

For every integer full-rank transport

`A in M_6(Z)`

with

`|det A|=41`,

let

`G=A^T A`

and

`Delta_6(A)=6 tr(G^2)-tr(G)^2`.

Then

`boxed: Delta_6(A)>=56`.

The bound is sharp. Therefore

`boxed: min_{|det A|=41} Delta_6(A)=56`.

The equality state is not an independently guessed p=41 geometry. It is the exact common-scale translate of the previously proved p=13 minimizer:

`G_41=G_13+I_6`.

Thus p=13 and p=41 are two distinct prime hits of the **same centered metric shape**.

This is the first exact cross-prime recurrence predicted by the Gram common-depth quotient before the new prime optimization is performed.

## 1. The p=13 centered shape

The exact p=13 equality Gram is

`G_13=H_13 direct_sum H_13`,

where

`H_13=[[2,-1,0],[-1,3,-1],[0,-1,3]]`,

`det H_13=13`.

Its defect is

`Delta_6(G_13)=56`.

The centered-shape theorem gives

`Delta_6(G_13+kI)=56`

for every integer k.

The rank-three determinant polynomial is

`q(k)=det(H_13+kI)`

`=k^3+8k^2+19k+13`.

Hence the doubled six-dimensional Gram has

`det[(H_13+kI) direct_sum (H_13+kI)] = q(k)^2`.

At

`k=1`,

`q(1)=41`.

Therefore the shape quotient predicts an abstract determinant-`41^2` state at the same defect 56.

## 2. Exact X6 lift

The predicted state is not merely an abstract Gram. Take

`A_41=`

`[[ 1,-1, 1,-1, 0, 0],`

` [ 1, 0,-1, 0, 1,-1],`

` [ 1, 0, 0, 1,-1, 1],`

` [ 0,-1,-1, 0,-1, 0],`

` [ 0,-1, 0, 0, 1, 1],`

` [ 0,-1, 1, 1, 0,-1]]`.

Then exactly

`|det A_41|=41`

and

`A_41^T A_41=(H_13+I_3) direct_sum (H_13+I_3)`.

Thus

`det(A_41^T A_41)=41^2`

and

`Delta_6(A_41)=56`.

So

`delta_min(41)<=56`.

## 3. Exact lower bound below 56

Assume an integral Gram matrix of determinant

`41^2=1681`

has

`Delta_6<56`.

Writing

`Delta_6=D+12M`,

we have `M<=4`, and the diagonal range is at most4.

If every diagonal is at least4, write

`G=4I+E+R`

with E zero diagonal and R diagonal nonnegative. The exact certificate enumerates every E with `M<=4` and finds

`min det(4I+E)=2960`.

The same trace-square estimate used in the prior sparse proofs makes the base family positive definite, so adding R can only increase determinant.

Since

`2960>1681`,

any determinant-1681 candidate below56 must have minimum diagonal `1,2,or3`.

The exact result-specific certificate checks the complete remaining window:

`323,337`

symmetric integer matrices.

It finds

`boxed: zero determinant-1681 candidates with Delta_6<56`.

Hence

`delta_min(41)>=56`.

Combined with the explicit lift:

`boxed: delta_min(41)=56`.

## 4. Exact recurrence of centered shape

Define

`C(G)=6G-tr(G)I`.

Because

`G_41=G_13+I`,

we have exactly

`C(G_41)=C(G_13)`.

Therefore the p=13 and p=41 equality states are identical in the centered metric-shape quotient and differ only by one unit of metric common depth.

Their arithmetic indices are different because the determinant polynomial reacts nonlinearly to that common-depth shift.

Thus:

`SAME CENTERED SHAPE + DIFFERENT COMMON DEPTH -> DIFFERENT PRIME INDEX`.

This is a direct exact realization of the general determinant-curve reduction.

## 5. Arithmetic curve interpretation

For this shape,

`p=q(k)=k^3+8k^2+19k+13`

whenever the doubled Gram determinant is `p^2`.

The first values are

`13,41,91,169,281,433,631,881,...`.

Some are prime, some composite.

The geometry therefore does not assign a separate shape independently to each arithmetic integer. One metric shape can intersect the arithmetic index axis at many values, and primality is an additional arithmetic observer on those determinant-polynomial values.

No claim is made that q(k) assumes infinitely many prime values.

## 6. Discriminant/gluing boundary

The doubled ternary blocks have the same discriminant phase. At a prime value p of q(k), same-phase self-gluing requires the relevant discriminant form to contain an isotropic line; in the cyclic equal-phase normalization this includes the familiar condition that `-1` be a square when the coefficients coincide.

Both

`13` and `41`

are `1 mod4`, and explicit X6 lifts have been constructed.

A future prime value of q(k) cannot be declared an X6 state from the determinant polynomial alone; the discriminant/ambient-lift test remains mandatory.

## 7. Consequence for the prime atlas

The exact atlas is no longer merely an ordered list of unrelated local minima.

At least one edge now exists between distinct primes:

`13 --same centered metric shape / +1 common depth--> 41`.

Both have exact minimum

`56`.

This is qualitatively different from coincidental equality of scalar minima: their full centered Gram repair coordinate is the same.

Therefore the correct organization of prime geometry should include **shape recurrence classes** in addition to prime order and congruence classes.

## 8. BRC / operation-safe audit

`T0_BRC`: `REUSE_APPLIED`.

- p=13 and p=41 arithmetic identities remain distinct even though the centered shape is equal;
- common depth and ambient-lift data are retained.

`T6_OPERATION_SAFE_QUOTIENT`: `REUSE_APPLIED`.

- `G -> C(G)` is safe for Delta but not sufficient for determinant/index or future multiplication;
- the common-depth repair is essential to recover the arithmetic determinant.

`T9_HOLONOMY_COCOYCLE_GLUING`: `COMPOSE_APPLIED`.

- determinant-curve hits are filtered by native gluing/lift state.

The p=41 C++ certificate is `RESULT_ONLY`.

## 9. Status ledger

Exact proved:

- `min_{|det A|=41} Delta_6(A)=56`;
- explicit determinant-41 equality transport;
- equality Gram is exactly `G_13+I_6`;
- p=13 and p=41 have the same centered metric shape;
- exact lower-window certificate excludes every smaller-defect determinant-41 state.

Still open:

- further prime hits of the same cubic determinant polynomial;
- whether every successful prime hit of a repeated-block determinant curve yields the same global minimum or only a bounded upper state;
- classification of all centered shapes at defect 56 and their determinant curves;
- a global shape-curve lower-envelope theorem.

## 10. Next frontier

The next non-blind task is:

**Enumerate centered shape classes by defect level rather than primes.**

Start with the exact levels already observed:

`Delta=8,32,48,56,68,72,77`.

For each centered shape orbit:

1. build its determinant polynomial;
2. determine whether it is generic genus-two or degenerate/repeated-spectrum;
3. find prime-square hits;
4. apply discriminant/ambient-lift admissibility;
5. compare with the exact prime-minimum atlas.

The p=13 -> p=41 recurrence is the first calibration point that such a shape-first program must reproduce automatically.
