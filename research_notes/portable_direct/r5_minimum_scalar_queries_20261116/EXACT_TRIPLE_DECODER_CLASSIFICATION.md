# R5 addendum — exact classification of all minimal nonadaptive three-budget scalar decoders

Date: 2026-11-16. Input pin: `435e77af0d180eac32bd1f9c4c464bc4010b7551`.
Status: AUTHOR_PROVED / EXACT_INTEGER_FINITE_VERIFIED / NOT_REVIEWED.
Model: the frozen 954-event derived integer-coordinate indexed-center radius-two optimizer observer, with original 28 independent closure bits, restricted to K=214..954. This addendum extends `r5_minimum_scalar_queries_20261116/RESEARCH.md`.

## Exact result

The preceding theorem proves that every fixed three-query decoder of the full eight-bit quotient U must query once in each of:

- Window A: K=214..221, effective bits {3,8,9,10,27} (8 choices).
- Window B: K=223..291, effective bits {25,27} (69 choices).
- Window C: K=293..314, effective bits {15,17} (22 choices).

There are exactly 12,144 structurally eligible unordered triples. We now classify which of these are actually injective as *scalar count* maps.

**Theorem.** The three-count map

`B -> (N_B(k_A),N_B(k_B),N_B(k_C))`

determines the complete high-budget optimizer-family quotient if and only if

`k_A in {214,215,216,217,218,219},`
`223 <= k_B <= 291,`
`294 <= k_C <= 313.`

Thus exactly

`6 * 69 * 20 = 8,280`

of the 12,144 structurally eligible triples are valid exact minimal nonadaptive decoders. The other 3,864 have provable scalar collisions.

## Proof and finite enumeration

Use the prior exact optimizer-family support theorem, so the scalar counts at any K only depend on the appropriate effective bits. Denote by a the five-bit local mask in ordered bit positions (3,8,9,10,27); b the two-bit mask (25,27); and c the two-bit mask (15,17). The unique overlap of the three windows is bit 27, shared by a and b.

The exact integer nearest-center DP was rerun from the 15 pinned subset-sum coefficients, yielding exactly 538/298/229 intermediate pools, 954 indexed events with last integer coordinate 1065, and 28 disjoint length-three gaps. For each of the 32 local a masks, four b masks and four c masks, the DP returns min-cost tie counts for every budget in its window. Only integer arithmetic and rational reconstruction of the frozen event multiset are used.

The computed scalar classifications are:

| Window | Exact distinct-count result |
|---|---|
| A | All 32 local counts distinct for K=214..219. At K=220 and 221 collisions remain even when cut 27 is fixed. |
| B | All four local counts distinct for each K=223..291. |
| C | All four local counts distinct for K=294..313. At K=293 and 314 the single-cut masks c=1 and c=2 have equal counts. |

An explicit obstruction at K=220 is a=9 and a=12, with cut 27=0 in both cases. Both yield `38,336,726,601,491,749,449,844,654,080,000` optimal center sets. At K=221, a=1 and a=4 also collide with cut 27 fixed at zero. These collisions differ on bits private to A and cannot be resolved by any B/C observation.

At K=293, c=1 and c=2 both give `13,102,659,259,476,980,304,288,153,600`; at K=314 they also collide. These masks differ on the private C bits and cannot be resolved by A/B observations.

When B's four count values are distinct, it recovers (25,27). Conditional on the recovered value of 27, A must distinguish all 16 possibilities of (3,8,9,10), which occurs precisely at K=214..219. C must distinguish all four possibilities of (15,17), which occurs precisely at K=294..313. These conditions are jointly necessary and sufficient.

As a second finite check, all 256 eight-bit closure signatures were explicitly evaluated at each of the 8*69*22=12,144 eligible budget triples. Exactly 8,280 triples yielded 256 distinct count tuples. For failing examples, (214,223,293) yielded 192 signatures, (220,223,294) yielded 240, and (221,223,294) yielded 128.

## Reproducibility and scope

The two companion Python scripts recreate the exact integer event construction and budget DP, then directly enumerate the 12,144 triples against all 256 quotient assignments. They produce the JSON evidence file and classify each failing budget window. The finite scientific domain is complete for the stipulated source and observer; this is an author-side mathematical verification and has not undergone independent review.

This classification concerns exact scalar observations of the derived optimizer-family quotient. Any native X6/BRC source-path or future-operation projection requires its own typed observer preservation certificate.

## Next

Classify minimal *adaptive* three-query decision trees and whether choosing budgets based on early scalar counts improves robustness or computational cost; determine the cheapest exact decoder under explicit query-cost and numerical-bit-length models. Continue recourse/max-new-min-old K214..291 on the indexed-set observer.
