# R749SOV — Exact two-dimensional first-onset Walsh minimax phase

**Date:** 2026-11-14. **Scientific status:** AUTHOR_EXACT_NOT_REVIEWED.  
**Frozen scientific input:** awdawmip/enterprise-math at commit a72226e2430ffa4786321ac86e7f0c599d5f0389, auxiliary 16-state Walsh source observer.  
**Dependencies:** R749SOS–SOT, PR #2399 @ 5f2830988e31eae99d9ef11882e626b56b022552; R749SOU on the same research branch, PR #2404. No native X6/V29/V39 correspondence asserted.

## Statement and exact source fiber

Let \(K=\mathbf F_2^4\), \(\chi_m(k)=(-1)^{\operatorname{popcount}(m\mathbin{\&}k)}\), \(A=\chi_3\), \(B=\chi_{12}\), \(C=\chi_{15}=AB\). The full compatible fiber comprises the sixteen nonnegative probabilities

\[
p_{t,s,h,u,v,w,z}(k)=
\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

The admissible source parameters are precisely those with all 16 atoms nonnegative. The free minimax TV radius \(\rho(t,s)\) minimizes maximum TV distance over all probability centers; the calibrated radius \(\rho^{\mathrm{cal}}(t,s)\) restricts centers to the same source fiber. Define \(g=\rho^{\mathrm{cal}}-\rho\).

**Theorem, including every real boundary point.** In the entire closed rectangle

\[
\boxed{\frac5{22}\le t\le\frac14,\qquad\frac{49}{100}\le s\le\frac12}
\]

we have exact formulas

\[
\boxed{\rho(t,s)=\frac{3-t+s}{8}},\qquad
\boxed{\rho^{\mathrm{cal}}(t,s)=\frac{1+t}{3}},\qquad
\boxed{g(t,s)=\frac{11t-3s-1}{24}}.
\]

The calibration gap is strictly positive everywhere in this rectangle except at the single point \((5/22,1/2)\), where it is exactly zero. At \(t=5/22\), the positive gap below the baseline equals \((1/2-s)/8\), a two-dimensional directional result at the exact first-onset threshold.

By the exact low/high-bit Walsh interchange, the same formulas hold after swapping \(t\) and \(s\), on \(49/100\le t\le1/2,\ 5/22\le s\le1/4\). These two disjoint rectangles have total area \(1/2200\). Combining them without double counting with R749SOU's two **upper** triangular halves adds area \(1/33792\); the certified union has area \(409/844800\).

## Exact free lower bound: diametral source pair

Use the notation \(p(t,s,h,u,v,w,z)\) for the law above. Construct

\[
p_+(t,s)=p(t,s,0,-t,-t,1-t,s),\qquad
p_-(t,s)=p(t,s,0,t,t,t-1,-s).
\]

Every atom of each distribution is affine in \(t,s\). All sixteen atoms are nonnegative at each of the four rectangle corners, hence throughout the rectangle by affine interpolation. The signs of the 16 atomwise differences \(p_+-p_-\) are weakly consistent at all corners. Exact sign summation therefore gives for **all real** \((t,s)\) in the rectangle

\[
\operatorname{TV}(p_+,p_-)=\frac{3-t+s}{4}.
\]

The triangle inequality for any probability center \(q\) shows

\[
\max\{\operatorname{TV}(q,p_+),\operatorname{TV}(q,p_-)\}
\ge\frac12\operatorname{TV}(p_+,p_-)
=\frac{3-t+s}{8}.
\]

Thus \(\rho\ge(3-t+s)/8\).

## Exact calibrated lower bound: invariant averaging and two dual events

Translation \(k\mapsto k\oplus a\) for \(a\in\{0,3,12,15\}\) preserves \(A,B,C\) and permutes the legal fiber; convex group averaging of a calibrated prediction center cannot increase its worst-case TV risk. The averaged center retains the fixed \(A=t,B=s\) moments and has no \(\chi_1,\chi_2,\chi_4,\chi_8\) coefficients, hence it is

\[
q_h(k)=p_{t,s,h,0,0,0,0}(k).
\]

Construct compatible source witnesses

\[
a_{t,s}=p(t,s,-t,0,0,-s-t,t-1),\qquad
b_{t,s}=p(t,s,1+t-s,0,0,t-s,t-s).
\]

Again all atoms are affine in the two parameters, and the exact four-corner check proves these are legal sources for the full rectangle. Two fixed TV event signs in canonical atom order \(k=0,\ldots,15\) are

\[
\begin{split}
\sigma_A&=(-1,-1,-1,-1,+1,-1,-1,+1,+1,-1,-1,+1,+1,+1,+1,+1),\\
\sigma_B&=(+1,-1,-1,+1,-1,+1,+1,-1,-1,+1,+1,-1,+1,-1,-1,+1).
\end{split}
\]

For any two distributions, TV is the maximum over all sign vectors \(\sigma\in\{\pm1\}^{16}\) of \(\frac12\sum_k\sigma_k(p_k-q_k)\). Direct exact algebra with the fixed signs yields, for **every real** \(h\),

\[
\operatorname{TV}(a_{t,s},q_h)\ge\frac{h+s+t+1}{4},
\qquad
\operatorname{TV}(b_{t,s},q_h)\ge\frac{1+t-s-h}{2}.
\]

The maximum of these two affine functions is at least their crossing value \((1+t)/3\); the crossing occurs at \(h=(1+t)/3-s\). Therefore \(\rho^{\mathrm{cal}}\ge(1+t)/3\).

## Explicit affine optimal centers

The calibrated center that reaches the stated upper bound is

\[
q_{\mathrm{cal}}(t,s;k)=p_{t,s,\,(1+t)/3-s,\,0,0,0,0}(k).
\]

For the free upper bound, an explicit affine simplex center is specified atomwise by

\[
q_{\mathrm{free}}(t,s;k)=Q_{00}[k]+x\,D_t[k]+y\,D_s[k],\quad
x=44t-10,\quad y=100(s-49/100).
\]

Here \(x,y\in[0,1]\) and the indexed arrays in \(k=0,\ldots,15\) order are

\[
\begin{aligned}
Q_{00}={}&(19/200,1569/17600,289/4400,1781/17600,5/88,1/88,211/8800,5/88,\\
&5/88,5/176,61/8800,5/88,1291/17600,289/8800,1609/17600,27/176),\\
D_t={}&(0,0,-29/8800,0,1/176,0,-3/550,27/8800,\\
&27/8800,-87/8800,39/8800,1/176,171/8800,-7/4400,-1/44,7/4400),\\
D_s={}&(-1/800,219/17600,-1/400,-131/17600,0,-1/800,0,0,\\
&0,0,-1/800,0,197/17600,0,-197/17600,1/800).
\end{aligned}
\]

The exact certificate below checks that these centers are normalized nonnegative laws throughout the rectangle; the free center is not required to preserve the frozen \(t,s\) moments.

## Exhaustive rational upper certificate: 7D joint polytope

Define the bounded 7D joint source-parameter polytope \(P\) in variables \((t,s,h,u,v,w,z)\) with sixteen affine atom-nonnegativity facets and four endpoint facets \(t\ge5/22,t\le1/4,s\ge49/100,s\le1/2\). It is full-dimensional: choose strict internal \(t,s\) and small remaining coefficients. Every vertex must therefore occur at the intersection of at least seven linearly independent active facets.

The accompanying standard-library Python 3 program enumerates **all** \(\binom{20}{7}=77,520\) active bases using integer Bareiss elimination and exact rational back-substitution. It obtains **30,208 non-singular bases**, **892 feasible active bases**, and **192 distinct rational vertices**: 50 at \((5/22,49/100)\), 50 at \((5/22,1/2)\), 50 at \((1/4,49/100)\), and 42 at \((1/4,1/2)\).

For every vertex the program checks that \(q_{\mathrm{free}}\) and \(q_{\mathrm{cal}}\) are valid probabilities and that

\[
\operatorname{TV}(p,q_{\mathrm{free}})\le\frac{3-t+s}{8},\qquad
\operatorname{TV}(p,q_{\mathrm{cal}})\le\frac{1+t}{3}.
\]

There are **zero upper-bound violations**; both maximum excesses equal exactly zero. For affine centers, TV\((p,q(t,s))\) minus its affine claimed radius is convex in the seven joint variables. Any point of bounded \(P\) is a convex combination of vertices; thus the vertex inequalities extend to **every real** \((t,s)\) in the rectangle and every compatible source law. The matching lower bounds complete both minimax equalities.

## Reproduction, scope and next problem

Files:
- research_notes/portable_direct/R749SOV_RECTANGLE_EXACT_CERTIFICATE.py
- research_notes/portable_direct/R749SOV_RECTANGLE_RESULTS.json

Run with Python 3 standard library only:

    python research_notes/portable_direct/R749SOV_RECTANGLE_EXACT_CERTIFICATE.py

The program regenerates the exact JSON result and verifies the four-corner lower-witness checks, both dual sign events, the full joint 7D vertex coverage, and the two upper-center bounds. Its claim is author-side exact proof pending independent mathematical review. It preserves the original scientific pin; native X6/V29/V39 typed correspondence is a separate open problem.

**Next discriminating problem:** construct full neighboring minimax chambers beyond \(s=1/2\) and \(t<5/22\) around \((5/22,1/2)\), test continuity and any corner in the true two-dimensional \(g=0\)/\(g>0\) boundary, and seek shorter event/center certificates than the 16-atom free array.
