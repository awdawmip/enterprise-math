# EC49FEM — Five-key tail obstruction and a new exact 22-path BRC exclusion

Date: 2026-11-08. Frozen scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Author-side finite research; independent Driver review and Source admission pending. Full signed-native-X6 path and complete positive-BRC key semantics inherited unchanged from EC49FEJ/FEK/FEL.

## Theorem 1: all H9-low five-high-signature families are impossible

Assume the minimal 22-path H2–H9 quota: five high horizons with signatures (16,32) each, three low horizons with signatures (1,2,4,8) each, global budget at most five complete BRC keys, and arbitrary within-horizon mixing. H2 forces the full key (3,1,1), and H3 is high.

**If H9 is a low horizon, no legal 22-path system exists**, independently of the prefix-edge objective. A high observer signature 16 or 32 is a final state 4 or 5 in the source nine-state DFA. To end there an operation word must start with f or g and never contain c or d. Thus its count r=#c+#d=0. Since the exact BRC identity is r=x+y−h−1 for a word of h operations with key (x,y,z), any key supplying a high horizon h has x+y=h+1. The five distinct high horizons demand five distinct complete keys, consuming the five-key budget. If H9 is low, all five high horizons lie among H3–H8, so each key satisfies x+y<=9. But an H9 word would require r=x+y−10>=0; this is impossible for every available key. Hence no H9 word exists, much less all four required low signatures.

High-key counts N_h=sum(z=1..floor((h−1)/2))(h−2z) for h=3..8 equal 1,2,4,6,9,12. The five possible H9-low families (omit high H4,H5,H6,H7,H8 respectively) have 2592,1296,864,576,432 distinct full-key inventories: **5760 impossible inventories**. This is an analytic proof plus exact finite counting, not a sample search.

## Theorem 2: highs H3,H4,H5,H8,H9 exclude native prefix cost <=93

Fix high horizons H3,H4,H5,H8,H9 and low horizons H2,H6,H7, 22 paths, maximum five full BRC keys and arbitrary mixed-key paths. There are 1*2*4*12*16=1536 exhaustive high-key inventories. Integer exact nine-state signature pool enumeration gives 576 quota-infeasible inventories (H6 low signature missing) and 960 quota-feasible inventories. The inherited EC49FEK depthwise set-cover lower bound reaches **at least 94** for each of all 960 quota-feasible inventories. Thus no system in the stated finite family has <=93 distinct nonempty signed-native prefixes.

Proof of the lower-bound method: every H2–H3 legal early variant has exactly 42 native prefixes; the union of all four variants has 54. Donate all 54 to each system for free. At native depth d, retain groups whose every admissible candidate path reaches depth d, then solve an exact minimum bitmask set cover m_d for remaining groups using all eligible primitive words over that inventory. Actual selected paths cover every retained group; hence C_native >=42+sum m_d. Early-union gifting and separate optimization at each depth are relaxations. Stop only after the nonnegative partial sum reaches 94. Four disjoint exhaustive input ranges [0,384),[384,768),[768,1152),[1152,1536) each produced 144 signature-infeasible and 240 cost-excluded inventories; partial bound values range 94–105. Eleven sampled nontrivial covers agreed with a separately coded SciPy/HiGHS 0–1 integer optimizer. The exact integer DP complete sweep, not the sample, establishes the finite exclusion.

## Other six H9-high families: exact necessary-signature screen

High set : total inventories / per-signature feasible

3,4,5,8,9: 1536 / 960; 3,4,7,8,9: 3456 / 1956; 3,5,6,7,9: 3456 / 3456; 3,5,6,8,9: 4608 / 4608; 3,5,7,8,9: 6912 / 6912; 3,6,7,8,9: 10368 / 4224. Total 30336 / 22116. Passing this screen does not itself establish a <=93 construction.

Earlier four H9-high families contain 5952 inventories (5616 cost-excluded, 336 infeasible). With this work 10 of 15 minimal observation-quota families have a <=93 disposition: total 13248 inventories, comprising 6576 cost-excluded after quota feasibility and 6672 infeasible; five H9-high families remain (28800 inventories, of which 21156 pass necessary signature pools).

## Evidence and next action

Exact source: pinned EC49FEJ commit 64b2b4a34e33c849e937dbf46df90a70c5d58ef2, EC49FEK commit faa9fab17b894757b8cfcd77bcb3bbd6fcf1ecdc, previous EC49FEL commit 9a251ac8cf0a719ebfbf6260f60d8c2f24f55fff. Local executed and archived reproducibility evidence: EC49FEM_complete_evidence.tar.xz (SHA256 3f7a29afe29dc7c5cde7ebb316b29384baee8718552a66fde4b6a55b0e8478c0); includes full 1536-row partitioned ledger, exact enumeration programs and independent audit report. No native Source CLAIM/Result/Driver acceptance claimed.

Next EC49FEN: exact depthwise lower-bound sweep for five remaining H9-high families; any <=93 bound survivor requires joint full native-prefix integer optimization or explicit witness. Mother objective is still <=5 complete BRC keys and <=93 native prefix edges; existing 94-edge construction remains incumbent.