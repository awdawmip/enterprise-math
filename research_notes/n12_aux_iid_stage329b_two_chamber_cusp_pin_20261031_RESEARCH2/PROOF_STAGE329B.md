# Stage329-B — Exact cusp-pinned allocation on the inherited one-group BRC branch

Date: 2026-10-31. Status: PORTABLE_AUTHOR_PROOF / EXACT_FRACTION_BERNSTEIN_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is a theorem for a **restricted family** of the auxiliary 3-visit, 2-source Bernoulli BRC model, **not** the full eight-parameter global Pareto problem and not P000-native X6.

## Source and scope

Fixed GLOBAL_KNOWLEDGE_V1 canonical main: 6d641db765283606da81862be0e2eb4336d27878. Enterprise Math canonical main: a70253d1d635b19e3337c155e7b15c0b48863160. Inherited predecessor Stage328-B: fec395bea87ac0c9d464ac31bb9439c2e1bb2aef. Current P000 V5, ACTIVE worldview and portable research procedure were read. Research authority was not granted: owner listing CONTROL_QUOTA, native own session start STATIC_READONLY_SCOPE_DENIED (operation_sent=false). The inherited minimizer and earlier global theorems are author-only; no Source CLAIM, Result, or Driver acceptance.

The model is defined for k=0,1,2,3 by B_k(z)=z^k(1-z)^(3-k), p_k=(61,21,9,9)_k/160, and r_k(x,y)=(4/5)B_k(x)+(1/5)B_k(y)-p_k. Let
\[
b(x,y)=\frac5{32}\sum_{k=0}^3{3\choose k}|r_k(x,y)|,\qquad
D_3(a,z)=\frac12\sum_{k=0}^3{3\choose k}|B_k(a)-B_k(z)|,
\]
\[
c(x,y)=\frac{63D_3(1/4,x)+D_3(3/4,x)+9D_3(1/4,y)+7D_3(3/4,y)}{256}.
\]
The inherited two-source public and tagged errors are P=b(x,y)+b(x',y') and T=33/1024+c(x,y)+c(x',y'). The inherited root (x*,y*) satisfies r_0=r_1=0, with x* in (231083940855521/10^15,231083940855522/10^15) and y* in (555508857277/10^12,555508857278/10^12).

Let the increasing right branch be r_1(x,y)=0 from (x*,y*) through y=577/1000 (and not beyond). Parameterize this branch by s=b(x,y)-b(x*,y*), write \phi(s)=c(x(s),y(s)), and denote the endpoint budget by S. Define
\[
y_\dagger=\frac{1+\sqrt{13}}8,\quad r_1(x_\dagger,y_\dagger)=0,\quad
\varepsilon_\dagger=b(x_\dagger,y_\dagger)-b(x_*,y_*).
\]

## Theorem — exact restricted allocation transition

The following assertions are certified, conditional only on the inherited exact root specification and BRC reduction:

1. On either smooth side of the single tagged cusp, \phi is strictly concave and satisfies \(-100<\phi''<0\). The interval \([0,S]\) has only this cusp.
2. Exact bounds are
\[
0.002181407226<\varepsilon_\dagger<0.002181407228,\qquad
0.002325933314<S<0.002325933315,
\]
and \(0<S-\varepsilon_\dagger<3/20000\).
3. On the **restricted allocation family** with both groups constrained to this one branch, minimize \(\phi(t)+\phi(E-t)\) over \(0\le t\le E\), \(E\le S\). If \(0<E\le\varepsilon_\dagger\), the only minimizers are \(t=0,E\). If \(\varepsilon_\dagger<E\le S\), the only minimizers are \(t=E-\varepsilon_\dagger,\varepsilon_\dagger\). They strictly improve on both single-group endpoint allocations. At \(E=0\) there is one coincident endpoint.

This is a branch-constrained structural transition at the exact tagged cusp; it does NOT locate the first global optimizer transition of all eight real rate parameters. Other branches, off-curve competitors and other sign chambers remain open.

## Continuous proof and rational certificate

Let \(h(z)=(1-z)(1-3z)\), \(g(z)=z(2-3z)\). Along r_1=0 we have r_{1,x}=4h(x)/5>0 and r_{1,y}=h(y)/5<0, so y'(x)=-4h(x)/h(y)>0. Throughout the declared branch r_0<0, r_2>0 and r_3<0, and \(b=15r_2/16\), with \(db/dx>0\). Hence s is a strict coordinate. The signs of all sixteen tagged Bernoulli atom comparisons are fixed on the encompassing rectangle
\[
R=[231/1000,239/1000]\times[555/1000,577/1000]
\]
except the \((a=3/4,z=y,k=2)\) comparison, whose exact factorization is
\[
B_2(3/4)-B_2(y)=\frac{(4y-3)(16y^2-4y-3)}{64}.
\]
Consequently the tagged-cost partial derivatives in the two chambers are
\[
c_x=-\frac{(1-x)(189-183x)}{256},\quad
c_{y,-}=\frac{3y(1-y)}{64},\quad
c_{y,+}=c_{y,-}+\frac{21}{256}g(y).
\]
These identities were checked directly from all sixteen tagged atoms, not assumed from the preceding author note.

