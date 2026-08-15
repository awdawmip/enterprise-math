# R059D Stage M REISSUE2 — BRC6 Three-Axis Vector Carrier / Geometric-Tool Refoundation / Endpoint-Count Microgrammar Robustness

Task-ID: `RS-R059D-STAGE-M-BRC6-THREE-AXIS-VECTOR-GEOMETRIC-TOOL-REFOUNDATION-MICROGRAMMAR-ROBUSTNESS`
Generation: `R059D`
Status: `DRIVER_APPROVED_REISSUE2_TASKBOOK`
Date: `2026-08-15`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Owner branch: `research/r059d-stage-m-brc6-three-axis-vector-refounded-geometry`

## 0. Frozen parent

Consume BRC6 Stage L only from frozen owner head:

`da350b7b1e2ae21491e6251fdf2ba9cf0d4557ca`

All Stage J/K/L BRC6 artifacts remain immutable.

The following earlier Stage-M taskbooks are superseded before execution:

- `R059D_STAGE_M_BRC6_EQUAL_L_ENDPOINT_BRANCH_COUNT_MICROGRAMMAR_ROBUSTNESS_20260815.md`
- `R059D_STAGE_M_BRC6_DISCRETE_THREE_AXIS_VECTOR_ENDPOINT_COUNT_MICROGRAMMAR_REISSUE_20260815.md`

This REISSUE2 is the only active Stage-M taskbook.

Also read and obey project policy:

`GEOMETRIC_TOOL_REFOUNDATION_POLICY.md`

Core policy:

`REFOUND, NOT REJECT`.

## 1. Scientific correction

Enterprise Math is not attempting to abolish Euclidean geometry or its mature tools.

The project keeps the concepts:

- VECTOR;
- LENGTH;
- ANGLE;
- NORM;
- DOT PRODUCT / PAIRING;
- SIN;
- COS;
- TAN;
- AREA / VOLUME;
- classical geometric constructions.

The correction is only:

`CLASSICAL_DEFINITION_NOT_AUTOMATICALLY_INHERITED_AS_FOUNDATION`.

For each mature tool, future tasks may rebuild a discrete / precision-aware definition from the project's number-theoretic substrate and then compare it against classical Euclidean mathematics.

Classical Euclidean results are permitted and important as:

- evidence;
- calibration targets;
- engineering compatibility targets;
- exact/approximate recovery tests;
- downstream tool interfaces.

Do not write global claims such as `NO LENGTH`, `NO ANGLE`, `NO TRIGONOMETRY`, `NO EUCLIDEAN GEOMETRY`.

Preferred Stage-M wording is only:

- `LENGTH_NOT_USED_AS_BRC6_SELECTOR_PREMISE`;
- `ANGLE_NOT_USED_AS_BRC6_SELECTOR_PREMISE`;
- `TRIG_NOT_USED_AS_BRC6_SELECTOR_PREMISE`.

Those statements do not deny the concepts.

## 2. Three-axis discrete vector plane

Freeze the current algebraic plane carrier:

`Lambda = {(a,b,c) in Z^3 : a+b+c=0}`.

It has two degrees of freedom.

Freeze three axis generators:

`u=(1,-1,0)`
`v=(0,1,-1)`
`w=(-1,0,1)`

with:

`u+v+w=0`.

Freeze six directed step vectors:

`D6={+u,-u,+v,-v,+w,-w}`.

Thus:

`PLANE_DIMENSION=2`
`AXIS_COUNT=3`
`DIRECTED_STEP_COUNT=6`.

The six BRC6 results are six directed vectors, not six independent dimensions.

Vector equality, addition, subtraction, additive inverse, integer scalar multiplication and finite path-vector sums are admitted mature algebraic operations.

## 3. Geometric-tool semantic slots

Stage M must explicitly freeze these semantic statuses before scoring:

`VECTOR_CONCEPT = ADMITTED`
`LENGTH_CONCEPT = ADMITTED`
`ANGLE_CONCEPT = ADMITTED`
`TRIGONOMETRIC_CONCEPTS = ADMITTED`
`EUCLIDEAN_GEOMETRY = REFERENCE_AND_CALIBRATION_LAYER_ADMITTED`

and simultaneously:

`CLASSICAL_LENGTH_DEFINITION_AS_NATIVE_PREMISE = WITHHELD`
`CLASSICAL_ANGLE_DEFINITION_AS_NATIVE_PREMISE = WITHHELD`
`CLASSICAL_TRIG_DEFINITION_AS_NATIVE_PREMISE = WITHHELD`

Stage M does **not** need to solve the complete length/angle/trigonometry refoundation problem. That is a later dedicated research lane.

For this Stage M only, none of those undeveloped readouts may be used to choose the BRC6 winner.

If the researcher wants to record a classical Euclidean length/angle/trig value as a diagnostic or calibration column, it must be marked:

`CALIBRATION_READOUT_ONLY_NOT_SELECTOR_PREMISE`.

## 4. Equal-L selector boundary

Retain the Stage-L experiment control:

`ALIGNED_SEGMENT_CELL_COUNT=L=4`

for all six directed vector candidates.

This L is a discrete packet/cell count used to define a common aligned endpoint evaluation boundary.

It is **not** a declaration that the mature geometric concept LENGTH is globally equal to packet count.

Freeze the distinction:

`SEGMENT_PACKET_COUNT = 4`

versus

`GEOMETRIC_LENGTH = CONCEPT_ADMITTED_DEFINITION_NOT_FROZEN_IN_STAGE_M`.

This distinction is mandatory.

All six candidates must have the same `SEGMENT_PACKET_COUNT=4` in the Stage-M comparison.

Do not use any geometric length readout, classical or rebuilt, as the BRC6 selector score in this stage.

## 5. BRC6 endpoint branch-count observable

Retain:

`B_d = exact admissible raw-history multiplicity arriving at candidate directed-vector d's next aligned endpoint after the common four packet cells`.

For Stage-M positive selection:

`BRC6_COUNT_MODE(sigma)=d`

iff

`B_d > B_e` for all other `e in D6`.

Exact maximal ties are:

`BRC6_UNRESOLVED_BY_ENDPOINT_BRANCH_COUNT`.

Unresolved is evaluator status, not a seventh vector.

This rule is canonical only inside the explicitly frozen endpoint-branch-count collapse semantics.

Continue:

`BRC6_NATIVE_CANONICALITY = NOT_ESTABLISHED`.

## 6. Main Stage-M question

Keep fixed:

- the three-axis vector carrier `Lambda`;
- the six directed vectors `D6`;
- the same four continuation packet cells for every candidate;
- the same next aligned endpoint convention;
- the same endpoint branch-count collapse rule.

Vary only the internal count-preserving branch / internal-state / recoalescence microgrammar carried through those same packet cells.

For every frozen microgrammar `g`, compute:

`B_d^(g)`

using both raw-history enumeration and exact CPBC compression.

Mandatory proof gate:

`CPBC_ENDPOINT_COUNT = RAW_HISTORY_MULTIPLICITY`.

No arbitrary weights.

No support-only collapse.

Any integer multiplicity >1 must arise from explicitly distinct admissible histories.

## 7. Microgrammar registry

Freeze before witness scoring at least:

- `M-G0 AFFINE_UV_REPLAY`;
- `M-G1 SINGLE_SPLIT_RECOALESCE`;
- `M-G2 DELAYED_SPLIT_RECOALESCE`;
- `M-G3 TWO_STAGE_SPLIT_RECOALESCE`;
- `M-G4 LAUNCH_CLASS_SPLIT_CONTROL`;
- `M-G5 VECTOR_INTERNAL_REWRITE_ENDPOINT_EQUIVALENT`.

All six candidate vectors must use the same grammar `g` within one evaluation.

Candidate-specific grammar selection is forbidden.

Each grammar must respect the frozen three-axis symmetry action.

## 8. Vector history bookkeeping

Every raw history stores its exact directed vector transition word.

For history h:

`VECTOR_SUM(h)=sum_t d_t`.

This is admitted exact vector algebra.

Required tiny cases:

- immediate reversal `d,-d`;
- repeated vector step;
- algebraic loop with vector sum zero;
- revisit;
- two distinct vector words recoalescing at one endpoint;
- same-axis opposite-orientation histories;
- different-axis histories reaching the same discrete coordinate;
- multiplicity >1 at one endpoint.

Do not infer a geometric LENGTH from `VECTOR_SUM` in Stage M unless explicitly marked calibration-only.

## 9. Symmetry and axis/orientation structure

At minimum test symmetry generated by:

- cyclic axis permutation `u->v->w->u`;
- global inversion `d->-d`.

No absolute privileged axis or sign.

Audit whether six-way endpoint-count collapse factors exactly into:

1. selection among three undirected axes;
2. orientation `+/-` within the selected axis.

Do not assume factorization. Prove equivalence or provide counterexample.

## 10. Robustness classes

For a fixed state across all frozen admissible microgrammars classify:

- `MICROGRAMMAR_STRONG_CONSENSUS_RESOLVED`;
- `MICROGRAMMAR_COMPATIBLE_WITH_TIES`;
- `MICROGRAMMAR_DEPENDENT`;
- `MICROGRAMMAR_ALL_UNRESOLVED`.

If two legal grammars uniquely select different vectors from the same exact state, freeze explicit microgrammar dependence and do not promote native canonicality.

## 11. Mandatory witness replay

Replay at minimum:

- `W_ASYM_BASE`;
- `W_CONSENSUS_DOMINANT2`;
- `W_FULLY_SYMMETRIC`;
- `W_S1_TIE_S2_RESOLVE`;
- `W_SIGNATURE_INSUFFICIENT_PAIRS`.

