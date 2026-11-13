# R749SNO — A larger exact Walsh zero-calibration triangle and a nonconvex fixed-center certificate

Date: 2026-11-14. Scope: 16-state auxiliary Walsh source observer; frozen scientific input \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This is a new mathematical continuation of R749SNK, SNM and SNN, using their exact definitions, not an asserted native X6/signed-Port/V29/V39 observer mapping. Status: AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED.

## Definitions and exact theorem

Let \(G=\mathbf F_2^4\), with Walsh characters \(\chi_m(x)=(-1)^{\operatorname{popcount}(m\mathbin{\&}x)}\). Retain \(B=\{3,5,6,7,9,10,11,12,13,14\}\), prescribe \(m_3=t,m_{12}=s\), and prescribe the remaining eight retained coefficients to vanish. Let \(F(t,s)\) be the nonempty compatible probability fiber. For \(\operatorname{TV}(\mu,q)=\frac12\sum_x|\mu(x)-q(x)|\) put

\[
\rho(t,s)=\min_{q\text{ probability}}\max_{\mu\in F(t,s)}\operatorname{TV}(\mu,q),\qquad
\rho^{\mathrm{cal}}(t,s)=\min_{q\in F(t,s)}\max_{\mu\in F(t,s)}\operatorname{TV}(\mu,q).
\]

**Theorem.** On the closed two-parameter triangle

\[
T=\{(t,s):t-s\ge\tfrac15,\quad t+s\le1,\quad3t+5s\ge3\}
=\operatorname{conv}\{(\tfrac12,\tfrac3{10}),(\tfrac35,\tfrac25),(1,0)\},
\]

**for every real** \((t,s)\in T\), the unrestricted and moment-calibrated minimax radii agree exactly:

\[
\boxed{\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=\frac{3+t-s}{8}.}
\]

The area of \(T\) is \(1/25\). The previous R749SNM quadrilateral (area \(11/800\)) is strictly contained in \(T\); the area ratio is \(32/11\). The triangle includes the complete R749SNN boundary segment \(t+s=1,\ 3/5\le t\le1\) as well as the R749SNK point \((1/2,3/10)\). This is an independent all-real joint-polytope proof, not an inference from endpoint fiber optima.

## Seven-coefficient Walsh parameterization

Set \(A=\chi_3,\ D=\chi_{12},\ AD=\chi_{15},\ U=\chi_1,\ AU=\chi_2,\ V=\chi_4,\ DV=\chi_8\). The inverse Walsh transform gives every admissible source uniquely as

\[
\mu_{t,s,h,u,v,w,z}(x)=\frac{1+tA(x)+sD(x)+hAD(x)+uU(x)+vAU(x)+wV(x)+zDV(x)}{16}
\]

with all 16 atoms nonnegative. On \(T\), the calibrated candidate

\[
q_0(t,s;x)=\frac{1+tA(x)+sD(x)}{16}
\]

is normalized and nonnegative because \(t,s\ge0\) and \(t+s\le1\); all prescribed Walsh coefficients are retained.

## Lower certificate, valid against all unrestricted decoders

Translations \(x\mapsto x\oplus3\) and \(x\mapsto x\oplus12\) preserve \(F(t,s)\), independently reverse the free \((u,v)\) and \((w,z)\) signs, and leave \(A,D,AD\) invariant. Group averaging an arbitrary decoder does not increase its worst-case TV loss by convexity, so the unrestricted optimum admits an invariant decoder \(q\) supported on Fourier characters \(1,A,D,AD\).

Choose the explicit affine compatible-source candidate

\[
W(t,s)=\mu_{t,s,\,0,\,s-1,\,-t,\,-s,\,-s}.
\]

The 16 atom masses of \(W\) are nonnegative and sum to one at each of the three triangle vertices (checked exactly by the reproducible script). Since the masses depend affinely on \((t,s)\), the same holds at every point of their convex hull \(T\).

Let \(E=\{3,5,7,9,11,13,14,15\}\). The sums of each of \(A,D,AD\) over \(E\) vanish. Every invariant probability decoder gives \(q(E)=1/2\), and direct Walsh substitution gives

\[
W(t,s)(E)-\tfrac12=\frac{3+t-s}{8}.
\]

The variational event inequality \(\operatorname{TV}(\mu,q)\ge\mu(E)-q(E)\) therefore yields \(\rho(t,s)\ge(3+t-s)/8\). It also bounds the calibrated radius below.

