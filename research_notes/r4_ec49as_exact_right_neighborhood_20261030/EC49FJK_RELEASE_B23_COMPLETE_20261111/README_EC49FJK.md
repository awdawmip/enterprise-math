# EC49FJK — Released-key radius-six B=23: exact 94-edge local minimum

Date: 2026-11-11. Status: AUTHOR_EXACT_FINITE / UNREVIEWED / NOT_ADMITTED.
Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Inputs: EC49FGJ witness A/B and EC49FGW nine-state native BRC complete legal word generator.

## Finite theorem

For each of the A/B seven-key, 94-native-prefix witnesses, choose six of the 24 *distinct labelled* BRC requirements for replacement, hold the other 18 original words fixed, and allow arbitrary legal replacement words with at most seven distinct **complete** raw cache keys. Denote the retained signed ordered native-X6 prefix set by F(Q). For every Q with |F(Q)|=70 and fewer than seven retained keys, the exact total native-prefix minimum is 94.

Exhaustive inspection of all binomial(24,6)=134596 Q per witness finds nine matching Q in A and nine in B. The 93-edge target permits only 23 new prefixes, while the original witnesses supply exactly 24 new prefixes.

## Complete seventh-key enumeration

The retained paths use exactly six complete raw keys in each of the 18 cases. Let Cov(k) denote the set of observation labels realized by any legal word of full raw key k in the complete 178850-word catalogue. Let M be the replaced labels not covered by the six retained keys. A seven-key completion must lie in a superset K_F union {k}, with k not in K_F and M subset Cov(k). There are 94 possible catalogue keys. Sixteen cases allow only the released original key. In the two other cases, Q=(18,19,20,21,22,23), 88 possible seventh keys require testing. This supersets all completions using only the six fixed keys as well.

## Exact signed-prefix trie optimization

For each allowed K_F union {k}, insert *all* legal words for each of the six labels into a signed ordered native-six-axis microstep prefix trie. Every incoming edge p has c(p)=0 if the prefix is already in F, otherwise c(p)=1. At node v let d_v(S) be the least cost of satisfying a subset S of six labels using paths in the rooted subtree, excluding the entering edge. All terminal submasks have cost zero; for each child u and disjoint label allocation T, update d_new(S union T)=min(d_old(S)+d_u(T)+c(u)[T nonempty]). Exhaustive label partitioning is exact: each valid solution is a set of root-to-terminal paths, each native prefix is charged once. Clipping at 24 distinguishes all potential costs <=23 from their absence.

Every one of the 18 cases has clipped minimum 24 (and its original six-word witness attains exactly 24). In total 192 distinct seven-key trie problems were solved: 16 forced cases and 88 choices for each of two flexible cases.

## Actual executed checks and scope

The full nine-state legal catalogue contains 178850 words and 94 complete raw keys. Exact Python sparse-mask DP printed `EC49FJK_ALL_18_PASS`. Separately compiled C++ full-64-mask array DP printed `SOLVED 18`; all rows yielded `best_clipped=24` and `feasible_93=0` using the same frozen data but a distinct implementation. The case ledger and reproducible Python source are in this directory. The independent C++ implementation, 192-key input case table, complete catalogue, runtime log, frozen inputs and SHA256 manifest are included in the attached author-side evidence archive.

A supplementary threshold-26 run of the two flexible cases found two seventh keys with cost 24, (6,5,1) and (7,4,1), and 86 other allowed keys each with cost at least 26. This supplementary classification is independent of the proof at threshold 24.

Reproduce: copy the frozen `EC49FGW_RADIUS5_SCREEN.py` and `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` beside `VERIFY_EC49FJK.py`; run `python VERIFY_EC49FJK.py`. The generator verifies the complete witnesses and the [2,0,0,0,0,0] signed native displacement. All claims are author-side finite mathematical evidence; independent Driver review and formal Result remain pending.

Next: resolve still-open released-key budget classes B=10,12,13,14,16,19–22 and then enlarge the number of replaced paths while retaining the seven-key global target C_min(7) ?= 94.
