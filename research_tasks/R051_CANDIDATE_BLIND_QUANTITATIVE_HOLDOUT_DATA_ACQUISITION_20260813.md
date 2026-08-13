<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R051-CANDIDATE-BLIND-QUANTITATIVE-HOLDOUT-DATA-ACQUISITION",
  "title": "R051 Candidate-Blind Quantitative Holdout Data Acquisition",
  "kind": "RESEARCH",
  "owner": "program/foundational-logic-engineering-inversion",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "QUANTITATIVE_EVALUATION_ELIGIBILITY / CANDIDATE_BLIND_HOLDOUT",
  "frontier": "Upgrade the candidate-blind R049 engineering surface from structural holdout definitions to source-grounded condition-indexed quantitative observations with frozen construction/holdout splits, without opening or adapting to G2 candidates.",
  "next_action": "Verify the frozen R049 target, freeze data-acquisition/eligibility rules before source search, then obtain authoritative numerical observations or transparently replace a row with a new candidate-blind protocol only when the original row cannot support quantitative holdout.",
  "dependencies": [
    {
      "target": "R049 Draft PR #540 @ 220aa5647389386d6c953e6aa04f32769f90f490",
      "action": "VERIFY_AND_CONSUME_FROZEN_ENGINEERING_SURFACE",
      "satisfied": true
    },
    {
      "target": "R049 target SHA-256 e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c",
      "action": "RECOMPUTE_BEFORE_ANY_EXTERNAL_DATA_ACQUISITION",
      "satisfied": true
    },
    {
      "target": "Foundational Logic V1 / Native-Semantics Gate V3",
      "action": "CONSUME_AS_GOVERNING_SEMANTICS",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R049 frozen target surface only",
    "authoritative/primary engineering measurement sources and official supplementary data"
  ],
  "evidence_status": "CANDIDATE_BLIND_QUANTITATIVE_HOLDOUT_CONSTRUCTION",
  "hard_block": null,
  "tags": [
    "R051",
    "candidate-blind",
    "quantitative-holdout",
    "engineering-data",
    "evaluation-eligibility",
    "source-grounded",
    "anti-cherry-pick"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R051",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R051 — Candidate-Blind Quantitative Holdout Data Acquisition

Status: `READY / P0 / CANDIDATE-BLIND QUANTITATIVE EVALUATION PACKET / CALIBRATION FORBIDDEN / NOT CANONICAL`

## 0. Mother question

R050 completed a valid candidate-blind out-of-sample **structural** screen, but Stage 0 determined before candidate access that every R049 row lacked enough condition-separated numerical observations/raw arrays to support an independently recomputable construction/holdout residual. Therefore `E4=0` in R050 is an evaluation-eligibility result, not a quantitative failure of G2.

R051 asks only:

> Can the engineering target side be upgraded, while still candidate-blind, into an auditable quantitative holdout packet containing real source-grounded observations, frozen construction/holdout splits and uncertainty/residual rules sufficient for later E3/E4 testing?

R051 does **not** calibrate, rank, inspect or repair any candidate.

## 1. Strict candidate-blind isolation

Before the R051 quantitative target is frozen, forbidden to read or consume:

- R048 PR #539 candidate definitions, names, theorems, counterexamples, hashes or internal structure;
- R050 PR #541 row/pressure matrices, candidate bridge mappings, candidate debt vectors, Pareto observations or candidate-specific failure analysis;
- any G1/G2 candidate score, ranking or bridge success/failure;
- any prompt/history summary that identifies which candidate performed well or poorly on which pressure;
- classical pi numerical value as a target-design or row-selection signal.

Allowed project inputs:

1. Foundational Logic V1;
2. Native-Semantics Gate V3;
3. R049 Draft PR #540 exact head `220aa5647389386d6c953e6aa04f32769f90f490`;
4. R049 frozen target surface and source registry only;
5. this taskbook.

If incidental candidate information appears in unavoidable context/tool metadata, record `CONTEXT_CONTAMINATION_RISK`, quarantine it, and do not use it to select sources, rows, splits, tolerances or replacements.

## 2. Stage 0 — freeze acquisition and eligibility protocol before searching for numbers

First recompute and verify R049 target SHA-256:

`e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c`

Then, **before looking for any new numerical dataset or table**, create and freeze:

`R051_DATA_ACQUISITION_PROTOCOL.json`

It must define at minimum:

- source priority order;
- admissible numerical evidence forms;
- inadmissible evidence forms;
- row-preservation versus replacement rules;
- construction/holdout split rule;
- uncertainty propagation rule;
- missing-data disposition;
- plot-digitization policy;
- duplicate/training-source collision policy;
- exact target-hash algorithm;
- anti-cherry-pick rule.

Freeze and report its SHA-256 before data acquisition begins.

### 2.1 Source priority

Use, in order of preference:

1. official machine-readable supplementary data from the protocol owner/source institution;
2. official tabulated values in primary measurement publications/technical reports;
3. official archival CSV/TXT/JSON/HDF5 or equivalent data repository linked by the primary source;
4. primary-source appendices containing condition-indexed numerical observations;
5. only if explicitly justified, source-native tables embedded in a PDF.

### 2.2 Inadmissible for E4 target construction

The following may not create an E4-eligible row:

- invented synthetic observations;
- numbers inferred only from prose without condition-indexed measurements;
- arbitrary tolerance chosen by the researcher;
- calculated model outputs presented as measured outputs;
- manual visual graph digitization without a source-supplied numerical table/data file;
- extracting a classical formula curve and treating it as empirical data;
- using candidate behavior to decide which measurement conditions become construction or holdout;
- selecting only conditions where a candidate later performs well.

If only plot images exist, record `PLOT_ONLY_NOT_E4_ELIGIBLE` unless an official numerical supplement is found.

## 3. Target pressure surface

Attempt quantitative data acquisition for all six frozen pressure families:

1. `GEOMETRIC_MEASURE_COHERENCE`
2. `CYCLE_CLOSURE_AND_RELATIVE_PHASE`
3. `DIFFUSIVE_RELAXATION`
4. `BOUNDED_MODE_SPECTRUM`
5. `TRANSFER_INVENTORY_BALANCE_CLOSURE`
6. `SOURCE_RECEIVER_INTERCHANGE_RECIPROCITY`

The starting empirical rows are exactly the eight R049 frozen rows:

- `A1-GMC-M48-STEP-GAGE`
- `A2-CCRP-PMU-PHASE`
- `A3-DR-FDTR-PUMP-PROBE`
- `A4-BMS-CAVITY-VNA`
- `B1A-TIBC-LIQUID-GRAVIMETRIC`
- `B1B-TIBC-GAS-PVTT`
- `B2A-SRIR-MIC-RECIP`
- `B2B-SRIR-ANTENNA-3PAIR`

## 4. Preserve-first rule; replacement only when numerically impossible

For each R049 row, first attempt to find source-grounded condition-indexed measured data for the **same frozen protocol and measured-output definition**.

If adequate data exist, retain the row identity and mark:

`R049_ROW_NUMERICALLY_UPGRADED`

If adequate data do not exist after a documented source search, do **not** fabricate or reconstruct them. Mark:

`SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT`

A replacement row may then be searched **candidate-blind** for the same pressure family only if it satisfies all of the following:

- materially independent engineering protocol with real measured observations;
- source-grounded numerical data accessible in machine-readable or tabulated form;
- measured output is not merely a calculated descendant;
- source-stated uncertainty/error model is available;
- construction/holdout split can be frozen before calibration;
- no candidate information was consumed in choosing it.

Any replacement is a **new R051 holdout generation row**, not a mutation of R049. Preserve both R049 provenance and replacement provenance.

## 5. Required quantitative row schema

Every row claimed `E4_ELIGIBLE_TARGET` must freeze:

- row ID;
- pressure family;
- protocol;
- apparatus;
- controlled input/intervention variable(s);
- condition index/key;
- measured-output carrier and exact units/representation;
- measured numerical values;
- per-observation uncertainty, covariance, or source-defined error model;
- source provenance including exact table/file/appendix location;
- extraction method;
- whether values are raw observations or source-processed measurements;
- calculated outputs explicitly excluded;
- construction subset indices;
- holdout subset indices;
- split-generation rule;
- residual definition allowed for later calibration;
- PASS/FAIL rule using only source-stated uncertainty/tolerance semantics;
- any realization-specific metrology constants, listed separately;
- licensing/redistribution note if relevant; do not reproduce copyrighted tables beyond what is necessary for auditable factual data fields.

Do not copy long copyrighted text. Numerical facts and short labels only.

## 6. Construction/holdout split discipline

The split must be frozen before any candidate access.

Acceptable split examples:

- predeclared disjoint condition ranges;
- alternating or hashed condition IDs independent of measured values;
- one physical realization as construction and a second independent realization as holdout;
- source-defined calibration subset versus validation subset when genuinely independent.

Forbidden:

- split by residual magnitude;
- split after seeing candidate predictions;
- moving failed conditions into construction;
- using the same measured observations for parameter estimation and holdout scoring.

The split rule itself must be deterministic and machine-checkable.

## 7. Special requirements for Block B

### 7.1 TRANSFER_INVENTORY_BALANCE_CLOSURE

Target realizations:

- liquid dynamic-gravimetric;
- gas PVTt.

To make the pressure E4-eligible later, obtain enough quantitative observations that at least one of these tests is possible:

- liquid construction -> gas holdout;
- gas construction -> liquid holdout;
- preferably both directions.

Any realization-specific conversion/metrology constants must be frozen separately as calibration debt.

Do not insert classical control-volume balance as a native axiom. The target side may of course retain the actual measured inventory/transfer quantities and metrology conventions.

### 7.2 SOURCE_RECEIVER_INTERCHANGE_RECIPROCITY

Target realizations:

- microphone reciprocity;
- three-antenna reciprocity/extrapolation.

For later E4 eligibility, freeze directed-pair measurements under role interchange/permutation with enough condition-indexed numerical values to test one bridge form across realizations.

Do not convert an acoustic/electromagnetic reciprocity theorem into native premises. R051 only freezes empirical target observations.

## 8. Data extraction and uncertainty discipline

- Preserve source units and source uncertainty semantics in the authoritative packet.
- Unit-normalized copies may be derived, but original source values remain authoritative.
- If covariance matrices are supplied, preserve them.
- If only standard deviations are supplied, do not invent correlations.
- If uncertainty varies by condition, store it per condition.
- If a source supplies only a global expanded uncertainty, record exactly that limitation.
- If source data are rounded, record displayed precision; do not add digits.
- Do not use OCR unless no structured text/table extraction exists; OCR-derived numeric arrays are not automatically E4-eligible and require exact cross-check against the source.

## 9. Required kill tests

R051 must attack and machine-record at least:

- `CANDIDATE_INFORMATION_USED_FOR_DATA_SELECTION`
- `CONSTRUCTION_HOLDOUT_SPLIT_AFTER_CANDIDATE_ACCESS`
- `PLOT_DIGITIZATION_AS_RAW_DATA`
- `MODEL_CURVE_AS_EMPIRICAL_OBSERVATION`
- `CALCULATED_OUTPUT_AS_MEASUREMENT`
- `TOLERANCE_INVENTED_WITHOUT_SOURCE`
- `SAME_OBSERVATION_USED_FOR_FIT_AND_HOLDOUT`
- `UNIT_CONVERSION_DOUBLE_COUNT`
- `SOURCE_TABLE_ROUNDING_IGNORED`
- `BLOCK_B_ONE_REALIZATION_ONLY_PROMOTED_TO_E4`
- `TRAINING_SOURCE_COLLISION_NOT_AUDITED`
- `TARGET_MUTATION_AFTER_FREEZE`
- `CLASSICAL_PI_NUMERIC_SELECTION`

## 10. Required artifacts

Return at minimum:

- `R051_REPORT.md`
- `R051_DATA_ACQUISITION_PROTOCOL.json`
- `R051_R049_ROW_DATA_AVAILABILITY.json`
- `R051_QUANTITATIVE_ENGINEERING_ATLAS.json`
- `R051_CONSTRUCTION_HOLDOUT_SPLITS.json`
- `R051_UNCERTAINTY_LEDGER.json`
- `R051_METROLOGY_CONSTANT_LEDGER.json`
- `R051_REPLACEMENT_ROW_LEDGER.json`
- `R051_SOURCE_REGISTRY.json`
- `R051_SOURCE_REGISTRY.md`
- `R051_TARGET_LEAKAGE_AUDIT.json`
- `R051_ADVERSARIAL_TEST_RESULTS.json`
- `R051_QUANTITATIVE_HOLDOUT_MANIFEST.json`
- exact checker/tests.

The manifest must list every authoritative target file and exact byte SHA-256, then freeze a single aggregate:

`R051_QUANTITATIVE_TARGET_SHA256`

## 11. Eligibility output

For every empirical row, output exactly one:

- `E4_ELIGIBLE_TARGET`
- `E3_ONLY_CONSTRUCTION_DATA_NO_INDEPENDENT_HOLDOUT`
- `STRUCTURAL_ONLY_NO_NUMERIC_OBSERVATIONS`
- `SOURCE_INSUFFICIENT_FOR_QUANTITATIVE_HOLDOUT`
- `PLOT_ONLY_NOT_E4_ELIGIBLE`
- `REPLACED_BY_NEW_CANDIDATE_BLIND_ROW`

Do not force an E4-eligible count.

A valid R051 return may have zero E4-eligible rows if authoritative data genuinely cannot be obtained. That is an evaluation-data availability result, not permission to invent data.

## 12. No calibration in R051

Strictly forbidden:

- opening G2 candidate content;
- scoring any candidate;
- choosing bridges for a candidate;
- ranking native mechanisms;
- declaring E3/E4/E5 for a candidate;
- generating G3 repairs.

R051 ends when the quantitative target packet is frozen.

## 13. Desired return classes

Preferred:

`CANDIDATE_BLIND_QUANTITATIVE_HOLDOUT_PACKET_FROZEN / NUMERICAL_E4_ELIGIBILITY_ESTABLISHED_FOR_AT_LEAST_ONE_PRESSURE / CALIBRATION_NOT_RUN / NOT_CANONICAL`

Also valid:

`CANDIDATE_BLIND_QUANTITATIVE_HOLDOUT_PACKET_FROZEN / NO_SOURCE_GROUNDED_E4_ELIGIBLE_ROWS_FOUND / CALIBRATION_NOT_RUN / NOT_CANONICAL`

or a mixed partial-eligibility return.

## 14. Foundation rule

Keep this top-level principle explicit throughout:

`Definition is not inherited. Success is evidence. Explain the success from a smaller native logic.`

R051 improves the **evidence surface** only. It does not define native mathematics.
