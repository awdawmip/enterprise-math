# R5: complete all-real NO-GO for time-only error kernels on the fixed 12-path STOP tree

Date 2026-10-31 Asia/Shanghai. **AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING**.

## Frozen sources and actual authority

GLOBAL_KNOWLEDGE_V1 canonical main 684bdef29322145083500887d4f563f89cf396e0; Enterprise Math canonical main 06257b8f444eed359c77e93bd8acf9c75a1f08c2. Read applicable bootstrap/manual, Enterprise Math project router, original P000, ACTIVE worldview, BRC research preference, mathematical research policy, and portable research protocol. Scientific predecessor: immutable commit 75da5f33122219704925721fe8eaba67504b7ebf, research_notes/brc_r5_time_error_curvature_cone_20261031_t0240/RESEARCH.md. The predecessor excluded c/d >= -4/357 for d!=0. This new proof covers the entire real c/d axis and the remaining d=0 cases.

The native session_start was explicitly denied STATIC_READONLY_SCOPE_DENIED (operation_sent=false). Active owner query returned CONTROL_QUOTA. No Source owner, CLAIM, Result, independent Driver review, or mathematical admission is claimed. GitHub branch publication is author-side evidence only. P000, including six native spatial axes + one time dimension and the 120-degree enterprise orthogonality, and the protected worldview are untouched. This is auxiliary finite two-measure probability theory, not native X6 physics.

## Model, observer and theorem

Let X,U in {0,1} and V in {0,1,2}. Q(X=0,U=0)=Q(X=1,U=1)=49/100 and Q(0,1)=Q(1,0)=1/100. Let t_0=1/16, t_1=1/8, and define the conditional Q kernel

\[
K_{x,0}=(1/2+t_x,\ 1/2-2t_x,\ t_x),\quad
K_{x,1}=(t_x,\ 1/2-2t_x,\ 1/2+t_x).
\]

For terminal likelihood ratios R=(1/2,1,3/2), the 12 complete-path masses are
\(q_{xuv}=Q(x,u)K_{x,u}(v)\) and \(p_{xuv}=R_v q_{xuv}\). Every p and q is strictly positive, and each law sums to 1. The LR key at time 2 is r_X=(19/25,31/25), at time 3 is r_U=(3/4,5/4), at time 4 is R_V. At stages 2, 3, 4, STOP is genuinely absorbing; CONTINUE from time 4 terminates at stage 5. FULL observes history, LR observes only (time, likelihood ratio). LR behavioral randomizations at distinct keys are independent and have **no persistent random seed**. No decision key repeats on a trajectory.

Choose arbitrary legal real epsilon_2,epsilon_3,epsilon_4,epsilon_5 in (0,1), common to P and Q and dependent only on terminal stopping time tau. Define
\(T_M=E_M[\tau]\), \(S_{j,M}=M(\tau=j)\), \(e_M=E_M[\epsilon_\tau]\), \(O=(e_P,e_Q,T_P,T_Q)\), for M=P,Q.

Set
\[
A=4\epsilon_3-3\epsilon_4,\quad B=\epsilon_4-\epsilon_3,\quad
c=\epsilon_2-2\epsilon_3+\epsilon_4,\quad
d=\epsilon_5-2\epsilon_4+\epsilon_3.
\]
The four-time identity yields
\[
 e_M=A+B T_M+c S_{2,M}+d S_{5,M}. \tag{1}
\]

**Complete theorem.** On this fixed model, if \((c,d)\neq(0,0)\), then
\[
 \operatorname{conv}\mathcal O_{\rm LR}
 \subsetneq\operatorname{conv}\mathcal O_{\rm FULL}.
\]
If c=d=0 then both observable images lie in an affine plane of dimension at most two. When d!=0 both observable convex hulls have affine dimension exactly four, but are strictly unequal. Thus **no legal time-only common error kernel** solves the original mother target of equal full-four-dimensional hulls but unequal actual real observer sets. This conclusion is about this carrier and kernel class, not arbitrary STOP trees or source-dependent errors.

## Exact signed supports: d != 0, ALL real c/d

