# X6 Unit115 — original LP028 modular-sector regression has optimized-mode false-PASS despite legitimate fixed-positive source inputs

**Date:** 2026-11-18. **Parent:** `PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905`; Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. **Author status:** `AUTHOR-SOURCE-EXECUTED / EXACT-INTEGER-VALIDATED / UNREVIEWED / NOT_ADMITTED`.

## Actual original-source verification

The original `experiments/tool_discovery_native_geometry_of_numbers_minima_calculus_20260822.py` has verified Git blob `643b2bac659a445891dcb5588b647972977104e0` at both frozen legacy `fd2bcff10ca6e147348b6c1236027fc0d2877df3` and current main. Its `check_spatial` around lines 101–131 performs modular-sector collision tests for moduli `m=2,...,20`, with seven bare `assert` guards. The input generator `sector_ball(R)` (lines 77–82) and the explicitly built grid points use the fixed nonnegative two-axis chart `(a,b,0)`. Source-pinned instrumentation **observed that every actual original checker residue call stays in this chart**; the defect below concerns optimized test verification, not erroneous original inputs.

The original function is imported unchanged by the new independent program, with exact Git blob checked. An AST reconstruction of **only the original function** converts its seven `assert` statements into semantically equivalent always-on `if not ...: raise RuntimeError` guards in a separately compiled callable. The original file and frozen Task inputs remain unchanged. Its original `residue` callable is instrumented to validate source input type and count every genuine call.

## Executed three-mode results

| Mode | Original `residue` calls | Always-on `residue` calls | Both original outputs | Inject constant-zero wrong residue, original | Same fault, always-on |
|---|---:|---:|---|---|---|
| CPython ordinary | 6,194 | 6,194 | same 19 rows / digest | `AssertionError` | `RuntimeError` |
| CPython `-O` | 228 | 6,194 | same 19 rows / digest | **false RETURN with 19 rows** | `RuntimeError` |
| CPython `-OO` | 228 | 6,194 | same 19 rows / digest | **false RETURN with 19 rows** | `RuntimeError` |

All three complete source-pinned test runs exited 0 with explicitly checked results. Valid original/strict output digest is `7e86e9e368032d8de24fd43461c8d71732f6d8bff86a7842d9d75308b6e188aa`. Corrupted original output in optimized modes retains 19 rows yet has digest `33cd6c86829707a66ffd569e87ae0723a188babe7b2b6601a303166dce6c0b5b`, demonstrating the false-PASS surface. In the optimized modes the original executes 228 reads due to unconditional Python expressions, while all calls located inside deleted assertions disappear; therefore equal row count alone is insufficient certification.

Exact executed code: `research_checks/X6_UNIT115_LP028_ALWAYS_ON_SPATIAL_ORIGINAL_SOURCE_CHECK_20261118.py`, Git blob `a8acf74320691cdfad613ccc06fd9602f9ae3cd1` and SHA256 `662daef6fa029d57fd668efb69e9ab052624470f09d2e6e10e38bc529e062799`. Complete mode-specific machine results: `research_checks/X6_UNIT115_LP028_ALWAYS_ON_SPATIAL_RESULTS_20261118.json`.

## Mathematical and repository typing

This is an exact reliability finding for the **unchanged original R063 fixed-positive two-generator modulo-sector program**. It gives a source-local validation repair that is independent of whether a broader signed-X6 projection is valid. The particular original `check_spatial` test points are properly typed positive chart points; preservation of all 19 correct chart rows is proved by actual source-pinned instrumentation across the specified moduli. A consumer may not upgrade these modulo-sector collisions into native Cell identity or native BRC counts without a separate typed lifting argument.

This unit is distinct from Unit114, which established the original `residue` input-gate bypass on off-plane/signed points. In the present unit we mutate the implementation of the residue calculation while keeping all supplied input points legal, exposing that the **original regression test itself** loses most of its mathematical guard calls in optimized CPython. The opt-in AST guard lift is executable verification material; it is not a patch of the frozen/current original checker.

**No original native R063/Helly C3/C4 benchmark was executed or replaced.** Support Issue #2416 retains its original target and acceptance conditions. The purported LP011 historical wrong dominant-axis and LP019 historical positive-count cancellation call sites remain `UNRESOLVED_PROVENANCE` pending independent Driver `REQUEST_REVISION` review. Existing mother 28-LP downstream consumer closure remains open.

## Control continuation

Research identity used for author activity: `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`, original CLAIM `MCP-3e221a50dc8818f914e228f6`, RUN `RUN-95866d78d35721116c362956` (as last verified in recovery/read-only control). Prior Native Unit112–113 PROGRESS original request `onhour-20261118-0852-x6-own-units112-113-native-progress-v1` is `SUCCEEDED / SOURCE_CHECKPOINT_PUBLISHED` with Source `e904de7f09680a8e0aa69744688e4cf248554572`. Original same-RUN resume `onhour-20261118-0834-x6-own-run9586-unit114-resume-v1` remained `QUEUED / error=null` on latest original-ID read; it is preserved, not resubmitted. Units114–115 GitHub author results and Activity are separate from Native semantic PROGRESS, which requires successful reauthorization and canonical owner CAS.

**Next exact task:** after original resume receipt becomes successful, check current winning own claim and authenticated writer generation, then checkpoint and publish Units114–115 to the **same original RUN** without duplicate previous PROGRESS. In parallel, source-trace live LP028 consumer calls of `residue/first_collision` with signed native points; if absent in the finite audited scope, give bounded negative evidence to Driver rather than claim universal nonexistence. The original R063 native execution issue remains separate.
