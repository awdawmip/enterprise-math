# R749SPG — two exact zero-calibration Walsh triangles (global reentrant region)

Date: 2026-11-15. Status: AUTHOR_EXACT_NOT_REVIEWED. Scope: auxiliary 16-atom Walsh compatible-source fiber, **not** native X6/V29/V39. Frozen scientific input remains \`awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389\`. Immediate predecessor: R749SPF, Draft PR #2428, scientific commit \`67f37c7d78ffebff210015b60ba08778ac5b828f\`. Do not rebase scientific assumptions to current policy HEAD.

## Main result: two closed triangles, all real parameters

For \`K=F_2^4\`, write \`chi_m(k)=(-1)^{popcount(k&m)}\`, and the normalized laws

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

Let \`F(t,s)\` consist of **all** such nonnegative laws with the displayed \`t,s\` fixed. Let \`rho\` be the minimax total-variation radius over all probability-law centers; \`rho_cal\` the same minimax radius with the center constrained to \`F(t,s)\`; \`g=rho_cal-rho\`.

Define
\[
T_1=\operatorname{conv}\{(1,0),(3/5,2/5),(1,1)\}
 =\{0\le t,s\le1:\ t+s\ge1,\ 3t-2s\ge1\}.
\]
For **every real** \`(t,s) in T_1\`,
\[
\boxed{\rho(t,s)=\rho^{\mathrm{cal}}(t,s)=\frac{3-t-2s}{4}},\qquad \boxed{g(t,s)=0}.
\]
The exact optimal center is \`q_0=p_{t,s,t+s-1,0,0,0,0}\`. By the bit-pair exchange \`(k_0,k_1)<->(k_2,k_3)\`, the identical result holds on the reflected triangle
\[
T_2=\operatorname{conv}\{(0,1),(2/5,3/5),(1,1)\}
\]
with \`rho=rho_cal=(3-s-2t)/4\` and optimal center \`q_0\`. Each triangle has planar area \`1/5\`. Their intersection is the single point \`(1,1)\`, so their combined new *certified region* has area \`2/5\`. This does not claim the complete global zero-gap locus.

The theorem strengthens the R749SPF zero-gap return on \`s=3/5,11/15<=t<=1\` to an actual two-dimensional region: \`T_1\` intersects that slice in \`11/15<=t<=1\`, preserving the earlier exact radius \`9/20-t/4\`. Unlike a thin neighboring wedge, this certificate covers parameters all the way to the boundary edges \`s=0\`, \`t=1\`, and \`t=s=1\`.

## Lower certificate: two antipodal compatible sources

Set \`h_0=t+s-1\` and
\[
P_\pm=p_{t,s,h_0,\ \pm(1-s),\ \pm(1-s),\ \pm(1-t),\ \pm(1-t)}.
\]
For \`t+s>=1\` and \`0<=s<=t<=1\` both are nonnegative probability laws. This follows from the four-branch BRC representation, where \`a=chi_3\`, \`b=chi_12\` and
\[
16p=M_{ab}+cU_a+dV_b,\quad M_{ab}=1+ta+sb+hab,\quad U_a=u+av,\quad V_b=w+bz.
\]
The branchwise inequalities \`M_ab >= |U_a|+|V_b|\` hold: the \`--\` block is zero; \`+-\` and \`-+\` saturate their respective budgets \`2(1-s)\` and \`2(1-t)\`; the \`++\` block has mass parameter \`2(t+s)\` and required deviations \`2(1-s)+2(1-t)\`, allowed by \`t+s>=1\`.

The midpoint is exactly \`q_0=(P_++P_-)/2\`. Averaging absolute deviations over the four atoms in each sign block gives
\[
\mathrm{TV}(P_+,q_0)=\frac{(1-s)+(1-t)+\max(1-s,1-t)}4
=\frac{3-t-2s}{4}=:R
\]
because \`t>=s\` on \`T_1\`. Hence \`TV(P_+,P_-)=2R\`, forcing both free and calibrated minimax radii to be **at least** \`R\`.

## Universal upper certificate: complete exact seven-dimensional polytope

For \`(t,s)\in T_1\`, the proposed center \`q_0\` is a normalized nonnegative element of \`F(t,s)\`, by the same branch analysis. To prove \`TV(p,q_0)<=R(t,s)\` for every law \`p\in F(t,s)\`, consider the bounded polytope in \`x=(t,s,h,u,v,w,z)\in R^7\`, cut out by the **16** Walsh-atom inequalities \`1+sum(row_i*x_i)>=0\` and the **three** triangle inequalities \`t<=1\`, \`t+s>=1\`, and \`3t-2s>=1\`. These three inequalities describe exactly \`T_1\`, so no clipping or sampling of the target region is involved.

The attached standard-library program enumerates all \`C(19,7)=50388\` seven-facet active sets with integer Bareiss elimination, rejects singular and infeasible solutions using Python \`Fraction\`, and checks normalization, nonnegativity, and the exact risk excess \`TV(p,q_0)-R(t,s)\` at every distinct vertex. Boundedness follows because every Walsh coefficient of a normalized nonnegative probability law lies between \`-1\` and \`1\`. Every vertex has seven independent active facets. At every vertex, \`TV(p,q_0)-R\` is **exactly <=0**, with attained maximum zero. This function is convex on the joint polytope (TV of two affine laws minus an affine radius). By convexity, its value throughout the polytope is at most its maximum over the vertices. This proves the upper certificate over the **entire continuum of real parameters**, not only rational sample points.

The exact executed result was:

| Check | Exact result |
|---|---:|
| Active 7-facet candidate sets | 50,388 |
| Non-singular candidates | 26,976 |
| Feasible bases, including repetitions | 6,048 |
| Distinct rational vertices | 25 |
| Risk-tight vertices | 11 |
| Maximum risk excess | 0 |
| Two-bit-pair exchange automorphism | PASS |
| Joint region area | 2/5 |

The 25 exact vertices project to just four parameter points: \`(1,0)\` (2 vertices), \`(1,1)\` (1), \`(2/3,1/3)\` (2), \`(3/5,2/5)\` (20). Interior-to-edge vertices at \`(2/3,1/3)\` are checked; the proof is **not** a three-corner-only argument. The explicit symmetry permutation \`k -> ((k&3)<<2)|((k&12)>>2)\` swaps \`chi_3<->chi_12\`, \`chi_1<->chi_4\`, \`chi_2<->chi_8\`, preserving \`chi_15\`, positivity and total variation. Therefore it transfers the complete proof to \`T_2\`.

## A sharp boundary for this explicit center, not a global gap claim

For \`t>=s\`, the alternative compatible law \`H=p_{t,s,1-t+s,0,0,0,0}\` exists; its distance from \`q_0\` is \`TV(H,q_0)=1-t\`. Relative to the proposed radius, the exact excess is
\[
(1-t)-\frac{3-t-2s}{4}=\frac{1-3t+2s}{4}.
\]
Thus whenever \`t+s>=1\`, \`0<=s<=t<=1\` but \`3t-2s<1\`, **this particular center and this particular radius certificate fail**. This is an exact witness for sharpness of the presented certificate boundary, but **not** a theorem that \`g>0\` outside either triangle; different centers and radii must be investigated.

## Scope, reproducibility, and continuation

Run: \`python3 R749SPG_WALSH_GLOBAL_REENTRANCE_EXACT_CERT.py > R749SPG_WALSH_GLOBAL_REENTRANCE_RESULTS.json\`. Both files use Python standard library only, integer Bareiss and exact fractions; no floating point, numerical optimization, or external input. The PASS JSON records all counts, projective-vertex histogram, exact lower-bound checks and the symmetry check. The code was executed locally on 2026-11-15; independent replication and mathematical review remain outstanding. Publication of this auxiliary theorem **does not** prove a provenance-preserving native X6/V29/V39 observer mapping, native signed-Port cancellation, or any P000 change.

Next: determine the actual zero/positive-gap boundary directly outside \`3t-2s=1\`, beginning with the exact \`s=3/5\` phase \`2/5<t<11/15\`, and find alternative minimax centers if the present midpoint fails. Retain the original scientific pin and signed-provenance distinctions, and do not replace the native three-dimensional research slice with this two-parameter auxiliary model.
