# Stage285-B — causal upstream occupancy / joint mixed moments (author handoff)
Status: PORTABLE_AUTHOR_PROOF / EXACT_FINITE_REPLAY / UNREVIEWED / NOT_ADMITTED.

Research question: when source-dependent downstream route masses depend affinely on an upstream source-blind control X, what exact BRC moment residuals preserve two repeated visits of one globally shared port Y under correlated ex ante controller mixtures?

Proof: `PROOF_STAGE285B.md`; actual executed Fraction program: `REPRO_STAGE285B.py`; exact stdout: `REPRO_STAGE285B_EXECUTED_STDOUT.txt`; next scientific unit: `NEXT_TASK_PACKET_286B.md`.

Result: the exact convex hull of (u,m1,m2,c1,c2)=(E[X],E[Y],E[Y²],E[XY],E[XY²]) is given by two coupled subprobability moment blocks (a0,b0,d0)=(1-u,m1-c1,m2-c2), (a1,b1,d1)=(u,c1,c2), each satisfying 0<=d<=b<=a and b²<=ad. Every real feasible point admits <=4 deterministic global settings; rational points admit rational witnesses. The five coordinates preserve every source-tagged ordered terminal-path mass in this declared two-visit finite-horizon model.

Explicit P/Q strictly positive non-IID source law: P(R=0)=1/4, Q(R=0)=1/3; P(S=0|R=0,1)=(1/4,3/4), Q=(1/3,2/3); U~Bern(X) before source draws, downstream route T=R XOR U, port Bern(Y) sampled twice. Ex ante mixtures A={(0,0),(1,1)} and B={(0,1),(1,0)} with weights 1/2 have same (u,m1,m2)=(1/2,1/2,1/2) but observer F=1[(T=0,B) or (T=1,C)] changes from P:1/8 to 3/8 and Q:1/6 to 1/3. At this moment slice, true mixed-policy optimal rewards are P=3/8 and Q=1/3; invalid product-moment factoring yields 1/4, gaps 1/8 and 1/12. This is NOT an unconstrained optimum gap and not a novelty claim.

Actual exact check: `python REPRO_STAGE285B.py` -> `STAGE285B_CAUSAL_SPLIT_MOMENT_HULL_EXACT_PASS`. 162 source-policy pair checks, 3888 ordered leaf checks, rational mixture and four-atom witness validation. General real theorem is algebraic, not inferred from the finite grid.

Frozen readings: GLOBAL_KNOWLEDGE_V1 main@ebc95a36c61f05438c3294b5dd4c1e2011f51f70, Enterprise Math main@e3148a75734182faea1e2822c84bd782b43005bb, predecessor Stage284-B@3fb3545eaa820982ffd3360b4e60965c472a7f92. Native Site research authority=false; owner query CONTROL_QUOTA; no CLAIM/Source Result/independent Driver review. No native P000 X6 dynamical correspondence asserted.

Next: Stage286-B three repeated tied-port trials, higher moments and an explicit 3/128 counterexample to five-coordinate sufficiency; preserve Stage278-A Bellman new-face separately.
