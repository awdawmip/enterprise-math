# Fixed R₄: sharp maximum observer order at budget 19

For the fixed family R₄ and old dictionary P,
**Ω₁₉(R₄) = Ω̂₁₉(R₄) = 1,290,240**.
With the previous results, there is exact doubling from budgets 11 through 19. The proof leaves open whether a 19-slot cover omitting 5 or 13 exists, and does not give complete minimal prime support, density, or the least exact-cost-19 root.

## Omission branch: high orders are impossible even without full classification

Use the [original 36 holes and weighted capacity setup](https://github.com/awdawmip/enterprise-math/blob/6f27a670c11f9791099deb87d1d9066b7b268d2d/research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/REPORT.md). If both 5 and 13 are omitted, work on the corresponding even exponents; when just one is omitted, work on the parity missed by the retained basic prime. Enumerate fixed extras and the finite low-period groups as before. Reserve one slot for a hypothesized raw order d > 10,080. On n = n₀ + sz with s = 2 or 4, its period h = d/gcd(d,s) satisfies h > 10,080/s. With base period L and g = gcd(h,L), the relative period m has lower bound ⌊10080/(sg)⌋+1. Therefore the maximum weighted hit capacity is the largest weight in any one residue mod g divided by that lower bound. Charge its full capacity even if previously removed phases at periods 11 and 13 would reduce it. A high-order class with no hits in this parity still consumes the slot. The standard weighted capacity inequalities apply to the other slots.

All 774, 2,855 and 1,482 refined cases across 41 fixed-extra groups are exhausted. Thirteen have no available exceptional slot; the other 5,098 yield exact strict contradictions. The finite reduced-period-17 prime inventory used by the checker is complete. Thus whenever a complete cover uses at most 19 new primes and omits either basic prime, each new prime used in it has raw order at most 10,080. This is a bound on that branch, not a nonexistence proof.

## Branches containing both basic primes

The [normalization and private-point arguments](https://github.com/awdawmip/enterprise-math/blob/83ca339158625f3143bd8d820c0aa0ab1e9d7b8f/research_notes/portable_direct/riesel_r4_sixteen_seventeen_sharp_20261125/REPORT.md) apply with expanded budgets:

* In the all-shared branch, the 17 remaining classes have periods prime to 3 on v=(n−8)/12. The digit-weight budget is 16, so include prime 17 when generating the relative periods. The exact capacity screen keeps 137 of 220 possible periods and the largest surviving period is 44,800, hence raw order at most 537,600. A second direct period enumeration gives the identical set.
* In the split branch, the same-root replacement gives both 19 and 73, leaving up to 15 tails on n=32+36w. The weighted private-point screen and exact finite search exhaust 30,669 high-period private-point cases across 233 branches, for h>35,840. Each of two traversal orders excludes every case, with matching counts in all 42 periods and zero survivors; the node totals are 1,832,204 and 1,729,593, respectively, with at most 257 sampled witness points. Largest candidate period 430,080 and largest joint period 5,230,697,472,000 are within the exact integer range. Thus raw order is at most 36·35,840 = 1,290,240.

The [lower construction](https://github.com/awdawmip/enterprise-math/blob/2ae5de00bf7e8f1e2571ef5666e95f82a25dc429/research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md) matches with 5,040·2^(19−11). Each relevant odd coordinate needs only a² mod q; either root residues or future values determine it since 2 is invertible modulo q. Thus both maximum observer orders agree.

## Reproduction and scope

[Scripts and frozen receipts](https://github.com/awdawmip/enterprise-math/blob/660f791ed86d245524e32610ee73bbb65db38085/research_notes/portable_direct/riesel_r4_nineteen_sharp_20261125/reproduction.json). Extract the named UTF-8 files. Run `node basic-omission-high-bound.js`, `node shared-order-capacity.js`, `node high-exclusion.js 35840`, and `node high-exclusion.js 35840 reverse`. The first two were rerun at archive time and match the certificates; the archived forward/reverse split receipts agree for each period. This is author-side scientific evidence, not a new formal Result, CLAIM, or independent Project Review.
