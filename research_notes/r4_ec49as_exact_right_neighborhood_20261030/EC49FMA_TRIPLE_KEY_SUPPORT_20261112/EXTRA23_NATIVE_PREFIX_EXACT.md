# EC49FMA — additional 23 complete three-key replacements solved exactly

Date: 2026-11-12. Scientific input frozen nine-state signed-X6 BRC `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Continue the same exact seven-full-cache-key 84-prefix problem. Exact full native prefix computations, with *every* eligible frozen word for each fixed keyset and all 24 observer demands, used unchanged EC49FKY `SCAN_7KEY_GENERAL.cpp` trie/subset dynamic programming.

For the two additional small coverable removed-triple classes:

| Removed class (zero-based triple enumeration) | Coverable exact key sets | Exact signed-prefix optimum histogram |
|---|---:|---|
| 29 — drop (3,1,1),(5,3,1),(6,4,1) | 15 | 102:1, 108:1, 112:3, 116:2, 124:1, 143:2, 151:2, 159:2, 194:1 |
| 30 — drop (3,1,1),(5,4,1),(6,4,1) | 8 | 108:2, 128:1, 138:2, 146:2, 172:1 |

**New 23-case result:** every exact fixed-key optimum is at least 102. The complete signed word input (original source generator and all eligible words per key) was generated locally, C++ solver executed on all 23 cases, and the C++ source independently recompiled before a second run; both output files compare byte-for-byte. Machine-readable cost bytes in sorted class and lexicographic added-key order have SHA256 `456e1ba997c73ab876dedf2b288484a1e120e270ecf1e82ae8a1cddc25c3247e`.

**Combined with prior EC49FMA 91 cases:** exactly 114 of 38,169 label-coverable three-key swaps now have complete native-prefix costs, all at least 102. Remaining unsolved for signed-prefix cost: 38,055. No new <=83 witness found in these 114; the known explicit 84-prefix construction continues to establish `C_min(7)<=84`.

The replay script `REPLAY_EXTRA23_EC49FMA.py` reconstructs the 23 exact problems from the original frozen generator and compiles the unchanged original C++ solver. It checks all exact integer optima against the published cost bytes. This is author-side exact finite evidence and awaits independent Driver review. Native session/CLAIM/Result authority was not granted in this run.