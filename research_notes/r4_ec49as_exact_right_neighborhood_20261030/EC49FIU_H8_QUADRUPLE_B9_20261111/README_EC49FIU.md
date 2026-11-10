# EC49FIU — four-H8-label lower bounds close another 52 radius-six B=9 backgrounds
Date: 2026-11-11. Author-side finite exact result; scientific source remains frozen at fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.

## Precisely proved result
For each of the original EC49FGJ seven-complete-key, 94-distinct-native-prefix BRC witnesses A and B, consider six observation-path replacement positions Q that include all four H8 signatures (8,1),(8,2),(8,4),(8,8), and whose other 18 unchanged paths have exactly 84 distinct signed, ordered native microstep prefixes. There are exactly **52 Q per witness**, split into four unique fixed native-prefix backgrounds F (13 Q per background).

Using the full 178,850-word nine-state legal BRC catalog and allowing **all 94 complete raw cache key types**, the exact minimum new signed native-prefix count to jointly satisfy the four H8 signatures over these four backgrounds is:
- A: 10, 9, 10, 9 (13 Q in each background).
- B: 9, 9, 10, 10 (13 Q in each background).

To reach 93 total prefixes with |F|=84 requires at most 9 new. In the two backgrounds per witness with minimum 10, the H8 four-label requirement alone forces total >=84+10=94, independent of any cache-key-count constraint. The original six paths complete all 24 demands at 94 and seven keys, so **26 exact 94-optimal Q per witness, 52 A/B-Q cases overall**, are newly proved.

The other two backgrounds per witness have four-H8 lower bound 9; they remain available to a stronger five/six-label or keyed bound.

## Proof and computation
Construct the exact rooted native-prefix trie of all legal H8 candidate words (counts 28063, 34777, 28063, 34777 across the four signatures, 623045 nodes). Charge each trie edge 0 if its full native signed prefix is already in F; otherwise charge 1. A legal choice of one complete H8 terminal per label has exact cost equal to the charged union of its rooted paths.

For a node v, d_v(S) is the minimum rooted subtree cost satisfying each label in S; combine one child u by

    D_new(S) = min_{T subset S} [D_old(S\T) + d_u(T) + c_u * 1[T nonempty]].

Induction on the rooted trie yields the exact minimum over all four legal words and all 94 key types. Four weighted backgrounds per witness are computed exhaustively; the original 94-prefix witness supplies a matching upper bound for the newly excluded 52 cases. Background sets and all 104 six-label Q lists are present in the structured report.

The actually executed portable Python verifier is VERIFY_EC49FIU.py. It reconstructs Q from any two non-H8 labels, checks |F|=84, validates 52 positions and four F backgrounds per profile, checks all original six-word 10-prefix upper bounds, evaluates the full four-demand trie and writes EXACT_REPORT_EC49FIU.json. A second independent local implementation of the trie algorithm, tracking attained terminal coverage masks instead of splitting requested-demand masks, returned the same minima [9,9,10,10] for both witnesses. The existing EC49FHD synthetic exhaustive-choice check was also executed.

Executed output:

    BRUTE_CROSSCHECK_PASS
    EC49FIU_PROFILE_PASS A H8_Q 52 new_94 26 minima [9, 9, 10, 10]
    EC49FIU_PROFILE_PASS B H8_Q 52 new_94 26 minima [9, 9, 10, 10]
    EC49FIU_EXACT_PASS 52 newly excluded six-label backgrounds

Inputs: already published EC49FGW_RADIUS5_EXACT_SCREENS_20261110/EC49FGW_RADIUS5_SCREEN.py, EC49FGJ_SEVEN_KEY_94_WITNESSES.json, and EC49FHD_PREFIX_TRIE_RADIUS5_20261110/VERIFY_EC49FHD.py on the EC49AS research PR. No new scientific or behavioral pin is substituted.

## Latest exact frontier
Following EC49FIS's 204 genuine alternative-key radius-six candidates/profile, EC49FIT eliminated 91/profile for B=7; EC49FIU eliminates another 26/profile for B=9. Remaining **87 per profile**: B9:38, B11:6, B15:32, B17:8, B18:2, B23:1. Some 26,681 forced-original-key joint-prefix subproblems per profile remain to be reconciled with independent author-side studies.

Next: investigate the two B9 4-H8 backgrounds per profile with lower bound 9 and the other 12 B9 Q not containing all four H8 labels, using a fifth label in the trie or an explicit full-key-state DP. Formal Result and independent Driver review remain pending, as the EC49AS publication is not current.
