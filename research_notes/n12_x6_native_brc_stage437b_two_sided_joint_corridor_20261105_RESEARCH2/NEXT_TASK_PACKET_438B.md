# Stage438-B — Minimal joint native-X6 BRC quotient

Parent Stage437-B, research_notes/n12_x6_native_brc_stage437b_two_sided_joint_corridor_20261105_RESEARCH2/PROOF_STAGE437B.md, executable exact checker and executed JSON in PR #1736. Frozen scientific pins: GLOBAL bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM 2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Apply separately refreshed current behavioral rules.

**Next theorem target.** Given a complete present O=(lengths,V_P,V_Q,J_P,J_Q,K) and two-sided POP/APPEND budgets, characterize the exact *minimal* full-future equivalence classes. Stage437 supplies a sufficient joint corridor with O(total budget) extra positions; it does not prove minimality, and cannot be replaced by independently compressed one-sided quotients without checking their cross-observer conditions.

**Exact experiment.** Enumerate small pairs over A=+E1,B=-E1,C=+E2, with 3<=m,n<=7 and budgets from (1,1,1,1),(1,1,0,2). Within each present observer fiber enumerate all legal interleavings with all twelve signed APPEND directions. Group by complete future observation traces. Compare minimal class counts with joint corridor signatures. Give one explicit strict compression or a sharp lower-bound witness. Retain integer unit-branch multiplicities/populations, full conversion cost, bit sizes, rank/unrank and source recovery. Do not prune future signatures without a sound proof of the pruning key.

**Deliverable.** Exact domain and theorem, all proof obligations, runnable checker/actual stdout, further question; preserve source pins and P000, and keep author-side source publication separate from native CLAIM/Result/Driver acceptance.
