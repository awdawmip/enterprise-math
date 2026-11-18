# EC49FSI follow-up: exact q32/q34 common discount alpha=7/16 anchors (exploratory)

Date: 2026-11-18. Frozen original BRC16943 input pin fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Same 141 named joint-response profiles, 228 original observations, and uniform prior as the EC49FSI rectangular theorem. Set the common q32/q34 discount alpha=7/16, q140 discount z in [0,1], with F=141V/t.

Four **individual points**, each computed using the full 228-original-observer exact Bellman DP and separately recomputed by the independently reconstructed raw-family decoder, agree as follows:

| z | exact F(7/16,z) | optimal witness triple (U,Q=N32+N34,K=N140) | witness root |
|---:|---:|---:|---:|
| 0 | 1811/8 | (306,182,0) | q32 |
| 1/4 | 3553/16 | (304,169,32) | q34 |
| 1/2 | 3325/16 | (319,93,141) | q140 |
| 1 | 2197/16 | (319,93,141) | q140 |

These are certified **finite point values**; the complete continuous interval phase diagram for alpha=7/16 has not yet been established. The data already identify different native root-observation regimes and can seed the next alpha corridor 3/8 to 1/2 without making an unverified full-interval extrapolation.

Original solver: EC49FSA_THREE_OBSERVER_SOLVER.py. Independent solver: EC49FSA_FSB_INDEPENDENT_CHECK.py. Both in the self-contained EC49FSH/FSF predecessor science packages. For each point the reported witness triple reconstructs the exact cost U-(7/16)Q-zK and equals Bellman optimum. Mathematical admission: AUTHOR_EXACT_FINITE_CHECKED / NOT_REVIEWED. Independent portable research, not formal Task/CLAIM/Result.
