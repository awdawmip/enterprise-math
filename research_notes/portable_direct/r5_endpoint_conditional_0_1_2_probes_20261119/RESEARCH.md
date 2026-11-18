# R5 — endpoint-class-conditional 0/1/2 interior probes (exact optimality)

Date: 2026-11-19. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Original researcher provenance: EM-DIRECT-4C3E47; existing Activity RA-F2257922D00B2FE4C4818DBD.
Mode: independent portable research. No formal CLAIM, RUN, Result, Review, working-truth promotion or X6-native equivalence is claimed.

## Input and precise claim

Frozen scientific input commit: 435e77af0d180eac32bd1f9c4c464bc4010b7551.
Frozen table EXACT_R5_ALL_101_BUDGETS.json: SHA-256 50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b.
Predecessor full-interval census: a661f387ef8819ef95a7121d4e73e6b677f64ee5, 30,876 nine-state pair-instances, 2,563 joint-endpoint classes, 2,711 whole-interval classes, 620 cross-daughter instance pairs.
Predecessor 620-pair witness CSV: SHA-256 3d2706270c490433b7c6fab8a4b606b570e771c27e35aed37260969225bacc32.
Predecessor fixed three-probe certificate: e0f69eab5b4831f4ae9e09f741cb0314402ffe9b.

Nine named slots are (18,24,82,34,17,x,144,208,y), x<y outside the fixed seven hypotheses. The 101 physical budgets are k=214..314. The diameter tau runs in the predecessor's exact fifth-noise interval, discretized into 18 exhaustive integer thresholds. An indexed maximal-support family S(T,k,tau) is the collection of inclusion-maximal named-slot sets whose scalar centers fit inside a closed interval of length tau. Its exact computation retains slot order and uses integer arithmetic.

**Theorem (conditional optimality).** Suppose an instance's complete indexed support signatures at both L and U-1 are already known (the same information assumed by the predecessor's fixed three-probe theorem). If the choice of subsequent interior probes may depend on that **endpoint-equivalence class**, the worst-case minimum number of additional fixed budget/diameter probes necessary and sufficient to decide entire-interval equivalence is **two**. This is sharp. There is no need for adaptivity after this endpoint-dependent choice.

Exact population classification:

| Full endpoint class type | Number of endpoint classes | Number of individual nine-state instances | Optimal extra probes per class |
| --- | ---: | ---: | ---: |
| No internal splitting | 2,455 | 30,428 | 0 |
| Two daughters, budget 220 witness | 28 | included in 256 one-probe instances | 1, choose (220, stage 2) |
| Two daughters, budget 214 witness | 40 | included in 256 one-probe instances | 1, choose (214, stage 3) |
| Three daughters, budget 214 witness | 40 | 192 | 2, choose (214, stage 4), (214, stage 8) |
| Total | 2,563 | 30,876 | max 2 |

Stage diameters are exact:
stage 2 = 33469190642398873308364800000;
stage 3 = 34543510342031429735546880000;
stage 4 = 35645376700628923507015680000;
stage 8 = 41430175083265765807226880000.

Thus 30,428 instances need zero extra tests; 256 need one; 192 need two. Under the *illustrative* uniform distribution on the 30,876 instances, the mean number of additional tests is (256+2*192)/30876 = 160/7719 = about 0.0207281. This is an observer-classification workload, not a stochastic claim about nature and not a reduction in the physical Bellman strategy's cost.

## Proof

