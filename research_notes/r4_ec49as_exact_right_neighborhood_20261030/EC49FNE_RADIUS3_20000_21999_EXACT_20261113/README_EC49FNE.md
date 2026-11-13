# EC49FNE — 2,000 exact seven-cache BRC configurations and a new 86-prefix radius-three record

Author-side research, 2026-11-13. Frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The non-overlapping contiguous window **20000–21999** continues [EC49FND PR #2238](https://github.com/awdawmip/enterprise-math/pull/2238) ending at 19999.

## Model and exact finite method

The frozen original nine-state BRC generator has 178,850 lawful operation words, 94 complete cache keys, 24 distinct observation labels and 38,169 lexically indexed radius-three seven-key configurations. Every lawful word expands to an **ordered, signed native X6 microstep path**. For each selected seven-key set K, define C(K) as the fewest distinct nonempty ordered/signed native prefixes in a set of lawful operation words covering all 24 labels. No endpoint-only, unsigned, unordered or coordinate-collapsed identification is used.

At each eligible first-microstep root r, form the original-word prefix trie. Bottom-up exact integer DP computes f_r(S), the minimum activated nonempty trie-node count covering a required subset S of its observation labels, with superset closure. Exhaustively assign each of the 24 labels to an eligible root, minimizing the sum of the root f_r values. A lawful word selection induces an admissible root assignment; each DP tree solution reconstructs lawful original words. These two directions give matching bounds for every fixed configuration, under completeness of the pinned frozen catalogue.

## Exact result

All **2,000** integer configurations i=20000,…,21999 were calculated from the same frozen source. The minimum **86** is attained at exactly two indices **21524 and 21525**; maximum **218** at **20203**; there are **96 distinct costs**.

| Index | Seven complete cache keys | Exact cost | Active first-root subtrees |
|---|---|---:|---|
| 21524 | 0, 4, 5, 11, 14, 15, 16 | **86** | 43 + 43 |
| 21525 | 0, 4, 5, 11, 14, 15, 26 | **86** | 43 + 43 |

Each minimum has a 24-word lawful original BRC witness covering all observation labels. Both have exactly 43 distinct nonempty signed native prefixes in each of roots 05 and 06, and none in 07. The witness is the matching upper bound; the trie/subset DP is the finite lower bound. A separate Python implementation re-computed selected cases **20000→159, 21524→86, 21525→86, 21999→112**, agreeing with the original C++ solver.

New radius-three family record: earlier **96** at index **17965** (`{0,4,5,6,11,14,26}`) falls by **10** when cache key 6 is replaced by key 15, with all six other keys fixed, giving index 21525 (`{0,4,5,11,14,15,26}`). Swapping 16 for 26 between 21524 and 21525 retains exact 86.

## Full root-mask counterexamples

Exact independent native trie DP compared all **4,096** root-05 subsets, all **4,096** root-06 subsets and all **256** root-07 subsets for each pair. Entries show (first configuration strictly better / equal / second configuration strictly better):

| Pair | Root 05 | Root 06 | Root 07 |
|---|---:|---:|---:|
| 17965 → 21525 | 312 / 872 / 2912 | 398 / 826 / 2872 | 10 / 54 / 192 |
| 21524 → 21525 | 184 / 3304 / 608 | 184 / 3304 / 608 | 6 / 230 / 20 |

**Finite theorem:** The one-key improvement 96→86 is **not** pointwise root-function domination: 17965 remains strictly better on some masks of each root. Equal total optimum 86 for 21524/21525 likewise coexists with nonidentical root functions and strict advantages in both directions. Every count is exact for the fixed frozen catalogue.

## Evidence and reproducibility

Companion `EXACT_CERTIFICATE_EC49FNE.json.xz.b64` is the entire lossless JSON certificate compressed with xz then base64 (decode: `base64 -d FILE | xz -d > EXACT_CERTIFICATE_EC49FNE.json`). It contains the **2,000-byte exact cost vector** (zlib/base85 codec), source digests, both 24-word legal witnesses, full root-mask comparison counts and case keys.

* Frozen master text SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
* Raw 2,000-row C++ output SHA256: `cf468f79a773f7daae8583494f5b8e87960a43bdba4c303762588bf4a8bb6cd7`.
* Cost-byte vector SHA256: `80c58d883de91dbf4b87c87317061a6a9d4134106448771de2f5fbfe9efa3ab6`.
* Expanded certificate JSON SHA256: `1ab0f428541d7c6dab40d27c39b99d12cdde6bafd50e38e281f63f2dfd1486f4`.

Local original evidence archive also contains frozen generator and input, C++ source and the 2,000 raw rows, 24-word native path certificates, independent Python optimizer and full root-function comparator. Exact range execution: complete 800 rows 20000–20799, complete 800 rows 20800–21599, completed 400 rows 21600–21999 from a later interrupted larger command. No incomplete row or unsolved configuration was counted. Hash checks, exact legality/prefix checker and selected independent Python DP passed.

The cost-vector digest alone is not a proof of 2,000 individual lower bounds; those rely on rerunning the frozen exact integer C++ trie/subset algorithm. No formal task result or independent driver acceptance is claimed by this author-side evidence.

With previous non-overlapping windows, the author-side radius-three frontier reaches **22,000 / 38,169 (57.64%)**. The unrestricted seven-key mother problem has a separate **84-prefix lawful upper-bound construction**; 86 is the best found in this scanned restricted family, not a global lower bound.

**Next contiguous index: 22000**, 16,169 configurations remaining. A further structural question is whether native trie features characterize substitutions with substantial global improvement absent componentwise dominance.