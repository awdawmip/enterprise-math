# Stage339-B — quantitative strict local Pareto theorem at the double-zero cusp

Date: 2026-11-01 Asia/Shanghai. **PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_SYMBOLIC_EXECUTED / UNREVIEWED / NOT_ADMITTED.**

Frozen global canonical main: 2dde259b7039962a5f02669e83f7ffc38081e01f; Enterprise Math main: a55b67a90d9ac18a22eb5a996f8a6a1ab4e3446e; native P000 V5 blob: bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Direct predecessor: Stage338-B proof blob fa7dd1afb0e5e135775b52c22b53b048ad399b3b, PR #1736 head b0476686fb3d9419526d356090c9ac47c6f3c5ad. This is a non-blind continuation of the same author line. The declared subject is the *source-labelled three-visit Bernoulli/BRC auxiliary observer*, not a native P000/X6 dynamics theorem.

For k=0,1,2,3, define B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9), and

r_k(x,y)=[4B_k(x)+B_k(y)]/5-m_k/160,    b(x,y)=(5/32) Σ_k w_k |r_k(x,y)|.

Preserving all 16 provenance-tagged source comparisons, define

D_3(a,z)=(1/2)Σ_k w_k|B_k(a)-B_k(z)|,

c(x,y)=[63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)]/256.

Two source groups have P=b(q1)+b(q2), T=33/1024+c(q1)+c(q2). The theorem below is about a *single group's local* Pareto status, not the global two-group optimum.

## Exact theorem

Let q*=(x*,y*) be the unique solution r0=r1=0 within

I_x=[231083/10^6,231085/10^6],  I_y=[5554961/10^7,5555202/10^7].

The uniqueness and existence were proved in Stage338-B; the accompanying checker rechecks the strict rational sign brackets. In this box r2(q*)>1/250 and r3(q*)<-3/250.

**For every real q ∈ [0,1]^2 satisfying 0<||q-q*||_2<=1/3000,**

\[
\boxed{\max\{b(q)-b(q_*),c(q)-c(q_*)\}>\|q-q_*\|_2/1000.}
\tag{339.1}
\]

In particular, no distinct q in this explicitly given neighbourhood weakly improves both b and c. Hence q* is a quantitatively strict, **locally Pareto-efficient** point.

## Proof: uniform first-order directional gap

The exact weighted conservation law is r0+3r1+3r2+r3=0. For r2>0,r3<0, it gives

\[
b=(5/16)[-r_3+(-r_0)_++3(-r_1)_+],\quad t_+=\max(t,0).
\]

The 16 tagged comparison signs on the root box are, respectively, -+++, --++, ++--, --++. They remain fixed over the radius-1/3000 enclosing strip. Differentiation of these *labelled* source terms gives

\[
A=\nabla c=(-p,q_a),\quad p=(1-x)(189-183x)/256,\quad q_a=3y(1-y)/64.
\]

Let J_i=∇r_i(q*), κ=5/16. The preceding Stage338 KKT construction chooses α=1 and

\[
\beta=-[q_a(r_{3,x}+r_{0,x})+p(r_{3,y}+r_{0,y})]/
       [3(q_a r_{1,x}+p r_{1,y})],
\]
\[
g=-\kappa(J_3+J_0+3\beta J_1),\qquad\lambda=p/g_x.
\]

Exact rational interval bounds throughout the root box yield
1/6<β<1/4, 7/20<g_x<2/5, 1<λ<2.
A symbolic rational-function identity (not a numerical approximation) gives A+λg=0.

For every real direction h, the exact directional derivatives at q* obey

\[
D c[h]=A\cdot h,\quad
D b[h]=g\cdot h+\kappa[(J_0\cdot h)_+
                   +3((-J_1\cdot h)_++\beta J_1\cdot h)].
\]

Thus Dc[h]+λ Db[h]>=5λ|J1·h|/32. Set t=max(Db[h],Dc[h]). Since λ>0, necessarily t>=0, and
|J1·h|<13t and |Dc[h]|<=2t.

