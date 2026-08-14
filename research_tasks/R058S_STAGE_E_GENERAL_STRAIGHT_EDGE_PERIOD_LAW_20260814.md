# R058S Stage E — General Straight-Edge Period Law and Adaptive Exact Collapse

Researcher-ID: `EM-R058S-7C91E4`

Generation: `RS-R058S-EXACT-SQUARE-COLLAPSE-GRAMMAR-DISCOVERY`

Driver-ID: `EM-DVR-R0457K / CONTROL_PLANE`

## Frozen parents

Stage D reviewed source head:

`4ea462388f5a455ae3f9290bec4f372884abf0b7`

Freeze and preserve immutable:

- `R058S_STAGE_D_PRIMITIVE_PERIOD_THEOREM_CHECKPOINT_SHA256 = bb8d9b5464732b88cf3873a272429ed435e0ceedcc2e04e6c7760d6193dad1d7`
- `R058S_STAGE_C_STRAIGHT_EDGE_DENSITY_CHECKPOINT_SHA256 = 22f285cc876ce9624200a1ff4d58b910a7d698c1d0fbb0ec455409396fd809bb`
- `R058S_STRAIGHT_EDGE_PERIODIC_PROTOCOL_SHA256 = acf22b9d2f256b0dccfa210abce69e2e994205a39d19bc3bed945026d75e78b9`
- all Stage 0/A/B1/B2 frozen bytes and hashes.

## Purpose

Stage D proved an abstract periodic-path whole-chord theorem and localized finite straight sides to exact complete periods plus bounded tails/corner layers.

Stage C/D also expose the following exact pattern on the eight frozen primitive tangent classes.  If a primitive axial tangent is `t=(a,b)`, define

`H_hex(t) = max(|a|, |b|, |a+b|)`.

For all eight frozen tangent classes the primitive exposed-edge period satisfies

`m(t) = 2 H_hex(t) = |a| + |b| + |a+b|`.

Stage E asks whether this is an exact carrier theorem for every primitive triangular-lattice tangent, not merely an eight-sample coincidence.

The scientific target is a general straight-edge collapse law:

`primitive digital straight period -> one endpoint chord`

with an adaptive, carrier-derived period length rather than a fixed empirical `K`.

## Epistemic status

`PROOF / EXACT STRUCTURAL ANALYSIS`.

Bounded enumeration may be used only as an independent theorem checker.  It is not a search, fit, or empirical square-prediction stage.

## Hard prohibitions

Do not:

- refit any coefficient;
- run a teacher-loss optimizer;
- invent a square-error-selected grammar/predicate/operator;
- modify B1/B2/C/D frozen bytes;
- consume the square holdout;
- generate rectangle/cube/circle/pi tasks or data;
- use any R057 fitted prior;
- do empirical `K>8` square prediction/ranking;
- tune a period law against the eight frozen tangents;
- claim a general theorem from bounded enumeration alone.

The adaptive period-collapse operator may be specified semantically after proof, but must remain **undeployed** in Stage E.

---

## LANE E0 — REPRODUCTION GATE

Reproduce:

1. Stage-D checkpoint hash and 451/451 checker status;
2. Stage-C checkpoint/protocol hashes and 6451/6451 checker status;
3. the eight frozen primitive tangent records:

`(1,0), (-1,2), (3,1), (-5,7), (2,1), (-4,5), (3,2), (-7,8)`

up to their frozen signs/orientations;

4. frozen primitive edge periods:

`m = (2,4,8,14,6,10,10,16)`.

Mismatch => `HARD_STOP_PARENT_DRIFT`.

---

## LANE E1 — GENERAL PRIMITIVE TANGENT / NORMAL ALGEBRA

Let

`t=(a,b) in Z^2`, `gcd(|a|,|b|)=1`, `t != 0`.

Use the frozen triangular-lattice form

`beta((a,b),(c,d)) = 2ac + ad + bc + 2bd`

and

`Q(a,b)=a^2+ab+b^2`.

Work with the exact un-reduced perpendicular

`n0=(a+2b, -(2a+b))`.

Prove exactly:

1. `beta(t,n0)=0`;
2. for `x=(x1,x2)`,
   `beta(x,n0)=3(b x1 - a x2)`;
3. because `gcd(|a|,|b|)=1`,
   `beta(Z^2,n0)=3 Z`;
