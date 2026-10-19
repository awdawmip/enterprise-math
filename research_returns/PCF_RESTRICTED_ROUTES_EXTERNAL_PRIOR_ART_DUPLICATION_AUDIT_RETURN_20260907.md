# PCF Restricted Routes — External Prior-Art / Duplication Audit (Independent Re-freeze)

Status: `FROZEN / TASK-TERMINAL / SOURCE-BACKED REPLICATION`

Task-ID: `RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`  
Publication-ID: `TP2-D7E01B4B2274498405F8`  
Researcher-ID: `EM-EBP6JT-25C94A`  
Claim-ID: `chatgpt-pcfpriorart-20260907-1012-sol25c94a`  
Execution-Record-ID: `ER-A27D58E659127CDE4B01`

## Primary verdict

`PCF5_PCF6_EXTERNAL_PRIOR_ART_AND_DUPLICATION_BOUNDARY_EXACTLY_CLASSIFIED`

This execution independently re-audited the highest durable frontier left by unmerged Result `RR-3D275FA80F4E26F00F3D`. The prior 20-row classification is **materially confirmed**, but this freeze tightens two statements that were too compressed in the earlier prose:

1. **PCF5 visibility:** `p <= U_m` is not justified by the loose slogan that an arbitrary interval contains a multiple of every prime. The exact proof is two-case: if `p >= L_m=m+2`, the prime `p` itself lies in the partition interval; if `p<L_m`, then `r=p*ceil(L_m/p)` satisfies `L_m <= r < L_m+p <= 2m+3 <= U_m`, so a divisible table entry exists.
2. **PCF6 fixed probes:** for a fixed `H`-independent probe with integer resultant `R`, the finite-prime-support argument applies when `R != 0`; when `R=0`, the probe is identically singular/zero across moduli and has no separating power. This closes the zero-resultant loophole without broadening the theorem.

No row is classified `NO_MATERIAL_MATCH`. Therefore this audit makes **no historical novelty finding**.

## Frozen accepted scope

### PCF5

Freeze accepted Result `RR-D4F90C15C5BB4261230D` only at `RESTRICTED_SUPPORT_COMPRESSION_PROVED / FIXED_KAPPA_COVERED_FAMILY_ONLY`:

- `m=max(2,ceil((kappa*N)^(1/6)))`;
- `m^2=O_kappa(N^(1/3))` table cells;
- exact cell partition `[m+2,m^3+m+1]`;
- visibility iff `p<=m^3+m+1`;
- all-prime-divisor coverage only under `P^+(N)^2<=kappa*N`;
- batch polynomial evaluation/gcd interface;
- explicit unbalanced guard `N=2018=2*1009`, `kappa=4`, `m=5`, `U_m=131`;
- no universal factoring algorithm, factoring speedup, or factoring lower bound.

### PCF6

Freeze accepted Result `RR-6F3A91D2C5E74B08A621` only at `FUNCTORIAL_REALIZATION_OBSTRUCTED / CORRECTED_FREE_RANK_2_ORIENTED_MIXED_REALIZATION_ONLY`:

- `A_H=(Z/HZ)[X]/((X^2+1)(X^2+X+1))`;
- within the corrected oriented free-rank-2 grammar, the hidden selector is `c=-tr(T)`;
- at that grammar, `CORRECTED_ORIENTED_MIXED_REALIZATION <=> NONTRIVIAL_CRT_IDEMPOTENT`;
- synchronized ambient determinant/rank families;
- finite fixed `H`-independent polynomial-determinant probes reduce to fixed integer resultants;
- frozen root-count and `H=91` regression witnesses;
- no factoring speedup, factoring lower bound, or general impossibility for genuinely `H`-dependent constructions.

## Comparison matrix

