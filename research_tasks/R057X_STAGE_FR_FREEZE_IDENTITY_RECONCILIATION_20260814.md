# RS-R057X-STAGE-FR-FREEZE-IDENTITY-RECONCILIATION

Researcher-ID: `EM-R057X-5E8C41`

Generation: `R057X`

Stage: `FR — STAGE-F FREEZE IDENTITY RECONCILIATION / DETERMINISTIC REPLAY`

## Purpose

Resolve the Stage-F freeze identity conflict without overwriting any previously frozen bytes and without beginning new scientific discovery.

Two mutually inconsistent Stage-F claims currently exist:

### Frozen V1 byte identity

The supplied frozen Stage-F summary records:

- `R057X_STAGE_F_MATCHED_RESIDUAL_HOTSPOT_CHECKPOINT_SHA256`
  `4cf6a1fd4d748e1175e77503247f41706aacb4946802a3da7bd03a52a4fdad54`
- `primary_disposition = INSUFFICIENT`
- `R057X_STAGE_F_HOTSPOT_VERDICT_SHA256`
  `14285c351e076996d040e41d31b044bb5b66af195398adc4caeb34af8bf30e8f`
- `R057X_STAGE_F_EXACT_CHECK_RESULTS_SHA256`
  `8889a44f2801fab2015bbadf8a376514e986b500a4b51f8ee37c3193b75a5edf`
- `R057X_STAGE_F_DELIVERY_MANIFEST_SHA256`
  `9cb0fb2c75533ad5b0afe4641122d67215573cf1315582a389f76a213ec370bc`
- deterministic checker: `PASS_48_OF_48`.

This V1 identity is immutable history whether or not a repaired V2 is later accepted.

### Conflicting later completion claim

A later natural-language completion claim states:

`COMMON_MATCHED_MOTIF_SIGNAL_COVERAGE_LIMITED`

with the same scientific firewall, but no independently auditable V2 checkpoint SHA256 was supplied on the Driver-visible source surface at conflict detection time.

The purpose of Stage FR is to determine whether:

1. V1 is the unique deterministic Stage-F result;
2. a distinct V2 result exists and is reproducible from the exact frozen inputs under the exact Stage-F rules;
3. a rule/code/input divergence explains the V1/V2 difference; or
4. the conflict cannot be resolved without violating frozen-generation immutability.

Stage FR is a repair/audit stage, not a new hotspot-discovery stage.

---

# Immutable scientific inputs

Use only the exact inputs authorized by Stage F:

- `R057X_STAGE_E_COMMON_COMPONENT_CHECKPOINT_SHA256`
  `3937572b2f8099f9ce125a86ccf90ec9aad6f9470b0af9ec4b8026df67796385`
- `R057_A_STAGE_H_JOINT_SURFACE_CHECKPOINT_SHA256`
  `bf3c30df26f7a4095935bfce2682e7f8b4bb834ec2c74b838a5d73b26b7e41dc`
- `R057_A_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE_SHA256`
  `4baad1a7c3528d9b147a3ee38fb5436a3e607a2141178a284f540bfc1ce5eaf3`
- `R057_A_FROZEN_TRANSITION_NUISANCE_SURFACE_SHA256`
  `ac58760ca6f460961e41287452127060e3e3d2dfd9cf069a65fc6029f1b06e6f`
- `R057G_STAGE_I_JOINT_SURFACE_CHECKPOINT_SHA256`
  `a963b2fa951435655885b7eca4ec1d01561825bbb712396aab3516405560171f`
- `R057G_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE_SHA256`
  `f50c9cdab6143e6d1e5339bfb3079e30b56e70991bca40ce9225cfdcc2415c22`
- `R057G_FROZEN_TRANSITION_NUISANCE_SURFACE_SHA256`
  `14b198f6d1b87cc40454453e99046a946b7f841a6b76469fbbf2f84009b1e723`
- `R057X_MATCHED_LOCAL_MOTIF_PROBES_SHA256`
  `f9256c9cac705e7208f5efd3667c7f9ee62deda9f5d38b713268d679f57fd2c0`

Original Stage-F taskbook semantics are frozen at:

`research_tasks/R057X_MATCHED_RESIDUAL_HOTSPOT_ISOLATION_COVERAGE_CONTROL_20260814.md`

source commit:

`8abe99ad7c2ea54cb112c7a96a4c92166ce47495`

No Stage-F rule may be reinterpreted or silently changed in Stage FR.

---

# Hard prohibitions

Stage FR must not:

- overwrite or mutate V1 bytes;
- refit coefficients;
- run an optimizer for model fitting;
- run symbolic regression;
- generate a new teacher;
- expand K;
- add or expand the motif catalog;
- add a feature/operator/surrogate;
- change parser/context/segmentation/assembly/readout;
- change the nuisance-light rule;
- change the residual quartile thresholds;
- change the Stage-E dimensionless-scale gate;
- change the all-eligible primary denominator rule;
- promote matched-only denominator to primary;
- read R057Y gravity evidence;
- invent D4 or any generator;
- start the next scientific stage.

