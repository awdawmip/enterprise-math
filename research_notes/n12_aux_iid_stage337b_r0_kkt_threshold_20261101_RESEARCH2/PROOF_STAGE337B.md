# Stage337-B — unique exact first-order KKT transition on a low-error r0=0 BRC stratum

Date: 2026-11-01 (Asia/Shanghai). Scientific classification: PORTABLE_AUTHOR_THEOREM / EXACT_FRACTION_SYMBOLIC_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Fixed source provenance and model scope

GLOBAL_KNOWLEDGE_V1 canonical main@21a6d767034f342fbb64d3788339333776d5b3bd; Enterprise Math canonical main@0e46715ac981a244ea0b799b29dc4efaf410acc8; original P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Scientific predecessor: Stage336-B, Enterprise Math source commit b7937ab921ad44f8bc72bccaaffd293d1be79721. Normative entry files, P000, ACTIVE worldview, TASK_RESEARCH and portable research protocol were read from these fixed snapshots. Exact algebra below is independently derived from the displayed model.

This is a three-visit, source-labelled auxiliary Bernoulli/BRC observer; the two parameters are not an Enterprise native two-dimensional plane. Preserve the four binomial multiplicities and all 16 tagged comparisons. Positive probability is not signed amplitude. Native X6, triadic closure, three-dimensional slice third component, independent time and final six-field Cell address require separate future-operation preserving bridges.

For k=0,1,2,3 define

\[
B_k(z)=z^k(1-z)^{3-k},\quad w=(1,3,3,1),\quad m=(61,21,9,9),
\]
\[
r_k(x,y)={4B_k(x)+B_k(y)\over5}-{m_k\over160},\qquad
b(x,y)={5\over32}\sum_{k=0}^{3}w_k|r_k(x,y)|,
\]
\[
D_3(a,z)={1\over2}\sum_{k=0}^{3} w_k|B_k(a)-B_k(z)|,\quad
c(x,y)={63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)\over256}.
\]
The source-tagged two-group objective is P=b(q1)+b(q2) and T=33/1024+c(q1)+c(q2), and \(\sum_kw_kr_k=0\) exactly.

## Theorem (continuous real domain, unique certified KKT switching point)

Let \(I=[2311/10000,2354/10000]\) and let \(Y(x)\in(1/2,2/3)\) be the unique root of
\[
r_0(x,Y(x))=0\iff 4(1-x)^3+(1-Y(x))^3=61/32.
\]
For every x in I, one has
\[
r_1(x,Y)>0,\quad r_2(x,Y)>0,\quad r_3(x,Y)<0,\qquad b(x,Y)<61/10000.
\]
There is exactly one \(\xi\in I\) satisfying
\[
F(\xi,Y(\xi))=0,\qquad
F(x,y)=(1-x)(189-183x)(2y-1)-48(1-2x)y(1-y),
\]
and its exact isolating interval is
\[
\boxed{\frac{233494}{10^6}<\xi<\frac{233495}{10^6}}.
\]

For each x in I with x<xi, arbitrarily close q' strictly decreases BOTH b and c relative to q=(x,Y(x)). It is therefore excluded from the global single-source Pareto set and from any two-source Pareto solution containing it (the other source stays fixed).

For each x in I with x≥xi, there is λ>0 with \(0\in\nabla c(q)+\lambda\partial b(q)\); no direction has both strict negative first directional derivatives of b and c. This is precisely a first-order Clarke/KKT obstruction, not a proof of local, global, or second-order Pareto optimality. The point xi is not asserted to equal the first global two-source allocation transition.

## Proof A — exact graph, residual and all tagged signs

Since \(r_{0,x}=-12(1-x)^2/5<0\), \(r_{0,y}=-3(1-y)^2/5<0\), the root is unique, differentiable, and
\[
Y'(x)=-4(1-x)^2/(1-Y)^2<0.
\]
Direct exact rational checks establish
\[
r_0(2354/10000,1/2)>0,\quad r_0(2311/10000,2/3)<0,
\]
\[
r_0(2311/10000,5553/10000)>0>r_0(2311/10000,5554/10000),
\]
\[
r_0(2354/10000,5091/10000)>0>r_0(2354/10000,5092/10000).
\]
Hence \(5091/10000<Y(x)<5554/10000\) and x<Y throughout I. Since \(r_{1,x}=(4/5)(1-x)(1-3x)>0\), \(r_{1,y}=(1/5)(1-y)(1-3y)<0\), r1 increases along Y and its lower seed is
\[
r_1(2311/10000,5554/10000)=11849097/1250000000000>0.
\]
Also
\[
{d\over dx}r_3(x,Y)=\frac{12}{5}\frac{(x-Y)(x+Y-2xY)}{(1-Y)^2}<0,
\]
with upper seed \(r_3(2311/10000,5554/10000)=-15139150903/1250000000000<0\).
Both partial derivatives of r2 are positive throughout the rectangle, and
\(r_2(2311/10000,5091/10000)=2048411301/10^{12}>0\).

