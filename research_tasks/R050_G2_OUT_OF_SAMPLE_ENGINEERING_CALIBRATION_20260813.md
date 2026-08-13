<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R050-G2-OUT-OF-SAMPLE-ENGINEERING-CALIBRATION",
  "title": "R050 G2 Out-of-Sample Engineering Calibration against Frozen Candidate-Blind Holdout",
  "kind": "RESEARCH",
  "owner": "program/foundational-logic-engineering-inversion",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "OUT_OF_SAMPLE_CALIBRATION / G2 / ENGINEERING_SUCCESS",
  "frontier": "Test the six frozen R048 G2 mechanisms against the exact candidate-blind R049 engineering holdout, with scoring/holdout protocol frozen before candidate content is opened, and determine whether any mechanism reaches quantitative out-of-sample or cross-pressure explanatory evidence without target leakage or core mutation.",
  "next_action": "Stage 0: verify and freeze the R049 target/scoring protocol before opening R048 candidate definitions. Stage 1+: verify G2 hashes, evaluate every frozen candidate against all eight empirical rows and six pressure families, audit bridges/parameters/leakage, and return a no-winner result unless strict evidence supports otherwise.",
  "dependencies": [
    {
      "target": "R048 Draft PR #539 head 58eaac9aa2d407d682c05bdd67ada8aded5fb642",
      "action": "CONSUME_EXACT_FROZEN_G2_CANDIDATE_SET_ONLY_AFTER_STAGE0_SCORING_FREEZE",
      "satisfied": true
    },
    {
      "target": "R048 G2 candidate-set SHA-256 2e1f85a3faf37a0525364c220f9449caea45408bf6a954c09045bf78646cf959",
      "action": "VERIFY_BEFORE_CALIBRATION",
      "satisfied": true
    },
    {
      "target": "R049 Draft PR #540 head 220aa5647389386d6c953e6aa04f32769f90f490",
      "action": "CONSUME_EXACT_FROZEN_HOLDOUT_BYTES",
      "satisfied": true
    },
    {
      "target": "R049 target SHA-256 e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c",
      "action": "RECOMPUTE_AND_VERIFY_BEFORE_ANY_CANDIDATE_CONTENT_IS_OPENED",
      "satisfied": true
    },
    {
      "target": "Foundational Logic V1 and Native-Semantics Admissibility Gate V3",
      "action": "CONSUME_DEFINITION_NOT_INHERITED_AND_NO_OUTPUT_COPYING",
      "satisfied": true
    }
  ],
  "source_refs": [
    "R048 frozen second-generation native mechanisms",
    "R049 candidate-blind frozen engineering holdout",
    "R049 publication acceptance comment 5276059245"
  ],
  "evidence_status": "OUT_OF_SAMPLE_ENGINEERING_CALIBRATION",
  "last_progress_ref": "R049 target publication accepted with exact target hash preserved; no calibration has been run against G2.",
  "last_progress_at": "2026-08-13T12:40:00+08:00",
  "hard_block": null,
  "tags": [
    "R050",
    "g2",
    "out-of-sample",
    "engineering-calibration",
    "candidate-blind-holdout",
    "metrology-bridge",
    "cross-pressure",
    "no-output-copying"
  ],
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

# R050 — G2 Out-of-Sample Engineering Calibration

Status: `READY / P0 / OUT-OF-SAMPLE CALIBRATION / FROZEN CANDIDATES + FROZEN TARGET / NOT CANONICAL`

## 0. Mother question

R048 generated six second-generation native mechanisms from a failure-derived debt basis while target details were withheld. R049 then independently froze a candidate-blind engineering holdout after those candidate cores already existed.

This task asks:

> **Do any frozen G2 mechanisms explain the unseen R049 engineering holdout beyond qualitative analogy, and can any mechanism transfer quantitatively across independent conditions or pressure families without target-specific patching, illegal effective-definition import, or candidate-core mutation?**

This is calibration only. Candidate definitions are immutable.

---

## 1. Exact frozen inputs

