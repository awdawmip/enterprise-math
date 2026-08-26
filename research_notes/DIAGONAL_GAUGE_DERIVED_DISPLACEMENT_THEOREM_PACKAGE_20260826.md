# Diagonal Gauge — Derived Displacement Theorem Package

Status: `DRIVER_HARVESTED / POST-INTEGRATION / NO_NEW_MATHEMATICS`
Date: `2026-08-26`
Source merge: `PR #651 / 6b958ec24dad0571c4a60b2e1259042feaaea0e8`
Accepted review: `driver_reviews/DIAGONAL_GAUGE_REFOUNDATION_INDEPENDENT_REVIEW_DRIVER_REVIEW_20260826.md`
Integrated definition: `definitions/ENTERPRISE_DERIVED_DIAGONAL_DISPLACEMENT_QUOTIENT_20260826.md`

## 0. Epistemic class

This package extracts only mathematics already independently accepted and merged.

Freeze:

`DGR_DERIVED_DISPLACEMENT_THEORY = G1_CURRENT_LINE_DERIVED_ENDPOINT_OBJECT`.

It is not a primitive native-point ontology, not a new native metric, and not a Path-formal quotient.

## 1. Exact quotient theorem

Define

`chi : Z^3 -> Z^2`

by

`chi(a,b,c)=(a-c,b-c)`.

Then:

1. `chi` is a surjective group homomorphism;
2. `ker(chi)=Z(1,1,1)`;
3. therefore

`G_D := Z^3 / Z(1,1,1) ~= Z^2`.

This is the exact derived displacement quotient.

## 2. Canonical section theorem

For `z=(a,b,c) in Z^3`, define

`can(z)=z-min(a,b,c)(1,1,1)`.

Then:

1. `can(z)` is nonnegative;
2. `min(can(z))=0`;
3. `can(z+k(1,1,1))=can(z)` for all `k in Z`;
4. `can(z)=can(z')` iff `z-z' in Z(1,1,1)`;
5. every class of `G_D` has exactly one nonnegative min-zero representative.

Define the typed section object

`A_D = MIN_ZERO_DERIVED_DISPLACEMENT_SECTION`.

Representation-level tuple coincidence with the primitive/current address set does not identify semantic types:

`A_D != A_E AS_SEMANTIC_TYPES`.

## 3. Transported abelian-group law

For `x,y in A_D`, define

`x (+)_D y = can(x+y)`.

Identity is `(0,0,0)`.

Define

`(-)_D x = can(-x)`.

Then `A_D` with these transported operations is a canonical representative model of the abelian group `G_D`.

For `x=(A,B,C)` min-zero and `M=max(A,B,C)`, the inverse has the exact representative formula

`(-)_D x=(M-A,M-B,M-C)`.

## 4. R061 Stage-2 compatibility theorem

For current R061 signed carrier difference

`delta_I(P,Q)=(r,s)`, let

`m=min(r,s,0)`.

The frozen decoder remains

`D_E(P->Q)=(r-m,s-m,-m)`.

Exactly:

`D_E(P->Q)=can(r,s,0)`

and

`chi(D_E(P->Q))=(r,s)`.

Thus the existing Stage-2 decoder is the canonical section of the derived quotient when interpreted at semantic type `A_D`.

Likewise, the existing R061 composition canonicalization is compatible with `(+)_D`, and the existing reverse decode is compatible with `(-)_D`.

No R061 formula is changed by these statements.

## 5. Start/target typed global object

A bare element `g in G_D` records displacement only. It does not determine a global native line because parallel translated segments with different starts may have the same displacement.

The safe global derived endpoint object is therefore typed as

`(P,g): P -> P·g`.

Composition is only for matching source/target objects:

`(P,g);(P·g,h)=(P,g+h)`.

This is an action-groupoid/category-level endpoint-displacement interpretation.

## 6. Path/BRC non-collapse theorem boundary

Current sources do not define a total bare map

`PF_PATH -> G_D`.

A path-to-displacement map requires explicit compatible endpoint typing, such as an R061 endpoint-anchored realization, endpoint decoration, or a separately frozen cell-to-vertex bridge.

Therefore:

`DERIVED_DISPLACEMENT_QUOTIENT != TRACE_QUOTIENT`.

`DERIVED_DISPLACEMENT_QUOTIENT != BOOLEAN_BRC_SUPPORT_QUOTIENT`.

Ordinary untyped multiplication in `N[G_D]` is not native Path-formal composition because it forgets source/target composability.

R062 remains

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

## 7. Metric fork theorem boundary

The quotient structure does not select a length functional.

The diagonal-invariant quadratic

`Delta(a,b,c)=a^2+b^2+c^2-ab-bc-ca`

is compatible with common diagonal-shift invariance, but it is not restored as current native Enterprise length.

Current R061 directed gauge remains

`ell_E(P->Q)^2=A^2+B^2+C^2`

for the frozen min-zero decoded displacement `(A,B,C)`.

Hence:

`QUOTIENT_STRUCTURE != NATIVE_LENGTH_CHOICE`.

`HISTORICAL_DELTA_NATIVE_METRIC = NOT_RESTORED`.

## 8. Reusable theorem interface

For any later model that explicitly declares the common-translation equivalence

`z ~ z+k(1,1,1)`

on integer triples, the algebraic quotient and canonical-section theorems above may be reused verbatim.

What cannot be reused without a separate semantic proof is the claim that a particular domain should be quotiented. Semantic admissibility remains an external typing premise.

## 9. Frozen package summary

`G_D = Z^3/Z(1,1,1) ~= Z^2`.

`can(z)=z-min(z)(1,1,1)` is the unique nonnegative min-zero section.

`A_D` is a separately typed derived displacement section and is not `A_E`.

R061 Stage-2 decode/composition/reversal are compatible with the derived quotient without changing their formulas.

Global displacement requires start/target typing.

No bare global `PF_PATH -> G_D` is accepted.

Untyped `N[G_D]` multiplication is not native path composition.

The quotient does not restore the historical diagonal-invariant quadratic as native metric.
