# HODGE Stage H0H — Lefschetz (1,1) / Picard–dlog Algebraic Lifting Gate

Date: `2026-08-17`
Status: `ACTIVE / DRIVER-ISSUED TASKBOOK`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Task ID: `RS-HODGE-H0H-LEFSCHETZ-11-PICARD-LIFTING-ATTRIBUTED-R2`
identity_policy: `AUTO_RESOLVE_OR_ALLOCATE`
identity_lane: `HODGE-H0H-PICARD-LIFTING`
owner branch: `research/hodge-h0h-lefschetz11-picard-lifting`
control branch: `research/hodge-special-control-plane`
parent H0G frozen head: `2335f1b91998943c055b9c02d144d0128e6cdc29`
parent H0D robust-R2 head: `102f6c73a099a97a412e72c810f8e63d2c370234`

## 0. Driver acceptance of H0G

H0G is accepted as a valid negative theorem-critical recognition result.

Frozen disposition:

`H0G_R1_SOURCE_COHOMOLOGICAL_NORMAL_FORM_ALREADY_COMPLETE`

Frozen hard-target result:

`ALGEBRAIC_DERHAM_FILTRATION_SOURCE_INSTANTIATES_ROBUST_ATTRIBUTED_R2 = NOT_ESTABLISHED`.

H0G is the first stage to use a genuinely Hodge-filtration-adjacent source.  It proves on the declared exact filtered Čech–de Rham source that

`FILTRATION_LIFT_1(z) <=> [pi0(z)] = 0 in L_Z / im(pi0 D|K1)`.

Its future repair quotient has real abstract leverage (`57 -> 34` reusable interface dimensions), but fair source homological algebra independently constructs the same quotient spaces and the same 10-dimensional obstruction.  Therefore the leverage is source-inherited under the H0D0 attribution criterion.

Driver route decision:

`HODGE_FILTRATION_RECOGNITION_SOURCE_COMPLETE__PIVOT_TO_ALGEBRAIC_LIFTING`.

This does **not** assert that H0G's bounded finite carrier computes all of `H_dR^2(P^2)`.  It means only that the recognition/filtration-repair obligation now has an exact source-native normal form, so further compression of recognition is not the missing Hodge step.

H0H attacks the first hard algebraicity gate instead.

---

## 1. Mission

The p=1 target is the Lefschetz `(1,1)` lifting mechanism.

For a smooth projective complex algebraic variety `X`, the classical target is to understand a rational class

`alpha in H^2(X,Q) ∩ H^(1,1)`

through a lifting route of the form

`rational Hodge class`
`-> clear denominator / integral lattice class`
`-> line-bundle / Picard class`
`-> Cartier divisor class`
`-> rational divisor-cycle representation`.

H0H does **not** assume this route succeeds merely because the classical Lefschetz `(1,1)` theorem is known.

Single hard target:

`LEFSCHETZ_11_LIFTING_SOURCE_INSTANTIATES_ROBUST_ATTRIBUTED_R2`.

Preferred stronger outcome:

`LEFSCHETZ_11_ENTERPRISE_R3_PRESEED`.

A successful result must find a non-tautological Enterprise operational lifting component that is load-bearing relative to a fair source baseline and that interfaces correctly with Picard/line-bundle/divisor data.

External novelty is not required.

H0H may use the classical Lefschetz `(1,1)` theorem, analytic exponential-sequence proof, GAGA, Picard/divisor theory and de Rham Chern classes **only as controls/comparison boundaries unless a specific substatement is independently regenerated without importing the target conclusion**.

Do not start full Enterprise H1 cohomology.

---

## 2. Frozen authority / minimal startup packet

Mandatory:

1. `AGENTS.md`
2. `docs/GITHUB_INTERACTION_BUDGET.md`
3. `research_common_surface.json`
4. `driver_handoffs/HODGE_SPECIAL_DRIVER_HANDOFF_20260817.md`
5. `driver_handoffs/HODGE_SPECIAL_DRIVER_PI_GEOMETRY_ADDENDUM_20260817.md`
6. H0A0 Criterion V2 artifacts at `f4e6cf84eb191e0b7442913e018e1f6347e9584e`.
7. H0D0 leverage-attribution artifacts at `96e79629b822a8cb3bc11be1cec8abe319e4cd20`.
8. H0D robust attributed-R2 artifacts at `102f6c73a099a97a412e72c810f8e63d2c370234`.
9. H0G frozen source/bridge/obstruction/classification/checkpoint at `2335f1b91998943c055b9c02d144d0128e6cdc29`.
10. `native_semantics_admissibility.json`.

Historical artifacts are read-only.

Do not recursively traverse unrelated repository history.

---

## 3. The exact p=1 lifting boundary

H0G has typed the classical recognition-side fact:

for a rational class `alpha` in a pure weight-2 Hodge structure,

`alpha is of type (1,1) <=> alpha_C lies in F^1`.

H0H now treats this recognition result as an **input boundary**, not as the theorem to optimize.

The unresolved p=1 algebraicity obligation is:

`recognized rational (1,1) class -> algebraic divisor class`.

Required typed steps:

1. **Rational lattice step**
   - state precisely how `alpha in H^2(X,Q)` is scaled by some positive integer `N` so that `N alpha` lies in the integral Betti lattice modulo torsion;
   - keep torsion/type conventions explicit;
   - never silently replace the rational problem by an integral one.

2. **Picard lift step**
   - seek a line-bundle/Picard object `L` with first Chern class matching the scaled class under an exact typed comparison;
   - nonuniqueness / Picard-kernel phenomena must be allowed.

3. **Divisor step**
   - type the conversion from an invertible sheaf/line bundle to Cartier divisor data on the declared algebraic scope;
   - preserve rational scaling when returning from `N alpha` to `alpha`.

4. **Cycle-class correctness**
   - final p=1 target must be stated as equality after the declared cycle-class comparison, not merely existence of a combinatorial or local cocycle.

No known target divisor may be fed into the generator.

---

## 4. Classical comparison firewall

The following are standard prior mathematics and may be used as controls/checkers:

- Picard group as line bundles / `H^1(O^×)` at the appropriate sheaf-theoretic level;
- Čech multiplicative cocycles and gauge/coboundary equivalence;
- Cartier divisors and principal-divisor relations;
- algebraic `dlog` and de Rham first Chern class constructions;
- divisor/valuation arithmetic;
- exact lattice algebra including Smith/Hermite normal forms;
- analytic exponential sequence;
- classical Lefschetz `(1,1)` theorem;
- GAGA algebraization of holomorphic line bundles in the projective setting;
- standard Picard/Néron–Severi calculations for benchmark varieties.

But:

`KNOWN_LEFSCHETZ_11_SURJECTIVITY_IS_CONTROL_ONLY`.

Do not define the Enterprise lift by taking the line bundle/divisor whose existence is supplied by the classical theorem.

Do not use a known Picard basis or known divisor generators to manufacture the target answer and then call the resulting coordinate vector an Enterprise lift.

If the load-bearing step is exactly the classical exponential-sequence proof, a standard divisor exact sequence, standard Picard quotienting, or standard Smith/Hermite reduction under new notation, classify it as source/prior-art operational structure with no Enterprise attribution unless a distinct transform-caused proof-form differential is proved.

### 4.1 Classical `2πi` / π guard

Any `2πi` normalization belonging to the classical Betti/de Rham/exponential comparison stays entirely in the classical comparison layer.

Standard real π, classical circle geometry or analytic exponential normalization may **not** be promoted into an Enterprise-native generator.

The Enterprise source should use typed exact-sequence/cohomological relations or algebraic transition data, not a native claim that standard π has been recovered.

