# RS-R057X-COMMON-RESIDUAL-COMPONENT-ISOLATION

Researcher-ID: `EM-R057X-5E8C41`

Generation: `R057X`

Stage: `E — COMMON RESIDUAL COMPONENT ISOLATION WITHOUT REFIT`

## Frozen inputs

Stage E starts only after Driver acceptance of R057X Stage D.

Freeze and consume read-only:

- `R057X_STAGE_D_RESIDUAL_STRUCTURE_CHECKPOINT_SHA256`
  `7059ec68f6ace7cb46360476b7378b12b06dbb5a426269c20ae598e6bde1e771`
- `R057X_STAGE_C1_STAR_COMPARISON_CHECKPOINT_SHA256`
  `1af2df3eefbb1eeee35418d59edf197657d91c1e14c47e8fdf319aab00a9c75d`
- A diagnostic checkpoint
  `R057_A_STAGE_G_RESIDUAL_DIAGNOSTIC_CHECKPOINT_SHA256=4f2280c85a831b0270b03a15f377f7dbb51569351b513d9b79bd7aaac35ea0f0`
- G diagnostic checkpoint
  `R057G_STAGE_H_RESIDUAL_DIAGNOSTIC_CHECKPOINT_SHA256=21f051e5f2cfe276a1a746112968ca7d8ca6dedee2efe9fe006da94e47f9726b`
- X Stage-B matched local motif semantics and Stage-C0R V2 STAR semantics, read-only.

All earlier R055/R056/R057/R057G/R057X frozen generations remain immutable.

R057Y gravity bridge is orthogonal and MUST NOT be read or used in Stage E.

## Scientific goal

Stage D froze:

`MIXED_COMMON_AND_CARRIER_SPECIFIC_RESIDUAL_STRUCTURE`.

It established only a weak common finite-scale component and common assembly-switching exclusion. It did NOT establish a common post-mixture rebound trajectory or one common residual mechanism. G carries a stronger diagnosed mixture/covariance/phase burden than A.

Stage E asks one narrower question:

> After removing or stratifying away the strongest already-diagnosed carrier-specific nuisance burden WITHOUT fitting any new model, does a common residual signature remain across A and G?

This is a diagnostics-only isolation stage. It is NOT a generator-discovery stage.

## Hard prohibitions

Do not:

- refit any coefficient;
- run an optimizer;
- run symbolic regression;
- train a nuisance model or residual predictor;
- create a new feature/operator/surrogate;
- change K;
- generate new teacher data;
- alter parser/context/segmentation/assembly/readout;
- compare raw A/G MSE or RMSE as commensurate quantities;
- fit a cross-arm rescaling map;
- use R057Y/R055/R056 gravity evidence;
- infer a new collapse generator directly from residual hotspots.

All transformations must be deterministic recombinations, ranks, bins, or stratifications of already-frozen diagnostics/predictions.

# LANE E0 — INPUT / REPRODUCTION GATE

Create `R057X_STAGE_E_INPUT_REGISTRY.json`.

Verify all Stage-D input hashes plus Stage-D checkpoint `7059...e771`.

Verify Stage D status:

- `NO_STAGE_D_FIT`;
- `MIXED_COMMON_AND_CARRIER_SPECIFIC_RESIDUAL_STRUCTURE`;
- `COMMON_ASSEMBLY_SWITCHING_EXCLUSION` supported;
- `COMMON_FINITE_SCALE_RESIDUAL_COMPONENT` supported only as weak matched statement;
- common post-mixture rebound `INSUFFICIENT`;
- `G_CARRIER_MIXTURE_BURDEN_STRONGER` descriptively supported.

If any gate fails: `R057X_STAGE_E_INPUT_FAIL` and stop.

# LANE E1 — COMMON DIMENSIONLESS SCALE COORDINATE

Use the already-frozen C0R carrier units only.

Define a non-fitted resolution coordinate:

`S = R / ell_edge`.

Thus:

- A: `ell_edge_A = 1/sqrt(3)` and `S_A = sqrt(3) R_A`;
- G: `ell_edge_G = 1` and `S_G = R_G`.

