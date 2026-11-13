# EC49FNM — exact BRC radius-three seven-key cases 31505–31999; sharp 27-case allocation-gap split

**Date:** 2026-11-13. **Status:** author-side exact finite research, not native CLAIM/Result or Driver review. **Frozen science:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab` (unchanged). **Nearest earlier research:** [EC49FNL PR #2282](https://github.com/awdawmip/enterprise-math/pull/2282), which completed 30500–31499; [EC49FNMA PR #2294](https://github.com/awdawmip/enterprise-math/pull/2294), exact 31502–31504. This report covers a disjoint, subsequently computed interval. Do not re-count FNL’s 220-case replication as extra coverage.

## Frozen mathematical instance

Use the original nine-state BRC transition grammar and 178,850 lawful words, **94 complete cache keys**, 24 observation labels and ordered, signed native-X6 microsteps, with distinct nonempty native prefixes as the objective. The indexed family contains 38,169 radius-three seven-key configurations. This is not an asymptotic complexity theorem or a full-world X6 dynamics claim.

The exact input file `master_and_radius3_cases.txt` used by the inherited C++17 optimizer has SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`. The source solver `scan_cached_radius3.cpp`, original-catalogue generator `EC49FGW_RADIUS5_SCREEN.py`, original words `EC49FGJ_SEVEN_KEY_94_WITNESSES.json`, and indexed configurations `cases.json` are preserved in the complete local evidence bundle; they are reused from the prior immutable FNL-science package. No science pin was changed.

## Exact finite calculation

Three independent complete C++17 command invocations, ranges `[31505,31600)`, `[31600,31900)` and `[31900,32000)`, returned `FINISHED` and 95 + 300 + 100 = **495 uninterrupted unique case lines**. The concatenated original text SHA256 is `51e1675165e68ef7fba7be9fa1b01d25540163cc1c517c2cc92e935dec5e061b`.

```text
min_{31505 <= i <= 31999} C(K_i) = 108
max_{31505 <= i <= 31999} C(K_i) = 196
{i : C(K_i)=108} = {31505,31506,...,31531}  (exactly 27)
```

All 27 minimizers have the same **unique optimal root-demand assignment**, sending all 12 labels available at first root 05 to 05 and all complementary 12 labels to 06; roots 03 (when present) and 07 receive none. The optimum is `54+54=108` for all 27 despite changing cache keys and available prefix trees. Here uniqueness is about the *allocation of the 24 labels to first roots*, not necessarily uniqueness of the 24 underlying lawful operation words.

For representative cases:

| index | seven key indices | global minimum | second distinct root allocation cost |
| --- | --- | ---: | ---: |
| 31505 | `[0,4,5,11,34,61,67]` | 108 | 116 |
| 31516 | `[0,4,5,11,34,61,78]` | 108 | **115** |
| 31531 | `[0,4,5,11,34,61,93]` | 108 | 116 |

More precisely, if `A_i` is the finite set of assignments of each label to one of its lawful first roots, `a_i^*` denotes the unique optimum, and `F_i(a)` the exact total prefix count after independently minimizing within each root, then

```text
F_i(a_i*)=108 for all 31505 <= i <= 31531;
min_{a in A_i\{a_i*}} F_i(a) = 115 if i=31516, else 116.
```

This is a **sharp exact finite counterexample** to the implication “equal global optimum implies equal root-assignment stability gap”, already for configurations differing in a single cache key (67→78). No universal gap-stability assertion is made.

**Sharp competing allocations, recorded in the full evidence package.** For 31505 the second-best root-demand masks are `03:0,05:4095,06:2743,07:170`; the exact per-root contributions are `0+54+37+25=116`. Root 07 receives exactly `{(4,8),(6,8),(7,8),(8,8)}`, formerly assigned to 06. For 31516 the second-best masks are `05:3419,06:4095,07:85`, giving `36+54+25=115`; root 07 receives `{(4,2),(6,2),(7,2),(8,2)}`, formerly assigned to 05. Both alternatives make root 07 cost 25, but the removal saves 17 from root 06 in 31505 and 18 from root 05 in 31516, explaining the one-prefix gap difference. All masks are indexed in each root's sorted *original* label list; the bits are not axes or abstract coordinate substitutions.

