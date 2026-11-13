# EC49FNC — 1,000 exact native BRC radius-three cases and a nonseparable key-interaction witness

Date: 2026-11-13. Role: author-side TASK_RESEARCH, not formal Task/Result acceptance. This continues EC49FNB ([PR #2226](https://github.com/awdawmip/enterprise-math/pull/2226)) without modifying its frozen science or previous evidence. Pinned input: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Source: nine-state original BRC, 178,850 legal original operation words, 94 complete cache keys, 24 observation labels, 38,169 ordered seven-key radius-three configurations. An operation path is a sequence of signed native six-axis microsteps; the cost `C(K)` counts *distinct nonempty ordered signed native path prefixes* in the union of one legal word selected per observation label.

## 1. Exact finite computation

For all configurations `18000 <= i <= 18999`, the original C++17 prefix-trie/subset optimizer computed 1,000 consecutive cost records. The minimum is **98**, attained at precisely indices **18111, 18123, 18383, 18656, 18668**; the maximum is **220**, at **18968**. There are 93 distinct observed costs. The contiguous completed radius-three family is now **19,000 / 38,169 (49.78%)**. Across the completed 0–18999 prefix, the best remains 96 at case 17965; the separately known unrestricted seven-key parent upper bound remains 84.

The complete 1,000-byte exact cost vector is in `EXACT_VECTOR_EC49FNC.json` (zlib/base85, one uint8 per case in ascending index order), together with the source C++ output SHA256, vector SHA256 and finite-range statistics. Raw uncompressed C++ output has exactly 1,000 rows and SHA256 `02b52c66d6c7799349bd9c1376e938f177b083a2184c0c65cf77c13df0f79dfe`; the cost-vector bytes SHA256 is `c804e0ea01543a6b91bcd2f96e1abbac1eadcc6a0eb005661033c436d03bba2f`. The frozen full input `master_and_radius3_cases.txt` from the previous evidence archive has SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.

Reproduce the full data from the frozen input and the original `scan_cached_radius3.cpp` (also preserved in the preceding EC49FNB evidence): `g++ -O3 -std=c++17 scan_cached_radius3.cpp -o scan; ./scan 18000 19000 < master_and_radius3_cases.txt > results.txt`. The original scan for 18000–18999 was interrupted after 700 completed rows and resumed for 18700–18999; only the 700 + 300 contiguous complete output rows are counted. Intermediate partial output was not treated as an exact completed 1,000-run execution, while every configuration has its own completed solver record. An independent Python prefix-trie optimizer was run on the selected new cases 18111, 18123, 18383, 18656 and 18668, and on relevant preceding cases listed below. All reported selected costs matched the C++ solver. The five minimum cases have separately reconstructed 24-word legal operation witnesses, each with 49 + 49 distinct nonempty prefixes for roots 05 and 06; the third available root is not used.

### Exactness argument

For a fixed configuration `K`, group permitted words by their first native signed microstep and build a prefix trie for each root. Each trie node stores terminal observation labels. A bottom-up integer dynamic program tabulates the minimum count of nonempty prefix nodes that can realize a given subset of labels, combining disjoint child subtrees and charging the current node exactly once if selected. After superset-closure this gives `f_r(S)`, the exact least cost to cover all labels in required set `S` using root `r`. Enumerate every assignment of all 24 observation labels to an eligible root; its cost is `sum_r f_r(S_r)`. Every legal solution induces such an assignment and subtree; conversely, each selected minimum DP state reconstructs legal words with the counted prefix union. Thus the finite DP provides matching lower and constructive upper bounds. This argument applies to this frozen finite catalogue and the declared exact prefix observer.

## 2. New finite structural counterexample: key contributions do not separate additively

Fix four keys `B0={0,4,5,11}`. Choose one key `a` from `{1,6,7}` and one two-key pair `b` from `{(14,26),(32,49),(34,49)}`. All nine seven-key configurations `B0 union {a} union b` occur in the original 38,169-case catalogue:

| a \\ b | (14,26) | (32,49) | (34,49) |
|---|---:|---:|---:|
| 1 | 98 (#16807) | 98 (#16953) | 98 (#16965) |
| 6 | **96 (#17965)** | 98 (#18111) | 98 (#18123) |
| 7 | 98 (#18383) | 98 (#18656) | 98 (#18668) |

These nine costs were recomputed using one selected-case C++ exact run from the unchanged frozen input; eight also passed separately implemented Python DP in this turn (16807,16953,17965,18111,18123,18383,18656,18668). Previous EC49FNA had independently verified 16965 at 98. For each of the eight new/previous independently checked cases, the selected C++ optimum agrees exactly.

**Proposition (finite nonseparability).** Within this fixed nine-configuration subfamily, no functions `u(a)` and `v(b)` satisfy `C(B0 union {a} union b)=u(a)+v(b)` for every listed `a,b`.

**Proof.** Any additively separable function has vanishing rectangular mixed difference. However, taking `a=6,1` and `b=(14,26),(32,49)` yields
`C(6,(14,26))-C(1,(14,26))-C(6,(32,49))+C(1,(32,49))=96-98-98+98=-2 != 0`.
Thus the stated additive representation is impossible. Both used roots decrease from 49 to 48 for `(14,26)` when key 1 is replaced by key 6, but neither improves for `(32,49)`. The pair/key interaction therefore influences exact optimized native prefix sharing. This is a rigorous finite counterexample to the additive ansatz under the frozen model; it motivates examination of root-interface coupling and shared subtree certificates.

## 3. Persistence, verification scope and next research

The output costs are exact integer DP results, with five direct 24-word reconstruction checks and the stated selected independent Python recalculations. The 1,000-row vector is complete for the declared interval; the wider 38,169 configurations are not yet exhausted. Reuse the original scientific pin. This report and compressed vector are author-side evidence, not a native CLAIM, Result, review, Working Truth or Foundation promotion.

Next contiguous exact configuration is **19000** (19,169 remaining). Investigate a general criterion for the nonzero mixed-difference interaction in terms of `f_{05}` and `f_{06}` and whether a reusable local certificate predicts which pair choices allow both roots to improve simultaneously. Preserve root identity and ordered prefix provenance before compression.

Source chain: EC49FNB PR #2226 and its frozen evidence archive; project P000 and native X6 rules; current project continuation and research protocols. Independent mathematical Driver audit remains a separate task.
