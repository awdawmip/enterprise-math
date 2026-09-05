# PCF Restricted Routes — External Prior-Art / Duplication Audit

Status: `FROZEN / TASK-TERMINAL / SOURCE-BACKED COMPARATIVE AUDIT`

Task-ID: `RS-PCF-RESTRICTED-ROUTES-EXTERNAL-PRIOR-ART-DUPLICATION-AUDIT`  
Publication-ID: `TP2-D7E01B4B2274498405F8`  
Researcher-ID: `EM-PCFPRIOR1-7E4B2A`  
Claim-ID: `chatgpt-pcfprior1-20260904-2158-7e4b2a`  
Execution-Record-ID: `ER-252C4A73FA0560CCF078`

## Primary verdict

`PCF5_PCF6_EXTERNAL_PRIOR_ART_AND_DUPLICATION_BOUNDARY_EXACTLY_CLASSIFIED`

The audit succeeds, but it **kills any novelty interpretation of the load-bearing classical machinery**.

- **PCF5:** the factorization skeleton “block product polynomial -> fast multipoint evaluation -> gcd per block -> refine a block when the gcd is `N`” is classical Strassen / Pollard–Strassen-family machinery. The project’s `m x m^2` cell organization is an unbalanced/rectangular parameterization of the same block-product idea. Product/subproduct/remainder trees and batch-gcd-adjacent arithmetic are also standard. What remains project-local is the exact Perfect-Prime-Table cell embedding, its mixed-radix interval identity, the fixed-`kappa` coverage statement, and the sharp interface-specific failure guards. None of these observations is a historical novelty certificate or a state-of-the-art factorization claim.
- **PCF6:** CRT/product-ring decomposition, nontrivial idempotents, rank-2 trace/determinant extraction, companion-matrix realization, finite-field cyclotomic root counts, and determinant/resultant identities are standard. What remains project-local is the **typed boundary** for the specific corrected Gaussian/Eisenstein oriented free-rank-2 carrier: within that grammar, the realization exposes `c=-tr(T)` and is equivalent to a nontrivial CRT idempotent. This is not a general obstruction to `H`-dependent algorithms.

The accepted PCF5 and PCF6 results therefore remain useful as sharply scoped internal boundaries, but they must not be promoted as a new factoring algorithm, factoring speedup, factoring lower bound, or general impossibility theorem.

## 1. Frozen project inputs

This audit does not change either accepted Result.

### PCF5 frozen strength

Freeze `RR-D4F90C15C5BB4261230D` at:

- `m=max(2,ceil((kappa*N)^(1/6)))`;
- `m^2=O_kappa(N^(1/3))` Perfect-Prime-Table cells;
- exact cell partition of `[m+2,m^3+m+1]`;
- prime visibility iff `p<=m^3+m+1`;
- all-prime-divisor coverage only when `P^+(N)^2<=kappa*N`;
- batch construction from the degree-`m` polynomial `P_m(X)=prod_{k=0}^{m-1}(X+1+k m^2)` evaluated at `m^2` public points;
- the explicit unbalanced guard `N=2018=2*1009`, `kappa=4`, `m=5`, `U_m=131`;
- no universal factorization claim and no general lower bound.

### PCF6 frozen strength

Freeze `RR-6F3A91D2C5E74B08A621` at:

- the factor-blind ambient algebra `A_H=(Z/HZ)[X]/((X^2+1)(X^2+X+1))`;
- the corrected oriented free-rank-2 local characteristic-polynomial conditions;
- `c=-tr(T)` as the hidden selector, hence
  `CORRECTED_ORIENTED_MIXED_REALIZATION <=> NONTRIVIAL_CRT_IDEMPOTENT`
  at the frozen grammar;
- the synchronized ambient cyclotomic/determinant/rank families;
- fixed `H`-independent polynomial-determinant probes reducing to fixed integer resultants;
- exact fused root counts `4,8,16`;
- the `H=91` pressure witness;
- no general impossibility result for genuinely `H`-dependent algorithms.

## 2. Source-backed comparison matrix

Classification vocabulary:

- `EXACT_ANTECEDENT`: the same load-bearing mechanism or theorem is already standard/classical.
- `STRICT_ANTECEDENT`: a standard antecedent strictly subsumes or is stronger than the local mechanism, though the packaging/parameters differ.
- `STANDARD_METHOD_REPACKAGING`: the row is a direct recombination of standard facts in project notation.
- `PROJECT_SPECIFIC_TYPED_RESIDUE`: the exact scoped formulation/embedding is project-local after standard machinery is stripped; **this does not imply historical novelty**.
- `NO_MATERIAL_MATCH`: no material antecedent found in the bounded audit. No row below needs this classification.