### G2 candidates

Source: Draft PR #539, exact head:

`58eaac9aa2d407d682c05bdd67ada8aded5fb642`

Authoritative candidate file:

`research_outputs/r048_20260813/R048_G2_CANDIDATE_SET.json`

Required candidate-set SHA-256:

`2e1f85a3faf37a0525364c220f9449caea45408bf6a954c09045bf78646cf959`

Six frozen candidates only. Do not repair, extend, merge, retune, or replace a core definition.

### Independent holdout

Source: Draft PR #540, exact head:

`220aa5647389386d6c953e6aa04f32769f90f490`

Authoritative target artifacts are exactly those listed in:

`research_outputs/R049/R049_HOLDOUT_MANIFEST.json`

Required target SHA-256:

`e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c`

The target contains eight empirical rows:

- four Block-A independent holdouts for inherited pressure families;
- two Block-B new pressure families, each represented by two materially different physical realizations.

No target field may change during R050.

---

## 2. Stage 0 — scoring protocol freeze BEFORE candidate opening

This stage is mandatory.

Before reading any R048 candidate definition/name/theorem/counterexample beyond the fact that six frozen candidates exist:

1. fetch R049 PR #540 at exact head;
2. recompute every manifest artifact SHA-256 and the aggregate target SHA-256;
3. reject execution if target hash is not exactly `e41cc96e...`;
4. inspect only R049 target/source artifacts;
5. define a candidate-independent calibration/scoring protocol;
6. freeze it to `R050_SCORING_PROTOCOL.json` with its own SHA-256;
7. only after that hash exists may candidate definitions be opened.

The scoring protocol must freeze:

- row-level eligibility;
- what counts as a legal physical-to-native input map;
- what counts as a legal native-to-measured-output readout;
- allowed fitted parameters and where they may be estimated;
- construction/holdout split rules where a source provides enough independent conditions;
- quantitative error metric and source-stated envelope use;
- aggregation from eight empirical rows to six pressure-family results;
- bridge classes and evidence levels below;
- no weighted total score.

If a source does not support a genuine independent quantitative split, freeze that fact as `NOT_ELIGIBLE_FOR_E4` rather than inventing data or tolerance.

### Block-B transfer rule

For each Block-B pressure family, the two physical realizations are distinct holdout arms.

A claim of cross-realization quantitative transfer must not independently redesign/refit a target-specific bridge for each realization.

Prefer a bidirectional test when source information permits:

- identify/freeze the bridge form on realization A and test B without changing candidate core or bridge semantics;
- identify/freeze the bridge form on B and test A likewise.

Any realization-specific metrology constants must be explicitly counted as calibration debt and may not become native premises.

---

## 3. Candidate freeze gate

After Stage 0 scoring freeze:

1. fetch R048 PR #539 at exact head;
2. recompute candidate-set and all per-candidate hashes;
3. verify six candidate definitions exactly;
4. record `CORE_EDIT_COUNT = 0` before scoring begins.

Any proposed improvement after seeing R049 is:

`NEW_GENERATION_CANDIDATE_FOR_LATER_TASK`

and cannot be scored as the frozen R048 candidate.

---

## 4. Required matrices

Evaluate all six candidates against all eight empirical rows:

\[
6\times 8 = 48
\]

row-level calibration cells.

Then aggregate to all six pressure families:

1. `GEOMETRIC_MEASURE_COHERENCE`
2. `CYCLE_CLOSURE_AND_RELATIVE_PHASE`
3. `DIFFUSIVE_RELAXATION`
4. `BOUNDED_MODE_SPECTRUM`
5. `TRANSFER_INVENTORY_BALANCE_CLOSURE`
6. `SOURCE_RECEIVER_INTERCHANGE_RECIPROCITY`

forming a complete:

\[
6\times 6 = 36
\]

candidate × pressure matrix.

No candidate or pressure family may be skipped because it looks implausible.

---

## 5. Typed bridge classes

Every row-level cell must explicitly contain:

```text
frozen physical protocol
→ physical-to-native encoding
→ frozen candidate dynamics/structure
→ native readout/quotient
→ metrology bridge if any
→ predicted measured-output statement
```

Classify the strongest live bridge:

- `B0_NATIVE_DIRECT` — target-relevant relation follows directly from frozen native/N0-definable structure with no added calibration mapping beyond representation.
- `B1_UNIFORM_READOUT` — one target-independent derived readout/quotient, no fitted target-specific parameters.
- `B2_CALIBRATED_METROLOGY_BRIDGE` — bridge form is fixed and legal, but finite calibration parameters are estimated only from the scoring protocol's declared construction subset; parameter count/dependency must be explicit.
- `B3_TARGET_SPECIFIC_ADAPTER` — protocol-specific adapter/codebook chosen after target access. This is explanatory debt, not foundational success.
- `B4_ILLEGAL_LEAKAGE` — imports effective target definitions or output-equivalent structure into the native premise. Reject.

`B3` may never support E4/E5. `B4` is a hard fail for that mapping.

---

## 6. Evidence levels

Use exactly:

- `E0_UNMAPPED` — no legal predictive mapping.
- `E1_QUALITATIVE_MECHANISM` — only analogy/shape/mechanism resemblance.
- `E2_EXACT_STRUCTURAL_CONSTRAINT` — an exact finite theorem implies a definition-stripped structural target statement, but no engineering-unit quantitative prediction.
- `E3_QUANTITATIVE_CONSTRUCTION` — quantitative agreement on the pre-frozen construction/calibration subset only.
- `E4_QUANTITATIVE_OUT_OF_SAMPLE` — bridge/parameters frozen first, then independent target conditions/realization pass the source-stated error/uncertainty envelope.
- `E5_CROSS_PRESSURE_SHARED_EXPLANATION` — one frozen candidate plus one target-independent bridge schema/shared native state achieves E4 on at least two independent pressure families without per-pressure B3 adapters.

Never promote E1/E2 to engineering validation.

---

## 7. Forbidden effective-definition imports

At minimum reject backward import of:

- center;
- distance/equidistance;
- radius/circle/sphere;
- Euclidean geometry/measure as undeclared native premise;
- angle/radian/`2π-per-cycle`;
- continuum PDE/heat kernel/Gaussian normalization;
- Fourier normalization/eigenmode formula;
- classical π numerical value or decimal target;
- classical control-volume balance as a native conservation axiom merely because Block B1 measures transfer;
- electromagnetic/acoustic reciprocity theorem as a native axiom merely because Block B2 measures interchange.

Effective mathematics may be used downstream to interpret/calibrate only after the native mechanism/readout is fixed.

---

## 8. Quantitative discipline

For every E3/E4 claim, record:

- exact source row;
- construction data/conditions used;
- holdout data/conditions used;
- fitted parameter names and count;
- parameter estimation rule;
- predicted quantity;
- measured quantity;
- residual/error;
- source uncertainty/tolerance envelope;
- PASS/FAIL rule;
- whether uncertainty is expanded, one-sigma, source-defined curve covariance, or another source-defined form.

Do not invent a universal tolerance.

If only source summary uncertainty is available without enough raw/condition-separated data to test a candidate prediction, return `NOT_ELIGIBLE_FOR_E4`.

---

## 9. Pressure-level aggregation

A pressure-family result must preserve constituent-row structure.

For Block A, pressure result inherits the single frozen protocol and any pre-frozen within-protocol construction/holdout split.

For Block B, a pressure result cannot exceed E3 unless at least one realization is genuinely held out from bridge identification; E4 requires successful transfer to a materially independent realization/condition under the Stage-0 rule.

Do not average away a failed row.

---

## 10. Parameter and explanatory debt

For every candidate return a debt vector including at least:

- E4 pressure coverage;
- E5 shared-pressure relations;
- B0/B1/B2/B3/B4 counts;
- fitted parameter count;
- target-specific adapter count;
- illegal import count;
- unexplained pressure count;
- native-state information cost;
- metrology-bridge description length;
- number of distinct bridge schemas needed across six pressure families.

