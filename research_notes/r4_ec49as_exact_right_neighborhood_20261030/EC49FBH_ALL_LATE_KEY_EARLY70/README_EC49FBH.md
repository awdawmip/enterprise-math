# EC49FBH — Exact H2–H6 70-edge optimum over all late-key choices

Date: 2026-11-05 (Asia/Shanghai). Scientific input is frozen at fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Result is an author-side exact finite theorem, independently crosschecked; formal Result and independent Driver admission remain pending.

## Theorem

In the frozen seven-operation native signed-six-axis BRC model, each selected horizon H2–H9 must end at signed displacement (2,0,0,0,0,0), achieve rational observation rank nine, and the union of all selected paths must use at most five complete six-coordinate positive BRC cache keys. Count the number E of distinct signed primitive-step prefixes over all selected ordered operation words.

Fix ONLY H2 = {fe,ge} and H3 = {feg,gef} (16 already-paid prefix edges, three complete cache keys). Leave all H4–H9 word choices and two remaining complete cache keys free, subject to a valid full nine-window completion. Then:

**min E(H2,...,H6) = 70**, uniquely among additional complete cache-key pairs at **L=(4,2,1,0,0,0), M=(6,4,1,0,0,0)**.

The uniqueness concerns the two additional complete keys, not individual word sets. This generalizes EC49FBG from a fixed future H9 key to ALL possible future key schedules consistent with the full five-key budget.

## Complete finite key reduction

A primitive operation is a signed native six-axis step sequence:
a=(-1,-1); b=(-2,-2); c=(1,2,-1,-2); d=(2,1,-2,-1); e=(3,1,1,-3); f=(1,-1); g=(2,-2).

Terminal signed displacement excludes b. For any word of length h, positive BRC key (x,y,z,0,0,0), its exact operation counts obey:

    #a=z-1
    #e=z
    #c+#d=x+y-h-1
    #f=h+1-y-2z
    #g=h+1-x

All counts are nonnegative, so x+y>=h+1. The three fixed early keys have x+y<=4. The future H9 key M has x+y>=10 and cannot appear at H4 because it would require at least five c/d operations plus one e, more than four total operations. Therefore all H4 words must use a single other new key L. Exact nine-state DFA count-vector enumeration has exactly nine rank-nine H4 keys L. All nine have x+y<=8; thus H8,H9 must both use M and the DFA gives exactly 50 M keys which separately have rank nine there.

When L has x+y<8, H7 likewise must have rank-nine M; when x+y<7, H6 likewise needs rank-nine M. These necessary filters leave **136 possible ordered (L,M) pairs**. Across them H4,H5,H6 can use all words at L or M and can mix these two keys freely within each horizon.

## Exact prefix optimization

Enumerate all ordered length-4,5,6 operation words over a,c,d,e,f,g and check native signed endpoint, complete positive key, and original nine-state DFA observation. Across ALL keys the eligible word totals are 206, 1062 and 5352, respectively. The rank-nine criterion is equivalent to four Boolean clauses on six allowed signatures: (E or F) and (C or F) and (D or G) and (J or G). These are EC49FAR's rational rank test. Encode four clause bits per horizon; the H4/H5/H6 full target is the integer 4095 (12 set bits).

Build the original signed native primitive-prefix trie, marking the 16 fixed early prefixes prepaid. For each node v and bitmask m, let D_v[m] be the least number of new signed primitive-prefix edges selected below v, with bitwise OR of terminal masks m. Include D_v[0]=0 and any terminal's own mask at cost zero. Combining subtrees applies exact OR/min-plus convolution:

    D_new[a OR b] = min(D_new[a OR b], D_old[a] + D_child[b]).

For each nonempty selected subtree, charge one unit for its incoming edge unless that exact signed primitive prefix belongs to the fixed prepaid set. Induction over the trie shows this equals the minimum union cost over EVERY eligible finite word selection, including all within-horizon key mixtures and all primitive-prefix sharing.

Exact finite DP gives 124 feasible key pairs and 12 infeasible pairs among the 136; **70 is the unique least early cost** and occurs only at the two full keys L and M stated above. These 124 feasible pairs also agree with the independently established 124 key-schedule rank possibilities of EC49FAW.

## Attainment and scope

An actual complete admissible nine-window witness uses:

    H2 fe ge
    H3 feg gef
    H4 fegc fegd gefc gefd
    H5 feggf gefgf
    H6 fegccc fegddd gefccc gefddd
    H7 fegccfg fegddgf gefccfg gefddgf
    H8 feggfgfc feggfgfd gefgfgfc gefgfgfd
    H9 feggfgfgf gefgfgfgf

Direct ordered signed-X6 prefix-union counts are 12,16,32,38,70,82,106,112 at horizons H2,...,H9. Every horizon satisfies the endpoint, the observed-rank clauses and five complete positive cache-key budget. Hence this is an actual globally extendible 70-edge H2–H6 attainment.

## Reproducibility / independent evidence

Run: node VERIFY_EC49FBH.js > EXACT_REPORT_EC49FBH.json

The standalone dependency-free checker emits **all 136 exact per-pair integer results**, checks the nine H4 keys, 50 H8/H9 keys, 124 feasible schedules, unique 70-edge minimizer and candidate word totals. The actual local author study separately ran a Python standard-library multiset operation-word generator and memoized integer DFA count-state checker, then a native signed-prefix OR/min-plus DP. A separately implemented Node.js literal 6^h word generator and trie-DP crosschecker compared the 136 exact pair minima, including the infeasible entries: **136 of 136 match**. The local check also confirmed counts 206/1062/5352. Evidence is author finite computation, not independent Driver admission.

The theorem covers fixed H2/H3 but all global two-key continuations. The previously established author-side unrestricted nine-window bounds remain 80 <= E*_H9 <= 94. Suffix-aware optimization can favor a greater H2–H6 cost with a lower H7–H9 addition; no 93-edge global witness is asserted here.

## Next EC49FBI

Optimize complete H2–H9 signed-prefix cost jointly across the 124 feasible key schedules; compare 70-edge early optimum with higher early-cost families that may share more late prefixes. Then vary the H2/H3 root family while preserving the five-key budget, frozen scientific input, P000 and the ACTIVE six-axis world.

Dependencies: EC49FAR rank test, EC49FAV full witness, EC49FAW late-key rank classification, EC49FBG fixed-H9-key optimum. Applicable current normative context: docs/RESEARCH_CONTINUATION_PROTOCOL.md#current-normative-context.
