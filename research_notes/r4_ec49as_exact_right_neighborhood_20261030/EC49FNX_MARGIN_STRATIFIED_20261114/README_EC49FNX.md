# EC49FNX — Margin-stratified rooted-cost envelope and sparse repair

Date: 2026-11-14. Scientific input frozen pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: `AUTHOR_EXACT_FINITE_PROOF / NOT_REVIEWED`.

This is a continuation of [EC49FNW, PR #2334](https://github.com/awdawmip/enterprise-math/pull/2334), retaining the 84 frozen first-neutral seven-cache-key exchanges originally selected by EC49FNS. It does not re-optimize the 1,000 configurations or assert a formal RS-EC49AS Result.

## Exact theorem: cut-margin-stratified rootwise dominance

Let `L={0,...,23}` be 24 distinguishable labels and `R={03,05,06,07}` the four legal native rooted-prefix microstep roots. For configuration `K`, `D_{K,r}(S)` is the exact integer minimal ordered signed native prefix cost covering label subset `S` using root `r` (other labels may also be covered). A complete lawful root assignment `a` has cost `F_K(a)=Σ_r D_{K,r}(S_r(a))`. Root cover monotonicity gives the exact bound `LB_K(p)=Σ_r D_{K,r}(S_r(p)) ≤ F_K(a)` for every complete extension `a` of partial assignment `p`.

Fix cutoff `B`. The source cutoff search collects `P={p:LB_K(p)>B}`. A source-cut node that assigns a label to a root no longer legal in target `K'` has no target completion and may be omitted from cut-transfer checks. For each remaining source-cut node put `m(p)=LB_K(p)-B`, a positive integer, and form the margin stratum `P_m={p:m(p)=m}`. Define per-root loss envelopes over the **actual cut-node rooted subsets**:

```
d_r(m) = max(0, max_{p∈P_m} (D_{K,r}(S_r(p)) - D_{K',r}(S_r(p)))).
```

**Theorem.** If `m > Σ_r d_r(m)`, then every node of `P_m`, and every target-lawful complete extension of such a node, costs strictly more than `B` under `K'`. Proof: summing `D_{K',r}(S_r(p))≥D_{K,r}(S_r(p))-d_r(m)` yields `LB_{K'}(p)≥B+m-Σ_r d_r(m)>B`. Monotonicity extends the inequality to every completion. The root subsets are grouped by *source margin*, with no collapse of signed native word order, branch/label identity, or root assignment provenance.

For strata not satisfying this sufficient inequality, check the target lower bound on their members individually. Only nodes with target `LB≤B` require a cutoff-based completion search. Separately enumerate every root choice newly legal in `K'` but absent in `K`. Finally compare all retained source low-cost complete root assignments under target rooted costs. If these checks find no new complete assignment of cost `≤B` and the low-cost assignment identity-to-cost maps coincide with source, the first two distinct layers `C` and `S` (both ≤B) remain identical; thus `(C,m_opt,g=S-C)` are identical. This is the EC49FNT two-layer lemma, with the new grouped cutoff-transfer certificate.

## Exact finite census (frozen 84 edges / 168 directions)

Source: 94 complete cache keys, 178,850 lawful ordered signed words, 38,169 seven-key configurations, original frozen 1,000 exact solutions numbered 32000–32999, and the 84 EC49FNS first-neutral edges with 51 distinct endpoint configurations.

| Measured finite quantity | Exact count |
|---|---:|
| Directed transfers / preserved first-two-layer assignment maps | 168 / 168 |
| Entire cut frontier certified with margin groups, no target cut-node comparisons | **166 / 168** |
| Prior FNW all-subset global root-envelope certification | 103 / 168 |
| Source cutoff-pruned nodes, all directions | 16,876 |
| Target-lawful source-cut nodes | 16,624 |
| Target-illegal source-cut nodes | 252 |
| Margin groups total | 3,587 |
| Margin groups certified without cut-node target checking | 3,575 |
| Cut nodes certified by grouping | **16,550** |
| Remaining candidate nodes | 74 (12 groups in two directions) |
| Direct target lower-bound comparisons for those candidates | 74 |
| Candidate cuts requiring local refinement | 18 |
| Local refinement DFS visits / new low-cost leaves | 84 / 0 |
| Newly legal target label-root pairs / their DFS visits / new low-cost leaves | 4 / 592 / 0 |
| Paired root-subset comparisons across margin groups | 47,760 |

The two exceptional directions are **32315→32279** and **32318→32279**. Each has 37 candidates in six unresolved groups, of which nine actual cut nodes need refinement; their 42 local DFS nodes give zero low-cost leaves. Each has two extra target-only root pairs, checked by 296 nodes and zero leaves. Every other directed transfer is fully certified by margin groups, except the separate new-root guard where applicable.

Compared with testing each of the 16,624 target-lawful source-cut nodes individually, the **grouped procedure calls only 74 direct target cut-node lower-bound checks (99.55% fewer)**. The grouped procedure queries 47,760 target root subsets, whereas naive separate four-root queries on every target-lawful cut would use 66,496 such queries (28.18% fewer in this particular query-count comparison). These are operation counts; no runtime-speedup claim is made, and margin-group creation / source-root costs still have computational cost.

All 168 original frozen directed transfers were reverified with the grouped certificate plus sparse exact repairs and target-only root enumeration. The result is an exact finite author-side computation and general sufficient inequality, not an independently reviewed theorem or a bound for arbitrary BRC family size.

## Evidence and reproduction

The attached `EC49FNX_MARGIN_CERT.txt.xz.b64` decompresses to all 168 directed certificate rows, SHA256 `7097b93083e70b559956adaa7788154019fe3c833b6d1d962b353ef87602279d`. The local full compilable `VERIFY_EC49FNX.cpp` uses the identical frozen native rooted trie and cutoff DFS from EC49FNU/FNW, adds margin partitioning and restricted root-subset envelopes, and performs fallback repairs. Its SHA256 is `c22259e5c15bdbbf28360b586c12974c22f199e7dcff2eeee359b4588e9ea5b5`. Both `g++ -std=c++17 -O2` and `-O3` produced byte-identical output and terminal summary. The repository `MARGIN_ENVELOPE_EXTENSION.cpp.txt` documents the new standalone reusable algorithmic insertion; the complete exact original local evidence bundle is separately retained.

Exact original frozen input SHA256 hashes:
- `master_and_radius3_cases.txt`: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
- `EXACT_NATIVE_32000_32999.txt`: `c9314021942397a0b5a3e7a90d965fb19a853bdc486f7610721fc748a057c0f9`.
- `FIRST_NEUTRAL_EDGES_EC49FNS.txt`: `db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41`.

Verification summary: `directions=168 all_safe=166 source_cuts=16876 legal_cuts=16624 impossible_cuts=252 groups=3587 safe_groups=3575 unsafe_groups=12 paired_root_queries=47760 safe_cuts=16550 possible_cuts=74 fallback_checked=74 fallback_failed=18 repair_nodes=84 repair_leaves=0 target_only_pairs=4 target_only_nodes=592 target_only_leaves=0`.

**Next research question:** derive a cross-root joint support envelope, rather than summing separate rootwise maxima, and measure whether one compact coupled certificate can eliminate the 74 residual cut checks without introducing a full target cutoff-DFS. Test against non-stable neighbor edges to establish discrimination, not only stability on preselected edges.

Task/authority scope: independent scientific research artifact. Formal shared Task, CLAIM, Result, mathematical acceptance, and any personal researcher activity remain distinct and must have their own genuine receipts.
