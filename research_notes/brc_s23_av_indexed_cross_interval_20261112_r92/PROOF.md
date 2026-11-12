# R92 — Cross-interval witnesses and indexed certified OUT boxes

Date: 2026-11-12. Scope: R90/R91's finite rational circular-source model; frozen scientific pin `43ec6098b1330ae86d0a7863be336c5d97f6ef34`. Predecessor [R91](https://github.com/awdawmip/enterprise-math/blob/970708169086e6ab8f3525da1020ff890d8d3fcd/research_notes/brc_s23_av_point_subtree_interval_cache_20261112_r91/PROOF.md), based on R90 `e8435d251eb02e2c8c868e1632a61c439a166f57`. Author-side proved lemmas and exact checks.

## Model

For a finite set of source identities `E={(t,branch)}`, signature `sigma=(j,x,a,b)` (integers `j,a,b`, rational `x`) and real parameter `theta`, let `s_t(theta)={x+(t-j)theta}`, `A(theta)={a theta}`, `B(theta)={b theta}`. The predicate `M_t(theta)` holds when `s_t` is in the directed half-open circular arc `[A,B)`, interpreting wrapping correctly and taking the arc empty if `A=B`. `W_E(theta)` returns the lexicographically greatest qualifying `(t,branch)`, else `NONE`. Query parameter intervals are closed with rational endpoints. R90's six-family exact critical partition certifies existence or absence of either Boolean polarity with exact rational witness or full absence certificate.

## R92.1 — Witnesses transport without interval nesting

Fix `t`, Boolean polarity `p`, and the **complete** signature. If an earlier exact oracle on any parameter interval `I0` returned a rational `z` with `M_t(z)=p`, then for every new interval `I` containing `z`, that exact `z` certifies `exists theta in I: M_t(theta)=p`. **No inclusion relation between `I0` and `I` is necessary.** Conversely, an exact `NONE` result on `I0` entails `NONE` on every `I subseteq I0`.

Proof: `M_t(z)=p` is a pointwise predicate independent of the interval where `z` was originally discovered; inclusion of `z` in the new domain suffices. The second assertion is monotonicity of universal absence under restriction. An old witness outside `I` alone does not decide its existence question; nor does absence on a smaller domain establish absence on a larger one. QED.

The R91 cache required old source-interval containment even for positive witnesses, leaving safe reuse unexplored. The R92 cache stores, per `(t,p,sigma)`, sorted verified witness points and inclusion-maximal exact `NONE` intervals. Binary search finds a witness in `[L,U]` or an absence interval `[l,u]` with `l<=L<=U<=u`. For absence, sorted starts plus prefix-max upper endpoints locate a covering interval exactly. Query: `O(log m)` rational comparisons, memory `O(m)`, current Python insertion `O(m)`; rational comparison bit complexity is separate. No source branch/version is used as a predicate key; branch identity remains preserved for winner recovery.

## R92.2 — Indexed verified-rectangle retrieval

Fix a residue `r` mod 16, signature `sigma`, and query rectangle `I × [lo,hi]`. Every OUT certificate `C=(r,J,[cl,ch],sigma)` is assumed **already exactly verified** to exclude all applicable source times in its rectangle (R90 `cert_box` constructs valid candidates). Build an immutable balanced interval tree on the parameter intervals `J`, with each subtree storing minimum lower endpoint and maximum upper endpoint. A subtree with `min_start>U` or `max_end<L` contains no box overlapping `I=[L,U]`; remove that subtree from candidate retrieval.

**Theorem:** Selecting exactly the boxes whose `J` meets `I`, then running R90's closed-endpoint/midpoint joint time-cover test, returns the exact same coverage answer as scanning all verified boxes.

Proof: A rectangle with `J ∩ I = ∅` contributes no coverage on the parameter domain. The interval tree's pruning inequalities exclude precisely subtrees with no overlapping `J`; the remaining nodes are checked for overlap. Consequently at every `theta in I`, the time-interval coverage union of retained rectangles equals that of the full collection. This union is piecewise constant between consecutive clipped rational `J` endpoints, and each boundary is tested individually because rectangles are closed; the sorted real-time intervals cover `[lo,hi]` iff they form a gap-free union there. Thus the finite exact cover test is equivalent. QED.

Index construction costs `O(B log B)` comparisons and `O(B)` nodes for `B` certified boxes. Sparse overlaps reduce query work; worst-case full overlap still requires many candidates. Index is immutable per certified box collection; persistent incremental box-index edits are next work.

## Composition with R91

R92 retains R91's existing algorithm: locate winner at left endpoint; check existence of a more recent source via the polarity oracle; then check absence of the initial winner. It returns `STABLE_NONE`, `STABLE(t,branch)`, or `CHANGES` with two directly checkable rational parameters and differing winners. R91's point and whole-interval subtree pruning use only exact OUT coverage. Substituting equivalent indexed coverage (R92.2) and logically entailed exact oracle answers (R92.1) preserves every winner, change witness and all-real interval classification. No general BRC family is invented: membership is typed Boolean support, and the lexicographic full-identity observer retains branch ties. The model is an auxiliary circular model, not a six-axis native slice without a declared correspondence.

## Exact reproducible checks

Source: `check_r92.py.gz.b64` (base64 decode, gzip decompress to `check_r92.py`; supply unchanged R90/R91 scripts from their cited releases); machine summary: `verification_r92.json`. Run `python check_r92.py`.

- 265 valid OUT boxes generated by the unchanged R90 certificate generator. 390 randomized exact rectangle-coverage equivalence tests, and 300 polarity-oracle tests against uncached critical-partition calculation all passed.
- 32 shifted intervals contained an earlier valid positive witness but were not subsets of the source interval: R91 called the exhaustive oracle 32 times; R92 once (31 witness reuses).
- 140 randomized queries across 141 retained historical AVL roots matched the R90 independent full critical-partition reference for **all real parameter values**, including 80 verified `CHANGES` witness pairs. In these queries R92 recorded 76 transported witness and 187 absence-subinterval cache uses.
- On 1,001 *actually certified* OUT boxes and 35 repeated sparse-overlap cover calls, the recorded process measured 41.5006ms for whole-list scans vs 1.6019ms for indexed candidates (35,035 candidate upper bound vs 140 returned candidates and 735 visited interval-tree nodes). Those timings exclude index construction and retention and therefore describe query-only cost.

Program output: `R92_PASS 390 300 32 1 140`; exact assertions passed. Source files plus full longer exposition and dependencies are available in the R92 user-facing bundle. This is an author-side computational check; independent review and native Task admission remain separate.

## State and next unit

The exact `RS-S23-AV` task lookup returned `CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION` in [the native receipt](https://github.com/awdawmip/kimi-query-bridge/issues/6847#issuecomment-6813135653). The exact-ID rejection establishes no fact about other S23 publications or owners. The current logical conversation requested its own native Researcher session in [#6848](https://github.com/awdawmip/kimi-query-bridge/issues/6848); its status is reported separately when verified. No takeover of another active owner was performed.

R93: build a persistent OUT certificate interval index with exact insertion/deletion and test identical multi-version input streams against R82 triple index, R86 full profile and R91/R92 algorithms; count all preprocessing/update/bit-complexity/memory and cold/warm queries with witness recovery. Preserve the frozen scientific pin.
