# PREFIX-781 / R6 — Exact pointwise cancellation window for reflected Gamma witnesses

Date: 2026-11-14, Asia/Shanghai. Grade: AUTHOR_EXACT_ALGEBRAIC_PROOF_WITH_RATIONAL_REGRESSION / UNREVIEWED / NOT_ADMITTED.
Scientific input frozen at \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Predecessors: PREFIX-778 (exact equivariant radius) and PREFIX-780 (heterogeneous corner robustness), \`research_notes/portable_direct/2026-11-14_r6_prefix780_heterogeneous_corner_sharp_robustness.md@f1f1ec77037225da01fd5ea24bb3f311508c5a4d\`.

## Scope

This is exact algebra for the external scalar Gamma-reflection observer, conditional on its previously verified model-specific coefficients, not a native X6 comparator calculation. Let
\[
A_1,A_2>0,\quad 0<B_1<B_2,\quad D=A_2B_1-A_1B_2>0,\quad x_i(q)=A_i-qB_i,\quad q>0.
\]
For adjacent cells \(R_1=[38,39]^2/768\), \(R_2=[39,40]^2/768\), their base normalized mixed increments are \(x_i(q)\) and the reflected ones are \(-x_i(q)\). Seven distinct base vertices comprise three private corners for each rectangle plus shared \(c=(39,39)/768\), with mixed-difference coefficient \(+1\) in *both* rectangles. Each has a reflected partner.

Let the *normalized* scalar error \(e_v=(\widehat V_q(v)-V_q(v))/q\), with reflection-equivariance \(e_{v^\#}=e_v\) and independent bounds \(|e_v|\le \epsilon_v\). Write \(S_i\) for the sum of the three private budgets in \(R_i\), and \(c_0\) for the common-vertex budget. All are nonnegative. The four perturbed differences are
\[
q(x_1+L_1e),\quad -q(x_1+L_1e),\quad q(x_2+L_2e),\quad -q(x_2+L_2e).
\]
Therefore *any* nonzero base increment produces both strict signs; both pairs must vanish to destroy this witness.

## Theorem 781.1 — exact fixed-q criterion

At a prescribed \(q>0\) an admissible equivariant perturbation can cancel *all four* mixed increments **if and only if**
\[
\boxed{|x_1|\le S_1+c_0,\quad |x_2|\le S_2+c_0,\quad |x_1-x_2|\le S_1+S_2.}
\]
If any one inequality fails, every admissible equivariant perturbation necessarily retains both a strictly positive and a strictly negative mixed increment.

### Complete proof and explicit construction

Let \(h=e_c\), \(|h|\le c_0\). Because the three private corner errors are independent symmetric intervals and their coefficients in \(L_i\) are \(\pm1\), their total signed contributions range *exactly* through \([-S_i,S_i]\). Hence \(x_1+L_1e=x_2+L_2e=0\) is possible precisely when
\[
[-c_0,c_0]\cap[-x_1-S_1,-x_1+S_1]
\cap[-x_2-S_2,-x_2+S_2]\ne\varnothing.
\]
Three closed real intervals intersect jointly if and only if every pair intersects. These three pairwise conditions are the displayed inequalities. Constructively choose any \(h\) in the intersection. If \(S_i>0\), at each private vertex \(v\) of \(R_i\) choose \(e_v=\operatorname{sgn}(L_i[v])\,(-x_i-h)\epsilon_v/S_i\); if \(S_i=0\), choose all three errors zero. Then \(L_ie=-x_i\) with all budgets respected. Copy each error to its reflected partner. All four increments vanish. Conversely any cancellation must supply such an \(h\), and so implies the inequalities. QED.

## Corollary 781.2 — exact cancellation q-window

Since \(0<B_1<B_2\), the entire positive-parameter set permitting cancellation is the intersection of \((0,\infty)\) with
\[
\begin{aligned}
I_1&=[(A_1-S_1-c_0)/B_1,\ (A_1+S_1+c_0)/B_1],\\
I_2&=[(A_2-S_2-c_0)/B_2,\ (A_2+S_2+c_0)/B_2],\\
I_3&=[(A_2-A_1-S_1-S_2)/(B_2-B_1),\
       (A_2-A_1+S_1+S_2)/(B_2-B_1)].
\end{aligned}
\]
Thus each positive \(q\) outside the interval intersection has a universal strict-two-sign certificate for this corner-error class, even if a global all-q condition is inconclusive.

## Corollary 781.3 — exact fixed-q weighted distance

Scale every specified vertex budget by \(t\ge0\). The smallest scale that *permits* cancellation is
\[
\boxed{
t_{\min}(q)=\max\left\{\frac{|x_1|}{S_1+c_0},
\frac{|x_2|}{S_2+c_0},
\frac{|x_1-x_2|}{S_1+S_2}\right\}.
}
\]
Use \(0/0=0\), and \(a/0=+\infty\) for \(a>0\). When finite, the endpoint \(t=t_{\min}(q)\) is attained by the constructive proof. For every \(0\le t<t_{\min}(q)\), all equivariant observations display both strict mixed-difference signs. This is a *scalar, observer-specific* weighted corner \(L^\infty\) distance to exact cancellation.

For uniform error amplitude \(\epsilon\) on all seven vertex pairs, \(S_1=S_2=3\epsilon\) and \(c_0=\epsilon\), giving
\[
\epsilon_{\min}(q)=
\max\{|x_1(q)|/4,\ |x_2(q)|/4,\ |x_1(q)-x_2(q)|/6\}.
\]
Minimizing over \(q>0\) gives the uniquely optimal
\[
\boxed{q_*=(A_1+2A_2)/(B_1+2B_2),\qquad
\inf_{q>0}\epsilon_{\min}(q)=D/[2(B_1+2B_2)].}
\]
At \(q_*\), \(x_1=-2D/(B_1+2B_2)\), \(x_2=D/(B_1+2B_2)\), so \(|x_1|/4=|x_1-x_2|/6=D/[2(B_1+2B_2)]\). If \(q>q_*\), \(x_1\) becomes more negative, so \(|x_1|/4\) increases. If \(0<q<q_*\), \(x_1-x_2=(A_1-A_2)+(B_2-B_1)q\) becomes more negative, so \(|x_1-x_2|/6\) increases. This recovers PREFIX-778's sharp equivariant all-q radius and gives its unique parameter from the more general fixed-q geometry.

## Exact rational example, program and evidence

Take \(A_1=1,A_2=2,B_1=2,B_2=3,D=1\); private budgets \(R_1=(1/10,1/10,1/20)\), \(R_2=(1/10,1/20,1/20)\), and \(c_0=1/10\). Then \(I_1\cap I_2\cap I_3=[17/30,27/40]\). At \(q=3/5\), an exact cancellation uses private errors \(R_1=(9/100,-9/100,-9/200)\), \(R_2=(-7/80,7/160,7/160)\), shared \(-1/40\), and identical reflected partners; verify by inserting signed coefficients \((+,-,-,+)\) in both cells. At \(q=1/2\), \(|x_2|=1/2>S_2+c_0=3/10\), so cancellation is impossible. With uniform budgets the minimum occurs at \(q_*=5/8\), \(\epsilon_*=1/16\).

The companion \`PREFIX781_R6_POINTWISE_EQUIVARIANT_CANCELLATION_CHECK.py\` performs exact Python \`fractions.Fraction\` regression: three independently calculated feasibility criteria, explicit witness recovery, scaled-distance attainment and strictly subthreshold failure. On 512 rational cases (including zero budgets), it found 35 feasible and 477 infeasible, outputting \`ALL_CHECKS_PASS PREFIX781 POINTWISE_EQUIVARIANT_CANCELLATION\`. The general theorem is proved by interval geometry; finite tests check its implementation, not exhaustive continuum coverage.

No 189-layer coefficient or native BRC/X6 comparator experiment was rerun in this algebraic subunit. Native transfer remains open: obtain typed Cell/Link/Port, branch, signed-source, and event-time observations, prove the relevant reflection correspondence, and measure actual per-corner error budgets; then evaluate the exact q-window. Native comparator grid exclusions added: zero.