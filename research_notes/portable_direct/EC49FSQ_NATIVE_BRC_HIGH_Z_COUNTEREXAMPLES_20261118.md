# EC49FSQ-H — Native BRC high-z counterexamples to inherited tree menu

Date: 2026-11-18. Frozen science source fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Portable continuation of EC49FSQ PR #2715, EC49FSN PR #2706. Original 310 configurations, 141 distinct joint-response profiles, 228 physical named observations and uniform prior. No formal CLAIM/Result/Review/Activity authority claimed.

## Exact question

The EC49FSN full-interval certificate supplied original-native optimal decision-tree menus at a=1/2,b=7/16 for z up to 107/248. EC49FSQ saturation lifting propagated their optimality to all real 1/2<=a<=1 within that same z range. Does the old fixed tree menu remain optimal at a=1 when z exceeds 107/248? This is distinct from the continued existence of *some* saturated optimal tree.

Let F(a,b,z)=141V(a,b,z)/t; q32, q34, q140 cost respectively (1-a)t,(1-b)t,(1-z)t; every other named observation costs t>0. Fix a=1, b=7/16.

Direct old four saturated tree tuples (U,N32,N34,N140):
(306,141,41,4), (307,141,41,10), (309,141,41,16), (313,141,47,20).

Swapped old six saturated tree tuples:
(306,41,141,10), (303,32,141,17), (305,32,141,29), (304,28,141,32), (309,28,141,46), (311,28,141,51).

Tree cost is U-a*N32-b*N34-z*N140 in direct orientation, and U-b*N32-a*N34-z*N140 after swapping the q32/q34 prices.

## New exact unrestricted all-228 Bellman values

| z | Orientation | Old menu minimum | Exact unrestricted Bellman | Old menu excess | New optimal vector (U,N32,N34,N140) |
|---|---|---:|---:|---:|---|
| 1/2 | Direct | 2263/16 | 2259/16 | 1/4 | (313,141,43,24) |
| 1/2 | Swapped | 529/4 | 1049/8 | 9/8 | (311,10,141,69) |
| 3/4 | Direct | 2183/16 | 1057/8 | 69/16 | (334,141,62,45) |
| 3/4 | Swapped | 239/2 | 435/4 | 43/4 | (332,8,141,105) |
| 1 | Direct | 2103/16 | 463/4 | 251/16 | (348,141,44,72) |
| 1 | Swapped | 427/4 | 161/2 | 105/4 | (340,8,141,115) |

The primary exact rational dynamic program over the original all-228 named observation table recomputed all six values. Two new independent original 94-family decoder Bellman runs at z=1/2 reproduced 2259/16 (direct, 5480 reached subsets) and 1049/8 (swapped, 5075 reached subsets). Values and vectors are outputs of exact primary finite Bellman enumeration. One original-named q32-saturated full tree with the vector (313,141,43,24) has now been published in the same PR as EC49FSQ_FULL_NATIVE_SATURATED_TREE_A133_246_20261118.json and is optimal at z=1/2,a=1 by saturation lifting. Other new high-z trees' full JSON bytes remain to be published; the six comparisons here are exact-point results, not a new all-real high-z phase certificate.

## New general structural lemma: free observation saturation

Let a deterministic finite adaptive identification problem have nonnegative costs and a named observer q with price 0. Assume that testing q is a legal initial observation on the full profile set (e.g. q splits that set when the decision-tree syntax only admits splitting tests), and that a previously observed deterministic q outcome may be reused to remove any later repeat. Then **some globally optimal complete identification tree asks q exactly once along every input-profile path**.

Proof. Take any globally optimal complete decision tree. Prepend a q-root of cost zero. Within each outcome branch, execute the original tree. Whenever that original tree asks q again on the same path, replace the redundant test by the uniquely compatible outcome branch (the root has already fixed q). This creates a complete feasible tree with the same cost and exactly one q occurrence per input path. As the original tree was globally optimal, the constructed tree is optimal too. The proof requires neither uniform priors nor any BRC-specific response alphabet; the root-admissibility condition is essential for models that prohibit non-splitting tests.

Thus in native BRC16943, where q32 and q34 each have verified legitimate original-native splitting-root witnesses, at a=1 **for every z in [0,1]** the direct optimum has a q32-saturated witness and the exchanged optimum has a q34-saturated witness. The failure of the particular inherited ten-tree menu at the six high-z points is therefore a genuine *menu instability*, not a saturation obstruction. The earlier bound z<=107/248 belongs to the certified menu across the entire a∈[1/2,1] slab, and is not an upper saturation boundary at a=1.

## Reproduction / evidence level / continuation

Original frozen source primary solver: code/EC49FSA_THREE_OBSERVER_SOLVER.py, function solve(discounts,return_tree=False). The separately reconstructed 94-family/CSV decoder uses code/EC49FSA_FSB_INDEPENDENT_CHECK.py, function certify(discounts). At a=1,b=7/16, enumerate z=1/2,3/4,1; call both direct and swapped discount maps and compute old finite-menu minimum from the ten tuples above. All arithmetic is exact fractions. The local frozen-data runs and detailed results were recorded in EC49FSQ_HIGH_Z_PROBE.py, EC49FSQ_HIGH_Z_PROBE_CERT.json, EC49FSQ_HIGH_Z_RUNLOG.txt and EC49FSQ_HIGH_Z_INDEPENDENT.json; their complete six numeric rows and independent comparisons are reproduced above.

Status: AUTHOR_PROVED general zero-price lemma; EXACT_PRIMARY_FINITE_EXHAUSTIVE for six specified native-BRC points; INDEPENDENT_PARTIAL 2/2 selected points; NOT_REVIEWED. No claim of a high-z continuous phase formula; one q32-saturated full original tree is preserved in the companion EC49FSQ-T certificate, while the remaining new trees await lossless publication.

Next: determine the actual lower-a saturation boundary for z>107/248 and enumerate the new exact price-affine tree phases with complete preserved native named-response trees. Start with z=1/2, a near 1/2; then map real-valued phase transitions without conflating menu failure and saturation failure.