---

## 5. Primary actual algebraic source family

Primary benchmark:

`X = P^1_C x P^1_C`

with its standard four affine charts.

Generate line-bundle transition data from algebraic overlap unit formulas, not from a predeclared answer `O(a,b)` attached to the requested Hodge class.

At minimum:

- construct the overlap rings/localizations exactly;
- enumerate a predeclared bounded family of algebraic unit candidates on pair overlaps;
- impose multiplicative triple-overlap cocycle conditions;
- quotient by local gauge/unit changes only through declared operations;
- derive `dlog` / de Rham Chern data from candidate unit cocycles;
- retain factor-swap naturality as a stress test;
- include positive and negative lift instances chosen **before** evaluating Enterprise success.

Known `Pic(P^1 x P^1) ≅ Z^2`, standard rulings, `O(a,b)` classification and known divisor basis are checker/control facts only.  They may verify a result after generation but may not generate the candidate lift.

### 5.1 Non-product stress

If the primary benchmark collapses completely to a source-native exponent lattice before any Enterprise candidate is evaluated, do not tune the bound merely to create an apparent advantage.

Add one exact non-product algebraic stress source, chosen from:

- the blow-up of `P^2` at one point via an explicit algebraic affine cover; or
- another smooth projective surface whose local unit/line-bundle source can be generated exactly without importing a known Picard answer.

The non-product stress is a qualification source, not a universal proof of Lefschetz `(1,1)`.

If exact sourcing becomes impossible without importing the target classification, freeze that as the missing object rather than fabricating a source.

---

## 6. Source problem / theorem-critical lifting language

At a minimum define a finite exact source problem containing:

- a typed target cohomological/de Rham class descriptor `a` independent of Enterprise state;
- a finite algebraically generated candidate space of multiplicative overlap-unit assignments `g_ij`;
- local gauge operations `h_i`;
- cocycle checks on triple overlaps;
- `dlog/c1` comparison data;
- optional divisor/valuation readout when algebraically generated;
- a final predicate `PICARD_LIFT(a)` meaning a valid candidate line-bundle class realizes the declared target comparison.

The target descriptor may be a finite exact surrogate for the lift interface; do **not** claim it is every Hodge class on the variety unless proved.

Required positive control:

an independently generated source class with a valid lift.

Required negative/control boundary:

an exact class inside the finite comparison carrier that is not realized by the frozen bounded candidate space, or a source instance showing that naive local `dlog` matching is insufficient because of multiplicative cocycle/gauge/global compatibility.

Do not select the candidate space by first looking at the desired lift.

---

## 7. Fair source-baseline sandwich

Freeze both baselines before using any Enterprise class counts/obstruction ranks as success evidence.

### `B_raw^lift`

May use:

- exact algebraic overlap-unit enumeration;
- direct multiplicative cocycle checks;
- direct local gauge/coboundary action;
- exact `dlog` and declared Chern comparison;
- brute-force/exact source solving on the frozen finite carrier;
- exact divisor/valuation readout when sourced.

Do not preinstall future-signature or Enterprise quotient state.

### `B_std^lift`

Must additionally include every fair standard source operation, including as applicable:

- `H^1(O^×)` / Picard cocycle-gauge quotient normal forms;
- Cartier divisor and principal-divisor arithmetic;
- valuation maps and exact integer-lattice reduction;
- Smith/Hermite normal form;
- standard Čech simplification;
- exact `dlog/c1` kernel/image/cokernel constructions;
- source-native Néron–Severi or divisor-lattice normal forms **only if independently derived from the source, not imported as the target answer**;
- exact linear/rational scaling algebra;
- filtered/de Rham comparison objects already available from H0G;
- any independently derived source obstruction to line-bundle lifting.

The classical Lefschetz `(1,1)` **conclusion itself** remains a checker/target theorem and is not inserted as a baseline oracle.

Anti-gaming rule:

