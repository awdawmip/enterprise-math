# Stage110 research continuation after Stage109

Mother question: exact V14(alpha) for all randomized full ordered-history ternary iid tests with P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), stopping depth<=14. This is an external auxiliary positive-rational branching model, not a P000/X6/Heartbeat theorem.

Stage109 author-exact frontier: all-real interval [alpha108,alpha109], alpha109=13084102500820187507/37682150988866125824, V109=1934432626777903782385/150728603955464503296, K109=491857029/506348, L109=116416632/126587. Ties A=(10,3,0) P/C and D=(10,3,3) Q/C; D Q-stop probability has reached 1, A P-stop probability is 159859205042303/211315200000000<1.

Next dual-only candidate: on L=-185064/635+(21376/17145)*K with D fixed Q and A continued, K110=6497577/6734, L110=3069240/3367, Gamma110=1805151/962 at E=(13,6,4), competing immediate Q. No Stage110 primal interval has been proved.

Proved cone lemma (count monotonicity): a count-state (n,a,b) can reach (n',a',b') only when Δa,Δb>=0 and Δa+Δb<=Δn. For A=(10,3,0) to E=(13,6,4), Δa+Δb=7>Δn=3; for D=(10,3,3) to E, 4>3; for B=(12,0,1) to E, 9>1. Thus E's path cone is disjoint from the preceding A/D randomized cones and from B. Although C=(11,5,4) could reach E by counts, C is deterministically stopped Q in the post-Stage108/109 policy, so no actual first-hit path to E passes through C. This establishes the cone-disjointness needed for affine error compensation, without proving Stage110 primal feasibility.

First executable research unit: enumerate true first-hit P/Q masses and full conditional termination suffixes of E with C/D fixed Q; compute exact balanced-error randomization and active probability cap, 680-state dual Bellman gaps, endpoint/midpoint four moments, all-real optimality and right-support sharpness, or identify the precise obstruction. Validate using separately coded full literal ordered-history DFS.

Reuse Stage109 proof, exact certificate and checked code, and preserve global snapshot main@babff194f059aaaa452e7827f815845aefcb647a plus EM predecessor main@f651ea40d12cee192ecab1bc741f98f1a9e01892. Stage109 remains author-only: native Owner/CLAIM/Result and independent Driver acceptance unverified.
