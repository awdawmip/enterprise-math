# R5: all-real full-rank curvature-cone obstruction in a genuine STOP tree

**Date:** 2026-10-31 Asia/Shanghai. **State:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Frozen inputs, predecessor, and authority

This work froze GLOBAL_KNOWLEDGE_V1 canonical main at 38ba47112bf1e35407c2bdfc3e5fb418c5d1e298 and Enterprise Math canonical main at d539220a4fc13a38f2e42531a3d4b2aa61816564. Applicable account-level bootstrap/manual, Enterprise Math project router, locked P000 original and ACTIVE worldview were read with the current portable research protocol. The latest R5 parent is the late-affine time-error dichotomy at scientific commit 97e41a43b9d25c05b2a4acc48368492e89e3a2f2, tracked by Draft PR #1663 and activity commit 8e727b18b9430e4059c588d23c1bc3c121253e81.

Current native research status returned research_authority_granted=false and executor_binding_configured=false; the bounded active-owner query returned CONTROL_QUOTA. This portable author proof does not claim a Source CLAIM, canonical Result, independently reviewed theorem, accepted Foundation result, X6 embedding or external physical prediction. P000 and ACTIVE worldview are unchanged.

## Exact finite model and observer

Nature chooses origin X in {0,1}, middle state U in {0,1} and final state V in {0,1,2} with strictly positive joint Q(X,U):

$$
Q(0,0)=Q(1,1)=49/100,\quad Q(0,1)=Q(1,0)=1/100.
$$

The time-3 P/Q likelihood ratios are r_0=3/4 and r_1=5/4. The time-4 ratios are R=(1/2,1,3/2). For t_0=1/16, t_1=1/8, the Q conditional V kernel is

$$
K_{x,0}=(1/2+t_x,\ 1/2-2t_x,\ t_x),\quad
K_{x,1}=(t_x,\ 1/2-2t_x,\ 1/2+t_x).
$$

Define q_xuv = Q(x,u)K_xu(v) and p_xuv=R_v q_xuv. The twelve complete paths all have p,q>0, and the measures normalize to one. At times 2,3,4 a STOP is real and immediately absorbing, and CONTINUE at time 4 forces terminal STOP at 5. FULL sees all prior history; LR observes only (time, current likelihood ratio), and has independent real behavioral decisions with **no persistent random seed**. No key is revisited along a trajectory.

At STOP time j, let epsilon_j in (0,1) be a common P/Q terminal error probability depending only on j. Put

$$
B=\epsilon_4-\epsilon_3,\quad A=4\epsilon_3-3\epsilon_4,\quad
c=\epsilon_2-2\epsilon_3+\epsilon_4,\quad
d=\epsilon_5-2\epsilon_4+\epsilon_3.
$$

The exact four-time identity is

$$
\epsilon_j=A+Bj+c\,1_{j=2}+d\,1_{j=5},\qquad j=2,3,4,5.
$$

Writing S_{2,M}=M(tau=2), S_{5,M}=M(tau=5) and T_M=E_M[tau], the four-observer vector O=(e_P,e_Q,T_P,T_Q) obeys for M=P,Q

$$
e_M=A+B T_M+c S_{2,M}+d S_{5,M}.
$$

These are observation readouts, not a lossless replacement for source-labelled branch states.

## Theorem: exact all-real separation throughout a full-rank cone

**Theorem.** In this fixed strictly-positive genuine STOP model, for every legal real epsilon tuple with d nonzero and r:=c/d >= -4/357, both observer convex hulls have affine dimension four, and

$$
\operatorname{conv}(\mathcal O_{\rm FULL})\ne
\operatorname{conv}(\mathcal O_{\rm LR}).
$$

Indeed define the following affine functional of the **four observable coordinates**:

$$
H=3T_P-\frac{147}{64}T_Q
  -\frac{2}{d}(e_P-A-BT_P)
  +\frac{83}{64d}(e_Q-A-BT_Q).
$$

For all such real epsilon and **all real behavioral** FULL and LR strategies, its exact support maxima are

$$
\boxed{
\sup_{\rm FULL}H=\frac{19149}{6400},\qquad
\sup_{\rm LR}H=\frac{4787}{1600},\qquad
\Delta_H=\frac{1}{6400}>0.
}
$$

The support gap is constant on the whole cone, although the observer coefficients depend on the terminal-error parameters.

### Proof: complete Bellman reduction

Using e_M-A-BT_M=cS_{2,M}+dS_{5,M}, rewrite

$$
H=3T_P-\frac{147}{64}T_Q
 -2(r S_{2,P}+S_{5,P})+\frac{83}{64}(r S_{2,Q}+S_{5,Q}).
$$

At time 4 on a path with final likelihood ratio R_v, CONTINUE rather than STOP changes H per unit Q mass by

$$
F_v=3R_v-\frac{147}{64}-2R_v+\frac{83}{64}=R_v-1.
$$

Therefore the optimal time-4 continuation increment is L_v=[F_v]_+ = (0,0,1/2); V=1 is a tie. Because F_v only depends on the LR-visible V key, this action can be chosen by both FULL and LR simultaneously.

At time 3 with state (x,u), the CONTINUE advantage over STOP is

$$
G_{x,u}=3r_u-\frac{147}{64}+\sum_v K_{x,u}(v)L_v.
$$

Direct exact substitution gives

$$
G_{0,0}=-1/64,\quad G_{1,0}=1/64,\quad
G_{0,1}=111/64,\quad G_{1,1}=113/64.
$$

Thus both strategy classes can take CONTINUE at U=1 wherever reached. At U=0, FULL can choose separately for each X but LR has only one shared bit h in {0,1}.

