# EC49FQG — Native BRC class 16943: minimal all-price optimal first-observation palettes, isolated ties and re-entry

Date: 2026-11-16. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scientific frozen commit: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab.
Previous verified frontier: EC49FQD–FQF, especially https://github.com/awdawmip/enterprise-math/pull/2531.
Researcher provenance: EM-DIRECT-E78124 / TASK_RESEARCH; Activity RA-D62DDE05DA91C7CB0E8C8919.
This is a new mathematical deduction and independently replayed audit of **inherited unrestricted Bellman endpoint certificates**, rather than another 25-anchor Bellman solve.

## Exact model and theorem

The original native BRC class 16943 contains 310 configurations inducing 141 full named-root cost profiles. The decision maker must identify the complete profile, including terminal-invisible differences, by adaptively choosing among 144 terminal observations q=0,...,143 (price t>0) and 84 named-root observations q=144,...,227 (price r>0). Let x=r/t. The full native profile and source multiplicities remain retained. U denotes the equal-weight prior on the 141 profiles; M denotes the prior assigning one unit of weight to each of the 310 original configurations. All finite complete identifying trees are allowed.

Let A_U(x) and A_M(x) be the **physical observation indices** that can start at least one globally minimum-expected-cost policy. Their exact unions over *every real price x>0* are:

| Prior | Union over all positive prices of optimal first-query indices | Count | Root actions excluded from root-level optimization |
|---|---|---:|---:|
| U | {32,34,140,142,153,161} | 6 | 222/228 |
| M | {16,23,46,59,88,93,124,131,153,161} | 10 | 218/228 |
| Both priors together | {16,23,32,34,46,59,88,93,124,131,140,142,153,161} | 14 | 214/228 |

Every listed action is actually optimal at some certified positive price. No excluded action is optimal as an initial action at any positive price for that prior. These unions are thus **minimal for preserving every possible globally optimal first-index choice**, rather than just finding some optimal tree. Pruning applies at the initial decision only; all 228 original actions remain available to subtrees.

Two additional exact phenomena hold for M:

1. **Isolated tie at equality.** Observation indices 124 and 131 are optimal first readings **if and only if x=1**. At precisely x=1, the full initial argmin is {16,23,124,131}. For every positive x unequal to 1, neither 124 nor 131 can start a global optimum.
2. **Re-entry.** Indices 59 and 88 are optimal first readings at x=17/24 and x=3, and are both strictly suboptimal at x=1. Hence global first-action optimality as a function of relative unit price can have disconnected price support in this finite BRC sensing problem.

## General affine-envelope lemma

For any finite exact identification problem with a finite action set of two positive prices, positive prior weights and a feasible complete identifying decision tree, remove strictly positive-cost noninformative reads/repeated reads along a path. Up to such deletion there are finitely many complete policies. For policy pi, let R_pi and T_pi be its aggregate prior-weighted counts of the two observation types. Then its (unnormalized) price cost is L_pi(x)=R_pi*x+T_pi and the global optimum is the lower envelope V(x)=min_pi L_pi(x).

Suppose the globally optimal cost V is affine over a closed price interval [a,b]. For every a<y<b and every policy pi optimal at y, the difference L_pi(z)-V(z) is affine and nonnegative at both endpoints. Being zero at an interior point, it must be zero at both endpoints. Consequently,

A(y) is a subset of A(a) intersect A(b).

This lemma allows all-price **necessary first-index screening** from the exact minimizing first-action sets at finitely many adjacent Bellman breakpoints. Endpoint ties are separately preserved, so isolated optimizers are not discarded.

## Proof of the exact BRC palettes

The inherited EC49FQD and EC49FQE full Bellman proofs provide the complete globally optimal affine value functions for U (10 positive breakpoints) and M (15 positive breakpoints). EC49FQF additionally provides the 228-component forced-first objective vector at each breakpoint, with 25 complete machine certificates and exact checks at x=1/4 and x=4. The new verifier checks exact certificate hashes, all saved Bellman first-query vectors, reconstruction of original BRC readouts, and full tree replay on all 141 profiles (310 source configurations by their exact multiplicities).

