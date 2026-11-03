# EC49EXV — Resolve all 18 EC49EXU timed-out H8/M5 signed-X6 cases by exact H7 prefix certificates

**Research date:** 2026-11-04 Asia/Shanghai. **Status:** AUTHOR-SIDE FINITE EXACT THRESHOLD CERTIFICATE / PORTABLE DRAFT / UNREVIEWED / NOT_ADMITTED. **Parent:** EC49EXU in Draft PR #1730. **Frozen scientific pins (unchanged):** Global `773d538180bfb49e24cffeb35c3ee75eb0628e2e`, Enterprise Math `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. P000 and ACTIVE worldview remain unchanged; current normative behavioral rules are separately read from canonical main.

## Exact finite theorem EC49EXV-1

All **18** original EC49EXS three-cache-collision schedules that timed out in EC49EXU satisfy **E_min(x) ≥ 80**. Original zero-based EXS catalogue indices:

`663,676,678,589,601,661,674,583,592,604,606,652,662,675,677,590,660,673`.

For each schedule, the complete legal signed-native six-axis operation-word prefix trie for horizons **h=2,...,7**, including all four T4 observer signatures at each h=2,...,6 and both T2 signatures at h=7, has **exact minimum cost E7≥76**, certified by the existing EC49EXJ exact integer OR-mask DP under full-cost cutoff 76. Every case has 22 mandatory observer colors, 28 prepaid h2 prefix edges, and 2582 or 2668 h7 trie nodes.

Here the signed primitive-step words follow the frozen 7-operation language, maintain complete six-component positive BRC keys, and apply the original nine-history observer map. For all 18 schedules the exact key formula `L(K)=2(u+v+w-1)` gives **all h≤7 primitive lengths ≤16** and **h8 primitive length exactly 18**, with h8 necessarily requiring two distinct observer signatures. The proven EC49EXQ same-full-BRC-key prefix theorem yields LCP≤18−3=15 for two distinct h8 legal words. Thus these paths have distinct edges at depths 17 and 18, none of which belongs to any h≤7 word. Therefore **E8≥E7+2·2≥76+4=80**. This independently derives the exact h8 increment for this finite class from checked lengths and the native LCP theorem.

The 18 full schedules have only **12 distinct serialized h7 trie input instances** (exact byte equality including topology, signed-step-induced prefix sharing, prepaid edges and terminal color bits). Equivalent h7 index pairs: `(663,662)`, `(676,675)`, `(678,677)`, `(589,590)`, `(661,660)`, `(674,673)`. All 12 input SHA256 hashes have recorded exact DP `BOUND_PASS minimum_total_at_least=76` outputs. Duplication follows from identical h2..7 key/observer schedules and different h8 keys; no heuristic equivalence was used.

## Exact execution and verification coverage

The local standalone Python generator faithfully implements the EC49EXJ `SCREEN_H5_EC49EXJ.py` frozen `native`, `sig`, `words`, and `build_input` logic, applied to the 18 exact EXS catalogue rows. The original EC49EXJ C++17 OR-mask integer DP algorithm was then compiled and executed at cutoff 76. 18 calls succeeded, with 12 unique SHA256 input texts; all reported the required `BOUND_PASS`. The attached `EC49EXV_H7_EXECUTED.json` records all indices, node counts, exact input digests, and output strings. `VERIFY_EC49EXV.py` is a source-level reproducer that reuses the *unchanged original* same-PR sibling generator and solver; the reproducer is provided for direct checkout execution, while the 18 actual computations used the equivalent standalone generator.

The OR-mask DP's local value at any trie node equals the minimum number of additional non-prepaid signed primitive edges necessary to realize each reachable union mask in its subtree. It combines disjoint child subtrees by mask OR and nonnegative integer cost summation. Induction yields exactness. With 28 prepaid h2 edges, cutoff 76 discards states with extra cost ≥48; no exact full-color mask remains below this cutoff for any of these 18 cases.

The execution evidence is an author-side exact finite computation; formal native CLAIM/Result and independent Driver admission remain governed by actual authenticated authority.

## Frontier and next question EC49EXW

EC49EXU left 597 triple-collision and 44,234 double-collision schedules. All 18 formerly timed-out triple cases are now excluded for E<80. **Remaining: 579 triple + 44,234 double = 44,813** candidate schedules; the 579 triple cases all have eligible word count N>700. Global proved bound remains **63≤E*≤80**, with the established E=80 witness from EC49EXK.

Next: for the 579 remaining triple arrangements, group identical h7 signed-native inputs before running the exact h7 cutoff-76 solver; where h7 cannot exclude E<80, continue full h8 cutoff-80 OR-mask DP. Then apply the same safe prefix method to 44,234 double-collision schedules. Preserve signed primitive steps, all complete BRC keys and the mandatory observer signatures.
