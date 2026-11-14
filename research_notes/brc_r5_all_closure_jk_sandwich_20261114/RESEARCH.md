# R5: Fixed-budget cost collapse under all 28 simultaneous or partial gap closures

**Date:** 2026-11-14. **Status:** author-side exact theorem and reproducible computation, **NOT_REVIEWED**. Scientific input **frozen** at `435e77af0d180eac32bd1f9c4c464bc4010b7551`. This concerns the *derived one-dimensional integer-event, radius-two center-cover observer*, **not** native X6 geometry, all BRC residual/provenance relations, or the independent 2,520-byte / 28-coordinate / 8,192-prefix-query benchmark.

## Setup and exact claim

The frozen construction gives 954 strictly increasing integer event boundaries and 28 indexed gaps (indexing begins at zero), each originally of length 3. A closure bit i shortens its selected gap from 3 to 2, shifting the suffix uniformly by one unit; closure choices on distinct gaps commute. Let B be any of the 2^28=268435456 subsets of closed gaps. For the resulting coordinate list X_B, write

J_B(K) = min_{S subset event indices, |S|=K, max_x min_{s in S}|x-s|<=2} sum_x min_{s in S}|x-s|.

The minimum is over event-coordinate centers and exact integer costs. The formula is defined only where a radius-2 feasible set of size K exists.

**Theorem.** For **every** subset B of the 28 gaps:

1. For all 214 <= K <= 954, J_B(K)=J_empty(K) exactly. Every one of these budgets is feasible for all B.
2. At K=213, which is also feasible for all B,

   J_B(213) = 1070 - 1_{(8 in B) or (9 in B)}.

3. In particular, for all closure patterns, the high-budget tail has the *explicit* closed form:

   J_B(K)=1305-2*K when 315<=K<=350, and

   J_B(K)=954-K when 351<=K<=954.

The original marginal gains for K=213,...,953 have multiplicities: gain 6 once, 5 eight times, 4 seventy times, 3 twenty-three times, 2 thirty-six times, 1 six-hundred-and-three times. This result is stronger than the prior **single-gap** stability result: it covers **all simultaneous choices** and the lower threshold K=214, where the marginal gain is 5 rather than at most 2.

## Proof by monotone closure sandwich

**Monotonicity lemma.** If B is a subset of C, every feasible chosen-center index set of X_B remains feasible on X_C with the *same* sum of nearest distances. Indeed it suffices to close one remaining length-3 gap. Before closing it, no cross-gap pair of events is within radius 2. After closing, the only cross-gap pair newly within radius 2 is the two endpoints, now at exact distance 2; that distance cannot strictly improve any already feasible old assignment, whose old nearest distance was at most 2 on its own side. All within-side distances stay unchanged. Hence J_C(K) <= J_B(K) at every old-feasible K. Applying the lemma one gap at a time proves monotonicity for arbitrary subset inclusion; no assumption about independent contributions is made.

Define five anchor closure sets: O=empty, A={0,...,27}, H=A\{8,9}, E8={8}, and E9={9}. The attached deterministic exact verification reconstructs the frozen events, computes the complete radius-two cost spectrum for all five anchors with *two independent recurrences*, and checks every budget. The anchored results are:

| Anchor | Smallest feasible K | J(213) | J(214) | J(315) | J(351) | J(954) |
|:--|--:|--:|--:|--:|--:|--:|
| O | 213 | 1070 | 1064 | 675 | 603 | 0 |
| A | 207 | 1069 | 1064 | 675 | 603 | 0 |
| H | 208 | 1070 | 1064 | 675 | 603 | 0 |
| E8 | 212 | 1069 | 1064 | 675 | 603 | 0 |
| E9 | 212 | 1069 | 1064 | 675 | 603 | 0 |

The certificate establishes J_O(K)=J_A(K) at **every** K=214,...,954 (741 entries, not only the displayed samples). For any B, O⊆B⊆A, so monotonicity gives J_A(K) <= J_B(K) <= J_O(K) and hence equality for all K>=214.

For K=213, if neither 8 nor 9 is closed, O⊆B⊆H and J_O(213)=J_H(213)=1070, forcing 1070. If 8 or 9 is closed, E8⊆B⊆A or E9⊆B⊆A; each endpoint cost is 1069, forcing 1069. This proves the exact two-valued formula for **every** one of the 268,435,456 configurations. The tail formula comes from the exactly checked original marginal-gain ranges and the already proven equality. QED.

## Why the finite anchor computations are exact

Two standard-library integer dynamic programs operate on the *actual 954 frozen coordinates*; no floating-point tolerance or unexplained heuristic is used.

**Chosen-center path DP:** For ordered chosen centers i<j, let e(i,j) be the sum of nearest-center distances of all strictly intermediate event points, rejecting the edge if any such distance is greater than 2. Define the cost of points before the first center and after the last center similarly, with radius checks. Then F_1(j)=prefix(j), F_{k+1}(j)=min_{i<j}(F_k(i)+e(i,j)), and J(K)=min_j (F_K(j)+suffix(j)). It is exact because nearest assignment in a line is to one of the two adjacent selected centers. The code only considers candidate edges of coordinate span at most 4+maximum_adjacent_gap: a longer span necessarily has an intervening event further than 2 from both endpoints.

**Contiguous-cluster DP:** Each selected center serves a contiguous block of event points under a consistent nearest-center tie rule, and serves its own event with distance 0. For an interval [a,b), compute C(a,b) as the least cost of serving all its points by one center chosen from that interval at radius at most 2; reject any other interval. Then G_k(b)=min_{a<b}(G_{k-1}(a)+C(a,b)). Each feasible interval has coordinate span at most 4, so the method is independent of the chosen-center edge recurrence. The two cost arrays agree **for every feasible budget** at all five anchors, including the previously unstudied new-feasible K=207..212.

Additionally, 480 seeded small integer sequences (N=2..9; 60 each) were checked against complete subset enumeration and both independent DP implementations. Another 100 pseudorandom closure patterns were directly checked at K=213,214,315; these are corroboration, **not** the basis of the all-pattern proof. The universal closure quantifier is discharged by the monotonicity lemma and five exact anchor certificates, not by pretending to enumerate 2^28 cases.

## Scope, preservation and next question

The previous 15-effective-bit / four-cluster compression for the **minimum center count D** is not adopted as a general sufficient observer here. This result is instead a proposition-specific exact cost certificate. Other observations—optimal center witnesses, edit distance, branch identities, joint relation provenance, native X6 state and future operations—are **not** claimed preserved by the same quotient. The 13 D-inert cuts need no general redundancy certification; this proof only gives the explicitly stated fixed-K total-cost invariance.

**Unfinished scientific boundary:** Compute exact J_B(K) for 207<=K<=212 whenever feasible, including the number and structure of distinct cost spectra over all 2^28 closure patterns and optimal center witnesses. The native 2,520-byte / 28-coordinate / 8,192-prefix-query end-to-end experiment and independent Result/Review remain open. No formal Task-ID or active CLAIM is asserted by this draft.

**Reproduce:** python3 VERIFY_R5_ALL_CLOSURE_JK.py. Its JSON output is also saved in EXACT_R5_ALL_CLOSURE_JK.json. Both are source-side research evidence, not independent mathematical acceptance.
