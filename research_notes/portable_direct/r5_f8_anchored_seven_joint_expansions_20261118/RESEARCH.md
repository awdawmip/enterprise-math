# R5 fifth noise chamber: exact 250-pair anchored seven-hypothesis star

Date: 2026-11-18 (Asia/Shanghai). Scientific input is frozen at `435e77af0d180eac32bd1f9c4c464bc4010b7551`; derived scalar integer observer, 101 legal physical costs k=214,...,314, 256 named closure hypotheses. The original 101x256 `EXACT_R5_ALL_101_BUDGETS.json` has SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. This is not a claim of collapsing P000/X6 native paths or joint provenance.

## Theorem (complete anchored two-state extensions, entire fifth chamber)

Let `C_f(H;tau)` be the exact optimal worst-case sum of physical query costs for adaptively identifying one unknown named hypothesis from H, with normal real replies within tau/2 of its integer center, and at most f arbitrary unmarked corrupted replies. Put

- `H0 = {18,24,82,34,17}`,
- `L = 25845652773852463277015040000`,
- `U = 58182461585441404127941754880`.

For every real `L <= tau < U` and every `h in {0,...,255} \\ (H0 union {0})`, **all 250 choices** satisfy

```text
C_8(H0 union {0,h}; tau) = 8335.
```

Thus adjoining mask 0 and any one further genuinely distinct mask to the five-state certificate never increases the restricted game's eight-error optimal budget. The fixed mask label 0 is a hypothesis identifier, not an assertion of a native spatial origin.

## Proof

The existing verified five-state exact Bellman computation gives `C_8(H0;L)=8335`. Enlarging the named hypothesis population cannot lower the worst-case identification cost, so each seven-state game has value at least 8335 throughout the chamber. For a fixed finite H, the game value is nondecreasing with tau since every possible normal response at smaller noise is still available at larger noise.

We performed two complete sets of 250 seven-state exact minimax calculations, one at tau=L and one at tau=U-1. For each of the 500 games, the computed root value was exactly 8335. The query centers are integers, hence when tau<U, the possible normal-response support families are contained in those at integer tau=U-1. Consequently, monotonicity and the two endpoint results give `8335 <= C_8(H; tau) <= 8335` for every stated H and tau. This closes the finite theorem.

Each seven-state endpoint calculation explicitly examines all 101 original physical query budgets and builds every maximal answer-support family from intervals of width tau among the seven exact integer centers. A support family is represented by seven-bit masks; dominated supports are discarded. Identical maximal-support families keep their cheapest physical budget. Seven lie counters with eliminated sentinel 9 are represented in seven unsigned four-bit nibbles. For an answer support S, active count e_i becomes min(9,e_i+1[i not in S]); terminal means at most one e_i<=8. The Bellman recurrence is `V(e)=min_k (k+max_S V(T_S(e)))` over actions with no nonterminal self-loop, and V=0 at terminal states. Every retained successor strictly increases the sum of live mismatch counts, making the exact finite recurrence acyclic. C++17 arithmetic is exact; full equality of packed state keys resolves hash collisions.

## Execution and coverage

The original executed loop used `VERIFY_SIX.cpp` from immutable prior commit `a08d1278c07e2d99f0620536531a69da633dbe45` and the recorded local `scan_seven_anchor.py` driver, compiling with `g++ -O3 -std=c++17`. The new `VERIFY_SEVEN.cpp` is the same Bellman kernel with standard input actions for portable reruns. `RECOMPUTE_ANCHORED_SEVEN.py` reconstructs the complete response-support actions directly from the frozen integer table and compares every root and statistic to the lossless rows certificate. Independent post-sweep spot replay of four rows per endpoint returned exact matching roots, memo-state counts and distinct action-family counts.

- Left-endpoint: 250/250 roots 8335; 78,752,388 aggregate memoized-state visits; largest single root memo 793,461.
- Right-endpoint (U-1): 250/250 roots 8335; 109,556,588 aggregate memoized-state visits; largest single root memo 978,417.
- Total: 500 exact restricted minimax calculations, 188,308,976 aggregate state visits.
- `RESULTS_COMPACT_ANCHORED_SEVEN.json` is a lossless compressed transcript of all 500 rows: [added mask, exact root cost, memoized states, reduced action count] in candidate order; it includes SHA-256 for both complete original local JSON results and the unpacked row lists. The frozen input is referenced by immutable pin/digest, not silently substituted.

**Validation status:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. The full 256-state eight-error optimum remains `8335 <= C_8^*(tau) <= 8343` on this chamber.

## Next scientific question

Repeat the complete 250-candidate two-added-mask star for an anchor other than 0 (e.g. 144 or 208), or exploit support-family invariances to cover all 31,375 unordered two-mask additions without redundant calculations. In parallel, seek an exact full-256 eight-error strategy costing 8335 or a larger multi-mask lower certificate. No new CLAIM/Result/Review or protected Activity update is asserted by this portable author artifact.