## Why the search is exact

For each complete-cache-key configuration K, collect its frozen lawful operation words by their first signed native microstep r. For each root, construct a prefix trie **over the original ordered signed microsteps**. At a trie node, a DP indexed by the exact subset of observed labels computes the minimum selected nonempty-prefix count in that subtree. Child unions add costs; choosing any nonempty subtree adds its current prefix node, while the virtual trie root adds zero. A word terminal can satisfy its original observation label. Superset downward relaxation yields `f_r(S)`: the least root prefix count covering all labels required in S, *permitting incidental coverage of further labels*. Then enumerate every lawful function `a:labels→eligible first root` and compute

```text
C(K) = min_a sum_r f_r(a^{-1}(r)).
```

The roots have disjoint first-prefix bytes, so their nonempty-prefix counts add exactly. Every legal selected word family induces an admissible root allocation; conversely root DP witnesses combine into a legal 24-label cover. This provides matching finite lower and upper bounds. Tracking the two distinct minimum assignment costs yields the sharp second-allocation certificate above. It is essential not to replace the original ordered signed paths with net six-axis coordinates or to discard word identity.

## Verification and evidence scope

- The stored compressed certificate `EXACT_CERTIFICATE_EC49FNM.json.xz.b64` contains **every one of the 495 minimum costs**, the exact number of globally optimal root allocations per case, 27 distinct second-assignment values, and 24 original legal words for each of cases 31505 and 31516. It binds the frozen input and complete output SHA256.
- Both 24-word witnesses were freshly reconstructed and checked against all 178,850 lawful original catalogue words and their complete seven keys. Each realizes exactly 108 different nonempty signed-native prefixes.
- A separately authored Python prefix-trie/subset DP recomputed four cases independently of C++: `31505→108`, `31531→108`, `31650→141`, `31999→134`. The other 491 cases have exact original C++ enumeration and certificate checks, not separate Python recomputation.
- `VERIFY_EC49FNM.py` checks the compressed certificate, frozen master input, all 495 rows, the 27 sharp second costs, and both original lawful witnesses. To reproduce all optimum values, compile and run the pinned `scan_cached_radius3.cpp` with this exact master input, split at the same three intervals, and compare the resulting rows with the certificate; the local complete bundle contains all source files, raw outputs, logs, independent verifier and hashes.

A complete reconstructable evidence archive was produced locally; the GitHub note and compact certificate are persistent author-side research artifacts. Original frozen sources and historical proofs remain at their existing pins. Neither the GitHub branch nor this report claims formally accepted mathematical status.

## Frontier

**Boundary closure checked separately:** cases 31500 and 31501 were also computed on the same frozen input, each with exact optimum 108 and a unique optimal root allocation. The native solver emitted FINISHED for both, and an independent Python trie/subset DP returned 108 in both cases. They are a two-case bridge, **not counted among the 495 cases** covered by the compact certificate; cases 31502–31504 are supplied by prior PR #2294. Thus, combining prior 0–31499 coverage, these verified bridge cases, PR #2294 and the 495 new cases closes the continuous index coverage through **31999** (32,000 of 38,169), with distinct evidence provenance for each segment. The next unsolved consecutive index in this author-side lane is **32000**, leaving 6,169 cases. A useful structural next question is to characterize which cache-key substitutions preserve `C(K)=108` while changing the second-best root allocation by exactly one, and whether a smaller root-function inequality certificate can determine that gap without full assignment enumeration.

**Native control:** An exact read-only lookup of `RS-EC49AS` was submitted under request `ec49fnm-taskcheck-20261113-01`; receipt remained `QUEUED` at the time of this report. No current winning CLAIM, formal Result, or Driver mathematical review is asserted.
