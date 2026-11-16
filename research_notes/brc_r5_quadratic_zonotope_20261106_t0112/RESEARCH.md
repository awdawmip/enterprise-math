# R5: exact six-variable quadratic / seven-ratio zonotope criterion for actual image membership

Date: 2026-11-06 (Asia/Shanghai). Author status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is an auxiliary finite BRC observer experiment under unchanged P000 / ACTIVE Heartbeat World; no native X6 dynamics claim.

## Mother objective and source
R5 asks for a finite strictly-positive P/Q stopping tree whose full-history (FULL_HIST) and seedless time/likelihood-ratio (LR) strategies share the entire four-observer convex hull but have distinct actual real-behavior observation sets. Scientific pins remain GLOBAL a01383f825ef9d43b4b754254303298c64041568 and EM 86149263e38c22292c9def1e0f69092efa1be77e.

Direct predecessor: PR #1767, research_notes/brc_r5_kernel_perturbation_phase_diagram_20261106_t0047/RESEARCH_HULL.md and VERIFY_HULL.py at fed51a882c12831a889cd5437da5d1dc564fd673. Its author-side exact certificate reports at delta=1/4 full four-dimensional hull equality, based on 80 integer halfspaces, 82 exact vertices, 806 distinct deterministic LR observations and exact FULL Bellman bounds. We READ but did not independently rerun that full hull certificate this turn. Our theorem tackles the remaining *actual real image* test.

Model: root time-1 LR=1; t2 ratios r2=(3/4,5/4), q2=(1/2,1/2); t3 ratios r3=(1/2,1,3/2), q3[0]=(13/20,1/5,3/20), q3[1]=(1/40,9/20,21/40); t4 ratios r4=(1/10,1,19/10). Conditional Q terminal rows indexed (i,j): q4[i,0]=(509,382,9)/900; q4[i,2]=(9,382,509)/900; q4[0,1]=(47/180,43/90,47/180); q4[1,1]=(67/162,14/81,67/162). Every row is strictly positive, normalized and has child-ratio mean equal to parent. P probability on each history path is its Q probability times the current LR. All stop nodes may declare P or Q, and both observers may use arbitrary real behavioral randomization. W=(P[declare Q],Q[declare P],E_P tau,E_Q tau).

## Theorem A: full-history actual observation image is a polytope

For any finite acyclic P/Q stopping tree in which FULL observes each distinct history, its *actual* real behavioral observation image is a compact convex polytope and equals its deterministic policy hull.

Proof. At history h define Q arriving mass m_h and Q action mass f_(h,a)>=0 for each legal action a. The constraints sum_a f_(h,a)=m_h, root mass=1, and m_child=q(child|h)*f_(h,continue) are finite linear equalities and inequalities and define a bounded polytope. Every feasible flow has a behavioral realization by action probabilities f_(h,a)/m_h for m_h>0 (arbitrary legal choices at zero mass). All error and time coordinates are linear in these stopped Q masses: Q-error is mass declaring P, P-error is LR(h) times mass declaring Q, and durations are weighted by time or LR(h)*time. Therefore W is a linear polytope image, hence convex/compact. For every linear support direction an optimal behavioral policy may also be chosen deterministic, by sequential vertex optimization of the local action simplexes on an acyclic tree; consequently the polytope equals the deterministic observation convex hull. QED.

Thus, conditional on the preceding certified hull identity H=conv O_LR=conv O_FULL, one has O_FULL=H exactly; R5 for this fixed model reduces to finding a point in H outside O_LR.

## Theorem B: exact six-variable quadratic semialgebraic criterion for O_LR

Take real unknowns g,u0,u1,z0,z1,z2 satisfying 0<=u_i<=g<=1 and 0<=z_j<=1. Here g is root continuation probability, u_i=g*a_i is Q-unweighted product of root and time2-i continuation probabilities, and z_j is shared continuation at time3 ratio r3[j]. Set V_j=sum_i q2[i]*q3[i,j]*u_i.

The two required stopping time coordinates are EXACTLY:
 T_P=1+g+sum_i q2[i]*r2[i]*u_i+sum_j r3[j]*V_j*z_j;
 T_Q=1+g+sum_i q2[i]*u_i+sum_j V_j*z_j.

