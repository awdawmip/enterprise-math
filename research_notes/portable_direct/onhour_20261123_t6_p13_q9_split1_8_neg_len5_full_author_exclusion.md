# T6 maximal-p13, order-9 split (1,8): complete negative-length-5 exact exclusion

2026-11-23 · Source science frozen at `enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`; Task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`. Author-only exact finite computation, pending independent review and native association.

## Exact statement

Let each side have total exponent mass at most 2331. Consider two signed exponent shapes with equal original `H_0,...,H_6` and maximal prime factor 13. After prior valid 13²/13³ cancellation, restrict to 13-adic valuation-one vertical atoms `(q,r)`, denoting the exponent denominator `13(13q+r)`, with `1 <= r <= 12`. For total positive vertical q-order 1, represented by one `(1,r)`, and negative q-order 8 represented by exactly five named vertical atoms, **no disjoint signed vertical configuration can satisfy all six necessary mixed congruences together with both original side-mass caps**. Coincident vertical atoms cancel into previously studied lower-order configurations.

The negative-side q-orders have exactly three nondecreasing partitions:
`(1,1,1,1,4)`, `(1,1,1,2,3)`, `(1,1,2,2,2)`.
For each partition, residues within a repeated q-block are a multiset; all twelve positive q1 residues were tested, with names and multiplicities retained.

| Negative q partition | Negative rosters | Raw positive/negative pairs | Common-atom cancellations | Exact GS nodes | Affine-ball leaves | Both caps pass |
|---|---:|---:|---:|---:|---:|---:|
| 1,1,1,1,4 | 16,380 | 196,560 | 52,416 | 355,897 | 2 | 0 |
| 1,1,1,2,3 | 52,416 | 628,992 | 134,784 | 1,218,771 | 5 | 0 |
| 1,1,2,2,2 | 28,392 | 340,704 | 52,416 | 713,334 | 3 | 0 |
| **Total** | **97,188** | **1,166,256** | **239,616** | **2,288,002** | **10** | **0** |

Thus 926,640 raw signed pairs remain after common-atom normalization. All ten affine-ball leaves satisfy the six necessary 13-adic modular conditions, yet have side-mass pairs respectively `(3524,4079)`, `(4994,4075)`, `(1043,6938)`, `(2665,4401)`, `(1971,5228)`, `(3315,5469)`, `(3651,3615)`, `(2531,4975)`, `(5120,2976)`, `(3183,4572)`. Each violates the cap on at least one side.

## Mathematical and computational certificate

In the saturated 12-dimensional q0 integer congruence lattice of index `13^21`, the signed q0 coefficients `u_r` satisfy the necessary conditions, for every `j=1,...,6`:

```
sum_{r=1}^{12} u_r*r^(-j)
+ sum_{(q,r) in positive} (13q+r)^(-j)
- sum_{(q,r) in negative} (13q+r)^(-j)
    == 0 (mod 13^j).
```

For signed vertical side costs `c_+` and `c_-`, the q0 weighted squared norm is bounded by `(2331-c_+)^2+(2331-c_-)^2`. The exact Gram–Schmidt minimum diagonal squared is

```
78577530278042129705264382752517501995032553011464356025
/ 4243983974238642688103181306691645151538473248349
```

which exceeds `2*2331^2=10867122`. Therefore, in each coordinate of the affine GS enumeration, only the two integers bracketing the exact conditional center can occur. The recursive search uses `Fraction` and integer arithmetic; every surviving vector is reconstructed and checked against all six congruences and both original mass caps. The finite tree counts and ten complete signed vectors are in the exact JSON certificate.

The computation was executed in nine disjoint enumerator ranges, using `[start,end)` indices of the canonical `all_rosters` generator:
- 11114: `[0,16380)`
- 11123: `[0,12000)`, `[12000,24000)`, `[24000,36000)`, `[36000,48000)`, `[48000,52416)`
- 11222: `[0,9500)`, `[9500,19000)`, `[19000,28392)`

The new replay wrapper uses the pinned prior checker `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py` (Git blob `883ed909d37bed4b7c8b54cc0004b3e1822ee98c`) and its published saturated q0 lattice. It will fail closed if that base file changes.

Sources:
- Exact certificate: `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN5_AUTHOR_EXACT_CERT_20261123.json`
- Replay wrapper: `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN5_EXACT_REPLAY_20261123.py`
- Previous completed negative lengths 1..4: `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split1_8_negative_lengths1to4_exact_author.md`, commit `1da6c7841361bafbf34aba5fb552b54dc2691644`.

## Continuation and scope

Previous signed split (1,8) negative lengths 1..4: 492,804 raw pairs, six affine-ball leaves and no budget-valid candidate. Combining the newly completed negative length5 with that earlier evidence yields **1,659,060 raw positive/negative pairs checked for lengths 1..5** (not the entire signed split).

Next unfinished unit: negative length6, first pattern `(1,1,1,1,1,3)`, then `(1,1,1,1,2,2)`; the negative length7–8 and order9 signed splits (2,7), (3,6), (4,5) remain open. Formal Source also contains a separate p17 q14 preflight/owner frontier. The T6 mother question remains OPEN.

Provenance and status: locally executed exact computation; GitHub source publication and scoped readback to be recorded; `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`. The new replay wrapper has not been independently executed after publication. No claim of winning native CLAIM, semantic PROGRESS, Result, reviewer independence or Activity owner linkage is made.
