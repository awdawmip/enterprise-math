# HODGE Stage H0 — Enterprise Realization Nontriviality Gate

Date: `2026-08-17`
Status: `ACTIVE / DRIVER-ISSUED TASKBOOK`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Task ID: `RS-HODGE-H0-ENTERPRISE-REALIZATION-NONTRIVIALITY`
identity_policy: `AUTO_RESOLVE_OR_ALLOCATE`
identity_lane: `HODGE-H0-REALIZATION`
owner branch: `research/hodge-h0-enterprise-realization-nontriviality`
control branch: `research/hodge-special-control-plane`

## 0. Mission

This is the first qualification stage of the Enterprise Math Hodge program.

Do **not** attempt to prove the Hodge conjecture in this stage.

The single load-bearing question is:

> **Does Enterprise Math provide a genuinely different geometric realization of an algebraic object, or only a reparameterization / redundant encoding of the classical realization?**

The stage must end with an auditable answer to:

`ENTERPRISE_REALIZATION_IS_NOT_MERE_COORDINATE_REPARAMETRIZATION`

Only if the strongest admissible result reaches the H0 PASS gate may the Driver issue H1 for Enterprise chains/cochains/cohomology.

A negative result is a valid and important outcome.

---

## 1. Frozen authority and startup packet

Read and obey, in authority order:

1. `AGENTS.md`
2. `docs/GITHUB_INTERACTION_BUDGET.md`
3. `research_common_surface.json`
4. `driver_handoffs/HODGE_SPECIAL_DRIVER_HANDOFF_20260817.md`
5. `driver_handoffs/HODGE_SPECIAL_DRIVER_PI_GEOMETRY_ADDENDUM_20260817.md`
6. `PROJECT_DEFINITION.zh-CN.md`
7. `PROJECT_DEFINITION.md`
8. `project_definition.json`
9. `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`
10. `definitions/ENTERPRISE_SQUARE_AND_ROOT_20260816.md`
11. `definitions/R059D_STAGE_AC_COUNT_RETYPE_20260816.md`
12. `FOUNDATIONAL_LOGIC.md`
13. `foundational_logic.json`
14. `native_semantics_admissibility.json`

The 2026-08-17 π-geometry addendum overrides weaker π wording in the older Hodge handoff.

The following project position is frozen for this task:

`CLASSICAL_EQUIDISTANT_CIRCLE_AS_NATIVE_GEOMETRY = REJECTED_BY_ENTERPRISE_MATH`

`CLASSICAL_PI_GEOMETRIC_APPLICABILITY_TO_ENTERPRISE_CIRCLE = NOT_ACCEPTED`

Classical mathematics may be used as external benchmark/control, not as native generator.

---

## 2. R059D Stage AD input policy

R059D Stage AD has now frozen independently.

Allowed read-only frozen input:

- owner branch: `research/r059d-stage-ad-triangular-coverage-circle-bridge`
- frozen owner head: `d5270439d41ab2a421195d7387d6c819eba4bf56`
- disposition: `COVERAGE_BRIDGE_ESTABLISHED__RESOLVE_RULE_UNDERDETERMINED`
- final checker: `2643/2643 PASS`
- final checker digest: `2627ce754fed59485f97c6c861f707f0d1e29b852d514b42272829fc81f7cde7`
- checkpoint SHA-256: `54e2fca7e2941b184991f057b6ebab50d74bbeee8dbc2e067949735e90a93ac5`

Consume AD only if needed to understand the existing BRC / Enterprise-circle realization boundary.

Do **not**:

- modify the AD branch;
- rewrite AD definitions;
- import AD finite circle results as Hodge evidence;
- infer a general algebraic-variety realization theorem from the AD plane carrier;
- import classical circle / Euclidean metric / classical π through AD.

Unrelated R059 lanes are out of scope unless the Driver explicitly adds them later.

---

## 3. External classical target — freeze exactly

At execution time, verify the current authoritative status from Clay Mathematics Institute or another equally authoritative primary source.

The classical Hodge target must remain:

For a smooth projective complex algebraic variety `X`, every rational Hodge class

`H^{2p}(X,Q) ∩ H^{p,p}(X)`

should be a rational linear combination of cohomology classes of codimension-`p` algebraic cycles.

Freeze the following distinctions:

- `CLASSICAL_THEOREM`
- `CLASSICAL_OPEN_CONJECTURE`
- `CLASSICAL_PRIOR_ART_METHOD`
- `ENTERPRISE_ANALOGY`
- `ENTERPRISE_HYPOTHESIS`
- `ENTERPRISE_PROVED_STATEMENT`
- `FINITE_COMPUTATION_ONLY`

