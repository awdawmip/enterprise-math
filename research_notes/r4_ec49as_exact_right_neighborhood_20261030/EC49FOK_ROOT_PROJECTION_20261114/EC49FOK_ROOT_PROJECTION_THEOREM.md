# EC49FOK — Legal-root projection theorem and invisible BRC root-table perturbations

Date: 2026-11-14. Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Parent: EC49FOJ PR #2390 (all-budget terminal filtration) and EC49FOI PR #2385. Status: exact finite author verification; NOT_REVIEWED.

## Exact general theorem

Let L be a finite set of named demands, R a finite set of named roots, and E(l) a nonempty set of legal roots for each l in L. Root choice is independent across labels. For each root r, define:

M_r = {l in L: E(l) = {r}} (mandatory labels).
O_r = {l in L: r is in E(l), and |E(l)| >= 2} (optional labels).

Let A be the set of all complete, legal named-root assignments, and let S_r(rho) be the set of labels assigned to root r by rho.

**Projection lemma (exact equality):**

P_r := {S_r(rho): rho in A} = {M_r union T: T subseteq O_r}.

Proof: A legal complete assignment must send every mandatory label to r, may send any optional label to r, and cannot send any other label to r. Conversely, fix any subset T of O_r; send exactly the M_r union T labels to r. Every omitted optional label has an alternative legal root distinct from r, and every label not legal at r has some legal root by hypothesis. These choices can be made simultaneously because the root choices are independent across labels. QED.

Now consider configurations K and K' with the **same** E(l) for every label, but possibly different exact root cover-cost functions D_r^K and D_r^K'. Suppose

D_r^K(M_r union T) = D_r^K'(M_r union T) for every r and every T subseteq O_r.

**Terminal observer invariance theorem.** The complete legal assignment-cost maps agree identically, including named-root assignment identity and exact integer cost. Consequently, the exact cost-labelled terminal observer F_b is identical at EVERY budget b, irrespective of the respective native DFS visit orders.

Proof: Every S_r(rho) is in P_r by the projection lemma, so the premise preserves each summand in the total exact cost C_K(rho) = sum_r D_r^K(S_r(rho)). The common legal assignment domain is unchanged. Hence C_K = C_K' on all complete assignments and their budget restrictions coincide. QED.

The test needs only sum_r 2^|O_r| root cost comparisons for a pair of configurations, rather than enumerating the product of |E(l)| over all labels. Rooted tables may differ on subsets outside the legal projections without affecting ANY complete assignment cost. This is a sufficient general test, not a universal necessary condition: simultaneous nonzero component perturbations can in principle cancel in the sum.

This implementation reuses the existing exact native signed-prefix rooted trie DP to obtain the root costs. It reduces which entries must be compared and avoids full assignment and DFS enumeration; local incremental recomputation of changed key paths remains future work.

## Frozen 84-edge exact census

Native input: master_and_radius3_cases.txt, SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e, under the original frozen science. Oriented edges: FIRST_NEUTRAL_EDGES_EC49FNS.txt, SHA256 db8d3b9232f4ff31ffd2bf7ed81237625ecb6491f7883f4b03263728d6ecdc41. The immutable FOJ parent file FOJ_EDGE_FIRST_SEPARATION_84.csv (blob 8f081749d47c318239bc37f4384a9794b1452cea) supplies the independent exact complete-assignment comparison for all 84 edges.

Of 84 neutral edges, **82 have the same legal-root domains**, and two ending in configuration 32279 change the legal-root domains. Among the 82 stable-domain edges, the projection test certifies **32 all-budget equalities** and finds visible root-cost differences on **50**. The 32/50 split coincides exactly with FOJ's independently computed infinite/finite first-separation classification on this finite family; the converse is an empirical fact of this census, not a general mathematical necessity. The two domain-changing edges require the separate FOJ full-cost witnesses and are not treated as passing the shared-domain theorem.

The native C++17 program computes 13,776 projected root-cost comparisons across all 82 stable-domain edges using 168 distinct cached root profiles across 51 configurations, with zero mismatch against all 82 independent FOJ first-separation statuses.

Two hidden-profile cases are structurally informative:

| Exchange | Full-root-table differing entries | Differences among reachable root masks | Number of independently checked full assignments |
|---|---:|---:|---:|
| 32315 -> 32308 | 443 | 0 | 648 |
| 32315 -> 32324 | 10 | 0 | 648 |

For 32315 -> 32308, raw root 05/06/07 tables differ in 202/237/4 entries respectively; for 32315 -> 32324, root 05 differs in 10 entries. In both exchanges, ALL changed entries are rooted masks outside the exact projection of complete legal assignments. Each has exactly (16,8,16,128) legal projection masks at roots (03,05,06,07), only 168 comparisons. In the 32315 -> 32324 edge, the native ordered DFS trace changes even though complete assignment costs agree at every budget.

## Verification

The included VERIFY_EC49FOK.cpp reconstructs the original signed-prefix tries and integer cover DP. It derives M_r and O_r from the legal root domains, evaluates exactly the 2^|O_r| reachable rooted masks, and asserts the 32/50/2 exact census against the independent FOJ file. g++ -std=c++17 -O2 and -O3 produced byte-identical 84-row CSV results.

A separately written Python reconstruction of the trie and DP checked both hidden-profile edges, every projected mask and the complete set of 648 legal assignment costs for each comparison, with exact integer arithmetic. Both pass.

The result assumes independent legal choices per demand. Any future constraint coupling root choices across different demand labels changes the projection formula. The rooted table and complete terminal observers are different observation levels: for a future operation requiring unused rooted subsets, raw prefix paths, signed branches or provenance, this quotient must be re-evaluated.

## Next precise mathematical problem

Construct a cache-key-local algorithm computing only the affected D_r(M_r union T) values, reusing unaffected signed-prefix subtrees and DP states rather than regenerating full rooted tables. Test cost and memory against the 168-signature baseline. Separately, characterize genuinely cancelling projected cost perturbations across roots to refine this sufficient criterion to a complete invariant.

Original R4 provenance: Researcher-ID EM-DIRECT-204C14; Activity RA-6893088D0A7347CE7F4D8720. The exact topic RS-EC49AS has no canonical publication directory on the last verified control read. This source preservation creates no formal CLAIM, Result or independent scientific acceptance.
