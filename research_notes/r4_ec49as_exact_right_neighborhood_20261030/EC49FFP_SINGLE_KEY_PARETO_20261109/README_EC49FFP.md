# EC49FFP — Exact one-key Pareto frontier for adjacent BRC low-observation windows

Date: 2026-11-09. Status: AUTHOR_EXACT_FINITE_RESULT; independent Driver mathematical review and native Result pending. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Signed native X6 primitive operation/DFA model from EC49FFJ, Git blob `6350340fbe869f17b5a50bd1ba30640db44a3a99`. P000 and ACTIVE worldview unchanged.

## Theorem and domain

Take two adjacent observation horizons `h,h+1`. At **each** horizon require four words with nine-state signatures `1,2,4,8`. All eight words must share **one identical complete BRC key** `K=(x,y,z)`. Each word must obey the original six operation types and prescribed count equations. Cost `C_native` is the number of distinct nonempty **ordered signed X6 microstep** prefixes among the eight words.

The exact global one-key minima are:

| Horizons | Common complete-key candidates | Exact global minimum | All minimizing keys |
| --- | ---: | ---: | --- |
| H3,H4 | 1 | **56** | (4,2,1) |
| H4,H5 | 3 | **62** | (4,3,1), (5,2,1) |
| H5,H6 | 7 | **60** | (5,3,1) |

Thus **the one-key optimum decreases when both horizons move from H4/H5 to H5/H6**, `62>60`. This is a complete finite result, not a claim of eventual monotonicity for arbitrary horizons.

EC49FFO already established unrestricted-key optima `40` for H4/H5 and `44` for H5/H6. Hence exact one-key premiums are **22** and **16** native edges; using a second key can be materially more valuable than a shorter isolated key.

## Full finite lower-certificate method

For horizon `h` and full key `(x,y,z)`, the original admissible word counts are:

`#a=z-1; #e=z; #c+#d=x+y-h-1; #f=h+1-y-2z; #g=h+1-x`.

The nonnegative integer constraints are `1<=z<=floor((h+1)/2)`, `2z<=x<=h+1`, `0<=y<=h+1-2z` and `x+y>=h+2`. Intersect the domains for adjacent horizons. This leaves exactly the following full-key inventories and optimal signed-prefix costs:

- H3/H4: (4,2,1):56.
- H4/H5: (4,3,1):62; (5,2,1):62; (5,3,1):72.
- H5/H6: (4,4,1):68; (5,3,1):60; (5,4,1):78; (6,2,1):68; (6,2,2):74; (6,3,1):78; (6,4,1):88.

For every inventory, split `#c+#d` in all possible ways, enumerate every operation permutation, and run the original 9-state DFA. Retain exactly signatures `1,2,4,8`, expand each candidate to the **ordered signed six-axis microsteps**, and merge its nonempty prefixes into one rooted trie. Directly verify each candidate's complete key, word counts, signed endpoint `(2,0,0,0,0,0)` and length `2(x+y+z-1)`.

Each terminal node carries the subset of eight required `(h,signature)` labels it realizes. For node `v` and subset `S`, let `D_v(S)` be the fewest edges below `v` required to realize exactly `S`; initialize every subset of labels realized at `v` to cost zero. For each child `u`, combine disjoint sets `A,B` by

`D_new(A union B) = min(D_old(A)+D_u(B)+[B != empty])`.

All eight demands can be assigned to selected terminals without duplicate demand ownership; conversely every DP assignment yields legal witness terminals. Induction over trie nodes establishes exact optimality. The root's full-eight-label state certifies each number in the table. The separately reconstructed witness sets have their native signed-prefix unions counted again independently.

The connected GitHub file `VERIFY_EC49FFP_COMPACT.py` reproduces all **11** key-specific integer minima without external optimization dependencies; its `EXPECTED` values are assertions, not the algorithm's inputs. Separate author-side independent binary prefix-closure MILP certificates also matched all H3/H4 and H4/H5 cases and the H5/H6 minimizer: integer objective and exact dual bound `56,62,62,72,60`, `status=0`, zero MIP gap. SciPy/HiGHS floating dual reports differ below 1e-12 from those integers.

## Explicit upper witnesses

Each block lists the four words at its horizon in signature order **1,2,4,8**.

- H3/H4, K=(4,2,1): H3 `ded,edd,cec,ecc`; H4 `degf,edgf,cefg,ecfg`. Signed prefix union **56**.
- H4/H5, K=(4,3,1): H4 `gedd,edgd,cegc,gecc`; H5 `gedgf,edggf,cegfg,gecfg`. Signed prefix union **62**.
- H5/H6, K=(5,3,1): H5 `gefdd,fgedd,fgecc,gefcc`; H6 `gefdgf,fgedgf,fgecfg,gefcfg`. Signed prefix union **60**.

## Scientific contribution and continuation

The new exact **key-budget versus native-prefix cost Pareto points** distinguish minimal number of keys, word length and true shared prefix cost. Previous cross-window unlimited-key optima alone could not answer the one-key case.

Next investigate the mother's exact H2/H3 plus later-high signature quotas using a **five-key-aware** prefix cover algorithm, with exact current owner/claim authority checked before any formal Task mutation. The EC49FFO 70-edge alternative-demand witness is kept distinct from the mother's original demands. A second local question is the one-key Pareto series for longer adjacent windows and chains; the nonmonotone behavior is now established for one specific adjacent pair shift.

Source work is authored and unreviewed; GitHub storage is not formal CLAIM, Source-native Result or mathematical admission.