Do not call any weaker statement “Hodge”. In particular, none of the following alone is Hodge:

- a closed combinatorial chain;
- a graph/lattice cycle;
- Betti-number recovery;
- a finite-cell `(p,p)` label;
- a fitted cycle;
- a tropical/combinatorial Hodge analogue;
- an Enterprise cycle without a rigorous algebraic lifting theorem.

The eventual missing arrow remains:

`Hodge class -> Enterprise cycle -> algebraic cycle on X`.

H0 addresses only whether the middle realization can contain genuinely non-reparameterized structure worth building on.

---

## 4. H0 type system

Create a Hodge-specific type layer without replacing the repository-wide N0/N1/N2/N3 discipline.

At minimum distinguish:

### HX0 — ALGEBRAIC_SOURCE

The algebraic object itself: smooth projective complex variety, algebraic morphisms, algebraic presentation data when explicitly declared, coordinate rings / homogeneous ideals / gluing data as appropriate.

### HX1 — ENTERPRISE_NATIVE_REALIZATION

Structures constructed from permitted Enterprise primitives and declared algebraic source data without importing classical metric, classical analytic Hodge decomposition, harmonic forms, classical circle, or target Hodge answers.

### HX2 — ENTERPRISE_DERIVED_OPERATIONAL

Declared transition, collapse, precision, branch/fiber, chain-building, counting, incidence, or other operational semantics derived from HX1.

### HX3 — COMPARISON_READOUT

Forgetful/collapse/comparison maps from Enterprise objects to classical or algebraic readouts. These are audit bridges, not generators of Enterprise structure.

### HX4 — CLASSICAL_ANALYTIC_REALIZATION

Classical complex manifold, differential-form, Hodge-decomposition, metric/harmonic realization, classical Euclidean geometry, and other classical analytic structures.

Every theorem-critical object and map must carry both:

- its Hodge-specific `HX*` type;
- its repository-wide native-semantics type (`N0/N1/N2/N3` or the strongest admissible equivalent).

A type mismatch must weaken/retype a claim rather than being hidden.

---

## 5. Main no-go / nontriviality classification

For each candidate Enterprise realization `E(X)`, define an explicit comparison/forgetful map when meaningful:

`U_X : E(X) -> C(X)`

where `C(X)` is a declared classical realization used only for comparison/audit.

Classify the candidate into exactly one strongest justified class:

### R0 — MERE_REPARAMETRIZATION

`E(X)` is isomorphic/equivalent to the classical realization in the theorem-relevant category, and all Enterprise structure is just transported classical structure.

Disposition:

`NO_NEW_HODGE_CONTENT`.

### R1 — REDUNDANT_ENRICHMENT

`U_X` may have nontrivial fibers or extra labels, but every theorem-critical Enterprise observable/operation/chain datum factors through `U_X`.

Extra state exists but is inert for the proposed Hodge mechanism.

Disposition:

`NO_NEW_HODGE_CONTENT_YET`.

### R2 — NONTRIVIAL_REALIZATION_CANDIDATE

There exist Enterprise states `e1 != e2` with the same classical image under the declared `U_X`, together with at least one theorem-relevant Enterprise-native operation/observable/constraint that distinguishes them and **does not factor through `U_X`**, while also passing the required choice/presentation/functoriality gates below.

This is the minimum H0 PASS class.

### R3 — HODGE_RELEVANT_REALIZATION_CANDIDATE

R2 plus evidence that the non-factorizing Enterprise structure enters a natural chain/cochain/cycle constraint and exposes a plausible comparison/descent interface toward algebraic cycles.

H0 may identify an R3 candidate but must not claim an algebraic lifting theorem.

---

## 6. Exact non-factorization certificate

A mere statement that “Enterprise has more information” is insufficient.

For every claimed R2/R3 candidate, produce an exact certificate of the form:

1. declare `e1 != e2`;
2. prove/check `U_X(e1) = U_X(e2)`;
3. declare an admissible Enterprise observable/operation `A_E`;
4. prove/check `A_E(e1) != A_E(e2)` or another exact theorem-relevant distinction;
5. conclude that `A_E` cannot factor through `U_X` on the declared carrier;
6. prove that the distinction is not caused only by an arbitrary color/tag/index/coordinate-chart choice;
7. state precisely what later chain/cochain construction could consume from this distinction.

