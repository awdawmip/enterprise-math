# R749SNP — Exact calibrated-center repair of a Walsh nonconvex certificate

Date 2026-11-14. Direct continuation of R749SNO, on the unchanged frozen auxiliary Walsh model at \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Status: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED. This result does not assert native X6/V29/V39 future-observer transfer.

## Theorem: the true minimax radii remain equal throughout the repaired segment

Let \(G=\mathbf F_2^4\); retain the ten Walsh moment masks \(B=\{3,5,6,7,9,10,11,12,13,14\}\), with \(m_3=7/10,\ m_{12}=s\), the other eight retained moments zero. Use the same source fiber \(F(t,s)\), total variation and unrestricted/calibrated minimax definitions as R749SNO.

**For every real** \(1/10\le s\le1/5\),

\[
\boxed{\rho(\tfrac7{10},s)=\rho^{\mathrm{cal}}(\tfrac7{10},s)
=\frac{37}{80}-\frac{s}{8}.}
\]

A single piecewise-affine *calibrated* decoder proves the upper bound. Set \(A=\chi_3,D=\chi_{12},AD=\chi_{15}\) and

\[
\eta(s)=
\begin{cases}
-\frac32(s-\frac1{10}),&\frac1{10}\le s\le\frac3{20},\\
\phantom{-}\frac32(s-\frac15),&\frac3{20}\le s\le\frac15.
\end{cases}
\qquad
q_s(x)=\frac{1+\frac7{10}A(x)+sD(x)+\eta(s)AD(x)}{16}.
\]

Both pieces agree at \(s=3/20\), where \(\eta=-3/40\); at both exterior endpoints \(\eta=0\). All atoms of \(q_s\) are nonnegative at each endpoint of the two subsegments, hence throughout by affinity. The \(\chi_{15}\) coefficient is an unretained source degree of freedom, so introducing \(\eta(s)\) preserves all ten required Walsh moments.

## Uniform lower witness for unrestricted prediction

The source inverse transform is

\[
\mu(x)=\frac{1+\frac7{10}A+sD+hAD+uU+vAU+wV+zDV}{16},
\quad U=\chi_1,\ V=\chi_4.
\]

Translations by xor masks \(3,12\) preserve the fiber, and averaging any decoder over this finite group cannot increase its worst-case TV loss. Thus an unrestricted minimax center can be taken to depend only on \(1,A,D,AD\).

For \(s\in[1/10,1/5]\), the affine source \(W_s\) with free coefficients

\[
(h,u,v,w,z)=(0,s-1,-\tfrac7{10},-s,-s)
\]

has nonnegative atom masses and total one at \(s=1/10,1/5\); hence it is feasible for the entire interval. Let \(E=\{3,5,7,9,11,13,14,15\}\); the \(A,D,AD\) sums over \(E\) are zero, so every invariant center \(q\) satisfies \(q(E)=1/2\). Exact substitution gives

\[
W_s(E)-\tfrac12=\frac{37}{80}-\frac{s}{8}.
\]

The variational event inequality proves the same lower bound for every decoder, calibrated or not.

## Exhaustive exact upper verification on two all-real subintervals

For either subinterval \(I=[s_-,s_+]\), the joint six-variable source/parameter polytope has coordinates \((s,h,u,v,w,z)\) and 18 linear halfspaces: 16 atom nonnegativity inequalities plus \(s_-\le s\le s_+\). Scale all six coordinates by 20; the atom inequalities have integer normals \((D,AD,U,AU,V,DV)\) and right side \(-20(1+\tfrac7{10}A)\). The interval halfspaces also have integer coefficients.

This compact nonempty polytope is full-dimensional. All vertices occur among the intersections of six independent active facets. The supplied Python checker enumerates all \({18\choose6}=18{,}564\) bases **for each interval**, reconstructs exact rational vertices with Bareiss integer elimination, validates all 18 inequalities, and evaluates

\[
\Delta(s,h,u,v,w,z)
=\operatorname{TV}(\mu_{s,h,u,v,w,z},q_s)-\left(\frac{37}{80}-\frac{s}{8}\right).
\]

On each interval \(q_s\) depends affinely on \(s\), so \(\Delta\) is convex in all six coordinates. Its maximum occurs at a polytope vertex.

| Interval | Bases | Nonsingular | Feasible bases | Distinct vertices | Equality vertices | Violations |
|---|---:|---:|---:|---:|---:|---:|
| \([1/10,3/20]\) | 18,564 | 9,536 | 516 | 80 | 32 | 0 |
| \([3/20,1/5]\) | 18,564 | 9,536 | 536 | 74 | 22 | 0 |

The maximum excess is exactly zero in each enumeration. Thus \(\operatorname{TV}(\mu,q_s)\le37/80-s/8\) for **all real** parameters in both intervals and every compatible source. Together with the lower witness this completes the exact theorem.

## A correction of representation, not a contradiction

R749SNO exhibited that the simpler calibrated center \(q_0(x)=[1+\frac7{10}A(x)+sD(x)]/16\) violates the *affine-target upper certificate* at \(s=3/20\): a compatible source with \((h,u,v,w,z)=(-3/20,17/20,17/20,0,0)\) attains TV \(\frac{37}{80}\), exceeding the target \(\frac{71}{160}\) by \(\frac3{160}\). The new calibrated center sets \(\eta=-3/40\) there, and exact enumeration proves the true minimax radius is \(\frac{71}{160}\). Therefore the earlier obstruction is a limitation of the \(q_0\) representative, not a positive minimax calibration gap. This is a concrete repair through an unretained Walsh residual degree of freedom.

## Reproduction and next frontier

Execute \`python research_notes/portable_direct/R749SNP_CALIBRATED_CENTER_REPAIR_SEGMENT_EXACT_CHECK.py\` and compare its full JSON stdout to the companion \`R749SNP_CALIBRATED_CENTER_REPAIR_SEGMENT_RESULTS.json\`. It verifies both 18,564-combination enumerations, nonnegative endpoint laws, event-source lower bounds, piecewise continuity and the explicit midpoint diagnosis, using Python standard-library integers and Fraction.

The result is author-verified in an auxiliary observation model. Independent review and native provenance-preserving observer correspondence are separate.

Next: join the R749SNO two-parameter q0 triangle with the repaired \((t,s)=(7/10,[1/10,1/5])\) segment using a piecewise-affine \(\eta(t,s)\), then check the resulting *joint* source/parameter polytope rather than interpolating only endpoint fiber optima. Search for a true calibration gap outside this repaired union, with an explicit free-vs-calibrated dual witness if one occurs.
