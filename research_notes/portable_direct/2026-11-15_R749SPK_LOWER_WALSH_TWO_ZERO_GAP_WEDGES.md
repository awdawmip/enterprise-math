# R749SPK — two exact lower-triangle Walsh zero-calibration wedges

**Date:** 2026-11-15. **Scientific status:** AUTHOR_EXACT_NOT_REVIEWED. **Scientific input pin:** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. This note concerns only the auxiliary sixteen-atom compatible Walsh source model; it neither asserts a native X6 / V29 / V39 transfer nor changes the P000 six-axis/triadic native axioms.

**Immediate predecessor:** R749SPJ, [Draft PR #2439](https://github.com/awdawmip/enterprise-math/pull/2439), immutable scientific head \`87b194d7a6096b32924ab9b319c0e8a0a35c5098\`, completely classified the upper parameter triangle \`t+s>=1\`. The present work proves a genuinely two-dimensional *lower* parameter region, not covered by that upper classification, using the retained four-branch BRC representation and an exact rational polytope certificate.

## 1. Model and theorem

For \`k in F_2^4\`, define \`chi_m(k)=(-1)^{popcount(k&m)}\`, and the full sixteen-atom probability laws

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

For fixed \`t,s\` let \`F(t,s)\` consist of all normalized nonnegative laws in this family. Define \`TV(P,Q)=\frac12\sum_k|P(k)-Q(k)|\`, \`\rho(t,s)=\min_{q\in\Delta_{15}}\max_{P\in F(t,s)}TV(P,q)\`, and \`\rho_{\mathrm{cal}}(t,s)=\min_{q\in F(t,s)}\max_{P\in F(t,s)}TV(P,q)\`; let \`g=\rho_{\mathrm{cal}}-\rho\`.

Define the closed triangle

\[
T=\operatorname{conv}\{(0,0),(0,1),(1/5,2/5)\}
=\{(t,s):t\ge0,\ s\ge2t,\ 3t+s\le1\}
\]

and its bit-pair reflected triangle \`T^\tau=\operatorname{conv}\{(0,0),(1,0),(2/5,1/5)\}\`.

**Theorem (all real parameters, exact):**

\[
\boxed{\quad
(t,s)\in T:\quad
\rho(t,s)=\rho_{\mathrm{cal}}(t,s)=\frac{1-t}{2},\qquad g(t,s)=0;
\quad}
\]

\[
\boxed{\quad
(t,s)\in T^\tau:\quad
\rho(t,s)=\rho_{\mathrm{cal}}(t,s)=\frac{1-s}{2},\qquad g(t,s)=0.
\quad}
\]

In both triangles the same simple admissible calibrated center is optimal:

\[
q_0(t,s)=p_{t,s,0,0,0,0,0}.
\]

Each triangle has area \`1/10\`, and they intersect only at \`(0,0)\`; thus the proved lower-parameter zero-gap union has area exactly **1/5**. These are **new proved subregions**, not an assertion that the zero-gap locus has no other points.

## 2. Exact lower bound via two complete source laws

In the four-branch BRC chart put \`a=chi_3\`, \`b=chi_12\`, \`c=chi_1\`, \`d=chi_4\`. Then

\[
16p_{abcd}=M_{ab}+cU_a+dV_b,\quad
M_{ab}=1+at+bs+abh,\quad U_a=u+av,\quad V_b=w+bz.
\]

The full sixteen-atom positivity condition, with **no loss of source/provenance coefficients**, is exactly

\[
M_{ab}\ge |U_a|+|V_b|,\qquad a,b\in\{-1,1\}.
\]

For **every** real \`t,s>=0\` with \`t+s<=1\`, introduce two explicit complete compatible laws

\[
P_\pm(t,s)=p_{t,s,0,-t,-t,\ \pm s,\ \pm(1-t)}.
\]

For each law, \`U_+=-2t\`, \`U_-=0\`, \`|V_+|=1-t+s\`, \`|V_-|=1-t-s\`. The four block constraints are saturated exactly:

| Block \`(a,b)\` | \`M_{ab}\` | \`|U_a|+|V_b|\` |
|---|---|---|
| \`(+,+)\` | \`1+t+s\` | \`2t+(1-t+s)=1+t+s\` |
| \`(+,-)\` | \`1+t-s\` | \`2t+(1-t-s)=1+t-s\` |
| \`(-,+)\` | \`1-t+s\` | \`1-t+s\` |
| \`(-,-)\` | \`1-t-s\` | \`1-t-s\` |

Therefore both are nonnegative probability laws in the **same fiber** \`F(t,s)\`. Their difference is purely in the retained \`dV_b\` terms; summing absolute differences over all sixteen atoms gives

\[
TV(P_+,P_-)=\tfrac12(|1-t+s|+|s-(1-t)|)=1-t.
\]

Every unrestricted probability center \`q\` must satisfy
\`max(TV(P_+,q),TV(P_-,q))>=TV(P_+,P_-)/2\`, hence \`\rho(t,s)>=(1-t)/2\` throughout the lower triangle \`t+s<=1\`. By exact bit-pair exchange, also \`\rho(t,s)>=(1-s)/2\`. In particular, \`s>=2t\` on \`T\`, so the relevant lower bound there is \`(1-t)/2\`.

This explicit pair construction, valid on **all** lower-triangle parameters, is an additional reusable bound even where the matching upper-bound certificate is not yet available.

## 3. Exact universal upper bound for the calibrated center

For every \`(t,s)\in T\`, the center \`q_0(t,s)\` lies in the same fiber because \`t+s<=1\` and \`1\pm t\pm s>=0\` on all four blocks. The required upper claim is

\[
\forall(t,s)\in T,\ \forall P\in F(t,s):\qquad
TV(P,q_0(t,s))\le (1-t)/2.
\]

The joint source polytope lives in the **seven** variables \`x=(t,s,h,u,v,w,z)\`. It is cut out by precisely **nineteen** linear rational inequalities: sixteen atomic nonnegativity inequalities plus \`t>=0\`, \`s-2t>=0\`, \`1-s-3t>=0\`. It is compact, because each Walsh coefficient of any probability law is an expectation of a sign and belongs to \`[-1,1]\`. It has nonempty seven-dimensional interior. Thus every vertex is captured among the \`C(19,7)=50,388\` candidate sets of seven active facets with linearly independent normals.

The accompanying original executable uses only Python standard-library integers and \`fractions.Fraction\`. It performs integer Bareiss elimination, exact rational back substitution, all-inequality feasibility filtering and full rational-vertex deduplication. On every vertex \`x\` it checks normalization/nonnegativity and computes **exactly**

\[
E(x)=TV(p_x,q_0(t,s))-(1-t)/2.
\]

The fully executed certificate returned:

| Certificate statistic | Exact result |
|---|---:|
| Seven-facet candidate combinations | 50,388 |
| Nonsingular combinations | 27,600 |
| Feasible combinations, repetitions included | 4,804 |
| Distinct complete rational vertices | **82** |
| Vertices attaining \`E=0\` | 40 |
| **Maximum \`E\`** | **0** |

The 82 vertices project to five parameter values: \`(0,0):26\`, \`(0,1/2):4\`, \`(0,1):2\`, \`(1/7,4/7):2\`, \`(1/5,2/5):48\`. The non-corner interior edge projections are explicitly included; a three-corner sample is **not** the certificate.

The function \`x\mapsto E(x)\` is convex on this joint polytope: both \`p_x\` and \`q_0(t,s)\` are affine in all seven variables, TV is an \`L^1\` norm, and the radius subtracted is affine. A convex function on a compact polytope is bounded above by its maximum over the vertices. Thus the finite **complete vertex certificate** establishes the upper inequality for all **real**, not merely rational/sample, \`(t,s)\in T\` and all compatible complete sources.

Combining the matching lower bound from Section 2 with the same-fiber calibrated center yields \`\rho=\rho_{\mathrm{cal}}=(1-t)/2\` and \`g=0\` on \`T\`.

## 4. Reflected triangle and boundary scope

The exact atom permutation \`k\mapsto ((k&3)<<2)|((k&12)>>2)\` interchanges \`chi_3\leftrightarrow chi_12\`, \`chi_1\leftrightarrow chi_4\`, \`chi_2\leftrightarrow chi_8\` and preserves \`chi_15\`. It is a total-variation isometry and carries the complete source fiber \`F(t,s)\` to \`F(s,t)\`. It fixes the form of \`q_0\`. Therefore it transfers every part of the theorem to \`T^\tau\`; the checker asserts this permutation identity for **all 16 atoms**.

For a strict illustration of certificate scope, at \`(t,s)=(1/5,1/2)\` (outside \`T\`) the explicitly compatible law

\[
P=p_{1/5,1/2,-7/30,1/30,-1/30,-11/15,-11/15}
\]

satisfies \`TV(P,q_0)=17/40>2/5=(1-t)/2\`. Consequently the **particular center** \`q_0\` and the **particular radius formula** do not extend there. This does **not** establish \`g>0\`: another center may have smaller radius, and identifying the actual minimax phase outside the wedges remains open. The arithmetic of this witness was independently checked with the exact fraction evaluator.

## 5. Reproducibility, evidence, limits and next research unit

- **Executed script:** \`research_notes/portable_direct/R749SPK_LOWER_WALSH_CORNER_EXACT_CERT.py\`.
- **Saved full machine output:** \`research_notes/portable_direct/R749SPK_LOWER_WALSH_CORNER_RESULTS.json\`.
- **Command:** \`python3 R749SPK_LOWER_WALSH_CORNER_EXACT_CERT.py > R749SPK_LOWER_WALSH_CORNER_RESULTS.json\`.
- **Actual execution:** Python 3 standard library, exact Bareiss/Fraction; completed with \`PASS\`, 50,388 candidate bases and 82 feasible distinct vertices, zero maximum risk excess. No float LP or numerical tolerances enter the proof certificate. Independently reviewed: **no**. Lean or formal checker: **not run**. Proven theorem pertains to the declared auxiliary model only.
- **Source lineage:** frozen original auxiliary Walsh source \`a72226e2430ffa4786321ac86e7f0c599d5f0389\`, and R749SPJ upper-parameter exact theorem \`87b194d7a6096b32924ab9b319c0e8a0a35c5098\`. The present material is an independent author-side portable research increment, not a shared Task CLAIM, native PROGRESS, or Result/Review.
- **Next mathematical dependency:** determine the exact **admissible minimax center and phase boundary outside** \`s=2t\` and \`s+3t=1\` in the lower parameter triangle, where the sharp universal source-pair lower bound survives but \`q_0\` may cease to be optimal. Seek additional affine centers and matching event dual certificates, avoiding claims of positive calibration gap from failure of a particular center. Independently preserve the X6/V29/V39 source/port/operation-fidelity bridge as open.