The exact root-box interval certificate gives
0.4<p<0.45, 0<q_a<0.012, 0<r1,x<0.19,
0.059<-r1,y<0.06, and

\[
\Delta=\det\begin{pmatrix}-p&q_a\\r_{1,x}&r_{1,y}\end{pmatrix}
=p(-r_{1,y})-q_a r_{1,x}>23/1000.
\]

Inverting these two linear forms gives |h_x|<12t,
|h_y|<271t, hence ||h||_2<500t. We have proved the uniform cone inequality

\[
\boxed{\max(Db[h],Dc[h])>\|h\|_2/500\quad(h\ne0).}
\tag{339.2}
\]

## Proof: finite radius

The enclosing rational strip is inside x∈[0.21,0.24], y∈[0.5,0.57], below the exact source-tag cusp. The checker certifies *all 16* strict sign comparisons on this strip. The global derivatives of r2,r3 on [0,1]^2 have Euclidean norms <1 and <3, respectively, so their strict base-point signs persist throughout radius 1/3000.

For z∈[0,1], |B_k''(z)|<=6. Taylor's theorem plus the 1-Lipschitz absolute-value map give

\[
|b(q_*+h)-b(q_*)-Db[h]|\le3\|h\|_2^2.
\]

The tagged polynomial c has Hessian diagonal with
|cxx|<372/256<3/2 and |cyy|<=3/64<3/2.
Therefore

\[
|c(q_*+h)-c(q_*)-Dc[h]|\le(3/4)\|h\|_2^2.
\]

Use (339.2) and ||h||_2<=1/3000:

\[
\max(\Delta b,\Delta c)>
\|h\|_2/500-3\|h\|_2^2
\ge\|h\|_2/1000.
\]

This proves (339.1) for all real parameters in the specified neighbourhood, not merely on a grid.

## Second result: the fixed supporting scalarization has negative second-order curvature

With the exact q*-chosen constants β,λ fixed, put

\[
G=c-\lambda(5/16)(r_3+r_0+3\beta r_1).
\]

Stationarity gives ∇G(q*)=0. On the r1=0 curve pointing into r0<0, G=c+λb.
The curve tangent v=(-r1,y,r1,x) at q* satisfies
J0·v< -1/10, Dc[v]=-Δ<0 and Db[v]=Δ/λ>0.

The Hessian of G is diagonal, with

\[
G_{xx}=(372-366x)/256-\lambda(5/16)
          [24/5+3\beta(4/5)(6x-4)]<-1/10,
\]

\[
G_{yy}=3(1-2y)/64-\lambda(5/16)
          [6/5+3\beta(1/5)(6y-4)]<-2/5.
\]

Hence v^T∇²G(q*)v<0. Along the implicit smooth curve r1=0,
the first derivative of G at q* vanishes and its second derivative is negative;
thus the fixed positive weighted sum c+λb strictly decreases on the short r0<0
side. This does **not** dominate q*: c decreases and b increases to first order.
It demonstrates precisely why a nonsmooth KKT-weighted scalarization cannot
replace an actual Pareto classification.

## Evidence and boundaries

REPRO_STAGE339B.py and REPRO_STAGE339B_EXECUTED_STDOUT.txt give a fully
rational interval certificate, exact symbolic stationarity and tagged derivative
identities, and all the strict inequalities above. Executed twice with
byte-identical stdout. The analytical cone/Taylor argument supplies the
continuous quantifiers; finite exact computation certifies its explicit inputs.

Scientific scope: single-group auxiliary Bernoulli/BRC observer. Full
two-group global allocation, comparisons with parameter points outside the
certified radius, and independent mathematical review remain open. No native
CLAIM, Source Result, Driver admission or P000 X6/3D-slice/triadic/time/Cell
observer bridge is inferred. Next: Stage340-B global competitor search and
two-group allocation analysis.