From the 10 U breakpoint certificates, the exact union of initial argmin sets is {32,34,140,142,153,161}. From the 15 M breakpoint certificates, the corresponding union is {16,23,46,59,88,93,124,131,153,161}. The affine-envelope lemma excludes every other index at all open **finite** cost phases. In every such open phase the necessary allowed set has cardinality at most two; its explicit interval-by-interval data are saved in the machine certificate.

**Low tail.** For x0=4/7 (U) or x0=26/71 (M), the earlier certified pure-root optimal cost is R0*x with R0=362 (U) or R0=1033 (M). For any complete policy and 0<x<x0,

L_pi(x)=(x/x0)L_pi(x0)+(1-x/x0)T_pi
          >= R0*x+(1-x/x0)T_pi.

Thus optimality requires no terminal readings and a root-only optimal tree also optimal at x0. The verified first-query set at x0 is {153,161}; the separate exact x=1/4 run has both actions as pure-root optimal witnesses. Hence both priors have precisely {153,161} at all prices below their respective low breakpoint.

**High tail.** Two terminal-invisible doubleton response fibers have positive mass one each. Distinguishing their members requires an aggregate of at least four named-root reads under either prior. At x=3 the unrestricted global optimum is 4*x+296 (U) or 4*x+688 (M) and is attained with exactly four aggregate named-root reads. Hence these formulas persist for all x>=3. Every globally optimal tree at x>3 must use exactly four root reads and be optimal at x=3. At x=4 the full Bellman initial sets are {32,34,140,142} (U) and {16,23,59,88} (M). Each x=4 optimal tree has exactly four root reads and therefore remains globally optimal for every x>=3. These exact tail sets equal the x=3 sets, proving the claimed high tails.

**Alias check.** All 228 native observations were independently reconstructed from the original frozen configuration and root-cost data. They induce 209 distinct response partitions and 15 non-singleton duplicate-partition classes (19 extra physical action indices), with no cross-type alias. All breakpoint-optimal initial indices have singleton partition classes. Therefore the original solver's canonical-partition optimization hid no additional physical initial minimizers. The exact 6/10 minimal physical palettes follow.

## Isolated tie and re-entry proofs

At x=1, M's complete forced-first Bellman argmin is {16,23,124,131}. No other certified breakpoint contains 124 or 131. For every finite open price phase adjacent to x=1, the intersection of neighboring optimal first-index sets is {16,23}, and all other phases/tails exclude 124 and 131. Their global first-action optimality therefore holds **only at x=1**.

The exact M first-index sets at x=17/24, 1 and 3 are respectively {59,88,153,161}, {16,23,124,131} and {16,23,59,88}. Both 59 and 88 are therefore witnessed as optimal, nonoptimal, and optimal again as x increases.

This is a precise finite exact-identification result for the declared native BRC observation interface. It is not a theorem about the entirety of P000 or every BRC class, and no observer quotient, unseen spatial collapse or alteration of the frozen science was used.

## Evidence, validation scope and next research

Frozen original source SHA256:
- master: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e
- root-cost CSV: a61a3ee4d2f13f9d216f52cd3529c72d395c1250bfb1d7ae96a1adf5a6837c1f

An independent verifier recreated all 228 query vectors and 209 partitions, audited 25 prior unrestricted Bellman endpoint certificates and 2 tail certificates, then independently replayed 54 saved decision trees. It validated every reported full-profile identification and exact aggregate integer cost, yielding EC49FQG_PALETTE_AND_REENTRY_CHECK_PASS. The unrestricted Bellman lower bounds at the inherited anchors are reused from EC49FQD–FQF, and no fresh 25-anchor recursion is claimed.

The complete evidence archive EC49FQG_GLOBAL_FIRST_ACTION_PALETTE_COMPLETE_20261116.tar.xz contains original frozen inputs, 27 full machine certificates, predecessor exact optimizer, new independent raw-observation verifier, full machine output, proof and execution log plus per-file SHA256 manifest.

The next questions are (a) sufficiency of the two candidate indices inside each open affine phase, not only their necessary membership; (b) structural classification of isolated/equality and re-entry optima under a continuously changing prior; and (c) root-level screened acceleration for additional BRC classes while keeping all branch observations and provenance. Status remains AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.

Formal task topic RS-EC49AS was not found as a current immutable Task publication in the native continuation receipt for this run; GitHub research publication is independent portable output, not an assertion of CLAIM, Result or Review authority.
