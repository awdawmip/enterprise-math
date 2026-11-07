# PCF Restricted Routes — External Prior-Art / Duplication Audit (Consolidated Verification)

Status: `FROZEN / TASK-TERMINAL RESEARCH RESULT / SOURCE-BACKED CONSOLIDATION`

Task-ID: `RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`  
Publication-ID: `TP2-D7E01B4B2274498405F8`  
Researcher-ID: `EM-PCFPA-6D9A31`  
Claim-ID: `chatgpt-pcfpriorart-20260908-0010-sol6d9a31-r1`  
Execution-Record-ID: `ER-6D9A31B7C5E20F4A8D13`

## Primary verdict

`PCF5_PCF6_EXTERNAL_PRIOR_ART_AND_DUPLICATION_BOUNDARY_EXACTLY_CLASSIFIED`

This execution takes the fresh unmerged replication `RR-3E98234ADC20423C156D / PR #1361` as the highest durable frontier, checks it against the older unmerged `RR-3D275FA80F4E26F00F3D / PR #1242`, re-reads the frozen PCF5 and PCF6 accepted Results, and independently verifies the load-bearing external antecedents.

The classification is **materially confirmed**. The stronger of the two prior replications is PR #1361 because it repairs two precision defects without changing theorem strength:

1. **PCF5 visibility.** For `L_m=m+2`, `U_m=m^3+m+1`, if `p>=L_m`, the prime itself lies in the partition interval. If `p<L_m`, let `r=p*ceil(L_m/p)`. Then `L_m<=r<L_m+p<=2m+3<=U_m` for `m>=2`; hence a table entry divisible by `p` exists.
2. **PCF6 fixed probes.** If a fixed probe has integer resultant `R!=0`, singularity can occur only at primes dividing `R`. If `R=0`, the probe is singular for every modulus and therefore non-separating. A finite fixed `H`-independent family therefore cannot universally encode arbitrary semiprime splits; no statement is made about genuinely `H`-dependent probes.

No row is classified `NO_MATERIAL_MATCH`; this audit makes **no historical novelty finding**.

## BRC observer / provenance gate

Resolution: `REUSE_APPLIED`.

The BRC policy is used here as an information-preservation discipline, not as a substitute for algebraic or historical evidence. The population is the 20 comparison rows. The carrier retains `row_id`, route, exact frozen theorem scope, antecedent class, citations, surviving typed residue, and scope guards. The permitted future operations are Driver verification and later theorem/novelty language.

A one-bit compression such as `NOVEL` / `NOT_NOVEL` is rejected: it would erase the exact distinction between classical machinery and project-specific typed residue. The row-level matrix is the smallest adequate observer for this task.

## Frozen accepted scope

### PCF5

Freeze `RR-D4F90C15C5BB4261230D` only at its restricted fixed-public-`kappa` support-compression scope:

- `m=max(2,ceil((kappa*N)^(1/6)))`;
- exactly `m^2=O_kappa(N^(1/3))` cells;
- exact partition `[m+2,m^3+m+1]`;
- prime visibility iff `p<=m^3+m+1`;
- all-prime-divisor coverage only under `P^+(N)^2<=kappa*N`;
- the batch polynomial-evaluation/gcd interface;
- guard `N=2018=2*1009`, `kappa=4`, `m=5`, `U_m=131`.

This is not a universal factorization algorithm, speedup, or factoring lower bound.

### PCF6

Freeze `RR-6F3A91D2C5E74B08A621` only at the corrected free-rank-2 oriented mixed-realization scope:

- `A_H=(Z/HZ)[X]/((X^2+1)(X^2+X+1))`;
- in the corrected grammar the selector is `c=-tr(T)`;
- `CORRECTED_ORIENTED_MIXED_REALIZATION <=> NONTRIVIAL_CRT_IDEMPOTENT`;
- synchronized ambient determinant/rank families;
- finite fixed `H`-independent polynomial-determinant probes reduce to fixed integer resultants;
- frozen root-count and `H=91` witnesses.

This is not a factorization speedup, factoring lower bound, or general impossibility theorem for `H`-dependent constructions.

## Cited comparison matrix

