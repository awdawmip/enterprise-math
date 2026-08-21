# R061 Stage 1R — Native Line Trace Final Driver Acceptance

Status: `ACCEPTED / FROZEN`
Date: `2026-08-21`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

## 1. Reviewed sources

Stage 1 taskbook source:

`4183c1300994e61f5a4443aea8487438a7210cc6`

Stage 1 owner branch:

`research/r061-stage1-native-line-trace-realization`

Stage 1R taskbook source:

`2fd179aa22db7fdc292817f24cb7f65008eb4b16`

Stage 1R owner branch:

`research/r061-stage1r-native-line-checker-replay`

Stage 1R frozen owner head:

`653071b8e230d1e707e0544cab22ad2a408b92bd`

The Stage 1R branch is exactly one commit ahead of its taskbook source and contains only the checker/replay package required by the correction stage.

## 2. Evidence-gate resolution

The Stage 1 provisional acceptance was blocked only because the claimed deterministic replay was not committed as executable evidence.

Stage 1R closes that gate.

Committed executable entrypoint:

`scripts/r061_stage1r_validate_native_line_trace.py`

The checker reconstructs the relevant data from exact integer/rational carrier arithmetic and combinatorics. Frozen Stage 0 and claimed Stage 1 digests are used only as post-generation comparison targets; the checker does not read the Stage 1 summary as generated evidence.

Freeze:

`STAGE1R_REPRODUCIBILITY_PASS = true`.

`R061_STAGE1_EVIDENCE_GATE = CLOSED_PASS`.

## 3. Exact replay results

Stage 0 regressions reproduced exactly:

- coordinate fiber `N=0..100000`: SHA256 `0f4bccc2ff3fd7e7ae22ccd9e4abf248cf215bffea7bdd02aabca9b8c2bb8338`;
- explicit shuffle through `a+b<=22`: `8,388,607` words, SHA256 `572562117dbc2ba388543fbbeaa73bd26359ef47c26ef7ff31314ee92b318f93`;
- compressed Pascal through `a+b<=512`: SHA256 `780c833ed685c707b2e57d70a2ecf015e56bc5196ee8e62a646720eb0707d002`;
- Euclid square-hypotenuse audit through `r<=4096`: zero mismatch.

Native Stage 1 replay reproduced exactly:

- origin incident cells: exactly `3`;
- affine typed endpoint records: `570`, zero mismatch;
- trace pairs `a+b<=18`: `190`;
- formal linearizations: `524,287`;
- three-sector native paths: `1,572,861`;
- native replay SHA256 `359474ba6b53ffbb3c326cf331d55dd3ed098837451a46b0754926b7c642d702`;
- compressed trace through `a+b<=256`: SHA256 `aa0e3761f7446cf89e782c74b8020157b41713a37022daf44a2f8e95179e4ead`;
- non-neighbor, endpoint, sector-prefix, simultaneous-state and within-trace duplicate counts: all `0`;
- local commuting diamonds: `570`, zero mismatch;
- physical axis identities through radial coordinate 18: `57`; chart presentations `114`; erroneous trajectory deduplication `0`;
- scaling cases: `729`; concatenation cases: `6,561`; explicit commutation-closure words: `131,071`; zero mismatch;
- final mismatch file: `mismatch_count=0`.

For `N=25` in one fixed sector:

`D_25={(0,5),(3,4),(4,3),(5,0)}`

with branch path counts

`1 + 35 + 35 + 1 = 72`.

## 4. Final accepted native line semantics

Freeze the object split:

1. `V_ij(a,b)` — coordinate/triple-intersection vertex carrying native components and native length;
2. `C_ij(a,b)` — terminal circle cell in the affine center chart;
3. `T_{a,b}^{(ij)}` — native line identity;
4. `Sigma_O^(ij);w` — one native single-cell path representative.

For a fixed native right sector `S_ij`, define

`T_{a,b}^{(ij)}=[X_i^a X_j^b]`

under the component-preserving commutation relation

`X_i X_j ~ X_j X_i`.

Its native realizations are exactly

`Realize_E(T_{a,b}^{(ij)})={Sigma_O^(ij);w : w in Sh_{a,b}(X_i,X_j)}`.

The terminal typed endpoint is

`END_E^(ij)(a,b)=(V_ij(a,b),C_ij(a,b))`.

The native length is owned by the vertex/component object:

`L_E^2=a^2+b^2`.

Freeze:

`ENTERPRISE_LINE_IDENTITY = NATIVE_COMPONENT_TRACE`.

`ENTERPRISE_LINE_PATH_FIBER = ALL_NATIVE_TRACE_LINEARIZATIONS_AFTER_TYPED_ORIGIN_INCIDENCE`.

`SAME_ENDPOINT_PATH != SAME_LINE_PATH` in general.

A reverse-third-family carrier shortcut may reach the same carrier endpoint but is not a member of the same `ij` native component trace. Its accepted classification is:

`CARRIER_ONLY_SHORTCUT_NOT_NATIVE_LINE`.

This distinction is made by native component identity, not by jump count.

## 5. Correct native sector-local line formula

For

`D_N={(a,b) in N_0^2 : a^2+b^2=N}`,

freeze

`LINE_E^(ij)(N) = disjoint_union_{(a,b) in D_N} Realize_E(T_{a,b}^{(ij)})`.

For one coordinate branch,

`|Realize_E(T_{a,b}^{(ij)})|=binom(a+b,a)`.

In particular:

`|Realize_E(T_{3,4}^{(ij)})|=35`.

Thus the native length `5` is one algebraic resultant/line identity branch with many discrete single-cell path representatives; it is not a unique visually straight carrier path and is not the seven center-transition count.

## 6. Scope boundary

This freeze is exact for origin-based lines in one fixed native right sector, together with cyclic transport across the three sector labels and axis gluing.

It does **not** yet solve arbitrary point-to-point lines whose start is not `O_E`, nor a general cross-sector displacement/metric law.

Freeze open boundary:

`ARBITRARY_POINT_TO_POINT_NATIVE_LINE = OPEN`.

`CROSS_SECTOR_POINT_TO_POINT_METRIC_AND_TRACE_GLUING = OPEN`.

## 7. Driver verdict

Stage 1 and Stage 1R are accepted and frozen.

`NATIVE_LINE_PATH_FIBER_IS_EXACTLY_TYPED_AND_ALGEBRAICALLY_GENERABLE = true`.

`NATIVE_LINE_PATH_FIBER_DERIVABLE_FROM_CURRENT_FOUNDATION = true`.

`R061_STAGE1_FINAL_ACCEPTANCE = PASS`.
