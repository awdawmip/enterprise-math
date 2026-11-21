# CBRC F7 Driver r456 — Exact two-path mixed-constraint energy penalties for L=3 and L=4

Date: 2026-11-22 (+08:00). Contributor: original F7 Researcher \`EM-CBRCF7-83A1D4\`; this nonblind/shared-context mathematical extension is by Driver line \`EM-DVR-DEBB5E\`. Frozen original Result \`RR-AA38973D56330E59D315\` is not altered. Source dependencies: original F7 scalar model, Driver r453 primitive old-axis graph, r454 exact path minimum, r455 mixed four-coordinate witness.

## Original scope and new theorem

Use the original F7 involution
\[
 A=I+uv^{T},\qquad
 u=(1,1,-1,-1)^T,\quad v=(1,-2,-1,2)^T,
\]
and the original \(q:\mathbb Z^2\to[0,\infty)\): \(q(0,0)=0\), \(q(-x,y)=q(x,y)\), \(q(s,0)=1\) for \(s\ne0\), \(q(x,y)\ge1/2\) for nonzero \((x,y)\), with \(q(2,1)=q(-1,-1)=1/2\).
Let
\[
D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(z_1,z_2)-q(z_3,z_4),\quad
E(q)=\sup_{z\in\mathbb Z^4}|D_q(z)|.
\]
For nonzero arguments put \(\delta(x,y)=q(x,y)-1/2\). Retain r454's primitive region
\[
\Omega_L=\{(x,y)\in\mathbb Z^2:x>0,\ y\ne0,\ \gcd(x,|y|)=1,\ x\le3L-2,\ |y|\le L-1\}.
\]
Assume \(1/2\le\varepsilon\le4/7\) and \(E(q)\le\varepsilon\), and set \(a=1-\varepsilon\), \(b=1/2-\varepsilon\). In particular \(-a/6\le b\le0\).

**Theorem (exact mixed-path improvement).**
\[
\boxed{\sum_{\Omega_3}\delta(x,y)^2
 \ge 6a^2+\frac{(4-7\varepsilon)^2}{30},}
\tag{1}
\]
\[
\boxed{\sum_{\Omega_4}\delta(x,y)^2
 \ge\frac{67}{6}a^2+\frac{(5-8\varepsilon)^2}{24}.}
\tag{2}
\]
The right-hand sides are **exact minima** of the finite restricted systems formed from r454's complete primitive old-axis graph, the original two scalar marks, nonnegative \(\delta\), and the additional *one original* F7 witness constraint at \(z=(-4,0,-1,2)\). In particular, (1)–(2) apply to every original globally admissible \(q\), but equality for the finite subsystem is not a global F7 construction.

At the endpoints: for \(\varepsilon=1/2\), the additional gaps over r454 are exactly \(1/120\) and \(1/24\); at \(\varepsilon=4/7\), they are \(0\) and \(3/392\). These sharpen r455's respective Cauchy–Schwarz gap bounds \((4-7\varepsilon)^2/72\) and \((5-8\varepsilon)^2/72\). The existing global minimax interval \(1/2\le E_\infty\le4/7\) is unchanged.

## Proof: the exact two affected components

The original witness \(z=(-4,0,-1,2)\) has \(v^Tz=1\), \(Az=(-3,1,-2,1)\). Using the fixed mark and axis condition,
\[
 D_q(z)=\delta(3,1)-\delta(1,2)-1/2.
\]
Writing \(x=\delta(3,1)\), \(y=\delta(1,2)\), its necessary half-space is \(x-y\ge b\); the witness's other inequality is also satisfied at the sharp configurations below because they take \(x-y=b\).

In the r453–r454 *complete* old-axis graph, the component containing \(x\) is a two-vertex path in \(\Omega_3\):
\[
x=\delta(3,1)\ \ --\ \ u=\delta(6,-1),\qquad x+u\ge a.
\]
In \(\Omega_4\) it is a three-vertex path:
\[
x=\delta(3,1)\ \ --\ \ u=\delta(6,-1)\ \ --\ \ w=\delta(9,1),
\quad x+u\ge a,\quad u+w\ge a.
\]
For both regions the component containing \(y\) is a three-vertex path with \(y\) in its middle:
\[
r=\delta(5,-2)\ \ --\ \ y=\delta(1,2)\ \ --\ \ s=\delta(7,-2),
\quad r+y\ge a,\quad y+s\ge a.
\]
All these paths are disjoint from each other, from the two original marks, and from the remaining graph components. The latter may therefore retain the exact r454 minimizers.

For \(0\le x,y\le a\), minimizing the energy in each path at fixed center/endpoint gives:

* \(\Omega_3\) x-path: \(f_2(x)=x^2+(a-x)^2\), attained by \(u=a-x\).
* \(\Omega_4\) x-path, for \(x\le a/2\): \(f_3(x)=2x^2+(a-x)^2\), attained by \(u=a-x,\ w=x\).
* y-path: \(g_3(y)=y^2+2(a-y)^2\), attained by \(r=s=a-y\).

The expressions above are also valid as global convex subproblem costs in the relevant ranges; outside these ranges the costs are the corresponding convex continuations, so a feasible global KKT point in the displayed ranges is globally optimal.

For \(\Omega_3\), the unique coupled candidate is
\[
x_3=\frac{3(a+b)}5,\qquad y_3=\frac{3a-2b}5,\qquad x_3-y_3=b.
\]
Since \(-a/6\le b\le0\), we have \(a/2\le x_3\le3a/5\) and \(3a/5\le y_3\le2a/3\). Here \(f_2'(x_3)=-g_3'(y_3)=2(a+6b)/5\ge0\), exactly the nonnegative KKT multiplier for \(x-y\ge b\). The feasible point is thus globally optimal for the two disjoint convex path problems and the coupling, and the excess over their uncoupled minimum \(a^2(F(2)+F(3))=7a^2/6\) is
\[
f_2(x_3)+g_3(y_3)-\frac76a^2
 =\frac{(a+6b)^2}{30}
 =\frac{(4-7\varepsilon)^2}{30}.
\]

For \(\Omega_4\), the coupled candidate is
\[
x_4=\frac{a+b}2,\qquad y_4=\frac{a-b}2,\qquad x_4-y_4=b.
\]
Here \(5a/12\le x_4\le a/2\), \(a/2\le y_4\le7a/12\), and \(f_3'(x_4)=-g_3'(y_4)=a+3b\ge0\). It is the global feasible convex KKT minimizer and its excess over the two uncoupled length-three paths, of minimum energy \(4a^2/3\), is
\[
f_3(x_4)+g_3(y_4)-\frac43a^2
 =\frac{(a+3b)^2}{6}
 =\frac{(5-8\varepsilon)^2}{24}.
\]

Every other old-axis component remains at its uncoupled exact minimum. Adding \(Q(3)=6\) and \(Q(4)=67/6\) from r454 proves (1)–(2), including *attainability within the stated restricted graph*. The additional F7 witness has \(D_q(z)=-\varepsilon\) at these finite minimizers, so its complete two-sided bound is satisfied. QED.

## Independent finite check and status

Separately rebuilt the primitive old-axis bipartite graph from its edge rules \(|x-y|=3t\) and, for \(t\ge2\), \(x+y=3t\), with gcd tests and both fixed marks. A fresh SLSQP solve of the full finite quadratic program (not just the derived two-path formulas) used 22 vertices / 13 edges at \(L=3\) and 44 vertices / 29 edges at \(L=4\). At \(\varepsilon=1/2,\ 11/20,\ 4/7\), the computed minima agree with the exact formulas to <1e-11. These finite numerical checks are corroboration; the proof is the exact algebraic graph decomposition and convex KKT certificate above.

Research classification: exact *restricted-subsystem* finite theorem and universally valid energy lower bounds, under the unchanged original F7 hypotheses. Contribution context: shared/nonblind Driver; no newly accepted Native Review, Native Result, Task completion, P000 promotion or original Source/Activity event is asserted. The next scientific discriminator is simultaneous exact coupling of multiple independent four-coordinate witnesses or a certified \(B=12\) minimax obstruction, preserving the original unmodified F7 scalar assumptions.
