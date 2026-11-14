# EC49FMD — 338 further radius-two seven-key native-prefix minima

Date: 2026-11-12. Status: author-side finite exact computation; not an independently admitted Result.

## Statement and scientific input

Continue the frozen nine-state BRC model `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`, retaining 178,850 legal words, 94 *complete* cache keys, 24 (window,DFA-signature) observation demands and ordered signed X6 microstep prefixes. The cost `C(K)` is the minimum number of **distinct nonempty native prefixes** in any collection of legal words satisfying all 24 demands, with every selected word having a raw key in the seven-element set `K`.

Let the EC49FKX baseline be
`S={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`.
The 87 other raw keys form `O`. Enumerate all 21 dropped pairs of `S` in increasing tuple order and, inside each, all 3,741 added pairs of `O` in increasing tuple order. Keep an instance if the bitwise union of the seven raw-key demand supports covers all 24 demands. This produces 6,315 feasible radius-two keysets. This ordering agrees exactly with the previously persisted EC49FKZ indices 0 through 399.

**New finite result.** For the 338 feasible radius-two keysets with zero-based global indices `400..737`, all exact prefix-tree minima lie in `[98,184]`; the minimum 98 occurs only at global indices **588** and **673**. Thus this entire 338-instance family has no 84-prefix or lower construction.

The cost histogram is stored in `EXACT_VECTOR_EC49FMD.json` alongside all 338 per-instance (local_index, optimum, root-assignment multiplicity, number_of_roots) records in losslessly compressed form; the raw row text SHA256 is `22fb8ff030f057a6876351141d32b2068b0acebfb0de921928367d2649904946`.

## Why the finite algorithm is exact

For a fixed K, include **every** legal word whose complete raw key belongs to K. Split the ordered, signed six-axis prefix trie by the first signed microstep. Within each root subtree, define an integer DP state for every subset of demand labels and store the minimal number of selected nonempty prefixes. At a terminal node, a word's demand can be covered at that node; child contributions combine by bitwise subset union and addition; a nonempty selected node adds cost one. By induction on trie height, this DP gives the minimum prefix count for every demand subset supported by that root. First-step root subtrees share no nonempty prefixes. Enumerating every admissible assignment of all 24 demands to roots and summing root minima is therefore exact.

The *same unmodified* C++17 engine `EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp` was used. The frozen catalogue and signed-prefix generator are `EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py`. The run actually completed all 338 cases sequentially, with no heuristic cutoff inside a case; a subsequent uncompleted case (index 738) was excluded from this result. Record integrity, contiguous indices, demand support and exact cost histogram were checked. A separately implemented Python standard-library prefix-trie/subset-DP independently recalculated global instances **588=98, 673=98 and 404=112**, agreeing with C++.

## Reproduction

Run `python REPLAY_EC49FMD.py` from this directory for complete frozen catalogue generation, all 6,315 radius-two support-coverability indices and stored evidence integrity. Run `python REPLAY_EC49FMD.py --run-all` to compile the original C++17 solver (g++) and independently recompute all 338 records, comparing their exact integer tuples and root-count fields against the persisted vector. The Python independent verifier for the three checked instances is available in the turn-local evidence bundle.

## Scope and next question

Earlier EC49FKZ exactly solved the first 400 globally ordered coverable radius-two cases. This study supplies the next **338**, so the contiguous author-side exact frontier advances to global index **737**, a total of 738 of 6,315 coverable radius-two instances. The remaining 5,577 radius-two instances, radius-three/radius-four feasible families and the all-seven-key global minimum remain open. The known 84-prefix construction gives `C_min(7) <= 84`. Resume at radius-two global index **738**, reusing the same generator and solver without replaying indices 0..737, or compare a lower-cost targeted neighbor. An algorithmic lower bound or new <=83 construction remains a useful independent route.

## Provenance, identity and admission

Source research PR #1730; this author's GitHub actor `awdawmip`. The current native session-start call returned `SESSION_ISSUANCE_QUOTA`, and an EC49AS exact task publication lookup returned `NO_CURRENT_IMMUTABLE_PUBLICATION`. No unrelated active owner was claimed, no native CLAIM/Result/Driver acceptance was asserted, and this author-side publication preserves its exact computation/provenance only. P000 and frozen model semantics were not changed.
