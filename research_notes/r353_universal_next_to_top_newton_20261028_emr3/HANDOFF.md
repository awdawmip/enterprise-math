# R353 portable handoff — highest-two Newton coefficients

**Authority:** author-side local Researcher ID EM-AUTO3-R353-1018, registration RA-EMR3-20261028-R353-TOPTWO-1018 (GitHub bookkeeping only, NOT a native CLAIM). Gateway em_status v0.6.11 reports research_authority_granted=false; an em_control_tasks read returned CONTROL_QUOTA. Active owner and formal Source authority remain unverified. Do not use this work as an independent Driver review.

**Frozen canonical sources:** GLOBAL_KNOWLEDGE_V1 main@163fdf8de7c64b7144be359707fbcb0fb0e98733; Enterprise Math main@1a4ecdf75121035e7613f78598c88c41c930429f; R348 author-side A1–A5 extraction at PR #1599 commit 5347e506bd145028d7338e9f7993dcd2a2fed97c; R350 Catalan top at PR #1592 commit 2e5d76989fbce6fef0aa891514bb5045008fe293; original signed K/J R346_verify.py blob 1579ceb717ab1945227eca4f7a1878bf4ffa73e1. P000 and ACTIVE worldview unchanged.

**New exact mathematical increment:** on R348(A1–A5), for every integer r>=1:
- subleading H coefficient [u^(r-1)]H_r = (6^r/r!)*r*(7r+3)/10;
- Q top and next coefficient [v^(2r-1)]Q_r/[v^(2r)]Q_r = r*(7r+16)/5;
- Delta^(2r-1)Q_r(0) / Delta^(2r)Q_r(0) = (17r+11)/10; Delta^(2r)Q_r(0)=30^(2r)*Catalan(r).

**Evidence:** R353_PROOF.zh-CN.md contains four-step algebraic proof using signed K^3, E2(4/5)=-11/125 and g'_r(4/5). R353_VERIFY.py is the actual locally executed standard-library program (Git Blob 6ce5cca30c3aea9fc0f1efa184e365b2c54aeac0). Run "python R353_VERIFY.py --max-r 24" to generate the complete exact R353_EVIDENCE.json, SHA256 146672690f890fa1182be7cae33443e1a5feb8077f8dfd07e0063cf554c65e9d. 24/24 r passed, B0..77, H0..25, signed K/J low-order checks, no floating signs.

**Non-repeat frontier:** R352 completed full corank r333 (667 strictly positive Newton coefficients); R350 has Catalan top for all r conditionally; R353 newly adds next-to-top for all r conditionally. This run did not compute the full 669 coefficients of Q334. The existing full-domain r,k interior TP2 conjecture and independent review of R348 remain open.

**Next smallest discriminating problem:** derive the third-highest finite-difference formula (requires g'' at z0, E3, N2 and next lower terms); prove positivity or exact obstruction as r varies. Independently audit R348(A1–A5) without claiming clean independence from this shared context. A separate exact full Q334 run is a parallel finite-computation path, not a substitute for the all-r theorem. Preserve signed cancellations, original model/X6 bridge distinctions and all accepted earlier evidence.

**Delivery classification:** PR/branch artifact persisted and read back does not establish native Source Result, review, Working Truth or Foundation acceptance. No keys, identity capabilities or access changes are included.