1. The predecessor exhaustively established that exactly 620 unordered pairs of nine-state **instances** have equal full endpoint signatures but unequal full-interval signatures. Equality/inequality is exact over 18 stages and all 101 budgets, and each distinct pair is represented in the immutable CSV. The 620 witness edges form 108 disjoint connected components when vertices are instances; because all cross-daughter pairs are listed and all within-daughter pairs are absent, the components are precisely the 108 split endpoint-equivalence classes. The remaining 2,455 endpoint classes never split; they need no interior probe.
2. For every witness edge, the predecessor checked all stages and all 101 budgets and found that only k=214 and k=220 ever distinguish such endpoint-equivalent instances. The edge sets are disjoint by budget: 448 edges with only k=214 and 172 with only k=220. No other budget can improve a class's extra-probe certificate.
3. Partition the 108 components using exact support tuples at every possible stage of the component's unique relevant budget. The executable verifier regenerates support sets directly by doubled-center closed-interval endpoint sweeps from the frozen table. It tests all 18 stages for each component, searches exhaustive single-stage and double-stage covers of the component's witness edges, and verifies that the selected probe signatures give the stated number and sizes of daughter classes.
4. The resulting exhaustive classification consists of 28 two-daughter k=220 components covered by stage 2, 40 two-daughter k=214 components covered by stage 3, and 40 three-daughter k=214 components covered by stages 4 and 8 together. The 108 components comprise 448 nine-state instances; their edge totals are 284 for one-probe and 336 for two-probe components, for the original 620.
5. **Sharp lower bound.** The endpoint component anchored by pair-instance (x,y)=(11,132) consists of six instances partitioned into three whole-interval daughters of sizes 2,2,2, producing 12 cross-daughter witness edges. Exhaustive independent testing of each of the 101 budgets at each of the 18 stages finds no single probe that separates all three daughters: for every such probe some cross-daughter edge has equal signatures. Consequently any conditionally chosen one-probe scheme fails on this known endpoint class. Two probes (214, stage 4) and (214, stage 8) distinguish all 12 edges, establishing optimality.
6. For each other component, the listed single/double probes hit every cross-daughter edge; equality at all selected tests is therefore equivalent to equality of the full-interval support signature *within that known endpoint class*. Combining with the 2,455 unsplit classes proves the theorem on all 30,876 instances.

The essential point is **class-conditional** versus **universal** probe selection: the predecessor correctly proved that any one common, class-independent set of fixed probes needs 3; the current theorem shows that using already-known endpoint information reduces the conditional maximum to 2. The claims are complementary, not contradictory. There is no automatic claim of X6 native equivalence, future-op preservation, or BRC information-losing descent.

## Verification and reproduction

Local source input and onset regeneration were rerun from the pinned frozen table. Recomputed all 18-stage census with original C++ solver: 2,563 endpoint classes, 2,711 final classes, 108 split endpoint classes; exact onset_18.bin SHA-256 ca175a4655b045d6427b9171c80198e548a8bc27f939a3b5e8f78a1c7f6b12bf.

New independent Python verifier VERIFY_R5_CONDITIONAL_0_1_2.py read the exact frozen table, stage thresholds, and 620 predecessor witnesses and returned PASS_EXACT_CLASS_CONDITIONAL_0_1_2; 108 classes, 11,664 cached exact support evaluations, 620 cross-daughter edges; full 101-budget x 18-stage single-probe impossibility check on the six-instance example. RESULTS.json carries all component anchors, daughter sizes, and chosen probes.

To reproduce: place the immutable EXACT_R5_ALL_101_BUDGETS.json, stages_18.json, and interior_distinguishing_budget_witnesses.csv from the predecessor next to VERIFY_R5_CONDITIONAL_0_1_2.py, then execute python VERIFY_R5_CONDITIONAL_0_1_2.py. No floating-point tests are used.

Scientific status: exact finite within pinned scalar-observer game; author-verified, not independently reviewed. The overall 256-state eight-error minimax bound remains 8335 <= C8* <= 8343, unaffected by this observer-quotient improvement.

Next question: apply this conditional decision table to avoid redundant nine-state signature comparisons while independently seeking a **strict** nine-state C8>8335 certificate, and test whether costs of computing full endpoint signatures erase any engineering speedup. Complete input-transformation and classification cost accounting is required before asserting a general complexity gain.
