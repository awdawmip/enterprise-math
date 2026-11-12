# EC49FMH — Complete exact radius-two seven-key signed-X6 prefix optimization

Date: 2026-11-12. Author-side finite mathematical evidence; Source task CLAIM/Result and independent Driver mathematical admission remain separate and pending.

## Frozen problem and exact theorem

Frozen nine-state BRC scientific pin: `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. The generator has 178,850 lawful operation words, 94 **complete raw cache keys**, 24 required observation labels, and the original ordered signed-X6 native microsteps. A word's cost contribution is the set of its nonempty raw microstep prefixes, not the abstract operation-word prefixes and not unsigned/coarse coordinate traces.

Let `K*` be the seven-key 84-prefix witness set
`{(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`.
For any seven-key set `K`, let `C(K)` be the minimum cardinality of the **union** of all nonempty native signed-X6 prefixes of a selection of legal operation words from keys in `K` covering each of the 24 frozen observations.

Define the exact radius-two neighborhood `N_2(K*) = {K: |K|=7, |K\K*|=|K*\K|<=2}`. Then

**THEOREM EC49FMH:**
```
min_{K in N_2(K*)} C(K) = 84.
```

The radius-two shell contains exactly `C(7,2) C(87,2)=78,561` seven-key sets. Exact 24-demand support excludes 72,246. The remaining 6,315 have each now been solved to full optimality by the integer signed-native prefix-tree / demand-subset DP. The 6,315 have minimum 84, achieved at global lexicographic coverable index 5883. Previous EC49FKY independently established the unchanged-base and radius-one minimum of 84. Hence the closed radius-two neighborhood has optimum 84. This is a **local radius-two theorem**, not an unrestricted global seven-key minimum theorem: the unrestricted mother objective retains the known upper bound `C_min(7) <= 84` and its radius-three/four obligations.

## New finite increment and a second 84-prefix witness

EC49FMG completed contiguous exact two-key cases 0..1619. This run finished **all 4,695 previously unfinished support-coverable cases indexed 1620..6314 inclusive**. Costs are integers in [84,204]. Exactly one of these cases costs 84, global #5883; the next smallest costs are 86 at #2473 and #4515. Lossless 4,695-byte cost vector, histogram, full explicit #5883 word witness and exact input/check provenance are in `EXACT_VECTOR_EC49FMH.json`.

For #5883 the full cache key set is
`{(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(6,3,1),(7,3,1)}`.
The 24-word witness in the adjacent JSON is lawful under these keys, covers the exact 24 labels in increasing order, and has an ordered **signed native-prefix union of 84**. Its two active first-step native subtrees each contribute 42 prefixes. In contrast with the baseline, two full keys are replaced; this is an independently checkable second radius-two configuration with optimum 84.

## Exhaustive computation and independent checks

All 4,695 input configurations were generated in the same lexicographic drop-two/add-two support-feasible enumeration as EC49FKZ. The native prefix optimizer groups the complete legal-word catalogue by first **signed** microstep, builds its prefix trees and exhaustively optimizes exact demand masks with integer min-plus child convolution and superset relaxation. For each root, subtree induction shows every legal selection is represented and every computed mask has a realizing legal selection; disjoint first-step roots make the final allocation additive. Thus the integer result is an exact finite theorem in the pinned model, with no floating numerical tolerance.

Frozen master input SHA256 `8db9447f5d9ad52e9cc919f2418a629eb0b0f7250b7acec93357ddc215d033ab` (same master as EC49FMG). Unmodified cached C++ engine SHA256 `8639af8a3c72f3dd38690fd0a537124a4a10f84478efc3e1595d78c39ca0219e`. Five completed no-gap batch logs cover 1620..1920, 1920..3000, 3000..4200, 4200..5200 and 5200..6315. The 4,695 raw cost-byte vector SHA256 is `c593055598ffd8140f4f28f43e8e8e0a40e1165f8215866757c2fba9b1fe49fc`.

A separate **original unmodified C++ solver** recomputed 21 chosen cases (including all small-cost anomalies and boundary cases): 1620,1687,1920,2473,2484,2999,3000,3176,3188,4199,4200,4419,4515,4712,5199,5200,5541,5755,5883,6183,6314. Every cost agrees with the cached implementation. An independently written Python standard-library signed-native prefix-trie DP also recomputed cases 1620,2473,3176,4515,5883,6183,6314, returning respectively 112,86,111,86,84,204,194. Independent traceback rebuilt and verified the 24 legal words and the 84-prefix union for #5883. See accompanying `REPLAY_EC49FMH.py`; full executed raw logs, frozen master input and independent-check logs are retained in the separate author evidence archive.

## Reproduction and provenance

The underlying frozen generator is sibling `EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`. Original exact C++ signed-prefix program is sibling `EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp`; cached integer engine source is included in the supporting evidence package. `REPLAY_EC49FMH.py` checks the compression, vector hash, exact support indexing, full frozen catalogue and explicit native-word witness; optional full original C++ recomputation may be performed from the same source/master with no scientific repin.

The research Author's real native session was registered this turn as Researcher `EM-DIRECT-26222F`, Activity `RA-E4AB22F16C16CF973C528AD8`; publication/control status remains author-side because the exact EC49AS native task lookup returned `NO_CURRENT_IMMUTABLE_PUBLICATION`. No unrelated owner/CLAIM was adopted. PR branch material is durable but remains unmerged. Mathematical admission requires independent Driver evaluation.

**Next discriminating unit:** prioritize the 38,169 support-coverable **radius-three** (three-key replacement) and 62,620 support-coverable **radius-four** configurations, using exact signed-native-prefix lower bounds/screening, branch and bound, and a search for an 83-or-lower legal construction. Reuse exact radius-zero/one/two and radius-five results without replay.
