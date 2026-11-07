# EC49EXX — Full finite exclusion of triple-collision BRC schedules at E<80

**Scientific scope:** Frozen H=8, exactly M=5 complete six-axis BRC keys, at most six nine-history observation matrices, seven-operation signed-native X6 path alphabet, 28 prepaid prefix edges. This is an author-side model-internal analytic lemma and exact finite calculation. No Source-native CLAIM/Result or independent Driver admission has been granted.

**Frozen scientific pins (unchanged):** Global `773d538180bfb49e24cffeb35c3ee75eb0628e2e`; EM `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Predecessor EC49EXW immutable commit `164036c0402419f40789d9d526cbb139023c0636` in Draft PR #1730.

## X1: cross-key signed-prefix intersection and private-suffix bound

For the full BRC key K=(u,v,w,0,0,0), the frozen signed primitive histogram is (u,v,w;u−2,v,w), so a legal native path has length L(K)=2(u+v+w−1). For any two legal keys put

`I(K,K') = 2(min(u,u')+min(v,v')+min(w,w')−1)`.

**Claim:** for any two legal native signed paths carrying K,K', their longest common signed primitive prefix satisfies `LCP≤I(K,K')`. Indeed every occurrence of each signed axis within their common prefix must fit in both signed histograms. Summing the six componentwise minima yields precisely I, proving the claim.

For h8 key K8, L8=L(K8), and m8 distinct mandatory h8 observer signatures (m8=2 for the present family), the earlier proven same-full-key intra-horizon separation `LCP≤L8−3` (EC49EXP/EXQ) gives

`d0=max(L8−3,max_(2≤h≤7) I(K8,K_h))`
`g=m8*max(0,L8−d0)`
`E8≥E7+g`.

**Proof:** the m8 selected h8 native paths are distinct because their full observation signatures differ. At every prefix-tree depth d>d0 up to L8, the paths have distinct edges by intra-horizon LCP separation, and none of those edges appears on a path assigned to h2…h7 by the cross-key intersection bound. The 28 prepaid base edges lie strictly shallower than those positive-gain depths in this frozen model; hence those m8(L8−d0) edges are additional charged edges. If K8 is reused at an earlier horizon then I(K8,K8)=L8, giving the valid trivial gain zero. QED.

## Exact exhaustive closure

Predecessor EC49EXS identified 123,147 triple-collision key schedules. Its exact necessary lower-bound screen eliminated 122,201 below E=80, leaving 946. Existing EC49EXR/T/U/V eliminated 367; EC49EXW eliminated 399; the 180 previously unresolved schedules are **fully excluded in this run**:

| Exact certificate | New schedules | Native computation |
|---|---:|---|
| H7_KEY_TAIL | 26 | 17 distinct H7 signed-prefix OR-mask integer DP inputs certify E7≥76; X1 gives g=4 |
| H7_MONOTONE | 130 | 130 exact H7 integer DP inputs certify E7≥80 |
| H8_FULL | 24 | 24 full H8 integer DP inputs certify E8≥80 |
| **Total** | **180** | **171 distinct successful native integer solver inputs** |

All 180 are distinct source-catalogue indices, disjoint from the prior exclusions and collectively complete the 946 survivor set. Exact DP stdout for each successful input has the shape `BOUND_PASS minimum_total_at_least=<cutoff> nodes=<nodes> colors=<colors>`. Some preliminary bounded runs timed out; these have subsequently been superseded by successful H7 results and were not used as proofs.

**Scoped theorem:** for every one of the 123,147 triple-collision arrangements in the declared frozen H8/M5/S≤6 model, `E_min≥80`. This relies on exact coverage in the earlier EC49EXS catalogue and the original EC49EXJ complete native operation-word generator, and on correctness of the published prefix OR-mask integer solver. It is author-side finite proof evidence pending independent review.

The **mother problem** still has 44,234 double-collision candidates below cutoff 80; the previously certified global bound remains `63≤E*≤80`. No proof of global E*=80 is claimed.

## Evidence and reproduction

Adjacent `EC49EXX_CASE_LEDGER.json.gz.b64` is an inspectable compact record of all 180 exact case IDs, mode, threshold, trie node count and observation color count, plus SHA256 of the *full* original raw 180-case JSON certificate ledger (`8835f71dd55876a1e5988a41093d736641ebf9b8228b1795c318062f7264d786`). Full raw JSON, actual stdout, per-case native input SHA256 hashes, signed-native source generator, C++17 OR-mask DP source, original execution logs, proof and next task are preserved together in `EC49EXX_COMPLETE_EVIDENCE.tar.gz` in the conversation deliverable. The compact GitHub ledger is not a substitute for the raw log when independently auditing a particular run.

Use `VERIFY_EC49EXX.py` against the expanded full ledger and the unchanged source `EC49EXJ_H8_M4_S6_GLOBAL_EXACT/SCREEN_H5_EC49EXJ.py` to reproduce all 180 trie hashes. `--solve` compiles the existing `EXACT_OR_MASK_DP.cpp` with `g++ -O3 -std=c++17` to rerun the 171 distinct exact computations. This session regenerated all 180 trie hashes, checked signed tail gains and the actual recorded successful outputs: PASS. Original 171 computations were executed during this run, distinct from the subsequent hash-only checker pass.

**Next:** EC49EXY applies X1 and exact OR-mask DP to the remaining 44,234 double-collision candidates; find a valid E<80 signed-native witness or complete exact elimination, while preserving full signed path/order and observation signatures.
