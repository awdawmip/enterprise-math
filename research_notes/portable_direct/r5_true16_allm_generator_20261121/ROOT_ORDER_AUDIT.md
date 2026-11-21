# R5 root-order dependency audit after the genuine-intersection correction

Date: 2026-11-21. Status: EXACT MASK ENUMERATION + COMBINATORIAL PROOF / AUTHOR_CHECKED / NOT_REVIEWED. Same frozen 101-price scalar R5 event sets and previous corrected mathematical input.

Let M_d={p in {214,...,314}: d divides p}. For a nonempty event mask I, the pole order at a primitive dth root is bounded above by
r_d(I)=|M_d \ union_{i in I} S_i|,
since every price in the event union has bounded multiplicity while all prices outside the union retain their geometric denominators. The actual order can be lower through numerator cancellation. Exhaustive enumeration of the 31 masks yields the following upper-order classes.

| d | |M_d| | maximal-order masks (binary integer) | masks at one lower order |
|---|---:|---|---|
| 11 | 9 | 1 (E0 only) | 2,3,4,5,6,7 |
| 13 | 8 | 1 (E0 only) | 2,3,4,5,6,7 |
| 16 | 6 | 1,2,3,4,5,6,7 | 16,17,18,19,20,21,22,23 |
| 17 | 6 | 1 (E0 only) | 2,3,4,5,6,7,16,17 |

Each mask bit 2^i means E_i is selected. The companion exact program enumerates the full frozen universe and all 31 masks, checks these results, and emits the complete order table.

**Structural consequence.** At primitive orders 11, 13, and 17, the top possible pole order comes solely from the single event E0. Its contribution is not altered by a false multi-event-intersection simplification. Therefore the previously reported *leading-pole* formulas at these three orders are isolated from that specific intersection mistake, subject to the separate validity of each original single-event calculation. In contrast, for the next Laurent order, multiple-event masks become eligible, so the existing universal next-order claims at 11 and 13 and next-order 17 calculations require genuine event-specific constraints. At primitive 16, seven masks all reach maximal order, which explains why the original all-threshold factor formula failed.

The new universal primitive-16 theorem at immutable Enterprise Math commit 5a1e74418561d46d9079652293b9af1703963ad8 already handles all seven genuine masks. The full exact minimum-period formula at O_m(N^4) remains unresolved until affected lower-order Laurent coefficients and relevant higher orders are recomputed using true intersections.

This is a denominator-order structural audit, not an independent reproduction of the older leading Fourier coefficient vectors. It preserves P000, frozen source, author attribution and NOT_REVIEWED status.
