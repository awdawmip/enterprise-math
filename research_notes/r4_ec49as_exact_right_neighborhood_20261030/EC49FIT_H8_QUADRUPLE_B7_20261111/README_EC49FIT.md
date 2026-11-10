# EC49FIT — exact four-H8-demand lower bound in six-label BRC perturbations
Date: 2026-11-11. Author-side finite mathematical result; frozen scientific input fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Inputs and algorithms retain ordered signed native X6 microsteps, 9-state BRC transitions, and complete raw cache keys. Formal Result and independent Driver admission remain pending.

## Precise theorem
Consider EC49FGJ's two 24-label, seven-full-cache-key witnesses A and B, each with 94 distinct nonempty native signed X6 microstep prefixes. Fix any six replacement indices Q containing all four H8 signature demands (8,1),(8,2),(8,4),(8,8), plus two of the twenty other indices, such that the other 18 original words occupy exactly 86 distinct native prefixes. Exhaustive exact enumeration finds 91 such Q for A and 91 for B, exactly EC49FIS's previously unresolved B=7 alternative-key cases.

For each profile the 91 Q yield one identical fixed prefix set F, |F|=86. Over the full 178,850-word frozen legal catalog, permitting *all 94 complete raw keys*, the exact minimum added native prefix union required by those four H8 labels is 8. Every feasible six-label replacement therefore uses at least 86+8=94 native prefixes even if cache keys are unrestricted. Original six witness words provide a matching 94-cost completion with seven keys. Thus the 182 specific A/B-Q radius-six subproblems are exactly 94-optimal under the original <=7 complete raw key condition.

A fixed-prefix fingerprint (SHA256 of lexicographically sorted signed prefix bytes separated by newline) is A: 7b80e132bfdf1c77f0f7ff483ea70046d6ee74e0783b2f8100154d50225b9a5c; B: 537342a35711582459ac734443ca442c0a074183c1aa5e278d5d7d6c73200b4e.

## Complete computation and proof
The frozen legal catalog has H8 candidate counts (28063,34777,28063,34777) for signatures (1,2,4,8). Every candidate operation word is expanded to its exact ordered signed X6 microstep bytes. Insert all candidates in a rooted prefix trie with 623045 nodes including root. Terminal masks identify labels realized by complete legal words. Each rooted edge has cost 0 if its corresponding full native prefix is in F, else cost 1.

At trie node v, let d_v(S) denote the minimum cost of a connected rooted subtree below v satisfying every requested label in S, S a subset of the four H8 labels. For a child u connected by edge cost c_u, exact bottom-up merge is:

    D_new(S) = min over T subset S of
               [ D_old(S\T) + d_u(T) + c_u * 1[T nonempty] ].

Terminal demand masks can be satisfied at zero extra edge cost. Induction on trie height establishes this recurrence covers every feasible choice of complete legal terminals and counts each shared prefix once. In particular d_root(all four H8 labels)=8 in A and =8 in B. Because the trie uses every legal key, this is a key-unrestricted lower bound. The original profile gives an 8-new-prefix upper bound for each of the six-label backgrounds, completing the exact-optimum proof.

An independent local checker used a second trie dynamic program tracking attainable terminal masks by bitwise OR; both algorithms returned 8 on both backgrounds. A synthetic four-label Cartesian enumeration with multiple charged backgrounds agreed with both solvers. The portable verification script also invokes the older EC49FHD exhaustive toy-tree crosscheck.

## Reproduction
Execute VERIFY_EC49FIT_PORTABLE.py under Python 3 with previously published sibling sources:
- EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGW_RADIUS5_SCREEN.py and EC49FGJ_SEVEN_KEY_94_WITNESSES.json
- EC49FHD_PREFIX_TRIE_RADIUS5_20261110/VERIFY_EC49FHD.py

The script independently enumerates Q from all pairs of non-H8 labels, checks |F|=86 and equality of F over the 91 positions per profile, regenerates all BRC candidate words, evaluates exact native-prefix trie DP, and writes exact case lists/fingerprints to EXACT_REPORT_EC49FIT_PORTABLE.json. Verified run:

    BRUTE_CROSSCHECK_PASS
    EC49FIT_PASS A cases 91 min 8 fixed 86 trie 623045
    EC49FIT_PASS B cases 91 min 8 fixed 86 trie 623045
    EC49FIT_EXACT_PASS:182 key-unrestricted H8 quadruple exclusions

Historical dependency: EC49FGJ, EC49FHD, EC49FIR, EC49FIS at PR #1730. EC49FIS left 204 genuinely key-reallocatable six-label positions per profile after its budget-cover and B=3 closure. This result removes 91, leaving 113 per profile with budgets B9:64, B11:6, B15:32, B17:8, B18:2, B23:1. In parallel, a different set of 26681 mandatory-original-key, joint-prefix-unsettled six-label backgrounds per profile remains subject to cross-check against other author-side results.

Next exact unit: budget B=9 surviving 64 positions per profile (16 distinct fixed backgrounds): design key-sensitive five/six-demand trie DP or a discriminating smaller-group native-prefix bound. Preserve scientific pin; retain the original full-configuration <=7-key 93-prefix existence question.
