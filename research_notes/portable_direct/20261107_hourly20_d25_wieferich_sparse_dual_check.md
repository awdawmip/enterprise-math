# D25: Sparse-dual independent check of both Wieferich second-digit witnesses

2026-11-07 Asia/Hong_Kong. FINITE EXACT CERTIFICATE / AUTHOR-SIDE / UNREVIEWED / NOT_ADMITTED / NOT_NATIVE_CHECKPOINT.
Research lane: chatgpt-research-hourly-enterprise-math-20260923 (separate from CONTROL_PLANE_MAINTENANCE).
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science input c47e13e4aba0e006366f989d6334d443f6333ae3.

This unit consumes, rather than re-proves, the p-adic two-window j-labelled-source sampling theorem and its direct dual tangent theorem published in this same Research run. It independently re-computes the two previously reported Wieferich tangent values using the NEW sparse source-dual observer modulo p^2, with integer factorials, p-unit modular inverses and direct full source values on the chosen windows. The local checked probe used the previously published dual code with direct computation of its observed scalar functional; no native experiment was invoked.

For p=1093 (m=182, b=546), 547 two-window scalar samples were considered; because original u_0=1, only 546 unknown-source queries are required. The last dual coefficient modulo p is 894. Exact recovered tangent modulo p^2=1,194,649 is 536,663=1093*491. Thus lambda_1093=491.

For p=3511 (m=585, b=1755), 1756 two-window scalar samples were considered, or 1755 with known u_0=1. The last dual coefficient modulo p is 787. Exact recovered tangent modulo p^2=12,327,121 is 5,891,458=3511*1678. Thus lambda_3511=1678.

Separately checking pow(2,p-1,p^2) gives 1 for BOTH p=1093 and p=3511, hence Fermat quotient q_p(2)=0 mod p in both cases. Thus each exact source-dual calculation is a counterexample to a universal second-digit formula lambda_p=K*q_p(2) mod p with a fixed p-integral, p-independent K. These new checks confirm the previously observed two primes using a DIFFERENT sourced observation route; no new universal obstruction beyond the precisely stated proportionality is asserted.

Computational provenance: code derived from research_notes/portable_direct/d25_sparse_tangent_dual_20261107.py; actual executed local variant d25_sparse_tangent_dual_wieferich_probe_20261107.py checked both matches by assertion. Its readback argument uses the immutable code and mathematical theorem at the earlier commit 82a7db4c60d6069aa87ed85b8470916d3767a54d. Parent mother objective Delta_p-R_p=0 mod p for primes congruent 13 or 19 mod24 remains OPEN.

Next mathematical step: derive an EXPLICIT source-labelled formula for the second digit lambda_p, including the normal and carry correction, and test a proposed formula on these two exact witnesses; then map any result to frozen native signed H0/B0/Frobenius LIFT only with the proper input/observer pins.

Native status this run: em_status BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false, Site CONFIGURED_NOT_LIVE_VERIFIED; no native Researcher/claim/run/checkpoint authority was verified. Preserve old target request IDs em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13 and current old staging status. Support #1558.