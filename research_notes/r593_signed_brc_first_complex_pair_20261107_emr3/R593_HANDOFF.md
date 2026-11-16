# R593 | signed BRC auxiliary zero pair handoff

- Frozen science: R462 @ `18783e01e3646c72b7aab3b16d3f565e83e6446f`; direct prior R592 @ `c64976ddd082a4c4c807908072128c4a94971ee9`; coefficient identity and envelope R590 @ `88406fcfe23c2c23c2c27887b87613f8dcd6031a`.
- Object: scalar auxiliary `F(z)=24 sum_{j>=0}(-8z)^j/(2j+4)!`; `F_k(z)=sum_{j=0}^{2k-1}(-1)^j H_k(j+2)/(H_k(2)k^(2j)) z^j`, not the joint twelve-branch native BRC spectrum.
- New exact result: `N_F(10)=N_F4096(10)=0`; `N_F(13)=N_F4096(13)=2`; both have exactly one nonreal conjugate simple pair in annulus `10<|z|<13`. Fully rational polygon winding and Rouché bounds, plus real-axis exclusion. See R593_PROOF.zh-CN.md.
- Exact executable `R593_VERIFY.py`; stdout `R593_EVIDENCE.txt`. Inputs (r,M,J,L,k)=(10,2048,18,32,4096) and (13,8192,18,32,4096); 8192 and 32768 polygon nodes. PASS decisions all Fraction comparisons.
- Researcher actor: connected GitHub `awdawmip` (admin); private native gateway `em_status` responded `BACKEND_IDENTITY_OR_VERSION_MISMATCH, operation_sent=false`. Owner and official CLAIM unconfirmed; this is author-side noncanonical research, not RR/DR/Foundations admission.
- Next test: tighten rational annulus and build certified complex root boxes; improve finite k bound while keeping signed BRC native branches and P000 unaltered. Independent Driver review of R590–R593 pending.