Store vector-keyed endpoint-count six-vectors and exact winner/tie status.

Search a pre-frozen bounded integer witness box for robust and dependent domains.

## 12. Structural theorem targets

Priority:

### M-T1 ENDPOINT-FUNCTIONAL EQUIVALENCE

Different internal organizations with identical endpoint branch-count functional must give identical BRC6 outcome for every state.

### M-T2 NONNEGATIVE COMPONENT DOMINANCE

Find sufficient conditions under which one vector candidate remains winner for every admissible grammar in the registry.

### M-T3 MICROGRAMMAR DEPENDENCE CERTIFICATE

Find explicit state + two legal grammars with conflicting strict vector winners if possible.

### M-T4 AXIS/ORIENTATION FACTORIZATION

Prove or refute exact factorization of six-way collapse into 3-axis then +/- orientation stages.

## 13. True vector-state dynamics

Use the Stage-K/L exact count update plus discrete vector coordinates.

After selecting vector d:

`O_x[d] += 1`
`M_x[i,d] += 1`

Traverse the declared four-packet segment, arrive at the declared vector endpoint, update target ingress counts, and recompute all six endpoint branch counts from the accumulated state.

Track:

- current discrete vector coordinate;
- selected vector sequence;
- vector sum of selected transitions;
- endpoint count table;
- first unresolved epoch;
- cross-microgrammar trajectory divergence;
- exact same-epoch state recoalescence if any.

Do not claim a full-state cycle merely from repeated vector direction words.

## 14. Perturbations

Repeat:

- one launch/count token;
- one incidence event;
- one real tagged adjacency/vector transition change.

Record BRC6 vector change, endpoint-count delta, trajectory divergence, unresolved creation/removal, and any exact recoalescence.

## 15. Classical geometric calibration status

Stage M may optionally record classical Euclidean diagnostics for the three-axis vector carrier, but only as calibration readouts.

If used, the report must clearly separate:

- `FOUNDATIONAL_OR_REBUILT_QUANTITY`;
- `CLASSICAL_EUCLIDEAN_CALIBRATION_READOUT`.

Do not treat disagreement with classical Euclidean formulas as automatic failure.

Do not treat agreement as proof that the classical definition belongs in the native substrate.

## 16. Large N

Retain symbolic exact probes near `10^36`.

N is system/tag/packet scale only.

It is not geometric length, angle, norm, vector magnitude or precision.

## 17. Required artifacts

At minimum freeze:

1. `R059D_STAGE_M_THREE_AXIS_VECTOR_PROTOCOL.json`
2. `R059D_STAGE_M_GEOMETRIC_TOOL_SEMANTIC_STATUS.json`
3. `R059D_STAGE_M_EQUAL_PACKET_COUNT_ENDPOINT_PROTOCOL.json`
4. `R059D_STAGE_M_VECTOR_SYMMETRY_PROTOCOL.json`
5. `R059D_STAGE_M_VECTOR_MICROGRAMMAR_REGISTRY.json`
6. `R059D_STAGE_M_RAW_HISTORY_CPBC_VECTOR_ORACLE.json`
7. `R059D_STAGE_M_VECTOR_ENDPOINT_FUNCTIONAL_ATLAS.json`
8. `R059D_STAGE_M_VECTOR_MICROGRAMMAR_ROBUSTNESS_LEDGER.json`
9. `R059D_STAGE_M_VECTOR_AXIS_ORIENTATION_FACTORIZATION_AUDIT.json`
10. `R059D_STAGE_M_VECTOR_TRUE_DYNAMICS_ATLAS.json`
11. `R059D_STAGE_M_VECTOR_PERTURBATION_RESPONSE.json`
12. `R059D_STAGE_M_VECTOR_LARGE_N_REGISTRY.json`
13. deterministic checker + output
14. report
15. artifact manifest
16. frozen checkpoint

Then:

`STOP_FOR_DRIVER_REVIEW`.

## 18. Permitted conclusions

If proved, Stage M may freeze:

- `DISCRETE_THREE_AXIS_VECTOR_CARRIER_ESTABLISHED`;
- `BRC6_VECTOR_ENDPOINT_COUNT_MICROGRAMMAR_ROBUST_DOMAIN_ESTABLISHED`;
- `BRC6_VECTOR_ENDPOINT_COUNT_MICROGRAMMAR_DEPENDENCE_ESTABLISHED`;
- `BRC6_AXIS_ORIENTATION_FACTORIZATION_ESTABLISHED` or rejected;
- exact true vector-state dynamics results.

It may not claim:

- classical Euclidean geometry is false;
- length/angle/trigonometry do not exist;
- a physical direction law has been calibrated;
- the current endpoint-count collapse is the unique native law.

Global project principle:

`REFOUND, NOT REJECT`.
