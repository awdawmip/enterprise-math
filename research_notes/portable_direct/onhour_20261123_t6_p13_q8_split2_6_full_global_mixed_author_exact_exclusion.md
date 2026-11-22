# T6 maximal-p13 order8 split (2,6): complete author exact finite exclusion
Date: 2026-11-23 (Asia/Hong_Kong) | Scope: frozen T6, `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`.

## Proposition and prerequisites

Under the frozen full integer/exponent carrier, side exponent masses at most 2331, exact (H_0,\ldots,H_6) equality, the previously established p13 higher-valuation cancellation lemma and previously established exclusions of lower p13 vertical orders, there is no surviving *disjoint named-support* p13 valuation-one vertical-order-8 pair with split (2,6).

A vertical atom indexed by ((q,r)), (q\ge1), (1\le r\le12), has original denominator (13(13q+r)), and original exponent mass (169q+13r-1). The q0 atom indexed by (r) has denominator (13r), cost (13r-1). Multiplicity and original integer denominators are retained. A cross-side repeated named atom may be cancelled, reducing the vertical order to a previously treated lower order.

Necessary congruences derived from the original observers are:
```
sum_{r=1}^{12} u_r*r^(-j)
 + sum_{(q,r) in V+} (13q+r)^(-j)
 - sum_{(q,r) in V-} (13q+r)^(-j)
 = 0 mod 13^j, j=1,...,6.
```
This is the full mixed-congruence global necessity, *not* an assumption that the p13 local rational moments equal separately.

## Exact finite method and coverage

Use the existing 12-dimensional saturated q0 congruence lattice, whose index is (13^{21}). Its weighted HNF/LLL basis has exact minimum Gram–Schmidt squared diagonal
```
78577530278042129705264382752517501995032553011464356025
/4243983974238642688103181306691645151538473248349
```
and this exceeds (2(2331)^2=10867122).

For each named signed vertical pair, construct an affine particular q0 solution by six exact modular pivot steps. The original two side-mass caps give the necessary weighted Euclidean ball radius (R^2=(2331-M_{V+})^2+(2331-M_{V-})^2). As (R^2) is smaller than *every* Gram–Schmidt diagonal squared, at each integer coordinate only `floor(-center)` and its successor can satisfy the residual norm bound. Exhaustively search these alternatives using exact rational arithmetic and independently check all resulting q0 vectors against each modulus and the original side masses. The finite domain consists of all 90 distinct unordered-internal named multisets of vertical order 2 paired with all 42,614 such multisets of order 6, with the two sides signed and ordered.

| Count | Result |
|---|---:|
| Raw signed named pair configurations | 3,835,260 |
| Cross-side common named atom configurations (cancelled) | 1,433,862 |
| Disjoint named configurations exhaustively searched | 2,401,398 |
| Exact Gram–Schmidt recursion nodes | 5,640,848 |
| Necessary-ball integer q0 leaves | 15 |
| Leaves satisfying both side mass caps | **0** |

All 15 relaxed leaves retain explicit plus/minus named multisets, signed 12-vectors, original side masses and their source-slice hashes in the corresponding JSON certificate. Among them, the least value of `max(M_plus,M_minus)` is **3858**, greater than 2331. No float tolerance is used.

Complete disjoint-support finite unit verdict: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**. Combined with earlier lower-order author results, this closes the q8 (2,6) branch at the same author-proof level. The global T6=2332 question remains OPEN.

## Reproduction and provenance

- Executed local script SHA-256: `070a47daa286f82fec3a3439f4225ee214e22c390f23a4f6d4801c2c926db992`.
- Published corresponding exact checker: `research_checks/T6_P13_Q8_SPLIT2_6_FAST_EXACT_CENSUS_20261123.py`; it is a compact transcription of the executed cached algorithm, **not** separately re-executed after publication.
- Full certificate: `research_checks/T6_P13_Q8_SPLIT2_6_FULL_EXACT_CERT_20261123.json`. It includes the contiguous [0,90) slice partition and ordered-pair digests.
- Frozen Task: `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md@d84bd940cfb093cdc60e569f15cad58772a51dca`.
- Prior reusable mathematical sources: p13 v13>=2 cancellation, 12D saturated q0 lattice, p13 q0..q7 and q8 (0,8)/(1,7) author evidence. They were consumed, not re-proved.

## Remaining scientific and Source obligations

Minimal next scientific unit: p13 vertical order8 split **(3,5)**; after it, **(4,4)**. Validate any surviving candidate against lower-prime completion rather than equating modular survivorship with a collision. The existing T6 Research Activity attribution differs from the current recovered service identity; this independent portable scientific artifact must not be relabeled as an authenticated native Activity or semantic PROGRESS. A current winning Research CLAIM/Run was not verified in this unit. No nonauthor review or formal acceptance has occurred.
