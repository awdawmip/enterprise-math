# R749STD — Four exact observations collide at cutoffs 602 and 604

2026-11-17. **AUTHOR_EXACT_NOT_REVIEWED**. Independent portable research in the frozen five-labeled-source auxiliary scalar model at awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. This is not native X6/BRC mathematical admission or a shared Task Result. Predecessor R749STC: exact four-read separation of the specific pair (73,77). R749SST: global eleven-read sufficiency.

## Theorem

Take five *separately labeled* nonnegative integer sources of weights (1,1,2,3,6) and mark the first unit-weight source. For n≥6 let

\[
\Omega_n=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le n-1\},\quad C_n=|\Omega_n|,\quad T_n=\sum_{k\in\Omega_n}k_1.
\]

Set \(S(n)=18n^4+54n^3-345n^2+2070n-16315\), and

\[
Y_n(e,d)=n^3\frac{T_n+e}{C_n+d}-\frac{S(n)}{108},\qquad
\mathcal O_n^{(m)}(e,d)=(Y_{n+6j}(e,d))_{j=0}^{m-1}.
\]

Each candidate holds its own real error pair fixed through all of its observations, and each pair lies in [-2,2]^2.

**There exist real \(e,d,E,D\in(-2,2)\) such that**

\[
\boxed{\mathcal O_{602}^{(4)}(e,d)=\mathcal O_{604}^{(4)}(E,D)}
\]

and, for those same states,

\[
\boxed{Y_{626}(e,d)-Y_{628}(E,D)>10^{-15}.}
\]

Consequently the unknown-cutoff global optimal exact horizon is now bounded by

\[
\boxed{5\le m_*\le11}.
\]

The upper bound is the independent R749SST eleven-read rational-function theorem; the present result is a new lower-bound witness. It strengthens R749STA's three-read collision family.

## Reduction to two cubic equations

For j=0,…,4 let a_j=602+6j, b_j=604+6j, and define

\[
t_j=C_{a_j}+d,\quad
\alpha_j=a_j^3/b_j^3,\quad
\beta_j=\frac{S(b_j)-S(a_j)}{108b_j^3},\quad
u_j=\alpha_j(T_{a_j}+e)+\beta_jt_j,\quad
w_j=C_{b_j}u_j-T_{b_j}t_j.
\]

Then \(x_j=(Y_{a_j}+S(b_j)/108)/b_j^3=u_j/t_j\), and \(v_j=x_jC_{b_j}-T_{b_j}=w_j/t_j\). The j-th equality says \(E-x_jD=v_j\). Define

\[
A=w_0t_1-w_1t_0,\quad B=u_1t_0-u_0t_1,\quad
E_N=w_0B+u_0A,\quad E_D=t_0B.
\]

When B>0 the first two equalities uniquely fix \(D=A/B\), \(E=E_N/E_D\). For j=2,3,4 define the exact-division polynomial

\[
P_j(e,d)=\frac{A(u_jt_0-u_0t_j)-(w_0t_j-w_jt_0)B}{t_0}.
\]

Direct exact polynomial division has zero remainder, with total degree 3 for each P_j. On the allowed rectangle where all t_j and B are positive, j-th equality for j≥2 is equivalent to P_j=0. Thus the first four observations match whenever P_2=P_3=0.

## Certified exact existence

Use rational center and radius

\[
e_c=\frac{7294566461180559224916}{10^{22}},\qquad
d_c=-\frac{14160257025121226420360}{10^{22}},\qquad
\rho=10^{-11}.
\]

Let \(\mathcal R=[e_c-\rho,e_c+\rho]\times[d_c-\rho,d_c+\rho]\), \(P=(P_2,P_3)^T\), \(J=DP(e_c,d_c)\), and \(G=J^{-1}P\). Exact rational arithmetic verifies det J≠0, along with the face signs

\[
G_1(e_c-\rho,d)<0<G_1(e_c+\rho,d),\quad
G_2(e,d_c-\rho)<0<G_2(e,d_c+\rho)
\]

for all d,e in their respective box ranges. **The Poincaré–Miranda theorem** therefore supplies an interior root \((e_*,d_*)\in\mathcal R\) satisfying P_2=P_3=0.

The companion executable verifies the signs via *strictly positive rational Bernstein coefficients* after affine mapping of each face to [0,1]. It likewise certifies across the whole box

\[
t_0>0,\ B>0,\quad 2B-A>0,\ 2B+A>0,\quad
2E_D-E_N>0,\ 2E_D+E_N>0.
\]

This proves \(-2<D<2\) and \(-2<E<2\). The rational center itself lies within the original error square, and the box radius preserves the source errors. Consequently the Poincaré–Miranda root gives admissible errors for **all four exact equalities**.

The fifth gap has the exact rational expression

\[
Y_{626}(e,d)-Y_{628}(E,D)
=\frac{628^3P_4(e,d)}{t_4(C_{628}B+A)}.
\]

Throughout \(\mathcal R\), the certificate proves \(P_4>0\), \(C_{628}B+A>0\), and

\[
10^{15}\cdot628^3P_4-t_4(C_{628}B+A)>0.
\]

This yields the strict fifth-read residual for the very same algebraic states.

## Certificate and evidence scope

Run Python 3 with SymPy: python R749STD_FOUR_READ_COLLISION_CERT.py. The code builds the five-source integer counts from the labeled generating function, verifies the exact division for P_2/P_3/P_4, constructs the rational inverse Jacobian, checks **88 strictly positive Bernstein coefficients over 13 polynomial certificates**, and writes a machine-readable result JSON. The four Poincaré–Miranda faces use 14 coefficients, and the parameter/fifth-gap constraints the other 74. Verification is exact symbolic rational arithmetic; the decimal diagnostics below do not participate in the proof.

Approximate algebraic root: \((e,d)\simeq(0.72945664611805592249,-1.41602570251212264204)\); reconstructed \((E,D)\simeq(1.96716018103247281458,-1.62590223191507148123)\). The observed fifth gap is about \(2.9827666952\times10^{-15}\), with proved strict lower bound \(10^{-15}\).

Exact counts include \((C_{602},T_{602})=(19230175073,1938941614326)\), \((C_{604},T_{604})=(19548563534,1977560635876)\). The code also independently checks earlier small cutoff counts, preventing source-weight conflation.

## Observer fidelity and continuation

The first four scalar observations merge two distinct source/cutoff states that have different fifth-read futures. An auxiliary BRC observer quotient must retain enough source and temporal provenance to distinguish these states if future fifth-read correctness is required. A native six-axis Cell/Link/Port transfer still needs its own typed embedding and operation-preservation proof; the present theorem makes no such transfer.

Next: test exact five-read aliases; improve the 11-read global upper bound; derive effective finite-range noise separation; seek a minimal source-preserving future-observer repair. No shared CLAIM, Result or independent Review is asserted.