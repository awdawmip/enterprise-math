# HODGE Stage H0H-R1 — Canonical-Plane-Rebased Lefschetz (1,1) / Picard–Divisor Algebraic Lifting

Date: `2026-08-21`
Status: `ACTIVE / DRIVER-ISSUED REISSUE`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Task ID: `RS-HODGE-H0H-R1-LEFSCHETZ-11-PICARD-LIFTING-CANONICAL-PLANE`
identity_policy: `AUTO_RESOLVE_OR_ALLOCATE`
identity_lane: `HODGE-H0H-R1-PICARD-LIFTING`
owner branch: `research/hodge-h0h-r1-canonical-plane-picard-lifting`
control branch: `research/hodge-special-control-plane`

## 0. Supersession / current progress

The previous dispatch

`RS-HODGE-H0H-LEFSCHETZ-11-PICARD-LIFTING-ATTRIBUTED-R2`

at taskbook source

`41828d214e65163baaef6c31fff4c759afe1c223`

is frozen as

`SUPERSEDED_BEFORE_EXECUTION`.

Its owner branch was still identical to its taskbook source (`ahead_by=0`) when this reissue was prepared. No H0H result is being discarded.

Parent accepted Hodge state remains:

- H0A0 Criterion V2: `f4e6cf84eb191e0b7442913e018e1f6347e9584e`;
- H0D0 attribution criterion: `96e79629b822a8cb3bc11be1cec8abe319e4cd20`;
- H0D abstract robust attributed R2: `102f6c73a099a97a412e72c810f8e63d2c370234`;
- H0G filtered Čech–de Rham recognition no-go: `2335f1b91998943c055b9c02d144d0128e6cdc29`.

H0G route decision remains:

`HODGE_FILTRATION_RECOGNITION_SOURCE_COMPLETE__PIVOT_TO_ALGEBRAIC_LIFTING`.

H0H-R1 attacks the first algebraicity gate rather than re-running Hodge-filtration recognition.

---

## 1. Current canonical Enterprise coordinate authority

The old signed-origin-one / no-native-zero foundation is superseded.

Canonical foundational authority for any native-coordinate claim in this task is:

`definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`

at commit

`c4649b276a3d604822c586dddafd028e15d02976`.

Supersession marker:

`ad6c8dc4ff3969eee29c68ea0cc15e1930c6db47`.

Required current facts:

- `O_E = 0`;
- native cells are circle cells;
- cell centers form a triangular lattice with nearest-neighbor spacing `1`;
- cell radius is `1/sqrt(3)`;
- every circle-boundary intersection is a triple-cell intersection;
- three positive primitive directions `e1,e2,e3` satisfy `e1+e2+e3=0`;
- native addresses use nonnegative triples modulo common diagonal shift, canonicalized by `min(a,b,c)=0`;
- the native displacement quadratic form is
  `Q_E(a,b,c)=a^2+b^2+c^2-ab-bc-ca`;
- cell center, circle cell, and coordinate vertex are distinct object types.

Historical assumptions forbidden as current native generators:

- `O_E=[+1]=[-1]`;
- `ZERO_IS_NOT_AN_ENTERPRISE_COORDINATE`;
- signed native `...,-3,-2,±1,+2,+3,...` axis ontology;
- pairwise-orthogonal three-axis metric;
- direct `sqrt(a^2+b^2+c^2)` on native three-axis addresses.

Read the canonical definition from the exact authority commit even if it is not present in the owner-branch tree.

---

## 2. Mission

Primary p=1 algebraicity target:

`alpha in H^2(X,Q) cap H^(1,1)`

through the typed lifting chain

`rational Hodge class`
`-> denominator-cleared integral lattice class`
`-> Picard / line-bundle class`
`-> Cartier divisor class`
`-> rational divisor cycle`
`-> exact rational cycle-class equality`.

Single hard target:

`LEFSCHETZ_11_LIFTING_SOURCE_INSTANTIATES_ROBUST_ATTRIBUTED_R2`.

Preferred stronger outcome:

`LEFSCHETZ_11_ENTERPRISE_R3_PRESEED`.

Coordinate compatibility is a qualification gate, not an independent success criterion.

A candidate may pass only if its coordinate status is one of:

- `COORDINATE_IRRELEVANT` — the load-bearing Enterprise operation is coordinate-free and makes no native-plane claim;
- `COORDINATE_COMPATIBLE` — the candidate genuinely uses native plane/cell/address structure and passes every current canonical-coordinate compatibility test.

Reject:

- `COORDINATE_INCOMPATIBLE`;
- `COORDINATE_UNTYPED` for any load-bearing native claim.

