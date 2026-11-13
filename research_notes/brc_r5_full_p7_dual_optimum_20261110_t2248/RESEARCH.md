# R5: exact full-P7/terminal-bridge optimization of seven fixed dual exclusion certificates

Date: 2026-11-10 Asia/Shanghai. Status: author-side exact derivation and executable rational verification; independent mathematical review and native Source Result pending.

## Scope and frozen scientific provenance

The object is the same seven-likelihood-ratio P/Q-BRC *auxiliary statistical Blackwell observer*, not a new claim about native Heartbeat X6 geometry. Frozen scientific commits: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Preserve the 30 permitted nonnegative arcs, 21 original transport equations, five physical equalities, 26 capacity inequalities, and the same eight physical perturbation coordinates.

Input authorship and immutable evidence: PR #1976 at b9d0da58b74a18fe45f4b29bb238b70df79b96bc (complete five-vertex closed P7 and the seven-column minimal support), PR #1986 at 590b50e71a58632b02c5fb930f9a5c8b1c1219f5 (original 30-column forcing duals and 15x8 sensitivity matrix), PR #1990 at 08ae691eaa7406c0f17a963294565e4f0f32f6f2 (P7-to-P3 bridge), and PR #1998 at e064558d5ae922fa45415e8652bb97bd8eb899aa (uniform-over-P7 two-parameter optimization). All predecessor results remain author-side pending independent admission.

Let V0,...,V4 be the five exact lawful P7 vertices ordered as POLYGON_VERTICES_EXACT.txt in PR #1976. Let W0=P3(1/10), W1=P3(13/40). Each P3(v) has three positive diagonal arcs and belongs to the same lawful physical affine family. The path family is p(t,v,P)=(1-t)P+tP3(v), with 0<=t<=1, 1/10<=v<=13/40, P in P7.

For each of the six 30-column forcing functionals y_f, indexed f=00,33,43,45,65,66, and seventh separator ell, let r_f(p)=(y_f^T q(p))/eta_f where eta_f=||T^T y_f||_1>0, and put R7(p)=min_f r_f(p). Positivity of all seven perturbed evaluations when ||delta||_infinity<R7(p) guarantees at least seven strictly positive arcs in any nonnegative 30-arc coupling (if one exists). At P7 itself a positive seven-arc coupling is explicitly given.

## New theorem: full physically lawful bridge-family optimization

The largest radius certified by these *seven fixed functionals*, allowing the P7 starting point, endpoint v, and bridge parameter t all to vary, equals exactly

R_star = 2335581000/194864094623 = 0.01198569189731236... .

One optimizer has t=0 and P_star=lambda_1 V1+lambda_3 V3, with

lambda_1 = 12297672472745316495884170635/221733247658614103185557105322,
lambda_3 = 209435575185868786689672934687/221733247658614103185557105322.

Its seven positive arcs are exactly E7={(0,0),(3,3),(4,3),(4,5),(6,5),(6,6),(0,3)}. At P_star the two binding radii are r43=r66=R_star; all other five are strictly larger. The original 21 transport equations, five physical equalities and all 26 nonnegative capacities pass exactly. The seven positive arc masses, in E7 order, are:

(500794529581/2338369135476,
641340896503/2338369135476,
47632820535/389728189246,
38106256428/194864094623,
47632820535/389728189246,
87976751611/2338369135476,
26462678075/779456378492).

The center is physically legal and has N_min=7 by the inherited six forcing duals and the seventh separator.

## Complete exact upper-bound certificate (global, not numerical LP conjecture)

The bridge family lies inside the convex hull of the seven explicit lawful samples V0,...,V4,W0,W1. In fact its convex decomposition has total V-vertex weight 1-t and terminal weight t. Every r_f is affine in this decomposition because q is affine and eta_f is fixed.

Define alpha=171472243623/194864094623, so 0<alpha<1, and U(p)=alpha*r43(p)+(1-alpha)*r66(p). For every p, R7(p)<=U(p). The executed exact verifier evaluates U at all seven samples and verifies U(V1)=U(V3)=U(W1)=R_star while the positive gaps R_star-U(sample) at the remaining samples are:

V0: 16611051322475475000/6222802389683251360439;
V2: 11583161354989089665625000/13645692406573825632930684503;
V4: 76581048761739845625/39161100507573401829901;
W0: 693450000/194864094623.

Thus U(p)<=R_star for every permitted p. This exact convex upper certificate proves R7(p)<=R_star without relying on the floating-point LP candidate search. The explicit P_star has the two binding evaluations equal R_star and the five other normalized evaluations larger, proving equality and global optimality.

The *entire maximizing set* is a closed one-dimensional line segment of lawful seven-arc physical policies. Its first endpoint is P_star above; its second endpoint is

P_end=(1-t_max)V3+t_max W1,

t_max=1944148810350222725565/56507105428884278215883
(approximately 0.03440538664287072).

At P_end the seven evaluations have exactly the same nonnegative gaps above R_star as at P_star. At all points of their connecting segment the two active functionals remain equal and the other five remain above R_star by affinity. Conversely, strict positivity of the upper-bound gaps outside samples {V1,V3,W1} forces every optimizer to use only these samples; R7=U further forces r43=r66, selecting precisely this segment. The endpoint keeps 1-t_max>0, so its full seven-arc Blackwell transfer is strictly positive.

## Mathematical interpretation and comparison

PR #1998 optimized a radius *uniform over all P in P7*, obtaining 0.004578255605657387... . The present R_star is approximately 2.6179604045 times that number, but changes the quantifier: it optimizes the best chosen physical center P in P7 instead of guaranteeing the same radius for every P. It does not enlarge PR #1998's uniform-over-P7 tube and does not claim that R_star is the true distance to the nearest six-arc physically admissible coupling.

The rational LP reconstruction was a candidate-discovery aid. The final optimum is certified by exact upper/lower rational identities, 30-column forcing-dual checks and explicit 21-row/primal physical verification. The supporting full calculation uses Python Fraction/SymPy; see VERIFY_FULL_P7.py and EXACT_OUTPUT.txt.

## Next discriminating question

Optimize over *new adaptive* forcing/separation functionals rather than only these seven fixed certificates. Determine the true nearest legal <=6-arc contact in the frozen eight-dimensional physical family, and compare it with the pointwise R_star. Review whether the optimal segment meets a physical capacity facet before a low-support contact. No native X6/physical-world promotion or formal mathematical admission is claimed.

## Control provenance

No current immutable R5 formal publication is asserted. Research is author-side, without claiming other task ownership. A native session may register activity independently; actual receipts are reported separately. Original frozen scientific pins remain intact.
