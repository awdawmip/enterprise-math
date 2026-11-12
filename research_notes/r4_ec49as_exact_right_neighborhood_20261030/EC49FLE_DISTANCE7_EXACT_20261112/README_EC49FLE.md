# EC49FLE — Complete exact distance-seven double-cache-key shell

Date: 2026-11-12. Frozen science: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Status: AUTHOR_EXACT_FINITE_COMPUTATION. Independent Driver mathematical review pending.

## Exact finite theorem

Retain the complete original nine-state signed-X6 BRC catalogue, consisting of 178,850 legal labeled operation words, 24 observer demands and 94 distinct full raw cache keys. For literal ordered, signed six-axis native microsteps, the verified EC49FKX construction uses seven full keys

K*={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}

and has a lawful witness with exactly 84 distinct nonempty native prefixes.

Remove two distinct old keys a,b in K*, and insert two distinct keys u,v in the 87-key complement. Their matched L1 distance is

d=min(||a-u||_1+||b-v||_1, ||a-v||_1+||b-u||_1).

There are exactly **5,227** distinct replacement key sets at distance d=7. Of these **810** can cover all 24 observer demands and **4,417** fail the exact per-key label-union coverage criterion. All 810 coverable sets have an **exact minimum signed-native-prefix cost of at least 98**. The attained minimum **98** occurs in **25** of the 810 cases, at indices listed in EXACT_REPORT_EC49FLE.json. No d=7 two-key replacement lowers the existing 84-prefix upper bound.

Together with EC49FLB (distance <=4), EC49FLC (distance 5), and EC49FLD (distance 6), the complete matched-distance <=7 two-key neighborhood contains exactly **13,024** distinct replacements, comprising **2,369** coverable and **10,655** uncoverable sets. The best cost of a distinct feasible replacement in this combined neighborhood is **84**, at the previously constructed distance-four alternative (EC49FLB). The unrestricted seven-key mother question is C_min(7) <= 84, with its exact minimum still open.

## Proof

The original frozen enumerator (sibling EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py) enumerates each legal observation/operation-word pair and its complete raw key and literal sequence of signed X6 native microsteps. For every key k, let L(k) be the bit mask of observer labels realized by at least one legal word of key k. A seven-key candidate K is coverable exactly when the OR of L(k) over K is the complete 24-label mask: every label can be chosen independently using a legal word.

Enumerating all C(7,2)C(87,2)=78,561 replacements, computing both possible assignments from deleted to inserted keys, and applying the above mask criterion gives exactly 5,227 distance-seven candidates and 810 coverable candidates. Of the latter, **328** have three distinct signed first-microstep roots and **482** have four.

For each coverable fixed key set, admit *every* legal word using one of those seven complete keys. Partition literal native byte paths by their first signed microstep. Different root tries share no nonempty native prefix. For each trie node, compute a min-plus dynamic program over every attainable union of demand bit masks; joining child subtrees uses bitwise OR and adds costs, and visiting a nonempty node adds exactly one prefix. Convert exact demand masks to superset coverage minima. Assign all 24 labels to compatible root tries and minimize the total across root assignments. Every lawful 24-word solution induces an admissible root assignment; conversely each root-DP solution yields legal words. Hence each computed cost is the **exact finite optimum**, with neither terminal-displacement identification nor floating-point relaxation.

The unchanged C++17 solver from sibling EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp was compiled with g++ -O3 -std=c++17 and executed on all 810 distance-seven coverable cases. Completed disjoint batches preserve every consecutive case index 0..809; incomplete combined attempts were not used as evidence. All minima are provided compactly as one uint8 per ordered case, base64-encoded in EXACT_REPORT_EC49FLE.json, with a SHA256 digest over the decoded 810 bytes. The complete histogram is included.

A separately structured Python standard-library signed-native trie DP was actually executed on indices **0,186,328,549,675,809**; its optima were **100,98,145,98,98,132**, matching the C++ solver, covering both three-root and four-root cases, and including distance-seven minimum achievers. This is independent selected-case verification; complete enumeration was performed by the C++ solver.

## Reproduction and precise evidence

Run REPRO_EC49FLE.py next to EXACT_REPORT_EC49FLE.json from this directory. The default mode recomputes the full key-level distance and coverage census, checks the 810-cost digest and minimum. With --solve, it compiles the unchanged sibling EC49FKY C++17 solver and recomputes all 810 optima from the frozen original operation-word catalogue. Run VERIFY_EC49FLE_INDEPENDENT.py for the six separately checked cases. The exact encoded array is ordered by (number of distinct first signed roots, sorted deleted-key pair, sorted added-key pair).

Source chain: frozen science pin above; EC49FKX explicit 84-prefix witness; EC49FKY complete-root signed-native exact solver; EC49FKZ 78,561 key-set coverage census; EC49FLB/EC49FLC/EC49FLD completed distance shells. Original local computation and evidence were performed in a retained source-compatible directory; the same solver source Git blob identity as the GitHub sibling was verified (d80d943d0470872ac067f4d2a2f700ec4631f4cf).

Next scientific question: exactly classify the 869 coverable matched-distance-eight double swaps and search for a lawful <=83-prefix seven-key witness, or derive global cache-key-independent bounds. Preserve complete raw key identity, signed path order, all 24 labels, and the frozen pin.

This is author-side research evidence on Draft PR #1730; no formal CLAIM, Result/Review or mathematical admission is asserted by GitHub publication. P000 and ACTIVE worldview are unchanged.
