# Stage205 — next exact full-history primal unit

**DUAL_CANDIDATE_ONLY / PRIMAL_UNPROVED / UNREVIEWED.** Continue the external IID ternary N14 minimax model with P=(3,1,20)/24, Q=(2,2,20)/24, **arbitrary complete ordered-history randomized policies**, and preserved exact positive P/Q branch mass provenance. This is not native P000/X6 dynamics.

Verified author-side Stage204 endpoint: alpha204=1237582032550008115/3505953353861431296, V204=2225727754437932573/219122084616339456; proof PROOF_STAGE204.md, exact certificate certificate204.json, executable independent reference REPRO_STAGE204.py (PASS 355660 ordered DFS nodes).

Stage205 *dual candidate only*: K205=L205=16200/137, H205=175689269891985199711/1876232849527406592, downward kink from K204 28063584/7352105. First switch at (12,3,1), continue→report P; ties (12,3,1) report P/continue and (14,0,0) report P/report Q. Rational Bellman enumerated 680 states and 1238 positive gaps, minimum 69107093/19635830784, in scan_stage205.py / certificate205_dual.json.

**Next exact question:** compute four deterministic tie-corner observation vectors (eP,eQ,tP,tQ) by both Fraction conditional-suffix recursion and independent unmerged integer-mass full ordered-history DFS; inspect mixed coefficient and ancestor cones, solve equal-error coin over its actual legal real range, verify strict P vs Q time dominance and contact with Stage204 endpoint, then prove the all-real optimal interval or give an exact rational obstruction. The strict-right fixed-line claim must be separately proved after primal construction.

Original source scope: global main 138a017a98649b4a7d16ddbff1cc0dfa13028cfb; EM main a7d98c76f02e09d6131f16b04a97dede4026b2eb; Stage203 parent d70598906ed8ffac8fba281107b581ccc0517cf3. Existing PR #1571; no native CLAIM, frozen Source Result or Driver acceptance.
