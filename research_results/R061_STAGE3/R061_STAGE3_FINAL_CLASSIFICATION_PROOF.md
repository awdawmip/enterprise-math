# R061 Stage 3 — Final Classification Proof

Researcher-ID: `EM-R061S3-2F9622`

Hard target:

`CANONICAL_UNORIENTED_SEGMENT_STRUCTURE_AND_SYMMETRIC_METRIC_DERIVABILITY_CLASSIFIED`.

## Result

The target passes with outcome:

`CANONICAL_BIDIRECTIONAL_SEGMENT_DERIVED_BUT_SCALAR_METRIC_NONUNIQUE`.

Precisely:

1. `T(P->Q)`, `T(P->Q)^(-1)`, and `T(Q->P)` are distinct typed constructions; the latter two coincide only on the zero segment.
2. The canonical unoriented segment is the endpoint-swap orbit `BSEG_E(P,Q)={T(P->Q),T(Q->P)}`.
3. Its exact orientation-free scalar data is `SPEC_E(P,Q)=multiset{ell_f,ell_r}`.
4. The exact path realization is the orientation-tagged disjoint union of the two canonical directed path fibers.
5. Many symmetric scalar metrics can be constructed from the spectrum, including `d_max`, `d_sum`, and `d_2`.
6. No frozen native invariant selects one scalarization.
7. Nonuniqueness survives unit calibration.
8. A symmetric translation-invariant scalar cannot retain the frozen directed origin gauge in every direction; the unit-step obstruction already proves this.
9. The translated `3-4-5` obstruction remains `5` versus `sqrt(17)` and is not modified.
10. No native negative axis and no carrier vector identity is introduced.

Therefore:

`CANONICAL_UNORIENTED_SEGMENT_STRUCTURE_AND_SYMMETRIC_METRIC_DERIVABILITY_CLASSIFIED = true`.

`CANONICAL_UNORIENTED_SEGMENT_STRUCTURE = BIDIRECTIONAL_CANONICAL_TRACE_PAIR`.

`CANONICAL_ORIENTATION_FREE_LENGTH_DATA = BIDIRECTIONAL_LENGTH_SPECTRUM`.

`MULTIPLE_SYMMETRIC_METRICS_EXIST_BUT_NONE_IS_CANONICALLY_DERIVED = true`.

`CANONICAL_SYMMETRIC_NATIVE_METRIC_DERIVED = false`.

This is a positive structure theorem plus a scalar-uniqueness/derivability no-go, not a failure of the directed geometry.
