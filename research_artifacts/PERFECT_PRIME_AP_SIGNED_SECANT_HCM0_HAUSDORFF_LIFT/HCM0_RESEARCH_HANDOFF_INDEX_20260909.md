# Perfect Prime AP HCM0 research handoff index — 2026-09-09

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Durable research base before this index: `ebc1467e7773566c49126a781837d0df4bb749c4`  
Status: **PARTIAL SUCCESS / DURABLE HANDOFF / HCM0 OPEN**

## 1. Mother result boundary

The accepted predecessor reduces strict residual coefficient positivity exactly to HCM0 for

`h_(m,a)=(-1)^a q_(m,a)/binom(d,a)`:

`(-1)^k Delta^k h_(m,0) > 0` for every admissible `m,k`.

This research did **not** prove all-m HCM0 and did **not** prove the parent Perfect-Prime determinant theorem. It materially narrows the open sign problem and freezes several reusable all-m structures and exact no-go boundaries.

## 2. Read this handoff in the following order

1. `COEFFICIENTWISE_TP_CAUCHY_SHIFT_CHECKPOINT_20260904.md`  
   - coefficientwise strict TP of the transformed moment kernel;
   - exact pure-shift Lagrange-transfer factorization;
   - all-m two-distinct-shift mixed-cell sign theorem with exact `(c-d)^(2m-2)` confluence factor.

2. `THREE_SHIFT_ARBITRARY_SHIFT_OBSTRUCTION_20260904.md`  
   - exact `m=7`, shifts `(0,2,5)` counterexample to the over-strong arbitrary-shift three-support sign conjecture;
   - same multiplicity cell recovers the target sign on actual `m^2` spacing.

3. `ACTUAL_LAYER_PASCAL_HAUSDORFF_NORMAL_FORM_20260904.md` and `POINTWISE_PASCAL_LDL_TWO_SCALE_GRID_20260904.md`  
   - actual layers synchronize integer translation by multiples of `m` with Hausdorff moment-index shifts by `m`;
   - exact two-scale atom coding `k=j+ms` and mask `(1-x)^n(1-x^m)^n`;
   - explicit pointwise Pascal LDL and principal-minor signs.

4. `BEZOUT_EUCLIDEAN_QUOTIENT_REDUCTION_20260904.md`  
   - signed moment Gram = scalar times inverse Bezoutian;
   - deterministic Euclidean-step reduction to an order-`m-1` Bezout pencil.

5. `SEPARATION_THRESHOLD_PENCIL_CHECKPOINT_20260904.md`  
   - exact Mellin-Euler synchronized quotient normal form;
   - positive-real generalized spectrum is false, including an actual `m=10` counterexample;
   - arbitrary synchronized integer shifts are false: exact `m=10,(r0,r,s)=(0,1,5)` wrong `t^8` coefficient;
   - pointwise mixed-discriminant positivity is false;
   - exact base-slice evidence remains positive on all 120 actual triples at `m=10`.

6. `RESIDUE_DUAL_STP_SECANT_FRAME_20260904.md`, `CODIM_ONE_DUAL_KREIN_NORMAL_20260904.md`, and `DUAL_HYPERPLANE_INERTIA_INVERSE_POSITIVITY_20260904.md`  
   - residue-dual transfer to fractional pole nodes;
   - all minors of the dual secant frame are strictly positive;
   - all frames span one explicit codimension-one hyperplane;
   - exact rank-one inverse formula, fixed inertia, and late/separated inverse positivity.

7. `ACTUAL_BLOCK_SEMIGROUP_NEWTON_NORMAL_20260904.md`  
   - actual gaps are controlled by one-layer translation `E` and positive Newton expansion
     `S_a(E)=sum_l binom(a,l+1)(E-I)^l`;
   - the natural three-layer variables are consecutive positive block lengths `(a,c)`.

8. Finite exact support evidence  
   - `ACTUAL_TRIPLE_SUPPORT_EXHAUSTION_20260904.md` and `actual_triple_support_m3_m7_exact_check_20260904.py`: complete exact three-layer support exhaustions through `m=7`;
   - `SEPARATION_THRESHOLD_PENCIL_CHECKPOINT_20260904.md`: all actual base-slice triples at `m=10` have common-sign pencil coefficients.

