# R050 — G2 Out-of-Sample Engineering Calibration Report

**Researcher-ID:** `EM-R050-93B6E2`  
**Task:** `RS-R050-G2-OUT-OF-SAMPLE-ENGINEERING-CALIBRATION`  
**Status:** `COMPLETE / DRAFT / NOT_CANONICAL`  
**Return class:** `G2_OUT_OF_SAMPLE_CALIBRATION_COMPLETE / NO_E4_E5 / FAILURE_DEBTS_FROZEN / NO_STRICT_WINNER / NOT_CANONICAL`

## 1. Executive result

R050 completed the required first G2 target-side calibration pass without modifying any G2 candidate core.

Stage 0 blind scoring freeze passed. The ten authoritative R049 target artifacts were fetched from Draft PR #540 exact head `220aa5647389386d6c953e6aa04f32769f90f490`; each exact-file-byte SHA-256 was independently recomputed and matched the frozen manifest. The aggregate target hash recomputed exactly as:

`e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c`

Before any R048 candidate content was opened, `R050_SCORING_PROTOCOL.json` was frozen with SHA-256:

`322f2e4ba66b4fbc8e47a513867399f9464a62a629af01f23cad6929d7c1d66b`

Only after that freeze was the R048 G2 candidate set opened from Draft PR #539 exact head `58eaac9aa2d407d682c05bdd67ada8aded5fb642`. Its canonical candidate-set SHA-256 recomputed exactly as:

`2e1f85a3faf37a0525364c220f9449caea45408bf6a954c09045bf78646cf959`

All six per-candidate freeze hashes matched. `CORE_EDIT_COUNT=0`. Recomputing the R049 target hash after candidate opening produced the same target hash, so the target was not mutated after exposure.

The required matrices are complete:

- 6 candidates × 8 frozen empirical rows = **48 row-level cells**
- 6 candidates × 6 pressure families = **36 pressure-level cells**
- row-level evidence counts: **E0 = 14, E1 = 30, E2 = 4, E3 = 0, E4 = 0, E5 = 0**
- no B3 cell was promoted above E1
- every B4 mapping was rejected
- fitted calibration parameters: **0**
- weighted total score: **not used**

The decisive Stage-0 fact is evaluation-side: R049 freezes protocols, measured-output carriers, scale regimes and source uncertainty envelopes, but does **not** freeze condition-separated numerical measured-output values/raw arrays from which a candidate-specific construction/holdout residual can be independently recomputed. Therefore all eight rows were frozen as `NOT_ELIGIBLE_FOR_E4`; under this packet the maximum legal evidence is E2. This ceiling was fixed before candidate access, so the absence of E4/E5 cannot be interpreted as a G2-mechanism failure.

## 2. Stage 0 blind scoring freeze

The scoring protocol fixed, before candidate access:

1. row eligibility and source uncertainty semantics;
2. legal physical-to-native encoding;
3. legal native-to-output readout;
4. B0/B1/B2/B3/B4 bridge semantics;
5. E0–E5 evidence semantics;
6. fitted-parameter declaration and construction-only estimation rule;
7. holdout split requirements;
8. Block-B two-realization transfer rule;
9. pressure aggregation without averaging;
10. strict-dominance-only winner rule;
11. all twelve required target-leakage attacks.

The frozen quantitative ceiling is not a later excuse. It is part of the Stage-0 hash-frozen scoring protocol.

### 2.1 Frozen row eligibility

| Frozen row | Pressure | Source envelope kind | E4 eligibility | Frozen reason |
|---|---|---|---|---|
| `A1-GMC-M48-STEP-GAGE` | GMC | `expanded_uncertainty_formula` | `NOT_ELIGIBLE_FOR_E4` | No condition-separated numerical measured-output array frozen in R049. |
| `A2-CCRP-PMU-PHASE` | CCRP | `source_setting_expanded_uncertainty` | `NOT_ELIGIBLE_FOR_E4` | No condition-separated numerical measured-output array frozen in R049. |
| `A3-DR-FDTR-PUMP-PROBE` | DR | `raw_phase_standard_deviation` | `NOT_ELIGIBLE_FOR_E4` | No condition-separated numerical measured-output array frozen in R049. |
| `A4-BMS-CAVITY-VNA` | BMS | `source_defined_curve_noise_and_estimator_envelope` | `NOT_ELIGIBLE_FOR_E4` | No condition-separated numerical measured-output array frozen in R049. |
| `B1A-TIBC-LIQUID-GRAVIMETRIC` | TIBC | `expanded_uncertainty` | `NOT_ELIGIBLE_FOR_E4` | No condition-separated numerical measured-output array frozen in R049. |
| `B1B-TIBC-GAS-PVTT` | TIBC | `expanded_uncertainty` | `NOT_ELIGIBLE_FOR_E4` | No condition-separated numerical measured-output array frozen in R049. |
| `B2A-SRIR-MIC-RECIP` | SRIR | `frequency_dependent_expanded_uncertainty` | `NOT_ELIGIBLE_FOR_E4` | No condition-separated numerical measured-output array frozen in R049. |
| `B2B-SRIR-ANTENNA-3PAIR` | SRIR | `typical_gain_measurement_uncertainty` | `NOT_ELIGIBLE_FOR_E4` | No condition-separated numerical measured-output array frozen in R049. |