## Entire-triangle upper certificate

Introduce the seven coordinates \(y=10(t,s,h,u,v,w,z)\). The joint source/parameter polytope is the intersection of nineteen integer halfspaces: sixteen Walsh-atom inequalities \(R_x\cdot y\ge-10\), one for each \(x=0,\ldots,15\), where

\[
R_x=(A(x),D(x),AD(x),U(x),AU(x),V(x),DV(x)),
\]

and three triangle inequalities

\[
(1,-1,0,0,0,0,0)\cdot y\ge2,\quad
(-1,-1,0,0,0,0,0)\cdot y\ge-10,\quad
(3,5,0,0,0,0,0)\cdot y\ge30.
\]

This is a nonempty bounded full-dimensional polytope in seven coordinates (for instance \(t=3/5,s=3/10,h=u=v=w=z=0\) is strictly interior). Every vertex therefore occurs at seven linearly independent active facets. The supplied Python checker enumerates all \({19\choose7}=50{,}388\) seven-facet combinations with integer Bareiss elimination, reconstructs exact rational solutions, checks all nineteen inequalities, deduplicates vertices and computes

\[
\Delta=\operatorname{TV}(\mu_{t,s,h,u,v,w,z},q_0(t,s))-\frac{3+t-s}{8}.
\]

Actual full enumeration: 28,288 nonsingular bases; 4,944 feasible bases; 70 distinct vertices; 26 vertices attaining equality; **zero positive excess**, maximum excess exactly zero.

The function \(\Delta\) is convex in the seven joint coordinates: the probability laws are affine and the radius term is affine. Every point of the compact joint polytope is a convex combination of its vertices; hence \(\Delta\le0\) everywhere. The lower and upper certificates prove the theorem for all real points in \(T\). The joint-polytope enumeration, rather than only checking fixed fibers over the triangle's three geometric corners, is essential.

## Additional exact finding: the q0-affine-bound equality set is nonconvex

Hold \(t=7/10\), and compare the three values \(s=1/10,3/20,1/5\). Enumerating all \({16\choose5}=4{,}368\) active-facet sets in each fixed five-variable fiber yields

| \(s\) | Distinct fiber vertices | \(\max_{\mu\in F}\operatorname{TV}(\mu,q_0)\) | \((3+t-s)/8\) | Excess |
|---|---:|---:|---:|---:|
| \(1/10\) | 44 | \(9/20\) | \(9/20\) | 0 |
| \(3/20\) | 36 | \(37/80\) | \(71/160\) | \(3/160\) |
| \(1/5\) | 38 | \(7/16\) | \(7/16\) | 0 |

At the middle point the explicit admissible source

\[
(t,s,h,u,v,w,z)=
(\tfrac7{10},\tfrac3{20},-\tfrac3{20},\tfrac{17}{20},\tfrac{17}{20},0,0)
\]

attains TV distance \(37/80\) to \(q_0\). Thus the set of parameters where this **specific** calibrated center obeys the affine upper bound is not convex on that cross-section. This refutes endpoint-only interpolation for \(q_0\); it does not assert positive calibration penalty or determine the unrestricted minimax radius at the middle point. It also explains why the whole joint-polytope certificate was necessary for the triangle.

## Reproduction, scope and next question

Run \`python research_notes/portable_direct/R749SNO_TRIANGLE_AND_CENTER_CERTIFICATE_EXACT_CHECK.py\`; compare its entire JSON stdout against \`R749SNO_TRIANGLE_AND_CENTER_CERTIFICATE_RESULTS.json\`. All mathematical comparisons are exact integers or \`Fraction\`; no floating threshold is used. The script checks the lower-witness endpoint atoms, Walsh event sums, all 50,388 seven-facet joint bases, and each of three complete five-variable fixed-fiber enumerations.

R749SNO is an author-side exact certificate, pending independent review. The result is about the declared auxiliary Walsh observer model only; P000 and original task freeze pins remain unchanged.

Next: determine whether the calibrated and unrestricted radii still agree at \((7/10,3/20)\) using an alternative center, and chart the exact neighboring cells of the *optimal* zero-calibration region rather than only the \(q_0\) certificate. A typed, provenance-preserving transfer to actual X6/V29/V39 future observers remains a separate proposition.
