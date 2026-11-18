# EC49FGM — two exact fixed-background obstructions at H8

Date: 2026-11-10 (Asia/Shanghai). Status: AUTHOR_EXACT_FINITE_THEOREM / REPRODUCED_LOCAL_EXHAUSTIVE_CHECK / UNREVIEWED / NOT_ADMITTED.

Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Preserve the original nine-state BRC DFA and ordered, signed native-X6 microsteps. Frozen code is the existing EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py (Git blob 7e97065ac9a0ff70435b92ee2f4bd718c9bf1859). The exhaustive 94 supported-key catalogue is the existing EC49FGK_SEVEN_KEY_COVER_TAXONOMY_20261110/EC49FGK_key_masks.txt (Git blob 21149331ef01890a05e4bc3531c9fe2a82814598). Original independently verified 24-word, seven-key, 94-prefix witnesses A and B are in EC49FGJ_SEVEN_KEY_94_20261110/WITNESSES_EC49FGJ.json.

## Precise finite theorem

For each of the two EC49FGJ witnesses W in {A,B}, hold its *twenty non-H8 operation words* fixed, each as a complete ordered signed-native path, and allow arbitrary legal replacement operation words for H8's four original BRC signatures (1,2,4,8), using any number of complete raw cache keys from the frozen model. Let F_W denote the union of nonempty signed native-six-axis microstep prefixes of those fixed twenty words. The union has exactly 86 distinct prefixes and uses six raw keys. Then

  min over legal H8 choices of | F_W union P(w_1) union P(w_2) union P(w_4) union P(w_8) | = 94.

There is no 93-prefix completion of *either* particular frozen 20-word background, even if the cache-key limit is removed. The corresponding previously published 94-prefix seven-key witnesses attain equality. Thus a 93-prefix seven-key construction, if any, must change at least one of the twenty non-H8 words of each of these two backgrounds. This statement is not a claim of global C_min(7)=94.

## Complete exact search and why pruning is exhaustive

For any operation word w, let P(w) be the set of all its nonempty ordered signed-X6 microstep prefixes. For fixed background F and threshold t, define D_F(w)=P(w) minus F. If four words can jointly add at most t new prefixes, every chosen word separately satisfies |D_F(w)| <= t. Similarly each pair's union of D_F sets has size <= t. These are exact necessary conditions with no approximation, therefore threshold filtering loses no potential <=t witness.

The verifier enumerates all 125,680 legal accepted H8 words from all 94 complete keys and the frozen observer. For each W it filters those with at most seven new prefixes, interns every remaining distinct signed ordered prefix, then forms all surviving signature (1,2) and (4,8) pairs with pair-union cost <=7. Every cross-pair union is finally tested using exact integer bitwise OR and bit_count; none has <=7. Therefore the total cost is >=86+8=94. The existing H8 words provide equality. Crucially, no key-budget assumption is imposed in this search.

Observed exact counts:

| Witness | F prefix count | Surviving candidates for sig 1,2,4,8 | Final cross-pair tests | <=93 completion? |
| --- | ---: | --- | ---: | --- |
| A | 86 | 33, 30, 32, 27 | 1296 | No |
| B | 86 | 30, 30, 34, 32 | 1188 | No |

The local script finished and reproduced the frozen model's 125,680 H8 candidates and every stated integer. Its machine-readable stdout is EXACT_AUDIT_H8.json.

## Independently checked local one-word neighborhood

A second, author-local exhaustive single-demand replacement run enumerated all 178,850 accepted words across the original 24 demand labels and re-evaluated the 94-prefix witnesses after one word replacement. For A and B separately the minimum cost remained 94 under unrestricted keys; among 9,838 substitutions retaining <=7 keys, the minimum also remained 94. This is an additional 1-exchange local stability observation, with separate local program and report; it is not relied on for the theorem above.

## Reproduction and next scientific unit

Run from the repository research-line checkout:
  python research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FGM_H8_FIXED20_20261110/VERIFY_EC49FGM_H8.py

Only the Python standard library and the three already published exact sibling source files are required. Signed microstep prefix identity uses the complete cumulative ordered signed sequence, not terminal displacement, support masks, or an endpoint quotient. All four observed signatures and existing P000/native-X6 scope are retained. The theorem is a frozen finite-model conclusion.

The immediate research next step is a joint redesign of at least one non-H8 word and the H8 block (e.g. H7+H8 coupling), while retaining exactly the original 24 demands and seven-key limit. Decide whether any such new construction has <=93 native prefixes, or build an all-seven-key >=94 certificate. Avoid re-running unchanged H8-only neighborhoods.

Author source contribution: EM-DIRECT-113F45 / TASK_RESEARCH; native RA-3840E6525D96650855C214F0 verified on canonical Source. Historical EC49AS did not have a current immutable publication when queried; no formal CLAIM, Result, or independent Driver admission is asserted.