E1 and E2 in this report are **not engineering validation**. E1 is qualitative mechanism evidence; E2 is an exact finite structural constraint. E3/E4 require numerical predicted/measured quantities, a declared split, a source uncertainty envelope and a recomputable residual. Those inputs are absent from the frozen target packet.

## 3. Candidate freeze integrity

The six immutable G2 candidates and verified hashes are:

| Candidate | Frozen name | Verified candidate SHA-256 |
|---|---|---|
| G2-M1 | PAIRWISE_EQUALIZATION_REWRITE | `a12bcaa3c6b22366865670513a065b1cf6b9fd95f3941b1e6d13b38becf44f52` |
| G2-M2 | SIGNED_CANCELLATION_LEDGER | `4b4da01eee68c59d683463fbd33b5a36fd36c8ed00456197f96ba3b22e0f1dac` |
| G2-M3 | BINARY_CARRY_RELAY | `ad4ac85dc5dc4463edf0f584e317f23e40aee47d509062803a19309d81ffb6fa` |
| G2-M4 | FINITE_UNION_PROPAGATION | `3830eab3a05532a3df5427a7c24ce15e50f62ae10130b149a432a47094cec85c` |
| G2-M5 | FINITE_REWRITE_ACTION_QUOTIENT | `be5c048b093423b07a1515f7f4b08baf99ef18d3fafceee0979c9fb5e17dee48` |
| G2-M6 | CONSERVATIVE_SWAP_GROUP | `90dfc14872299e611c1949d5784f32ac6f071ca58752609f72b5150d5d9e30ca` |

No candidate definition, name, theorem, counterexample, N0 substrate, N1 operation, N2 readout, parameter list or internal structure was changed.

## 4. Pressure-level calibration result

| Candidate | GMC | CCRP | DR | BMS | TIBC | SRIR |
|---|---:|---:|---:|---:|---:|---:|
| G2-M1 PAIRWISE_EQUALIZATION_REWRITE | E1 | E0 | E1 | E0 | E2 | E1 |
| G2-M2 SIGNED_CANCELLATION_LEDGER | E1 | E0 | E1 | E0 | E1 | E1 |
| G2-M3 BINARY_CARRY_RELAY | E0 | E1 | E0 | E1 | E0 | E0 |
| G2-M4 FINITE_UNION_PROPAGATION | E0 | E0 | E1 | E0 | E1 | E1 |
| G2-M5 FINITE_REWRITE_ACTION_QUOTIENT | E1 | E1 | E1 | E1 | E1 | E1 |
| G2-M6 CONSERVATIVE_SWAP_GROUP | E1 | E1 | E0 | E1 | E2 | E1 |

This table is categorical, not additive. There is no total score and no ranking generated from E0/E1/E2 counts.

### 4.1 GEOMETRIC_MEASURE_COHERENCE

No candidate derives the frozen CMM pairwise-separation coherence statement. M1 and M2 can represent integer discrepancies only after a target-specific coding; M6 has permutation invariants but no separation relation. Any stronger mapping would either become B3 or import effective metric/coordinate content. Maximum evidence: E1.

### 4.2 CYCLE_CLOSURE_AND_RELATIVE_PHASE

M3 has exact finite recurrence and nested rational return periods; M6 has exact finite recurrent group action; M5 can generate recurrent classes after a concrete action is chosen. None derives a target-independent relative timing/phase readout across independent channels. M1/M2/M4 terminate and have no nontrivial recurrence. Maximum evidence: E1.