Finite exact carriers may establish the certificate only for the declared toy carrier. Do not promote a finite witness to a theorem for all varieties without proof.

---

## 7. Choice and presentation independence gate

A non-factorizing distinction caused only by arbitrary representation choices does not pass H0.

For every R2/R3 candidate, test at minimum:

### 7.1 Algebraic presentation independence

Use at least two algebraically equivalent presentations of the same toy variety.

The Enterprise construction must either:

- be invariant under the relevant algebraic isomorphism; or
- come with a canonical/natural equivalence relating the resulting Enterprise objects.

If neither is established, classify:

`PRESENTATION_DEPENDENT_AUXILIARY_STRUCTURE`.

### 7.2 Relabeling / automorphism independence

The theorem-relevant distinction must survive declared Enterprise relabelings and source automorphisms.

### 7.3 No hidden center / metric choice

Do not silently select:

- Euclidean center;
- shortest path;
- distance sphere;
- norm;
- angle;
- radius;
- classical circle;
- classical π;
- harmonic metric;
- preferred classical coordinate chart.

If such a choice is required, type it as HX4/N3 calibration and do not call the resulting structure native.

### 7.4 Precision choice typing

If precision/collapse/fiber is used, state whether precision is:

- algebraically generated;
- externally chosen operational data;
- a readout parameter.

External choice does not automatically invalidate the model, but it blocks promotion to native/canonical status without a choice-independence theorem.

---

## 8. Functoriality gate

The Hodge route cannot rest on isolated pictures.

For an admissible candidate `E`, attempt to define behavior on algebraic morphisms:

`f : X -> Y`

and a corresponding Enterprise map/relation:

`E(f) : E(X) -> E(Y)`

or the strongest correctly typed relational analogue.

At minimum test:

- identity compatibility;
- composition compatibility;
- one nontrivial algebraic morphism;
- one automorphism;
- product compatibility on a toy product if the candidate claims product structure.

If exact functoriality is not available, freeze the strongest weaker statement and classify the defect.

Do not use the word `functorial` for empirical agreement on a finite sample alone.

---

## 9. Required candidate families and controls

Study at least three structurally distinct families. They do not all need to succeed.

### Candidate A — Enterprise precision/fiber/collapse route

Attempt to construct a realization from algebraic source data plus explicitly declared Enterprise precision/collapse semantics.

Core question:

> Can nontrivial fibers carry admissible information not recoverable from the classical realization and not reducible to arbitrary labels?

### Candidate B — Enterprise incidence/transition/path route

Attempt an algebraically sourced relational realization where incidence/transition/path/branch-recoalescence structure is primary and metric geometry is withheld.

BRC/path-count machinery may be used only with correct semantic typing. Do not infer Hodge relevance merely from multiplicity or recoalescence.

### Control C — Prior-art nontrivial realization comparator

Use at least one established comparator such as tropicalization, valuation/non-Archimedean realization, or another mathematically established nontrivial realization mechanism.

Purpose:

- understand what “not merely a coordinate change” looks like;
- identify which properties are prior art;
- prevent Enterprise vocabulary from relabeling an already-known construction.

Do not count the control as an Enterprise result.

### Negative controls

Include at least:

- a pure coordinate reparameterization;
- an arbitrary fiber coloring/tagging construction;
- a refinement/subdivision whose theorem-critical data all factor through the original object.

The classifier must correctly reject these.

---

## 10. Tiny exact algebraic test registry

Use only small objects in H0. Their classical Hodge answers are not generator inputs.

Minimum registry:

1. a point;
2. `P^1`;
3. `P^1 x P^1` or an equally simple smooth projective product;
4. one nontrivial algebraic morphism `P^1 -> P^1`;
5. at least one nontrivial automorphism or factor-swap map;
6. at least two algebraically equivalent presentations of the same object.

The purpose is not Hodge-number recovery. The purpose is to test:

- construction source;
- presentation independence;
- non-factorization;
- automorphism compatibility;
- functoriality;
- product compatibility;
- whether H1 chains can be generated from Enterprise data alone.

Elliptic curves, `P^2`, general toric examples, and known Hodge-number recovery belong to later stages unless needed only as a sharply justified stress test.

---

## 11. Literature / prior-art map

Build a compact but serious matrix covering at minimum:

- Hodge decomposition;
- cycle class map;
- Lefschetz `(1,1)` theorem;
- Hard Lefschetz;
- Hodge–Riemann bilinear relations;
- mixed Hodge structures;
- algebraic cycles / Chow groups;
- motives as relevant context;
- tropical Hodge theory;
- combinatorial Hodge theory;
- non-Archimedean / tropicalization realization mechanisms.

