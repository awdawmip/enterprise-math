# R5 next unit — genuinely non-seedless mixed low-ratio parameters

Frozen scientific pins unchanged: Global a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. This concerns the frozen seven-node P/Q-BRC observer, not native X6 dynamics.

**Two exact extreme source corners are author-proved for all real 0<=t=a/b<=1 with g=b=1:**

1. **Positive residual:** x_plus(t)=(1,t,1,0,t/10,3t/40+21/80,t/10), R=+9t/10. RESEARCH.md, BRIDGE.md, exact programs/outputs prove t in [0,1/5] using a rational-function 11-edge kernel and a fixed-face two-anchor bridge; preceding PR #1800 covers t>=1/5.
2. **Negative residual:** x_minus(t)=(1,t,1,13t/40+1/80,9/40,0,0), R=-9t/10. NEGATIVE_CORNER.md, NEGATIVE_VERIFY.py and NEGATIVE_OUTPUT.txt give an affine nine-edge full-real F-face construction on [0,1/5]; PR #1800 covers t>=1/5.

Both are author-side theorems relying on independent author-side PR #1800 for their t>=1/5 range. Independent review/Result/acceptance remain pending.

**Important correction:** the initially suggested p=q=theta=kappa=1/2 interior test has R=(9ab/10)(theta-kappa)=0 and is already seedless. It is NOT a discriminating mixed non-seedless test. Do not count it as new research progress.

**Next discriminating tests:** fix t=1/20 and p=q=1/2; choose (theta,kappa)=(1/4,3/4) with residual -9t/20 or (3/4,1/4) with residual +9t/20. Seek exact target and nonnegative 7x7 Blackwell kernel for those sources, ideally also for t=0 and t=1/5 on a common affine seedless C_tau face enabling all-real interpolation. Exploratory floating LP observed feasible candidates for (theta,kappa)=(1/4,3/4) at tau=3/4 and (3/4,1/4) at tau=1/2 for t in {0,1/50,1/20,1/5}; **no exact rational reconstruction or independent certified feasibility for these mixed candidates yet**. A floating LP suggestion is not proof. Recover exact rational anchors, verify each seven Q mass rows, columns, weighted columns, physical capacities, seedless equation and two stops; then prove interpolated family analytically. If a chosen face fails, change representation; a face-specific negative LP does not imply full-model impossibility.

**Source/control:** ten verified research files and actual local output in Draft PR #1801; previous source-tracking RA-R5-LOWALPHA-CF17FA19-20261108T1352 remains retrospective UNKNOWN session, not formal CLAIM. Native control_tasks/session_start returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE / operation_sent=false, Site research_authority_granted=false; no authenticated Researcher-ID, Owner, CLAIM or mathematical admission. Preserve frozen science pins.
