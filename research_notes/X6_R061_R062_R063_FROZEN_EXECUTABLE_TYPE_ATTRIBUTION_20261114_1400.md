# X6 historical executable provenance: R061 direction gauge, R062 natural BRC, R063 C4 interaction

Date: 2026-11-14 14:00 Asia/Hong_Kong.
Mother task: `RS-X6-LEGACY-PLANE-RECONCILIATION`; publication `TP2-B4A441B23DA3159232C2`.
Research lane: `chatgpt-research-onhour-enterprise-math-20260923`; inherited researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`.
Scientific status: **AUTHOR-VERIFIED SOURCE-AND-TYPE ATTRIBUTION / UNREVIEWED / NOT_ADMITTED**.
This is a new exact provenance finding, not a rerun of the original R061/R062/R063 benchmarks and not an independent review.

## Frozen input and source identification

Mother frozen current-native baseline: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`: P000 V5, native signed Cell torsor `Z^6`; selected signed `Z^3` slice. Historical pre-rebase comparison: `fd2bcff10ca6e147348b6c1236027fc0d2877df3`.

The earlier audits of frozen main `experiments/` did not cover the following original *research branches*. This audit reads actual full source bodies at pinned research branch commits (branch refs resolved, then file content read by immutable commit); the original frozen Driver review makes the historical task relationship explicit.

1. **R061 Stage 2**, original branch head `e20cb308e330d70fb62c6bfb1c67e2f9e861713f`, full source `scripts/r061_stage2_validate_arbitrary_point_line_gluing.py`, blob `2ff0fac51b2630ee94571ee0c109ccc2b137ebfb` (238 lines); historical Driver `driver_reviews/R061_STAGE2_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_DRIVER_REVIEW_20260821.md` at `fd2bcff10ca6e147348b6c1236027fc0d2877df3`, blob `7795f5b5fb2398c908e6c286ff5d42046ac030cb`.
2. **R062 Stage 0**, original branch head `879caabddf8ba049c2e9a26e723e6528cb71befa`, full source `scripts/r062_stage0_validate_brc_multipath_bridge.py`, blob `48ba38a55969b32fab40bc33d066b10216a249d0` (730 lines); frozen Driver blob `d46593b6c2c257d5ff43f653ab32eb0385b238dd`.
3. **R063 Stage 3**, frozen source head `69b7a90328bdb72852d47b338dedd7b276740ac9`, file `scripts/r063_stage3_validate_pairwise_interaction_process.py`, blob `4fca0c160acaa2b5d257d9bc1aefe82e1e3f4636` (125 lines); historical Driver `driver_reviews/R063_STAGE3_PAIRWISE_INTERACTION_SIGNED_CANCELLATION_DRIVER_REVIEW_20260822.md`, blob `32ab69b84c479f34846ae9addf4a601f80645194`; original PR #574. Stage 3 expressly limits its claim to the N1 derived two-axis process, not globally native N0 multiplication.

## Exact executable type and smallest witness

### R061: confirmed historical executable native-typing call, retyped on current main

At R061 Stage 2 **lines 43-45**, `can(p,q)` maps any carrier pair to `(p-m,q-m,-m)` with `m=min(p,q,0)`, and `vid(P)` labels `can(*P)` as `NATIVE_COORDINATE_VERTEX`. At **lines 207-217**, `reversal` tests squared `L2` gauges of the forward and reverse *min-zero decoding* as historic native direction length.

For the exact carrier displacement `Q-P=(1,0)`:
- historic positive/min-zero forward = `can(1,0)=(1,0,0)`, squared component gauge = `1`;
- historic reverse = `can(-1,0)=(0,1,1)`, squared gauge = `2`.

These are true computations about the historical **directed relative observer/chart gauge**, and the historic checker explicitly classified asymmetry as its negative metric outcome. In the current frozen centered signed native Cell torsor, the raw one-axis displacement is `+E_i` and its inverse is `-E_i`; both have squared native length `1`. There is no contradiction within either declared type; interpreting the old `vid`/decoded gauge as a current native Cell/metric is the exact historical source-level type leak.

