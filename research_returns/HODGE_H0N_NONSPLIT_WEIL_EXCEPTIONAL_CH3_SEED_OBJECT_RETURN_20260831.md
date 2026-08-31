# HODGE H0N — Non-Split Weil Sixfold Exceptional `ch_3` Seed Object Return

Researcher-ID: `EM-HODGEH0N-40AF21`
Task-ID: `RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT`
Publication: `TP2-9A71D4C6E2B5083F16CD`
Claim: `chatgpt-hodgeh0n-20260831-1344`
Execution branch: `research/hodge-h0n-exceptional-ch3-seed-em-hodgeh0n-40af21`
Date: `2026-08-31`

## Verdict

Primary classification:

`NATURAL_SOURCE_FAMILY_NO_GO_CLASSIFIED_WITH_NONTAUTOLOGICAL_FRONTIER_OPEN`.

Hard target:

`NONSPLIT_WEIL_SIXFOLD_TARGET_SIDE_EXCEPTIONAL_CH3_SEED_OBJECT_CONSTRUCTED_OR_NATURAL_SOURCE_FAMILY_NO_GO_CLASSIFIED = SATISFIED_AT_NEGATIVE_FAMILY_NO_GO_STRENGTH`.

No target-side object with nonzero exceptional `W_K` component of `ch_3` is constructed. Instead, five broad and explicitly delimited natural source families are proved unable to produce such a component on the declared very-general `[-3]` target. The surviving frontier is narrower: any successful seed must leave the semihomogeneous/divisor/K-tautological envelope, or arise from a genuinely non-tautological algebraic correspondence.

No non-algebraicity claim is made. No Hodge-conjecture claim is made. H1 is not opened.

## 1. Independent audit of the H0M premises actually used

H0N was published before Driver review of H0M, so no H0M statement is imported as Working Truth. The pinned H0M model and defect artifacts were rechecked at the exact strength needed here.

Let

`K=Q(i)`, `U=K^6`, `Lambda=Z[i]^6`

and take the Hermitian form

`h=diag(1,1,1,-1,-1,-3)`.

Its signature is `(3,3)` and its determinant representative is `-3`. A split six-dimensional `K`-Hermitian space with a three-dimensional totally isotropic `K`-subspace is three hyperbolic planes and has determinant class `[-1]`. Their ratio is `[3]`.

If `3=Nm_Q(i)/Q(a+bi)` for rational `a,b`, clearing denominators yields coprime integers

`x^2+y^2=3z^2`.

Modulo `3`, a square is `0` or `1`, so `x^2+y^2=0 (mod 3)` forces `x=y=0 (mod 3)`. The equation then forces `z=0 (mod 3)`, contradicting coprimality. Thus `3` is not a Gaussian norm and

`[-3] != [-1]`.

This independently preserves the discrete split/non-split wall used below.

The polarization construction in the H0M model is also internally consistent. With

`E(x,y)=(1/2)Tr_K/Q(i h(x,y))`

and `J0` acting by `+i` on the positive three coordinates and `-i` on the negative three, `E(x,J0x)>0` for nonzero `x`. Hence the corresponding Weil-type period domain is nonempty. H0N uses a very-general member `A` of the fixed `[-3]` component, chosen outside all additional rational degree-two Hodge loci and decomposition/isogeny Hodge loci. At the used strength this gives

`NS(A)_Q = Q*theta`

for the polarization class `theta`, and `A` is simple. These are genericity statements only; no algebraicity of exceptional middle classes is inferred from them.

Let `V=H^1(A,Q)`. Since `dim_K V=6`,

`W_K(A)=wedge_K^6 V`

is one-dimensional over `K` and therefore two-dimensional over `Q`. After complexification,

`V_C = V_sigma direct_sum V_sigma_bar`

and

`H^6(A,C) = direct_sum_(a=0)^6 B_a`,
`B_a = wedge^a V_sigma tensor wedge^(6-a) V_sigma_bar`.

The exceptional Weil space is exactly

`W_K(A)_C = B_6 direct_sum B_0`.

The Weil signature `(3,3)` makes the determinant line of each embedding block of Hodge type `(3,3)`, so every rational class in `W_K(A)` is a Hodge class.

A `K`-compatible divisor class is in the mixed embedding-count block. Since `NS(A)_Q=Q*theta`, all rational divisors are multiples of `theta`, and

`theta^3 in B_3`.

Therefore

`(Q*theta^3)_C intersect (B_6 direct_sum B_0) = 0`.

