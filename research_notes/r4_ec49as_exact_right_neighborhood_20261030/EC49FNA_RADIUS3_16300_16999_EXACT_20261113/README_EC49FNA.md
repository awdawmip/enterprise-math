# EC49FNA — Exact BRC seven-key radius-three configurations 16300–16999

Date: 2026-11-13. Classification: **author-side finite exact computation**, not an independently accepted mathematical Result. Predecessor: [EC49FMZ PR #2218](https://github.com/awdawmip/enterprise-math/pull/2218) at `69b87a339e159589d0d3a7e8138e35ecebb84ab3`.

## Fixed mathematical domain and source

The scientific input stays pinned to `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, with the previously verified 9-state BRC catalogue, 178,850 lawful operation words, 94 distinct *complete raw cache keys*, 24 observation labels, and 38,169 radius-three replacement configurations. No generated configuration or scientific rule was changed.

For an enumerated seven-key configuration `K_i`, let `C(K_i)` be the least number of **distinct nonempty, ordered, signed native-X6 microstep prefixes** in a set of lawful operation words covering each of the 24 labels with raw keys in `K_i`. Prefix identity retains axis, sign, order and provenance, not merely displacement or endpoint.

The 700 complete, consecutive exact integer-DP outputs for `16300 <= i <= 16999` establish

```
min C(K_i) = 98, attained exactly at indices 16807, 16953 and 16965;
max C(K_i) = 204, attained exactly at index 16827.
```

Thus the continuously checked radius-three prefix is now `0..16999`, **17,000 / 38,169 configurations (44.54%)**, and its best cost improves from **102** to **98**. The broader unrestricted seven-key BRC mother problem retains its earlier **84-prefix constructive upper bound**, which is a different, unrestricted domain.

| exact minimizer | seven raw-key indices | first signed-microstep root costs |
|---|---|---|
| 16807 | [0,1,4,5,11,14,26] | 05:49 + 06:49 + 07:0 = 98 |
| 16953 | [0,1,4,5,11,32,49] | 05:49 + 06:49 + 07:0 = 98 |
| 16965 | [0,1,4,5,11,34,49] | 05:49 + 06:49 + 07:0 = 98 |

## Constructive certificate: index 16807

This certificate contains exactly one **lawful word per label** (label `[level, observer]`, operation word). All words are checked against the frozen generator and the seven complete raw keys. In root `05` select:

```
[2,16] fe        [3,16] feg          [4,2] fegd
[4,4] fegc      [5,16] fegfg        [6,2] fegdgg
[6,4] fegcgg    [7,2] fegdggd      [7,4] fegcggc
[8,2] fegfgggd  [8,4] fegcggfg     [9,16] fegfggggf
```

In root `06` select:

```
[2,32] ge       [3,32] gef          [4,1] gefd
[4,8] gefc      [5,32] geffg        [6,1] gefdgg
[6,8] gefcgg    [7,1] gefdggd      [7,8] gefcggc
[8,1] geffgggd  [8,8] gefcggfg     [9,32] geffggggf
```

The union of actual native signed prefix-byte strings has **49** distinct nonempty elements under first byte `05` and **49** under `06`; none under `07`. This establishes `C(K_16807) <= 98`.

For the lower bound, build the complete legal-word prefix trie separately by first microstep. At each trie node, track the minimal selected nonempty-node count for each attainable subset of observation labels. At a terminal, the word's label may be selected with no extra terminal cost; union sibling subtrees by bitwise OR and add their costs; a selected non-root trie node adds one. Induction on subtree height yields the exact node-subset function. Over the disjoint first-microstep tries, assign each required label to one permissible root and minimize the sum of the exact root costs. This yields `C(K_16807) >= 98`. Hence **`C(K_16807) = 98`**, on the exact frozen finite input.

The same exact DP finds **98** for 16953 and 16965, each with reconstructed 24-word legal witness with first-step counts `49+49+0`. Their witnesses and original 700 solver rows are retained in the complete evidence archive; the companion machine-readable vector in this PR preserves all 700 exact costs.

## Independent execution and coverage

- C++17 prefix-tree/subset integer DP: complete consecutive 700 rows, original unmodified `scan_cached_radius3.cpp` and pinned 9.6 MB master input. The intended larger `16300..19298` job was interrupted after 700 complete rows; **no index >= 17000 is counted**.
- Independent Python trie/subset integer DP (not invoking the C++ optimizer) recalculated `16300=174`, `16807=98`, `16953=98`, `16965=98`, `16999=150`; all match C++.
- `RECONSTRUCT_EC49FNA.py` reconstructed all 3 complete 24-word witnesses from the frozen catalogue and exact root-mask outputs, checking their prefix unions and legal membership.
- Frozen master input SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. A complete evidence archive preserves the native rows, all three full witnesses, generator, complete 38,169-case catalogue, independent checker, C++ source, input and hashes.

The proof is exact for the declared finite configuration family. New invariant to study: three distinct seven-key configurations share `49+49+0` root-optimal allocation, even with different selected legal words. A useful next goal is an explicit sufficient condition for cost-preserving raw-cache-key substitutions, by comparing the **full labeled prefix-trie DP** rather than only root costs.

## Source / control

Current `RS-EC49AS` task-directory lookup returned `NO_CANONICAL_PUBLICATION_DIRECTORY` at Source `acb9f0ce2a1caf830393d35bb5d2c541cdff093a`; this is a directory observation, **not** an assertion about every native owner event. A TASK-bound session registration using that unpublished topic returned `CANONICAL_REJECTED: UNKNOWN_CURRENT_TASK`. This research is author-side GitHub evidence, not a CLAIM or formal Result. An independent Driver may review the mathematical evidence on its actual merits.

Next exact index: **17000**; `38169 - 17000 = 21169` remaining enumerated cases.
