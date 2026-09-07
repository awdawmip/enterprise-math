# PCF Restricted Routes — External Prior-Art / Duplication Audit (Current-Main Recovery Re-freeze)

Status: `FROZEN / TASK-TERMINAL-RESEARCHER / SOURCE-ANCHOR-RECHECKED`

Task-ID: `RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`  
Publication-ID: `TP2-D7E01B4B2274498405F8`  
Researcher-ID: `EM-PCFPRIORART-A93F52`  
Claim-ID: `chatgpt-pcfpriorart-20260908-0010-sola93f52`  
Execution-Record-ID: `ER-DD6E66946D5EC47C2FCE`

## Primary verdict

`PCF5_PCF6_EXTERNAL_PRIOR_ART_AND_DUPLICATION_BOUNDARY_EXACTLY_CLASSIFIED`

This execution consumes, rather than replays, the verified durable 20-row classification in `RR-3E98234ADC20423C156D / PR #1361`, together with its earlier precursor `RR-3D275FA80F4E26F00F3D / PR #1242`. The current claim rechecked the load-bearing public source anchors against the exact frozen PCF5 and PCF6 inputs and found **no classification drift**.

Two previously repaired precision points remain frozen without mathematical strengthening:

1. **PCF5 visibility:** for `p <= U_m=m^3+m+1`, if `p >= L_m=m+2`, the prime `p` itself lies in the partition interval; if `p<L_m`, then `r=p*ceil(L_m/p)` satisfies `L_m <= r < L_m+p <= 2m+3 <= U_m`.
2. **PCF6 fixed probes:** for a fixed `H`-independent probe with integer resultant `R`, `R!=0` gives finite prime support; `R=0` makes the probe uniformly singular/zero and non-separating.

No row is classified `NO_MATERIAL_MATCH`. This audit therefore makes **no historical novelty finding** and creates no speedup, lower-bound, or general `H`-dependent impossibility claim.

## Recovery classification

- `RR-3E98234ADC20423C156D / PR #1361`: `VERIFIED_COMPLETE` at the 20-row prior-art classification frontier.
- `RR-3D275FA80F4E26F00F3D / PR #1242`: retained as earlier durable provenance, not as current authority.
- Current smallest unfinished unit: current-main source-anchor verification, BRC observer/provenance freeze, current-claim execution/result records, and Driver handoff.
- Mathematical replay of the 20 rows: **not performed and not required**.

## BRC applicability / observer audit

Resolution: `REUSE_APPLIED`.

The BRC carrier here is not a new factoring construction. The population is the 20 load-bearing ingredient rows; branch identity is `(row_id, route, ingredient)`; observed output is `(classification, strongest antecedent, source_ids, exact scope consequence)`; the allowed future operation is independent Driver verification and gate closure.

The forbidden compression is to replace the rowwise state by a single label such as “novel” or “standard”. Such a quotient would erase the scientifically load-bearing fiber contrast between classical machinery and project-specific typed residues. Accordingly:

`STANDARD_ANTECEDENT_MECHANISM + PROJECT_SPECIFIC_TYPED_RESIDUE != HISTORICAL_NOVELTY`.

Row provenance, exact theorem scope, and zero/nonzero-resultant branching are retained through the audit.

## Frozen accepted scope

### PCF5

Freeze `RR-D4F90C15C5BB4261230D` only at the restricted fixed-`kappa` covered-family support-compression strength:

- `m=max(2,ceil((kappa*N)^(1/6)))`;
- `m^2=O_kappa(N^(1/3))` table cells;
- exact partition `[m+2,m^3+m+1]`;
- visibility iff `p<=m^3+m+1`;
- all-prime-divisor coverage only under `P^+(N)^2<=kappa*N`;
- standard batch polynomial evaluation/gcd interface;
- unbalanced regression `N=2018=2*1009`, `kappa=4`, `m=5`, `U_m=131`;
- no universal factoring algorithm, factoring speedup, or factoring lower bound.

