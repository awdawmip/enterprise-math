# R5 — exact three-count decoder cost frontier and adaptive-robust bit-length minimum

Date: 2026-11-16. Frozen scientific input: \`435e77af0d180eac32bd1f9c4c464bc4010b7551\`.
Provenance: the complete derived 954-indexed-event, radius-two nearest-center model and its 28 closure bits; earlier exact three-query and all-triples classification in \`research_notes/portable_direct/r5_minimum_scalar_queries_20261116/\` at immutable commit \`143ada28910f2b0e042d2d0ffcb066fee45d083e\`.
Evidence status: AUTHOR_PROVED / EXACT_INTEGER_FINITE_CHECKED / NOT_REVIEWED. This is a typed auxiliary integer observer, not a native X6 observer admission, Activity, Claim, Result, Review or Foundation promotion.

## Question and cost model

The eight effective closure bits are U={3,8,9,10,15,17,25,27}. A complete exact scalar-count decoder uses three queries, one per private-bit window:
- A: K=214..221, with local bit coordinates (3,8,9,10,27).
- B: K=223..291, with coordinates (25,27).
- C: K=293..314, with coordinates (15,17).

For each input mask m, a budget query returns the positive exact integer N_m(K), the number of optimal center subsets. **One count costs \`N_m(K).bit_length()\` raw binary data bits**. No compression, channel metadata, budget-selection signaling or computing time is included. A protocol has three scalar queries; its cost is the sum of those three bit lengths. We also compare the total *center budget* K_A+K_B+K_C, the worst count bit length, and expected total count bits under the uniform eight-bit quotient prior. The quotient has 256 equally likely signatures under uniform original 28-bit masks.

## Exact theorems

**Theorem 1 (universal per-input three-query bit-cost minimum).** Among all deterministic exact three-query scalar-count protocols, including protocols whose next K may depend on previous count values, the fixed budgets
\[
(K_A,K_B,K_C)=(214,291,294)
\]
minimize the sum of raw positive-integer count bit lengths **for every one of the 256 effective masks separately**. Thus they also minimize worst-case total bits, uniform mean total bits and worst individual count width.

*Proof.* The earlier exact support theorem shows that each successful depth-three path must query all three disjoint private-bit windows. To identify the C-private pair, its one C query must distinguish four masks without help from the A or B outputs, hence it must use K=294..313 (the exact classification proves K=293,314 collide). The B query must lie in K=223..291 to see bit 25. The A query must lie in K=214..221 to see bit 3; allowing K=220 or 221 on conditional branches only strengthens the comparison below.

Run the exact pinned event generator and integer shortest-cover DP as in the preceding three-count classification. Exhaustively compare the local integer bit lengths: for every A mask a in 0..31 and every K=214..221,
\[
\operatorname{bits}N_a(214)\le\operatorname{bits}N_a(K).
\]
For every B mask b in 0..3 and every K=223..291,
\[
\operatorname{bits}N_b(291)\le\operatorname{bits}N_b(K).
\]
For every C mask c in 0..3 and every K=294..313,
\[
\operatorname{bits}N_c(294)\le\operatorname{bits}N_c(K).
\]
These are 8*32+69*4+20*4=612 local exact integer comparisons, completely verified by the accompanying executable. Any adaptive protocol's realized three queries contain one from each of these windows and share exactly the same input-specific local masks; summing the three inequalities proves pointwise domination. The fixed triple is an exact decoder by the earlier scalar injectivity result, independently rechecked on all 256 masks. QED.

**Theorem 2 (minimal center-budget cost even with adaptivity).** Every exact three-query protocol expends total query budget at least 214+223+294=731 on every input. The fixed triple (214,223,294) attains 731. This follows from the three private windows and their minimum eligible budget positions. Consequently a lower raw-bit-cost query scheme trades at least some center budget against readout width.

**Theorem 3 (exact nonadaptive two-resource Pareto frontier).** Among all 8,280 injective fixed three-budget triples, the entire nondominated set for the pair (sum of query budgets, worst-case total raw count bits) is
\[
(731,319):\ (214,223,294),\qquad
(798,317):\ (214,290,294),\qquad
(799,305):\ (214,291,294).
\]
The source Python program enumerates all 6*69*20 valid triples, checks each against all 256 quotient signatures, computes bit cost for all masks and compares the integer resource pairs. This exhaustive enumeration proves the stated nonadaptive frontier; Theorem 1 also gives adaptive robustness for the 305-bit solution.

## Exact finite metrics

| Budgets (A,B,C) | Sum K | Maximum sum of 3 bits | Uniform mean sum bits | Maximum single integer width |
|---|---:|---:|---:|---:|
| 214,223,294 | 731 | 319 | 80960/256 = 316.25 | 118 |
| 214,290,294 | 798 | 317 | not needed for the two-resource frontier | not needed |
| 214,291,294 | 799 | 305 | 77504/256 = 302.75 | 104 |

Relative to the minimum-budget decoder, the pointwise-bit-optimal decoder saves 14 bits in worst-case total raw payload, 13.5 bits on average, and 14 bits of largest single count width, for 68 additional total budget units.

## Reproducibility and scientific scope

Run \`python research_notes/portable_direct/r5_decoder_cost_20261116/VERIFY_R5_DECODER_COST_COMPACT.py\` from the checked-out research branch containing the earlier \`VERIFY_R5_ALL_TRIPLE_DECODERS.py\` dependency. Python standard library only, all arithmetic exact (integers and rational input reconstruction). The earlier dependency's precise arithmetic functions \`frozen\`, \`close\`, \`spectrum\` are reused; no numerical MILP solver or floating-point operation is involved. The output JSON includes the exact metrics, 612 pointwise comparison cases, 8,280 valid triples and Pareto points. Locally executed result: \`PASS_R5_DECODER_COST_EXACT\`; independent review remains open.

This result concerns the raw-bit cost of the declared derived scalar observer. The execution cost of computing the counts, encoding overhead, and preservation of richer native X6 paths, BRC provenance, signed information or future operations were not optimized or asserted by this result.

## Next discriminating work

Determine the adaptive decision-tree Pareto frontier for the *joint* objective (sum K, worst-case raw bits), allowing K to depend on earlier scalar counts. In particular test whether a conditional B budget can improve the intermediate 798/317 trade-off. Separately analyze the computational DP cost as a function of K and the optimal-center recourse distance for K214..291, with full input representation cost stated before claiming an algorithmic speedup.
