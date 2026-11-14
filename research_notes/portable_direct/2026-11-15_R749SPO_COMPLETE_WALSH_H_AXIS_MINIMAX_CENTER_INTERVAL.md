# R749SPO — Complete exact interval of calibrated minimax Walsh centers on the SPN wedge

**Status:** AUTHOR_EXACT_NOT_REVIEWED. **Scientific pin:** awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. **Predecessor:** R749SPN, https://github.com/awdawmip/enterprise-math/pull/2449. **Date:** 2026-11-15. **Scope:** frozen auxiliary 16-atom Walsh fiber, with no native X6/V29/V39 identification.

## 1. Precise problem and result

Retain the complete signed/provenance Walsh coordinates in the frozen source family

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16},\quad
\chi_m(k)=(-1)^{\operatorname{popcount}(k\mathbin{\&}m)}.
\]

Write F(t,s) for the nonnegative probability laws with fixed t,s and all five free coefficients; TV denotes total variation. The unconstrained and calibrated Chebyshev radii are respectively rho(t,s) and rho_cal(t,s). R749SPN proved that for every real (t,s) in

\[
S=\{t\ge0,\ s\ge t,\ 4t+s\le1\},
\]

the common radius is (1-t)/2, achieved by the calibrated center q_t=p_{t,s,t,0,0,0,0}.

**Theorem (complete h-axis characterization).** At every real (t,s) in S, restrict candidate centers to the signed Walsh h-axis

\[
q_h=p_{t,s,h,0,0,0,0}.
\]

Define

\[
L(t,s)=\max\{2t-s,\ 3t+s-1\},\qquad
U(t,s)=\min\{s,\ 1-3t-s\}.
\]

Then

\[
\boxed{q_h\text{ is a calibrated minimax center }\iff L(t,s)\le h\le U(t,s).}
\]

Throughout this interval the exact maximal risk is (1-t)/2, and rho=rho_cal=(1-t)/2. The interval is nonempty on S and is in general larger than the formerly established [0,t] subfamily on S intersect the SPK wedge. For example, (t,s)=(1/10,1/2) has the **complete h-axis interval [-1/5,1/5]**, with infinitely many different optimal calibrated centers. On the diagonal t=s=1/5 it collapses to h=1/5. The theorem describes all centers of the stated five-free-coefficient family **within the h-axis**, not every minimax center in the full 16-law simplex.

## 2. Exact necessary inequalities, with three actual compatible source witnesses

The four-branch BRC nonnegativity criterion remains

\[
M_{ab}=1+at+bs+abh,\quad U_a=u+av,\quad V_b=w+bz,\quad
M_{ab}\ge |U_a|+|V_b|\quad(a,b\in\{\pm1\}).
\]

This is a provenance-preserving grouping of all sixteen atoms, not a quotient deleting the source branches. For t,s in S, any q_h in F(t,s) has \(t+s-1\le h\le1+t-s\). Set R=(1-t)/2.

**Upper bounds.** Put m=t+s and choose the compatible source law
\(P_H=p_{t,s,m-1,-m,-m,0,0}\).
All four BRC conditions hold for t+s<=1. With b=1-m+h>=0, exact summation over sixteen atoms gives

\[
TV(P_H,q_h)=\frac{b+\max(b,2m)}4.
\]

Since the minimax risk cannot exceed R, necessarily \(b\le1-t\) and \(b+2m\le2(1-t)\), giving \(h\le s\) and \(h\le1-3t-s\).

**First lower bound.** Put d=s-t and choose the compatible law
\(P_{L1}=p_{t,s,1+t-s,t-s,s-t,0,0}\).
Its BRC block masses make it nonnegative on S. With a=1+t-s-h>=0,

\[
TV(P_{L1},q_h)=\frac{a+\max(a,2d)}4\ge\frac a2.
\]

Risk <=R therefore gives \(h\ge2t-s\).

**Second lower bound.** Choose
\(P_{L2}=p_{t,s,0,-t,-t,t-1,-s}\).
All four BRC inequalities are equalities for t+s<=1, hence this is a complete compatible source law. For k=0,...,15 set the fixed sign vector

\[
\sigma=(-1,-1,-1,-1,-1,+1,+1,+1,-1,-1,-1,-1,+1,+1,+1,+1).
\]

Since TV is one-half the sum of absolute atomic differences, for **every real h**,