If Enterprise wins only because `B_raw^lift` withholds an obvious Picard/divisor/lattice normal form admitted in `B_std^lift`, classify `BASELINE_SENSITIVE_ATTRIBUTION`.

---

## 8. Required Enterprise candidate families

Study at least three structurally distinct candidates.

### H1 — Multiplicative cocycle future quotient

Use partial algebraic unit-cocycle assignments / gauge states as a multi-step source.

At each cut, define the strongest admissible future signature for all remaining cocycle, gauge and target-Chern obligations.

Ask whether the quotient:

- strictly reduces reusable lifting-interface state;
- has descended cocycle/gauge continuation;
- preserves complete lift/nonlift language;
- remains smaller than `B_std^lift` source-normal-form interfaces.

Do not confuse a standard Picard quotient with Enterprise attribution.

### H2 — `dlog` additive/multiplicative bridge

Starting from algebraically generated unit data, compare:

`multiplicative g_ij`
`-> dlog(g_ij)`
`-> filtered/de Rham class data`.

Seek an Enterprise operational constraint that detects or constructs liftability with strict leverage.

Required controls:

- two multiplicative cocycles with the same `dlog` behavior where gauge/Picard information differs, if such a source exists;
- local additive matching that fails global multiplicative cocycle compatibility;
- kernel/nonuniqueness cases.

If ordinary `dlog` kernel/image/cokernel mathematics completely controls the source language, freeze source-inherited leverage.

### H3 — Divisor / valuation lifting carrier

When exact algebraic source supports it, map transition/rational-function data to integer valuations along codimension-one components.

Seek a finite integral obstruction or normal form for the lift.

Fair baseline must include standard divisor/principal-divisor lattices and SNF/HNF.

Do not award Enterprise credit merely because integer coordinates are convenient.

### Optional H4 — Rational scaling / denominator interface

Track the operation

`alpha -> N alpha -> integral line-bundle/divisor lift -> (1/N) divisor_Q`.

A successful interface must be independent of arbitrary denominator choices up to the declared rational cycle equivalence.

---

## 9. Attribution gate

Every claimed Hodge-special R2 must carry both:

- a Criterion V2 `PROOF_LEVERAGE_CERTIFICATE`;
- an H0D0 `LEVERAGE_ATTRIBUTION_CERTIFICATE`.

Accepted attribution classes are unchanged.

Hard-target credit requires:

`ROBUST_TRANSFORM_ATTRIBUTED`

against both `B_raw^lift` and `B_std^lift`.

Possible leverage classes include:

- `FINITE_OBSTRUCTION_BASIS`;
- `DEPENDENCY_REDUCTION`;
- `COMPOSITIONAL_FACTORING`;
- `NORMAL_FORM`;
- `LAYER_LOWERING`;
- `INTEGRALITY_POSITIVITY_MONOTONICITY`.

A lift being computable is not enough.

A known theorem being reimplemented is not enough.

The transform must be load-bearing in creating the credited operational form relative to the fair source baseline.

---

## 10. Rational / integral typing

This stage must not conflate:

- `H^2(X,Z)`;
- its torsion-free image/lattice;
- `H^2(X,Q)`;
- `H^2(X,C)`;
- algebraic de Rham cohomology;
- Picard classes;
- divisor classes.

For rational `alpha`, record the exact denominator-clearing statement used.

If an integral lift `L` is constructed for `N alpha`, the final rational cycle must be typed as `(1/N)D` in the rational cycle group, with correctness after the declared rational cycle-class map.

Different admissible `N` must yield compatible rational classes at the exact claim scope.

No integral Hodge conjecture claim is permitted.

---

## 11. Presentation / descent / gauge naturality

At the declared scope audit:

- cover-index relabeling;
- chart/frame/unit changes;
- local gauge transformations;
- factor swap on `P^1 x P^1`;
- coboundary-equivalent transition cocycles;
- refinement only if claimed;
- divisor representative changes by principal divisors when divisor readout is used.

