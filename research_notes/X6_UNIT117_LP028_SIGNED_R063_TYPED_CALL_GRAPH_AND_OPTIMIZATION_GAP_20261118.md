# X6 Unit117 — current LP028 native BRC call-site audit and optimized-mode validation gap

Date: 2026-11-18. Parent: `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`. Canonical task: `RS-X6-LEGACY-PLANE-RECONCILIATION` / `TP2-B4A441B23DA3159232C2`. Scientific inputs remain frozen: P000 centered signed X6 `59538f585d037d09ef687b28715c4bc1a3f9fe03`; historical plane `fd2bcff10ca6e147348b6c1236027fc0d2877df3`. Classification: `AUTHOR-SOURCE-ANALYZED / STANDALONE-EXACT-PYTHON-EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## Which concrete current LP028 program consumes the old R063 chart?

The actual original frozen `experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py`, blob `643b2bac659a445891dcb5588b647972977104e0`, defines `sector_ball` (lines 77–82), `residue` (85–88), `first_collision` (91–98), and `groots_square` plus `path_fiber_size` (136–149). The first pair are **fixed-positive modulo-sector** observables; they must not be confused with the separate six-dimensional relative/min-zero `rho(z)=z-min(z)` observer.

Actual current direct-import consumer `research_checks/X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py` (Git blob `db46dde5a962b93b65775bf2b4d8f52d5e3f83b9`):
- Lines 19–24 pin unchanged R063 / `x6_signed.py` / `signed_brc.py` blobs. Lines 40–42 import the original `groots_square,path_fiber_size`, native `Spatial6,full_distance_squared`, and native signed `shortest_path_multiplicity,endpoint_multiplicity,spatial_norm_squared`.
- Lines 45–65, especially 51–63, require a real `Spatial6` start, sorted distinct axis labels, two explicit signed polarities and ordered nonnegative original roots before embedding as native signed steps. The R063 root is typed as a chart component, **not** as full native Cell identity.
- Lines 67–94 count actual labelled chart roots, deduplicate axial endpoints, and compare chart-local binomial path mass with signed-native BRC. Original-source normal-mode author execution and 24,600 chart checks were previously reported in `research_notes/X6_LP028_SIGNED_CHART_NATIVE_BRC_CONSUMER_DEDUP_20261112_2300.md`; this unit **consumes** that evidence and does not rerun or rediscover its mathematical result.
- The newly identified exact verification weakness is at lines 78–81: `full_distance_squared`, `spatial_norm_squared`, `shortest_path_multiplicity` and `endpoint_multiplicity` are invoked only inside bare `assert` expressions. CPython `-O/-OO` removes the calls and comparisons, while the `checks += 1` counter at line 83, chart-local `path_fiber_size` calls at lines 77/88 and final PASS print at line 143 persist. The separate `require_source_pins` always-on explicit source check remains intact. Other bare checks for deduplication and translated start (e.g. 85–94, 141) are likewise removed.
- The exact positive root counts over `1<=r<=128` sum to 398; `r=50` has 6. Hence the declared per-program chart-root iterations equal `60*(398+2*6)=24600`. Under a successful original normal-mode execution, each of the two native BRC functions is called in every such iteration from its assert site. Under `-O/-OO`, **zero calls originate from those assert sites**. This is a source-execution fact, not a claim that this unit fully reran the original module.

## Nine-file bounded current LP028 caller census

Each of the following complete current-main source bodies was fetched, inspected and its Git blob recorded. **None** directly calls the original module's `residue()` or `first_collision()`.

| Current `research_checks/` basename | Git blob SHA1 | Typed source finding |
| --- | --- | --- |
| `X6_LP028_G25_FULL_SIGNED_NATIVE_SHELL_20261113_1700.py` | `d0693361c8e343c48cf7dc9a1983d20442dc79d4` | Local signed X6 shell and word combinatorics; no R063 modulo call. |
| `X6_LP028_G25_PATHSQRT_NATIVE_OBSERVER_COLLISION_BOUNDARY_20261113.py` | `aec58e8e0ebfc803138c74e02cc91967272274d2` | Defines a **different** relative/min-zero `rho` at line 22; calls `rho` at 59,70,84,85 and `brc` at 55,74,86. |
| `X6_LP028_NATIVE_NORM_PROBE_BRC_MINIMALITY_20261112_ONHOUR.py` | `365f1c59271be86b28a0d57b7480ccc806d8c8db` | Independent signed norm/BRC probes, no R063 modulo call. |
| `X6_LP028_NATIVE_NORM_PROBE_CAPACITY_20261112_ONHOUR.py` | `8b2ae2ca320a336d5fe92a1b55152dfd0576508d` | Two signed probe capacity, no R063 modulo call. |
| `X6_LP028_PATHSQRT_CHART_GLUE_TRACE_CAPACITY_20261112_ONHOUR.py` | `7b44e0e509b2eb9d02a2433977484c31a3ee9792` | Explicit ordered roots and chart-gluing; no R063 modulo call. |
| `X6_LP028_R063_ALL_PAIR_GLUE_20261112_ONHOUR.py` | `41939eff764b26ffd849c482c983aaec9fe9f56d` | Explicit `ordered_positive_roots` and signed embedding; no R063 modulo call. |
| `X6_LP028_R2500_FULL_NATIVE_SHELL_20261112_ONHOUR.py` | `4cedddae1cafca1004d19b849bb626712c0caa82` | Full signed shell standalone DP, not modulo-sector. |
| `X6_LP028_R25_ORDERED_CHART_VS_SIGNED_NATIVE_FIBERS_20261113_1100.py` | `ac4e10220a8aa41c512b6c1afbe8504da6734c64` | Explicit source chart-vs-native fibers, local BRC; no R063 modulo call. |
| `X6_LP028_SIGNED_PATHSQRT_TYPED_CURRENT_CONSUMER_CHECK_20261112_2300.py` | `db46dde5a962b93b65775bf2b4d8f52d5e3f83b9` | **Real** R063 root / binomial importer; signed X6 lift explicitly typed, but native correctness checks elided under optimized CPython. |

Source discovery used the current `research_checks` directory's 369-entry GitHub listing and full reads of the nine LP028-named candidates. This is a **nine-file current `research_checks` bounded census**; other names or directories are outside this census. Original 28-claim ledger and earlier LP023/A6 consumer audit remain canonical starting evidence.

## Independently executed precise Python control

A self-contained CPython program `research_checks/X6_UNIT117_LP028_ASSERT_CALL_ELISION_CHECK_20261118.py` enumerates exact ordered nonnegative square-root counts, and uses `compile(..., optimize=0/1/2)` on representative original `assert native()` and repaired always-on `if actual != expected: raise` forms. It actually ran in three interpreter modes (normal, `-O`, `-OO`), with byte-identical JSON SHA256 `65f542c6905bea28707df0bb325c9a4afb0b45bd985a776474db23e0c38e83be`. For good/bad injected native return values:

- Original `assert` case at optimization 0 invokes native once, passes correct value and rejects wrong value.
- Original `assert` case at optimization 1 and 2 invokes native **zero** times, and falsely passes the injected wrong value.
- Corrected always-on case invokes native once and correctly rejects the wrong value in every mode.

This control tests the exact relevant CPython `assert` behavior; it is **not** a complete three-mode import/run of the original LP028 consumer. The original normal-mode exact mathematics and source-pinned integrations from earlier units are preserved.

## Concrete repair/next native action

Preserve the original frozen R063 and existing current checker as prior evidence. For the existing LP028 source consumer, create a versioned strict `V2` adapter that moves all native calls outside `assert` and performs always-on comparisons including local chart/Cell embedding, BRC, union and return checks. Execute that `V2` against **unchanged source-pinned original** `groots_square`, `path_fiber_size`, `Spatial6`, `signed_brc.py` in normal/`-O`/`-OO`; verify each native BRC call counter is 24,600 and mutation tests fail in all modes. Do not claim native integration until actually run.

The alleged LP011 original incorrect native argmax and LP019 positive natural N-BRC cancellation callers still lack exact historical `commit:path:line` and remain `UNRESOLVED_PROVENANCE`. The independent Driver `REQUEST_REVISION` remains pending; original R063 same-object six-blob 512/512 author-run evidence is in Issue #2416 and requires independent authority/admission, not a new original benchmark run.

Original Source-protected Research session: SID `MCP-082892eb480e45dea6d4b9fcc0491034`, researcher `EM-X6-FB6990`, claim `MCP-3e221a50dc8818f914e228f6`, run `RUN-95866d78d35721116c362956`. Previous original request `onhour-20261118-0927-x6-own-units114-116-native-progress-v1` was independently reconciled this turn: `SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED`, verified Source `214daa797fc6db37c44be11c44d13e315c4daa70`; do not replay. Unit117 is an author research result, not an independent Driver acceptance or Task completion.