Do not collapse this to one weighted scalar score.

---

## 11. Dominance / winner discipline

A candidate may strictly dominate another only if, on the declared axes, it has:

1. strictly greater E4 pressure coverage or E5 cross-pressure coverage;
2. no greater B3/B4 debt;
3. no greater fitted-parameter debt;
4. no target leakage;
5. no candidate core edits.

If no strict dominance exists, return a Pareto family and **do not choose a winner**.

A structurally elegant candidate that never reaches E4 is not an engineering-success explanation.

---

## 12. Generation-level inference boundary

R050 calibrates only R048 G2 candidates.

Do not claim from R050 alone that G2 is superior to R047 G1, because G1 is not scored on the same R049 target in this task.

You may note future comparative-test requirements, but do not retroactively infer causal improvement.

---

## 13. Required attacks

Explicitly run and record:

- `TARGET_MUTATION_AFTER_CANDIDATE_OPEN`
- `CANDIDATE_CORE_REPAIR`
- `CLASSICAL_PI_NUMERIC_SELECTION`
- `OUTPUT_DEFINITION_BACKFILL`
- `B3_ADAPTER_PROMOTED_TO_SUCCESS`
- `TRAINING_RELABELED_AS_HOLDOUT`
- `TOLERANCE_INVENTED_WITHOUT_SOURCE`
- `BLOCK_B_PER_REALIZATION_REFIT`
- `METAPHOR_AS_QUANTITATIVE_EXPLANATION`
- `PARAMETER_EXPLOSION`
- `FAILED_ROW_AVERAGED_AWAY`
- `CROSS_PRESSURE_SHARED_STATE_ASSERTED_WITHOUT_E4`

---

## 14. Failure inheritance

If no E4/E5 candidate survives, this is a valid and important result.

Extract the smallest failure-derived next necessities, but type them before any new generation:

- native/N0D structure debt;
- N1 operational debt;
- N2 readout debt;
- metrology bridge debt;
- evaluation-only requirement.

Do not modify any G2 candidate in R050.

If a candidate reaches E4/E5, isolate exactly which frozen theorem + bridge + parameter structure made it possible and attack that result adversarially before recommending follow-up.

---

## 15. Required artifacts

At minimum return:

- `R050_REPORT.md`
- `R050_SCORING_PROTOCOL.json`
- `R050_FREEZE_INTEGRITY.json`
- `R050_ROW_LEVEL_6x8_MATRIX.json`
- `R050_PRESSURE_LEVEL_6x6_MATRIX.json`
- `R050_BRIDGE_LEDGER.json`
- `R050_PARAMETER_DEBT.json`
- `R050_METROLOGY_BRIDGE_LEDGER.json`
- `R050_HOLDOUT_RESULTS.json`
- `R050_CROSS_PRESSURE_SHARED_STATE.json`
- `R050_EXPLANATORY_DEBT_VECTORS.json`
- `R050_PARETO_FRONTIER.json`
- `R050_TARGET_LEAKAGE_AUDIT.json`
- `R050_FAILURE_INHERITANCE.json`
- exact checker/tests for manifest/hash/matrix/scoring consistency.

Keep the PR Draft / `NOT_CANONICAL`.

CI: `CI_NOT_REQUIRED_FOR_RESEARCH` unless a later acceptance/promotion task explicitly asks for CI.

---

## 16. Return classes

Use the strongest justified classification, e.g.:

```text
G2_OUT_OF_SAMPLE_CALIBRATION_COMPLETE /
NO_E4_E5 /
FAILURE_DEBTS_FROZEN /
NO_STRICT_WINNER /
NOT_CANONICAL
```

or, only if supported:

```text
G2_OUT_OF_SAMPLE_ENGINEERING_TRANSFER_FOUND /
E4_OR_E5_SURVIVOR_ISOLATED /
ADVERSARIAL_REPLICATION_REQUIRED /
NOT_CANONICAL
```
