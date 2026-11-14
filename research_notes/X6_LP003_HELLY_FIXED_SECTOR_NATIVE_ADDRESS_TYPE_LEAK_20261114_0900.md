# X6 LP003 — live Helly fixed-sector output mislabelled as a native address

Date: 2026-11-14. Parent: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`.
Status: **AUTHOR-SIDE, SOURCE-ATTESTED BOUNDED CONSUMER FINDING / UNREVIEWED / NOT_ADMITTED / NO NATIVE SEMANTIC PROGRESS CLAIM**.
This is a new consumer-typing observation, not a new Helly theorem, Result, independent review, Task claim or change to a frozen source.

## Immutable baseline and actual producer

- Frozen P000 V5 `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json` (Git blob `c93d8150f1d223424b3506a6d2cdd5280b50825f`).
- Frozen signed native Cell torsor `@59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md` (blob `b4d49a1bbcccad0521618c6d20f6dcfa242b420a`), Sections 2–4: selected-Cell anchored native coordinates are **six signed integers**, with six signed unit-axis directions, native `G=Σz_i²`.
- Frozen 2026-09-05 old corpus pin: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.
- Actual current executable producer `scripts/tool_discovery_helly_radon_certificate_calculus.py` (current observed Git blob `31ca41fd628dd2728c3e0ac2f3e080d7e73e3217`; identical blob at old pin), lines 133–144: `S_12` is represented solely by local `(a,b)`, displayed as `(a,b,0)`. Lines 162–168: under `fixed_sector_chart`, the emitted field is `"sample_native_address": [5,3,0]`.
- Existing research result `research_notes/TOOL_DISCOVERY_ENTERPRISE_HELLY_RADON_CERTIFICATE_CALCULUS_RESULT_20260822.md` (current Git blob `cbcdf10909326e21a2b693718cfdfe16a242d356`), lines 499–543: its theorem is explicitly a fixed `S_12` chart with state space `N_0 × N_0`; nevertheless the prose says “native address” for `(5,3,0)`.

## Exact new finding

**The true result is a valid two-coordinate fixed-positive-sector intersection, but the executable field name and two prose occurrences presently promote that historical chart coordinate to a full native Cell address without the additional anchor and ordered signed-axis embedding required by P000 V5.**

The original three interval boxes are
`[2,7]×[1,6]`, `[5,9]×[0,4]`, `[4,8]×[3,9]`.
Direct exact interval intersection gives `a∈[5,7]`, `b∈[3,4]`; hence `(a,b)=(5,3)` and its **selected-chart notation** `(5,3,0)` are legitimate witnesses. Their pairwise/global Helly calculation remains intact. No original Helly theorem or supporting finite checker needs recomputation.

But a native position requires, at minimum, a chosen spatial Cell anchor and an ordered signed-axis interpretation. With a common anchor at native zero, two permitted but different axis declarations give

- `(i,j)=(1,2)`: `x=(5,3,0,0,0,0)`;
- `(i,j)=(1,3)`: `y=(5,0,3,0,0,0)`.

Both encode the same bare historical fixed-chart reading `(5,3,0)` once their respective chart embedding is declared, yet `x≠y` and the exact native squared distance is `Σ(x_i-y_i)²=18`. Thus the **undecorated chart output has no uniquely justified native six-axis identity**. This is a precise typing failure of a live result field, not a failure of interval intersection or an allegation about a historical author's intent.

## Bounded neighbouring checks: do not conflate algebraic cancellation with LP019

At the same frozen pin the following source bodies were fetched and examined as bounded neighbouring tools (this is not an exhaustive dependency closure):
- `experiments/tool_discovery_native_oriented_matroid_circuit_calculus_check.py`, blob `bce4453d740ac3c0c401843b732dc78c74056883`: `path_chain` and `sub` operate on *integer graph edge chains*. Their signed circuit elimination is not cancellation of positive N-BRC word multiplicities.
- `scripts/tool_discovery_discrete_morse_acyclic_matching_check.py`, blob `3bdd2a9ffc2d0bfd61f5bbaf338591d6ea232951`: lines 275–330 explicitly cancel only legal invertible incidences in a chain-complex reduction and reject an integer nonunit coefficient 2. Its rational coefficient cancellation does not establish path-count cancellation.
- `scripts/tool_discovery_helly_radon_certificate_calculus.py`, blob `31ca41fd628dd2728c3e0ac2f3e080d7e73e3217`: `typed_boolean_brc_support` (lines 148–174) is a Boolean support compatibility product, not a signed N-BRC multiplicity algebra.
The other freshly inspected frozen original script bodies `scripts/tool_discovery_carrier_voronoi_delaunay_dual_cell_check.py` (`900e246b0dafaa35d2452191e3df508a2d15a389`), `scripts/tool_discovery_discrete_laplacian_chip_firing_potential_check.py` (`f9799d3a9d86f68392d8fdf9aef8c9014775d7f2`), `scripts/tool_discovery_weighted_incidence_energy_dirichlet_check.py` (`e147d103e4e835877bc82b0a6001ab87c4b3b730`), `scripts/tool_discovery_discrete_conformal_circle_pattern_admissibility_check.py` (`1406b39b83c1a31f78a0930456840cfba157d451`), and `scripts/tool_discovery_helly_radon_certificate_calculus.py` were searched for the target dominant-axis/signed-count tokens without a target lexical hit. This negative finite observation is **not** a whole-program semantic proof or blanket KEEP judgment.

## Required scope-correct repair and next exact action

- Preserve the historical 2026-08-22 Result and its fixed-chart Helly-2 theorem as historical provenance.
- In the current executable output producer, after checking actual downstream consumers, retype `sample_native_address` as `sample_fixed_positive_chart_address` or an equivalently explicit selected-chart field, and declare the two-axis chart provenance. Add an explicit native coordinate separately **only if** a chosen native anchor and ordered axes are supplied; do not invent a canonical six-axis lift from the current data.
- Check the actual current consumers of the JSON field before changing its schema. This report demonstrates the output-field bug, not a successful patch or downstream compatibility test.
- Mother task residues remain unchanged: exact frozen LP011 wrong native argmax and LP019 wrong signed N-BRC cancellation callers still **UNRESOLVED_PROVENANCE**, and the 28-LP downstream dependency graph/Driver `REQUEST_REVISION` remain open. Do not misclassify graph-chain signs or Morse coefficient cancellations as LP019.
- Source semantic binding: original Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, CLAIM `MCP-899eb9f77ad9eebb90eb5f73`, RUN `RUN-87968b801c1dacea28269652` are historical pointers only until fresh current role/claim authorization. Pending exact resume request `onhour-20261114-0905-x6-own-run87968-resume-v1` must be read by original ID; do not duplicate.
- Original failed publication `onhour-20261114-0710-x6-chart-event-progress-v1` remains `FAILED / INVALID_UPLOAD_SET`. PR #81 allows zero-upload native research checkpoint upon **fresh** authorization, not automatic publication. Already saved GitHub research evidence is preserved independently.

Arithmetic check in this research turn: integer interval intersection and the two lifted endpoints were computed independently with `d_X6²(x,y)=18`; no original source script was rerun and no live native Task PROGRESS/CLAIM/Result is asserted.
