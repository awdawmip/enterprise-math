# EC49FSE — Exact four-phase native BRC q140 price slice at quarter discount

Date: 2026-11-18. Status: AUTHOR_PROVED / EXACT_FINITE_BELLMAN_CROSSCHECKED / NOT_INDEPENDENTLY_REVIEWED.
Frozen scientific input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Continuation of EC49FSD, parent PR #2675 (and EC49FSC PR #2672).

## Exact model and result

Use the original BRC class 16943 instance: 141 distinct named state profiles (310 underlying configurations), 228 physically named native observers with their original joint response fibers, uniform prior on the 141 profiles, and all complete finite deterministic adaptive identification trees. Do not quotient named observers merely because their response partitions coincide. Base observation price t>0. The prices of q32 and q34 equal 3t/4; price of q140 is (1-z)t; all remaining observers cost t. Let F(z)=141 times the global minimum expected cost divided by t, for 0<=z<=1.

**Exact theorem:**

- [0,1/6]: F(z)=258-16z.
- [1/6,1/4]: F(z)=260-28z.
- [1/4,101/384]: F(z)=1057/4-45z.
- [101/384,1]: F(z)=579/2-141z.

The boundary values agree, including F(101/384)=32309/128 and F(1)=297/2. Exactly four distinct fixed complete-tree cost types are necessary and sufficient for the entire real price interval. Other tied trees may exist at a specific price point.

## Full native witness counts

For a tree T let U(T) be the sum of all observations along its 141 distinct named-state paths and Nq(T) the number of occurrences of named observation q on those paths. Its exact normalized total price is C_T(z)=U-(N32+N34)/4-z*N140.

Each witness below is a complete 141-state native tree with no repeated physical observer on any state path, exact singleton leaves and maximum depth 3:

| branch | generating Bellman anchor | U | N32 | N34 | N140 | first observer |
|---|---|---:|---:|---:|---:|---:|
| 258-16z | 1/14 | 296 | 11 | 141 | 16 | q34 |
| 260-28z | 21/94 | 298 | 11 | 141 | 28 | q34 |
| 1057/4-45z | 59/226 | 300 | 2 | 141 | 45 | q34 |
| 579/2-141z | 1 | 301 | 7 | 39 | 141 | q140 |

The full 8 computed tree files (including the 4 load-bearing witnesses), pinned native inputs and exact checker code are preserved in the companion self-contained EC49FSE evidence archive.

## Independent global Bellman endpoints

| z | exact F(z) | independently visited nontrivial DP masks |
|---|---:|---:|
| 0 | 258 | 11437 |
| 1/6 | 766/3 | 11383 |
| 1/4 | 253 | 11301 |
| 101/384 | 32309/128 | 11344 |
| 1 | 297/2 | 8770 |

At every endpoint, two distinct implementations agree exactly: one on the frozen 228-observer source and one rebuilding all 228 named observers independently from the original 94-family representation. The second implementation re-enumerates all admissible observer splits. The first solver also checked non-boundary anchors 1/14, 21/94 and 59/226 to discover complete witness trees. Exact rational scaling and integer subset Bellman recursion were used, without floating-point optimization.

## Proof of all-real optimality

For a non-singleton subset S of named states, let D(S) be the minimum sum over the states in S of the remaining path costs. For each original physically named observer q with at least two nonempty response fibers on S, the recurrence is

D(S) = min_q [ |S| c(q) + sum_{r} D(S intersect q^{-1}(r)) ], with D(singleton)=0.

Every nonempty child of a legal split is strictly smaller than S. This well-founded finite recursion enumerates all legal adaptive decision trees and proves exact global optimality of the five endpoint values. Each witness tree attains the same exact value as the Bellman minimum at both endpoints of its stated interval.

For each fixed tree T, C_T(z) is affine in z. Thus the global optimum F(z)=min_T C_T(z) is concave. On an interval [l,r] whose corresponding witness T satisfies C_T(l)=F(l) and C_T(r)=F(r), concavity yields F(z) >= the chord connecting those endpoints = C_T(z), while existence of T yields F(z) <= C_T(z). Equality follows for all real z, irrational included.

The four open intervals have distinct slopes -16,-28,-45,-141. A fixed tree contributes a single affine line; a finite fixed-tree menu achieving the optimum on all four open intervals needs a separate cost type for each slope. The four witness trees achieve the minimum cardinality.

## Scientific comparison and next question

At shared discount 1/2 for q32,q34, EC49FSD proved eight phases. The present shared discount 1/4 gives four phases, including a short exact phase (1/4,101/384). This is a new certified bifurcation target for variable shared discount s. The theorem applies to the finite internal BRC model with uniform 141-profile prior only; it does not cover the full (a,b,z) domain or imply an external physical calibration. The underlying P000 and named joint-observer provenance are unchanged.

Next: determine precise shared-discount bifurcation walls between s=1/4 and s=1/2, then free a and b separately to classify the three-dimensional optimum phase complex. No formal Task, CLAIM, Result, Review or project mathematical admission is asserted by this portable research file.
