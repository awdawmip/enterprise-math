# T6 p13 onepower vertical order8 split (3,5): complete exact finite exclusion

Date: 2026-11-23 (Asia/Hong_Kong). Mother Task: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`, frozen input at `research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md@d84bd940cfb093cdc60e569f15cad58772a51dca`.

## Scoped result

Given each original exponent-side mass at most 2331, (H_0,\ldots,H_6) equality, previously established complete p13 higher-valuation cancellation, and the previously completed lower vertical-order cases, there is no legal named-support-disjoint maximal-p13 valuation-one vertical-order-8 split (3,5).

Each vertical atom has denominator (13(13q+r)), mass (169q+13r-1), (q\ge1, 1\le r\le12). Each q0 atom has denominator (13r), mass (13r-1). Multisets preserve repeated factors, original integer denominator identities and sign. Cross-side common atoms are cancelled to a lower-order case and are recorded separately.

Full global modular necessity derived from the original observer equations:
```
sum_r u_r*r^(-j)+sum_{plus}(13q+r)^(-j)-sum_{minus}(13q+r)^(-j)
= 0 mod 13^j,  j=1,...,6.
```
This allows smaller-prime compensation: we never assume the rational p13-local observer moments match separately. The previously verified homogeneous q0 lattice has rank 12 and index (13^{21}), minimum exact GS squared diagonal (18,515,039.35\ldots>2(2331)^2). In each affine coset, the necessary mass-ball radius squared is strictly below this diagonal; the two-nearest-integer GS recursion therefore enumerates every relevant q0 integer solution. Every leaf was checked exactly against six congruences and both original side mass caps.

| Scope | Exact number |
|---|---:|
| First-side vertical-order 3 named multisets | 520 |
| Second-side vertical-order 5 named multisets | 10,908 |
| Raw ordered signed pairs | 5,672,160 |
| Opposite sides share at least one named atom | 2,408,760 |
| Fully searched disjoint-support pairs | 3,263,400 |
| Exact GS recursion nodes | 7,333,379 |
| Necessary weighted-ball q0 leaves | 8 |
| Leaves with both original masses \(\le2331\) | **0** |

All eight relaxed q0 survivors have signed 12-vectors, integer atomic multisets and actual positive/negative masses saved in `research_checks/T6_P13_Q8_SPLIT3_5_FULL_EXACT_CERT_20261123.json`. Their smallest larger-side mass is **3367**, above the 2331 bound. The certificate preserves all 12 disjoint contiguous first-side ranges covering [0,520) and their SHA256 pair-order digests; no unfinished rows remain.

Executed exact local calculation using `/mnt/data/p13_q8_3_5_partial_exact_20261123.py`, script SHA256 `d99d9e31199b59dfaaafb85800fccf171f3688ad9127340fedc4baed7c9544ee`; a preexisting repository portable checker `research_checks/T6_P13_Q8_BOUNDED_AUTHOR_AFFINE_CHECK_20261123.py` permits the same (3,5) model in chunks. Published checker is not claimed separately re-executed or independently reviewed. Mathematical classification: **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

Earlier p13 order8 (0,8), (1,7), and the newly completed (2,6) are reused, not recomputed. The next minimal scientific unit is p13 order8 (4,4). The global mother question (T_6=2332) remains OPEN. Source state shows no winning authorized claim in this Research lane and no protected Native semantic progress; this portable note does not alter task ownership.
