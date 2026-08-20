# R061 Stage 0 — Enterprise Line Formula: Algebraic Path-Lift Broad Validation

Task-ID: `RS-R061-STAGE0-ENTERPRISE-LINE-FORMULA-ALGEBRAIC-PATH-LIFT-VALIDATION`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r061-stage0-line-formula-path-lift-validation`

This stage is a broad falsification/validation stage for the proposed Enterprise line formula. It is not a request to assume the formula is correct.

Do not modify prior frozen R059/R060 branches. Do not reopen the geometry unless an exact contradiction is found under the current premises.

## 0. Read first / current premises

Read first:

- `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md` at or after source commit `0708e49def6b24683c245fa79f4d26cd19dd44f2`;
- `definitions/ENTERPRISE_VECTOR_RADIUS_DISCRETE_ROTATION_THEORY_20260817.md` only for downstream principles not superseded by the 2026-08-20 coordinate reset.

Current native premises to preserve unless contradicted exactly:

- `O_E = 0`;
- every native cell is a circle cell identified by its center;
- nearest cell-center spacing is 1;
- uniform cell radius is `1/sqrt(3)`;
- neighboring cells overlap, the cover has no gaps, and circle-boundary intersections are triple-cell intersections;
- there are three positive native axes;
- the three positive axes divide the full turn into three native right sectors;
- `ENTERPRISE_RIGHT_ANGLE = 120_DEGREES` in the carrier presentation;
- the canonical address atlas is the glued union
  - `S_12={(a,b,0):a,b>=0}`,
  - `S_23={(0,b,c):b,c>=0}`,
  - `S_31={(a,0,c):a,c>=0}`;
- no common-diagonal quotient is active;
- within one native right sector, the native metric is Pythagorean:
  - `L_E(a,b,0)^2=a^2+b^2`, cyclically;
- carrier Euclidean length is not native Enterprise length;
- one discrete trajectory state is one circle cell;
- native line length is not graph jump count.

## 1. Candidate line formula under test

Fix one native right sector, initially `S_12`, and let `X,Y` be the two noncommuting primitive cell-transition generators associated with its active positive axes.

For a target squared native length `N in N_0`, define the integer coordinate fiber

`D_N = {(a,b) in N_0^2 : a^2+b^2=N}`.

For one coordinate pair `(a,b)`, define the formal noncommutative path lift

`Lambda(a,b) = [u^a v^b] (u X + v Y)^(a+b)`

where `u,v` commute with everything, while `X,Y` are free/noncommuting at the formal path level.

Equivalent candidate notation:

`Lambda(a,b) = X^a shuffle Y^b`.

The proposed sector-local scalar-to-path formula is

`LINE_E(N;X,Y) = sum_{(a,b) in D_N} Pi_cell(Lambda(a,b))`.

`Pi_cell` is intentionally not assumed to be the identity. It is the native cell-admissibility realization/filter that this stage must derive, validate, or show to be nontrivial.

For the motivating example:

`N=25`,

`D_25={(5,0),(4,3),(3,4),(0,5)}`,

and the nondegenerate branch `(3,4)` gives

`Lambda(3,4)=[u^3 v^4](uX+vY)^7`,

with formal shuffle cardinality `C(7,3)=35`.

The hard claim under test is not merely that the coefficient identity is true. The hard claim is that a scalar/native length can be lifted algebraically to the correct native discrete line-path fiber.

## 2. Required distinction: scalar, coordinate fiber, path fiber

Keep three levels strictly separate:

1. `SCALAR LENGTH LEVEL`: `sqrt(N)`;
2. `COORDINATE DECOMPOSITION FIBER`: `D_N`;
3. `NONCOMMUTATIVE PATH FIBER`: the admissible path words above each `(a,b)`.

Freeze only as a typing requirement:

`SCALAR != COORDINATE_PAIR != PATH_WORD`.

A successful formula may be one-to-many.

Do not require `sqrt(N)` to select a unique `(a,b)` or a unique path.

If several coordinate decompositions exist, preserve all of them with multiplicities/symmetry labels handled explicitly.

## 3. First hard objective — completeness of algebraic coordinate extraction

Determine whether `D_N` can be generated from `N` algebraically without manual search or target leakage.

Validate at least three mutually cross-checking routes:

### 3A. Exact integer definition

Use the definition

`a^2+b^2=N`

as ground-truth enumeration/checker semantics.

This is allowed for validation but must not be the final claimed closed-form derivation if a stronger factorization formula exists.

### 3B. Native right-sector quadratic algebra

Introduce, if useful,

`A_E = Z[J]/(J^2+1)`

with purely algebraic native interpretation

`Norm_E(a+bJ)=a^2+b^2`.

`J` is an algebraic Enterprise-right-sector unit. Do not interpret `J` as evidence that the carrier angle is classical 90 degrees.

Test whether factorization/norm arithmetic in `A_E` gives a complete and deduplicated method to recover all `(a,b)` with norm `N`.

### 3C. Euclid/Pythagorean parameterization for integer hypotenuse cases

For `N=r^2` and nondegenerate integer solutions, validate the classical algebraic parameterization as an external theorem/cross-check:

`a=k(m^2-n^2)`

`b=2kmn`

`r=k(m^2+n^2)`

with the required gcd/parity/order conditions stated exactly.

Prove or verify that this produces every nondegenerate integer decomposition of `r^2`, up to leg swap and the declared sector symmetry.

Do not use the theorem as a geometric import of classical 90-degree angle. Only its integer algebra may be reused.

Outputs:

- `research_results/R061_STAGE0/R061_STAGE0_COORDINATE_FIBER_THEOREM.md`
- `research_results/R061_STAGE0/R061_STAGE0_COORDINATE_FIBER_CENSUS.json`

## 4. Mandatory scalar cases

The formula must distinguish the following cases correctly:

1. `D_N` empty — native scalar length exists algebraically/continuously but has no integer-center endpoint in that sector;
2. axis-only decomposition — `(sqrt(N),0)` or `(0,sqrt(N))` when integral;
3. one nondegenerate pair up to swap;
4. several inequivalent nondegenerate pairs;
5. scaled/nonprimitive decompositions;
6. square and nonsquare `N`;
7. `N=0` boundary case.

Mandatory hand-checked values include at least:

`N = 0,1,2,3,4,5,8,9,10,13,16,17,18,20,25,26,29,32,34,37,41,50,65,85,125,169,325,625,1105,4225`.

In particular:

- `N=25` must recover `(3,4)` and `(4,3)` plus axis degenerates;
- `N=65` must expose multiple norm decompositions;
- some nonrepresentable `N` must return an empty integer path fiber rather than inventing a cell endpoint.

## 5. Second hard objective — exact noncommutative path-lift theorem

For fixed `(a,b)`, prove exactly what

`[u^a v^b](uX+vY)^(a+b)`

generates in the free associative algebra.

Required theorem candidates:

- every term is a word of length `a+b` containing exactly `a` copies of `X` and `b` copies of `Y`;
- every such word appears exactly once before any native quotient/filter;
- the formal number of words is

`binom(a+b,a)=binom(a+b,b)`;

- different words are distinct path candidates because path order is noncommutative;
- abelianization sends every word to the same coordinate displacement `(a,b)`.

Define an exact endpoint map

`End(w)=(#X(w),#Y(w))`

at the formal sector level and prove

`L_E(End(w))^2=N`

for every `w` in the lifted fiber above `(a,b)`.

Output:

- `research_results/R061_STAGE0/R061_STAGE0_NONCOMMUTATIVE_PATH_LIFT_THEOREM.md`

## 6. Critical scope audit — what class of paths does the formula actually generate?

Do not call the shuffle expansion “all paths” without proving the path class.

Classify precisely whether `Lambda(a,b)` is:

- all coordinate-monotone two-generator paths;
- all minimum-jump paths inside the fixed sector;
- all simple native cell paths realizing the endpoint;
- only a strict subset of legitimate native line realizations;
- or something else.

The set of all unrestricted walks is generally infinite because loops may be inserted. Therefore a canonical Enterprise line-path fiber must state a finite admissibility/minimality condition.

Required question:

`WHAT_FINITE_PATH_CLASS_IS_CANONICALLY_GENERATED_BY_THE_LINE_FORMULA?`

Do not assume the answer is “minimum jump” merely because the shuffle length is `a+b`; remember native line length is `sqrt(a^2+b^2)`, not jump count.

Output:

- `research_results/R061_STAGE0/R061_STAGE0_PATH_CLASSIFICATION.md`

## 7. Third hard objective — native circle-cell admissibility

Replay the formal path words on the actual current circle-cell plane.

For every generated word, verify step by step:

- every instantaneous state is exactly one circle cell;
- every transition corresponds to an allowed nearest-center / overlap-incidence move under the current carrier;
- no teleportation;
- no simultaneous multi-cell state;
- the intended sector/chart remains valid or an explicit chart transition is recorded;
- the path endpoint has the claimed integer address;
- the native endpoint length is the claimed `sqrt(N)`;
- carrier Euclidean distance is never substituted for native length.

Determine whether

`Pi_cell = identity`

on the full shuffle fiber inside one right sector.

If not, characterize exactly which words are rejected and derive the minimal native admissibility projection.

Do not patch by arbitrary tie-breaking.

Outputs:

- `research_results/R061_STAGE0/R061_STAGE0_CELL_ADMISSIBILITY_THEOREM.md`
- `research_results/R061_STAGE0/R061_STAGE0_CELL_ADMISSIBILITY_CENSUS.json`

## 8. Origin-is-not-center audit — mandatory off-by-one test

The native origin `O_E=0` is a triple cell-boundary intersection, not a cell center.

Therefore the formal word algebra must not silently treat the origin as a cell state.

Audit the exact relation among:

- scalar segment origin at `O_E`;
- the three cells incident to `O_E`;
- first selected cell state;
- first primitive `X/Y` transition;
- integer endpoint address;
- path word length.

Test whether the true native realization requires an explicit start-incidence operator such as

`Sigma_O`

before the free word,

`NativePath = Sigma_O * w`,

or whether the current affine integer-center atlas already absorbs this offset without changing path counts.

This stage must detect and report any `+1`, `-1`, or affine-offset error.

For the `3-4-5` case, explicitly verify whether the native realization really contains 7 primitive center transitions, or whether the origin incidence changes that count.

Output:

- `research_results/R061_STAGE0/R061_STAGE0_ORIGIN_AFFINE_OFFSET_AUDIT.md`

## 9. Third-axis / cross-sector completeness challenge

For an endpoint in `S_12`, the candidate formula uses only `X,Y`.

Actively search for legitimate native cell realizations using the third sector/axis or sector changes that:

- reach the same endpoint;
- have the same admissibility/minimality status as shuffle paths;
- but are not generated by `Lambda(a,b)`.

If such paths exist, the proposed line formula is incomplete as a native line fiber.

If none exist under the chosen canonical finite path class, prove why.

This is a mandatory falsification channel.

Output:

- `research_results/R061_STAGE0/R061_STAGE0_THIRD_AXIS_COMPLETENESS_AUDIT.md`

## 10. Three-sector covariance and axis gluing

Transport the full construction cyclically to

- `S_12` with generators `(X_1,X_2)`;
- `S_23` with generators `(X_2,X_3)`;
- `S_31` with generators `(X_3,X_1)`.

Validate exact covariance under cyclic relabeling.

Handle axis-degenerate decompositions carefully because an axis is shared by two neighboring sector charts.

Do not double-count a physical axis realization merely because it appears in two chart descriptions.

Derive the exact gluing/deduplication rule for the global line fiber.

Output:

- `research_results/R061_STAGE0/R061_STAGE0_SECTOR_COVARIANCE_AND_GLUING.md`

## 11. Reverse map / collapse consistency

For every admissible generated native path `w`, compute:

1. its ordered path word;
2. its endpoint displacement/address;
3. its native squared length;
4. the scalar `sqrt(N)`.

Require the reverse consistency diagram

`PATH -> ENDPOINT -> NATIVE LENGTH`

and

`NATIVE LENGTH -> COORDINATE FIBER -> PATH LIFT`

to agree on the same fiber classification.

Do not require a one-to-one inverse. The intended object is a fiber-valued inverse.

Test whether two distinct coordinate decompositions of the same `N` remain distinguishable as direction branches above the same scalar.

Output:

- `research_results/R061_STAGE0/R061_STAGE0_FORWARD_REVERSE_FIBER_AUDIT.md`

## 12. Large deterministic validation

After the structural proofs are written, run deterministic validation at scale.

Minimum requirements:

### Coordinate decomposition census

- exhaustive `N=0..100000` against direct integer enumeration;
- for all square `N=r^2` with `r<=4096`, compare the nondegenerate solutions against complete Euclid-parameter generation;
- compare the factor/norm route in `A_E` against brute ground truth on the same range;
- record empty, unique, multiple, primitive, nonprimitive, and axis-degenerate classes.

### Explicit word enumeration

For every `(a,b)` with `a+b<=22`, explicitly generate every shuffle word and verify:

- exact count `binom(a+b,a)`;
- no duplicate free words;
- endpoint counts;
- native admissibility;
- symmetry under leg swap.

### Compressed large-word validation

For larger cases up to at least `a+b<=512`, do not materialize exponentially many words. Use a deterministic DAG/dynamic-programming/hash or equivalent exact compressed representation to verify:

- coefficient/count recursion;
- endpoint class;
- cell-admissibility invariants if local;
- sector covariance.

### Stress examples

Include at least:

- `3-4-5`;
- `5-12-13`;
- `8-15-17`;
- `7-24-25`;
- `20-21-29`;
- several scaled triples;
- a hypotenuse with multiple inequivalent Pythagorean decompositions, especially `r=65`;
- nonsquare `N` with multiple sum-of-two-squares decompositions;
- nonrepresentable `N`.

All scripts must be deterministic and committed.

Outputs:

- `research_results/R061_STAGE0/R061_STAGE0_VALIDATION_SUMMARY.json`
- `research_results/R061_STAGE0/R061_STAGE0_COUNTEREXAMPLES.json`
- scripts under `scripts/` or a task-scoped validation directory.

## 13. Candidate final line formula

The stage may recommend a canonical formula only after all audits pass.

Candidate form:

`LINE_E^(ij)(N) = sum_{a^2+b^2=N} Pi_cell( [u^a v^b](u X_i + v X_j)^(a+b) )`.

A global formula may then glue the three sector-local fibers with an explicit axis deduplication relation.

If `Pi_cell` is identity, prove it.

If the actual canonical finite path class is narrower or wider than the shuffle fiber, replace the candidate formula with the minimal exact correction.

Do not preserve the candidate merely for elegance.

## 14. Hard acceptance gates

Set

`ENTERPRISE_LINE_FORMULA_VALIDATED = true`

only if all gates pass:

1. `COORDINATE_FIBER_COMPLETE`;
2. `ALGEBRAIC_FACTOR_EXTRACTION_COMPLETE`;
3. `NONCOMMUTATIVE_COEFFICIENT_LIFT_EXACT`;
4. `PATH_CLASS_TYPED_FINITE_AND_CANONICAL`;
5. `CELL_ADMISSIBILITY_EXACT`;
6. `ORIGIN_AFFINE_OFFSET_RESOLVED`;
7. `THIRD_AXIS_COMPLETENESS_PASS`;
8. `THREE_SECTOR_COVARIANCE_PASS`;
9. `AXIS_GLUE_DEDUP_PASS`;
10. `FORWARD_REVERSE_FIBER_CONSISTENCY_PASS`;
11. `NO_CARRIER_EUCLIDEAN_METRIC_LEAKAGE`;
12. `LARGE_DETERMINISTIC_VALIDATION_PASS`.

If any gate fails, set

`ENTERPRISE_LINE_FORMULA_VALIDATED = false`

and preserve the smallest exact counterexample.

Partial success must be typed, for example:

- `COORDINATE_LIFT_VALID_BUT_NATIVE_PATH_LIFT_INCOMPLETE`;
- `SHUFFLE_THEOREM_VALID_BUT_PI_CELL_NONTRIVIAL`;
- `SECTOR_LOCAL_VALID_BUT_GLOBAL_GLUE_OPEN`;
- `ORIGIN_OFFSET_BREAKS_NAIVE_WORD_COUNT`.

## 15. Mandatory proof deliverable

Produce

`research_results/R061_STAGE0/R061_STAGE0_ENTERPRISE_LINE_FORMULA_VALIDATION_PROOF.md`

with, at minimum:

1. exact definitions;
2. theorem for scalar-to-coordinate fiber;
3. theorem for coordinate-to-noncommutative word lift;
4. path-class theorem;
5. native cell-admissibility theorem or counterexample;
6. origin affine-offset theorem;
7. third-axis completeness theorem or counterexample;
8. sector covariance/gluing theorem;
9. large-census results;
10. final status and the exact strongest formula that survives.

## 16. Forbidden shortcuts

Do not:

- assume every shuffle word is a native path without replay;
- call unrestricted loop-containing walks “the line”;
- identify native line length with `a+b`;
- reintroduce the superseded carrier quadratic form `a^2+b^2-ab` as native metric;
- use classical carrier 90-degree angle to redefine Enterprise orthogonality;
- treat `O_E` as a cell center;
- silently identify cell centers with coordinate vertices;
- select only the `3-4` decomposition of 25 while discarding other valid decomposition branches;
- use numerical floating tolerance where exact integer/symbolic arithmetic is available;
- hide failed cases by post-selection;
- modify the current foundation to rescue the formula unless an exact contradiction forces Driver review.

## 17. Stop condition

Stop for Driver review after the validation package is complete.

Do not automatically freeze the line formula as canonical merely because the checker passes.

Do not open R061 Stage A automatically.

The Driver will decide whether the result is:

- `ACCEPT_AS_CANONICAL_LINE_FORMULA`;
- `ACCEPT_SECTOR_LOCAL_ONLY`;
- `CORRECT_AND_RETEST`;
- `REJECT_WITH_COUNTEREXAMPLE`;
- or `OPEN_NEXT_FOUNDATIONAL_QUESTION`.
