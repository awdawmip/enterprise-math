# R749SNQ — An exact two-parameter bridge for the repaired Walsh calibration center

Date: 2026-11-14. Frozen scientific input: \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Immediate dependencies: R749SNO–SNP, scientific PR #2339 @6bbb3912051c391307d2970f64fe17f9d9c20811. Status: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED. This is about the 16-state auxiliary Walsh observer; it does not assert a native X6, signed-Port, V29 or V39 observer correspondence.

## Exact theorem and new two-dimensional region

Let \(G=\mathbf F_2^4\), \(\chi_m(x)=(-1)^{\mathrm{popcount}(m\&x)}\). Preserve masks \(B=\{3,5,6,7,9,10,11,12,13,14\}\), with \(m_3=t\), \(m_{12}=s\), and the other eight retained Walsh coefficients zero. Let \(F(t,s)\) be the fiber of compatible probability measures. With \(\operatorname{TV}(\mu,q)=\frac12\sum_x|\mu(x)-q(x)|\), define

\[
\rho(t,s)=\min_{q\in\mathcal P(G)}\max_{\mu\in F(t,s)}\operatorname{TV}(\mu,q),
\quad
\rho^{\mathrm{cal}}(t,s)=\min_{q\in F(t,s)}\max_{\mu\in F(t,s)}\operatorname{TV}(\mu,q).
\]

Set the closed triangle
\[
K=\operatorname{conv}\left\{(7/10,3/20),(7/10,1/5),(4/5,1/5)\right\}
=\left\{(t,s):t\ge7/10,\ s\le1/5,\ 2s-t\ge-2/5\right\}.
\]

**Theorem. For every real \((t,s)\in K\)**,
\[
\boxed{\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=\frac{3+t-s}{8}.}
\]
A calibrated minimax center is
\[
\boxed{q_{t,s}(x)=\frac{1+tA(x)+sD(x)+\eta(t,s)AD(x)}{16},
\qquad \eta(t,s)=\frac32(s-\frac15),}
\]
where \(A=\chi_3,\ D=\chi_{12},\ AD=\chi_{15}\).

The triangle has area \(1/400\), intersects the earlier zero-gap triangle R749SNO along its top edge \(s=1/5,\ 7/10\le t\le4/5\), and has a two-dimensional portion outside R749SNO. Its edge \(t=7/10,\ 3/20\le s\le1/5\) agrees with the R749SNP second-piece repair. In particular, this extends the one-dimensional repaired center to a genuine open two-dimensional zero-gap region.

## Common seven-coefficient Walsh parameterization

Every source has the inverse Walsh form
\[
\mu_{t,s,h,u,v,w,z}(x)=
\frac{1+tA+sD+hAD+uU+vAU+wV+zDV}{16},
\]
with \(U=\chi_1,\ AU=\chi_2,\ V=\chi_4,\ DV=\chi_8\); the free five coordinates are exactly \(h,u,v,w,z\), constrained only by nonnegative atoms. The candidate \(q_{t,s}\) is normalized and preserves all ten retained moments. Its atoms are affine in \((t,s)\) and nonnegative at all three vertices of \(K\), therefore everywhere in \(K\).

## Unrestricted lower bound

Translations \(x\mapsto x\oplus3\) and \(x\mapsto x\oplus12\) preserve \(F(t,s)\), reverse the appropriate unretained Walsh directions, and keep \(1,A,D,AD\) invariant. Averaging a decoder over this translation group cannot increase its maximum TV loss; hence an unrestricted optimum may be sought among invariant decoders \(q\), all with Fourier support in \(1,A,D,AD\).

Consider
\[
W_{t,s}=\mu_{t,s,0,s-1,-t,-s,-s}.
\]
Its 16 atoms are nonnegative throughout the first-quadrant simplex \(t,s\ge0,\ t+s\le1\), as follows directly by grouping the atomic numerators into \(0\), \(2(1-t-s)\), \(2(1+t-s)\), \(4s\), \(2(1-t+s)\), \(2(1+t+s)\). Thus \(W_{t,s}\in F(t,s)\) on all of \(K\).

For \(E=\{3,5,7,9,11,13,14,15\}\), the sum of \(A,D,AD\) over \(E\) is zero, so invariant decoders satisfy \(q(E)=1/2\). Exact Walsh summation yields
\[
W_{t,s}(E)-\frac12=\frac{3+t-s}{8}.
\]
The variational characterization of TV gives \(\rho(t,s)\ge(3+t-s)/8\), hence also \(\rho^{\mathrm{cal}}(t,s)\ge(3+t-s)/8\).

## Complete exact upper certificate

Introduce scaled joint coordinates \(y=20(t,s,h,u,v,w,z)\). The compact full-dimensional joint source/parameter polytope has 19 integer halfspaces: 16 source-atom inequalities
\[
(A,D,AD,U,AU,V,DV)\cdot y\ge-20
\]
(one for each \(x\in G\)), and the three triangle inequalities
\[
y_t\ge14,\quad -y_s\ge-4,\quad -y_t+2y_s\ge-8.
\]
For instance \(t=18/25,\ s=9/50,\ h=u=v=w=z=0\) is strict interior.

Every vertex is determined by seven independent active facets. The supplied exact Python checker enumerates all \(\binom{19}{7}=50{,}388\) active sets and solves with integer Bareiss elimination and rational back-substitution. Measured certificate:

- active bases: 50,388
- nonsingular bases: 25,616
- feasible bases: 1,308
- distinct vertices: 88
- equality vertices: 26
- TV excess above \((3+t-s)/8\): maximum 0; violations 0.

For every vertex it verifies \(\mu,q\ge0\), total mass 1 and the exact inequality
\[
\Delta(y)=\operatorname{TV}(\mu_y,q_{t,s})-\frac{3+t-s}{8}\le0.
\]
Both the source measure and the proposed center are affine in \(y\), so \(\Delta\) is convex. Any point in the bounded joint polytope is a convex combination of its vertices; convexity proves the bound on **all real parameters** in \(K\). Together with the lower witness, this proves the theorem.

## Reproduction, evidence level, and next questions

Execute \`python research_notes/portable_direct/R749SNQ_BRIDGE_TRIANGLE_EXACT_CHECK.py\` and compare entire stdout to \`R749SNQ_BRIDGE_TRIANGLE_RESULTS.json\`. Only integer Bareiss arithmetic and Python Fraction rational comparisons are used. The source and input pin are recorded without changing the frozen scientific task.

The result belongs to the auxiliary Walsh model and is author-checked; independent mathematical review, task admission and source-faithful native X6/V29/V39 mapping remain distinct.

Next: characterize the maximal polyhedral region on which this affine \(\eta=\frac32(s-\frac15)\) center is optimal, including an exact exterior counterexample; then test an adjacent piecewise-affine correction to widen the zero-gap atlas.
