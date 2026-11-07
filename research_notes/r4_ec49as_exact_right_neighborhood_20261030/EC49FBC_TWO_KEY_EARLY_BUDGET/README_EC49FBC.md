# EC49FBC — exact H2–H5 early-edge minimum with the 31-edge, two-key H2/H3 baseline

Date: 2026-11-05 (Asia/Shanghai). Type: author-side finite exact optimization and independent Python numerical crosscheck. Scientific-input pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Status: AUTHOR_EXACT_FINITE_DP_CHECKED / UNREVIEWED / NOT_ADMITTED.

## Theorem (full H9-budget implication, fixed H2/H3)

Consider the frozen seven-operation native signed-X6 BRC model of EC49FAV–EC49FBB, with final signed displacement `(+2,0,0,0,0,0)`, complete positive-primitive-step six-axis keys, nine-history observation rank nine at every horizon H2–H9, and at most five distinct complete cache keys globally. Fix the **31-edge, two-key** initial construction

- H2 = {`de`, `ec`, `fe`};
- H3 = {`feg`, `gef`}.

Allow arbitrary finite legal word subsets and arbitrary cache-key mixtures inside H4 and H5. Then the minimum number of distinct **signed primitive X6 prefix edges** in H2–H5 among complete legal H2–H9 constructions is exactly

```
           min E(H2..H5) = 39.
```

In particular this strengthens a local early-window optimization to the *actual global five-key budget* and contrasts with the 38-edge early optimum for the fixed 16-edge, three-key H2/H3 baseline proven in EC49FBB. It makes no global E(H2..H9) optimum assertion.

The restricted subproblem in which H4/H5 use at most one new complete key beyond the initial two has exact minimum **53** early signed edges, even without imposing H9 extendibility.

## Enumeration and proof

Primitive steps are `a=(-1,-1)`, `c=(+1,+2,-1,-2)`, `d=(+2,+1,-2,-1)`, `e=(+3,+1,+1,-3)`, `f=(+1,-1)`, `g=(+2,-2)`. The seventh operator `b=(-2,-2)` cannot occur on any target-endpoint word because it contributes negative net E2 with no compensating operator. Enumerating all `6^4+6^5=9072` words over `acdefg` with signed displacement and the frozen nine-state observer gives precisely **206** legal H4 words and **1062** legal H5 words. They use **27** complete keys outside the two fixed early keys `(3,0,1,0,0,0)` and `(3,1,1,0,0,0)`.

For a target-endpoint Hh word, write `z=#e=#a+1`, `r=#c+#d`, and let `x,y` be the first two coordinates of the positive-primitive cache key. Counting operation occurrences yields `r=x+y-h-1>=0`. Thus an H9 key requires `x+y>=10`. Among the 27 new keys appearing at H4/H5, precisely one satisfies this: `k9=(6,4,1,0,0,0)`. Neither original key can serve H9.

Every globally five-key H2–H9 completion belongs to one of the following **covering relaxations** of its H4/H5 candidate pool:

1. The H9 key does **not** occur at H4/H5. Allow the original two keys plus any two of the other 26 early keys, reserving the fifth key for H9. Exhaust `C(26,2)=325` pools; 172 are rank-feasible and the minimum signed-prefix edge count is **39**.
2. The H9 key **does** occur at H4/H5. Allow the original two plus `k9` and any two of the other 26 keys. Exhaust another 325 pools; 193 are rank-feasible and the minimum is **39**.

Allowing keys that are not selected only enlarges these candidate pools, preserving lower bounds. Each pool includes all ordered eligible operation words, inserted into a trie of **signed primitive steps**, marking the 31 previously paid prefixes. A terminal H4 signature contributes its six-bit mask, and a terminal H5 signature contributes the mask shifted by six bits. For every node v, a min-plus DP over exact 12-bit bitwise-OR masks minimizes the number of selected nonfree incoming primitive edges. The recurrence combines children by `D_new[a|b]=min(D_new[a|b], D_old[a]+D_child[b])`; a nonempty selected nonfree branch pays exactly one incoming edge. Induction on trie height proves the DP enumerates all candidate subsets and computes their exact prefix-union cost. Apply EC49FAR's verified rank-nine clauses `(E|F)&(C|F)&(D|G)&(J|G)` to both window masks. The two cases cover every global five-key completion, giving `E(H2..H5)>=39`.

With at most *one* new early key, 27 pools were tested; seven feasible, minimum 53. These calculations use integer arithmetic and ordered signed native X6 prefixes; no observer quotient is used for costs.

## Achieving the bound and full legal extension

An early 39-edge witness is H4={`fegg`,`gefg`}, H5={`feggg`,`gefgg`}; its two added keys are `(3,2,1,0,0,0)` and `(3,3,1,0,0,0)`. It has masks F|G at both horizons. One actual full H2–H9 completion using exactly five keys is:

```
H2: de ec fe
H3: feg gef
H4: fegg gefg
H5: feggg gefgg
H6: fegccc fegddd gefccc gefddd
H7: fegccfg fegddgf gefccfg gefddgf
H8: feggfgfc feggfgfd gefgfgfc gefgfgfd
H9: feggfgfgf gefgfgfgf
```

The H6–H9 key is `(6,4,1,0,0,0)`. Independent literal enumeration of all selected primitive signed prefixes gives cumulative edge counts `22,31,35,39,85,97,125,131` at H2,…,H9: **131** edges total. Every horizon passes signed endpoint, allowed observation, nine-history rank, and the five-key budget. This attains **39 early edges**, but is not competitive with the known independent global upper bound of 94.

## Verification, provenance and remaining question

`VERIFY_EC49FBC.js` is the actual executed Node.js 22.16.0 integer enumerator. Its full raw JSON includes all 27+325+325 pool records, optimal witnesses, node counts and state counts; `EXACT_SUMMARY_EC49FBC.json` records the concise result. A separately implemented, actually executed pure-Python enumeration and primitive-prefix min-plus DP matched **all 677 exact pool minima**, and independently checked the full 131-edge eight-horizon witness. The Python local source/report are retained as distinct verification assets for this run and may be added to this branch at the next coherent handoff.

Next EC49FBD: fix the 31-edge H2/H3 branch and the four keys in the 39-edge early witness; jointly optimize H6–H9 under the fifth key instead of using the 131-edge extension, or search alternative two-key H2/H3 rank-nine schedules. Compare effects on total native-prefix cost against the proven 38-edge early alternative and existing 94-edge upper bound.

Frozen sources unchanged; P000/ACTIVE worldview unchanged. GitHub storage is author evidence, not a native CLAIM, Result, independent Driver admission, or P000 promotion.