### 4.3 DIFFUSIVE_RELAXATION

M1, M2 and M4 have genuine finite well-founded relaxation structures and therefore receive E1 mechanism credit. M5 has quotient-level descent only after a concrete target action is selected, so it remains B3/E1. M3 is purely periodic and M6 has a theorem-level no-relaxation obstruction. No candidate derives the frozen modulation-indexed delayed-response curve. Maximum evidence: E1.

### 4.4 BOUNDED_MODE_SPECTRUM

M3's return-period hierarchy, M5's recurrent classes and M6's finite orbits provide only qualitative discrete/recurrent structure. None derives response peaks, widths or retuning under the frozen physical interventions. Turning those internal finite objects into microwave resonance peaks would require a target-specific response adapter or forbidden classical eigenmode machinery. Maximum evidence: E1.

### 4.5 TRANSFER_INVENTORY_BALANCE_CLOSURE

This is the only pressure where exact structural E2 appears.

**G2-M1.** For a supplied receiver subset `R`, define `I_R(x)=Σ_{v∈R}x(v)`. Every legal M1 move internal to `R` or its complement leaves `I_R` unchanged. Every cross-interface move into `R` increments `I_R` by exactly one; every reverse crossing decrements it by exactly one. Telescoping any finite trajectory gives

`ΔI_R = N_in − N_out`.

This follows from the frozen one-token update law and exact conservation; no classical control-volume equation is inserted as a native axiom.

**G2-M6.** For transported label `a`, define `I_R(a)=#{v∈R: λ(v)=a}`. An internal swap leaves `I_R(a)` unchanged. A cross-interface swap changes it by `+1`, `−1` or `0` exactly according to the signed crossing of label `a`; telescoping gives

`ΔI_R(a) = N_in(a) − N_out(a)`.

Again this follows from the frozen swap law plus label multiplicity conservation.

The same structural bridge form is used for both frozen realizations:

- liquid dynamic-gravimetric;
- gas PVTt.

No per-realization semantic refit is introduced. Liquid weighing/buoyancy/timebase/meter constants and gas tank-volume/pressure/temperature/timebase/state-realization constants are separately logged as downstream calibration debt. Because R049 contains no realization-level numerical observations sufficient for a construction/holdout residual, both directions of the preferred A→B and B→A transfer test are `NOT_ELIGIBLE_FOR_E4`.

M2, M4 and M5 receive only E1/B3 because they can represent bookkeeping, nonextensive propagation or a target-chosen action, but do not independently force inventory change to equal transfer. M3 has no conserved carrier and is unmapped.

### 4.6 SOURCE_RECEIVER_INTERCHANGE_RECIPROCITY

M1 and M4 have endpoint-symmetric local laws; M6 has involutive swap symmetry; M2 can represent signed directional discrepancies; M5 can choose role-permutation generators. None possesses a frozen signal-valued readout whose measured value is forced to be compatible under source/receiver interchange. State/action symmetry is therefore not promoted to reciprocity of acoustic or RF transfer measurements. Maximum evidence: E1.

For the microphone and three-antenna realizations the same pressure-level rule is retained, and no realization-specific bridge refit occurs. E4 is unavailable because the frozen packet does not contain the directed numerical pair measurements needed for a residual.

## 5. Bridge and parameter debt

Across 48 row-level cells:

- B0_NATIVE_DIRECT: 0
- B1_UNIFORM_READOUT: 16
- B2_CALIBRATED_METROLOGY_BRIDGE: 0
- B3_TARGET_SPECIFIC_ADAPTER: 18
- B4_ILLEGAL_LEAKAGE: 14

No B2 numerical calibration was actually run because no row is quantitatively eligible. Source metrology dependencies are nevertheless itemized in `R050_METROLOGY_BRIDGE_LEDGER.json` so that realization-specific constants are not hidden or mistaken for native primitives.

The fitted-parameter count is zero for every candidate. M5's abstract generator-family flexibility is not treated as free predictive power: every pressure-specific concrete instantiation remains B3 debt unless independently frozen in a later generation/calibration design.

## 6. Cross-pressure shared state and E5

`E5 = 0` for all six candidates.