Do not force coordinate geometry onto a proof component that is naturally Picard/divisor/homological algebra.

---

## 3. Fundamental typing firewall

Keep the following objects distinct even when the same numeral is written:

1. `0_source` — zero in an abelian group, vector space, ring, divisor lattice, chain complex, etc.;
2. `O_E=0` — Enterprise geometric origin;
3. `1_Ox` — multiplicative unit in `O^×`;
4. native cell/address labels;
5. classical integer valuations;
6. rational coefficients in cycle groups.

Numerical coincidence does not establish an identification.

Negative divisor valuations are ordinary source integers. They are not evidence for native negative axes; the current Enterprise plane does not require native negative axes.

If a candidate claims a native realization of an integer/rank-two lattice, it must explicitly define the realization and prove all required algebraic operations. The canonical nonnegative address set by itself is not automatically an abelian group.

If group structure is required, type a displacement group such as a proved quotient of `Z^3` by the diagonal relation and prove how canonical nonnegative representatives realize it. Do not silently identify

`A_E = { (a,b,c) in N_0^3 : min(a,b,c)=0 }`

with a source Picard/divisor group.

`Q_E` is a native geometric metric only. Do not install it on Picard, Néron–Severi, divisor, or cohomology groups unless a theorem independently supplies that structure.

---

## 4. Classical comparison firewall

The following are standard source/control mathematics:

- line bundles / Picard group / `H^1(O^×)`;
- Čech multiplicative cocycles and gauge equivalence;
- Cartier divisors and principal divisors;
- valuations along codimension-one components;
- `dlog` and algebraic/de Rham first Chern constructions;
- integer/rational lattice algebra, SNF/HNF;
- analytic exponential sequence;
- GAGA in its valid projective comparison scope;
- classical Lefschetz `(1,1)` theorem;
- known Picard/Néron–Severi computations for benchmark varieties.

Controls may verify results but may not generate the target line bundle/divisor.

Freeze:

`KNOWN_LEFSCHETZ_11_SURJECTIVITY_IS_CONTROL_ONLY`.

`KNOWN_PICARD_BASIS_IS_NOT_A_GENERATOR`.

`KNOWN_DIVISOR_REPRESENTATIVE_IS_NOT_A_GENERATOR`.

`CLASSICAL_2PII_NORMALIZATION_STAYS_CLASSICAL`.

If the load-bearing step is ordinary Picard quotienting, exponential-sequence reasoning, divisor exact-sequence algebra, valuation reduction, or SNF/HNF under renamed states, classify it as source-inherited unless a transform-caused proof differential is proved.

---

## 5. Primary algebraic source

Primary benchmark:

`X = P^1_C x P^1_C`

with its standard four affine charts.

Generate source data from exact overlap rings/localizations and a predeclared bounded family of algebraic unit candidates. Do not start from the known answer `Pic(X)=Z^2`, the ruling divisors, or `O(a,b)` attached to the requested target.

Required source construction:

- exact overlap rings/localizations;
- algebraic units on pair overlaps from a predeclared bounded grammar;
- multiplicative triple-overlap cocycle conditions;
- local gauge/unit transformations;
- exact `dlog` / Chern comparison data;
- optional valuation/divisor readout only when derived from generated rational functions/units;
- positive and negative/boundary lift instances frozen before Enterprise success evaluation.

Known `Pic(P^1 x P^1)=Z^2` and standard rulings are checker facts only.

### 5.1 Rank-two/native-A2 anti-leakage guard

The current Enterprise displacement geometry also has a rank-two relation because `e1+e2+e3=0`.

This numerical/rank coincidence must not influence source selection, candidate bounds, expected Picard rank, or target answer.

Any later comparison between a source rank-two lattice and native three-axis displacement coordinates is post-generation qualification only.

A mere isomorphism/reparameterization receives at most R0/R1 and never hard-target credit.

### 5.2 Non-product stress

If the product benchmark collapses to an independently derived source-normal-form lattice before Enterprise evaluation, do not tune the bound to manufacture leverage.

Add one exact non-product stress source, preferably:

- `Bl_p(P^2)` with an explicit algebraic affine cover;

or another smooth projective surface whose local unit/divisor source can be generated without importing its Picard answer.

If exact sourcing would require the target classification, freeze that as a missing object.

---

## 6. Fair source baselines

Freeze before any Enterprise success count.

### `B_raw^lift`

Allow:

- exact overlap-unit enumeration;
- cocycle checks;
- direct gauge/coboundary action;
- exact `dlog/c1` computation;
- direct source solving;
- exact divisor/valuation readout when independently sourced.

Do not install future signatures or behavioral minimization.

