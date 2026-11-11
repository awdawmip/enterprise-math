# EC49FJR — B10, B12–B15 released-key six-path exact local optimum

Date: 2026-11-11. Status: **AUTHOR_EXACT_FINITE / REPRODUCIBLE / UNREVIEWED / NOT_ADMITTED**.

Scientific input frozen at `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`: EC49FGW nine-state signed native X6 generator, EC49FGJ witnesses A/B with 24 labelled observation demands, seven complete cache keys and 94 distinct signed ordered native prefixes each. Catalogue contains exactly 178,850 legal words and 94 complete raw key triples.

## Theorem (finite, all released-key radius-six cases in the stated budget classes)

Fix either original 94-prefix witness A or B. For each choice Q of six of its 24 demand paths, hold the other eighteen original paths fixed. Let F(Q) be the union of their complete signed ordered native X6 microstep prefixes and K_F(Q) their full raw cache key set. Consider **all** Q for which at least one original key is released and B(Q):=93-|F(Q)| lies in {10,12,13,14,15}.

Allow the six omitted paths to be replaced by **any** legal frozen-catalogue words, with at most seven complete raw cache keys overall. For every one of these contexts the **exact minimum total native-prefix cost is 94**.

| B=93-|F| | Fixed prefix count | A contexts | B contexts | Both | Exact minimum added prefixes |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10 | 83 | 2,188 | 2,188 | 4,376 | 11 |
| 12 | 81 | 1,720 | 1,720 | 3,440 | 13 |
| 13 | 80 | 936 | 936 | 1,872 | 14 |
| 14 | 79 | 572 | 572 | 1,144 | 15 |
| 15 | 78 | 1,001 | 1,001 | 2,002 | 16 |
| **Total** | | **6,417** | **6,417** | **12,834** | |

Release counts: 11,708 contexts release one raw key; 1,120 release two; 6 release three. Exactly **18,606** admissible complete seven-key superset options were explored for the 12,834 fixed-background contexts. A, B original witnesses each attain 94, establishing an upper bound matching the lower bounds.

## Proof of completeness

Let r=7-|K_F| (r=1,2,3 for this census), and let R denote six omitted labelled demands. Given *any* legal completion of these demands with at most seven raw keys, extend its used-key set, if necessary, to a seven-key superset K_F∪L; choose L of size r from the original catalogue's 94 keys outside K_F. Extension only enlarges the candidate word set and cannot exclude the completion. The labels not already covered by K_F must be covered by L. Our exact generator enumerates every such L, including keys that do not individually cover a missing label but might improve sharing of native prefixes. Thus the enumeration includes at least one full-key superset for every feasible solution.

For each allowed superset, construct the rooted trie of *all* legal signed ordered X6 microstep words satisfying each of six labelled demands. An edge's purchase cost c(e) is 0 if its entire native prefix belongs to F(Q), and 1 otherwise. Let d_v(S) be the least cost for realizing demand subset S below node v, excluding the edge entering v. Terminal node masks supply zero for all their subsets. For child u merge disjoint S,T via the exact recurrence:

```
d_new(S union T) = min(d_old(S) + d_u(T) + c(v,u) * [T nonempty])
```

The root result for the full six-label mask equals the optimal number of new native prefixes, because the union of root-to-terminal witness words is exactly a rooted prefix subtree and a shared prefix edge is purchased once. No scalar endpoint, unsigned quotient, path-order erasure, or cache-key collapse is performed.

Each root result is clipped at `CAP=B+1`, which discriminates *every* cost ≤B from the original witness cost B+1. The executed finite search returned clipped best value B+1 in **all 12,834 cases** and never found `feasible_93>0`. Therefore each exact optimum is |F|+B+1=94.

## Executed verification and exact source identity

The author executed the frozen generator and a compiled C++17 64-mask signed-prefix trie solver over every case. A long first process produced 12,364 ordered records; 464 records were resumed; six separately computed three-key-release records were inserted in exact (profile,Q) order. A final strict 12,834-row join checked uniqueness, order, admissible options, B distribution, `best_clipped=B+1` and `feasible_93=0`. Author-side independent Python set-antichain union DP reproduced 46 sampled grouped cases, two from each populated (profile, B, released-key-count) group with a unique key option, exactly agreeing with C++.

The two deployed source-code Git blob identities for actually executed generator/solver:
- `MAKE_B10_B15_RELEASE.py` — `bb25c00ec315e0c83f758cf7a70ecd02bf17d8ef`.
- `FJR_EXACT_TRIE.cpp` — `11ec5eb13ae0075aa9fbf891093183f1c17135bd`.

Full source and result SHA256:
- `FJR_CATALOG.tsv`, 3,409,032 bytes: `b4e7bcc88306fa846f752f1ca1e6b31957e9ac65080d80a0c7506447004dc489`.
- `FJR_CASES.tsv`, 29,514,984 bytes: `6f3ab6e14d2aecc7d0b820619ae199b1ee32f3fea3d595c16c3719aa119fe3c3`.
- `FJR_CPP_RESULTS.jsonl`, 1,293,272 bytes (canonical exact joined 12,834 rows): `fc643a9fb008cb2ed05046538f91e1a0c61309196c02aea982fe56f5aa539c59`.
- `FJR_PY_CROSSCHECK_REPORT.json`: `3d1282ae4c628623f96af409ca17bd0060a64cf15862de75716241674ead0995`.

Frozen input dependencies already on the same PR: `EC49FGW_RADIUS5_SCREEN.py`, `EC49FGJ_SEVEN_KEY_94_WITNESSES.json` and `ec49fjd_shared.py`. For reproduction, place these next to the sources in this directory; run:

```sh
python MAKE_B10_B15_RELEASE.py
g++ -std=c++17 -O3 FJR_EXACT_TRIE.cpp -o fjr_exact
./fjr_exact FJR_CATALOG.tsv FJR_CASES.tsv FJR_CPP_RESULTS.jsonl
python FJR_PY_CROSSCHECK_60.py
```

The generated input report `FJR_CASE_SUMMARY.json` records all (profile,Q) backgrounds. The complete generated 12,834-row outputs and raw TSV inputs are preserved in the separately downloadable full author evidence package; these files can also be regenerated from the published code. If a one-shot C++ output differs in serialization whitespace from the joined original, compare each indexed JSON record semantically before comparing SHA256.

## Next step and authority

Account for all remaining six-path budget classes against the now completed EC49FJD B11, EC49FJQ B16–19, EC49FJO/FJP B20–22, EC49FJI/FJK B23/B25, and earlier partial categories; then extend to seven-path replacement and nonlocal direct construction/search for ≤93 edges. Global `C_min(7) ?= 94` remains open.

Evidence is independent author-side project research on Draft PR #1730; no current immutable EC49AS task CLAIM, Formal Result, or independent Driver mathematical review is asserted.
