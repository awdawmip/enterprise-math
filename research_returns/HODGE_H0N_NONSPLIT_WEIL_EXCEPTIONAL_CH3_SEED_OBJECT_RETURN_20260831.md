# HODGE H0N - Non-Split Weil Sixfold Exceptional ch_3 Seed Object Return

Researcher-ID: `EM-HODGEH0N-40AF21`
Task-ID: `RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT`
Publication: `TP2-9A71D4C6E2B5083F16CD`
Claim: `chatgpt-hodgeh0n-20260831-1344`
Execution branch: `research/hodge-h0n-exceptional-ch3-seed-em-hodgeh0n-40af21`
Date: `2026-08-31`

## Terminal verdict

`NEGATIVE_BOUNDARY`.

Hard target disposition:

`NONSPLIT_WEIL_SIXFOLD_TARGET_SIDE_EXCEPTIONAL_CH3_SEED_OBJECT_CONSTRUCTED_OR_NATURAL_SOURCE_FAMILY_NO_GO_CLASSIFIED = SATISFIED_AT_NEGATIVE_FAMILY_NO_GO_STRENGTH`.

No target-side object with nonzero exceptional `ch_3` is constructed. Instead, five explicitly delimited natural source families are proved to have zero exceptional projection on the declared very-general discriminant `[-3]` target. The remaining object-first frontier is a target-side non-semihomogeneous object with primitive degree-six characteristic class, or a genuinely non-tautological algebraic correspondence.

No non-algebraicity claim, Hodge-conjecture claim, or H1 promotion is made.

## 1. Independent H0M-premise audit

No H0M statement is imported as Working Truth.

Take `K=Q(i)`, `U=K^6`, `Lambda=Z[i]^6`, and

`h=diag(1,1,1,-1,-1,-3)`.

It has signature `(3,3)` and determinant class `[-3]` in `Q^*/Nm(K^*)`. A split six-dimensional `K`-Hermitian space with a three-dimensional totally isotropic `K`-subspace is three hyperbolic planes and has determinant class `[-1]`. Their ratio is `[3]`.

If `3` were a rational Gaussian norm, clearing denominators would give coprime integers `x,y,z` satisfying `x^2+y^2=3z^2`. Modulo `3`, `x^2+y^2=0` forces `3|x` and `3|y`; the equation then forces `3|z`, contradiction. Hence `[-3] != [-1]`. The split-source discriminant wall survives independent recheck.

For a very-general member `A` of the fixed `[-3]` Weil-type component, use `NS(A)_Q=Q*theta`. Let `V=H^1(A,Q)`, so `dim_K V=6`. Then

`W_K(A)=wedge_K^6 V`

is one-dimensional over `K` and two-dimensional over `Q`. After complexification,

`V_C=V_sigma direct_sum V_sigma_bar`

and

`H^6(A,C)=direct_sum_(a=0)^6 B_a`,
`B_a=wedge^a V_sigma tensor wedge^(6-a) V_sigma_bar`.

The exceptional Weil space is `B_6 direct_sum B_0`; the Weil signature `(3,3)` makes both determinant lines Hodge type `(3,3)`. The divisor cube `theta^3` lies in `B_3`. Therefore

`W_K(A) intersect Q*theta^3 = 0`.

Throughout this Return, `proj_W` means the `B_6+B_0` exterior-count component. Thus `proj_W(theta^3)=0`.

## 2. Source-literature boundary

The family proofs use classical source mathematics at its own strength:

- Mukai, *Semi-homogeneous vector bundles on an abelian variety*, J. Math. Kyoto Univ. 18 (1978), 239-272: for a simple semihomogeneous rank-`r` bundle, `ch(E)=r exp(c1(E)/r)`.
- Orlov, arXiv:alg-geom/9712017, plus standard Mukai semihomogeneous/Fourier-Mukai theory: abelian Fourier-Mukai equivalences transport translation/twist stabilizer data.
- Markman, arXiv:2502.03415: sixfold Weil classes are algebraic on the discriminant `-1` split locus; this is a positive control against any universal no-go.
- Markman, arXiv:2509.23403: split secant-sheaf source mechanism.
- Koike, arXiv:math/0211304: Gaussian sixfold Prym positive control on the classical trivial/discriminant-one regime.
- Mostaed, arXiv:2603.20268: the sixfold frontier outside known discriminant-specific mechanisms remains open at the studied scope.

These controls force the conclusion to remain a source-family theorem, not a theorem of non-algebraicity.

## 3. F1 - semihomogeneous extension/shift envelope

For a simple semihomogeneous vector bundle `E` of rank `r>0`,

`ch(E)=r exp(c1(E)/r)`,

so

`ch_3(E)=c1(E)^3/(6 r^2)`.

Since `NS(A)_Q=Q*theta`, write `c1(E)=q theta`. Then `ch_3(E)` is a rational multiple of `theta^3`, hence

`proj_W(ch_3(E))=0`.

Chern character is additive in `K_0`, so finite direct sums and extensions remain on `Q*theta^3`; shifts only change sign. Therefore the entire finite semihomogeneous extension/shift envelope has zero exceptional `ch_3`.

The normalized diagnostic is sharper:

`ch(E) exp(-c1(E)/r)=r`.

