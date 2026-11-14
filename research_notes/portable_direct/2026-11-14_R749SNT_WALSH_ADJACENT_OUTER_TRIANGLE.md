# R749SNT — Exact outer wedge extending the Walsh zero-calibration polygon

Date: 2026-11-14. Evidence: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED.
Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessor: R749SNS, PR #2346, head 847b3617e5e61f862bf31883e998d23825588e53.
Scope: 16-state auxiliary Walsh source observer, not a native X6/V29/V39 event correspondence. P000, Task CLAIM and Result/Review records are unchanged.

## 1. Statement, domain, explicit minimax center

On the group \(G=\mathbb F_2^4\), define \(\chi_m(x)=(-1)^{\operatorname{popcount}(m\mathbin{\&}x)}\).
The known Walsh moments have masks \(3\) and \(12\), with values \(t\) and \(s\); the other eight retained masks \(5,6,7,9,10,11,13,14\) have moment zero. The compatible source laws are

\[
\mu_{t,s,h,u,v,w,z}(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+h\chi_{15}(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)}{16},
\]

subject to nonnegativity of all sixteen atom probabilities. Write \(\mathcal F(t,s)\) for the resulting probability fiber and \(\mathrm{TV}(\mu,q)=\frac12\sum_x|\mu(x)-q(x)|\). Let

\[
\rho(t,s)=\min_{q\in\Delta(G)}\max_{\mu\in\mathcal F(t,s)}\mathrm{TV}(\mu,q),\qquad
\rho^{\mathrm{cal}}(t,s)=\min_{q\in\mathcal F(t,s)}\max_{\mu\in\mathcal F(t,s)}\mathrm{TV}(\mu,q).
\]

Set \(A=(7/10,1/10)\), \(C=(3/5,7/40)\), \(X=(3/5,3/20)\), and

\[
\mathcal W=\operatorname{conv}\{A,C,X\}
=\{(t,s):\,t\ge3/5,\quad3t+4s\le5/2,\quad t+2s\ge9/10\}.
\]

**Theorem R749SNT.** For every real \((t,s)\in\mathcal W\),

\[
\boxed{\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=\frac{3+t-s}{8}.}
\]

An exact optimal calibrated prediction center is

\[
q_{t,s}(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+\eta(t,s)\chi_{15}(x)}{16},\qquad
\boxed{\eta(t,s)=\frac{31}{40}-\frac{3t}{4}-\frac{5s}{2}.}
\]

On the common side \(AC\), defined by \(3t+4s=5/2\), the new formula reduces identically to the old SNS P1 coefficient \(\eta_{\mathrm{old}}=3/20-3s/2\). The resulting piecewise optimal center is continuous. The new triangle lies outside the predecessor polygon except for the common edge and has area \(1/800\). Adding it to the previously certified area \(43/800\) yields \(44/800=11/200\), an increase of \(1/43\) relative to the previous domain.

## 2. Unrestricted lower bound

XOR translations by 3 and 12 preserve the source fiber. Averaging an arbitrary predictor over the four-element translation subgroup cannot increase its worst-case total variation risk. All averaged predictors lie in the Walsh span of \(1,\chi_3,\chi_{12},\chi_{15}\). The event

\[
S=\{3,5,7,9,11,13,14,15\}
\]

has zero sum for each of the three nonconstant characters, so every such invariant predictor has \(q(S)=1/2\).

The affine source

\[
W_{t,s}=\mu_{t,s,0,s-1,-t,-s,-s}
\]

is nonnegative at each of A, C, X; affinity makes it compatible throughout the triangle. Exact evaluation gives

\[
W_{t,s}(S)-1/2=(3+t-s)/8.
\]

The event variational inequality therefore yields \(\rho(t,s)\ge(3+t-s)/8\) and the same lower bound for \(\rho^{\mathrm{cal}}\).

## 3. Upper bound for all real parameters: complete joint-vertex certificate

The proposed center has the prescribed retained Walsh moments. Its sixteen probabilities are nonnegative at A, C, X, so they are nonnegative throughout the entire triangle. It is an admissible calibrated predictor.

The joint source-parameter polytope, in the seven variables \((t,s,h,u,v,w,z)\), has 16 source-atom nonnegativity inequalities and the three parameter halfspaces. After scaling \(y=40(t,s,h,u,v,w,z)\), the additional integer inequalities are

\[
(1,0,0,0,0,0,0)\cdot y\ge24,\qquad
(-3,-4,0,0,0,0,0)\cdot y\ge-100,\qquad
(1,2,0,0,0,0,0)\cdot y\ge36.
\]

Enumerate all seven-element subsets of 19 constraints, solve the active equalities using exact integer Bareiss elimination, discard singular or infeasible intersections, and deduplicate the rational vertices. At each feasible vertex compute

\[
\Delta=\mathrm{TV}(\mu_{t,s,h,u,v,w,z},q_{t,s})-(3+t-s)/8.
\]

The exact Python standard-library certificate reports:

| Quantity | Value |
|---|---:|
| Seven-facet combinations | 50,388 |
| Nonsingular bases | 27,600 |
| Feasible bases | 648 |
| Distinct rational vertices | 132 |
| Tight vertices | 38 |
| Vertices with \(\Delta>0\) | 0 |
| Maximum \(\Delta\) | 0 |

This joint polytope is compact: its source distributions are probabilities and the inverse Walsh coefficients are bounded, while \((t,s)\) ranges in a bounded triangle. Every vertex is identified by seven independent active constraints. The function \(\Delta\) is convex in the seven joint parameters (absolute values of affine quantities minus an affine target). Thus its maximum over this polytope occurs at a vertex. The exact exhaustive computation proves the upper bound for *all real* points of \(\mathcal W\), not merely rational samples. Combined with Section 2, this proves the theorem.

## 4. A precise failure of the preceding center

At \(X=(3/5,3/20)\), the unchanged extension of SNS's P1 center gives \(\eta_{\mathrm{old}}=-3/40\). Choose the compatible source coefficients

\[
(h,u,v,w,z)=(0,17/20,3/5,-3/20,-3/20).
\]

All atoms of the source and old center are nonnegative, but exact evaluation gives

\[
\mathrm{TV}(\mu,q_{\mathrm{old}})
=\frac{277}{640}
=\underbrace{\frac{69}{160}}_{(3+t-s)/8}+\frac1{640}.
\]

The new coefficient \(\eta_{\mathrm{new}}(X)=-1/20\) attains \(69/160\) uniformly over the fiber, as Section 3 establishes. This is an exact decoder-specific obstruction to naive extension, and a constructive repair retaining zero calibration penalty.

## 5. Reproduction, research boundary and continuation

Run the accompanying R749SNT_WALSH_NEW_WEDGE_EXACT_CHECK.py with standard Python and compare the full deterministic stdout to R749SNT_WALSH_NEW_WEDGE_RESULTS.json. The program asserts exact source and decoder nonnegativity, the event lower bound, 50,388 complete active-basis combinations, all 132 vertex comparisons, the shared-edge identity, rational area and the counterexample. There are no floating-point proof steps.

This proof is author-side, not independently reviewed. The preceding frozen scientific source, native X6/P000 model and existing task publications remain unchanged.

**Next mathematical unit:** track the piecewise-optimal center along the new exposed edges \(t+2s=9/10\) and \(t=3/5\), determine the next breakpoint, and distinguish center-specific failure from a genuine strictly positive minimax calibration gap. A signed-Port/provenance-preserving mapping to native X6/V29/V39 observations remains an independent research obligation.
