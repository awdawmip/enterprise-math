# EC49FLF — exact distance-eight two-full-key BRC/X6 shell

Date: 2026-11-12. Status: AUTHOR_EXACT_FINITE_COMPUTATION; independent Driver review pending. Frozen science input: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. P000 and ACTIVE worldview unchanged.

## Exact finite result

The frozen nine-state BRC corpus has 178,850 legal labeled operation words, 94 complete raw cache keys and 24 observer demands. The previously verified EC49FKX signed-X6 seven-key witness has 84 nonempty ordered native prefixes, with

\`K*={(2,1,1),(3,0,1),(3,1,1),(4,2,1),(5,3,1),(5,4,1),(6,4,1)}\`.

Remove two distinct old keys \`a,b\` in \`K*\` and insert two distinct keys \`u,v\` outside \`K*\`. The matched raw-key L1 distance is

\`d=min(||a-u||_1+||b-v||_1, ||a-v||_1+||b-u||_1)\`.

Among all **6,555** distinct two-key replacement sets at distance exactly **8**, exactly **5,686** fail the complete 24-label support-union condition. Every one of the remaining **869** key sets was exhaustively optimized over all legal words with those exact seven full keys, retaining literal ordered signed six-axis native prefixes.

**The exact minimum is 94 distinct nonempty native prefixes, achieved by exactly one key set.** In the declared sorted case order its index is **303**, with deleted keys \`(5,4,1),(6,4,1)\` and inserted keys \`(7,2,1),(8,2,1)\`. Another 16 sets attain 98. The complete 869-integer optimum vector has SHA256 \`a16edae817789000dc7055c6fa3a4007e0d9f3d45be6dc3bb9bbc1df3cf37e7d\`.

Together with the exact distance <=7 predecessor shells, distance <=8 contains **19,579** distinct double-key replacements: **3,238** label-coverable and **16,341** not label-coverable. All 3,238 feasible replacements have exact prefix minimum >=84, and 84 is attained at distance four. The unrestricted seven-key mother question retains the lawful upper bound \`C_min(7) <= 84\`; its exact value is open.

## Exact proof and actual execution

1. For each full raw key \`k\`, compute its 24-bit demand-support mask \`L(k)\` by OR-ing the labels of **all** admissible original BRC operation words using that exact key. The condition \`OR_{k in K} L(k)=2^24-1\` is necessary and sufficient for demand coverage without prefix-cost restriction: each demand may independently select any one of its legal words. The complete \`C(7,2)*C(87,2)=78,561\` enumeration also checks that the distance-eight class contains 6,555 sets and 869 coverable sets.
2. For each coverable \`K\`, insert every legal word using a key of \`K\` into a trie of literal ordered signed X6 microsteps. Partition by first microstep: distinct first-root tries share no nonempty native prefix. Within each trie, a min-plus DP over exact attainable demand masks uses terminal words as witnesses, combines children by bitwise OR, and adds one for each selected nonempty prefix node (parent closure). Assign the 24 demands to compatible roots and minimize the sum of exact root costs. Every original lawful solution induces such an assignment; conversely every realized assignment provides a legal word selection. The computed optimum is therefore exact for each fixed \`K\`.
3. Actually ran the unchanged predecessor C++17 \`EC49FKY_ONE_KEY_SWAP_84_LOCAL_OPTIMUM_20261112/SCAN_7KEY_GENERAL.cpp\` over all 869 distance-eight coverable sets in consecutive nonoverlapping batches, with the frozen generator \`EC49FJD_RELEASE_B11_COMPLETE_20261111/EC49FGW_RADIUS5_SCREEN.py\`. A separate Python standard-library trie/subset DP was actually executed on indices \`[0,43,296,303,400,700,868]\` (including the unique 94 and both 3-root/4-root cases). All seven independently recomputed optima match the C++ output.
4. The original per-case outputs and local scripts, the identical frozen generator/C++ solver, and a SHA256 manifest are preserved in the accompanying locally delivered evidence archive. The GitHub numeric summary and reproducer use the same frozen model. This is author-side finite evidence; independent Driver review, current formal CLAIM and Result have not been asserted.

## Source and next scientific unit

Parent source chain: EC49FKX explicit 84 witness; EC49FKY full-root signed-native DP; EC49FKZ complete 78,561 support census; EC49FLB/C/D exact distances <=6; EC49FLE distance seven. Original scientific pin: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`. Both the original generator and C++ solver are reused unchanged.

Next: the remaining **3,077 label-coverable distance >8 two-key replacements**, beginning with distance nine, or a verified <=83 seven-key witness by another route. Exact local computation and independent proof semantics may be reviewed before mathematical admission.