Current main `definitions/ENTERPRISE_ARBITRARY_POINT_DIRECTED_LINE_GAUGE_20260821.md` is already explicitly `RETYPED / RELATIVE-OBSERVER GAUGE ONLY / SUPERSEDED AS NATIVE POINT-TO-POINT LENGTH` (read blob `875e3b274e5be03c5872f782872065a0b96d14eb`). Therefore **classification for this specific original executable is `SUPERSEDE_NATIVE / PRESERVE_OBSERVER`; no second rewrite of that current definition**. This resolves a named historical Stage 2 execution provenance candidate, but does not prove the LP011 `argmax` caller has been found.

### R062: actual historical positive multiplicity implementation does not subtract paths

At R062 Stage 0 **lines 151-163**, `n_brc_terminal_count(a,b)` adds `count` along two positive typed steps in a dictionary of nonnegative integer counts. **Lines 164-173** separately propagate Boolean support sets. The original theorem is a fixed two-generator, component-typed enrichment `PATH_FORMAL -> N -> BOOLEAN`; its `N=25` one-sector 72-word result is not the signed native six-axis shell. It does not implement a negative-to-positive cancellation of natural-number BRC multiplicity.

**Classification: `PRESERVE_PATH_BRC` at the original component-typed positive-chart scope; `NO_WRONG_POSITIVE_N_CANCELLATION_FOUND` in this exact source.** Current main R062 has already been retyped to signed X6 (read blob `97ab1403ab04b4fa80034625fb1b2e3ed115e59b`).

### R063 Stage 3: signed C4 process cancellation is a different algebra

At original R063 Stage 3 **lines 21-36**, the product first creates `C4`-labelled interaction cells; the `(ac-bd,ad+bc)` pair results from cancelling labels of opposite signed process phases. At **lines 40-57**, residual position-poset linear extensions then produce a source-sensitive `Counter` of target path witnesses; `Counter.update` *adds* these witness counts. At **line 120**, the output separately reports `R062_N_BRC:35`, Boolean support 1, `process_formal_witness_count:102`, and a different signed process normalization.

The frozen Stage 3 Driver itself accepts `N1_DERIVED_OPERATIONAL`, explicitly excludes `GLOBAL_N0_NATIVE_MULTIPLICATION`, and identifies position-retaining cancellation as nonconfluent (minimal `iij x ij`) even though count-level signed cancellation is confluent. Thus the name `SIGNED_CANCELLATION` is **not** evidence that the checker subtracts positive N-BRC path masses.

**Classification: `PRESERVE_DERIVED_PROCESS` with signed C4/source-poset and typed multiplicity layers; `NO_WRONG_POSITIVE_N_CANCELLATION_FOUND` at this exact caller.** Do not modify the frozen accepted process, infer a new native law, or use it as evidence that LP019's alleged wrong positive N-BRC cancellation has been located.

## Mother-task advancement and exact remaining evidence

This source audit directly identifies the original executable that produced R061 Stage 2 asymmetric min-zero `native` labels, verifies its present semantic retyping, and rules out two plausible but mistyped positive-N-BRC-cancellation attributions through full code reads. It removes these specific candidates from the pending historical-search set without asserting that the entire old corpus or current 28-LP dependency ledger is closed.

Remaining provenance: original LP011 *spatial argmax/dominant-axis* actual wrong caller (not the now-typed R061 reversal implementation) and LP019 *positive N-BRC* wrong sign-subtraction caller, if any; additional old branch/PR code and remaining current callers. Current active correctness and historical frozen semantics must be assessed separately. Native R063 C3/C4 benchmark has not been rerun.

Most valuable next action: locate the exact function and caller chain that consumes a spatial `argmax` as a native axis or subtracts positive `N`-multiplicity, using immutable historical branch/PR heads; record file/function/line/test and current descendant, and correct only active wrong-native consumers. Preserve X6/P000 frozen pin, original seven completed Source units, and independent Driver `REQUEST_REVISION` debt.
