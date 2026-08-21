# R063 Stage 1 — General Integer Path-Norm Root Discovery Beyond Perfect Squares

Task-ID: `RS-R063-STAGE1-GENERAL-NON-SQUARE-PATH-NORM-ROOT-DISCOVERY`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r063-stage1-general-path-norm-root`

## 0. Read first / frozen inputs

Read first:

1. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`;
2. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`;
3. `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`;
4. `definitions/ENTERPRISE_PATH_VALUED_SQUARE_ROOT_20260821.md`;
5. `driver_reviews/R063_STAGE0_PATH_VALUED_SQRT_2500_DRIVER_REVIEW_20260821.md`;
6. frozen R063 Stage 0 owner branch `research/r063-stage0-path-valued-sqrt-2500`.

Freeze from R063 Stage 0:

- for square native norms `N=r^2`, C3 scaled-square and C4 Gaussian-factorization discovery recover the exact ordered nonnegative component-root fiber;
- C2 unscaled square lift is incomplete in general;
- `PathSqrt_E(N)` pathifies each discovered component root `(a,b)` by
  `[u^a v^b](uX_i+vX_j)^(a+b)`;
- native trace/path semantics are inherited from frozen R061;
- algebraic derivation multiplicity and native path multiplicity are distinct layers;
- BRC is downstream projection only and must not participate in root discovery;
- discovery must remain separate from brute verification.

Do not reopen R061/R062/R063 Stage 0 unless an exact contradiction is found under the same frozen premises.

## 1. Hard objective

Generalize or falsify the Stage 0 factorization-first root operator from perfect-square inputs to **arbitrary positive integers `N`**.

Hard target:

`GENERAL_INTEGER_PATH_NORM_ROOT_DISCOVERY_CLASSIFIED_AND_COMPLETE_ON_INTEGER_COMPONENT_SUPPORT`

The central object to derive, if valid, is:

`GRoot_E(N) = {(a,b) in N_0^2 : a^2+b^2=N}`

but it must be generated **constructively from the arithmetic/Gaussian factorization of `N`**, not by solving the target equation first.

Then define, if exact:

`PathNormRoot_E(N) = disjoint_union_{(a,b) in GRoot_E(N)} [u^a v^b](uX_i+vX_j)^(a+b)`.

If `GRoot_E(N)=empty`, this must be returned as a mathematically meaningful empty integer-addressed native root fiber, not patched by real/irrational coordinates.

## 2. Discovery phase barrier — mandatory

The discovery phase may use only:

- the integer input `N`;
- exact integer factorization of `N`;
- arithmetic in `Z[J]/(J^2+1)`;
- Gaussian prime classification:
  - `2` ramified;
  - `p == 1 mod 4` split;
  - `q == 3 mod 4` inert;
- exact Gaussian multiplication, conjugation, norm, units;
- deterministic construction of split-prime Gaussian factors.

The discovery phase must **not** call, inspect, import or encode:

- brute enumeration of `a^2+b^2=N`;
- a precomputed sum-of-two-squares table;
- target branch literals for mandatory examples;
- any function whose semantics are equivalent to scanning candidate `a` or `b` against the target equation.

Required sequence:

1. run factorization-first discovery;
2. materialize a JSON-safe discovery object;
3. freeze/hash it;
4. only then run brute verification.

A source anti-hardcode audit is mandatory.

## 3. Sum-of-two-squares support theorem as a discovery gate

From the integer factorization alone, prove or falsify:

`GRoot_E(N) != empty`

iff every prime `q == 3 mod 4` occurs in `N` with even exponent.

This criterion must be derived/implemented independently of brute root enumeration.

Classify at least:

- `N=1`;
- `N=2`;
- `N=3`;
- `N=5`;
- `N=6`;
- `N=7`;
- `N=10`;
- `N=13`;
- `N=25`;
- `N=50`;
- `N=65`;
- `N=85`;
- `N=125`;
- `N=325`;
- `N=2500` as square-regression anchor.

Do not hard-code their roots.

## 4. General Gaussian factorization root generator

Promote/falsify the Stage 0 C4 idea on arbitrary `N`.

For

`N = 2^e2 * product p_i^e_i * product q_j^f_j`

where `p_i == 1 mod 4` and `q_j == 3 mod 4`, construct all Gaussian integers `z=a+bJ` of norm `N` by:

1. fixed ramified contribution from `(1+J)^e2`;
2. fixed integer Gaussian contribution `q_j^(f_j/2)` when every inert exponent is even;
3. for each split prime `p_i = pi_i * conjugate(pi_i)`, allocate the exponent `e_i` between `pi_i` and `conjugate(pi_i)` in all exact ways;
4. multiply by units;
5. quotient/deduplicate only by the declared ordered nonnegative native component return policy.

Prove or falsify:

`GAUSSIAN_FACTORIZATION_DISCOVERY_ROOTSET = COMPLETE_INTEGER_COMPONENT_NORM_FIBER`.

Separate:

- raw Gaussian derivation channels;
- deduplicated ordered nonnegative component roots;
- unordered component shapes;
- native trace identities;
- native path fibers.

## 5. Root-count theorem / factorization census

Derive a factorization-level count certificate for the Gaussian root fiber before explicit coordinate-root verification.

At minimum compare against the classical ordered signed representation count `r_2(N)` if reconstructed internally from the factorization theorem. Do not merely import a library result without showing the exact mapping to the generated Gaussian channels.

Classify how units, axes, equal-component roots, swaps and sign orbits affect:

- signed Gaussian root count;
- ordered nonnegative component-root count;
- unordered native component-shape count.

Preserve the smallest counterexample if any proposed count formula fails.

## 6. Pathification for non-square native lengths

For every discovered `(a,b)` define:

`Lambda(a,b) = [u^a v^b](uX_i+vX_j)^(a+b)`.

Verify that the frozen R061 trace semantics applies without requiring `sqrt(N)` to be an integer:

- trace identity: `T_{a,b}^{(ij)}`;
- exact native squared length: `N`;
- exact native length: `sqrt(N)` as an algebraic/radical scalar readout when non-integral;
- exact path cardinality: `binom(a+b,a)`;
- path-letter count `a+b` remains distinct from native length;
- no carrier Euclidean metric or vector relation is used as native geometry.

The crucial classification is whether an irrational scalar length such as `sqrt(13)` can still have a fully discrete integer-addressed native path fiber.

## 7. Mandatory non-square discovery witnesses

For each mandatory witness, discovery must precede brute verification and must output:

- integer factorization;
- Gaussian prime typing;
- raw factor-allocation channels;
- deduplicated ordered nonnegative component roots;
- unordered shapes;
- path-polynomial formula per root;
- exact path cardinality per root;
- exact total one-sector path cardinality;
- support/no-support reason.

Mandatory positive non-square witnesses:

`N = 2,5,10,13,50,65,85,125,325`.

Mandatory negative witnesses:

`N = 3,6,7,11,12,14,15,21,27`.

The checker source must not contain their nontrivial component roots as expected literals.

## 8. General exhaustive regression

Run a broad exact regression over at least:

`1 <= N <= 100000`.

For every `N`:

1. discovery/support criterion executes first;
2. discovery root set is frozen in-memory before verification;
3. brute verifier independently enumerates `a^2+b^2=N` only after discovery;
4. compare exact root-set equality;
5. compare empty/nonempty support classification;
6. compare no-extra / no-missing roots;
7. compare path cardinality formula for every discovered root using exact integers.

If `100000` is computationally excessive under deterministic replay, use the largest range that comfortably runs and is at least `1..20000`, and additionally test a deterministic sparse suite up to `10^9`. Record the exact tested range/suite.

Preserve the smallest failing `N`, discovered set, brute set and factorization if any mismatch occurs.

## 9. Multiplicative structure discovery

Investigate whether factorization channels expose a compositional law unavailable at the scalar-root level.

For representable `A,B`, compare Gaussian multiplication channels for roots of `A` and `B` against roots of `AB`.

Classify:

- when root multiplication is surjective onto the `AB` root fiber;
- when multiple algebraic derivation routes collapse to the same component root;
- whether derivation provenance forms a useful multiplicative enrichment above the deduplicated native trace;
- whether any such derivation multiplicity has a lawful relation to native path multiplicity.

Do not assume these multiplicities multiply.

At minimum audit products built from `2,5,13,17,25,65`.

## 10. BRC downstream projection only

R062 may be used only after path fibers are constructed:

`Path witness fiber -> N multiplicity -> Boolean support`.

BRC must not be used to discover roots, decide sum-of-two-squares representability or infer component labels.

## 11. Deterministic checker — mandatory

Commit an executable checker under `scripts/`.

Requirements:

- exact integer arithmetic only for all discovery/classification decisions;
- no float-based square-root or angle tests;
- discovery code path cannot call brute verifier;
- source anti-hardcode scan for mandatory roots;
- frozen discovery hash for central witnesses;
- exact factorization and Gaussian exponent-allocation replay;
- exact root-set equality after phase barrier;
- exact path cardinalities with big integers;
- compressed path representation with deterministic rank/unrank samples for large fibers;
- square-scope regression against frozen R063 Stage 0, including `N=25` and `N=2500`;
- non-square regression as above;
- mismatch file with `mismatch_count` and `smallest_mismatch`;
- nonzero process exit on any unclassified mismatch.

## 12. Required outputs

At minimum:

- `scripts/r063_stage1_validate_general_path_norm_root.py` or equivalent;
- `research_results/R063_STAGE1/R063_STAGE1_REPLAY_SUMMARY.json`;
- `R063_STAGE1_DISCOVERY_PHASE_FROZEN.json`;
- `R063_STAGE1_GENERAL_GAUSSIAN_ROOT_THEOREM.md`;
- `R063_STAGE1_SUM_OF_TWO_SQUARES_SUPPORT_THEOREM.md`;
- `R063_STAGE1_ROOT_COUNT_AND_ORBIT_CERTIFICATE.json`;
- `R063_STAGE1_NONSQUARE_PATH_FIBER_CERTIFICATE.json`;
- `R063_STAGE1_MULTIPLICATIVE_DERIVATION_AUDIT.md`;
- `R063_STAGE1_GENERAL_REGRESSION.json`;
- `R063_STAGE1_MISMATCHES.json`;
- `R063_STAGE1_REPRODUCIBILITY_PROOF.md`;
- `R063_STAGE1_FINAL_CLASSIFICATION.md`.

## 13. Acceptance gates

Stage 1 passes only if the selected construction satisfies all applicable gates:

1. `DISCOVERY_PHASE_INDEPENDENT_OF_BRUTE_TARGET_FIBER`;
2. `SUM_OF_TWO_SQUARES_SUPPORT_CLASSIFIED_FROM_FACTORIZATION`;
3. `GENERAL_GAUSSIAN_ROOT_GENERATOR_EXACT_OR_FALSIFIED`;
4. `NO_EXTRA_COMPONENT_ROOTS`;
5. `NO_MISSING_COMPONENT_ROOTS`;
6. `ROOT_COUNT_FACTOR_CERTIFICATE_CLASSIFIED`;
7. `NONSQUARE_NATIVE_TRACE_PATHIFICATION_EXACT`;
8. `IRRATIONAL_NATIVE_LENGTH_WITH_DISCRETE_PATH_FIBER_CLASSIFIED`;
9. `ALGEBRAIC_DERIVATION_VS_NATIVE_PATH_MULTIPLICITY_CLASSIFIED`;
10. `MULTIPLICATIVE_ROOT_PROVENANCE_CLASSIFIED`;
11. `SQUARE_SCOPE_R063_STAGE0_REGRESSION_PASS`;
12. `GENERAL_INTEGER_REGRESSION_PASS_OR_MINIMAL_COUNTEREXAMPLE_PRESERVED`;
13. `NO_BRC_ROOT_DISCOVERY_LEAKAGE`;
14. `NO_CARRIER_VECTOR_RELATION_PROMOTED_TO_NATIVE_IDENTITY`;
15. `NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE`;
16. `COMMITTED_DETERMINISTIC_CHECKER_PASS`.

## 14. Final classification options

Use the strongest result actually supported, for example:

- `PATH_NORM_ROOT_FACTORIZATION_OPERATOR_COMPLETE_FOR_ALL_POSITIVE_INTEGER_N_WITH_INTEGER_COMPONENT_SUPPORT`;
- `PATH_NORM_ROOT_OPERATOR_COMPLETE_EXACTLY_ON_SUM_OF_TWO_SQUARES_SUPPORT`;
- `GAUSSIAN_DISCOVERY_ROOTSET_COMPLETE_BUT_NATIVE_PATHIFICATION_HAS_OBSTRUCTION`;
- `NON_SQUARE_EXTENSION_PARTIAL_WITH_MINIMAL_COUNTEREXAMPLE`;
- another strictly evidenced classification.

Do not promote a theorem merely because the finite regression passes.

## 15. Stop rule

After committing all Stage 1 evidence and result artifacts, stop for Driver review.

Do not open R063 Stage 2.
