# EC49FNI: 500 exact seven-key BRC configurations and cardinality-envelope shadow-gap certificate

**Date:** 2026-11-13. **Scope:** author-side finite mathematical research, continuation of [EC49FNH / PR #2251](https://github.com/awdawmip/enterprise-math/pull/2251).

## Fixed scientific object and method

The frozen scientific input remains `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`: original nine-state BRC, 178,850 lawful operation words in 94 complete cache keys, and 24 demanded observation labels. The indexed radius-three three-replacement family contains 38,169 seven-key configurations. An admissible selection covers all 24 labels with original lawful words; its objective `C(K)` counts the distinct **nonempty ordered signed native-X6 microstep prefixes** across those words, keeping sign, microstep order, branch identity and provenance.

The exact solver groups available lawful words by their first native microstep, forms their prefix tries, computes each root's exact required-label-subset cover function by bottom-up integer DP, then exhaustively assigns each label to one admissible root and minimizes the sum of independent-root costs. Every chosen witness is an original lawful BRC word, giving a constructive matching upper bound. This is finite exact optimization under the frozen input, not a claim about an unrestricted or asymptotic optimum.

## EC49FNI computation: indices 27000 to 27499

There are **500 complete consecutive exact C++ output rows**, with no gaps, corresponding to `27000..27499`. The larger run was interrupted after these 500 rows; it lacks a final `FINISHED` line. Each row was emitted after completing that index's exact search. A separate single-index native C++17 run at the minimum returned `FINISHED` and exit 0. An independent Python native-trie/subset-DP calculation agreed at indices 27000, 27086 and 27499.

| Index | C++ exact | Independent Python |
| --- | ---: | ---: |
| 27000 | 112 | 112 |
| **27086** | **98** | **98** |
| 27499 | 138 | 138 |

The exact finite interval minimum is **98, uniquely at index 27086**, with complete cache keys `[0,4,5,11,26,34,49]`. Its independently reconstructed lawful 24-word witness has 49 distinct nonempty prefixes under native root 05 and 49 under root 06 (07 is unused); the trie-DP lower bound matches **98**. The maximum is **138**, occurring in 224 configurations (first at 27188). The compressed lossless cost vector and 24 original witness words are in `EXACT_DATA_EC49FNI.json`.

Contiguous author-side coverage now reaches indices `0..27499`, i.e. **27,500 / 38,169** cases. The earlier best within the scanned radius-three family remains 86 (21524/21525); the unrestricted seven-key mother problem separately has an 84-prefix feasible construction. Thus this interval adds a classification and a structural comparison, not a new global upper bound.

## Cardinality-envelope lemma and three exact shadow gaps

For each of `K=26955,26966,27086`, roots 05 and 06 have disjoint 12-label domains `L05,L06` covering all 24 labels. Root 07 may take a subset `T` of the same eight labels `Q={5,7,11,13,15,17,19,21}` (frozen label indices). Let `f_r(S)` be the exact root-trie required-label cover cost, including allowable incidental output labels. Define

```
B_K = f05(L05)+f06(L06)
S_K(T) = f05(L05)-f05(L05\T) + f06(L06)-f06(L06\T)
G_K(T) = f07(T)-S_K(T)
F_K(T) = B_K+G_K(T).
```

These equalities follow because distinct first-root prefix sets are disjoint and the only alternate root allocation is to send `T` to 07.

**Lemma (cardinality envelope).** Define `a_k=min_{|T|=k} f07(T)` and `b_k=max_{|T|=k} S_K(T)` for `k=1..8`. For every such `T`, `G_K(T)>=a_k-b_k`. Consequently a target gap `g` holds on all masks of cardinality `k` whenever `a_k-b_k>=g`. Only the remaining cardinalities need coupled exchange-mask comparison. This is a direct order inequality; no submodularity or port/provenance quotient is assumed.

For **both 26955 and 26966**, complete exact integer root tables give

```
k:          1  2  3  4  5  6  7  8
a_k-b_k:    8  8  7  8  8  7 10 12
```

Thus six cardinalities are proved by root-local envelopes, and only `C(8,3)+C(8,6)=56+28=84` coupled masks require direct comparison, instead of 255. Their exact minimum margin is 8. Computing the root-local envelopes still requires their own DP/size-wise extrema; this improvement counts *coupled mask comparisons*, not all root-function computations.

For the new index **27086**, replacing key `32→49` in 26955 raises the empty-transfer optimum `B` from **92 to 98**, but a fresh exact 256-mask computation yields the same strict exclusion margin

```
G_27086(empty)=0;
min_{nonempty T subset Q} G_27086(T)=8.
```

The same equality holds for 26955 and 26966. Therefore the optimum first-root allocation remains uniquely `T=empty` under this key replacement, although the optimal two-root cost rises by six; uniqueness of selected lawful *words* is not asserted. For 27086, the envelope margins are `[6,4,4,3,5,7,8,8]`, so the envelope shortcut certifies target margin 8 directly only at cardinalities 7 and 8. These statements concern exactly the three pinned finite configurations.

## Evidence, limitations and next question

A local full evidence package contains the unchanged frozen 9.3MB master input, 500 complete original C++ rows, C++17 solver, independent Python solver and successful selected-case logs, the 24-word witness with full native signed prefix paths, all 3 exact root tables and 256 transfer margins, the envelope inspector, a standalone certificate verifier and SHA256SUMS.

- Frozen master SHA256: `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`.
- Raw 500-row output SHA256: `0e0a6a77fc01c08e8430a8c479004c60f5fee463edebb09b1167499752005419`.
- Complete local JSON certificate SHA256: `ecd2ae0ea6c0d2fd2ce3c8f7ae9902888e30aad2d674d514202328bf49fbbdb5`.

The GitHub file `EXACT_DATA_EC49FNI.json` keeps the full cost vector and original witness in compact, directly decodable form; the user-delivered evidence archive carries the larger exact root-function tables and reproducibility input. The 500 rows do not have a final bulk-run completion receipt, and only 3 selected configurations were independently recomputed in Python. These provenance facts are part of the evidence, not grounds to discard the completed rows.

On this run the native `em_status` and `em_control_task(RS-EC49AS)` attempts returned `BACKEND_IDENTITY_CHECK_UNAVAILABLE` with `operation_sent=false`. No canonical current owner/CLAIM/Result could be verified or mutated. This PR is author-side research evidence, not a formal task claim or independent Driver mathematical acceptance.

**Next nonoverlapping radius-three index: 27500 (10,669 remain).** Further structural direction: derive less expensive root-local sufficient conditions for positive transfer margins and test stability under the substitutions `32→49` and `34→46`.