Several candidates reuse one native state across more than one qualitative/structural pressure—for example M1's `x` state supports finite relaxation and the exact transfer identity; M6's label state supports recurrence and the exact transfer identity. The scoring protocol explicitly forbids promoting such reuse to E5 without E4 on at least two independent pressure families. `R050_CROSS_PRESSURE_SHARED_STATE.json` records these observations without claiming cross-pressure engineering validation.

## 7. Pareto result

No strict winner exists.

Every candidate has:

- E4 pressure coverage = 0;
- E5 cross-pressure coverage = 0;
- core edits = 0;
- fitted parameters = 0.

The frozen dominance rule requires a strict E4/E5 advantage before lower debt can establish strict dominance. Therefore the strict-dominance graph has no edges and the Pareto family remains:

`[G2-M1, G2-M2, G2-M3, G2-M4, G2-M5, G2-M6]`

The E2 transfer result for M1/M6 is preserved as a non-ranking structural observation only.

## 8. Target leakage and adversarial audit

All required attacks were executed in the returned ledger.

- target mutation after candidate opening: PASS;
- candidate core repair: PASS;
- classical-pi numerical selection: PASS;
- output-definition backfill: PASS;
- B3 promoted to success: PASS;
- training relabeled as holdout: `PASS_WITH_TOOLING_LIMITATION`, preserving the exact R049 status;
- invented tolerance: PASS;
- Block-B per-realization refit: PASS;
- metaphor promoted to quantitative explanation: PASS;
- parameter explosion hidden as calibration: PASS;
- failed row averaged away: PASS;
- cross-pressure shared state asserted without E4: PASS.

No center, native distance/equidistance, radius/circle, Euclidean native geometry, angle/radian/2π-per-cycle, continuum PDE, heat-kernel/Gaussian/Fourier normalization, classical wave/eigenmode formula, classical pi numerical value, control-volume balance axiom, or acoustic/electromagnetic reciprocity theorem was imported into N0/N1.

## 9. Failure inheritance

The smallest independent next debts are frozen in `R050_FAILURE_INHERITANCE.json`.

1. **Evaluation-only numeric holdout debt.** Freeze condition-indexed numerical measured outputs/raw arrays plus uncertainties and a real construction/holdout split before future candidate access.
2. **Calibration/metrology bridge debt.** Freeze target-independent bridge forms while keeping realization-specific constants separately counted.
3. **N1 driven-response debt.** Generate a finite driven-response operation capable of intervention-indexed response without continuum/Fourier/eigenmode imports.
4. **N2 measurable-readout debt.** Derive relative periodic displacement, delayed response, bounded-response and directed-transfer compatibility from native state rather than measured outputs.
5. **N0/N0-definable port/interface/role debt.** Explore source/receiver/interface structures without center/metric/geometry or target-coded labels.
6. **Conservation-relaxation-recurrence coexistence debt.** Seek a low-description finite mechanism containing all three without silently retyping one downstream.
7. **Signal reciprocity readout debt.** Derive a signal-valued role-interchange invariant; endpoint/action symmetry alone is insufficient.

Items that imply a new native mechanism are labeled `NEW_GENERATION_CANDIDATE_FOR_LATER_TASK`. None is written back into G2.

## 10. Exact checker/tests

`check_r050.py` and `test_r050.py` pass locally.

- freeze integrity: 17 checks
- matrix/scoring consistency: 488 checks
- M1 transfer identity bounded regression: 552 checks
- M6 transfer identity bounded regression: 486 checks
- ledgers/audits: 11 checks
- exact checker total: **1554 checks**
- unit tests: **4 / 4 PASS**
- CI: `CI_NOT_REQUIRED_FOR_RESEARCH`

The finite regressions test the algebraic transfer identities; they do not create engineering evidence and do not alter the Stage-0 evidence ceiling.

## 11. Final disposition

R050 is a complete calibration return even though E4/E5 are zero. The result is intentionally negative at the quantitative layer and informative at the structural/debt layer:

- blind scoring freeze preserved;
- target and candidate hashes verified;
- G2 cores immutable;
- 48/48 row cells and 36/36 pressure cells completed;
- no fabricated raw data, tolerance or residual;
- no target-specific per-realization Block-B refit;
- no weighted score;
- no strict winner;
- full Pareto family retained;
- next-generation failure debts extracted without repairing G2.

**Final class:** `G2_OUT_OF_SAMPLE_CALIBRATION_COMPLETE / NO_E4_E5 / FAILURE_DEBTS_FROZEN / NO_STRICT_WINNER / NOT_CANONICAL`
