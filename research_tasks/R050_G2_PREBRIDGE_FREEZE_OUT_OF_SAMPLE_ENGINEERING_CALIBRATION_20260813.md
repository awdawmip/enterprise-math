<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R050-G2-PREBRIDGE-FREEZE-OUT-OF-SAMPLE-ENGINEERING-CALIBRATION",
  "title": "R050 G2 Pre-Bridge Freeze and Out-of-Sample Engineering Calibration",
  "kind": "RESEARCH",
  "owner": "program/foundational-logic-engineering-inversion",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "OUT_OF_SAMPLE_VALIDATION / METROLOGY_BRIDGE / G2",
  "frontier": "Test the six frozen R048 G2 mechanisms against the candidate-blind R049 engineering holdout while preventing target-aware readout/bridge invention: freeze native observable catalogs first, train/freeze any metrology bridges only on legacy R046/R047C surfaces second, and open R049 only after both freezes are immutable.",
  "next_action": "Verify the frozen input lock, execute Stage A pre-bridge observable freeze, execute Stage B legacy-training bridge freeze, then and only then open the exact R049 target and run row-level and pressure-level out-of-sample calibration without editing candidate cores, readouts, bridge grammar, parameters, or target fields.",
  "dependencies": [
    {"target":"research_inputs/r050/R050_FROZEN_INPUT_LOCK_20260813.json @ f90da1e09584d7bc9176d51e8a9a0397e7efeec0","action":"CONSUME_EXACT_LOCK","satisfied":true},
    {"target":"R048 Draft PR #539 head 58eaac9aa2d407d682c05bdd67ada8aded5fb642 / candidate-set 2e1f85a3faf37a0525364c220f9449caea45408bf6a954c09045bf78646cf959","action":"CONSUME_FROZEN_G2_CORES","satisfied":true},
    {"target":"R049 Draft PR #540 head 220aa5647389386d6c953e6aa04f32769f90f490 / target e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c","action":"KEEP_CLOSED_UNTIL_STAGE_C","satisfied":true},
    {"target":"R046 PR #534 head 72b68e49ab22c0d948cd5e5439f5e656a2399d77 + R047C PR #537 head 92d751f49174ec792839938a64d489ac902db11a","action":"LEGACY_TRAINING_SURFACE_ONLY","satisfied":true}
  ],
  "source_refs": ["R048 frozen G2 generation","R046/R047C legacy calibration surface","R049 candidate-blind frozen holdout"],
  "evidence_status": "TRUE_OUT_OF_SAMPLE_ENGINEERING_CALIBRATION",
  "last_progress_ref": "R049 publication checkpoint accepted at PR #540 with exact target hash preserved.",
  "last_progress_at": "2026-08-13T12:40:00+08:00",
  "hard_block": null,
  "tags": ["R050","out-of-sample","G2","metrology-bridge","prebridge-freeze","engineering-holdout","anti-overfit"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R050",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# R050 — G2 Pre-Bridge Freeze and Out-of-Sample Engineering Calibration

Status: `READY / P0 / THREE-STAGE OOS CALIBRATION / R049 TARGET CLOSED UNTIL STAGE C / NOT CANONICAL`

## 0. Mother question

R048 produced six G2 mechanisms after failure-debt factorization but before seeing the R049 holdout. R049 independently froze an engineering holdout before seeing any G2 candidate.

The remaining question is:

> **Can any frozen G2 mechanism acquire a legal, low-debt calibration bridge using only old construction/training evidence, then predict the unseen R049 engineering holdout without target-aware repair?**

A mechanism is not successful because it metaphorically resembles an engineering phenomenon. Out-of-sample success requires an observable/readout grammar frozen before R049 is opened, a bridge trained/frozen without R049, and then an unchanged prediction that meets the frozen R049 protocol/error rule.

## 1. Integrity gate

Before mathematics/calibration:

1. verify `research_inputs/r050/R050_FROZEN_INPUT_LOCK_20260813.json` exactly;
2. verify R048 PR #539 head and G2 candidate-set SHA-256;
3. verify R049 PR #540 head and target SHA-256 **without reading R049 target-bearing files**;
4. record the six frozen G2 core hashes;
5. candidate core edits must remain zero throughout R050.

If any frozen hash differs, stop with `FREEZE_INTEGRITY_FAILURE`.

## 2. Hard sequence — auditable commit ordering

R050 MUST create three chronological checkpoints on one research branch:

### Commit A — PREBRIDGE FREEZE

Complete Stage A and commit its frozen artifacts before reading any R049 target-bearing file.

### Commit B — LEGACY TRAINING BRIDGE FREEZE

Complete Stage B using only frozen G2 + R046/R047C legacy training surfaces; commit bridge definitions/parameters before reading R049 target-bearing files.

### Commit C — OOS HOLDOUT RESULT

Only after Commit A and Commit B exist and are immutable may R049 target-bearing files be opened and evaluated.

Do not amend/rebase/rewrite A or B after R049 is opened. Any changed A/B freeze is a new calibration generation and loses the OOS claim.

## 3. Stage A — candidate-native observable / bridge grammar freeze

Allowed inputs:

- R048 PR #539 exact frozen G2 artifacts;
- Foundational Logic V1 / Gate V3;
- the R050 input lock metadata.

Forbidden in Stage A:

- R049 report, raw atlas, target files, source registry, pressure names, row IDs, protocols, tolerances, source details;
- R046/R047C training content;
- classical π numeric value as a design/selection signal.

For each of six G2 candidates freeze:

- exact N0/N1 core hash;
- every admissible native/N2 observable already derivable from the frozen core;
- admissible operations on those observables: finite counts, ratios, quotient maps, pushforwards, composition laws, recurrence counts, reachability/order relations, etc.;
- forbidden new readouts that would require target-aware invention;
- generic bridge grammar allowed later in Stage B;
- structural parameters already inside the candidate;
- potential calibration/metrology parameter slots, typed as calibration-only;
- parameter-count/description-length accounting;
- candidate-wide versus family-specific bridge distinction;
- no row/target-specific adapter is allowed to earn OOS credit.

**Stage A may not add a new candidate primitive, state variable, update law, quotient, observable or parameter family merely because it may be useful later.**

Required Stage-A artifacts:

- `R050_PREBRIDGE_OBSERVABLE_CATALOG.json`
- `R050_PREBRIDGE_FORBIDDEN_ADAPTERS.json`
- `R050_PREBRIDGE_FREEZE_MANIFEST.json`
- exact checker/hash certificate.

Freeze and COMMIT A.

## 4. Stage B — legacy training / metrology bridge freeze

After Commit A only, open the legacy training surfaces:

- R046 PR #534 at frozen head;
- R047C PR #537 at frozen head.

R049 remains closed.

Purpose: pay the R048 D5 calibration/metrology debt legally, without modifying native cores or Stage-A readouts.

For each G2 candidate:

1. attempt to map only Stage-A-frozen observables to legacy engineering quantities;
2. any fitted parameters must be estimated solely from legacy construction/training evidence;
3. record training data used, fitting rule, parameter count, uncertainty, identifiability and residuals;
4. distinguish a candidate-global bridge from pressure-family-specific bridges;
5. forbid per-row adapters;
6. if no quantitative bridge is possible, freeze that failure honestly;
7. training success does not count as R049 evidence.

Bridge classes:

- `B0_NATIVE_DIRECT` — no calibration parameter or effective conversion;
- `B1_PREFROZEN_UNIFORM_READOUT` — Stage-A readout only;
- `B2_LEGACY_TRAINED_METROLOGY_BRIDGE` — parameters fit only on legacy R046/R047C training data and frozen before R049;
- `B3_POST_TARGET_ADAPTER` — invented/changed after R049 open; debt only, OOS-ineligible;
- `B4_ILLEGAL_LEAKAGE` — target/effective definition copied into native side; reject.

Required Stage-B artifacts:

- `R050_LEGACY_TRAINING_LEDGER.json`
- `R050_TRAINED_BRIDGE_REGISTRY.json`
- `R050_PARAMETER_DEBT.json`
- `R050_TRAINING_RESULTS.json`
- `R050_BRIDGE_FREEZE_MANIFEST.json`
- exact checker/hash certificate.

Freeze and COMMIT B.

## 5. Stage C — open exact R049 holdout and run OOS evaluation

Only now open PR #540 target-bearing files and verify exact target SHA-256:

`e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c`

If target hash differs, stop with `HOLDOUT_HASH_FAILURE`.

After opening R049:

- no native core edit;
- no Stage-A readout edit;
- no Stage-B bridge/parameter edit or refit;
- no target-specific tolerance change;
- no new pressure-specific bridge;
- no deletion of hard rows;
- no classical π numeric matching loss.

Evaluate all six candidates against **all 8 frozen R049 empirical rows**. Then aggregate to the 6 frozen pressure families.

For Block-B pressure families that contain two independent realizations, family-level success requires the same frozen bridge/readout system to satisfy both realizations; one-row success is not family success.

## 6. Evidence ladder

Use exactly:

- `O0_UNMAPPED` — no legal frozen mapping;
- `O1_STRUCTURAL_ONLY` — qualitative mechanism/readout correspondence only;
- `O2_EXACT_NONQUANTITATIVE_CONSTRAINT` — exact target-relevant finite/relational prediction, but no engineering-unit quantitative prediction;
- `O3_TRAINING_QUANTITATIVE_ONLY` — quantitative legacy training bridge existed, but R049 row does not pass the frozen OOS criterion;
- `O4_OUT_OF_SAMPLE_QUANTITATIVE_PASS` — unchanged pre-R049 bridge predicts an R049 row within its frozen source-stated eligibility/error rule;
- `O5_CROSS_PRESSURE_SHARED_OOS_EXPLANATION` — one candidate with the same low-debt frozen shared state/readout/bridge system achieves family-level OOS success on at least two independent R049 pressure families, with no new target-specific parameter.

Never upgrade O1/O2 to O4 because the mechanism “looks right”.

## 7. Required matrices and accounting

Return:

1. complete `6 candidates × 8 R049 rows` matrix;
2. `6 candidates × 6 pressure families` aggregate matrix;
3. row-by-row predicted observable before seeing measured output where practicable;
4. frozen measured output / error rule;
5. residual/error and PASS/FAIL;
6. bridge class B0–B4;
7. evidence O0–O5;
8. fitted parameter count and where each parameter came from;
9. bridge description length / target-specific adapter count;
10. leakage audit;
11. training-source-overlap caveat propagation from R049;
12. explanatory-compression accounting.

## 8. Dominance / selection

No weighted total score.

A candidate may strictly dominate another only if it has:

- strictly more O4/O5 frozen holdout coverage;
- no greater target-specific adapter debt;
- no greater illegal-import debt;
- no greater fitted-parameter debt under the declared comparison;
- and no worse failure on any pressure family counted in the dominance claim.

If no strict dominance, retain Pareto family. Do not force a winner.

A mechanism that passes only legacy training but not R049 is not an engineering-success explanation.

## 9. Mandatory kill tests

Attack at least:

- `READOUT_INVENTED_AFTER_TARGET`
- `BRIDGE_REFIT_ON_HOLDOUT`
- `TARGET_SPECIFIC_PARAMETER`
- `FAMILY_SPECIFIC_PATCHWORK_AS_SHARED_EXPLANATION`
- `CLASSICAL_PI_NUMERIC_SELECTION`
- `CALCULATED_OUTPUT_AS_MEASUREMENT`
- `SAME_SOURCE_TRAINING_HOLDOUT_COLLISION`
- `ONE_BLOCK_B_REALIZATION_AS_FAMILY_PASS`
- `QUALITATIVE_ANALOGY_AS_O4`
- `CANDIDATE_CORE_MUTATION`
- `TARGET_FIELD_MUTATION`
- `POST_TARGET_FREEZE_REWRITE`

## 10. Required artifacts

At minimum:

- `R050_REPORT.md`
- `R050_FREEZE_INTEGRITY.json`
- `R050_PREBRIDGE_OBSERVABLE_CATALOG.json`
- `R050_PREBRIDGE_FORBIDDEN_ADAPTERS.json`
- `R050_PREBRIDGE_FREEZE_MANIFEST.json`
- `R050_LEGACY_TRAINING_LEDGER.json`
- `R050_TRAINED_BRIDGE_REGISTRY.json`
- `R050_PARAMETER_DEBT.json`
- `R050_TRAINING_RESULTS.json`
- `R050_BRIDGE_FREEZE_MANIFEST.json`
- `R050_R049_ROW_CALIBRATION_MATRIX.json`
- `R050_R049_PRESSURE_COVERAGE_MATRIX.json`
- `R050_OUT_OF_SAMPLE_RESULTS.json`
- `R050_TARGET_LEAKAGE_AUDIT.json`
- `R050_PARETO_FRONTIER.json`
- `R050_NEW_GENERATION_QUESTIONS.json`
- exact checker/tests and artifact manifest.

## 11. Success / honest negative return

Positive high-value return requires at least one genuine O4. Strong cross-domain return requires O5.

But the following is also a valid high-value result:

`G2_OUT_OF_SAMPLE_QUANTITATIVE_FAILURE / PREBRIDGE_DISCIPLINE_PRESERVED / METROLOGY_DEBT_OR_NATIVE_DEBT_LOCALIZED / NO_WINNER / NOT_CANONICAL`

Do not repair a failed frozen candidate inside R050. Convert failure only into a later-generation question.

CI: `CI_NOT_REQUIRED_FOR_RESEARCH` unless a later promotion boundary explicitly requires it.
