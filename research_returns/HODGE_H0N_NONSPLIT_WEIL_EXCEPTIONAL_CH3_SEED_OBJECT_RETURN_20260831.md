# HODGE H0N — Non-Split Weil Sixfold Exceptional `ch_3` Seed Object Gate Return

Researcher-ID: `EM-HODGEH0N-40AF21`
Task-ID: `RS-HODGE-H0N-NONSPLIT-WEIL-EXCEPTIONAL-CH3-SEED-OBJECT`
Publication: `TP2-9A71D4C6E2B5083F16CD`
Claim: `chatgpt-hodgeh0n-20260831-1344`
Execution branch: `research/hodge-h0n-exceptional-ch3-seed-em-hodgeh0n-40af21`
Date: `2026-08-31`

## Verdict

Primary terminal classification:

`NATURAL_SOURCE_FAMILY_NO_GO_CLASSIFIED_WITH_NONTAUTOLOGICAL_FRONTIER_OPEN`.

Hard target:

`NONSPLIT_WEIL_SIXFOLD_TARGET_SIDE_EXCEPTIONAL_CH3_SEED_OBJECT_CONSTRUCTED_OR_NATURAL_SOURCE_FAMILY_NO_GO_CLASSIFIED = SATISFIED_AT_NEGATIVE_FAMILY_NO_GO_STRENGTH`.

No target-side object with nonzero exceptional Weil projection of `ch_3` is constructed. Instead, the task closes five broad **natural/tautological source families** by theorem-level structural no-go. The surviving object-first frontier is sharply narrower:

- a target-side **non-semihomogeneous** algebraic/derived object with a primitive codimension-three characteristic class, or
- a genuinely **non-tautological algebraic correspondence** whose degree-six image has nonzero projection to `W_K`.

No non-algebraicity statement, no Hodge-conjecture claim, and no H1 promotion is made.

## 1. Independent audit of the H0M premises actually used

H0N does not inherit Working Truth from H0M. The following ingredients were independently rechecked from the pinned H0M model and by direct linear/algebraic verification.

### 1.1 Exact target model and discriminant component

Take `K=Q(i)`, `U=K^6`, `Lambda=Z[i]^6`, and

`h=diag(1,1,1,-1,-1,-3)`.

Then `h` has signature `(3,3)` and determinant `-3`, hence Hermitian discriminant class `[-3]` in

`Q^*/Nm_{K/Q}(K^*)`.

The split sixfold class is `[-1]`. Their ratio is `3`. If `3` were a norm from `Q(i)`, after clearing denominators there would be coprime integers

`x^2+y^2=3z^2`.

Modulo `3`, the only solution of `x^2+y^2=0` is `x=y=0`, forcing `3|x,y`, and then the displayed equation forces `3|z`, contradiction. Thus `3` is not a rational Gaussian norm and

`[-3] != [-1]`.

This independently confirms that the declared target component is genuinely non-split and cannot be identified with the split positive-control component by a `K`-Hermitian similitude.

### 1.2 Exceptional Weil carrier

Let `V=H^1(A,Q)` for a very general member `A` of the fixed `[-3]` Weil-type component. Since `dim_K V=6`,

`W_K(A)=wedge_K^6 V`

is one-dimensional over `K`, hence two-dimensional over `Q`.

After complexifying with the two embeddings `sigma, sigma_bar` of `K`,

`V_C = V_sigma direct-sum V_sigma_bar`

and

`W_K(A)_C = wedge^6 V_sigma direct-sum wedge^6 V_sigma_bar`.

Because the Weil signature is `(3,3)`, both determinant lines are of Hodge type `(3,3)`. Hence every rational vector of `W_K` is a rational Hodge class of degree six.

### 1.3 Exact exceptional projection / divisor separation

For bookkeeping define the exterior-count blocks

`B_a = wedge^a V_sigma tensor wedge^(6-a) V_sigma_bar`, `0<=a<=6`.

Then

`H^6(A,C)=direct-sum_{a=0}^6 B_a`

and

`W_K(A)_C = B_6 direct-sum B_0`.

For a very general target, `NS(A)_Q=Q*theta`, where `theta` is the polarization class. Since a rational `(1,1)` divisor class has one `sigma` and one `sigma_bar` leg, `theta^3` belongs to `B_3`. Therefore

`proj_W(theta^3)=0`,

and indeed

`W_K(A) intersect Q*theta^3 = 0`.

This direct-summand description is the projection convention used throughout the Return. It does not assume algebraicity of `W_K`.

### 1.4 Split-source transport wall

For a six-dimensional `K`-Hermitian similitude

