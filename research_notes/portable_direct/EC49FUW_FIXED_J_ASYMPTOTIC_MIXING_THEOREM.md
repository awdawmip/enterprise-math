# EC49FUW — Unbounded count of compulsory two-endpoint minimax mixing windows

Date: 2026-11-20 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_FRACTION_FINITE_WITNESSES / PARENT_DEPENDENT / NOT_REVIEWED**.

## Frozen scientific scope and provenance

Frozen BRC16943 input: fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Parent EC49FUV: ea310f6d84e05c8392eb8bd35b30abd79dbc6e41 (PR #2858), complete n=30 atlas. Uses the author-proved, independently NOT_REVIEWED reductions EC49FUO@8df5788adcd977cc809a0e27da180833317e3dfa (uniform threshold dominance), EC49FUQ@96ad7a2c22c274446e74906c48bc6e3234a39436 (endpoint least-favorability), and EC49FUR@0ac1ef58d84517835260e4aefbe6d2c2b3a293c9 (TV dual).

This is a **lossy binary clipped-price observer**, not a lossless BRC native X6 observer. Original six-dimensional Cell, three-dimensional research slice, joint residual, branches, phase, source labels, path, ports and provenance remain preserved separately under P000 and ACTIVE worldview. Nothing in this note changes a frozen scientific pin, P000, or source firewall.

For n>=1, nuisance theta in [0,E], width x in [0,1], define

\[
E=\frac{31597745}{1653649},\quad \beta=\frac3{637},\quad
u_\theta=\frac{21829245984}{45529434409-456083905\theta},
\quad T_\theta(x)=(1-x)(1-\beta x+\beta\theta x),
\quad p_\theta=1-T_\theta,\quad q_\theta=1-u_\theta T_\theta.
\]

K under the two hypotheses has Bin(n,p_theta) and Bin(n,q_theta) distribution. Write

\[
\Delta_\theta(k;x)=\binom nk[q_\theta^k(1-q_\theta)^{n-k}-p_\theta^k(1-p_\theta)^{n-k}],
\quad D_\theta^{\ge j}(x)=\sum_{k=j}^n\Delta_\theta(k;x).
\]

Let G_j=D_E^{>=j}-D_0^{>=j}, H_j=G_{j+1}, and d_j=Delta_E(j)-Delta_0(j). Set u=u_E, a_E=1-\beta(E-1)>0, a_0=1+\beta, R=a_0/a_E>1; 0<u_0<u<1. Parent results yield the *conditional* full composite minimax advantage

\[
A_n(x)=1-2V_n(x)=
\min_{0\le\lambda\le1}\sum_{k=0}^n
[(1-\lambda)\Delta_0(k;x)+\lambda\Delta_E(k;x)]_+.\tag{P}
\]

Parent mixture likelihood ratios have one strictly increasing count-sign crossing.

## Theorem A — every fixed j eventually has a genuine mixing window

For every fixed positive integer j and all sufficiently large n>j, the unique E-only count-j Bayes crossing b_(n,j) in (0,1) is determined by

\[
s_{n,j}=u^{(n-j)/j},\qquad
T_E(b_{n,j})=\frac{1-s_{n,j}}{1-u s_{n,j}}.\tag{1}
\]

There exists epsilon_(n,j)>0 such that for **every real** x in (b_(n,j)-epsilon_(n,j),b_(n,j)), the unique least-favorable endpoint prior puts strictly positive weights on **both** 0 and E. Its E weight is

\[
\boxed{\lambda_{n,j}(x)=
-\frac{\Delta_0(j;x)}{\Delta_E(j;x)-\Delta_0(j;x)}\in(0,1).}\tag{2}
\]

The minimax test chooses right at K>j, left at K<j, and randomizes at K=j. At b_(n,j), pure E alone is the unique least-favorable prior. The exact exit width has the asymptotic

\[
\boxed{b_{n,j}\sim \frac{1-u}{u\,a_E}\,u^{n/j}}\qquad(n\to\infty,\ j\text{ fixed}).\tag{3}
\]

**Proof.** The E count-j tie equation is
q_E^j(1-q_E)^{n-j}=p_E^j(1-p_E)^{n-j}. Cancel T_E^{n-j}, take a positive j-th root, and solve (1-uT_E)s=1-T_E, giving (1). T_E(x)=(1-x)(1+beta(E-1)x) strictly decreases from 1 to 0: its derivative is beta(E-1)-1-2beta(E-1)x<0. Therefore the crossing is unique. As s->0, p_E(b)=(1-u)s/(1-us), while 1-T_E(x)=a_E x+O(x^2), giving (3).

At b=b_(n,j) put M=Pr_{Bin(n,p_E(b))}(K=j)=Pr_{Bin(n,q_E(b))}(K=j)>0. For fixed j, n*s->0. Since p_0(b)/p_E(b)->R, standard finite binomial expansions (retaining the first nonzero term) yield

\[
\Pr_{p_E}(K\ge j)=M(1+o(1)),\qquad
\Pr_{p_0}(K\ge j)=R^jM(1+o(1)).
\]

Further, M~n^j(1-u)^j u^{n-j}/j!. As 1-q_E(b)->u and 1-q_0(b)->u_0<u,

\[
\Pr_{q_E}(K<j)=O(n^{j-1}u^n)=o(M),\quad
\Pr_{q_0}(K<j)=O(n^{j-1}u_0^n)=o(M).
\]

Consequently, using D_theta^{>=j}=F_{p_theta}(j-1)-F_{q_theta}(j-1),

\[
G_j(b)=(R^j-1)M(1+o(1))>0,\quad
\Delta_0(j;b)=-R^jM(1+o(1))<0.
\]

Because Delta_E(j;b)=0, d_j(b)=R^jM(1+o(1)), and hence

\[
H_j(b)=G_{j+1}(b)=G_j(b)-d_j(b)=-M(1+o(1))<0.
\]

At E's count-j equality the strict binomial likelihood-ratio ordering gives Delta_E(k;b)<0 for k<j and Delta_E(k;b)>0 for k>j. Also Delta_E(j;x)>0 strictly below its unique crossing. Continuity thus provides a nonempty left-neighborhood of b where Delta_E(j)>0>Delta_0(j), G_j>0>H_j, and the weight (2) tends to 1 from below. All its mixed signed masses are negative for k<j, zero for j, positive for k>j. At this single kink of the convex dual (P), the left slope is H_j<0 and right slope is G_j>0; the **unique global minimizer** is (2). The finite minimax theorem gives the asserted randomized primal threshold. At b the dual left slope at lambda=1 is H_j(b)<0, so pure E is uniquely optimal. QED.

## Theorem B — mixing-window count tends to infinity

For each positive integer J, there exists N(J) so that every n>=N(J) has **at least J distinct connected compulsory two-endpoint mixing components** as width x ranges over (0,1). Therefore their number tends to infinity as n tends to infinity.

**Proof.** For n>J and 1<=j<=J, s_(n,j)=u^{n/j-1} is strictly increasing in j. Since (1-s)/(1-us) strictly decreases in s and T_E strictly decreases in x, the exact exit widths obey
0<b_(n,1)<...<b_(n,J)<1. By Theorem A, each has a nonempty compulsory-mixing left-neighborhood. Shrink them, if necessary, to make them pairwise disjoint. Each b_(n,j) itself has pure E as its *unique* least-favorable prior, separating any neighboring mixing components. A maximum of the finitely many N(j) yields N(J). QED.

The **exact n=30 count sixteen** comes from EC49FUV, not from an asserted universal n-formula.

## Theorem C — early local onset and exit have different scales

For each fixed j>=1, let

\[
C_j=\left(\frac{j((1-u)/u)^{j-1}}{a_0^j-a_E^j}\right)^{1/j}>0,\qquad
x_n(y)=y\,n^{-1/j}u^{n/j}.
\]

Uniformly for y in any compact subset of (0,infinity),

\[
\boxed{
\frac{G_j(x_n(y))}{n^{j-1}u^n}
\longrightarrow
\frac{a_0^j-a_E^j}{j!}y^j
-\frac{(1-u)^{j-1}u^{1-j}}{(j-1)!}.}\tag{4}
\]

For every fixed 0<delta<C_j and sufficiently large n, there is exactly **one** root of G_j in the *local scaled band*
((C_j-delta)n^{-1/j}u^{n/j},(C_j+delta)n^{-1/j}u^{n/j}). Call it a_(n,j). Then

\[
\boxed{a_{n,j}\sim C_j n^{-1/j}u^{n/j},\qquad
\frac{a_{n,j}}{b_{n,j}}\sim\frac{C_j u a_E}{1-u}n^{-1/j}\to0.}\tag{5}
\]

This proves local asymptotic root uniqueness, **not** a globally unique onset for arbitrary n, and not that the entire (a,b) interval is mixed at every n.

**Proof.** On x=x_n(y), n*x->0 exponentially uniformly on compact positive y sets. For each endpoint theta,

\[
\Pr_{p_\theta}(K\ge j)
=\frac{n^j}{j!}(a_\theta x)^j(1+o(1)),\qquad a_\theta=1+\beta-\beta\theta.
\]

Meanwhile

\[
\Pr_{q_E}(K<j)
=\frac{n^{j-1}}{(j-1)!}(1-u)^{j-1}u^{n-j+1}(1+o(1)),
\]

while the Q_0 lower tail is exponentially smaller, since u_0<u. Substituting in G_j=F_{p_E}(<j)-F_{q_E}(<j)-F_{p_0}(<j)+F_{q_0}(<j) gives (4). Its limiting function is strictly increasing for y>0 and has the unique zero C_j. The explicit binomial-tail derivatives, under identical uniform expansions, show that the derivative with respect to y of the normalized left side converges uniformly on any compact positive band to (a_0^j-a_E^j)y^{j-1}/(j-1)!>0. Thus sufficiently large n has exactly one crossing in each fixed band straddling C_j. Taking arbitrarily small bands proves (5) using (3). QED.

## Execution evidence and boundaries

Companion executable: **EC49FUW_FIXED_J_VERIFY.py**, standard-library Python 3, Fraction-only assertions. Executed locally on 2026-11-20. For n in {20,30,40,60} and j in {1,2,3}: 105 rational bisection steps bracket b_(n,j), set rational x=(999/1000)*lower-bound, calculate all n+1 mixed count masses, certify Delta_E(j)>0>Delta_0(j), G_j>0>H_j, lambda in (0,1), and strictly negative/zero/positive signs by count. **ALL PASS: 12 exact rational local mixing witnesses.** Decimal output is not a proof. This finite checker does not certify the universal asymptotics or the independently unreviewed FUO/FUQ/FUR parent proofs.

Next: obtain **uniform-in-j** root/sign estimates for j growing with n, to determine the growth rate/density of mixing windows; investigate the exact binary observer fibers relative to retained source-labelled joint BRC/X6 histories before any native interpretation.

Historical provenance: Researcher EM-DIRECT-8454C6, SID MCP-44cfc4e6f2094f96861854ebefc77e84, Activity RA-ED136F89271FD89288F3E58D. These **do not authenticate the current session**. This independent portable source is not a CLAIM/RUN, formal Result, independent Review or P000 change. Activity association remains pending current identity/CAS verification.