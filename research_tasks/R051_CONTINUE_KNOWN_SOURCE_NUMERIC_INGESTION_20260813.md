<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R051-CONTINUE-CANDIDATE-BLIND-KNOWN-SOURCE-NUMERIC-INGESTION",
  "title": "R051 Continuation — Candidate-Blind Known-Source Numeric Ingestion",
  "kind": "RESEARCH_CONTINUATION",
  "owner": "program/engineering-success-inversion",
  "base_state": "CONTINUE_SAME_TASK",
  "priority": "P0",
  "leverage": "QUANTITATIVE_HOLDOUT_DATA_INGESTION / E4_ELIGIBILITY",
  "frontier": "Ingest already-discovered authoritative machine-readable/source-native measurement data without candidate access, preserving R051 generation-1 immutability and creating a separate generation-2 quantitative target if source semantics permit.",
  "next_action": "Verify R051 generation-1 hashes, exhaust the known authoritative machine-readable/table sources in the frozen registry, freeze per-source schema/split maps before numerical value inspection, then ingest values and freeze a new candidate-blind target generation.",
  "dependencies": [
    {"target":"R051 Draft PR #542 head b6fbf431a3c76c4a437acf97cb7a784762e524ab","action":"CONSUME_ACCEPTED_R051_GENERATION1","satisfied":true},
    {"target":"R051 generation-1 quantitative target 58b5bcd03cf7070008b2f97a3457d376f566355e1848933317f57a5d2edcc498","action":"VERIFY_AND_NEVER_MUTATE","satisfied":true},
    {"target":"R051 acquisition protocol 029d33ce71064dbcc584f10a757d237868dc921f5345646970b7357f1804e22f","action":"PRESERVE_AS_GOVERNING_BASELINE","satisfied":true}
  ],
  "evidence_status": "KNOWN_SOURCE_INGESTION_CONTINUATION",
  "hard_block": null,
  "tags": ["R051","continue-same-task","candidate-blind","quantitative-data","source-ingestion","holdout"],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "PRESERVE_EXISTING_RESEARCHER_ID",
  "identity_lane": "R051",
  "policy_review": {"policy_set":"research_taskbook_policy.json","policy_digest":"sha256:5e1e1e3dd925c9c1a434e8dae7eafd4b5a8e62a88cd725f43d5aa7b400cad242","review_state":"PASS","temporary_overrides":[]}
}
-->

# R051 continuation — Candidate-Blind Known-Source Numeric Ingestion

Status: `CONTINUE_SAME_TASK / P0 / GENERATION1_IMMUTABLE / CANDIDATE_BLIND / NOT CANONICAL`

Researcher identity is preserved:

`Researcher-ID: EM-R051-8B4D70`

This is **not R052**. The mother question from R051 is still actionable because authoritative numeric sources were discovered but not actually ingested.

## 0. Accepted R051 boundary

Consume exactly:

- R051 Draft PR #542 exact head: `b6fbf431a3c76c4a437acf97cb7a784762e524ab`
- R051 acquisition protocol SHA-256: `029d33ce71064dbcc584f10a757d237868dc921f5345646970b7357f1804e22f`
- R051 generation-1 target SHA-256: `58b5bcd03cf7070008b2f97a3457d376f566355e1848933317f57a5d2edcc498`
- R049 target SHA-256: `e41cc96ecc40bf1c992ad75bc552b2e68b36a5620e4343f10e15b71d9cf64f0c`

First action: independently re-verify all hashes that are reproducible from the exact artifacts.

Generation 1 is immutable. Do **not** edit, replace, or reinterpret any generation-1 artifact in place. Any newly ingested quantitative evidence belongs to **R051 generation 2** with a new manifest and target hash.

## 1. Candidate firewall remains active

Until generation-2 target freeze, forbidden:

- R048 PR #539 candidate definitions/names/theorems/counterexamples/internal structure;
- R050 PR #541 candidate-specific matrices, bridge results, debt vectors, Pareto observations;
- any G1/G2 score, ranking or candidate-performance summary as a data-selection signal;
- classical pi numerical value as a source/condition/split/tolerance signal;
- calibration, bridge scoring, candidate ranking, or G3 generation.

If incidental candidate-specific context appears, record `CONTEXT_CONTAMINATION_RISK`, quarantine it, and do not use it for source/schema/column/condition/split/uncertainty/eligibility decisions.

## 2. Known-source ingestion comes before any broad replacement search

Exhaust these already-discovered candidate-blind authoritative sources first.

### Priority K1 — NIST LSNA phase-calibration CSV

Source registry ID:

`SRC-R051-CCRP-NIST-LSNA-PDR`

Known source facts frozen by R051:

- official NIST PDR record;
- file: `AWG_LSNA_25KHz.csv`;
- approximate size: 17.4 MB;
- expected source SHA-256:
  `486fbc54eac9e091e071ff1bed7170bcde41c20166a6070ec625baaa7bcac934`;
- primary paper: `Large-Signal-Network-Analyzer Phase Calibration on an Arbitrary Grid`.

Requirements:

1. Resolve the official PDR download through authoritative NIST metadata/API/download surfaces.
2. Acquire exact file bytes.
3. Verify the exact source SHA-256 before using any numerical rows.
4. Record source URL, retrieval metadata, byte size, hash and deterministic acquisition procedure.
5. Do not treat “file exists” as evidence; actual row content must be ingested.

### Priority K2 — BIPM/APMP step-gauge source-native table

Source registry ID:

`SRC-R051-GMC-BIPM-APMP-L-K5-2006-1`

Known source fact:

- official KCDB record states measurement data `x_i` occur on pp. 9–15 of the final report.

Requirements:

1. Acquire the official final-report PDF/source file from BIPM/KCDB.
2. Record exact file hash.
3. Extract only **source-native tabulated numerical values** and source-stated uncertainty semantics.
4. Manual plot digitization remains forbidden.
5. Derived DoE/En values cannot be relabeled as raw measurements.

### Priority K3 — NIST thermography raw dataset

Source registry ID:

`SRC-R051-DR-NIST-THERMOGRAPHY-PDR`

Only continue with it if the primary/source metadata supports a genuinely matching `DIFFUSIVE_RELAXATION` measured carrier, condition index and uncertainty/error semantics without stretching the pressure family. If not, retain rejection.

### Priority K4 — other already-discovered official machine data

The NIST S2P archive remains rejected unless a bounded-resonator measured-response dataset is independently found. Do not repurpose on-wafer calibration data as a cavity/resonator target.

Only after K1–K4 are exhausted may a broader candidate-blind replacement search resume.

## 3. Header/schema-before-values freeze

For every source file/table that is successfully acquired, use a two-step firewall.

### Step H1 — source integrity

Before numerical interpretation:

- verify source file/hash;
- identify source paper/report and source-defined semantics;
- identify file/table version.

### Step H2 — schema-only freeze

Before inspecting numerical measured values beyond what is necessary to parse headers/schema, create and freeze:

`R051_G2_SOURCE_SCHEMA_AND_SPLIT_PROTOCOL.json`

For each source it must specify:

- source ID/file hash;
- exact measured carrier column(s)/table field(s);
- columns explicitly rejected as model-derived/calculated/normalized descendants;
- condition key fields;
- source units;
- uncertainty/covariance fields and semantics;
- deterministic row inclusion/exclusion rule based only on source metadata/schema;
- construction/holdout split rule based only on stable condition keys/source ordering;
- allowed residual form;
- whether source provides a valid PASS/FAIL uncertainty semantics.

Return and freeze its SHA-256 **before evaluating the numeric values themselves**.

If a source cannot be semantically typed from header/report metadata without looking at outcome magnitudes, reject it rather than cherry-pick.

## 4. Numerical ingestion after schema freeze

Only after the schema/split protocol hash is frozen may the selected numerical rows be parsed and frozen.

For every retained row record:

- original source-native condition key;
- original measured numerical value;
- original source unit;
- original source precision/rounding;
- per-condition uncertainty/covariance/error semantics if supplied;
- deterministic construction/holdout membership;
- exact source location/row number/table cell/file offset or deterministic parser index;
- whether value is raw measurement, source-processed measurement, or derived/calculated output.

Derived/calculated outputs may be retained for provenance but cannot become the authoritative measured carrier unless the source itself explicitly defines them as the measured observation and this matches the frozen pressure semantics.

## 5. Construction/holdout rule

Preserve R051 generation-1 split discipline:

1. source-defined independent split if available;
2. cross-realization split when genuinely independent realizations exist;
3. predeclared disjoint condition ranges from source condition keys;
4. otherwise alternating condition IDs in stable source-native ordering;
5. final fallback: SHA-256(condition_key_utf8) parity.

No measured-value magnitude, residual, candidate prediction, or success/failure may influence the split.

The same observation may never appear in both construction and holdout.

## 6. E4 eligibility

A generation-2 row is `E4_ELIGIBLE_TARGET` only if the frozen packet contains enough source-grounded information for a later researcher to compute an independent residual without inventing data:

- condition-indexed measured values;
- disjoint construction and holdout subsets;
- source-grounded uncertainty/tolerance/error semantics sufficient for the declared residual;
- exact source provenance and file hash;
- deterministic extraction and split rules;
- no target/candidate leakage.

If a numerical array exists but no defensible independent holdout exists, classify `E3_ONLY_CONSTRUCTION_DATA_NO_INDEPENDENT_HOLDOUT`.

