# R189 — All-aperture exact lifting for latest-source subset queries

Date: 2026-11-16 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Independent portable research; no formal Task CLAIM, native Result/Review, or Foundation promotion is asserted.

**Frozen scientific input:** `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Precursors: R182–R188; immediately preceding exact R188 at `awdawmip/enterprise-math@43366e9337a009acb803ca773b69205e503fd2f1`, especially R187's singleton necessity and R188's pair-oracle lift. Current normative source: `docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context`. P000 and six-axis native spatial typing are unchanged.

## Model and observation boundary

Fix `k >= 1` distinguished, pairwise distinct source IDs and aperture `b >= 2`; queries use nonempty subsets `U` of size at most `min(b,k)`. A complete underlying native history contains ordered X6 paths, branch IDs, positive-rational BRC weights, multiplicities, provenance, and potentially joint-relation coordinates. **Only the declared source-last-occurrence observer is being recovered here.** Its state is a partial permutation `s=(s_1,...,s_r)` of the sources ordered from oldest to newest last occurrence, with `0 <= r <= k`.

The oracle `q_U(s)` returns the rightmost element of `s` contained in `U`, or `NONE` if no element of `U` occurs. The algorithm adaptively chooses `U`, paying unit cost for each oracle query; it knows `k,b`, but not `r`.

Let `Q_b(k)` be the optimal worst-case deterministic number of such queries to recover every partial permutation. Let `C_b(k)` be the optimal worst-case number of **known-support** maximum-of-subset queries of sizes `2,...,min(b,k)` required to sort `k` distinct named elements in an unknown strict total order; on known support a singleton gives its one element for free. Define `C_b(1)=0`. The minimax numbers are finite, since pair queries already sort.

## Theorem R189 — exact minimax transfer for every aperture

For all integers `k >= 1` and `b >= 2`:

```
Q_b(k) = C_b(k) + 1.
```

This extends R188 (aperture two) without requiring a closed formula for the known-support subset-maximum sorting number `C_b(k)`. In particular `Q_b(k)=k` for `b>=k`, since `C_b(k)=k-1`. For `k=1` the empty and singleton histories require exactly one singleton query.

### Lemma 1: adjacent-pair witness for subset-maximum sorting

Fix a deterministic algorithm that sorts every strict order of the `k` elements using queries returning the maximum of a subset of size at most `b`. Along its execution on the particular strict order `a_1<...<a_k`, for **each** adjacent pair `(a_i,a_{i+1})` at least one executed query `U_i` must contain both elements and contain no element strictly later than `a_{i+1}`. On that query the returned maximum is precisely `a_{i+1}`.

Proof: swap those adjacent elements in the input strict order. The winner of a queried subset changes under this swap only when the subset contains both and no element later than `a_{i+1}`; all comparisons with third elements are unchanged. If no such query occurs along the original adaptive transcript, every answer and therefore every subsequent query/output remains identical on the swapped input. The sorted outputs should differ, contradiction. This proves the claim. Each query can witness at most one final adjacent pair, since its maximum is fixed. Thus `C_b(k)>=k-1`.

### Lemma 2: every partial order admits a simulated known-support comparator

Fix a deterministic ID tie-breaking order. Given an unknown partial history `s`, impose a **derived total order** on all `k` IDs: put absent IDs first in the fixed tie-breaking order; place present IDs afterward in their actual last-occurrence order. A known-support sorter requesting the maximum of `U` is simulated using exactly one `q_U(s)` call whenever `|U|>=2`. If the reply is a present ID, that ID is the maximum in the derived order; if it is `NONE`, return the tie-breaking maximum of `U` (then all members of `U` are absent). Queries of size one are deterministic and cost nothing in this simulation. Thus the sorter receives the exact answers of an ordinary strict total order.

Keep both the simulated maximum and the **raw** source oracle result for each query. At completion write the derived sorted order as `a_1,...,a_k`; let `m` be the number of absent elements (an unknown prefix length). Lemma 1 guarantees for every adjacent pair `(a_i,a_{i+1})` a previously issued witness `U_i`. Because every member of `U_i` precedes or equals `a_{i+1}`, its saved raw answer is:
- `NONE`, exactly when `i<m` (then the whole witness subset is absent);
- `a_{i+1}`, exactly when `i>=m` (then its latest member is present).

One additional singleton query `q_{\{a_1\}}(s)` tells whether `m=0`. If present, output all `a_1,...,a_k`. Otherwise `m=1+(`number of initial consecutive `NONE` replies among the saved adjacent witness results`)`; output `a_{m+1},...,a_k`. This also handles `m=k` (empty history). No further nonsingleton query is used.

### Upper and lower bounds

Choose any optimal deterministic known-support sorting decision tree of worst-case cost `C_b(k)`. Lemma 2 simulates it on the derived order and recovers the exact present suffix with one additional singleton, proving `Q_b(k)<=C_b(k)+1`.

For the reverse inequality, restrict an arbitrary correct unknown-support algorithm to full-support permutations. On all such inputs, singleton answers are predetermined and carry no relative-order information, so their nodes can be removed from the decision tree, leaving a valid known-support subset-maximum sorting algorithm. Hence some full-support input requires at least `C_b(k)` nonsingleton queries. R187 Theorem A (also immediate by deleting the oldest full-support source) requires the singleton of its oldest source **on every full-support execution**: deleting that source leaves all nonsingleton answers and all other singleton answers identical. Therefore that same path uses at least one additional singleton, giving `Q_b(k)>=C_b(k)+1`. Equality follows.

## Consequences and uniform resource bounds

1. For `b=2` we recover `Q_2(k)=C_{pair}(k)+1` from R188.
2. For `b>=k`, one maximum query on all remaining sources successively reveals the entire known-support order in `k-1` calls, and Lemma 1 gives the matching lower bound. Thus `Q_b(k)=k`.
3. Any known-support subset query has at most `b` different answers, giving `C_b(k)>=ceil(log_b(k!))`; Lemma 1 independently gives `C_b(k)>=k-1`.
4. A balanced `b`-ary winner tree with at most `k-1` internal nodes supports full selection sorting by rebuilding only an extracted winner's ancestors, at most `ceil(log_b k)` per extraction. This gives the constructive (loose) bound `C_b(k) <= (k-1)(1+ceil(log_b k))`. The same tree lift, using stored witness answers, recovers unknown support using one singleton. Combined with the lower bounds, the query cost is `Theta(k(1+log k/log b))` uniformly for `2<=b<=k` when `k>=2`, with asymptotic constants independent of these integers.
5. Exact exhaustive decision-tree calculations for `k<=4` yield `C_2(4)=5, C_3(4)=4, C_4(4)=3`; hence `Q_2(4)=6, Q_3(4)=5, Q_4(4)=4`. This includes a strict gain at aperture three.

## Reproducibility and evidence scope

The accompanying `R189_bounded_aperture_oracle_check.py` independently implements the source oracle, a b-ary tournament extraction sorter, raw adjacent-witness recovery, and a memoized exact belief-state minimax solver. Integer-only exhaustive runs cover all partial histories for `2<=k<=7`, each `2<=b<=k`, totaling **93,521** (history,aperture) checks and **547,995** adjacent-witness checks. For `k<=4` it separately computes exact known/unknown minimax decision trees and confirms their difference is one. The stored JSON records the exact case tables and observed tournament query counts. These finite tests corroborate the universal symbolic argument; they are not its proof. Independent scientific review: `NOT_REVIEWED`.

The declared observer discards full native path/branch/joint/multiplicity/weight data **only at the source-last-occurrence observer interface**. If a future query touches those richer fields, the full typed BRC/X6 carrier remains necessary until an additional scoped descent certificate is supplied. The unit-cost oracle model excludes source-index construction, input conversion, byte length and native `brc_transport` runtime cost. No claim of external novelty or practical runtime speedup is made.

## Next frontier

Determine closed forms or stronger constructive/minimax bounds for `C_b(k)` at intermediate apertures (especially `3<=b<k`), including its optimal decision-tree structure, and cost the actual positive-rational BRC source-selector against the full typed carrier. Reuse this exact R189 theorem rather than re-running the R187–R188 pair-only work. Control inventory request `em-r1-20261116-0011-inventory-read-v1` was queued when last observed; no owner or Claim is inferred from that pending receipt. Historical researcher `EM-DIRECT-BF4AD7` and SID `MCP-46f202db13e64ad6b4c8860e06908245` are provenance, not new formal execution authorization.
