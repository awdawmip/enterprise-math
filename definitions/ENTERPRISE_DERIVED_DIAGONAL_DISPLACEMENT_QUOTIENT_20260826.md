# 进取派生对角位移商：G1 Derived Displacement Quotient

Status: `ACTIVE / DERIVED G1 / TYPED INTEGRATION / NO NEW MATHEMATICS`
Date: `2026-08-26`
Source task: `RS-DIAGONAL-GAUGE-REFOUNDATION-TYPED-INTEGRATION`
Accepted review: `driver_reviews/DIAGONAL_GAUGE_REFOUNDATION_INDEPENDENT_REVIEW_DRIVER_REVIEW_20260826.md`

## 1. Scope and type boundary

This definition integrates only the Driver-accepted derived displacement interpretation already implicit in current R061 Stage 2.

It does **not** modify primitive native point/address ontology, native line identity, Path-formal provenance, R062 BRC semantics, the current directed line gauge, or the Stage-3 bidirectional spectrum.

Freeze the semantic separation:

`A_E = CURRENT_NATIVE_POINT_OR_SECTOR_ADDRESS_TYPE`.

`A_D = MIN_ZERO_DERIVED_DISPLACEMENT_SECTION`.

Even when `A_E` and `A_D` use the same underlying set of nonnegative min-zero integer triples as representations,

`A_D != A_E`

as semantic types.

A representation-level bijection is permitted. Semantic identification is not.

## 2. Lifted displacement carrier

Use the lifted integer displacement carrier

`L_D = Z^3`.

Define

`chi : Z^3 -> Z^2`

by

`chi(a,b,c)=(a-c,b-c)`.

The accepted exact kernel is

`ker(chi)=Z(1,1,1)`.

Therefore define the derived G1 displacement quotient

`G_D := Z^3 / Z(1,1,1)`.

Equivalently,

`G_D ~= Z^2`

through the chart induced by `chi`.

This is a **derived endpoint/displacement object**. It is not a primitive native coordinate quotient and does not convert arbitrary lifted triples into additional native points.

Freeze:

`DERIVED_G1_DISPLACEMENT_QUOTIENT = G_D`.

`PRIMITIVE_NATIVE_POINT_ADDRESS_QUOTIENT = NOT_INTRODUCED`.

## 3. Canonical min-zero section

For `z=(a,b,c) in Z^3`, define

`can(z)=z-min(a,b,c)(1,1,1)`.

Then `can(z)` is nonnegative and has minimum component zero.

The accepted exact properties are:

1. `can(z+k(1,1,1))=can(z)` for every `k in Z`;
2. `can(z)=can(z')` iff `z-z' in Z(1,1,1)`;
3. every class of `G_D` has one unique nonnegative min-zero representative.

Define

`A_D := {d in N_0^3 : min(d)=0}`

**with the semantic type tag DERIVED_DISPLACEMENT_SECTION**.

The section is

`sec_D : G_D -> A_D`,

`sec_D([z])=can(z)`.

The tuple-set equality

`underlying_set(A_D)=underlying_set(A_E)`

does not imply semantic equality of the two typed objects.

Freeze:

`MIN_ZERO_DERIVED_DISPLACEMENT_SECTION = A_D`.

`A_D_A_E_TYPE_SEPARATION = REQUIRED`.

## 4. R061 Stage-2 compatibility

For current R061 signed carrier difference

`delta_I(P,Q)=(r,s) in Z^2`,

let

`m=min(r,s,0)`.

The frozen R061 decoder remains exactly

`D_E(P->Q)=(r-m,s-m,-m)`.

At the derived displacement layer this satisfies

`D_E(P->Q)=can(r,s,0)`

and

`chi(D_E(P->Q))=(r,s)`.

Thus current R061 Stage-2 decoding is compatible with the canonical section of `G_D`.

No R061 decoder formula is changed by this interpretation.

Freeze:

`R061_STAGE2_DECODE_COMPATIBLE_WITH_G_D = true`.

## 5. Derived composition and inverse

For canonical derived displacement representatives `x,y in A_D`, transport the group law of `G_D` by

`x (+)_D y = can(x+y)`.

Identity is `(0,0,0)` in `A_D`.

Derived inverse is

`(-)_D x = can(-x)`.

For `x=(A,B,C)` and `M=max(A,B,C)`,

`(-)_D x=(M-A,M-B,M-C)`.

These formulas record the accepted algebraic interpretation of the existing R061 Stage-2 composition and reversal formulas. They do not identify displacement inverse with native trace/path inversion.

Freeze:

`R061_STAGE2_COMPOSITION_COMPATIBLE_WITH_DERIVED_ADDITION = true`.

`R061_STAGE2_REVERSAL_COMPATIBLE_WITH_DERIVED_INVERSE = true`.

