# PREFIX-767 / R6 — Exact gamma phase upper bound and an interior diagonal stationary point

Date: 2026-11-14. Frozen science: \`awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d\`.
Status: AUTHOR_ANALYTIC_AND_EXACT_INTEGER_CHECK / UNREVIEWED / NOT_ADMITTED.
Model: **external** 189-layer stopped-BRC and independent Gamma clock maximum, with no native X6 coordinate transfer.

## Definitions and exact matrix identities

Use the row-survival polynomials \(s_i(x)=\Pr(T_x>i)\), \(0\le i\le188\), reconstructed by the frozen killed-Pascal width predicate. Let \(K_{ij}=\binom{i+j}{i}/2^{i+j+1}\) and \(L_{ij}=(i+j+1)K_{ij}\). For \(Y(p,z)=\max(C_p,C_z)\), set \(\mu=\mathbb E Y\), \(\sigma^2=\mathrm{Var}(Y)\), \(V_q=q^2\sigma^2-q\mu\). These exact kernels and moments are established in PREFIX-760.

For \(0<u<1/2\), put \(s=s(u)\), \(d=s'(u)\), \(e=s''(u)\) and define

\[
m=2\mathbf1^\top s-s^\top Ks,\quad
v=\mathbf1^\top d-d^\top Ks,\quad
A=d^\top Kd,\quad B=d^\top Ld,\quad
D=B+2v^2-2mA.
\]

Direct differentiation of the exact first and second moments gives

\[
\partial_{pz}\mu(u,u)=-A,\qquad
\partial_{pz}\sigma^2(u,u)=-D,\qquad
\partial_{pz}V_q(u,u)=q(A-qD).
\]

Consequently, wherever \(D>0\), the diagonal local phase ratio is the rational function \(Q(u)=A(u)/D(u)\).

The derivative can be certified without numerical differentiation:

\[
A'=2e^\top Kd,\quad B'=2e^\top Ld,\quad
m'=2v,\quad
v'=\mathbf1^\top e-e^\top Ks-A,
\]

\[
D'=B'+4vv'-4vA-2mA',\qquad
\mathrm{sgn}\,Q'=\mathrm{sgn}(A'D-AD')
\quad(D>0).
\]

All statements are exact polynomial/rational identities on the external auxiliary model.

## Theorem 767.1 — A smaller exact finite-rectangle witness

For the rational square \(R=[3296/65536,3297/65536]^2\), the exact finite Gamma moments satisfy

\[
\Delta_R\mu<0,\quad \Delta_R\sigma^2<0,\quad
q_R:=\frac{\Delta_R\mu}{\Delta_R\sigma^2}
<\frac{285186}{10000000}=0.0285186.
\]

Thus the global supermodularity threshold \(q_c\) defined in PREFIX-763 obeys

\[
0<q_c\le q_R<0.0285186.
\]

Proof: Let \(H=65536^{188}\), \(T=2^{377}\), \(E=H^2T\), and let \(U_i(x)=Hs_i(x)\) be exact integers at the two rational endpoints. Set \(C(v,w)=\sum_{ij}v_iw_j\binom{i+j}{i}2^{376-i-j}\) and \(L^*(v,w)\) the same sum weighted by \(i+j+1\). Write \(d=U(b)-U(a)\). Then \(E\Delta\mu=-C(d,d)\); for the three means, their integer numerators on denominator \(E\) are
\(m_{aa}=2H T\sum U(a)-C(U(a),U(a))\),
\(m_{ab}=H T\sum(U(a)+U(b))-C(U(a),U(b))\),
\(m_{bb}=2H T\sum U(b)-C(U(b),U(b))\).
The exact variance difference on denominator \(E^2\) has numerator
\[
-\;E L^*(d,d)-(m_{bb}^2-2m_{ab}^2+m_{aa}^2).
\]
The attached Python checker verifies the two strict signs and the ratio bound by cross-multiplication of these integers. Approximate *displays* only: \(\Delta_R\mu=-6.7814805019063645\cdot10^{-7}\), \(\Delta_R\sigma^2=-2.3779156555107471\cdot10^{-5}\), \(q_R=0.028518591423503561\).

## Theorem 767.2 — An interior stationary candidate with a denominator-positive certificate

There exists \(u_*\in(251/5000,63/1250)=(0.0502,0.0504)\) for which \(Q'(u_*)=0\). Its existence does not assert uniqueness or global optimality.

For the whole closed interval \(I=[251/5000,252/5000]\), the exact integer interval enclosure in the attached checker gives

\[
A(u)<3156,\quad B(u)>242137,\quad 0<v(u),\ v(u)>225,\quad m(u)<50.
\]

Hence \(D(u)=B+2v^2-2mA>242137+2(225)^2-2(50)(3156)=27787>0\) on \(I\). The lower and upper survival/derivative interval bounds are obtained term by term from the nonnegative killed-Pascal monomials \(c_{n,k}u^k(1-u)^{n-k}\). For \(s'_n\), positive and negative derivative monomials are bounded separately. For \(0\le n<25\), \(s_n\equiv1\) and \(s'_n\equiv0\). All lower bounds on \(s'_n\) are verified nonnegative, so positive kernel bilinear forms preserve the stated enclosures.

At the rational endpoints, evaluate \(A'D-AD'\) using the exact derivative numerators \(Hs_i'\) and \(Hs_i''\). The attached program proves

\[
Q'(251/5000)<0,\qquad Q'(63/1250)>0.
\]

As \(Q\) is differentiable throughout \(I\), the intermediate value theorem gives the required zero of \(Q'\). The exact endpoint values, shown only for orientation, are \(Q(0.0502)\approx0.028518614542741932\) and \(Q(0.0504)\approx0.028518617361480442\). A separate floating-point finite-difference check agreed with the derivative signs, but is not used as proof.

## Reproduction, scope, and frontier

Run \`python PREFIX767_R6_DIAGONAL_PHASE_CERTIFY.py\` under Python 3 standard library; its expected terminal is \`ALL_CHECKS_PASS PREFIX767\`. It reconstructs all 189 rows, checks 9,529 nonzero survivor positions and a zero final row, and uses exact integers for every sign, interval and ratio bound. The computation is a complete finite certificate for the stated model, relying on the frozen width predicate. The analysis uses elementary Gamma maximum moment identities and differentiation of finite polynomials.

This is an author-level certificate for an **external scalar-parameter auxiliary**, not a native X6-time theorem or a new \(1/768\) Gamma comparator-cell exclusion. Independent review is pending. The next discriminating work is a certified interval isolation/uniqueness test for the stationary point in \(I\), or a native-comparator continuous-box sign enclosure using these same integer kernels.

Dependencies: PREFIX-760 exact moment kernels, PREFIX-762 positive mixed rectangle, PREFIX-763 definition of \(q_c\), PREFIX-766 square method.