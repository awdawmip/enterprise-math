# Legacy R061 bidirectional segment spectrum — centered-X6 retyping

Status: `RETYPED / OBSERVER-DIAGNOSTIC ONLY / SUPERSEDED AS NATIVE LENGTH REPAIR`
Original date: `2026-08-21`
Retyped: `2026-09-05`
Steward: `EM-STW-C31A7F / FOUNDATION_STEWARD`

Current native three-axis authority is:

`ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md`.

The original bidirectional spectrum was introduced because the historical positive/min-zero directed gauge assigned different scalar values to opposite orientations. Under the signed centered X6 slice, that asymmetry is not native.

For native Cells `P,Q` in one selected slice:

`d(P,Q)=x(Q)-x(P) in Z^3`,

`d(Q,P)=-d(P,Q)`,

and

`L_E(P,Q)^2=sum_i d_i^2=L_E(Q,P)^2`.

Therefore the native orientation-free scalar distance is already canonical at this layer.

Freeze:

`NATIVE_SIGNED_SLICE_DISTANCE_IS_REVERSAL_SYMMETRIC=true`.

`BIDIRECTIONAL_LENGTH_SPECTRUM_NOT_REQUIRED_TO_REPAIR_NATIVE_METRIC=true`.

The historical object

`SPEC_rel(P,Q)=multiset{ell_rel(P->Q),ell_rel(Q->P)}`

may still be used as a diagnostic of the **relative/min-zero observer**, where `ell_rel` is explicitly typed as the legacy observer gauge.

Recomputed witnesses:

- native unit segment: orientation-free length is `1`; historical observer spectrum `{1,sqrt(2)}` is not native;
- native raw `(3,4,0)` segment: orientation-free length is `5`; historical observer spectrum `{5,sqrt(17)}` is not native.

Path orientation and provenance still matter: the reversed path witness is a distinct oriented path object. Symmetry of scalar native distance does not collapse Path-formal/BRC provenance.

Freeze:

`SCALAR_DISTANCE_REVERSAL_SYMMETRY != PATH_PROVENANCE_COLLAPSE`.

`LEGACY_BIDIRECTIONAL_SPECTRUM = RELATIVE_OBSERVER_DIAGNOSTIC`.

The full original R061 Stage-3 text remains in Git history as provenance.