| ID | Accepted load-bearing ingredient | Strongest audited antecedent | Classification | Audit consequence |
|---|---|---|---|---|
| P5-1 | Block product polynomial, fast multipoint evaluation, gcd per evaluated block | Strassen’s deterministic factorization explicitly evaluates a block-product polynomial at many points and takes gcds with `N` [S1] | `EXACT_ANTECEDENT` | The core PCF5 extraction skeleton is classical. |
| P5-2 | `m` factors per block and `m^2` evaluation blocks, covering `m^3` consecutive candidates with `m≈N^(1/6)` | Strassen uses a balanced block size/count `d≈N^(1/4)` to process about `sqrt(N)` candidates and achieves `N^(1/4+o(1))` deterministic factoring [S1,S2] | `STRICT_ANTECEDENT` | PCF5 is an unbalanced rectangular reparameterization, not an algorithmic novelty or speedup. |
| P5-3 | Product/subproduct/remainder-tree realization of fast multipoint evaluation | Fast multipoint evaluation via a subproduct tree is standard and implemented directly in FLINT [S5] | `EXACT_ANTECEDENT` | Tree-based fast evaluation cannot support novelty. |
| P5-4 | Batch-gcd-adjacent product/remainder-tree arithmetic | Remainder trees consume product trees and are a standard batch-gcd subroutine [S4]; Bernstein’s small-factor work places such product batching in classical factor-search literature [S3] | `STRICT_ANTECEDENT` | Same-modulus cell gcds are not literally the standard many-moduli batch-gcd problem, but the batching toolkit is classical. |
| P5-5 | Exact Perfect-Prime-Table cells `C_ij={1+i+mj+k m^2}` partition `[m+2,m^3+m+1]` | No separate external mechanism is needed: it is an elementary mixed-radix identity internal to the table coordinates | `PROJECT_SPECIFIC_TYPED_RESIDUE` | Useful exact coordinate lemma; no historical novelty is inferred. |
| P5-6 | Prime visibility iff `p<=U_m=m^3+m+1` | Once the interval partition is fixed, visibility is the elementary fact that an interval contains a multiple of every prime up to its endpoint | `PROJECT_SPECIFIC_TYPED_RESIDUE` | Exact table-interface boundary, not a new factorization principle. |
| P5-7 | Fixed-`kappa` family `P^+(N)^2<=kappa*N`, with `m=ceil((kappa*N)^(1/6))` and `m^2=O_kappa(N^(1/3))` cells | Classical block-product factoring already handles unrestricted composites with better `N^(1/4+o(1))` asymptotic complexity [S1,S2] | `PROJECT_SPECIFIC_TYPED_RESIDUE` | The contribution is only the exact coverage theorem for this table support/parameterization. |
| P5-8 | If a block gcd equals `N`, refine inside that block to find a proper factor | Strassen’s recalled algorithm explicitly performs within-block gcd refinement when a block gcd is `N` [S1] | `EXACT_ANTECEDENT` | The refinement rule is classical. |
| P5-9 | Guard `2018=2*1009` and the full-layer `Omega(N^(2/3))` cell lower bound for universal all-prime visibility | The guard/lower bound is specific to the frozen full-layer Perfect-Prime-Table interface | `PROJECT_SPECIFIC_TYPED_RESIDUE` | Retain only as an interface-specific obstruction; never state it as a factoring lower bound. |
| P6-1 | Factor-blind decomposition `R_H[X]/(fg) ≅ R_H[X]/(f) × R_H[X]/(g)` from Bezout/comaximality | Ring-theoretic Chinese remainder theorem for pairwise comaximal ideals [S6] | `EXACT_ANTECEDENT` | Ambient product decomposition is standard CRT. |
| P6-2 | Proof-side coefficient split for `H=pq` and product-ring decomposition | Chinese remainder theorem for `(p)` and `(q)` [S6] | `EXACT_ANTECEDENT` | Hidden-factor product structure is standard. |
| P6-3 | Nontrivial selector/idempotent `c=(0 mod p,1 mod q)` and factor extraction by `gcd(c,H)` | CRT supplies the idempotent; idempotents are the standard algebra behind product decompositions [S6,S7] | `EXACT_ANTECEDENT` | A nontrivial idempotent is already factor-equivalent information, not a new primitive. |
| P6-4 | Interpolation/gluing `h_c=(1-c)f+c g=X^2+cX+1` | Idempotent gluing across a product ring is standard product-ring algebra [S6,S7] | `STANDARD_METHOD_REPACKAGING` | The formula is a project-specific notation for standard CRT gluing. |
| P6-5 | Extract selector from rank-2 operator by `c=-tr(T)` and `det(T)=1` | For a `2x2` operator, the characteristic polynomial is `x^2-Tr(T)x+det(T)` [S8]; companion matrices realize any monic quadratic [S9] | `STANDARD_METHOD_REPACKAGING` | Trace/determinant readout and converse companion realization are standard linear algebra. |
| P6-6 | Exact typed equivalence for the corrected Gaussian/Eisenstein oriented free-rank-2 carrier | Follows by combining CRT/idempotents with the rank-2 characteristic-polynomial identity [S6-S9] | `PROJECT_SPECIFIC_TYPED_RESIDUE` | Retain the exact grammar-specific equivalence as an internal boundary; it is not a general no-go theorem. |
| P6-7 | Ambient order `12` and fused root counts `4,8,16` | `F_q^×` is cyclic of order `q-1` [S11], so roots of `Phi_4`/`Phi_3` are controlled by divisibility of `q-1`; CRT multiplies the local counts [S6,S11] | `STANDARD_METHOD_REPACKAGING` | Root census is standard cyclotomic/finite-field arithmetic in project notation. |
| P6-8 | `det(P(T_H))=Res(F,P) mod H` for fixed `P` | Resultant equals the determinant of the multiplication map in the quotient algebra (monic `F` case) [S10] | `EXACT_ANTECEDENT` | The determinant/resultant identity is standard. |
| P6-9 | Finite fixed `H`-independent determinant probes cannot universally separate semiprimes because each probe is one fixed integer resultant | Direct consequence of P6-8: a finite family has only the finite prime support of finitely many fixed integers | `STANDARD_METHOD_REPACKAGING` | Retain only this narrowly quantified probe-class no-go; it says nothing about genuinely `H`-dependent observables. |
| P6-10 | `H=91`, selector `c=78`, mixed-root pressure witness | Concrete arithmetic check of the typed theorem | `PROJECT_SPECIFIC_TYPED_RESIDUE` | Validation witness only; it carries no novelty authority. |
| P6-11 | Routing label `N_ONLY_NONTRIVIAL_IDEMPOTENT_OR_EQUIVALENT_SELECTOR_GENERATOR` | CRT/idempotent theory shows that any such nontrivial idempotent already exposes a factor [S6,S7] | `PROJECT_SPECIFIC_TYPED_RESIDUE` | Keep only as a project routing label for “generate the asymmetry from `H`”; do not present idempotents themselves as new mathematics. |