Put \(N=c_xh(y)-4c_yh(x)\) and \(D=g(x)h(y)-g(y)h(x)\). A polynomial identity gives
\[
D=(x-y)(6xy-3x-3y+2),\quad
\phi'=\frac43\,\frac ND.
\]
With \(L=\partial_xh(y)-4h(x)\partial_y\) acting on polynomials, define the polynomial
\[
K=(LN)D-N(LD).
\]
Direct differentiation of \(b'=3D/(4h(y))\) yields exactly
\[
\phi''=\frac{16K}{9D^3}.
\]
The executable verifier constructs polynomial coefficients in \(\mathbb Q[x,y]\), transforms each K into tensor-product Bernstein form on all of R, and checks **all 49 Bernstein coefficients** for each chamber. It reports:
\[
\begin{array}{c|cc}
&\min \operatorname{Bern}(K)&\max \operatorname{Bern}(K)\\
\text{left}&
214460253857742673770561/5120000000000000000000000&
54073624893068962608741/1024000000000000000000000\\
\text{right}&
1441514481498630220983249/25600000000000000000000000&
354513151477816187614389/5120000000000000000000000
\end{array}
\]
Both intervals lie strictly inside (1/25,7/100). Since \(6xy-3x-3y+2\ge187861/500000\) on R and \(y-x\ge 316/1000\), \(D<-1/9\) on R. Therefore \(0<K<7/100\) and \(-100<\phi''<0\) on both smooth portions. A Bernstein convex-hull bound covers every real point of the rectangle: this is **not** finite-grid interpolation.

The verifier uses isqrt to enclose \(\sqrt{13}\) by exact rationals, monotone bisection for x on r_1=0, and exact rational interval evaluation for \(\varepsilon_\dagger,S\), giving the above strict intervals. Direct rational interval differentiation yields
\[
-1.197918<\phi'(0+)<-1.197917,\qquad
-1.163997<\phi'(\varepsilon_\dagger+)<-1.163996,
\]
thus \(\phi'(\varepsilon_\dagger+)-\phi'(0+)>1/30\).

For E≤\varepsilon_\dagger, H_E(t)=\phi(t)+\phi(E-t) is strictly concave on [0,E], so its unique minima are t=0,E. For E>\varepsilon_\dagger, note \(E\le S<2\varepsilon_\dagger\) and consider t≤E/2 by symmetry. The only interior kink is \(t_0=E-\varepsilon_\dagger\). On each smooth interval [0,t_0] and [t_0,E/2], H is strictly concave. The latter interval's minimum is at t_0, because H(E/2)>H(t_0) by strict concavity and symmetry. On [0,t_0],
\[
H'(0+)=\phi'(0+)-\phi'(E)
\le-\frac1{30}+100(E-\varepsilon_\dagger)
<-\frac1{30}+100\frac3{20000}<0.
\]
Since H is concave there it decreases strictly, giving H(t_0)<H(0). The only symmetric minima are therefore t_0 and E-t_0=\varepsilon_\dagger. At E=\varepsilon_\dagger these coalesce with the two endpoints, as the first case states.

## Verification, scientific boundary, next unit

Executed exact Python stdlib Fraction script with 49+49 complete Bernstein coefficients and full continuous rectangular coverage, sixteen comparison polynomials, symbolic derivatives, exact algebraic-root bracketing and strict slope bounds. Final marker: STAGE329B_BERNSTEIN_TWO_CHAMBER_CUSP_PIN_RESTRICTED_SWITCH_EXACT_PASS. The complete executable and actual stdout are delivered alongside this proof. The script does not re-run upstream Stage307/316/324 global certificates. Mathematical conclusion is author proof within inherited model, unreviewed and not admitted. Native X6 paths, full 3D crystal-slice embedding, triadic closure, separately ordered time and registered six-field lossless Cell addresses remain independent bridge obligations.

Next Stage330-B: prove full-model off-curve competitor exclusion near \(\varepsilon_\dagger\), or construct an exact earlier full-eight-parameter competitor, explicitly covering all public/tagged sign chambers and alternative r_0/r_1 arms.