For each item record:

- exact theorem/object;
- assumptions;
- conclusion;
- current status;
- whether it is classical theorem, open problem, prior-art mechanism, or analogy;
- what H0 may use as benchmark;
- what H0 may **not** inherit as an Enterprise premise.

Use primary/authoritative sources for load-bearing claims where practical.

Target leakage is not allowed under the label “literature review”.

---

## 12. Foundation and target-leakage firewall

Apply `FOUNDATIONAL_LOGIC.md` strictly:

> Definition is not inherited. Success is evidence. Explain the success from a smaller native logic.

The following are forbidden as Enterprise generators in H0:

- classical Hodge decomposition;
- harmonic representatives;
- classical metric or Kähler metric as undeclared native data;
- classical Hodge numbers;
- classical cycle answers;
- classical Euclidean distance/angle/length;
- classical equidistant-point circle;
- standard real `π` as a selection/calibration target;
- a classical analytic chart converted into a new coordinate label and renamed Enterprise;
- a tropical/non-Archimedean output renamed Enterprise without a new construction theorem.

The following may be used only as checkers/controls with explicit HX4/N3 typing:

- classical topology;
- known Betti/Hodge numbers;
- classical theorems;
- established realization mechanisms;
- engineering/analytic success.

Every final candidate must include a target-leakage audit.

---

## 13. H1-readiness interface

Do **not** build full Enterprise cohomology in H0.

For every R2/R3 candidate, define an H1 entry contract specifying exactly what native data would generate:

- `C_k^E(X)` candidate chain carriers;
- boundary candidate `∂_E`;
- cochain candidate;
- coboundary candidate `d_E`;
- orientation/incidence data if needed;
- expected proof obligation `∂_E^2 = 0` / `d_E^2 = 0`;
- comparison map target;
- which parts depend on choices/precision.

The H1 contract must be generated from Enterprise-side data, not copied from the classical singular/cellular complex and relabeled.

If no such contract can be stated without target leakage, H0 cannot PASS.

---

## 14. Required artifacts

Freeze at least the following:

1. `research_results/HODGE_H0_CLASSICAL_TARGET_TYPE_PROTOCOL.json`
2. `research_results/HODGE_H0_LITERATURE_PRIOR_ART_MATRIX.md`
3. `research_results/HODGE_H0_REALIZATION_CANDIDATE_REGISTRY.json`
4. `research_results/HODGE_H0_REALIZATION_NONTRIVIALITY_CLASSIFICATION.json`
5. `research_results/HODGE_H0_NONFACTORIZATION_WITNESS_REGISTRY.json`
6. `research_results/HODGE_H0_PRESENTATION_AUTOMORPHISM_GATE.json`
7. `research_results/HODGE_H0_FUNCTORIALITY_TOY_REGISTRY.json`
8. `research_results/HODGE_H0_TARGET_LEAKAGE_LEDGER.json`
9. `research_results/HODGE_H0_H1_ENTRY_CONTRACT.json`
10. `research_results/HODGE_H0_CLAIM_LEDGER.json`
11. `research_results/HODGE_H0_COMPUTATION_REGISTRY.json`
12. `tools/check_hodge_h0_realization_gate.py`
13. deterministic checker output
14. manifest + semantic checkpoint document

If an artifact is not applicable because every candidate fails earlier, create the artifact with an explicit `NOT_REACHED` / `FAILED_GATE` disposition rather than silently omitting it.

---

## 15. Deterministic checker requirements

The checker must reject at minimum:

- missing type assignments;
- Hodge conjecture misstated with integral coefficients as the general target;
- any claim that a finite sample proves general Hodge;
- any R2/R3 candidate lacking a non-factorization witness;
- same-classical-image witness missing;
- arbitrary tag/color used as the only distinction;
- missing presentation-independence result;
- missing automorphism/relabeling audit;
- untyped classical metric/angle/distance/radius/circle/π usage in a native claim;
- classical Hodge answer used as generator;
- `functorial` claimed without identity/composition evidence at the declared level;
- H1 entry contract copied from classical chain complex without an Enterprise generator;
- `ALGEBRAIC_CYCLE` claimed from a combinatorial cycle without a lifting theorem;
- any claim that Hodge has been solved.

Checker success validates protocol completeness and declared finite/exact cases only. It is not itself a proof of Hodge or of a universal realization theorem.