This is unit conversion, not a fitted cross-arm alignment.

Report both native radius and S.

Do not interpolate one arm onto the other.

Construct only nearest-neighbor or tolerance-declared scale pairs where useful. Freeze the tolerance rule BEFORE inspecting residual outcomes. Prefer a symmetric log-scale distance rule, for example `|log(S_A/S_G)| <= log(4/3)`; if a different threshold is used, justify and freeze it before outcome comparison.

# LANE E2 — NUISANCE-LIGHT STRATA

Stage D indicates G has stronger packet-mixture/covariance/phase burden; A has weaker but nonzero nuisance structure.

Construct arm-internal nuisance-light strata WITHOUT fitting.

For each arm separately use only frozen diagnostics and deterministic rank thresholds.

At minimum consider:

1. packet/motif mixture variation burden;
2. STAR feature covariance rotation/concentration burden;
3. phase-stratum burden;
4. orientation burden on G only, kept as arm-specific and never imputed to A.

Do not combine incomparable raw statistics across arms.

Permitted selection examples:

- lowest 50% within-arm mixture-burden ranks;
- lowest 50% within-arm covariance-rotation/concentration-change ranks;
- intersection of predeclared low-burden ranks;
- phase-balanced strata using frozen equal-weight semantics.

Freeze all rank/tie conventions before inspecting common residual conclusions.

Output `R057X_NUISANCE_LIGHT_STRATA_REGISTRY.json`.

# LANE E3 — FINITE-SCALE COMPONENT AFTER NUISANCE STRATIFICATION

Within each arm, using frozen D1/D2/D3 residuals only, test whether early-scale residual burden persists inside nuisance-light strata.

Primary basis for cross-arm structural comparison: frozen compact candidate D2.

D1 may be used as topology-only sensitivity reference. D3 remains stability-rejected and must not be promoted by lower fit error.

Use within-arm normalization only, such as:

- residual RMSE divided by that arm's frozen global residual RMS;
- radius-rank percentile;
- sign/direction of early-vs-late normalized residual contrast.

No cross-arm raw magnitude subtraction.

Predeclare an ordinal isolation test, for example:

`EARLY_SCALE_BURDEN_PERSISTS_AFTER_NUISANCE_STRATIFICATION`

for each arm.

Then classify cross-arm:

- `COMMON_FINITE_SCALE_COMPONENT_SURVIVES_NUISANCE_STRATIFICATION`
- `A_ONLY_FINITE_SCALE_COMPONENT_SURVIVES`
- `G_ONLY_FINITE_SCALE_COMPONENT_SURVIVES`
- `FINITE_SCALE_COMMONALITY_DISSOLVES_AFTER_STRATIFICATION`
- `INSUFFICIENT`.

# LANE E4 — MATCHED LOCAL-MOTIF RESIDUAL ENRICHMENT

Use the already-frozen X Stage-B semantic matched-motif vocabulary. Do not match raw A/G class IDs.

Shared range is at least K<=6.

Because A deployment may use longer selected packets, when needed define deterministic K<=6 contiguous submotifs of the actually deployed selected boundary packets. Freeze the extraction convention before residual analysis.

For each matched motif compute descriptive, non-causal residual association separately in A and G.

Preferred robust statistic:

- within each radius, rank teachers/samples by frozen signed residual and absolute residual;
- compare motif exposure/enrichment in predeclared upper vs lower quartiles;
- aggregate across radii by median sign / sign-consistency count;
- separately report occurrence support.

Alternative deterministic descriptive statistics are allowed, but no regression, learned weighting or optimizer.

Do NOT assign a unique packet-level residual contribution when assembly does not mathematically provide one. Exposure association is not causal attribution.

For each motif compare across carriers:

- signed residual-enrichment direction;
- absolute residual hotspot enrichment;
- zero/low-support status;
- scale persistence;
- D1 vs D2 sensitivity.

Classify motifs only as:

- `COMMON_RESIDUAL_HOTSPOT`
- `COMMON_RESIDUAL_COLDSPOT`
- `A_SPECIFIC_ASSOCIATION`
- `G_SPECIFIC_ASSOCIATION`
- `SIGN_DISAGREEMENT`
- `LOW_SUPPORT`
- `NO_ASSOCIATION`.

Output `R057X_MATCHED_MOTIF_RESIDUAL_ENRICHMENT.json`.

# LANE E5 — RESIDUAL GEOMETRY AFTER NUISANCE-LIGHT FILTERING

Within the nuisance-light strata, recompute only descriptive frozen STAR geometry:

- AREA_STAR / RUN_DEFECT_STAR mean and variance;
- covariance/correlation sign;
- leading-eigen share/effective rank where defined;
- residual hotspot overlap with AREA/RUN_DEFECT ranks.

No fitted projection.

Ask:

1. Does G's stronger covariance rotation largely disappear in nuisance-light strata?
2. Does A retain its R=448/640 unexplained rebound even under nuisance-light selection?
3. Is there a common AREA-vs-RUN_DEFECT residual-hotspot orientation after nuisance suppression?

Allowed status:

- `COMMON_RESIDUAL_GEOMETRY_AFTER_NUISANCE_SUPPRESSION`
- `CARRIER_SPECIFIC_RESIDUAL_GEOMETRY_PERSISTS`
- `INSUFFICIENT`.

# LANE E6 — COMMON COMPONENT ISOLATION VERDICT

Return exactly one primary disposition:

1. `COMMON_RESIDUAL_COMPONENT_ISOLATED`
2. `COMMON_FINITE_SCALE_COMPONENT_ONLY`
3. `CARRIER_SPECIFIC_NUISANCE_DOMINATES_AFTER_ISOLATION`
4. `COMMON_COMPONENT_NOT_ISOLATED`
5. `INSUFFICIENT`

Threshold for (1) is deliberately high. It requires at least one nontrivial matched signature beyond common early-scale burden, for example a supported matched motif residual-hotspot pattern or matched nuisance-light residual geometry.

If only early-scale burden survives but no matched motif/geometry signature does, choose (2), not (1).

If no common component is isolated, do not invent a generator.

# NEXT-STAGE ROUTING

If `COMMON_RESIDUAL_COMPONENT_ISOLATED`:

- next X stage may authorize a tightly bounded omitted-generator discovery search targeted only at the isolated common hotspot/geometry signature;
- all new candidates must be labeled `CROSS_ARM_INSPIRED_POST_SERIOUS_CHECKPOINT`;
- generator discovery remains separate from this stage.

If `COMMON_FINITE_SCALE_COMPONENT_ONLY`:

- prefer scale/asymptotic analysis or matched-teacher bridge before generator invention.

If carrier-specific nuisance remains dominant or common component is not isolated:

- return residual search to carrier-specific arms or improve diagnostics; do not force a common algebra.

# REQUIRED ARTIFACTS

Produce at least:

- `R057X_STAGE_E_INPUT_REGISTRY.json`
- `R057X_COMMON_SCALE_PAIR_REGISTRY.json`
- `R057X_NUISANCE_LIGHT_STRATA_REGISTRY.json`
- `R057X_FINITE_SCALE_NUISANCE_ISOLATION.json`
- `R057X_MATCHED_MOTIF_RESIDUAL_ENRICHMENT.json`
- `R057X_NUISANCE_LIGHT_RESIDUAL_GEOMETRY.json`
- `R057X_COMMON_RESIDUAL_COMPONENT_VERDICT.json`
- `R057X_STAGE_E_COMMON_COMPONENT_CHECKPOINT.json`
- deterministic checker / exact check results
- delivery manifest with SHA256 anchors

Freeze and return:

`R057X_STAGE_E_COMMON_COMPONENT_CHECKPOINT_SHA256`

Then stop for Driver review.

## Epistemic label

`POST_FIT_CROSS_CARRIER_COMMON_COMPONENT_DIAGNOSTIC / NOT_THEOREM / NOT_CANONICAL`
