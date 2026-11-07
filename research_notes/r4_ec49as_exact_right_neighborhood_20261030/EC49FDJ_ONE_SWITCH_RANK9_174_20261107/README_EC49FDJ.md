# EC49FDJ — 174 one-switch rank-nine BRC schedules (exact finite theorem)

Date: 2026-11-07; Status: AUTHOR_EXACT_FINITE / EXECUTED / UNREVIEWED / NOT_ADMITTED.
Frozen source: `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`.
Predecessor: EC49FDI `cb424b4f7391e2e3c2cbcdb31eb8ee546a70466f`; audited independent predecessor: `research_notes/r4_ec49as_exact_right_neighborhood_20261030/EC49FAW_TWO_NEW_KEY_RANK_SCHEDULE/EXACT_REPORT_EC49FAW.json`, blob `ed0026064e55c0730f1b2d91df239f01c8dc7fe6`.
P000 and ACTIVE Heartbeat World remain unchanged.

## Theorem (scope: signature/rank-nine key availability)

Fix the four H2/H3 operation paths `fe,ge,feg,gef` (16 signed native-prefix edges, three full positive cache keys). For H4–H9, impose exactly two additional distinct full positive BRC cache keys, signed six-axis primitive expansions of `a,c,d,e,f,g`, the original nine seeded observer states, six signatures `de,ed,ce,ec,feg,gef`, and rank nine at each horizon via the original four-clause mask.

The full finite horizon census yields 158 distinct raw endpoint-feasible new keys, 128 endpoint-cover unordered key pairs, and **124 pairs satisfying the combined rank-nine cover**. For **every one** of these 124 pairs, **each horizon H4–H9 individually admits rank nine under one key alone**. Orient each pair as E (the unique key reaching rank nine at H4) and L (the unique key reaching rank nine at H9). Across the six horizons, the per-key rank availability forms E-only, then an optional contiguous both-keys overlap, then L-only. Therefore every pair admits a monotone **one-switch** rank-nine schedule E through horizon s, L afterwards.

Exactly **174** (pair,s) schedules satisfy rank nine at every horizon. For 84 pairs there is one valid switch boundary; for 31 pairs two; for 8 pairs three; and for 1 pair four. The possible switch counts by s are H4=9, H5=49, H6=66, H7=50, H8=0. Every one-switch rank-nine schedule uses the late key at H8 and H9.

The ten exact patterns ELLLLL, EELLLL, E*LLLL, EEEELL, EEELLL, EE*LLL, E**LLL, EEE*LL, EE**LL, E***LL have multiplicities 2, 24, 4, 28, 30, 12, 2, 15, 6, 1 respectively, where `*` means both keys independently achieve rank nine.

## Certificate, reproducibility and proof

`VERIFY_EC49FDJ.js` is a self-contained executable using exact integer/bit state transitions on nine observer seeds and each signed primitive expansion. It enumerates all **2,376,230 endpoint-valid ordered operation words** at horizons 2–9 (of which **812,924** have an allowed observer signature). It computes the exact rank masks per (h,full positive key), then enumerates the full feasible key census with the proven lifespan condition `max(x-1,y+2z-1)<=h<=x+y-1` over `0<=x,y<=10,1<=z<=5`. Rank nine is the predicate `(mask&18)&&(mask&20)&&(mask&33)&&(mask&40)`. Enumeration of all key pairs and every horizon produces all 124 rank-feasible pairs, their per-key rank patterns and all possible one-switch boundaries.

The executable asserts both earlier word/signature censuses and 158/128/124 counts, as well as 174 schedules and its full distribution. The complete new 124-pair set was **independently cross-compared with the immutable EC49FAW report**; the equality check succeeded. The exact output `EXACT_REPORT_EC49FDJ.json` retains each pair, the six-horizon availability pattern and every valid switch. No sampling, floating-point observer, mixed-key shortcut or word-order collapse is used. The finite theorem follows by exhaustive coverage of the stated bounded key set, observer language and schedule predicate.

## Consequence and parent objective

The 174 schedules supply a complete collection of **one-switch rank-nine feasibility witnesses** for all 124 pairs. This is a useful starting family for signed-native prefix optimization. It is not an assertion that every minimum-prefix path solution may be represented by a one-switch schedule: two keys may still contribute different words to the same horizon, and alternative key patterns may improve cross-horizon prefix sharing.

The verified author-side five-key construction with 94 edges remains the parent comparison frontier; the original five-key <=93-edge H2–H9 mother target remains open. Next: exact signed-native prefix minimum cover on the 174 restricted schedules, followed by an unrestricted comparison of any missing mixed-key behavior.

The actual Github actor may save author-side evidence; native ownership/claim and independent Driver review are separate project operations.
