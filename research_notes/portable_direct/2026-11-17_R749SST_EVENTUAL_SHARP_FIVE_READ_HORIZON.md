# R749SST — Eventual sharp five-read cutoff separation; infinitely many exact four-read collisions

Date: 2026-11-17. Evidence **AUTHOR_EXACT_NOT_REVIEWED** (author's exact algebra/interval certificate PASS, independent review pending). Continuation of R749SSS, source PR #2589 @ 6e0afa8ad61aa326868018d6a3736e5981e99117; frozen scientific source awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Independent portable N2 scalar observer, not native X6 time, BRC Cell/Link/Port or a shared-task Result.

## Definition

Five distinct labeled source weights \(w=(1,1,2,3,6)\), with the first unit-weight source specially marked. For integer \(q\ge6\),

\[
\Omega_q=\{k\in\mathbb Z_{\ge0}^5:k_1+k_2+2k_3+3k_4+6k_5\le q-1\},\
C_q=|\Omega_q|,\quad T_q=\sum_{k\in\Omega_q}k_1.
\]

Let \(S(x)=18x^4+54x^3-345x^2+2070x-16315\) and

\[
Y_q(e,d)=q^3\frac{T_q+e}{C_q+d}-S(q)/108,\quad
\mathcal O_q^{(m)}(e,d)=(Y_{q+6j}(e,d))_{j=0}^{m-1}.
\]

The real errors \(e,d\in[-2,2]\) are fixed across the observations of one candidate, while different candidate cutoffs may independently select their errors.

## Main theorem (sharp eventual horizon)

**There exists an integer \(Q\)** such that every integer \(q\ge Q\) with \(q\equiv2\pmod6\), when compared to \(p=q+2\), has:

\[
\boxed{\mathcal O_q^{(4)}([-2,2]^2)\cap\mathcal O_{q+2}^{(4)}([-2,2]^2)\ne\varnothing}
\]

but

\[
\boxed{\mathcal O_q^{(5)}([-2,2]^2)\cap\mathcal O_{q+2}^{(5)}([-2,2]^2)=\varnothing.}
\]

Therefore the exact minimum guaranteed number of ordered six-step observations needed to distinguish these two candidate cutoffs is **five for all sufficiently large \(q\equiv2\pmod6\)**. This is a genuine infinite family of four-read exact collisions; it disproves a universal four-read exact-identifiability conjecture. The present proof is existential in \(Q\) and does **not** give a numerical value for the eventual threshold.

Additionally, a fully explicit exact-arithmetic contraction certificate proves a four-read collision already for **\(q=602\) versus \(q+2=604\)**. This finite example is an existence proof for a real solution strictly inside the permitted error square, not a floating-point near-collision.

## Exact algebraic jet and its nonsingular coefficient map

By the source-generating-function identities of R749SSR and R749SSS, on phases \(q\equiv2\) and \(q+2\equiv4\bmod6\), the count \(C\) and first marked-source moment \(T\) are exact degree-five/six polynomials; the denominator is nonzero for real errors in the allowed square and sufficiently large q. Thus the following rational function is analytic at infinity:

\[
F(x;\theta)=Y_x(e,d)-Y_{x+2}(E,D),\quad
\theta=(e,d,E,D)\in[-2,2]^4,
\]
where phase-specific quasi-polynomials are used for each polynomial extension. It has Laurent expansion

\[
F(x;\theta)=\sum_{k\ge1}c_k(\theta)x^{-k}.
\]

Its constant term vanishes identically, because both phases have the same limiting readout \(-25/36\). Exact rational polynomial division yields

\[
\begin{aligned}
c_1&=-\tfrac{80}{9}(-81D+81d-17),\\
c_2&=\tfrac{10}{9}(-18792D-3888E+17496d+3888e-967),\\
c_3&=-\tfrac{40}{81}(-854631D-297432E+691335d+262440e-16988),\\
c_4&=\tfrac{40}{27}(-4916862D-2260872E+3372840d+1701000e-18479),\\
c_5&=-\tfrac{80}{243}(-349991442D-194188104E+201756582d+123084360e+3235021).
\end{aligned}
\]

The exact Jacobian of the first four coefficients in the variable order \((e,d,E,D)\) is

\[
J_{\mathrm{jet}}=
\begin{pmatrix}
0&-720&0&720\\
4320&19440&-4320&-20880\\
-129600&-341400&146880&422040\\
2520000&4996800&-3349440&-7284240
\end{pmatrix}
\]

with

\[
\boxed{\det J_{\mathrm{jet}}=18794499932160000\ne0.}
\]

Consequently \(c_1=c_2=c_3=c_4=0\) has the unique real solution

\[
\boxed{
\theta_0=
\left(
\frac{69402481}{101966688},
-\frac{656227}{472068},
\frac{194725627}{101966688},
-\frac{755303}{472068}
\right)\in(-2,2)^4,
}
\]

while

\[
\boxed{c_5(\theta_0)=55842420440/39339>0.}
\]

## Infinite family of four-read collisions: exact analytic proof

Set \(u=1/q\) and \(z_j(u)=u/(1+6ju)\) for \(j=0,1,2,3,4\). Define \(H(z;\theta)=F(1/z;\theta)/z\), which extends real-analytically to \(z=0\), with Taylor series

\[
H(z;\theta)=c_1(\theta)+c_2(\theta)z+c_3(\theta)z^2+\cdots.
\]

For \(j=0,1,2,3\), let \(g_j(u,\theta)\) be the order-j **Newton divided difference** of \(H(\cdot;\theta)\) on the distinct nodes \(z_0(u),\dots,z_j(u)\). These functions extend real-analytically to \(u=0\): expand H in a convergent power series; divided differences of monomials are complete homogeneous symmetric polynomials of the nodes, and converge to the appropriate Taylor coefficient when all nodes coalesce at zero. In particular,

\[
(g_0,g_1,g_2,g_3)(0,\theta)=(c_1,c_2,c_3,c_4)(\theta).
\]

The nonsingular Jacobian at \((0,\theta_0)\) permits application of the **real-analytic implicit function theorem**. There exists \(\varepsilon>0\) and an analytic parameter function \(\theta(u)\), with \(\theta(0)=\theta_0\), satisfying \(g_0=g_1=g_2=g_3=0\) for all \(0<u<\varepsilon\). Because \(\theta_0\) lies in the interior of the allowed error cube, these parameters remain admissible for sufficiently small \(u\).

Vanishing of the Newton divided differences is equivalent (by the invertible triangular interpolation transformation on distinct nodes) to \(H(z_j(u);\theta(u))=0\) for all four j. Since every \(z_j(u)\ne0\), this is \(F(q+6j;\theta(1/q))=0\), i.e. exact equality of all four observations. Restrict to integers \(q\equiv2\bmod6\) large enough to use the exact quasi-polynomial model. This proves the first boxed assertion for every sufficiently large such q.

## Five-read eventual separation: exact compactness proof

Suppose conversely there were an unbounded sequence \(q_n\equiv2\bmod6\) having a five-read collision with arbitrary admissible, potentially q-dependent, parameters \(\theta_n\in[-2,2]^4\). By compactness, take a subsequence with \(\theta_n\to\theta_*\in[-2,2]^4\).

The five read equalities make all Newton divided differences of \(H(\cdot;\theta_n)\) of orders 0 through 4 vanish at the five nodes \(z_0(1/q_n),\ldots,z_4(1/q_n)\). Their continuity under coalescing nodes gives

\[
c_1(\theta_*)=c_2(\theta_*)=c_3(\theta_*)=c_4(\theta_*)=c_5(\theta_*)=0.
\]

The first four equations force \(\theta_*=\theta_0\), whereas the fifth has the strictly nonzero value displayed above. Contradiction. Thus such q cannot form an unbounded sequence. The five-read images are disjoint for all sufficiently large q in this residue class. Combining with the four-read collision proves the sharp eventual horizon five.

## Explicit finite witness: q=602 has a four-read real collision

Let \(q=602\), \(p=604\), and define the real four-equation system

\[
G_j(e,d,E,D)=Y_{602+6j}(e,d)-Y_{604+6j}(E,D),\quad j=0,1,2,3.
\]

Choose the **exact decimal rational center** \(a=(e,d,E,D)\), in that order:

\[
\begin{aligned}
e={}&0.729456646118055922491591897091774570952454989074974313514745,\\
d={}&-1.4160257025121226420362613056563861050326455137097596990824,\\
E={}&1.96716018103247281457798031508484711341332978475277300809199,\\
D={}&-1.6259022319150714812272708279189472411837831869354200078453.
\end{aligned}
\]

These terminating decimals are **exact rational inputs**, not an appeal to approximate root-finding. Put \(r=10^{-30}\). The entire closed max-norm cube \(B_\infty(a,r)\) is strictly inside \((-2,2)^4\).

Define \(J=DG(a)\), \(B=J^{-1}\). For each \(u=602+6j\), the Jacobian row is exactly

\[
\left(
\frac{u^3}{C_u+d},
-\frac{u^3(T_u+e)}{(C_u+d)^2},
-\frac{(u+2)^3}{C_{u+2}+D},
\frac{(u+2)^3(T_{u+2}+E)}{(C_{u+2}+D)^2}
\right).
\]

The companion exact rational certificate verifies

\[
\det J\ne0,\quad \|B\,G(a)\|_\infty<10^{-59},\quad
\|B\|_\infty<10^{13}.
\]

For any point in the permitted error cube, a rowwise absolute Hessian-entry sum is bounded by

\[
M_u=
\frac{2u^3}{(C_u-2)^2}+
\frac{2u^3(T_u+2)}{(C_u-2)^3}+
\frac{2(u+2)^3}{(C_{u+2}-2)^2}+
\frac{2(u+2)^3(T_{u+2}+2)}{(C_{u+2}-2)^3}.
\]

The exact certificate verifies \(M=\max_j M_{602+6j}<10^{-9}\). Consequently, on \(B_\infty(a,r)\),

\[
\|I-B\,DG(x)\|_\infty \le \|B\|_\infty M r <10^{-26}.
\]

The Newton preconditioned map \(x\mapsto x-BG(x)\) is a strict contraction mapping this closed ball into itself because

\[
\|BG(a)\|_\infty+r\,10^{-26}<r.
\]

The Banach fixed point theorem proves a unique exact zero of G in this ball, which is a permitted four-read collision. No floating-point equality is asserted or needed.

## Verification, interpretation, and remaining questions

The companion Python/SymPy certificate is exact throughout: full labeled-count recurrence to cutoff 630, exact mod-six polynomials, exact first-five Laurent coefficients and their Jacobian determinant, unique interior jet solution, strict fifth-coefficient inequality, rational center, rational 4x4 inverse, exact Hessian bound and Banach inequalities. Local run returned **PASS** on 2026-11-17. This is author validation; external mathematical review and any formal admission remain open.

This result shows an unexpectedly important distinction: four observations exactly separate some fixed small cutoff pairs (R749SSM/SSQ), yet fail to separate this entire sufficiently-large family. Five observations eventually repair exact identifiability for this specific family, while R749SSR and R749SSS still show that there is no cutoff-independent positive absolute-noise radius even with infinitely many reads. No conclusion is asserted for arbitrary cutoff pairs, integer-only calibration or native X6 heartbeat dynamics. Translating to BRC requires preservation of labeled-source identity, jointly shared errors, ordered future observations and task-typed native observers.

Next: find an **explicit numerical upper bound** for the five-read separation threshold and characterize the five-read minimax noise margin, potentially with q-dependent calibration. Determine whether other residue-pair families require more than five observations.