Define the nine Q stop-key masses s_K by:
 time1, ratio1: s=1-g;
 time2,i: s=q2[i]*(g-u_i);
 time3,j: s=V_j*(1-z_j);
 time4,k: s=sum_(i,j) q2[i]*q3[i,j]*u_i*z_j*q4[i,j,k].
These masses are nonnegative and obey sum_K s_K=sum_K ratio(K)*s_K=1. Aggregate by ratio (not by time): R={1/10,1/2,3/4,1,5/4,3/2,19/10}, M_r=sum_(K:ratio(K)=r) s_K. Each M_r is a quadratic polynomial in the six unknowns.

For each rho in R define
 L_rho=1+sum_(r>rho)(rho-r)*M_r,
 U_rho=1+sum_(r<rho)(rho-r)*M_r.

**Exact iff (all real behavior policies):** W=(e_P,e_Q,T_P,T_Q) belongs to the actual seedless LR image if and only if there exist the above six unknowns obeying their linear bounds, the two displayed time equalities, and exactly the fourteen two-sided scalar inequalities
  L_rho <= e_P+rho*e_Q <= U_rho, for every rho in R.
All coefficients are rational; there are six real quantified variables, two equations and fourteen inequalities of polynomial degree at most TWO (plus linear variable bounds). The assertion includes boundary cases g=0, g=1, u_i=0 and z_j in {0,1}.

Proof. Any LR strategy gives the stated survival/stop equations by elementary Q-flow conservation (and P mass=ratio*Q mass). If x_K is the conditional probability of declaring P at stopped key K, its errors are e_P=sum_K r_K*s_K*(1-x_K)=1-sum_K r_K*s_K*x_K, e_Q=sum_K s_K*x_K. Equal-ratio keys have parallel error increments; combine them with their Q-mass-weighted mean into x_r in [0,1]. Therefore for fixed continuation variables the entire error set is the planar translated zonotope
 Z(M)=(1,0)+sum_(r in R) M_r * [0,(-r,1)].
Each normal (1,rho) is perpendicular to its generator (-rho,1); its minimum and maximum support values are L_rho and U_rho. Necessity follows.

For sufficiency, a 2D finite zonotope has all polygon edges parallel to its nonzero generating segments, hence its intersection-of-supporting-halfspaces description consists precisely of the two normals perpendicular to each distinct generator slope. The global R contains seven distinct slopes; including inactive generators merely adds redundant inequalities. Degenerate one-dimensional segments and the point case also satisfy the stated iff: the normal matching the active slope fixes the supporting line, while a second distinct slope bounds both segment endpoints; for the point case both distinct normals fix the unique point. Hence the 14 inequalities imply the existence of x_r in [0,1] giving the prescribed pair of errors. For each key set x_K=x_r; these are valid independent behavioral declarations. When g>0 choose a_i=u_i/g; when g=0 all u_i=0 and a_i may be arbitrary. Together with z_j these choices realize the time pair and both errors exactly. QED.

## Scientific gain and verification
The time/ratio observer had 6 continuation variables plus 9 independent conditional P/Q declaration variables, i.e. 15 real degrees before eliminating choices. Theorem B eliminates all 9 label probabilities; real image membership is an existential rational QUADRATIC test with only 6 unknowns and 14 explicit planar inequalities. This retains the history-dependent q4[i,1] kernels instead of silently substituting a history-lumpable approximation. A certified real-algebraic UNSAT for a rational point W in H would finish the image-difference half of the mother construction, subject to independent review; an exact universal synthesis for all W in H would prove image equality for this model and redirect parameter selection.

The attached Python stdlib Fraction checker verifies row normalization and likelihood-ratio moments; 180 exact random/boundary continuation-plus-declaration strategies and 1080 exact rational test points are compared against both the 14 inequalities and a separately enumerated 2^7-endpoint zonotope polygon. It passed. These finite checks do not replace the above all-real analytical proof.

REUSE_APPLIED: typed BRC Q/P positive branch mass and LR observer; previous author-side delta=1/4 hull certificate (not rerun); classical occupancy-flow linearity and planar zonotope edge-support geometry, with full derivation here. No formal Source claim, RR, Driver review or Foundation adoption is represented.
