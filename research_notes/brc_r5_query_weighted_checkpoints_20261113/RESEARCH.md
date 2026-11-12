# R5 — Exact query-weighted activation checkpoint placement

Date: 2026-11-13 (Asia/Shanghai). Scope: frozen 28-coordinate/15-operation auxiliary P/Q–BRC certificate model. Frozen scientific source pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. This is author-side mathematical and computational research, continuing the verified signed-event correction method in Draft PR #2210 (commit `20bda42c655ae37d905c5876126af1700c27aa55`). The new result concerns index placement; the original path, terminal identities, operation labels, and rational activation semantics are unchanged.

## Statement: workload-optimal sampled activation checkpoints

Let `M` terminal certificates have exact rational activation walls `w_0 < ... < w_(W-1)` and immutable terminal-preorder positions. Each threshold `b in {0,...,W}` includes precisely the events with wall index less than `b`. Let
`E(b) = # {terminals with wall index < b}`.
In the frozen R5 model, `W=953`, `M=1065`, and all wall groups are nonempty, so `E(0)=0 < E(1) < ... < E(953)=1065`.

The signed correction algorithm stores a complete-wall checkpoint bitmap at a boundary `s`. At query boundary `b`, it inspects exactly `|E(b)-E(s)|` event positions to correct its checkpoint prefix count (in addition to a bitmap popcount and a checkpoint lookup). For a fixed finite forecast/workload `a_b >= 0`, and a budget of exactly `K` checkpoints drawn from complete-wall boundaries, the precise *event inspection objective* is

```
     L(S) = sum_{b=0}^W a_b * min_{s in S} |E(b)-E(s)|,
     |S| <= K,  S subset of {0,...,W}.
```

**Theorem.** The global minimum of `L(S)` is obtained by an exact one-dimensional weighted `K`-median dynamic program. For a contiguous block of query indices `[i,j]`, a weighted median `m(i,j)` of the points `E(i),...,E(j)`, with weights `a_i,...,a_j`, is a minimizing center, and its block cost is

```
    D(i,j) = sum_{b=i}^j a_b * |E(b)-E(m(i,j))|.
    DP[1,j] = D(0,j)
    DP[k,j] = min_{k-2 <= t < j} { DP[k-1,t] + D(t+1,j) }.
```

Backtracking the minimizing cuts and weighted medians produces an optimal checkpoint set. All arithmetic can be integer exact; medians and costs can be tabulated using prefix sums of `a_b` and `a_b E(b)`. Straightforward implementation requires `O(W^2+KW^2)` time and `O(W^2+KW)` auxiliary storage, with reducible constants.

**Proof.** For fixed ordered checkpoint event positions, assign each query boundary to its closest checkpoint in event-count distance, resolving ties consistently. The resulting Voronoi regions in the one-dimensional ordered set are contiguous. On a contiguous region, a weighted median minimizes the absolute-distance loss; each median belongs to the allowed set of boundary event coordinates, so replacing its center is feasible. Conversely, the centers obtained from any contiguous partition are a feasible checkpoint set, whose closest-center loss is no greater than the partition's median cost. Thus minimization over contiguous partitions equals minimization over all checkpoint subsets, and the displayed dynamic program is exact. Zero weights and coincident event counts also satisfy the argument (deduplicate redundant centers when needed).

The result is a workload-tailored application of the classical weighted one-dimensional `K`-median principle to exact BRC certificate activation event ranks. It does not claim that weighted `K`-median is a new general algorithm or that average-optimal placement also minimizes the maximum correction.

### Composition and exact semantic preservation

For each prefix-trie node `v`, its terminal interval is `[L_v,H_v)`. If checkpoint `s` has bitmap `A_{E(s)}`, count activated terminals by the previous exact signed-correction theorem: popcount within that terminal interval, plus or minus one for each event position between `E(s)` and `E(b)` that lies inside the interval. Choosing `s` to minimize event distance changes only the computation schedule, not which labeled certificates count. A rational query parameter `r` uses `b=bisect_right(walls,r)`, preserving equality-at-wall activation and duplicate-wall multiplicity.

## Exact experiment on unchanged frozen fixture

Local CPython source fixture `VERIFY_R5_OFFLINE_FENWICK.py` was executed from its previously verified frozen-model source; the output reconstructs 1,065 terminal certificates, 2,880 prefix nodes, and 953 exact rational walls. This experiment compares complete-wall checkpoint placements without modifying the frozen scientific inputs.

Two explicitly synthetic workloads over all 954 ranks were used:

- `uniform`: `a_b=1`.
- `three_hotspots`: `a_b=2 + floor(300 max(0,22-|b-floor(W/7)|)/22) + floor(280 max(0,30-|b-floor(W/2)|)/30) + floor(260 max(0,18-|b-floor(7W/8)|)/18)`, where `W=953`.

| Workload | Budget K | Weighted-median checkpoints | Mean event edits, weighted median | Minimax checkpoints | Mean event edits, minimax | Mean event edits, uniform spacing |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| uniform | 15 | 15 | 17.61950 | 15 | 18.01887 | 18.97694 |
| uniform | 30 | 30 | 8.77254 | 29 | 9.24948 | 9.13836 |
| three_hotspots | 15 | 15 | 5.59270 | 15 | 21.77475 | 12.63543 |
| three_hotspots | 30 | 30 | 2.87252 | 29 | 8.49248 | 9.30150 |

The three-hotspot / 30-checkpoint optimization reduces the *weighted expected number of signed event inspections* to 2.87252 from 8.49248 for the 29-checkpoint minimax baseline under this specified workload. The worst-case correction increases from 18 to 37 events, an explicit average-versus-worst-case tradeoff.

A separate finite 8-point exhaustive subset-enumeration check verified the dynamic-program objective for K=1,2,3,4. The frozen 2,880-node model passed **123,392** comparison checks for the weighted and minimax signed correction variants: 4,096 randomized (prefix,boundary) checks plus all 57,600 original Fraction/Wavelet (prefix,parameter) checks for each method. Ten thousand additional held-out synthetic queries agreed exactly with the direct terminal-count oracle for both methods.

Same-process CPython 7-repeat median for **10,000 held-out synthetic queries**, with checkpoint event-rank lookup and signed membership corrections included: weighted-median 30 checkpoints **8.329 ms**; minimax 29 checkpoints **11.638 ms**, both checksum 14,049. The measured execution time was 28.4% lower in this sample, with a larger checkpoint count. Sampled mean event inspections were 2.8633 vs 8.6197.

### Scope, replication and further question

These times exclude original certificate generation/seed decoding, wall construction, full process startup, checkpoint construction, rational-to-boundary conversion, output serialization and end-to-end peak memory. Bitmaps alone occupied 4,832 and 4,592 Python object bytes respectively; these are not complete index or process memory footprints. The workload law is synthetic, rather than inferred actual demand. The full actually-executed script and `EXACT_OUTPUT.json` are preserved as run-local artifacts. The accompanying compact source program reproduces the optimizer, the frozen-data comparisons and integer totals; its GitHub version is provided for independent clean-environment execution and is not represented as already run from its remote bytes.

Next scientific problem: train placements on observed or independently generated parameter workloads, test out-of-distribution robustness and adaptive checkpoint reconfiguration accounting for placement rebuild time. Separately, reconcile the exact formal X6 owner/CLAIM before authorizing any shared Task Result or Review; author-side R5 notes are not a substitute for task ownership, native activity checkpoint or independent mathematical review.
