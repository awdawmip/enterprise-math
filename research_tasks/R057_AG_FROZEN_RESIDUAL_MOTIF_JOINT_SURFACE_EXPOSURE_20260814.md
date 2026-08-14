# RS-R057-AG-FROZEN-RESIDUAL-MOTIF-JOINT-SURFACE-EXPOSURE

Generation family: R057 / R057G / R057X

Purpose: expose the missing frozen diagnostic surfaces identified by accepted R057X Stage E, without refit and without inventing a new operator.

This task is executed independently by the A-arm owner and the G-arm owner. The two arms must not read each other's newly generated numeric exposure tables before both arm checkpoints are frozen.

## Frozen cross-arm anchors

- R057X_STAGE_E_COMMON_COMPONENT_CHECKPOINT_SHA256
  `3937572b2f8099f9ce125a86ccf90ec9aad6f9470b0af9ec4b8026df67796385`
- R057X_STAGE_D_RESIDUAL_STRUCTURE_CHECKPOINT_SHA256
  `7059ec68f6ace7cb46360476b7378b12b06dbb5a426269c20ae598e6bde1e771`
- R057X_STAGE_C1_STAR_COMPARISON_CHECKPOINT_SHA256
  `1af2df3eefbb1eeee35418d59edf197657d91c1e14c47e8fdf319aab00a9c75d`
- R057_A_STAGE_G_RESIDUAL_DIAGNOSTIC_CHECKPOINT_SHA256
  `4f2280c85a831b0270b03a15f377f7dbb51569351b513d9b79bd7aaac35ea0f0`
- R057G_STAGE_H_RESIDUAL_DIAGNOSTIC_CHECKPOINT_SHA256
  `21f051e5f2cfe276a1a746112968ca7d8ca6dedee2efe9fe006da94e47f9726b`

Stage-E disposition is `INSUFFICIENT` because the durable surfaces did not expose symmetric A per-transition nuisance arrays or sample-level frozen-residual x matched-motif exposure tables. This task fills only those evidence-surface gaps.

## Hard prohibitions

No coefficient refit.
No optimizer.
No symbolic regression.
No new teacher.
No teacher expansion.
No K expansion.
No new feature/operator/surrogate.
No parser/context/segmentation/assembly/readout mutation.
No cross-arm fitted rescaling.
No use of R057Y gravity evidence.
No residual-driven generator proposal.
No reading the other arm's newly generated numeric surface before own checkpoint freeze.

Deterministic replay/re-extraction from already frozen corpora, boundary words, packet catalogs, frozen predictions and frozen residuals is explicitly authorized.

## Common matched-motif semantics

Use only the already-frozen X Stage-B shared motif dictionary: 62 motifs covering all +/-1 turn words for k=2..6. Do not match raw A/G class IDs.

For exposure counting, use cyclic contiguous boundary windows of k=2..6 on the frozen teacher boundary, not model-dependent packet class IDs. This gives the same semantic counting object in both arms even though deployed segmentation differs.

Each window must be mapped to the frozen Stage-B semantic key when possible. If it is outside the frozen 62-motif domain, count it as `UNMATCHED_BY_FROZEN_62_CATALOG`; do not silently discard it.

For every sample and every motif key freeze at least:
- integer window count;
- fraction over all eligible k=2..6 cyclic windows;
- fraction over matched-catalog windows only;
- matched/unmatched denominator totals.

No learned motif weighting is allowed.

## Frozen residual surface

Primary residual is the already-frozen D2 sample residual from the arm's accepted STAR transfer stage. Do not recompute coefficients.

For each teacher sample expose:
- stable sample id;
- radius;
- phase;
- orientation when native to that arm;
- frozen D2 prediction;
- frozen D2 signed residual;
- absolute residual;
- within-radius signed residual rank/percentile;
- within-radius absolute-residual rank/percentile.

If a quantity is already stored, byte/recompute-check it. If reconstructed deterministically, record the exact reconstruction formula and upstream hashes.

D1 residual exposure may be published as a secondary sensitivity surface, but D2 is primary. Do not add D3-only hotspot selection because D3 is already rejected as a common stable basis.

## A-arm execution: R057-A Stage H

Researcher-ID: `EM-R057-6A31F2`

Use only frozen TD000+TD001, K<=8 carrier data, Stage-F STAR predictions/residuals and Stage-G diagnostics.

### A-H0 reproduction gate

Reproduce the accepted Stage-G / Stage-F D2 sample predictions and aggregate metrics before exposure extraction. Any unexplained mismatch is `HARD_STOP_SURFACE_INVALID`.

### A-H1 sample residual x motif exposure table

