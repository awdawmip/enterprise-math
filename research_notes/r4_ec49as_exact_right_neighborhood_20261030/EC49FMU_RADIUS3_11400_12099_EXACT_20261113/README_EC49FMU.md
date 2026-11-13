# EC49FMU — exact seven-key BRC radius-three configurations 11400–12099

Date: **2026-11-13**. Classification: author-side finite exact computation; awaiting independent Driver review.

## Frozen model, question and exact finite conclusion

Continue EC49FMT from the consecutive frontier **11399**. The scientific pin remains `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`: nine-state BRC, **178,850** lawful operation words, **94** complete raw keys, **24** observation labels, and ordered signed native X6 microstep-prefix cost. No input or admissibility changes. The 38,169-case deterministic catalogue indexes coverable seven-key configurations formed by replacing three keys in the frozen baseline.

Let `K_i` be the fixed seven-key case at index `i`, and `C(K_i)` the minimum number of distinct nonempty ordered signed-native X6 prefixes among lawful words covering all 24 labelled observations. Complete exact enumeration of the 700 configurations `11400 <= i <= 12099` establishes:

```
min C(K_i) = 118, uniquely attained at i=11511.
max C(K_i) = 196, attained at 21 indices.
Root-option counts: 105 cases with 3 roots; 595 cases with 4 roots.
```

The cumulative minimum for the full previously completed consecutive window `0..12099` stays **102**, witnessed at earlier indices (32, 93, 6589, 11121). This radius-three family is a constrained test set. The separately existing unrestricted seven-key construction retains its **84-prefix upper bound**.

## Constructive certificate at index 11511

`EXACT_DATA_EC49FMU.json` lists all 24 lawful BRC operation words and the seven complete raw-key indices `[0,4,5,6,24,34,49]`. Their *ordered signed-native* prefix union has exactly **118** distinct nonempty elements. The three used first-microstep roots contribute **42 + 52 + 24 = 118**, respectively. This is the upper certificate. Full exact trie/subset dynamic programming gives the matching lower value **118** for index 11511.

## Exact algorithm and audit

Frozen original solver `scan_cached_radius3.cpp`, SHA256 `6ea17ff267f599c69967b420ebf1a8abe151e587e57b25f599f8ecdfb9f2ecac`; original input `master_and_radius3_cases.txt`, SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. The input contains **94 keys, 178850 legal words and 38169 pre-enumerated cases**. Exact reproduction command:

```bash
g++ -O3 -std=c++17 scan_cached_radius3.cpp -o scan
./scan 11400 12100 < master_and_radius3_cases.txt > EXACT_NATIVE_OUTPUT_11400_12099.txt
```

Each first-microstep root has a trie of complete signed-native prefixes. A bottom-up integer DP computes the minimum counted nonempty nodes for any subset of terminal demand labels. At a node, child label subsets combine by bitwise union and min-plus addition; selecting a nonempty subtree costs one additional prefix at the current nonroot node. The induction starts at leaves and is exact. After subset closure, all legal label-to-root assignments are enumerated; distinct first-microstep roots are disjoint in prefix identity, so summing their exact minima is exact. This yields both an attainable upper solution and exhaustive lower certificate per fixed case. No sampling, floating approximation or projection of path order is used.

The 700 consecutive raw solver rows have SHA256 `27721aa9c64546ba84d51049df1d5d2792f444a7c03728e185a2e26d912a0143`; the complete ordered cost-byte vector is losslessly encoded in `EXACT_DATA_EC49FMU.json` as zlib+base64, SHA256 `6f4304a15098e2edce36c6fe92047f218715f3ef3af6db6811dd080ffb8fad16`. All 700 sequential rows are present in the companion full-evidence archive. The separate Python prefix-trie solver, independently rebuilding the original BRC word catalogue, returned `11400=130, 11511=118, 12099=140`, matching the C++ output. The exact 24-word witness was independently revalidated against the full 178850-word catalogue.

## Original sources, remaining question

The immediately preceding published author-side evidence is [EC49FMT PR #2195](https://github.com/awdawmip/enterprise-math/pull/2195), commit `bc7b66ba3ad4a8af5fb0ebba695c745147413ead`; use its companion original source/evidence bundle and frozen generator. The original 700-row output, frozen original 9 MB master, complete 38169-case list, independent verifier, witness reconstruction, logs and hashes are also preserved in this run's local full-evidence bundle. This GitHub note carries the compact verifiable finite result and construction.

Next exact unfinished index: **12100**; 26,069 of the 38,169 coverable radius-three configurations remain after this run. Continue independent lower-bound certification across key configurations and investigate whether a lawful unrestricted seven-key construction can improve the separate 84 bound.

Control: author-side material. Latest native `RS-EC49AS` task read and this execution-session registration were QUEUED at publication preparation; neither a winning CLAIM nor formal Result/review is asserted. Preserve existing owner rights, immutable input pins and author/Driver distinction.
