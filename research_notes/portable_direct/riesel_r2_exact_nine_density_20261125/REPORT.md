# R₂ exact ninth-cost density and fully factored observation support

The relative natural density of roots in the fixed R₂ family whose additional cover cost is exactly nine is

**0.000000027661088300840075588637686306409054973190168533…**

This is approximately one in 36,151,868 R₂ roots. Its disjoint components are:

| Root event | Relative natural density |
|---|---:|
| Exact cost nine with a dictionary using only orders through 840 | 2.5984537725335383279458438479310173225… × 10⁻⁸ |
| Exact cost nine with no low-order dictionary, so order 1260 is necessary | 1.6765505755046923091792478270988817478… × 10⁻⁹ |

Among roots supporting an inclusion-minimal ninth-budget dictionary containing order 1260, **96.41533418186368766…%** actually need that order. The last published interval is now replaced by the exact fraction in the companion certificate.

The 69-digit order-1260 cofactor splits as

`15169173997557864184867895400813639018421 × 17369459529909057773233442461`.

These are P41 and P29 in the Cunningham Project's entries 2,630L and 2,630M, respectively. The replay independently checks their exact product, order 1260, and complete recursive Lucas primality certificates. With the three previously known order-1260 primes and the 97 low-order primes, the exact minimal support has **102 primes in R₂** and **104 primes in R₁**. The two extra primes are 433 and 38737, as in the necessary-coordinate theorem. Their corresponding squarefree observation moduli have 3,265 and 3,289 bits, or 983 and 991 decimal digits.

## Reduce every split-phase cover to the same remaining phase

After the forced primes 5 and 13, let the residual exponent variable be v. The 13 target residues are modulo 35. A tail with period divisible by 3 covers only a single v mod 3 phase; the others are shared-phase tails. A minimal split cover has at least one dedicated tail in each phase. Otherwise the shared tails alone would cover all target points in the phase lacking dedicated tails, and CRT with the modulus 3 would extend that coverage to every phase. The dedicated tails would then be redundant.

In any such dictionary replace all dedicated tails in phase 0 by 19, and all dedicated tails in phase 1 by 73. They are available throughout R₂ and cover those entire phases. This uses no more primes, preserves coverage and leaves phase 2 unchanged, even if the original dictionary used neither or only one of these primes. Therefore it suffices to count shared-only dictionaries and split dictionaries with both fixed primes, on the same root space.

For two fixed primes, only v=2+3w remains, with room for five further tails. The proved finite order universe has local period h=f/gcd(f,3), where f is the v period. In the low-order universe, collect all distinct free primes implementing the same h. A local residue b mod h means v=2+3b mod f separately for each such prime. Distinct local residues cannot use the same prime, because these v residues are distinct. The fixed 38737 gives the extra odd-w slot and still costs a tail when selected.

Enumerate all inclusion-minimal local covers up to five tails over the full common period 5,040, containing 1,872 target points. An uncovered point forces selection of one of its covering slots. To count each unordered cover once, branch on the first such selected slot, excluding earlier options in that branch. A chosen slot losing all private points cannot occur in a minimal completion. Group capacity bounds are applied, and every accepted set is fully checked. The 107 local slots yield **3 three-tail, 21 four-tail and 215 five-tail** geometries. Two enumeration orders match. Projecting all published split eight-budget templates to these local period groups gives exactly the same 24 smaller geometries.

## Exact low-order union and global subtraction

A slot condition is the disjunction over its eligible primes in that residue color. The used color weights are two per residue class and q−2k for all remaining values at a prime q with k relevant colors. The weights multiply over distinct primes by CRT.

Let W be the low-order two-fixed-prime event, C the previously proved shared-only event, and E the full ≤8 event. Split E as E_s and E_c according to those two source families. The exact computation counts W minus E, C minus E and their intersection. To keep the decision diagrams small, order first the 18 primes with periods 7, 10 or 35, which are the only shared variables of the W and C sides. Once those shared variables are assigned, the two exclusive supports are independent. The weighted pair recursion retains exact products on this disjoint part and never constructs a full union graph. This gives P((W∨C) minus E) without assuming different dictionaries represent different roots. The implementation matches the already published exact fractions for E, C and C minus E.

## Exact high-order gain

The known top-order geometry has both fixed primes, two long columns and three short cells. For a nonempty high-prime occupancy mask H, define T_H to require the two long columns and low-order occupancy of every short cell outside H. The top-order event conditioned on H is exactly T_H. Use the same low-order decision diagram to count g_H=P(T_H minus (W∨C)). This excludes every low-order substitute, including any eight-budget one.

The five high primes are independent of the low ones. Each has three distinguished cell colors of weight two and one remaining state of weight p−6. Convolve these eight mask states exactly, then sum P(H) g_H. The seven g_H agree in groups by the size of H, which the certificate checks. This is an exact disjoint addend to the low-order exact-nine density. Every low-order cover, every top-order substitute and every root of cost at most eight is thereby accounted for.

## Sources and scope

- [Cunningham Project main table, 2,630L and 2,630M](https://homes.cerias.purdue.edu/~ssw/cun/pmain1126.txt) and [Appendix A prime expansions](https://homes.cerias.purdue.edu/~ssw/cun/appa1126.txt).
- [The R₂ low-order predicate](https://github.com/awdawmip/enterprise-math/blob/2b80afd7bbb034d1b3ef4fffb4491824d2bee6fb/research_notes/portable_direct/riesel_r2_ninth_predicate_20261125/REPORT.md).
- [The R₂ exact eighth-budget templates](https://github.com/awdawmip/enterprise-math/blob/89b9571189e2c8b576f4972f3775961f7cf01836/research_notes/portable_direct/riesel_r2_eight_exact_20261125/REPORT.md).
- [The shared-only union and its exact E₈ intersection](https://github.com/awdawmip/enterprise-math/commit/940f6b84a312c1b1e8735456f1d7a3707030c7a3).
- [The top-order short-cell classification](https://github.com/awdawmip/enterprise-math/blob/0fc72cdda05ca8d3d2d3da048b65476d4d16da6f/research_notes/portable_direct/riesel_r2_top_order_20261125/REPORT.md).
- [Minimum observation support theorem and full order universe](https://github.com/awdawmip/enterprise-math/blob/3138e445ab326a3162c0999cdd0d2dfa3d64ecea/research_notes/portable_direct/riesel_minimal_wide_support_20261125/REPORT.md).
- [Exact 97-prime low inventory](https://github.com/awdawmip/enterprise-math/commit/e45eb9dbc459360b87996a824d0ed0f5b043da8a).

These are scalar exact calculations in the fixed R₂ model and do not assert formal project Review.

## Reproduction checks

Two local template orders enumerate the same 239 minimal geometries. Two prime orders inside each period group independently produced all the same exact fractions, with 678,887 and 677,915 decision nodes respectively. The three independently published E₈, C₉ and C₉ minus E₈ fractions agree in both numerator and denominator. A direct high-coordinate inclusion-exclusion formula independently matches all eight mask weights. The exact gain represents about 6.0610% of all exact-cost-nine R₂ roots. The complete result and reproducible replay accompany this report.

## Integrated verification

The standalone replay was rerun from the saved text and matched every exact rational field. Independently, the previously published three short-slot coefficients and low-order union were substituted into the all-five-prime inclusion-exclusion formula; the reduced gain and total fractions both matched exactly. The archived exact result supersedes the remaining high-factor interval in the earlier R₂ report.
