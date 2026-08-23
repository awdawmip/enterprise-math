# HODGE Stage H0M — Weil Sixfold Open-Frontier Semiregularity / Obstruction-Cancellation Gate

Date: `2026-08-23`
Status: `ACTIVE / DRIVER-ISSUED TASKBOOK`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Task ID: `RS-HODGE-H0M-WEIL-SIXFOLD-SEMIREGULARITY-OBSTRUCTION-CANCELLATION`
identity_policy: `AUTO_RESOLVE_OR_ALLOCATE`
identity_lane: `HODGE-H0M-WEIL6-OBSTRUCTION`
owner branch: `research/hodge-h0m-weil-sixfold-obstruction-cancellation`
control branch: `research/hodge-special-control-plane`

## 0. Route status

H0L is Driver-accepted as:

`H0L_SUPPORT_FIRST_EQUALS_CYCLE_GYSIN_NORMAL_FORM_R1`.

Driver review:

`driver_reviews/HODGE_H0L_CONIVEAU_SUPPORT_DOWNWARD_COLLAPSE_DRIVER_REVIEW_20260823.md`.

Freeze the H0L route decision:

`CONIVEAU_SUPPORT_FIRST_FORMULATION_IS_SOURCE_COMPLETE_AT_AUDITED_FERMAT_SCOPE__DO_NOT_SCALE_KNOWN_POSITIVE_BENCHMARKS`.

H0E–H0L collectively show that on audited known-positive Hodge benchmarks the following mechanisms repeatedly become source-inherited under a fair baseline:

- future-signature / provenance quotient;
- algebraic regularity / filtered recognition normal forms;
- Picard/divisor lifting;
- vector-bundle/Chern/zero-locus lifting;
- classical correspondence + BRC multipath;
- character/DFT/Galois interaction;
- coniveau/local-cohomology/Gysin support lowering.

H0M therefore changes both **benchmark status** and **operational mechanism**.

The benchmark must lie on a genuine unresolved algebraicity frontier rather than a theorem-positive control family.

---

## 1. Current literature routing gate — verify before mathematics

The literature status is fast-moving and must be re-audited at task start from primary sources.

Driver routing references as of `2026-08-23`:

1. E. Markman, `Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds`, arXiv:2502.03415.
   Routing fact to verify: Weil classes are algebraic for polarized abelian sixfolds of Weil type in the discriminant `-1` / split locus treated there; the fourfold case follows much more generally.
2. A. Mostaed, `McMullen's Curve, the Weil Locus, and the Hodge Conjecture for Abelian Sixfolds`, arXiv:2603.20268.
   Routing fact to verify: outside the known discriminant-`-1` sixfold locus, Weil-class algebraicity remains outside existing general theorems at the paper's stated scope.

Do not trust this routing freeze blindly. Produce:

`HODGE_H0M_LITERATURE_FRONTIER_LEDGER.json`.

It must classify the chosen target family as one of:

- `CURRENTLY_OPEN_FRONTIER_AT_DECLARED_SCOPE`;
- `NOW_CLASSICALLY_SOLVED__RESELECT_MODEL`;
- `LITERATURE_STATUS_UNRESOLVED`.

If the selected family has become classically solved before execution, reselect **before any Enterprise success evaluation**.

---

## 2. Primary benchmark class

Work with a polarized complex abelian sixfold `A` of Weil type for an imaginary quadratic field `K`.

Typed source data:

- `dim_C A = 6`;
- `V = H^1(A,Q)` has dimension `12` over `Q` and dimension `6` over `K`;
- `K -> End^0(A)` acts on `H^{1,0}(A)` with the two complex embeddings of `K` each occurring with multiplicity `3`;
- a polarization determines the usual `K`-Hermitian form on the rational homology/Hodge structure;
- freeze a discriminant class `delta` outside the currently solved sixfold discriminant-`-1` locus, after the literature gate confirms the scope.

The distinguished Weil-Hodge space is

`W_K(A) = wedge_K^6 H^1(A,Q)`

viewed as a two-dimensional `Q`-subspace of `H^6(A,Q)`.

Hard typing requirements:

- prove `dim_Q W_K(A)=2`;
- prove every vector in `W_K(A)` is of Hodge type `(3,3)` under the Weil-type multiplicity condition;
- distinguish `W_K(A)` from the divisor-generated Hodge algebra;
- freeze the carrier **before any codimension-3 cycle search**.

### Hard prerequisite A

`OPEN_WEIL_SIXFOLD_EXACT_RATIONAL_HODGE_CARRIER_AND_FRONTIER_MODEL_ESTABLISHED`.

No later candidate may be evaluated before prerequisite A passes.

---

