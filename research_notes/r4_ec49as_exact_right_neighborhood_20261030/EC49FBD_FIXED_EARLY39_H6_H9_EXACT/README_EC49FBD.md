# EC49FBD — 127 signed-X6 edges, exact optimum for the fixed 39-edge early family and fifth key

Date: 2026-11-05 (Asia/Shanghai). Scientific input frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Status: AUTHOR_FINITE_THEOREM / TWO_IMPLEMENTATION_EXACT_CHECK / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED.

## Exact theorem

Work within the previously frozen seven-operation, ordered native signed-six-axis BRC model, with signed endpoint displacement `(+2,0,0,0,0,0)`, six allowed observation signatures, nine initial observation histories (rational rank 9 per horizon), and at most five distinct complete positive-primitive-step cache keys over H2–H9.

Fix the following H2–H5 word sets:
```
H2  de ec fe
H3  feg gef
H4  fegg gefg
H5  feggg gefgg
```
They have exactly 39 different **signed primitive prefix edges**, and the four complete cache keys `(3,0,1,0,0,0)`, `(3,1,1,0,0,0)`, `(3,2,1,0,0,0)`, `(3,3,1,0,0,0)`. Fix the sole additional key for each of H6,H7,H8,H9 to `K=(6,4,1,0,0,0)`. Within this explicitly defined family, allow **arbitrary finite legal ordered-word subsets in all four late windows**. Then:

```
           min E(H2,...,H9) = 127 = 39 + 88.
```

The previous EC49FBC 131-edge continuation therefore improves by four native edges without changing the H2–H5 baseline. This is the exact answer for this fixed-key family, not a bound on the unrestricted nine-window mother problem (previous author-side 80 <= E* <= 94).

## Exact candidate universe

As in EC49FBC, primitive step words are:
`a=(-1,-1); c=(1,2,-1,-2); d=(2,1,-2,-1); e=(3,1,1,-3); f=(1,-1); g=(2,-2)`.
The seventh operation `b=(-2,-2)` contributes a negative E2 step without any compensating positive E2 step and cannot occur in a target-endpoint path. Every signed primitive step is retained in order; no vector-sum equivalence identifies different prefix edges.

For each target-key word of length `h`, its operation counts obey
`#e=1, #a=0, #c+#d=9-h, #f=#g=h-5`.
Enumerate every c/d assignment and every distinct permutation of these operations. Apply the frozen 9-state observer and the signed X6 terminal condition. Exact retained word counts, for `h=6,7,8,9`, are respectively `240,1260,2240,560`. Observed signature histograms:
- H6: 1:80, 2:40, 4:80, 8:40.
- H7: 1:360, 2:270, 4:360, 8:270.
- H8: 1:560, 2:560, 4:560, 8:560.
- H9: 16:280, 32:280.

The EC49FAR exact rank-nine criterion on an OR of signature bits `m` is
`(m&18) != 0 && (m&20) != 0 && (m&33) != 0 && (m&40) != 0`.
For the above signature sets, it is equivalent to selecting **all four** signatures 1,2,4,8 independently at each of H6,H7,H8, and **both** 16 and 32 at H9. Thus a 14-bit mask exactly encodes all late rank requirements.

## Complete finite min-plus proof

Construct a rooted trie with one edge per native signed primitive step (not per macro-operation). Mark a trie edge `free` if it already occurs among the H2–H5 fixed prefixes. Insert every one of the 4,300 retained legal late word paths, tagging each terminal with its horizon/signature bit from the 14-bit coverage mask.

For each node `v`, compute `D_v[m]`: the minimum number of *nonfree* signed primitive edges in its subtree whose selected terminal words attain exact OR-mask `m`. Start from `{0:0}`, add the possible local terminal mask at cost zero, and combine each child `u` by
`D_new[m|n] = min(D_new[m|n], D_old[m] + D_u[n])`.
At a nonroot node, add one to every nonzero-mask state exactly when its incoming edge was not already a fixed early edge. A rooted-subtree induction proves that this exhausts every possible selected word subset and charges every selected primitive edge once. In particular, prefix overlaps across H6–H9 are counted exactly.

The unpruned pure-Python DP in `VERIFY_EC49FBD.py` has 26,705 native trie nodes and actually executes 425,376 min-plus pairs; it returns minimum **88 newly paid edges** at coverage mask `2^14-1=16383`. A separately implemented C++ DP using exact superset-dominance reductions returned the same 88, and a second literal-word audit checks its selected witnesses. Both were run locally. The Python program is self-contained and directly reconstructs its own candidate universe.

## Upper-bound witness (127 edges)

```
H2 de ec fe
H3 feg gef
H4 fegg gefg
H5 feggg gefgg
H6 ecgcfc fegccc fegddd gefddd
H7 ecgcffg fegccfg fegddgf gefddgf
H8 fegggffc fegggffd gefggffc gefggffd
H9 fegggffgf gefggffgf
```

The full literal-native audit recomputes every operation's signed primitive steps, every complete six-axis key, each endpoint displacement, observation signatures, rank-nine mask, and the unique ordered signed prefix union. Cumulative primitive edge counts at H2...H9 are exactly `22,31,35,39,85,97,121,127`, and the full nine-window witness uses five keys. This meets the exact DP lower bound.

## Provenance, limits, next question

Baseline: EC49FBC `954c3cac68a8d21a905e5aa8b89a5a56e9cc807f`; frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The current canonical control rules were read from global main `42c72244d7a26470aed0e2a96efc9ee3e09635e6` and Enterprise Math main `0ce66db2fed5b5e2135258ef904786ae84cd85e5` (2026-11-05), retaining the historical scientific pin. P000 and ACTIVE worldview remain unchanged.

This is an author-side exact finite computational proof, with a mathematically complete recurrence and executable full-enumeration verifier. Native Source CLAIM/Result and independent Driver admission are separate operations.

**Next EC49FBE:** optimize alternative legal fifth keys together with free H6–H9 choices while retaining this early witness; then compare the cost frontier with EC49FBB's 38-edge early structure and the known 94-edge unrestricted construction. A distinct path is to change H2/H3 or jointly reschedule early/late keys. State the cost/coverage of each precise family.