### `B_std^lift`

Must additionally allow every fair standard source normal form, including:

- Picard cocycle/gauge quotients;
- Cartier/principal-divisor arithmetic;
- valuation maps;
- divisor lattices;
- SNF/HNF;
- Čech simplification;
- exact `dlog/c1` kernel/image/cokernel;
- source-native Néron–Severi/divisor normal forms if independently derived;
- denominator clearing and rational rescaling;
- H0G filtered/de Rham source results;
- any independently derived lifting obstruction.

The classical Lefschetz `(1,1)` conclusion itself is not inserted as an oracle.

If a candidate wins only because `B_raw^lift` withholds an obvious standard normal form available in `B_std^lift`, classify:

`BASELINE_SENSITIVE_ATTRIBUTION`.

---

## 7. Required candidate families

Study at least H1, H2, H3. H4 is a mandatory coordinate qualification/control if any native-coordinate claim is attempted.

### H1 — Multiplicative cocycle future quotient

Use partial algebraically generated unit-cocycle assignments / gauge states as a multistep source.

Define complete future signatures for all remaining cocycle, gauge, and target-Chern obligations.

Audit:

- exact correctness;
- descended continuation;
- coarsest/sufficient quotient at declared scope;
- strict proof leverage;
- attribution against both baselines.

Do not award credit for the ordinary Picard quotient itself.

### H2 — `dlog` additive/multiplicative bridge

From generated units:

`g_ij -> dlog(g_ij) -> de Rham/Chern data`.

Required controls where available:

- same additive/`dlog` behavior but distinct multiplicative/gauge information;
- local additive matching without global multiplicative cocycle compatibility;
- kernel/nonuniqueness cases.

If standard kernel/image/cokernel completely controls the language, freeze source-inherited leverage.

### H3 — Divisor / valuation lifting carrier

When the algebraic source supports it, derive integer valuations along codimension-one components and test an operational lift/obstruction carrier.

Fair baseline includes standard divisor/principal-divisor lattice mathematics and SNF/HNF.

Integer coordinates are not Enterprise-native merely because they are integer-valued.

### H4 — Canonical native-plane lattice bridge audit / anti-false-positive control

Perform this only after an independent source lattice has been generated.

If a native bridge is proposed, audit all of:

1. exact domain/codomain typing;
2. `O_E=0` versus source zero separation;
3. diagonal-shift relation `(a,b,c)~(a+k,b+k,c+k)`;
4. canonical representative `min(a,b,c)=0`;
5. any claimed group law via a proved displacement-group construction;
6. origin/cell-center/coordinate-vertex type separation;
7. no use of signed-origin-one history;
8. no use of pairwise-orthogonal native axes;
9. no use of `Q_E` unless metric relevance is independently justified;
10. reparameterization control showing that a bare rank-two lattice isomorphism earns no R2 credit.

Possible verdicts:

- `COORDINATE_IRRELEVANT`;
- `COORDINATE_COMPATIBLE_NON_LOAD_BEARING`;
- `COORDINATE_COMPATIBLE_LOAD_BEARING_CANDIDATE`;
- `COORDINATE_INCOMPATIBLE`.

Even `COORDINATE_COMPATIBLE_LOAD_BEARING_CANDIDATE` still must pass H0D0 attribution.

---

## 8. Rational / integral lifting correctness

Never conflate:

- `H^2(X,Z)` and torsion-free image;
- `H^2(X,Q)`;
- `H^2(X,C)`;
- algebraic de Rham cohomology;
- Picard classes;
- divisor classes;
- Enterprise native addresses.

For rational `alpha`, record an explicit positive integer `N` with the exact integral-lattice statement used.

If `N alpha` lifts to a line bundle/divisor `D`, return to the rational target only as `(1/N)D` in the rational cycle group and prove equality after the declared rational cycle-class map.

Different admissible denominator choices must agree at the exact rational-cycle equivalence scope claimed.

No integral Hodge conjecture claim is permitted.

---

## 9. Attribution and R3 gate

Every claimed Hodge-special R2 requires:

- Criterion V2 `PROOF_LEVERAGE_CERTIFICATE`;
- H0D0 `LEVERAGE_ATTRIBUTION_CERTIFICATE`;
- coordinate status from Section 2/7 when native claims are present.

Hard-target credit requires:

`ROBUST_TRANSFORM_ATTRIBUTED`

against both baselines, plus coordinate status

`COORDINATE_IRRELEVANT`

or

`COORDINATE_COMPATIBLE*`.

Possible leverage classes include:

- `FINITE_OBSTRUCTION_BASIS`;
- `DEPENDENCY_REDUCTION`;
- `COMPOSITIONAL_FACTORING`;
- `NORMAL_FORM`;
- `LAYER_LOWERING`;
- `INTEGRALITY_POSITIVITY_MONOTONICITY`.

For the stronger

`LEFSCHETZ_11_ENTERPRISE_R3_PRESEED`,

require all of:

1. robust attributed R2 lifting component;
2. typed input from recognized rational `(1,1)` data without target leakage;
3. exact Picard/line-bundle or divisor output;
4. rational cycle-class correctness;
5. gauge/presentation/descent compatibility;
6. no known target line bundle/divisor used as generator;
7. explicit statement of which HBR obligations are now satisfied and which remain missing.

Do not auto-start H1 even if an R3 preseed is found.

---

## 10. Presentation / naturality / target leakage

Audit at claim scope:

- cover-index relabeling;
- chart/frame/unit changes;
- local gauge transformations;
- factor swap on `P^1 x P^1`;
- coboundary-equivalent cocycles;
- denominator choice;
- any native-plane coordinate recanonicalization used by a candidate.

Forbidden generator inputs include:

- known Lefschetz `(1,1)` line bundle/divisor;
- known Picard basis;
- known ruling/divisor generators selected to match the target;
- Hodge numbers;
- known algebraic-cycle representative of the target class;
- signed-origin-one native semantics;
- old orthogonal three-axis metric;
- any native-plane metric inserted into source Picard/divisor algebra without theorem.

---

## 11. Required artifacts

At minimum produce:

- `research_results/HODGE_H0H_R1_COORDINATE_AUTHORITY_LEDGER.json`
- `research_results/HODGE_H0H_R1_ALGEBRAIC_SOURCE_SPEC.json`
- `research_results/HODGE_H0H_R1_SOURCE_BASELINE_SANDWICH.json`
- `research_results/HODGE_H0H_R1_PICARD_LIFT_REGISTRY.json`
- `research_results/HODGE_H0H_R1_DLOG_BRIDGE_REGISTRY.json`
- `research_results/HODGE_H0H_R1_DIVISOR_VALUATION_REGISTRY.json`
- `research_results/HODGE_H0H_R1_NATIVE_COORDINATE_COMPATIBILITY_LEDGER.json`
- `research_results/HODGE_H0H_R1_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json`
- `research_results/HODGE_H0H_R1_ATTRIBUTION_CERTIFICATE_REGISTRY.json`
- `research_results/HODGE_H0H_R1_RATIONAL_LIFTING_LEDGER.json`
- `research_results/HODGE_H0H_R1_PRESENTATION_NATURALITY_LEDGER.json`
- `research_results/HODGE_H0H_R1_TARGET_LEAKAGE_LEDGER.json`
- `research_results/HODGE_H0H_R1_PRIOR_ART_NOVELTY_LEDGER.json`
- `research_results/HODGE_H0H_R1_R3_PRESEED.json`
- `research_results/HODGE_H0H_R1_CLASSIFICATION.json`
- `research_results/HODGE_H0H_R1_CHECKER_OUTPUT.json`
- `research_results/HODGE_H0H_R1_SEMANTIC_CHECKPOINT.md`
- `research_results/HODGE_H0H_R1_MANIFEST.json`
- deterministic checker under `tools/`.

The checker must verify at least:

- taskbook/parent identities;
- canonical coordinate authority commit;
- absence of historical signed-origin native assumptions in load-bearing claims;
- source-vs-native zero typing;
- source generation before target answer;
- baseline fairness;
- attribution classification;
- rational denominator bookkeeping;
- coordinate compatibility verdict for every native claim;
- no target leakage;
- R3/H1 firewall.

---

## 12. Final classification

Choose exactly one primary disposition:

- `H0H_R1_ROBUST_ATTRIBUTED_LIFTING_R2_FOUND`
- `H0H_R1_LEFSCHETZ11_R3_PRESEED_FOUND`
- `H0H_R1_SOURCE_PICARD_DIVISOR_NORMAL_FORM_ALREADY_COMPLETE`
- `H0H_R1_BASELINE_SENSITIVE_ONLY`
- `H0H_R1_COORDINATE_REBASE_INVALIDATES_NATIVE_CANDIDATE_ONLY`
- `H0H_R1_SOURCE_GENERATION_BLOCKED_WITH_TYPED_MISSING_OBJECT`
- `H0H_R1_ATTRIBUTION_UNRESOLVED`

Historical H0A0/H0D0/H0D/H0E/H0F/H0G dispositions are immutable.

`H1_ADMISSIBLE=false` unless the Driver later issues an explicit new task.

Return to:

`EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`.
