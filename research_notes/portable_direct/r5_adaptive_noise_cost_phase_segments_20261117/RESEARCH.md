# R5 — Exact adaptive noise–cost plateaus: low-noise staircase and full four-query regime

Date: 2026-11-17 (Asia/Shanghai). Frozen science pin: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Scope: the 954-event derived integer indexed-center observer with 256 effective closure masks, query budgets 214–314. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This extends earlier R5 results in Draft PR #2427.

## Model and notation

An unknown mask b in {0,…,255} is observed at an integer budget k via a real y obeying |y-N_b(k)| ≤ η. The adversary chooses answers in the closed intervals. Each query costs k and subsequent budgets may depend on previous readings; any finite number and repetitions are allowed. C*(η) is the optimal worst-case sum of queried budgets for exact mask recovery.

This is a finite scalar observer quotient. The native six-axis X6 state, path/branch provenance and future BRC dynamics remain separately typed; no inference about their global equivalence is made from scalar-mask recovery.

Exact positive integer thresholds:
A=76289178155959966960189440
B=3133722521542003559403356160
C=13883516118328421520506880000
D3=1744659037213380157479321600000
D4=1882951873548292168718745600000

## Theorem 1: Three sharp low-noise budget plateaus

For arbitrary finite adaptive policies:

- C*(η)=731 for 0 ≤ η < A/2.
- C*(η)=732 for A/2 ≤ η < B/2.
- C*(η)=733 for B/2 ≤ η < C/2.

Achieving fixed queries, respectively: (214,223,294), (214,223,295), (214,223,296).

**Upper-bound certificate.** For a budget tuple Q, define g(Q)=min_{b≠c} max_{k∈Q}|N_b(k)-N_c(k)|. Exact integer enumeration over all 32,640 pairs yields g(Q)=A,B,C for the three tuples. The first two gaps are attained by 64 pairs, including (16,32). The third gap is attained by 16 pairs, including (2,8). Distinct masks have disjoint possible transcript sets precisely when 2η<g(Q), since individual observation intervals are closed.

**Lower-bound certificate.** The exact readout windows are E=214..221, M=223..291, L=293..314, and budgets 222 and 292 add no distinctions. The pairs (2,8), (0,64), (16,32) respectively force at least one E, M, L query on a worst-case identification path. Every four-query policy costs at least 4×214=856 >733, so lower-cost policies must use three queries, including one from each window. In particular, E costs at least 214 and M at least 223. The witness pair (16,32) has identical outputs outside L, and absolute gaps at 293,294,295 equal 0,A,B. Consequently any policy with total cost ≤731 has late query ≤294 and cannot identify that pair once 2η≥A; any policy with total cost ≤732 has late query ≤295 and cannot identify the pair once 2η≥B. Since the observations from E and M are identical for these two hypotheses, adaptive query ordering and branching cannot evade this obstruction. This proves the two successive increases, and the three upper tuples give equality on the stated intervals.

## Theorem 2: C*(η)=955 across the complete four-query regime

For every D3/2 ≤ η < D4/2, the exact minimax total cost is **955**. This strengthens the former narrow result (D4−1)/2 ≤ η < D4/2.

**Lower bound.** On the 64-state Cartesian family S={lo | middle | late : 0≤lo≤15, middle∈{0,64}, late∈{16,32}}, bitwise OR combines disjoint bits. All 101 readout budgets were checked exactly: each E query depends only on lo, each M query only on middle, each L query only on late, and budgets 222 and 292 are constant on S. Thus the independent adversarial responses force the sum of the three factor minimax costs. At 2η=D3, the early 16-state factor cannot be solved in one query; enumerating all maximal real-interval overlap cliques for all eight first E choices gives the minimum worst cost **433** for two E queries. The two middle masks first separate at k=224 and the two late masks at k=298. Therefore every adaptive strategy costs at least 433+224+298=955 at η=D3/2, and cost is monotonic in η.

**Upper bound.** Query 215. At the hardest permitted integer center-spread D4−1, exactly 19 maximal candidate-mask overlap cliques occur. For each clique there is a second early query in {214,216,217,218} such that this second query together with 224 and 298 separates all pairs by at least D4 in one coordinate. The selected second budgets have histogram 214:5, 216:7, 217:5, 218:2. The actual first real answer induces a subset of such a clique, so choose its certified second early query, then 224 and 298. The policy's worst-case cost is 215+218+224+298=955 for every 2η<D4. Combined with the lower bound, this proves the complete interval. At η=D4/2 the earlier R5 indistinguishable-pair certificate supplies the endpoint obstruction.

## Proof and reproducibility

The verifier rebuilds 101×256=25,856 exact integer counts from the independently preserved sparse cohort data, checks every count against the full frozen count table, certifies the 64-state product fibre at all budgets, enumerates the three global pair margins, eight early-first decision cases and the 19 maximal full-state observation cliques. It uses integer interval comparisons, not sampled real observations.

Run:
python VERIFY_R5_ADAPTIVE_NOISE_COST_PLATEAUS.py compact_stdout.json EXACT_R5_ALL_101_BUDGETS.json > RESULTS_EXACT.json

Required SHA256 of inputs:
- compact_stdout.json: a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d
- EXACT_R5_ALL_101_BUDGETS.json: 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b

Expected status: PASS_R5_NOISE_COST_FOUR_QUERY_FULL_INTERVAL_AND_LOW_STEPS. These inputs and the full R5 reproduction bundle were preserved in the preceding R5 lineage, with frozen pin unchanged. The work is exact postprocessing of the 954-event observer's prior data, not a new native-heartbeat/BRC experiment. No new BRC arithmetic was needed.

## Next frontier and provenance

The incomplete cost phase segment is C/2 ≤ η < D3/2. Determine the next minimax cost after η=C/2 and its exact decision-tree certificate; independently retain the indexed-center max-new/min-old optimizer-set recourse question. Historical registered Researcher-ID: EM-DIRECT-C52C70, Activity: RA-E56F584D739D86CC48916236. Formal task claim, protected Activity association and independent review are distinct control operations.
