# EC49FGV — Seven-key BRC: exact radius-four exclusion around EC49FGJ A/B

Date: 2026-11-10. Research mode: independent TASK_RESEARCH author work; formal EC49AS CLAIM and independent Driver review are separate. Scientific input frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Baseline witness file: EC49FGJ `WITNESSES_EC49FGJ.json`, Git blob `e65c1598ad9fa2680558046ed1e59d83806536b8`, with two profiles A/B, 24 labeled original nine-state BRC demands, seven complete raw cache keys, and 94 nonempty ordered signed-X6 native microstep prefixes.

## Exact theorem (radius four)

Fix either EC49FGJ profile A or B. Choose any subset Q of **at most four** of its 24 demand-labeled words. Replace only those words by arbitrary legal operation words satisfying their exact labels, signed six-axis endpoint and original automaton constraints, while requiring **at most seven different complete raw cache keys** over the full 24-word replacement. Then the total native-prefix-union cost is at least 94.

Since the unmodified profile has cost exactly 94, the minimum over these radius-four neighborhoods is exactly 94. The word “radius” counts changed *labeled operation words*, not the number of operation letters or native steps.

This is a finite-author exhaustive search with explicit mathematical reductions. Its only independent prior local classification used for completeness is EC49FGS's 7-key forcing lemma for the 7,565 nonexceptional positions, and EC49FGM's unrestricted-key H8-only fixed-20 lower bound for the one exceptional position.

## Full finite domain and exact reduction

The 24 labels are (H2,H3,H5,H9) times signatures 16/32 and (H4,H6,H7,H8) times signatures 1/2/4/8. Legal operation alphabet, nine-state transition matrix, sink-8 rule, signature observer, native signed-X6 operator expansions, and final endpoint (2,0,0,0,0,0) are those of the frozen model. A complete raw key `(x,y,z)` counts positive signed native axes 1,2,3. The legal-key operation multiplicities are exactly:
```
a=z-1; b=x+y-h-1; f=h+1-y-2*z; g=h+1-x;
count(a,c,d,e,f,g)=(a,c,b-c,z,f,g), c=0..b.
```
Enumerate all permutations of these multiplicities, rejecting state-8 paths and observing the exact requested terminal signature. For each A/B seven-key allowlist, this yields **9,838** legal labeled words in total and a shared **42,734-node nonroot native-prefix trie**. Path-native prefixes are sequences of signed axis microsteps, not X6 endpoints.

For a chosen four-label set Q, let `F(Q)` be the union of the 20 unmodified paths' native-prefix sets, and set `B(Q)=93-|F(Q)|`. Any cost-93 or better solution must choose each replacement word `w` from the complete finite candidate catalog with `D_F(w)=P(w)\\F(Q)` and satisfy `|U_{i in Q} D_F(w_i)| <= B(Q)`.

The exact computation uses three sound lossless rejection stages:

1. **Singleton screen**: reject Q if any of its four labels has no candidate with `|D_F(w)|<=B(Q)`. A native-prefix-to-minimum-total-length index gives this screen without pairing all candidate words.
2. **Pair screen**: reject Q if some pair of selected labels has no pair of allowed candidate words with `|D_F(w_i) U D_F(w_j)|<=B(Q)`. A depth/budget-pruned signed-prefix trie enumerates *all* candidates within the exact budget, and uses exact set unions.
3. **Four-way screen**: for remaining Q, enumerate four-label set unions with subset-dominance pruning (if two words realize the same label and `D_1 ⊆ D_2`, it suffices to retain `D_1`), backtracking, admissible lookahead and exact repeated-state memoization. No threshold-feasible four-way union exists.

The one Q replacing all four H8 signatures can replace the seventh cache key. It is treated by EC49FGM's stronger exact fixed-20 H8 calculation, allowing **all legal cache keys**. That earlier check found no H8 completion within the seven additional-prefix budget. All other Q may use only the original seven keys under EC49FGS's exact forcing lemma.

## Complete case partition (per A/B)

| Disjoint rejection class | Profile A | Profile B |
| --- | ---: | ---: |
| Baseline 20 unchanged words already cost >=94 | 3,060 | 3,060 |
| Singleton necessary condition fails | 4,832 | 4,832 |
| Pair necessary condition fails | 2,273 | 2,275 |
| Pair succeeds; exhaustive four-way feasibility fails | 460 | 458 |
| H8-only key-release exception; EC49FGM | 1 | 1 |
| **All quadruples** | **10,626** | **10,626** |

The first three new numerical stages were computed using `radius4_singleton_screen.py` and `radius4_pair_trie.py`; the final four-way search used `radius4_quad_exact.py`. These actual executed checks were performed on the EC49FGJ witness JSON from the immutable blob above; pure Python integer/set arithmetic, no MIP or floating point. For A/B respectively, the final four-way DFS visited 4,095 / 4,092 nodes in total, with a maximum of 57 visited nodes in any remaining case; no satisfying four-way word choice was found. Every intermediate/terminal selected word was generated from the original pinned automaton and native signed-X6 expansion.

The case partition covers all `C(24,4)=10,626` four-label subsets. Any modification of one, two or three words can be embedded in a four-label subset by retaining the original word at the additional labeled positions, so the same result covers **at most four replacements**.

## Reproducible records, scope and next question

Existing verified immutable sources: `EC49FGJ_SEVEN_KEY_94_20261110/WITNESSES_EC49FGJ.json`; `EC49FGS_RADIUS4_SUPPORT_20261110/{README_EC49FGS.md,VERIFY_EC49FGS.py,EXACT_AUDIT_EC49FGS.json}`; EC49FGM H8 complete-enumeration certificate. New exact evidence files and run logs accompany this note, and the separately packaged executed Python scripts are provided in the author handoff.

The theorem proves the *radius-four neighborhood* optimum around the two specific 94-edge witnesses. The whole seven-key model still has the constructive upper bound `C_min(7)<=94`; global optimality remains an open task. Any seven-key cost-93 construction must be at distance **at least five labeled words** from both A and B. The next independently discriminating problem is five-word coordinated replacement: compute the frozen baseline support-hypergraph `B(Q)=93-|F(Q)|` for `|Q|=5`, then test early low-budget necessary conditions and all legitimate key-release classes before expensive five-way search.

No P000/ACTIVE worldview changes, Working Truth promotion, formal Result, or independent Driver admission are asserted by this author note.
