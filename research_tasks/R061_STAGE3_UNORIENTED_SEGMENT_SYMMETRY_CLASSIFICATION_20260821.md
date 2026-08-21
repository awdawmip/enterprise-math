# R061 Stage 3 — Unoriented Segment Identity and Symmetric-Metric Derivability Classification

Task-ID: `RS-R061-STAGE3-UNORIENTED-SEGMENT-SYMMETRY-CLASSIFICATION`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r061-stage3-unoriented-segment-symmetry`

## 0. Read first / frozen inputs

Read first:

1. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`;
2. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`;
3. `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`;
4. `driver_reviews/R061_STAGE2_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_DRIVER_REVIEW_20260821.md`;
5. Stage 2 owner branch `research/r061-stage2-arbitrary-point-line-gluing`.

Freeze from Stage 2:

- arbitrary integer directed point pairs admit a unique positive-axis displacement decode, modulo axis chart gluing;
- translated line identities and translated path fibers are exact;
- the directed line gauge is
  `ell_E(P->Q)^2=A^2+B^2+C^2` for canonical `D_E(P->Q)=(A,B,C)`;
- `ell_E` is positive, translation invariant and triangle-subadditive;
- reversal decodes by
  `D_E(Q->P)=M(1,1,1)-D_E(P->Q)`, `M=max(D_E(P->Q))`;
- reversal symmetry fails in general;
- smallest obstruction: `(1,0,0)` forward has squared gauge `1`, reverse `(0,1,1)` has squared gauge `2`;
- translated `3-4-5`: forward squared gauge `25`, reverse squared gauge `17`;
- path-groupoid inverse of a forward trace is generally **not** the canonical positive-axis reverse trace;
- `NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC=false` for the directed gauge;
- no native negative axes;
- carrier vector relations are not native vector identities.

Do not reopen these except upon an exact contradiction under the same premises.

## 1. Hard objective

Classify the orientation-free segment structure forced by the current Enterprise geometry, and determine whether a **canonical symmetric scalar point-distance** is derivable without adding an arbitrary aggregation rule or violating frozen line/axis semantics.

Hard target:

`CANONICAL_UNORIENTED_SEGMENT_STRUCTURE_AND_SYMMETRIC_METRIC_DERIVABILITY_CLASSIFIED`.

The stage must distinguish:

1. one directed native line trace `T(P->Q)`;
2. its path-groupoid inverse `T(P->Q)^{-1}`;
3. the independently canonical positive-axis reverse trace `T(Q->P)`;
4. an unoriented physical segment identity, if derivable;
5. an orientation-free length invariant, if derivable;
6. a symmetric scalar metric, if derivable.

Do not assume any two of these are the same object.

## 2. First no-confusion theorem: inverse trace versus canonical reverse trace

For arbitrary `P!=Q`, compare exactly:

- `INV(T(P->Q))`: reverse traversal of the same directed path/trace object through inverse carrier morphisms;
- `T(Q->P)`: the canonical positive-axis translated trace freshly decoded at `Q`.

Classify the locus on which they coincide, if any.

Mandatory checks:

- component trace labels;
- path fibers;
- start-incidence anchors;
- terminal typing;
- directed gauge values;
- the Stage 2 reversal-symmetry locus `2 sum(D)=3 max(D)`;
- axis and `(a,a)` cases;
- translated `3-4-5`.

Do not identify them merely because they have the same endpoint pair.

Output:

`R061_STAGE3_INVERSE_TRACE_VS_CANONICAL_REVERSE_THEOREM.md`.

## 3. Candidate unoriented segment identities

Audit at least the following candidates.

### U0 — INVERSE-QUOTIENT OF ONE DIRECTED TRACE

For a selected directed trace `T`, define an unoriented class `{T,T^{-1}}`.

Question: is this determined by the unordered endpoint pair `{P,Q}`, or do the independently canonical traces `T(P->Q)` and `T(Q->P)` generate different inverse-quotient classes?

### U1 — BIDIRECTIONAL CANONICAL TRACE PAIR

Define

`BSEG_E(P,Q) = { T(P->Q), T(Q->P) }`

as an unordered pair/multiset of the two canonical positive-axis directed traces.

Test whether this is:

- endpoint-canonical;
- symmetric under swapping `P,Q`;
- translation invariant;
- compatible with axis gluing;
- compatible with Stage 1 origin traces;
- free of arbitrary orientation choice;
- algebraically generable;
- sufficient to recover both directed path fibers.

### U2 — SINGLE CANONICAL TRACE CHOSEN FROM THE TWO DIRECTIONS

Test all native/invariant selection rules actually forced by the current premises. Do not invent lexicographic, global-coordinate, shorter-direction or longer-direction tie-breaks unless a frozen native invariant forces them.

### U3 — OTHER INCIDENCE/TRACE-FORCED UNORIENTED OBJECT

If a different exact object is forced, derive it.

Output a candidate matrix.

## 4. Orientation-free length data

For an unordered endpoint pair define the exact bidirectional directed-gauge data

`SPEC_E(P,Q) = multiset{ ell_E(P->Q), ell_E(Q->P) }`.

Audit whether this spectrum/multiset is the minimal canonical orientation-free scalar-data object forced by the current foundation.

Required properties:

- symmetry under endpoint swap;
- translation invariance;
- positivity typing;
- exact scaling behavior;
- exact recovery of each directed gauge after orientation is supplied;
- axis gluing;
- cyclic covariance;
- translated `3-4-5` gives exactly `{5,sqrt(17)}`;
- one-tick axis example gives exactly `{1,sqrt(2)}`.

If another stronger orientation-free invariant is uniquely forced, derive it.

Output:

`R061_STAGE3_BIDIRECTIONAL_LENGTH_SPECTRUM_THEOREM.md`.

## 5. Symmetric scalarization — derivability, not preference

A symmetric scalar point-distance would require a rule

`d_F(P,Q)=F(ell_E(P->Q),ell_E(Q->P))`

with `F(x,y)=F(y,x)`.

Do **not** choose an `F` because it looks natural.

Classify derivability/uniqueness under the current premises.

At minimum audit these comparison families as **noncanonical candidates**, not presumed truths:

- `F_max(x,y)=max(x,y)`;
- `F_sum(x,y)=x+y`;
- normalized arithmetic mean;
- `F_p(x,y)=(x^p+y^p)^(1/p)` for representative exact/integer-checkable `p>=1` where useful;
- any incidence/trace-derived scalarization actually forced by the native structure.

For each candidate classify:

- symmetry;
- positivity;
- translation invariance;
- homogeneity/scaling;
- triangle inequality;
- compatibility with origin-sector length `ell_E(O->Q)`;
- compatibility with frozen `3-4-5` value `5` when orientation is forgotten;
- axis unit calibration;
- whether the rule consumes a new arbitrary choice/parameter;
- whether different admissible scalarizations coexist.

A key possible outcome is:

`MULTIPLE_SYMMETRIC_METRICS_EXIST_BUT_NONE_IS_CANONICALLY_DERIVED`.

If so, prove it by constructing at least two distinct valid symmetric metrics from the directed quasi-metric/gauge and prove both satisfy their claimed axioms.

Do not call nonuniqueness a failure; it is a derivability result.

Output:

`R061_STAGE3_SYMMETRIC_SCALARIZATION_DERIVABILITY_THEOREM.md`.

## 6. Metric construction theorem for standard symmetrizations

Because `ell_E` and its reverse both satisfy directed triangle inequalities, test exact general lemmas rather than only finite data.

At minimum prove or falsify:

- `d_max(P,Q)=max(ell_E(P->Q),ell_E(Q->P))` is a symmetric metric;
- `d_sum(P,Q)=ell_E(P->Q)+ell_E(Q->P)` is a symmetric metric;
- more generally, for a symmetric monotone norm `Phi` on `R_+^2`, whether
  `d_Phi(P,Q)=Phi(ell_f,ell_r)`
  inherits the triangle inequality.

These are classification tools only. Passing does **not** promote any candidate to native canonical status without a separate derivability/uniqueness argument.

Keep carrier Euclidean geometry out of the native metric proof.

## 7. No-go / incompatibility audit

Test exactly which combinations of desired properties are jointly impossible under the frozen premises.

Mandatory properties to compare:

- endpoint-swap symmetry;
- translation invariance;
- exact agreement with the directed origin norm for every `Q`:
  `d(O,Q)=ell_E(O->Q)`;
- exact agreement with directed translated trace norm in both orientations;
- `3-4-5` orientation-free scalar remains `5`;
- positive-axis unit remains `1`;
- no native negative axes;
- no carrier relation promoted to a native vector identity.

Use the one-tick and `3-4-5` reversal examples as mandatory witnesses.

If an impossibility theorem holds only after adding a stated axiom, state the axiom explicitly. Do not overclaim an unconditional no-go theorem.

Output:

`R061_STAGE3_SYMMETRY_NO_GO_AND_AXIOM_MATRIX.md`.

## 8. Path-fiber semantics of an unoriented segment

If `BSEG_E(P,Q)` or another unoriented object survives, derive its realization object.

Candidates include:

- unordered pair of the two directed trace fibers;
- disjoint union with orientation tags;
- quotient by path-groupoid reversal where legitimate;
- another exactly typed structure.

Preserve the Stage 1/2 rule that one instantaneous trajectory state is one circle cell.

Do not merge distinct directed trajectories into a simultaneous multistate.

Determine whether an unoriented segment can have two inequivalent directed path-fiber families between the same endpoint pair.

Output:

`R061_STAGE3_UNORIENTED_SEGMENT_PATH_FIBER_THEOREM.md`.

## 9. Exact examples

Mandatory examples:

1. `P=Q`;
2. one positive-axis tick: spectrum `{1,sqrt(2)}`;
3. one displacement opposite a positive carrier direction;
4. translated `(1,1)`;
5. translated `3-4-5`: spectrum `{5,sqrt(17)}`;
6. a reversal-symmetric nonzero locus example satisfying `2 sum(D)=3 max(D)`;
7. axis-glued pair;
8. several noninteger radical pairs;
9. examples separating `T^{-1}` from canonical reverse trace;
10. examples showing two different valid scalar symmetrizations give different numerical answers.

## 10. Deterministic checker — mandatory

Commit an executable deterministic checker under `scripts/`.

Minimum evidence:

- regress Stage 2 accepted decomposition/path/gauge facts;
- exhaustive unordered and ordered endpoint pairs on at least the Stage 2 `81`-vertex patch;
- exact bidirectional spectra;
- inverse-trace versus canonical-reverse classification;
- candidate unoriented-object deduplication;
- `d_max` and `d_sum` symmetry/triangle checks;
- at least one additional scalarization family if claimed;
- exact one-tick and `3-4-5` witnesses;
- scaling checks;
- axis gluing;
- mismatch file with smallest mismatch;
- no floating-point dependence for theorem-critical comparisons.

Proof/typing dominates finite checker evidence.

## 11. Acceptance gates

Stage 3 passes if it produces an exact classification, not necessarily a symmetric metric.

Required gates:

1. `INVERSE_TRACE_VS_CANONICAL_REVERSE_CLASSIFIED`;
2. `UNORIENTED_SEGMENT_IDENTITY_CANDIDATES_CLASSIFIED`;
3. `BIDIRECTIONAL_LENGTH_DATA_EXACT`;
4. `SYMMETRIC_SCALARIZATION_DERIVABILITY_CLASSIFIED`;
5. `AT_LEAST_TWO_VALID_SCALAR_METRICS_OR_UNIQUENESS_PROOF`;
6. `ORIGIN_AND_3_4_5_COMPATIBILITY_AUDITED`;
7. `UNORIENTED_PATH_FIBER_TYPED`;
8. `NO_NEGATIVE_AXIS_REINTRODUCTION`;
9. `NO_CARRIER_METRIC_LEAKAGE`;
10. `COMMITTED_DETERMINISTIC_CHECKER_PASS`.

Allowed final outcomes include:

- `CANONICAL_SYMMETRIC_NATIVE_METRIC_DERIVED`;
- `CANONICAL_BIDIRECTIONAL_SEGMENT_DERIVED_BUT_SCALAR_METRIC_NONUNIQUE`;
- `DIRECTED_GEOMETRY_ONLY_IS_FORCED_BY_CURRENT_PREMISES`;
- an exact impossibility/underspecification theorem.

Do not choose among these in advance.

## 12. Stop condition

Stop after Stage 3 for Driver review.

Do not open Stage 4 automatically from the researcher branch.
