# Stage512-B RSS and latency appendix

Date: 2026-11-08. This is supplementary directly executed evidence for [PROOF_STAGE512B.md](PROOF_STAGE512B.md).

The original benchmark `STAGE512B_COMPACT_EXECUTED.json` measured peak Python allocations through `tracemalloc`. Because those allocations are not process resident set, this appendix adds actual independent-process **peak RSS** measurements. Exact executable: `RSS_STAGE512B.py`, paired with `REPRO_STAGE512B_COMPACT.py`; full raw output: `STAGE512B_RSS_EXECUTED.json`.

Five fresh Linux Python subprocesses were launched per case and algorithm. Each called the identical BRC exposure routine once and recorded `resource.getrusage(RUSAGE_SELF).ru_maxrss` (KiB) plus `perf_counter_ns` wall time. All quotient masks matched reference masks; all assertions passed.

| Case | Old states | Quotient states | Reference median peak RSS (KiB) | Quotient median peak RSS (KiB) | Reference / quotient median wall time (ms) |
|---|---:|---:|---:|---:|---:|
| n=19,h=3 | 26 | 19 | 95504 | 95504 | 0.1154 / 0.0765 |
| n=28,h=2 | 6 | 5 | 95504 | 95504 | 0.0489 / 0.0365 |
| n=28,h=5 | 263 | 119 | 95520 | 95504 | 1.3890 / 0.6904 |
| n=100,h=5 | 516 | 253 | 96540 | 95896 | 6.2617 / 2.4951 |

Resident set is dominated by the interpreter's startup allocation at these sizes; the n=100,h=5 median difference is 644 KiB, while smaller cases mostly share the same baseline. Timing and RSS are environment-specific comparisons; the mathematical result is exact equality of exposed original identities under the structural quotient. All scientific input freezes and current behavioral rule scopes remain as stated in the proof.

**Next:** test larger h where process RSS rises above interpreter floor, and investigate a rank/interval transducer avoiding explicit structurally distinct skeleton enumeration.
