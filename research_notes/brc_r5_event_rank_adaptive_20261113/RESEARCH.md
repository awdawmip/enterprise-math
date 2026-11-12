# R5 — 精确激活阈值秩与按需祖先索引

Date: 2026-11-13 (Asia/Shanghai). Status: author-side finite algorithm theorem, locally executed exact original-fixture verification; independent review and formal Source Result pending.

## Exact inherited frozen science

This continuation consumes the unmodified R5 28-coordinate, 15-labeled-operation P/Q–BRC Blackwell *auxiliary* model, not a native X6 physical theorem. Frozen scientific input is the immutable commit `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Parent material is [R5 arbitrary-order prefix query, Draft PR #2186](https://github.com/awdawmip/enterprise-math/pull/2186), commit `a26c7246cdc304a4ec73d5769f0adf67a8273a09`. The branch retains the original 2,520-byte BP/4-bit-label/terminal seed and all parent verification paths; the branch does not alter the scientific pin.

Original counts: 2,880 ordered-trie nodes; 1,065 distinct marked terminal certificates; 953 distinct rational activation walls; total terminal depth 6,379. For terminal t, the exact activation wall is
[
\tau_t=(1-36q_t/n_t)/23,\qquad q_t\in\{3,12,15\},\ n_t>0.
]
For an arbitrary prefix node v, its terminal descendants have a contiguous terminal-preorder interval `[L_v,H_v)`, and `C_v(r)=#{t in subtree(v): tau_t <= r}` (ties inclusive).

## Theorem — event-rank integer carrier

More generally, let T be any finite ordered rooted tree with M marked terminals, and let each marked terminal carry a totally ordered threshold `tau_t`. Let `w_0 < ... < w_{W-1}` be the sorted *distinct* thresholds. List the terminals in depth-first preorder and define `e_i=j` exactly when `tau_i=w_j`. For any parameter r let `b(r)=upper_bound(w,r)`, the number of distinct thresholds not exceeding r. Then for every prefix node v:

[
\boxed{C_v(r)=\sum_{i=L_v}^{H_v-1}[e_i<b(r)]}.
]

**Proof.** `e_i<b(r)` if and only if `w_{e_i}<=r`. Each marked descendant of v occurs exactly once in its contiguous terminal-preorder interval. Summing its activation indicator proves the identity. Distinct terminals with equal walls have identical code but remain separate terms, so the formula also preserves multiplicities and equality at a wall. This holds for any query order and every permitted r. QED.

For the frozen R5 corpus `W=953`, so every event code fits in **10 bits**. The terminal-preorder code vector contains exactly `1,065*10=10,650` logical bits, i.e. **1,332 bytes if tightly bit-packed**. The implemented Python `array('H')` uses **2,130 raw data bytes**. Both are derived in memory from the unmodified 2,520-byte persisted seed; these are *not* additional stored seed bytes. The separate sorted wall table preserves 953 exact rationals.

The global wall rank costs `O(log W)` exact comparisons and the integer scan of a cold prefix costs `O(m_v)`, where `m_v=H_v-L_v`. A hot prefix may cache its *sorted* integer code vector, spending `O(m_v log m_v)` to build it and `2 m_v` array-data bytes in the implemented 16-bit representation, to answer subsequent requests in `O(log W+log(m_v+1))`. A configurable two-hit, minimum-16-terminal policy is only an engineering choice; correctness is independent of it. Across all possible cached nodes, exact code-reference inventory is the inherited 7,444, requiring 14,888 bytes of raw 16-bit array elements, plus container/object overhead.

## Executed exact original-fixture evidence

The locally executed standalone `VERIFY_R5_EVENT_RANK_ADAPTIVE.py` (conversation artifact) imports the independently executed prior R5 original-fixture Python rebuild, which recomputes all 32,768 subsets, 1,065 terminal paths and exact rational prefix constraints from the 28-coordinate frozen coefficients. The newly implemented code tests every one of 2,880 prefixes against 20 rational parameters: **57,600 exact equality checks** against the independent Wavelet engine; it also checks all **953** root-wall equality cases. All passed. In addition, all 7,444 ancestor references were rebuilt as sorted 16-bit arrays and checked against the same 57,600 pairs. Local output is `EXACT_OUTPUT.json`, marker `PASS_R5_EVENT_RANK_ADAPTIVE_REAL_FIXTURE`.

**Local CPython measurement, median of three for warm cases; seconds, reference corpus reconstruction excluded:**

| workload | requests | coded direct | lazy cold, includes materialization | lazy warm | fully built ancestor warm |
|---|---:|---:|---:|---:|---:|
| root | 256 | 0.008559 | 0.000957 | 0.000787 | 0.000723 |
| broad | 512 | 0.003738 | 0.002433 | 0.001739 | 0.001108 |
| uniformly random prefixes | 2,048 | 0.007126 | 0.007259 | 0.007301 | 0.000911 |
| hot-node mixture | 2,048 | 0.015744 | 0.007239 | 0.006587 | 0.003400 |

For the cold adaptive pass, cached array data comprised respectively 2,130, 5,348, 218 and 4,772 bytes. The fixed 2-hit choice deliberately avoids building most low-frequency nodes: among 1,464 distinct nodes in the random sample, only three were materialized in its first pass. Fully materializing all 2,880 node arrays took 0.058684 s in this local run, with 268,528 bytes peak traced allocations *during that specific construction window*; this is not whole-process RSS. Including one-time rational-wall/code-table construction, pure coded-direct queries measured 0.014656, 0.009629, 0.013484 and 0.025366 s respectively. CPU affinity and GC were not controlled. These timings compare the stated concrete workloads and implementations, not an abstract complexity hierarchy.

The GitHub `VERIFY_R5_EVENT_RANK_ADAPTIVE_FROM_PINNED.py` is a compact stacked-branch verifier which imports the pinned parent verifier, checks every prefix/sampled r, checks all 953 wall ties, constructs the same integer rank index and exercises workloads. It is published for independent remote-byte execution; the executed local full-fixture script and its recorded exact output are separate artifacts.

## Continuation and ownership

The native Source inventory request `r5-20261113-0040-owner-inventory-01` reached SUCCEEDED and returned a **bounded 50-item** view out of 491 entries; the R5 formal task/owner was not established by that view. This research is preserved as *unreviewed author-side science*, not a CLAIM or formal Result. No other researcher's live ownership was changed. Existing PR #2186 remains a separate historical author contribution; publication here adds neither review independence nor current native execution permission.

The next research question is to optimize the cache policy under a declared distribution and memory budget. Derive a cost-based admission threshold from `m_v`, per-node query count and expected reuse, while including the cost of exact rational-wall construction, seed decode, complete process RSS and output verification. A discriminating next experiment should measure total end-to-end latency (not only warm queries) for increasing request counts and skew distributions, and compare event-rank caching against the earlier Wavelet/Fenwick designs. The frozen source and all original path labels must remain unchanged.
