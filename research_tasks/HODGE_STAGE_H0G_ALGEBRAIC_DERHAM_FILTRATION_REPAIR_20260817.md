# HODGE Stage H0G — Algebraic de Rham Filtration Repair / Hodge-Side Operational Source

Date: `2026-08-17`
Status: `ACTIVE / DRIVER-ISSUED TASKBOOK`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Task ID: `RS-HODGE-H0G-ALGEBRAIC-DERHAM-FILTRATION-REPAIR-ATTRIBUTED-R2`
identity_policy: `AUTO_RESOLVE_OR_ALLOCATE`
identity_lane: `HODGE-H0G-DERHAM-FILTRATION-REPAIR`
owner branch: `research/hodge-h0g-derham-filtration-repair`
control branch: `research/hodge-special-control-plane`
parent H0D robust-R2 head: `102f6c73a099a97a412e72c810f8e63d2c370234`
parent H0E frozen head: `01bda7971b3023c486985bfe008ddfebbced52aa`
parent H0F frozen head: `9d7f28e706371c5485c5777a7ef7cda45b61e3c6`

## 0. Driver acceptance of H0F

H0F is accepted as a valid negative algebraic-source result.

Frozen disposition:

`H0F_R1_SOURCE_NORMAL_FORM_ALREADY_COMPLETE`

Frozen hard-target result:

`ALGEBRAIC_KAHLER_FORM_SOURCE_INSTANTIATES_ROBUST_ATTRIBUTED_R2 = NOT_ESTABLISHED`.

H0F proved that exact `P^2_C / Omega^1(m)` chart transport genuinely has non-diagonal Jacobian mixing and cancellation.  Weak componentwise pole summaries fail.  Nevertheless, as long as the theorem-critical observation asks only whether the **whole form is regular on future standard charts**, the source-native whole-form regularity support gives a complete recursive interface:

`rho(omega,c) = (1[P(c) in RegSupp(omega)], 1[M(c) in RegSupp(omega)])`.

On all frozen H0F instances,

`ker(Sigma_i) = ker(rho_i)`.

Therefore increasing twist, coefficient complexity, seed windows, or Jacobian mixing while retaining finite chart-regularity as the only theorem-critical observation is not an admissible next route.

H0G changes the **algebraic theorem-critical obligation**.

---

## 1. Mission

The next source must be cohomological/Hodge-filtration-adjacent rather than regularity-only.

Primary source:

`X = P^2_C`

with its standard three-affine cover `U_0,U_1,U_2`, and the algebraic Čech–de Rham total complex for `Omega_X^bullet` on that cover.

Primary degree / filtration:

- total cohomological degree `2`;
- Hodge filtration index `p=1`;
- source question: whether a closed total degree-2 algebraic de Rham cocycle can be changed by an exact total coboundary so that all de Rham-degree `<1` components vanish.

Equivalently, on the exact declared source carrier, seek an operational realization of the filtration-lift predicate

`[z] in F^1 H^2_dR(X)`.

Do **not** use the known Hodge numbers of `P^2`, the hyperplane class, a known divisor/cycle representative, or the fact that the Hodge conjecture is known for this toy object as generator data.

Single hard target:

`ALGEBRAIC_DERHAM_FILTRATION_SOURCE_INSTANTIATES_ROBUST_ATTRIBUTED_R2`.

Preferred stronger outcome:

`HODGE_FILTRATION_R3_PRESEED`.

H0G does not prove Hodge and does not automatically start H1.

---

## 2. Classical comparison boundary — typed control only

Use these only to type why the source is genuinely Hodge-adjacent:

1. A. Grothendieck, *On the de Rham cohomology of algebraic varieties*, Publ. Math. IHÉS 29 (1966), 95–103, DOI `10.1007/BF02684807`.
2. P. Deligne, *Théorie de Hodge II*, Publ. Math. IHÉS 40 (1971), 5–57, DOI `10.1007/BF02684692`.

Permitted boundary statement:

- for smooth complex algebraic varieties, algebraic de Rham hypercohomology compares to the complex cohomology of the associated analytic/topological realization in the scope of the algebraic de Rham theorem;
- for smooth projective complex varieties, the Hodge filtration is represented by the filtered de Rham complex / stupid filtration in the classical Hodge-theoretic comparison.

For a rational class `alpha in H^{2p}(X,Q)`, its complexification is fixed by conjugation.  H0G may prove and use the elementary typed consequence that, in weight `2p`,

`alpha is of type (p,p) <=> alpha_C in F^p`

provided the exact Hodge-structure hypotheses are stated.  This is a comparison/type statement, not a cycle theorem.

