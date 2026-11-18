# EC49FJH — complete released-key radius-six B=18: 94 native-prefix optimum

Date: 2026-11-11. Scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Prior author frontier: EC49FJG on PR #1730, commit 6fea7532117455bf0c212cf3c63575a72a611f71. Status: AUTHOR_EXACT_FINITE / UNREVIEWED / NOT_ADMITTED.

## Precise statement

Use the frozen EC49FGJ constructions A and B, each satisfying 24 **distinct labeled** BRC observation demands, at most seven complete raw cache keys, and with exactly 94 distinct ordered signed native X6 microstep prefixes. Select any six of the 24 witness words for replacement, holding the other 18 words fixed with prefix union F and complete key set K_F. Restrict to the class with |F|=75 and at least one original cache key released (one or more of the seven original keys absent from K_F). Arbitrary legal replacement words meeting their respective original six labels and at most seven complete keys globally are allowed.

**Theorem:** Every such six-position fixed-background subproblem has minimum total native-prefix count exactly 94. There are 418 positions for A and 418 for B (836 total). An improvement to 93 would require at most 18 new prefixes; the original six words attain 19.

## Exhaustive certificate

The exact frozen nine-state grammar has 178,850 legal words and 94 complete raw key types. All C(24,6)=134,596 position sets per witness are examined before restricting to F=75 and released keys. An exhaustive six-label key cover over the 94 keys determines whether each released original key is indispensable.

**Class I: 416 positions per witness, total 832.** All original seven complete keys are forced to return. Both H9 demands (9,16) and (9,32) occur among the six replaced labels. Each H9 label has 280 legal words on the original seven keys. The separately executed PAIR_H9_B18.py enumerates all 280×280 word pairs, preserving the signed ordered prefix sets, and yields

min |(P(w_16) ∪ P(w_32)) \ F| = 19

in **each** of the 832 fixed backgrounds (exact minimum histogram {19:832}). Thus two of the six required words alone exceed the 18-edge budget. Full six-label trie DP independently returns clipped value 19 on all these positions.

**Class II: two positions per witness, four total.** The exact position tuples are (8,18,19,20,21,22) and (9,18,19,20,21,23). K_F contains exactly six distinct complete keys. At most one seventh key may be added. A key is safely discarded if no replacement label has an individual legal path adding <=18 prefixes under that key: any union of <=18 new edges would also make each individual subset <=18. Exactly 42 candidate seventh keys survive for each of these four backgrounds; the original released key is included. For each of the 4×42=168 allowed key sets K_F∪{k}, the exact full six-label native prefix trie DP returns value at least 19, clipped at 19. This includes six-key-only solutions. Hence no Class II solution meets budget 18.

The combined exact C++ computation includes 832 forced-key + 168 optional-key = **1,000** allowed-key trie solves, recorded as 836 position rows, each best_clipped=19 and feasible_93=0. Original witnesses prove the matching 19-edge attainable bound.

## Exact dynamic program and completeness

A node of the signed native prefix trie represents the *entire ordered prefix*, not its endpoint coordinate. Its edges cost 0 if already in F and 1 otherwise. With S a subset of the six distinct labeled demands, let d_v(S) be the minimum incremental cost for a subtree rooted at v satisfying S. Initialize terminal masks with cost 0. Merging one child u assigns any disjoint demand subset T to that child and applies

d_new(S) = min_{T⊆S} [ d_old(S\T) + d_u(T) + edge_cost(u) 1_{T ≠ ∅} ].

All 2^6 masks are evaluated; clipping at CAP=19 is exact for the decision <=18. Every legal word maps to one root-to-terminal path, and every union of legal paths corresponds to a rooted trie subgraph. Every seven-key configuration must fall into Class I's forced set or Class II's enumerated/safely screened allowed sets. Hence the enumeration is exhaustive for the stated finite domain.

## Execution and reproduction

The scripts in this folder require the pinned dependencies EC49FGW_RADIUS5_SCREEN.py, EC49FGJ_SEVEN_KEY_94_WITNESSES.json, and ec49fjd_shared.py from the earlier PR #1730 source/evidence directories, colocated in the working folder. Run python MAKE_B18_INPUT.py to generate B18_CATALOG.tsv (178,850 words) and B18_CASES.tsv (836 positions, 1000 allowed-key solves). Compile g++ -std=c++17 -O3 B18_EXACT_TRIE.cpp -o B18_EXACT_TRIE, then run ./B18_EXACT_TRIE B18_CATALOG.tsv B18_CASES.tsv B18_RESULTS.jsonl. Execute python PAIR_H9_B18.py and python INDEPENDENT_CHECK_B18.py. The result JSONL has 836 rows, all with best_clipped=19, feasible_93=0. The two-H9 independent report has 832 rows, all minima 19. The independent check verifies original witness cost 94 for every recorded position and ten reduced-label cross-checks.

Author execution on 2026-11-11: 178850 word rows, 94 keys, 836 positions, 1000 allowed-key exact tries, 168 optional-key tries; all pass. Local complete C++ run elapsed 10.26 seconds, a machine-specific measurement. The full original executed TSV inputs, 836-row report, 832-row independent report, logs, local exact code and SHA256 manifests are preserved in the separately delivered evidence archive.

SHA256 of local executed code and results: B18_EXACT_TRIE.cpp = 8c077f7a41d798b216522b491eb865b5db674379dec90ae5a80ac5bdd1f6495d; MAKE_B18_INPUT.py = cd328b9383525c9ab44d057a6d0215b945738cfdd0c7c1fdaa01c4ea5100fdd5; PAIR_H9_B18.py = 696265780426f46f27e80861296be4048c708033c31ec8505a6f9154fdc60fd7; B18_CASES.tsv = cae19d0dcd13b5f66187fd982322257972927e49f953a8c3a79c0dde127c83b3; B18_RESULTS.jsonl = 51e673826c399caa2e1363ae2f51b9598b932f81991622126e34570e4bb2db44; EXACT_H9_PAIR_REPORT_B18.json = 17e71900714f90c68a5d5fdabef984fcc7cf39018f92361d5ec7a164e62b587d.

This proves the **finite local subproblem**, not the unrestricted seven-key global question C_min(7) ?= 94; independent Driver review and Source-native Result remain pending. Next action: regenerate a disjoint complete six-replacement-budget partition, check remaining scopes, then pursue larger/nonlocal (at least seven changed paths) 93-prefix constructions or prove further exact lower bounds.
