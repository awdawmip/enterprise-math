# RS-R057Y-GRAVITY-STAR-RELAXATION-BRIDGE-DIAGNOSTICS

Status: DRIVER-ROUTED / NEW CROSS-TASK DIAGNOSTIC GENERATION / NOT CANONICAL

## 0. Purpose

Test, without any new fitting, whether the frozen R057 STAR boundary operators carry reproducible information along the already-frozen R055 gravity-relaxation trajectories.

This is a cross-task diagnostics bridge, not a continuation that may mutate R055 or R057. It must preserve both source generations byte-for-byte.

The scientific question is deliberately narrower than “derive gravity from STAR”:

> Along strict frozen R055 gravity descent, do STAR boundary observables exhibit stable trajectory-level compactification structure, and in particular is integrated `RUN_DEFECT_STAR` a useful coarse observable even if local STAR densities are not Lyapunov functions?

No theorem, gravitational field law, or physical identification is assumed.

## 1. Immutable frozen inputs

### R055 gravity source

Use the exact frozen R055 generation only:

- `R055_RELAXATION_PROTOCOL_SHA256 = aa69f2bc31cb9b5ec574a85de2879b9f8f765cfdfdb6dd0cbfc625cf8feed683`
- `R055_MOVE_ENERGY_REGISTRY_SHA256 = 83d546105a3fa721ba5cadea9a1bbf217a1661fdf0d1560fcdccc6d4c9d29ceb`
- `R055_INITIAL_STATE_REGISTRY_SHA256 = 5de0e7ae6ff89cf81342f6c18125eb1eebd78c4725c0324acee2893552acd7f2`
- `R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256 = 159ba8ed8e664522fec5fa9771b8efc7630d0b0c78ca5a2f67e7c33c724ac660`
- `R055_ARTIFACT_MANIFEST_SHA256 = 84d41e0d7c392576cfef8717eaa8fcdd6a5e780c02915b125e60043938dffdc7`
- full-sync source branch/head: `agent/r055-fixed-n-gravity-relaxation @ ea0781f564b8c4016d592521a50c02888e2f371d`

Primary data source: the frozen R055 relaxation trajectory corpus and its frozen move/energy protocol. Reconstruct states from the frozen initial state plus accepted moves when necessary; do not rerun move selection to create replacement trajectories.

### R057 STAR source

Use the accepted R057X C0R V2 STAR semantics only:

- `R057X_COMMON_DIMENSIONLESS_OPERATOR_PROTOCOL_V2_SHA256 = 3307339c0c2d1f41803a2d1b717635e096620a09f92fd292b900824822a8ef29`
- `R057X_CARRIER_UNIT_CONVERSION_REGISTRY_V2_SHA256 = 17cf3a4ca2be99ecd9679381e0df4f1afd3eccc299c050dd80c7f527acf1fec2`
- `R057X_DIMENSIONLESS_TRANSFER_TEST_PROTOCOL_V2_SHA256 = 0fa21641a749611a4b8e6b81991fd27f42a735be54f57e324c11550e49989940`
- `R057X_STAGE_C0R_CHECKPOINT_SHA256 = 30e44e4312d43e90777457e3213247ae7ff19ed3d26e7172844b59502269ffda`

Read-only semantic context may also use:

- `R057X_STAGE_C1_STAR_COMPARISON_CHECKPOINT_SHA256 = 1af2df3eefbb1eeee35418d59edf197657d91c1e14c47e8fdf319aab00a9c75d`

Do not consume A/G fitted coefficients. This task studies raw STAR observables, not fitted R057 corrections.

## 2. Mandatory genealogy disclosure: Driver pilot exposure

Before this taskbook was frozen, Driver ran a bounded N=19 pilot on four frozen R055 D1 trajectories: elongated strip, six-arm star, L-shape/wedge, and one EDEN seed.

The pilot suggested:

- gravity descent strongly reduces total boundary length;
- initial-to-final `sum RUN_SWITCH_STAR` and `sum RUN_DEFECT_STAR` decreased in all four pilot trajectories;
- mean signed `AREA_STAR` increased in all four;
- mean `RUN_DEFECT_STAR` was not uniformly decreasing;
- `sum RUN_DEFECT_STAR` had strong positive rank correlation with G on the three longer pilot trajectories, but was not stepwise monotone on all of them.

Therefore this full generation is **not blind to these pilot outcomes**. Label all task results:

`POST_DRIVER_PILOT_FULL_FROZEN_CORPUS_DIAGNOSTIC`

The pilot does not authorize tuning formulas, K, trajectory selection, thresholds, or weights.

## 3. Hard prohibitions

Do NOT:

- fit any coefficient;
- optimize any linear/nonlinear combination of STAR features;
- use pi or any R057 teacher target;
- modify R055 dynamics, move selection, tie-breaks, state predicates, gravity objective, or trajectories;
- modify R057 STAR definitions;
- add a gravity-radius, potential, field-strength, centroid-distance, or teacher-center feature;
- invent a new generator from the residuals in this generation;
- choose a subset of trajectories after seeing STAR results;
- tune K after seeing results;
- call a correlation a causal law or a theorem.

No weighted combination `alpha*AREA_STAR + beta*RUN_DEFECT_STAR` is permitted in this generation, fitted or hand-picked.

## 4. Stage Y0 — bridge protocol freeze before full computation

Before computing the full corpus, freeze:

`R057Y_GRAVITY_STAR_BRIDGE_PROTOCOL.json`

It must specify exactly:

- source hashes/heads;
- trajectory inclusion rule;
- state reconstruction rule;
- boundary extraction rule;
- boundary orientation convention;
- K=7 as the first-generation fixed packet length;
- STAR formulas;
- all summary statistics and hypothesis labels below;
- numerical tolerance policy;
- missing/unusable-state policy;
- no-fit/no-retune firewall.

Do not inspect full-corpus STAR results before Y0 is frozen.

## 5. Geometry bridge

R055 state sites live on the normalized triangular center lattice. Interpret each occupied site as the regular-hexagonal Voronoi cell of that center lattice solely for this derived boundary diagnostic.

Use the R057X C0R V2 A-side unit conversion:

- Voronoi boundary edge length `ell_edge = 1/sqrt(3)` in the R055 center-lattice Euclidean unit;
- endpoint chord `L_chord^2 = Q/3` in the corresponding boundary-edge axial coordinate;
- signed closure area conversion consistent with C0R V2.

The bridge must independently check, not merely assert, that the extracted boundary edge geometry has the C0R V2 unit identities.

For every hole-free connected state, extract each boundary component. Under frozen R055 admissibility the expected ordinary trajectory states are connected and hole-free; if a reconstruction violates this, hard-stop that trajectory and report source inconsistency.

Use occupied-on-left CCW boundary orientation.

## 6. STAR observables — fixed K=7 first generation

For every cyclic K=7 boundary packet compute, with no fitted coefficients:

- `SIGNED_AREA_DENSITY_STAR`
- `RUN_SWITCH_DENSITY_STAR`
- `CHORD_DEFECT_RATIO_STAR`
- `RUN_DEFECT_STAR = RUN_SWITCH_DENSITY_STAR * CHORD_DEFECT_RATIO_STAR`

Also record boundary edge count `B`.

For each state report both local-density and integrated forms:

- `mean_SIGNED_AREA_STAR`
- `mean_ABS_SIGNED_AREA_STAR`
- `mean_RUN_SWITCH_STAR`
- `mean_CHORD_DEFECT_STAR`
- `mean_RUN_DEFECT_STAR`
- `sum_SIGNED_AREA_STAR = B * mean_SIGNED_AREA_STAR`
- `sum_ABS_SIGNED_AREA_STAR = B * mean_ABS_SIGNED_AREA_STAR`
- `sum_RUN_SWITCH_STAR = B * mean_RUN_SWITCH_STAR`
- `sum_CHORD_DEFECT_STAR = B * mean_CHORD_DEFECT_STAR`
- `sum_RUN_DEFECT_STAR = B * mean_RUN_DEFECT_STAR`