A theorem-critical lift must descend to line-bundle/Picard or divisor-class level, not depend on one arbitrary Čech representative.

Historical all-presentations H0A remains suspended as a mainline task.

---

## 12. R3 / Lefschetz `(1,1)` preseed gate

An R3 preseed is allowed only if robust attributed R2 has already passed.

Then type all of the following:

### HBR-1 — Hodge recognition bridge

`alpha in H^2(X,Q) ∩ H^(1,1)`

through the classical typed comparison to the declared de Rham/filtration source, with no finite-carrier overclaim.

### HBR-2 — Independent Enterprise lifting constraint

An Enterprise operational state/constraint defined without querying a known line bundle/divisor answer.

### HBR-3 — Hodge-to-Enterprise theorem

A correctly scoped implication/equivalence showing the recognized p=1 Hodge condition enters the lifting source.

### HBR-4 — Robust attributed leverage

A passed H0D0 attribution certificate.

### HBR-5 — Algebraic lifting interface

An explicit path to line-bundle/Picard and then Cartier-divisor/rational-cycle data.

### HBR-6 — Correctness obligation

At minimum type the eventual theorem:

`cl_Q((1/N)D) = alpha`.

If existence remains unproved, state exactly which lift-existence object is missing.

R3 preseed is not the full Lefschetz theorem unless all necessary global statements are actually proved.

---

## 13. Target-leakage firewall

Forbidden as generator input:

- known divisor representative of the target class;
- known line bundle lifting the target class;
- a known Picard basis used to solve the target and then renamed Enterprise coordinates;
- the Lefschetz `(1,1)` surjectivity conclusion;
- known Hodge numbers used to fit dimensions;
- known cycle-class coordinates used as labels;
- classical Hodge decomposition answer for a specific benchmark class;
- analytic exponential-sequence output line bundle;
- GAGA output object selected from the known answer.

Classical results may validate or type the final comparison only.

---

## 14. Prior-art / source-normal-form firewall

Build an explicit matrix including at minimum:

- Čech `O^×` cocycles and gauge quotient;
- Picard group;
- `dlog` and de Rham Chern class;
- Cartier divisors / principal divisors;
- divisor class group on the smooth benchmark;
- valuations;
- SNF/HNF and integer lattice solving;
- analytic exponential sequence;
- classical Lefschetz `(1,1)`;
- GAGA;
- standard Picard calculations for the chosen benchmark.

Novelty remains independent of operational rank.

But if the exact credited lifting normal form already exists in the source through one of these standard structures, attribution fails even when the Enterprise packaging is elegant.

---

## 15. Required classification

Freeze exactly one strongest disposition:

### `H0H_R3_LEFSCHETZ_11_PRESEED_FOUND`

Robust attributed R2 plus a typed p=1 Hodge-to-line-bundle/divisor lifting interface survives all firewalls.

### `H0H_R2_PICARD_LIFT_OPERATION_FOUND`

A robust attributed R2 lifting component is found, but the Hodge/R3 bridge is not yet sufficiently typed.

### `H0H_R1_SOURCE_PICARD_NORMAL_FORM_ALREADY_COMPLETE`

The actual algebraic lift source is correct, but fair Picard/divisor/lattice mathematics already owns the same operational normal form.

### `H0H_CLASSICAL_PROOF_ONLY_NO_ENTERPRISE_CREDIT`

The only viable route reproduces the classical Lefschetz/exponential/GAGA proof without transform-attributed operational leverage.

### `H0H_FAIL_ALGEBRAIC_LIFT_SOURCE_GENERATION`

The declared finite algebraic unit/Picard source cannot be generated without importing the target answer.

No other final disposition without Driver review.

---

## 16. H1 firewall

No automatic H1 start.

