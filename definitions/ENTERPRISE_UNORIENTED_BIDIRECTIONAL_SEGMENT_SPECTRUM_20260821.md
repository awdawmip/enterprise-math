# 进取无向线段：双向 Canonical Trace Pair 与长度 Spectrum

Status: `ACTIVE / CANONICAL / FROZEN`
Date: `2026-08-21`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Canonical review source:

`driver_reviews/R061_STAGE3_UNORIENTED_SEGMENT_FINAL_DRIVER_REVIEW_20260821.md`

## 1. Directed foundation retained

For arbitrary integer-addressed coordinate vertices `P,Q`, the frozen Stage 2 construction provides one canonical directed native trace

`T(P->Q)`

and directed native line gauge

`ell_E(P->Q)`.

These are generally not reversal symmetric.

Do not replace them by a symmetric scalar and do not introduce native negative axes.

## 2. Canonical unoriented segment

For an unordered endpoint pair `{P,Q}`, freeze

`BSEG_E(P,Q) = { T(P->Q), T(Q->P) }`

as an endpoint-swap orbit / unordered typed pair of the two independently decoded canonical positive-axis traces.

Freeze:

`CANONICAL_UNORIENTED_SEGMENT_STRUCTURE = BIDIRECTIONAL_CANONICAL_TRACE_PAIR`.

The two directed traces may have different sector labels, component triples, path-fiber cardinalities, and directed line gauges.

## 3. Inverse trace is not canonical reverse trace

For `P!=Q`, distinguish:

- `T(P->Q)^(-1)` — groupoid inverse / reverse traversal of the same carrier path fiber;
- `T(Q->P)` — newly decoded canonical positive-axis native trace based at `Q`.

Freeze:

`T(P->Q)^(-1) != T(Q->P)` for every nonzero segment.

Equality occurs only for the zero trace.

No native rule identifies inverse carrier morphisms with positive-generator traces.

## 4. Orientation-free length data

Freeze the exact orientation-free length datum

`SPEC_E(P,Q) = multiset{ ell_E(P->Q), ell_E(Q->P) }`.

This is symmetric under endpoint exchange without discarding the directional information already forced by the native geometry.

Freeze:

`CANONICAL_ORIENTATION_FREE_LENGTH_DATA = BIDIRECTIONAL_LENGTH_SPECTRUM`.

Examples:

- unit positive-axis segment: `SPEC_E={1,sqrt(2)}`;
- translated 3-4-5 segment: `SPEC_E={5,sqrt(17)}`;
- reversal-symmetric `(2,1,0)`-type segment: `SPEC_E={sqrt(5),sqrt(5)}`.

## 5. Unoriented path fiber

Let `Realize_E(T(P->Q))` and `Realize_E(T(Q->P))` be the two frozen directed path fibers.

Define the unoriented realization object as the orientation-tagged disjoint union

`Realize_E(BSEG_E(P,Q)) = ({P->Q} x Realize_E(T(P->Q))) disjoint_union ({Q->P} x Realize_E(T(Q->P)))`.

The orientation tag must be retained because the two directed trace identities are distinct objects.

For translated 3-4-5:

- forward path fiber has `35` members;
- canonical reverse path fiber has `5` members;
- the groupoid inverse of the forward fiber has `35` reversed paths but is not the canonical reverse trace fiber.

## 6. Symmetric scalar metrics are noncanonical choices

Let

`v(P,Q)=(ell_E(P->Q),ell_E(Q->P))`.

If `Phi` is any norm on `R^2` satisfying:

- coordinate-swap symmetry;
- componentwise monotonicity on `R_+^2`;

then

`d_Phi(P,Q)=Phi(v(P,Q))`

is a symmetric metric.

Examples:

- `max(ell_f,ell_r)`;
- `ell_f+ell_r`;
- `(ell_f+ell_r)/2`;
- `sqrt(ell_f^2+ell_r^2)`;
- symmetric `l_p` norms.

These are conditional scalarizations after an additional choice of `Phi`.

Freeze:

`MULTIPLE_SYMMETRIC_METRICS_EXIST_BUT_NONE_IS_CANONICALLY_DERIVED = true`.

`CANONICAL_SYMMETRIC_NATIVE_METRIC_DERIVED = false`.

No current native invariant selects one `Phi`.

## 7. Nonuniqueness survives unit calibration

Even after requiring a chosen symmetric scalar metric to assign value `1` to the positive-axis unit segment, uniqueness does not follow.

Normalized `d_max` and normalized `d_2` both satisfy that calibration but disagree on a reversal-symmetric `(2,1,0)` segment.

Therefore metric axioms + translation invariance + homogeneity + unit calibration still do not force one scalarization.

## 8. R061 completion

The canonical R061 line theory is now layered as follows:

- directed line identity: native component trace;
- directed realization: all trace linearizations after typed start incidence;
- arbitrary-point directed line: translated trace;
- directed length: `ell_E` gauge;
- unoriented line segment: bidirectional canonical trace pair;
- orientation-free length data: bidirectional length spectrum;
- symmetric scalar metric: optional additional scalarization, not canonically derived.

Freeze:

`R061_PROGRAM_STATUS = COMPLETE_AND_FROZEN`.
