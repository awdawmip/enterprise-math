# R5: all 244 single-label extensions of W plateau through f=8

Date: 2026-11-20, Asia/Shanghai. Mode: independent portable TASK_RESEARCH, historical contributor `EM-DIRECT-4C3E47`; status `AUTHOR_EXACT_FINITE_CHECKED / SELECTED_INDEPENDENT_DP_CROSSCHECK / NOT_REVIEWED`. No formal CLAIM/RUN or native Result/Review is asserted.

## Frozen definitions and proven predecessor

The scientific input is immutable `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`, file `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. There are 256 named hypotheses, exact integer scalar centers N_h(k), physical query prices k=214,...,314 and fixed robust diameter tau=58182461585441404127941754879. A truthful response y to k satisfies 2|y-N_h(k)| <= tau. Up to f responses can be unflagged errors, and an adaptive strategy minimizes worst-case cumulative physical query price until only one name remains possible.

Fix W=(0,16,32,48,1,64,17,80,18,24,34,82). The predecessor twelve-label certificate reports V_8(W)=8335, at `enterprise-math@3cc19a1b5b6588a5d1e191615d130386db8bec27`, `research_notes/portable_direct/r5_twelve_pair_synergy_20261119/RESEARCH.md`. The predecessor thirteen-label census at `enterprise-math@9bda779f9ae0a4c2340d63eb8e16cc465392b896` proved the following result through f=6, for all 244 individual new names.

## Exact finite theorem: R5-13-F8

For every t in {0,...,255} outside W and every integer 0<=f<=8, at the frozen robust endpoint and with all 101 priced actions,

`V_f(W union {t})=735+950*f`.

Thus every one of the 244 original-name extensions has cost vector
`(735,1685,2635,3585,4535,5485,6435,7385,8335)`.

The new work exhausts f=7 and f=8 for **all** 244 additions (48 complete priced-signature classes, 96 exact root Bellman evaluations). In particular, a restricted witness **containing W** can only beat the f=8 value 8335 after adding at least two fresh names together. This claim does not concern other thirteen-label seeds not containing W.

## Exact algorithm and proof of finite completeness

For each priced action k and 13-name vector H, define its joint response support S_k(y)={i: |2y-2N_{H_i}(k)|<=tau}. All nonempty supports are contained in supports witnessed at doubled interval endpoints. For any i, the doubled right endpoint yields the exact integer mask `{j:0<=N_{H_j}(k)-N_{H_i}(k)<=tau}`; independent Python reconstruction uses doubled *left* endpoints. Retain inclusion-maximal masks F_k. Inclusion-maximal supports suffice because the Bellman value is monotone in the retained possible-hypothesis set. If two query prices have exactly the same maximal mask family, retain the cheaper query: their successors agree for every capped mismatch state. These are exact finite-horizon scalar-observer quotients; no Port/BRC source is discarded or claimed equivalent.

For e=(e_1,...,e_13) in {0,...,f+1}^13, a response support S updates e_i to min(f+1,e_i+1_{i not in S}). The live set consists of e_i<=f. The Bellman value is 0 for <=1 live name, and otherwise exactly

`V(e)=min_{k: each S in F_k misses a live i} [k+max_{S in F_k}V(T_{k,S}e)]`.

An action admitting a support containing every live name has a zero-progress worst-case branch, so positive cost makes it unnecessary in an optimal terminating policy. For all remaining actions, every branch strictly decreases the nonnegative integer potential `sum_i max(0,f+1-e_i)`; memoized exact recursion is finite and complete. Integer costs and integer support comparisons make this a finite exact proof when all signatures and states have been enumerated.

All 244 named t are classified by their **entire priced joint-support family**, not a pairwise projection. Exactly 48 distinct signatures result. Class sizes have histogram: 20 classes of size 1, 8 of size 2, 8 of size 4, 8 of size 8, 4 of size 28. For all 48 representatives, the C++17 capped-counter solver finished f7 and f8 without hitting its state limit. In every class it returned V7=7385 and V8=8335. Maximum memoized nonterminal states: 3,853,240 for f7, 9,426,228 for f8. The 48-class state-count certificate and 244-row value table are included here.

Independent endpoint reconstruction checks all 244 signature assignments from frozen center integers, using a different endpoint orientation from the C++ adjacency. A second C++ oracle with four-bit counter packing (instead of base f+2) and independently constructed endpoint-action lists verified f8 for t=2, 21, 144, returning 8335 in each case, with state counts 2,762,736; 6,850,293; 9,426,228. The second oracle checks three classes, not all 48. These computations are author evidence and have not received independent mathematical Review.

## Full target and next discriminating problem

The full 256-name f8 target remains `8335<=C_8*<=8343`. The new theorem closes the **single-extension route from W**. Search next among fourteen-name sets W union {t,u}, recomputing complete joint supports for each pair rather than combining 13-name decisions. A second independent scientific question is to establish a typed observer/future-operation bridge before using any scalar quotient to suppress native X6/BRC/Port provenance. Preserve the exact original names and frozen science pin throughout.

Publication of this independent evidence does not assert live owner authority, formal Task completion or review acceptance.
