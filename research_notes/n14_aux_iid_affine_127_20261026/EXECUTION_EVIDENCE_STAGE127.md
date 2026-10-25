# Stage127 author-side local exact execution evidence

Local environment: Python standard library Fraction, exact integers, no float-based scientific verification, no Monte Carlo.

* Bottom-up rational Bellman + four-observer corners, file VERIFY_STAGE127.py: PASS. 680 states, 1238 strictly positive nonchosen action gaps, no negative gaps, exactly B=(11,0,1) Q/C and C=(11,6,2) P/C; min positive 71/9459. Exact equalities for Stage126 left endpoint, new Stage127 endpoint, compensation, time margin and dual contact passed.
* Separately authored recursive Bellman + literal ordered-prefix integer-weight DFS, file INDEPENDENT_ORDERED_STAGE127.py: PASS. Node visits for 00/10/01/11 = 809650/809518/789841/789709. First-hit B: 11 prefixes, P 107421875/1451188224, Q 107421875/725594112. First-hit C: 2201 prefixes, P 275125/32614907904, Q 275125/92876046336. Full 4-corner observer vectors and two tie derivatives agree.
* SCAN_STAGE128.py exact first-event ray enumeration: PASS as DUAL_CANDIDATE_ONLY. K=7794/11, L=7256/11, new tie D=(12,2,0), root 5444247642339796165/11158995049906176; min positive 71/8748; no formal Stage128 primal claim.

Evidence status is LOCAL_EXECUTED_BY_AUTHOR; GitHub storage readback is not remote program execution. Native research claims/reviews remain separate.
