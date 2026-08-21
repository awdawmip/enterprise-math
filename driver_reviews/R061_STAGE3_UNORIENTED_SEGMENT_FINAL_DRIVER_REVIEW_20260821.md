# R061 Stage 3 — Unoriented Segment Final Driver Review

Status: `ACCEPTED / FROZEN / R061 COMPLETE`
Date: `2026-08-21`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Taskbook source:

`fded2481f78219c13c981fbcdb9ee07167fb6027`

Owner branch:

`research/r061-stage3-unoriented-segment-symmetry`

The owner branch is one commit ahead of the taskbook source and contains only Stage 3 theorem/census/checker artifacts.

## Final classification

Freeze:

`CANONICAL_UNORIENTED_SEGMENT_STRUCTURE_AND_SYMMETRIC_METRIC_DERIVABILITY_CLASSIFIED = true`.

`CANONICAL_UNORIENTED_SEGMENT_STRUCTURE = BIDIRECTIONAL_CANONICAL_TRACE_PAIR`.

`CANONICAL_ORIENTATION_FREE_LENGTH_DATA = BIDIRECTIONAL_LENGTH_SPECTRUM`.

`MULTIPLE_SYMMETRIC_METRICS_EXIST_BUT_NONE_IS_CANONICALLY_DERIVED = true`.

`CANONICAL_SYMMETRIC_NATIVE_METRIC_DERIVED = false`.

For distinct endpoints `P,Q`, define the two canonical positive-axis traces independently:

`T_f=T(P->Q)` and `T_r=T(Q->P)`.

The canonical unoriented segment is the endpoint-swap orbit

`BSEG_E(P,Q)={T(P->Q),T(Q->P)}`.

Its exact orientation-free length datum is the multiset

`SPEC_E(P,Q)=multiset{ell_E(P->Q),ell_E(Q->P)}`.

The unoriented path fiber is the orientation-tagged disjoint union of the two directed trace fibers.

## Inverse versus canonical reverse

For every nonzero segment,

`T(P->Q)^(-1) != T(Q->P)`.

The former is reverse traversal through inverse carrier morphisms. The latter is a fresh positive-axis decode from `Q` to `P` under the frozen three-positive-axis ontology.

Equality occurs only for the zero segment.

Even on the nonzero length-symmetric locus, the typed traces remain distinct.

## Exact witnesses

Unit positive-axis segment:

- forward components `(1,0,0)`, squared gauge `1`;
- reverse components `(0,1,1)`, squared gauge `2`;
- orientation-free spectrum `{1,sqrt(2)}`.

Translated 3-4-5 segment:

- forward components `(3,4,0)`, gauge `5`, path-fiber cardinality `35`;
- reverse components `(1,0,4)`, gauge `sqrt(17)`, canonical reverse path-fiber cardinality `5`;
- orientation-free spectrum `{5,sqrt(17)}`.

Reversal-symmetric nonzero locus:

for canonical displacement `(M,m,0)` with `M>=m>0`, the two directed gauges agree iff `M=2m`; nevertheless inverse trace and canonical reverse trace remain distinct.

## Symmetric scalar metric classification

Let

`v(P,Q)=(ell_E(P->Q),ell_E(Q->P))`.

For any norm `Phi` on `R^2` that is coordinate-swap symmetric and componentwise monotone on `R_+^2`,

`d_Phi(P,Q)=Phi(v(P,Q))`

is a symmetric metric.

Examples include `d_max`, `d_sum`, `d_mean`, `d_2`, and all symmetric `l_p` norms.

These are valid conditional constructions, not canonical native promotions.

Nonuniqueness survives unit calibration: normalized `d_max` and normalized `d_2` both give unit segments scalar value `1` but disagree on the reversal-symmetric `(2,1,0)` segment.

Therefore the frozen structure does not determine a unique symmetric scalar distance.

## Reproducibility

Committed checker:

`scripts/r061_stage3_validate_unoriented_segment_symmetry.py`

The checker regresses Stage 2 decomposition/path/axis results and audits the Stage 3 bidirectional and scalarization claims.

Key deterministic facts:

- ordered point pairs: `6,561`;
- nonzero ordered point pairs: `6,480`;
- unordered nonzero endpoint pairs: `3,240`;
- nonzero inverse-trace/canonical-reverse coincidences: `0`;
- reversal-length asymmetric ordered pairs: `5,616`;
- reversal-length symmetric nonzero ordered pairs: `864`;
- ordered triples tested for metric scalarizations: `531,441`;
- final `mismatch_count=0`.

## R061 closure

R061 is complete at the current foundational scope.

Frozen progression:

1. Stage 0: scalar -> integer Pythagorean fiber -> exact noncommutative shuffle lift; native realization blockers isolated.
2. Stage 1/1R: native component trace and exact circle-cell multipath realization frozen.
3. Stage 2: arbitrary-point translated traces and directed native line gauge frozen; symmetric metric obstruction identified.
4. Stage 3: canonical unoriented bidirectional trace pair and bidirectional length spectrum frozen; scalar symmetric metric proven nonunique/noncanonical.

No R061 Stage 4 is opened automatically.

`R061_PROGRAM_STATUS = COMPLETE_AND_FROZEN`.
