# EC49FJP — two-key-release radius-six contexts B=20,21

Date: 2026-11-11. Status: AUTHOR_EXACT_FINITE / UNREVIEWED / NOT_ADMITTED. Frozen scientific input SHA: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

## Exact theorem and scope

Fix 18 of the 24 distinct labelled native-X6 signed-word BRC observation paths of either EC49FGJ witness A/B (seven full raw cache keys, 94 ordered/signed native prefixes), allowing six paths to change arbitrarily with at most seven complete raw cache keys in the final construction. Among all 134596 six-position selections for each witness, there are 8 positions at incremental budget B=20 and one at B=21 per witness where **two original keys are released**. The retained prefix set F has size 73 or 72 respectively. In each of these 18 cases, the exact minimum final native-prefix count is 94.

## Full-key pair-cover lemma

Enumerate the complete frozen nine-state BRC catalogue (178850 legal words, 94 complete raw key types). The retained paths have five raw keys, so a legal completion can add no more than two keys. Each of the 18 cases has precisely the uncovered labelled observations (window,signature)=(2,16) and (2,32). Exhaustive all-key cover over the 94 types shows the only possible unordered pair completing the two missing labels is the original released raw-key pair {(2,1,1),(3,0,1)}. Thus the complete seven-key set is uniquely forced in each case.

## Exact native-prefix dynamic program

Build the signed ordered X6 microstep trie of every legal replacement path under that forced key set. An edge costs zero if its exact signed prefix is in the retained fixed set F, otherwise one. For each node and six-bit label mask, a bottom-up dynamic program assigns six distinct required labels among the node terminal set and child subtrees, charging a shared prefix edge only once. This is the exhaustive exact minimum for the chosen six labels, using the same typed recurrence and C++ engine as EC49FJO.

At B=20, clipped optimal new-prefix cost is 21, and at B=21, 22. All 18 cases have no completion of added-prefix cost <= B, while the original six paths realize B+1. Hence each exact optimal cost is 94.

Executed generator MAKE_EC49FJP_INPUT.py: EC49FJP_PAIR_COVER_PASS, counts A/B each (B20=8, B21=1). Executed compiled EC49FJO_EXACT_TRIE.cpp from EC49FJO with this generator's case TSV: SOLVED 18. Each row shows one allowed full key set, zero feasible_93, and best_clipped=94-|F|. Source exact Git blob SHA: 2ad9420f9b0e3ca27bd5a80288725ac06cbce49a.

The complete original catalogue, case TSV, all 18 executed JSONL rows, run logs and SHA256 manifest are in archive EC49FJP_B20_B21_two_key_exact_18_evidence_20261111.tar.xz, SHA256 46e942061a9c63da78002425133f37647f327af3589a7ad0d524356899902a07. Reproduce with the unchanged frozen generator and witness from the referenced EC49FGW/FGJ inputs.

## Frontier

Together with EC49FJO, all 716 released-key B=20..22 contexts (A/B) are classified. Combined with EC49FJK (18 B=23 cases), this turn establishes 734 new finite local optimality instances. Next: other unreconciled B classes, larger radius and nonlocal seven-key existence. The global C_min(7) ?= 94 remains open; no formal Result or independent Driver acceptance is implied by this author-side draft.