Write r=c/d and define \(W_M=(e_M-A-BT_M)/d=rS_{2,M}+S_{5,M}\). This is an invertible affine coordinate change when d!=0. Put s=-7/200, and for a in {100,-100} define
\[
 b=s-3a/4,\quad k=1-a,\quad \ell=-1-b,\quad
 H_a=aT_P+bT_Q+kW_P+\ell W_Q. \tag{2}
\]
Thus H_a is a valid affine functional in the **original four observables**. For either a, the time-4 advantage per unit Q mass of CONTINUE rather than STOP is
\[
(a+k)R_v+(b+\ell)=R_v-1.
\]
Its optimal positive part is \(L=(0,0,1/2)\).

The time-3 continuation advantage at history (x,u) per unit Q mass, after optimizing time 4, is
\[
 G_{x,u}=a r_u+b+\sum_v K_{x,u}(v)L_v.
\]
Direct rational substitution gives
\[
 G_{0,0}=-3/800,\qquad G_{1,0}=11/400.
\]
For a=100, \((G_{0,1},G_{1,1})=(40197/800,20111/400)\), both positive. For a=-100, they equal \((-39803/800,-19889/400)\), both negative. Hence both FULL and LR optimally CONTINUE at u=1 if a=100 and STOP at u=1 if a=-100; only the u=0 bit conflicts between origins.

Check that a seedless LR strategy cannot avoid the conflict by early time-2 STOP. Relative to STOP at time 2, its conditional time-2 CONTINUE advantage for X=x, with u=0 STOP and the optimal u=1 bit, is
\[
 D_x=a r_x+b-r(k r_x+\ell)+
     \sum_u Q(u\mid x)\,h_u G_{x,u},
 \qquad h_0=0,\ h_1=\mathbf{1}_{a=100}. \tag{3}
\]
The exact expressions are
\[
\begin{array}{c|cc}
 &D_0&D_1\\\hline
a=100&(78797+48200r)/40000&(1964739+974500r)/20000\\
a=-100&-207/200-(159/200)r&-9807/200-(1971/40)r
\end{array}
\]
In the a=100 case, for ALL real \(r\ge-3/2\), the minima are \(6497/40000\) and \(502989/20000\). In the a=-100 case, for ALL real \(r\le-3/2\), the minima are \(63/400\) and \(9951/400\). These bounds also dominate the possible negative contribution from changing the shared u=0 bit, whose worst source-specific loss is \((49/50)(3/800)=147/40000\). Consequently BOTH time-2 origins optimally continue, for both choices of the shared u=0 LR bit, throughout the stated ratio half-lines. The u=1 bit already has an unambiguous sourcewise optimal sign and cannot improve by changing jointly with time 2.

With both origins continuing, FULL independently STOPs at (x,u)=(0,0) and CONTINUEs at (1,0). LR must use a common bit for u=0. Its net continuation gain is
\[
 (49/100)(-3/800)+(1/100)(11/400)=-1/640<0,
\]
so LR chooses STOP. FULL alone captures
\[
 (1/100)(11/400)=11/40000.
\]
Therefore the exact gap between support maxima is
\[
 \boxed{\sup_{\rm FULL}H_a-\sup_{\rm LR}H_a=11/40000>0}, \tag{4}
\]
using a=+100 on the entire half-line r>=-3/2 and a=-100 on the entire half-line r<=-3/2. Every real ratio is covered. The exact values are:
\[
\begin{array}{c|cc}
a & \sup_{\rm LR}H_a & \sup_{\rm FULL}H_a\\\hline
100 & 320107/3200 & 8002697/80000\\
-100&-15021/200&-3004189/40000.
\end{array}
\]
These constants do not depend on r because maximizing strategies have \(S_{2,M}=0\).

Every observer expression is multi-affine in the independent behavioral action probabilities because no key is revisited. Hence for **all real behavioral strategies**, maxima of any affine observer functional occur at deterministic Boolean policies. This proves the whole-real assertion analytically; finite code tests are independent checks, not a substitute for the proof.

## Exact full affine rank for d != 0

