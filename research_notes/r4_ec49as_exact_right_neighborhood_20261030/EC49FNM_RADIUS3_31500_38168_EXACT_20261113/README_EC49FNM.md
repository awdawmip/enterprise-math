# EC49FNM — final 6,669 configurations of the radius-three signed-BRC seven-key family

2026-11-13 · Author-side mathematical evidence · Scientific freeze `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`

## Exact finite result

Use the original nine-state BRC, all 178,850 legal native words, 94 complete cache keys, 24 distinguished observations and the original signed ordered X6 native microsteps. Let `K_i` be configuration `i` in the original fixed enumeration of 38,169 seven-key radius-three configurations. Let `C(K_i)` be the exact minimum number of distinct **nonempty, ordered, signed native microstep prefixes** of lawful words covering all 24 observations with allowed complete keys.

**Theorem (exhaustive final segment).**

```
min {C(K_i) : 31500 <= i <= 38168} = 106,
unique minimizer: i = 31503.
max {C(K_i) : 31500 <= i <= 38168} = 234,
unique maximizer: i = 34796.
```

The final index 38168 has cost 202. No index in this final 6,669-case segment has cost 105 or below. The six cases independently recomputed by a separate Python root-trie/subset exact solver are:

| Global index | Original C++ | Independent Python |
| ---: | ---: | ---: |
| 31503 | 106 | 106 |
| 32770 | 150 | 150 |
| 34796 | 234 | 234 |
| 36000 | 138 | 138 |
| 37210 | 152 | 152 |
| 38168 | 202 | 202 |

Both extreme configurations are **in the stated finite frozen 38,169-item enumeration**; these are not optima over unrestricted seven-key subsets. The frozen generator retains complete signed ordered microstep provenance, and cost is not a scalar readout of a single coarse path.

## Proof

For each fixed allowed key set, construct the rooted trie separately for every eligible first signed native microstep. Mark each original lawful word's full ordered native path and its original demand label. At each node, compute the exact integer dynamic program for all achievable unions of terminal demand masks, adding one to each nonempty child's prefix union. Take superset closure to obtain each root's minimum-prefix cost function. Distinct first-root subtries have disjoint nonempty native prefixes, so exhaustive assignment of each demanded label to its eligible root and minimization of the sum of these exact functions gives precisely `C(K_i)`. No approximation or heuristic pruning enters these calculations.

This exact finite algorithm was applied at every integer `i` from 31500 through 38168, partitioned into **67 disjoint native C++17 runs** of 100 consecutive indices except the last 69. Each reported `FINISHED` and produced an output record. All 6,669 records were joined by numerical case index; each integer occurred exactly once, without gaps, and the complete raw output was verified with SHA256 `d810517c052b6e42b13c819302f55f7d8f387cc80c5daaa916cddaa8420b2429`. The entire lossless integer cost vector is in `EXACT_CERTIFICATE_EC49FNM.json`; `VERIFY_EC49FNM.py` reconstructs it, checks every index and both extrema, and optionally checks the raw native logs and frozen input bytes.

This is an exact exhaustive proof for the defined finite input set conditional on the faithful implementation of the specified rooted-trie recurrence. The independent Python recalculations on the six declared inputs are implementation crosschecks; they do not by themselves verify all 6,669 individual C++ executions. Preservation of native input, full raw result, source, and every completed run receipt makes the finite enumeration reproducible.

## Continuation and family-level interpretation

Previous independently saved author-side intervals include PR #2278 for indices 28500–30499 and PR #2282 for 30500–31499; PR #2282 proves its segment minimum 94 and two distinct configurations with identical 8,448-entry root cost profiles. Earlier work records consecutive coverage through 28499, including an 86-prefix configuration within the 0–30499 segment. By combining *all earlier declared consecutive segment calculations with the presently completed final 6,669*, the total enumerated index coverage reaches **38,169/38,169**; the previously reported minimum **86** remains unchanged by the last 7,669 cases. A single independently stitched 0–38168 master-vector audit is a separate useful consolidation task before labeling the full-family 86 minimum as a newly independent whole-family certificate. This does not affect the exact theorem for 31500–38168 proven above.

The unrestricted mother objective over any choice of seven complete keys is separate. Its previously known 84-prefix **feasible upper bound** persists. This radius-three family is one defined finite subfamily and does not settle the unrestricted minimum.

**Frozen input integrity.** Scientific source commit `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, original master input SHA256 `cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e`, cases enumerator SHA256 `d18c8f3177083c5b39ef6c8ca068589042617a2a797b53f98818a427040e4f33`. Same original C++17 exact scanner used by earlier EC49FNK/FNL; input generated once and reused.

**Research admission and ownership.** Real own research identity from this research turn: `EM-DIRECT-8FECDD`, Source Activity `RA-31D3AD635CC0BECE8E6F3BFC`. Exact task lookup `RS-EC49AS` returned `NO_CANONICAL_PUBLICATION_DIRECTORY`, observed 2026-11-13 09:34:00 UTC at Source `75096238fce46c44d4a0c39da4a35e7fa9a1e34d`; therefore the present science is persisted author-side, NOT_REVIEWED, and no formal CLAIM, Result or independent Driver mathematical acceptance is asserted.

**Next mathematically discriminating work.** Check whether all case-cost vectors from prior published intervals can be stitched into one verified 38,169-value vector; then pursue the root-cost profile substitution criterion evidenced in EC49FNL and search beyond the fixed radius-three shell for a legal seven-key construction with cost ≤83 (or a stronger unrestricted lower bound).
