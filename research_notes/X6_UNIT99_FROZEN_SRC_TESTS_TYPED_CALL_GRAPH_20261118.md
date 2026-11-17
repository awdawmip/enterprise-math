# X6 Unit99 — frozen `src/` → `tests/` typed BRC / signed call graph

Date: 2026-11-18. Lane: TASK_RESEARCH. Mother objective: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; canonical Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. Historical source `fd2bcff10ca6e147348b6c1236027fc0d2877df3`; immutable signed-X6 baseline `59538f585d037d09ef687b28715c4bc1a3f9fe03`.

**AUTHOR-SOURCE-INSPECTED / UNREVIEWED / NOT_ADMITTED.** This note documents verified historical source-reading and provenance classification, not a claim that original test binaries or the R063/Helly native benchmark ran.

## Scope and method

Continuation of the already-published Unit97 116-file `experiments/` and Unit98 56-file `scripts/` frozen-source audits. This Unit99 independently retrieved full contents of **27 direct `src/enterprise_math` entries and 27 direct `tests/` entries**, chosen by the identical basename filter:

`brc|signed|plane|dominanc|axis|coordinate|relative|space|native|slice|fcc` (case-insensitive).

These are **54 selected source records**, each located at the historical frozen commit. Their original Git blob IDs and exact paths are in the adjacent machine-readable manifest. Classification inspected import statements and the relevant signed/positive/observer/aggregation operations. This does not assert repository-wide coverage of every module or of tests whose basename is unrelated to that predicate.

## Actual typed edges and decisive witnesses

1. **Finite positive BRC: no signed-native X6 promotion.** `src/enterprise_math/brc_weighted.py`, blob `3f205696709e847909958a153f8fe10d3f6b70f0`, lines 1–9, 20–35, 40–69, 80–111, explicitly models a finite positive rational branch family as CWM `(count,total,dominant)`. `cwm_recoalesce` uses `(+,+,max)`; the maximum is over **branch weight**, not spatial axis. `tests/test_brc_weighted_foundation_tool.py`, blob `69963f8a1089a87b6fb48e648f15ef19bff70e56`, lines 26–45 and 108–112, checks exact positive merging and rejects `-1` as a branch weight. The actual import is `from enterprise_math.brc_weighted import ...` at test line 6. This source/test pair is a positive-path consumer with its own algebraic type, not LP011's alleged native X6 dominant-axis selection or LP019's alleged subtraction of natural N-BRC multiplicity.

2. **Newton coefficient cancellation is a different ring operation.** `src/enterprise_math/brc_newton_handoff.py`, blob `92dbddfd756562da7de31b480b4099cfde5e42ed`, lines 350–438, aggregates Taylor **coefficients** in `raw[residual][order] += coefficient`. `tests/test_brc_newton_handoff_resonance_foundation.py`, blob `d7f38f044659a0d94e43daaa42150ff80ea2270c`, lines 93–106, passes `(one,(1,-2,1))`, `(quarter,(1,))`, `(quarter,(-1,))` to `rational_newton_pushforward` and expects `edge_fiber.polynomial == (0,0,1)`. Signed **polynomial coefficient** cancellation is explicitly tested at the newton-resonance observer. It is not subtraction of nonnegative native path multiplicities.

3. **Other homonyms are typed separately.** `src/enterprise_math/signed.py` (blob `46386899c59483a9d83f8fe23387dbf8d20e18ec`) and `tests/test_p006_signed.py` (blob `e74d69aef5d853d587597770db4aecee8d5babc9`) manipulate signs of integer roots and collapses. `src/enterprise_math/euler_fcc_chirality.py` (blob `6f8b147c094720c2749f620a40394c4d7b67a386`) uses the signed sheet of a four-slice combinatorial cover, not six independent signed X6 Cell axes. The BRC critical `smallest-positive` selectors select scalar polynomial roots, not native spatial axes.

4. **Selected import-edge result.** Among the 54 fully read selected files, the inspected direct source imports and test consumers contain **zero direct imports of `x6_signed`, `x6_coordinate`, `signed_brc` or `x6_cover`**. Their positive BRC, Newton, signed integer-root and FCC chirality interfaces are independently typed. An unrelated filename/term such as `signed`, `native`, `dominant`, or `cancellation` is not evidence of X6 native-promotion fault.

## Exact mathematics of the classification

For the finite positive CWM source, parallel branches with weights `a,b>0` give `(2,a+b,max(a,b))`; signed polynomial coefficients `+1,-1` give `0` in a coefficient ring. These calculations operate in distinct carriers with different observers and state identities. No type-respecting map from *signed coefficient summation alone* can recover the original two positive branch occurrences: the coefficient pairs `(+1,-1)` and empty input both sum to zero, while their original path counts are 2 and 0. This is an exact two-input counterexample to the proposed lossless recovery, not a finding of misuse in the current sources.

## Mother-task disposition and next exact work

The alleged LP011 old wrong native dominant-axis source and LP019 old wrong subtraction of natural N-BRC retain **`UNRESOLVED_PROVENANCE`** across the inspected Unit97/Unit98/Unit99 populations. The actual Unit99 consumers above are classified **KEEP_CORRECT_TYPED_SOURCE**. Existing LP011/LP019 mathematical repairs and frozen original numerical evidence are consumed unchanged; their attribution should be reviewed by the independent Driver through the already existing `REQUEST_REVISION` path, with these pinned positive/negative witnesses.

Next useful action: inspect the historical **`research_checks/`** and theorem-facing/direct downstream reference edges that actually import the old R061/R062/path observer APIs, then finish the typed 28-LP dependency map. If a true incorrect *native* consumer is located, record its exact commit/blob/path/line/arguments and perform targeted repair. Avoid re-reading the Unit97/98 populations or reproducing this finite selection.

## Native writer and execution state

Original X6 Research lane `chatgpt-research-onhour-enterprise-math-20260923`; historical Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, Activity `RA-5E3FE1E761E4963EC461A892`. Current Sites recovery was read and lists prior runs as metadata, but `execution_authorized=false`. Exact own continuation request `onhour-20261118-0004-x6-own-exact-cont-read-v1` was **QUEUED** on last same-ID read; its effect must be read under the same request ID. No CLAIM/open/resume/Native PROGRESS mutation was submitted. Maintenance conversation lane remains untouched. Historical original benchmark and original source modules were not executed or rewritten.
