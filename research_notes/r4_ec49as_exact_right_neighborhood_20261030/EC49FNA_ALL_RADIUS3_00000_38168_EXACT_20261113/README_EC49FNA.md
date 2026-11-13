# EC49FNA — Full finite seven-cache-key BRC radius-three scan (38,169 cases)

2026-11-13 | Researcher EM-DIRECT-78789D | author-side exact computation, **not** independent mathematical admission.

## Frozen science and objective

Fixed scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Frozen `master_and_radius3_cases.txt` SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.

The frozen nine-state legal BRC catalogue has **178,850** full lawful words and **94** complete cache keys. The radius-three replacement enumerator gives **38,169** distinct, indexed seven-key configurations, each with 24 labeled observation demands. For a fixed key set K, minimize the cardinality of the union of distinct, nonempty, **ordered signed native X6-step prefixes** of legal selected words that collectively cover all 24 demands. Denote this finite integer optimum C(K). A raw cache-key index is not a physical spatial axis.

## Exhaustive result for precisely this finite family

Every index 0..38168 is covered, with a contiguous, losslessly compressed full exact cost vector in `EXACT_VECTOR_ALL_RADIUS3.json` and 18 source shards. The exhaustive finite result is

`min_{0<=i<=38168} C(K_i) = 86`

and the only five minimizers are:

| i | Seven complete key indices | C(K_i) | first-step roots |
|---:|:---|---:|:---|
| 21524 | 0,4,5,11,14,15,16 | 86 | 43+43+0 |
| 21525 | 0,4,5,11,14,15,26 | 86 | 43+43+0 |
| 30266 | 0,4,5,11,32,34,49 | 86 | 43+43+0 |
| 30393 | 0,4,5,11,32,46,49 | 86 | 43+43+0 |
| 30396 | 0,4,5,11,32,46,61 | 86 | 43+43+0 |

The maximum is 234, unique at index 34796.

Previous source-verified archives covered 5,500..16,299 (10,800 cases, previous minimum 102). This run newly solved **16,300..38,168** (21,869 cases), and independently recomputed **0..5,499** (5,500 cases). The earlier 10,800 cases were faithfully reconstructed from 11 prior evidence archives. Together those results are 38,169 complete contiguous cases, with raw shard paths, SHA256 digests, and byte content bound in the offline full source archive. This is an exhaustive calculation only for the *enumerated restricted* family, not every possible unrestricted seven-key choice.

The previously established global seven-key mother-problem construction yielding `C_min(7)<=84` remains valid. In particular, a restricted-family minimum of 86 **does not** improve or contradict the 84 global upper bound, and must not be confused with the unrestricted optimum.

## Exact optimization and why the dynamic program gives the true finite minimum

For each signed first-step root r, construct a trie from every legal complete-key word available in K with first step r. Trie vertices are the complete ordered signed prefixes, and terminals carry observation-label masks. Define D_v(S) as the minimum number of charged prefixes in vertex v's subtree for realizing label mask S. At a terminal, its available mask may be taken. Children have disjoint strict-descendant prefix sets: combine child alternatives by mask OR and additive cost, then add one when the non-root v is used. Induction over this finite trie gives exact D_v. Superset relaxation provides F_r(S): the exact minimum cost to cover required local mask S, allowing extra labels.

Assign each one of the 24 distinct demands to any first-step root capable of supplying it. Prefix sets of distinct roots are disjoint. Thus

`C(K) = min_(feasible demand assignments A) sum_r F_r(A_r)`.

This exact finite assignment enumeration and integer trie DP give a *lower bound matching a constructible upper bound* for each one of the enumerated K_i. The C++17 solver caches exactly equivalent root subset signatures. There is no floating point or heuristic pruning. Recompute with frozen `scan_cached_radius3.cpp` using `g++ -std=c++17 -O3 -DNDEBUG scan_cached_radius3.cpp -o scan_radius3`, then `./scan_radius3 START END < master_and_radius3_cases.txt` (exclusive END).

For the five minimizers, independently reconstructed source witnesses each consist of 24 actual lawful complete-cache-key BRC words covering the 24 distinct labels, with **86** different nonempty native signed prefixes. Their first-step partition is exactly root 05:43 + root 06:43 + root 07:0. Source-witness checker verifies word identity, key membership, all prefix bytes, demand uniqueness, and prefix count against the original frozen generator. See the full original evidence archive.

An independent Python trie/Demand-mask implementation, separate from the C++ engine, matched selected original cases including indices 0=116, 5499=160, 16300=174, 16807=98, 17965=96, 21524=86, 21525=86, 30266=86, 30393=86, 30396=86, 34796=234. It did **not** independently rerun all 38,169; the completeness claim relies on the exact C++ scan, 18 exact-contiguous logs, per-shard checks, and verified source recurrence.

## Reusable lemma: pointwise root-envelope dominance

Consider the two legal configurations i=16807 (C=98) and i=17965 (C=96) differing by a complete-key swap 1->6. They have identical admissible root and label domains. Exhaustive comparison of F_{i,r}(S) for all 4096+4096+256=**8448** root/mask combinations showed new <= old for every mask: **3534** masks strictly lower and **4914** unchanged. Therefore an old legal assignment remains available and its cost cannot increase, proving C(new)<=C(old) as a sufficient condition whenever root-domain availability is preserved. Strict improvement to 96 is separately certified by the exact solver. The root-envelope checker in the full source archive produces the mask counts.

## Files, integrity and limits

- `EXACT_VECTOR_ALL_RADIUS3.json`: lossless zlib/base64 of 38,169 unsigned-byte costs, complete 18-group source manifest, minima/maxima, source metadata.
- Byte cost-vector SHA256: `b191610ed4f372b033536143999a86e7a3cdae39e8b28b8a63fc3660a916b8ba`.
- Concatenated full uncompressed native output SHA256: `37a6ca07b4c771125ef845bc691465362fd2eb0a52ed033eaa257d0269ec312c`.
- All five full lawful-word witnesses, Python code, C++ solver, frozen master input and native outputs are in the original source evidence package `EC49FNA_FULL_RADIUS3_00000_38168_SOURCE_EVIDENCE_20261113.tar.xz`, SHA256 `824a7ea06a62c7d0f3f754912a95632f2d29201209bd1ae248a52a16027656c4`.
- Source origin: earlier immutable PRs #1730, #2191, #2195, #2198, #2202, #2207, #2209, #2212, #2218; source archive records exact original tar member digests. A source hash is integrity evidence, not a mathematical admission.
- Native Task lookup for `RS-EC49AS`: `NO_CANONICAL_PUBLICATION_DIRECTORY` at pinned Source `b7fdc4eeac26a5e0ac582514322252570b6e586a`; this read-only directory absence does not establish owner state of any unrelated task. No CLAIM, Result or independent Driver acceptance was asserted.

## Scientific continuation

Seek an unrestricted seven-complete-cache-key construction using at most 83 ordered signed X6 prefixes, or new global lower bounds. Within the restricted completed family, characterize the exact root-envelope equivalence that allows five distinct cache-key sets to attain 86 without recalculating every case. Distinguish reuse/partial isomorphism from native operation permission and from all-key optimality.
