# R5 — Fourteen-name priced observer dominance frontier and three new exact f8 references

Date: 2026-11-20 (Asia/Shanghai). Mode: independent portable scalar research under historical provenance `EM-DIRECT-4C3E47` / original Activity `RA-F2257922D00B2FE4C4818DBD`. Status: **AUTHOR_PROVED_ORDER_REDUCTION / EXACT_FINITE_CENSUS / PARTIAL_INDEPENDENT_BELLMAN_CROSSCHECK / NOT_REVIEWED**. No formal CLAIM/RUN, no native X6/Port promotion.

## Frozen problem

Science pin: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. Exact 101-budget input `EXACT_R5_ALL_101_BUDGETS.json` has SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`; noise endpoint `tau=58182461585441404127941754879`. There are 256 named scalar hypotheses, integer-priced actions k=214..314, and up to f unflagged response errors. All joint masks are rebuilt from frozen integer centers, retaining all 14 named hypotheses and original prices.

Fixed seed W=(0,16,32,48,1,64,17,80,18,24,34,82). A fourteen-name instance is W plus an unordered pair {u,v} of the remaining 244 labels. The previous R5 computation found 29,646 pairs represented by **1,906 priced complete-joint-observer classes**. The previously verified twelve-name lower certificate is V8(W)=8335, hence every such fourteen-name instance has value at least 8335.

## New theorem: reduce cost certification to terminal components of the priced-observer preorder

For two 14-name priced-support signatures A,B with a fixed bijection of named hypotheses, write A <= B if **for each B action b** there exists an A action a with price(a)<=price(b), and every inclusion-maximal joint support mask S of a is contained in at least one maximal joint support mask T of b. The T may depend on S; the selected a may depend on b. We permit either identity or the exchange of the two added label positions, fixing the seed W pointwise.

The earlier D14 policy simulation proves V_f(A)<=V_f(B) for every integer f>=0: simulate the B policy by replacing b with a; map each observed A support S to any containing B support T. Every virtual B mismatch is also an actual A mismatch, and every physical A price is bounded by its B counterpart. This holds for *entire joint support families*, not merely for pairwise separations or scalar marginal signatures.

The relation, with the two-element permutation group acting on the extras, is reflexive and transitive: composing the certified masks, actions, prices and permutations yields the required inclusion. Therefore its strongly connected components are equivalence classes of **dominance-transfer strength**. The finite condensation digraph is acyclic. Every node reaches a sink component. Consequently, to establish V_f<=K for an entire finite family it suffices to certify one representative of every sink component at V_f<=K; all predecessors inherit the bound. This is a *sufficient order-theoretic reduction*, not an assertion that sink classes are independent of every other possible mathematical argument.

## Exhaustive priced-preorder census

On the frozen 14-name signature classes, computed every ordered signature-pair comparison (1906^2=3,632,836 comparisons), with identity or extras-swap matching and the exact action-mask inclusion test. The resulting relation contains **38,127 directed edges (including self edges)**, has **1,066 strongly connected components**, and **333 sink components containing 367 individual signature classes**.

The existing 22 f8=8335 benchmark classes from `research_notes/portable_direct/r5_fourteen_dominance_20261120/` already certified 836 of 1,906 signatures, covering 20,159 of 29,646 named pairs. The new full-price preorder census exactly reproduced those old coverage counts, independently protecting against class-index drift.

## New exact eight-error references and strict additional coverage

Full 14-counter exact integer Bellman minimax at f=8 yielded:

| Signature class | Added pair | V8 | Memoized nonterminal states | Independent doubled-endpoint nibble DP |
|---:|---|---:|---:|---|
| 295 | (19,88) | 8335 | 5,102,830 | agrees: 8335 / 5,102,830 |
| 354 | (21,85) | 8335 | 6,099,014 | agrees: 8335 / 6,099,014 |
| 291 | (19,81) | 8335 | 5,723,293 | not completed |

Recompute complete joint masks and apply the same D14 transfer against the 22 old plus these three new exact references. The union certifies **876/1,906 signatures and 21,301/29,646 named pairs**, an increase of **40 signatures and 1,142 pairs**. Every covered fourteen-name instance has exactly V8=8335: transfer gives <=8335 and monotonic restriction to W gives >=8335.

For clarity, the new contributions in the stated order are: reference class 295 adds 24 signatures / 1,030 named pairs; class 354 adds 13 / 72; class 291 adds 3 / 40. All these counts are strict nonduplicate increments relative to the prior accumulated reference set.

The other **1,030 signatures / 8,345 named pairs** remain without an f8 equality certificate in this run. The 333 sink components are a complete structural frontier for this *specific* preorder, not a claim that all 333 need expensive Bellman evaluation.

## Reproduction and proof boundaries

The initial C++ priced-support census and preorder program were compiled with g++ -O3 -std=c++17 and executed against `window_adj.bin` (6,619,136 bytes, computed from the pinned JSON with the predecessor's `make_adj.py`). `CHECK_PREORDER.cpp` is a compact repeatable implementation using the prior branch's exact action construction; it checks all key integers as assertions.

The first exact f8 oracle used an expanded 14-counter version of the earlier exact packed Bellman recursion. Two cases, (19,88) and (21,85), were also rebuilt independently from doubled integer endpoints, with distinct 4-bit counter packing and the same 8335 result. (19,81) has one exact solver only; its review status remains authored. Each DP retains all 14 named counters, all 101 physical actions up to proven same-mask least-price reduction, and exact support transitions. No finite search limit was reached for these three completed runs.

No new claim is made about the other 8,345 pairs, about full-256 C8*, or about native six-axis X6/BRC equivalence. In particular, the pre-existing full-game bound remains **8335 <= C8* <= 8343**.

## Next research question

Choose high-f8-value or high-transfer-coverage representatives among the remaining 1,030 signatures, retaining the 333 sink-component frontier. Compute another exact 14-counter reference, or derive a stronger policy-level observer simulation beyond static action dominance. A witnessed V8>8335 for *any* remaining pair would tighten the full-game lower bound; until then no such improvement is asserted.