`h' = c g^* h g`, `c in Q^*`,

one has

`det(h') = c^6 Nm(det g) det(h)`.

The factors `c^6=Nm(c^3)` and `Nm(det g)` are norms. Hence the discriminant class is invariant. The split `[-1]` source component therefore cannot be transported to this `[-3]` target by the standard `K`-compatible similitude/isogeny route. This is used only as a leakage firewall; H0N's family no-go below is proved directly on the target.

Result of the premise audit:

`H0M_USED_PREMISES_REVERIFIED = PASS`.

No part of H0N depends on accepting H0M's terminal Driver disposition.

## 2. Literature/frontier boundary rechecked

The source boundary was rechecked at exact claim strength.

1. Mukai's semihomogeneous-bundle theory supplies the Chern-character exponential formula used below. This is classical source mathematics, not an Enterprise discovery.
2. Orlov/Mukai Fourier-Mukai theory supplies the preservation/transport facts for semihomogeneous objects used in the target-side FM no-go.
3. Markman's 2025 sixfold theorem concerns the discriminant `-1` / split locus. It is a positive control showing that any no-go stated for all Weil sixfolds would be false.
4. Koike's Gaussian-field Prym construction gives another positive-control algebraicity result on a different discriminant regime. It again prevents promotion of the target-side family no-go to universal non-algebraicity.
5. The declared `[-3]` target-side exceptional seed remains an open object-level frontier under the sources checked here.

The present result is therefore a **source-family classification**, not a historical novelty claim about semihomogeneous theory, Fourier-Mukai theory, Thom-Porteous formulas, or Weil-type Hodge classes.

## 3. Family F1 — semihomogeneous bundles, sums, shifts, and extensions

### Theorem F1

Let `A` be the very general target above with `NS(A)_Q=Q*theta`. Let `E` be a simple semihomogeneous vector bundle of rank `r>0`. Then

`proj_W(ch_3(E))=0`.

The same conclusion holds for every finite direct sum, shift, or iterated extension whose simple semihomogeneous constituents have positive rank.

### Proof

For a simple semihomogeneous vector bundle, Mukai's Chern-character formula is

`ch(E)=r exp(c1(E)/r)`.

Hence

`ch_3(E)=c1(E)^3/(6 r^2)`.

Because `NS(A)_Q=Q*theta`, write `c1(E)=q theta`. Therefore

`ch_3(E)=q^3 theta^3/(6 r^2) in Q*theta^3`.

By the direct-summand audit above, `proj_W(theta^3)=0`, so `proj_W(ch_3(E))=0`.

Chern character is additive in `K_0(A)`. Finite direct sums and short exact extensions add Chern characters, while a derived shift changes sign in `K_0`. Therefore every finite object assembled additively from these constituents still has degree-six Chern character in `Q*theta^3`, and has zero exceptional projection. QED.

### Strong diagnostic form

The normalized character satisfies

`ch(E) exp(-c1(E)/r)=r`.

Thus a successful positive-rank seed on this target cannot be simple semihomogeneous: it must carry a genuinely primitive higher characteristic class not determined by rank and `c1` alone.

This is the first exact narrowing of the H0M missing-object statement.

## 4. Family F2 — target-side Fourier-Mukai orbit of line/semihomogeneous sources

### Theorem F2

Consider a Fourier-Mukai autoequivalence of the target derived category whose kernel defines the usual abelian-variety equivalence and whose source object is a line bundle or semihomogeneous object on the **same target-side equivalence geometry**. If the resulting object has positive-dimensional/full support and remains semihomogeneous, then its `ch_3` has zero exceptional projection by F1. If it is point-supported, its codimension-three Chern-character component is zero on a sixfold. Therefore the target-side FM orbit of the declared line/semihomogeneous source class does not supply an exceptional `ch_3` seed.

### Proof and scope

Semihomogeneity is characterized by a maximal-dimensional stabilizer under translations and degree-zero twists; the standard Fourier-Mukai equivalence induces the corresponding symplectic isomorphism of `A x Ahat`, so the semihomogeneous stabilizer property is preserved for the appropriate transforms. Consequently a line/semihomogeneous source that transforms to a positive-rank/full-support semihomogeneous object is covered by F1.

The familiar extreme transform of a degree-zero line bundle can be point-supported. On a sixfold its Chern character begins in codimension six; in particular `ch_3=0`. Hence this boundary case cannot hit `H^6` either.

This theorem deliberately does **not** claim that every Fourier-Mukai image of every arbitrary complex is semihomogeneous. An input already possessing a primitive degree-six class would simply move the problem into the input. The no-go is exactly for the natural line/semihomogeneous FM source family declared by the task.

