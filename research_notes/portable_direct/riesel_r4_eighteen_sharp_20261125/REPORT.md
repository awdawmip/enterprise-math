# Fixed R₄: sharp maximum observer order at budget 18

For the same fixed 74-channel family and old dictionary as the preceding results,
`Ω₁₈(R₄) = Ω̂₁₈(R₄) = 645,120`.
The exact maximum-order sequence doubles at each step from budget 11 through 18. This result does not give the complete minimum prime support, the density of exact-cost 18 roots, or the least such root.

## 1. Forcing the basic pair

The earlier unweighted omission argument no longer closes at budget 18. Retain its exhaustive parameter enumeration and give the 36 holes in the original `u = n/2 (mod 105)` nonnegative weights, per fixed-class branch. For a remaining class of relative period `m`, the capacity is the largest compatible weight sum on any residue, divided by `m`. The exact checker treats the possible removals at periods 11 and 13 by CRT: where a remaining period is coprime, a removable phase has exactly its relative fraction of mass; otherwise charge it conservatively. Where the reduced-period-17 inventory can affect the bound, enumerate its possible usage separately. The five eligible primes there are 131071, 43691, 137, 953 and 26317, checked by primitive products and primality; raw orders are 17, 34 and 68.

The integer certificate rejects all 8, 376 and 271 refined cases in the double-omission and two single-omission parity scopes. The respective maximum capacity/demand ratios are `8741052747/9350000000`, `1067262199/1100000022` and `1213/1292`. All are strictly below 1. This proves 5 and 13 compulsory at budget 18 as well as the previously known smaller budgets. The numerical means of selecting weights are not assumed in the verification.

## 2. Cover types and the upper bound

Use the [previous reduction and private-point digit bound](https://github.com/awdawmip/enterprise-math/blob/83ca339158625f3143bd8d820c0aa0ab1e9d7b8f/research_notes/portable_direct/riesel_r4_sixteen_seventeen_sharp_20261125/REPORT.md). On `v=(n−8)/12`, a cover with dedicated mod-3 phases can replace two phases with the fixed 19 and 73. If a phase had no dedicated class, the shared classes would already cover it and, by CRT, all phases. Therefore the existence predicate splits into a normalized split branch and a separate all-shared branch. Replacement preserves the root and does not raise cost; it is not necessary to preserve every original dictionary.

* Split branch: at most 14 tails on `n=32+36w`. The base holes are `w mod 35 in {0,3,5,8,10,15,21,23,26,28,30,31,33}`. For each choice of active fixed tails and complete mod-seven rows, apply the private-point digit bound at the common base period and the period-dependent capacity screen. On the resulting finite representative set, a candidate with private point must leave it uncovered by all competitor classes. Search finitely many residual witnesses in the remaining slots, retaining a relaxation even for candidate orders without known available primes. A contradiction in this relaxation excludes the full cover. Both orders reject all 27,842 high-period private-point cases, with identical counts in each of 40 tested periods and zero survivors. Each covers 233 branches that reach the high-period search. Forward/reverse total search nodes: 1,465,285 and 1,395,574; at most 249 witness points. Thus `h ≤ 17,920`, and raw order is at most `36h ≤ 645,120`. The largest checked combined period is 435,891,456,000.
* All-shared branch: at most 16 classes on the `v` variable, with periods coprime to 3. The period/digit capacity screen leaves 103 of 183 candidates, with effective period at most 22,400. Thus raw order is at most 268,800. These are admissible candidates for an upper bound, not a claim that each occurs.

The geometry receipt separately records 1,152 old-dictionary holes in a 6,720 exponent period, all even; the 20,160-exponent normalized-tail check had zero discrepancies.

## 3. Matching lower bound and the observer interpretations

The [ordinary-root CRT switch](https://github.com/awdawmip/enterprise-math/blob/2ae5de00bf7e8f1e2571ef5666e95f82a25dc429/research_notes/portable_direct/riesel_r4_twelve_observer_lower_20261125/REPORT.md) gives lower bound `5040·2^(18−11) = 645120` for both observation types. On the upper side the classification needs only a finite set of odd coordinates of raw order at most 645,120. The coverage predicate at such a coordinate is a function of `a² mod q`, recovered equally from a root coordinate or from any one future term modulo q because 2 is a unit.

## Reproduction

[Source, frozen receipts and geometry crosscheck](https://github.com/awdawmip/enterprise-math/blob/37ea7118715feab970a943d0deacfb164e912eb8/research_notes/portable_direct/riesel_r4_eighteen_sharp_20261125/reproduction.json). Extract the named UTF-8 strings to files. Run `node basic-pair-weighted.js`, `node shared-order-capacity.js`, `node high-exclusion.js 17920` and `node high-exclusion.js 17920 reverse`; compare parsed outputs to the same-named frozen receipts. The archived geometry crosscheck is a separate saved result. This archive is author-side research evidence, not a new official task claim, Result submission, or Project Review.
