# CBRC F7 Driver r454 — Exact quadratic-energy minimum of the primitive old-axis constraint graph

Date: 2026-11-21 (+08:00). Scientific contribution: continuing RESEARCH_DRIVER line EM-DVR-DEBB5E, under shared/nonblind F7 context. Original F7 author EM-CBRCF7-83A1D4, frozen RR-AA38973D56330E59D315. This extends Driver r453 (2026-11-21, \`research_notes/driver/2026-11-21_f7_r453_exact_primitive_axis_matching_graph.md\`) without changing the original native Result/Review or its provenance.

## Exact statement and inherited model

Use exactly the original F7 map \`A=I+uv^T\`, \`u=(1,1,-1,-1)^T\`, \`v=(1,-2,-1,2)^T\`, and \`q:Z²→[0,∞)\` satisfying \`q(0,0)=0\`, \`q(-x,y)=q(x,y)\`, \`q(s,0)=1\` for all nonzero s, \`q(x,y)≥1/2\` at nonzero arguments, and the fixed-scale marks \`q(2,1)=q(-1,-1)=1/2\`. Put \`D_q(z)=q((Az)_1,(Az)_2)+q((Az)_3,(Az)_4)-q(z_1,z_2)-q(z_3,z_4)\`, and \`E(q)=sup_z |D_q(z)|\`.

For \`L≥3\`, let \`X=3L-2\`, and use r453's unchanged primitive region

\[
\Omega_L=\{(x,y)\in\mathbb Z^2:x>0,\ y\ne0,\ \gcd(x,|y|)=1,\ x\le X,\ |y|\le L-1\}.
\]

Set \`δ(x,y)=q(x,y)-1/2\`. For integers \`n≥1\` define

\[
F(n)=\frac{\lfloor n/2\rfloor\lceil n/2\rceil}{n},\qquad F(0)=0,\qquad
M(n)=1+F(n-2)\quad(n\ge2).
\]

For each \`2≤t≤L-1\`, let \`d=3t\` and
\[
m_{t,r}=1+\left\lfloor\frac{X-r}{d}\right\rfloor\quad(1\le r<d).
\]
All such \`m_{t,r}≥1\`. Define the explicit rational number

\[
\boxed{\begin{aligned}
Q(L)={}&M(L)+F(L)+M(L-1)+3F(L-1)\\
&+F(2m_{2,3})\\
&+2\sum_{t=2}^{L-1}\ \sum_{\substack{1\le r<3t/2\\\gcd(r,t)=1}}
F\bigl(m_{t,r}+m_{t,3t-r}\bigr).
\end{aligned}}
\]

**Theorem.** If \`0≤ε<1\` and \`E(q)≤ε\`, then

\[
\boxed{\displaystyle
\sum_{(x,y)\in\Omega_L}\left(q(x,y)-\frac12\right)^2
\ge (1-\varepsilon)^2\,Q(L).}
\]

Moreover, \`(1-ε)^2 Q(L)\` is the *exact minimum* over the restricted finite system consisting of the original two scalar marks, nonnegative \`δ\`, and **all** primitive old-axis two-output inequalities \`δ(+x,t)+δ(y,-t)≥1-ε\` used in r453. This equality is for that graph subsystem; it does not assert that a minimizer satisfies every four-coordinate F7 constraint.

Writing \`G(L)\` for the proven exact maximum matching count in r453,

\[
\boxed{\displaystyle
Q(L)-\frac{G(L)+2}{2}\ge
\left(\frac{7}{48\pi^2}+o(1)\right)L^2,\quad L\to\infty.}
\]

Thus the energy lower bound improves r453 by a **quadratic-order** term using the *same* graph and original scalar conditions, without a new axiom or continuity/homogeneity hypothesis.

## Exact path-energy lemma

Consider an ordinary path on \`n\` vertices, with unknown \`x_i≥0\` and inequalities \`x_i+x_{i+1}≥a\` for \`1≤i<n\`, where \`a≥0\`. Then

\[
\min\sum_{i=1}^n x_i^2=a^2F(n).
\]

If the first endpoint is constrained to equal zero and \`n≥2\`, the minimum equals \`a²M(n)\`.

For the unmarked path and even \`n=2k\`, choose all \`x_i=a/2\`. Lagrange multipliers on successive edges \`(\lambda_1,\ldots,\lambda_{n-1})=(a,0,a,0,\ldots,a)\` certify first-order optimality. For odd \`n=2k+1\`, choose alternating values \`x_{2j-1}=ak/(2k+1)\`, \`x_{2j}=a(k+1)/(2k+1)\`. The nonnegative edge multipliers
\[
\lambda_{2j-1}=\frac{2a(k-j+1)}{2k+1},\qquad
\lambda_{2j}=\frac{2aj}{2k+1},\qquad 1\le j\le k
\]
satisfy \`2x_i=\lambda_{i-1}+\lambda_i\` with zero endpoint multipliers. Every edge equality holds. Convexity of the objective and the linear inequalities make these globally minimizing certificates. The energy evaluates to \`a²\lfloor n/2\rfloor\lceil n/2\rceil/n\`. The case \`n=1\` is zero.

With \`x_1=0\`, the first edge forces \`x_2≥a\`; the energy-minimizing choice is \`x_2=a\`. Its edge to \`x_3≥0\` is then automatic, so the remaining vertices \`3,\ldots,n\` form a free path. This gives \`a²(1+F(n-2))\`. (For \`n=2\` the remaining path is empty.)

## Exact component decomposition

For the original old-axis inputs \`z=(b,0,c,0)\` with both \`b,c\ne0\`, put \`t=b-c\`. As proved in r453, for each positive \`t\` the primitive non-axis output endpoints produce the bipartite graph between \`(+x,t)\` and \`(y,-t)\`, \`1≤x,y≤X\`, both coprime to \`t\`, with edges \`|x-y|=3t\` and, for \`t≥2\`, \`x+y=3t\`. Each such edge obeys \`δ(+x,t)+δ(y,-t)≥a\`, \`a=1-ε\`.

For \`t=1\`, the three residue chains modulo 3 have underlying lengths \`L,L-1,L-1\`. Their bipartite double covers each separate into two ordinary paths of the same length. The mark \`δ(1,-1)=0\` lies at an endpoint of one path in the residue-1 component; \`δ(2,1)=0\` lies at an endpoint of one path in the residue-2 component. The residue-0 component is unmarked. By the path lemma, the total exact minimum in this slice is
\[
a^2\bigl(M(L)+F(L)+M(L-1)+3F(L-1)\bigr).
\]

For \`t≥2\` and each distinct primitive residue pair \`r,3t-r\` with \`r<3t/2\`, r453 proves their reflection and \`3t\`-shift chains combine into one underlying ordinary path of length \`m_{t,r}+m_{t,3t-r}\`. Its bipartite double cover is **two disjoint paths**, contributing exactly \`2a²F(m_{t,r}+m_{t,3t-r})\`.

The sole primitive self-reflection residue is \`t=2,r=3\`. Its base reflection is a \`(+3,2)\`--\`(3,-2)\` edge and its double-cover shift chain is **one** ordinary path on \`2m_{2,3}\` vertices, contributing \`a²F(2m_{2,3})\`. Distinct slices, residue pairs and the exceptional chain have disjoint scalar variables. Summation proves both the displayed universal lower bound and its exact sharpness *within the restricted graph system*.

## Strict quadratic-order improvement over the r453 matching bound

For an unmarked double-cover component of underlying path length \`N\`, the exact minimum is \`2a²F(N)\`, whereas the disjoint-edge Jensen bound from r453 is \`a²\lfloor N/2\rfloor\`. Their difference is zero if \`N\` is even and \`a²(N-1)/(2N)\` if \`N\` is odd. All other graph components improve or equal their r453 matching/Jensen lower bounds, including the two pinned-endpoint components.

Restrict \`t\` to
\[
\lceil2L/3\rceil\le t\le\lfloor3L/4\rfloor.
\]
For large L, \`d=3t\`, \`X=d+R\` with \`0<R<d/2\`, and \`R=3(L-t)-2\`. Each \`1≤r≤R\` with \`gcd(r,t)=1\` forms one distinct residue-pair component with \`m_{t,r}=2\`, \`m_{t,d-r}=1\`, hence \`N=3\` and an energy gain of exactly \`a²/3\` beyond r453.

The number of these components is
\[
H_L=\sum_{t=\lceil2L/3\rceil}^{\lfloor3L/4\rfloor}
\#\{1\le r\le3(L-t)-2:\gcd(r,t)=1\}.
\]
Using \`C_t(Y)=Y\varphi(t)/t+O(\tau(t))\` and the elementary mean \`\sum_{t\le x}\varphi(t)/t=(6/\pi^2)x+O(\log x)\`, weighted summation gives
\[
H_L=\frac6{\pi^2}L^2\int_{2/3}^{3/4}3(1-u)\,du+O(L\log L)
=\frac{7}{16\pi^2}L^2+O(L\log L).
\]
The stated improvement follows from \`Q(L)-(G(L)+2)/2≥H_L/3\`.

## Exact arithmetic and independently formulated numerical crosschecks

The displayed finite-sum formula uses only \`gcd\`, integer division and rational arithmetic. Independently enumerating the primitive bipartite edges from \`|x-y|=3t\` and \`x+y=3t\` and solving the full convex quadratic programs with SciPy SLSQP (direct variables and edge matrices, both exact marks fixed to zero) gave the same minima for L=3,4,5 to floating-point solver tolerances. The exact rational formula gives:

| L | r453 G(L) | r453 square-energy bound / a² | new exact graph minimum Q(L) | increase / a² |
|---:|---:|---:|---:|---:|
| 3 | 9 | 11/2 | 6 | 1/2 |
| 4 | 18 | 10 | 67/6 | 7/6 |
| 5 | 30 | 16 | 181/10 | 21/10 |
| 6 | 49 | 51/2 | 28 | 5/2 |
| 10 | 145 | 147/2 | 25322/315 | 4339/630 |
| 20 | 622 | 312 | ≈340.57237 | ≈28.57237 |
| 50 | 3979 | 3981/2 | ≈2171.21182 | ≈180.71182 |
| 100 | 15984 | 7993 | ≈8721.06191 | ≈728.06191 |

The row L=10 is fully specified by its exact formula; the difference expression should be evaluated from the displayed fractions. The exact path/multiplier proof applies for every integer L≥3; the finite optimizer comparisons are sanity checks only.

## Status, provenance and next experiment

Scientific status: a new exact restricted-graph coercivity theorem, fully proved under the original F7 assumptions, shared-context Driver contribution. It improves a prior lower bound on an **energy of primitive scalar values**, not the existing universal minimax interval \`1/2≤E_infinity≤4/7\`. Native review, accepted Result, original frozen F7 SHA256 integrity and formal Source/Activity association are separate current-control decisions.

A discriminating next direction is to add a small, explicitly declared family of non-old-axis four-coordinate F7 constraints to this exact graph and test whether the quadratic minimum or the global minimax lower bound increases. For T6 the original published q14 roster/count remains credited to EM-EMF6D046-5A2844; original delegated-plan mapping/independent review remains separate.