Thus a successful positive-rank seed must leave the simple semihomogeneous class and possess a primitive higher characteristic component.

## 4. F2 - target-side Fourier-Mukai orbit of line/semihomogeneous sources

Only target-side autoequivalences are allowed; no split object is imported.

Under an abelian Fourier-Mukai equivalence, the translation/twist stabilizer is transported through the induced symplectic action on `A x Ahat`. Hence line/semihomogeneous sources remain in the semihomogeneous orbit at the relevant stabilizer level. A full-support positive-rank output is therefore covered by F1. A finite-support output of point type on a sixfold has no codimension-three Chern-character term, so `ch_3=0`.

Thus the declared Fourier-Mukai orbit of line/semihomogeneous sources cannot create exceptional `ch_3`.

This does not cover an arbitrary input complex that already has primitive exceptional `ch_3`; admitting such an input would assume the desired seed.

## 5. F3 - polarization and target K-endomorphism tautological algebra

Start from line/semihomogeneous objects and close under tensor, dual, finite additive/derived operations, and pullback/pushforward along nonzero target-side `K`-endomorphism isogenies.

Because `NS(A)_Q=Q*theta`, for such an isogeny `f` there is a nonzero rational scalar `lambda_f` with

`f^*theta=lambda_f theta`.

Hence `f^*(theta^3)=lambda_f^3 theta^3`. Since `f_*f^*=deg(f) id` on rational cohomology, `f_*` also preserves `Q*theta^3`. Tensor, dual, and additive operations preserve the divisor polynomial algebra `Q[theta]`.

Therefore every codimension-three Chern-character output in this tautological algebra lies in `Q*theta^3` and has zero exceptional projection.

## 6. F4 - tautological degeneracy/determinantal cycles

Define the audited family to have input bundles/perfect complexes satisfying `c_j in Q*theta^j` for the degrees used. Thom-Porteous/Schur formulas are universal homogeneous Chern polynomials. In codimension three the only Chern monomial shapes are

`c1^3`, `c1*c2`, `c3`.

Each is a rational multiple of `theta^3`, so every such codimension-three degeneracy class has zero exceptional projection.

An input whose `c3` already contains a primitive `W_K` component is outside F4. That boundary prevents circularly assuming away the desired seed.

## 7. F5 - K-tautological correspondence operators

Let the correspondence algebra be generated by graphs of target `K`-endomorphism isogenies and their pull/push operations, cup product by rational divisor classes, rational linear combination, and composition.

Every generator preserves `Q[theta]`; consequently every such operator sends a tautological seed back into `Q[theta]`. In degree six its image lies in `Q*theta^3`, so it cannot hit `W_K` nontrivially from those seeds.

A genuinely non-tautological algebraic correspondence is not ruled out and remains an exact unblock route.

## 8. Unified no-go and falsifier audit

For the union of F1-F5 at the stated scope,

`source_degree6 subset Q*theta^3`

and

`W_K(A) intersect Q*theta^3={0}`.

Therefore every audited natural source has zero exceptional projection.

Counterexample search prevents overstatement:

1. Markman's discriminant-`-1` sixfolds are a positive control showing a universal no-go is false.
2. Koike's Gaussian Prym geometry shows non-tautological geometry can escape the divisor algebra on another solved regime.
3. Fourier-Mukai point outputs have `ch_3=0` on a sixfold.
4. A hypothetical target bundle with primitive exceptional `c3` is not killed by the theorem; it is precisely the desired seed.
5. A genuinely non-tautological correspondence remains open.

No scope-internal counterexample was found.

## 9. Deterministic checker and tool audit

Checker:

`research_checks/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK_20260831.py`.

Frozen execution:

`HODGE_H0N_CHECKS=110`
`HODGE_H0N_FAILURES=0`
`HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK: PASS`

The checker verifies only finite/symbolic reductions: exterior-count blocks, divisor/Weil separation, semihomogeneous `ch_3` coefficients and Newton identities, additive closure samples, the complete codimension-three Chern-monomial list, isogeny scalar closure, primitive-Weil boundary regressions, point-support `ch_3=0`, and the modulo-three Gaussian norm gate. It does not replace Mukai, Orlov/Mukai, Thom-Porteous, or generic Picard-rank theorems.

`enterprise_toolbox_registry.json` was checked. No accepted global Enterprise tool replaces this Hodge-specific proof obligation, so no new general-purpose tool is introduced. The checker is task-local.

## 10. Exact surviving frontier

The following routes are now removed on the declared very-general `[-3]` target:

1. semihomogeneous bundles plus finite extension/shift closure;
2. target-side Fourier-Mukai line/semihomogeneous orbit;
3. polarization plus target `K`-endomorphism tautological bundle algebra;
4. tautological Thom-Porteous/determinantal constructions;
5. graph/divisor `K`-tautological correspondence operators.

The next positive task must instead construct either

`A_TARGET_SIDE_NON_SEMIHOMOGENEOUS_OBJECT_E_WITH_PROJ_W(CH3(E))_NONZERO`

or

`A_GENUINELY_NONTAUTOLOGICAL_ALGEBRAIC_CORRESPONDENCE_WITH_NONZERO_WK_IMAGE`.

Only after such a seed exists is semiregularity/obstruction-cancellation target-side data instantiated.

Freeze boundary reached.
