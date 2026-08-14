# RS-R057X-FROZEN-STAR-RESIDUAL-STRUCTURE-COMPARISON

Researcher-ID: `EM-R057X-5E8C41`

Generation: `R057X`

Stage: `D — CROSS-CARRIER FROZEN STAR RESIDUAL-STRUCTURE COMPARISON`

## Frozen inputs

This stage begins only from the following already-frozen checkpoints and their hash-anchored diagnostic artifacts.

A arm:

- `R057_STAGE_F_STAR_TRANSFER_CHECKPOINT_SHA256`
  `e8ad43b87b4a64f8b7b1d888bab1bcb96711c36faba592caac724c35edfb848e`
- `R057_A_STAGE_G_RESIDUAL_DIAGNOSTIC_CHECKPOINT_SHA256`
  `4f2280c85a831b0270b03a15f377f7dbb51569351b513d9b79bd7aaac35ea0f0`
- source head at Driver review: `research/r057-stage0@6b2253365fa13a6e96a1037d757bbff53a27f700`

G arm:

- `R057G_STAGE_G_STAR_TRANSFER_CHECKPOINT_SHA256`
  `3593fa3eddd7983d55983f214e77f8318267bf7768daa169a205dd948dd89134`
- `R057G_STAGE_H_RESIDUAL_DIAGNOSTIC_CHECKPOINT_SHA256`
  `21f051e5f2cfe276a1a746112968ca7d8ca6dedee2efe9fe006da94e47f9726b`
- sparse publication source at Driver review: `agent/r057g-em-r057g-93d4a8-stageh@e9b0656fa413fd640efcc03d9562835225fcd3c4`
- Stage-H publication index byte-reproduction: `PASS_8_OF_8`

Cross-arm semantic anchor:

- `R057X_STAGE_C1_STAR_COMPARISON_CHECKPOINT_SHA256`
  `1af2df3eefbb1eeee35418d59edf197657d91c1e14c47e8fdf319aab00a9c75d`

All earlier A/G/X frozen bytes remain immutable.

## Stage goal

Determine whether the remaining frozen STAR residual structure in A and G is best described as:

1. a common cross-carrier residual mechanism;
2. a mixture of common and carrier-specific mechanisms;
3. predominantly carrier-specific residual structure; or
4. insufficiently resolved.

This is a diagnostics-only comparison stage. It is not a new fitting stage and is not authorized to invent a new correction generator.

The key question is no longer whether A and G both use the same STAR vocabulary. That was frozen by Stage C1. The question is now:

> after the common STAR vocabulary is frozen, do the two carriers fail in structurally similar ways, or for different reasons?

## Hard prohibitions

Do **not** perform any of the following:

- coefficient refit;
- optimizer run;
- symbolic regression;
- multivariable regression used as a new predictor;
- new teacher generation;
- teacher expansion;
- K expansion;
- new feature/operator/surrogate;
- parser/context/segmentation change;
- assembly/readout change;
- copying A coefficients into G or G coefficients into A;
- comparing raw A/G fit MSE or RMSE as though the teacher corpora/carriers were numerically commensurate;
- using residual diagnostics to directly invent a new generator;
- using the R057Y gravity pilot or any R055/R056 result as evidence in this stage.

R057Y remains scientifically orthogonal until separately frozen and reviewed.

## Allowed inputs

Read only the frozen Stage-G/Stage-H diagnostics and their frozen upstream STAR semantics, including:

A:

- reproduction gate;
- residual diagnostic atlas;
- motif-mixture trajectory;
- STAR feature geometry;
- assembly / active-set diagnostics;
- residual cause ledger;
- Stage-G checkpoint/report/check results.

G:

- Stage-H publication index;
- reproduction gate;
- residual diagnostic atlas;
- motif-mixture trajectory;
- STAR feature geometry;
- assembly diagnostics;
- residual cause ledger;
- Stage-H checkpoint/check results;
- frozen Stage-G STAR transfer artifacts only where needed to interpret Stage-H fields.

Use Stage C1 only for the already-frozen semantic mapping of STAR coordinates.

---

# LANE D0 — REPRODUCTION / PROVENANCE GATE

Before comparison, freeze an X-owned input registry containing all consumed A/G artifact SHA256 values.

Verify:

- A Stage-G source checkpoint matches `4f2280...a0f0`;
- G Stage-H source checkpoint matches `21f051...726b`;
- both descend from the frozen STAR transfer checkpoints named above;
- both reference X Stage C1 `1af2df...a9c75d`;
- A reports no refit/optimizer/K/teacher/operator/parser/assembly change;
- G reports no refit/optimizer/K/teacher/operator/parser/segmentation change;
- A reproduction gate is exact-difference-zero on 144 circles × 3 frozen models;
- G H0 reproduction is `204/204`, max absolute difference `8.881784197001252e-16`;
- G sparse publication semantics are explicitly recorded: the publication index is the durable source object and its hash/byte table anchors the Stage-H generated artifacts.

