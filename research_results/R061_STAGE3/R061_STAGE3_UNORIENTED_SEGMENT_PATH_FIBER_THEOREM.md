# R061 Stage 3 — Unoriented Segment Path Fiber

Researcher-ID: `EM-R061S3-2F9622`

For `P!=Q`, let `BSEG_E(P,Q)={T_f,T_r}` with `T_f=T(P->Q)`, `T_r=T(Q->P)`.

The exact realization object is the orientation-tagged disjoint union

`UREAL_E(P,Q)=({F} x Realize_E(T_f)) disjoint_union ({R} x Realize_E(T_r))`.

The orientation tags are part of the typing, not extra physical simultaneous states.

## Why no inverse-path quotient is taken

`Realize(T_f)^{-1}` is the set of reversed traversals of the forward path family. It is generally not `Realize(T_r)`.

The translated `3-4-5` witness is decisive: forward canonical fiber cardinality `C(7,3)=35`; inverse forward fiber cardinality `35`; canonical positive-axis reverse decode `(1,0,4)`; reverse canonical fiber cardinality `C(5,1)=5`.

Therefore quotienting a forward fiber by groupoid reversal would discard the independently canonical reverse fiber. Even when cardinalities happen to agree, as in the unit segment or `(2,1,0)` reversal-symmetric locus, trace typing still distinguishes the families.

## Axis gluing

A directed positive-axis identity is globally deduplicated from its two adjacent sector presentations, while the two chart-local cell trajectories remain separate supports inside that directed fiber. `BSEG_E` pairs the already-glued directed identities and does not deduplicate their distinct chart-local trajectories against each other.

## Single-cell state rule

Every member of either directed fiber remains one circle cell at each discrete state. The unoriented segment object is a pair of alternative directed trajectory families, not a simultaneous multistate.

## Zero segment

For `P=Q`, the canonical trace is the zero trace. The segment identity is a singleton zero trace; its three sector-incidence support branches remain available as the frozen zero realization structure.

`UNORIENTED_SEGMENT_REALIZATION = ORIENTATION_TAGGED_PAIR_OF_CANONICAL_DIRECTED_FIBERS`.
