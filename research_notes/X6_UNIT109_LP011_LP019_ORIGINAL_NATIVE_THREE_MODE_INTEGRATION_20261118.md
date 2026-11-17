# X6 Unit109 — full original-module integration for LP011/LP019 always-on native comparisons

**Scope:** Task `RS-X6-LEGACY-PLANE-RECONCILIATION`, publication `TP2-B4A441B23DA3159232C2`, frozen P000 V5 science @ `59538f585d037d09ef687b28715c4bc1a3f9fe03`. Author status: **SOURCE EXECUTED / INTEGER EXACT / UNREVIEWED / NOT ADMITTED**.

## Exact immutable source and executable boundary

Use existing opt-in Unit108 consumers, unchanged Git blobs `296e4cdb8b5710a6b2017f24e4b6059a2554714e` (LP011) and `c1842fbd34fb6fffa08a40a709b4838a6f2a5640` (LP019). Import the actual unchanged `experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py` Git blob `300a96e3dc24bf6fff73743037a0347a8bc83176`. All three local file bytes were verified against GitHub-returned blob IDs using Git object hashing. No external network or substitute module was used in execution.

Run both complete scripts against the original import, in Python normal, `-O`, `-OO`. A separate standard-library execution wrapper calls `sys.setprofile` and counts actual Python call-entry events with code filenames ending in the original native module path. This instrumentation does not mutate the native module or the two checkers.

## Results (six actual process runs)

| Consumer | Modes | Program-reported valid comparisons | Profiler-observed native API calls | Exit |
|---|---|---:|---:|---|
| LP011 shortest path | normal, -O, -OO | 3,375 each | `shortest_path_multiplicity` 3,375 each | 0 each |
| LP019 signed endpoint | normal, -O, -OO | 10,364 each | `endpoint_multiplicity` 10,368 each | 0 each |

The LP019 total contains 10,364 endpoint DP comparisons + 3 calls through `return_multiplicity` + one explicit odd-parity endpoint probe. The profiler independently counted 3 calls to `return_multiplicity` in each mode. For each consumer the complete emitted JSON stdout was byte-identical in three modes:
- LP011 SHA256 `fba4072526686d8bf1c1415c977f565d8c652788f34a9d58e5b85831a8f8ff33`.
- LP019 SHA256 `eae53806d60ac8cfc6e757b004cce2f5f2ee3d989a318801226de45b8e5fcfac`.

LP011 printed 3,375 signed points, 644 dominant ties, one zero case and 1,513 legacy-selector agreements. LP019 printed 625 exact four-counter histograms, 2,925 signed endpoint formulas in its two-axis model, six-axis endpoints at lengths 0..6 of [1,12,73,304,985,2668,6321], and original six-axis return counts at lengths 2 and 4 of 12 and 396.

## Negative pin experiment

A throwaway **separate local copy** of the original BRC file was altered by appending an inert comment. Its Git blob changed to `437f18a0357203ed78eabfbdea04682e1faeeab7`. The LP019 opt-in consumer explicitly rejected this mismatch with `RuntimeError` under all three modes, exit code 1. The actual original pinned source remained unchanged.

## Mathematical and engineering conclusion

**Unit108 original module import integration now has measured, genuine native calls and value comparisons across normal, -O and -OO.** The prior Unit107 optimized-`assert` native-call elision is fixed for the scoped calls. The elementary exact integer comparisons agree with the pinned six-axis signed BRC semantics.

Other secondary `assert` invariants in the opt-in checkers are checked in normal execution but elided in optimized modes; the fixed claim concerns native original API calls and their explicit equality tests. This is **not** an execution of the original frozen R063/Helly benchmark (support Issue #2416). Historical LP011/LP019 *original wrong* callsite provenance and 28-LP typed-consumer ledger remain separate open research, with independent Driver `REQUEST_REVISION` outstanding.

## Reproducibility

The machine-readable certificate `research_checks/X6_UNIT109_LP011_LP019_ORIGINAL_NATIVE_THREE_MODE_INTEGRATION_20261118_RESULTS.json` records original Git blob identities, each mode's captured stdout checksum, source-output values, real profiler entry counts, and the negative pin experiment. The program files of Unit108 remain at their existing immutable Git commits. The tested original implementation is byte-for-byte identical to existing GitHub source; the local external profiler is a measurement wrapper only.