No split-to-`[-3]` transport is used.

## 5. Family F3 — polarization plus target `K`-endomorphism tautological algebra

### Definition

Let `T_K(A)` be the rational `K_0`/cohomological source envelope generated from line bundles and positive-rank semihomogeneous target-side objects by finite sums, differences/cones, tensor products, duals, and pullback/pushforward along nonzero target `K`-endomorphism isogenies.

### Theorem F3

For every `x in T_K(A)`, the codimension-three component satisfies

`ch_3(x) in Q*theta^3`,

and therefore `proj_W(ch_3(x))=0`.

### Proof

The generators have Chern characters in `Q[theta]` by F1 and the line-bundle formula `ch(L)=exp(c1(L))`.

The ring operations `+,-,tensor,dual` preserve `Q[theta]`.

Now let `f:A->A` be a nonzero target endomorphism isogeny induced by the declared `K`-endomorphism structure. Because `NS(A)_Q=Q*theta`, there is a rational scalar `lambda_f` with

`f^* theta = lambda_f theta`.

Therefore `f^*(Q[theta]) subset Q[theta]` and, in degree six,

`f^*(theta^3)=lambda_f^3 theta^3`.

For finite `f`, the cohomological identity

`f_* f^* = deg(f) id`

implies on the one-dimensional line `Q*theta^3` that `f_*` also preserves that line. Thus pull-push closure cannot escape `Q[theta]` in codimension three.

Hence every degree-six Chern-character output of `T_K(A)` lies in `Q*theta^3` and has zero exceptional projection. QED.

The result is stronger than the split-discriminant transport wall because it is an intrinsic target-side tautological closure theorem.

## 6. Family F4 — tautological degeneracy/determinantal constructions

### Definition

A **tautological determinantal input** is a finite vector-bundle/complex datum whose relevant Chern classes satisfy

`c_j in Q*theta^j`

for all indices used by the construction. This includes the F1-F3 source envelope.

### Theorem F4

Every codimension-three Thom-Porteous/Schur class formed universally from such inputs lies in `Q*theta^3`. Hence it has zero exceptional `W_K` projection.

### Proof

A universal codimension-three Chern-polynomial expression is homogeneous of total Chern weight `3`. Its monomial shapes are generated by

`c1^3`, `c1*c2`, `c3`.

Under `c_j in Q*theta^j`, every one of these is a rational multiple of `theta^3`. Determinantal/Schur polynomials are rational/integer linear combinations of these weight-three monomials, so the resulting codimension-three class belongs to `Q*theta^3` and has zero `W_K` projection. QED.

### Non-circular boundary

This theorem does not cover an input bundle or complex whose `c3` already has an exceptional component. Such an input would already be the sought H0N primitive source object. Calling it a “determinantal input” cannot be used to hide the construction problem.

Thus standard tautological degeneracy loci do not generate the missing primitive class ex nihilo.

## 7. Family F5 — `K`-tautological algebraic correspondences

### Definition

A `K`-tautological cohomological correspondence operator is generated by rational linear combinations and compositions of:

- graphs of nonzero target `K`-endomorphism isogenies and their transposes, hence pull/push;
- cup product by divisor classes;
- identities and the resulting compositions on the target.

### Theorem F5

Starting from the divisor/semihomogeneous tautological seed algebra `Q[theta]`, every such operator preserves that algebra. In degree six its image is contained in `Q*theta^3`, and hence cannot produce a nonzero exceptional `W_K` component.

### Proof

Divisor cup products preserve `Q[theta]`. Pullback and pushforward by the allowed endomorphism isogenies preserve `Q[theta]` by F3. Rational linear combination and composition preserve the same subalgebra. Therefore the degree-six image of a tautological seed remains on the line `Q*theta^3`, whose exceptional projection is zero. QED.

### Exact surviving correspondence frontier

A genuinely new algebraic correspondence not generated by these tautological operations is **not** ruled out. It is one of the two exact surviving routes.

## 8. Unified source-family no-go theorem

Let `S_nat` be the union of F1-F5 under the hypotheses stated above. Then

`proj_W(ch_3(E))=0`

for every object-class output in F1-F4, and every degree-six class obtained from the declared tautological seeds by F5 also has zero exceptional projection.

Equivalently:

`S_nat_degree6 subset Q*theta^3`,

while

`W_K(A) intersect Q*theta^3 = 0`.

Therefore

`S_nat_degree6 intersect W_K(A) = {0}`.

This is the exact negative success claimed by H0N.

