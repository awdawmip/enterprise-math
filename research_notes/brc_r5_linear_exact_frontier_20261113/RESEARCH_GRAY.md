# R5: constant-state Gray-code event enumeration

Date: 2026-11-13. The unchanged frozen science input is awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551. This supplements the exact one-bit subset recurrence and monotone midpoint proof in RESEARCH.md. Author-side mathematical and numerical evidence only, no P000, Task, CLAIM, Result or review change.

## Theorem

For integer weights w_j,k_j over m=15 labeled atoms, enumerate subsets via reflected binary Gray code

\[
g(i)=i\oplus(i\gg1),\qquad 1\le i<2^{m}.
\]

For every i>=1, Gray masks g(i-1) and g(i) differ only at bit j=nu_2(i), the index of the lowest set bit of i. Maintain the current subset M and two integer sums n(M),k(M). If bit j enters, subtract w_j,k_j from the running sums; if it exits, add them. Starting with M empty and sums zero, an induction shows that these are exactly the sums for each current mask. The Gray sequence is a permutation of all 2^m binary masks; each nonempty subset is processed exactly once.

Keeping the same eligibility n>=3, 36|k, q=k/36 in {3,12,15}, deduplicate n separately for each q, then sort the exact rational ratios n/q. This produces the identical R5 event-wall multiset, including 953 distinct thresholds with multiplicity histogram 869:56:28 and 954 cumulative boundaries ending at 1065 events.

The scalar accumulator uses O(1) extra running numeric state plus the immutable O(m) weights and required per-family deduplication/output, versus two O(2^m) arrays in the earlier low-bit recurrence. Arithmetic iterations remain O(2^m). Arbitrary-precision bit costs and final rational sorting are accounted separately.

## Executed tests and cost

The exact locally executed source VERIFY_GRAY_EVENT_BUILDER.py (Git blob bc89c1762544ac7b3c1451919094929c75c64c3c) imports the prior exact verifier in the same directory. It checks all 32,767 Gray transitions against the actual reflected Gray mask, independently verifies each family's n-set sizes, event histogram and boundary array against naive and array-recurrence algorithms, and checks R=0,1,2,9,25,26,36 exact DP outputs. Its run status is PASS_GRAY_EXACT.

Warm single-process interleaved 13-run medians, with five Python allocation tracing runs:

| Event-builder method | Naive rescans | Cached subset recurrence | Constant-state Gray |
|---|---:|---:|---:|
| Warm event construction (ms) | 66.7286 | 8.3802 | 7.1197 |
| Peak Python allocations while building (bytes) | 228880 | 2181960 | 194376 |
| Fresh-process R2 build + DP median with tracing (ms) | 358.9622 | 149.4443 | 147.3967 |
| Fresh-process R2 peak traced Python allocations (bytes) | 504626 | 2366900 | 458998 |

Gray is about 9.37 times as fast as naive rescanning in the warm event-builder experiment and 1.18 times as fast as the cached recurrence. It avoids approximately 91% of the cached recurrence's peak traced builder memory. Because tracing changes timing, fresh-process traced runtimes and warm untraced runtimes are separate experiments. The collected maximum RSS readings are all 104476 KiB in this environment; they do not distinguish the implementations.

Complete independent-process 28-coordinate prefix-index construction, query batches and serialization remain open. This result is an exact auxiliary R5 threshold-observer implementation; it makes no claim that collapsed scalar-event coordinates fully encode native signed X6 source, branch or joint-observer residuals.

## Next unit

Inject Gray event generation into existing original-seed (2520-byte) full prefix-query reproduction, verify byte-identical answers and compare actual fresh-process setup/peak RSS, 8192-query batches and output serialization. Establish whether event-corpus reconstruction lies on that path's critical cost before extrapolating its local speedup.


## Path-selection result from the already saved complete-query implementation

The independently preserved predecessor Draft PR #2220 contains a different construction path: its REPRO_SEED_BENCH.py decodes the 2,520-byte BP/label/terminal seed into the 2,880-node prefix trie, obtaining exactly 1,065 original terminal (q,n) pairs and their 953 rational walls directly. This route does **not** enumerate all 32,767 nonempty 15-atom masks, so adding the Gray enumerator as an extra stage would duplicate work and would not imply an end-to-end speedup. The previous nine-process seed-only measurement reported approximately 111 ms median setup, 29.8 ms for 8,192 queries, 0.36 ms JSON serialization and about 1.22 MB traced setup allocation for the mean-optimal scheme. These previous figures have different tracing/baseline conditions and are not directly comparable to the warm Gray microbenchmark.

There are thus two distinct admissible upstream data paths:

1. **Raw 15-atom source / missing prepacked seed:** Gray-code enumeration can replace per-mask resummation or a full cached subset DP while preserving the deduplicated rational event corpus.
2. **Already packed 2,520-byte prefix seed:** Decode each terminal pair once, reuse it to build both the threshold wall index and per-prefix ranges. Prefer that direct 1,065-pair extraction unless a measured, nonduplicating replacement has an advantage.

The next discriminating experiment is a common-source, independently timed end-to-end comparison with exact answer hashes, not simply inserting Gray work into the existing packed-seed path. This is a computational-model/accounting boundary, not a change to the frozen mathematics.