Take five valid seedless LR deterministic policies with stage-indexed STOP bits ordered (t2 X0,X1; t3 U0,U1; t4 V0,V1,V2):
\[
0000000,\quad0000001,\quad0000010,\quad0001000,\quad0010000.
\]
All have \(S_{2,P}=S_{2,Q}=0\). The determinant of the four differences relative to the first point in coordinates \((S_{5,P},S_{5,Q},T_P,T_Q)\) is exactly \(55/8192\neq0\). Equation (1) transforms the first two columns to error coordinates by the nonzero factor d, so
\[
 \boxed{\det_{\rm LR}(e_P,e_Q,T_P,T_Q)=55d^2/8192\neq0}. \tag{5}
\]
Both LR and FULL hulls have affine rank four, even though equation (4) separates them.

## Independent boundary: d=0, c != 0

Set \(Z_M=(e_M-A-BT_M)/c=S_{2,M}\) and choose the valid four-observer direction
\[
 J=T_P-\frac{17}{20}T_Q-10Z_Q. \tag{6}
\]
Time-4 optimal continuation gains are \([R_v-17/20]_+=(0,3/20,13/20)\). Time-3 continuation gains are
\[
 (G_{0,0},G_{1,0})=(-1/320,3/160),\qquad
 (G_{0,1},G_{1,1})=(263/320,27/32).
\]
Time-2 STOP is strictly dominated by CONTINUE at both X (the baseline source-specific continuation differences are \(991/100\) and \(1039/100\) even before the positive u=1 reward, and the possible u=0 negative loss is tiny). LR shares the u=0 bit and optimally STOPs because
\[
 Q_{00}(-1/320)+Q_{10}(3/160)=-43/32000<0.
\]
FULL instead continues only the positive (1,0) source, yielding
\[
\boxed{\sup_{\rm FULL}J=27899/32000,\quad
\sup_{\rm LR}J=27893/32000,\quad \Delta_J=3/16000>0.} \tag{7}
\]
This holds for every legal d=0,c!=0 error tuple because J is a legitimate observer functional after dividing by c. If c=d=0, (1) becomes e_M=A+B T_M, giving the stated affine-rank-at-most-two result. The theorem is complete.

## Explicit interior witness, exact verification, BRC and next boundary

Take \((\epsilon_2,\epsilon_3,\epsilon_4,\epsilon_5)=(7/20,1/2,1/2,3/5)\). Then c=-3/20,d=1/10,r=-3/2. A FULL deterministic maximizer never STOPs at time2, STOPs at time3 exactly at (x=0,u=0), and STOPs at time4 for v=0,1 but CONTINUEs for v=2. Its observation vector is
\[
\mathcal O^*=(17503/32000,\ 8501/16000,\ 13127/3200,\ 6117/1600),
\]
with H_100=8002697/80000 versus all seedless LR policies' bound 320107/3200. This is an actual real-set nonmembership witness as well as convex-hull separation, but NOT a valid mother counterexample because the hulls differ.

The saved standard-library Fraction verifier constructs all 12 positive P/Q masses, checks normalization and the exact rank determinant, analytically checks sign endpoints, and **fully enumerates** all 262144 FULL and 128 LR deterministic policies for each of four rational (a,r) settings, plus a fifth enumeration for d=0,c!=0. Its actual output ends with PASS_EXACT_R5_TIME_ONLY_ERROR_ALL_REAL_COMPLETE_NO_GO. These finite runs verify the formulae at the declared rational inputs; the half-line and all-real theorem is proved by equations (2)-(7).

BRC use: retain source-labeled positive masses \(q_{xuv},p_{xuv}\) and the origin-dependent continuation reward residual instead of discarding them in the likelihood-ratio quotient. This is a finite auxiliary probabilistic model; no native Heartbeat World/X6 transfer, physical prediction, or new Foundation theorem is asserted. The wider mother question remains OPEN. The previous remaining curvature wedge is now entirely excluded for THIS carrier and common time-only error family.

**Next distinct task:** change Q/P strictly positive transition weights, likelihood-ratio collision structure, or stopping topology (not merely the four errors). First test two-dimensional STOP-time convex hull equality exactly. Then seek ALL-SIGNED four-observer hull equality through rational primal combinations of every FULL vertex using <=5 LR deterministic observer vertices, or reject with an exact Farkas separating direction. If hulls equal and rank four, investigate actual real seedless LR image nonmembership using exact maximal-action-subcube facet analysis or certified quantifier elimination. Preserve true Source authority, P000, branch provenance and independent mathematical review.
