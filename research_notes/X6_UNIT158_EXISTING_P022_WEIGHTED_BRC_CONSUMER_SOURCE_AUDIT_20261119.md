# X6 Unit158 — P022 existing BRC geodesic consumer audit and Unit157 novelty correction

Date: 2026-11-19. Mother objective: PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905. Task: RS-X6-LEGACY-PLANE-RECONCILIATION / TP2-B4A441B23DA3159232C2. Original research lane: `chatgpt-research-onhour-enterprise-math-20260923`; provenance EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034. Status: **SOURCE-AUDITED / EXACT_FORMULA_CHECK_EXECUTED / UNREVIEWED / NOT_ADMITTED**. No independent review, Result, admission or worldview change.

## Finding: a previously implemented P022 consumer subsumes Unit157's root-weighted formula

The historical immutable comparison source `fd2bcff10ca6e147348b6c1236027fc0d2877df3` already contains:

- `src/enterprise_math/p022_geodesic_multiplicity.py` Git blob `46373050168d2430b6cb3952aa763f3081284632`, `a_geodesic_path_count` at lines 62–84, `sc_geodesic_path_count` at lines 87–97, `stirling_second` at lines 154–168, **`a_shell_total_geodesic_paths` at lines 171–203**. The latter is an explicit production function for the full *weighted* `A_p` shortest-root-path shell total, not merely the endpoint shell cardinality.
- Actual test consumer `tests/test_p022_geodesic_multiplicity.py` blob `ef3da1a789186867c538b604da1b642bf6039591`, tests `test_a_endpoint_formula_matches_independent_recursive_counts` line 109 and `test_shell_total_formulas_match_endpoint_sums` line 130. This directly tests the weighted-shell function.
- Separately `src/enterprise_math/lattice_geometry.py` blob `825ee26c918a4d7007e280aeaa1d7b750cd46aba`, `a_coordinator_shell_count` line 75, explicitly computes **endpoint count**, not BRC path multiplicity. Unit157 had inspected this latter function and its tests but omitted the P022 weighted-shell producer and its real test consumer.

Hence Unit157's `W_A` formula, claimed as a new weighted-shell theorem, is **not a new mathematical identity relative to the actual historical repository**. It is the P022 formula in the equivalent inclusion-exclusion notation. Unit156/157's cross-type interpretation remains a valid exact bridge to the X6 signed-native standard-axis path observer; P022 already provides the two endpoint count APIs from which that bridge follows algebraically. The work's remaining value is an explicit type-correct reuse map and extension of checked numerical instances, not novelty of the root weighted-shell identity.

## Full integer proof of reuse

For `n=p+1≥2`, `m≥1`, let `S(m,a)` be the second-kind Stirling number. P022 computes

`W_P022(n,m)=Σ_{a,b≥1,a+b≤n} C(n,a)C(n−a,b) a!S(m,a)b!S(m,b)`.

Unit157 uses `T(m,a)=Σ_{j=0}^{a} (−1)^j C(a,j)(a−j)^m`, exactly the number of onto functions from an m-element label set to an a-element alphabet. Partitioning onto functions by unlabeled nonempty fibers proves `T(m,a)=a!S(m,a)` for all relevant `m,a`; thus **`W_P022(n,m)=W_Unit157(n,m)` for all n≥2 and m≥0**, with m=0 separately 1.

For any zero-sum `x∈A_p` of root radius m, P022 defines `B_A(x)=(m!)² / Π_i |x_i|!` and `B_SC(x)=(2m)! / Π_i |x_i|!` because the standard-axis L1 radius is 2m. Therefore **`B_SC(x)=C(2m,m) B_A(x)`**, hence after summing the same immutable root shell **`W_SC^A(n,m)=C(2m,m) W_P022(n,m)`**. This is a derived typed comparison between root-generated and signed-standard-axis-generated paths, *not* an assertion that P000 native space has `A_p` root primitives.

P022's existing unconditioned `sc_shell_total_geodesic_paths(d,m)` is a different population (all Z^d endpoints at L1 radius m), and must not be substituted for the restricted zero-sum-root-shell `W_SC^A`. `a_coordinator_shell_count` is another different observer (distinct endpoints). This is the precise countermeasure against an invalid 28-LP source identification.

## New exact finite extension beyond Unit157's m≤4 check range

For the six-coordinate embedding n=6 and root radii 5–8, the two mathematically independent integer formulas give:

| m | P022 existing W_A = Unit157 W_A | C(2m,m) | restricted signed-native W_SC^A |
|---:|---:|---:|---:|
| 5 | 1,324,470 | 252 | 333,766,440 |
| 6 | 13,284,630 | 924 | 12,274,998,120 |
| 7 | 126,657,750 | 3,432 | 434,689,398,000 |
| 8 | 1,170,107,190 | 12,870 | 15,059,279,535,300 |

The independent reconstructed checker verifies 78 onto/Stirling values and 63 complete pairs `n=2..8, m=0..8`, using explicit exceptions. Normal, `-O` and `-OO` produce the same stdout SHA256 `e55725ccf288f20fa449599c287406325dd41d91b86efb28bda7de60cd904ca1`. This check reimplements formula semantics read from exact frozen source; **it does not execute the historical P022 module/tests or rerun Unit157's original DP / Unit50 R063 benchmark**.

Reproducible checker: `research_checks/X6_UNIT158_P022_UNIT157_EXISTING_FORMULA_REUSE_CHECK_20261119.py` at commit `4c0e190579dd724353a61e2960d52fb9972bf920` / blob `fc13f835d260283881368c44ceeeee1a22ad41b9`, sha256 `a4615a31c0b1c2c3b4c6c334b725b70bb2bceb61b795f1c5b33d12ff6768af9d`. Exact JSON: `research_checks/X6_UNIT158_P022_UNIT157_EXISTING_FORMULA_REUSE_RESULTS_20261119.json` at commit `1d0494356c79ae1420ddaffed725bdb41718d785` / blob `3c9b2a513bfb36e8e3810b60e115e9d96a17e3f8`.

## Provenance and remaining native work

This source audit identifies a *correct existing production implementation* and its actual test caller. It does not identify a buggy production caller, nor locate historical LP011/LP019 alleged erroneous `commit:path:line`. No general all-repository absence claim is made. The new source edge should be incorporated into the existing 28-LP ledger; do not duplicate P022 theory in a new native module.

Own Unit157 original Native PROGRESS `onhour-20261119-1530-x6-own-unit157-weighted-shell-native-progress-v1` is **SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED**, authenticated Source `c16945a91dbe0eb6be383a4db222d4b2d9b9a42b`, event `7002944633`. The completed Source fact does not imply mathematical novelty, author independence or admission.

Own current exact continuation read `onhour-20261119-1557-own-unit157-cont-v1` is SUCCEEDED as an **as-of read**, not write authority. Maintain original `EM-X6-FB6990 / MCP-082892eb480e45dea6d4b9fcc0491034 / MCP-dedc91932641535d284fc171 / RUN-c92057890282aaaeec520881` only while current native ownership and lease remain valid. Units149–152 author evidence exists with missing semantic association; terminal failed Unit149 request is never replayed. Other pending items: real remaining 28-LP downstream callers, exact LP011/019 provenance, independent Driver review. No maintenance identity, scheduler or notification changes.

**Next precise research action:** follow P022 geodesic path-count consumers and the remaining 28-LP records to isolate a real call expecting a different observer; check its actual inputs/returns against the typed bridge before alleging a bug. Source-derived classifications, proof, local exact tests and native publication/admission remain distinct.