Do not reinterpret these sums as physical energies. They are boundary-integrated diagnostics.

## 7. Stage Y1 — trajectory reproduction gate

For every included frozen trajectory:

1. reconstruct every state by applying the frozen accepted moves to the frozen initial state;
2. verify fixed N after every move;
3. verify every recorded source/destination occupancy transition;
4. verify reconstructed final state equals frozen final state;
5. verify the trajectory length matches `G_sequence`;
6. independently recompute or use the accepted R055 exact checker logic to verify each recorded G state / delta-G within exact declared semantics;
7. verify every accepted move is strict G descent.

Any source inconsistency:

`HARD_STOP_GRAVITY_BRIDGE_SOURCE_REPLAY_FAILURE`

No STAR interpretation is valid until Y1 passes.

## 8. Stage Y2 — full-corpus directional diagnostics

For every nontrivial trajectory (`move_count > 0`) and every observable X above, compute:

- initial X;
- terminal X;
- absolute change;
- relative change where denominator is safe;
- number/fraction of accepted steps with `Delta X < 0`, `=0`, `>0`;
- Pearson correlation of X with G where variance permits;
- Spearman correlation of X with G where variance permits;
- normalized trajectory progress profiles at fixed quantiles of accepted-move index and of G-drop fraction.

Also keep zero-move trajectories as terminal/metastability controls, but do not include them in stepwise monotonicity denominators.

Stratify by:

- N;
- initial family;
- D1 vs D2 R055 dynamics where both exist;
- tie-break;
- construction / strict holdout / other frozen regime;
- terminal D6 shape class if available from frozen R055 artifacts.

## 9. Stage Y3 — preregistered hypothesis tests

Evaluate all of the following. No hypothesis may be silently dropped because the pilot made it inconvenient.

### H-GS1 — local area Lyapunov hypothesis

`MEAN_SIGNED_AREA_STAR_DECREASES_WITH_GRAVITY`

Possible status:
- SUPPORTED
- FALSIFIED
- MIXED
- NOT_IDENTIFIED

Pilot expectation: likely falsified. Do not repair it.

### H-GS2 — local run-defect Lyapunov hypothesis

`MEAN_RUN_DEFECT_STAR_DECREASES_WITH_GRAVITY`

Same status vocabulary.

Pilot expectation: mixed. Do not repair it.

### H-GS3 — integrated run-defect compactification correspondence

`SUM_RUN_DEFECT_STAR_TRACKS_GRAVITY_COMPACTION`

Primary evidence:
- initial-to-final decrease frequency;
- trajectory-level Spearman distribution;
- robustness across N / initial family / tie-break / dynamics;
- stepwise monotonicity fraction.

This may be supported as a **coarse correspondence** even if it is not a stepwise Lyapunov function.

### H-GS4 — integrated run-switch compactification correspondence

`SUM_RUN_SWITCH_STAR_TRACKS_GRAVITY_COMPACTION`

Evaluate separately from H-GS3.

### H-GS5 — curvature concentration hypothesis

`GRAVITY_COMPACTION_CONCENTRATES_LOCAL_SIGNED_BULGE`

Operational evidence:
- boundary edge count decreases;
- mean signed/absolute area density increases while integrated/perimeter quantities are separately reported.

Do not call this continuum curvature unless an exact bridge is separately proved.

## 10. Stage Y4 — scale decomposition

The pilot indicates that local means and boundary-integrated quantities may move in opposite directions. Explicitly decompose each change into:

`sum_X = B * mean_X`.

