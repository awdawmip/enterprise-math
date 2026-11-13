# EC49FMT — BRC seven-key radius-three exact optimization, cases 10000–11399

Date: 2026-11-13. Status: AUTHOR-SIDE EXACT FINITE COMPUTATION, UNREVIEWED. Frozen scientific input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.

## Exact proposition and quantified domain

With the frozen nine-state BRC word automaton, 178,850 lawful operation words, 94 complete keys, 24 observations, and ordered signed-native X6 prefixes, let `C(K_i)` count the fewest distinct nonempty prefix microstep paths needed to cover every label using only seven keys from deterministic coverable radius-three configuration `i`.

For every integer index `10000 <= i <= 11399` (exactly 1,400 configurations), full C++17 root-trie/min-plus label-subset optimization gives **minimum 102**, uniquely at **11121**, and **maximum 205**, attained at **10864 and 10909**. There are 213 configurations with three available first-step roots and 1,187 with four. `EXACT_VECTOR_EC49FMT.json` stores all 1,400 exact integer costs losslessly as zlib/base64 uint8; SHA256 protects the decompressed vector, and the full original 1,400-row output is identified by SHA256.

Combining the predecessor 0–9999 exact window gives **minimum 102 across completed contiguous indices 0–11399**. The previously constructed unrestricted seven-key 84-prefix witness still gives `C_min(7) <= 84`.

## Finite exactness and sharp witness

The pinned original `scan_cached_radius3.cpp` computes per-root prefix-tree integer DP: states are masks of covered labels; children compose by min-plus mask union, terminal labels may be selected, and every used nonempty trie node costs one. Tree-height induction proves the per-root optimum. Assigning all 24 labels to every capable first-step root and exhaustively evaluating assignments proves the global optimum for each selected seven-key configuration; distinct first-step roots have disjoint prefix sets. This proof is scoped to the 1,400 enumerated cases and the pinned frozen catalogue.

`WITNESS_11121_EC49FMT.json` contains 24 actual legal BRC operation words, one for each labelled observation, using the seven keys `[0,4,5,6,14,24,26]`. Ordered signed-native prefixes split as root `05:46`, `06:44`, `07:12`, totaling **102**, matching the exact DP lower bound. Frozen-generator validation checks legal word membership, target labels, key membership, native ordered prefix count and roots.

A separately implemented Python prefix-trie solver reoptimized `10000=162`, `11121=102`, `11274=104`, `11399=126` without calling the C++ solver or reusing its cost vector. The complete 1,400-case C++ outputs and independent checks are in the companion full archive.

## Source and complete-run boundary

Upstream frozen source is byte-identical to [EC49FMS PR #2191](https://github.com/awdawmip/enterprise-math/pull/2191) at `648fb02c9e16393b40dfb2471171a67ca3139a14`; original source SHA256 `6ea17ff267f599c69967b420ebf1a8abe151e587e57b25f599f8ecdfb9f2ecac`, original frozen catalogue SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. The 10000–10499 run completed. The subsequent 10500–11999 run was interrupted **after** flushing 900 completed rows 10500–11399; rows 11400 onward are **not** claimed. Reproduce the exact target range by running `g++ -O3 -std=c++17 scan_cached_radius3.cpp -o scan && ./scan 10000 11400 < master_and_radius3_cases.txt`.

The author-side research is durable here. The current RS-EC49AS task/native session checks were queued during this computation, so this file asserts neither a formal CLAIM, Result nor an independent Driver decision.

Next contiguous exact input: **11400** (remaining 26,769 of 38,169 configurations). Additional scientific questions: classify the two cost-205 cases, find reusable cross-configuration lower-bound certificates, or a lawful unrestricted <=83-prefix construction, retaining native signed order and source provenance.
