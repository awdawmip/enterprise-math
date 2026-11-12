# EC49FMS — radius-three BRC exact optimization, cases 8000–9999

Date: 2026-11-13. Research status: AUTHOR-SIDE EXACT FINITE COMPUTATION / INDEPENDENT SPOT CHECKS / CONSTRUCTIVE WITNESS / UNREVIEWED. Frozen science: \`fc0f038e7bfd12c886b4d37f900bfb770c0f61ab\`.

## Scoped mathematical result

Within the fixed nine-state BRC word automaton, signed ordered six-axis microsteps, 178,850 legal words, 94 complete cache keys and 24 labelled observations, define C(K) as the least number of distinct **nonempty ordered signed-native prefixes** needed to select lawful observation words covering all 24 labels using seven preselected keys. The radius-three deterministic catalogue has 38,169 coverable seven-key configurations indexed 0..38168.

For the **complete finite range** 8000 <= i <= 9999:

- Exact minimum is **126**, attained only at **i=9004**; exact maximum is **168**.
- In 8000..8999, the exact minimum is **130**, attained only at **8428**.
- In 9000..9999, the exact minimum is **126**, attained only at **9004**.
- Among the 2,000 configurations, 128 have three available first-microstep roots and 1,872 have four. Complete exact vector and full histogram are in \`EXACT_VECTOR_EC49FMS.json\`.
- Combining with the previously completed i=0..7999 predecessor, the **continuous i=0..9999 window has minimum 102** (previous witnesses i=32,93,6589). The unrestricted seven-key 84-prefix witness continues to imply C_min(7)<=84.

## Why the computation is an exact finite optimization

Each selected legal word contributes its full ordered signed-native prefix path in a finite trie. At each trie node, dynamic programming stores for every mask of covered terminal labels the minimum number of selected nonempty trie nodes below that node. It combines child masks by min-plus union and optionally selects a terminal witness, adding one for a selected nonempty trie node. Induction on the finite tree height establishes exact optimality for each mask, with superset relaxation covering redundant labels. Different first-microstep roots have disjoint prefix sets; every observation label is assigned to one available root, and the optimizer exhausts all such assignments. The C++17 source used was the byte-identical pinned \`scan_cached_radius3.cpp\` from EC49FMR (source SHA256 in JSON), run with \`-O3 -std=c++17\` on intervals [8000,8500), [8500,9000), [9000,10000). All three runs finished with complete 2,000 consecutive rows. This proves exact values for the declared finite input domain under the explicitly pinned solver/induction argument.

Original frozen input \`master_and_radius3_cases.txt\`, its generator \`EC49FGW_RADIUS5_SCREEN.py\`, and case catalogue \`cases.json\` were recovered from the previously verified EC49FMR evidence package (PR #1730, commit \`b6c9d2b64d3a10686337ee7d0aa4048f27d39f78\`) and checked against its SHA256 manifest. The complete original raw 2,000-row output, logs, independent Python solver checks and reconstruction files are included in the local companion evidence archive; the full cost vector is stored losslessly here.

## Independent confirmation and constructive evidence

A separately implemented Python trie optimizer, not the C++ cost cache, recomputed i=8000,8428,8999,9004,9999 and obtained costs 138,130,168,126,162 respectively. \`WITNESS_9004_EC49FMS.json\` contains 24 actual lawful observation words, using seven keys [0,4,5,20,32,34,36]. The signed-native prefix union has **126 distinct nonempty prefixes**, split 18 + 54 + 54 between root bytes 03,05,06; the fourth available root 07 is unused. The witness gives the 126 upper bound, while complete root-mask DP gives the matching lower bound. The separate standalone validator checks lawful automaton transitions, X6 signed steps, target displacement, observation labels, seven keys and prefix count; when original raw output is present it also checks every indexed row and its SHA256.

## Status, provenance, and next question

This is mathematical author-side evidence, not an accepted formal Result or a Driver Review. At this research boundary, task \`RS-EC49AS\` was queried and returned \`CANONICAL_REJECTED: NO_CURRENT_IMMUTABLE_PUBLICATION\`; no CLAIM was made and no active owner was displaced. A new task-scoped session registration was rejected as \`UNKNOWN_CURRENT_TASK\`. The author-side route preserves evidence independently of task admission.

Next exact continuous unit is index **10000**; 28,169 coverable radius-three configurations remain after 9999. A separate line should seek a reusable cross-configuration lower-bound certificate or a lawful unrestricted <=83-prefix construction. Preserve the original signed order and frozen input for both lines.
