# X6 R25 — Minimum-threshold consumer theorem for repeated signed-Port replenishment

Date: 2026-11-19. Task RS-X6-NATIVE-TIME-DYNAMICS, immutable taskbook @f41c2690daba467ecbde99615a1337e67be46ffd, P000 V5 @a72226e2430ffa4786321ac86e7f0c599d5f0389.
Status: CONDITIONAL_AUTHOR_PROOF / EXACT_BOOLEAN_BRC_PASS / NOT_REVIEWED / NATIVE_EVENT_ADMISSION_PENDING.
Predecessor: R24 source/signed-Port repeatable two-step resource grant quotient; original Research2 source lineage, historical EM-X6-214D9C. This publication is not a native CLAIM/PROGRESS/Result.

## Controller and observer

Retain all R24 hypotheses: m independently moving intact triadic B_i carriers, each alternating +E1,-E1 on its own two-cell lane, with a hidden conserved frame bit theta_i in {0,1}; at most u unit shared-credit grants on the first u completed return cycles if theta_i=1. No negative credit and all B movements remain legal independently of theta. Replace R24's single consumer by any finite family of distinct single-use intact A_j consumers on disjoint lanes, each with a positive integer resource price q_j. Each successful A_j action deducts q_j from one global pool, capped at Q>=max_j q_j; none of the A_j events changes B sources, grant counters, frame choices or the enablement of other consumers except through the single numeric credit balance. Multiple consumers may spend and later receive replenished credit through subsequent B return cycles. All action labels preserve source and signed Port. Let q*=min_j q_j>0 and t=ceil(q*/u).

## Theorem R25.1 — additional consumers add no future-language classes

On the complete initial public observation fiber of 2^m hidden frame vectors, for every h<=2q* every successful source/Port future language is identical. For every h>=2q*+1, two frame vectors yield the same full successful future language if and only if either (a) both have fewer than t frame-one sources, or (b) they have exactly the same frame-one source support S. Therefore

    C(m,u,{q_j})=1+SUM_{s=t}^m binomial(m,s)
    b_min=ceil(log2 C) bits

at and above the horizon 2q*+1; the sum is empty if t>m.

**Proof.** Any consumer requires at least q* positive grants. Each requires a preceding B_i^+ and B_i^- pair, so no A action can occur in <=2q* events; B-only words are independent of theta. For any support S with u|S|<q*, the total available credit during the entire run is at most u|S|, irrespective of consumer actions. Every A_j is forever disabled. Thus all these supports have the identical full B-only language.

For every support with u|S|>=q*, consider only the cheapest consumer A_* at price q*. As in R24, each q*-multiset of B excursions with per-source multiplicity <=u and support within S yields an exact signed-Port witness ending in A_*. Every element i of S occurs in at least one such multiset, because u|S|>=q* and u>=1. The union of supports of the successful cheapest-consumer words therefore reconstructs S uniquely at horizon 2q*+1. Hence distinct high supports are already distinguished; no later word involving any other A_j can split a singleton S-class. Conversely identical S means identical full controllers, and distinct low supports permit no A_j at any future horizon. The stated partition persists forever. Counting gives the exact bit bound. QED.

The result is deliberately about the initial-fiber observer. For intermediate states, consuming credit changes what can happen next; retaining merely S without the current resource and consumer-used state is not a valid Markov quotient.

## Consequences

1. Adding an arbitrary number of *larger-price, non-feedback* consumers does not reveal new hidden frame information, even when a first consumer spends credit and later B cycles replenish it.
2. The smallest consumer price q*, rather than max_j q_j, controls the exact earliest distinction depth and initial hidden-frame storage.
3. To gain further history discrimination from repeated spending, an event must introduce a new genuinely observer-relevant guard/feedback (for example source-sensitive cost, branch-specific Link state, or consumer influence on future B grants). Such mechanisms require their own typed native admission and proof.
4. For m=4,u=1,q*=4 the initial-fiber minimum remains one bit with any number of more expensive consumers; for u>=q*, it is m bits.

## Verification and limits

Checker x6_multiconsumer_threshold_invariance_verify_r25.js computes deterministic complete source/signed-Port labelled-language signatures with exact recursion. JSON x6_multiconsumer_threshold_invariance_results_r25.json covers 30 parameter sets m=1..3, q*=1..2, q_max=q*..3, u=1..2, all 2^m initial theta assignments, and compares both the first horizon and later horizons; finite tests PASS. The displayed theorem follows from its symbolic proof for any finite family of positive-priced consumers. The proposed grant/cost and Port guards remain conditional; P000 fixes whole-triad closure and native directions but does not admit this replenishment law. No independent scientific Review is claimed.

## Next frontier

Seek an actual native Link/Port event admission and the smallest feedback-guarded counterexample to R25 under a genuinely changed controller, with the exact extra history coordinate stated and preserved. This will test whether the real X6 transition requires richer Markov state than the one-resource grant-support quotient.
