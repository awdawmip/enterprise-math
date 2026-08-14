# RS-R057X-MATCHED-RESIDUAL-HOTSPOT-ISOLATION-COVERAGE-CONTROL

Researcher-ID: `EM-R057X-5E8C41`

Generation: `R057X`

Stage: `F — MATCHED RESIDUAL HOTSPOT ISOLATION WITH CATALOG-COVERAGE CONTROL`

## Frozen inputs

This stage begins only after Driver acceptance of the independently frozen A/G joint-surface exposures.

Cross-arm anchors:

- `R057X_STAGE_E_COMMON_COMPONENT_CHECKPOINT_SHA256`
  `3937572b2f8099f9ce125a86ccf90ec9aad6f9470b0af9ec4b8026df67796385`
- `R057X_STAGE_D_RESIDUAL_STRUCTURE_CHECKPOINT_SHA256`
  `7059ec68f6ace7cb46360476b7378b12b06dbb5a426269c20ae598e6bde1e771`
- `R057X_STAGE_C1_STAR_COMPARISON_CHECKPOINT_SHA256`
  `1af2df3eefbb1eeee35418d59edf197657d91c1e14c47e8fdf319aab00a9c75d`
- frozen Stage-B 62-motif dictionary:
  `R057X_MATCHED_LOCAL_MOTIF_PROBES_SHA256`
  `f9256c9cac705e7208f5efd3667c7f9ee62deda9f5d38b713268d679f57fd2c0`

A arm:

- `R057_A_STAGE_H_JOINT_SURFACE_CHECKPOINT_SHA256`
  `bf3c30df26f7a4095935bfce2682e7f8b4bb834ec2c74b838a5d73b26b7e41dc`
- `R057_A_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE_SHA256`
  `4baad1a7c3528d9b147a3ee38fb5436a3e607a2141178a284f540bfc1ce5eaf3`
- `R057_A_FROZEN_TRANSITION_NUISANCE_SURFACE_SHA256`
  `ac58760ca6f460961e41287452127060e3e3d2dfd9cf069a65fc6029f1b06e6f`
- source head at Driver review:
  `research/r057-stage0@2f12c79548d236a757bdba1e57fc48cc0522c020`

G arm:

- `R057G_STAGE_I_JOINT_SURFACE_CHECKPOINT_SHA256`
  `a963b2fa951435655885b7eca4ec1d01561825bbb712396aab3516405560171f`
- `R057G_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE_SHA256`
  `f50c9cdab6143e6d1e5339bfb3079e30b56e70991bca40ce9225cfdcc2415c22`
- `R057G_FROZEN_TRANSITION_NUISANCE_SURFACE_SHA256`
  `14b198f6d1b87cc40454453e99046a946b7f841a6b76469fbbf2f84009b1e723`
- source head at Driver review:
  `agent/r057g-em-r057g-93d4a8-stagei@da9975f733e25a4319e56919faea66ad7785cd38`

Joint-surface taskbook source:
`d7f379be95c0e31e130e9b9c088fcaf1e1fd7815`.

All earlier A/G/X frozen bytes remain immutable.

## Stage goal

Stage E was `INSUFFICIENT` because the durable A/G surfaces did not expose sample-level frozen-D2 residual × matched-motif exposure or symmetric per-transition nuisance arrays. Those surfaces now exist.

Stage F asks one narrow question:

> after controlling for catalog coverage, scale and already-frozen nuisance burden without refitting anything, is there a nontrivial local motif whose exposure is associated with large frozen D2 residuals in the same direction in both carriers?

This is a post-fit diagnostic stage. It is not authorized to invent or fit a new generator.

## Critical catalog-coverage fact

The two carriers have strongly different coverage by the frozen 62-motif ±1 turn-word catalog:

- A: 1,862,510 eligible k=2..6 cyclic windows; 0 unmatched; catalog coverage 100%.
- G: 285,655 eligible windows; 64,608 matched; 221,047 unmatched; catalog coverage about 22.6% overall.

This asymmetry is scientifically material.

Therefore:

1. **Primary motif exposure must use the fraction over ALL eligible cyclic k=2..6 windows.**
2. Matched-catalog-only fractions are secondary sensitivity diagnostics only.
3. G `UNMATCHED_BY_FROZEN_62_CATALOG` fraction must be retained as an explicit coverage diagnostic.
4. No result based only on matched-only denominators may be promoted to a cross-carrier hotspot.
5. Do not expand the motif catalog in Stage F. Catalog incompleteness, if supported, is a possible next-stage routing result, not an excuse to change the frozen dictionary here.

## Hard prohibitions

