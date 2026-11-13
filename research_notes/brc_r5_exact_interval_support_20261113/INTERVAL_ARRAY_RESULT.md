# R5 exact interval array: completed implementation and cold-process test

**Date** 2026-11-13. **Scope** author-side exact verification, unchanged frozen scientific input `435e77af0d180eac32bd1f9c4c464bc4010b7551`. This report extends the interval-support theorem in this same directory and Draft PR #2287.

## Implementation and exact results

`VERIFY_R5_INTERVAL_ARRAY_DP.py` uses exact interval endpoints for every suffix layer, representing the min-plus/tied-optimal-count rows as triples `(start_index, cost_list, count_list)`, indexed directly by `p-start_index`. It reconstructs the original 953 rational activation walls and 954-event-boundary array directly from the frozen 15-atom integer coefficients, then derives the 4,383 legal R=2 graph edges. It decodes the exact historical 56-byte center list, constructs 213 rows, un-ranks the original 12-byte optimal-path rank, re-ranks the reconstructed centers, and constructs the 954-byte nearest-center directory.

The actually executed local CPython exact checker produced:
- `J_min=1070`.
- `T_opt=1338767625695954932334592000`.
- `rank=417027933051277583800994379` (12-byte big-endian payload `0158f5198cd12c63a2ba0a4b`).
- 213 original center indices, exactly identical to earlier verified rank and 56-byte gap codec.
- 83,813 exact interval DP cells.
- 954-byte direct directory matching the historical output: SHA-256 `a947d07d7d494e00e14013eb929b3ffdc9224938ec15289209e68316c50a14b1`.
- 213 center indices serialized as `uint16 little-endian`: SHA-256 `b6d9f351d2ed5c41e8b6061de6517519037fdb3918dd7656f420e584e8bda4a1`.

These identities support direct substitutivity at the boundary-selection layer; the original 2,880-prefix query oracle was **not** executed in this new run.

## Fresh-process workload

Nine fresh Linux CPython subprocesses per variant execute the same exact R5 `15-atom Fraction fixture → legal radius graph → DP → original rank unrank → direct directory` workload. The paired baseline `DICT_DP_ENGINE.py` uses the prior radius-limited nonzero-support dictionary recurrence. The new method uses the proved contiguous intervals and direct list offsets. The results are local process medians, not universal performance bounds:

| Variant | Cold workload median | DP + unrank + directory median | Peak process RSS |
|---|---:|---:|---:|
| Previously support-pruned dictionary | 0.183467 s | 0.109097 s | 112,928 KiB |
| Exact contiguous-array recurrence | **0.146970 s** | **0.073615 s** | **103,812 KiB** |

The measured difference in this specific workload is 0.036497 s (19.89%) in cold elapsed, and 9,116 KiB (~8.07%) in process peak RSS. Each process includes interpreter startup imports before the measured `perf_counter` clock begins; thus `cold_seconds` is **from fixture computation onset**, not total process launch latency. The `resource.getrusage` peak RSS is over the whole process, including imports, and is platform-specific. The dictionary baseline module imports its exact fixture at module load, before the explicit measurement start; the subprocess `-c` code imports both implementations before starting the clock. This is a **measurement comparability limitation**: both use the same fixture and final outputs, but some baseline-specific setup takes place before the measured clock. Do not regard the ~19.89% comparison as an uncontaminated end-to-end or portable speedup.

`BENCH_R5_COLD_SUBPROCESS.py`, `DICT_DP_ENGINE.py`, and `COLD_RESULT.json` preserve the workload, baseline and measured figures. The mathematical work uses exact integers and fractions; timing uses ordinary clocks.

## Open next question

1. Refactor both implementations to eliminate module-import-time fixture computation and measure true process-launch-to-JSON elapsed time, including all construction and teardown for both variants.
2. Run the original frozen 2,520-byte compressed certificate-seed decode, 2,880 prefix nodes and complete **2,747,520 boundary × prefix-node** oracle, including true rational-parameter queries.
3. Compare the reduced-memory blockwise interval strategy as well as dense, dictionary and array rows, then report reproducible overall RSS and query-throughput tradeoffs.

GitHub Draft PR preserves this result; project Task owner/CLAIM and independent Result/Review authority remain separately pending.
