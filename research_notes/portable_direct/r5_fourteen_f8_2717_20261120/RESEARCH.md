# R5 — fourteen-label joint Bellman exact f=8: 2,717 named pair extensions

2026-11-20, Asia/Shanghai. Evidence grade: AUTHOR_EXACT_FINITE_CHECKED / INDEPENDENT_ENDPOINT_RECONSTRUCTION_CHECKED / NOT_REVIEWED. This is frozen R5 *scalar* observation research. No native X6/Port observer equivalence or formal CLAIM/RUN/Result is asserted.

## Frozen model and inherited frontier

Science source: awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551, file EXACT_R5_ALL_101_BUDGETS.json (SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b), companion stages_18.json. At fixed robust endpoint tau=58182461585441404127941754879, 256 named hypotheses h support integer responses y with 2|y-N_h(k)| <= tau; physical query costs k range 214..314. There are at most f unflagged arbitrary wrong reports. V_f(A) denotes the minimum worst-case total physical cost of adaptively identifying h in named subset A.

Fix W=(0,16,32,48,1,64,17,80,18,24,34,82), and let A(u,v)=W∪{u,v}, for distinct u,v not in W. The preceding complete exact census gave V_f(A(u,v))=735+950f for all 29,646 such pairs at f=0..3, grouped by 1,906 distinct priced *fourteen-way* joint support signatures. Earlier 13-name computations gave V_8(W∪{u})=8335 for every one-name extension. All frozen scientific premises are unchanged.

## Exact finite result

For every pair (u,v) in the 2,717-row class-membership ledger included in this run's reproduction bundle, the exact eight-error optimum is

    V_8(A(u,v)) = 8335.

There are 13 distinct full priced joint-support signature classes with these sizes and representatives:

| Representative | Class size | Memoized f=8 nonterminal states |
|---|---:|---:|
| (162,179) | 308 | 2,800,131 |
| (146,179) | 308 | 4,546,662 |
| (146,163) | 308 | 5,948,001 |
| (130,179) | 308 | 2,000,072 |
| (130,163) | 308 | 4,656,532 |
| (130,147) | 308 | 7,284,748 |
| (117,178) | 214 | 3,160,504 |
| (117,162) | 214 | 4,556,157 |
| (117,146) | 214 | 7,339,375 |
| (117,130) | 214 | 2,067,748 |
| (2,3) | 4 | 4,106,074 |
| (2,5) | 8 | 4,807,044 |
| (2,8) | 1 | 2,560,551 |

All 13 representatives were solved by the fourteen-counter, integer-cost C++ minimax oracle at f=8 with value 8335 and without state-cap failure. The class groups are disjoint: 6×308 + 4×214 + 4+8+1 = 2717 distinct pairs, i.e. 13 of the 1,906 signatures. The remaining 1,893 signatures and 26,929 pairs remain open at f=8.

## Exact quotient and recurrence argument

For each action k and integer observed y, the correct-label support is S_k(y)={i:2|y-N_i(k)|<=tau}. Each inclusion-maximal support is witnessed by a doubled left interval endpoint 2y=2N_i(k)-tau. Equivalently, its bit mask is {j:0<=N_j(k)-N_i(k)<=tau}. Enumerate all 14 left endpoints, discard proper submasks, and retain the physical action price. A response with a larger support weakly lowers every incompatibility counter and is at least as hard for an identifying strategy, hence maximal supports suffice for the adversarial worst-case recurrence. If two actions have precisely identical full joint maximal families, the less expensive action dominates.

Retain e_i∈{0,...,f+1}, live iff e_i<=f. For full support S, update e'_i=min(f+1,e_i+1_{i∉S}). For at most one live label V_f(e)=0. Otherwise the exact recurrence is

    V_f(e) = min_{k: no maximal support contains every live name}
                [k + max_{S∈F_k} V_f(e^S)].

Any omitted action admits an unchanged live state at positive cost; every retained branch advances at least one capped live counter, so the recurrence is finite and acyclic. Identical price-aware signatures have exactly the same action masks, counter updates and costs for *all* states at the fixed f; this is an observer-and-future-operation equivalence over the full game, not a heuristic compression. The C++ solver memoizes integer base-(f+2) counter states and computes the full minimax value, with no floating-point interval tests.

The run rebuilt the 101×256×256 integer center comparisons from the frozen SHA-256-verified source. It enumerated all 29,646 pairs and recovered exactly 1,906 price-aware classes. A separate Python verifier reconstructed the 13 representative families using doubled-left-endpoint integers, agreeing with the adjacency-based C++ families (13/13) and checked 2,717 distinct covered-member rows. Output: PASS_R5_FOURTEEN_ENDPOINTS 13 unique_representatives 2717 covered_pairs. These are author-run proof/compute checks; independent mathematical review remains NOT_REVIEWED.

## Consequence and next direction

The 2,717 named pair cases constitute a proved finite plateau at f=8, and the full 256-label optimal-cost interval remains 8335<=C_8*<=8343. Continue f=8 scanning across the uncomputed 1,893 joint classes, prioritizing high information gain and distinct expensive cases. A discovery of V_8>8335 would strengthen the lower bound; until then, do not generalize the plateau to the remaining pairs. Preserve named labels, signed branch/provenance and future-observer residuals before any native BRC/X6 transfer.

Historical contribution identity: EM-DIRECT-4C3E47, Activity RA-F2257922D00B2FE4C4818DBD. GitHub publication and Activity association are tracked independently of formal execution authority.