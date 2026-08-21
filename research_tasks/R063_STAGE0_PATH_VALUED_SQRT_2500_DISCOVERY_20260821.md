# R063 Stage 0 — Path-Valued Square Root 2500 Discovery

Task-ID: `RS-R063-STAGE0-PATH-VALUED-SQUARE-ROOT-2500-DISCOVERY`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r063-stage0-path-valued-sqrt-2500`

## 0. Read first / frozen inputs

Read first:

1. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`;
2. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md`;
3. `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md`;
4. `driver_reviews/R061_STAGE1R_NATIVE_LINE_TRACE_FINAL_ACCEPTANCE_20260821.md`;
5. frozen R061 Stage 0/1/1R algebraic and path evidence;
6. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` only as a downstream readout reference, not as a generator of roots or paths.

Freeze from R061:

- one native right sector uses component algebra `A_E = Z[J]/(J^2+1)` as a sector-local algebraic carrier only;
- `N_E(a+bJ)=a^2+b^2`;
- `T_{a,b}^{(ij)}=[X_i^aX_j^b]` is the frozen native component-trace identity;
- `Realize_E(T_{a,b}^{(ij)})` has exact cardinality `binom(a+b,a)`;
- native path length is not path-letter count;
- same endpoint does not imply same line;
- no carrier vector identity may be promoted to native geometry.

Do not modify any frozen R061 canonical definition.

## 1. Hard question

Start from the single scalar input

`N = 2500`.

The ordinary scalar square root is

`r = sqrt(N)`.

The research question is:

> Can one define and validate a genuinely algebraic, factorization-driven **path-valued square-root procedure** which begins from `N` / `r`, discovers all native component branches whose norm is `N`, and then produces the exact compressed native path fibers, without seeding those branches by brute-force enumeration?

Hard target:

`SQRT_2500_ALGEBRAICALLY_DISCOVERS_COMPLETE_NATIVE_COMPONENT_AND_PATH_FIBER`

A weaker outcome is allowed if an exact obstruction survives. Do not force completeness.

## 2. Critical anti-cheating requirement — discovery must precede verification

The discovery phase may use only:

- input integer `N=2500`;
- exact scalar square-root test producing `r` if square;
- integer factorization of `r` and/or `N`;
- exact arithmetic in `Z[J]/(J^2+1)`;
- factorization/norm identities;
- canonical Euclid/Gaussian parametrization rules derived from those inputs.

The discovery phase MUST NOT receive any nontrivial solution pair `(a,b)` of `a^2+b^2=N` as an input, constant, expected table, branch list, or branch-count oracle.

A separate verification phase may brute-force `a^2+b^2=N` only AFTER the generative output has been materialized and hashed. There must be no data flow from brute verification back into discovery.

The deterministic checker should make this separation explicit, preferably as two functions/phases:

1. `discover_from_scalar_root(N)`;
2. `verify_against_norm_fiber(N, discovered)`.

If the checker hardcodes nontrivial branch pairs, the stage fails.

## 3. Candidate path-root operators to classify

Compare at least the following.

### C0 — ordinary scalar square root

`N -> r`.

Classify exactly what information this retains and loses.

### C1 — brute inverse-norm fiber baseline

`RootFiber_E(N)={a+bJ : a,b>=0, a^2+b^2=N}`.

This is the completeness oracle/baseline only. It is not accepted by itself as the desired generative square-root mechanism because it merely restates the Diophantine equation.

### C2 — unscaled square lift

Search sector-local algebraic roots `beta=m+nJ` with

`N_E(beta)=r`

and generate

`alpha=beta^2`.

Classify whether this recovers the entire nonnegative ordered norm-`N` fiber. Preserve every missing branch if incomplete.

### C3 — scaled square lift from factorization of the scalar root

Search exact triples `(k,m,n)` generated from the scalar root factorization satisfying

`r = k(m^2+n^2)`

with a canonical primitive/nonprimitive convention made explicit.

Generate

`alpha = k(m+nJ)^2`

so that

`alpha = k(m^2-n^2) + 2kmn J`

up to the exact allowed sector ordering/sign/unit normalization.

Prove or falsify that this operator is complete for the nonnegative ordered norm-`N` branches.

If it is complete, prove why this is not an accidental `N=2500` coincidence. If it is incomplete, preserve the smallest missing branch and explain why.

### C4 — Gaussian/factorization-first lift

Use factorization in `Z[J]` or an equivalent exact norm-factor construction beginning from the integer factorization of `N` or `r`.

Determine whether it produces exactly the same canonical component-root fiber as C3, produces extra derivation provenance for the same branches, or exposes a stronger generative structure.

Do not import a result table from C1.

## 4. Root-channel provenance graph

For every branch discovered from the scalar root, preserve its algebraic derivation provenance.

Distinguish:

- **component-root identity** `alpha=a+bJ`;
- **derivation channel** `(k,m,n, units/sign/order/factor choices, ...)` leading to that same `alpha`;
- **native trace identity** `T_{a,b}^{(ij)}`;
- **native path witnesses** inside `Realize_E(T_{a,b}^{(ij)})`.

Mandatory question:

`ALGEBRAIC_ROOT_DERIVATION_MULTIPLICITY == NATIVE_PATH_MULTIPLICITY ?`

Do not assume equality. They are different layers unless proved otherwise.

If multiple algebraic derivations lead to the same component root, classify whether the path-valued square root should:

- quotient derivation provenance and return one trace branch;
- retain provenance as a higher enrichment;
- or expose another canonical structure.

## 5. Desired square-root-to-path formula

Test whether the following structure can be made exact.

For square input `N=r^2`, define a generated component-root set `GRoot_E(r^2)` from scalar-root factorization only.

For every generated nonnegative ordered branch `(a,b)`, pathify by

`Lambda(a,b)=[u^a v^b](uX_i+vX_j)^(a+b)`

with commuting coefficient markers `u,v` and noncommuting path generators `X_i,X_j`.

Candidate path-valued square root:

`PathSqrt_E(N)=disjoint_union_{(a,b) in GRoot_E(N)} Lambda(a,b)`.

If C3 survives, derive an equivalent factorization-first expression of the form

`r=k(m^2+n^2)`

followed by

`a=k(m^2-n^2)`, `b=2kmn`

and then the exact coefficient extraction.

All sign/order/unit normalization required to recover the full **ordered nonnegative** branch fiber must be explicit.

## 6. `sqrt(2500)` central discovery report

The report must begin from the single input `2500` and show the entire generated tree:

`2500 -> scalar root -> integer/Gaussian factors -> algebraic root channels -> deduplicated component roots -> native trace branches -> compressed path fibers`.

Do not seed any nontrivial branch in the task code or report template.

For every discovered branch output:

- exact `(a,b)`;
- exact `alpha=a+bJ`;
- derivation channel(s);
- exact norm certificate `a^2+b^2=2500`;
- trace ID;
- word length `a+b` as path-letter count only;
- exact fiber cardinality `binom(a+b,a)`;
- first/last deterministic ranked path IDs or combinadic representatives;
- compressed polynomial representation;
- whether the branch was found by C2, C3, C4;
- whether any candidate misses it.

Also output the exact one-sector total path-fiber cardinality across all ordered nonnegative branches.

Because the total fiber may be astronomically large, explicit full-path enumeration is forbidden when infeasible. Use exact integers, combinatorial ranking/unranking and hashes of compressed certificates.

## 7. Completeness and no-extra proof

After discovery is frozen, independently compute the brute baseline

`D_2500={(a,b) in N_0^2 : a^2+b^2=2500}`.

Compare generated vs brute:

- missing branches;
- extra branches;
- duplicate generated roots after canonicalization;
- ordered-vs-unordered confusion;
- unit/conjugation/sign normalization mistakes.

Acceptance requires exact set equality for whichever candidate is claimed complete.

A simple numerical match is not enough: provide a theorem-level explanation of completeness or preserve the exact finite classification only.

## 8. General regression — prove the operator is not tailored to 2500

For every integer `1 <= r <= 512`, compare the surviving factorization-driven square-root generator on `N=r^2` against brute nonnegative ordered norm fibers.

Requirements:

- zero missing branches;
- zero extra branches;
- exact deduplication;
- axis degenerates handled;
- component ordering handled;
- no branch table hardcoded.

If the operator fails for some `r<=512`, preserve the smallest `r` and smallest missing/extra branch and downgrade the theorem accordingly.

This regression may use brute enumeration only as the verifier, never as the generator.

## 9. Compare direct norm-fiber inversion with genuine scalar-root discovery

Explicitly distinguish:

`INVERSE_NORM_FIBER`

from

`SCALAR_ROOT_FACTORIZATION_GENERATOR`.

Mandatory question:

> Is `sqrt_E(N)={alpha:N_E(alpha)=N}` merely a set-valued definition, while the factorization-driven operator provides an actual constructive route from the ordinary scalar root `r` to the component/path fiber?

Classify the answer precisely.

## 10. Information discovered specifically at 2500

Without assuming the answer in advance, inspect whether `2500` reveals structures not visible at `25`, including but not limited to:

- multiple inequivalent nondegenerate component-root channels;
- incomplete unscaled-square lifting;
- scaled-square completion;
- multiple algebraic derivations of one component root;
- huge differences in path-fiber cardinalities between branches;
- concentration/dominance of the total multipath count;
- nested factorization paths from the scalar root into component roots;
- any unexpected symmetry or quotient.

Every such finding must be derived, not postulated.

## 11. BRC is downstream only

After path fibers are derived, it is permitted to report the corresponding R062 projections:

`Path -> N multiplicity -> Boolean support`.