`DERIVED_DISPLACEMENT_INVERSE != AUTOMATIC_NATIVE_TRACE_INVERSE`.

## 6. Start/target typing

Bare `g in G_D` records displacement only. Parallel translated segments with the same displacement remain distinct when their starts differ.

The globally safe derived endpoint object is therefore a start/target-typed arrow

`(P,g): P -> P·g`.

Composition is permitted only for matching source/target objects:

`(P,g);(P·g,h)=(P,g+h)`.

This is an action-groupoid/category-level interpretation of endpoint displacement.

Freeze:

`GLOBAL_DERIVED_ENDPOINT_OBJECT = START_TARGET_TYPED_DISPLACEMENT_ARROW`.

`BARE_G_D_ELEMENT != GLOBAL_NATIVE_LINE_IDENTITY`.

## 7. Path boundary

The packet/path Foundation types native PATH endpoints as packet/cell states. Current R061 Stage-2 displacement is typed on coordinate/triple-intersection vertex endpoints.

Therefore this integration does **not** define a total map

`PF_PATH -> G_D`.

A path-to-displacement map is admitted only after one of the following supplies the required endpoint typing:

1. an R061 endpoint-anchored translated-line realization;
2. an explicitly endpoint-decorated path category;
3. a separately frozen cell-to-vertex endpoint bridge.

Without such typing, a native closed path remains a nontrivial closed path, but Stage-2 displacement is not automatically attached to it.

Freeze:

`BARE_GLOBAL_PF_PATH_DISPLACEMENT = NOT_DEFINED`.

`ENDPOINT_DECORATION_REQUIRED_FOR_PATH_TO_G_D`.

## 8. Path-formal / BRC boundary

Current R062 remains unchanged:

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

The derived displacement quotient is a separate forgetful endpoint target. It does not identify Path-formal witnesses, native line identity, or Boolean BRC support.

In particular, ordinary everywhere-defined multiplication in the group semiring

`N[G_D]`

is **not** declared to be native path composition, because it forgets source/target composability.

If coefficient pushforward is needed, the safe target is a start/target-typed action-groupoid/category algebra, basis elements `[P,g]` with composition constraints, or a later explicitly declared translation/object identification.

Freeze:

`DERIVED_DISPLACEMENT_QUOTIENT != TRACE_QUOTIENT`.

`DERIVED_DISPLACEMENT_QUOTIENT != BOOLEAN_BRC_SUPPORT_QUOTIENT`.

`UNTYPED_N_GD_PATH_MULTIPLICATION = NOT_NATIVE_PATH_COMPOSITION`.

## 9. Metric fork

The existence of `G_D` does not choose the native length functional.

The historical diagonal-invariant symmetric quadratic

`Delta(a,b,c)=a^2+b^2+c^2-ab-bc-ca`

is not restored as current native Enterprise length.

Current R061 directed line gauge remains

`ell_E(P->Q)^2=A^2+B^2+C^2`

for the frozen min-zero decoded displacement `(A,B,C)`, and current Stage-3 bidirectional spectrum remains unchanged.

Freeze:

`QUOTIENT_STRUCTURE != NATIVE_LENGTH_CHOICE`.

`HISTORICAL_DELTA_NATIVE_METRIC = NOT_RESTORED`.

`CURRENT_R061_DIRECTED_GAUGE = UNCHANGED`.

`CURRENT_STAGE3_BIDIRECTIONAL_SPECTRUM = UNCHANGED`.

## 10. Primitive native-point prohibition

The current plane Foundation prohibition is retained at its exact accepted type:

`NO_PRIMITIVE_NATIVE_POINT_DIAGONAL_SHIFT_QUOTIENT`.

For primitive native point/sector addresses, one must not identify

`(a,b,c)`

with

`(a+k,b+k,c+k)`

as two names for one native point merely from diagonal shift.

This primitive prohibition does not forbid the separately typed G1 displacement quotient defined here.

Freeze:

`PRIMITIVE_POINT_ONTOLOGY_PRESERVED`.

`DERIVED_G1_DISPLACEMENT_QUOTIENT_ALLOWED_SEPARATELY`.

## 11. Integration invariant

This definition is an interpretive/type integration only.

It changes no equation in:

- R061 Stage-2 decoder;
- R061 translated trace identity;
- R061 directed gauge;
- R061 triangle inequality;
- R061 reversal formula;
- R061 Stage-3 bidirectional spectrum;
- R062 Path-formal/N/Boolean BRC tower.

Freeze final boundary:

`DERIVED_G1_DIAGONAL_DISPLACEMENT_TYPED_INTEGRATION = TYPE_ONLY`.

`NO_NEW_MATHEMATICS`.
