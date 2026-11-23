# T6 / maximal p13 / q-order 9 / signed split (1,8): complete negative length-five exact exclusion

Date: 2026-11-23 (Asia/Hong_Kong). Source task input: `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca:research_tasks/T6_SHAPE_MOMENT_GLOBAL_LOWER_BOUND_20260909.md`. Research mode: portable TASK-informed author calculation. `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`.

## Statement and original model

For the maximal-p13 layer with all higher 13 valuations canceled (previous source result), let the vertical signed p13-valuation-one atoms have positive q-order 1 and negative q-order 8. Every atom is a named pair `(q,r)` corresponding to the full denominator `a=13(13q+r)`, where `q>=1, 1<=r<=12`, with exponent mass `a-1`. Both original signed sides have exponent mass at most 2331; the observer remains the exact original `H_0,...,H_6`. Repetition and signs are retained.

**New exhaustive finite result:** When the negative side has exactly five vertical atoms, there is no admissible original two-sided shape collision. The only three integer q multisets of sum 8 and length 5 are `(1,1,1,1,4)`, `(1,1,1,2,3)`, `(1,1,2,2,2)`. All residues are enumerated as nondecreasing within each equal-q block, preserving each named multiset exactly once. The positive atom is one of twelve `(1,r)`. Pairs sharing a named vertical atom are canceled and belong to a strictly lower order already handled in this research line.

The six necessary signed congruences, retaining possible smaller-prime compensation, are

```
sum_{r=1}^{12} u_r*r^(-j)
 + sum_{(q,r) in Vplus}(13q+r)^(-j)
 - sum_{(q,r) in Vminus}(13q+r)^(-j) == 0 (mod 13^j),
j=1,...,6.
```

Use the previously published saturated 12-dimensional q0 congruence lattice with index `13^21=247064529073450392704413`, weighted by `w_r=13r-1`. Its exact rational Gram-Schmidt minimum squared diagonal is

```
78577530278042129705264382752517501995032553011464356025
/
4243983974238642688103181306691645151538473248349
```

This exceeds `2*2331^2 = 10867122`. With vertical masses `cplus,cminus`, any admissible q0 compensation must have weighted squared norm at most `(2331-cplus)^2+(2331-cminus)^2`. Every coordinate of the exact nearest-integer GS recursion therefore has no more than two adjacent integer choices; searching these choices with exact rational comparisons covers the entire necessary ball. Each leaf is checked against six exact modular identities and both **original** exponent masses.

## Complete author computation

| Negative q-multiset | Named negative rosters | Original signed pairs | Same-atom cancellations | GS recursion nodes | Affine-ball leaves | Valid under both side caps |
|---|---:|---:|---:|---:|---:|---:|
| (1,1,1,1,4) | 16,380 | 196,560 | 52,416 | 355,897 | 2 | 0 |
| (1,1,1,2,3) | 52,416 | 628,992 | 134,784 | 1,218,771 | 5 | 0 |
| (1,1,2,2,2) | 28,392 | 340,704 | 52,416 | 713,334 | 3 | 0 |
| **Total** | **97,188** | **1,166,256** | **239,616** | **2,288,002** | **10** | **0** |

Exactly 926,640 common-atom-disjoint pairs were searched. All ten affine-ball leaves pass the six mixed modular equalities but exceed at least one of the two side-mass caps; all signed 12-vectors, masses and radii are in the linked author certificate. No premature elimination by an unproved low-prime filtering rule was used. Independent arithmetic rechecks of all ten stored leaves recomputed the congruences and masses; this is a same-author audit, not an outside review.

This finite census was run in six source-order intervals with the exact rational implementation. Coverage intervals for the three q-patterns are respectively `[0,16380)`, `[0,10000)+[10000,20000)+[20000,36000)+[36000,52416)`, and `[0,28392)`; per-interval SHA256 digests and exact counters are in the certificate. The published compact replay imports the already-committed prior saturated lattice and `pair_search` implementation, then enumerates the three new partitions. The post-publication standalone compact replay is **not performed**.

## Source pins and continuation

- Author certificate: `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN5_AUTHOR_EXACT_CERT_20261123_1000.json`.
- Reproducible exact checker: `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN5_EXACT_REPLAY_20261123_1000.py`.
- Reused q0 checker and lattice: `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN1TO4_EXACT_REPLAY_20261123_0900.py`.
- Previously completed exact signed (1,8) negative lengths 1..4: 492,804 raw signed pairs, 6 affine-ball leaves, zero valid; report `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split1_8_negative_lengths1to4_exact_author.md`.
- Combined negative lengths 1..5 now cover **1,659,060** raw signed pairs; **299,376** common-atom pairs, **1,359,684** support-disjoint pairs, 16 ball leaves, none original-budget-valid.
- Smallest remaining **portable** p13 mathematical unit: negative length 6 of signed q-order (1,8), beginning q-multiset `(1,1,1,1,1,3)`, then `(1,1,1,1,2,2)`. Later lengths 7..8 and signed splits (2,7),(3,6),(4,5).
- The separate **native** T6 Source frontier still names the maximal-p17 q14 (7,7) full-roster/cost preflight and its own ownership/verification requirements. This p13 author material does not substitute for its native experiment.
- Historical Activity `RA-5E3FE1E761E4963EC461A892` remains attribution-pending after 328 reported events. The current Sites subject has no verified winning native T6 CLAIM/run. This report claims no Activity, Native PROGRESS, frozen Result or independent review.

The mother question `T6=2332` remains **OPEN**. Frozen task input, P000 and applicable ACTIVE worldview were not changed.