| ID | Ingredient | Classification | Evidence / consequence |
|---|---|---|---|
| P5-1 | block product polynomial -> fast multipoint evaluation -> gcd per block | `EXACT_ANTECEDENT` | S1, S2: The extraction skeleton is classical; project coordinates do not create a new factorization mechanism. |
| P5-2 | m factors per block and m^2 evaluation blocks with m≈N^(1/6), covering m^3 candidates | `STRICT_ANTECEDENT` | S1, S2: The rectangular m-by-m^2 organization is a restricted project parameterization. Its O_kappa(N^(1/3)) support count is not a factoring runtime claim or speedup. |
| P5-3 | subproduct-tree fast multipoint evaluation | `EXACT_ANTECEDENT` | S3: The fast-evaluation implementation is standard. |
| P5-4 | batch-gcd-adjacent product/remainder-tree arithmetic | `STRICT_ANTECEDENT` | S4, S12: The same-modulus PCF5 cell-gcd list is not literally the many-moduli batch-gcd problem, but the batching machinery is classical. |
| P5-5 | exact cells C_ij={1+i+mj+km^2} partition [m+2,m^3+m+1] | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof / frozen witness: Retain only as the exact Perfect-Prime-Table coordinate interface; project-local typing is not historical novelty. |
| P5-6 | prime visibility iff p<=U_m=m^3+m+1 | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof / frozen witness: Exact proof: if p>=m+2 then p itself lies in the partition interval; if p<m+2, r=p*ceil((m+2)/p) satisfies m+2<=r< m+2+p <=2m+3<=U_m for m>=2. This is a table-interface boundary, not a new factoring principle. |
| P5-7 | fixed-kappa coverage P^+(N)^2<=kappa*N with m^2=O_kappa(N^(1/3)) cells | `PROJECT_SPECIFIC_TYPED_RESIDUE` | S1, S2: Retain only the exact covered-family support theorem. Never convert support cardinality into a factoring speedup claim. |
| P5-8 | when a block gcd equals N, refine inside that block by gcd descent | `EXACT_ANTECEDENT` | S1: The refinement rule is classical. |
| P5-9 | N=2018=2*1009 guard and full-layer Omega(N^(2/3)) universal-visibility obstruction | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof / frozen witness: Retain only as a full-layer interface obstruction; it is not a general integer-factorization lower bound. |
| P6-1 | R_H[X]/(fg) product decomposition from comaximality | `EXACT_ANTECEDENT` | S5: The ambient product decomposition is standard CRT. |
| P6-2 | coefficient CRT for H=pq / product-ring split | `EXACT_ANTECEDENT` | S5: The hidden-factor product structure is standard. |
| P6-3 | nontrivial selector idempotent c=(0 mod p,1 mod q) and gcd(c,H) factor extraction | `EXACT_ANTECEDENT` | S5, S6: A nontrivial idempotent already carries factor-equivalent CRT information. |
| P6-4 | h_c=(1-c)f+c g idempotent gluing | `STANDARD_METHOD_REPACKAGING` | S5, S6: The formula is project notation for standard CRT gluing. |
| P6-5 | c=-tr(T), det(T)=1 and converse companion realization | `STANDARD_METHOD_REPACKAGING` | S7, S8: Trace/determinant readout and converse realization are standard linear algebra. |
| P6-6 | corrected Gaussian/Eisenstein oriented free-rank-2 realization iff nontrivial CRT idempotent | `PROJECT_SPECIFIC_TYPED_RESIDUE` | S5, S6, S7, S8: The exact grammar-specific equivalence remains a useful typed boundary; it is not a general H-dependent no-go theorem. |
| P6-7 | ambient order 12 and fused root counts 4,8,16 at frozen scope | `STANDARD_METHOD_REPACKAGING` | S5, S9: The root census is standard finite-field/cyclotomic arithmetic expressed in project notation. |
| P6-8 | det(P(T_H))=Res(F,P) mod H for fixed P | `EXACT_ANTECEDENT` | S10, S11: The determinant/resultant identity is standard; no novelty attaches to it. |
| P6-9 | a finite family of fixed H-independent determinant probes cannot universally separate semiprimes | `STANDARD_METHOD_REPACKAGING` | S10, S11: If a fixed resultant R is nonzero, only finitely many primes divide R; choose semiprime factors outside that finite support and every probe is a unit. If R=0, the probe is singular for every modulus and is non-separating. Thus a finite fixed family cannot encode arbitrary hidden semiprime splits. This says nothing about H-dependent probes. |
| P6-10 | H=91, c=78 mixed-root pressure witness | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof / frozen witness: Validation witness only; it carries no novelty authority. |
| P6-11 | N_ONLY_NONTRIVIAL_IDEMPOTENT_OR_EQUIVALENT_SELECTOR_GENERATOR routing label | `PROJECT_SPECIFIC_TYPED_RESIDUE` | S5, S6: Keep only as a project routing label for generating asymmetry from H; do not present idempotents themselves as new mathematics. |

## Exact surviving project-local boundary

### PCF5 residue

After Strassen/Pollard-Strassen fast-polynomial factoring and standard product/remainder-tree batching are removed, the useful residue is only the typed Perfect-Prime-Table interface:

1. the exact mixed-radix cell embedding and partition;
2. the exact visibility boundary `p<=m^3+m+1`, with the bounded-multiple proof above;
3. the fixed-public-`kappa` covered-family implication `P^+(N)^2<=kappa*N`;
4. the `N=2018` guard and the `Omega(N^(2/3))` obstruction **only for universal visibility by the full table layer**.

The `O_kappa(N^(1/3))` support cardinality is not an algorithmic runtime claim. Classical deterministic factoring already used fast polynomial multiplication/multipoint evaluation at approximately the `N^(1/4)` scale, with later improvements beyond that historical bound.

### PCF6 residue

After CRT, idempotents, product-ring gluing, rank-2 trace/determinant identities, companion realization, finite-field cyclicity and resultant machinery are removed, the useful residue is only the typed corrected-carrier boundary:

> In the particular corrected Gaussian/Eisenstein oriented free-rank-2 grammar, the local characteristic-polynomial split forces `c=-tr(T)`, and conversely that selector constructs the carrier; within this grammar the mixed realization is equivalent to exposing a nontrivial CRT idempotent.

The primitive idempotent and the linear-algebra machinery are standard. The remaining statement is useful because it pins down exactly where hidden orientation enters this project grammar.

For fixed `H`-independent determinant probes, the zero/nonzero-resultant split above gives a narrow scope guard only. It does not rule out `H`-dependent selectors.

## Novelty / superiority kill list

Rejected interpretations:

- `PCF5_NEW_FACTORING_MECHANISM`;
- `PCF5_FACTORING_SPEEDUP_FROM_N_ONE_THIRD_SUPPORT`;
- `PRODUCT_TREE_REMAINDER_TREE_OR_BATCH_GCD_NOVELTY`;
- `PCF6_CRT_PRODUCT_RING_OR_IDEMPOTENT_NOVELTY`;
- `PCF6_TRACE_DETERMINANT_SELECTOR_NOVELTY_AS_LINEAR_ALGEBRA`;
- `PCF6_RESULTANT_DETERMINANT_NOVELTY`;
- `PCF6_GENERAL_H_DEPENDENT_IMPOSSIBILITY`;
- `PROJECT_SPECIFIC_TYPED_RESIDUE => HISTORICAL_NOVELTY`.

## Source register

- **[S1]** Markus Hittmeir, *A babystep-giantstep method for faster deterministic integer factorization*. Abstract and recalled Strassen method: deterministic fast-polynomial factoring at soft-O(N^(1/4)) scale. https://arxiv.org/abs/1608.08766
- **[S2]** Markus Hittmeir, *Integer factorization as subset-sum problem*. Introduction: Pollard and Strassen use fast polynomial multiplication and multipoint evaluation; historical deterministic soft-O(N^(1/4)) bound. https://doi.org/10.1016/j.jnt.2023.02.010
- **[S3]** FLINT project, *nmod_poly — multipoint evaluation*. Fast multipoint evaluation builds or consumes a subproduct tree. https://flintlib.org/doc/nmod_poly.html
- **[S4]** Daniel J. Bernstein / FactHacks, *Batch gcd, product tree and remainder tree material*. Product/remainder trees are standard batching subroutines for simultaneous gcd-style factor discovery. https://cr.yp.to/talks/2012.12.28/slides.pdf
- **[S5]** The Stacks Project, *Chinese remainder theorem*. Tag 00DT: pairwise comaximal ideals yield quotient/product decompositions. https://stacks.math.columbia.edu/tag/00DT
- **[S6]** The Stacks Project, *Idempotents and product decompositions*. Tag 00EM: complementary idempotents encode product decompositions. https://stacks.math.columbia.edu/tag/00EM
- **[S7]** MIT OpenCourseWare, *Eigenvalues and the Characteristic Equation of a Matrix*. For a 2x2 matrix, characteristic polynomial is x^2-Tr(A)x+det(A). https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter04/section06.html
- **[S8]** Wolfram MathWorld, *Companion Matrix*. A monic polynomial is the characteristic polynomial of its companion matrix. https://mathworld.wolfram.com/CompanionMatrix.html
- **[S9]** The Stacks Project, *Finite fields*. Tag 09HY: F_q^* is cyclic of order q-1. https://stacks.math.columbia.edu/tag/09HY
- **[S10]** David A. Cox; John Little; Donal O'Shea, *Using Algebraic Geometry, 2nd ed.*. Resultant as determinant of the multiplication map / norm-type construction in the quotient algebra. https://eclass.uoa.gr/modules/document/file.php/D231/Papers/Cox-UsingAlgebraicGeometry.pdf
- **[S11]** The Stacks Project, *Determinants of endomorphisms of finite length modules*. Tag 0GSZ: determinant of multiplication equals a norm, supporting the standard determinant-of-multiplication viewpoint. https://stacks.math.columbia.edu/tag/0GSZ
- **[S12]** Daniel J. Bernstein, *How to find small factors of integers*. Classical product/remainder-tree and batched small-factor machinery. https://cr.yp.to/papers/sf-20020923-retypeset20220327.pdf

## Replication disposition

`RR-3E98234ADC20423C156D / PR #1361` is independently confirmed at the classification level and is stronger than `RR-3D275FA80F4E26F00F3D / PR #1242` only in precision of exposition: P5-6 uses the exact bounded-multiple proof, and P6-9 explicitly handles `R=0`. Neither repair strengthens PCF5 or PCF6.

`method_harvest = NO_TOOL_PAYLOAD`  
`independence_status = INDEPENDENT_CONSOLIDATION_OF_TWO_UNMERGED_FRONTIERS`  
`source_exposure_status = NONBLIND_DISCLOSED`

Smallest remaining control step: Driver review may close the shared prior-art gate at this typed-residue boundary. No mathematical residue remains inside the audit task itself.
