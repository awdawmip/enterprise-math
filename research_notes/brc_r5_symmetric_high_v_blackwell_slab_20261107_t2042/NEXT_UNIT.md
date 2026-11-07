# R5 next unit: Blackwell lifting with w>0 side flows

Frozen science pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e.

Completed author-side proofs and executed exact checkers in this folder:
1. RESEARCH.md, VERIFY.py, EXACT_OUTPUT.txt: all-real 3-parameter high-v slab x=(g,s,s,0,9s/40,0,z) with 0<=s<=g<=1, 0<=z<=s/10, all seven declarations, both signs of residual.
2. SIDE_FLOW_U_MAX.md, VERIFY_SIDE_U_MAX.py, OUTPUT_SIDE_U_MAX.txt: full seven-key declaration cube at strict-negative corner x=(1,1,1,27/80,9/40,0,0), lifted by y=(686/705,686/705,659/705,1233/3760,347/1128,0,343/3525) with exact seven-key calibrated transport and both times preserved.

Next independent corners: x=(1,1,1,0,9/40,27/80,0) and x=(1,1,1,27/80,9/40,27/80,0). Find one legal seedless y with both times identical and a nonnegative seven-by-seven rational matrix Q with row sums M(y), column sums M(x), and weighted column sums r*M(x). Derive an explicit all-declarations kernel, then interpolate across a parameter family if possible. For variable y, obey full flow bounds and seedless bilinear condition 9bz=4a(v-z); a failed single candidate channel is not global infeasibility. If seeking a four-observer separation witness, certify all seedless feasible flows.

State: author-side portable GitHub PR #1767, native active owner/CLAIM unconfirmed because service status/task list returned BACKEND_IDENTITY_OR_VERSION_MISMATCH with operation_sent=false; independent mathematical review still pending.