Forbidden inference:

`F^p membership => algebraic cycle`.

Also forbidden:

- using the known `P^2` Hodge decomposition as source data;
- using Lefschetz `(1,1)` as a generator;
- using known cycle representatives to select a repair or quotient.

---

## 3. Frozen authority / minimum startup packet

Read only the smallest sufficient packet:

1. `AGENTS.md`
2. `docs/GITHUB_INTERACTION_BUDGET.md`
3. `research_common_surface.json`
4. `driver_handoffs/HODGE_SPECIAL_DRIVER_HANDOFF_20260817.md`
5. `driver_handoffs/HODGE_SPECIAL_DRIVER_PI_GEOMETRY_ADDENDUM_20260817.md`
6. H0A0 Criterion V2 artifacts at `f4e6cf84eb191e0b7442913e018e1f6347e9584e`.
7. H0D0 attribution-addendum artifacts at `96e79629b822a8cb3bc11be1cec8abe319e4cd20`.
8. H0D robust attributed-R2 artifacts at `102f6c73a099a97a412e72c810f8e63d2c370234`.
9. H0F checkpoint at `9d7f28e706371c5485c5777a7ef7cda45b61e3c6`.
10. `native_semantics_admissibility.json`.

Classical Čech/de Rham/hypercohomology machinery is prior art.  It may be used to define the source and fair source baseline, but never receives Enterprise novelty credit.

Do not recursively traverse the repository.

---

## 4. Exact algebraic source

### 4.1 Standard cover

Use the standard affine cover of `P^2_C`:

`U_i = {X_i != 0}`, `i=0,1,2`.

All pairwise and triple intersections are explicit algebraic localizations.

### 4.2 Čech–de Rham total complex

Fix one sign convention and type it exactly.

A total-degree-2 source state has the schematic form

- Čech degree 0 / de Rham degree 2: local algebraic `2`-forms on `U_i`;
- Čech degree 1 / de Rham degree 1: algebraic `1`-forms on `U_i∩U_j`;
- Čech degree 2 / de Rham degree 0: algebraic functions on `U_0∩U_1∩U_2`.

Write the exact total differential `D` from the chosen Čech differential `delta` and algebraic de Rham differential `d`.

Mandatory theorem/check:

`D^2 = 0`

on the declared algebraic source class.

### 4.3 Finite exact subcarrier

H0G may not enumerate the infinite Čech–de Rham complex directly.

Before any quotient-success evaluation, predeclare a finite seed family and deterministically generate a finite-dimensional exact subcarrier by closure under all source operations actually used:

- restriction/localization;
- `delta`;
- `d`;
- total differential `D`;
- declared repair/coboundary operations.

Preferred exact arithmetic carrier: rational coefficients in a fixed algebraic monomial/form basis when the source formulas have rational structure constants, followed by an explicit embedding into `C`.

Important:

`Q-valued coordinate arithmetic in the finite algebraic model != rational singular cohomology class`.

Do not conflate them.

The closure procedure and coefficient/degree bounds must be frozen before behavior-quotient success is inspected.

---

## 5. The theorem-critical filtration-repair predicate

Let `K^*` denote the finite exact total-complex carrier.

Let

`z in K^2`, `D z = 0`.

Let `F^1 K^2` denote total degree-2 states whose components all have de Rham degree at least `1`; in particular the Čech-degree-2 / `Omega^0` component must vanish.

Define the source predicate independently:

`FILTRATION_LIFT_1(z)` iff there exists `b in K^1` such that

`z + D b in F^1 K^2`.

The sign `+`/`-` is convention-dependent; freeze one consistent convention.

This is a finite exact analogue of representing the same algebraic de Rham class in filtration `F^1`.

Required controls:

- at least one `FILTRATION_LIFT_1 = true` instance;
- at least one `false` instance in the declared finite subcarrier, unless a theorem proves the chosen finite carrier makes every instance true, in which case change the predeclared carrier before quotient evaluation rather than post-selecting labels;
- exact coboundary invariance;
- exact cocycle condition;
- no use of known `P^2` cohomology basis/classes.

---

## 6. Multi-step repair language

H0G must not reduce the source to one matrix yes/no query and then call row reduction Enterprise.

Construct a genuine multi-step operational language from the filtration-repair problem.

Permitted stage variables include, if generated naturally from the total complex:

- local `K^1` repair blocks on `U_i`;
- overlap function/one-form repair blocks;
- ordered elimination/gluing cuts;
- residual low-filtration components;
- residual cocycle/compatibility obligations.

At least three nontrivial repair/gluing stages are required for the primary finite source.

