# HODGE Stage H0J — Cubic-Fourfold Incidence / BRC Multipath Correspondence Lifting

Date: `2026-08-22`
Status: `ACTIVE / DRIVER-ISSUED TASKBOOK`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Task ID: `RS-HODGE-H0J-CUBIC-FOURFOLD-BRC-MULTIPATH-CORRESPONDENCE-LIFTING`
identity_policy: `AUTO_RESOLVE_OR_ALLOCATE`
identity_lane: `HODGE-H0J-BRC-CORRESPONDENCE`
owner branch: `research/hodge-h0j-cubic-fourfold-brc-correspondence`
control branch: `research/hodge-special-control-plane`

## 0. Driver acceptance of H0I

H0I is accepted as a valid negative codimension-two class-first benchmark.

Frozen disposition:

`H0I_SOURCE_VECTOR_BUNDLE_CHOW_NORMAL_FORM_ALREADY_COMPLETE`.

Frozen hard-target result:

`CODIMENSION_TWO_CLASS_FIRST_LIFTING_SOURCE_INSTANTIATES_ROBUST_ATTRIBUTED_R2 = NOT_ESTABLISHED`.

H0I nevertheless established all of the following on the declared `Gr(2,4)` benchmark:

- a degree-four `(2,2)` target carrier was frozen before bundle search;
- the target was not defined from `c2(S)`, `c2(Q)`, Schubert cycles or a known Chow basis;
- a genuinely codimension-two direction independent of the divisor-square line was present;
- source-generated bundles/sections produced exact codimension-two cycles;
- exact class-first rational lifting existed on the declared two-dimensional target carrier;
- Boolean support was shown insufficient when scheme multiplicity differed;
- but GL2 gauge, Chern/zero-locus, ideal/Chow and rational matrix normal forms already supplied the same leverage in the fair source baseline.

H0I checker: `2465/2465 PASS`.
H0I semantic core: `46978c8e27574b7c76e5677687ec4d5678e7beb379c9bd4393d0523250a42d0d`.
H0I owner branch: `research/hodge-h0i-codim2-class-first-lifting`.

Scientific consequence:

`LOCAL_BUNDLE_CHERN_CHOW_CLASS_FIRST_BENCHMARK_IS_SOURCE_COMPLETE__CHANGE_OPERATIONAL_SOURCE`.

Do not rerun H0I with a larger bundle grammar, more Plucker charts, more sections, or another homogeneous variety while keeping the same Chern/ideal/matrix mechanism.

---

## 1. Mission

Change the operational source from local bundle/Chern/ideal normal forms to **algebraic correspondences with explicit multipath/fiber provenance**.

Primary benchmark:

- `X subset P^5_C` a smooth cubic fourfold;
- `F=F(X)` its Fano variety of lines;
- `P={(ell,x): x in ell} subset F x X` the universal incidence variety;
- projections `p:P->F`, `q:P->X`.

Classically, the Beauville-Donagi Abel-Jacobi/incidence correspondence gives a Hodge-theoretic bridge between primitive `H^4(X)` and primitive `H^2(F)`; the integral Hodge conjecture in degree four for cubic fourfolds is known (Voisin). These are **controls and fairness constraints**, not Enterprise generators.

Single hard target:

`BRC_MULTIPATH_ADDS_ROBUST_PROOF_LEVERAGE_BEYOND_CLASSICAL_INCIDENCE_CORRESPONDENCE`.

Preferred stronger target:

`CUBIC_FOURFOLD_CLASS_FIRST_ENTERPRISE_R3_PRESEED`.

The hard target is intentionally incremental: classical correspondence leverage does not count as Enterprise leverage.

---

## 2. Frozen authority

Mandatory startup packet:

1. `AGENTS.md`
2. `docs/GITHUB_INTERACTION_BUDGET.md`
3. `research_common_surface.json`
4. `FOUNDATIONAL_LOGIC.md`
5. `foundational_logic.json`
6. H0A0 Criterion V2 at `f4e6cf84eb191e0b7442913e018e1f6347e9584e`
7. H0D0 attribution criterion at `96e79629b822a8cb3bc11be1cec8abe319e4cd20`
8. H0D abstract robust-R2 result at `102f6c73a099a97a412e72c810f8e63d2c370234`
9. H0G filtered-recognition checkpoint at `2335f1b91998943c055b9c02d144d0128e6cdc29`
10. H0H-R1 semantic core `04a0abdad437e777bd2476e360fa17d30059580fd6fcbc4269bcb4844bfdb298`
11. H0I semantic core `46978c8e27574b7c76e5677687ec4d5678e7beb379c9bd4393d0523250a42d0d`
12. canonical BRC multipath enrichment definition `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` at commit `b5bdc33578f324b55a57e5bdff9cf9c3acc30034`

