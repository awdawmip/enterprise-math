# EC49FMR — Exact native BRC seven-key radius-three configurations 7000–7999

Date: 2026-11-12. Frozen scientific pin `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

The model and observer remain unchanged: nine-state signed-X6 BRC, 178,850 lawful operation words, 94 complete cache keys, 24 first/last observation labels, and the previously fixed lexicographic list of 38,169 coverable seven-key radius-three configurations. The objective `C(K)` is the minimum number of **distinct nonempty ordered signed-native X6 prefixes** among lawful witness words meeting all 24 labels, not the word count or unsigned displacement set size.

## Exact finite theorem and new construction

For the complete 1,000-member finite family `K_i, 7000 <= i <= 7999`:

`min C(K_i) = 110`, attained at indices **7145 and 7157** only, with maximum 138. The exact cost histogram is:

`110:2, 116:3, 118:2, 120:1, 122:49, 124:3, 126:2, 128:2, 130:94, 132:49, 134:1, 136:4, 137:44, 138:744`.

Of the 1,000 instances, 250 have three first-microstep root subtrees; 750 have four. All 1,000 native C++ output records were actually completed with uninterrupted case indices and a `FINISHED` receipt for each 500-case run. The exact byte-valued cost vector and SHA256 hashes are in [EXACT_VECTOR_EC49FMR.json](EXACT_VECTOR_EC49FMR.json).

A concrete 110-prefix witness for case **7145** is recorded in [WITNESS_7145_EC49FMR.json](WITNESS_7145_EC49FMR.json). Its seven full-key indices are `[0,4,5,19,36,43,46]`. The 24 operation words cover every required label; first signed-native roots 05, 06 and 07 contribute exactly 48, 44 and 18 distinct prefixes respectively, totaling 110. The finite optimizer gives the matching lower bound for that case.

The preceding author-side exact results for `0..6999` plus this calculation imply `min_{0<=i<=7999} C(K_i)=102`, with known attaining indices 32, 93 and 6589. The already constructed unrestricted legal seven-key 84-prefix solution continues to give `C_min(7)<=84`. These three claims refer to their respective exact domains.

## Why the integer optimizer is exact

For each chosen key set, form every full ordered signed-native prefix path of its lawful BRC words. Group them by first native microstep. For each resulting finite trie, a bottom-up min-plus dynamic program records the smallest number of charged nonempty trie vertices able to cover each set of observation labels. At a terminal, selecting the lawful word witnesses its terminal label. At an internal node, combine children's attainable masks and minimum costs, charging the current node exactly when a nonempty witness set is selected. Induction on the finite trie shows those costs are exact. The superset closure converts exact-mask costs into costs for covering **at least** a desired label subset. Assign all 24 demand labels to roots in which they occur and minimize the sum: different root subtrees share no nonempty prefix, and every lawful full witness belongs to one root. Exhaustive enumeration of assignments therefore gives the exact optimum `C(K)`. This proof is for the actual finite native catalogue and its specific observer, not a generic physical time-evolution assertion.

## Actual verification

The unchanged optimized C++17 solver `scan_cached_radius3.cpp` (SHA256 `6ea17ff267f599c69967b420ebf1a8abe151e587e57b25f599f8ecdfb9f2ecac`) was compiled `-O3 -std=c++17` and executed over `7000 7500` and `7500 8000` against the pinned complete input (SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`). The 1,000 concatenated original lines have SHA256 `613ba4a075d73808a69f8b6fc0e66113fafebea1c0d4ed3ef6b00bca8b476c1c`. Uncompressed cost vector SHA256: `5795f6e304043c617121e5ed374861062044e130e87164bca3ea72ffb26b2509`.

An independently implemented Python BRC path generator and separate native-prefix-trie optimizer were executed for case indices: 7000=138, 7145=110, 7157=110, 7500=138, 7558=128, 7572=128, 7999=138. The constructive certificate was also reconstructed directly from the frozen catalogue and checked with the [verification script](VERIFY_EC49FMR.py). A complete local tar.xz evidence archive additionally preserves the original input, C++ solver, exact 1,000 native rows, source generator, independent check code, run logs, witness reconstruction, and SHA256 manifest.

## Continuing frontier

Next continuous radius-three range starts at index **8000**; 30,169 coverable configurations remain. A different useful research route is a cross-key reusable native-prefix lower-bound certificate or an unrestricted valid `<=83`-prefix seven-key construction. P000, ACTIVE worldview, frozen science, authorship and formal review/admission controls are unchanged. This is author-side mathematics pending independent Driver review and separate formal task/CLAIM binding.
