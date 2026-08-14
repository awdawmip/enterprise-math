# R058S Stage B2 — Edge/Corner Unblinding and Frozen-Grammar Interpretation

Researcher-ID: `EM-R058S-7C91E4`

Generation: `RS-R058S-EXACT-SQUARE-COLLAPSE-GRAMMAR-DISCOVERY`

Driver-ID: `EM-DVR-R0457K / CONTROL_PLANE`

## Frozen parent

Stage B1 exact head:

`81fba01c21a991208daa85bfa109705706534da0`

First serious blinded grammar checkpoint SHA256:

`00faf065bb1769f4df7d7e51cec8b8754c414f280666d785adc7ed554acd753b`

Stage-A checkpoint SHA256:

`e43da09e347503223cde29de378570e76e79e63f44fe2bd9195b6a7dd6b1a925`

All Stage-0 / Stage-A / Stage-B1 bytes are immutable.

## Purpose

Stage B2 is **post-search interpretation only**.

For the first time, reveal teacher-side square geometry and ask whether the already-frozen blinded collapse grammar corresponds to a finite macro decomposition into:

- straight-side collapse;
- corner-neighborhood collapse.

This stage must not improve the grammar. It may only label, cross-tabulate, decompose error, and classify evidence.

## Permanent prohibitions

Do not:

- refit any B1 grammar;
- change any composition leaf;
- change any predicate/score/parameter;
- run a new optimizer or candidate search;
- create a new grammar from the revealed roles;
- use holdout corpus or holdout predictions;
- expand `K>8`;
- use R057 fitted rules, coefficients, packet lookups, exception predicates, D1/D2/D3 winners;
- introduce rectangle, cube, circle, radius, circumference, arc, tangent, or pi;
- change carrier, digitization, packet extraction, D6 canonicalization, all-cyclic readout, or sample weights.

Any future grammar inspired by B2 is a new post-unblinding generation and cannot retain the blinded-discovery claim.

---

## LANE B2.0 — REPRODUCTION / FREEZE GATE

Before teacher-side role computation, reproduce:

- all Stage-0 hashes;
- all Stage-A hashes;
- Stage-A 20/20 checker;
- Stage-B1 protocol SHA256 `60ac08b1070327352f1090bead53e910aa7cf693ccae2a8bda8fb8d23a9f3f98`;
- Stage-B1 checkpoint SHA256 `00faf065bb1769f4df7d7e51cec8b8754c414f280666d785adc7ed554acd753b`;
- Stage-B1 independent checker 35/35 PASS;
- frozen B1 metrics for G0, G1-balanced, G1-min-RMSE, and G2.

If any scientific byte changes:

`HARD_STOP_B1_DRIFT`.

---

## LANE B2.1 — FREEZE TEACHER ROLE CLASSIFIER BEFORE READING COLLAPSE STATISTICS

This is the critical anti-postselection gate.

Create and hash:

`R058S_TEACHER_EDGE_CORNER_ROLE_PROTOCOL.json`

**before** computing any joint table of teacher role versus selected collapse count/composition.

The protocol may use only the frozen exact square teacher geometry and frozen packet geometry.

It must define a deterministic, exact/algebraic classification of every packet occurrence into at least:

- `SIDE_INTERIOR`;
- `CORNER_NEAR`;
- `AMBIGUOUS_ROLE`.

Recommended exact construction:

1. Use the four frozen square supporting halfspaces/side linear forms; no trigonometric angle parameterization.
2. For each packet boundary edge midpoint and/or packet vertex, compute the exact normalized slack/distance ordering to the four teacher supporting lines/segments in the square-axis algebra.
3. `SIDE_INTERIOR`: all tested packet points have one unique common nearest teacher side, with no adjacent-side tie and no endpoint/corner ambiguity under the frozen exact comparison rule.
4. `CORNER_NEAR`: the packet has deterministic association to two adjacent teacher sides / one teacher corner according to the predeclared exact criterion.
5. Anything not uniquely resolved is `AMBIGUOUS_ROLE`.

The researcher may choose an equivalent exact classifier, but it must be fully specified and frozen before role × collapse statistics are inspected.

Record:

- arithmetic field/representation;
- tie rule;
- exact side/corner association rule;
- any tolerance only if unavoidable, with exact-fallback behavior;
- D6/square-symmetry covariance check;
- role-classifier deterministic checker.