---

## 16. H0 PASS / FAIL gate

### PASS requires all of the following

1. exact classical target/type discipline frozen;
2. prior-art map complete enough to distinguish theorem/open/analogy/Enterprise hypothesis;
3. at least one **Enterprise-specific** candidate reaches `R2_NONTRIVIAL_REALIZATION_CANDIDATE` or stronger;
4. exact same-classical-image non-factorization certificate for the declared toy carrier;
5. presentation-independence or natural-equivalence gate passed on at least two equivalent presentations;
6. relabeling/automorphism gate passed;
7. identity + composition compatibility established at the strongest claimed functoriality level;
8. at least one nontrivial morphism tested exactly;
9. target-leakage audit PASS;
10. an H1 chain/cochain entry contract can be generated from Enterprise-side data alone;
11. all universal statements are separated from finite computation;
12. deterministic checker PASS.

Recommended additional strength before Driver approval:

- the same candidate passes on at least two non-isomorphic toy varieties;
- product compatibility is nontrivial and exact;
- the non-factorizing information is shown to affect a prospective chain/cycle constraint rather than being merely observable trivia.

### FAIL / PARTIAL dispositions

Use the strongest honest disposition:

- `H0_PASS_NONTRIVIAL_ENTERPRISE_REALIZATION`
- `H0_PARTIAL_R1_ONLY_REDUNDANT_ENRICHMENT`
- `H0_FAIL_MERE_REPARAMETRIZATION`
- `H0_FAIL_PRESENTATION_DEPENDENCE`
- `H0_FAIL_TARGET_LEAKAGE`
- `H0_INSUFFICIENT_FUNCTORIALITY`
- `H0_INSUFFICIENT_H1_ENTRY_INTERFACE`
- `H0_INSUFFICIENT`

If no Enterprise candidate reaches R2, freeze the negative result and **do not start H1 automatically**.

---

## 17. Scientific red lines

Never:

- redefine Hodge into an easier discrete conjecture;
- claim breakthrough from terminology similarity;
- call a grid cycle an algebraic cycle;
- call a non-injective map “new geometry” without a non-factorization theorem;
- call arbitrary extra labels “hidden geometry”;
- assume the 3-axis Enterprise plane already realizes arbitrary complex dimension;
- assume BRC already extends from the plane to algebraic varieties;
- use known Hodge numbers to tune the Enterprise construction;
- hide failed candidates;
- erase negative controls;
- infer nature must use classical π;
- infer the Enterprise circle constant is transcendental from standard real-π transcendence;
- claim standard real π is algebraic without locating a specific failure in the classical theorem chain.

Classical internal validity and Enterprise geometric applicability remain separate questions.

---

## 18. Execution / repository discipline

Research phase is `REMOTE_SILENT` between semantic checkpoints.

Do not poll CI.

At the final H0 semantic checkpoint:

- batch artifacts;
- commit on the owner branch;
- keep working tree clean;
- publish once;
- create/update at most one Draft PR if useful;
- do not query workflow status merely because the checkpoint was published;
- preserve all negative results and exact source SHAs.

A soft blocker on one candidate does not stop independent candidates.

Only the repository-defined four-field mathematical/research `HARD_BLOCK` may stop the stage.

---

## 19. Stage objective and expected advancement

Before H0 execution:

- Hodge-special conceptual route: approximately `10%`;
- Enterprise cohomology: `0%`;
- native Hodge-type structure: `0%`;
- algebraic lifting theorem: `0%`;
- unknown-Hodge readiness: `0%`.

A genuine H0 PASS should advance approximately:

`realization-test +35 / literature-type-discipline +30 / enterprise-cohomology-entry +15 / native-hodge +0 / algebraic-lifting +0 / unknown-hodge +0`.

Do not inflate completion percentages for document production alone.

---

## 20. Final handoff packet

Return to Driver with:

1. Researcher-ID;
2. exact owner head;
3. H0 disposition;
4. strongest R-class reached by each candidate;
5. exact non-factorization witness summary;
6. presentation/functoriality status;
7. target-leakage status;
8. checker result + digest;
9. manifest/checkpoint SHA-256;
10. whether H1 is admissible;
11. one recommended next task only.

Do not start H1, H2, Lefschetz `(1,1)`, or unknown Hodge work without a new Driver route.

---

Handoff target:

`EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`

Stage slogan:

> **先证明我们真的有另一种 realization，再谈它能不能看见经典侧看不见的代数循环。**