## 3. Exact surviving project-local boundary

After removing standard antecedents, the useful residue is small and sharply scoped.

### PCF5 residue

The surviving content is the **typed embedding and boundary**, not a new factoring algorithm:

1. the exact table-specific mixed-radix identity
   `C_ij^(m) -> [m+2,m^3+m+1]`;
2. the induced exact table visibility criterion `p<=m^3+m+1`;
3. the fixed-public-`kappa` implication
   `P^+(N)^2<=kappa*N => every prime divisor is represented in the full m^2-cell layer`
   under `m=ceil((kappa*N)^(1/6))`;
4. the explicit unbalanced counterexample and the `Omega(N^(2/3))` **full-layer interface** obstruction.

The polynomial batching/gcd implementation is classical Strassen-style machinery. In particular, the existence of an `O_kappa(N^(1/3))` cell support for a restricted family must not be advertised as a factorization speedup: classical Strassen already gives deterministic unrestricted factoring in `N^(1/4+o(1))` time [S1].

### PCF6 residue

The surviving content is the **typed corrected-carrier equivalence**, not CRT/idempotents themselves:

> For the particular oriented free-rank-2 grammar with local characteristic polynomials `X^2+1` at one hidden factor and `X^2+X+1` at the other, the trace necessarily exposes the CRT selector `c=-tr(T)`, and conversely that selector constructs the carrier.

This remains a useful project-local interface theorem because it says exactly where hidden orientation information enters this grammar. But its proof is a direct combination of standard CRT/idempotent decomposition and the standard rank-2 characteristic-polynomial identity. It must not be promoted to impossibility of all `H`-dependent constructions.

The fixed-probe resultant observation also survives as a narrow scope guard: a finite family of fixed `H`-independent polynomial determinant probes reduces to finitely many fixed integer resultants. That is a standard resultant consequence applied to this ambient algebra, not a general lower bound.

## 4. Novelty / superiority kill list

The following interpretations are **rejected** by this audit:

1. `PCF5_NEW_FACTORING_MECHANISM` — rejected.
2. `PCF5_FACTORING_SPEEDUP_FROM_N_ONE_THIRD_SUPPORT` — rejected; support count is not a novelty metric and Strassen’s unrestricted classical bound is already asymptotically stronger.
3. `PCF5_PRODUCT_TREE_OR_BATCH_GCD_NOVELTY` — rejected.
4. `PCF6_CRT_OR_IDEMPOTENT_NOVELTY` — rejected.
5. `PCF6_TRACE_DETERMINANT_SELECTOR_NOVELTY_AS_LINEAR_ALGEBRA` — rejected.
6. `PCF6_RESULTANT_DETERMINANT_NOVELTY` — rejected.
7. `PCF6_GENERAL_H_DEPENDENT_IMPOSSIBILITY` — rejected.
8. `PROJECT_SPECIFIC_TYPED_RESIDUE => HISTORICAL_NOVELTY` — rejected. The classification means only that the exact typed statement/embedding is project-local in this bounded audit.

No row is classified `NO_MATERIAL_MATCH`; accordingly, this audit makes **no historical novelty finding**.

## 5. Source register

- **[S1]** Markus Hittmeir, *A babystep-giantstep method for faster deterministic integer factorization*, arXiv:1608.08766, especially §3 “Strassen’s approach”.  
  https://arxiv.org/abs/1608.08766
- **[S2]** Markus Hittmeir, *Integer factorization as subset-sum problem*, Journal of Number Theory 2023, DOI 10.1016/j.jnt.2023.02.010. The introduction explicitly summarizes Pollard/Strassen use of fast polynomial multiplication and multipoint evaluation.  
  https://doi.org/10.1016/j.jnt.2023.02.010
- **[S3]** Daniel J. Bernstein, *How to find small factors of integers* (paper/author landing).  
  https://cr.yp.to/papers.html#sf
- **[S4]** Bernstein et al., FactHacks, *Remainder tree*: product tree -> remainder tree; explicitly identified as an important batch-gcd subroutine.  
  https://facthacks.cr.yp.to/remainder.html
- **[S5]** FLINT documentation, `nmod_poly` / `fmpz_mod_poly` fast multipoint evaluation: temporary or precomputed subproduct trees.  
  https://flintlib.org/doc/nmod_poly.html
- **[S6]** The Stacks Project, Tag 00DT, Chinese remainder theorem for pairwise comaximal ideals.  
  https://stacks.math.columbia.edu/tag/00DT
- **[S7]** The Stacks Project, Tag 00EM, idempotents and product decompositions.  
  https://stacks.math.columbia.edu/tag/00EM
- **[S8]** MIT OpenCourseWare 18.013A, §4.6: for a `2x2` matrix, characteristic polynomial `x^2-x Tr(M)+det(M)`.  
  https://ocw.mit.edu/ans7870/18/18.013a/textbook/HTML/chapter04/section06.html
- **[S9]** Wolfram MathWorld, *Companion Matrix*: the companion matrix of a monic polynomial has that polynomial as characteristic polynomial.  
  https://mathworld.wolfram.com/CompanionMatrix.html
- **[S10]** David A. Cox, John Little, Donal O’Shea, *Using Algebraic Geometry*, 2nd ed., Ch. 3 §1, Proposition (1.5): resultant as determinant of the multiplication map.  
  https://eclass.uoa.gr/modules/document/file.php/D231/Papers/Cox-UsingAlgebraicGeometry.pdf
- **[S11]** Daniel Evans, Durham University, *Galois Theory III — Finite fields*, Theorem 5.2: finite multiplicative subgroups of fields are cyclic; in particular `F_q^× ≅ Z/(q-1)`.  
  https://www.maths.dur.ac.uk/users/daniel.evans/GaloisTheory/Notes/finite-fields.html

## 6. Audit limitations

This is a bounded, source-backed duplication audit against the strongest directly relevant standard antecedents specified by the task. It is not an exhaustive history of every appearance of every elementary identity.

`PROJECT_SPECIFIC_TYPED_RESIDUE` is deliberately weaker than a novelty claim. It records only that, after stripping standard machinery, the exact project-scoped formulation remains operationally useful. Establishing historical priority or novelty would require a separate, broader literature review and is not authorized here.

## Terminal disposition

`SUCCESS / DRIVER_REVIEW_REQUIRED`

Hard target reached exactly:

`PCF5_PCF6_EXTERNAL_PRIOR_ART_AND_DUPLICATION_BOUNDARY_EXACTLY_CLASSIFIED`

Recommended Driver action: accept the audit as the external-antecedent gate for PCF5/PCF6 at the classifications above; preserve PCF5 only as a table-specific support/visibility boundary and PCF6 only as a corrected-carrier typed selector boundary; reject any novelty, speedup, lower-bound, or general-impossibility interpretation beyond those scopes.