## 3. Model-selection requirement

A purely abstract two-dimensional Hodge structure is not enough. H0M must instantiate an actual polarized abelian sixfold/family at the declared frontier scope.

Acceptable model styles include:

1. an exact unitary-Shimura-family model with a fixed imaginary quadratic field, lattice, Hermitian form/discriminant and generic period-domain point specified before cycle search;
2. an explicit polarized complex torus satisfying the Riemann relations and Weil-type `K` action, together with a proof that it lies outside the currently solved sixfold locus;
3. another exact algebraic/moduli presentation accepted by the same typing strength.

Required artifact:

`HODGE_H0M_WEIL_SIXFOLD_MODEL_SPEC.json`.

It must record:

- `K`;
- lattice/rational Hodge data;
- polarization/Hermitian form;
- discriminant class;
- Weil-type signature `(3,3)`;
- exact rational Hodge carrier;
- why the model is outside known solved sixfold loci at the literature-freeze date.

If no exact frontier model can be instantiated without falling into a solved/special family, return a precise `HARD_BLOCK` rather than replacing the target with a known-positive model.

---

## 4. Solved-locus positive control

Use the discriminant-`-1`/split sixfold result only as a **positive mechanism control**.

The control may include, at source-appropriate strength:

- the `X x Pic^0(X)` geometry arising from an abelian threefold `X`;
- Fourier-Mukai / Orlov equivalence;
- secant sheaves/complexes;
- semiregularity;
- deformation of algebraic characteristic classes;
- the resulting algebraicity theorem for the known sixfold locus.

Freeze:

`KNOWN_DISCRIMINANT_MINUS_ONE_CYCLE_OR_SHEAF != FRONTIER_TARGET_GENERATOR`.

Do not import a known secant sheaf, Chern character, cycle class or deformation family into the frontier target by renaming it Enterprise.

The known case is used to learn which obligations a successful mechanism must satisfy and which data genuinely depend on the discriminant/split structure.

---

## 5. Mechanism change: obstruction cancellation, not quotient compression

H0M must not use future-signature minimization, BRC provenance quotient, Fermat DFT, or coniveau/Gysin rank as the primary Enterprise mechanism.

The intended new mechanism class is **derived obstruction formation and cancellation**.

For a candidate algebraic/derived object `E` on `A`, the relevant process may involve:

- deformation/extension data;
- `Ext^1(E,E)` tangent directions;
- `Ext^2(E,E)` obstruction carriers;
- semiregularity/trace maps into Hodge cohomology;
- finite source-labelled obstruction interactions;
- cancellation/annihilation of obstruction channels;
- survival of a characteristic class in `W_K(A)` under deformation/transport.

The Enterprise operational candidate must be built from exact source data and must be compared against ordinary derived deformation and semiregularity theory.

Do not call an obstruction map Enterprise merely because it is written as a finite process.

---

## 6. Candidate M1 — discriminant-defect carrier

Determine exactly which part of the known split/discriminant-`-1` construction fails when the frontier discriminant is substituted.

Construct a typed defect ledger separating at least:

- existence of the required auxiliary abelian threefold / secant geometry;
- existence of a Fourier-Mukai source object with the required characteristic class;
- semiregularity of the object;
- deformation family dimension;
- Mumford-Tate invariance of the target characteristic class;
- polarization/discriminant compatibility.

Required artifact:

`HODGE_H0M_DISCRIMINANT_DEFECT_REGISTRY.json`.

A vague statement such as `known construction does not apply` is insufficient. Isolate exact missing objects/maps.

For every missing object use:

- `missing_object`;
- `owner`;
- `necessity`;
- `unblock_condition`.

---

## 7. Candidate M2 — semiregularity obstruction-cancellation process

If a frontier candidate object/family is available, construct the exact obstruction process.

At minimum distinguish:

`DEFORMATION_STATE`
`-> EXT2_OBSTRUCTION`
`-> SEMIREGULARITY_OR_TRACE_CHANNELS`
`-> CANCELLED / SURVIVING OBSTRUCTION`
`-> CLASS_TRANSPORT_STATUS`.

Research whether the process admits an independently generated finite operational normal form with any of:

- local obstruction factorization;
- signed cancellation;
- dependency reduction;
- finite obstruction basis;
- compositional gluing of local deformation steps;
- monotone/integral obstruction certificate.

A positive result must not be a restatement of the standard semiregularity theorem or ordinary obstruction spectral sequence.

Required artifact:

`HODGE_H0M_OBSTRUCTION_CANCELLATION_REGISTRY.json`.

---

## 8. Candidate M3 — derived/Hecke/isogeny transport gate

