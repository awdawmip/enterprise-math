# Legacy R061 arbitrary-point directed min-zero gauge — centered-X6 retyping

Status: `RETYPED / RELATIVE-OBSERVER GAUGE ONLY / SUPERSEDED AS NATIVE POINT-TO-POINT LENGTH`
Original date: `2026-08-21`
Retyped: `2026-09-05`
Steward: `EM-STW-C31A7F / FOUNDATION_STEWARD`

Current native three-axis authority is:

`ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`.

The original construction decoded every carrier displacement to a unique nonnegative min-zero triple and then applied a sum-of-squares directed gauge. That decoder remains mathematically valid as a **relative/carrier observer section**, but it is no longer the native signed displacement in the centered X6 slice.

## Current native point-to-point displacement

For native Cells `P,Q` in one centered selected slice, use raw signed coordinates

`x(P),x(Q) in Z^3`

and exact displacement

`d(P,Q)=x(Q)-x(P)`.

Native squared distance is

`d_S(P,Q)^2=sum_i d_i(P,Q)^2`.

Therefore

`d(P,Q)=-d(Q,P)`

and

`d_S(P,Q)=d_S(Q,P)`.

Freeze:

`CENTERED_SIGNED_DISPLACEMENT = RAW_COORDINATE_DIFFERENCE`.

`NATIVE_POINT_TO_POINT_DISTANCE_IS_SYMMETRIC = TRUE`.

`NO_MIN_ZERO_DECODE_REQUIRED_FOR_NATIVE_POINT_TO_POINT_DISTANCE`.

## Historical min-zero decoder survives as observer

For any raw signed triple `d`, define

`can3(d)=d-min(d)*(1,1,1)`.

This is the canonical section of the carrier quotient `Z^3/Z(1,1,1)`. It forgets the common depth and therefore cannot by itself carry native point-to-point length.

The old directed gauge

`ell_rel(d)^2=sum_i can3(d)_i^2`

is retained only as a **positive/min-zero relative observer gauge**.

Freeze:

`LEGACY_DIRECTED_GAUGE = RELATIVE_OBSERVER_GAUGE`.

`LEGACY_DIRECTED_GAUGE != NATIVE_SIGNED_DISTANCE`.

## Recomputed reversal witnesses

### Unit step

Native:

`d=(1,0,0)`, `L_E^2=1`;

`-d=(-1,0,0)`, `L_E^2=1`.

Historical min-zero reverse observer:

`can3(-1,0,0)=(0,1,1)` with component-square sum `2`.

Thus the old `{1,sqrt(2)}` reversal spectrum is an observer artifact.

### 3-4-5 displacement

Native:

`d=(3,4,0)`, `L_E^2=25`;

`-d=(-3,-4,0)`, `L_E^2=25`.

Historical min-zero reverse observer:

`can3(-3,-4,0)=(1,0,4)` with component-square sum `17`.

Thus the old `5` versus `sqrt(17)` asymmetry is not a native signed metric asymmetry.

## Repaired min-zero coordinates

For a point coordinate `x`, the lossless pair is

`r=can3(x)`, `h=min(x)`,

with `x=r+h*(1,1,1)`.

For `P<->(r,h)` and `Q<->(s,k)`, native squared distance is

`sum_i (s_i-r_i+(k-h))^2`.

This is the exact repair missing from the historical observer-only gauge.

## BRC consequence

Raw signed reversal preserves the shortest-path multiplicity

`B_min(d)=(sum |d_i|)!/product |d_i|!`.

Hence `(3,4,0)` and `(-3,-4,0)` both have 35 shortest native path words. The historical observer triple `(1,0,4)` has 5 positive words, but it is not the native reverse displacement.

Freeze:

`LEGACY_REVERSAL_ASYMMETRY = MIN_ZERO_OBSERVER_EFFECT`.

`SIGNED_NATIVE_REVERSAL_PRESERVES_LENGTH_AND_BRC_MULTIPLICITY`.

The full original R061 Stage-2 text remains in Git history as provenance.