Each stage must have an exact algebraic meaning; do not invent arbitrary `L/R` actions merely to mimic H0D.

The final observation must be theorem-critical for `FILTRATION_LIFT_1`, not chart regularity.

---

## 7. Candidate G1 — full future repair quotient

For a partial repair state `s` at cut `i`, define a complete remaining repair/obstruction behavior signature `Sigma_i(s)` over the declared remaining repair language.

The exact signature may be Boolean, finite obstruction-valued, or a typed linear relation; choose the strongest finite exact language justified by the source.

Define

`q_i(s)=q_i(t) iff Sigma_i(s)=Sigma_i(t)`.

Required theorems:

1. soundness for every remaining repair query;
2. descended next-stage repair transitions are well-defined;
3. the final filtration-lift predicate factors through the quotient;
4. coarsest sufficiency on the exact declared behavior language, if claimed;
5. exact comparison to source execution.

A generic future-signature/minimal-automaton theorem is prior art and earns no novelty credit.  R2 depends on attribution against the fair source baseline.

---

## 8. Candidate G2 — Enterprise repair recoalescence

Use BRC/recoalescence only if it adds a distinct operational mechanism.

Question:

Can two distinct local repair histories be forgotten because they induce the same remaining filtration-obstruction state, with an exact theorem that future gluing/repair behavior is preserved?

Distinguish:

- class discovery / quotient formation;
- ordinary union/linear combination/coboundary algebra already available at source.

If G2 only executes G1 classes, mark it auxiliary/shared attribution.

---

## 9. Candidate G3 — obstruction / normal-form realization

Search for an independently defined Enterprise operational obstruction object `Ob_E(z)` such that

`FILTRATION_LIFT_1(z) <=> Ob_E(z)=0`

on the declared carrier, or the strongest correct one-sided theorem.

Allowed leverage classes:

- `FINITE_OBSTRUCTION_BASIS`;
- `DEPENDENCY_REDUCTION`;
- `COMPOSITIONAL_FACTORING`;
- `NORMAL_FORM`;
- `LAYER_LOWERING`;
- another exact V2 class with predeclared witness.

Hard anti-tautology:

Do not define `Ob_E` as `0` exactly when `FILTRATION_LIFT_1` is known to be true.

Its Enterprise-side definition must use declared primitives/derived operations before comparison.

---

## 10. Fair source-baseline sandwich

This gate is mandatory and must be frozen before Enterprise quotient/obstruction success counts are used.

### `B_raw^dR`

Must permit at least:

- exact algebraic Čech restriction/localization;
- algebraic `d`;
- Čech `delta`;
- total differential `D`;
- explicit cochain/coboundary execution;
- brute-force/exact linear solve on the declared finite carrier.

### `B_std^dR`

Must strengthen `B_raw^dR` with all source-native mathematics that a fair algebraic geometer would obviously use, including at least:

- exact finite-dimensional linear algebra over the declared coefficient field;
- Gaussian elimination / RREF or equivalent exact kernel-image solving;
- kernel/image/cokernel and quotient-space formation;
- ordinary Čech–de Rham total-complex identities;
- the truncated-complex inclusion `F^1 K -> K`;
- the source-native projected obstruction to eliminating the de Rham-degree-0 total component, if derivable independently;
- any source-native spectral-sequence / filtration normal form actually used at the finite declared scope;
- change of basis and cover relabeling.

Do **not** weaken `B_std^dR` merely to preserve Enterprise credit.

Do not automatically install the exact Enterprise future-behavior quotient unless it is already independently a source-native normal form.

### Attribution outcomes

Use H0D0 semantics:

- `ROBUST_TRANSFORM_ATTRIBUTED`;
- `BASELINE_SENSITIVE_ATTRIBUTION`;
- `SOURCE_INHERITED_LEVERAGE`;
- `ATTRIBUTION_SHARED_OR_PARTIAL`;
- `ATTRIBUTION_UNRESOLVED`.

Only `ROBUST_TRANSFORM_ATTRIBUTED` may satisfy the H0G hard target.

---

## 11. Baseline-gaming controls

Mandatory controls:

1. A finite linear system whose apparent Enterprise reduction is exactly Gaussian elimination / quotient by a known source kernel.  It must fail robust attribution under `B_std^dR`.
2. H0D D1 remains a positive abstract prior-art transform-attribution control.
3. H0E/H0F source-normal-form no-go results remain valid on their frozen scopes.

The checker must reject:

`B_raw win => robust attribution`.

---

## 12. Hodge-side typed bridge

H0G must produce an explicit bridge registry, even if no R2 survives.

At minimum distinguish:

- `C_H(X)` rational cohomology + Hodge filtration/decomposition;
- `H_dR^2(X/C)` algebraic de Rham comparison target;
- `F^1 H_dR^2` filtration side;
- the finite `K^*` source carrier as a bounded computational/algebraic subcarrier, **not automatically all of** `H_dR^2`.

State exactly what theorem is classical and what remains unproved.

The finite source may not be advertised as a complete model of all `H^2_dR(P^2)` unless completeness is separately proved without using the known Hodge answer.

### Rational Hodge-class boundary

If using

`alpha in H^2(X,Q)` and `alpha_C in F^1`,

state the rational/conjugation argument exactly and separate it from the finite algebraic carrier.

No integral-Hodge substitution.

---

## 13. R3 preseed gate

An H0G `HODGE_FILTRATION_R3_PRESEED` is allowed only if all of the following hold:

1. a robust transform-attributed R2 passes on the actual algebraic filtration-repair source;
2. the Hodge-side rational-class -> de Rham filtration interface is typed without target leakage;
3. the finite operational constraint is linked to the declared filtration-lift predicate by an exact theorem;
4. an explicit downstream algebraic-cycle/Chow lifting interface is written with unresolved obligations;
5. known cycles are absent from generator data.

The lifting interface must identify, not solve, at least:

- how an Enterprise filtration/obstruction state would produce or constrain codimension-1 line-bundle/divisor data;
- cycle-class compatibility;
- rational coefficient/scaling compatibility;
- presentation/descent independence;
- existence and lifting correctness.

Do **not** invoke Lefschetz `(1,1)` as the proof of this interface.

If R2 fails, no R3 preseed is allowed.

---

## 14. Prior-art / novelty firewall

Treat as classical/source prior art unless a separate novelty theorem is proved:

- algebraic de Rham theorem;
- Hodge filtration from the filtered de Rham complex;
- Čech cohomology and Čech–de Rham total complexes;
- hypercohomology;
- spectral sequences;
- Gaussian elimination / RREF;
- kernel/image/cokernel/cohomology quotient;
- standard homological algebra;
- minimal linear realization / behavioral quotient when applicable.

Prior-art status is **not** an R2 veto.

The attribution gate, not novelty, decides Hodge-special route credit.

---

## 15. Presentation / functoriality subgate

At the exact claimed scope test:

- permutations of homogeneous coordinates of `P^2`;
- induced permutation of the standard affine cover;
- sign convention / orientation consistency for Čech indices;
- regular local basis changes for forms/cochains;
- at least one algebraic automorphism/permutation stress on the generated finite carrier.

Do not claim arbitrary-cover/refinement independence unless proved.

---

## 16. Target leakage firewall

Forbidden generator inputs:

- known Hodge numbers of `P^2`;
- known basis of `H^2(P^2)`;
- hyperplane/divisor class chosen because it is the expected answer;
- known algebraic-cycle representatives;
- Lefschetz `(1,1)` conclusion/proof;
- harmonic representatives or Kähler metric;
- Hodge decomposition truth values for candidate source states;
- cycle-class answers used to select a quotient/obstruction.

Allowed classical comparison data must be logged as `CONTROL_OR_TYPED_BRIDGE_ONLY`.

---

## 17. Required artifacts

At minimum produce:

1. `research_results/HODGE_H0G_CLASSICAL_HODGE_DERHAM_BRIDGE.json`
2. `research_results/HODGE_H0G_CECH_DERHAM_SOURCE_SPEC.json`
3. `research_results/HODGE_H0G_FINITE_SUBCOMPLEX_GENERATION.json`
4. `research_results/HODGE_H0G_TOTAL_DIFFERENTIAL_DERIVATION.json`
5. `research_results/HODGE_H0G_FILTRATION_REPAIR_REGISTRY.json`
6. `research_results/HODGE_H0G_MULTISTEP_REPAIR_LANGUAGE.json`
7. `research_results/HODGE_H0G_SOURCE_BASELINE_SANDWICH.json`
8. `research_results/HODGE_H0G_FUTURE_QUOTIENT_REGISTRY.json`
9. `research_results/HODGE_H0G_OBSTRUCTION_REGISTRY.json`
10. `research_results/HODGE_H0G_COMPARISON_THEOREM_REGISTRY.json`
11. `research_results/HODGE_H0G_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json`
12. `research_results/HODGE_H0G_ATTRIBUTION_CERTIFICATE_REGISTRY.json`
13. `research_results/HODGE_H0G_BASELINE_GAMING_CONTROL.json`
14. `research_results/HODGE_H0G_PRESENTATION_NATURALITY_LEDGER.json`
15. `research_results/HODGE_H0G_RATIONAL_HODGE_BOUNDARY.json`
16. `research_results/HODGE_H0G_R3_PRESEED.json`
17. `research_results/HODGE_H0G_PRIOR_ART_NOVELTY_LEDGER.json`
18. `research_results/HODGE_H0G_TARGET_LEAKAGE_LEDGER.json`
19. `research_results/HODGE_H0G_CLASSIFICATION.json`
20. `research_results/HODGE_H0G_SEMANTIC_CHECKPOINT.md`
21. deterministic checker + output;
22. manifest with SHA-256 digests.