### PCF6

Freeze `RR-6F3A91D2C5E74B08A621` only at the corrected oriented free-rank-2 mixed-realization obstruction:

- `A_H=(Z/HZ)[X]/((X^2+1)(X^2+X+1))`;
- within the corrected oriented free-rank-2 grammar, the hidden selector is `c=-tr(T)`;
- at that grammar, `CORRECTED_ORIENTED_MIXED_REALIZATION <=> NONTRIVIAL_CRT_IDEMPOTENT`;
- synchronized ambient determinant/rank families;
- finite fixed `H`-independent polynomial-determinant probes reduce to fixed integer resultants;
- frozen root-count and `H=91` regression witnesses;
- no factoring speedup, factoring lower bound, or general impossibility for genuinely `H`-dependent constructions.

## Cited comparison matrix

| ID | Ingredient | Class | Evidence / boundary |
|---|---|---|---|
| P5-1 | block product polynomial -> fast multipoint evaluation -> gcd per block | `EXACT_ANTECEDENT` | S1, S2. The load-bearing extraction skeleton is classical; project notation does not create a new factorization mechanism. |
| P5-2 | m factors per block and m^2 evaluation blocks with m≈N^(1/6), covering m^3 candidates | `STRICT_ANTECEDENT` | S1, S2. PCF5's rectangular m-by-m^2 parameterization is a restricted specialization/reparameterization; it is not a factoring speedup. |
| P5-3 | subproduct/remainder-tree fast multipoint evaluation | `EXACT_ANTECEDENT` | S3. The fast-evaluation implementation is standard. |
| P5-4 | batch-gcd-adjacent product/remainder-tree arithmetic | `STRICT_ANTECEDENT` | S4, S12. The same-modulus PCF5 cell-gcd list is not literally the many-moduli batch-gcd problem, but its batching machinery is classical. |
| P5-5 | exact cells C_ij={1+i+mj+km^2} partition [m+2,m^3+m+1] | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof/witness. Retain as an exact table-coordinate lemma only; project-local typing is not historical novelty. |
| P5-6 | prime visibility iff p<=U_m=m^3+m+1 | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof/witness. If p>=m+2, p itself lies in the interval; if p<m+2, r=p*ceil((m+2)/p) lies in [m+2,U_m]. This is an exact table-interface boundary, not a new factoring principle. |
| P5-7 | fixed-kappa coverage P^+(N)^2<=kappa*N with m^2=O_kappa(N^(1/3)) cells | `PROJECT_SPECIFIC_TYPED_RESIDUE` | S1, S2. Retain only the exact coverage theorem for this table support; never advertise O_kappa(N^(1/3)) support as a factoring speedup. |
| P5-8 | when a block gcd equals N, refine inside that block by gcd descent | `EXACT_ANTECEDENT` | S1. The refinement rule is classical. |
| P5-9 | N=2018=2*1009 guard and full-layer Omega(N^(2/3)) universal-visibility obstruction | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof/witness. Retain only as a full-layer interface obstruction; it is not a general integer-factorization lower bound. |
| P6-1 | R_H[X]/(fg) product decomposition from comaximality | `EXACT_ANTECEDENT` | S5. The ambient product decomposition is standard CRT. |
| P6-2 | coefficient CRT for H=pq / product-ring split | `EXACT_ANTECEDENT` | S5. The hidden-factor product structure is standard. |
| P6-3 | nontrivial selector idempotent c=(0 mod p,1 mod q) and gcd(c,H) factor extraction | `EXACT_ANTECEDENT` | S5, S6. A nontrivial idempotent already carries factor-equivalent CRT information. |
| P6-4 | h_c=(1-c)f+c g idempotent gluing | `STANDARD_METHOD_REPACKAGING` | S5, S6. The formula is project notation for standard CRT gluing. |
| P6-5 | c=-tr(T), det(T)=1 and converse companion realization | `STANDARD_METHOD_REPACKAGING` | S7, S8. Trace/determinant readout and converse realization are standard linear algebra. |
| P6-6 | corrected Gaussian/Eisenstein oriented free-rank-2 realization iff nontrivial CRT idempotent | `PROJECT_SPECIFIC_TYPED_RESIDUE` | S5, S6, S7, S8. The exact grammar-specific equivalence remains a useful project boundary; it is not a general H-dependent no-go theorem. |
| P6-7 | ambient order 12 and fused root counts 4,8,16 at the frozen admissible scope | `STANDARD_METHOD_REPACKAGING` | S5, S9. The root census is standard finite-field/cyclotomic arithmetic expressed in project notation. |
| P6-8 | det(P(T_H))=Res(F,P) mod H for fixed P | `EXACT_ANTECEDENT` | S8, S10, S11. The determinant/resultant identity is standard; no novelty attaches to it. |
| P6-9 | a finite family of fixed H-independent determinant probes cannot universally separate semiprimes | `STANDARD_METHOD_REPACKAGING` | S10, S11. If a fixed resultant is nonzero, only its finitely many prime divisors can affect vanishing/invertibility; if zero, the probe is uniformly singular and non-separating. This is limited to fixed H-independent probes. |
| P6-10 | H=91, c=78 mixed-root pressure witness | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof/witness. Validation witness only; it carries no novelty authority. |
| P6-11 | N_ONLY_NONTRIVIAL_IDEMPOTENT_OR_EQUIVALENT_SELECTOR_GENERATOR routing label | `PROJECT_SPECIFIC_TYPED_RESIDUE` | S5, S6. Keep only as a project routing label for generating asymmetry from H; do not present idempotents themselves as new mathematics. |

