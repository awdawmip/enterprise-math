# EC49FNB — exact BRC radius-three cases 17000–17999 (new 96-prefix witness)

Scientific input frozen to `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; 9-state BRC, 178,850 original lawful words, 94 complete cache keys, 24 observation labels, 38,169 seven-key radius-three configurations. Continuation of [EC49FNA, PR #2224](https://github.com/awdawmip/enterprise-math/pull/2224). Cost = number of distinct, **nonempty ordered signed native X6 microstep prefixes** shared by the selected lawful operation words.

## Exact finite result

All 1,000 configurations `17000 <= i <= 17999` were completely computed using the frozen C++ prefix-trie/label-subset integer optimizer. The finite-family minimum is **96**, attained uniquely at index **17965**; the maximum is **204**, attained at 17038, 17212, and 17423. There are 82 distinct observed costs. Cumulative contiguous coverage is now **18,000 / 38,169 = 47.16%**. The minimum of this radius-three subfamily improves from 98 to 96. The broader unrestricted seven-key mother problem retains its independent 84-prefix constructed upper bound.

The minimizer uses the seven complete-key indices `[0,4,5,6,11,14,26]`. Its explicitly reconstructed solution contains 24 original lawful BRC operation words, one for each observation label, and has **48 + 48 = 96** distinct nonempty prefixes distributed over first-microstep bytes 05 and 06 (root 07 unused). The complete words and all 1,000 exact costs are in the companion certificate.

## Exactness argument

For each first signed microstep root `r`, form the finite trie of every eligible frozen operation word. At an endpoint record its observation label. Bottom-up dynamic programming stores for each observed-label subset the minimum number of nonempty nodes in a selected union of subtrees; combining children unions their masks and adds their costs, and retaining a nonempty subtree charges its root. Taking supersets yields `f_r(S)`, the exact minimum for all labels in required set `S`. Finally exhaust all assignments of the 24 labels to eligible roots and minimize `sum_r f_r(S_r)`. Every legal selection induces one such assignment, establishing the lower bound; every optimal DP selection lifts back to eligible lawful words, giving a matching upper bound. The frozen native C++ optimizer therefore determines the exact finite costs. Independent Python trie/subset dynamic programming recomputed indices **17000 = 167**, **17965 = 96**, **17999 = 155**, agreeing with C++. A separate reconstruction verifies the 24-word minimizer gives exactly 96 prefixes.

## One-key substitution experiment

The prior 98-cost minimizer 16807 has `[0,1,4,5,11,14,26]` and splits as `49+49`. Replacing only key **1 with 6** produces configuration 17965, reducing the exact cost to `48+48=96`. Five selected lawful words change in each of the two active roots; each root retains 27 old prefixes, loses 22 and gains 21. This is a concrete two-unit improvement via a single cache-key substitution, providing a useful test case for sufficient conditions phrased in terms of the root cost functions `f_05` and `f_06`.

## Verification and provenance

Frozen full input SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Complete original 1,000-row C++ output SHA256: `a457f8c1f0535a4cba14ce67fb8f0afb084fb0c068993fb3503662dc5b35ddbb`. The companion JSON stores the complete lossless vector compressed using zlib/base85 and the full 24-word lawful witness; the Python validator checks all saved values, legal word membership and native-prefix union against the unchanged frozen catalogue. The source execution requested a wider window but stopped after exactly 1,000 complete rows, so indices starting at 18000 are not counted.

This is author-side **exact finite mathematical evidence**, with independent implementation spot-checks. Formal task publication/CLAIM/Result and Driver admission are separate. At the observed Source snapshot the `RS-EC49AS` canonical publication directory was absent; an additional native exact-task lookup remained QUEUED. No ownership is asserted by this report.

Next: resume from **18000**, with **20,169** configurations remaining, and test key-substitution rules using the 16807→17965 pair.
