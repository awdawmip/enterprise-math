# R5: parametric Pareto-frontier bound and nonmonotone closure-background recourse

Date: 2026-11-15. Status: AUTHOR_PROVED / REPLAYED_EXACT_TABLE / NOT_INDEPENDENTLY_REVIEWED.
Frozen scientific input: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Scope: frozen 954-event, radius-two, indexed-center **derived 1D observer**. No native X6 or BRC equivalence is claimed.

## 1. Parametric state-count theorem (general layered-DAG minimax)

Fix a new-optimizer DAG node at some layer and center/event index j. Let its old-optimizer max-plus response state consist of the old frontier score vector `v` of width `w>=1`. Let `h` be the number of newly selected, weight-bearing internal centers processed since the common starting anchor (the anchor itself has weight zero). Every score coordinate belongs to

```
{-infinity, 0, 1, ..., h}.
```

At that *one fixed new node*, the exact minimax Pareto update retains only vectors that are pairwise incomparable under componentwise `<=`. Therefore the number of stored nondominated vectors is bounded by

```
A(j,h) <= (h+2)^(w-1).
```

At a whole new-DAG rank r with nodes j and corresponding frontier widths `w_j`, the number of retained state vectors is at most

```
sum_{j in NewLevel[r]} (h_r+2)^(w_j-1)
    <= |NewLevel[r]| * (h_r+2)^(W_r-1),
W_r = max_j w_j.
```

**Proof of component alphabet.** Each old path's finite score is the number of coincidences with the h selected weighted new centers processed up to cutoff j. Each coincidence contributes exactly one, and no score can exceed h. An old vertex not reachable from the starting anchor has score minus infinity. Hence the stated finite alphabet has h+2 symbols.

**Proof of antichain bound.** Project the score vectors onto any chosen w-1 coordinates. Two distinct vectors with identical projection differ in their sole remaining coordinate; because that coordinate is totally ordered, the two vectors are comparable. Thus a Pareto antichain contains at most one vector per projection, and at most (h+2)^(w-1) vectors overall. Apply this at each new DAG node and sum over the nodes of a rank.

**Why Pareto deletion preserves the exact minimax.** Every continuation of a fixed new node and rank invokes the same monotone max-plus continuation map F on its old frontier. If u<=v coordinatewise, then F(u)<=F(v). The new player minimizes the final old maximum overlap, so state v cannot improve over u for any common suffix. Discarding v is exact. At the terminal anchor, the minimum retained old overlap equals `min_new max_old |S intersect T|`, yielding `m-min_new max_old |S intersect T|` as the offline max-new/min-old replacement distance.

**Complexity scope.** For a bounded old-frontier width W, the number of retained states per new DAG node is polynomial in h (degree at most W-1). If W grows with input size, the bound is not a uniform polynomial or fixed-parameter-tractable bound: it is an XP-style parameterized state bound. The scalar score alphabet and monotonically increasing DAG edges are hypotheses. The existing implementation uses a finite NEG sentinel (-10^9), valid for the executed h<10^9 instance; a general-purpose implementation should use a true minus-infinity sentinel or a proven finite bound.

## 2. Clarification of the previous measured maximum of 30

The published `VERIFY_R5_OFFLINE_MAXMIN_RECOURSE.py` computes

```python
max_antichain = max(max_antichain, sum(len(v) for v in state.values()))
```

where `state` maps distinct **new DAG nodes** to individual Pareto buckets. Consequently the reported maximum `greatest_pareto_antichain=30` (and case-wise `max_nondominated_states`) is **the largest aggregate retained-state count over one rank**, not the maximum size of an antichain at one node. The maximum old-frontier width 19 is a distinct observed quantity. Both numbers retain their original numeric values; only the label/scope requires correction. In the full 256-case author output, the maximum aggregate 30 occurs for K=219, changed cut 8, old effective masks 12,13,28,29. The proof above supplies a per-node theoretical bound and then an aggregate rank bound.

## 3. Exact nonmonotonicity of worst necessary recourse

Let `r_i(K,B)=max_{S in Opt_{B+i}(K)} min_{T in Opt_B(K)} |S minus T|` with `i not in B`. This is the directed Hausdorff distance between the optimal indexed-center families under set-replacement distance.

The saved 256-row full-background finite table establishes at K=214, changed cut i=8, the exact chain

```
B={}            r_8(214,B)=7
B={9}           r_8(214,B)=3
B={9,10}        r_8(214,B)=7
```

Thus enlarging the *other* closed-gap background may strictly **decrease** or strictly **increase** the max-new/min-old recourse even when the optimum objective value is unchanged and optimizer families expand by inclusion. This is an exact counterexample to either background-monotonicity direction for this observer.

For comparison, the 256-row table gives for i=9 no increasing single-other-bit flips across K214..221; there are 24 decreasing and 232 unchanged. The complete counts of single-other-effective-bit flips (8 budgets, four other effective bits, eight background pairs per bit, hence 256 flips per changed cut) are:

| Changed cut | Increasing | Decreasing | Unchanged | Total |
|---|---:|---:|---:|---:|
| 8 | 28 | 40 | 188 | 256 |
| 9 | 0 | 24 | 232 | 256 |

The two original effective-but-observer-inert bits 3 and 27 contribute only zero flips in both rows. For cut 8, toggling cut 10 can increase recourse when cut 9 is already closed. All figures are deduced from actual `old_effective_mask_order` / `recourse_by_old_mask` entries, rather than resampling paths.

**Proof of finite exhaustiveness.** The existing optimizer-family support theorem establishes that, over K214..221, all 28 closure bits affect the complete optimum families only through E={3,8,9,10,27}. For a selected changed bit, each other-bit flip therefore reduces to one of the eight effective-background pairs among the remaining four bits. Enumerating those pairs for eight budgets and two changed cuts exhausts the 512 finite flips in the original 27-bit background domain up to their exact quotient. The cited table's 256 entries themselves were checked by the previous offline max-plus minimax algorithm; this new step is deterministic integer readout and consequence checking, not an independent reproof of those 256 entries.

## Reproducibility and remaining questions

Sources on the same Draft PR branch: `OFFLINE_MAXMIN_EXACT_RECOURSE_THEOREM.md`, `VERIFY_R5_OFFLINE_MAXMIN_RECOURSE.py`, and `EXACT_R5_OFFLINE_MAXMIN_ALL_BACKGROUND_VALUES.json`. The original complete author output is 144081 bytes, SHA-256 `e8157e196f3d8408a11bf5f67935d4e083578844d6461433f209fed63f4e04ed` (also attached to prior conversation); the compact committed table is sufficient for the flip calculation. Reproduce with `python VERIFY_R5_PARETO_BOUND_AND_BACKGROUND_REVERSALS.py` beside the committed compact table. Expected `PASS_EXACT_R5_PARETO_SCOPE_AND_BACKGROUND_REVERSALS`, 256 rows, 512 effective single-bit comparisons.

Independent review still needed: (i) old/new optimizer language reconstruction and common-anchor exactness; (ii) sufficiency of the old frontier interface; (iii) validity of Pareto deletion in the original rank-labeled event DAG. A useful further mathematical target is a structural bound on W_r from the radius-two geometry or an explicit family with large Pareto width. The present bound makes no asymptotic claim for unbounded W.

This is durable author-side science on an existing Draft branch, not a new Task CLAIM, Source Result or independent Driver review. Preserve provenance and the frozen input pin.