The time-2 likelihood ratios are 19/25 for X=0 and 31/25 for X=1. The Q-conditional U=1 probabilities are 1/50 and 49/50 respectively. Let D_x(h) be the time-2 gain of CONTINUE, after choosing U=1 CONTINUE, U=0 action h, and optimal time-4 control. Accounting for the early stopping-error contrast r gives the exact formulas

$$
D_0(0)=\frac{57+714r}{3200},\quad
D_0(1)=\frac{8+714r}{3200},
$$

$$
D_1(0)=\frac{10091+3786r}{3200},\quad
D_1(1)=\frac{10092+3786r}{3200}.
$$

Each is nonnegative for every real r>=-4/357, with only D_0(1) potentially zero at the endpoint. The same positivity bounds cover FULL's independent U=0 bits because the formulas are source-local. Hence both classes can optimize while continuing at time 2 at both origins; no early-STOP clipping hides the source collision.

With time-2 CONTINUE established, at U=0 the source-specific weighted gains are

$$
Q(0,0)G_{0,0}=-49/6400,\qquad
Q(1,0)G_{1,0}=1/6400.
$$

FULL stops at (0,0) and continues at (1,0). LR must share h, and because the total weighted gain is -48/6400, LR chooses h=0. The strict FULL advantage is exactly +1/6400.

The unconditional U=1 gain is

$$
Q(0,1)G_{0,1}+Q(1,1)G_{1,1}
  =(111+49\cdot113)/6400=353/400.
$$

The time-2 STOP baseline is 45(2-r)/64, while the aggregate time-2 continuation gain includes +45r/64, canceling r. Therefore

$$
\sup_{\rm LR}H=3(3-147/64)+353/400=4787/1600;
$$

FULL adds 1/6400. Every finite behavioral expectation is multiaffine in the independent control probabilities, because no decision key repeats along a path. Sequential maximization of a multiaffine function reaches its maximum on Boolean controls, so these Bellman bounds cover **all real behavioral policies**, not only the exact rational samples. The gap proves strict non-equality of the convex hulls.

### Uniform four-dimensional affine rank

Take five valid seedless LR deterministic policies with binary indices (3,7,11,23,39), precisely decoded in VERIFY.py. Each continues at time 2, so both S_{2,P} and S_{2,Q} are zero. Their four difference rows in coordinates (S_{5,P},S_{5,Q},T_P,T_Q) have exact determinant

$$
\det=67199/20480000\ne0.
$$

Since the e_P and e_Q observer coordinates restricted to these five policies are A+B T_M+d S_{5,M}, their determinant in (e_P,e_Q,T_P,T_Q) is

$$
\boxed{\det_{\rm LR}=\frac{67199}{20480000}\,d^2\ne0}.
$$

Thus the LR observer hull and its containing FULL observer hull both have full affine dimension four, uniformly for every nonzero d and any c,B.

### Strictly interior rational witness and distance

Choose epsilon=(5/8,1/2,1/2,5/8), so A=1/2, B=0 and c=d=1/8, r=1. A genuine FULL deterministic policy indexed 149563 has the exact observable point

$$
\mathcal O^*=
(14303/25600,\ 6901/12800,\ 13127/3200,\ 6117/1600).
$$

It saturates sup_FULL H. At these parameters the covector of H in the four observable coordinates has L1 norm 2027/64. Thus for **every real LR behavioral observer**

$$
\boxed{\|\mathcal O^*-\mathcal O_{\rm LR}\|_\infty
       \ge \frac{1/6400}{2027/64}=\frac{1}{202700}>0.}
$$

For any fixed legal parameters within the theorem, a corresponding bound is the support gap divided by

$$
|3+2B/d|+|147/64+83B/(64d)|+211/(64|d|).
$$

The bound is a certified lower bound, not the asserted exact metric distance.

## Consequences and precise unclassified region

The predecessor author-side result already proves for d=0: c=0 gives observer rank at most two; c!=0 gives a strict convex-hull support gap. Combining these separately proved results, **the necessary condition for any full-rank, equal-four-hull counterexample in this fixed carrier and common time-only error family** is now

$$
\boxed{d\ne0,\qquad c/d<-4/357.}
$$

This is an exclusion theorem, not a construction in the remaining opposite-sign wedge. The original more general full-rank equal-hull / unequal-actual-real-image STOP mother question is still open.

## Computational evidence, BRC scope, and next unit

Executed the attached Python standard-library Fraction/integer verifier and saved actual EXACT_OUTPUT.txt. It enumerates all 262144 FULL and 128 LR deterministic policies, checks 12 strictly positive normalized P/Q paths, the exact determinant, and exact extrema for seven rational ratios (-4/357,-1/100,0,1/3,1,3,100). End marker: PASS_EXACT_R5_STOP_TIME_CURVATURE_CONE_NO_GO. Exhaustive rational instances validate the formulas on those inputs; **the analytic Bellman argument, not a seven-point sweep, proves the all-real parameter theorem**.

BRC reuse is source-labelled positive branch masses and future-operation-sensitive likelihood-ratio quotient residual. No native Heartbeat X6/three-dimensional-slice operation or BRC–Shor numerical route was executed or asserted; this is external auxiliary finite-probability algebra. No sensitive data, permissions, native owner, P000 or worldview were changed.

**Next:** Analyze real ratios c/d<-4/357 with exact signed Bellman normal-fan inequalities or rational primal/Farkas convex-hull certificates. Do not test actual observer-image nonmembership until full-rank equality of all signed four-observer supports is proved. Continue to separate author evidence from independent Source admission.
