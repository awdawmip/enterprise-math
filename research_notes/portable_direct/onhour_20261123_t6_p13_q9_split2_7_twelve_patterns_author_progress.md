# T6 maximal p13 q-order9: complete split(1,8) and exact partial split(2,7)

Date 2026-11-23 · immutable science `awdawmip/enterprise-math@d84bd940cfb093cdc60e569f15cad58772a51dca`. Mother Task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND`. Both original exponent mass caps: 2331. Original finite shape observers `H_0,...,H_6`.

## Completed signed split (1,8)

The exact finite author computation has now closed **all negative lengths one through eight** for maximal p13, valuation-one, q-order split (1,8). The positive side has one q1 named residue (12 choices), while the negative side runs through all partitions of q-order8. Every named atom, multiplicity and sign was retained; identical opposite-side atoms were canceled into lower-order cases. After six exact mixed 13-adic congruences, 12D saturated q0 affine GS enumeration and both full original mass caps:

- 6,254,820 raw signed pairs.
- 1,847,520 common-named-atom cancellations.
- 4,407,300 disjoint signed pairs checked; 10,729,231 exact GS recursive nodes.
- 29 affine-ball leaves; **0 satisfy both original side caps**.

The full proof and breakdown are in `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split1_8_all_negative_lengths_author_exact_exclusion.md` (commit `1cc5a93fc7701b42aa99111678481bbdb4cc0ce4`), with exact certificates for new lengths5,6,7,8 published under `research_checks/T6_P13_Q9_SPLIT1_8_NEG_LEN*`. Previously completed signed split (0,9) remains separately preserved. These are author-level finite exclusions, not independent review or formal Native Result.

## New split (2,7) input census and exact finite reduction

The positive q-order2 named roster has precisely 90 possibilities: one q2 atom with residue1..12 (12), or a multiset of two q1 residues (78). The negative q-order7 side has 153,960 named rosters across 15 nondecreasing q partitions. All standalone vertical costs are below 2331, leaving 13,856,400 raw signed pairs. For a given negative roster having `d1` distinct q1 residues and `d2` distinct q2 residues, common-atom cancellation hits exactly `d2 + (78 - C(13-d1,2))` of the positive rosters. Thus 5,547,384 raw pairs contain a common atom; 8,309,016 disjoint pairs require affine search. The full exact table and reproducible integer-only census are in `research_notes/portable_direct/onhour_20261123_t6_p13_q9_split2_7_exact_roster_preflight.md` and `research_checks/T6_P13_Q9_SPLIT2_7_EXACT_ROSTER_PREFLIGHT_20261123.py`.

In the same run, execute the exact 12D saturated-lattice/GS search across **12 complete negative q partitions** (all named residues and all 90 positive rosters), using exact fractions and six mod `13^j` signed mixed congruences. Results:

| Completed negative q partition | Raw pairs | Common canceled | Exact GS nodes | Ball leaves | Original-budget-valid |
|---|---:|---:|---:|---:|---:|
| (7) | 1,080 | 0 | 2,673 | 0 | 0 |
| (3,4) | 12,960 | 0 | 30,742 | 0 | 0 |
| (2,5) | 12,960 | 144 | 30,659 | 0 | 0 |
| (1,6) | 12,960 | 1,728 | 26,755 | 0 | 0 |
| (2,2,3) | 84,240 | 1,728 | 191,505 | 0 | 0 |
| (1,3,3) | 84,240 | 11,232 | 170,252 | 1 | 0 |
| (1,1,5) | 84,240 | 19,944 | 149,723 | 0 | 0 |
| (1,2,4) | 155,520 | 22,464 | 309,195 | 0 | 0 |
| (1,1,1,4) | 393,120 | 125,280 | 612,960 | 0 | 0 |
| (1,2,2,2) | 393,120 | 63,648 | 750,224 | 1 | 0 |
| (1,1,2,3) | 1,010,880 | 250,560 | 1,736,102 | 3 | 0 |
| (1,1,1,1,3) | 1,474,200 | 567,216 | 2,041,935 | 4 | 0 |
| **TOTAL** | **3,719,520** | **1,063,944** | **6,052,725** | **9** | **0** |

For the nine affine-ball leaves, the exact certificate retains every signed q0 coefficient vector, positive/negative named atom and both original side masses; all nine violate the original mass cap on at least one side. The original exponent/moment carrier is never collapsed to a total-only summary. The saturated q0 index is `13^21` and its exact smallest GS squared diagonal exceeds `2*2331²`, enabling exhaustive two-neighbor rational recursion.

Complete finite author certificate: `research_checks/T6_P13_Q9_SPLIT2_7_TWELVE_PATTERNS_AUTHOR_EXACT_CERT_20261123.json` at commit `c45f7ec556be67bdc2bb8749dfd660184425b409`. Segment checker `research_checks/T6_P13_Q9_SPLIT2_7_PATTERN_EXACT_REPLAY_20261123.py` at commit `3ba68f730f4efa2bd621ec6fd90c15d7a2fb78d6`, importing the exact Git-blob-pinned prior 12D checker. The trivial negative q partition (7) was separately checkpointed as `research_checks/T6_P13_Q9_SPLIT2_7_NEG_PATTERN7_EXACT_AUTHOR_CERT_20261123.json` (commit `b5828553149cc3e65d0596dab6fdd8b33f32369e`).

## Exact remaining range

Three negative q partitions remain in signed split (2,7): `(1,1,1,1,1,1,1)` (31,824 negative rosters), `(1,1,1,1,1,2)` (52,416) and `(1,1,1,2,2)` (28,392). They contain **112,632 negative rosters, 10,136,880 raw signed pairs, 4,483,440 common-atom pairs and 5,653,440 disjoint pairs**. Next smallest exact unit: carry out the complete finite search on `(1,1,1,2,2)` or nonoverlapping intervals thereof, then the other two partitions, without repeating the 12 closed partitions.

The global T6 target remains OPEN; after (2,7), address (3,6), (4,5), higher q-orders and lower maximal prime factors. Formal Source p17 q14 preflight and native owner remain separate. Proof status: `AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED`. Post-publication independent replay and native semantic association are outstanding; no privileged claim/role has been borrowed or asserted.
