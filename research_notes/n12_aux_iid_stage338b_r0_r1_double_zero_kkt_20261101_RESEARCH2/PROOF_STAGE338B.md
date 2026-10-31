# Stage338-B — exact Clarke/KKT certificate at the r0=r1=0 double zero

Date: 2026-11-01 Asia/Shanghai. Research classification: PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_SYMBOLIC_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Sources and type

Frozen GLOBAL_KNOWLEDGE_V1 canonical main 21a6d767034f342fbb64d3788339333776d5b3bd; Enterprise Math canonical main 0e46715ac981a244ea0b799b29dc4efaf410acc8; original P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Normative bootstrap/manual, ACTIVE worldview, TASK_RESEARCH and portable research protocol read. Scientific predecessor Stage337-B immutable EM commit 8db2fe68f2bbb9f9cf86afb4ea48f98f7eb41d20. This is a three-visit source-labelled Bernoulli/BRC AUXILIARY observer, not a native P000/X6 state or a native two-dimensional plane.

For k=0,1,2,3 let B_k(z)=z^k(1-z)^(3-k), w=(1,3,3,1), m=(61,21,9,9). Define
\[
r_k(x,y)=\frac{4B_k(x)+B_k(y)}5-\frac{m_k}{160},\quad
b(x,y)=\frac5{32}\sum_{k=0}^3w_k|r_k(x,y)|,
\]
\[
D_3(a,z)=\frac12\sum_{k=0}^3w_k|B_k(a)-B_k(z)|,\quad
c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]
The exact conservation law is r0+3r1+3r2+r3=0, and two source groups use P=b(q1)+b(q2), T=33/1024+c(q1)+c(q2). All 16 source-tag comparisons are retained.

## Theorem

Let I_x=[231083/10^6,231085/10^6] and I_y=[5554961/10^7,5555202/10^7]. There exists exactly ONE real q*=(x*,y*) in I_x×I_y satisfying r0(q*)=r1(q*)=0. At this point r2(q*)>0,r3(q*)<0. The four strict tagged sign strings, in k order, are -+++, --++, ++--, --++.

There is a positive lambda, alpha=1, and beta in (14/73,3/14) for which
\[
\boxed{0\in\nabla c(q_*)+\lambda\partial_Cb(q_*)}.
\]
For all directions d, D_dc(q*)+lambda D_db(q*)>=0; no direction strictly lowers both objectives at FIRST order. This is a first-order Clarke/KKT necessary condition, NOT a local/global Pareto proof, independent admission, or first global two-source transition.

## Proof of unique algebraic intersection

The r0 graph is uniquely defined by r0(x,Y0(x))=0 because r0,x=-(12/5)(1-x)^2<0 and r0,y=-(3/5)(1-y)^2<0. Its derivative is Y0'(x)=-4(1-x)^2/(1-Y0)^2<0.

At xL=231083/10^6 exact rational evaluations prove r0(xL,5555201/10^7)>0>r0(xL,5555202/10^7), and r1 is negative at BOTH indicated y endpoints. At xH=231085/10^6 rational evaluations prove r0(xH,5554961/10^7)>0>r0(xH,5554962/10^7), and r1 is positive at both corresponding y endpoints. Hence Y0(x)∈I_y throughout I_x.

Since r1,x=(4/5)(1-x)(1-3x)>0, r1,y=(1/5)(1-y)(1-3y)<0, and Y0'<0, the continuous function r1(x,Y0(x)) is strictly increasing with opposite endpoint signs. The root q* is unique. Strict r2>0 and r3<0 follow from exact endpoint evaluations r2(xL,min I_y)>0, r3(xH,max I_y)<0 and monotonicity of r2,r3 on the box. The 16 source-tag polynomial comparisons have constant strict signs on this tiny rational box by their derivative monotonicity intervals and exact rational endpoint evaluations.

## The complete two-cusp public observer and its supporting gradient

Since y<(1+sqrt(13))/8, the exact 16-tag audit gradient is
\[
\nabla c=(-p,q),\qquad p=\frac{(1-x)(189-183x)}{256}>0,\quad q=\frac{3y(1-y)}{64}>0.
\]
Near q*, r2>0 and r3<0. Conservation and binomial multiplicities imply exactly
\[
b=\frac5{16}[-r_3+(-r_0)_++3(-r_1)_+],\qquad z_+=\max(z,0).
\]
Thus its ENTIRE Clarke subdifferential is
\[
\partial_C b(q_*)=\left\{-\frac5{16}[\nabla r_3+\alpha\nabla r_0+3\beta\nabla r_1]:0\le\alpha,\beta\le1\right\}.
\]
Take alpha=1 and define
\[
N=-[q(r_{3,x}+r_{0,x})+p(r_{3,y}+r_{0,y})],\quad D=3(qr_{1,x}+pr_{1,y}),\quad\beta=N/D.
\]
Exact polynomial identities are
\[
N=-\frac9{1280}(122x^2y-61x^2-32xy^2-216xy+124x+16y^2+110y-63),
\]
\[
D=\frac9{1280}(x-1)(y-1)(135xy-61x-173y+63).
\]
Unrounded rational interval arithmetic on the WHOLE box certifies
\[
-15/1000<N<-14/1000,\qquad -73/1000<D<-70/1000,
\]
and hence 14/73<beta<15/70=3/14<1. The selected subgradient is
\[
g=-\frac5{16}(\nabla r_3+\nabla r_0+3\beta\nabla r_1)=(g_x,g_y).
\]
The same interval arithmetic gives g_x>0,g_y<0; exact symbolic substitution gives qg_x+pg_y=0. Define lambda=p/g_x>0. Then nabla c+lambda g=(-p,q)+lambda(g_x,g_y)=0.

At q*, the directional derivative of the maximum-of-smooth-branches b satisfies D_db=max{h·d:h in partial_C b}>=g·d. Therefore D_dc+lambda D_db >= (nabla c+lambda g)·d=0, proving the theorem for every real d without sampling.

## Execution, interpretation and next unit

The accompanying REPRO_STAGE338B.py performs exact Fraction interval arithmetic and SymPy identities, independently validating both algebraic root brackets, residual signs, 16 tag signs, polynomial N/D identities, strict beta interval, the selected gradient's sign, and exact supporting stationarity. It executed and reran with byte-identical stdout ending STAGE338B_R0_R1_DOUBLE_ZERO_KKT_EXACT_PASS.

The monotonic and directional argument supplies the continuous quantifiers; exact computation checks the load-bearing rational inequalities. This author result remains UNREVIEWED / NOT_ADMITTED. Native X6, three-dimensional slice third coordinate, triadic force closure, independent time, preserved branch/path operations and six-field Cell addressing require a separately proved observer bridge.

Stage339-B: determine second-order/local Pareto status of q*, test the critical tangent and level set b<=b(q*), compare with surviving r0/r1 arcs, two-source additive allocations and outside-rectangle competitors.