---

## 18. Mandatory checker gates

At minimum verify:

- actual `P^2` algebraic Čech–de Rham source formulas are used;
- `D^2=0` on declared source;
- finite subcomplex/source carrier is frozen before quotient evaluation;
- coordinate-Q arithmetic is not equated with rational singular cohomology;
- filtration-repair predicate is independently defined;
- at least one positive and one negative repair control, or an exact theorem explaining why one side is absent;
- multi-step depth >= 3;
- `B_raw^dR` and `B_std^dR` frozen before success evaluation;
- standard linear algebra/homological normal forms are admitted to `B_std^dR`;
- any R2 has V2 proof-leverage + H0D0 attribution certificates;
- novelty does not decide rank;
- Hodge/de Rham bridge typed separately from finite carrier completeness;
- no known Hodge/cycle answer leakage;
- R3 preseed requires robust R2 first;
- H1 remains blocked;
- no Hodge proof claim.

Checker PASS is protocol/exact-source consistency only.

---

## 19. Allowed final dispositions

Freeze exactly one:

### `H0G_ROBUST_ATTRIBUTED_DERHAM_FILTRATION_R2_FOUND`

Actual algebraic filtration-repair source + strict V2 leverage + robust attribution pass.

### `H0G_HODGE_FILTRATION_R3_PRESEED_FOUND`

R2 passes and the typed Hodge/de Rham/operational/lifting preinterface satisfies Section 13.  No lifting theorem/Hodge proof is claimed.

### `H0G_R1_SOURCE_COHOMOLOGICAL_NORMAL_FORM_ALREADY_COMPLETE`

The fair source baseline already contains an operational normal form of the same theorem-critical strength as the Enterprise quotient/obstruction.

### `H0G_R1_ALGEBRAIC_SOURCE_REALIZED_NO_ROBUST_ATTRIBUTION`

Source and Enterprise realization are exact, but attribution is baseline-sensitive/source-inherited for another precise reason.

### `H0G_FAIL_FINITE_ALGEBRAIC_SOURCE_GENERATION`

The declared finite exact filtration-repair source cannot be generated/closed without forbidden or target-dependent structure.

### `H0G_ATTRIBUTION_UNRESOLVED`

Only for a concrete missing source-baseline or comparison theorem.

No other disposition without Driver review.

---

## 20. Route decision required

H0G must end with exactly one Driver-facing route recommendation:

1. `PROMOTE_TO_R3_BRIDGE_SEARCH`
2. `HODGE_FILTRATION_RECOGNITION_SOURCE_COMPLETE__PIVOT_TO_ALGEBRAIC_LIFTING`
3. `SEARCH_DIFFERENT_COHOMOLOGICAL_OPERATIONAL_SOURCE`
4. `SOURCE_MODEL_REPAIR_REQUIRED`
5. `ATTRIBUTION_CRITERION_REPAIR_REQUIRED`

Do not automatically execute the recommendation.

---

## 21. H1 firewall

`H1 = NOT_ADMISSIBLE` during H0G.

Even an R3 preseed returns to Driver review.

Do not build an Enterprise chain/cochain/cohomology theory in this stage.  The Čech–de Rham complex is the **classical algebraic source**, not Enterprise H1.

---

## 22. Advancement vector

Before H0G:

- Criterion V2: `FROZEN`;
- attribution criterion: `FROZEN`;
- abstract robust attributed R2: `FOUND at H0D`;
- scalar actual algebraic attributed R2: `FAILED / source normal form H0E`;
- differential-mixing actual algebraic attributed R2: `FAILED / source normal form H0F`;
- Hodge filtration operational source: `OPEN`;
- R3: `NOT FOUND`;
- H1: `NOT ADMISSIBLE`.

A successful H0G advances the route from local regularity semantics to a theorem-critical filtered-cohomological obligation.

Advancement vector:

`Hodge-side typing +25 / algebraic deRham source +25 / filtration-repair semantics +30 / attribution test +25 / cycle lifting +0 / H1 +0`.

---

Driver return target:

`EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`

Do not automatically start a later stage.