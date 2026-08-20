# R061 Stage 0 — Enterprise Line Formula Validation Driver Review

Status: `ACCEPTED_PARTIAL_THEOREM / NATIVE_FORMULA_NOT_VALIDATED / OPEN_NEXT_FOUNDATIONAL_QUESTION`
Date: `2026-08-20`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Task-ID: `RS-R061-STAGE0-ENTERPRISE-LINE-FORMULA-ALGEBRAIC-PATH-LIFT-VALIDATION`
Taskbook source: `0936ade269bcdc3a58b3d8b4c2148c6197dc1a63`
Frozen owner branch: `research/r061-stage0-line-formula-path-lift-validation`
Frozen owner head: `e6657ce00382d52acda319f0108b787a03e9d5f2`

## 1. Driver verdict

Stage 0 is accepted as a successful falsification/typing stage.

Do **not** freeze the full candidate

`scalar sqrt(N) -> coordinate decomposition -> shuffle -> native circle-cell line fiber`

as a validated native formula.

Freeze instead the strongest exact surviving split:

1. scalar/norm -> integer Pythagorean coordinate fiber: **VALIDATED**;
2. coordinate pair -> free noncommutative shuffle fiber: **VALIDATED**;
3. free shuffle fiber -> canonical native circle-cell line fiber: **NOT VALIDATED**.

Driver classification:

`COORDINATE_LIFT_VALID_BUT_NATIVE_PATH_LIFT_INCOMPLETE`.

This is `OPEN_NEXT_FOUNDATIONAL_QUESTION`, not `REJECT_WHOLE_DIRECTION`.

## 2. Frozen exact theorems from Stage 0

### 2.1 Coordinate decomposition fiber

For every nonnegative integer `N`,

`D_N={(a,b) in N_0^2 : a^2+b^2=N}`

is exactly recoverable algebraically through the `J^2=-1` / Gaussian norm factorization route used in Stage 0.

The owner reports zero mismatch for `N=0..100000` against direct integer ground truth and zero mismatch for square hypotenuse cases `r<=4096` against complete Euclid parameterization.

Freeze:

`R061_S0_COORDINATE_FIBER_COMPLETE = true`.

`R061_S0_ALGEBRAIC_FACTOR_EXTRACTION_COMPLETE = true`.

### 2.2 Noncommutative coefficient lift

For every `(a,b)`,

`[u^a v^b](uX+vY)^(a+b)`

is exactly the sum of all free words containing `a` copies of `X` and `b` copies of `Y`, each exactly once.

Cardinality:

`|Sh_{a,b}| = binom(a+b,a)`.

Freeze:

`R061_S0_NONCOMMUTATIVE_COEFFICIENT_LIFT_EXACT = true`.

The exact surviving formal formula is

`FORMAL_LIFT_E^(ij)(N) = disjoint_union_{a^2+b^2=N} Sh_{a,b}(X_i,X_j)`.

This is a formal scalar-to-coordinate-to-free-word theorem, not yet a native line theorem.

## 3. Independent Driver replay

Driver independently replayed the main deterministic invariants and reproduced the owner digests exactly:

- coordinate fiber, `N=0..100000`: mismatch count `0`;
- coordinate fiber SHA256: `0f4bccc2ff3fd7e7ae22ccd9e4abf248cf215bffea7bdd02aabca9b8c2bb8338`;
- Euclid-vs-brute square-hypotenuse audit through `r=4096`: mismatch count `0`;
- explicit shuffle words through `a+b<=22`: `8,388,607` words;
- explicit shuffle global SHA256: `572562117dbc2ba388543fbbeaa73bd26359ef47c26ef7ff31314ee92b318f93`;
- compressed Pascal validation through `a+b<=512`: mismatch count `0`;
- Pascal SHA256: `780c833ed685c707b2e57d70a2ecf015e56bc5196ee8e62a646720eb0707d002`.

Thus the formal computational evidence is accepted.

## 4. Frozen counterexamples / blockers

### 4.1 Origin typing blocker

`CE-R061-ORIGIN-000` is accepted.