If any gate fails, stop and return `R057X_STAGE_D_INPUT_REPRODUCTION_FAIL`.

---

# LANE D1 — EXACT CAUSE-LEDGER CROSSWALK

Construct an exact crosswalk over the union of diagnostic causes:

- `ASSEMBLY_ACTIVE_SET_SWITCHING`
- `FEATURE_COVARIANCE_DRIFT`
- `PACKET_MIXTURE_EVOLUTION`
- `PHASE_MIXTURE`
- `ORIENTATION_MIXTURE`
- `FINITE_SCALE_EFFECT`
- `UNEXPLAINED_RESIDUAL_STRUCTURE`

For every cause, record separately:

- A frozen rating;
- G frozen rating;
- whether the observable is semantically available in both arms;
- whether the two diagnostics measure the same object, analogous objects, or incomparable objects;
- evidence direction only, not raw numeric score comparison.

Allowed crosswalk classifications:

- `COMMON_SUPPORTED`
- `COMMON_REJECTED`
- `COMMON_WEAK`
- `A_STRONGER`
- `G_STRONGER`
- `ARM_SPECIFIC_OBSERVABLE`
- `SEMANTICALLY_ANALOGOUS_NOT_IDENTICAL`
- `INCOMPARABLE`

Do not collapse `WEAK_SUPPORT` and `SUPPORTED` into the same epistemic status.

Primary Driver-reviewed starting facts to reproduce, not assume:

A Stage G:

- assembly switching: `NOT_SUPPORTED`;
- finite-scale effect: `SUPPORTED`;
- feature covariance drift: `WEAK_SUPPORT`;
- packet-mixture evolution: `WEAK_SUPPORT`;
- phase mixture: `WEAK_SUPPORT`;
- unexplained residual structure: `SUPPORTED`.

G Stage H:

- assembly switching: `NOT_SUPPORTED`;
- finite-scale effect: `SUPPORTED`;
- feature covariance drift: `SUPPORTED`;
- packet-mixture evolution: `SUPPORTED`;
- phase mixture: `SUPPORTED`;
- orientation mixture: `WEAK_SUPPORT`;
- unexplained residual structure: `SUPPORTED`.

---

# LANE D2 — WITHIN-ARM NORMALIZED RESIDUAL-TRAJECTORY SHAPES

Raw A/G residual magnitudes are not directly comparable.

Instead compare only within-arm normalized / ordinal structure.

For each arm construct descriptors such as:

- radius ordering by frozen residual RMSE / MSE;
- early-scale vs middle-scale vs largest-scale trend direction;
- existence and location of large-radius rebound relative to that arm's own radius grid;
- whether packet-mixture variation contracts before residual rebound;
- whether feature-covariance rotation/eigenspectrum variation contracts before residual rebound;
- whether residual bias sign exhibits persistent phase strata;
- whether the best/worst phase or orientation strata persist by rank.

Any normalization must be dimensionless and internal to one arm, for example:

- divide by that arm's own global residual RMS;
- rank / percentile within that arm;
- normalize scale by the arm's own ordered radius index.

Do not create a cross-arm fitted rescaling map.

Explicitly test the structural signature:

`RESIDUAL_REBOUND_AFTER_MIXTURE_CONTRACTION`.

Record separately for A and G.

---

# LANE D3 — STAR-COORDINATE RESIDUAL GEOMETRY

Using only frozen STAR coordinates and already-produced diagnostic quantities, compare the role of:

- `AREA_STAR`;
- `RUN_DEFECT_STAR`;
- their within-arm covariance / correlation geometry;
- effective rank / leading-eigen share where already available;
- residual hotspot strata where already available.

No regression is permitted.

Use only descriptive quantities already present or deterministic recombinations of frozen diagnostics, such as:

- sign of correlation;
- rank ordering;
- covariance eigenvalue ratios;
- within-arm z-scores;
- overlap of top/bottom residual strata with top/bottom STAR-feature strata.

Explicitly ask:

1. Is RUN_DEFECT behavior more stable across scale than AREA behavior in both arms?
2. Does AREA credit/allocation appear noisier or more carrier-sensitive than RUN_DEFECT in both arms?
3. Is the A/G difference primarily amplitude/conditioning, or does the residual geometry genuinely rotate differently?

Allowed conclusions here are descriptive only.

---