Do **not** choose the classifier to maximize separation of B1 compositions.

---

## LANE B2.2 — ROLE LABEL EXPOSURE

After the role protocol hash is frozen, label all 384 discovery-corpus packet occurrences for each `k=2..8`.

Create a teacher-role exposure census with:

- counts and fractions by role;
- counts by `k`;
- counts by side length, orientation, phase;
- ambiguity rate;
- symmetry/covariance audit.

Teacher roles remain interpretation metadata only; they are never fed back into the grammar.

---

## LANE B2.3 — FROZEN G0 WHOLE-CHORD INTERPRETATION

B1 found that for every `k=2..8`, the exhaustive G0 universal-composition winner is whole chord `(k)`, collapse count `c=1`.

Do not rerun selection.

Interpret this frozen result by reporting, for each `k`:

- fraction of `SIDE_INTERIOR` packets;
- fraction of `CORNER_NEAR` packets;
- role-wise B1 G0 error contribution;
- whether whole-chord is exact/biased on side-interior windows in aggregate;
- whether corner-near windows carry a disproportionate residual contribution.

This lane tests whether universal whole-chord is primarily a straight-edge law with corner defect, without assuming that answer.

---

## LANE B2.4 — FROZEN G1 COLLAPSE-COUNT × ROLE TABLE

Primary frozen structural candidate:

`G1_BALANCED_STRUCTURE_WINNER`, `k=5`, with:

- zero branch -> `(5)`, `c=1`;
- positive branch -> `(3,2)`, `c=2`;
- negative branch -> reflected `(2,3)`, `c=2`;
- score `PREFIX_SUFFIX_ABS_NET_TURN_DIFF`, parameter `2`.

Secondary frozen metric candidate:

`G1_MIN_RMSE_REFERENCE`, `k=8`, with:

- false branch -> `(8)`, `c=1`;
- true branch -> `(1,1,4,1,1)`, `c=5`;
- predicate `PREFIX_SUFFIX_DOT_NONPOS`, parameter `2`.

For both candidates report exact cross-tabs:

- role × selected composition;
- role × collapse count;
- role × split positions;
- role × predicate/score branch;
- composition entropy by role;
- conditional probabilities `P(c | role)` and `P(role | c)`;
- mutual information / concentration only as descriptive statistics, not fitted objectives.

Also report the same tables for every frozen per-k G1-balanced and G1-min-RMSE program already present in B1. No new candidate may be selected.

Core hypotheses to classify:

- `SIDE_WHOLE_CHORD_CONCENTRATION`;
- `CORNER_FINITE_SPLIT_ENRICHMENT`;
- `SIDE_CORNER_COLLAPSE_COUNT_SEPARATION`;
- `LOCAL_TEACHER_FREE_GRAMMAR_PREDICTS_ROLE`.

Allowed statuses:

- `SUPPORTED`;
- `WEAK_SUPPORT`;
- `NOT_SUPPORTED`;
- `NOT_IDENTIFIED`.

Do not rename a hypothesis after seeing results.

---

## LANE B2.5 — SAME LOCAL CLASS / DIFFERENT TEACHER ROLE TEST

A central locality question is whether the exact same teacher-free local packet type can occur both far along a square side and near a teacher corner.

For each `k=2..8` and each frozen D6 packet class:

- count role occurrences;
- identify classes appearing in both `SIDE_INTERIOR` and `CORNER_NEAR`;
- report role entropy within class;
- report whether the frozen G1 grammar assigns the same or different composition where its allowed local inputs differ despite the same canonical class key.

Classify:

- `LOCAL_PACKET_GEOMETRY_SUFFICIENT_FOR_ROLE_SEPARATION`;
- `ROLE_ALIASING_WITHIN_LOCAL_PACKET_CLASS`;
- `ROLE_SEPARATION_NOT_IDENTIFIED`.

Do not modify `K` to resolve aliasing.

---

## LANE B2.6 — EDGE/CORNER ERROR DECOMPOSITION WITHOUT REFIT

For the frozen G0/G1 candidates, decompose the sample-level estimator exactly as far as possible into contributions from packet-role strata:

`P_hat - 4s = E_side + E_corner + E_ambiguous`

under the frozen all-cyclic normalization.

For fixed orientation/phase and each available discovery side length, report trajectories of:

- `E_side`;
- `E_corner`;
- `E_ambiguous`;
- total error;
- role-window counts.

