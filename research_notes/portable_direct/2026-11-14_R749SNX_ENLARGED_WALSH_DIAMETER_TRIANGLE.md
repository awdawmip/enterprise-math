# R749SNX — Enlarged exact two-parameter Walsh source-diameter phase

Date: 2026-11-14. Status: **AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED**. Scientific input remains **awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389**. Independent auxiliary 16-state Walsh source-observer statement.

## The exact enlarged triangle

Use \(G=\mathbb F_2^4\) and \(\chi_m(x)=(-1)^{\operatorname{popcount}(m\mathbin{\&}x)}\). As in R749SNW, define compatible source probabilities

\[
\mu(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+h\chi_{15}(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)}{16}
\]

for nonnegative atom masses. The retained Walsh moments are \(m_3=t,m_{12}=s\), and \(m_j=0\) for \(j=5,6,7,9,10,11,13,14\). Define unrestricted minimax radius \(\rho(t,s)\) by minimizing the worst-case total variation to the compatible source fiber over arbitrary probability laws; \(\rho^{\mathrm{cal}}\) minimizes over centers that themselves belong to the source fiber.

**Theorem R749SNX.** For every real pair in the closed triangle

\[
\mathcal D^+=\{(t,s):s\ge0,\ 2t+s\ge1,\ t+3s\le1\}
=\operatorname{conv}\{(2/5,1/5),(1/2,0),(1,0)\},
\]

\[
\boxed{\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=\frac{1-s}{2}.}
\]

The following calibrated prediction law achieves this radius:

\[
q_{t,s}(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+(t+3s-1)\chi_{15}(x)}{16}.
\]

The region has area \(1/20\), contains R749SNW's full triangle of area \(1/24\), and expands the certified domain by **20%**. The corner \((2/5,1/5)\) extends the two-dimensional source-diameter phase strictly into \(t<1/2\).

## Matching lower bound

For every \((t,s)\) in the triangle, define

\[
\mu_\pm(x)=\mu_{t,s,\,-s,\,\pm(1-s),\,\pm(t+s),\,0,\,0}(x)
\]

with simultaneous signs. All atom masses are nonnegative at the three triangle vertices; the proof checker verifies this in exact rationals. Since the masses are affine, these sources remain feasible throughout the triangle. The characters \(\chi_1,\chi_2\) have all four sign combinations equally often, hence

\[
\operatorname{TV}(\mu_+,\mu_-)=\max(1-s,t+s)=1-s.
\]

Here \(t+3s\le1\) implies \(t+2s\le1\), and all parameters in this triangle are nonnegative. By the total-variation triangle inequality every prediction law \(q\), calibrated or not, has worst-case error at least \((1-s)/2\).

## Complete exact upper-bound certificate

The displayed center \(q_{t,s}\) belongs to the source fiber at all three vertices, hence at each parameter point by affine interpolation. Let \(P\) be the joint seven-dimensional polytope in \((t,s,h,u,v,w,z)\) defined by sixteen source-mass nonnegativity inequalities plus the three displayed parameter inequalities. As each Walsh coefficient of a probability law has magnitude at most one, \(P\) is bounded.

Scale \(y=5(t,s,h,u,v,w,z)\). Its **19 integer halfspaces** are

\[
(\chi_3(x),\chi_{12}(x),\chi_{15}(x),\chi_1(x),\chi_2(x),\chi_4(x),\chi_8(x))\cdot y\ge -5,\quad x\in G,
\]

\[
2y_t+y_s\ge5,\qquad y_s\ge0,\qquad-y_t-3y_s\ge-5.
\]

The excess

\[
E=\operatorname{TV}(\mu_{t,s,h,u,v,w,z},q_{t,s})-\frac{1-s}{2}
\]

is convex on \(P\), so it is maximized at a vertex. The accompanying exact Python standard-library checker enumerates **all** \(\binom{19}{7}=50,388\) seven-constraint bases using integer Bareiss elimination and rational Fraction computations, discards the singular/infeasible bases, deduplicates rational vertices, and evaluates \(E\) at each vertex. Results:

| Item | Exact result |
|---|---:|
| Active bases | 50,388 |
| Nonsingular bases | 27,600 |
| Feasible bases | 4,636 |
| Distinct vertices | 80 |
| Tight vertices (excess zero) | 42 |
| Upper bound violations | **0** |
| Maximum excess | **0** |

Therefore \(\operatorname{TV}(\mu,q_{t,s})\le(1-s)/2\) for every source and **every real parameter** in \(\mathcal D^+\). The matching lower-bound diameter proves both minimax equalities.

## Evidence and next frontier

Run the standard-library script R749SNX_WALSH_SHARP_CENTER_TRIANGLE_EXACT_CHECK.py; stdout must equal the full R749SNX_WALSH_SHARP_CENTER_TRIANGLE_RESULTS.json. The checker verifies source and center positivity, source pair diameter and all 50,388 active bases. It uses no sampling and no floating-point assumptions. Reuse earlier R749SNV, R749SNU and R749SNW only at their proven model and parameter scopes.

The next question is the exact **maximal region of optimality of this explicit center**, and alternative centers beyond the two straight boundary lines \(2t+s=1\) and \(t+3s=1\). This is an auxiliary-model author result awaiting independent mathematical review, without asserting native X6/V29/V39 event admission or any shared TASK CLAIM.