Only deterministic replay, byte comparison, code/rule/input provenance comparison and publication repair are authorized.

---

# FR0 — V1 IMMUTABILITY REGISTRY

Freeze a registry containing the exact known V1 identity.

At minimum record:

- V1 checkpoint SHA256 `4cf6...ad54`;
- V1 disposition `INSUFFICIENT`;
- V1 verdict SHA256 `14285c...0e8f`;
- V1 check-results SHA256 `8889a4...5edf`;
- V1 manifest SHA256 `9cb0fb...70bc`;
- every V1 artifact hash available from the supplied freeze summary;
- V1 publication state at conflict detection: Driver-visible Stage-F branch still pointed to Stage-E head `872e23d76fe9c29b8a5fd922a3c05b98ef39062c`.

Classification:

`R057X_STAGE_F_V1_HISTORICAL_FROZEN_IDENTITY`

This identity must remain immutable even if V2 is later accepted.

---

# FR1 — RECOVER ORIGINAL STAGE-F WORKSPACE

If the original completed Stage-F local/workspace directory still exists, do not recompute first.

Inventory every Stage-F artifact and script byte exactly as it exists.

Record:

- path;
- byte count;
- SHA256;
- modification provenance if available;
- embedded primary disposition;
- embedded parent/input hashes;
- checker result;
- whether the artifact belongs to the V1 identity or a distinct later identity.

Search specifically for the required Stage-F artifacts:

- `R057X_STAGE_F_INPUT_REGISTRY.json`
- `R057X_MOTIF_CATALOG_COVERAGE_AUDIT.json`
- `R057X_SYMMETRIC_NUISANCE_LIGHT_STRATA.json`
- `R057X_MOTIF_RESIDUAL_ENRICHMENT_A.json`
- `R057X_MOTIF_RESIDUAL_ENRICHMENT_G.json`
- `R057X_CROSS_ARM_MOTIF_HOTSPOT_CROSSWALK.json`
- `R057X_STAGE_F_HOTSPOT_VERDICT.json`
- `R057X_STAGE_F_MATCHED_RESIDUAL_HOTSPOT_CHECKPOINT.json`
- exact checker/check results;
- delivery manifest;
- report.

Do not synthesize missing files during FR1.

Return one of:

- `ONE_STAGE_F_BYTE_IDENTITY_FOUND`
- `TWO_DISTINCT_STAGE_F_BYTE_IDENTITIES_FOUND`
- `INCOMPLETE_STAGE_F_WORKSPACE_FOUND`
- `NO_STAGE_F_WORKSPACE_RECOVERABLE`.

---

# FR2 — EXACT RULE AND CODE DIFF

If two identities exist, compare them before any rerun.

Produce an exact diff ledger over:

- input SHA256 registry;
- motif catalog keys;
- eligible/matched/unmatched denominator rules;
- all-eligible versus matched-only exposure selection;
- G unmatched-fraction coverage diagnostic;
- nuisance-light ranking rule;
- nuisance-light selected transitions;
- dimensionless scale formula and tolerance;
- residual percentile/rank convention;
- HIGH/LOW quartile thresholds;
- association statistics;
- BH correction implementation if used;
- motif-level classification thresholds;
- final disposition decision logic;
- code/script SHA256.

Any scientific-rule difference is not a publication repair. It must be labeled:

`POST_FREEZE_RULE_CHANGE_DETECTED`

and may not silently replace V1.

A pure serialization/publication bug must be isolated separately from a scientific-rule/code bug.

---

# FR3 — DETERMINISTIC CLEAN REPLAY

After FR0-FR2 are frozen, perform one clean replay only if needed to decide identity.

Replay the exact original Stage-F taskbook from the exact frozen A/G/X inputs.

Requirements:

1. primary motif exposure is exactly `motif_count / all eligible k=2..6 windows`;
2. matched-only exposure is sensitivity only;
3. G unmatched fraction remains an explicit coverage diagnostic;
4. the Stage-E nuisance-light rule is reproduced exactly, not redesigned;
5. the Stage-E dimensionless scale gate remains exactly
   `S_A=sqrt(3)R_A`, `S_G=R_G`, `|log(S_A/S_G)|<=log(4/3)`;
6. no interpolation or fitted cross-arm rescaling;
7. no generator synthesis.

The clean replay must write into a new Stage-FR/V2 directory and must never overwrite V1 paths.

Run the deterministic checker twice from clean output if feasible. Byte-identical second execution is preferred.

---

# FR4 — DECISION-DIVERGENCE LEDGER

