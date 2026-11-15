# R762BP — Oriented triad partitions, exact BRC observer fibers, and equivariant selection obstruction

**Date:** 2026-11-16 (Asia/Shanghai). **Task:** RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. **Status:** author-proved and exact finite checked; independent review NOT_REVIEWED; conditional incidence-network mathematics, not a native TRIADIC_CLOSURE_E admission or Result.

## Sources and frozen model

Scientific task pins, unchanged: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json, definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md, and definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md. The task itself is pinned at research_tasks/RS_X6_TRIADIC_CLOSURE_DYNAMICS_20260906.md. Follow the previously proved R762BO three-Port directed-incidence candidate (PR #2514, immutable 0b6618afaf157e84dc3258b225b1c118aeb1ad42): its oriented 3-Port Link is an internal force-incidence relation, never a zero-displacement 3-step spatial walk. P000 fixes triadic arity and internal 120-degree PERP_E, not a complete Link-admissibility or rotation-update predicate.

For an integer k>=1 let n=3k distinct **labelled force Ports**, and let B_k be all permutations sigma of {1,...,n} with every cycle of length exactly 3. A cycle (a b c) stands for the directed internal Links a->b, b->c, c->a and is unchanged by cyclic choice of its starting vertex. The k disjoint cycles form an **unordered** composite triadic decomposition. Every Port has one equal positive quantum; no signed force cancellation is asserted. For the actual native X6 instantiation use k=2, n=6, one fixed sign and one force quantum on each of six distinct axes; k>2 is an abstract port-family extension, not extra native spatial axes. A sign-decorated six-Port candidate additionally attaches one independent sign to each named Port while retaining the full permutation.

**Typed BRC carrier:** use the finite explicit labelled positive-rational branch object F=sum_(sigma in B_k) [sigma] with unit weight 1/1, and its exact pushforward by a declared observer. Here [sigma] carries the entire cycle permutation, Link directions and labelled provenance. The count is a positive multiplicity, not a physical mass or signed-force balance. This is the finite explicit-branch type described by definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json. No ordinary matrix propagator, trigonometric computation, or native residual attribution is involved.

## Theorem 1 — Exact oriented triad-decomposition count and symmetry

For every integer k>=1,

    |B_k| = (3k)! / (3^k k!).

The action of S_(3k) by conjugation is transitive. The stabilizer of any single sigma in B_k is the wreath product C_3 wr S_k and has order 3^k k!.

**Proof.** Partition 3k named Ports into k unordered triples: (3k)!/((3!)^k k!) choices. Each triple has (3-1)!=2 cyclic orientations, giving (3k)! 2^k /((3!)^k k!)=(3k)!/(3^k k!). Any two permutations with common cycle type 3^k are conjugate by relabelling; a commuting relabelling rotates each of the k cycles independently (3^k choices) and permutes cycles (k! choices). All such choices commute, exhausting the stabilizer.

For native six-axis one-force-per-axis X6, |B_2|=40, with stabilizer order 18 under S6. No decomposition is fixed by the whole S6. Thus any deterministic single-decomposition selector using only the unlabeled six-force population and respecting full S6 equivariance is impossible: equivariance at an S6-fixed input would force an S6-fixed output, while the orbit has 40 members. Selecting a unique decomposition requires extra Port/Link/history decoration, restriction of allowed symmetries, or a non-deterministic/branch-family output.

## Theorem 2 — Exact single directed-Link fiber

Fix distinct named Ports a,b and declare the observer statement sigma(a)=b (the directed Link a->b exists). Then exactly

    L_k = (3k-2)! / (3^(k-1) (k-1)!)

branches satisfy the observation. If only the unordered fact that a,b belong to the same triad is observed, exactly 2 L_k branches remain.

**Proof.** Choose the third Port c in the cycle containing a->b, in n-2 ways. That cycle is then necessarily (a b c). Arrange the remaining 3(k-1) labelled Ports into disjoint oriented 3-cycles: (3k-3)!/(3^(k-1)(k-1)!) choices. Their product equals L_k. If the observation says only that a and b lie in one triple, there are two orientations of that triple, hence 2L_k. These cases are disjoint.

Consequently for n=6 the BRC fiber over a named edge a->b contains exactly 8 distinct labelled branch states, and the same-triad but direction-forgotten observer contains 16. The full directed-Link query family {sigma(x): x in {1,...,n}} separates all branches. Hence preserving all future named Link queries after observing a->b requires at least ceil(log2 8)=3 bits for the hidden branch index; a fixed total-mass/count-only projection of the eight unit-weight branches does not distinguish those individual branches.

When signs on a,b are revealed and the remaining four signs are independent attributes, the joint observer fiber on X6 contains exactly 8*2^4=128 full sign-decorated branches. If future named Link and sign queries are allowed, its minimal lossless fixed-length binary index requires 7 bits. This is a conditional *information-theoretic* lower bound and a constructive upper bound (enumerate the finite fiber), not evidence that physical X6 admits each sign assignment.

## Theorem 3 — Exact carrier and admitted-set dichotomy

On fixed equal-sign six-Port input with no additional structure, the S6 action on B_2 is transitive. If an eventual **candidate** Link-admission subset A of B_2 is required to be invariant under the entire S6 relabelling action, then A is either empty or all 40 branches. Proof: an invariant subset of a single transitive orbit is a union of whole orbits. This sharpens the outstanding native question: to admit only some oriented decompositions while retaining S6 covariance, the event predicate must take additional transforming state/fields as input (e.g. signed Port labels, a Link/history decoration, a selected slice, or a physically justified restricted rotation group). It cannot be implemented as a nontrivial invariant Boolean filter on unadorned B_2 alone.

This is **not** a proof that all 40 branches satisfy native TRIADIC_CLOSURE_E: the native signed Cell/Link/Port admissibility predicate and V17/V29/V39 transport remain to be sourced and checked.

## Exact computation and scope

The companion Node.js checker builds the typed explicit BRC branch carrier recursively by choosing the least remaining Port, its two triad partners, and both cyclic orientations. Every permutation occurs once. It checks k=1,2,3: counts 2,40,2240; named edge fibers 1,8,280; same-triad fibers 2,16,560; n=6 exact full S6 conjugacy orbit size 40, stabilizer 18, 28,800 conjugation-preservation checks, five outgoing named Link histogram bins of mass 8 each, and 128 distinct fixed-visible-sign branches. No floats or approximate arithmetic are used. The k=3 calculation validates the abstract combinatorial identity only; six native spatial axes have not been expanded to nine.

Run: node R762BP_BRC_TRIADIC_PARTITION_VERIFY.js R762BP_BRC_TRIADIC_PARTITION_EVIDENCE.json. The output JSON records all exact counts. Theorems 1–3 have complete combinatorial arguments independent of the finite tests.

## Subsequent discriminating question

Read the exact frozen and authenticated native signed Cell/Link/Port TRIADIC_CLOSURE_E admission predicate and admissible V17/V29/V39 updates. Determine whether its event state includes (1) a directed 3-cycle Link record, (2) one or multiple simultaneously permitted decompositions for six quanta, (3) a sign/quantum rule, and (4) an actual rotation subgroup. Restrict B_2 to the admitted event set before claiming a physical BRC observer fiber. Carry the labelled branch identifiers and their multiplicity until a context-typed future-observer descent is proved. Preserve the R762BO odd-path parity theorem and R762BJ–BM coordinate observer theorems without conflating their observers with this candidate force-incidence family.


## Supplementary Theorem 4 — Complete signed S6 orbit classification

Equip each of six distinct named Ports with an **independent sign** in {+,-}, while retaining the oriented two-triad decomposition sigma. The signed candidate carrier has |B_2|*2^6=2560 labelled states. Define the multiset (u,v), 0<=u<=v<=3, where u and v count positive signs on each of the two oriented three-cycles.

**Theorem.** These unordered pairs (u,v) classify the S6-relabelling orbits exactly. There are ten orbits; their sizes are:

| sign-count pair | orbit size | stabilizer order |
|---|---:|---:|
| (0,0) | 40 | 18 |
| (0,1) | 240 | 3 |
| (0,2) | 240 | 3 |
| (0,3) | 80 | 9 |
| (1,1) | 360 | 2 |
| (1,2) | 720 | 1 |
| (1,3) | 240 | 3 |
| (2,2) | 360 | 2 |
| (2,3) | 240 | 3 |
| (3,3) | 40 | 18 |

**Proof.** For each fixed oriented two-cycle decomposition, if u<v the sign allocations are 2*C(3,u)*C(3,v); if u=v they are C(3,u)^2. Multiply by the 40 underlying sigma values. These cases are disjoint and sum to 2560. Any two sign configurations within a single oriented 3-cycle with a fixed positive count are related by a cyclic rotation of the three positions; consequently any two decompositions with equal unordered sign-count pairs are related by an S6 relabelling, allowing the two cycles to be interchanged. Orbit-stabilizer yields the displayed stabilizers. In particular, the (1,2) signed structure has trivial S6 stabilizer. The full signed carrier has exactly 2^10 possible S6-invariant Boolean admissibility subsets: a candidate native predicate may now distinguish entire signed orbit types without losing label covariance. Which, if any, are physically admitted remains an independent P000 force-law and V17/V29/V39 question.

**Exact extension check.** The checker enumerates all 2560 sign-decorated branch records; groups their sign-count types; verifies all ten orbit counts; and explicitly conjugates one representative from each class by all 720 S6 permutations (7200 transformations), confirming the full predicted orbit as a set. This is a source-preserving typed candidate check, not a native force computation.
