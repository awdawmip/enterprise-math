# R5 — Exact affine-curvature dual and ternary signed Bellman chambers

Date: 2026-10-27. Status: **PORTABLE AUTHOR / UNREVIEWED / NOT_ADMITTED**. This is an external finite two-measure observation-tree result, not P000 native dynamics, a native CLAIM/Result, or a Driver mathematical admission.

## Frozen sources and typed scope

GLOBAL_KNOWLEDGE_V1 fixed read: main@64ee78649f92fdc0f078d98b112d401c4d4d61d2, including bootstrap, manual, ACTIVE worldview and task-research route. Project scientific read: main@94a39c5c31e0be9a2a8550e680586994c9d6a123, including P000, mandatory X6/time and joint-observer retention, portable/autonomous research rules. Direct predecessor: research_notes/brc_lr_adjoint_curvature_20261027_r5/PROOF.md and NEXT_TASK.md; the latter explicitly requests the exact rational affine-curvature LP dual and signed objective chambers.

BRC reuse is **REUSE_APPLIED**: positive exact Q path masses, P/Q likelihood ratios, historical branch labels and conditional next-likelihood-ratio kernels. The information-reducing observer maps (time, history, LR) to (time, LR), with finite future stop/continue/declare operations; only a proof of future-safe equality permits dropping history. For X6 typing, each auxiliary packet may be carried at one chosen native X6 Cell c with separate typed time t and nonspatial history register h. This auxiliary embedding does not assert that a native Heartbeat evolution generates these stochastic transition kernels.

## Definitions and Theorem 1: full finite affine-curvature primal-dual certificate

Let distinct real successors y_1<...<y_m and real continuation values f_i be given. Set

rho_Y(f) = inf_{A,B real} [max_i(f_i-A-B*y_i) - min_i(f_i-A-B*y_i)].

The intercept A cancels. For a triple i<j<k, let

C_ijk(f) = f_j - ((y_k-y_j)*f_i + (y_j-y_i)*f_k)/(y_k-y_i).

**Exact theorem (all real f and arbitrary finite m):**

rho_Y(f) = max_{i<j<k} |C_ijk(f)|  for m>=3;  rho_Y(f)=0 for m<=2.   (1)

The primal finite LP minimizes M-m0 subject to
m0 <= f_i-B*y_i <= M for every i, over real B,m0,M.
Its dual is

maximize sum_i (alpha_i-beta_i)*f_i
subject to alpha_i,beta_i>=0;
sum alpha_i=sum beta_i=1;
sum y_i*alpha_i=sum y_i*beta_i.                                  (2)

**Proof.** Use alpha_i>=0 on f_i-B*y_i-M<=0 and beta_i>=0 on m0-f_i+B*y_i<=0. Taking the Lagrangian infimum in unrestricted B,M,m0 yields exactly the three equalities and the objective (2). The primal is feasible and bounded below by zero; ordinary finite LP strong duality applies. The dual has three independent equalities (for >=2 distinct y values), so an optimal basic feasible solution has at most three positive variables. A nonzero optimum therefore has one probability vector concentrated at an intermediate y_j and the other on two bracketing y_i<y_j<y_k. The two weights are (y_k-y_j)/(y_k-y_i) and (y_j-y_i)/(y_k-y_i), making the dual objective C_ijk or -C_ijk. Conversely each triple and its reverse are feasible dual certificates. A one- or two-point f is affine, giving rho=0. QED.

For any probability kernels K,L having the same y-mean, delta=K-L annihilates both 1 and y. Subtract an arbitrary A+B*y from f, and use |delta dot g| <= TV(K,L)*osc(g) to deduce

|sum_i (K_i-L_i)*f_i| <= TV(K,L)*rho_Y(f).                       (3)

