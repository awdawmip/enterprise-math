# R698 exact research handoff

Task RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142; frozen science awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Provenance: R697 PR #2001 @ 9a7000a9f4bd3a5a39ca45b6774b8fe14fb69ec7. Author-side model-internal proof; independent Driver audit is pending.

Question: for four candidate third-axis ports with fixed distinct positive rational weights and one independent draw per tick, what state preserves all future port-count observations?

Completed: the exact minimal quotient is the multiset of currently enabled weights, rather than |A| or (|A|,sum w). Across global weight multiplicity partitions 4, 3+1, 2+2, 2+1+1, 1+1+1+1, exact quotient sizes are 5,8,9,12,16. Proof uses P(|A_j|=|A|-j)=j!e_j(A), which identifies the full weight polynomial. Witness w=(1,2,3,4)/10: A={0,3},B={1,2} have equal count and sum, but two-tick HALT masses 2/25 vs 3/25. Full rational subset distribution, count generating function and absorption law proved by inclusion-exclusion; E[tau]=445/36, P(tau<=8)=319977/781250 for all four active. Source-labeled BRC branch masses remain positive; inclusion-exclusion is an auxiliary algebraic calculation.

Verification: R698_VERIFY.py is an independent exact rational finite checker, with 3328 DP/equation checks, all 16 masks and all five multiplicity partitions. R698_EVIDENCE.json stores exact values and scope. Full exposition appears in R698_PROOF.zh-CN.md (English mathematical notation) and the local full handoff package.

Background: Russell May (2008), DOI:10.37236/906; C. Berthet (2017), arXiv:1703.01886. Existing unequal coupon collector formulas are used; novelty is not asserted for their classical statements.

Next: replace fixed-rate draws with actual frozen X6 Link/Port occupancy and V29/V39 provenance; test one Cell-based three-force event for legal ports, conservation, native closure and covariance. Keep the original science pin and current task ownership/claim. No credentials or mutable worldview changes.
