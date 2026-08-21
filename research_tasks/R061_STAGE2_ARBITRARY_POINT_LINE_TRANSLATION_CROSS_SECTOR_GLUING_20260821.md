# R061 Stage 2 — Arbitrary-Point Native Line Translation and Cross-Sector Gluing

Task-ID: `RS-R061-STAGE2-ARBITRARY-POINT-NATIVE-LINE-TRANSLATION-CROSS-SECTOR-GLUING`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r061-stage2-arbitrary-point-line-gluing`

## 0. Read first / frozen inputs

Read first:

1. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`;
2. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`;
3. `driver_reviews/R061_STAGE1R_NATIVE_LINE_TRACE_FINAL_ACCEPTANCE_20260821.md`;
4. frozen Stage 1 result branch `research/r061-stage1-native-line-trace-realization`;
5. frozen Stage 1R reproducibility head `653071b8e230d1e707e0544cab22ad2a408b92bd`.

Freeze from Stage 1/1R:

- `O_E=0` is a triple cell-boundary intersection, not a cell or cell center;
- the plane has three positive native axes only;
- adjacent positive axes form a native right angle of `120 degrees`;
- the three native right sectors are `S_12,S_23,S_31`;
- inside one sector, native length satisfies `L_E^2=a^2+b^2`;
- circle-cell carrier nearest-center spacing is `1` and radius is `1/sqrt(3)`;
- every fixed origin sector has one canonical incident anchor cell;
- coordinate vertex addresses and cell-center addresses are distinct typed copies linked by a constant affine offset;
- for a fixed origin sector,
  `T_{a,b}^{(ij)}=[X_i^a X_j^b]` under `X_iX_j~X_jX_i` is the frozen line identity;
- `Realize_E(T_{a,b}^{(ij)})={Sigma_O^(ij);w : w in Sh_{a,b}(X_i,X_j)}`;
- `|Realize_E(T_{a,b}^{(ij)})|=binom(a+b,a)`;
- same carrier endpoint does not imply same line identity;
- reverse-third carrier shortcuts are `CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE` relative to the fixed `ij` trace;
- graph jump count is not native line length;
- carrier vector relations must not be promoted to native vector identities.

Do not reopen those results unless an exact Stage 2 contradiction is found under the same frozen premises.

## 1. Hard objective

Extend or falsify the frozen origin-based sector-local line formula to **arbitrary integer-addressed native coordinate vertices**.

The hard target is:

`ARBITRARY_POINT_TO_POINT_NATIVE_LINE_TRACE_AND_CROSS_SECTOR_GLUING_DERIVED`.

The intended question is not merely whether two carrier vertices can be connected. It is whether the current native line identity admits a canonical translated form with exact typing, exact native length, exact discrete path fiber, and exact sector/gluing semantics.

At minimum answer:

1. Given arbitrary coordinate vertices `P,Q`, what is the native displacement object from `P` to `Q`?
2. Can the three positive axes be translated to `P` without introducing native negative axes?
3. Does every nonzero integer-lattice displacement fall into exactly one translated open native right sector, or on one translated native axis?
4. If so, what are its nonnegative integer component coordinates `(a,b)`?
5. Is the line identity from `P` to `Q` a translated trace `T_{P;a,b}^{(ij)}`?
6. What is the exact start-incidence operator at `P`?
7. What is the exact terminal typed endpoint at `Q`?
8. How are axis-boundary double chart presentations glued?
9. Does reversal `P->Q` versus `Q->P` preserve native length and map to the appropriate translated opposite sector without creating a native negative axis?
10. Does this construction resolve the currently open cross-sector point-to-point metric for integer native vertices?

If the current foundation is insufficient, freeze the smallest exact obstruction. Do not invent a tie-break or reintroduce signed axes.

## 2. Translate the native coordinate/sector atlas to an arbitrary start vertex

Let `P` be an arbitrary native coordinate/triple-intersection vertex.

Construct the three translated positive rays through `P`, parallel in the carrier presentation to the three global native axis families.

Define translated sectors

`S_12(P), S_23(P), S_31(P)`.

Prove or falsify:

- these three translated sectors partition directions around `P` exactly as at the origin;
- each translated sector has native opening/right angle `120 degrees`;
- each fixed translated open sector contains exactly one circle-cell center incident to `P`;
- translated axis rays pass through same-orientation coordinate vertices at unit native tick spacing and through no cell centers.

Define, if derivable,

`Sigma_P^(ij): P -> C_P^(ij)(0,0)`

as the unique translated sector-local start incidence.

It must be obtained by translation of the frozen incidence geometry, not by a guessed numeric offset.

Outputs:

- `R061_STAGE2_TRANSLATED_SECTOR_ATLAS_THEOREM.md`
- `R061_STAGE2_TRANSLATED_ORIGIN_INCIDENCE.json`

## 3. Canonical nonnegative displacement decomposition

For arbitrary integer coordinate vertices `P,Q`, derive the exact decomposition of the directed displacement `P->Q` using the three **positive** native sector charts.

Do not write a native negative axis coordinate.

The desired form, if true, is:

- either `Q` lies in exactly one translated open sector `S_ij(P)` and has unique nonnegative active components `(a,b)` with `a,b>0`;
- or `Q` lies on one translated positive axis and admits the two adjacent sector presentations that must be glued as one physical axis displacement;
- or `P=Q` gives the zero displacement.

Carrier signed coordinates may be used internally only to prove incidence/decomposition facts. They are not native signed coordinates.

Prove uniqueness after sector/axis typing.

Audit all six carrier directions explicitly: the absence of native negative axes must not make half of the directed displacements inexpressible.

Output:

`R061_STAGE2_POINT_PAIR_COMPONENT_DECOMPOSITION_THEOREM.md`

and a machine-readable decomposition census.

## 4. Translated line identity

If `P->Q` has translated-sector components `(a,b)` in `S_ij(P)`, test the canonical translated identity

`T_{P;a,b}^{(ij)}`

obtained from the frozen origin trace by translation of its base vertex.

The component content remains

`[X_i^a X_j^b]`

under

`X_iX_j~X_jX_i`,

but the line identity must now include enough start typing to distinguish parallel translated lines.

Determine the minimal identity fields. Candidates include:

- `(P,ij,a,b)`;
- `(start_vertex_id, trace_class)`;
- a translation orbit class plus a concrete placement;
- another strictly derived typed form.

Do not collapse parallel lines at different starting vertices into one physical line segment identity.

Output:

`R061_STAGE2_TRANSLATED_LINE_IDENTITY_THEOREM.md`.

## 5. Arbitrary-point native path realization

Derive or falsify

`Realize_E(T_{P;a,b}^{(ij)})`

as translated trace linearizations:

`{Sigma_P^(ij);w : w in Sh_{a,b}(X_i,X_j)}`.

For every path prove:

- exactly one circle cell at each discrete state;
- every center transition is between overlapping nearest-neighbor cells;
- all prefix cells lie in the translated sector affine chart;
- the terminal cell is incident to `Q`;
- all representatives share the same translated native component trace;
- cardinality remains `binom(a+b,a)`;
- jump count remains downstream and does not define native length.

Check whether translation introduces any new path collision/deduplication not present at the origin.

Output:

`R061_STAGE2_ARBITRARY_POINT_PATH_FIBER_THEOREM.md`.

## 6. Point-to-point native length and cross-sector metric

If the displacement decomposition is `(a,b)` in translated sector `S_ij(P)`, test

`d_E(P,Q)^2=a^2+b^2`.

This would define the integer-vertex point-to-point native metric even when `P` and `Q` live in different **origin-based** sector charts.

Mandatory metric audits:

- `d_E(P,P)=0`;
- positivity;
- reversal symmetry `d_E(P,Q)=d_E(Q,P)`;
- translation invariance on the coordinate-vertex lattice;
- compatibility with the frozen origin norm when `P=O_E`;
- compatibility across axis gluing;
- no carrier Euclidean metric leakage;
- do not assume the triangle inequality: test it exactly and classify the result;
- if triangle inequality fails, preserve the smallest counterexample and do not call the object a metric; use a weaker typed name.

The native `120 degree` right-angle law, not the classical carrier Gram form, controls the length after native sector decomposition.

Output:

`R061_STAGE2_POINT_TO_POINT_NATIVE_METRIC_AUDIT.md`.

## 7. Reversal without native negative axes

For a translated line from `P` to `Q`, derive the reversed line from `Q` to `P`.

The reverse carrier path may traverse inverse morphisms, but the native coordinate description must use one of the three positive translated sectors based at `Q`.

Prove or falsify an exact reversal map

`REV: T_{P;a,b}^{(ij)} -> T_{Q;c,d}^{(kl)}`

with

`L_E(P,Q)=L_E(Q,P)`.

Classify how sector labels transform.

Do not introduce `-E_i` as a native axis.

Output:

`R061_STAGE2_REVERSAL_POSITIVE_AXIS_THEOREM.md`.

## 8. Axis and sector gluing

A point-pair displacement lying on a translated native axis has two adjacent translated-sector presentations.

Derive the exact global line-identity deduplication rule while retaining distinct chart-local cell trajectories when their start anchor cells differ.

Also audit endpoints that lie on global/origin sector boundaries while their **displacement from P** lies in a different translated sector. Origin-chart membership of endpoints must not be confused with displacement-sector typing.

Output:

`R061_STAGE2_CROSS_SECTOR_AND_AXIS_GLUING_THEOREM.md`.

## 9. Same endpoint / same line under translation

Replay the Stage 1 third-direction distinction away from the origin.

For translated `(1,1)` and general `(a,b)`, check whether reverse-third carrier shortcuts remain:

`SAME_CARRIER_ENDPOINT / DIFFERENT_NATIVE_COMPONENT_TRACE`.

Prove translation covariance of the classification or preserve a counterexample.

Do not decide by jump count.

Output:

`R061_STAGE2_TRANSLATED_THIRD_DIRECTION_CLASSIFICATION.md`.

## 10. Exact examples

At minimum give fully typed examples for:

1. `P=Q`;
2. one-step positive-axis displacement;
3. a displacement geometrically opposite one global positive axis, expressed without a native negative axis;
4. translated `(1,1)`;
5. translated `3-4-5` from a non-origin vertex;
6. a pair `P,Q` lying in different origin-based sectors but whose displacement is one translated-sector `(3,4)` trace;
7. a translated axis-boundary case with two chart presentations;
8. reversal of each of the above;
9. several point pairs whose native displacement length is non-integer `sqrt(N)`;
10. a triangle-inequality stress example.

## 11. Deterministic checker — mandatory committed evidence

Unlike Stage 1, the checker publication gate is part of the initial acceptance criteria and must be committed on the owner branch.

Minimum requirements:

- executable deterministic checker committed under `scripts/`;
- no float dependence for combinatorial/typing decisions;
- exact replay of Stage 1R frozen hashes as regression targets;
- exhaustive translated-sector incidence on a nontrivial finite coordinate patch;
- exhaustive directed point-pair decomposition on that patch;
- verify every nonzero pair is classified into one translated open sector or one translated axis class;
- verify uniqueness modulo required axis gluing;
- explicit path replay for all translated trace pairs with `a+b<=12` over multiple start vertices in all three translated sectors;
- verify path count `binom(a+b,a)`;
- reversal audit for all tested directed pairs;
- translation covariance audit;
- axis gluing dedup audit;
- translated third-direction classification;
- point-to-point native length symmetry;
- exhaustive triangle-inequality test on a bounded patch, with smallest counterexample if any;
- mismatch file with `mismatch_count` and `smallest_mismatch`;
- committed replay summary and reproducibility proof.

The checker must regenerate evidence rather than copy Stage 1/1R result artifacts.

## 12. Acceptance gates

Stage 2 passes only if the selected construction satisfies all applicable gates:

1. `TRANSLATED_SECTOR_ATLAS_EXACT`;
2. `TRANSLATED_START_INCIDENCE_EXACT`;
3. `ALL_INTEGER_DIRECTED_DISPLACEMENTS_POSITIVE_AXIS_DECOMPOSABLE`;
4. `DISPLACEMENT_DECOMPOSITION_UNIQUE_UP_TO_AXIS_GLUE`;
5. `TRANSLATED_LINE_IDENTITY_EXACT`;
6. `ARBITRARY_POINT_PATH_FIBER_EXACT`;
7. `PATH_FIBER_CARDINALITY_TRANSLATION_INVARIANT`;
8. `POINT_TO_POINT_LENGTH_WELL_DEFINED`;
9. `REVERSAL_WITHOUT_NATIVE_NEGATIVE_AXES_PASS`;
10. `CROSS_SECTOR_AXIS_GLUE_PASS`;
11. `TRANSLATED_THIRD_DIRECTION_CLASSIFICATION_PASS`;
12. `ORIGIN_FORMULA_REGRESSION_PASS`;
13. `NO_CARRIER_METRIC_AS_NATIVE_METRIC_LEAKAGE`;
14. `COMMITTED_DETERMINISTIC_CHECKER_PASS`.

Triangle inequality is an explicit classification gate:

- if it passes, set `NATIVE_INTEGER_VERTEX_DISTANCE_IS_METRIC=true`;
- if it fails, set it false and retain the smallest counterexample, while continuing to classify whether a weaker point-to-point native length law survives.

The hard target may still pass in a weaker `line-length` sense only if the exact failed metric property is clearly separated and does not invalidate line identity/path realization.

## 13. Stop condition

Stop for Driver review after Stage 2.

Do not open a later stage automatically from the researcher branch.
