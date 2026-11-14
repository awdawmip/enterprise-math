# R749SNW — A two-dimensional Walsh source-diameter minimax phase

**Date:** 2026-11-14. **Status:** \`AUTHOR_EXACT_CERTIFICATE / NOT_REVIEWED\`. **Scientific input (unchanged):** \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. **Scope:** the frozen auxiliary 16-state Walsh source/observer model, not a native X6/V29/V39 event equivalence or a change to P000.

## 1. Statement

Take the group \(G=\mathbb F_2^4\), with Walsh characters \(\chi_m(x)=(-1)^{\operatorname{popcount}(m\mathbin{\&}x)}\). Let \(\mathcal F_{t,s}\) be the family of probability laws

\[
\mu_{t,s,h,u,v,w,z}(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+h\chi_{15}(x)+u\chi_1(x)+v\chi_2(x)+w\chi_4(x)+z\chi_8(x)}{16},
\qquad x\in G,
\]

whose 16 masses are nonnegative. Retained Walsh moments are \(3,12\), taking values \(t,s\), and \(5,6,7,9,10,11,13,14\), taking value zero. The variables \(h,u,v,w,z\) parametrize five unretained moments. With \(\operatorname{TV}(p,q)=\frac12\sum_x |p(x)-q(x)|\), define

\[
\rho(t,s)=\inf_{q\in\Delta_{16}}\sup_{\mu\in\mathcal F_{t,s}}\operatorname{TV}(\mu,q),
\qquad
\rho^{\mathrm{cal}}(t,s)=\inf_{q\in\mathcal F_{t,s}}\sup_{\mu\in\mathcal F_{t,s}}\operatorname{TV}(\mu,q).
\]

**Theorem R749SNW.** For **every real** pair \((t,s)\) in the closed triangle

\[
\mathcal D=\big\{(t,s):t\ge1/2,\ s\ge0,\ t+3s\le1\big\}
=\operatorname{conv}\big\{(1/2,0),(1,0),(1/2,1/6)\big\},
\]

\[
\boxed{\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=\frac{1-s}{2}.}
\]

One optimal calibrated center is

\[
q_{t,s}(x)=
\frac{1+t\chi_3(x)+s\chi_{12}(x)+(t+3s-1)\chi_{15}(x)}{16}.
\]

The triangle area is \(1/24\). The established one-dimensional R749SNV phase \(t=3/5,\ 0\le s\le2/15\) is an interior segment that reaches the upper edge, where it joins the earlier R749SNU phase at \((3/5,2/15)\).

## 2. Exact diameter lower bound

For each \((t,s)\in\mathcal D\) consider

\[
\mu_\pm=\mu_{t,s,-s,\ \pm(1-s),\ \pm(t+s),\ 0,\ 0},
\]

using simultaneous signs for \(u,v\). Each law has all 16 masses nonnegative at all three triangle vertices, directly verified by the attached exact code. Since the masses are affine in \((t,s)\), the laws are feasible throughout the triangle. Their difference is

\[
\mu_+(x)-\mu_-(x)=\frac{2(1-s)\chi_1(x)+2(t+s)\chi_2(x)}{16}.
\]

The pair \((\chi_1,\chi_2)\) realizes all four sign configurations equally often over \(G\), so

\[
\operatorname{TV}(\mu_+,\mu_-)
=\max\{|1-s|,|t+s|\}=1-s,
\]

because \(t+3s\le1\) implies \(t+2s\le1\). The triangle inequality therefore yields for **every** probability predictor \(q\),

\[
\max\{\operatorname{TV}(\mu_+,q),\operatorname{TV}(\mu_-,q)\}\ge\frac{1-s}{2}.
\]

This establishes the lower bound for both unrestricted and calibrated minimax risks.

## 3. Complete rational upper-bound certificate

The proposed center \(q_{t,s}\) retains all prescribed moments. The 16 masses of \(q_{t,s}\) are nonnegative at the three triangle vertices and hence throughout \(\mathcal D\). It is thus an admissible calibrated center.

Consider the **seven-dimensional compact joint source polytope** in \((t,s,h,u,v,w,z)\), with sixteen source nonnegativity inequalities plus \(t\ge1/2,\ s\ge0,\ t+3s\le1\). It is bounded because \(t,s\) range in a compact triangle and every Walsh coefficient of a probability measure lies in \([-1,1]\). Use the scaled variables \(y=6(t,s,h,u,v,w,z)\). The 19 integer halfspaces are

\[
(\chi_3(x),\chi_{12}(x),\chi_{15}(x),\chi_1(x),\chi_2(x),\chi_4(x),\chi_8(x))\cdot y\ge-6
\quad(x\in G),
\]

\[
y_t\ge3,\qquad y_s\ge0,\qquad -y_t-3y_s\ge-6.
\]

The function

\[
\Delta(y)=\operatorname{TV}(\mu_{t,s,h,u,v,w,z},q_{t,s})-\frac{1-s}{2}
\]

is convex on this polytope: total variation is a norm of an affine difference and the subtracted radius is affine. Its maximum is therefore attained at a vertex.

The companion **standard-library-only**, exactly rational checker enumerates **all** \(\binom{19}{7}=50,388\) potential seven-constraint bases; it uses integer Bareiss elimination, discards singular and infeasible intersections, deduplicates feasible points, and checks \(\Delta\) at each vertex:

| Certificate component | Exact result |
|---|---:|
| Active bases | 50,388 |
| Nonsingular bases | 25,664 |
| Feasible bases | 4,596 |
| Distinct rational vertices | 82 |
| Tight vertices (\(\Delta=0\)) | 36 |
| Violating vertices (\(\Delta>0\)) | **0** |
| Maximum \(\Delta\) | **0** |

Therefore \(\operatorname{TV}(\mu,q_{t,s})\le(1-s)/2\) everywhere on the joint source polytope. The lower-bound sources and upper-bound center prove the stated exact theorem over the entire real triangle, not just sample points.

## 4. Comparison, provenance, and open question

On \(t=3/5\), the new domain condition is \(0\le s\le2/15\). It recovers the R749SNV slope \(-1/2\); on the neighboring R749SNU interval, the already proved common risk is \((3+t-s)/8\), with slope \(-1/8\). At \((3/5,2/15)\), both equal \(13/30\), and their displayed calibrated centers have zero \(\chi_{15}\) coefficient.

This is an **auxiliary Walsh model-internal author theorem**, pending independent review. The frozen science pin is unchanged. A native X6/V29/V39 dynamics correspondence and any formal Result/admission remain separate.

**Reproduction:** run \`python R749SNW_WALSH_DIAMETER_TRIANGLE_EXACT_CHECK.py\` and compare its complete standard output with \`R749SNW_WALSH_DIAMETER_TRIANGLE_RESULTS.json\`. The validator uses exact integers and \`Fraction\` throughout, including source feasibility, source-pair diameter, predictor feasibility, all 50,388 active bases, and exact worst-case vertex excess.

**Next research:** characterize the boundary of the diameter phase for \(t<1/2\), and test alternative calibrated prediction centers beyond \(t+3s=1\). Loss of optimality of the displayed center alone does not show a positive calibration gap.