The machine-readable copy is `research_artifacts/PCF_RESTRICTED_ROUTES_EXTERNAL_PRIOR_ART_DUPLICATION_AUDIT/comparison_matrix_20260908.json`.

## Exact surviving project-local boundary

### PCF5 residue

After Pollard-Strassen/Strassen fast-polynomial factoring and standard product/remainder-tree machinery are removed, the useful residue is only the typed Perfect-Prime-Table interface:

1. exact mixed-radix cell embedding and partition;
2. exact visibility boundary `p<=m^3+m+1` with the two-case proof;
3. fixed-public-`kappa` covered-family implication `P^+(N)^2<=kappa*N`;
4. the `2018` regression and `Omega(N^(2/3))` obstruction **only for universal visibility by the full table layer**.

The support cardinality `O_kappa(N^(1/3))` is not a factoring-runtime improvement. Classical deterministic fast-polynomial factoring already has substantially stronger unrestricted complexity antecedents.

### PCF6 residue

After CRT, complementary idempotents, product-ring gluing, rank-2 trace/determinant identities, companion matrices, finite-field cyclicity and resultant machinery are removed, the useful residue is only:

> In the particular corrected Gaussian/Eisenstein oriented free-rank-2 grammar, the required local characteristic-polynomial split forces the selector `c=-tr(T)`, and conversely that selector constructs the carrier; hence the grammar-specific realization is equivalent to exposing a nontrivial CRT idempotent.

This locates the project-specific typed boundary. It is not a no-go theorem for arbitrary `H`-dependent constructions.

For a finite fixed family of `H`-independent determinant probes, each probe reduces to a fixed integer resultant. A nonzero resultant has finite prime support; a zero resultant is uniformly singular and non-separating. The obstruction is strictly limited to that fixed-probe class.

## Novelty / superiority kill list

Reject:

- `PCF5_NEW_FACTORING_MECHANISM`;
- `PCF5_FACTORING_SPEEDUP_FROM_N_ONE_THIRD_SUPPORT`;
- `PCF5_PRODUCT_TREE_REMAINDER_TREE_OR_BATCH_GCD_NOVELTY`;
- `PCF6_CRT_PRODUCT_RING_OR_IDEMPOTENT_NOVELTY`;
- `PCF6_TRACE_DETERMINANT_SELECTOR_NOVELTY_AS_LINEAR_ALGEBRA`;
- `PCF6_RESULTANT_DETERMINANT_NOVELTY`;
- `PCF6_GENERAL_H_DEPENDENT_IMPOSSIBILITY`;
- `PROJECT_SPECIFIC_TYPED_RESIDUE => HISTORICAL_NOVELTY`.

## Source register

- **[S1]** Markus Hittmeir, *A babystep-giantstep method for faster deterministic integer factorization*. Abstract: Strassen's deterministic rigorous factorization uses fast polynomial arithmetic and runs at soft-O(N^(1/4)) scale. https://arxiv.org/abs/1608.08766
- **[S2]** Markus Hittmeir, *Integer factorization as subset-sum problem*. Introduction: Pollard and Strassen use fast polynomial multiplication and multipoint evaluation; later deterministic bounds improve the 1/4 exponent. https://doi.org/10.1016/j.jnt.2023.02.010
- **[S3]** FLINT project, *nmod_poly — fast multipoint evaluation*. Fast multipoint evaluation builds a temporary subproduct tree; precomputed variant consumes a subproduct tree. https://flintlib.org/doc/nmod_poly.html
- **[S4]** FactHacks / Bernstein et al., *Remainder tree*. Remainder trees use product trees and are an important batch-gcd subroutine. https://facthacks.cr.yp.to/remainder.html
- **[S5]** The Stacks Project, *Chinese remainder theorem*. Tag 00DT: pairwise comaximal ideals yield quotient/product decomposition. https://stacks.math.columbia.edu/tag/00DT
- **[S6]** The Stacks Project, *Idempotents and product decompositions*. Tag 00EM: an idempotent e yields the complementary product decomposition by e and 1-e. https://stacks.math.columbia.edu/tag/00EM
- **[S7]** Wolfram MathWorld, *Characteristic Polynomial*. For a 2x2 matrix the characteristic polynomial is x^2-Tr(A)x+det(A). https://mathworld.wolfram.com/CharacteristicPolynomial.html
- **[S8]** Wolfram MathWorld, *Companion Matrix*. A monic polynomial's companion matrix has that polynomial as characteristic polynomial. https://mathworld.wolfram.com/CompanionMatrix.html
- **[S9]** The Stacks Project, *Finite fields*. Tag 09HY: F_q^* is cyclic of order q-1. https://stacks.math.columbia.edu/tag/09HY
- **[S10]** Wolfram MathWorld, *Resultant*. The resultant has the standard root-product definition and equals a Sylvester determinant. https://mathworld.wolfram.com/Resultant.html
- **[S11]** Wolfram MathWorld, *Sylvester Matrix*. The determinant of the Sylvester matrix is the resultant. https://mathworld.wolfram.com/SylvesterMatrix.html
- **[S12]** Daniel J. Bernstein / FactHacks, *Product/remainder-tree batch arithmetic*. Standard product/remainder-tree batching surface used by batch-gcd style algorithms. https://facthacks.cr.yp.to/remainder.html

## Current-claim disposition

`method_harvest = BRC_REUSE_APPLIED_AS_PROVENANCE_OBSERVER_GATE`  
`independence_status = RECOVERY_CONSOLIDATION_WITH_CURRENT_SOURCE_ANCHOR_RECHECK`  
`source_exposure_status = NONBLIND_DISCLOSED`  
`mathematical_delta = NONE`

The researcher's hard target is complete. The remaining authority step is Driver review: compare this current-main recovery Result with `RR-3E98234ADC20423C156D / PR #1361` and `RR-3D275FA80F4E26F00F3D / PR #1242`; if accepted, close the shared external-prior-art gate exactly at the typed-residue boundary. No stronger novelty, speedup, lower-bound, or general `H`-dependent impossibility interpretation is authorized.