This gives the required typed exceptional projection without choosing an arbitrary inner product: `proj_W` means the `B_6+B_0` component in the exterior-count decomposition. In particular,

`proj_W(theta^3)=0`.

This is the only projection property used in the no-go theorem.

## 2. Literature and frontier recheck

The task was checked against the source literature rather than treating the H0M literature ledger as inherited truth.

Mukai's semihomogeneous theory gives, for a simple semihomogeneous vector bundle `E` of positive rank `r` on an abelian variety,

`ch(E)=r exp(c_1(E)/r)`.

The reference is S. Mukai, *Semi-homogeneous vector bundles on an abelian variety*, J. Math. Kyoto Univ. 18 (1978), 239-272, DOI `10.1215/kjm/1250522574`.

Orlov's derived-equivalence theory for abelian varieties identifies Fourier-Mukai equivalences with the corresponding symplectic action on `A x Ahat`; semihomogeneous stabilizer data is transported by that action. The reference used is D. Orlov, arXiv:`alg-geom/9712017`. Gulbrandsen, arXiv:`0711.2238`, is used only as a concrete line-bundle/semihomogeneous Fourier-Mukai source reference.

The positive controls are important because they prevent overstatement:

- Markman, arXiv:`2502.03415`, proves algebraicity of Weil classes for abelian sixfolds of Weil type of discriminant `-1` in his convention.
- Markman, arXiv:`2509.23403`, describes the split/secant-sheaf mechanism.
- Koike, arXiv:`math/0211304`, gives the Gaussian sixfold discriminant-`1`/trivial-control Prym algebraicity result (conventions differ from the determinant representative used above).
- Mostaed, arXiv:`2603.20268`, explicitly records that outside the known sixfold discriminant-specific mechanisms the Weil-class algebraicity problem remains open at the studied frontier.

Nothing in this source check gives algebraicity on the present very-general `[-3]` target. Equally importantly, the split and Prym positive controls show that a theorem claiming that *all* algebraic/derived sources have zero exceptional projection would be false or at least unjustified. H0N therefore proves a family theorem with explicit boundaries.

## 3. Family F1 — semihomogeneous extension/shift envelope

Define `F1` to be the class generated by simple semihomogeneous vector bundles on `A` under finite direct sums, extensions, and shifts.

For a simple semihomogeneous bundle `E` of rank `r>0`, Mukai gives

`ch(E)=r exp(c_1(E)/r)`,

hence

`ch_3(E)=c_1(E)^3/(6 r^2)`.

Because `NS(A)_Q=Q*theta`, write `c_1(E)=q theta` with `q in Q`. Then

`ch_3(E)=q^3/(6 r^2) theta^3`.

Consequently

`proj_W(ch_3(E))=0`.

The Chern character is additive in `K_0`. For an exact sequence

`0 -> E' -> E -> E'' -> 0`

one has `ch(E)=ch(E')+ch(E'')`; for an odd shift the class changes sign. Therefore every object obtained from finitely many such generators by the declared direct-sum/extension/shift operations still has

`ch_3 in Q*theta^3`

and hence zero exceptional projection.

A useful normalized form makes the obstruction even sharper. For a positive-rank semihomogeneous bundle,

`ch(E) exp(-c_1(E)/r) = r`.

Thus the normalized characteristic class used in split secant-sheaf constructions has no higher component at all for a semihomogeneous seed. A successful target object must therefore cease to be semihomogeneous in precisely the sense relevant to the exceptional middle class.

Result:

`F1_EXCEPTIONAL_CH3 = ZERO`.

## 4. Family F2 — target-side Fourier-Mukai orbit

The task forbids importing a split-component object by renaming it. Accordingly `F2` is deliberately target-side:

`F2 = { Phi(E) : Phi in Aut(D^b(A)), E a line bundle or simple semihomogeneous source on A }`,

together with shifts.

For an object `E`, consider its translation/twist stabilizer in `A x Ahat`. A Fourier-Mukai autoequivalence transports translations and twists through the associated symplectic automorphism of `A x Ahat`; therefore it preserves the stabilizer dimension. Line bundles and semihomogeneous sources have maximal semihomogeneous stabilizer dimension, so their Fourier-Mukai images remain semihomogeneous objects/sheaves at this numerical-stabilizer level.

On the very-general simple target there are two relevant output types for the declared source orbit:

1. full-support semihomogeneous output: it is governed by the semihomogeneous Chern-character formula and reduces to F1;
2. finite-support output, such as the familiar Fourier exchange between degree-zero line-type data and point-type data: on a sixfold its Chern character starts in codimension six, so `ch_3=0`.

Hence a target-side Fourier-Mukai autoequivalence does not turn a line/semihomogeneous seed into an exceptional codimension-three source:

`F2_EXCEPTIONAL_CH3 = ZERO`.

This statement is intentionally not a claim about an arbitrary object already carrying a primitive `ch_3`. Fourier-Mukai equivalence cannot be used to assume away the very seed H0N is trying to find.

## 5. Family F3 — polarization and target-side K-endomorphism tautological algebra

Let `F3` be the source algebra generated from line/semihomogeneous objects by:

- tensor product and dual;
- finite sums, cones/extensions and shifts at the `K_0` level;
- pullback and pushforward along nonzero target-side `K`-endomorphism isogenies.

Because `NS(A)_Q=Q*theta`, every nonzero isogeny `f` induced by the target endomorphism algebra acts on `NS_Q` by a nonzero scalar:

`f^*theta = lambda_f theta`.

Therefore

`f^*(theta^3)=lambda_f^3 theta^3`.

For an isogeny,

`f_* f^* = deg(f) id`

on rational cohomology, so `f_*` also preserves the one-dimensional line `Q*theta^3`.

Tensor products multiply Chern characters, duals change the expected signs by degree, and the additive operations are `K_0`-linear. Since the starting Chern characters lie in the divisor polynomial algebra `Q[theta]`, every F3 characteristic class remains in `Q[theta]`; in codimension three it lies in `Q*theta^3`.

Result:

`F3_EXCEPTIONAL_CH3 = ZERO`.

This also shows why merely applying the existing algebraic `K`-action to a divisor-generated seed cannot generate the two-dimensional exceptional Weil space.

## 6. Family F4 — tautological degeneracy/determinantal constructions

Arbitrary determinantal geometry is too broad for a no-go theorem: if one inputs a bundle whose `c_3` already has an exceptional component, a degeneracy formula can simply propagate the missing seed. H0N therefore defines the reusable natural family precisely.

Let `F4` consist of expected-codimension degeneracy/determinantal loci built from vector bundles or perfect complexes whose rational Chern classes satisfy

`c_j in Q*theta^j`

for the degrees used. This includes the F1-F3 source bundles.

Thom-Porteous and Schur formulas express the cycle class of such a degeneracy locus as a universal polynomial in the Chern classes of the virtual difference of the input bundles. In codimension three, the only Chern monomial shapes are

`c_1^3`, `c_1 c_2`, `c_3`.

Under the F4 hypothesis all three are multiples of `theta^3`. Hence every codimension-three F4 degeneracy class satisfies

`proj_W([D])=0`.

Result:

`F4_EXCEPTIONAL_CLASS = ZERO`.

Hard boundary:

`ARBITRARY_DETERMINANTAL_INPUT_WITH_PRIMITIVE_C3 != F4`.

This boundary is essential; removing it would make the theorem circular.

## 7. Family F5 — K-tautological correspondence operators

Let `F5` be the cohomological correspondence algebra generated by:

- graphs of target-side nonzero `K`-endomorphism isogenies, acting by pullback/pushforward;
- cup product with rational divisor classes;
- composition and rational linear combination of those operators.

Each generator preserves the divisor algebra `Q[theta]`: divisor cup product obviously does, while the graph operators preserve it by the F3 pull/push calculation. Therefore every F5 operator maps a divisor/semihomogeneous seed back into the divisor algebra. In degree six its output lies in

`Q*theta^3`.

Thus

`F5_EXCEPTIONAL_IMAGE_FROM_TAUTOLOGICAL_SEEDS = ZERO`.

A genuinely new algebraic correspondence whose cohomological action is not generated by these operations remains open. That is not a defect in the theorem; it is the exact surviving route demanded by the task.

## 8. Counterexample search and falsifier audit

The no-go was actively tested against cases that would falsify an overbroad statement.

### 8.1 Split sixfold positive control

Markman's discriminant-`-1` secant-sheaf construction produces algebraic Weil classes. Therefore the H0N theorem cannot contain arbitrary secant sheaves or arbitrary algebraic objects. It does not: the target component is `[-3]`, and F1-F5 are target-side semihomogeneous/tautological families.

Status: `NO_CONTRADICTION / SCOPE_BOUNDARY_CONFIRMED`.