Current foundation freezes:

`O_E=0`;

`ORIGIN_IS_TRIPLE_CELL_INTERSECTION`;

`ORIGIN_IS_NOT_CELL_CENTER`;

`ORIGIN_IS_NOT_A_CELL`.

Therefore a free word in center-to-center transition generators cannot act directly on `O_E`.

A native realization requires a type-changing origin-incidence/start operator of the form

`Sigma_O : O_E -> one incident circle cell`

or a corrected ontology in which the line endpoint/path carrier is typed differently.

Freeze:

`NAIVE_PI_CELL_IDENTITY_FROM_ORIGIN = false`.

`ORIGIN_AFFINE_START_TYPING = OPEN`.

No guessed `+1/-1` offset is allowed.

### 4.2 Third-direction endpoint-path blocker

`CE-R061-THIRDAXIS-11` is accepted **as a counterexample to the claim that the two-generator shuffle equals all nearest-center/minimum-jump endpoint realizations**.

At the triangular circle-center carrier level, after a valid start cell is chosen, the endpoint reached by the two-step formal words

`X1 X2`, `X2 X1`

also has a one-nearest-center-edge realization in the reverse third carrier-direction family.

This uses carrier adjacency only. It does not redefine native Enterprise length by carrier Euclidean length.

Freeze:

`TWO_AXIS_SHUFFLE != ALL_MINIMUM_JUMP_ENDPOINT_PATHS`.

However, this does **not** by itself prove that the third-direction one-step path belongs to the *same native line*. It proves that `same endpoint` and `same line realization` cannot be conflated.

## 5. Critical conceptual distinction opened by Stage 0

Stage 0 exposes the next foundational distinction:

`ENDPOINT_PATH_FIBER != LINE_PATH_FIBER` in general.

A native straight line may need an algebraic identity stronger than common endpoint and different from graph-geodesic minimality.

One natural candidate is a trace/partial-order object:

- line identity: one algebraic trace with multiplicities `(a,b)` on the two Enterprise-orthogonal positive axes;
- path realizations: the linearizations/shuffles of that trace;
- a third-family path reaching the same endpoint may be a different endpoint realization rather than a representative of the same line trace.

This is a **candidate only**. It is not frozen by this review.

## 6. Native foundation that remains fixed

Stage 1 must preserve unless an exact contradiction is proved:

- `ENTERPRISE_RIGHT_ANGLE = 120_DEGREES`;
- each native right sector uses the Pythagorean law `a^2+b^2`;
- `L_E(3,4,0)=5`;
- three positive axes only;
- cell centers form the overlapping triangular carrier with nearest-center spacing `1`;
- every circle cell has carrier radius `1/sqrt(3)`;
- neighboring cells overlap and the cover has no gaps;
- origin is a triple cell-boundary intersection and not a cell center;
- native geometric state is one circle cell per trajectory step;
- jump count is not native line length;
- carrier direction relations are not native vector identities.

## 7. Stage 0 acceptance map

Freeze:

`R061_STAGE0_ACCEPTED = true`.

`ENTERPRISE_LINE_FORMULA_VALIDATED = false`.

`FORMAL_LINE_LIFT_VALIDATED = true`.

`NATIVE_LINE_REALIZATION = OPEN`.

`PI_CELL = NONTRIVIAL_OR_UNDERDETERMINED`.

`SAME_ENDPOINT_DOES_NOT_IMPLY_SAME_LINE = OPEN_AND_MUST_BE_TYPED`.

## 8. Next-stage directive

Open R061 Stage 1.

Hard question:

`WHAT_IS_THE_NATIVE_LINE_PATH_FIBER_AND_HOW_DOES_IT_START_FROM_ORIGIN?`

Stage 1 must derive or reject a trace-class realization, resolve the origin/cell affine typing, and distinguish:

- line identity;
- line path representatives;
- arbitrary endpoint paths;
- minimum-jump endpoint paths;
- carrier-only alternate routes.

Do not reopen Stage 0's validated algebraic decomposition/shuffle theorems unless a checker contradiction is found.
