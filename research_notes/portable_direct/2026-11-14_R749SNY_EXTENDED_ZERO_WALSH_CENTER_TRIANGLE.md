# R749SNY — Extended zero-Walsh-center minimax triangle

Date: 2026-11-14. Status: **AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED**.
Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`.
Auxiliary 16-state Walsh source-observer model only. This note extends R749SNX (PR #2356), without changing P000 or a shared native task.

## 1. Statement

On \(G=(\mathbb Z/2)^4\), let \(\chi_m(x)=(-1)^{\operatorname{popcount}(m\mathbin{\&}x)}\).
The compatible source fiber consists of probability laws

\[
\mu_{t,s,h,u,v,w,z}(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+h\chi_{15}(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)}{16},
\]

where each of the 16 displayed atom masses is nonnegative. Known Walsh moments are \(m_3=t,m_{12}=s\); the eight other retained moments \(m_5,m_6,m_7,m_9,m_{10},m_{11},m_{13},m_{14}\) vanish. Let \(\rho(t,s)\) minimize worst-case total variation over **all probability predictions**, and let \(\rho^{\mathrm{cal}}(t,s)\) minimize over predictions within the compatible fiber.

**Theorem R749SNY.** For every real \((t,s)\) in the closed triangle

\[
\mathcal T_0=\{s\ge0,\quad t\ge2s,\quad t+3s\le1\}
=\operatorname{conv}\{(0,0),(1,0),(2/5,1/5)\},
\]

\[
\boxed{\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=\frac{1-s}{2}.}
\]

The optimal calibrated center uses **no unretained coefficients**:
\[
\boxed{q_{t,s}(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)}{16}}.
\]

The new triangle has area \(1/10\), **twice** the \(1/20\) area of R749SNX's previously certified triangle \(\mathcal D^+\); it includes all of \(\mathcal D^+\). At the vertices \((0,0),(1,0),(2/5,1/5)\), the center's minimum atom mass is respectively \(1/16,0,1/40\), hence it remains a probability law throughout \(\mathcal T_0\).

## 2. Universal lower bound by explicit diameter

For all \((t,s)\in\mathcal T_0\), define the pair
\[
\mu_\pm(x)=\mu_{t,s,\,-s,\,\pm(1-s),\,\pm(t+s),\,0,\,0}(x)
\]
with simultaneous signs. At the triangle's three vertices the atom masses of both laws are nonnegative; the exact checker verifies this, and affine interpolation proves feasibility throughout the entire real triangle.

For any two character values \(a=\chi_1(x)\), \(b=\chi_2(x)\), the four signs of \((a,b)\) occur equally often. Thus
\[
\operatorname{TV}(\mu_+,\mu_-)=\frac1{16}\sum_{x\in G}|(1-s)\chi_1(x)+(t+s)\chi_2(x)|
=\max(1-s,t+s)=1-s.
\]
The final equality uses \(t+3s\le1\), implying \(t+2s\le1\). By the triangle inequality every (even uncalibrated) prediction \(q\) has maximum source error at least
\[
\max(\operatorname{TV}(\mu_+,q),\operatorname{TV}(\mu_-,q))\ge\frac{1-s}{2}.
\]

## 3. Complete seven-dimensional rational certificate for the upper bound

Consider the joint polytope \(P\) with variables \((t,s,h,u,v,w,z)\), source-law nonnegative masses, and the three triangle halfspaces. It is bounded because the seven Walsh coefficients of every compatible probability law are moments in \([-1,1]\).

Use scaled variables \(y=5(t,s,h,u,v,w,z)\). The 19 exact integer halfspaces are:
\[
(\chi_3(x),\chi_{12}(x),\chi_{15}(x),\chi_1(x),\chi_2(x),\chi_4(x),\chi_8(x))\cdot y\ge -5\quad(x\in G),
\]
\[
y_s\ge0,\qquad y_t-2y_s\ge0,\qquad -y_t-3y_s\ge-5.
\]

The function \(E=\operatorname{TV}(\mu,q_{t,s})-(1-s)/2\) is convex over this polytope: both \(\mu,q\) are affine, TV is convex and the subtracted risk affine. Hence its maximum is attained at a vertex. The attached standard-library checker enumerates **every** \(\binom{19}{7}=50{,}388\) seven-constraint active set, solves each nonsingular exact integer matrix by fraction-free Bareiss elimination, filters infeasible intersections, deduplicates rational vertices and evaluates exact TV.

| Certified item | Count |
|---|---:|
| All seven-facet active bases | 50,388 |
| Nonsingular bases | 27,600 |
| Feasible bases (with degeneracy) | 4,804 |
| Distinct exact rational vertices | 82 |
| Vertices attaining the bound | 40 |
| Vertices violating upper bound | 0 |
| Exact maximum excess | 0 |

The 19 inequalities define a full-dimensional bounded polytope and the complete seven-active-basis enumeration covers its vertices. Therefore \(E\le0\) throughout \(P\), for **all real** \((t,s)\in\mathcal T_0\), and \(q_{t,s}\) attains the unrestricted diameter lower bound. This establishes both equalities.

## 4. Exact block-swap companion triangle

The coordinate permutation \((x_1,x_2,x_3,x_4)\mapsto(x_3,x_4,x_1,x_2)\) sends \(\chi_3\leftrightarrow\chi_{12}\), \(\chi_1,\chi_2\leftrightarrow\chi_4,\chi_8\), and fixes \(\chi_{15}\). It bijects the compatible source fibers, preserves total variation, and maps calibrated predictions to calibrated predictions. Applying this exact isometry to the proved theorem gives a second all-real parameter triangle

\[
\mathcal T_0^\ast=\{t\ge0,\quad s\ge2t,\quad s+3t\le1\}
=\operatorname{conv}\{(0,0),(0,1),(1/5,2/5)\},
\]

on which
\[
\boxed{\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=\frac{1-t}{2}}
\]
with the same unretained-zero center \(q_{t,s}\). The two proved triangles meet only at \((0,0)\), where both formulas give \(1/2\), and their combined area is \(1/5\). In particular, both entire nonnegative coordinate-axis segments have exact radius \(1/2\). This second triangle is a symmetry corollary: its proof inherits the complete R749SNY certificate under an explicit coordinate bijection, not a second independent enumeration.

## 5. Novelty, scope and reproduction

This is a strict parameter-region extension of R749SNX. It reuses that result's source-law family and diametral witness; the new ingredient is the simpler *zero* unretained-coefficient center, which remains optimal on a larger triangle that reaches the origin and the complete \(s=0\) edge. The current exact certificate says nothing about positive calibration gaps outside \(\mathcal T_0\).

The executable standard-library checker is `R749SNY_WALSH_ZERO_CENTER_EXTENDED_TRIANGLE_EXACT_CHECK.py` with deterministic JSON at `R749SNY_WALSH_ZERO_CENTER_EXTENDED_TRIANGLE_RESULTS.json`. Its assertions cover all 50,388 bases, source and center positivity, exact source-pair diameter, 82 distinct vertices and zero upper-bound excess. The check was run on 2026-11-14 using Python integer arithmetic and `fractions.Fraction`. Mathematical status remains author-proved/computationally checked, **NOT_REVIEWED**. Native X6/V29/V39 event transfer and formal shared TASK CLAIM are not asserted.

**Next question:** determine the sharp region of optimality of the zero-coefficient center (including whether its outer boundary has curved or further piecewise-linear chambers), and the first genuinely positive calibration gap beyond the certified union of the zero-center and repaired-center regions. In particular, evaluate exact parametric transitions across \(t=2s\) and \(t+3s=1\).
