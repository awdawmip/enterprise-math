# R5 packed-seed fresh-process benchmark (local run, CPython 3.13.5)

The same frozen science pin `435e77af0d180eac32bd1f9c4c464bc4010b7551` was rebuilt once from the original 28-coordinate, 15-operation exact rational fixture to export an **actual packed 2,520-byte BP+labels+terminal seed** and the exact 15 integer port coefficients. Each of nine fresh child processes per algorithm used only the packed seed and port coefficients to reconstruct the 2,880-node trie, all 1,065 `(q,n)` terminal labels, 953 rational walls, event order, prefix terminal intervals and 213 sampled bitmap checkpoints. Query workload: the same 8,192 deterministic rational complete-wall queries (first 64 at root), including rational-to-wall binary search and JSON result serialization. Process baseline/repeated warm-up cost and corpus generation are outside the measured child intervals.

| CPython process median, nine runs | Greedy minimax R=2 | Same-radius mean-optimal R=2 | Unconstrained mean-optimal R=3 |
|---|---:|---:|---:|
| Packed-seed decoding, index construction and tracing (ms) | 116.098 | 111.036 | 110.898 |
| 8,192 rational parameter prefix queries (ms) | 30.747 | 29.828 | 30.211 |
| JSON result serialization (ms) | 0.356 | 0.367 | 0.359 |
| Sum of the above three stages (ms) | 146.190 | 141.747 | 141.641 |
| Peak traced setup allocation (bytes) | 1,227,522 | 1,220,802 | 1,220,678 |
| Peak process RSS, Linux ru_maxrss (KiB) | 99,596 | 99,596 | 99,604 |

All 27 fresh-process runs returned **identical 8,192-count result arrays**, with checksum `48432` and exact serialized UTF-8 SHA-256 `c66f0e06184987e0fbbf1b1c89b3b329a9b87e20e2c0c525b947d9723d5a317c`.

**Interpretation:** The exact all-boundary event-correction objective improves by 3.080% at fixed K=213 and R=2. This particular single-machine synthetic request workload also showed a modest query-time improvement, from 30.747 to 29.828 ms (nine-process median; ~2.99%), but the differences in setup and aggregate time are noisy. Tracemalloc was active during setup only; ru_maxrss includes Python process infrastructure. The seed-only setup *excludes* regeneration of the 28-dimensional candidate corpus; it begins with the persisted 2,520-byte seed. This is an operationally useful distinction because corpus-generation time was approximately 1.49s in the earlier separate run.

The exact integer optimizer, same-radius feasibility recurrence and over one million independent prefix comparisons are in `VERIFY_R5_MEAN_OPT_FROM_PINNED.py`. The portable benchmark reproduction driver is `REPRO_SEED_BENCH.py`; the JSON summary records the originally observed local timings, not a claim of having executed the GitHub-hosted verifier in a clean remote checkout.

Next: test query distributions not uniform over complete-wall boundaries, cache-warming/long-running processes, same-byte-budget checkpoint count changes and independent portable execution. No physical-time or native operation semantics are inferred from these engineering measurements.
