# EC49FQA — Exact priced BRC sensing for native class 16943

Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. Research date: 2026-11-15. Research type: independent portable continuation of EC49FPZ, without a formal task CLAIM or Result.

## Frozen model and question

Scientific pin: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Original master SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e. Root-cost CSV SHA256: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f. These are the same frozen scientific inputs as EC49FPZ PR #2512.

The native domain represented by original configuration 16943 contains 310 original configurations and 141 distinguishable full named-root cost profiles. There are exactly 144 legal full terminal scalar queries and 84 legal named-root scalar queries. The complete action set has 228 actions, with zero-based terminal indices 0–143 and named-root indices 144–227. Every adaptive policy must identify the *full named-root cost profile* exactly. Repeated queries are allowed but are never helpful on a constant response fiber.

Let the positive per-query prices be r (named root) and t (terminal). The uniform prior on the 141 root profiles uses weight 1 each; the source-multiplicity prior on the 310 configurations uses the positive integer multiplicity of each root profile. Costs below are the *sum of path costs* over the corresponding integer population; the expected cost is the indicated sum divided by 141 or 310.

## Theorem A — Complete finite Bellman optima at three unequal prices

The unrestricted finite adaptive optimum, with no a priori maximum depth, has the following *exact* sums.

| r:t | uniform 141-profile sum | multiplicity-weighted 310-config sum | optimal first indices (uniform / weighted) | globally evaluated Bellman masks |
|---|---:|---:|---|---:|
| 1:3 | 362 | 1033 | [153,161] / [153,161] | 10494 |
| 1:2 | 362 | 1014 | [153,161] / [153,161] | 10494 |
| 3:4 | 1057 | 2602 | [153,161] / [59,88] | 10304 |

For comparison, at r:t=1:1 the same new solver reproduces prior EC49FPZ exact results: 296/141 and 690/310 with optimal first indices [32,34] / [16,23,124,131] and 7612 Bellman states. The root-only action restriction has global minimum sums 362r (uniform) and 1033r (source-multiplicity). The root-only solver evaluates 2568 masks.

At r:t=1:2 the weighted optimal policy has 962 weighted root reads and 26 weighted terminal reads, hence exact sum 962r+26t=1014 (r=1,t=2); its maximum depth is 5. The uniform optimal policy is root-only at this price (362 root reads). At r:t=3:4 the uniform optimal policy has 303 root reads and 37 terminal reads, hence 303r+37t=1057; the weighted optimal policy has 202 root reads and 499 terminal reads, hence 202r+499t=2602. Their maximum depths are 4 and 3 respectively. All trees distinguish each of the 141 profiles for all 310 configurations.

## Theorem B — Exact sharp global modality-transition thresholds

The global optimal policies change modality at **exact rational price ratios**, and these thresholds are sharp across *all* positive real prices:

1. **Uniform 141 root profiles:** for every r,t>0 with r/t<=4/7, the unrestricted optimal expected cost is precisely 362r/141, attained by a pure named-root policy. For r/t>4/7, **every** globally optimal policy must use *both* named-root and terminal observations. At r/t=4/7, a pure-root policy and a genuine mixed policy tie for the global optimum.
2. **Weighted 310 original configurations:** for r/t<=26/71, the unrestricted optimum is exactly 1033r/310, attained by a pure named-root policy. For r/t>26/71, **every** globally optimal policy must use both modalities. At r/t=26/71, pure-root and mixed strategies tie globally.

These are the exact first price ratios where a pure-root strategy ceases to be globally optimal; there is no gap between the two cases.

**Exact finite boundary lower bounds:** The all-228-action, arbitrary-depth integer Bellman solver gives at (r,t)=(4,7) the optimum uniform total **1448=362*4** over the 141 full root profiles (10,461 evaluated subset masks). At (26,71), it gives weighted total **26858=1033*26** over the 310 original configurations (10,496 evaluated subset masks). The root-only optimum totals 362r and 1033r have already been exhaustively checked using only the 84 root action choices (2568 subset masks). Thus the pure-root strategy is globally optimal at each exact boundary, against **all 228** possible actions.