Test whether a cycle/sheaf-producing source object can be transported from a known solved sixfold to the frontier model by a chain of exact algebraic operations such as:

- isogeny;
- Fourier-Mukai equivalence;
- duality;
- Hecke correspondence;
- deformation inside an allowed moduli component;
- another explicitly typed algebraic correspondence.

The transport must preserve/identify the target Weil-Hodge carrier at the stated scope.

Do not assume the discriminant can be changed by these operations. Prove the transformation law of the discriminant and use it as a hard gate.

Possible accepted result:

`DISCRIMINANT_TRANSPORT_NO_GO`.

If every legal source operation preserves the obstruction/discriminant class preventing passage to the frontier target, freeze the exact no-go rather than inserting an untyped jump.

Required artifact:

`HODGE_H0M_DERIVED_TRANSPORT_REGISTRY.json`.

---

## 9. Candidate M4 — class-first codimension-3 algebraic lift

The target is the already frozen arbitrary input

`w in W_K(A)`.

A genuine lift requires an algebraic codimension-3 cycle `Z(w)` on the **frontier model** with

`cl_Q(Z(w)) = w`.

It is enough to construct a source-generated algebraic family whose cycle classes span the two-dimensional `W_K(A)` and then solve arbitrary rational input exactly, provided the family itself was not selected from a known target cycle theorem.

Potential algebraic outputs may arise from:

- Chern characters/classes of newly constructed sheaves/complexes;
- degeneracy loci;
- correspondences;
- algebraic families produced by the obstruction-cancellation mechanism.

But standard divisor products do not count if `W_K(A)` is the exceptional Weil subspace outside the divisor algebra.

Required artifact:

`HODGE_H0M_CLASS_FIRST_WEIL_LIFT_REGISTRY.json`.

If no candidate cycle is constructed, say so. Do not infer algebraicity from absolute-Hodge or Mumford-Tate status alone.

---

## 10. Fair source baselines

Freeze before Enterprise success evaluation.

### `B_raw^Weil6`

Allow:

- exact `K`-linear Hodge structure;
- explicit Hermitian/polarization data;
- direct exterior-algebra construction of `W_K(A)`;
- direct candidate sheaf/cycle calculations;
- explicit Ext/obstruction calculations;
- brute-force finite presentation where declared.

### `B_std^Weil6`

Additionally allow all standard source mathematics reasonably available at the declared scope:

- Mumford-Tate / unitary representation theory;
- Weil-class construction;
- Fourier-Mukai and Orlov equivalences;
- derived categories of abelian varieties;
- Ext/deformation/obstruction theory;
- Buchweitz-Flenner-type semiregularity and trace maps where applicable;
- Gauss-Manin transport and variation of Hodge structure;
- algebraic-cycle/Chern-character arithmetic;
- isogeny/Hecke/correspondence transport;
- exact linear algebra, SNF/HNF, exterior algebra;
- all known solved-locus sixfold/fourfold theorems as controls, not as frontier generators.

Freeze:

`STANDARD_SEMIREGULARITY_OR_DERIVED_DEFORMATION_NORMAL_FORM_COUNTS_AGAINST_ENTERPRISE_ATTRIBUTION`.

A candidate earns Enterprise credit only if the proof-critical operation is absent from both baselines and its leverage is caused by the Enterprise transform/process.

---

## 11. Attribution / rank gate

Use H0A0 + H0D0 unchanged.

For each M1–M4 candidate record:

- typed source baseline;
- Enterprise map/process;
- information tag;
- exact correctness theorem;
- strict leverage vs `B_raw^Weil6`;
- strict leverage vs `B_std^Weil6`;
- attribution classification;
- novelty/prior-art classification;
- target-leakage audit;
- presentation/naturality scope.

Primary hard target B:

`OPEN_WEIL_SIXFOLD_ENTERPRISE_ALGEBRAICITY_MECHANISM_CLASSIFIED_WITHOUT_TARGET_LEAKAGE`.

This target passes as a classification if H0M produces one of the following exact outcomes:

1. `FRONTIER_CLASS_FIRST_CYCLE_WITH_ROBUST_TRANSFORM_ATTRIBUTED_R2`;
2. `FRONTIER_CYCLE_FOUND_BUT_SOURCE_INHERITED`;
3. `DISCRIMINANT_OR_SEMIREGULARITY_NO_GO_CLASSIFIED`;
4. `EXACT_HARD_BLOCK_WITH_MISSING_OBJECT_AND_UNBLOCK_CONDITION`.

Preferred stronger target C:

`WEIL_SIXFOLD_FRONTIER_ENTERPRISE_R3_PRESEED`.

This requires all HBR1–HBR6 analogues plus exact arbitrary class-first equality on the frontier model and robust Enterprise attribution.