But BRC must not be used to discover component roots or generate paths. This stage is about the algebraic square-root operator itself.

## 12. Deterministic checker — mandatory

Commit an executable checker under `scripts/`.

Minimum requirements:

- exact integer arithmetic only for discovery/classification;
- exact `isqrt` square-root check;
- integer factorization generated from input;
- no hardcoded nontrivial norm-2500 branches;
- two-phase discovery/verification separation;
- C2/C3/C4 candidate comparison;
- independent brute `D_2500` verification after discovery;
- general `r<=512` regression;
- exact big-integer binomial counts;
- deterministic combinadic path rank/unrank samples;
- compressed branch/path certificate hash;
- mismatch file with `mismatch_count` and `smallest_mismatch`;
- preserve classified negative results separately from checker errors.

## 13. Required outputs

At minimum:

- `research_results/R063_STAGE0/R063_STAGE0_SQRT2500_DISCOVERY_TREE.json`
- `research_results/R063_STAGE0/R063_STAGE0_PATH_ROOT_OPERATOR_CANDIDATE_MATRIX.md`
- `research_results/R063_STAGE0/R063_STAGE0_COMPONENT_ROOT_FIBER.json`
- `research_results/R063_STAGE0/R063_STAGE0_SCALED_SQUARE_LIFT_THEOREM.md`
- `research_results/R063_STAGE0/R063_STAGE0_GAUSSIAN_FACTOR_ROUTE_AUDIT.md`
- `research_results/R063_STAGE0/R063_STAGE0_PATH_VALUED_SQRT_FORMULA.md`
- `research_results/R063_STAGE0/R063_STAGE0_PATH_CARDINALITY_CERTIFICATE.json`
- `research_results/R063_STAGE0/R063_STAGE0_DERIVATION_PROVENANCE_GRAPH.json`
- `research_results/R063_STAGE0/R063_STAGE0_GENERAL_SQUARE_REGRESSION.json`
- `research_results/R063_STAGE0/R063_STAGE0_MISMATCHES.json`
- `research_results/R063_STAGE0/R063_STAGE0_REPLAY_SUMMARY.json`
- `research_results/R063_STAGE0/R063_STAGE0_REPRODUCIBILITY_PROOF.md`
- `scripts/r063_stage0_validate_path_valued_sqrt_2500.py`

## 14. Acceptance gates

1. `INPUT_ONLY_DISCOVERY_NO_BRANCH_HARDCODE`
2. `SCALAR_SQRT_2500_EXACT`
3. `SECTOR_NORM_ALGEBRA_TYPED`
4. `C2_UNSCALED_SQUARE_LIFT_CLASSIFIED`
5. `C3_SCALED_SQUARE_LIFT_CLASSIFIED`
6. `C4_GAUSSIAN_FACTOR_ROUTE_CLASSIFIED`
7. `DISCOVERED_COMPONENT_ROOTS_MATCH_D2500_EXACTLY` if completeness is claimed
8. `NO_EXTRA_COMPONENT_ROOTS`
9. `ALGEBRAIC_DERIVATION_VS_NATIVE_PATH_MULTIPLICITY_CLASSIFIED`
10. `PATHIFICATION_FORMULA_EXACT`
11. `HUGE_PATH_FIBER_COMPRESSED_REPRESENTATION_EXACT`
12. `ONE_SECTOR_TOTAL_PATH_CARDINALITY_EXACT`
13. `R061_TRACE_IDENTITY_COMPATIBILITY_PASS`
14. `GENERAL_R_SQUARED_REGRESSION_R_LE_512_PASS_OR_MINIMAL_COUNTEREXAMPLE_PRESERVED`
15. `NO_JUMP_COUNT_AS_NATIVE_LENGTH_LEAKAGE`
16. `NO_CARRIER_VECTOR_RELATION_PROMOTED_TO_NATIVE_IDENTITY`
17. `COMMITTED_DETERMINISTIC_CHECKER_PASS`

## 15. Final classification vocabulary

Return the strongest true statement only. Candidate outcomes include:

- `PATH_VALUED_SQUARE_ROOT_FACTORIZATION_OPERATOR_COMPLETE_FOR_SQUARE_NATIVE_NORMS`
- `SQRT2500_COMPLETE_BUT_GENERAL_OPERATOR_FAILS_AT_R_EQ_<minimal>`
- `SCALED_SQUARE_LIFT_INCOMPLETE_WITH_MINIMAL_MISSING_BRANCH_<...>`
- `INVERSE_NORM_FIBER_COMPLETE_BUT_NO_NONCIRCULAR_SCALAR_ROOT_GENERATOR_FOUND`
- another exact classification forced by the evidence.

Do not use “validated” if only the `N=2500` finite case passed and the claimed theorem is broader.

## 16. Stop rule

Complete Stage 0, commit all evidence, and stop for Driver review.

Do not automatically open R063 Stage 1.
