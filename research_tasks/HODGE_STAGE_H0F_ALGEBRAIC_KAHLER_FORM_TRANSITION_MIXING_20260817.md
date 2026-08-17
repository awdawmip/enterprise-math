# HODGE Stage H0F — Algebraic Kähler-Form Transition Mixing / Robust Attribution

Date: `2026-08-17`
Status: `ACTIVE / DRIVER-ISSUED TASKBOOK`
Driver: `EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`
Task ID: `RS-HODGE-H0F-ALGEBRAIC-KAHLER-FORM-MIXING-ATTRIBUTED-R2`
identity_policy: `AUTO_RESOLVE_OR_ALLOCATE`
identity_lane: `HODGE-H0F-KAHLER-FORM-MIXING`
owner branch: `research/hodge-h0f-kahler-form-transition-mixing`
control branch: `research/hodge-special-control-plane`
parent H0D robust-R2 head: `102f6c73a099a97a412e72c810f8e63d2c370234`
parent H0E frozen head: `01bda7971b3023c486985bfe008ddfebbced52aa`

## 0. Driver acceptance of H0E

H0E is accepted as a valid negative algebraic-instantiation result.

Frozen disposition:

`H0E_R1_ALGEBRAIC_SOURCE_REALIZED_NO_ROBUST_ATTRIBUTION`

Frozen hard-target result:

`ACTUAL_ALGEBRAIC_SOURCE_INSTANTIATES_ROBUST_ATTRIBUTED_R2 = NOT_ESTABLISHED`.

H0E established that the H0D complete-suffix quotient is mathematically correct on a real algebraically generated `P^1 x P^1 / O(a,b)` multi-step source, but the fair source baseline already contains the exact same recursive normal form:

`RegSupp / toric-pole-support`.

On all six predeclared instances,

`ker(Sigma_i) = ker(RegSupp_i)`

and both source baseline and Enterprise quotient have the same stagewise interface count `4,4,4`.

Therefore the failure is not lack of algebraic sourcing. The theorem-critical source is too close to scalar toric regularity, whose source-native pole-support language already solves the future-behavior compression problem.

Do **not** rerun H0E with larger `B`, different lucky line-bundle degrees, or a weakened `B_std^alg`.

---

## 1. Mission

Change the theorem-critical algebraic source while preserving every H0A0/H0D0 qualification gate.

Primary source family:

`X = P^2_C`

with its standard three affine charts and algebraic Kähler differential data, preferably twisted algebraic one-forms

`Omega^1_X(m)`

for a predeclared small set of twists `m`.

The source must involve **non-diagonal algebraic transition mixing** of differential components under coordinate changes. The point is to leave the scalar `RegSupp` regime without importing analytic Hodge machinery.

Single hard target:

`ALGEBRAIC_KAHLER_FORM_SOURCE_INSTANTIATES_ROBUST_ATTRIBUTED_R2`.

A successful witness must satisfy:

- actual algebraic source generation;
- exact multi-step continuation semantics;
- Criterion V2 R2;
- H0D0 attribution addendum;
- robust attribution against both `B_raw^alg` and a fair strengthened `B_std^alg`;
- presentation/basis naturality at the exact scope claimed;
- target-leakage PASS.

External novelty is not required.

H0F does **not** prove Hodge and does **not** automatically start H1.

---

## 2. Frozen authority / minimal startup packet

Mandatory:

1. `AGENTS.md`
2. `docs/GITHUB_INTERACTION_BUDGET.md`
3. `research_common_surface.json`
4. `driver_handoffs/HODGE_SPECIAL_DRIVER_HANDOFF_20260817.md`
5. `driver_handoffs/HODGE_SPECIAL_DRIVER_PI_GEOMETRY_ADDENDUM_20260817.md`
6. H0A0 Criterion V2 artifacts at `f4e6cf84eb191e0b7442913e018e1f6347e9584e`:
   - `HODGE_H0A0_REALIZATION_CLASSIFIER_V2.json`
   - `HODGE_H0A0_PROOF_LEVERAGE_CERTIFICATE_SPEC.json`
