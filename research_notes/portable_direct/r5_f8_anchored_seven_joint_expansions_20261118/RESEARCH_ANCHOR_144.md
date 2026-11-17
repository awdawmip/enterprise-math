# R5 f=8: second complete seven-state anchor star (mask 144)

Date: 2026-11-18 Asia/Shanghai. Same frozen input `435e77af0d180eac32bd1f9c4c464bc4010b7551`, scalar observer input SHA256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.

Write `H0={18,24,82,34,17}`, `L=25845652773852463277015040000`, and `U=58182461585441404127941754880`. The prior `RESEARCH.md` in this directory certified the 250 distinct seven-state games `H0 union {0,h}` across the entire real interval `L<=tau<U`.

**New exact theorem:** for all real `L<=tau<U` and every `h in {0,...,255} \\ (H0 union {144})` (250 distinct choices),
```text
C_8(H0 union {144,h};tau)=8335.
```
The previously certified restriction `C_8(H0;L)=8335` is a lower bound for every such enlarged hypothesis population. Direct exact C++17 seven-counter Bellman minimax runs across all 101 physical budget options returned **8335 in every one** of the 250 games at each of the two endpoint thresholds `L` and `U-1`. Because centers and pairwise gaps are exact integers and the response support game is monotone in the real noise width, those endpoint bounds give the stated full-interval result.

Calculation evidence (500 new seven-state runs):
- Left: 250/250 exact roots = 8335, total 75,506,621 memoized-state visits; original local full JSON SHA256 `19ab6899e78f578fa17fd14bfbc7ac330fcb0085ddd913b474204d8a1f8fb1b5`.
- Right: 250/250 exact roots = 8335, total 118,635,350 memoized-state visits; original full JSON SHA256 `db49efacc5c1f81ec9db4dbf3c13de66e61a08d073d4799aad7e4da6ba7fd116`.
- `RESULTS_ANCHOR_144_COMPACT.json` losslessly stores the complete 500 rows as zlib/base64 JSON arrays of `[added_mask,root_cost,memoized_states,reduced_action_families]`, with separate decoded-row SHA256 hashes.
- Execute/verify with `VERIFY_SEVEN.cpp` and `VERIFY_ANCHOR_144.py` from this same directory, using the frozen original input table at the referenced immutable pin.

**Combined local result:** the stars anchored at mask 0 and mask 144 cover `250+250-1=499` distinct unordered pairs among the 251 masks outside H0, each with exact seven-state game value 8335 uniformly in the fifth noise interval. This is a finite two-anchor theorem over **499 of the 31,375** possible two-mask extensions of H0. Full256 f=8 optimum remains in [8335,8343].

Mathematical status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. The named masks are scalar hypothesis labels and not P000 native origins. No protected owner/CLAIM/Result/Review updates are asserted. Next: test the anchor 208 star, seek a support-family structural classification that covers the remaining unordered pairs, or find a 256-state eight-error strategy of cost 8335.
