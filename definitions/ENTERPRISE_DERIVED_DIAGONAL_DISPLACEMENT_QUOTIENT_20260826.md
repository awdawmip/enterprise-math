# Legacy G1 diagonal displacement quotient — centered-X6 retyping

Status: `ACTIVE AS CARRIER/RELATIVE QUOTIENT / SUPERSEDED AS NATIVE DISPLACEMENT`
Original date: `2026-08-26`
Retyped: `2026-09-05`
Steward: `EM-STW-C31A7F / FOUNDATION_STEWARD`

Current centered slice authority is:

`ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`.

## 1. Exact quotient retained

The algebraic map

`chi: Z^3 -> Z^2`,

`chi(a,b,c)=(a-c,b-c)`

still has exact kernel

`Z*(1,1,1)`.

Therefore

`G_REL3 := Z^3/Z(1,1,1) ~= Z^2`

is retained exactly.

What changes is its type: it is now the **relative/FCC STAR-slice carrier endpoint quotient**, not the native signed point-to-point displacement carrier.

Freeze:

`G_REL3 = THREE_AXIS_RELATIVE/CARRIER_ENDPOINT_QUOTIENT`.

`G_REL3 != NATIVE_SIGNED_SLICE_DISPLACEMENT`.

Native signed slice displacement is the raw difference `d in Z^3`.

## 2. Min-zero section and repair

`can3(z)=z-min(z)*(1,1,1)`

remains the unique nonnegative min-zero section of `G_REL3`.

The missing coordinate is the common depth

`h=min(z)`.

Lossless reconstruction is

`z=can3(z)+h*(1,1,1)`.

Freeze:

`MIN_ZERO_SECTION = RELATIVE/CARRIER REPRESENTATIVE`.

`MIN_ZERO_SECTION_ALONE != NATIVE_CELL_OR_DISPLACEMENT_IDENTITY`.

`MIN_ZERO_SECTION + COMMON_DEPTH = LOSSLESS_RAW_Z3`.

The historical symbol `A_D` may be retained as a compatibility alias for the section object, but it has no authority to replace raw signed native displacement.

## 3. Composition

The quotient addition

`[x]+[y]=[x+y]`

and canonical representative operation

`can3(can3(x)+can3(y))`

remain exact at relative/carrier strength.

However, native centered-slice displacement composition is simply raw signed addition in `Z^3` before any quotient.

Freeze:

`NATIVE_DISPLACEMENT_COMPOSITION = Z3_ADDITION`.

`RELATIVE_QUOTIENT_COMPOSITION = DOWNSTREAM_PROJECTION_OF_NATIVE_ADDITION`.

## 4. Reversal

Native reversal is

`d -> -d`.

The quotient inverse is

`[d] -> [-d]`

and its min-zero representative is `can3(-d)`.

These must not be conflated.

Witness:

`d=(3,4,0)` has native reverse `(-3,-4,0)` with squared native length `25` and shortest BRC multiplicity `35`.

Its relative min-zero inverse representative is `(1,0,4)`, whose component-square observer value is `17` and whose positive-word count is `5`.

Freeze:

`CAN3_MINUS_D = QUOTIENT_INVERSE_REPRESENTATIVE_NOT_NATIVE_REVERSE_COORDINATE`.

## 5. Carrier meaning

For an established FCC STAR slice with equal unit carrier vectors `u_i,u_j,u_k` satisfying

`u_i+u_j+u_k=0`,

`G_REL3` is exactly the carrier-center coordinate quotient. The raw common-depth displacement `(1,1,1)` is invisible to this carrier center readout.

Thus:

`CARRIER_TRIANGLE_RETURN = ZERO_IN_G_REL3`

while

`(1,1,1) != 0_IN_NATIVE_Z3`.

This is an explicit observer-information-loss witness.

## 6. Metric boundary

The diagonal-invariant classical carrier quadratic

`Q_car(a,b,c)=a^2+b^2+c^2-ab-bc-ca`

factors through `G_REL3` and remains a carrier Euclidean metric.

Native signed slice squared distance

`L_E(d)^2=a^2+b^2+c^2`

does not factor through `G_REL3` without common-depth repair.

Freeze:

`QUOTIENT_STRUCTURE != NATIVE_LENGTH_CHOICE`.

`CARRIER_Q != NATIVE_ENTERPRISE_METRIC`.

## 7. BRC/path boundary

Endpoint quotienting does not collapse Path-formal provenance or N-BRC multiplicity. Apply signed native path/BRC analysis before discarding common depth whenever future operations depend on native endpoint, reversal, length, multiplicity or provenance.

Freeze:

`RAW_SIGNED_NATIVE_ENDPOINT -> OPTIONAL G_REL3`.

`G_REL3_ENDPOINT_EQUALITY != NATIVE_ENDPOINT_EQUALITY`.

`G_REL3_ENDPOINT_EQUALITY != PATH_EQUALITY`.

The detailed original G1 integration remains in Git history as provenance.
