# R5 — exact event-weighted minimax bitmap checkpoints

Date: 2026-11-13 (Asia/Shanghai). Status: author-side theorem and finite original-fixture verification. This is an unclaimed R5 auxiliary-model development, not a task Result/review. Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Stack parent: R5 sampled bitmap PR #2199, commit `79b45859d27fed78b0a25fedf27806a0debc30c4`. No change to 28 coordinate inputs, 15 labeled operations, the 1,065 ordered certificates or the 2,520-byte serialized seed.

## The new theorem

Let terminal activation-wall codes `e_i` be sorted into distinct rational walls `w_0<...<w_{W-1}` with multiplicities, `M` terminal certificates, `W` walls, and terminal intervals `[L_v,H_v)` for the prefix tree. Define `E(b)=#{i:e_i<b}` for each integer `0<=b<=W`. The sequence `E` is nondecreasing, with `E(0)=0` and `E(W)=M`. This formulation counts tied terminals independently and only permits a checkpoint at a **complete wall-group boundary**.

Choose any set `S subseteq {0,...,W}` of checkpoint wall ranks and store bitmap `A_s=sum_{i:e_i<s}2^i` at each `s in S`. For a query `b=upper_bound(w,r)` choose a checkpoint `s` minimizing `|E(b)-E(s)|`. If `b>=s`, insert terminal-position bits for all events with `s<=e_i<b`; if `b<s`, delete precisely the bits with `b<=e_i<s`. The resulting bitmap is **exactly** `sum_{i:e_i<b}2^i` because the event classes are disjoint. Thus restricting it to `[L_v,H_v)` and applying popcount gives the exact certificate count `C_v(r)` for arbitrary prefix, rational parameter, repeated wall and arbitrary query order.

For checkpoint budget `K>=1`, define the exact worst residual-event count

`R*(K)=min_{|S|<=K} max_{0<=b<=W} min_{s in S}|E(b)-E(s)|`.

The following greedy feasibility test is optimal for a proposed integer radius `R`: take the leftmost uncovered `E(b)`; choose the farthest available checkpoint center `E(s)<=E(b)+R`; cover all remaining `E(t)<=E(s)+R`; repeat. **Proof of greedy optimality:** any feasible first center covering this leftmost point is at most `E(b)+R`. Replacing it by the rightmost feasible center cannot lose uncovered points to its right; all points to its left were previously covered. Exchange this first center and induct. Binary search the least `R` whose greedy covering uses at most `K` centers. This constructs an optimal **discrete** radius, including duplicate positions `E(b)`. No continuous-center relaxation or approximation is used.

Preprocessing: event sorting `O(M log M)` and `E` construction `O(W+M)` if not already available. Each greedy check is `O(W log W)` with the shown binary searches, or `O(W)` with a monotone two-pointer sweep; binary search needs `O(log M)` checks. Query uses a checkpoint directory and exactly the counted residual terminal bit updates, plus bitmap popcount. Width `M` affects bit-operation cost. Nonuniform checkpoints add a directory (checkpoint ranks / event positions) absent from constant-stride arithmetic.

## Original frozen-fixture findings

A local Python standard-library verifier re-executed the previously verified exact rational source fixture and obtained `N=2880, M=1065, W=953`, wall multiplicity at most 3. It compared to the original Wavelet/fraction oracle for every one of 2,880 nodes at 20 original parameters (57,600 cases), plus all 953 equal-wall root queries, for all seven budgets. At `K=239` it additionally compared **all 954 possible rank boundaries across all 2,880 nodes**, 2,747,520 further exact counts. All passed. The precise executed local program and its full JSON record are available in the current run's attached artifacts; the GitHub portability version here needs independent clean-checkout execution.

| Uniform stride B | Snapshot budget K | Optimized centers actually used | Uniform one-sided worst events | Uniform nearest-center worst | Proven optimal worst events |
|---:|---:|---:|---:|---:|---:|
| 1 | 954 | 954 | 0 | 0 | 0 |
| 2 | 477 | 351 | 3 | 2 | 1 |
| 4 | 239 | 213 | 5 | 3 | 2 |
| 8 | 120 | 120 | 10 | 6 | 4 |
| 16 | 60 | 57 | 21 | 10 | 9 |
| 32 | 30 | 29 | 40 | 25 | 18 |
| 64 | 15 | 15 | 78 | 57 | 36 |

Notably `K=239` requires only 213 stored masks for an exact worst-case bound of 2 event updates, versus 239 masks and a worst-case count of 5 with the earlier one-sided `B=4` method. Measured Python mask-list objects: 33,108 bytes instead of 37,516, **excluding** the new checkpoint directory (15,624 Python bytes as implemented) and all shared event/rank/wall structures. Thus the full resident-heap claim is **not** a net reduction without compacting the checkpoint directory.

In a same-process five-median experiment, the weighted `K=239` variant measured 0.999/1.791/7.527/9.348 ms across root(256), broad(512), random(2048), hotmix(2048) workloads versus one-sided uniform `B=4` at 0.938/1.746/7.329/8.836 ms. The additional nearest-checkpoint selection and bit clearing currently outweigh lower update counts on these loads. At a 15-mask budget, weighted improved random queries from 12.106 to 11.479 ms and hotmix from 13.924 to 12.839 ms. Timing includes rational wall lookup and query itself, not corpus construction, seed decoding, index construction, process RSS or output serialization. Numbers are one local CPython environment, not cross-platform performance bounds.

## Next discriminating unit

Implement the optimal checkpoint directory using compact uint16 event-position/rank arrays, avoid repeated Python-object allocation, measure allocation/build time and end-to-end RSS; compare uniform one-sided, uniform bidirectional and weighted bidirectional at equal total byte budgets (not just equal bitmap count). Separately execute the committed portable script from actual GitHub bytes on its stacked ancestry and read back the output. Frozen R5 inputs remain unchanged. Formal Source Activity checkpoint, task CLAIM, Result and independent mathematical review retain their actual separate authorities.
