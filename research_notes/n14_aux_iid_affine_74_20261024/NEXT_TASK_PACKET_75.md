# N=14 auxiliary iid: 75th affine interval — unproved continuation

Exact external model: P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=14. Error pair e_P=P(declare Q), e_Q=Q(declare P); objective V(alpha)=inf max(t_P,t_Q) for e_P,e_Q<=alpha.

Proved by the author (not independently Driver-admitted) through segment 74:
alpha74 = 2585972551358493847/7450150876955541504
V74 = 24565716022242816749/1862537719238885376
s74 = 12002006216766011/20889600000000000 at B=(12,0,1).
The stop A74=(12,5,1) must be fixed to immediate P. Retain every inherited deterministic stop decision from the 74th verifier. The earlier 73rd source is pinned at 44b91386326e39d851697927ca33db98baf86f4e.

New *exploratory* dual crossing (not a theorem):
K75 = 35653474730376/9239954171,
lambda_P = 72 + (8/9) K75, lambda_Q=K75,
A75=(4,1,3), prospective continuation versus immediate Q.

First unanswered question: precisely enumerate surviving ordered first-hit paths to A75 and P/Q probability weights after all earlier stops; enumerate all newly truncated descendant terminal paths; obtain exact continuation risks and the compensating B coin. Establish eta75 and verify its sign and real-parameter coin feasibility. Carry out all 680 normalized Bellman state comparisons and 1240 nonselected action comparisons, primal endpoint/worst-time checks, zero mixed terms (if true), and right-end support sharpness. Publish a complete exact proof or a certified counterexample/obstruction; a candidate is not acceptance.

Reproduction/source: PROOF.en.md, verify_n14_74.py, verify_n14_74_crosscheck.py and certificate74.json in this directory. This is an auxiliary iid ordered-branch model, not a native BRC/X6/Heartbeat proof. P000 and ACTIVE worldview are unchanged; no formal owner CLAIM, frozen Result or Driver acceptance is implied.