No coefficient refit.
No optimizer.
No symbolic regression.
No new teacher or matched-teacher generation.
No K expansion.
No new feature/operator/surrogate.
No parser/context/segmentation/assembly/readout mutation.
No fitted cross-arm rescaling.
No raw A/G residual magnitude ranking.
No reading or using R057Y gravity evidence.
No generator invention.
No post-hoc change of nuisance-light selection rules after looking at residual outcomes.

Descriptive association statistics, rank comparisons and predeclared multiple-testing correction are allowed.

---

# LANE F0 — INPUT / INDEPENDENCE GATE

Freeze an X-owned registry of all consumed A/G artifact SHA256 values.

Verify:

- both joint surfaces descend from the accepted Stage-E checkpoint;
- A parent Stage-G and G parent Stage-H checkpoints match frozen anchors;
- both use exactly the frozen 62 Stage-B motif keys;
- both count all cyclic contiguous boundary windows k=2..6;
- A did not read the new G numeric surface before freezing its checkpoint;
- G did not read the new A numeric surface before freezing its checkpoint;
- A D2 sample reproduction is exact on 144 samples;
- G D2 reproduction gate passed on 120 samples;
- exposure definitions were residual-blind and residual columns joined only afterward;
- no refit/optimizer/teacher/K/operator/parser/assembly/readout change occurred.

If any item fails: `HARD_STOP_STAGE_F_INPUT_INVALID`.

---

# LANE F1 — CATALOG COVERAGE AUDIT

For each arm and sample, compute only from the frozen exposure tables:

- eligible window count;
- matched window count;
- unmatched window count;
- matched fraction over all eligible windows;
- unmatched fraction over all eligible windows.

Freeze aggregate and by-radius distributions.

For G only, descriptively test whether `unmatched_fraction` co-varies with:

- within-radius absolute residual percentile;
- within-radius signed residual percentile;
- radius;
- phase;
- orientation.

Allowed statistics: Spearman/Pearson where meaningful, quantile tables, rank ordering.
No predictor synthesis.

Required classification:

- `CATALOG_COVERAGE_ASYMMETRY_CONFIRMED`
- and one of:
  - `G_UNMATCHED_BURDEN_RESIDUAL_ASSOCIATED`
  - `G_UNMATCHED_BURDEN_NOT_ASSOCIATED`
  - `G_UNMATCHED_BURDEN_INSUFFICIENT`

This is a diagnostic of semantic coverage only, not a new generator.

---

# LANE F2 — SYMMETRIC NUISANCE-LIGHT STRATA

Reproduce the exact residual-blind nuisance-ranking definitions frozen by Stage E. Do not invent a new ranking rule.

Stage E used non-residual nuisance quantities such as:

- packet/motif mixture change;
- AREA_STAR × RUN_DEFECT_STAR correlation/covariance change;
- covariance leading-eigen concentration;
- phase/orientation weights only as predeclared nuisance metadata, never selected from residual magnitude.

Now instantiate the same Stage-E rule on the newly exposed A per-transition nuisance arrays and reproduce the already-instantiated G result.

Freeze:

- A strict nuisance-light transitions/radii;
- G strict nuisance-light transitions/radii;
- any matched dimensionless-scale pairs that survive on both sides.

If the exact Stage-E rule cannot be reconstructed from frozen artifacts without ambiguity, return `NUISANCE_RULE_NOT_REPRODUCIBLE` and do not invent a replacement.

---

# LANE F3 — PRIMARY MOTIF × RESIDUAL ENRICHMENT

Primary residual readout: frozen D2 only.

Primary motif exposure:

`motif_count / all_eligible_k2_6_windows`.

Matched-only exposure:

`motif_count / matched_catalog_windows`

is sensitivity-only.

For each of the 62 motifs, separately within A and G compute at least:

1. support/sample nonzero count;
2. mean/median primary exposure;
3. Spearman association with within-radius absolute residual percentile;
4. Spearman association with within-radius signed residual percentile;
5. high-vs-low absolute-residual enrichment:
   - HIGH = within-radius absolute-residual percentile >= 0.75
   - LOW = within-radius absolute-residual percentile <= 0.25
   - report `mean(exposure|HIGH)-mean(exposure|LOW)`;
6. analogous signed-residual upper-vs-lower quartile contrast.

Use the frozen within-radius percentiles already exposed by the arms. Do not reselect thresholds after seeing results.

For the 62 simultaneous motif tests, if p-values are reported, apply a predeclared Benjamini-Hochberg correction separately within each arm and clearly label it descriptive post-fit inference. Do not use significance alone to define a generator.

