# Frozen R5: exact second optimal-budget reconfiguration via optimal-path automata

Date: 2026-11-14. Scientific input: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. This author-side result continues drafts #2302, #2307, #2312 and #2320. It concerns the original integer **event-boundary** abstraction, not the native 28-coordinate end-to-end workload. P000 remains unchanged.

## Mathematical statement

Let `X={x_0<...<x_(N-1)}` consist of distinct integers. A subset `S⊆X` of cardinality `K` is radius-2 feasible when every `x∈X` is within distance 2 of some center. Let `J(S)=Σ_{x∈X}min_{s∈S}|x-s|`, `J_2(K)=min_{|S|=K,feasible}J(S)` and `Opt(K)` be all feasible minimizers. Define `ρ_K=min_{S∈Opt(K),T∈Opt(K+1)}|S\T|`. The least symmetric difference is `2ρ_K+1`.

**New frozen R5 conclusion:** `J_2(214)=1064`, `J_2(215)=1059`, yet `ρ_214=2`. Moving between any optimal 214-center set and an optimal 215-center set requires deleting at least **two old centers**, adding at least **three new centers**, and has minimum symmetric difference **five**. Previously #2320 proved `ρ_213=3`; the next transition has a different exact reconfiguration size.

## General theorem: exact edit distance via the product of two optimal path DAGs

For any finite increasing integer coordinate set and fixed feasible budget, feasible increasing center sequences are paths in an acyclic graph. An edge between consecutive centers p<q exists if those two centers cover every intervening coordinate to radius 2. Start and finish edges cover leading and trailing coordinates. The exact interior edge cost is the sum of distances to the nearer endpoint. Since integer coordinates are distinct, a feasible edge satisfies q-p≤5 (distance in **indices**, not positions).

Min-plus dynamic programming finds the least cost for each center-count and ending vertex, retaining tied path counts. Start from globally cost-minimizing terminal states, and traverse backwards only predecessor edges attaining the exact prefix-cost equality. The resulting labeled finite DAG `A_K` recognizes **all and only** optimal increasing center sequences of length K; construct `A_(K+1)` analogously.

Form the asynchronous product of those two DAGs. It permits three moves: consume one equal center label in both paths (synchronized; zero edit count), consume a label in the K-path only (one deletion), or consume a label in the (K+1)-path only (one addition). At a state `(i,p,j,q,d,a)`, with i/j consumed centers, p/q current vertices and d/a unmatched old/new centers, the moves are:

```text
sync(c): (i,p,j,q,d,a) -> (i+1,c,j+1,c,d,a), c in next_K(i,p) ∩ next_(K+1)(j,q)
old(c):  (i,p,j,q,d,a) -> (i+1,c,j,q,d+1,a), c in next_K(i,p)
new(c):  (i,p,j,q,d,a) -> (i,p,j+1,c,d,a+1), c in next_(K+1)(j,q)
```

Search in increasing d, accepting only after consuming both complete paths with `a=d+1`. This gives **exactly ρ_K**, without enumerating the actual optimum-set family. Proof: every two optimal sorted center sets admit an alignment that synchronizes all common labels, with exactly `d=|S\T|`. Conversely each accepted product path yields two genuine optimal center sets, and no alignment can synchronize a label not in both. Thus the minimum accepted deletion count equals the minimum actual deleted centers. Every move increases the combined path length; bounded-product reachability is exact and terminates. This does not alone imply a uniform polynomial bound for all budgets without accounting for the product state size and arithmetic bit lengths.

## Exact frozen R5 allocation and reconfiguration proof

The frozen fifteen integer atoms reconstruct 953 distinct rational activation thresholds, 954 integer event boundaries and 1,065 activation events. Twenty-eight coordinate gaps of size 3 split the radius-2 covering problem into 29 independent blocks. Their minimum center budgets sum to 213; the corresponding optimum total costs sum to 1070.

The first additional center has a unique saving 6 in zero-based block 22. Seven zero-based blocks `4, 11, 14, 16, 19, 23, 28` have first-extra saving 5. An exact local minimum-cost enumeration of all ways to allocate two extra centers establishes that the saving 11 is achieved **only** with one extra in block 22 and one in one of those seven saving-5 blocks; other allocations save at most 10. Consequently, every global optimum at K=214 uses one extra in block 22, and every global optimum at K=215 uses the same allocation plus one extra in a saving-5 block.

For *each* of the seven saving-5 blocks, the optimal-path product accepts **no** old/new optimal pair with 0 or 1 deleted old center, and does accept one with 2 deletions and 3 additions. A direct integer nearest-center calculation verifies every produced witness's radius-2 feasibility and both optimum costs. For the largest block 28, containing 471 positions, the tied optimum counts are `144822240` at K=97 and `217233360` at K=98. This is a finite DAG-product search, **not an enumeration of the hundreds of millions of optimal sets**.

Every global K=214→215 pair must change one of the saving-5 blocks from its minimum-budget optimum to its next-budget optimum, so globally `ρ_214≥2`. A matching witness occurs in block 4. Relative to that block's left boundary:

```text
old optimum (K=3, cost 15): {2,7,11}
new optimum (K=4, cost 10): {1,4,8,11}
removed: {2,7}; added: {1,4,8}
```

Choose identical optimal centers in block 22 and identical minimum-budget optimal sets in every other block. This constructs global optimizers with two removals, proving `ρ_214≤2`. Together, `ρ_214=2` and `min|S△T|=5`.

## Verification scope and limits

The complete local standard-library Python implementation `VERIFY_R5_SECOND_RECONFIGURATION.py` uses exact integer and `fractions.Fraction` arithmetic. It reconstructs the pinned 15-atom input; computes 29 local center DAGs, costs, counts and first gains; constructs the exact budget-specific optimal languages; checks product reachability at deletion counts 0, 1 and 2 in the seven relevant blocks; and checks each returned witness by an independent direct nearest-center distance loop. As a separate finite crosscheck, it exhaustively enumerates every subset center choice on 465 small point sets of the declared family `X={0}∪Y, Y⊆{1,...,9}, 2≤|X|≤7`: **1,346** neighboring-budget comparisons match the exact product method. This finite test suite does not replace the general path-language proof.

The `EXACT_OUTPUT.json` is the numerical record. No floating-point computation, formal theorem checker, independent-author review, authenticated formal Task CLAIM, accepted Result or real 28-coordinate end-to-end timing is asserted. Exact provenance and the full runnable source are part of the same research bundle.

Next: extend the product of local optimal path DAGs to a blockwise pair-cost/intersection convolution for all R5 budgets. Determine the other 78 known forced-nonnested budget transitions and whether some gain-2/3 transitions are nonnested. Separately run the original 2,520-byte certificate / 28-coordinate / 8,192-query end-to-end experiment. Preserve the frozen science pin and its native source firewall.