Build the common-schema sample table described above from frozen A cyclic boundary words and the frozen 62-motif semantic dictionary.

Important: matched motif exposure is counted on all cyclic k=2..6 subwindows, not on raw K7 class IDs and not only on the packet decomposition selected by the solver.

### A-H2 per-transition nuisance surface

Expose the per-radius-transition arrays that Stage E could not instantiate from the durable A summary. Recompute deterministically from frozen Stage-G inputs using the exact Stage-G definitions, with no residual-driven selection.

At minimum freeze for each successive radius transition:
- deployed packet/class-mixture total variation;
- AREA_STAR / RUN_DEFECT_STAR covariance and correlation endpoints;
- covariance leading-eigen share endpoints;
- principal-axis rotation angle when defined;
- any Stage-G concentration/entropy statistic actually used;
- phase weights and the fact they remain equal if applicable.

Also freeze exact definitions and denominators.

### A-H3 integrity / no-selection audit

Verify motif extraction and nuisance arrays do not depend on residual magnitude or sign. The only residual columns are readouts joined after the exposure surface is defined.

### Required A artifacts

- `R057_A_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE.json`
- `R057_A_FROZEN_TRANSITION_NUISANCE_SURFACE.json`
- `R057_A_JOINT_SURFACE_INPUT_REGISTRY.json`
- `R057_A_STAGE_H_JOINT_SURFACE_CHECK_RESULTS.json`
- `R057_A_STAGE_H_JOINT_SURFACE_CHECKPOINT.json`
- deterministic checker
- delivery manifest / bundle as normal research delivery

Freeze and return:
`R057_A_STAGE_H_JOINT_SURFACE_CHECKPOINT_SHA256`

Then stop. Do not perform enrichment analysis or new generator search.

## G-arm execution: R057-G Stage I

Researcher-ID: `EM-R057G-93D4A8`

Use only frozen T0+T1, K<=6 carrier data, Stage-G STAR predictions/residuals and Stage-H diagnostics.

### G-I0 reproduction gate

Reproduce the accepted Stage-H / Stage-G D2 sample predictions and aggregate metrics before exposure extraction. Any unexplained mismatch is `HARD_STOP_SURFACE_INVALID`.

### G-I1 sample residual x motif exposure table

Build the same common-schema sample table from frozen G cyclic contour boundary words and the same frozen 62-motif semantic dictionary.

Count all cyclic k=2..6 subwindows, even though G deployment is fixed-K6 plus canonical remainder. The common exposure object is the local boundary window, not the deployment segmentation block.

### G-I2 per-transition nuisance surface

Persist the already diagnostic-relevant per-radius-transition quantities in a durable explicit table, including at least:
- motif concentration/entropy and successive change;
- AREA_STAR / RUN_DEFECT_STAR correlation endpoints and absolute change;
- covariance leading-eigen share endpoints;
- phase/orientation weights;
- any Stage-H covariance/eigenspectrum quantities needed to reproduce its nuisance-light ranking.

No new statistic selected from residual outcome may be added as a gate variable.

### G-I3 integrity / no-selection audit

Same as A-H3. Exposure definitions are residual-blind; residual columns are joined afterward as frozen readouts.

### Required G artifacts

- `R057G_FROZEN_SAMPLE_RESIDUAL_MOTIF_EXPOSURE.json`
- `R057G_FROZEN_TRANSITION_NUISANCE_SURFACE.json`
- `R057G_JOINT_SURFACE_INPUT_REGISTRY.json`
- `R057G_STAGE_I_JOINT_SURFACE_CHECK_RESULTS.json`
- `R057G_STAGE_I_JOINT_SURFACE_CHECKPOINT.json`
- deterministic checker
- sparse publication index plus bundle according to the established G delivery convention

Freeze and return:
`R057G_STAGE_I_JOINT_SURFACE_CHECKPOINT_SHA256`

Then stop. Do not perform enrichment analysis or new generator search.

## Driver review after both arms freeze

Driver will verify both surfaces use exactly the same 62-motif semantic keys and counting convention, no cross-arm new numeric leakage occurred before each arm froze, and no residual-dependent exposure definition was introduced.

Only after both checkpoints are accepted may R057X resume with a new stage to compute matched residual enrichment / hotspot isolation. A new omitted generator remains unauthorized until that X comparison finds a nontrivial cross-carrier residual signature beyond common early finite-scale burden.

Epistemic label for both arm outputs:
`FROZEN_POST_FIT_JOINT_DIAGNOSTIC_SURFACE / NO_REFIT / NOT_THEOREM / NOT_CANONICAL`
