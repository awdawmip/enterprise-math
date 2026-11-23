# T6 maximal p13, signed order-9 split(2,7), positive length-one q2: complete author exclusion

Date: 2026-11-23. Frozen T6 task source: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. Source scientific status: `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## Statement

Assume the original integer/exponent carrier, both signed side exponent masses <=2331, and H_0,...,H_6 equal. Reuse the earlier proven maximal-p13 higher-valuation cancellation and exact saturated q0 integer lattice. For p13-valuation-one signed vertical q-order 9, split(2,7), if the **positive side consists of a single atom (q,r)=(2,r), 1<=r<=12**, there is no legal two-sided collision. The negative side may have any complete canonical named multiset of q>=1 atoms whose q values sum to 7 (length 1..7); all composites, residues, multiplicities, signs and original mass constraints are retained.

The necessary mixed congruences are
```
sum_(r=1..12) u_r r^(-j) + (26+r_pos)^(-j)
  - sum_(q,r in negative) (13q+r)^(-j) = 0 mod 13^j,
j=1,2,3,4,5,6.
```
The affine q0 coset uses the previously committed 12D saturated lattice of index 13^21 and its exact rational Gram–Schmidt basis.

## Exhaustive integer census

| Negative atom count | Canonical negative rosters | Raw signed pairs | Common-name cancellation | Exact GS nodes | In-sphere leaves | Legal after both side budgets |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 12 | 144 | 0 | 380 | 0 | 0 |
| 2 | 432 | 5,184 | 144 | 12,338 | 0 | 0 |
| 3 | 4,536 | 54,432 | 3,456 | 122,405 | 1 | 0 |
| 4 | 19,968 | 239,616 | 22,464 | 512,848 | 1 | 0 |
| 5 | 44,772 | 537,264 | 52,416 | 1,125,056 | 2 | 0 |
| 6 | 52,416 | 628,992 | 52,416 | 1,318,336 | 1 | 0 |
| 7 | 31,824 | 381,888 | 0 | 865,525 | 1 | 0 |
| **Total** | **153,960** | **1,847,520** | **130,896** | **3,956,888** | **6** | **0** |

No disjoint pair exceeded its negative vertical-only cap. The common-name pairs reduce exactly to previously closed lower p13 order and are excluded by their earlier proofs. All 1,716,624 remaining support-disjoint pairs were checked.

The positive vertical mass lies between 350 and 493; negative vertical mass is `169*7 + 13*sum(residues) - length`, at least 1195. Therefore the necessary weighted q0 radius squared is at most `(2331-350)^2+(2331-1195)^2=5,214,857`. This is strictly smaller than the exact smallest Gram–Schmidt diagonal square, about 18,515,039.35. Exact two-neighbor recursion enumerates every point of the necessary affine sphere and found exactly six leaves. Each was independently checked by integer modular inverse powers and original side masses; all fail at least one original 2331 cap.

In particular, one leaf has positive mass exactly **2331** but negative mass **5433**. It is a genuine mixed-congruence ball candidate and not a legal original collision. Complete six signed witnesses and exact original masses are in `research_checks/T6_P13_Q9_SPLIT2_7_POS_Q2_ALL_NEG_AUTHOR_EXACT_CERT_20261123_1026.json`; reproducible full Python checker in `research_checks/T6_P13_Q9_SPLIT2_7_POS_Q2_AUTHOR_REPLAY_20261123_1026.py`.

Canonical roster-line SHA256: `a551554e8c631814caee26fb6471150f01f044f38f0bf35e96503d25e21901f9`. Actual full author run used GMP exact rational arithmetic (28.43s) with existing HNF/LLL coefficients; published compact Python replay not separately rerun. Original p13 signed split(1,8) negative lengths1..8 and (0,9) are preserved as completed, with source provenance unchanged.

## Precise next unit

Signed p13 order-9 split(2,7), **positive length two q-pattern(1,1)** with 78 positive named residue multisets, paired with all 153,960 negative q7 rosters, excluding exact same-name common atoms. This may produce actual valid modular kernels; if so, the next step is full lower-prime H-moment completion, not discarding them. The other (3,6), (4,5) signed splits and full global T6=2332 remain OPEN. Formal Native T6 Source p17 q14 (7,7) roster-cost preflight has independent ownership and review; it has not been performed here.
