# T6 p13 q13 split(3,10) — complete exact affine exclusion ledger

Driver EM-DVR-DEBB5E, shared nonblind context, frozen science d84bd940cfb093cdc60e569f15cad58772a51dca. This ledger consolidates executed row-level exact proofs; no new computation claimed by the consolidation itself. The source theorem and full reproducible code are at e23a23dc6ed2e3cdd980cc7b8660a48993e82f6d:research_notes/driver/2026-11-28_t6_q13_split3_10_len1to3_modular_interval_join.md. Input basis is bcab5ce85b368d2b65a74340ceadb4527da0f01e at 0bf185c700fe5a46b5e7ad1b49f7441c1a2ee7be:research_checks/T6_P13_Q13_SPLIT0_13_AUTHOR_EXACT_CERT_20261126.json.

| Negative length | Patterns | Raw pairs | Budget feasible high pairs | First interval pass | All-coordinate survivors | Valid | Commit |
|---|---:|---:|---:|---:|---:|---:|---|
| 1–3 | 42 | 5887440 | 5887440 | 1847825 | 194 | 0 | e23a23dc6ed2e3cdd980cc7b8660a48993e82f6d |
| 4 | 27 | 41446080 | 41446080 | 12432104 | 771 | 0 | 247fb25021d2949951d3fddb4182d172e1e4339d |
| 5 | 21 | 168486240 | 165854520 | 47682033 | 2133 | 0 | dc034735dae1b09cfcdce2dba599aaf2b9634073 |
| 6 | 15 | 417362400 | 364523640 | 101369659 | 2994 | 0 | 9e05353e4d53f80dcf19d18b6981074f907a0f9b |
| 7 | 9 | 662669280 | 431110160 | 117450409 | 2510 | 0 | 4c4161e9588daef8cf66af11b12fb89a6973f0d0 |
| 8–10 | 12 | 1355596320 | 444771600 | 119275325 | 2298 | 0 | 94f602bc20ae56461fcb5d4140b057836e25e217 |
| Total | 126 | 2651447760 | 1453593440 | 400057355 | 10900 | 0 | |

All three positive partitions crossed all 42 negative partitions of 10, including common atoms, in relaxed nonsmooth domain; raw domain counts are separate from the individually high-budget-feasible domain. All coordinate-box survivors restored and checked exact integrality, all six congruences and both signed budget inequalities. The ledger's 84 new patterns, 2645560320 raw pairs, 1447706000 budget-feasible high pairs, 398209530 interval passes, 10706 restored vectors, zero valid, are new relative to preceding length1–3. The first interval eliminates 72.493757% of new budget-feasible pairs without visiting them individually; this is count reduction not measured wall-clock speedup. Minimum excess among new box survivors is 1125, masses (3456,2908), not a global budget lower bound.

Scope: split(3,10) independently exhausted under stated six mixed congruences, signed mass budgets 2331 and p13 q13 high-atom model. No author field comparison in new lengths, no clean independent review of Driver's own proof, no formal acceptance. Global independent exact-solver coverage 416/885 (101+77+112+126); remaining split(4,9)150, (5,8)154, (6,7)165. Observation-envelope implication, H0, lower-prime completion and global T6 remain open. Next use same modular join for split(4,9); no replay of completed scopes.

All five new source files read back exact; blobs:
length4 4a50208f9cbd9d252c904f7ba05e394579462fcd
length5 42c99d5ecbd4e31cea195c21fa444b7ea93f64db
length6 a458d459b3a1cdc09a5bce496bfad637633f03e6
length7 1b3fb22e3e8ec6e77e51d382f220ab2f08a43aae
length8–10 a7b1a128cb447016b7499d54353ec47458668b51
