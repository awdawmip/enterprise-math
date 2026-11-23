# T6 p13 order9 signed split (4,5): complete positive q(1,1,2) family

Date: 2026-11-23. Source scientific freeze `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`; mother `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`. Two original side mass caps 2331, named 13-unit atom `13(13q+r)`, signed multiplicities, exact six mixed congruences modulo `13^j`, `j=1,...,6`, with lower-prime obligations preserved. Scientific status `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## New complete negative q(1,1,1,1,1) result

For positive vertical q-partition `(1,1,2)` and negative vertical q-partition `(1,1,1,1,1)`, complete enumerations give 936 positive named rosters and 4368 negative named rosters, thus **4,088,448** raw ordered pairs. Exactly **2,070,432** common named-support cases reduce to earlier lower-order research; **2,018,016** disjoint pairs underwent exact rational affine Gram–Schmidt checks. There were **4,063,519** recursive nodes and exactly **one** sphere leaf. That leaf violates both original mass caps:

```text
plus : [(1,6),(1,7),(2,2)]
minus: [(1,2),(1,5),(1,5),(1,12),(1,12)]
u(r=1..12) = [9,-12,8,-7,-2,-8,6,4,7,5,-1,6]
vertical masses = (868,1308)
q0 correction masses = (3751,1543)
total masses = (4619,2851)
six modular residues j=1..6 = (0,0,0,0,0,0).
```

The six disjoint, complete negative-index intervals are `[0,600),[600,2000),[2000,2600),[2600,3300),[3300,3900),[3900,4368)`. Each interval's raw count, cancellations, exact recursive-node count, negative roster SHA256, ordered-pair SHA256 and original local JSON SHA256 are in `research_checks/T6_P13_Q9_SPLIT45_POS112_NEG11111_FULL_AUTHOR_EXACT_CERT_20261123.json`. A larger `[2000,4368)` attempted execution timed out without producing a complete result; it is excluded from the sums and was replaced by four completed intervals.

The original denominator cost is `169q+13r-1`; q0 integer correction has weight `13r-1`. For every `j=1,...,6` the mixed congruence is
```text
sum_r u_r*r^(-j) + sum_plus(13q+r)^(-j) - sum_minus(13q+r)^(-j) == 0 mod 13^j.
```
The saturated 12D q0 lattice has index `13^21`; its exact minimum rational GS diagonal square is recorded in the certificate and exceeds `2*2331^2=10867122`. Hence two nearest-coordinate choices at each recursion step exhaust the original-budget necessary sphere, with exact Fraction arithmetic. The unique leaf's residues and mass arithmetic were also recomputed separately with modular integer operations.

The author-local script `t6_p13_q9_split45_pos112_neg11111_slice.py` executed the completed intervals; its SHA256 is `25774784c6c08dc98a50e99e7ff26f43ee225862956d69c2109219a031e19df7`. The published compact replay wrapper `research_checks/T6_P13_Q9_SPLIT45_POS112_NEG11111_REPLAY_20261123.py` uses the existing published exact q0 kernel; it has not been independently executed after publication.

## Combined closure for positive (1,1,2)

Three negative q5 named-roster subfamilies now cover *all* 10908 negative q-order5 configurations, including repeated atoms:

| Negative q5 family | Negative rosters | Raw signed pairs | Common support | Exact GS nodes | Sphere leaves | Budget valid |
|---|---:|---:|---:|---:|---:|---:|
| length1–3, all five partitions (prior verified author result) | 2172 | 2,032,992 | 520,128 | 3,222,963 | 1 | 0 |
| (1,1,1,2), newly complete | 4368 | 4,088,448 | 1,718,784 | 4,889,804 | 0 | 0 |
| (1,1,1,1,1), newly complete | 4368 | 4,088,448 | 2,070,432 | 4,063,519 | 1 | 0 |
| **Full q5** | **10908** | **10,209,888** | **4,309,344** | **12,176,286** | **2** | **0** |

Exactly 5,900,544 disjoint pairs were fully searched. Both relaxed sphere leaves fail the 2331-side limits. Shared-support pairs cancel to the already author-excluded lower q-orders. Thus **for positive q-partition (1,1,2), all negative q-order5 configurations are excluded at original-budget scope**.

This combines the existing prior report `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split4_5_pos_q112_neg_len1to3_author.md` with the two new independent subfamily enumerations; source author and review status remain their own, no independent admission claimed.

## Next frontier

In p13 qorder9 signed split `(4,5)`, previous positive q-partitions `(4),(1,3),(2,2)` are consumed and now `(1,1,2)` is complete. The remaining positive q-partition is `(1,1,1,1)` with 1365 positive rosters against all 10908 negative order5 rosters, or **14,889,420 raw named pairs** before exact cancellation and mass filtering. Use the previously verified signed q0 lattice, pair enumeration and original caps; segment by canonical positive roster index. Keep p13 qorders >9, maximal p11 and smaller primes, H0 completion and global T6=2332 OPEN.

Native Source's delegated p17 q14 preflight is separately owned. This author continuation has no verified winning CLAIM, protected semantic PROGRESS or formal Result. Activity/Researcher author identity reconciliation is pending; do not append events under the historical RA328 identity without proper authorization.
