# T6 p13 order9, signed split(1,8): negative length6 completely excluded

Date 2026-11-23. Frozen scientific Task commit: `d84bd940cfb093cdc60e569f15cad58772a51dca`. Task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`. The original two exponent-mass caps are 2331 each.

## Verified local exact finite computation

For maximal prime 13, valuation-one vertical atoms and q-order split (1,8), the positive side has one named q1 atom. All signed configurations with exactly six negative vertical atoms, total negative q-order8, have been enumerated with exact 12-dimensional saturated q0 correction and the six mixed congruences modulo `13^j`, `j=1,...,6`. After cancellation of common named atoms into earlier lower-order cases, **no six-negative-atom configuration meets both original side masses**.

The only nondecreasing negative q partitions are `(1,1,1,1,1,3)` and `(1,1,1,1,2,2)`. Within each equal-q block, residues are counted by multisets, preserving each named atom and its multiplicity.

| Negative q pattern | Negative rosters | Signed raw pairs | Shared-atom pairs | Exact Gram–Schmidt nodes | Affine-ball leaves | Original-budget-valid |
|---|---:|---:|---:|---:|---:|---:|
| (1,1,1,1,1,3) | 52,416 | 628,992 | 196,560 | 1,056,399 | 4 | 0 |
| (1,1,1,1,2,2) | 106,470 | 1,277,640 | 340,704 | 2,286,516 | 4 | 0 |
| **Total** | **158,886** | **1,906,632** | **537,264** | **3,342,915** | **8** | **0** |

There are 1,369,368 pairs after cancellation. All eight exact affine-ball leaves have signed two-side mass pairs `(2624,5184)`, `(5876,2453)`, `(2775,5320)`, `(4243,3497)`, `(3456,4449)`, `(4964,2738)`, `(1634,5408)`, `(2326,3777)`. The last is a near-boundary case: its positive mass 2326 is legal, but its negative mass 3777 exceeds 2331.

The weighted q0 lattice `13^21` and exact Gram–Schmidt `d_min^2=78577530278042129705264382752517501995032553011464356025/4243983974238642688103181306691645151538473248349` carry over unchanged from the prior verified proof architecture. The radius in every configuration is `(2331-c_+)²+(2331-c_-)²`, bounded above by `2·2331² < d_min²`. Two-neighbor exact rational coordinate enumeration is exhaustive. Every leaf is reconstructed as a signed integer q0 vector, and all six mixed congruences and both side masses are tested.

Local author computation consisted of 14 disjoint checked intervals: for q-pattern 111113, indices `[0,13000)`, `[13000,26000)`, `[26000,39000)`, `[39000,52416)`; for q-pattern 111122, intervals `[0,11000)`, `[11000,22000)`, `[22000,33000)`, `[33000,44000)`, `[44000,55000)`, `[55000,65000)`, `[65000,75000)`, `[75000,85000)`, `[85000,95000)`, `[95000,106470)`. These cover the exact combinatorial counts `C(16,5)·12` and `C(15,4)·C(13,2)`.

New immutable supporting artifacts:
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN6_AUTHOR_EXACT_CERT_20261123.json`: per-interval counts, eight signed integer q0 witnesses, mass pairs and exact radii
- `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN6_EXACT_REPLAY_20261123.py`: bounded wrapper around the original pinned checker, validated against the exact base Git blob `883ed909d37bed4b7c8b54cc0004b3e1822ee98c`

Combined with previous, verified author-level negative lengths 1 through 6 of signed split (1,8) cover 3,565,692 raw signed pairs, all with zero original-budget-valid full mixed-congruence candidate. The previous length5 completion is `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split1_8_neg_len5_full_author_exclusion.md`.

## Next scientific unit and shared-state separation

Remaining in signed split (1,8): negative length7 with partition `(1,1,1,1,1,1,2)`, then length8 with partition `(1,1,1,1,1,1,1,1)`. Their exact roster counts are 148,512 and 75,582, respectively. Then order9 splits (2,7), (3,6), (4,5) and smaller-prime completion remain. Parent T6=2332 is OPEN.

Evidence grade: `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`. The newly published wrapper has not undergone independent post-publication replay. No current own Source winning CLAIM or Native semantic PROGRESS has been established; no borrowed historical Activity/Researcher identity was used. Formal p17 order14 preflight belongs to its own Source owner chain.
