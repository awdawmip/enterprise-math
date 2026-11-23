# T6 maximal p13: q-order9 signed split (1,8) complete author exact exclusion

Date: 2026-11-23. Task: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`. Frozen scientific input: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`; exact Task blob `87b3a6f38e9350f7a3f56624b27bff2a7778a439`. P000 remains ACTIVE_LOCKED.

## Statement, exact domain and bound

Fix two named signed exponent shapes, each exponent mass at most 2331, with identical original shape observers `H_0,...,H_6`. Apply the previously established exact cancellation of 13²-and-higher valuations and consider maximal prime factor 13 and the remaining 13-adic valuation-one vertical atoms. Write each vertical denominator as `13(13q+r)`, where `q>=1`, `1<=r<=12`; its exponent mass is `13(13q+r)-1`. For signed vertical q-order split `(1,8)`, the positive vertical side is one named `(1,r)` and the negative side has q-order8 with between one and eight named atoms. Identical named atoms across signs are canceled, yielding previously handled lower-order cases. This report establishes by exhaustive exact rational/integer finite computation that **no remaining disjoint signed pair satisfies all six necessary 13-adic mixed congruences and both original side-mass caps**. Consequently no original moment collision occurs in this exact signed split.

The signed q0 coefficients `u_r` lie in the saturated 12D congruence lattice of index `13^21`. For `j=1,...,6`, the necessary condition is

```
sum_{r=1}^{12}u_r*r^(-j)
 + sum_{(q,r) in V_plus}(13q+r)^(-j)
 - sum_{(q,r) in V_minus}(13q+r)^(-j)
 == 0 mod 13^j .
```

Use original costs `c_+`, `c_-` for the two signed vertical sides, and `W_r=13r-1` for q0. The cap constraints imply the weighted q0 square norm bound `(2331-c_+)²+(2331-c_-)²`. The exact Gram–Schmidt smallest diagonal squared equals

```
78577530278042129705264382752517501995032553011464356025
/4243983974238642688103181306691645151538473248349
```

which exceeds `2*2331²=10867122`. Every affine integral coordinate is exhaustively enumerated by at most two neighbors bracketing its exact conditional center. All leaves are checked for six mixed congruences and full original two-side mass caps using integers and `Fraction`.

## All negative-roster lengths

| Negative length | Raw signed pairs | Common-atom cancellation | Exact GS recursion nodes | Affine-ball leaves | Both budgets legal |
|---|---:|---:|---:|---:|---:|
| 1–4, previously saved | 492,804 | 59,760 | 1,087,373 | 6 | 0 |
| 5, new this run | 1,166,256 | 239,616 | 2,288,002 | 10 | 0 |
| 6, new this run | 1,906,632 | 537,264 | 3,342,915 | 8 | 0 |
| 7, new this run | 1,782,144 | 628,992 | 2,784,730 | 5 | 0 |
| 8, new this run | 906,984 | 381,888 | 1,226,211 | 0 | 0 |
| **Total** | **6,254,820** | **1,847,520** | **10,729,231** | **29** | **0** |

Thus 4,407,300 distinct raw signed pairs remain after common-named-atom cancellation. Their 29 affine-ball leaves all violate at least one original 2331 side budget. The exact finite scope is fully accounted for without treating common cancellation as a new disjoint configuration.

For newly completed negative length5, its only three q partitions are `(1,1,1,1,4)`, `(1,1,1,2,3)`, `(1,1,2,2,2)`, with 97,188 canonical residue-multiset rosters and ten leaves. Negative length6 has only `(1,1,1,1,1,3)`, `(1,1,1,1,2,2)`, with 158,886 rosters and eight leaves. Negative length7 has only `(1,1,1,1,1,1,2)`: 148,512 rosters, 5 leaves; negative length8 has only `(1,1,1,1,1,1,1,1)`: 75,582 rosters and no leaves. The length7 and length8 computations included 17,033 pairs excluded immediately on an original side overbudget. Negative length7 has five leaves, with mass pairs `(3065,3140)`, `(3071,4226)`, `(3414,4402)`, `(924,7394)`, `(4061,3433)`; negative length8 has none. Exact named negative/positive rosters, integer `u_r`, radii, per-segment indices and counts are preserved in the certificates.

## Reproduction and provenance

The segment checkers import the existing published exact lattice computation `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py` only when its original Git blob matches `883ed909d37bed4b7c8b54cc0004b3e1822ee98c`. Each enumerates nondecreasing q-orders and nondecreasing residues only within equal-q groups, while retaining full named atoms, signs and multiplicities. The exact author executions were split into nonoverlapping intervals; all interval sums are recorded.

New evidence:
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN5_AUTHOR_EXACT_CERT_20261123.json`
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN5_EXACT_REPLAY_20261123.py`
- `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split1_8_neg_len5_full_author_exclusion.md`
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN6_AUTHOR_EXACT_CERT_20261123.json`
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN6_EXACT_REPLAY_20261123.py`
- `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split1_8_neg_len6_full_author_exclusion.md`
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN7_8_AUTHOR_EXACT_CERT_20261123.json`
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN7_8_EXACT_REPLAY_20261123.py`

Earlier:
- `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split1_8_negative_lengths1to4_exact_author.md` at commit `1da6c7841361bafbf34aba5fb552b54dc2691644`
- `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split0_9_complete_author_exclusion.md` at commit `0423e5bc23e3d074e89e0e5c33818013e004c98f`.

This author result closes two p13 order9 signed splits, `(0,9)` and now `(1,8)`, as separate finite exclusions. The remaining order9 splits `(2,7)`, `(3,6)`, `(4,5)` and smaller-prime layers require continued exact analysis. The mother target `T6=2332` remains OPEN. The distinct formal p17 order14 preflight and its current Source owner are unchanged.

Status: `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`. The published compact replay wrappers have not been independently rerun; separate nonauthor review is outstanding. No Native winning claim, native PROGRESS or old Research Activity attribution is asserted by this portable publication.
