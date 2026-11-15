# X6 R063 original same-object replay: optimized Python acceptance-bypass repair (unit 48)

**Date:** 2026-11-16 (on-hour Research lane). **Parent:** `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`. **Author:** `EM-X6-FB6990`, original Source session `MCP-082892eb480e45dea6d4b9fcc0491034`. **Status:** AUTHOR-EXECUTED REPLAY-ATTESTOR REPAIR / ORIGINAL SIX-FILE BENCHMARK NOT EXECUTED / NONBLIND / UNREVIEWED / NOT_ADMITTED.

## Exact functional defect and discriminating witness

The original same-object runner introduced by unit 47 used **28 Python `assert` statements** to enforce six frozen source blobs and the exact loader part inventory, all 13 expected output artifacts, 17 exact acceptance gates, the frozen discovery digest, exactly 512 regression rows and the original process exit / PASS. A Python interpreter run with `-O` or enabled `PYTHONOPTIMIZE` removes assertion statements. Thus the attestor could report source/output validity on a false synthetic input even when its claims were not checked. This is a defect in the *author-side acceptance wrapper*, **not** evidence against the historical original R063 theorem or its frozen six-file source.

Reproducing fixture: fabricate the six correctly named files with wrong Git blobs; separately supply 13 synthetic outputs with a false `PATHIFICATION_FORMULA_EXACT` gate and `tested_r_count=0` while keeping a self-consistent synthetic summary. Preserve the actual R063 frozen digests for the real future native replay; substitute a fixture-local hash **only in this test**. Execute the exact witness program below with the old/updated wrapper under both ordinary Python and `python -O`:

| Wrapper / Python mode | Wrong six-file source rejected? | `tested_r_count=0` and a false gate rejected? |
|---|---|---|
| Before fix, normal | YES | YES |
| Before fix, `-O` | **NO** | **NO** |
| Updated wrapper, normal | YES | YES |
| Updated wrapper, `-O` | YES | YES |

All four combinations were **actually executed in the local Python stdlib environment** and emitted the expected JSON classifications, exit code 0. The local witness includes the explicit `original_r063_benchmark_executed=false` flag. The previous acceptance code's optimized-mode false positive is a direct reproduced counterexample; the fixed check's success is a bounded runtime safety validation, not proof of the full old science.

## Minimal repair and source/byte evidence

- Historical first wrapper: [original unchanged commit](https://github.com/awdawmip/enterprise-math/blob/46731d958b284b1018658a70d55f15f1739edb6d/research_checks/X6_R063_PINNED_SAME_OBJECT_REPLAY_RUNNER_20261116.py); Git blob `8d89a2a82f0fd5eab0b21761cf3e1d667e3342b2`. Preserved as immutable provenance.
- [Corrected same-object wrapper](https://github.com/awdawmip/enterprise-math/blob/66859ef1caf0cf37fc2e503558fd597ea845b912/research_checks/X6_R063_PINNED_SAME_OBJECT_REPLAY_RUNNER_20261116.py): Git blob `0f46e872d9aafc2a9980e9f6cd26b01c46d7f2a9`; executable local exact bytes SHA256 `52b82abc911621f8f5296c78518b6d3d8c7ab85ffc01fa033ac747c6e459281a`. Replaces precisely 28 assertions with explicit `if not (...) : raise AssertionError(...)` checks; retains original 6 frozen blob pins, five-part exact inventory, `N=2500`, `r=1..512`, 17 original gate names, expected discovery/row digests, all 13 original output files and CLI invocation. Neither frozen R063 loader nor any `.inc` code changed.
- [Corrected stdlib regression test](https://github.com/awdawmip/enterprise-math/blob/8b764785f2552853dd33d6845d4379b88f173536/research_checks/test_x6_r063_replay_wrapper_20261116.py): blob `76e97f9dc90d177ed23bbb42c85fc46e6c1e1b1e`; replaces four test-only assertions with optimization-resistant explicit raises. Its exact checked-in candidate bytes were run with both `python` and `python -O`: `PASS_WRAPPER_SYNTHETIC_TESTS` in each mode, with wrong source, false gate and zero test count rejected.
- [Exact synthetic counterexample program](https://github.com/awdawmip/enterprise-math/blob/7ccb27047e0e7405ee6f0dd4361859c3840b6ac8/research_checks/X6_R063_PYTHON_OPTIMIZATION_ACCEPTANCE_BYPASS_WITNESS_20261116_0400.py): Git blob `57d9b89179d3daf5df06b873c1a5a3b5dcfcd239`, local SHA256 `b1c0c437154e70d975ea30db0fe8985f498c40e71ad0f2120e0a5a6ba6a2ac57`. Directly compares `check_sources` and `audit_outputs` for deliberately invalid synthetic data.

Source pins remain the exact six-file R063 owner branch `research/r063-stage0-path-valued-sqrt-2500`: loader `b4e000a6377f2858ae434eb0eecd0c25c33e8592` and parts `4a69c4d698887bce56323f393cb979609ce4ab0a`, `913078c642b8995bfc135ef0350912387a17cdb8`, `b543e185ec415b512c0ca0421616404cc12a19a7`, `4f1bbf72abed19dc7dc605371872ee31c501cebe`, `a1834a4b39a9d528760e67220b5fe5f368c9e655`. Original real row SHA256 expected `51891fbf9c3a66b1e00dfaa92fa6ae46984e4a6c99325624ec5b88371b66dcae`, discovery SHA256 expected `6dd26e75436fb6740134590fc243b59ab9eb287cadbc46d417d5bbbb74022f0d`.

## Original experimental debt and next exact action

**Original native benchmark remains NOT EXECUTED**. The [authorized environment support route #2416](https://github.com/awdawmip/enterprise-math/issues/2416) remains the real path; owner not established at this observation. Existing local Python can run the synthetic wrapper/witness but has no original authorized repository checkout containing the exact six frozen files. A responsible authorized runner must execute the repaired wrapper against the unmodified original branch in a fresh isolated output directory, record actual exit code and unchanged discovery-before-verification order, validate all 17 original gates, 512 distinct original radius cases, 13 output artifact hashes and frozen digests, then publish immutable actual evidence. This fix must not be used as substitute completion of the original native experiment.

Other X6 parent obligations remain: exact historical LP011 mistaken native dominant-axis caller, LP019 positive N-BRC cancellation caller (both historically UNRESOLVED_PROVENANCE in bounded audits), final 28-LP consumer coverage and independent Driver REQUEST_REVISION review. No task publication, scheduler, Foundation, Result, or Native author status is inferred from the GitHub changes.