The triple dual witnesses yield disjoint-support K,L with common mean y_j, TV=1 and difference |C_ijk|; (3) is sharp as a uniform coefficient over all mean-matched kernels. On rational Y and rational f, enumerating O(m^3) triples yields an exact rational dual witness. A rational primal witness comes from a minimizing slope B chosen among the O(m^2) pairwise crossing slopes (f_i-f_j)/(y_i-y_j): osc(f-B*y) is convex piecewise linear, with its minimum at a breakpoint unless identically zero. This is an exact finite primal-dual algorithm, not a numerical LP approximation.

For fixed rational seedless LR policy q on a rational tree, continuation values V^{q,lambda}(y_i) are rational-linear in any real signed lambda=(a,b,u,v). Formula (1) is a finite maximum of absolute rational-linear functionals: a positively homogeneous rational polyhedral curvature fan. Zero curvature means all its triple functionals vanish. When q itself is Bellman-selected as a function of lambda, separate its optimality chambers first; global convexity is asserted only for fixed q.

## Theorem 2: universal equality for three support values

For y1<y2<y3 and any K,L with the same mean, delta=K-L is necessarily

delta=t*((y3-y2)/(y3-y1), -1, (y2-y1)/(y3-y1)),  TV(delta)=|t|.

Therefore for **every real f**,

|delta dot f| = TV(K,L)*|f2-((y3-y2)*f1+(y2-y1)*f3)/(y3-y1)|
              = TV(K,L)*rho_Y(f).                              (4)

This is an identity, not merely a bound. The predecessor's strictly positive pair at Y=(1/2,1,3/2),
K_a=(1/4,1/2,1/4), K_b=(1/8,3/4,1/8), TV=1/4,
therefore saturates (3) **for every continuation value**, including signed directions, rather than just its earlier single positive objective.

## Theorem 3: sharp fixed-current-ratio ternary reachability cap

Fix r in [y1,y3], and let E_r be all probability kernels with expected y equal to r. Define

gamma_Y(r) = (r-y1)/(y2-y1) if y1<=r<=y2;
             (y3-r)/(y3-y2) if y2<=r<=y3.

Then

sup_{K,L in E_r} TV(K,L)=gamma_Y(r),
sup_{K,L in E_r} |(K-L) dot f|=gamma_Y(r)*rho_Y(f).               (5)

**Proof.** E_r is a line segment. If r<=y2 its endpoints are the two-point laws on {y1,y2} and {y1,y3}; their TV is (r-y1)/(y2-y1). If r>=y2 its endpoints lie on {y2,y3} and {y1,y3}, with TV (y3-r)/(y3-y2). Every difference of points on the segment is a multiple of the endpoint difference. Theorem 2 then gives the exact value width. QED.

This is a sharpened **local BRC prediction diameter budget**: at a collision ratio r different from the middle successor, no two hidden kernels supported on exactly those three successors can be TV distance 1. For strict positivity and r strictly interior, mix each extremal kernel with the same strictly positive mean-r kernel and let the mixing weight tend to zero.

**Exact witness:** Y=(1/2,1,3/2), r=3/4; endpoints K=(1/2,1/2,0), L=(3/4,0,1/4), gamma=TV=1/2. For f=min(y,1), rho=1/4 and |(K-L) dot f|=1/8. A strictly positive shared mean-r kernel (3/5,3/10,1/10) permits positive perturbed kernels whose differences satisfy (4) exactly.

## Theorem 4: all real signed terminal Bellman chambers on predecessor Y

At the compulsory terminal declaration, Q-value for signed four-observable coefficients lambda=(a,b,u,v) is

f_lambda(y) = min(a*y,b) + T*(u*y+v),

because declaring Q costs a*y, declaring P costs b, and the terminal time contribution is affine. The affine term is invisible to rho. For Y=(1/2,1,3/2), put lo=min(a/2,3*a/2), hi=max(a/2,3*a/2). The **complete signed coefficient answer** is

rho(f_lambda) = (1/2)*min(b-lo,hi-b)  if lo<=b<=hi;
                0                     otherwise.              (6)