4. `ker_Z beta(.,n0) = Z t`.

Therefore `t` is the primitive lattice translation along the digital straight boundary defined by the half-plane normal `n0`.

Handle signs and zero coordinates explicitly; no generic-position assumption.

---

## LANE E2 — EXPOSED VORONOI EDGE ORBIT COUNT

Use the frozen six triangular-lattice nearest-neighbor directions.  For neighbor direction `e_j`, let

`w_j = beta(e_j,n0)`.

From the exact half-plane exposure condition, prove that the number of exposed Voronoi-edge translation orbits of type `j` in one primitive `t`-period is

`max(w_j,0)/3`.

Derive the six support increments explicitly as the signed pair set

`{+/- 3a, +/- 3b, +/- 3(a+b)}`

up to the frozen neighbor-code convention.

Then prove

`m(t) = sum_{w_j>0} w_j/3`

and hence

`m(t) = |a| + |b| + |a+b|`.

Prove the axial identity

`|a| + |b| + |a+b| = 2 max(|a|,|b|,|a+b|)`.

Freeze the theorem status only if the derivation is complete:

`TRIANGULAR_VORONOI_STRAIGHT_PERIOD_LENGTH_THEOREM_PROVED`.

Also record the exact edge-type multiplicities in one primitive period.

---

## LANE E3 — PERIODIC BOUNDARY CYCLE / MINIMALITY

Prove, or honestly delimit if proof fails, that for the frozen center-in-half-plane Voronoi digitization:

1. the exposed boundary modulo translation by `t` is one oriented cycle;
2. that cycle contains exactly `m(t)` exposed edges;
3. lifting once gives endpoint displacement exactly `t`;
4. `t` is the minimal nonzero translational period;
5. the minimal edge-word period is also `m(t)`.

Do not infer word-period minimality merely from eight examples.  If an implication needs an extra lemma, state and prove it.

If minimal edge-word period is not established generally, distinguish:

- `TRANSLATIONAL_PERIOD_LENGTH_PROVED`
- `EDGE_WORD_MINIMAL_PERIOD_NOT_PROVED`.

---

## LANE E4 — GENERAL ADAPTIVE WHOLE-CHORD LAW

Combine Stage-D Theorem D1.A with the Stage-E carrier period theorem.

For every primitive tangent `t=(a,b)`, define

`m(t)=|a|+|b|+|a+b|`.

Prove that an aligned `m(t)`-edge primitive digital straight period collapses by whole chord to

`sqrt(Q(t))`

exactly.

More generally, for `k=q m(t)`, prove the frozen all-period estimator is exact.

State clearly:

`m|k` is sufficient in the abstract periodic theorem, not necessary in arbitrary periodic polygonal paths.

If you additionally prove a carrier-specific converse, isolate its assumptions and proof.  Do not promote the Stage-C 56/56 observation to a converse without proof.

Candidate theorem status:

`ADAPTIVE_PRIMITIVE_PERIOD_WHOLE_CHORD_STRAIGHT_EDGE_LAW_PROVED`.

---

## LANE E5 — D6 / SCALE / PRIMITIVE-REDUCTION SEMANTICS

Prove exact covariance under the corrected spatial D6 action:

- `Q(t)` invariant;
- `H_hex(t)` invariant;
- `m(t)` invariant;
- whole-period endpoint-chord length invariant.

For nonprimitive `u=r t` with primitive `t`, distinguish:

- geometric translation vector `u`;
- primitive carrier period `t`;
- repetition count `r`.

Do not redefine the primitive period as `m(u)` without reduction.  Record the exact reduction rule.

---

## LANE E6 — RAW DIGITAL DENSITY COROLLARY

Each exposed Voronoi edge has frozen physical length `1/sqrt(3)`.

Derive the exact raw digital perimeter per primitive period:

`L_raw(t) = m(t)/sqrt(3)`.

Teacher straight translation length is

`L_teacher(t)=sqrt(Q(t))`.

Therefore derive the raw carrier anisotropy factor

`rho_raw(t) = m(t) / sqrt(3 Q(t))`.

Prove its exact relation to the adaptive period-collapse law, and state what is and is not orientation independent.

This is a corollary, not a fitted correction coefficient.

---

## LANE E7 — INDEPENDENT EXACT CHECKER