### 8.2 Gaussian Prym positive control

Koike-Schoen supplies algebraic Weil classes on the classical Gaussian trivial-discriminant sixfold family. These cycles arise from Prym geometry, not from the claim that semihomogeneous divisor algebra itself spans `W_K`.

Status: `NO_CONTRADICTION / NONTAUTOLOGICAL_GEOMETRY_REMAINS_POSSIBLE`.

### 8.3 Fourier-Mukai point output

The Poincare transform can exchange line-type and point-type data. A point sheaf on a sixfold has its nonzero top support class in codimension six, not codimension three.

Status: `ch_3=0 / CONSISTENT`.

### 8.4 Hypothetical primitive `c_3` bundle

Assume, only as a falsifier, that a target bundle `G` already satisfies

`proj_W(ch_3(G)) != 0`.

Then F1-F4 must not classify `G` unless an independent theorem puts its Chern classes in the divisor algebra. H0N explicitly excludes such a primitive input.

Status: `THEOREM_DOES_NOT KILL THE DESIRED_SEED`.

### 8.5 Non-tautological correspondence

A correspondence with a new codimension-six kernel class on `A x A` could have an operator that mixes the divisor line into `W_K`. F5 does not rule this out because its generators are deliberately limited to graph/divisor operations.

Status: `OPEN / EXACT UNBLOCK ROUTE`.

No counterexample was found to the stated family theorem. Several counterexamples exist to stronger formulations, and those stronger formulations are therefore rejected.

## 9. Deterministic symbolic checker

Checker:

`research_checks/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK_20260831.py`

Its role is limited. It certifies:

- the seven exterior-count blocks in `H^6_C`;
- separation of `(3,3)` divisor weight from `(6,0)/(0,6)` exceptional weights;
- the semihomogeneous `ch_3` coefficient algebra;
- Newton-identity consistency for `c_2,c_3`;
- extension/shift additivity at sample regression points;
- complete codimension-three Chern monomial shapes for Thom-Porteous reduction;
- scalar closure under model isogeny pull/push;
- preservation of primitive Weil weights as a boundary test;
- the modulo-three Gaussian norm gate.

Frozen run:

`HODGE_H0N_CHECKS=110`
`HODGE_H0N_FAILURES=0`
`HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK: PASS`

The checker does not pretend to prove Mukai's, Orlov's, or Thom-Porteous's unbounded theorems. Those are source mathematics; the checker only certifies the finite/symbolic reductions used after those theorems are invoked.

## 10. Tool reuse resolution

`enterprise_toolbox_registry.json` was checked after the task was understood. The current Enterprise toolbox contains no general-purpose Hodge/semihomogeneous-source classifier matching this proof obligation. No new global tool family is introduced.

Resolution:

`NO_NEW_GENERAL_PURPOSE_TOOL / TASK_LOCAL_SYMBOLIC_CHECKER_ONLY`.

## 11. Exact terminal frontier

The following broad natural target-side sources are now removed:

1. semihomogeneous bundles and their finite extension/shift envelope;
2. their target-side Fourier-Mukai autoequivalence orbit, including line-bundle seeds;
3. the polarization + target `K`-endomorphism tautological source algebra;
4. Thom-Porteous/determinantal cycles whose input Chern data is tautological;
5. graph/divisor `K`-tautological correspondence operators.

All of them have zero exceptional `W_K` projection in codimension three on the declared very-general target.

What remains is exact:

`CONSTRUCT_A_TARGET_SIDE_NON_SEMIHOMOGENEOUS_ALGEBRAIC_OR_DERIVED_OBJECT_E_WITH_PROJ_W(CH3(E))_NONZERO`

or

`CONSTRUCT_A_GENUINELY_NONTAUTOLOGICAL_ALGEBRAIC_CORRESPONDENCE_WITH_NONZERO_WK_IMAGE`.

A particularly sharp object-side diagnostic is:

`normalized_ch(E)=ch(E) exp(-c_1(E)/rk(E))`.

For every positive-rank semihomogeneous seed this collapses to the rank and has no middle component. Therefore a successful positive-rank seed must have nontrivial normalized higher characteristic class, and specifically a nonzero `B_0+B_6` degree-six component.

Only after such an object exists does it become meaningful to compute its `Ext^1`, `Ext^2`, semiregularity map, or obstruction-cancellation package. Semiregularity remains downstream, not a seed generator.

Freeze boundary reached.