Proof: min(a*y,b) is concave as a function of y even when a,b are negative; the single triple formula gives rho = min(a,b) - [min(a/2,b)+min(3*a/2,b)]/2 >=0. Evaluate the three minima across b=a/2,a,3*a/2. This gives (6), with two active linear chambers per sign of a, and zero curvature outside the tent. It peaks at |a|/4 on b=a. At all u,v the same result holds. For the old K_a,K_b,

(K_a-K_b) dot f_lambda = -(1/4)*rho(f_lambda)                    (7)

for all signed lambda, since their difference is (1/8,-1/4,1/8). This is a uniform *kernel continuation-value* identity, not a claim that a single frozen terminal decision table is Bellman-optimal for every signed lambda.

## Independent 4-support exact certificate and 8 strictly positive leaves

Take Y=(1/2,3/4,5/4,3/2) and f=min(y,1)=(1/2,3/4,1,1).
Primal B=1/2 gives residuals (1/4,3/8,3/8,1/4), range 1/8.
Dual alpha=(0,1/2,1/2,0), beta=(1/2,0,0,1/2) are equal-mean-1 probabilities with objective 1/8. Hence rho=1/8 exactly, with explicit matching primal and dual certificates.

Mix each of these extremal laws with common U=(1/4,1/4,1/4,1/4) by epsilon=1/8:

K_plus=(1/32,15/32,15/32,1/32),
K_minus=(15/32,1/32,1/32,15/32).

Both are strictly positive probability kernels with mean LR=1, and

TV(K_plus,K_minus)=7/8;
K_plus dot f=111/128; K_minus dot f=97/128;
difference=7/64=(7/8)*(1/8)=TV*rho.                         (8)

A complete positive P/Q observation tree has first hidden history h=+/- with P(h)=Q(h)=1/2, then four terminal outcomes labeled y. Set Q(h,y)=K_h(y)/2 and P(h,y)=y*K_h(y)/2. All eight leaves are strictly positive; sums P=Q=1 and P/Q terminal ratios are exactly Y. Equation (8) compares conditional terminal Bayes risks of two hidden histories; it is **not** evidence of a full-vs-LR support-function gap or attainable-set nonconvexity.

## Validation, prior art, and next target

The adjacent VERIFY.py was executed using Python fractions.Fraction. It checks 2401 exactly rational signed four-coefficient choices for the 3-point formula and predecessor kernels; the fixed-mean triangular witness and positivity; the complete four-point primal/dual and eight-leaf P/Q certificate; and 1344 independent rational primal-versus-triple-dual cases on three/four/five support values. Adjacent EXACT_OUTPUT.txt contains literal stdout ending ALL EXACT CHECKS PASSED. The arbitrary-real/unbounded-coefficient claims rely on the displayed finite LP/algebra proofs, **not** finite grids; no Lean or independent review is claimed.

Moment-constrained extreme points are prior mathematics, not asserted as original here: Winkler (1988), Extreme Points of Moment Sets, Math. Operations Research 13, 581–587, DOI 10.1287/moor.13.4.581; Pinelis (2016), On the extreme points of moments sets, Math. Methods Oper. Res. 83, 325–349, DOI 10.1007/s00186-015-0530-0. Also note the 2026-06-19 *preprint* by Henrion, Kružík and Weis, Extreme points and faces in the moment problem, arXiv:2606.21391; only its public abstract was checked, not its full proof or peer review. This work's application increment is an exact BRC observer-aware rational curvature oracle, all-signed terminal chambers and fixed-r cap tied to the existing adjoint identity.

The stronger parent question stays open: find/exclude strictly positive rational N=3 model with conv(O_LR)=O_full while O_LR differs from O_full under all real seedless LR strategy probabilities. Next use exact rational convex-hull separation/membership and real-algebraic nonattainability only after all linear support directions pass the exact finite gate.