Motifs with too little exposure support must be labeled `LOW_SUPPORT`, not zero-effect.

---

# LANE F4 — COVERAGE AND NUISANCE SENSITIVITY

For every motif that appears among the strongest residual-enrichment candidates in either arm, repeat the direction-only diagnostics under:

1. all samples, primary all-eligible denominator;
2. nuisance-light strata from F2;
3. frozen Stage-E matched dimensionless-scale pairs where sample support exists;
4. matched-only denominator as sensitivity only.

For G additionally stratify by low/high unmatched-fraction burden using residual-blind coverage quantiles.

Do not promote a motif if its cross-arm direction appears only under matched-only normalization or only in a high-unmatched G stratum.

---

# LANE F5 — CROSS-CARRIER HOTSPOT CROSSWALK

Construct a 62-row cross-arm table containing at least:

- A/G support counts;
- A/G primary exposure ranks;
- A/G absolute-residual Spearman signs/ranks;
- A/G high-minus-low absolute-residual enrichment signs/ranks;
- signed-residual direction diagnostics;
- nuisance-light persistence status;
- matched-scale persistence status;
- G coverage-sensitivity status;
- whether matched-only normalization changes the qualitative conclusion.

Do not compare raw residual amplitudes or require coefficient equality.

Allowed motif-level classifications:

- `COMMON_HOTSPOT_CANDIDATE`
- `COMMON_COLDSPOT_CANDIDATE`
- `A_ONLY_SIGNAL`
- `G_ONLY_SIGNAL`
- `COVERAGE_SENSITIVE`
- `NUISANCE_SENSITIVE`
- `LOW_SUPPORT`
- `NO_STABLE_ASSOCIATION`
- `INSUFFICIENT`

A `COMMON_HOTSPOT_CANDIDATE` must at minimum have:

- non-low support in both arms;
- same positive direction for primary all-eligible exposure vs absolute-residual diagnostics in both arms;
- no sign reversal in nuisance-light sensitivity where evaluable;
- no dependence on matched-only denominator for the cross-arm direction;
- no obvious G unmatched-fraction confounding sufficient to reverse the direction.

This is still only a candidate residual signature, not an operator.

---

# LANE F6 — PRIMARY DISPOSITION

Return exactly one:

1. `COMMON_MATCHED_MOTIF_HOTSPOT_ISOLATED`
2. `COMMON_MATCHED_MOTIF_SIGNAL_COVERAGE_LIMITED`
3. `CATALOG_DOMAIN_MISMATCH_DOMINATES`
4. `NO_COMMON_MATCHED_MOTIF_HOTSPOT`
5. `INSUFFICIENT`

Threshold for (1) is deliberately high: one coincidental rank overlap or matched-only signal is not enough.

Interpretation:

- (1): a later Driver-authorized stage may inspect the local geometry of the isolated motif(s) and formulate omitted-generator hypotheses. Do NOT formulate them in Stage F.
- (2): common signal exists but frozen 62-catalog coverage, especially on G, prevents clean isolation. Do not fit a new generator.
- (3): G's large unmatched domain materially controls the diagnostic; next step should examine semantic catalog completeness before any generator search.
- (4): current 62-motif vocabulary has enough support/coverage to reject a stable common hotspot at this diagnostic resolution. This does not prove no omitted mechanism exists.
- (5): evidence remains insufficient for a directional conclusion.

---

# REQUIRED ARTIFACTS

Produce at least:

- `R057X_STAGE_F_INPUT_REGISTRY.json`
- `R057X_MOTIF_CATALOG_COVERAGE_AUDIT.json`
- `R057X_SYMMETRIC_NUISANCE_LIGHT_STRATA.json`
- `R057X_MOTIF_RESIDUAL_ENRICHMENT_A.json`
- `R057X_MOTIF_RESIDUAL_ENRICHMENT_G.json`
- `R057X_CROSS_ARM_MOTIF_HOTSPOT_CROSSWALK.json`
- `R057X_STAGE_F_HOTSPOT_VERDICT.json`
- `R057X_STAGE_F_MATCHED_RESIDUAL_HOTSPOT_CHECKPOINT.json`
- deterministic checker / exact check results
- delivery manifest / bundle as normal research delivery

Freeze and return:

`R057X_STAGE_F_MATCHED_RESIDUAL_HOTSPOT_CHECKPOINT_SHA256`

Then stop for Driver review.

## Epistemic label

`POST_FIT_CROSS_CARRIER_MATCHED_RESIDUAL_HOTSPOT_DIAGNOSTIC / NOT_THEOREM / NOT_CANONICAL`
