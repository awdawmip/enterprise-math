# R062 BRC × multipath bridge — centered-X6 signed retyping

Status: `ACTIVE / RETYPED TO SIGNED CENTERED X6 / BOOLEAN SHADOW RETAINED`
Original date: `2026-08-21`
Retyped: `2026-09-05`
Steward: `EM-STW-C31A7F / FOUNDATION_STEWARD`

Current spatial authority:

- `ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`;
- `ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`.

The BRC enrichment hierarchy remains valid:

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

What changes is the native transition skeleton. The old bridge assumed a non-Cell triple-boundary origin and a three-positive-generator/min-zero native ontology. Current native slice state uses raw signed `Z^3` Cell coordinates.

## 1. Signed component-typed skeleton

For selected axes `S={i,j,k}`, primitive transition labels are

`+E_i,-E_i,+E_j,-E_j,+E_k,-E_k`.

A native path begins at an actual Cell `P` and is a typed word in these signed generators. Its raw endpoint displacement is

`d in Z^3`.

Freeze:

`BRC_CENTERED_SLICE_SKELETON = SIGNED_NATIVE_CELL_TO_CELL_STEPS`.

`BRC_NATIVE_PATH_START = NATIVE_CELL`.

`NO_NONCELL_ORIGIN_INCIDENCE_PREFIX`.

## 2. Enrichment hierarchy

Path-formal BRC retains concrete ordered path witnesses and provenance.

N-BRC applies occurrence augmentation and retains multiplicity.

Boolean-BRC applies support and retains only nonempty reachability on the same typed skeleton.

Freeze:

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

`BOOLEAN_SUPPORT_DOES_NOT_RECONSTRUCT_DISCARDED_MULTIPLICITY_OR_PROVENANCE`.

## 3. Exact shortest-path law

For raw signed displacement

`d=(d_i,d_j,d_k)`,

`N_min(d)=sum |d_a|`.

The exact N-BRC shortest multiplicity is

`B_min(d)=N_min(d)!/product |d_a|!`.

This is the restriction of the signed X6 BRC kernel already implemented in

`experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py`.

Positive support-two shuffles from historical R062 survive as the special case `d=(a,b,0)` with `a,b>=0`:

`B_min=binom(a+b,a)`.

Examples retained:

- `(1,1,0)`: 2 path witnesses -> N-BRC 2 -> Boolean support 1;
- `(3,4,0)`: 35 path witnesses -> N-BRC 35 -> Boolean support 1.

## 4. Reversal recomputation

The native reverse of `d` is `-d`, not `can3(-d)`.

Therefore

`B_min(-d)=B_min(d)`.

For `(3,4,0)`, both orientations have 35 shortest native witnesses.

The historical positive/min-zero reverse observer `(1,0,4)` has 5 positive shortest words, but it is a different lower-information observer representative and is not the native reverse endpoint.

Freeze:

`SIGNED_NATIVE_REVERSAL_PRESERVES_N_BRC_MULTIPLICITY`.

`LEGACY_MIN_ZERO_REVERSE_MULTIPLICITY_ASYMMETRY = OBSERVER_EFFECT`.

## 5. Carrier recoalescence does not imply native recoalescence

For the three selected positive axes let

`H_S=(1,1,1)`.

In the established triangular/FCC carrier readout,

`pi_S(H_S)=0`

because the three chart-local carrier vectors sum to zero.

In native X6,

`H_S != 0`, `L_E(H_S)^2=3`.

There are exactly

`3!=6`

shortest signed-native path words using each positive selected axis once.

Thus all six paths recoalesce at the same **native endpoint `H_S`**, while the carrier readout reports the same carrier center as the start.

Freeze:

`CARRIER_ENDPOINT_RECOALESCENCE != NATIVE_ENDPOINT_RECOALESCENCE`.

`CARRIER_TRIANGLE_RETURN = OBSERVER_RETURN_WITH_HIDDEN_COMMON_DEPTH`.

`BRC_BEFORE_CARRIER_QUOTIENT = MANDATORY_WHEN_NATIVE_ENDPOINT_OR_PROVENANCE_MATTERS`.

This is a direct Joint Relation Observer Preservation witness.

## 6. Recomputed N=25 shell

The full signed centered three-axis shell

`d_i^2+d_j^2+d_k^2=25`

contains 30 raw displacement endpoints:

- 6 signed support-one axis endpoints;
- 24 signed support-two `(3,4,0)` permutations/signs.

Total shortest N-BRC mass over the shell is

`6*1 + 24*35 = 846`.

The historical `72` count remains the subtotal for one nonnegative support-two sector list

`(0,5,0),(3,4,0),(4,3,0),(5,0,0)`.

Freeze:

`FULL_SIGNED_THREE_AXIS_N25_NBRC_TOTAL=846`.

`LEGACY_N25_72=POSITIVE_SECTOR_SUBTOTAL`.

## 7. Trace quotient versus carrier quotient versus Boolean quotient

Three distinct compressions must remain typed:

1. component/order trace quotient — may forget order while retaining declared signed component counts;
2. carrier endpoint quotient — forgets common diagonal depth in an FCC STAR slice;
3. Boolean BRC — forgets multiplicity/provenance to support.

They are not interchangeable.

Freeze:

`TRACE_QUOTIENT != CARRIER_ENDPOINT_QUOTIENT != BOOLEAN_SUPPORT_QUOTIENT`.

`RECONSTRUCTIBLE_CARRIER_ENDPOINT != NATIVE_STATE_REDUNDANCY_CERTIFICATE`.

## 8. Current bridge statement

The strongest current statement is:

`SIGNED_COMPONENT_TYPED_PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`

on the centered native slice, with any carrier/min-zero projection applied only afterward and with explicit common-depth/provenance repair when required by the declared observer and future operations.

The detailed original R062 text, replay hashes and historical positive-only skeleton remain in Git history as provenance.
