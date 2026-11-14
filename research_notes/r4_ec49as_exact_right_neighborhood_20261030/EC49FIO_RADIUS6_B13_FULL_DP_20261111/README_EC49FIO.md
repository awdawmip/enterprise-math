# EC49FIO — Exact six-path native-BRC B=13 classification

**2026-11-11; frozen scientific pin:** fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Predecessor EC49FIN at PR #1730, observed head efaacd63b65f444439c02341c22dc95ec1bd62dc. The original 94-edge EC49FGJ seven-key witnesses A and B have blob SHA1 e65c1598ad9fa2680558046ed1e59d83806536b8. Original source formulas and signed-X6 step ordering are maintained.

**Author identity:** authenticated TASK_RESEARCH session returned Researcher-ID EM-DIRECT-4C5B06, Activity-ID RA-2A1465A1BA1C46B28EFE8242, verified canonical Source at 87546de60e24454c5f60224d3e1dbaa0998768fd. No EC49AS task CLAIM or independent Driver review was obtained.

## Exact finite proposition

For each of the EC49FGJ A/B witnesses (24 labeled BRC observations, seven *complete* original keys, 94 distinct nonempty signed six-axis ordered microstep prefixes), replace any six words Q while keeping the other eighteen original words unchanged. Consider the Q for which the 18 fixed words preserve **all seven** original complete keys and their prefix union F(Q) has exactly 80 members. Each witness has exactly **2,498** such Q.

Every admissible six-word completion satisfying the six BRC observations with **at most seven** complete cache keys must contribute **at least 14** different native prefixes outside F(Q). The original six words contribute exactly 14. Therefore for all **4,996** subproblems:

\[
\min_{\mathrm{legal\ six\ words},\,\#K\le7}|F(Q)\cup P(w_1)\cup\cdots\cup P(w_6)|=94.
\]

The 93-edge target corresponds to a new-prefix budget B=13. The result refers to this exact fixed-background class; key-releasing cases and larger local/global searches remain open.

## Complete input enumeration

The frozen nine-state BRC word generator produces 178,850 legal words in the declared 24 observation classes. The complete seven-key restricted catalog contains exactly 9,838 words, represented in a prefix trie of 42,735 nodes. Every full word has one exact labeled terminal. Since the fixed 18 words already occupy all seven permitted complete keys, any admissible completion must use the original seven-key catalog; this establishes exhaustiveness of the restricted catalog.

MAKE_INPUT_EC49FIO.py enumerates all C(24,6)=134,596 six-index subsets, computes exact per-prefix support and per-key support, and emits exactly the 2,498 subsets per profile meeting the 80-background and full-key-retention tests. The generator uses the original EC49FGW_RADIUS5_SCREEN.py and EC49FGJ frozen witnesses without changing source, observer or key semantics.

## Prefix-trie proof

Give each trie edge entering prefix v cost c(v)=0 if its prefix is in F(Q), or 1 otherwise. For subset S of the six required labels, let d_v(S) be the minimum cost of selecting rooted paths below node v meeting the requirements S; d_v(empty)=0. A terminal for label i gives d_v({i})=0. To merge child u into a parent with previously processed children, use:

\[
d_{\mathrm{new}}(S)=\min_{T\subseteq S}
[d_{\mathrm{old}}(S\setminus T)+d_u(T)+c(u)\mathbf1_{T\ne\emptyset}].
\]

Every chosen word is a root-to-terminal path. Its prefix union is a rooted subtree, so the recurrence pays every selected child edge exactly once and enumerates all possible allocations of labels to branches. Structural induction on trie height and children establishes exactness. Subsets are updated in descending integer-mask order, so for T nonempty the smaller mask S\T has not been overwritten by the current child merge. Arithmetic is integer and saturated at B+3=16, above the observed optimum 14.

VERIFY_EC49FIO.cpp first gives exact pair and triple lower-bound exclusions, and VERIFY_FULL6_EC49FIO.cpp solves all six labels for every surviving Q. The executed local proof produced:

| Outcome | A | B |
|---|---:|---:|
| Full fixed-seven-key B=13 positions | 2498 | 2498 |
| Excluded by exact pair bound | 77 | 154 |
| Further excluded by exact triple bound | 989 | 912 |
| Full six-label DP cases | 1432 | 1432 |
| Full DP exact minimum new prefixes 14 | 1432 | 1432 |
| 93-edge feasible completions | 0 | 0 |

The original 94-edge witness matches all lower bounds, establishing the precise optimum.

## Verification and reproducibility

The source run compiled the C++ programs with g++ -O3 -std=c++17, regenerated each trie and Q list, and processed the full DP survivors in five deterministic chunks per profile (300+300+300+300+232). All ten chunks reported exactly new-prefix optimum 14 and zero <=13 completions. The raw local evidence archive, with full Q and trie inputs and actual run outputs, is named EC49FIO_B13_all_exact_evidence_20261111.tar.xz, SHA256 905d945a8c26c444cd6c4687d0e1f7ac93993d014f2e4ef924f8c8702daad736. The independent toy oracle additionally compared 160 literal six-label choices to a separate Python trie recurrence and all 4,996 original witness upper bounds passed.

Steps with the frozen predecessor dependency in the sibling directory:

1. python MAKE_INPUT_EC49FIO.py
2. g++ -O3 -std=c++17 VERIFY_EC49FIO.cpp -o check_triple
3. g++ -O3 -std=c++17 VERIFY_FULL6_EC49FIO.cpp -o check_full
4. For each X in A B: run ./check_triple TRIE_X.txt QS_X_13.txt 13 > RUN_X13.log
5. For each X: sed -n 's/^SURV //p' RUN_X13.log > SURV_X13.txt
6. For each X: run ./check_full TRIE_X.txt SURV_X13.txt 13

The first output has the pair/triple counts above; the second outputs checked=1432, excluded=1432, possible=0, optimal_new_prefix_hist={"14":1432}. Source files and the machine-readable summary are adjacent to this note.

## Next precise question

Continue B=10, B=12, and B>=14 fixed-key six-path cases, then design a key-selection state that permits original-key release. Seek a 93-edge construction globally, or extend rigorous 94-edge local bounds. This work is an exact finite author-side result, pending independent Driver mathematical review and formal Result admission.
