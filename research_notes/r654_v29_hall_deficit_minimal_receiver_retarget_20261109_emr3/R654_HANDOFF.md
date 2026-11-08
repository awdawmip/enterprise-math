# R654 handoff — exact minimal receiver-target correction by Hall deficit

2026-11-09 Asia/Shanghai. Parent RS-X6-GLOBAL-TRIADIC-FIELD-NETWORK-LAW. Predecessor R653@29ee0ede86b98a63334b2872978436b908abb2f6. Frozen science R462 signed BRC@18783e01e3646c72b7aab3b16d3f565e83e6446f and native V29@b62110008321d9147212cb89f2627ff613c2550d unchanged.

Theorem: Fix a sender margin s and receiver target t on a finite licensed port graph H, sum s=sum t=L. If every positive-supply sender has some licensed receiver, the minimum number of receiver-target unit relocations that makes t realizable by nonnegative V29 TRANSFER events is exactly max_U(s(U)-t(N(U)))=L-maxflow. Proof: Hall lower bound; integer maximum flow followed by completion of unmatched senders to arbitrary licensed receivers yields equality. Dual fixed-receiver sender correction has the same sharp bound when each positive-demand receiver has a neighbor; isolated active senders make receiver-only correction impossible.

P000 X6 four-cell adjacent path witness: c0 send1, c3 receive1, Δ=1; retarget receipt to c1, realize with one c0→c1 transfer. Signed observer Ω fixed, Δu=Δrin; preserving eventual V27 signed BRC winner or V17/V30 path holonomy is not asserted.

Artifacts: R654_PROOF.zh-CN.md, R654_VERIFY.py, R654_EVIDENCE.json. Author-side exact proof plus 20 finite license graph tests; 1,365 balanced configurations (204 active-isolated infeasible; 1,161 exact Δ cases), 1,069 dual cases and 1,161 signed delta checks. Marker R654_MINIMAL_TRANSFER_RETARGET_HALL_DEFICIT_EXACT_PASS.

Next: retrieve Source >=3-cell actual licensed port connections. Analyze constrained retargeting and the frozen V27 signed BRC observer response to optimal terminal repair. Do not infer a formal native CLAIM, Driver acceptance, physics or writable Source identity from this author-side artifact.
