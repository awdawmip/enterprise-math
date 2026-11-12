# R5 — Exact signed event correction for sampled activation bitmaps

Date: 2026-11-13 (Asia/Shanghai). Author-side mathematical and computational result. Continuation of Draft PR #2206 (commit `6871bb2cd322e26b3a5b21f3a3414880bcd35c67`); immutable scientific input `435e77af0d180eac32bd1f9c4c464bc4010b7551`. The underlying 28-coordinate/15-operation auxiliary BRC model, 1,065 exact certificates, 2,880 trie nodes and 953 rational activation walls are unchanged.

## Exact theorem — signed checkpoint correction

Let terminal positions be `0,...,M-1`. Each terminal has an exact activation wall and a distinct terminal position. Let `pi` be the permutation of positions sorted by (wall, position), and for any complete-wall query rank `b`, let `x=E(b)` be the number of terminals at walls strictly below `b`. For any stored checkpoint event count `y`, let `A_y=sum(2^pi(j) for j=0,...,y-1)`. Any prefix node `v` spans a contiguous terminal-preorder interval `[L_v,H_v)`.

**Claim.** The exact activated count is

```
C_v(b) = popcount((A_y >> L_v) & (2^(H_v-L_v)-1))
        + sum_{j=y}^{x-1} [L_v <= pi(j) < H_v]          if x>=y
        - sum_{j=x}^{y-1} [L_v <= pi(j) < H_v]          if x< y.
```

The two signed sums are empty whenever their upper endpoint equals their lower endpoint. This formula is exact for every finite certificate tree, every complete-wall boundary, ties, and arbitrary query order. With `b=bisect_right(walls,r)`, it implements the exact inclusive-wall activation condition for rational `r`. Proof: the difference between the terminal sets encoded by `A_y` and `A_x` is precisely the event-index interval `[min(x,y),max(x,y))`. Taking cardinality after restricting each set to `[L_v,H_v)` gives the stated signed sum. No new snapshot bits must be constructed, and the stored source identity/ordered tree is unchanged.

For the predecessor's minimax 213 complete-wall checkpoints (budget 239), `max_b min_y |E(b)-y|=2` is exact under its discrete checkpoint theorem. Each query thus needs at most **two signed membership comparisons**, a binary search among the 213 stored event counts, and one existing checkpoint bitmap range popcount. Time is `O(log K + bitmap_slice_popcount + R)`, with `R<=2` in the frozen corpus, and **no new retained fields** compared with the compact directory of PR #2206.

This improves the query implementation of the existing exact observer, not the underlying BRC physical model or the asymptotic bound of all algorithms.

## Executed frozen-original validation

Local CPython 3.13.5 on x86_64 reconstructed the original 28-dimensional Fraction certificate fixture from the locally retained previously verified source, then verified signed correction and the predecessor bitmap-mutation algorithm against an independent exact terminal prefix-sum oracle at all `954 * 2880 = 2,747,520` complete-wall/node pairs. The signed implementation also agreed with the original Fraction/Wavelet oracle on all 57,600 node/sample pairs. The predecessor minimax geometry was re-derived: 213 checkpoints, exact worst residual event count 2.

Same-process query-only medians, 11 repetitions per method, **rational query parameters already converted to wall ranks**; neither source reconstruction, wall binary search, index building, output serialization, nor peak RSS is timed:

| Query batch | Original bitmap mutation (ms) | Signed correction (ms) |
| --- | ---: | ---: |
| Root, 256 | 0.219 | **0.195** |
| Broad subtrees, 512 | 0.478 | **0.392** |
| Random prefixes, 2,048 | 2.123 | **1.359** |
| Mixed hotspots, 2,048 | 1.844 | **1.599** |

The frozen-corpus generation step in this local run took 1.4185 s. The two query algorithms shared exactly the same stored 213 bitmap objects, checkpoint coordinates, event order and E array; counted object bytes: masks 33,108, coordinates 522, compact event-order array 2,210 and Python-list E 34,544. The previously proven optional uint16 compression of E may be applied separately, but it was not benchmarked in this experiment.

## Replication and unfinished question

`VERIFY_SIGNED_EVENT_FROM_PINNED.py` is a portable stacked-source verifier importing the predecessor original-frozen dataset from `brc_r5_offline_fenwick_20261112`. Its logic is an independent implementation of the same mathematics and is committed for clean-environment execution; this GitHub-hosted program was not executed as part of the local test. `EXACT_OUTPUT.json` contains the actual **local** output, not a claim of remote execution.

Next: execute the committed portable program in a clean checkout, measure full end-to-end cost including seed decode, exact wall ranking, event-index building, allocation/RSS and recovery of returned counts; benchmark equal-total-memory versions. Resolve current R5 native owner/CLAIM and activity semantic checkpoint through live receipts before a formal Result/Review. The research note is independently durable author-side material and makes no CLAIM or review assertion.
