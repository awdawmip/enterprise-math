# R5 next research unit — characterize genuine four-observer projection after explicit mass-fiber repair

Frozen science: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Reuse scalar gate 57f7d654e5dd002567e0b0d333937e6e38f3b4cb and its complete seven-variable polytope K(W).

This directory establishes two exact complementary outcomes.

1. An enriched five-observer FULL_HIST point (eP,eQ,TP,TQ,M_{3/2})=(161801/180000,6499/18000,267/80,137/40,27/80) cannot be reached by seedless LR. Exact support gap at the fixed (TP,TQ,M_{3/2}) is 57/8000.
2. After projecting away M_{3/2}, that same four-observer W **IS** reachable by seedless LR: g=u0=1,u1=12/13; X=(81/520,4/13,0); shared z=(81/175,1,0); declare P at r=1/10 with probability 92924/93649, at r=1/2 with probability 169/188, Q elsewhere. The two strategies differ in M_{3/2} by exactly 21/1040. See PROJECTION_REPAIR.md and VERIFY_PROJECTION.py.

The next question is to characterize when this occupancy/label repair works for **all** FULL_HIST four-observer W, rather than extrapolating from the one repaired point. Candidate route: choose rational times strictly inside the timing octagon and construct extreme FULL_HIST declarations with nonzero central J defect. For each target W, build K(W) using all 14 zonotope halfspace inequalities, flow capacities, exact time equations and central J bounds; test the quadratic F=(A+B)J-X1(alpha*A+beta*B) over all real feasible v. Opposite signs give a continuous-root LR construction, strict one sign requires an all-real extremum certificate. A second route derives an explicit rational LR lift for a nontrivial neighborhood or new face family via occupancy transfer, extending the current exact rational repair.

Research classification remains author-side / exact Fraction checked / unreviewed / not admitted. Active owner and CLAIM must be checked separately through native service before formal workflow writes.
