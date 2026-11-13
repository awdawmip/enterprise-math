# R749SNE — Exact post-one-third diagonal Walsh minimax interval

Date: 2026-11-13 (Asia/Shanghai). Scientific origin: R749SND and earlier R749SMY–R749SNC. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Status: author-side proof plus exhaustive rational verification, not independent acceptance or a native X6/V29/V39 event mapping.

## Theorem

Use the source fibre and notation from R749SND: G=F_2^4, A=chi_3, D=chi_12, P=chi_1, Q=chi_4, with retained Walsh moments m_3=m_12=p and other eight B moments zero, B={3,5,6,7,9,10,11,12,13,14}. The compatible source laws are

\[
\mu_{p,h,u,v,w,z}=[1+p(A+D)+hAD+uP+vAP+wQ+zDQ]/16\ge0.
\]

**For every real p in [1/3,3/8]:**

\[
\boxed{\rho(p)=\frac{41-31p}{75},\qquad
\rho^{cal}(p)=\frac{2(1-p)}{3}.}
\]

Explicit optimal unrestricted and calibrated centres are

\[
q_p^{free}=\frac{1+\frac{18-13p}{25}(A+D)+\frac{62p-7}{75}AD}{16},
\quad
q_p^{cal}=\frac{1+p(A+D)+\frac{4p-1}{3}AD}{16}.
\]

Both are nonnegative throughout the interval. At p=1/3, this result meets the preceding R749SND exact values rho=92/225 and rho_cal=4/9. Thus the unrestricted radius decreases immediately above 1/3, with explicit witnesses and optimal centres.

## Symmetry and analytic lower bound

As in R749SNC/R749SND, the fibre is invariant under the flips of P,Q and the interchange (A,P)<->(D,Q). An unrestricted minimax centre can therefore be averaged to

\[
q_{\tau,\eta}=[1+\tau(A+D)+\eta AD]/16.
\]

Take three compatible source laws

\[
\mu_{AD}=[1+p(A+D)+AD]/16,
\]

\[
\mu_N=[1+p(A+D)+(2p-1)AD+(1-3p)(P+AP)+(p-1)(Q+DQ)]/16,
\]

\[
\mu_C=[1+p(A+D)+(1-2p)AD/3-(1+p)(P+AP+Q+DQ)/3]/16.
\]

Their sixteen source atoms are affine in p and are nonnegative at p=1/3 and p=3/8, therefore nonnegative at every interior real p. The original state index is x=0,...,15; chi_m(x)=(-1)^{popcount(m AND x)}.

For the fixed events
T_AD={1,2,4,7,8,11,13,14},
T_N={0,1,2,3,5,6,9,10},
T_C={0,1,2,3,4,8,12},
the signed TV event inequalities imply, for every feasible tau,eta,

\[
\begin{aligned}
TV(q,\mu_{AD})&\ge (1-\eta)/2=:L_{AD},\\
TV(q,\mu_N)&\ge (3-3p-\tau+\eta)/4=:L_N,\\
TV(q,\mu_C)&\ge (13-8p+18\tau-3\eta)/48=:L_C.
\end{aligned}
\]

As before, weights 1/5,12/25,8/25 are nonnegative and sum to one. They cancel both prediction parameters:

\[
\boxed{\tfrac15 L_{AD}+\tfrac{12}{25}L_N+\tfrac8{25}L_C=\tfrac{41-31p}{75}.}
\]

Consequently no unrestricted centre has smaller worst-case error.

For a calibrated centre (tau=p), the event
H={D=1,Q=-1} union {A=1,D=-1}
has mu_N(H)=(5-3p)/4 and q_{p,eta}(H)=(2+p-eta)/4. Hence

\[
TV(q,\mu_N)\ge(3-4p+\eta)/4,\qquad
TV(q,\mu_{AD})\ge (1-\eta)/2.
\]

The maximum is at least 2(1-p)/3; equality of these two affine lower bounds occurs at eta=(4p-1)/3.

## Complete finite upper certificate

The six-dimensional joint polytope (p,h,u,v,w,z) is specified by 16 source-positivity inequalities plus 3p>=1 and 8p<=3. It is bounded and full-dimensional (free coefficients zero and interior p yield strict inequalities). Every vertex is recovered by solving one of the C(18,6)=18,564 six-facet bases. The accompanying exact Bareiss/Fraction checker confirms:

- 18,564 six-facet subsets; 10,848 nonsingular;
- 592 feasible bases, yielding 78 distinct vertices;
- 37 vertices at p=1/3 and 41 at p=3/8;
- zero negative slack for both explicitly proposed centres at every vertex.

Both candidate distributions and bounds are affine in the six joint variables. TV(source,centre)-bound(p) is convex; its maximum on the bounded polytope occurs at a vertex. Thus the finite exact computation proves both upper bounds for all real p in the entire interval, completing the theorem.

## Continuation

After p=3/8 the current affine predictor no longer remains minimax. Numerically suggested further candidate breakpoints near 23/57 require separate exact proofs and are not included as established results here. Native attribution, independent review and shared Task CLAIM remain separate.