If native-plane geometry is invoked, use current canonical authority rather than any historical signed-origin foundation. Native plane geometry is **not required** for this stage and must not be imported merely to make the construction look Enterprise-specific.

Historical H0/H0A/H0B/H0C/H0E/H0F/H0G/H0H/H0I artifacts are read-only.

---

## 3. Classical benchmark controls

Use the following only with correct typing and attribution:

### C0 — Beauville-Donagi incidence transform

For a smooth cubic fourfold, the universal-line incidence correspondence classically induces the Abel-Jacobi/Hodge transform between primitive middle cohomology of `X` and primitive second cohomology of `F(X)`.

This may have genuine `LAYER_LOWERING` proof leverage relative to a bare `H^4(X)` presentation, but it is **classical prior art** and is not by itself Enterprise credit.

Freeze separate labels:

`CLASSICAL_INCIDENCE_TRANSFORM_LEVERAGE`

and

`ENTERPRISE_BRC_INCREMENTAL_LEVERAGE`.

Never merge them.

### C1 — Lefschetz `(1,1)` on `F(X)`

The p=1 algebraicity step is classical and H0H-R1 has already shown that Picard/divisor normal forms are source-complete at the audited level.

Do not claim H0J progress merely because an incidence-transformed `(1,1)` class can be represented by a divisor.

### C2 — Cubic-fourfold integral Hodge theorem

The known theorem that integral degree-four Hodge classes on smooth cubic fourfolds are algebraic is **checker/control only**.

No known algebraic surface representative may be fed into an Enterprise generator.

---

## 4. Actual algebraic source generation

H0J must use an actual algebraic correspondence source, not a hand-written transition graph that is later labeled `F(X)`.

Required source-generation route:

1. choose and freeze an explicit smooth cubic fourfold over an exact characteristic-zero coefficient field, preferably `Q` or a small exact algebraic extension;
2. provide a deterministic smoothness certificate for the chosen cubic;
3. construct standard Grassmannian/big-cell charts for lines in `P^5`;
4. generate local equations of `F(X)` by substituting the line parametrization into the cubic equation and setting all cubic-in-line-parameter coefficients to zero;
5. construct local incidence equations for `P subset F x X`;
6. construct declared divisor/line-bundle/cycle candidates on `F` algebraically, without importing a known Hodge answer on `X`;
7. generate the corresponding incidence surfaces/cycles on `X` by exact algebraic pushforward/elimination at the finite declared scope.

If full exact elimination is too large, freeze a smaller exact chart family with explicit scope. Do not replace algebraic generation by a synthetic automaton.

Required controls:

- at least one incidence path with nontrivial fiber provenance;
- at least one recombination case where different local/intermediate presentations produce the same final cycle/class;
- at least one multiplicity-sensitive case where Boolean support alone is insufficient, if such a case exists in the frozen source;
- at least one failed/partial candidate whose support exists but whose declared class/lifting obligation fails.

---

## 5. BRC correspondence-typing gate

The canonical R062 BRC multipath bridge is defined on a component-typed native transition skeleton. H0J may **not** simply rename arbitrary algebraic correspondences as BRC.

Before any Hodge-special credit, prove an exact correspondence typing theorem or freeze a hard block.

Required objects:

- typed source/target object labels;
- typed correspondence edges;
- composable path witnesses represented by algebraic fiber-product/intersection data;
- provenance tags sufficient to distinguish distinct intermediate algebraic paths;
- a well-defined path-formal sum;
- a well-defined composition law;
- exact forgetful maps to the declared multiplicity and support carriers.

Required theorem:

`ALGEBRAIC_CORRESPONDENCE_PATH_FORMAL_CARRIER_IS_WELL_TYPED`.

At minimum prove associativity on the declared finite source and compatibility with ordinary correspondence composition after forgetting provenance.

If this cannot be established without analogy or hand labeling, disposition:

`H0J_BRC_CORRESPONDENCE_TYPING_HARD_BLOCK`.

Hard-block fields must include:

- `missing_object`
- `owner`
- `necessity`
- `unblock_condition`.

---

## 6. Coefficient tower and signed/rational firewall

Canonical R062 freezes:

`PATH_FORMAL_BRC -> N_BRC -> BOOLEAN_BRC`.

That tower is sufficient for positive path multiplicity but **not** for arbitrary signed/rational Hodge-cycle combinations.

Therefore distinguish:

### Positive effective lane

Use canonical path-formal/N/Boolean semantics exactly.

### Signed lane

A `Z`-group completion of path-formal/N provenance may be studied only as a new candidate. It is not predeclared canonical BRC.

Must prove:

- well-defined additive inverse;
- compatibility with typed composition;
- cancellation semantics;
- comparison with ordinary free-abelian cycle/correspondence groups.

### Rational lane

A `Q` extension may be studied only after the integral lane is typed. Denominator clearing and return to rational cycle classes must be explicit.

Do not infer signed cancellation from Boolean or `N` support.

---

## 7. Fair baseline sandwich

Freeze both baselines before Enterprise success metrics.

### `B_raw^corr`

May use:

- exact algebraic equations of `X`, `F(X)` and `P`;
- direct fiber-product/intersection execution;
- explicit path enumeration;
- direct pushforward/pullback on declared cycles/classes;
- explicit multiplicity computation;
- brute-force exact finite candidate search.

Do not preinstall BRC future/provenance quotient.

### `B_std^corr`

Must additionally include every fair standard operation available to the classical correspondence source:

- ordinary algebraic correspondences and their composition;
- Chow groups / cycle groups / rational equivalence at the declared scope;
- proper pushforward and flat/Gysin pullback when typed;
- projection formula;
- intersection multiplicities and scheme-theoretic fiber products;
- standard matrix/kernel/image/cokernel/SNF/HNF normal forms;
- ordinary provenance-free composition of correspondence maps;
- the classical Beauville-Donagi incidence/Hodge transform at the benchmark scope;
- the p=1 Picard/divisor lifting route on `F(X)` already accepted as source mathematics;
- any source-native decomposition or obstruction independently derivable before Enterprise evaluation.

The final known cubic-fourfold Hodge conclusion is checker/control only, but its standard proof ingredients may not be artificially withheld if they are load-bearing source mathematics.

Anti-gaming rule:

`CLASSICAL_INCIDENCE_TRANSFORM_ATTRIBUTION != ENTERPRISE_INCREMENTAL_ATTRIBUTION`.

Hard-target PASS requires strict leverage absent from **both** baselines and absent from the already-known classical incidence route.

---

## 8. Required candidate families

### J0 — Classical incidence positive control

Type the route

`H^4(X) -> H^2(F) -> divisor/Picard -> incidence surface on X`

at the exact benchmark scope.

Record which leverage is caused by the classical incidence transform.

Expected classification may be:

`CLASSICAL_PRIOR_ART_TRANSFORM_WITH_REAL_LAYER_LOWERING`.

This receives **zero Enterprise incremental credit** unless a distinct Enterprise operation is proved load-bearing.

### J1 — Path-formal incidence provenance

Realize algebraically generated incidence paths in a path-formal carrier.

Test whether retaining intermediate line/divisor/fiber provenance gives a theorem-critical normal form unavailable in ordinary classical correspondence composition.

Required stress:

- same final cohomology class, distinct path provenance;
- same support but different multiplicity when available;
- recombination of presentation-equivalent paths.

### J2 — `Z/Q` group-completed multipath cycle carrier

If J1 is well typed, test signed and rational formal cycle combinations.

Compare directly against ordinary free abelian cycle groups and Chow correspondence algebra.

If group completion is merely the standard cycle-group construction under new notation, classify source-inherited / prior-art with no Enterprise credit.

### J3 — Multi-step lifting suffix/recoalescence interface

Build at least a three-stage lifting process, e.g.

`class descriptor -> F-side class/divisor obligations -> incidence-family obligations -> X-side cycle/class`.

Define a predeclared structural measure and test whether an Enterprise future/provenance quotient strictly reduces the reusable interface while preserving all declared downstream obligations.

The measure may count:

- live provenance classes;
- independent fiber/multiplicity obligations;
- correspondence branches retained;
- cycle-class verification tokens;
- obstruction tokens.

The exact candidate quotient/minimal interface must not be inserted into `B_std^corr` by definition, but ordinary correspondence/Chow normal forms must remain available.

### J4 — Optional class-first cubic Hodge preseed

Only if an exact, non-target-leaking Hodge-class input carrier can be frozen independently of algebraic surface representatives.

An opaque symbol “alpha is a Hodge class” is not enough for a finite exact R3 claim unless the typed comparison obligations are explicit.

Do not use a known special surface, plane, scroll, or Schubert-type cycle to define the target class.

---

## 9. Attribution certificate

Every positive R2 claim requires both:

- Criterion V2 `PROOF_LEVERAGE_CERTIFICATE`;
- H0D0 `LEVERAGE_ATTRIBUTION_CERTIFICATE`.

The attribution certificate must contain two separate counterchecks:

1. against `B_std^corr`;
2. against the classical incidence-transform route J0.

Hard-target credit requires:

`ROBUST_TRANSFORM_ATTRIBUTED_ENTERPRISE_INCREMENT`.

Not sufficient:

- classical correspondence lowers cohomological degree;
- classical Lefschetz `(1,1)` solves the F-side class;
- BRC stores more provenance;
- path counts are larger than Boolean support;
- a signed free abelian group can represent cycle differences.

The Enterprise transform must create a strict theorem-critical operational form that the fair classical source does not already own.

Allowed leverage classes include:

- `LAYER_LOWERING`
- `DEPENDENCY_REDUCTION`
- `COMPOSITIONAL_FACTORING`
- `FINITE_OBSTRUCTION_BASIS`
- `NORMAL_FORM`
- `INTEGRALITY_POSITIVITY_MONOTONICITY`

---

## 10. Hodge / target-leakage firewall

Forbidden as generators:

- Voisin's conclusion that every integral degree-four Hodge class on a cubic fourfold is algebraic;
- a known algebraic surface representing the test Hodge class;
- a known special-cubic lattice generator chosen because its surface representative is known;
- known Chow generators inserted before the Enterprise search;
- known final divisor on `F(X)` corresponding to the target class;
- known Hodge numbers used to fit the candidate transform.

Allowed as controls/checkers after candidate freeze:

- Beauville-Donagi incidence/Hodge isomorphism;
- Lefschetz `(1,1)`;
- known cubic-fourfold integral Hodge theorem;
- standard intersection theory and Chow push-pull;
- known benchmark cohomology dimensions when used only for verification.

No claim of a general Hodge proof is permitted.

`H1_ADMISSIBLE=false` throughout H0J unless a later Driver decision explicitly changes it.

---

## 11. Required deliverables

At minimum:

1. `HODGE_H0J_ALGEBRAIC_CUBIC_SOURCE_SPEC.json`
2. `HODGE_H0J_FANO_LINE_SOURCE_REGISTRY.json`
3. `HODGE_H0J_INCIDENCE_CORRESPONDENCE_REGISTRY.json`
4. `HODGE_H0J_BRC_CORRESPONDENCE_TYPING_THEOREM.json`
5. `HODGE_H0J_COEFFICIENT_TOWER_LEDGER.json`
6. `HODGE_H0J_SOURCE_BASELINE_SANDWICH.json`
7. `HODGE_H0J_CLASSICAL_INCIDENCE_CONTROL.json`
8. `HODGE_H0J_MULTIPATH_PROVENANCE_REGISTRY.json`
9. `HODGE_H0J_SIGNED_RATIONAL_CARRIER_REGISTRY.json`
10. `HODGE_H0J_MULTISTEP_LIFTING_REGISTRY.json`
11. `HODGE_H0J_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json`
12. `HODGE_H0J_ATTRIBUTION_CERTIFICATE_REGISTRY.json`
13. `HODGE_H0J_PRESENTATION_NATURALITY_LEDGER.json`
14. `HODGE_H0J_TARGET_LEAKAGE_LEDGER.json`
15. `HODGE_H0J_PRIOR_ART_NOVELTY_LEDGER.json`
16. `HODGE_H0J_R3_PRESEED.json`
17. `HODGE_H0J_CLASSIFICATION.json`
18. `HODGE_H0J_SEMANTIC_CHECKPOINT.md`
19. deterministic checker
20. manifest with SHA-256s

The checker must recompute the load-bearing finite algebraic/provenance claims, not merely schema-check JSON.

---

## 12. Dispositions

Primary dispositions:

- `H0J_ENTERPRISE_INCREMENTAL_ROBUST_R2`
- `H0J_CLASSICAL_INCIDENCE_ONLY_NO_ENTERPRISE_INCREMENT`
- `H0J_BRC_CORRESPONDENCE_SOURCE_INHERITED`
- `H0J_SIGNED_GROUP_COMPLETION_SOURCE_INHERITED`
- `H0J_BRC_CORRESPONDENCE_TYPING_HARD_BLOCK`
- `H0J_NO_STRICT_LEVERAGE`
- `H0J_ATTRIBUTION_UNRESOLVED_HARD_BLOCK`

Optional stronger disposition:

`H0J_CUBIC_FOURFOLD_CLASS_FIRST_R3_PRESEED`.

If H0J fails because ordinary correspondence/Chow mathematics already supplies the complete normal form, do **not** rerun with more lines, more charts or a larger finite bound. Return to Driver and change the Enterprise mechanism itself.

If H0J succeeds, do not automatically start H1; return to Driver for a dedicated R3 qualification stage.

---

## 13. Frozen interpretation

H0J is not a request to reprove the known cubic-fourfold Hodge theorem by renaming its classical proof.

It asks a narrower and harder question:

> after the classical incidence transform and standard correspondence/Chow machinery are fully credited to the source, does the canonical Enterprise multipath/provenance realization add any exact, load-bearing proof structure of its own?

Only a positive answer may advance the Enterprise Hodge route.