7. H0D0 attribution artifacts at `96e79629b822a8cb3bc11be1cec8abe319e4cd20`:
   - `HODGE_H0D0_SOURCE_BASELINE_SPEC.json`
   - `HODGE_H0D0_LEVERAGE_ATTRIBUTION_CERTIFICATE_SPEC.json`
   - `HODGE_H0D0_FOUR_AXIS_MODEL.json`
8. H0D robust R2 artifacts at `102f6c73a099a97a412e72c810f8e63d2c370234`.
9. H0E frozen negative artifacts at `01bda7971b3023c486985bfe008ddfebbced52aa`:
   - source spec;
   - algebraic baseline sandwich;
   - quotient registry;
   - attribution certificate;
   - semantic checkpoint.
10. `native_semantics_admissibility.json`.

Read exact classical algebraic sources for Kähler differentials / projective-coordinate changes only as needed. Do not recursively traverse the repository.

Historical H0E remains read-only.

---

## 3. Source object — actual algebraic `P^2` differential forms

Use homogeneous coordinates

`[X0:X1:X2]`

and standard affine charts:

- `U0: X0 != 0`, coordinates `x=X1/X0`, `y=X2/X0`;
- `U1: X1 != 0`, coordinates `u=X0/X1=1/x`, `v=X2/X1=y/x`;
- `U2: X2 != 0`, coordinates `s=X0/X2=1/y`, `t=X1/X2=x/y`.

The algebraic source object is a finite declared family of rational algebraic one-forms, optionally twisted by `O(m)`, represented locally by exact coefficient pairs in the Kähler basis on each chart.

For example on `U0`:

`omega = A(x,y) dx + B(x,y) dy`

with exact rational/polynomial `A,B` from a predeclared finite seed family.

Transition to another chart must be derived from exact algebraic coordinate substitution and the differential identities obtained from the coordinate change. Do not hand-write a transition table.

Example identities used only as mandatory replay checks include:

`u=1/x`, `v=y/x`, hence

`du = -x^{-2} dx`

and

`dv = x^{-1} dy - y x^{-2} dx`.

The researcher must derive the corresponding coefficient transport in the target Kähler basis and verify both directions exactly.

For twisted `Omega^1(m)`, include the exact `O(m)` local-frame transition factor as part of source transport. Do not guess a sign/power convention; derive it from the declared frame convention and verify inverse composition.

### 3.1 No analytic generator

Allowed source language:

- algebraic coordinate rings/localizations;
- algebraic Kähler differentials;
- rational functions/forms;
- exact chart/frame transition formulas;
- algebraic regularity/pole conditions;
- exact finite-dimensional linear algebra on declared coefficient carriers.

Forbidden as generators:

- harmonic forms;
- Kähler metric;
- Hodge decomposition;
- analytic differential forms selected by Hodge type;
- known Hodge numbers;
- known algebraic-cycle representatives.

The word `Kähler` in `Kähler differentials` is algebraic terminology and does not authorize metric/Kähler-manifold data.

---

## 4. Predeclared finite seed/parameter family

Freeze the seed registry **before quotient counts are used as success evidence**.

Use at least two twists or source strengths. Preferred primary sweep:

- `m in {1,2}` for `Omega^1_{P^2}(m)`;
- seed degree/window `B in {1,2}`;
- root chart `U0`;
- continuation depth at least `3`;
- at least two continuation actions from every nonfinal cut.

The exact finite source seed family must include both pure and mixed components so that non-diagonal transition/cancellation is genuinely exercised. At minimum include representatives of the shapes:

- `x^r y^s dx`;
- `x^r y^s dy`;
- `x^r y^s (dx+dy)`;
- one antisymmetric/mixed form such as `x^r y^s (y dx - x dy)` or the strongest exact algebraic analogue after twist conventions are fixed.

Choose finite exponent windows and coefficient normalization deterministically. Scalar-ray quotienting is permitted only if nonzero scalar is theorem-inert for every declared observation; prove that before using it.

Do not tune seed families after seeing quotient success/failure.

If `m=1` or another predeclared parameter degenerates, retain it as a negative/trivial control rather than deleting it.

---

## 5. Multi-step continuation language

Use all three standard charts and define two deterministic chart-move actions at each stage, for example:

- `P`: move to the next chart in the cycle `U0 -> U1 -> U2 -> U0`;
- `M`: move to the previous chart in the cycle `U0 -> U2 -> U1 -> U0`.

Each move is source algebraic transport of the same rational/twisted one-form into the target chart coordinates.

A continuation succeeds iff, after exact rational simplification, the transported form is regular on the target chart in the declared source sense. Failure may enter one absorbing verification-only `SINK`.

At depth `3`, evaluate all eight `P/M` words from each declared root state. A larger fixed depth may be used only if predeclared before success evaluation and computationally exact.

The source must therefore support:

- multiple distinct suffix queries;
- repeated chart routes;
- coordinate-change composition identities;
- non-diagonal mixing of coefficient components;
- cancellation-sensitive regularity.

Do not collapse the task to one fixed query.

---

## 6. Deterministic algebraic generation firewall

Required pipeline:

`P^2 chart formulas + Omega^1(m) frame/basis formulas + frozen seed registry`

`-> exact algebraic transport`

`-> generated multi-step source table`

`-> hash / replay certificate`

`-> only then behavior quotient`.

Forbidden:

- copying H0D/H0E source tables;
- choosing target tables first and reverse-engineering forms;
- hand-labelling synthetic states with differential-form names;
- using quotient classes to choose seed forms;
- using Hodge/cycle answers to select forms or observations.

Produce source-table digests for every primary parameter.

---

## 7. Fair dual algebraic baseline

Freeze both baselines before quotient success evaluation.

### `B_raw^alg`

May use:

- exact chart/basis transport;
- direct execution of a declared continuation word;
- explicit intermediate states;
- exact final regularity observation.

It may not preinstall behavioral quotient/minimization.

### `B_std^alg`

Must extend `B_raw^alg` with every obviously source-native algebraic simplification relevant to the chosen source, including at minimum:

- exact rational-function simplification;
- common-denominator reduction and exact numerator cancellation;
- Jacobian / differential-basis matrix composition;
- exact local-frame change for `O(m)`;
- source-native pole order / polar-support information along coordinate hyperplanes;
- regularity support of the whole one-form, not just componentwise support;
- exact linear algebra on coefficient pairs;
- algebraic change of local differential basis by regular invertible matrices when part of the declared presentation semantics;
- any Euler/homogeneous-form or principal-part normal form that the researcher can derive independently from the source before quotient evaluation.

The source baseline must not be kept artificially weak merely because a source-native normal form threatens Enterprise attribution.

However `B_std^alg` may not simply install the complete future-signature quotient or generic automaton minimization by definition.

### Baseline gaming control

Include at least one case where withholding an obvious Jacobian/composition/cancellation simplification creates fake attribution against `B_raw^alg`, and prove that `B_std^alg` rejects it.

---

## 8. Enterprise candidate E1 — full suffix behavior quotient

For every nonfinal source state `s` at cut `i`, define

`Sigma_i(s)`

as the complete declared future regularity/observation function on all remaining `P/M` words.

Define

`q_i(s)=q_i(t) iff Sigma_i(s)=Sigma_i(t)`.

Construct:

- quotient carriers `Q_i`;
- descended `P/M` transitions;
- exact factorization of every future query;
- coarsest-sufficiency theorem on the declared finite language.

Reuse the H0D general suffix-signature theorem only as an abstract correctness theorem. The **algebraic sourcing and attribution must be redone** for H0F.

---

## 9. Comparison and proof-leverage gate

At minimum prove/check:

1. source execution vs quotient execution for every declared state/suffix;
2. descended transitions well-defined;
3. quotient coarsest sufficient for the declared complete suffix language;
4. a predeclared strict interface/dependency/normal-form measure;
5. exact reduction against `B_raw^alg` if present;
6. exact comparison against `B_std^alg`.

A raw state-count drop does not pass the hard target.

To pass robust attributed R2, the credited operational form must be absent from both baselines and the quotient transform must be load-bearing in constructing it.

Allowed attribution outcomes:

- `ROBUST_TRANSFORM_ATTRIBUTED`;
- `BASELINE_SENSITIVE_ATTRIBUTION`;
- `SOURCE_INHERITED`;
- `ATTRIBUTION_SHARED_OR_PARTIAL`;
- `ATTRIBUTION_UNRESOLVED`.

Only the first may satisfy the H0F hard target.

Prior-art status is descriptive only.

---

## 10. Source-native-normal-form challenge

H0E failed because `RegSupp` exactly equaled the Enterprise quotient.

H0F must explicitly search for the strongest fair algebraic source normal form before awarding attribution.

Candidate source-native summaries that must be tested if definable include:

- polar divisor/support plus pole orders;
- componentwise valuation vectors;
- basis-independent principal-part data;
- reduced common-denominator coefficient pairs;
- Euler/homogeneous differential-form representatives;
- exact invariant subspace or module generators naturally exposed by the source.

If any such source-native object recovers the complete suffix language with an interface no larger/stronger than the Enterprise quotient, attribution fails.

Do not hide a source normal form in order to preserve R2.

---

## 11. Non-diagonal mixing and cancellation controls

Mandatory controls:

### Negative scalarized control

Project the form to componentwise pole-support only. Exhibit at least one pair of forms with the same componentwise support/pole summary but different continuation behavior if such a pair exists. If no such pair exists on the declared seed family, record that the source still collapses to support semantics and H0F is not testing the intended mechanism.

### Cancellation control

Include an exact example where a coordinate change produces multiple terms and algebraic cancellation changes regularity or future behavior. If every declared form transports monomial-by-monomial without theorem-critical cancellation, classify the chosen seed family as insufficiently mixed and use the predeclared mixed controls rather than retuning after quotient evaluation.

### Basis-change control

A regular invertible change of local differential basis must not create/destroy theorem-critical behavior. Audit quotient transport under at least one nontrivial declared local basis change.

---

## 12. Presentation naturality / algebraic automorphism stress

At the claimed scope test at least:

- permutation of homogeneous coordinates `X0,X1,X2` generating standard-chart relabelings;
- at least one transposition and one 3-cycle;
- induced coordinate/basis transport on differential forms;
- quotient/signature transport;
- class-count invariance;
- descended-transition conjugacy.

Do not claim arbitrary-cover or full automorphism naturality unless proved.

Historical H0A remains a subgate, not the main task.

---

## 13. Hodge adjacency / R3 firewall

The algebraic source `Omega^1_X(m)` is closer to algebraic de Rham/Hodge language than the H0E scalar regularity source, but this does **not** authorize use of the classical Hodge answer.

If robust attributed R2 passes, produce only an R3 **preinterface** specifying what would still be needed for:

`C_H(X)`

`-> algebraic differential-form / local-source condition`

`-> Enterprise attributed quotient constraint`

`-> algebraic-cycle lifting interface`.

Required missing obligations must still include:

- a non-target-leaking `C_H` source map;
- rational coefficient compatibility;
- proof that the Enterprise constraint is theorem-critical for Hodge classes, not merely local regularity;
- cycle-class compatibility;
- algebraic-cycle/Chow existence;
- lifting correctness.

Do not use harmonic representatives or known Hodge decomposition to define the source.

No automatic H1 start.

---

## 14. Prior-art / novelty firewall

Explicitly classify as prior art/control where applicable:

- Kähler differentials;
- Jacobian coordinate transport;
- algebraic de Rham forms;
- pole divisors/principal parts;
- linear algebra / module reduction;
- automaton/future-equivalence quotienting.

`PRIOR_ART_IS_NOT_A_NEGATIVE_R2_GATE` remains frozen.

The issue is attribution, not originality.

---

## 15. Required artifacts

At minimum produce:

1. `research_results/HODGE_H0F_ALGEBRAIC_SOURCE_SPEC.json`
2. `research_results/HODGE_H0F_PARAMETER_REGISTRY.json`
3. `research_results/HODGE_H0F_DIFFERENTIAL_TRANSITION_DERIVATION.json`
4. `research_results/HODGE_H0F_ALGEBRAIC_GENERATION_REPLAY.json`
5. `research_results/HODGE_H0F_MULTISTEP_SOURCE_REGISTRY.json`
6. `research_results/HODGE_H0F_ALGEBRAIC_BASELINE_SANDWICH.json`
7. `research_results/HODGE_H0F_SOURCE_NORMAL_FORM_REGISTRY.json`
8. `research_results/HODGE_H0F_SUFFIX_QUOTIENT_REGISTRY.json`
9. `research_results/HODGE_H0F_COMPARISON_THEOREM_REGISTRY.json`
10. `research_results/HODGE_H0F_PROOF_LEVERAGE_CERTIFICATE_REGISTRY.json`
11. `research_results/HODGE_H0F_ATTRIBUTION_CERTIFICATE_REGISTRY.json`
12. `research_results/HODGE_H0F_MIXING_CANCELLATION_CONTROLS.json`
13. `research_results/HODGE_H0F_BASELINE_GAMING_CONTROL.json`
14. `research_results/HODGE_H0F_PRESENTATION_NATURALITY_LEDGER.json`
15. `research_results/HODGE_H0F_PRIOR_ART_NOVELTY_LEDGER.json`
16. `research_results/HODGE_H0F_TARGET_LEAKAGE_LEDGER.json`
17. `research_results/HODGE_H0F_HODGE_R3_PREINTERFACE.json`
18. `research_results/HODGE_H0F_CLASSIFICATION.json`
19. `research_results/HODGE_H0F_SEMANTIC_CHECKPOINT.md`
20. deterministic checker + output;
21. manifest with SHA-256 digests.

---

## 16. Mandatory checker gates

At minimum verify:

- source table generated from exact `P^2 / Omega^1(m)` formulas;
- no H0D/H0E table copied;
- parameter/seed registry frozen before success counts;
- non-diagonal differential transition replay passes;
- inverse/composition identities checked on declared overlaps;
- mixed/cancellation controls present;
- `B_raw^alg` and `B_std^alg` both frozen;
- source-native normal-form search recorded;
- no post-hoc weakening of `B_std^alg`;
- quotient correctness/coarsest sufficiency;
- strict measure predeclared;
- attribution against both baselines;
- prior art does not decide R2;
- coordinate permutation/basis-change scope explicit;
- target leakage PASS;
- no Hodge proof claim;
- H1 remains blocked.

Checker PASS means protocol/exact-source consistency only unless the classification explicitly passes robust attributed R2.

---

## 17. Allowed final dispositions

Freeze exactly one strongest disposition:

### `H0F_ROBUST_ATTRIBUTED_R2_ON_ALGEBRAIC_KAHLER_SOURCE`

Actual `P^2 / Omega^1(m)` source is generated algebraically and an Enterprise quotient/operation passes robust transform attribution against both fair baselines.

### `H0F_R1_SOURCE_NORMAL_FORM_ALREADY_COMPLETE`

Actual differential-form source exists and Enterprise quotient is exact, but a fair source-native algebraic normal form already supplies the same theorem-critical interface.

### `H0F_R1_MIXING_PRESENT_NO_STRICT_LEVERAGE`

Non-diagonal/cancellation source is genuine, but no strict V2 leverage survives.

### `H0F_FAIL_ALGEBRAIC_SOURCE_GENERATION`

The declared finite differential-form source cannot be generated exactly without illicit/synthetic structure.

### `H0F_ATTRIBUTION_UNRESOLVED`

A concrete baseline/normal-form ambiguity remains; freeze the exact missing object.

No other disposition without Driver review.

---

## 18. Advancement vector

Before H0F:

- Criterion V2: `FROZEN`;
- attribution addendum: `FROZEN`;
- abstract robust attributed R2: `FOUND` in H0D;
- scalar toric algebraic instantiation: `R1 / source-inherited` in H0E;
- actual algebraic differential-form attributed R2: `OPEN`;
- R3: `NOT FOUND`;
- H1: `NOT ADMISSIBLE`.

Expected advancement:

`algebraic-source complexity +30 / non-diagonal mixing +35 / attribution stress +30 / Hodge adjacency +15 / R3 +0 unless preinterface only / H1 +0`.

---

Driver return target:

`EM-DVR-HODGE-4Q7M2K / HODGE_CONTROL_PLANE`

Do not automatically start any later stage.