If a numerical array exists but no source-grounded PASS/FAIL envelope exists, retain quantitative descriptive data but do not fabricate an E4 threshold.

## 7. Block B remains strict

Do not weaken R051 generation-1 rules merely to create E4.

`TRANSFER_INVENTORY_BALANCE_CLOSURE` requires independent liquid + gas realizations for pressure-level E4 transfer.

`SOURCE_RECEIVER_INTERCHANGE_RECIPROCITY` requires directed-pair numerical observations for both microphone + three-antenna realizations for pressure-level E4 transfer.

One-realization success may be retained as row-level quantitative evidence but cannot be promoted to pressure-level cross-realization E4.

## 8. Large-file publication rule

Do not bloat the repository merely to vendor a large official source file.

For large authoritative files, it is sufficient to freeze:

- official download identifier/URL;
- exact source-file SHA-256 and byte size;
- deterministic acquisition script/instructions;
- deterministic extraction parser;
- source-schema receipt;
- extracted authoritative target rows necessary for later calibration.

The extracted rows must be reproducible exactly from the hashed source file.

## 9. Mandatory attacks

Run at least:

- `SOURCE_HASH_NOT_VERIFIED`
- `NUMERIC_VALUES_READ_BEFORE_SCHEMA_SPLIT_FREEZE`
- `CANDIDATE_INFORMATION_USED_FOR_SOURCE_SELECTION`
- `CANDIDATE_INFORMATION_USED_FOR_COLUMN_SELECTION`
- `CANDIDATE_INFORMATION_USED_FOR_SPLIT`
- `MODEL_OR_DERIVED_COLUMN_PROMOTED_TO_MEASUREMENT`
- `PLOT_DIGITIZATION_AS_RAW_DATA`
- `HEADER_ONLY_DATASET_EXISTENCE_PROMOTED_TO_E4`
- `SAME_OBSERVATION_USED_FOR_CONSTRUCTION_AND_HOLDOUT`
- `TOLERANCE_INVENTED_WITHOUT_SOURCE`
- `SOURCE_TABLE_ROUNDING_IGNORED`
- `UNIT_CONVERSION_DOUBLE_COUNT`
- `PRESSURE_FAMILY_STRETCHED_FOR_AVAILABLE_DATA`
- `BLOCK_B_ONE_REALIZATION_ONLY_PROMOTED_TO_PRESSURE_E4`
- `GENERATION1_TARGET_MUTATED`
- `CLASSICAL_PI_NUMERIC_SELECTION`

## 10. Required return

Produce a generation-2 packet, without modifying generation 1:

- `R051_CONTINUE_REPORT.md`
- `R051_G2_SOURCE_RECEIPTS.json`
- `R051_G2_SOURCE_SCHEMA_AND_SPLIT_PROTOCOL.json`
- `R051_G2_QUANTITATIVE_ENGINEERING_ATLAS.json`
- `R051_G2_CONSTRUCTION_HOLDOUT_SPLITS.json`
- `R051_G2_UNCERTAINTY_LEDGER.json`
- `R051_G2_REPLACEMENT_ROW_LEDGER.json`
- `R051_G2_SOURCE_REGISTRY.json`
- `R051_G2_TARGET_LEAKAGE_AUDIT.json`
- `R051_G2_ADVERSARIAL_TEST_RESULTS.json`
- `R051_G2_QUANTITATIVE_HOLDOUT_MANIFEST.json`
- deterministic download/extraction/checker/tests.

Manifest must freeze:

`R051_GENERATION2_QUANTITATIVE_TARGET_SHA256`

Every retained source/row must end in one of:

- `E4_ELIGIBLE_TARGET`
- `E3_ONLY_CONSTRUCTION_DATA_NO_INDEPENDENT_HOLDOUT`
- `QUANTITATIVE_DATA_NO_SOURCE_GROUNDED_PASSFAIL`
- `SOURCE_FILE_ACQUIRED_BUT_MEASURED_CARRIER_INELIGIBLE`
- `SOURCE_ACQUISITION_FAILED`
- `REPLACEMENT_REJECTED`

If generation 2 still has 0 E4 rows after the known official machine-readable/table sources are actually exhausted, return that result honestly. That would be a materially stronger negative result than generation 1.

## 11. Stop condition

Do **not** open R052 in this task.

Return one of:

`R051_CONTINUATION_QUANTITATIVE_TARGET_FROZEN / E4_ROWS_PRESENT / CALIBRATION_NOT_RUN / NOT_CANONICAL`

or

`R051_CONTINUATION_KNOWN_SOURCES_EXHAUSTED / ZERO_E4_ROWS / CALIBRATION_NOT_RUN / NOT_CANONICAL`

No candidate calibration occurs here.
