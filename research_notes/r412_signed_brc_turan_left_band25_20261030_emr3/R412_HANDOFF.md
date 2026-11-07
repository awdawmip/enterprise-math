# R412 Portable Research Handoff

Research status: AUTHOR_SIDE_EXACT / UNREVIEWED / NOT_ADMITTED. This is a theorem for the stated signed BRC auxiliary combinatorial object; no native X6/physical transfer claimed.

Predecessor: R411 immutable source commit 50265984abd73464b103f2c1075f4de569d585d8, same Draft PR #1708. Do not redo s=24. New mathematical claim: for every integer r>=26, D_(r,25)>0, where delta/H/D are defined in R412_PROOF.zh-CN.md.

All exact P/Q integer coefficients (51+51 positive) are in R412_EVIDENCE.json. Original JSON SHA256 d30954cd5e3131b89164c567c8d7fe4a3a2612587623970d4db1c83d9e55400e. Reproduce: python r412_verify.py (SymPy rational/integer arithmetic) -> R412_EXACT_PASS 2 51 51 95 285; python r412_independent_verify.py (standard library) -> R412_INDEPENDENT_INTEGER_PASS 10 points, 30 Catalan-kernel checks. Symbolic rational-identity plus coefficient positivity provides the unbounded proof; finite grid checks are secondary tests.

Combined author-side frontier: fixed left s=3..25; fixed right 1<=r-s<=128. Open region: s>=26 and r-s>=129, first integer (r,s)=(155,26). Smallest next unit: prove/refute all r>=27 with s=26, or derive a uniform two-parameter positivity mechanism/counterexample. Independent review must check upstream R403/R404 model transfer and exact symbolic identity, not only sample points.

Snapshot pins: Global Knowledge main@51309f36bdcd96b26f08d9a10153cfca1142ecda; Enterprise Math main@dcde68d8979770a9aa5d29ef7a0591a98b9913de, 2026-10-30. Native gateway: research_authority_granted=false, CODE_REVIEW_REQUIRED, CONTROL_QUOTA. Formal owner/CLAIM/Result/Review not secured. GitHub persistence or activity registration is not mathematical admission. No worldview/P000 changes. No credentials or permission changes.
