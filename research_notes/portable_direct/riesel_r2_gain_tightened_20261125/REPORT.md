# R₂ top-order gain | Tightened interval and complete low-order factor inventory

Let T be the event of an inclusion-minimal ninth-budget dictionary using a prime of order 1260, and L the event of a dictionary of budget at most nine whose orders are all at most 840. In the same fixed R₂ root family, the relative natural density of T minus L is in **[1.6755028689, 1.6772046413] × 10⁻⁹**. Among roots in T, this is **96.3549% to 96.4530%**. Endpoints here are rounded outward. The previous strict interval was [1.6015219825, 1.6772046413] × 10⁻⁹. The new interval is about 44 times narrower.

All low-order carriers used in the published predicate are now fully factored. The four unresolved order layers were 135, 162, 270 and 324. Their previously unresolved remainders have these exact factorizations:

| Order | Prime factors of the prior unresolved remainder |
|---:|---|
| 135 | 348031 × 49971617830801 |
| 162 | 135433 × 272010961 |
| 270 | 385838642647891 |
| 324 | 3618757 × 106979941 × 168410989 × 4977454861 |

Each possible prime factor of an exact-order carrier is 1 modulo its order. The replay exhaustively checks that arithmetic progression through the square root whenever it certifies the trailing prime. It verifies discovered primes and their exact orders, along with the reconstruction of every carrier of order at most 840. The distinct high-order unresolved carrier of order 1260 remains under the earlier strict domination bound. The complete low inventory can be used as CRT weights for the next low-order union calculation.

## Exact lower bound using 21 witness points

Use the previously proved top-order shape. The two long columns must both be occupied. The three short cells have base even lifts v=170,80,200 and all other even lifts differ by multiples of 210. Take seven lifts at each base, adding 0,210,420,630,840,1050,1260.

At an individual selected point, 19 and 73 do not hit its phase and the fixed 38737 channel does not hit the even lift. Demand that all six long-column primes avoid the short column, while still occupying both long columns. Require the selected short cell to be unoccupied by its low-order geometry primes, and all short cells to be covered by the union of low-order geometry and the three proved order-1260 primes. This ensures T. If no other low-order prime hits the selected point, the complete low-order predicate cannot cover it. This proves membership in T minus L. Additional order-1260 factors can never invalidate this witness.

To count the union over 21 points without double-counting roots, use exact inclusion-exclusion across all 2²¹−1 nonempty intersections. For each intersection impose low geometry exclusion on the short cells containing its points. For any other low-order prime of period f, if the selected point set has k distinct residues modulo f then exactly q−2k root residues avoid it. Independence over distinct primes holds by CRT. All terms have the same integer denominator, so they can be summed as integers before reduction. This includes all nine newly resolved primes, hence there is no missing lower-order slot and no approximation to the lower endpoint. A separate exact dynamic program over covered point masks agrees with inclusion-exclusion for one, two and three lifts per cell.

The upper bound retains the published event in which no all-low dictionary can fill the same geometry. Any true gain lies inside that event. As in the published proof, the unknown top-order factors are covered by six independent virtual coordinates, each having at least the true factor's weight for each of the three cells. Recompute the denominator event T from exact occupancy and use opposite endpoint divisions for the conditional interval.

The reported interval concerns the gain from order 1260. The union of low-order dictionary events and the resulting full exact-cost-nine density are separate calculations. The complete low-order prime list and exact rational bounds are emitted in the companion replay.

## Sources

- [Published top-order gain interval and original source geometry](https://github.com/awdawmip/enterprise-math/blob/97b08c28dcf4716fe9e87dfaa96fd15f396d08df/research_notes/portable_direct/riesel_r2_top_order_density_20261125/REPORT.md).
- [Full low-order predicate and admissible orders](https://github.com/awdawmip/enterprise-math/blob/2b80afd7bbb034d1b3ef4fffb4491824d2bee6fb/research_notes/portable_direct/riesel_r2_ninth_predicate_20261125/REPORT.md).

## Size of the minimal observation support

The candidate inventory contains exactly 97 distinct low-order primes across 46 nonempty layers. The existing necessary-coordinate theorem makes each a necessary prime of the full nine-budget observation modulus. There are three separately proved order-1260 primes. The unresolved high carrier is composite, by the modular base-3 witness, and has at most six prime factors counted with multiplicity because all factors exceed 10¹⁰. Its exact integer roots for exponents 2 through 6 lie strictly below it when raised to those powers. It is therefore not a prime power, so it contains at least two distinct primes. This gives **102–106** necessary prime coordinates for R₂, and **104–108** for R₁ because its minimal support has the two additional primes 433 and 38737. [Minimal support theorem](https://github.com/awdawmip/enterprise-math/blob/3138e445ab326a3162c0999cdd0d2dfa3d64ecea/research_notes/portable_direct/riesel_minimal_wide_support_20261125/REPORT.md)

## Reproduction

Run `node replay.js` to reproduce the certificate. Previously proved large prime factors are pinned from the cited inventory; the newly split layers, sorted arithmetic-progression search, exact carrier products, 97 different low primes and absence of a perfect power are checked in the replay. This is a direct, independently replayed research artifact, not a formal project Review.
