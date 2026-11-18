# EC49FEG follow-up: 94-edge H7 quota differs from the 109-edge restricted family

Date 2026-11-08. Frozen science fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Evidence: original EC49FDN EXACT_REPORT_EC49FDN.json (case 2200) and original EC49FEG signed native-X6 grammar.

**Exact finding:** EC49FEG's 109-edge optimum applies to 24 words with H2...H9 quotas (4,2,2,4,2,4,4,2), including four H7 paths with nine-state signatures 1,2,4,8. The existing 94-edge certificate has only **22** words, quotas (4,2,2,4,2,2,4,2): its H7 has **two** paths, signatures 16 and 32. Both H7 signature sets satisfy the four exact rank-9 clauses 18,20,33,40. The 109 lower bound is valid in its 24-path subfamily, and does not govern the unrestricted parent 94 witness or its potential ≤93 improvements.

Cache-key allocation also differs. The 94 witness uses one early key (3,1,1) and four late keys (3,2,1),(4,3,1),(4,4,1),(5,5,1). The 109 witness uses two early keys (2,1,1),(3,1,1) and three late keys (3,2,1),(4,3,1),(6,4,1).

Exact native signed X6 prefix accounting:

| H | 94 newly introduced / cumulative edges | 109 newly introduced / cumulative edges |
|---|---:|---:|
| 2 | 28 / 28 | 26 / 26 |
| 3 | 14 / 42 | 9 / 35 |
| 4 | 4 / 46 | 4 / 39 |
| 5 | 16 / 62 | 16 / 55 |
| 6 | 6 / 68 | 6 / 61 |
| **7** | **4 / 72** (two paths 16,32) | **24 / 85** (four paths 1,2,4,8) |
| 8 | 16 / 88 | 18 / 103 |
| 9 | 6 / **94** | 6 / **109** |

94 has 7 more early-prefix edges (42 versus 35), but 22 fewer late increments (52 versus 74), a net 15-edge advantage. This is an exact comparison of two different complete witness structures; it does not isolate a single causal factor because paths, key budgets and quota choices also differ.

A reproducible independent audit is in EC49FEG_94_FRONTIER_AUDIT.py; original rank-2200 certificate is retained unchanged in EC49FDN. Key insight for the next ≤93 search: treat the H7 rank-9 signature family (16/32 pair versus 1/2/4/8 quartet) and per-horizon path count as **decision variables**, alongside the division of five full BRC keys between early and late horizons. Preserve the previously computed 94 optimality certificates for their four fixed early seeds and fixed five-key sets, while exploring changed key sets or early seeds.
