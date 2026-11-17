# EC49FRX — 原生 BRC 双具名观察的四树精确价格相带

Date: 2026-11-18. Frozen scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Direct portable continuation of EC49FRW (PR #2663). Scientific status: **AUTHOR_PROVED / EXACT_FINITE_BELLMAN_AND_141_STATE_REPLAY / NOT_REVIEWED**. No formal TASK CLAIM, Result, Review or Foundation promotion.

## Model, statement and quantifiers

Use original BRC class 16943, with 310 source configurations, 141 *complete named-response states*, and exactly 228 distinct original physical named observers (144 terminal + 84 root). Keep response/provenance identity of every physical query. All 141 states have equal prior mass. The base price is `t>0`. Only physical observers 32 and 34 have discounted prices `p32=(1-a)t`, `p34=(1-b)t`; the other 226 prices remain `t`. Every allowed query remains strictly positive in the domain below.

For a legal complete adaptive native decision tree `Q`, let `U_Q` be total observer calls over all 141 state paths and `N32_Q,N34_Q` be the two original named-query usages. Thus `141 C_Q/t=U_Q-a N32_Q-b N34_Q`. Let `F(a,b)=141 V(a,b)/t` be the infimum over **all** legal complete native decision trees, not only the proposed witnesses.

**Theorem.** For all real `0<=a,b<=1/2` satisfying `min(a,b)<=1/3`, with `M=max(a,b), m=min(a,b)`,

```text
F(a,b) = 296 - 141*M - 11*m       (0 <= m <= 1/4),
F(a,b) = 297 - 141*M - 15*m       (1/4 <= m <= 1/3).
```

Both branches agree at `m=1/4`. On this entire L-shaped domain, exactly four fixed complete-tree **affine cost types** are sufficient and necessary to provide an optimal choice at every real parameter point:

| Native witness | (U,N32,N34) | Affine normalized total cost |
| --- | --- | --- |
| L32, previous EC49FRW | (296,141,11) | 296-141a-11b |
| L34, previous EC49FRW | (296,11,141) | 296-11a-141b |
| H32, newly constructed | (297,141,15) | 297-141a-15b |
| H34, newly constructed | (297,15,141) | 297-15a-141b |

All four full *physical-named* tree witnesses replay 141/141 original states with no repeated physical observation on a state path; worst depth is 3. The two new full witness trees are included in the complete local scientific evidence archive; no observer-response quotient is substituted.

## Exact finite anchors

Original immutable input hashes (SHA-256): `frozen_original_master.txt = cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`; `EC49FPG_PROFILE.csv = a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f`.

Nine unique full-state, all-228-observer, integer Bellman oracles give:

| (a,b) | F(a,b) |
| --- | --- |
| (0,0) | 296 |
| (1/2,0), (0,1/2) | 451/2 |
| (1/4,1/4) | 258 |
| (1/2,1/4), (1/4,1/2) | 891/4 |
| (1/3,1/3) | 245 |
| (1/2,1/3), (1/3,1/2) | 443/2 |

For each subset `S` of original states the exact recurrence is `D(S)=min_q (|S| c_q + sum_{A in Pi_q(S)} D(A))` with singleton value zero and `q` ranging over all 228 original named physical queries whose response partition strictly refines `S`. Costs `c_q` are rational parameters rescaled to integers. Since the prices are strictly positive, an optimal complete tree never needs an uninformative query. Every recursive call has a smaller nonempty state subset, so exhaustive memoized finite Bellman recursion computes the unrestricted native optimum. Two original raw response reconstructions agree on all 228 named vectors; the optimization recurrence is implemented once (these are **not** two independent solvers).

## Continuous-domain proof

Partition the L-shaped domain into four *closed convex trapezoids*, with the symmetric 34 regions obtained by exchanging `a,b`:

```text
D_L32 = {(a,b): 0<=b<=1/4, b<=a<=1/2}.
D_L34 = {(a,b): 0<=a<=1/4, a<=b<=1/2}.
D_H32 = {(a,b): 1/4<=b<=1/3, b<=a<=1/2}.
D_H34 = {(a,b): 1/4<=a<=1/3, a<=b<=1/2}.
```

Each complete tree contributes an affine cost function. The all-tree infimum `F` is concave in `(a,b)`. On each trapezoid, *one* of the four replayed witnesses achieves the exact Bellman value at all four vertices: `L32,L34,H32,H34` respectively, using the nine anchors above. If `x` is any convex combination of those vertices, concavity gives `F(x) >= sum(weight_i F(vertex_i)) = L_witness(x)`; the legal complete witness gives the reverse inequality `F(x)<=L_witness(x)`. Therefore equality holds throughout each trapezoid, for **every real pair** in the stated domain. The four trapezoids cover precisely `[0,1/2]^2 ∩ {min(a,b)<=1/3}`.

On four nonempty open regions the optimum is affine with the distinct gradients `(-141,-11), (-11,-141), (-141,-15), (-15,-141)`. A fixed complete tree has one affine cost gradient; if it attains the optimum across one of these open regions, its gradient must agree there. Therefore fewer than four fixed affine tree types cannot cover the domain. Four explicit complete witnesses prove sufficiency.

## Reproducibility and research frontier

Exact checker: `EC49FRX_PHASE_BELT_CERTIFIER.py` (same research-notes directory), using frozen raw reconstruction modules and all-228 dynamic programming from EC49FRW. It verifies nine distinct anchors, both original and both new complete native trees and exact source hashes. Original local run: `9/9 exact anchors PASS; 4/4 full witnesses PASS (141/141, max depth 3)`. A checked 13-item, self-contained evidence tar.xz (including all 11 MB uncompressed frozen raw inputs, source parsers, solver, witness JSON, complete proof and logs) was preserved as the conversation delivery artifact: `EC49FRX_NATIVE_BRC_PHASE_BELT_COMPLETE_EVIDENCE_20261118.tar.xz`, SHA256 `05f0efc29c8c35147e00084407da7481df17b46cf920bb6c5d93d4d082a70245`.

Unfinished region: `1/3 < a,b <= 1/2`. Multi-dimensional vertex separation was explored, but a large-rational vertex stalled computation; its partial output is not a complete diagram or a proof. Continue with bounded-denominator, scoped cell certificates, preserving all named native observations. Mathematical admission: `NOT_REVIEWED`. Formal Source `RS-EC49AS` task-directory read returned `NO_CANONICAL_PUBLICATION_DIRECTORY`, so this artifact is **independent portable research**, without asserting active owner or a new CLAIM.
