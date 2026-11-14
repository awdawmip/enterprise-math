# R762AA — Sharp nested-chronology seed frontier and three-root BRC scheduling residual

Date: 2026-11-14 (Asia/Shanghai). Scientific status: **AUTHOR PROOF + EXACT FINITE RECOMPUTATION / NOT_REVIEWED**.

Mother question: `RS-X6-TRIADIC-CLOSURE-DYNAMICS` / publication `TP2-8B7E13C5904A2D6F1142`. Scientific pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Scientific predecessors R762Y (#2358) and R762Z (#2362). Current author's own Source session registration was requested as `emr3-20261114-1034-r762aa-new-researcher-start-01`, SID `MCP-4b2d70a97f594366a7c94a0f8b45df38`; formal Researcher-ID / RA / CLAIM are not inferred from its QUEUED reply.

## 1. Exact model

Take the directed cycle `v_i -> v_(i+1 mod q)`, with q>=2 named ports. A labelled macro `C_r` starts at root r, traverses all q cycle edges once in their oriented order, and returns to r. Each elementary edge consumes one integer token at its tail and places it at the head. Tokens are indistinguishable, stocks remain nonnegative, and total stock K is fixed at time zero; no new tokens arrive. Macros have individual progress counters 0..q. Their steps may interleave but each internal step order remains fixed. The *first start* of every macro must follow an imposed source-root word w. Leaving a previously active macro that is still unfinished to execute another macro incurs one interruption; switching after its completion costs zero. Let H_q(K;w) minimize interruptions over all nonnegative initial allocations of K tokens and all legal schedules.

These are auxiliary, provenance-labelled V29 PASS schedulers. No assertion of native `TRIADIC_CLOSURE_E` admissibility, V17 frame dynamics or V39 transport follows from this model.

## 2. Theorem AA1 — sharp palindromic chronology frontier

Let 1<=d<=q and let r_0,...,r_(d-1) be pairwise distinct cycle vertices, in **any** order. Define the first-start word

`w = (r_0,r_1,...,r_(d-1),r_(d-2),...,r_0)`.

For every integer K>=1,

`H_q(K;w) = max(0,d-K)`.

For K=0 and nonempty w there is no legal execution.

**Proof — lower bound.** At most K of the d distinct roots can have an initial token. For each other root, consider its first ever macro start. No previously finished macro rooted elsewhere could have left a token there: each complete C_r returns its token to r. To enable this first start, an unfinished different-root macro must carry a token to this root, and switching from that unfinished macro to the new one incurs an interruption. Distinct newly activated roots require distinct switching events. Therefore every legal schedule has at least d-K interruptions (also at least zero).

**Proof — constructive attainment.** If K>=d, place one token at each root and execute every macro uninterrupted in first-start order. Suppose 1<=K<d. Place one token at r_0,...,r_(K-1). Execute the first-start macros at r_0,...,r_(K-2) completely, leaving their root tokens unchanged. Start the first r_(K-1) macro and advance it to r_K; suspend it exactly once and start the first r_K macro. Repeat: suspend the current macro at the next distinct root until first r_(d-1) is reached. This is possible because a full directed q-cycle from any root visits every other vertex once before returning. Finish the deepest r_(d-1) macro. Unwind the suspended macros in reverse order; when each C_(r_j) finishes and returns its token to r_j, execute the second macro rooted at r_j completely, for j=d-2,...,K-1. Finally execute the second macros rooted at the previously seeded r_(K-2),...,r_0, in the prescribed order. Exactly d-K departures from unfinished macros occurred, and every first start follows w. This attains the bound. QED.

The construction preserves source labels, temporal order, macro progress and integer inventories. It is an exact zero-slack resource–interruption tradeoff under a nontrivial prescribed chronology, contrasting with the possible order penalty of R762Z.

## 3. AA2 — complete finite three-root chronological census

Fix q=3, root 0 as the first-start root, K=1 initially at port 0, and allow each subsequent root to be 0,1,2. The independent exact-integer verifier enumerated **all 3^(n-1) words** for each n=1,...,7 (1093 total), every legal interleaving, and computed the optimal interruption count by memoized Bellman recursion. Among these, 846 words visit all three roots. The full three-root cost histogram is:

| n | all three-root words | cost 2 | cost 3 | cost 4 |
|---|---:|---:|---:|---:|
| 3 | 2 | 2 | 0 | 0 |
| 4 | 12 | 12 | 0 | 0 |
| 5 | 50 | 40 | 10 | 0 |
| 6 | 180 | 100 | 78 | 2 |
| 7 | 602 | 210 | 336 | 56 |
| **total** | **846** | **364** | **424** | **58** |

This is a complete finite classification for the stated bounded domain, not an assertion of a universal enumeration formula.

**Same terminal BRC/V29 counts, different chronology requirements.** Compare `w_1=(0,0,1,1,2,2)` and `w_2=(0,1,2,0,1,2)`. Each has two macros of each named source and therefore exactly six PASS occurrences per directed cycle edge, the same nonnegative terminal M, source histogram, boundary balance and (u,Omega). Nevertheless the exact optimization gives:

| seed budget K | H_3(K;w_1) | H_3(K;w_2) |
|---|---:|---:|
| 1 | 2 | 4 |
| 2 | 1 | 2 |
| 3 | 0 | 0 |

The 1-seed difference 2 is an observable chronological source residual beyond the complete terminal V29 count. The n=6 count histogram additionally certifies two three-root words reach cost 4. The exact DP witness `(0,1,2,0,2,1)` has optimum 3, while naive source-stack greedy that always pops to an available earlier root uses four pushes; this shows one cannot assume the cheapest chronology is obtained by local source reuse.

## 4. Verification kernel, completeness, and provenance

Source: `research_notes/R762AA_THREE_ROOT_VERIFY.py`. JSON output: `research_notes/R762AA_THREE_ROOT_EVIDENCE.json`. A state stores the vector of per-macro progress and last executed macro. At any state, reconstruct port stocks from the fixed initial stock by adding `-e_r+e_(r+p mod q)` for each incomplete macro with progress p. Only the first not-yet-started macro may first start, and its next edge may fire only when its source stock is positive. Each transition increases the total progress by one, so the state graph is finite and acyclic; Bellman minimization over every legal transition is exact for the declared finite domain. It charges one precisely when switching away from the last active unfinished macro. The validator independently checks all 30 distinct-root palindromic cases q=3,4 fixing r_0=0 with every budget K=1..d and every initial token allocation; all attain d-K. It also retests 127 binary-root words against R762Z's B-run formula. Every assertion passed.

The human construction proves AA1 for all finite q,d,K under the specified hypotheses. AA2 is a finite computational classification, with no claim beyond the enumerated n and q.

## 5. Scientific continuation

The actual native `TRIADIC_CLOSURE_E` Cell/Link/Port rule, allowable macro preemption and resource semantics remain the decisive missing bridge. A focused independent next unit is to derive typed native legality for these macro traces and test whether AA1 survives the actual event update and V17/V39 observer; a separate mathematical extension is an exact general three-root language/frontier characterization beyond n=7. P000, ACTIVE worldview and frozen Source science are unchanged. No formal Result or Driver review is claimed.
