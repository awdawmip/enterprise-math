# R749SNV — Exact vertical Walsh minimax phase and continuous transition at s=2/15

Date: 2026-11-14. Status: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED. Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Auxiliary 16-state Walsh source-observer result; not a native X6/V29/V39 event identification.

## 1. The vertical phase theorem

Use \(G=\mathbb F_2^4\), Walsh characters \(\chi_m(x)=(-1)^{\operatorname{popcount}(m\mathbin{\&}x)}\) and the compatible source laws

\[
\mu_{t,s,h,u,v,w,z}(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+h\chi_{15}(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)}{16}
\]

with sixteen nonnegative atom masses, retaining the known moment masks 3,12 and zero moments on 5,6,7,9,10,11,13,14. As before \(\rho(t,s)\) is unrestricted minimax total-variation prediction error and \(\rho^{\mathrm{cal}}(t,s)\) is the same minimax error when the predictor belongs to the compatible source fiber.

**Theorem R749SNV.** For every real \(s\in[0,2/15]\), with \(t=3/5\),

\[
\boxed{\rho(3/5,s)=\rho^{\mathrm{cal}}(3/5,s)=\frac{1-s}{2}.}
\]

The following calibrated center is optimal:

\[
q_s(x)=\frac{1+(3/5)\chi_3(x)+s\chi_{12}(x)+(3s-2/5)\chi_{15}(x)}{16}.
\]

At \(s=2/15\), the coefficient vanishes and the radius is \(13/30\). R749SNU gives radius \((3+t-s)/8\) immediately above this boundary on the segment \(t=3/5,\ 2/15\le s\le3/20\); at \(s=2/15\) the values and centers agree. Thus the already certified polygon joins the complete zero-calibration-penalty ray from \((3/5,0)\) to \((3/5,2/15)\) continuously. Its one-dimensional extension does not add area to the two-dimensional certified domain.

## 2. Direct diameter lower bound

For each \(0\le s\le2/15\), consider the two compatible sources

\[
\mu_\pm(x)=\mu_{3/5,s,-s,\,\pm(1-s),\,\pm(3/5+s),\,0,\,0}(x)
\]

using the same sign for \(u,v\). At both interval endpoints all 16 atom masses of each law are nonnegative; by affine dependence the laws are nonnegative throughout the interval. Because the primitive Walsh characters \(\chi_1,\chi_2\) supply all four sign combinations and \(1-s\ge3/5+s\) on this interval, the exact total variation between the two laws is

\[
\operatorname{TV}(\mu_+,\mu_-)=1-s.
\]

For every probability predictor \(q\), the triangle inequality gives

\[
\max\{\operatorname{TV}(\mu_+,q),\operatorname{TV}(\mu_-,q)\}
\ge\tfrac12\operatorname{TV}(\mu_+,\mu_-)
=\frac{1-s}{2}.
\]

This establishes the unrestricted minimax lower bound without any restriction on the predictor.

## 3. Exact complete upper bound

The displayed \(q_s\) has the retained Walsh moments. Its 16 atom masses are nonnegative at \(s=0,2/15\), hence throughout this interval. To prove its uniform worst-case radius, consider the bounded six-dimensional joint polytope in \((s,h,u,v,w,z)\) with \(t=3/5\). Scale \(y=15(s,h,u,v,w,z)\). The sixteen source inequalities are

\[
(\chi_{12}(x),\chi_{15}(x),\chi_1(x),\chi_2(x),\chi_4(x),\chi_8(x))\cdot y\ge -15-9\chi_3(x),\qquad x\in G.
\]

Add the two parameter inequalities \(y_s\ge0,\ -y_s\ge-2\). This gives eighteen exact integer halfspaces. The accompanying standard-library Fraction/Bareiss checker enumerates all \(\binom{18}{6}=18,564\) active bases, solves exactly, discards singular and infeasible intersections, deduplicates vertices, and checks

\[
\Delta=\operatorname{TV}(\mu_{3/5,s,h,u,v,w,z},q_s)-\frac{1-s}{2}
\]

at each vertex. Its complete output is:

| Check | Exact count |
|---|---:|
| Active bases | 18,564 |
| Nonsingular bases | 9,536 |
| Feasible bases | 560 |
| Distinct rational vertices | 76 |
| Vertices at the bound | 32 |
| Bound violations | **0** |
| Maximum excess | **0** |

The polytope is bounded because every source-law Walsh coefficient is bounded by one. The TV loss of an affine predictor minus an affine radius is convex over the joint polytope, so the maximum is attained at a vertex. Complete enumeration therefore proves the exact upper bound for *all real* \(s\in[0,2/15]\). Together with the diameter lower bound, this proves the theorem.

## 4. The exact phase transition and meaning

On the preceding R749SNU vertical segment, the radius is \((3+3/5-s)/8=(18/5-s)/8\); on the newly proved segment it is \((1-s)/2\). At \(s=2/15\), these equal \(13/30\), while their slopes in \(s\) differ: \(-1/2\) below and \(-1/8\) above. This is an exact breakpoint of the common minimax prediction error, *not* a strictly positive calibrated-versus-unrestricted penalty.

At \(s=0\), the formula gives \(\rho=\rho^{\mathrm{cal}}=1/2\) with feasible \(q_0\) and the source pair at total variation diameter 1. The theorem covers the closed interval including both endpoints.

## 5. Reproduction, provenance, open problem

Execute R749SNV_WALSH_VERTICAL_PHASE_EXACT_CHECK.py with standard Python and compare its deterministic stdout to R749SNV_WALSH_VERTICAL_PHASE_RESULTS.json. Its computations use exact integer elimination and fractions; assertions cover both extremal laws, pairwise TV distance, the calibrated center, complete joint vertices and the maximum excess.

R749SNS (PR #2346), R749SNT and R749SNU supply the adjacent two-dimensional region and original source pin. This is author-side proof awaiting independent mathematical review. No new native CLAIM, accepted Result, P000 modification, or claim about native signed-port dynamics is made.

**Next specific problem:** determine the two-dimensional continuation and sharp boundary of this piecewise phase around \((3/5,2/15)\). Distinguish loss of a particular predictor, an increase of the *shared* minimax risk and a genuinely positive penalty \(\rho^{\mathrm{cal}}-\rho\), using exact source/event witnesses.
