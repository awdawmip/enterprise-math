# Legacy R061 component-trace line formula — centered-X6 retyping

Status: `RETYPED / POSITIVE-PATH COMBINATORICS RETAINED / NOT CURRENT PRIMITIVE-LINE AUTHORITY`
Original date: `2026-08-21`
Retyped: `2026-09-05`
Steward: `EM-STW-C31A7F / FOUNDATION_STEWARD`

Current native three-axis authority is:

`ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`.

The original R061 construction at this path assumed a non-Cell triple-boundary origin, three positive native generators only, and support-two component traces as native line identities. Those assumptions are no longer current native geometry after P000 V5 + signed X6 unification.

## Current native line gate

For raw signed slice displacement

`d=(d_i,d_j,d_k) in Z^3`,

`PRIMITIVE_STRAIGHT_SEGMENT <=> support_size(d)=1`.

A support-two displacement such as `(3,4,0)` is therefore a **composite native displacement/path family**, not a new primitive straight direction.

Native squared length is

`L_E(d)^2=d_i^2+d_j^2+d_k^2`.

Signed reversal is `d -> -d` and preserves length.

## Exact R061 combinatorics that survive

For a raw positive support-two displacement `(a,b,0)` with `a,b>=0`, shortest native words using the two selected positive generators are still exactly the shuffles of `a` copies of one generator and `b` copies of the other:

`B_min(a,b,0)=binom(a+b,a)`.

Thus:

- `(1,1,0)` has 2 shortest positive path words;
- `(3,4,0)` has 35;
- `(4,3,0)` has 35;
- `(5,0,0)` and `(0,5,0)` each have 1.

The historical fixed-positive-sector `N=25` subtotal

`1+35+35+1=72`

is retained exactly as that **positive-sector subset**.

The complete signed three-axis squared-length-25 shell is instead:

- 30 raw displacement endpoints;
- 6 support-one primitive endpoints;
- 24 support-two composite endpoints;
- 846 total shortest native path words.

## Origin/incidence correction

A native path now begins at an actual Cell anchor. The historical type-changing start incidence

`Sigma_O : triple-boundary origin -> first circle Cell`

is not part of current native path algebra.

Triple circle-boundary points survive as carrier incidence vertices `V_E` only.

Freeze:

`NATIVE_PATH_START = NATIVE_CELL`.

`NO_SPECIAL_NONCELL_ORIGIN_INCIDENCE_STEP`.

`LEGACY_SUPPORT_TWO_LINE_TRACE = COMPOSITE_NATIVE_DISPLACEMENT_TRACE`.

`LEGACY_SHUFFLE_COUNTS = RETAINED_FOR_MATCHING_RAW_POSITIVE_DISPLACEMENTS`.

`LEGACY_N25_72 = POSITIVE_SECTOR_SUBSET_NOT_FULL_SIGNED_SHELL`.

## BRC typing

The richer current shortest-path count is the signed X6 restriction

`B_min(d)=(sum |d_i|)! / product |d_i|!`.

Path-formal provenance remains richer than N-BRC multiplicity, which remains richer than Boolean reachability.

The full original R061 text remains in Git history as provenance.