\[
TV(P_{L2},q_h)\ge
\frac1{32}\sum_{k=0}^{15}\sigma_k
\left[-h\chi_{15}(k)-t\chi_1(k)-t\chi_2(k)+(t-1)\chi_4(k)-s\chi_8(k)\right].
\]

The sign sum is exactly

\[
\frac{7-5t+s-h}{16}
=R+\frac{3t+s-1-h}{16}.
\]

Therefore risk <= R forces \(h\ge3t+s-1\). Combined, these three source laws prove the full necessary interval. No optimization solver or interpolated numerical guess is used in this half of the proof.

## 3. Exact sufficient upper bound on four chambers

For the reverse implication, it is enough to prove that both endpoint centers q_L and q_U are valid calibrated centers with risk at most R; their whole interval follows from convexity of the source fiber and TV in the center.

The endpoint functions are affine separately on the following four polygonal subwedges of S:

| Chamber | Additional facet | Candidate h(t,s) |
| --- | --- | --- |
| lower-left | t+2s<=1 | 2t-s |
| lower-right | t+2s>=1 | 3t+s-1 |
| upper-left | 3t+2s<=1 | s |
| upper-right | 3t+2s>=1 | 1-3t-s |

For each chamber the complete **seven-dimensional joint parameter-source polytope** consists of sixteen atomic nonnegativity constraints, the three defining facets of S, and the single additional chamber facet. It is bounded, full-dimensional, and rational. Its 20 rows yield exactly C(20,7)=77,520 possible seven-active-constraint bases. All feasible vertices are enumerated by integer Bareiss elimination and Python Fraction arithmetic, including degeneracies and duplicate bases. Because the source law and each chamber center are affine in all seven joint coordinates, the function

\[
E(t,s,h_{\rm source},u,v,w,z)=TV(p_{t,s,h_{\rm source},u,v,w,z},q_{h(t,s)})-R(t)
\]

is convex on that polytope. An upper bound at every vertex establishes E<=0 at every real point.

The actually executed exact verifier reports:

| Chamber | Nonsingular bases | Feasible bases with repetitions | Different rational vertices | E=0 vertices | Max exact E |
| --- | ---: | ---: | ---: | ---: | ---: |
| lower-left | 41,456 | 1,540 | 155 | 87 | 0 |
| lower-right | 41,456 | 4,636 | 80 | 34 | 0 |
| upper-left | 41,504 | 1,704 | 107 | 67 | 0 |
| upper-right | 41,504 | 5,032 | 87 | 61 | 0 |
| **Total** | **165,920** | **12,912** | **429 counted per chamber** | **249** | **0** |

The program explicitly checks probability nonnegativity and unit mass at every candidate center and source vertex, and asserts maximal excess exactly zero. Convexity then proves feasibility and the TV bound for the full continuous parameter domains of the chambers, and convex combination handles intermediate h. The R749SPN explicit compatible source pair with TV(P+,P-)=1-t supplies the matching universal lower bound R.

**Conclusion:** the exact necessary interval and the exact sufficient interval agree. This characterizes the h-axis slice of the complete optimal-center polytope for every real (t,s) in S.

## 4. Reproducibility, evidence boundary, next question

Files accompanying this report:

- R749SPO_WALSH_H_AXIS_INTERVAL_CERT.py — self-contained standard-library checker enumerating all 310,080 candidate seven-facet bases across four chambers.
- R749SPO_WALSH_H_AXIS_INTERVAL_RESULTS.json — observed results (PASS), with per-chamber counts and exact excess.
- Run: python3 R749SPO_WALSH_H_AXIS_INTERVAL_CERT.py > R749SPO_WALSH_H_AXIS_INTERVAL_RESULTS.json.

The paper's witness identities can also be verified by direct expansion of the 16-entry Walsh formula. All reported computations use exact integer/rational arithmetic; no floating-point tolerances are involved. The certificate supports the auxiliary model and this h-axis characterization, without identifying the auxiliary moments with native X6/V29/V39 operations. Mathematical status is AUTHOR_EXACT_NOT_REVIEWED.

**Next discriminating unit:** characterize the entire calibrated minimax-center polytope in the remaining four free Walsh coefficients (u,v,w,z), at fixed (t,s), beginning with (1/10,1/2), and determine whether the h-axis segment is an exposed edge or lies in a higher-dimensional optimal face. Preserve all sixteen signed source/provenance atoms when testing such projections.
