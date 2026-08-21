# R061 Stage 2 — Arbitrary-Point Directed Line Gauge Driver Review

Status: `ACCEPTED / FROZEN_WEAKER_DIRECTED_RESULT / SYMMETRIC_METRIC_OBSTRUCTION`
Date: `2026-08-21`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

## 1. Reviewed scope

Task-ID:

`RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`

Taskbook source:

`8b197776249e0b18850cee8375488de9aa57cbb4`

Owner branch:

`research/r061-stage2-arbitrary-point-line-gluing`

Repository audit against the taskbook source:

- owner branch is exactly one commit ahead;
- zero commits behind;
- only Stage 2 task-scoped results and `scripts/r061_stage2_validate_arbitrary_point_line_gluing.py` were added;
- no frozen prior definition/result file was modified.

The reviewed Stage 2 replay summary reports `mismatch_count=0` for all positive structural/checker gates. The only negative result is the explicitly classified reversal-length symmetry obstruction; it is not hidden as a checker mismatch.

## 2. Accepted arbitrary-point translation theorem

For arbitrary integer-addressed coordinate vertices `P,Q`, carrier coefficients may be used internally only as an implementation/decoding carrier.

Let

`delta_I(P,Q)=(r,s)`

in the frozen carrier presentation, let

`m=min(r,s,0)`,

and define the unique canonical positive-axis displacement address

`D(P->Q)=(r-m, s-m, -m)`.

Freeze:

`ALL_INTEGER_DIRECTED_DISPLACEMENTS_POSITIVE_AXIS_DECOMPOSABLE = true`.

`DISPLACEMENT_DECOMPOSITION_UNIQUE_UP_TO_AXIS_GLUE = true`.

This is a carrier-to-native decoding map, not restoration of the deleted native common-diagonal quotient.

Every nonzero directed point pair is typed as either:

- one translated positive axis displacement; or
- one translated open `120°` native right-sector displacement.

No native negative axis is introduced.

## 3. Accepted translated line identity and path fiber

For a translated open sector `S_ij(P)` with decoded native components `(a,b)`, freeze

`T_{P;a,b}^{(ij)} = (P,[X_i^a X_j^b])`

under the already frozen component-preserving relation

`X_iX_j ~ X_jX_i`.

The start vertex is part of the concrete line identity; dropping it would collapse distinct parallel translated segments.

The unique translated sector-local start incidence is

`Sigma_P^(ij): P -> C_P^(ij)(0,0)`.

Freeze the translated realization fiber:

`Realize_E(T_{P;a,b}^{(ij)}) = { Sigma_P^(ij); w : w in Sh_{a,b}(X_i,X_j) }`.

Its cardinality is translation invariant:

`|Realize_E(T_{P;a,b}^{(ij)})| = binom(a+b,a)`.

Stage 2 checker replayed `172,011` explicit paths over seven nontrivial starts, all three sectors and all trace pairs with `a+b<=12`, with zero endpoint, adjacency, sector-prefix, single-cell-state or collision mismatch.

Freeze:

`TRANSLATED_LINE_IDENTITY_EXACT = true`.

`ARBITRARY_POINT_PATH_FIBER_EXACT = true`.

`PATH_FIBER_CARDINALITY_TRANSLATION_INVARIANT = true`.

`CROSS_SECTOR_AXIS_GLUE_PASS = true`.

`TRANSLATED_THIRD_DIRECTION_CLASSIFICATION_PASS = true`.

The third-family carrier shortcut remains `SAME_CARRIER_ENDPOINT / DIFFERENT_NATIVE_COMPONENT_TRACE`, not a member of the translated line trace.

## 4. Directed native line gauge

For the unique canonical displacement triple

`D(P->Q)=(A,B,C)`, `min(A,B,C)=0`,

define

`ell_E(P->Q)^2 = A^2+B^2+C^2`.

Because one component is zero, this is exactly the frozen two-active-component Pythagorean law in the selected translated right sector.

Freeze:

`POINT_TO_POINT_LENGTH_WELL_DEFINED = true`.

`POINT_TO_POINT_NATIVE_LINE_LENGTH_OBJECT = DIRECTED_NATIVE_LINE_GAUGE`.

It satisfies:

- zero on `P=P`;
- positivity on `P!=Q`;
- translation invariance;
- origin-formula compatibility;
- axis-glue compatibility;
- exact triangle inequality;
- no carrier-Euclidean-metric leakage.

The exact triangle proof is accepted: if canonical displacement triples for `P->Q` and `Q->R` are `D1,D2`, then the canonical triple for `P->R` is obtained from `D1+D2` by subtracting the nonnegative common minimum from all three entries. Componentwise nonnegative decrease followed by the ordinary scalar-list `l2` triangle inequality gives

`ell_E(P->R) <= ell_E(P->Q)+ell_E(Q->R)`.

The checker independently tested all `81^3 = 531,441` ordered triples on the declared patch with zero failure.

## 5. Exact reversal obstruction

Let

`D(P->Q)=(A,B,C)`

and

`M=max(A,B,C)`.

The unique canonical positive-axis decoding of the reverse displacement is

`D(Q->P)=(M-A,M-B,M-C)`.

This proves reversal can be represented without native negative axes.

However the squared lengths transform as

`ell_E(Q->P)^2-ell_E(P->Q)^2 = M(3M-2(A+B+C))`.

Hence reversal symmetry holds only on the exceptional locus

`2(A+B+C)=3M`.

The smallest exact counterexample, canonical up to translation and cyclic axis relabeling, is one native `E1` tick:

`D(P->Q)=(1,0,0)`, so `ell_E(P->Q)^2=1`,

while

`D(Q->P)=(0,1,1)`, so `ell_E(Q->P)^2=2`.

For the translated `3-4-5` branch:

`D_f=(3,4,0)`, `ell_f^2=25`,

but

`D_r=(1,0,4)`, `ell_r^2=17`.

Freeze:

`REVERSAL_TRACE_REDECOMPOSITION_WITHOUT_NATIVE_NEGATIVE_AXES = true`.

`REVERSAL_LENGTH_SYMMETRY = false`.

`NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC = false`.

`GROUPoid_INVERSE_IS_TARGET_POSITIVE_TRACE_FIBER = false` in general.

This is a theorem/obstruction under the current premises, not a checker defect.

## 6. Driver classification

The Stage 2 hard target is accepted in the exact weaker sense explicitly allowed by the taskbook:

`ARBITRARY_POINT_TO_POINT_NATIVE_LINE_TRACE_AND_CROSS_SECTOR_GLUING_DERIVED = true`

for **directed native line identities/path fibers and a directed triangle-subadditive line gauge**.

The stronger symmetric point-to-point metric claim is rejected:

`FULL_STAGE2_METRIC_ACCEPTANCE = false`.

Do not call `ell_E` a metric.

Do not patch the unit-step asymmetry by reintroducing native negative axes, by promoting the carrier relation to a native vector identity, or by silently changing the frozen `120°` Pythagorean law.

## 7. Open foundational question

Stage 2 exposes a new foundational fork that is deeper than ordinary cross-sector chart gluing:

- either Enterprise line length is intrinsically directed/asymmetric;
- or an orientation-free segment invariant must be defined as a new object distinct from the directed trace gauge;
- or one of the frozen positive-axis / right-angle / translation premises must eventually be superseded by an exact contradiction-driven correction.

The next stage must classify this fork rather than mechanically symmetrize `ell_E`.
