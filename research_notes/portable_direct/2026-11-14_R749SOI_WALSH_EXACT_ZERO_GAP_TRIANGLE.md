# R749SOI — Exact two-dimensional zero-calibration triangle adjoining the transverse transition

**Date:** 2026-11-14. **Mode:** independent portable TASK_RESEARCH, with no new shared CLAIM. **Scientific status:** author-side complete analytic + exact rational polytope certificate; **NOT_REVIEWED**.
**Frozen scientific source:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`.
**Actual prior evidence:** R749SOF (PR #2370, commit \`9dc5a0242c1b5dcb42fb7101eaea66ba91e727fd\`) and especially R749SOH (PR #2376, commit \`dfd63f878b2d33f189ddddc93846d3fb20a69827\`).
This is a theorem about the **auxiliary 16-state Walsh source-observer model**. Native X6/V29/V39 correspondence remains a distinct mathematical question.

## Definitions and theorem

Let \(G=\mathbb F_2^4\), \(\chi_m(k)=(-1)^{\operatorname{popcount}(m\mathbin{\&}k)}\), \(A=\chi_3\), \(B=\chi_{12}\), \(C=\chi_{15}=AB\). The full source fiber with retained Walsh coordinates \(t,s\) is
\[
F_{t,s}=\left\{\mu_{t,s,h,u,v,w,z}(k)=\frac{1+tA(k)+sB(k)+hC(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}\ge0\ (k=0,\ldots,15)\right\}.
\]
Each such law is normalized because nonconstant Walsh characters sum to zero. Write
\[
\rho(t,s)=\min_{q\in\Delta_{16}}\max_{\mu\in F_{t,s}}\operatorname{TV}(q,\mu),
\qquad
\rho^{cal}(t,s)=\min_{q\in F_{t,s}}\max_{\mu\in F_{t,s}}\operatorname{TV}(q,\mu).
\]

**Theorem (R749SOI).** For **every real** \((t,s)\) in the closed nondegenerate triangle
\[
T=\operatorname{conv}\{(1,0),(3/5,2/5),(1,1)\}
=\{t\le1,\ t+s\ge1,\ 3t-2s\ge1\},
\]
the exact minimax radii coincide:
\[
\boxed{\rho(t,s)=\rho^{cal}(t,s)=\frac{3-t-2s}{4}.}
\]
The triangle has exact area \(1/5\). It touches the full-line positive-to-zero transition of R749SOF at \((t,s)=(2/3,1/2)\), which lies on the oblique edge \(3t-2s=1\). One explicitly optimal calibrated predictor throughout the entire triangle is
\[
\boxed{q_{t,s}(k)=\frac{1+tA(k)+sB(k)+(t+s-1)C(k)}{16}.}
\]

## Proof: admissibility and matching lower bound

The three inequalities defining \(T\) imply \(0\le s\le t\le1\) and \(t+s\ge1\). The four sign-block numerators of the proposed \(q\), indexed by \((A,B)=(++),(+-),(-+),(--)\), are
\[
2(t+s),\qquad2(1-s),\qquad2(1-t),\qquad0,
\]
respectively. Hence \(q\in F_{t,s}\) for every point of \(T\).

Reuse and directly verify the explicitly compatible pair from R749SOH:
\[
\mu_\pm=\mu_{t,s,\;t+s-1,\;\pm(1-s),\;\pm(1-s),\;\pm(1-t),\;\pm(1-t)}.
\]
For \(t\ge s\) and \(t+s\ge1\), all sixteen source atom probabilities are nonnegative; in the four \((A,B)\) blocks the minimal source numerator is \(4(t+s-1),0,0,0\), respectively. Exact summation of the sixteen absolute differences gives
\[
\operatorname{TV}(\mu_+,\mu_-)=\frac{3-t-2s}{2}.
\]
For any probability decoder \(q'\) (including uncalibrated ones), the triangle inequality yields
\[
\max\{\operatorname{TV}(q',\mu_+),\operatorname{TV}(q',\mu_-)\}
\ge\frac12\operatorname{TV}(\mu_+,\mu_-)
=\frac{3-t-2s}{4}.
\]
This establishes the uniform lower bound for both radii.

## Proof: exact finite universal upper certificate

In seven joint variables \(X=(t,s,h,u,v,w,z)\), define the compact convex polytope \(P\) by sixteen source atom inequalities
\[
1+X\cdot (A(k),B(k),C(k),\chi_1(k),\chi_2(k),\chi_4(k),\chi_8(k))\ge0\quad(k=0,\dots,15)
\]
and the three triangle inequalities \(-t\ge-1\), \(t+s\ge1\), \(3t-2s\ge1\). Every point of \(P\) is a normalized source law; conversely every source with \((t,s)\in T\) occurs in \(P\).

On \(P\), \(q(t,s)\) and \(\mu(X)\) are affine, so
\[
f(X)=\operatorname{TV}(q(t,s),\mu(X))-\frac{3-t-2s}{4}
\]
is convex. It suffices to show \(f\le0\) at every vertex. A vertex has seven linearly independent active inequalities. The attached Python standard-library exact checker enumerates **every** seven-subset of the 19 constraints, solves its square system by fraction-free integer Bareiss elimination, discards singular or infeasible solutions, deduplicates exact rational vertices, and computes \(f\) with \`fractions.Fraction\`.

Exact executed result:
- \(\binom{19}{7}=50,388\) candidate active bases examined;
- 26,976 nonsingular bases, 6,048 feasible bases, **25 distinct feasible vertices**;
- 11 tight vertices, zero violating vertices, **maximum excess exactly 0**;
- \(q\) and every source law have nonnegative sixteen-atom probabilities and unit mass at all certified vertices;
- exact lower-pair identity independently checked at all three triangle corners.

Because \(P\) is bounded (parameters are in \(T\) and coefficients of normalized nonnegative laws are bounded) and \(f\) is convex, every \(X\in P\) is a convex combination of certified vertices and \(f(X)\le0\). This proves the upper bound for **all real parameters**, matching the analytic lower bound.

**Reproduction:** run \`python3 R749SOI_WALSH_ZERO_GAP_TRIANGLE_EXACT_CHECK.py\` (Python standard library only) and compare the JSON with \`R749SOI_WALSH_ZERO_GAP_TRIANGLE_RESULTS.json\`. Arithmetic is exact rational, no floating point tolerances or numerical LP solver are used in the certificate. This is author-side verified, pending independent review.

## Edge-specific falsification of this affine decoder

The oblique inequality has substantive content. At \((t,s)=(13/20,1/2)\), outside \(T\), the extrapolated predictor has \(h=t+s-1=3/20\). The valid compatible source
\[
\mu_A=\mu_{13/20,1/2,\;17/20,\;-3/20,\;-3/20,\;0,\;0}
\]
has \(\operatorname{TV}(q,\mu_A)=7/20\), whereas the extrapolated target \((3-t-2s)/4=27/80\). The exact excess is \(1/80\). This refutes universal continuation of **this decoder/radius formula** beyond the edge; the actual minimax radii at that external point are given by R749SOF, with positive gap \(1/400\).

## Research frontier and provenance

This adds a full **area \(1/5\)** two-dimensional zero-gap region which reaches the transverse \(g=0\) transition, complementing the positive two-dimensional collar from R749SOG. The oblique edge \(3t-2s=1\) is a sharp onset edge for the particular explicit center, and its status as a complete local **global** \(g=0\)/\(g>0\) phase boundary away from \(s=1/2\) remains to be determined.

**Next discriminating unit:** obtain a joint two-parameter exact piecewise formula on the outer side \(3t-2s<1\) near \((2/3,1/2)\), with matching free/calibrated lower bounds and center constructions; determine exact one-sided directional gap derivatives and whether the oblique edge is a true local phase boundary. Do not regenerate the already verified R749SOF/SOG/SOH work.

**Evidence:** this note; \`R749SOI_WALSH_ZERO_GAP_TRIANGLE_EXACT_CHECK.py\`; \`R749SOI_WALSH_ZERO_GAP_TRIANGLE_RESULTS.json\`. Formal shared Task/CLAIM ownership remains governed by current canonical control; this independent paper is not a Result/Review/admission.
