# EC49FMK — Frozen BRC radius-three indices 1000–1999: exact prefix optima

Date: 2026-11-12. Status: author-side exact finite computation, pending independent mathematical review. Parent: the 84-native-prefix seven-complete-cache-key construction, source-frozen scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Consecutive prior calculations: EC49FMI indices 0–599, EC49FMJ indices 600–999, in PR #1730.

## Proposition

In the 9-state BRC lawful-word catalogue (178,850 words, 94 complete cache-key kinds and 24 observation demands), let `K_i` be the i-th support-covering seven-key set obtained by **exactly three** complete-key replacements, in the generator's deterministic order. The full radius-three support-covering list has 38,169 entries. Define `C(K_i)` as the minimum number of distinct nonempty **ordered signed six-axis native prefixes** among lawful words collectively fulfilling all 24 demands.

**Complete integer optimization for all 1,000 cases with indices 1000 ≤ i ≤ 1999 gives**
`min C(K_i) = 106`, achieved exactly at index 1724 (one assignment in the solver's complete root-allocation count). The maximum is 138. There are 477 three-root and 523 four-root instances. The minimum among the 2,000 previously and newly checked consecutive cases 0–1999 is **102**, achieved in the previously published 0–999 block. In this precisely defined finite family, no tested case reduces the earlier verified 84-prefix upper bound.

Exact costs for **every** i=1000,...,1999 are in `EXACT_VECTOR_EC49FMK.json` as a lossless 1000-byte base64 unsigned-byte vector. Values and histogram were produced from completed C++ native outputs, never from a partial timed-out line. Raw result text SHA256: `a419abc1c2f6d3e7fd800fcca783154cc5a0f3fd7f7f699df2c32860c287ab08`.

## Why the finite optimization is exact

The full lawful-word enumeration and support-covering deterministic case list are frozen by `master_and_radius3_cases.txt` SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. Within a fixed seven-key set, partition legal words by the first signed native microstep (root). Each root contains a trie of ordered nonempty native microstep prefixes. A bottom-up integer DP counts the exact minimum union of selected trie nodes for each demand subset, using bitwise OR for combined demands, adding a node exactly when its descendant is selected. Rootwise supersets are minimized by subset closure. Then enumerate every allocation of each of the 24 demands among eligible roots and minimize the sum. Distinct roots cannot share nonempty prefixes. All search and arithmetic are finite/exact; caching depends only on a root and its exact available key subset, not on a heuristic approximation.

The previously published C++17 implementation `scan_cached_radius3.cpp`, Python independent `VERIFY_RADIUS3_SELECTED.py`, frozen generator and case source are reused unchanged from EC49FMI/FM J evidence. **New complete executed exact block:** 1000–1999. Fresh independent Python trie/DP checks recomputed indices 1000→138, 1342→108, 1724→106 and 1999→138, matching the C++ solver. The local evidence package also preserves all 1,000 raw output lines, replay programs, inputs, logs, and per-file SHA256 manifest.

## Continue

Next uncomputed contiguous radius-three block begins at index 2000 and ends at 38168. Study exact cheaper candidates and reuse root-level subproblem certificates where helpful. The original global seven-key bound remains `C_min(7) ≤ 84`; this paper settles the explicitly indexed family, not the entire global minimum.

Formal Source status in this author contribution: no native EC49AS CLAIM/Result and no independent Driver admission have been obtained. Scientific model pins, P000, and ACTIVE worldview have not been changed.