Even target C does **not** automatically open H1.

---

## 12. Target-leakage firewall

Forbidden as frontier generators:

- a known algebraic representative of a Weil class from the solved discriminant-`-1` locus;
- Markman/Schoen cycle coefficients copied into the target model;
- assuming the Hodge conjecture for the selected frontier sixfold;
- choosing the model only because a known cycle is already available;
- treating absolute Hodge as algebraic;
- using a literature theorem whose hypotheses secretly place the model in a solved locus;
- changing the discriminant/model after seeing which candidate mechanism succeeds.

The frontier model, discriminant and Hodge carrier must freeze before cycle search.

---

## 13. Mandatory controls

At minimum include:

### C1 — solved discriminant-`-1` positive control

Reproduce only enough source structure to verify the task understands why the known mechanism works there. Receive **zero Enterprise credit** for the known theorem itself.

### C2 — divisor-algebra negative control

Verify that the exceptional Weil subspace is not silently replaced by ordinary divisor products at the selected generic/frontier scope.

### C3 — discriminant transport control

Attempt at least one natural isogeny/derived/Hecke transport and prove its discriminant transformation law.

### C4 — semiregularity null control

Construct a case where an obstruction survives or the needed semiregularity map is unavailable, so the process cannot declare automatic cancellation.

### C5 — rational scaling

Any successful lift must handle negative and denominator-bearing inputs in `W_K(A)`.

---

## 14. Deterministic evidence

Commit a deterministic checker where the source admits finite exact replay.

At minimum the checker/ledger must validate:

- `dim_Q W_K(A)=2`;
- `(3,3)` Hodge typing;
- model/discriminant freeze;
- solved-locus exclusion at the declared algebraic/model level;
- no target-cycle constants in generators;
- exact discriminant transport formulas used by M3;
- any finite Ext/obstruction matrices or cancellation tables claimed;
- exact cycle-class equality if M4 succeeds;
- attribution consistency.

Do not turn an open algebraicity statement into a checker assertion. The checker verifies the declared finite algebra/source computations, not the unknown theorem.

---

## 15. Required return artifacts

Return at minimum:

1. `research_results/HODGE_H0M_LITERATURE_FRONTIER_LEDGER.json`
2. `research_results/HODGE_H0M_WEIL_SIXFOLD_MODEL_SPEC.json`
3. `research_results/HODGE_H0M_RATIONAL_WEIL_HODGE_CARRIER.json`
4. `research_results/HODGE_H0M_DISCRIMINANT_DEFECT_REGISTRY.json`
5. `research_results/HODGE_H0M_OBSTRUCTION_CANCELLATION_REGISTRY.json`
6. `research_results/HODGE_H0M_DERIVED_TRANSPORT_REGISTRY.json`
7. `research_results/HODGE_H0M_CLASS_FIRST_WEIL_LIFT_REGISTRY.json`
8. `research_results/HODGE_H0M_SOURCE_BASELINE_SANDWICH.json`
9. `research_results/HODGE_H0M_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json`
10. `research_results/HODGE_H0M_ATTRIBUTION_CERTIFICATE_REGISTRY.json`
11. `research_results/HODGE_H0M_TARGET_LEAKAGE_LEDGER.json`
12. `research_results/HODGE_H0M_PRESENTATION_NATURALITY_LEDGER.json`
13. `research_results/HODGE_H0M_R3_PRESEED.json`
14. `research_results/HODGE_H0M_CLASSIFICATION.json`
15. `research_results/HODGE_H0M_SEMANTIC_CHECKPOINT.md`
16. deterministic checker + output
17. manifest/digests.

If a branch is not applicable because an earlier exact hard block is reached, still return a typed registry explaining the block rather than omitting the artifact silently.

---

## 16. Stop conditions

Stop and freeze immediately on any exact decisive outcome:

- frontier model now classically solved -> `RESELECT_MODEL_BEFORE_RESEARCH`;
- exact frontier model cannot be instantiated -> `HARD_BLOCK`;
- known mechanism cannot cross discriminant and no candidate object exists -> freeze the defect/no-go;
- candidate cycle succeeds but all leverage is source-inherited -> freeze valid negative;
- robust attributed class-first cycle succeeds -> freeze R2/R3 candidate and stop; do not open H1.

Do not scale model dimension, add arbitrary derived machinery, or weaken the fair baseline after failure.

---

## 17. H1 gate

`H1_ADMISSIBLE = false` at task start.

No H1 task may be opened automatically, even if H0M produces a frontier cycle. The Driver must separately audit frontier status, class equality, attribution, and HBR1–HBR6 before any bridge-stage promotion.