# LANE D4 — COMMON UNEXPLAINED RESIDUAL SIGNATURE

The main purpose of Stage D is to decide whether the unresolved remainder has a shared structural signature.

Test at least:

### D4.1 Assembly exclusion

Both arms currently reject assembly switching as the dominant explanation.

Determine whether this supports the cross-arm statement:

`COMMON_ASSEMBLY_SWITCHING_EXCLUSION`.

Do not overstate A's missing ordered-path/tie-margin fields; those remain `NOT_AVAILABLE`.

### D4.2 Finite-scale commonality

Both arms support finite-scale effects.

Determine whether the evidence supports only the weak statement

`COMMON_FINITE_SCALE_RESIDUAL_COMPONENT`

or a stronger matched trajectory statement.

### D4.3 Post-mixture rebound

A has a residual rebound at R=448/640 after packet-mixture TV and covariance rotations are already relatively small.

G has nonmonotone large-radius residual behavior after strong early-scale decay.

Determine carefully whether these qualify as the same structural signature under within-arm normalization.

Possible status:

- `COMMON_POST_MIXTURE_REBOUND_SIGNATURE`
- `A_ONLY_POST_MIXTURE_REBOUND`
- `G_ONLY_POST_MIXTURE_REBOUND`
- `NO_COMMON_REBOUND_SIGNATURE`
- `INSUFFICIENT`

### D4.4 Carrier-specific mixture burden

Test the descriptive proposition:

> G residuals carry a stronger carrier-specific packet/covariance/phase mixture component than A residuals, even though both retain an unexplained component.

Allowed classification:

- `G_CARRIER_MIXTURE_BURDEN_STRONGER`
- `NO_MATERIAL_DIFFERENCE_ESTABLISHED`
- `INCOMPARABLE`

Do not interpret this as a statement that one carrier is intrinsically better.

---

# LANE D5 — CROSS-CARRIER RESIDUAL-STRUCTURE DECISION

Return exactly one primary disposition:

1. `COMMON_RESIDUAL_MECHANISM_SUPPORTED`
2. `MIXED_COMMON_AND_CARRIER_SPECIFIC_RESIDUAL_STRUCTURE`
3. `CARRIER_SPECIFIC_RESIDUAL_STRUCTURE_DOMINANT`
4. `CROSS_CARRIER_RESIDUAL_STRUCTURE_INSUFFICIENT`

The preferred epistemic threshold for (1) is high: common cause labels alone are not enough. There must be at least one matched structural residual signature beyond the trivial fact that both have nonzero residuals.

If the evidence instead shows:

- common assembly exclusion;
- common finite-scale component;
- but substantially stronger mixture/covariance/phase burden on G;
- plus unresolved remainder in both;

then disposition (2) is likely more appropriate than (1).

Do not pre-commit to it; reproduce the evidence first.

---

# NEXT-STAGE ROUTING RULE

This Stage D must stop after diagnostics and Driver review.

If `COMMON_RESIDUAL_MECHANISM_SUPPORTED` or a strong common unexplained signature is found, the **next** generation may consider an X-owned matched-teacher residual bridge or an analytic decomposition stage.

If `MIXED_COMMON_AND_CARRIER_SPECIFIC_RESIDUAL_STRUCTURE`, the next step should first isolate the common residual component from carrier-specific mixture/covariance effects before any new operator proposal.

If `CARRIER_SPECIFIC_RESIDUAL_STRUCTURE_DOMINANT`, return residual investigation to each carrier separately.

No branch is authorized by this task to invent a new generator immediately from the diagnostic result.

---

# REQUIRED ARTIFACTS

Produce at least:

- `R057X_STAGE_D_INPUT_REGISTRY.json`
- `R057X_STAR_RESIDUAL_CAUSE_CROSSWALK.json`
- `R057X_NORMALIZED_RESIDUAL_TRAJECTORY_COMPARISON.json`
- `R057X_STAR_RESIDUAL_COORDINATE_COMPARISON.json`
- `R057X_COMMON_UNEXPLAINED_RESIDUAL_LEDGER.json`
- `R057X_STAGE_D_RESIDUAL_STRUCTURE_CHECKPOINT.json`
- `R057X_STAGE_D_REPORT.md`
- independent checker / exact check results
- delivery manifest with SHA256 for all frozen outputs

Freeze and return:

`R057X_STAGE_D_RESIDUAL_STRUCTURE_CHECKPOINT_SHA256`

Then stop for Driver review.

## Epistemic label

All results from this stage must remain:

`POST_FIT_CROSS_CARRIER_RESIDUAL_DIAGNOSTIC / NOT_THEOREM / NOT_CANONICAL`
