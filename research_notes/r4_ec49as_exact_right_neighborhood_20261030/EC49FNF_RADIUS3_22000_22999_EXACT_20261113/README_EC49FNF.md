# EC49FNF — 1,000 exact BRC radius-three cases and a 2 × 2 cost rectangle

Author-side mathematical research, 2026-11-13. Frozen scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` is kept unchanged. This nonoverlapping interval **22000–22999** follows [EC49FNE PR #2243](https://github.com/awdawmip/enterprise-math/pull/2243), whose last complete index was 21999.

## Exact problem and computation

The original nine-state frozen BRC catalogue has 178,850 lawful operation words, 94 complete cache keys, 24 observation labels and 38,169 seven-key radius-three configurations. Each original operation word expands to a path of **ordered, signed native X6 microsteps**, with branch/path provenance preserved. For each selected seven-key configuration K, C(K) is the minimum number of *distinct nonempty ordered signed native prefixes* in lawful words jointly covering all 24 observation labels. Endpoints, unsigned axes or unordered coordinates are not collapsed.

The original C++17 exact prefix-trie / demand-subset integer DP calculated **all 1,000 configurations i=22000,…,22999** in a single complete scan with terminal `FINISHED` and exit code 0. For each first microstep root r, a full lawful-original-word prefix trie yields the minimum activated node count f_r(S) for every required label subset S, with superset closure. Exhaustive assignment of every label to eligible roots, followed by minimization of the sum of root f_r values, yields C(K). The double realization correspondence between an original lawful cover and root trie solutions proves the matching finite upper/lower bounds, subject to the completeness of the frozen original catalogue.

The unique minimum cost is **96** at exactly **22247** and **22404**. Maximum cost is **206** at index **22233**; 84 distinct costs are attained.

| Index | Seven complete cache keys | Exact optimal cost | Original lawful witness |
|---|---|---:|---|
| 22247 | 0,4,5,11,15,16,32 | **96** | 24 words, 48+48 native prefixes |
| 22404 | 0,4,5,11,15,26,32 | **96** | 24 words, 48+48 native prefixes |

Both minimum configurations have reconstructed sets of 24 lawful original BRC words covering all labels; they use 48 distinct nonempty signed native prefixes in root 05, 48 in root 06, and none in root 07. Independent Python native-trie/subset optimization separately checked **22000→112**, **22247→96**, **22404→96**, **22999→136**, agreeing exactly with C++.

## New finite 2×2 cache-key rectangle

Fix the shared five-key set `B={0,4,5,11,15}`. Let `A∈{14,32}`, `D∈{16,26}`; set `K(A,D)=B∪{A,D}`. The four exactly solved configurations form:

| A | D=16 | D=26 |
|---|---|---|
| 14 | **21524:** C=86 | **21525:** C=86 |
| 32 | **22247:** C=96 | **22404:** C=96 |

Hence, for the four listed frozen configurations, replacing key **14→32** raises the global exact optimum by **10** under either choice of D, whereas replacing **16→26** preserves the optimum for both A values. The mixed second finite difference vanishes exactly:

[
C(K(14,16))-C(K(14,26))-C(K(32,16))+C(K(32,26))=86-86-96+96=0.
]

**This is a complete four-case finite proposition about exact global optimal costs, not a universal statement for all key substitutions.**

For each substitution pair the independent native trie DP computed **all** 4,096 root-05 label masks, all 4,096 root-06 masks and all 256 root-07 masks. Values show `(first configuration strictly better / equal / second strictly better)`:

| Pair | Root 05 (4096) | Root 06 (4096) | Root 07 (256) |
|---|---|---|---|
| 22247→22404 | 392 / 2480 / 1224 | 368 / 2534 / 1194 | 10 / 184 / 62 |
| 21524→22247 | 2740 / 1316 / 40 | 2740 / 1316 / 40 | 169 / 85 / 2 |
| 21525→22404 | 2608 / 1412 / 76 | 2608 / 1412 / 76 | 169 / 85 / 2 |

Every pair is strictly better in **both** directions on some root masks. Thus neither individual pair is pointwise root-function dominated, but their complete global optima have the exact rectangle relation above. This provides a concrete example of **min-plus allocation-level invariance and compensation** worth exploring. It does not disturb the previously proved general sufficient lemma that pointwise weak dominance of every root function implies nonincrease of the global optimum.

## Verifiable source and evidence

- Frozen full master input SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
- Original complete 1,000-row C++ output SHA256: `983633097b8bbe16adf455e9f6a48781687b20c09a84fc3abb9a8ebb9a3f1782`.
- 1,000-byte cost vector SHA256: `bfd9474433ccc0f169511ca5479803a95945c86dcf933f65a704dcd6c0b580f3`.
- Expanded certificate JSON SHA256: `5e54a8992dd5eb4a08055a42e829ab7adcdd606d499843be97c42b4905cde7db`.

Companion `EXACT_CERTIFICATE_EC49FNF.json.xz.b64` contains a **lossless zlib/base85 cost vector for all 1,000 cases**, two full lawful original 24-word witnesses, cache keys, source hashes and exact root comparisons. Decode the outer container with `base64 -d ... | xz -d`. The companion checker verifies vector and original-word legal signed-prefix witnesses when placed with the original frozen generator and master input from the full evidence archive.

The deliverable complete local evidence archive additionally holds the original full frozen master and case catalogue, C++17 exact solver, original full scan output and stderr with completion evidence, independent Python trie/subset solver, root-function comparator, two lawful 24-word witness paths, and a SHA256 manifest. The exact cost-vector hash alone is not the proof of all optimum lower bounds: those follow from the frozen C++ integer DP and can be checked by reexecuting it.

Combining nonoverlapping author-side saved windows, the contiguous frontier is now **23,000 / 38,169 (60.26%)**; the best value in this *restricted* family is still **86**, from EC49FNE. The unrestricted seven-key mother problem retains the separate lawful **84-prefix upper-bound construction**.

**Next contiguous index: 23000**, remaining 15,169 cases. A next useful direction is to characterize the exact min-plus root-allocation conditions for cost-flat key changes or zero mixed differences even when the underlying root-mask functions vary substantially. This is author-side science, pending formal task/CLAIM/Result authority and independent Driver review.
