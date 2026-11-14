# EC49FOO — Exact native one-key BRC neighborhood

Date 2026-11-14. Status: AUTHOR_FINITE_EXACT_CHECK / NOT_REVIEWED.
Frozen scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Original signed-prefix input SHA256 cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e.
Parent: EC49FON, https://github.com/awdawmip/enterprise-math/pull/2406 at commit 6d9565a71f8e1e90823c7e5d504b0b696d24877a.

## Question and exact domain

The 11-dimensional hub-root kernel from EC49FON allows abstract globally cancelling rooted-cost changes. Can a one-key substitution in the original BRC signed-prefix inventory preserve all named assignment costs while changing a reachable rooted-cover cost?

Fixed baseline is case 32315, with seven named keys (0,4,5,11,37,39,81), 24 demands and four named roots 03,05,06,07. Replace exactly one selected key by a distinct key from the original 94-key inventory, and retain only swaps preserving the full 24-demand-to-root eligibility relation. All positional, branch and named-label information is retained in the source; the terminal map is a separately declared observer.

For each root r, the original signed-prefix trie induces D(K,r,S), the minimum prefix-node cover cost for its mandatory demands and a chosen subset S of optional demands. Its finite DP merges rooted child costs by union of labels, adds one node for nonempty coverage, then applies exact superset closure to impose required labels. For a legal complete assignment rho, C(K,rho)=sum_r D(K,r,S_r(rho)).

## Exact finite theorem

All possible one-key substitutions from the baseline are 7*(94-7)=609 distinct candidates. The legal-root-domain criterion retains exactly 73 swaps. They all occur in the existing 38,169 frozen named cases, but 29 lie OUTSIDE the earlier 51-configuration study of EC49FON.

Every retained configuration has exactly 648 legal named assignments and 168 reachable rooted-cost coordinates, split into 16+8+16+128 for roots 03,05,06,07. Exhaustively calculating all 73*168=12,264 target root entries and 73*648=47,304 target complete assignments gives:

* 37 swaps preserve the entire exact terminal-cost map, and all 37 preserve every accessible rooted-cost coordinate.
* 36 swaps alter the terminal map, and all 36 alter at least one accessible rooted-cost coordinate.
* 0 swaps have equal terminal map but distinct accessible rooted costs.
* Among 29 newly covered configurations, 11 preserve both observers and 18 change both; this expands beyond the previous 51-config census.

This establishes native injectivity of terminal observation on the exact radius-one, common-domain neighborhood of baseline 32315. It is a complete finite proposition under the pinned 94-key input and original root-cover operator.

## Proof / exhaustive certificate

The generator enumerates each outgoing key in the seven-key baseline and each incoming key among the other 87 keys once, checks the 24 exact named legal-root sets, and generates all 73 surviving rooted tries. At each trie node, DP states are labeled masks with exact minimum integer cover counts. For a root, all subsets of the eligible optional demands are evaluated while mandatory labels remain included. A full legal assignment independently chooses its named root from the original eligibility set; there are 2*2*2*3*3*3*3=648 such choices. The sum of the four exact root costs determines the terminal map. All rooted profiles and all terminal maps are compared to baseline in integer arithmetic. The program emits the complete 73-row result table; source code supports regeneration of the full 12,432 data rows including baseline.

The algebraic implication "equal reachable root profiles => equal terminal map" follows by substitution in C(K,rho). Exhaustive data proves the converse FOR THIS FINITE NEIGHBORHOOD, by recording zero terminal-equal/root-distinct pairs.

## Newly observed exact single-assignment compensation

Swap 37 -> 62 yields original case 33269=(0,4,5,11,39,62,81), outside the previous 51-config inventory. It changes exactly 12 of the 168 reachable root coordinates: 4 for root 05, 4 for root 06, 4 for root 07, none for root 03. Its terminal cost changes on 357/648 assignments; on 54 assignments, nonzero root changes sum to zero.

For assignment (5->05,7->06,13->07,15->03,17->03,19->03,21->03), root differences (03,05,06,07)=(0,+1,-1,0), with total cost 181 in both configurations. Changing only demand 13 to root 06 gives root differences (0,+1,0,0) and total cost 177->178. Thus local exact compensation is realized in the native model, but this pair is not a global equality gauge.

## Verification and continuation

C++17 signed-prefix trie DP at O2 and O3 produces byte-identical full 12,432-line output (including header). For the 44 configurations overlapping the previous 51-case inventory, all 44*168=7,392 rooted costs agree with its separately saved profiles. An independent Python implementation reconstructs native prefix tries from the pinned raw input and recomputes configurations 32315 and 33269: all 336 projected costs agree with C++ and all 648 assignments independently give 357 unequal totals and 54 exact compensated totals. No floating point or non-BRC model arithmetic is used.

Files: VERIFY_EC49FOO_NEIGHBOR_EXTRACT.cpp (full native generator), VERIFY_EC49FOO_NEIGHBOR.py (complete finite observer classifier), VERIFY_EC49FOO_INDEPENDENT.py (independent Python DP check), EC49FOO_73_NEIGHBORS.csv (all 73 cases), EC49FOO_RESULT.json (summary). Reproduce with frozen original master_and_radius3_cases.txt at SHA256 above. The complete original raw input, full computed root profiles, logs and SHA256 checklist also reside in the author reproducibility archive EC49FOO_NATIVE_ONE_KEY_EVIDENCE_20261114.tar.xz.

Next: examine two-key common-domain substitutions, specifically the binary spoke {7,13} at roots 06/07, for a nonzero all-assignment cancellation gauge. Distinguish such a gauge from individual assignments where the sum of two root deltas happens to be zero.

Authority: On 2026-11-14T11:35:01.916809Z the original exact control read for RS-EC49AS returned NO_CANONICAL_PUBLICATION_DIRECTORY and execution_authorized=false. This is independent portable science, with historical researcher attribution EM-DIRECT-204C14 and Activity RA-6893088D0A7347CE7F4D8720 only. No new identity/CLAIM/Result/review has been asserted.
