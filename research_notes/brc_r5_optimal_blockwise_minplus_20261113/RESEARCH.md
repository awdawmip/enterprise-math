# R5 — Exact blockwise min-plus/count decoding of the frozen 12-byte optimal-checkpoint rank

Date: 2026-11-13. Status: original mathematical proof and independently executed exact finite computations; **author-side, not formal Source Result/review**.

## Frozen source and latest verified frontier

Original scientific input: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`; no scientific input repinning or P000 change.

Draft PR #2267 (original pinned wall array) reconstructs 953 exact rational activation walls, 954 strictly increasing cumulative event coordinates, 1,065 labeled certificate events and 4,383 radius-2 graph edges. Draft PR #2268 (head `f1da858b124bea152e5894518ab9ab87dc7b9ffe`) proves there are exactly 1,338,767,625,695,954,932,334,592,000 *mean-optimal* radius-2, K=213 center subsets. Their minimum total event correction is J=1070. The original historical 213-center list has rank 417027933051277583800994379 in this exact class, encoded by the **12-byte** big-endian payload `0158f5198cd12c63a2ba0a4b`.

The previous blockwise suffix-count method in #2267 applies to an *unweighted*, 17-byte radius-feasible center class. This increment supplies and verifies the **weighted min-plus and tie-count** analogue required to decode #2268's smaller 12-byte index.

## Theorem: exact blockwise min-plus/count suffix decode

Assume a strictly increasing integer event-coordinate array `x[0],...,x[W]`, nonnegative integral radius R, and fixed K. Define the exact radius-cover directed acyclic graph by `p -> q` (p<q) iff every boundary between p and q is within event-distance R of one of those two endpoints. Define edge cost
`w(p,q)=sum_{b=p+1}^q min(x[b]-x[p],x[q]-x[b])`, first-tail cost `A(p)=sum_{b<p}(x[p]-x[b])` and final-tail cost `Z(p)=sum_{b>p}(x[b]-x[p])`.

Let `C_t(p)` be minimum edge-plus-final-tail cost over all legal t-center suffixes beginning with p; let `N_t(p)` count suffixes attaining that minimum. For legal final p,
`(C_1(p),N_1(p))=(Z(p),1)`; otherwise `(+infinity,0)`. For t>1:
`C_t(p)=min_{p->q,N_{t-1}(q)>0}(w(p,q)+C_{t-1}(q))`
and
`N_t(p)=sum_{p->q: w(p,q)+C_{t-1}(q)=C_t(p)}N_{t-1}(q)`.
Unreachable states have count zero, and arithmetic uses exact integers. The optimal total value is `J=min_{p admissible start}(A(p)+C_K(p))`; counts sum over minimizing starts. Lexicographic rank/unrank uses only minimizing outgoing edges, weighted by `N_{t-1}`.

Fix a block width B>=1. In one forward t-sweep, store **both** (C,N) rows at t=1,1+B,1+2B,...; retain the last row if necessary for the initial choice. During ranking or unranking, which consumes t=K,K-1,...,1 monotonically, reconstruct each encountered block from its stored anchor by exactly the same recurrence, then discard it before entering the next block. Every reconstructed pair equals the full-DP pair by induction on t, *including ties and their exact multiplicities*. Hence the class cardinality, minimizing set, lexicographic ranking, unranking, and all 213 checkpoint center IDs are **identical** to full storage for every rank 0<=rank<Topt.

There are at most 2R+1 outgoing edges per vertex because integer x is strictly increasing. Each row costs O((W+1)(2R+1)) exact arithmetic transitions. One preprocessing sweep and at most one recomputation per row yield O(K(W+1)(2R+1)) transitions overall, with at most O((W+1)(ceil(K/B)+B)) stored arbitrary-precision **cost/count pairs**, versus O((W+1)K) pairs for the full table. This counts arithmetic operations/pairs, not their integer-bit cost, Python object overhead or end-to-end original-query runtime. B near sqrt(K) balances anchor and transient row counts.

The theorem applies to any finite declared integral event array satisfying those assumptions; the specific original R5 computation below is one exact instance.

## Independently executed original frozen R5 computation

The accompanying standalone standard-library Python verifier independently enumerates the 2^15-1 nonempty masks with the exact frozen W/K0 15-atom coefficients, retaining only `n>=3`, `k%36==0`, `q=k/36 in {3,12,15}`, and deduplicating (q,n) pairs. It sorts exact `(1-36q/n)/23` rational activation thresholds, preserves tied multiplicities and decodes the previously published 56-byte original center sequence (verified by its SHA-256).

Original real pinned instance: 954 boundaries, 1,065 events, 4,383 eligible graph edges, K=213 and R=2. Full-table and blockwise **both** recover J=1070; Topt=1338767625695954932334592000; original rank=417027933051277583800994379; 12-byte stream `0158f5198cd12c63a2ba0a4b`; all 213 original center indices. Independent exact re-ranking of the recovered centers agrees. For each B in {1,4,8,12,15,16,24,32,64}, blockwise unranking is byte-identical to the full-table result. Additional exhaustive verification covers 2,184 small (integer x,R,K) instances, including **7,683 individual blockwise mean-optimal rank/unrank crosschecks** over B in {1,2,3}; all pass.

### Measured local CPython resource trade-off

Single-run `tracemalloc` peaks for **construction of the DP plus one exact unrank**, after the common original fixture and graph are built; timings are one-run and machine-dependent:

| Decoder | Maximum cost/count rows held | Python peak bytes | Seconds |
|---|---:|---:|---:|
| Full K-row table | 213 | 8,227,908 | 0.323940 |
| B=4 | 58 | 2,343,080 | 0.557199 |
| B=8 | 35 | 1,583,160 | 0.617307 |
| **B=12** | **30** | **1,458,404** | **0.568900** |
| B=15 | 30 | 1,561,468 | 0.553384 |
| B=16 | 30 | 1,570,744 | 0.592246 |
| B=32 | 39 | 2,083,524 | 0.562310 |
| B=64 | 68 | 3,508,036 | 0.635530 |

For B=12, peak allocated Python bytes decline by approximately **82.27%** relative to the full-table baseline; the measured decoder time rises from 0.324 s to 0.569 s. The byte saving is in **transient decoding memory**, not in the persistent 12-byte center stream (unchanged). Fixture build, original 2,520-byte certificate seed reconstruction, bitmap/index build, peak process RSS and arbitrary rational-prefix query throughput require a separate common-load benchmark.

## Evidence, authorization and next question

Files: this `RESEARCH.md`, independently executed `VERIFY_R5_OPTIMAL_BLOCKWISE.py`, and exact stdout `EXACT_OUTPUT.json`. Exact integers/Fraction arithmetic, finite exhaustive small-case verification, no floating oracle. Reusing original 28-coordinate legal-word census is explicit provenance, not a new independent legal-path proof. Results and scope may be reused after independent source-byte execution and the project's actual review.

No active TASK CLAIM, official Result, reviewer independence or Foundation promotion is inferred from this branch/PR. Preserve the task's original frozen scientific pin and original author contributions. No Drive fallback is needed when authenticated GitHub publication succeeds.

**Next scientific unit:** integrate the blockwise 12-byte unranker and the 17/33/35/56-byte alternatives under one identical cold-start pipeline, measure real process peak RSS, exact rational-wall reconstruction, bitmap construction, original prefix queries and serialized outputs, and solve for a measured memory/query-count crossover. Investigate checkpoint row compression only if the memory table remains an observed bottleneck.
