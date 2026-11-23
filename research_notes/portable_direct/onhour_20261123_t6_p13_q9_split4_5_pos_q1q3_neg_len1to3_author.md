# T6 p13 q-order9 signed split(4,5): positive (1,3) against negative q5 lengths 1–3

Date: 2026-11-23. Frozen inputs: awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca. Mother: RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND.

## Exact finite result
Assume equality of original H0,...,H6, full named denominator 13*(13q+r), both original exponent masses <=2331, and prior proven cancellation of higher 13-valuations. Positive vertical order4 has q pattern (1,3), with all 12*12=144 choices of residues. Negative order5 includes **all** named rosters of lengths 1, 2 or 3, i.e. q partitions (5),(1,4),(2,3),(1,1,3),(1,2,2). Under the six mixed necessary 13-adic congruences and the saturated 12D q0 lattice, there are no admissible disjoint-support collisions in this exact scope.

| Negative q partition | Raw pairs | Shared canceled | Exact GS nodes | Ball leaves |
|---|---:|---:|---:|---:|
| (5) | 1728 | 0 | 4027 | 0 |
| (1,4) | 20736 | 1728 | 42792 | 0 |
| (2,3) | 20736 | 1728 | 42676 | 0 |
| (1,1,3) | 134784 | 30240 | 229543 | 1 |
| (1,2,2) | 134784 | 11232 | 271111 | 1 |
| **Total** | **312,768** | **44,928** | **590,149** | **2** |

2,172 complete negative named rosters were visited. Of 267,840 disjoint-support pairs, exactly two enter the necessary affine weighted ball. Both signed q0 vectors satisfy all six 13-adic conditions (j=1,...,6), but neither meets the two side budgets. Full witnesses:

1. positive [(1,2),(3,3)] and negative [(1,1),(1,1),(3,11)], u=(32,17,-24,-12,-8,-10,2,-6,6,-2,5,1), original masses (3289,4693).
2. positive [(1,1),(3,6)] and negative [(1,5),(2,2),(2,5)], u=(-42,3,25,-3,12,-4,-3,-3,4,-4,-5,4), original masses (3642,3768).

Algorithm: reuse exact saturated q0 13^21 congruence lattice and exact rational Gram–Schmidt. For signed q0 u, mixed congruences are sum(u_r*r^-j) + sum(positive (13q+r)^-j) - sum(negative (13q+r)^-j)=0 modulo 13^j. Each weighted affine search radius is at most 2*2331^2=10867122, below exact least GS diagonal square 78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349, so two-neighbor recursion is exhaustive. Each ball witness was recomputed using exact integers, with positive and negative contributions and signs preserved.

This is a **complete subfamily** (negative lengths 1..3), not the full positive (1,3) case. The remaining negative q partitions (1,1,1,2) and (1,1,1,1,1) were not completed in this execution and must remain unfinished; no negative inference is made for them. No native role-bound claim, independent review, or mathematical admission is asserted.

Evidence: research_checks/T6_P13_Q9_SPLIT4_5_POS_Q1Q3_NEG_LEN1TO3_AUTHOR_CERT_20261123_1100.json. Original Python Fraction/SymPy author execution; the dedicated compact published checker of this partial range has not been separately generated or run.
Next exact action: finish negative q5 pattern (1,1,1,2) in bounded disjoint roster slices, followed by (1,1,1,1,1); then remaining positive order4 patterns (2,2),(1,1,2),(1,1,1,1). Native p17 q14 separate.
Status: AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED.