For each step and each full trajectory, attribute the exact multiplicative/log change where defined to:

- boundary-count contraction component;
- local-density component.

This is descriptive decomposition only, not causal inference.

Answer whether the gravity signal is mainly:

- `PERIMETER_CONTRACTION_DOMINATED`,
- `LOCAL_DENSITY_CHANGE_DOMINATED`,
- `MIXED_SCALE_RESPONSE`,
- `NOT_IDENTIFIED`.

## 11. Stage Y5 — R056 secondary witness lane

Read-only optional secondary lane after Y0-Y4 freeze/results are persisted.

Use the frozen R056 one-cell support-radius-3 descent witness for r>=7 only as a separate symbolic/finite diagnostic. Compute before/after STAR boundary observables for the exact moved-cell geometry where feasible.

Do NOT use R056 to tune or repair the R055 hypotheses.

Label:

`SECONDARY_CROSS_GENERATION_WITNESS / NOT_PART_OF_R055_TRAJECTORY_STATISTICS`.

## 12. Required epistemic boundaries

Allowed conclusions include:

- `INTEGRATED_RUN_DEFECT_GRAVITY_COMPACTIFICATION_CORRESPONDENCE_SUPPORTED`
- `INTEGRATED_RUN_DEFECT_NOT_STEPWISE_LYAPUNOV`
- `LOCAL_STAR_DENSITIES_NOT_GRAVITY_LYAPUNOV`
- `BOUNDARY_CONTRACTION_WITH_LOCAL_CURVATURE_CONCENTRATION_SUPPORTED`
- `NO_ROBUST_GRAVITY_STAR_CORRESPONDENCE_FOUND`
- `MIXED_BY_INITIAL_FAMILY_OR_DYNAMICS`

Do not claim:

- Newtonian gravity;
- inverse-square law;
- physical gravitational potential;
- field equation;
- emergent general relativity;
- STAR operator = gravitational energy;
- theorem from correlations.

## 13. Required artifacts

At minimum:

- `R057Y_GRAVITY_STAR_BRIDGE_PROTOCOL.json`
- `R057Y_SOURCE_REPLAY_CHECK_RESULTS.json`
- `R057Y_STATE_STAR_ATLAS.json` or a hashed bounded equivalent if too large for source publication
- `R057Y_TRAJECTORY_STAR_SUMMARY.json`
- `R057Y_GRAVITY_STAR_CORRELATION_ATLAS.json`
- `R057Y_SCALE_DECOMPOSITION.json`
- `R057Y_HYPOTHESIS_LEDGER.json`
- `R057Y_GRAVITY_STAR_BRIDGE_CHECKPOINT.json`
- deterministic independent checker
- artifact manifest
- single complete Git bundle

Large raw/state atlases may remain bundle-only if repository liveness policy requires; exact byte SHA-256 must be frozen in the manifest.

## 14. Return questions

Return exact answers to:

1. Across the full frozen R055 trajectory corpus, how often does `sum RUN_DEFECT_STAR` decrease initial-to-final?
2. What is the distribution of Spearman(G, sum RUN_DEFECT_STAR), stratified by N/family/dynamics/tie-break?
3. Is `sum RUN_DEFECT_STAR` stepwise monotone often enough to call it a Lyapunov candidate, or only a coarse compactification observable?
4. Are mean local `AREA_STAR` and mean local `RUN_DEFECT_STAR` monotone? If not, freeze the counterevidence.
5. How much of the integrated STAR change is explained by perimeter contraction versus local-density change?
6. Does the six-arm / elongated / wedge / EDEN pilot pattern survive the full corpus and strict holdout?
7. Is there a robust difference between R055 D1 and D2 dynamics in STAR response?
8. Does the optional R056 escape witness align with the R055 full-corpus direction?
9. What, if anything, is now justified about a gravity-like interpretation of the R057 STAR generators?

Freeze and stop for Driver. Do not open a new fitted gravity operator generation.
