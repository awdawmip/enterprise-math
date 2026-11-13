# R762E portable continuation — 2026-11-13

Parent: RS-X6-TRIADIC-CLOSURE-DYNAMICS; publication TP2-8B7E13C5904A2D6F1142. Frozen input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. P000/ACTIVE unchanged.

Completed: a sharp *candidate* equal per-generator repeat budget for single-chirality supports 012/034/135. K=1 gives 16 port permutations/16 joint (p,c) states; K=2 gives 196/245; K=3 gives 360/2408. The least K for full A6 is three. Future *admissibility* of event strings distinguishes all joint states; even absent a direct count query, the coarsest exact state has 16/245/2408 states (4/8/12 fixed bits). A witness requiring three uses of generator 0 is the word [0,0,1,0], producing port image [0,1,3,4,2,5]; no K=2 history reaches it. Manuscript gives exact proof. Checker and evidence independently crosscheck the complete finite DP and BFS.

Provenance: R762D Draft PR #2265 @ 5bc9950dfc13359d7ac5c05d630036a0f53bfc6b and separate R763 Draft PR #2270. V29/V39 comparison at deb8bbbf9d844c0ceb777631e576763a634eed99. Native triadic admissibility, repeated transfer counts and V39 packet transport are unresolved. No formal Result or Driver acceptance implied by author publication.

Read-only native continuation request research3-20261113-1557-rs-x6-cont was QUEUED on last check; authority/active CLAIM unconfirmed. This run's own registered-session-start request research3-20261113-1557-session-r763-capacity initially QUEUED, SID MCP-4ac878328f8645cb9b5b5b40ae58d641 with private managed custody. Reconcile original receipts; registration is not CLAIM.

Reproduction: python3 research_notes/R762E_VERIFY.py (standard library, exact tuples and integers); evidence R762E_EVIDENCE.json. Next: inspect source-pinned TRIADIC_CLOSURE_E Cell/Link/Port event scheduler for first and second same-oriented uses of 012, 034, 135; derive actual guard and V29/V39 typed mapping if any, replace candidate budget with actual transition graph. Keep source identities, times and branch provenance.