The all-16 comparison signs, in k order, are
\[
\begin{array}{c|c}
B_k(1/4)-B_k(x)&-+++\\
B_k(3/4)-B_k(x)&--++\\
B_k(1/4)-B_k(y)&++--\\
B_k(3/4)-B_k(y)&--++
\end{array}
\]
They hold everywhere in the displayed rational rectangle by monotonicity of the four explicit cubics and rational endpoint evaluations. Here y<5554/10000<23/40<(1+\sqrt{13})/8, so no source-tag cusp is crossed. Differentiating all tag contributions yields
\[
c_x=-p(x)=-{(1-x)(189-183x)\over256}<0,\qquad
c_y=q(y)={3y(1-y)\over64}>0.
\]

Along the zero curve, only r3 is negative, hence b=-5r3/16. Because r3 decreases along Y, b increases. At the right endpoint, Y>5091/10000 and r3 increases in y; consequently
\[
b(x,Y)\leq b(2354/10000,Y(2354/10000))
<-{5\over16}r_3(2354/10000,5091/10000)
={97122999973\over16000000000000}<{61\over10000}.
\]

## Proof B — both one-sided objective gradients and KKT

Near the zero stratum the strict signs r1,r2>0,r3<0 remain valid. Write
\[
b=\max\{b_+,b_-\},\quad b_+=-\frac5{16}r_3,\quad
b_-=-\frac5{16}(r_0+r_3),
\]
where b+ is the r0>0 formula and b- the r0<0 formula. Put
\[
A={3\over4}(1-2x)>0,\quad G={3\over16}(2y-1)>0,\quad
u={3\over4}x^2>0,\quad v={3\over16}y^2>0.
\]
Then \(\nabla b_+=(-u,-v),\ \nabla b_-=(A,-G),\ \nabla c=(-p,q)\), and
\[
\Delta=pG-Aq={3\over4096}F(x,y).
\]

When Δ>0 choose \(A/G<t<p/q\). For d=(1,t), a small positive displacement moves into r0<0 and
\[
D_db=A-Gt<0,\quad D_dc=-p+qt<0.
\]
This proves simultaneous strict dominance for the original absolute-value objectives.

When Δ≤0, \(p/q\le A/G\). Consider
\[
R(\theta)=\frac{-(1-\theta)u+\theta A}{(1-\theta)v+\theta G},\quad 0\le\theta\le1.
\]
It increases strictly (quotient-rule numerator \(Av+uG>0\)), and
\(R(0)<0<p/q\le R(1)=A/G\). Thus there exists unique \(\theta\in(0,1]\) with \(R(\theta)=p/q\). Let
\[
\lambda=\frac{q}{(1-\theta)v+\theta G}>0.
\]
Then
\[
\nabla c+\lambda[(1-\theta)\nabla b_++\theta\nabla b_-]=0.
\]
For every direction d, the derivative of b=max(b+,b-) is the larger branch derivative, so
\(D_dc+\lambda D_db\ge0\). Hence both directional derivatives cannot be strictly negative. At Δ=0, theta=1; at Δ<0, theta lies strictly between 0 and 1.

## Proof C — unique sign crossing and exact isolation

Let H(x)=F(x,Y(x)). On I and the above y rectangle,
\[
F_x=(-372+366x)(2y-1)+96y(1-y)\le24,
\]
\[
F_y=2(1-x)(189-183x)-48(1-2x)(1-2y)>200,
\qquad Y'(x)<-9.
\]
Therefore \(H'(x)<24-1800<0\), proving strict monotonicity on the COMPLETE continuous arc.

For \(x_L=233494/10^6\), exact r0 signs isolate \(Y(x_L)\in(528433/10^6,528434/10^6)\), and BOTH F endpoint values are positive. For \(x_H=233495/10^6\), exact r0 signs isolate \(Y(x_H)\in(528423/10^6,528424/10^6)\), and BOTH F endpoint values are negative. F is strictly increasing in y, so these signs enclose H(xL)>0>H(xH). The intermediate-value theorem and strict monotonicity prove a UNIQUE xi in the displayed rational interval, completing the theorem.

## Independent exact rational witness and reproducibility

With \(q_0=(233/1000,533717/10^6)\) and \(q_1=(2330001/10^7,1067441/2000000)\), all four residual sign tests give r0<0,r1>0,r2>0,r3<0 at both points, all 16 labelled comparisons remain in the fixed chamber, and direct exact original-objective evaluation yields
\[
b(q_1)-b(q_0)=-{6729387\over1600000000000000}<0,\qquad
c(q_1)-c(q_0)=-{773639338698561\over256000000000000000000000}<0.
\]
These rational points lie NEAR the algebraic boundary, not on it. They supply finite, exact, independently checkable evidence for its dominance side.

The reproducible Python Fraction/SymPy script validates conservation, all tagged signs, symbolic gradient laws, graph intervals, F determinant, exact critical rational isolation and the rational witness. Author execution and re-execution produced identical stdout ending STAGE337B_EXACT_R0_KKT_FIRST_ORDER_SWITCH_PASS. Exact rational checks support the load-bearing inequalities; continuous quantifiers follow from the displayed derivative and continuity arguments. This result awaits independent review and canonical Source admission.

## Next mathematical unit

Stage338-B: compute the complete one-sided Pareto/KKT cone at the r0=r1=0 intersection and along r1=0 through its tagged cusp; decide actual second-order/local Pareto on the r0-zero KKT half-arc; then compare uneven two-source budget allocations and outside-R competitors. The auxiliary result does not settle a native X6 claim or the first global eight-parameter Pareto transition.
