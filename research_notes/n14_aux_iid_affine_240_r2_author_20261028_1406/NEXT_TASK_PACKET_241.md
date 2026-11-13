# NEXT_TASK_PACKET_241 — Author-side exact Stage241 continuation

2026-10-28. Class `STAGE241_DUAL_ONLY`; frozen objective is the **external** N14 IID full ordered-history minimax problem, P=(3,1,20)/24, Q=(2,2,20)/24. Prior stages 236–240 have completed **author-side** full-real intervals (not native/independently admitted). This packet does not create a formal Source task, CLAIM, or owner delegation.

Global canonical pin `GLOBAL_KNOWLEDGE_V1 main@4faffbe68584637f37d630e345543a8f7300f394`; Enterprise Math main `f01fb212f8d640ebced88b2dc836b52f4d933596`; protected P000 original blob `770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc`.

Latest Stage240 right endpoint (author proof in `PROOF_STAGE240.md`) `alpha240=362608860595/975198486528`, `V240=2682386241371/365699432448`.

**Stage241 dual-only candidate, exact Fraction Bellman scan:** `lambdaP=452793624/8007455`, `lambdaQ=483729408/8007455`, `H=265760568220237397/5229145980094464`; 680 states, 11 binary ties, 1,229 positive strict gaps, smallest `78125/57653676`. Ties: (4,1,0) P/C; (5,1,0) P/C; (5,1,1) Q/C; (6,1,0), (7,1,0), (8,1,0), (9,1,0), (10,1,0), (11,1,0), (12,1,0), (13,1,0) P/C. `REPRO_STAGE241_DUAL.py` regenerates `certificate241_dual.json`. **No primal interval yet certified for Stage241.**

**First exact next unit:** enumerate all `2^11=2048` deterministic Bellman-tight policies with exact Fraction suffix DP and an independently unmerged integer P/Q ordered-history DFS; compute every `(eP,eQ,tP,tQ)` vector, check Bellman-tight universal support and whether all corners satisfy tP>tQ. Compute all opposite-sign error-balance edge intersections and any directly balanced vertices. Check whether the exact minimal equal error equals alpha240 and whether the maximum is strictly greater; if so prove full-real affine optimality with endpoint witness weights, irrational-interpolation argument, and strict-right separation; otherwise provide a rational obstruction and seek a different non-symmetric dual. Record actual DFS visits, all counts/certificates and validation limits. The exact positive branch-mass representation is BRC-compatible only within this external IID model; no native-X6 transfer is implied.

Publish source, proof, certificate/reproduction details and actual readback to existing Draft PR #1571; preserve this work as `PORTABLE_AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED` until authorized native Source and independent Driver review.
