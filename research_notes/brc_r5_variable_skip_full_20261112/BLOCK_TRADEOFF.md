# R5 — Block-stride tradeoff for the sampled variable subtree-size codec

Observation date: 2026-11-12 (Asia/Shanghai). Same frozen 1,065 selected original R5 words and 2,880 preorder nodes as the accompanying RESEARCH.md. This is a reproducible author-side *Python interpreter microbenchmark* of subtree-size lookup, not a benchmark of full Wavelet queries or a cross-language CPU guarantee.

## Parametric exact codec family

Keep the same 13,436-bit variable size codes and the identical remaining 28,987 indexed bits. For any positive integer stride \`B\`, store one **16-bit variable-code bit offset** at preorder nodes \`0,B,2B,...\`. Every offset is below \`2^16\` for this particular tree. The full bitstream size is exactly

\[
F(B)=42,423+16\lceil2,880/B\rceil\quad\mathrm{bits},
\qquad \operatorname{bytes}(B)=\lceil F(B)/8\rceil.
\]

For any node \`i\`, start at \`offset[floor(i/B)]\` and parse at most \`B-1\` prior variable codes; then decode its tagged payload. Every node's size is recovered exactly and the parent/child preorder navigation and terminal/rank/wavelet query semantics are unchanged.

This proves a finite explicit **space/access-scan tradeoff** for the frozen original selected-word corpus. The 64-node instance in RESEARCH.md has the \`B=64\` parameters and 5,393 bytes.

## Exact sizes and measured lookup cost

Single-process Python 3 prototype, exact original corpus reconstructed from immutable R5 coefficients, fully decoded list of variable bits and sampled starts used for each \`B\`. For each stride, every one of 2,880 node sizes was compared against the original integer sizes; five repeated sequential full-scan timings were collected, median shown.

| Stride B | Saved offset entries | Complete indexed stream (bytes) | Median for 2,880 subtree-size reads (ms) |
|---:|---:|---:|---:|
| 8 | 360 | 6,023 | 2.605 |
| 16 | 180 | 5,663 | 3.444 |
| 32 | 90 | 5,483 | 5.343 |
| 64 | 45 | 5,393 | 9.461 |
| 128 | 23 | 5,349 | 15.091 |
| 256 | 12 | 5,327 | 29.861 |
| 512 | 6 | 5,315 | 56.170 |

All seven strides passed \`for i in 0..2879: decoded_size_B(i)==source_size(i)\`. The size results follow the closed formula and are exact bit-budget results; timings are environment-specific Python microbenchmarks with decoded bit arrays and block starts already in memory, excluding build, heap allocation, Wavelet rank/count, file I/O and original input conversion.

**Decision supported by these measurements:** the \`B=16\` variant uses 270 more bytes than the current 5,393-byte \`B=64\` compact index, while its author-side local sequential-size lookup median was lower (3.444ms vs 9.461ms for 2,880 reads). For this specific task a runtime benchmark with equal decoded and packed lookup representations should determine which point to deploy. The \`B=32\` variant is another nearby candidate, using just 90 more bytes than \`B=64\`.

Next: benchmark fair full indexed prefix counts and peak memory at B=16/32/64 on the immutable selected corpus and the same parameter/prefix workload, with build cost and random-access distribution included. A current proof or result admission review has not been requested through a live formal R5 CLAIM in this branch.


## Reproducibility implementation and second measurement

\`VERIFY_R5_STRIDE_BENCH.py\` in this branch imports the sibling full original-corpus verifier, constructs the same variable-coded size sequence, checks all 2,880 node sizes for every stride, then records seven within-process repetitions of both sequential and fixed-seed shuffled subtree-size lookups. This is a runnable benchmark source, not an additional theorem premise. The local author-side reproduction with the independently reconstructed original frozen source-equivalent module returned:

| B | Bytes | Median sequential (ms) | Median shuffled (ms) |
|---:|---:|---:|---:|
| 8 | 6,023 | 1.730 | 1.730 |
| 16 | 5,663 | 2.526 | 2.482 |
| 32 | 5,483 | 4.036 | 4.106 |
| 64 | 5,393 | 7.104 | 7.108 |
| 128 | 5,349 | 13.248 | 13.447 |
| 256 | 5,327 | 25.506 | 25.551 |
| 512 | 5,315 | 50.644 | 50.439 |

All strides passed \`PASS_R5_ALL_STRIDE_EXACT_DECODE_2880_NODES\`. This second session differs in absolute timing from the first table, as expected for interpreter/machine load; the size formula and direction of the time-space tradeoff agree. Timings are strictly Python-memory lookup microbenchmarks, not published full-query throughput.