**Extend optimality to every cheaper root price:** Fix terminal price t and boundary r0. Every query cost at (r,t), 0<r<=r0, is at least (r/r0) times its cost at (r0,t); root queries have equality, terminal queries obey t>=(r/r0)t. Consequently every policy's expected cost is at least (r/r0) times the globally optimal expected cost at (r0,t). The pure-root witness attains the bound. This argument works for *all real positive prices*, independent of decision-tree depth.

**Strict mixture beyond the boundary:** A uniformly weighted valid mixed tree has 355 root reads and 4 terminal reads, giving total cost **355r+4t**, which is strictly less than 362r exactly when r/t>4/7. A configuration-weighted valid mixed tree has 962 root reads and 26 terminal reads, giving cost **962r+26t**, strictly less than 1033r exactly when r/t>26/71. Therefore for larger ratios no pure-root strategy is globally optimal.

**Terminal-only impossibility witness:** Original configurations 17928 and 38165 produce identical outputs for *all 144 legal terminal observations*, but the named-root observation index 148 (root 5, empty optional-subset mask) yields respectively **66 and 62**. These configurations have distinct full named-root profiles; no purely terminal adaptive tree, of any finite depth, can identify every profile. Consequently whenever pure-root strategies are suboptimal, *every* globally optimal strategy necessarily mixes both modalities.

**Endpoint tie:** At r:t=4:7 the mixed uniform tree costs 355*4+4*7=1448, matching the pure-root total 362*4. At r:t=26:71 the mixed weighted tree costs 962*26+26*71=26858, matching the pure-root total 1033*26. Complete original-configuration replay validates the boundary trees. This establishes a sharp transition **with mixed/pure ties precisely at the critical ratios**. These claims concern modality necessity; the complete piecewise affine *numerical cost envelope above* each threshold remains an independent optimization question.

## Complete optimality argument and finite verification scope

Let Omega be the set of 141 distinct root profiles. The 228 exact native queries induce integer-valued response partitions Pi_q(S) of any subset S of Omega. For each weight vector a_s (all ones or the multiplicities) and prices c_q=t for terminal / r for named-root, put A(S)=sum_{s in S} a_s. Set F_a({s})=0 and, for |S|>1, use

    F_a(S) = min_{q: |Pi_q(S)|>1} [ c_q*A(S) + sum_{B in Pi_q(S), |B|>1} F_a(B) ].

Every query that makes progress creates strict subsets, hence the recursion is well-founded and exhausts every finite adaptive decision tree. A query with one response fiber can be deleted from an optimal tree because its strictly positive cost reveals nothing. For each candidate q, the admissible lower bound is

    c_q*A(S) + min(r,t)*sum_{B in Pi_q(S), |B|>1} A(B).

A price-sensitive implementation prunes q only if this lower bound is no better than the incumbent for the relevant prior. It also deduplicates queries inducing exactly the same unlabeled partition, retaining a minimum-price representative. Such queries are interchangeable for exact identification after relabeling their response children. A separate root-only run restricts q to 144–227. Prices are positive integers in the finite checks (and the continuous interval results then follow by the stated comparison argument); no floating-point calculation is used to establish the theorem.

Machine outputs include every initial-query optimum value, all globally attaining first indices, full response-labeled optimal witness trees, exact profile and configuration multiplicities, and the number of evaluated Bellman subproblems. A separate verifier reconstructs native allocations and every root scalar response from the two frozen source files, then replays all 310 configurations on all witness trees. All eight prior/price checks and the unit-price regression pass. The root-only invisible terminal-pair witness is independently reconstructed.

## Artifacts, novelty and continuation

This research reuses EC49FPZ's exact native domain construction and unrestricted Bellman principle, extending them to unequal costs, root-only comparisons, exact rational critical-price lower bounds and the sharp continuous pure-root/mixed transition for both priors. Executed scripts and full certificates accompany this report; no published theorem admission or independent mathematical review is asserted.

The sharp first global modality-transition ratios have now been proved exactly: 4/7 (uniform) and 26/71 (multiplicity-weighted). The next problem is the complete piecewise-affine optimal expected-cost envelope for r/t above each threshold, including all later rational breakpoints and how the globally optimal decision trees change.

Sources: EC49FPZ PR #2512, immutable scientific pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab, and the frozen source SHA256 values above. All results are in the project's declared finite native BRC observer model, retaining full named-root distinctions and provenance, not a general theorem for arbitrary BRC categories.