Before running the checker, freeze its bounded domain in the output protocol/check metadata.

Use a deterministic theorem-check domain such as all primitive axial tangents satisfying

`H_hex(t) <= 32`

modulo or including full signs/D6 as convenient, provided the choice is declared before results are read.

For every checked tangent independently reconstruct the exact half-plane Voronoi quotient boundary and verify:

- orthogonality;
- image subgroup / primitive kernel;
- translation `t`;
- quotient-cycle closure;
- exposed edge count;
- `m(t)=|a|+|b|+|a+b|`;
- edge-type multiplicities;
- exact whole-period endpoint displacement;
- exact whole-period chord length `sqrt(Q(t))`;
- D6 covariance on a deterministic subset or full bounded domain.

This checker validates implementation and proof bookkeeping only.

No square corpus or holdout is needed.

---

## LANE E8 — FROZEN EIGHT-TANGENT BACK-CHECK

Reproduce the Stage-C eight classes from the general formula:

`m=(2,4,8,14,6,10,10,16)`.

Reproduce the Stage-D 56-pair divisibility consistency audit without changing its interpretation.

Explicitly separate:

- theorem: general period-multiple exactness;
- theorem: general carrier period-length formula if proved;
- frozen finite observation: Stage-C exactness iff divisibility on those 56 pairs;
- false statement: divisibility is necessary for every abstract periodic path.

---

## LANE E9 — UNDEPLOYED GENERATOR SPEC

Only after the proofs are frozen, write a semantic specification for

`ADAPTIVE_PRIMITIVE_PERIOD_WHOLE_CHORD`

whose mathematical input is a carrier-intrinsic primitive straight-boundary period `(word, t)` and whose output is its endpoint chord.

Required fields:

- domain;
- primitive-period detection assumptions;
- `m(t)` formula;
- endpoint displacement semantics;
- exact output length;
- D6 behavior;
- reversal behavior;
- scale/primitive reduction behavior;
- failure / not-applicable conditions;
- provenance.

Mark:

`POST_STAGE_D_GENERAL_EDGE_LAW_OPERATOR_SPEC / UNDEPLOYED`.

Do not apply it to square discovery or holdout in Stage E.

---

## Required artifacts

At minimum:

1. `R058S_GENERAL_STRAIGHT_EDGE_PERIOD_THEOREM.md`
2. `R058S_GENERAL_PERIOD_LENGTH_FORMULA.json`
3. `R058S_GENERAL_PERIOD_EDGE_TYPE_LEDGER.json`
4. `R058S_GENERAL_EDGE_THEOREM_CHECK_RESULTS.json`
5. `R058S_ADAPTIVE_PRIMITIVE_PERIOD_COLLAPSE_SPEC.json`
6. `R058S_STAGE_E_GENERAL_EDGE_LAW_CHECKPOINT.json`
7. compact artifact hash manifest.

Return at least:

- `R058S_GENERAL_STRAIGHT_EDGE_PERIOD_THEOREM_SHA256`
- `R058S_GENERAL_PERIOD_LENGTH_FORMULA_SHA256`
- `R058S_GENERAL_EDGE_THEOREM_CHECK_RESULTS_SHA256`
- `R058S_ADAPTIVE_PRIMITIVE_PERIOD_COLLAPSE_SPEC_SHA256`
- `R058S_STAGE_E_GENERAL_EDGE_LAW_CHECKPOINT_SHA256`
- exact source head.

Then STOP for Driver review.

## Allowed final statuses

Use only statuses justified by proof/checks, including:

- `TRIANGULAR_VORONOI_STRAIGHT_PERIOD_LENGTH_THEOREM_PROVED`
- `ADAPTIVE_PRIMITIVE_PERIOD_WHOLE_CHORD_STRAIGHT_EDGE_LAW_PROVED`
- `RAW_DIGITAL_STRAIGHT_DENSITY_FORMULA_PROVED`
- `TRANSLATIONAL_PERIOD_LENGTH_PROVED`
- `EDGE_WORD_MINIMAL_PERIOD_PROVED`
- `EDGE_WORD_MINIMAL_PERIOD_NOT_PROVED`
- `GENERAL_EDGE_LAW_PARTIAL`
- `CORNER_GENERATOR_STILL_OPEN`

Do not call the undeployed operator canonical for arbitrary shapes.
