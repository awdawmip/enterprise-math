# R5 next unit — below the solved saturated-v physical ratio slab

Date: 2026-11-08 Asia/Shanghai. Current author-proved frontier is RATIO_BRIDGE.md in this directory, extending RESEARCH.md. Frozen scientific pins: global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Mathematically exact evidence includes 8 inherited rational calibrated Q matrices and the all-real convex proof; new Fraction checker: 2187 cases.

Verified proof scope: for every real 0<=s<=g<=1, 1/2<=eta<=1, 0<=p,q,theta,h<=1, FULL_HIST source
x=(g,s,eta*s, s*(13/40+eta/80)*p, 9*eta*s/40+s*theta/10, s*(3/40+21*eta/80)*q, s*theta/10)
and its interpolation with one seedless target y have an exact 7-key Blackwell transfer matching eP,eQ,TP,TQ for all randomized declarations. This fills the **entire physical (u,w) rectangle** at each eta in the stated interval, full saturated-v z range, and early g,s cone; residual R=(9/10)*eta*s^2*(theta-1).

**First new falsifiable route:** fix eta=1/4, g=s=1, p=q=1, theta=0. Exact input is
x=(1,1,1/4, 21/64, 9/160, 9/64, 0),
where u_max=13/40+1/320=21/64, w_max=3/40+21/320=9/64, v-z=9/160, residual R=-9/40.
Search a legal seedless LR target y constrained to common affine face F={z=a/10, v-z=9b/40}, preserving both times and admitting a nonnegative rational 7x7 matrix Q such that
sum_j Q[i,j]=M_i(y),
sum_i Q[i,j]=M_j(x),
sum_i r_i Q[i,j]=r_j M_j(x),
with same seven r=(1/10,1/2,3/4,1,5/4,3/2,19/10).
A rational solution would supply a new anchor to interpolate across eta in [1/4,1/2]; an exact dual infeasibility certificate would exclude only this chosen affine-face strategy, leaving other seedless faces possible. Test eta=0 edge separately: b=0 makes v=z and R=0, but z<a/10 is generally not on F.

**Alternative independent route:** vary unsaturated v-z<9b/40 at a selected rational a,b,z,u,w; seek another affine face, an observer-equivalent lift, or a pointwise four-observer separation witness.

Mother objective remains full FULL_HIST versus seedless LR pointwise four-observer equality (not only convex support equality). Current material is author-side: GitHub authenticated user awdawmip; native status and tasks returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / STATUS_DATABASE_UNAVAILABLE, operation_sent=false, Site research_authority_granted=false. Active owner/formal CLAIM unresolved; review and admission pending. No protected state modified.
