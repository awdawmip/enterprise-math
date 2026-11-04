# EC49FAP — H3/H4/H5/H6-rooted nine-window 94-edge optimum

Date: 2026-11-04. Evidence class: author-side finite theorem with actual integer computation and independent exact-rational checks; Driver admission pending.

## Immutable inputs and exact domain

Use frozen scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Source frontier: EC49FAO at `d032ffb7a4dfc88f5ef5746cb47e38449654d71a`. The four source schedules 1512, 1513, 2200 and 2203 fix all selected H2–H7 operation words. Each fixed schedule has 72 distinct ordered signed-six-axis primitive prefix edges, four complete positive BRC keys and six global observation signatures. Each horizon's nine-history observation matrix has rational rank nine.

**New candidate family:** H8 and H9 select operation words independently. Each word extends any previously selected word at **H3, H4, H5 or H6**, by an arbitrary ordered seven-operation suffix with zero signed-X6 net displacement. The H8/H9 roots may differ. All selected words retain native signed-X6 net displacement (2,0,0,0,0,0), exactly five complete BRC keys overall, at most six global observer signatures, and rank nine at every horizon over Q. Rooted subfamily selection is the *only* new restriction beyond the inherited frozen H9 model.

## Theorem

For each fixed H2–H7 source schedule 1512, 1513, 2200 and 2203, the exact minimum number of distinct nonempty signed-primitive prefixes in the above H3/H4/H5/H6-rooted family equals **94**.

## Exhaustiveness and lower bound

Enumerate all seven-letter suffix words at lengths 1 through 6 whose *signed six-axis* sum is exactly zero. Their counts are respectively **4, 18, 88, 454, 2,424 and 13,236**. For every existing selected H3–H6 root, append every suffix of the required length, then compute the full positive six-coordinate BRC key and original nine-start observer DFA signature. Filter only signatures outside the inherited six. Group complete surviving H8/H9 words by their exact full key.

Across the four schedules, the numbers of separately rank-nine capable H8/H9 key classes are 34/50 in every case. Zero of the four old key classes can furnish a rank-nine H8 or H9 word pool. Thus H8 and H9 must jointly use a *single new fifth key*. The rank-nine-capable intersection is exactly 22 new keys per schedule, i.e. **88 fixed-schedule/key cases** (not distinct keys across schedules).

Write P0 for the 72 primitive nonempty prefixes from H2–H7. For a new key K let W8(K), W9(K) denote all the eligible H8/H9 word pools and Pref(S) their ordered signed-primitive prefix sets. Define

```
d8(K) = min_{A subset W8(K), rank_Q(A)=9}
          |Pref(A) \ P0|

d9_plus(K) = min_{B subset W9(K), rank_Q(B)=9}
          |Pref(B) \ (P0 union Pref(W8(K)))|.
```

For any actual admissible H8 selection A and H9 selection B, H9 can only reuse prefixes selected into the actual trie. Giving H9 the *entire* W8(K) pool for free is an optimistic relaxation; consequently

```
E >= 72 + d8(K) + d9_plus(K).
```

The exact trie dynamic program assigns every node a six-bit OR mask of observation signatures served by its selected descendant leaves. A nonfree primitive trie node is charged one edge iff its subtree selects a nonempty mask. Independent child masks combine by bitwise OR and costs add. By induction on trie depth, this computes the minimum number of charged primitive prefixes for every mask. Enumerating all 64 masks and their nine-history matrix ranks selects the exact rank-nine masks. Row reduction modulo prime 1,000,003 is equivalent to rational rank nine here because every 9-by-9 subdeterminant of a 0/1 nine-row matrix obeys the Hadamard bound 3^9=19,683 < 1,000,003; each nonzero rational 9-by-9 determinant remains nonzero modulo the prime and vice versa.

The executed integer program checked every one of the 88 cases and obtained lower bound >=94, with exactly one class attaining 94 per fixed source schedule. In every attaining class d8=16 and d9_plus=6. The attaining fifth keys are respectively (5,5,1,0,0,0), (7,3,1,0,0,0), (5,5,1,0,0,0), (7,3,1,0,0,0). The inherited EC49FAJ explicit witness, with H8={pc,pd : p selected at H7}, H9={pfg : p selected at H7}, has 94 native edges, satisfies every observer/rank/key/net requirement, and belongs to the enlarged H3/H4/H5/H6-rooted family. Hence the lower bound is attained.

## Actual verification, reproducibility and scope

An independent, locally implemented Python exact-integer verifier executed on 2026-11-04 and produced the complete per-key JSON certificate (retained as local research evidence). The repository `VERIFY_EC49FAP.py` is a separately derived, reproducible extension of the existing EC49FAO verifier; this publication did not record a fresh local execution of that particular published source file. A separate `CROSSCHECK_EC49FAP.py` checked all 64 observation-mask ranks by exact Python Fraction arithmetic for each of the four schedules (256 comparisons), checked all four 94-edge upper-bound witnesses and independently counted 13,236 length-six zero-net six-axis suffixes by coordinate-vector state DP. Results agree. The attached compact `EXACT_REPORT_EC49FAP.json` records the executed counts and all 88 class bounds.

This is an exact result for the four stated fixed H2–H7 candidate families. The unrestricted H9 mother problem retains the author-side bound 80 <= E*_H9 <= 94; its global optimum is still open. Native CLAIM/Result and independent Driver acceptance require separate current authority.

## Next EC49FAQ

Choose one of (i) allow H8/H9 to branch from selected H2 words, or (ii) change the H2–H7 early schedule itself. Use the same frozen signed-X6 operations, complete cache keys, six-signature limitation and rational rank; seek a valid <=93-edge construction or an explicitly bounded impossibility certificate. As branching from H3 was verified, optimization of H2–H7 is an increasingly useful alternate route.

## Provenance

- Frozen input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
- Parent: `awdawmip/enterprise-math@d032ffb7a4dfc88f5ef5746cb47e38449654d71a`, EC49FAO.
- Source/verification: standalone exact-integer and Fraction programs published adjacent to this note.
- P000 and ACTIVE worldview unchanged.