9. Extreme-coefficient exact certificates  
   - full-parameter normalized trace certificates exist for `m=3,4,5,6`;
   - `M6_ALL_PARAMETER_NORMALIZED_TRACE_CERTIFICATE_20260906.md` freezes the `m=6` theorem and its `6214`-term all-positive primitive polynomial certificate.

10. Current all-m frontier  
    - `EXTREME_COEFFICIENT_SIGNED_BRANCH_BRC_REDUCTION_20260906.md`: exact signed Cauchy-Binet branch expansion for every mixed coefficient; for the first dangerous extreme coefficient, an inverse-free three-index alternating-square formula and Vandermonde-integral branch amplitudes;
    - `ALL_M_TANGENT_FACE_COEFFICIENTWISE_POSITIVITY_20260906.md`: the entire tangent `c^0` numerator face is coefficientwise strictly positive for every `m`, with full monomial support of size `binom(m^2+2,2)`.

## 3. Proved all-m statements that must not be re-proved as discovery

- coefficientwise strict TP of the transformed moment kernel;
- pure-shift Lagrange-transfer factorization and rank statement;
- correct sign for every mixed cell supported on exactly two distinct shifts;
- actual-layer Pascal/Hausdorff synchronization and strict Hausdorff moment shift;
- actual translation-difference total nonnegativity;
- pointwise Pascal LDL and closed leading-principal-minor formula;
- inverse-Bezout and one-step Euclidean quotient reduction;
- residue duality and strict TP of the dual secant frame;
- codimension-one common hyperplane, exact Krein normal, fixed inertia;
- late/separated entrywise inverse positivity and monotonic strengthening with the moment level;
- actual block semigroup / positive-Newton normal;
- normalized endpoint determinant monotonicity;
- signed branch expansion for all mixed coefficients and maximal-minor rigidity;
- all-m coefficientwise positivity of the tangent `c^0` face.

## 4. Exact finite-only evidence

Do not promote these to all-m theorems:

- full shifted HCM is exact only through `m<=12` in this branch line;
- complete actual three-distinct-layer support sign checks are finite (`m<=7`);
- complete actual base-slice triple-pencil check at `m=10` is finite;
- full-parameter normalized trace positivity is proved separately for `m=3,4,5,6`, not yet arbitrary `m`.

## 5. Closed or over-strong routes — do not reopen without new information

Exact counterexamples or theorem-level boundaries already reject:

- arbitrary nonnegative shift all-support sign regularity;
- positive-real generalized spectrum as the all-m mechanism;
- arbitrary synchronized integer shifts without the actual block condition;
- pointwise mixed-discriminant positivity before Hausdorff integration;
- P-matrix / termwise principal-minor positivity as a sufficient mechanism;
- internal secant Pólya-frequency / Toeplitz total positivity;
- generic TP plus positive binomial contractions as a sufficient signed-cofactor theorem;
- classical two-parameter Hahn identification of the actual weight.

The valid BRC use is the signed branch carrier from `EXTREME_COEFFICIENT_SIGNED_BRANCH_BRC_REDUCTION_20260906.md`: preserve positive and negative parity populations separately. Positive total mass cannot replace the signed determinant.

## 6. Two recommended successor tasks

### A. Extreme branch parity domination

Starting from equation (6.2) and the Vandermonde integral (7.2) of `EXTREME_COEFFICIENT_SIGNED_BRANCH_BRC_REDUCTION_20260906.md`, prove the actual-gap oriented parity-mass domination for

`M=ma`, `N=m(a+c)`, `S>=0`, `a,c>0`.

This is the sharp provenance-preserving form of the all-m normalized-trace target. It should use the beta-weight ratios and branch-amplitude structure, not matrix-spectrum surrogates.

### B. Tangent-face induction beyond c^0

Starting from `ALL_M_TANGENT_FACE_COEFFICIENTWISE_POSITIVITY_20260906.md`, differentiate the normalized inverse/trace identity one further order and obtain a dimension-free formula for the `c^1` numerator face. Either prove coefficientwise positivity and identify an induction over `c`-degree, or freeze the first exact obstruction to such a face induction.

This route is deliberately complementary to A: it attacks the observed positive `m^2`-block polynomial structure instead of parity pairing.

## 7. Handoff boundary

A successor should begin from this index and the immutable research commit containing it. Do not reconstruct the route from conversation history and do not repeat the finite `m` scans unless required as a regression for a genuinely new formula.

The parent HCM0 objective remains open. A success on either successor is an intermediate theorem unless it is separately shown to imply every HCM0 cell.
