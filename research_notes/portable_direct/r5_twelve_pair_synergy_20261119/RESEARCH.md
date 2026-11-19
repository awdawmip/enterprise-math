# R5 — Twelve-label joint-observer synergy and a compact exact 8335 lower-bound witness

Date: 2026-11-19 (Asia/Shanghai). Status: **AUTHOR_EXACT_FINITE_CHECKED / PARTIAL_INDEPENDENT_CROSSCHECK / NOT_REVIEWED**. Independent portable scalar research; no formal CLAIM/RUN or native X6/Port review is asserted.

## Frozen input and original problem

Scientific pin `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`; exact file `EXACT_R5_ALL_101_BUDGETS.json`, SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`, 1,549,048 bytes. It gives 256 named integer response centers `N_h(k)` for every k=214,...,314, 101 query prices. At the frozen robust endpoint `tau=58182461585441404127941754879`, a correct unflagged scalar response y for h obeys `2|y-N_h(k)|<=tau`. An adversary may make at most f arbitrary unflagged errors; the learner selects queries adaptively and pays the physical price k.

Fix ten named hypotheses `S=(0,16,32,48,1,64,17,80,18,24)`. The preceding exact eleven-label result `enterprise-math@e3f94af33d3eb08e9ce5a9d21481d23e9083e73d` gives `V_8(S∪{t})=8310` for every one of 246 excluded t.

## T12-1 — complete two-addition census at f=0,1,2

For **each** unordered pair {u,v} contained in {0,...,255}\S, there are C(246,2)=30,135 distinct twelve-label subproblems. Direct exact priced maximal-support Bellman recursion over all 101 physical query prices produced these exhaustive distributions:

| f | Baseline | Exceptions |
|---|---|---|
| 0 | V=733: 30,129 | V=734: 3; V=735: 3 |
| 1 | V=1681: 30,128 | V=1682: 1; 1683: 2; 1684: 3; 1685: 1 |
| 2 | V=2628: 30,128 | V=2629: 1; 2631: 2; 2633: 3; 2635: 1 |

No state cap was hit. Six pairs increase V0: `(2,82),(34,82),(50,82)` give 735, while `(8,88),(40,88),(56,88)` give 734. The seventh `(33,81)` preserves V0=733 but increases V1 to 1682 and V2 to 2629. No other pair increases V1 or V2.

Independent Python checked 79 f0 cases, including all seven distinguished pairs, using doubled real-response endpoints instead of the C++ adjacency. It independently recomputed all seven f1 and f2 results.

## T12-2 — exact 12-label eight-error witness at 8335

Define `W=S∪{34,82}`, twelve distinct named hypotheses. Complete exact Bellman recursion yielded

```
V_8(W) = 8335
```

with 2,840,397 nonterminal memo entries. A **separately implemented C++ recurrence** over independently generated endpoint support families reproduced both 8335 and 2,840,397 entries. The exact seven minimal-price maximal families for W appear in `W_ENDPOINT_FAMILIES.txt`; `CHECK_W.cpp` re-evaluates their entire Bellman recursion. The endpoint reconstruction from the frozen integer centers is described below.

Other seven-family values at f8: `(2,82):8327`, `(8,88):8319`, `(33,81):8311`, `(34,82):8335`, `(40,88):8327`, `(50,82):8327`, `(56,88):8319`. All were computed exactly with no state cap. The other 30,128 pairs at f8 remain uncomputed.

Since W is an exact subset of the 256 named hypotheses, `C*_8>=V_8(W)=8335`. Along with the existing full-state upper bound 8343, the prior interval remains `8335<=C*_8<=8343`. **New structural contribution:** a twelve-label 8335 witness replaces the need for seventeen labels in one *specific* existing lower-bound certificate. It is not a proof of globally minimal witness size. It also demonstrates a two-label joint constraint: none of the 246 individual extensions raises S above 8310, but two additions can raise it to 8335.

## Mathematical exactness

For each k, label i has compatible real interval `I_i=[N_i-tau/2,N_i+tau/2]`. Every nonempty observation support is contained in one occurring at the greatest left endpoint among its labels. Thus all inclusion-maximal joint supports are attained at one of the twelve doubled endpoints `2N_i-tau`. Membership of j at endpoint i is the exact integer comparison `0<=N_j-N_i<=tau`. No floating point or discretized-y approximation is involved.

For mismatch vector e_i∈{0,...,f+1}, live indices have e_i<=f, and observation mask M maps `e_i -> min(f+1,e_i+1[i not in M])`. Terminal V=0 when <=1 live label remains. Else `V(e)=min_k(k+max_{M in F_k}V(e^M))`. Maximal supports suffice because a larger compatible mask cannot reduce the adversarial remaining state. Equal maximal support families have equal transitions, so retain the smallest price. Any action having a possible mask containing all live labels is nonprogressing under worst-case observation and can be excluded at positive cost. Every remaining branch advances the finite capped mismatch state; recursion is acyclic.

Source code, independent support verifier, seven complete f8 witness calculations and all 30,135×3 raw rows are retained in the full reproducibility ZIP delivered with the research. The GitHub directory preserves the core proof, scanner, and independent witness checker.

## Scientific scope and next discriminating problem

These conclusions are about the frozen **scalar** R5 observer; BRC/Port/X6-native fidelity requires a separate source-preserving representation map. Independent mathematical review and formal Result acceptance have not occurred. Seek a thirteen-label exact joint witness exceeding 8335, or discriminate whether any other twelve-label pair (including the 30,128 with f0–f2 baseline values) has V8>8335. Do not extrapolate f8 from f0–f2 without the exact DP.
