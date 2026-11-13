# Preliminary G-stride select microbenchmark (same frozen 2,880-node BP word)

Date: 2026-11-12; source: executed local Python 3 stdlib program using the frozen real 1,065-word R5 corpus.

The executed benchmark imported the separately validated original-corpus BP and performed five whole-corpus runs of the naive superblock-select loop for each G; each run selects all 2,880 openings in preorder order. Timing uses perf_counter_ns with median per queried opening. All settings recovered the same sum of opening positions (8,276,543). This is a Python-list, **unpacked** BP navigation microbenchmark, *not* an end-to-end Wavelet query benchmark, not an immutable environment calibration, and not an estimate of resident memory or packed bitvector performance.

| G (B=64) | Stored rank anchors | Total fixed-field bits | Bytes | Median ns / opening select (this local run) |
|---:|---:|---:|---:|---:|
| 1 | 90 | 36,457 | 4,558 | 1,443.9 |
| 2 | 45 | 35,917 | 4,490 | 2,747.6 |
| 4 | 23 | 35,653 | 4,457 | 4,913.9 |
| 8 | 12 | 35,521 | 4,441 | 9,406.6 |
| 16 | 6 | 35,449 | 4,432 | 18,539.8 |
| 32 | 3 | 35,413 | 4,427 | 36,007.8 |
| 90 | 1 | 35,389 | 4,424 | 107,196.7 |

Interpretation: on this pure-Python direct-scan implementation, G=8 saves 117 fixed payload bytes relative to G=1 while the opening-select path takes approximately 6.5× the local time. The larger G values barely save more bytes but continue to slow this particular select path; G=4 is a plausible next full-query candidate with 4,457 bytes and roughly half G=8 select latency on this run. These are observations under this precise implementation, not a proven globally optimal setting.

The repository file BENCH_SPARSE_SUPERRANK_SELECT.py reconstructs the same frozen BP from pinned Source ancestry. The integrated remote-byte benchmark has not been executed from its newly published commit. Next: repeat with packed bitvectors, controlled repeated warm and cold trials, full Wavelet/rank queries, memory accounting, and alternate rank/select navigation.
