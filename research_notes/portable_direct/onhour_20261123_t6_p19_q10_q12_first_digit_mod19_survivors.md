# T6 / p19 orders 10–12: exact first-digit congruence census and residual loss

**Author status:** AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED (2026-11-23 Asia/Hong_Kong). Mother task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`; this is a necessary-congruence census, not a full mixed-congruence or lower-prime-completion result. Original research lane SID `MCP-082892eb480e45dea6d4b9fcc0491034`, no current T6 winning CLAIM verified.

## Mathematical condition actually tested

Given two finite exponent shapes A and B, side masses <=2331, matching H0,...,H6 implies matching reciprocal power sums S1,...,S6. By the separately proved p19² cancellation lemma, every 19²-divisible denominator has the same multiplicity and may be cancelled. For each remaining denominator divisible by 19 exactly once, write a=19c with 19∤c. Multiply S_k(A)-S_k(B)=0 by 19^k and reduce modulo19. All denominators prime to 19 disappear from that residue. Hence for k=1,...,6:

    sum_{a in A, v19(a)=1} (a/19)^(-k) = sum_{b in B, v19(b)=1} (b/19)^(-k) (mod 19).

This is a necessary condition for the original full collision, even when lower-prime denominators are present. For vertical cofactor c=19q+r, it depends only on the residue r mod19; for q0 cofactor j=1,...,18 it depends only on j. The vertical q information is a *structural residual lost by first-digit observation*. That loss motivates a higher-digit saturated mixed congruence rather than treating separate p19-only exact H1-H3 equalities as necessary.

## Complete bounded enumeration of the necessary first digit

Retain the frozen p19 valuation-one atom alphabet: vertical q in 1..6, r in 1..18 with 19q+r smooth over primes <=19; q0 cofactor j in 1..18; exact named multiplicities, positive side mass <=2331, nondecreasing multiset enumeration, and no common p19-denominator support across the two signed sides. A vertical atom has denominator 19(19q+r), mass 19(19q+r)-1; a q0 atom has denominator 19j, mass 19j-1. Side q totals 10–12 admit precisely splits (4,6),(5,5),(5,6),(6,6) up to sign.

| q split | Full side states (A/B) | Ordered mod19 6-moment matches | Support-disjoint unordered matches |
|---|---:|---:|---:|
| (4,6) | 43,043,867 / 675 | 33,666 | **3,640** |
| (5,5) | 852,346 / 852,346 | 59,175,434 | **212,688** |
| (5,6) | 852,346 / 675 | 19,709 | **2,127** |
| (6,6) | 675 / 675 | 10,767 | **582** |

**Total necessary-congruence survivors: 219,037**, all over exact integers modulo19. In symmetric splits the oriented support-disjoint count was divided by two; same-side identical pairs automatically fail support disjointness. The counts include all admissible p19-valuation-one side configurations (without yet spending mass on lower-prime completion), hence a necessary-survivor superset under the declared frozen alphabet.

## Explicit surviving first-digit example and why it matters

A denominators = [380,380,380,380], exponent mass 1516, vertical q=4. B denominators = [741,741,741,19], exponent mass 2238, vertical q=6. Their named supports are disjoint. Every cofactor a/19 is congruent to 1 modulo19, and the two sides have four occurrences. Hence all six first-digit inverse-power congruences hold. This **does not** produce a full H0..H6 collision: higher p19 digits and lower-prime completion are unresolved.

The earlier p19 q9 valuation-one author enumeration showed zero pairs with exact equality of H0..H3 on the **isolated p19-divisible components**; that stronger equality is not a necessary condition for the entire shapes because denominators prime to19 may compensate their rational differences. Its bounded finite result remains saved but cannot be used as a global p19 q9 elimination without the original mixed-congruence condition.

## Reproducibility and next exact action

The companion C++17 checker computes all six cofactor inverse-power residues mod19, packs base19 signatures, joins exact side signatures, and filters the full named-support overlap; the JSON certificate contains the four exact counts, resource-independent parameters and the displayed modular witness. Original complete observations, high-digit lift and p19-free completion remain outstanding.

Next: preserve the 219,037 necessary survivors as a bounded input **count** (not the complete materialized list) and use the existing certified p19 saturated congruence lattice / mixed-digit resolver to test whether any lift with lower-prime completion survives under both true mass budgets. No manual queue jump or formal TASK completion is asserted. In particular, do not use the isolated exact-H013 census as a substitute for the original native mixed-congruence benchmark.

Prior inputs: `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md`, `research_notes/portable_direct/onhour_20261122_t6_p19_q9_onepower_h013_exclusion.md`, and new `research_notes/portable_direct/onhour_20261123_t6_p19_v19_squared_mod19_universal_cancellation.md`. Frozen P000/worldview and Original Source scientist scope preserved.
