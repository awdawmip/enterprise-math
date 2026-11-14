# R749SOF — Complete transverse Walsh minimax phases and exact zero-gap transition

**Scientific status:** Author-side proof with exact rational polytope certificates; \`NOT_REVIEWED\`.
**Date:** 2026-11-14.
**Immutable scientific input:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
**Immediate dependency:** R749SOE in this research branch; prior R749SNG and R749SOD. The result is within the *auxiliary 16-state Walsh source-observer model*. It is not a native X6/V29/V39 event correspondence.

## Exact theorem (entire real segment)

For \`G=F_2^4\`, write \`chi_m(k)=(-1)^popcount(m&k)\`, \`A=chi_3\`, \`B=chi_12\`, \`C=chi_15=AB\`. Consider the full probability fiber

\[
F_{t,s}=\left\{\mu_{t,s,h,u,v,w,z}(k)=
\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}
\ge0\quad (k=0,\ldots,15)\right\}.
\]

All eight additional retained moments vanish; these seven displayed Walsh coefficients give the complete compatible fiber. Define free and calibrated total-variation minimax radii by

\[
\rho(t,s)=\min_{q\in\Delta_{16}}\max_{\mu\in F_{t,s}}TV(q,\mu),
\qquad
\rho^{cal}(t,s)=\min_{q\in F_{t,s}}\max_{\mu\in F_{t,s}}TV(q,\mu).
\]

For **every real \(\frac12\le t\le1\)** with \(s=\frac12\), the exact values are

\[
\boxed{\rho(t,\tfrac12)=
\begin{cases}
\frac{13}{20}-\frac{t}{2},&\frac12\le t\le\frac35,\\[2pt]
\frac{2-t}{4},&\frac35\le t\le1;
\end{cases}}
\]

\[
\boxed{\rho^{cal}(t,\tfrac12)=
\begin{cases}
\frac9{22}-\frac6{11}(t-\frac12),&\frac12\le t\le\frac9{16},\\[2pt]
\frac35-\frac{2t}{5},&\frac9{16}\le t\le\frac23,\\[2pt]
\frac{2-t}{4},&\frac23\le t\le1.
\end{cases}}
\]

Thus the **precise positive-to-zero calibration transition on this transverse line is \(t=2/3\)**:

\[
\boxed{
g(t,\tfrac12)=\rho^{cal}-\rho=
\begin{cases}
\frac1{110}-\frac{t-\frac12}{22},&\frac12\le t\le\frac9{16},\\
\frac{2t-1}{20},&\frac9{16}\le t\le\frac35,\\
\frac{2-3t}{20},&\frac35\le t\le\frac23,\\
0,&\frac23\le t\le1.
\end{cases}}
\]

All formulas agree on their common endpoints; in particular the gap rises to \(\frac1{100}\) at \(t=3/5\), then falls to zero at \(t=2/3\).

## Explicit optimal predictors

All predictors have the form \(q_{a,b,c}=[1+aA+bB+cC]/16\). On the indicated real intervals choose

| Radius | Interval | \(a\) | \(b\) | \(c\) |
|---|---|---|---|---|
| free I | \([1/2,3/5]\) | \(1\) | \(1/5\) | \(1/5\) |
| free II | \([3/5,1]\) | \(1\) | \((1-t)/2\) | \((1-t)/2\) |
| calibrated I | \([1/2,9/16]\) | \(t\) | \(1/2\) | \((2+t-1/2)/11\) |
| calibrated II | \([9/16,2/3]\) | \(t\) | \(1/2\) | \(3/10-t/5\) |
| calibrated III | \([2/3,1]\) | \(t\) | \(1/2\) | \(t-1/2\) |

Every center is nonnegative on its whole interval. The calibrated centers possess the fixed retained Walsh moments \(t,1/2\), with all other eight retained moments zero, and therefore belong to the source fiber.

## Analytic universal lower bounds

Translation by \(3\) and by \(12\) within \(G\) preserves the fiber and flips the non-retained paired characters, so symmetrization reduces any minimizing predictor to \(q_{a,b,c}\), with \(a=t,b=1/2\) for calibrated prediction.

Put \(x=t-1/2\), so \(0\le x\le1/2\). Use two compatible source laws, specified by \((h,u,v,w,z)\):

\[
\mu_A:(1-x,-x,-x,0,0),\qquad
\mu_G:(x,-\tfrac12,-\tfrac12,x-\tfrac12,x-\tfrac12).
\]

All atoms of these laws are affine in \(x\), nonnegative at both \(x=0\) and \(x=1/2\), hence nonnegative throughout. Let \(L_E=q(E)-\mu(E)\) for an indicated event/source and note \(TV(q,\mu)\ge L_E\). For

\[
\begin{aligned}
E_A&=\{1,2,4,7,8,11,13,14\},\\
E_{GI}&=\{0,1,2,3,4,8,12\},\\
E_{GII}&=\{0,1,2,3,4,5,6,8,9,10,12\},\\
E_{GM}&=\{0,1,2,4,5,6,8,9,10,12\}
\end{aligned}
\]

with \(E_A\) using \(\mu_A\) and the other three using \(\mu_G\), exact Walsh sums give

\[
\begin{aligned}
L_A&=(1-x-c)/2,\\
L_{GI}&=(3a+3b-c)/16-x/2+3/16,\\
L_{GII}&=(-a-b+3c)/16-x/2+7/16,\\
L_{GM}&=(-a-b+c)/8-x/4+1/2.
\end{aligned}
\]

The nonnegative event convex combinations eliminate the unknown center parameters:

\[
\frac{L_A+L_{GI}+3L_{GII}}{5}=\frac25-\frac{x}{2}
\quad\text{(every free center);}
\]

\[
\frac{3L_A+8L_{GII}}{11}=\frac9{22}-\frac{6x}{11}
\quad\text{(every calibrated center);}
\]

\[
\frac{L_A+4L_{GM}}5=\frac25-\frac{2x}{5}
=\frac35-\frac{2t}{5}
\quad\text{(every calibrated center).}
\]

These establish the respective first free and first two calibrated phase lower bounds.

For the remaining phase, construct a symmetric pair of compatible source laws

\[
\mu_\pm:\quad(h,u,v,w,z)
=(t-\tfrac12,\ \pm\tfrac12,\ \pm\tfrac12,\ \pm(1-t),\ \pm(1-t)).
\]

Their atoms are nonnegative at \(t=1/2\) and \(t=1\) and affine in between. Direct atomwise sign inspection gives

\[
TV(\mu_+,\mu_-)=\frac{2-t}{2}.
\]

For every predictor \(q\), the TV triangle inequality forces
\(\max(TV(q,\mu_+),TV(q,\mu_-))\ge(2-t)/4\).
This gives the matching lower bound for free phase II and calibrated phase III, without assuming a particular prediction center. The pair is a true fiber diameter witness for the claimed exact radius.

## Exact upper bounds and complete finite certificate

On each of the five parameter intervals above, form the joint six-dimensional polytope in variables \((t,h,u,v,w,z)\), constrained by sixteen atom nonnegativity inequalities and two interval-endpoint inequalities. Every vertex has six independent active facets among 18. Exhausting \(\binom{18}{6}=18,564\) six-facet subsets is complete.

All proposed center probabilities and radii are affine in these variables within each interval. Therefore \(TV(q(t),\mu)-r(t)\) is convex; it achieves its maximum at a joint-polytope vertex. The attached exact checker \`R749SOF_COMPLETE_TRANSVERSE_PHASES_EXACT_CHECK.py\` reuses the author-verified bare integer Bareiss solver and Walsh source representation in \`R749SOE_TRANSVERSE_WALSH_EXACT_CHECK.py\`, using Python standard-library \`fractions.Fraction\`.

| Phase | Active subsets | Nonsingular bases | Feasible bases | Distinct vertices | Tight vertices | Largest excess |
|---|---:|---:|---:|---:|---:|---:|
| FREE I | 18,564 | 9,536 | 812 | 37 | 13 | 0 |
| FREE II | 18,564 | 9,536 | 724 | 24 | 12 | 0 |
| CAL I | 18,564 | 9,536 | 812 | 37 | 13 | 0 |
| CAL II | 18,564 | 9,536 | 392 | 40 | 16 | 0 |
| CAL III | 18,564 | 9,536 | 724 | 24 | 10 | 0 |

All 92,820 active-facet subsets were examined. Every feasible rational vertex satisfies both source and decoder nonnegativity, and every upper excess is **exactly zero or negative** (max 0), with **zero violations**. Completeness plus convexity gives the exact upper bounds for all real parameters on the full segment. Matching the analytic lower bounds proves the theorem.

**Reproduction:** place the R749SOE script and the R749SOF script together in \`research_notes/portable_direct/\`, run \`python3 R749SOF_COMPLETE_TRANSVERSE_PHASES_EXACT_CHECK.py\`, and compare stdout exactly with \`R749SOF_COMPLETE_TRANSVERSE_PHASES_RESULTS.json\`. No external packages or floating point methods participate in the proof-level certificate.

## Scope and next research front

This is an exact model-internal result on the frozen auxiliary 16-state Walsh fiber. Independent scientific review is pending; the native X6/V29/V39 relationship is not inferred. The newly established \(t=2/3,s=1/2\) boundary provides a concrete anchor for seeking the adjacent **two-dimensional zero/positive calibration-gap phase curve**, including local tangent(s), corners, and possible nonconvexity. Test nearby \(s\neq1/2\) with exact joint-parameter polytopes and parameter-dependent centers, preserving original Walsh/source observation semantics.