It is not an assertion that all algebraic classes lie in `Q*theta^3`, nor that `W_K` is non-algebraic.

## 9. Active counterexample / falsifier audit

The no-go was pressure-tested against the following failure modes.

### 9.1 Split discriminant `-1` positive control

Known sixfold algebraicity on the split/discriminant-minus-one locus is a direct falsifier of any universal no-go. The present theorem therefore keeps the `[-3]` target and the declared source families explicit.

### 9.2 Gaussian-field Prym positive control

Classical Gaussian-field sixfold constructions on a solved discriminant regime show that non-tautological geometric constructions can escape the divisor algebra. This is consistent with H0N and is why the surviving non-tautological correspondence route is kept open.

### 9.3 Fourier-Mukai point-support boundary

A transform of a degree-zero line bundle can become point-supported rather than positive-rank semihomogeneous. This does not falsify F2: on a sixfold a point class has codimension six, hence its `ch_3` is zero.

### 9.4 Primitive-input boundary

If an arbitrary vector bundle/complex is admitted with an already nonzero exceptional component of `c3` or `ch_3`, F4 cannot conclude zero projection. But that is not a counterexample to the theorem; it is precisely the desired H0N seed and is excluded from the tautological-input hypothesis to avoid circularity.

### 9.5 Non-tautological correspondence boundary

No argument here rules out an algebraic correspondence whose cohomological action is not generated by divisor cups and target `K`-endomorphism pull/push. This remains an explicit unblock condition rather than being silently absorbed into the no-go.

Counterexample audit result:

`NO_SCOPE_INTERNAL_COUNTEREXAMPLE_FOUND; UNIVERSALIZATION_EXPLICITLY_REJECTED`.

## 10. Deterministic checker and certificate scope

Checker:

`research_checks/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK_20260831.py`

The checker verifies only finite/symbolic reductions genuinely appropriate for computation:

- the seven exterior-count blocks and the separation `B_0/B_6` vs `B_3`;
- `dim_Q W_K=2` in the frozen `K`-dimension-six model;
- the semihomogeneous `ch_3` coefficient obtained from `r exp(c1/r)` and Newton identities;
- additive/shift closure samples;
- complete weight-three Chern-monomial shapes `{c1^3,c1*c2,c3}`;
- scalar pullback/pushforward preservation of the `theta^3` line;
- explicit primitive-`W_K` boundary regression;
- point-support `ch_3=0` in dimension six;
- the modulo-three Gaussian norm gate used in the discriminant audit.

Frozen local execution:

`HODGE_H0N_CHECKS=110`

`HODGE_H0N_FAILURES=0`

`HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT_CHECK: PASS`.

The checker does not purport to prove Mukai's unbounded semihomogeneous theorem, Orlov/Mukai Fourier-Mukai theory, Thom-Porteous theory, or the generic Picard-rank theorem. Those are source mathematics and are cited/reported at exact strength.

Certificate:

`research_artifacts/HODGE_H0N_NONSPLIT_WEIL_EXCEPTIONAL_CH3_SEED_OBJECT/HODGE_H0N_SOURCE_FAMILY_NO_GO_CERTIFICATE.json`.

## 11. Tool reuse audit

The current Enterprise toolbox registry was checked before introducing machinery. No accepted global tool directly replaces the Hodge-theoretic source-family calculation. The exact gap is theorem-specific: Chern-character/exterior-count interaction with the exceptional Weil summands.

No new general-purpose tool is proposed. The checker is task-local structural regression only.

`TOOL_REUSE_RESOLUTION = NO_NEW_GENERAL_PURPOSE_TOOL_REQUIRED`.

## 12. Exact terminal frontier

H0N has converted the H0M missing-object statement into a sharper dichotomy.

A successful target-side positive seed must leave the closed natural envelope proved above. In particular, the next candidate should satisfy at least one of:

1. it is a genuinely **non-semihomogeneous** coherent sheaf/complex and one can compute a primitive degree-six `ch_3` component not determined by `rank,c1`;
2. it arises from a **non-tautological algebraic correspondence** whose action on degree-six cohomology can be proved to have nonzero projection to `B_0 direct-sum B_6`.

A plausible next research task should therefore not enumerate more line-bundle/semihomogeneous/FM-tautological variants. It should specify an exact non-semihomogeneous source geometry or an explicit new correspondence and make its exceptional projection falsifiable.

Terminal freeze:

`NATURAL_SOURCE_FAMILY_NO_GO_CLASSIFIED_WITH_NONTAUTOLOGICAL_FRONTIER_OPEN`.

No H1, no non-algebraicity, no Hodge-conjecture closure.