Whether the replay returns V1 or a different result, explicitly identify the decisive evidence behind the final disposition.

For each of the five Stage-F allowed dispositions record whether its threshold is satisfied:

1. `COMMON_MATCHED_MOTIF_HOTSPOT_ISOLATED`
2. `COMMON_MATCHED_MOTIF_SIGNAL_COVERAGE_LIMITED`
3. `CATALOG_DOMAIN_MISMATCH_DOMINATES`
4. `NO_COMMON_MATCHED_MOTIF_HOTSPOT`
5. `INSUFFICIENT`

For the claimed `COMMON_MATCHED_MOTIF_SIGNAL_COVERAGE_LIMITED` route, name the exact motif IDs that supply the residual common signal and freeze, for each motif:

- A support count;
- G support count;
- A/G primary all-eligible exposure association direction;
- A/G high-minus-low absolute-residual enrichment direction;
- nuisance-light persistence;
- matched-scale persistence;
- matched-only sensitivity;
- G coverage/unmatched sensitivity;
- exact reason the evidence exceeds `INSUFFICIENT` but does not reach `COMMON_MATCHED_MOTIF_HOTSPOT_ISOLATED`.

If no concrete motif IDs satisfy the frozen Stage-F criteria, `COMMON_MATCHED_MOTIF_SIGNAL_COVERAGE_LIMITED` cannot be the repaired disposition.

For `INSUFFICIENT`, identify the exact missing/evaluable criteria that prevent promotion.

No natural-language-only verdict is acceptable; every decisive item must trace to frozen artifact fields.

---

# FR5 — FINAL FREEZE-IDENTITY VERDICT

Return exactly one:

### A. `V1_REPRODUCED_AUTHORITATIVE`

Clean replay reproduces V1 disposition and decisive fields. V1 remains the Stage-F result. The later coverage-limited natural-language claim is rejected as non-frozen/non-authoritative.

### B. `V2_REPAIR_REPRODUCED_AND_EXPLAINED`

A distinct V2 is deterministically reproduced, and the V1→V2 difference is explained by an identified implementation/publication defect or other bounded repair that does not change the frozen Stage-F scientific rules.

Requirements for B:

- V1 remains immutable historical checkpoint;
- V2 receives new checkpoint SHA256;
- V2 uses explicit schema/version such as `R057X_STAGE_FR_*_V2`;
- V1/V2 diff ledger is frozen;
- all V2 required Stage-F artifacts exist;
- clean checker PASS;
- no rule changes.

### C. `POST_FREEZE_RULE_CHANGE_REQUIRES_NEW_SCIENTIFIC_STAGE`

The coverage-limited result depends on changing Stage-F rules after V1 freeze. It cannot be called a repair. V1 remains authoritative for Stage F; any changed analysis requires a separately authorized scientific stage.

### D. `FREEZE_IDENTITY_UNRESOLVED`

Evidence remains insufficient to identify one deterministic result. D4 remains blocked.

No other primary verdict is allowed.

---

# FR6 — PUBLICATION

If verdict A:

- publish V1 bytes exactly as historical Stage-F V1;
- do not rewrite their content;
- publish a reconciliation report/checkpoint explaining that V1 was reproduced.

If verdict B:

- publish V1 historical registry;
- publish V2 under distinct filenames/schema/version;
- never replace V1 files in place;
- publish exact V1→V2 diff ledger and repair explanation.

If verdict C or D:

- publish the conflict/reconciliation checkpoint only;
- do not authorize D4.

---

# Required Stage-FR artifacts

Produce at least:

- `R057X_STAGE_F_V1_FREEZE_REGISTRY.json`
- `R057X_STAGE_FR_WORKSPACE_IDENTITY_AUDIT.json`
- `R057X_STAGE_FR_V1_V2_DIFF_LEDGER.json`
- `R057X_STAGE_FR_RULE_REPRODUCTION_AUDIT.json`
- `R057X_STAGE_FR_DECISION_DIVERGENCE_LEDGER.json`
- `R057X_STAGE_FR_FREEZE_IDENTITY_VERDICT.json`
- `R057X_STAGE_FR_FREEZE_IDENTITY_CHECKPOINT.json`
- deterministic checker / exact check results
- report
- delivery manifest.

Freeze and return:

`R057X_STAGE_FR_FREEZE_IDENTITY_CHECKPOINT_SHA256`

If and only if verdict B is selected, also return:

`R057X_STAGE_F_V2_MATCHED_RESIDUAL_HOTSPOT_CHECKPOINT_SHA256`

Then stop for Driver review.

## Epistemic label

`FREEZE_IDENTITY_RECONCILIATION / DETERMINISTIC_REPLAY / NO_NEW_SCIENCE / NOT_THEOREM / NOT_CANONICAL`
