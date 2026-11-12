# R5: exact batch activation of every labeled BRC certificate prefix

Date: 2026-11-12 (Asia/Shanghai). Status: author-side proved finite-data-structure theorem and executed exact original-fixture reimplementation. Scope: the **frozen external** 28-coordinate, 15-labeled-atom P/Q–BRC Blackwell auxiliary model. This note continues the 2,520-byte seed construction of Draft PR #2179 at commit `e2c143f57f279847153349e6b8da579dd4f0862a`. Scientific input remains `435e77af0d180eac32bd1f9c4c464bc4010b7551`; original selected-word witness at `ad7013218d0474e1e942906e3beadec1eccb9213`.

## Problem and exact result

The previous 2,520-byte stream is BP topology (5,760 bits), four-bit incoming labels on 2,879 edges (11,516 bits), and 2,880 terminal bits; its fixed external atom table recovers the 1,065 distinct terminal pairs `(q,n)`, with `q in {3,12,15}` and 953 distinct rational activation walls. Earlier work used a reconstructed three-family Wavelet index to evaluate one prefix count `C_p(r)` at a time. A very different workload requests **all 2,880 prefix counts at one shared parameter**. We construct two exact full-snapshot engines from the same seed:

**Theorem A (linear batch snapshot).** For any finite rooted ordered trie, any fixed set of terminal leaves/nodes carrying integer pair labels `(q_t,n_t)` with `q_t,n_t>0`, and every rational `r<1/23`, let
`a_t(r) = 1{ n_t(1-23r) <= 36 q_t }`. At `r=1/23` set `a_t=1`. Define `C_v(r)=sum_{t in subtree(v)}a_t(r)`. One initialization of a length-N integer array from all M terminal flags followed by a reverse-preorder parent accumulation yields **every** `C_v(r)` in `O(N+M)` exact arithmetic operations, with `O(N)` working counters. It uses no Wavelet reconstruction or range-count calls. For the frozen R5 witnesses, `C_v` equals the previously proved exact word-prefix activation count.

Proof: preorder places a parent before all descendants. Initially the counter at node v is `a_v` if terminal, and zero otherwise. Processing every nonroot node from largest preorder index to 1 and adding its counter to its parent transfers exactly the sum of active terminal contributions in that subtree. Each edge is used once and every terminal is tested once. The frozen collision/right-persistence theorem identifies `a_t` with the original full 28-coordinate word legality: `r>= (1-36q_t/n_t)/23`. For rational r, multiplying by the positive denominator of `1-23r` gives the integer test written above. All ordered paths remain those of the frozen corpus.

**Theorem B (monotone multi-snapshot sweep).** Sort the M terminals by the exact rational activation threshold `tau_t=(1-36q_t/n_t)/23`. For nondecreasing query parameters `r_1<=...<=r_K<=1/23`, maintain one integer counter per trie node. At each crossing, add one to the terminal and each ancestor; snapshot the N counters at the requested r. This costs `O(M log M + sum_t(depth(t)+1) + KN)` exact comparisons/additions including initial sorting and full output materialization. If threshold order is already available, omit the sorting cost. The same procedure can answer an on-demand fixed set of prefixes without materializing each full snapshot, and identical activation walls are processed together for inclusive thresholds.

Proof: induction over sorted activation events. Initially every terminal with threshold greater than the current parameter contributes zero. At the event for terminal t, the only affected node counts are precisely the ancestors of t (including itself); adding one changes each from the previous correct value to the next correct value. Equal-wall events commute, and inclusive `<=` processes every such contribution at its wall. Between walls, no status changes. The final stored count vector is therefore the full `C_v(r)` for every queried r.

For R5, `sum_t depth(t)=6,379` (one operation label per level of each selected word), so the **whole exact sweep has precisely 6,379 + 1,065 = 7,444 ancestor counter increments**, independently of the number of snapshots, plus array-copy/output cost `K*2,880`. This is the same independently justified 7,444 count as in previous monotone-counter work, now integrated with the 2,520-byte reconstruction and explicit end-to-end workload comparisons.

## Executed independent real-fixture calculation

An independent CPython standard-library source fixture was reconstructed from the original frozen 28-coordinate R5 data, including all 15 integer operation vectors, all 32,768 masks, the 1,065 minimum-cardinality legal ordered words with all 28 exact rational prefix inequalities, a 2,880-node ordered trie, its packed 20,156-bit BP/label/terminal seed, full decode and port re-derivation. This was run locally **on actual frozen coefficients**, rather than a synthetic tree of matching size.

After reconstructing the auxiliary Wavelet matrices, 57,600 exact comparisons (`20 parameters * 2,880 nodes`) confirmed Theorem A against indexed per-prefix queries; Theorem B matched every parameter snapshot exactly. At all 953 event walls, the root Wavelet count matched the direct threshold census. Root counts were `C_root(0)=605` and `C_root(1/23)=1,065`. All outputs were independently recomputed by the exact-integer threshold test. No floating-point quantity entered the mathematical comparison.

Local run excerpt (`EXACT_OUTPUT.json`, 2026-11-12 Asia/Shanghai):

| Item | Actual value |
|---|---:|
| Terminal certificates / trie nodes | 1,065 / 2,880 |
| BP seed | 20,156 bits / 2,520 bytes |
| Distinct activation walls | 953 |
| Exact prefix comparisons | 57,600 |
| Root event checks | 953 |
| Total sweep ancestor increments | 7,444 |
| Sum of counts over 20 full snapshots | 62,728 |
| Corpus construction | 0.9389 s |
| BP decode and derived-index initialization | 0.3439 s |
| Peak traced allocations during initialization | 1,000,680 bytes |
| 20 full snapshots using per-prefix Wavelet (median of 3) | 0.562343 s |
| 20 full snapshots using batch postorder (median of 3) | 0.047106 s |
| 20 **sorted** snapshots using event sweep (median of 3) | 0.001104 s |

Corresponding same-run measured factors: batch/Wavelet = 11.938x; event-sweep/Wavelet = 509.276x. These are algorithm/workload-specific preliminary timings in one CPython process, not universal asymptotic speedups or a general hardware-independent performance claim. The event sweep benefits specifically from sorted parameters and amortizes processing across them. Benchmarks timed query workload separately from seed/index initialization, frozen-corpus generation and event sorting. The 1,000,680-byte trace is a Python allocator measurement for the designated init interval, not total process RSS or a claim that the 2,520-byte serialized payload occupies that much runtime memory.

## Reproduction and source status

`VERIFY_R5_BATCH_FROM_PINNED.py` is a portable branch-integrated checker importing the immutable predecessor verification modules, replaying their original 1,065 certificates, and adding both exact algorithms and the workload timing; it is a distinct implementation from the executed independent fixture script. The executed fixture source and its output are retained as local deliverables attached to this run; `EXACT_OUTPUT.json` records the performed run. As the branch-integrated checker was not itself run from a clean checkout of its published remote bytes, its independent remote-byte replay remains a next validation task. The prior Source Result/Review, Task owner, CLAIM and native X6 transfer remain distinct current-control questions.

## Next discriminating work

Benchmark mixed online workloads (one prefix vs complete snapshot, sorted vs random parameter order), including seed decoding, event sorting and actual RSS. Derive an adaptive selector between per-prefix Wavelet, linear batch and monotone sweep based on `N, M, K`, query locality and reordering constraints. For the fixed dataset, compare size and latency after selective materialization of rank and BP navigation directories; preserve the external atom table and full labeled operation provenance.
