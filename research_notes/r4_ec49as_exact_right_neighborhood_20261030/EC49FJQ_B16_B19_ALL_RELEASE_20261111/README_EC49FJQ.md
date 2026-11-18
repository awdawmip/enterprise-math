# EC49FJQ — all released-key radius-six B=16–19 contexts: exact minimum 94

Date: 2026-11-11. Status: AUTHOR_EXACT_FINITE / UNREVIEWED / NOT_ADMITTED.
Frozen input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab, unchanged EC49FGW nine-state signed X6 native generator and EC49FGJ A/B 94-prefix seven-full-key witnesses. All counts refer to distinct labelled BRC demand paths and **signed ordered** native six-axis microstep prefixes.

## Finite theorem

For either fixed A/B witness with 24 labelled requirements, replace arbitrary six witness paths and retain the other 18 original paths. Let F be the fixed 18-path signed-prefix union and K_F the full raw key set of those fixed paths. Among the C(24,6)=134596 subsets per witness, consider exactly those releasing one or two original keys and with B=93-|F| in {16,17,18,19}. For **all** these fixed-background subproblems, allowing any legal replacement words using <=7 complete raw keys, the exact minimum final distinct native-prefix cost is 94.

| B=93-|F| | |F| | A | B | Both | Minimum added native prefixes |
|---:|---:|---:|---:|---:|---:|---:|
| 16 | 77 | 64 | 64 | 128 | 17 |
| 17 | 76 | 936 | 936 | 1872 | 18 |
| 18 | 75 | 418 | 418 | 836 | 19 |
| 19 | 74 | 308 | 308 | 616 | 20 |
| Total | | 1726 | 1726 | 3452 | |

3232 cases release one key; 220 cases release two. The original witnesses realize exactly B+1 new prefixes and establish 94 as a matching upper bound.

## Exhaustive cache-key enumeration

The frozen source generates 178850 legal nine-state operation words, occupying 94 complete raw key triples. For each original fixed K_F and six replacement labels R, let M be the labels in R not covered by any key in K_F. If r=7-|K_F| is one or two, every legal <=7-key completion has full keys contained in K_F union L for some outside-key subset L of size r, necessarily M contained in the union of complete-key coverage sets Cov(k) over L. The executable generator enumerates all outside-fixed keys and **all** r-subsets passing this cover condition; it does not omit a key that might help prefix sharing merely because it is unnecessary for the missing-label cover.

Actual enumeration yields 5192 admissible seven-key superset alternatives across 3452 backgrounds. Key-choice distribution: 16 instances at B17 and 4 at B18 each have 88 alternatives; the other 3432 backgrounds have a single alternative. Consequently, optimizing each alternative fully is exhaustive for the allowed <=7-key replacements.

## Exact six-label signed-prefix tree

For each admissible full-key set, insert every legal replacement word under that exact set into a rooted trie of signed and ordered X6 microsteps. Assign edge weight c(p)=0 when the corresponding full signed prefix belongs to F and c(p)=1 otherwise. A bottom-up 64-mask DP computes d_v(S), the minimum number of newly purchased edges needed to realize a subset S of the six distinct labels in the subtree of v, excluding its entering edge. Terminal masks cost zero; for disjoint S,T and child u:

    d_new(S union T) = min { d_old(S) + d_u(T) + c(u) [T != empty] }.

Every feasible six-word completion corresponds to six root-to-terminal paths and a partition of their labelled demands among children, so every shared native prefix is charged exactly once. Costs are clipped at B+1 to prove absence of completions using <=B extra prefixes.

The actually executed Python generator returned EC49FJQ_INPUT_PASS 3452 KEYSET_TRIES 5192. The independently compiled C++ 64-mask DP returned SOLVED 3452. All 3452 case rows have feasible_93=0 and best_clipped=B+1; there are no candidate replacement solutions using <=93 native prefixes. Outcome counts by best_clipped: 17=128, 18=1872, 19=836, 20=616. This is a complete finite exact local theorem under the frozen scientific inputs; independent Driver mathematical review remains pending.

## Code, evidence and provenance

This directory holds the **exact bytes of both executed programs**: MAKE_EC49FJQ_INPUT.py (Git blob 444b88db63a9b4bc63a49b961c9446b6ba4bc6d4) and EC49FJQ_EXACT_TRIE.cpp (Git blob 7ecd21a12f80d8ad5924a57216718141b8ab324a), plus a compact numerical report. Reproduce beside frozen EC49FGW_RADIUS5_SCREEN.py and EC49FGJ_SEVEN_KEY_94_WITNESSES.json by running:

    python MAKE_EC49FJQ_INPUT.py
    g++ -std=c++17 -O2 EC49FJQ_EXACT_TRIE.cpp -o exact
    ./exact EC49FJQ_CATALOG.tsv EC49FJQ_CASES.tsv result.jsonl

Full catalogue SHA256: b4e7bcc88306fa846f752f1ca1e6b31957e9ac65080d80a0c7506447004dc489.
All-case input SHA256: ea501ac0b2debf95eab39eac66eb4d1af65263d6ab587bdb1d90b03119f636d9.
Actual 3452-row output SHA256: 8014d17a064aff76c77169c1706604f9ac253383993e39520ee97d227cfbbd1f.
Complete user-facing evidence package (original catalogue, full case TSV, every result row, logs and executable frozen inputs) is EC49FJQ_B16_B19_3452_exact_evidence_20261111.tar.xz, SHA256 74559db10b74b372b93dac48f5b268041ccde5419ec4fedd027ade59ba3cf45c.

## Frontier

Combining this theorem with EC49FJK B23 (18), EC49FJO B20..22 one-key release (698), and EC49FJP B20..21 two-key release (18) gives **4186** newly classified six-path fixed-background optimality problems this round. Follow-on research: B=10,12,13,14,15 and remaining low-budget classes, then seven-or-more substitutions/nonlocal 93-native-prefix construction. Global C_min(7) ?=94 is open. PR #1730 remains author-side Draft pending the actual formal Result/Driver review path.