Test descriptively whether:

- side contribution grows proportionally with side length;
- side contribution is approximately/exactly zero-density while corner term remains bounded;
- corner contribution is finite-scale/constant/periodic across the discovery sizes;
- error is dominated by edge-density bias instead of a finite corner defect.

Allowed classifications include:

- `EDGE_DENSITY_EXACT_CORNER_DEFECT_REMAINS`;
- `FINITE_CORNER_CORRECTION_SUFFICES_ON_DISCOVERY_FAMILY`;
- `EDGE_DENSITY_BIASED`;
- `MIXED_EDGE_AND_CORNER_DEFECT`;
- `NOT_IDENTIFIED`.

No regression may be promoted to an all-scale theorem.

---

## LANE B2.7 — HIGH-CAPACITY G2 AS INTERPRETATION BENCHMARK ONLY

Use frozen G2 lookup only to ask whether its extra complexity is concentrated in a small set of role-associated packet classes.

Report:

- description units by role-associated classes;
- which G2 class decisions differ from whole-chord;
- role enrichment of those deviations;
- whether G1 compresses the same role structure.

Do not optimize or alter G2.

Do not claim role labels are legitimate grammar inputs merely because G2 aligns with them.

---

## LANE B2.8 — VERDICT

Return the strongest honest combination of:

- `STRAIGHT_WHOLE_CHORD_PLUS_CORNER_SPLIT_DISCOVERED`;
- `WHOLE_CHORD_IS_GLOBAL_BASE_BUT_CORNER_SPLIT_NOT_IDENTIFIED`;
- `OTHER_COMPACT_EDGE_CORNER_COLLAPSE_DISCOVERED`;
- `LOCAL_GRAMMAR_ROLE_SEPARATION_PARTIAL`;
- `EDGE_DENSITY_EXACT_CORNER_DEFECT_REMAINS`;
- `EDGE_DENSITY_BIASED`;
- `FINITE_CORNER_CORRECTION_SUFFICES_ON_DISCOVERY_FAMILY`;
- `SQUARE_COLLAPSE_STRUCTURE_OPEN_WITH_EXACT_BOUNDED_EVIDENCE`.

The headline `STRAIGHT_WHOLE_CHORD_PLUS_CORNER_SPLIT_DISCOVERED` requires at minimum:

1. strong concentration of frozen `c=1` on `SIDE_INTERIOR`;
2. strong enrichment of a finite `c>1` mode on `CORNER_NEAR`;
3. the association arises from the already-frozen teacher-free G1 program, not a role-aware post-hoc rule;
4. robustness across the discovery side-length/orientation/phase strata;
5. no material contradiction from ambiguous/mixed-role classes.

Otherwise use a narrower verdict.

---

## REQUIRED ARTIFACTS

At minimum:

1. `R058S_TEACHER_EDGE_CORNER_ROLE_PROTOCOL.json`
2. `R058S_TEACHER_ROLE_EXPOSURE_CENSUS.json`
3. `R058S_G0_EDGE_CORNER_INTERPRETATION.json`
4. `R058S_G1_EDGE_CORNER_COLLAPSE_LEDGER.json`
5. `R058S_LOCAL_CLASS_ROLE_ALIASING_ATLAS.json`
6. `R058S_EDGE_CORNER_ERROR_DECOMPOSITION.json`
7. `R058S_G2_ROLE_INTERPRETATION.json`
8. `R058S_STAGE_B2_UNBLINDING_RESULTS.json`
9. `R058S_STAGE_B2_CHECK_RESULTS.json`
10. `R058S_STAGE_B2_EDGE_CORNER_CHECKPOINT.json`

Return SHA256 for all required artifacts and especially:

`R058S_STAGE_B2_EDGE_CORNER_CHECKPOINT_SHA256`

Then STOP for Driver review.

## Holdout firewall

The Stage-0 holdout registry remains frozen but unconsumed throughout B2.

No holdout square corpus or prediction may be generated in this stage.

## Publication liveness

Use compact JSON/checkpoint/checker publication. Do not repeat the Stage-A base64/chunk pipeline. `CI_NOT_REQUIRED_FOR_RESEARCH`.

## Epistemic status

`POST_SEARCH_ROLE_UNBLINDING / DISCOVERY_INTERPRETATION / NOT_THEOREM / NOT_CANONICAL`