| ID | Ingredient | Classification | Evidence / consequence |
|---|---|---|---|
| P5-1 | block product polynomial -> fast multipoint evaluation -> gcd per block | `EXACT_ANTECEDENT` | S1, S2: The load-bearing extraction skeleton is classical; project notation does not create a new factorization mechanism. |
| P5-2 | m factors per block and m^2 evaluation blocks with m≈N^(1/6), covering m^3 candidates | `STRICT_ANTECEDENT` | S1, S2: PCF5's rectangular m-by-m^2 parameterization is a restricted reparameterization; it is not a speedup and is asymptotically weaker than classical unrestricted factoring bounds. |
| P5-3 | subproduct/remainder-tree fast multipoint evaluation | `EXACT_ANTECEDENT` | S3: The fast-evaluation implementation is standard. |
| P5-4 | batch-gcd-adjacent product/remainder-tree arithmetic | `STRICT_ANTECEDENT` | S4, S12: The same-modulus PCF5 cell-gcd list is not literally the many-moduli batch-gcd problem, but its batching machinery is classical. |
| P5-5 | exact cells C_ij={1+i+mj+km^2} partition [m+2,m^3+m+1] | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof/witness: Retain as an exact table-coordinate lemma only; project-local typing is not historical novelty. |
| P5-6 | prime visibility iff p<=U_m=m^3+m+1 | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof/witness: Precise proof: if p>=m+2, p itself lies in the partition interval; if p<m+2, r=p*ceil((m+2)/p) lies in [m+2,U_m]. This is an exact table-interface boundary, not a new factoring principle. |
| P5-7 | fixed-kappa coverage P^+(N)^2<=kappa*N with m^2=O_kappa(N^(1/3)) cells | `PROJECT_SPECIFIC_TYPED_RESIDUE` | S1, S2: Retain only the exact coverage theorem for this table support; never advertise O_kappa(N^(1/3)) support as a factoring speedup. |
| P5-8 | when a block gcd equals N, refine inside that block by gcd descent | `EXACT_ANTECEDENT` | S1: The refinement rule is classical. |
| P5-9 | N=2018=2*1009 guard and full-layer Omega(N^(2/3)) universal-visibility obstruction | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof/witness: Retain only as a full-layer interface obstruction; it is not a general integer-factorization lower bound. |
| P6-1 | R_H[X]/(fg) product decomposition from comaximality | `EXACT_ANTECEDENT` | S5: The ambient product decomposition is standard CRT. |
| P6-2 | coefficient CRT for H=pq / product-ring split | `EXACT_ANTECEDENT` | S5: The hidden-factor product structure is standard. |
| P6-3 | nontrivial selector idempotent c=(0 mod p,1 mod q) and gcd(c,H) factor extraction | `EXACT_ANTECEDENT` | S5, S6: A nontrivial idempotent already carries factor-equivalent CRT information. |
| P6-4 | h_c=(1-c)f+c g idempotent gluing | `STANDARD_METHOD_REPACKAGING` | S5, S6: The formula is project notation for standard CRT gluing. |
| P6-5 | c=-tr(T), det(T)=1 and converse companion realization | `STANDARD_METHOD_REPACKAGING` | S7, S8: Trace/determinant readout and converse realization are standard linear algebra. |
| P6-6 | corrected Gaussian/Eisenstein oriented free-rank-2 realization iff nontrivial CRT idempotent | `PROJECT_SPECIFIC_TYPED_RESIDUE` | S5, S6, S7, S8: The exact grammar-specific equivalence remains a useful project boundary; it is not a general H-dependent no-go theorem. |
| P6-7 | ambient order 12 and fused root counts 4,8,16 at the frozen admissible scope | `STANDARD_METHOD_REPACKAGING` | S5, S9: The root census is standard finite-field/cyclotomic arithmetic expressed in project notation. |
| P6-8 | det(P(T_H))=Res(F,P) mod H for fixed P | `EXACT_ANTECEDENT` | S8, S10, S11: The determinant/resultant identity is standard; no novelty attaches to it. |
| P6-9 | a finite family of fixed H-independent determinant probes cannot universally separate semiprimes | `STANDARD_METHOD_REPACKAGING` | S10, S11: Precision guard: if a fixed resultant is nonzero, only its finitely many prime divisors can affect vanishing/invertibility; if it is zero, that probe vanishes for every modulus and carries no separating information. Hence a finite fixed family cannot encode arbitrary hidden semiprime splits. This says nothing about H-dependent probes. |
| P6-10 | H=91, c=78 mixed-root pressure witness | `PROJECT_SPECIFIC_TYPED_RESIDUE` | project-internal exact proof/witness: Validation witness only; it carries no novelty authority. |
| P6-11 | N_ONLY_NONTRIVIAL_IDEMPOTENT_OR_EQUIVALENT_SELECTOR_GENERATOR routing label | `PROJECT_SPECIFIC_TYPED_RESIDUE` | S5, S6: Keep only as a project routing label for generating asymmetry from H; do not present idempotents themselves as new mathematics. |

## Exact surviving project-local boundary

### PCF5 residue

After classical Pollard-Strassen/Strassen fast-polynomial factoring and standard product/remainder-tree machinery are removed, the useful residue is only the **typed Perfect-Prime-Table interface**:

1. the mixed-radix partition of the exact cells;
2. the exact visibility boundary `p<=m^3+m+1`, with the two-case proof above;
3. the fixed-public-`kappa` coverage implication `P^+(N)^2<=kappa*N`;
4. the unbalanced `2018` regression and the `Omega(N^(2/3))` obstruction **only for universal visibility by the full table layer**.

The batching implementation is classical. The `O_kappa(N^(1/3))` support cardinality is not an algorithmic speedup metric; public historical summaries already place Pollard-Strassen/Strassen deterministic factoring at approximately `N^(1/4)` scale and later work improves that bound further [S1,S2].

### PCF6 residue

After CRT, complementary idempotents, product-ring gluing, rank-2 trace/determinant identities, companion matrices, finite-field cyclicity and resultant machinery are removed, the useful residue is only the **typed corrected-carrier boundary**:

> In the particular corrected Gaussian/Eisenstein oriented free-rank-2 grammar, the required local characteristic-polynomial split forces the selector `c=-tr(T)`, and conversely that selector constructs the carrier; hence the grammar-specific realization is equivalent to exposing a nontrivial CRT idempotent.

This is a useful internal boundary because it locates exactly where hidden orientation information enters that grammar. Its primitives are standard and it is not a no-go theorem for all `H`-dependent constructions.

For a finite fixed family of `H`-independent determinant probes, each probe reduces to a fixed integer resultant. A nonzero resultant has finite prime support; a zero resultant makes the probe uniformly singular and therefore non-separating. The resulting obstruction is strictly limited to that fixed-probe class.

## Novelty / superiority kill list

The audit rejects all of the following interpretations:

- `PCF5_NEW_FACTORING_MECHANISM`;
- `PCF5_FACTORING_SPEEDUP_FROM_N_ONE_THIRD_SUPPORT`;
- `PCF5_PRODUCT_TREE_REMAINDER_TREE_OR_BATCH_GCD_NOVELTY`;
- `PCF6_CRT_PRODUCT_RING_OR_IDEMPOTENT_NOVELTY`;
- `PCF6_TRACE_DETERMINANT_SELECTOR_NOVELTY_AS_LINEAR_ALGEBRA`;
- `PCF6_RESULTANT_DETERMINANT_NOVELTY`;
- `PCF6_GENERAL_H_DEPENDENT_IMPOSSIBILITY`;
- `PROJECT_SPECIFIC_TYPED_RESIDUE => HISTORICAL_NOVELTY`.

## Source register

- **[S1]** Markus Hittmeir, *A babystep-giantstep method for faster deterministic integer factorization*. Abstract and §3 historical/algorithmic discussion of Strassen's deterministic fast-polynomial factoring approach. https://arxiv.org/abs/1608.08766
- **[S2]** Markus Hittmeir, *Integer factorization as subset-sum problem*. Introduction: Pollard/Strassen use fast polynomial multiplication and multipoint evaluation; deterministic ~O(N^(1/4)) historical bound. https://doi.org/10.1016/j.jnt.2023.02.010
- **[S3]** FLINT project, *nmod_poly — fast multipoint evaluation*. Fast multipoint evaluation uses temporary or precomputed subproduct trees. https://flintlib.org/doc/nmod_poly.html
- **[S4]** FactHacks / Bernstein et al., *Remainder tree*. Remainder trees are built from product trees and are a standard batch-gcd subroutine. https://facthacks.cr.yp.to/remainder.html
- **[S5]** The Stacks Project, *Chinese remainder theorem*. Tag 00DT: pairwise comaximal ideals give quotient/product decompositions. https://stacks.math.columbia.edu/tag/00DT
- **[S6]** The Stacks Project, *Idempotents and product decompositions*. Tag 00EM: nontrivial idempotents encode product decompositions. https://stacks.math.columbia.edu/tag/00EM
- **[S7]** Wolfram MathWorld, *Characteristic Polynomial*. For a 2x2 matrix, chi_A(x)=x^2-Tr(A)x+det(A). https://mathworld.wolfram.com/CharacteristicPolynomial.html
- **[S8]** Wolfram MathWorld, *Companion Matrix*. The companion matrix of a monic polynomial has that polynomial as characteristic polynomial. https://mathworld.wolfram.com/CompanionMatrix.html
- **[S9]** The Stacks Project, *Finite fields*. Tag 09HY: F_q^* is cyclic of order q-1. https://stacks.math.columbia.edu/tag/09HY
- **[S10]** Wolfram MathWorld, *Resultant*. Root-product and Sylvester-determinant definitions of the resultant. https://mathworld.wolfram.com/Resultant.html
- **[S11]** Wolfram MathWorld, *Sylvester Matrix*. The determinant of the Sylvester matrix equals the resultant. https://mathworld.wolfram.com/SylvesterMatrix.html
- **[S12]** Daniel J. Bernstein, *How to find small factors of integers*. Classical product/remainder-tree and batched small-factor literature landing page. https://cr.yp.to/papers.html#sf

## Replication disposition

The September 4 unmerged audit is **confirmed at the classification level**. This execution does not import its Result as authority; it reuses it only as the canonical highest durable frontier and independently checks the load-bearing comparisons against current source material and the accepted PCF5/PCF6 frozen statements.

The only changes are precision repairs to P5-6 and P6-9 described above. They do not change the accepted mathematics or the hard-target disposition.

`method_harvest = NO_TOOL_PAYLOAD`  
`independence_status = INDEPENDENT_REPLICATION_OF_UNMERGED_FRONTIER`  
`source_exposure_status = NONBLIND_DISCLOSED`

Next action: Driver review this fresh Result together with the prior unmerged Result/PR #1242. If accepted, close the shared PCF5/PCF6 prior-art gate at the typed-residue boundary and reject novelty, speedup, lower-bound, or general `H`-dependent-impossibility interpretations beyond the frozen scopes.
