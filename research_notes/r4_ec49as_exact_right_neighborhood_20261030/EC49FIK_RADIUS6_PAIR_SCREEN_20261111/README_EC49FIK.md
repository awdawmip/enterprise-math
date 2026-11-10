# EC49FIK — Exact two-demand native-prefix exclusion, six-path BRC neighborhood (2026-11-11)

## Question and frozen inputs

Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The original 24 BRC observation labels, nine-state observer, fully ordered signed-native-X6 microsteps, original seven raw complete cache keys for A/B, and 94-prefix witnesses are unchanged. EC49FHH established each known 94-prefix witness is optimal within radius <=5 under at most seven complete keys; EC49FIJ excluded 92,611 of 134,596 radius-six nominated positions per witness.

This result checks **six nominated replacements Q excluding the two H2 labels, where the other 18 witness words still use all original seven complete keys**. A new replacement word therefore must use one of those seven keys to satisfy #keys<=7.

## Exact pairwise necessary condition

Write F(Q) for the union of the unchanged 18 witness paths' **native ordered signed nonempty prefix sets**. The maximum additional-prefix budget for a total <=93 is B(Q)=93-|F(Q)|. For a legal candidate word w meeting label j and one of the seven keys, put D_Q(w)=P(w)\F(Q). A feasible six-word completion necessarily supplies, for every two distinct j,k in Q, a pair u,v with |D_Q(u) union D_Q(v)| <= B(Q). Thus, if any two labels have minimum union cost exceeding B, **all six-way completions at that nominated replacement position are impossible**.

The finite catalog has 178,850 total legal words, 9,838 words with these original seven keys. Full raw keys, labels, path order, signs and distinct prefix identity are retained. The exact integer-bitset procedure enumerates all candidates at each label, filters only candidates with |D|<=B, then forms all pair unions of the remaining candidate sets. Subset domination is sound: if X subset Y, then X union Z subset Y union Z for every Z, so retaining only inclusion-minimal D sets preserves pairwise feasibility. All tests use exact integers.

## Exhaustive finished budgets

| Profile | B | Q positions in this class | Singleton rejects | Singleton survivors | New pairwise rejects | Pairwise survivors |
|---|---:|---:|---:|---:|---:|---:|
| A | 3 | 9,344 | 3,740 | 5,604 | 5,604 | 0 |
| A | 5 | 4,400 | 0 | 4,400 | 3,300 | 1,100 |
| A | 7 | 6,582 | 5,412 | 1,170 | 390 | 780 |
| A | 9 | 8,700 | 0 | 8,700 | 8,568 | 132 |
| B | 3 | 9,344 | 3,740 | 5,604 | 5,604 | 0 |
| B | 5 | 4,400 | 0 | 4,400 | 3,300 | 1,100 |
| B | 7 | 6,582 | 5,412 | 1,170 | 390 | 780 |

These are disjoint additional eliminations relative to EC49FIJ's exact singleton screen. New exclusions: A=17,862; B=9,294. New six-path unresolved position counts are A=24,123 (22,111 fixed-seven-key and 2,012 released-key), B=32,691 (30,679 fixed-seven-key and 2,012 released-key).

## Scope, reproducibility and next question

Executable, self-checking reproducer: `VERIFY_EC49FIK.py`; invocation: `python VERIFY_EC49FIK.py --profile A --budget 9`, or `--profile B --budget 7`. Each invocation checks the exact tuple against `EXPECTED` and returns `EC49FIK_EXACT_PAIR_PASS`. The older complete legal catalog and A/B witnesses are imported from sibling `EC49FGW_RADIUS5_EXACT_SCREENS_20261110`. The structured exact case report `EXACT_REPORT_EC49FIK.json` records completed combinations and the original local execution status; scripts use an immutable science input. A/B budget 3/5 and A budget 7/9 were already independently run as separate focused full enumerations; current exact verifier reruns included A budgets 3/5/7/9 and B budget 7. B budget 3/5 have also previously completed on a focused verifier. No assertion is made for the still-running/unverified **B budget 9** class.

This finite negative result is an additional local witness-neighborhood certificate, not a seven-key global bound. Next apply higher-budget pair screening (B9 B, B11+) with pair-priority ordering and six-terminal native-prefix trie dynamic programming to the exact survivors, and solve released-key allocation with complete raw-key enumeration. Formal Result and independent Driver review remain separate.
