# EC49FLB — Exact complete two-key distance-4 BRC neighborhood of the 84-prefix witness

**Date:** 2026-11-12. **Frozen input:** `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. **Status:** AUTHOR_EXACT_FINITE_COMPUTATION; six independent Python reference instances; pending independent Driver audit.

## Theorem: the whole matched-L1 two-key distance <=4 neighborhood is 84-optimal

Preserve the **entire** original nine-state signed-X6 BRC catalogue (178,850 lawful labeled operation words, 24 observer demands, 94 distinct raw full cache keys). The explicit EC49FKX construction has seven keys

`K*={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}`

and 84 distinct nonempty ordered signed six-axis native prefixes.

For two distinct deleted keys `a,b` and two distinct added keys `u,v` outside K*, define the minimum matched-key coordinate distance

`d=min(||a-u||_1+||b-v||_1, ||a-v||_1+||b-u||_1)`.

**For all distinct two-key replacement sets with d<=4, if all 24 observer labels remain coverable, the exact minimum original signed-prefix count is at least 84.** Equality occurs in exactly **one** of the 410 feasible key sets in this specified neighborhood, when deleting `(5,4,1),(6,4,1)` and adding `(6,3,1),(7,3,1)`. That new key set has exact optimum 84 (root05=42, root06=42, root07 unused). Thus the EC49FKX witness is also a **non-strict local optimum under every matched-distance <=4 two-key replacement**.

This theorem extends EC49FLA (d<=3, strict lower bound 90 on distinct replacements). The original global seven-key optimum is still open with the explicit upper bound `C_min(7)<=84`. The second 84-optimal key set is proved by full finite integer optimization; a separate explicit list of its 24 realizing operation words remains a useful next extract.

## Complete finite counts

The frozen universe has `binom(7,2)*binom(87,2)=78,561` distinct two-key replacements, with exactly 6,315 passing necessary union-of-label coverage.

| Matched distance | All two-key replacements | Demand-coverable | Coverage impossible |
|---:|---:|---:|---:|
|2|98|22|76|
|3|458|111|347|
|4|1,181|277|904|
|**<=4**|**1,737**|**410**|**1,327**|

Among the 410 coverable near-neighbors, 199 have three distinct first signed native roots and 211 have four. Every one was solved exactly with the existing EC49FKY original native trie solver; every feasible set admits as many words per demand and key as allowed by the frozen catalogue.

Exact optimum histogram for the 410 instances:

```
84:1 86:2 90:1 92:4 94:4 96:1 98:44 100:12
102:2 104:81 106:19 108:12 109:2 110:10 111:1
112:123 114:4 116:33 120:3 122:2 124:9 129:1
130:3 131:1 133:1 134:3 137:3 138:3 140:1
141:2 142:2 145:1 146:13 149:3 160:1 161:2
```

All 410 case keys are ordered deterministically by `(matched_distance, first_root_count, deleted_two_key_tuple, inserted_two_key_tuple)`, with complete ordered optimal costs in `COSTS_EC49FLB.json`; the unique 84-minimum is case index **266**, and the two 86 minima are indices 222 and 234.

## Exact proof/verification

The full frozen legal operation-word enumerator `../EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py` recomputes every operation's demand bit, **complete** raw key, and ordered **signed** native X6 bytes, without identifying paths by terminal displacement. Enumerate all 78,561 two-key sets, reject 1,327 covered-distance-4 candidates lacking full label coverage, and retain all legal words from each of the other 410 fixed-key sets.

Partition allowed native words by their literal first signed microstep byte. Prefix trees for different roots are disjoint. In each root, exact subset-mask dynamic programming selects any compatible terminal word and combines child prefix sets, charging every visited nonempty prefix once. Finally enumerate all allocations of 24 labels to roots capable of supplying them and minimize the sum. Every valid word solution induces an allocation, and every collection of root solutions yields a valid global solution; therefore these minima are exact for the declared finite model.

The unchanged integer-only C++17 exact solver from EC49FKY was executed on all 410 cases. A long initial process completed the first **238** cases before hitting the execution time limit in the next case. A second execution covered cases 238–409, and the two fully completed, disjoint ranges were joined into a 410-case report with exact consecutive indices. Its SHA256 is `a7a708637d59ef7572e89590fd7e01ef3ab8695b2f1aba850f134f43e9ebd1ac`.

The **independently implemented** EC49FKY Python standard-library native-trie DP, applied to exact cases 6,14,222,234,266,300, agrees on every optimum, including the 84-optimum and both 3-root/4-root branches.

**Reproduce:** generate `EC49FLB_CASE_INDEX.json` and `EC49FLB_CASES.txt` with `REPRO_EC49FLB.py`. Build `../EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp` using `g++ -O3 -std=c++17` and solve the cases. Compare its 410 ordered integer minima with `COSTS_EC49FLB.json`. Run `VERIFY_EC49FLB_SELECTED.py` after generating the case index to rerun independent reference checks.

**Next discriminating unit:** continue beyond matched distance 4 (all 6,315 coverable two-key sets), identify a lawful <=83 prefix witness or new lower-bound certificate, and extract 24 explicit realizing words for case 266. Preserve full keys, literal signed native prefix sharing, all 24 labels and frozen pin.

**Source/authority state:** author-side GitHub evidence on Draft PR #1730, no independent Driver mathematical review or verified current formal EC49AS CLAIM/Result; protected P000 and ACTIVE worldview unchanged.
