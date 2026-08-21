# R061 Stage 1R — Native Line Trace Checker Replay / Reproducibility Repair

Task-ID: `RS-R061-STAGE1R-NATIVE-LINE-TRACE-CHECKER-REPLAY`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Identity: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r061-stage1r-native-line-checker-replay`

This is a narrow correction/reproducibility stage. It does not reopen Stage 0 and does not redesign the Stage 1 trace candidate unless the executable replay finds a real mismatch.

## 0. Read first / frozen inputs

Read first:

1. `definitions/ENTERPRISE_THREE_POSITIVE_AXIS_OVERLAPPING_CIRCLE_CELL_PLANE_20260820.md`;
2. `driver_reviews/R061_STAGE0_LINE_FORMULA_VALIDATION_DRIVER_REVIEW_20260820.md`;
3. `driver_reviews/R061_STAGE1_NATIVE_LINE_TRACE_DRIVER_REVIEW_20260821.md`;
4. frozen Stage 0 owner head `e6657ce00382d52acda319f0108b787a03e9d5f2`;
5. Stage 1 owner branch `research/r061-stage1-native-line-trace-realization`, especially:
   - `R061_STAGE1_NATIVE_OBJECT_TYPING_THEOREM.md`;
   - `R061_STAGE1_ORIGIN_INCIDENCE_AFFINE_ANCHOR_THEOREM.md`;
   - `R061_STAGE1_TRACE_LINE_CANDIDATE_AUDIT.md`;
   - `R061_STAGE1_THIRD_DIRECTION_LINE_IDENTITY_CLASSIFICATION.md`;
   - `R061_STAGE1_NATIVE_LINE_FORMULA_THEOREM.md`;
   - `R061_STAGE1_VALIDATION_SUMMARY.json`.

Driver status entering Stage 1R:

`STAGE1_MATHEMATICAL_CONSTRUCTION = PROVISIONALLY_ACCEPTED`.

`STAGE1_DETERMINISTIC_EVIDENCE_GATE = FAILED_AS_DELIVERED`.

`STAGE1_FINAL_ACCEPTANCE = PENDING_STAGE1R_REPLAY`.

Do not assume the Stage 1 claimed hashes are correct. Recompute them.

## 1. Hard objective

The only hard objective is:

`REPRODUCE_OR_FALSIFY_STAGE1_NATIVE_LINE_TRACE_VALIDATION_FROM_COMMITTED_EXECUTABLE_CHECKER`.

The stage succeeds only if an executable checker committed on the owner branch independently reconstructs the Stage 1 validation evidence from the frozen geometry and theorem definitions.

If any material mismatch appears, preserve the smallest exact mismatch and downgrade/correct the Stage 1 theorem instead of editing expected values to fit the old summary.

## 2. Mandatory checker artifact

Commit:

`scripts/r061_stage1r_validate_native_line_trace.py`

or an equivalently explicit deterministic executable with the same scope.

Requirements:

- exact integer/rational arithmetic for all incidence/combinatorial decisions;
- no floating-point angle/length decision;
- no hard-coded expected hashes as validation logic;
- expected frozen hashes may be compared only after independently regenerating the data;
- deterministic ordering of generated words/paths/records;
- nonzero exit on any failed acceptance invariant.

The checker must be sufficient for an independent reviewer to reproduce every machine-readable Stage 1 validation claim from repository state.

## 3. Reproduce Stage 0 frozen regression invariants

Without modifying Stage 0 artifacts, rerun/regenerate the frozen regression checks used by Stage 1:

- coordinate fiber `N=0..100000`;
- Stage 0 coordinate SHA256
  `0f4bccc2ff3fd7e7ae22ccd9e4abf248cf215bffea7bdd02aabca9b8c2bb8338`;
- Euclid square-hypotenuse audit through `r<=4096`;
- explicit shuffle through `a+b<=22`;
- explicit shuffle word count `8,388,607`;
- Stage 0 shuffle SHA256
  `572562117dbc2ba388543fbbeaa73bd26359ef47c26ef7ff31314ee92b318f93`;
- compressed Pascal through `a+b<=512`;
- Stage 0 Pascal SHA256
  `780c833ed685c707b2e57d70a2ecf015e56bc5196ee8e62a646720eb0707d002`.

A mismatch here is a hard stop and must be reported before native replay conclusions.

## 4. Exact carrier/origin incidence reconstruction

The checker must reconstruct the origin incidence geometry from the frozen carrier parameters:

`D_CENTER=1`, `R_CELL=1/sqrt(3)`.

Use exact carrier coordinates/rational quadratic form to verify:

1. exactly three cell centers are incident to `O_E`;
2. their pairwise center distance is exactly `1`;
3. their origin distance squared is exactly `1/3`;
4. no fourth nearest/next-shell center boundary passes through `O_E`;
5. each open 120-degree sector contains exactly one of the three incident centers;
6. no anchor center lies on a native number axis;
7. cyclic relabeling produces the same incidence counts.

Do not use this carrier quadratic form as native Enterprise line length.

Emit an exact machine-readable origin/incidence certificate.

## 5. Typed affine chart replay

Implement distinct typed records for:

- `VADDR_ij(a,b)` / coordinate vertex;
- `CADDR_ij(a,b)` / circle-cell center address;
- `C_ij(a,b)` / circle cell;
- `T_{a,b}^{(ij)}` / native line trace identity;
- path representative / prefix cell sequence.

Verify mechanically that:

`ctr(C_ij(a,b)) - V_ij(a,b) = s_ij`

is constant for every tested pair and each sector.

Verify that `V_ij(0,0)=O_E` while `ctr(C_ij(0,0)) != O_E`.

Verify terminal incidence of `C_ij(a,b)` with `V_ij(a,b)` using the circle equation at radius `1/sqrt(3)`.

No raw tuple may be silently treated as both a coordinate vertex and a cell center.

## 6. Trace-linearization native replay

For every pair `a,b>=0` with

`a+b<=18`, for all three sectors:

1. generate every shuffle linearization of `T_{a,b}^{(ij)}`;
2. prepend exactly the unique sector-local `Sigma_O^(ij)` incidence;
3. replay one circle-cell state per prefix;
4. verify every center transition is a nearest-neighbor carrier edge;
5. verify every prefix remains in the intended typed sector chart;
6. verify terminal typed endpoint `(V_ij(a,b),C_ij(a,b))`;
7. detect duplicate trajectories within one trace pair;
8. verify no simultaneous multi-cell state.

Recompute from scratch the Stage 1 claimed counts:

- pair count `190`;
- formal linearization count `524,287`;
- all-three-sector native path count `1,572,861`.

Recompute the Stage 1 native replay digest. Compare only after generation with the claimed digest:

`359474ba6b53ffbb3c326cf331d55dd3ed098837451a46b0754926b7c642d702`.

If the digest differs, determine whether ordering/serialization or mathematical content differs. Canonicalize serialization and preserve a semantic mismatch if present.

## 7. Compressed trace validation

Independently compute trace linearization counts through

`a+b<=256`.

Verify against exact binomial coefficients and trace recursion.

Recompute and compare the claimed Stage 1 compressed digest:

`aa0e3761f7446cf89e782c74b8020157b41713a37022daf44a2f8e95179e4ead`.

No copied digest acceptance.

## 8. Third-direction classification audit

For every tested nondegenerate `(a,b)` and especially `(1,1)`:

- enumerate/construct same-carrier-endpoint paths using the reverse third carrier direction where available;
- verify they are valid nearest-center circle-cell paths;
- verify they are **not** linearizations of `T_{a,b}^{(ij)}` unless an explicit component-preserving trace equality proves otherwise;
- verify the classification is based on native component labels, not jump count.

Mandatory exact witness:

`(1,1)`:

- trace reps `X_i X_j`, `X_j X_i`;
- carrier shortcut `-X_k`;
- same carrier endpoint;
- different native component trace.

If the checker discovers a third-family word that preserves the same native trace under the Stage 1 definitions, Stage 1 C1 is falsified.

## 9. Local commutation diamond audit

For every tested prefix cell and each sector, verify the local pair:

`X_i X_j`

and

`X_j X_i`

forms a valid commuting cell-incidence diamond:

- same typed start cell;
- two distinct legal intermediate cells when expected;
- same typed terminal cell;
- same native component multiplicities;
- all edges nearest-neighbor overlaps.

This is the executable incidence certificate supporting the trace commutation law.

## 10. Axis gluing, scaling, concatenation

Recompute rather than copy:

- physical-axis line identity gluing through radial coordinate `18`;
- distinct adjacent-sector anchor trajectories retained without accidental trajectory deduplication;
- scaling/concatenation audit for parameter grid through `8`;
- trace identity law
  `T_(a,b)*T_(c,d)=T_(a+c,b+d)`;
- concatenated representatives lie in the larger trace and adjacent-commutation closure reaches the full larger trace class at the tested ranges.

Preserve exact counterexample if any claimed Stage 1 composition statement fails.

## 11. Exact N examples

The checker must produce exact records for at least:

- `N=0`;
- `N=1`;
- `N=2`, branch `(1,1)`;
- `N=5`, `(1,2)/(2,1)`;
- `N=25`, including `(3,4)` and `(4,3)`;
- `N=65`;
- `N=169,289,625,841,4225`;
- scaled triples `(6,8,10)`, `(9,12,15)`, `(10,24,26)`, `(16,30,34)`, `(40,42,58)`;
- nonrepresentable `N` examples.

For `N=25` confirm from generated data, not a literal constant:

`|Realize_E(T_3,4)|=35`,

`|Realize_E(T_4,3)|=35`,

and fixed-sector total across `D_25` is `72` if and only if the axis branches and typing replay support that count.

## 12. Required outputs

Commit at least:

- `scripts/r061_stage1r_validate_native_line_trace.py`;
- `research_results/R061_STAGE1R/R061_STAGE1R_REPLAY_SUMMARY.json`;
- `research_results/R061_STAGE1R/R061_STAGE1R_ORIGIN_INCIDENCE_CERTIFICATE.json`;
- `research_results/R061_STAGE1R/R061_STAGE1R_TRACE_REPLAY_CERTIFICATE.json`;
- `research_results/R061_STAGE1R/R061_STAGE1R_MISMATCHES.json`;
- `research_results/R061_STAGE1R/R061_STAGE1R_REPRODUCIBILITY_PROOF.md`.

The proof must state the exact command used to run the checker and its exit status.

## 13. Final acceptance logic

If and only if the committed checker independently reproduces all material Stage 1 structural invariants and all claimed deterministic evidence, set:

`STAGE1R_REPRODUCIBILITY_PASS = true`.

Then Stage 1 may be returned to Driver for final acceptance of:

`NATIVE_LINE_PATH_FIBER_IS_EXACTLY_TYPED_AND_ALGEBRAICALLY_GENERABLE`.

If any mathematical mismatch survives canonical serialization/replay, set:

`STAGE1R_REPRODUCIBILITY_PASS = false`

and preserve:

- smallest failing `(sector,a,b)` or `N`;
- expected vs observed value;
- whether the failure attacks incidence, typing, trace identity, path replay, gluing, scaling, or only an old digest serialization.

Do not silently regenerate expected values.

## 14. Prohibitions

Do not:

- change `ENTERPRISE_RIGHT_ANGLE=120_DEGREES`;
- change `R_CELL=1/sqrt(3)`;
- change nearest-center spacing `1`;
- turn carrier `t_1+t_2+t_3=0` into a native Enterprise vector identity;
- use graph jump count as native line length;
- invent a balanced/Christoffel tie-break;
- discard third-direction same-endpoint routes from the endpoint-path object;
- reopen Stage 0 coordinate/shuffle theorem unless a regression mismatch is actually found;
- modify Stage 1 owner result files to hide mismatches.

## 15. Stop condition

Stop for Driver review after Stage 1R.

Do not open Stage 2 automatically from the researcher branch.