Even `H0H_R3_LEFSCHETZ_11_PRESEED_FOUND` returns to Driver review.

Do not build a full Enterprise chain/cochain theory in H0H.

---

## 17. Required artifacts

At minimum produce:

1. `research_results/HODGE_H0H_LIFTING_SOURCE_SPEC.json`
2. `research_results/HODGE_H0H_UNIT_COCYCLE_GENERATION.json`
3. `research_results/HODGE_H0H_SOURCE_BASELINE_SANDWICH.json`
4. `research_results/HODGE_H0H_PICARD_GAUGE_REGISTRY.json`
5. `research_results/HODGE_H0H_DLOG_CHERN_BRIDGE.json`
6. `research_results/HODGE_H0H_DIVISOR_VALUATION_REGISTRY.json`
7. `research_results/HODGE_H0H_LIFTING_COMPARISON_REGISTRY.json`
8. `research_results/HODGE_H0H_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json`
9. `research_results/HODGE_H0H_ATTRIBUTION_CERTIFICATE_REGISTRY.json`
10. `research_results/HODGE_H0H_RATIONAL_SCALING_LEDGER.json`
11. `research_results/HODGE_H0H_PRESENTATION_GAUGE_NATURALITY.json`
12. `research_results/HODGE_H0H_PRIOR_ART_NOVELTY_LEDGER.json`
13. `research_results/HODGE_H0H_TARGET_LEAKAGE_LEDGER.json`
14. `research_results/HODGE_H0H_LEFSCHETZ_R3_PRESEED.json`
15. `research_results/HODGE_H0H_CLASSIFICATION.json`
16. `research_results/HODGE_H0H_SEMANTIC_CHECKPOINT.md`
17. deterministic checker + checker output
18. manifest with SHA-256 digests.

---

## 18. Mandatory checker gates

At minimum verify:

- Criterion V2 unchanged;
- H0D0 attribution addendum active;
- H0G historical result preserved;
- source unit data generated algebraically, not from target divisor/line bundle;
- multiplicative cocycle conditions exact;
- gauge/coboundary equivalence exact;
- `dlog/c1` typing explicit;
- rational/integral/torsion typing explicit;
- denominator clearing explicit;
- no known target divisor/line bundle generator;
- no Lefschetz `(1,1)` conclusion used as generator;
- no standard π used as Enterprise-native generator;
- `B_raw^lift` and `B_std^lift` frozen before success metrics;
- source-native Picard/divisor/SNF normal forms counted fairly;
- any R2 has both leverage and attribution certificates;
- any R3 preseed has HBR-1 through HBR-6 typed;
- cycle-class correctness obligation explicit;
- finite checks not promoted to general theorem;
- target leakage PASS;
- H1 remains blocked;
- no full Hodge conjecture claim.

---

## 19. Completion / advancement vector

Before H0H:

- realization criterion V2: `FROZEN`;
- leverage attribution criterion: `FROZEN`;
- abstract robust attributed R2: `FOUND (H0D)`;
- actual algebraic regularity-source attributed R2: `NO-GO (H0E/H0F)`;
- Hodge-filtration recognition source: `SOURCE-NORMAL-FORM COMPLETE (H0G scope)`;
- p=1 algebraic lifting mechanism: `OPEN`;
- R3: `NOT FOUND`;
- Enterprise H1/cohomology: `NOT STARTED`;
- general algebraic-cycle lifting: `0%`.

Expected H0H advancement vector:

`p=1 algebraicity gate +15%`
`Hodge recognition search -20% (de-emphasized)`
`lifting interface +20%`
`full H1 0%`.

---

## 20. Return protocol

Return to:

`EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`

with:

- exact owner head;
- final classification;
- hard-target result;
- strongest candidate and attribution status;
- exact source-normal-form competitor;
- R3 preseed status;
- H1 status;
- checker count/digest;
- manifest digest;
- next route recommendation.

No automatic next stage.
