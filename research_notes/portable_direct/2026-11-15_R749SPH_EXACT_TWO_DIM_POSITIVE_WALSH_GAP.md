# R749SPH — Exact positive two-dimensional Walsh calibration gap

**2026-11-15 · AUTHOR_EXACT_NOT_REVIEWED · frozen auxiliary Walsh science**  
Scientific pin: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Predecessors: R749SPD–SPF and R749SPG at [PR #2431](https://github.com/awdawmip/enterprise-math/pull/2431), commit `e985f1c8f8d7fe2a7ff2914b1835d68d5ef5b6fc`.

## Theorem — all real parameters in a positive-area trapezoid

Write `K=F_2^4`, `χ_m(k)=(-1)^popcount(k&m)` and
\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]
Let `F(t,s)` be *all* nonnegative probability laws of this form with t,s fixed, and let `ρ(t,s)` be the minimax total-variation radius over all probability centers; `ρ_cal(t,s)` the minimax radius restricted to centers in `F(t,s)`; `g=ρ_cal−ρ`.

On the closed real trapezoid
\[
\mathcal Q=\{(t,s):1/2\le s\le 11/15,\quad 0\le t-s\le1/30\},
\]
the **exact** three quantities are
\[
\boxed{\rho=(8-5t-3s)/10},\qquad
\boxed{\rho_{\mathrm{cal}}=(9-6t-3s)/11},\qquad
\boxed{g=(2-5t+3s)/110\ge1/300>0}.
\]
The optimal free center is `q_f=p(1,(8s−3)/5,(8s−3)/5,0,0,0,0)`, and an optimal calibrated center is `q_c=p(t,s,(t+17s−7)/11,0,0,0,0)`. Both are legitimate normalized nonnegative probability laws on the full region; `q_c∈F(t,s)`. No uniqueness is asserted.

The parameter region has exact planar area `7/900`; bit-pair exchange maps it to an equally sized reflected trapezoid `Q*={(t,s):(s,t)∈Q}`, with t and s swapped in the radius formulas. The two regions intersect only in a diagonal line segment, giving **combined positive-gap area `7/450`**, with gap uniformly at least `1/300`.

## Lower certificates: explicit source laws and two fixed events

Use the exact four-branch BRC chart `a=χ_3,b=χ_12,c=χ_1,d=χ_4`:
\[
16p=M_{ab}+cU_a+dV_b,\quad M_{ab}=1+ta+sb+hab,\quad U_a=u+av,\quad V_b=w+bz.
\]
The four conditions `M_ab≥|U_a|+|V_b|` are equivalent to all sixteen atom nonnegativities; the chart retains signs and the joint Walsh coefficient.

Define the compatible affine source families
\[
P_-=p(t,s,t+s-1,s-1,s-1,t-1,t-1),\quad
P_a=p(t,s,1+s-t,s-t,s-t,0,0).
\]
They are nonnegative and normalized on Q. This is an exact affine assertion: the attached checker confirms all 16 inequalities at the four vertices of Q, therefore everywhere on their convex hull.

For `E_A={7,11,13,14,15}`, `E_B={0,3,5,6,9,10,12,15}`, exact Walsh expansion gives
\[
P_-(E_A)=5/4-(t+s)/2,\qquad P_a(E_B)=1+(s-t)/2.
\]
The four-element group `G=ker χ_3∩ker χ_12` preserves the source family and total variation. Group-averaging any probability center does not increase its maximum risk. A G-invariant free center has four per-atom sign-block weights `x_0,x_1,x_2,x_3≥0` with `4Σx_i=1`. The events contain respectively `(0,2,2,1)` and `(4,0,0,4)` atoms of the `(--),(-+),(+-),(++)` blocks, so
\[
(4/5)q(E_A)+(1/5)q(E_B)=2/5-(4/5)x_0.
\]
From `TV(P,q)≥P(E)−q(E)` and maximum ≥ weighted average:
\[
\sup_{P∈F(t,s)}TV(P,q)\ge\frac45(P_-(E_A)-q(E_A))+\frac15(P_a(E_B)-q(E_B))
=\frac{8-5t-3s}{10}+\frac45x_0
\ge\frac{8-5t-3s}{10}.
\]
This is the **free** minimax lower bound, covering any law center by symmetrization.

The same averaging sends any calibrated center to `q_h=p(t,s,h,0,0,0,0)`. Direct event calculations give the two lower expressions
\[
\sup_P TV(P,q_h)\ge\max\{(15-9t-9s+3h)/16,\ (1+s-t-h)/2\}.
\]
The lines meet at `h=(t+17s−7)/11`, where both equal `(9−6t−3s)/11`. The increasing/decreasing affine maximum cannot be smaller at any h (even when h is allowed to be arbitrary real), proving the **calibrated** lower bound.

## Exact upper certificate over the continuum

The 7-dimensional joint parameter/source polytope has variables `x=(t,s,h,u,v,w,z)` and constraints: **16** Walsh atom inequalities, `2s≥1`, `15s≤11`, `t-s≥0`, and `30(t-s)≤1`. Each coefficient of a probability law is a Walsh expectation in `[-1,1]`, so the polytope is bounded. Every vertex is determined by seven independent facets, hence enumeration of every `C(20,7)=77,520` potential active set is complete.

The exact standard-library Python checker uses integer Bareiss elimination, rational back-substitution and fraction-only feasibility/risk checks. It found:

| Verified quantity | Exact output |
|---|---:|
| Candidate active bases | 77,520 |
| Non-singular bases | 32,832 |
| Feasible bases, including repeats | 1,380 |
| Distinct rational vertices | 74 |
| Free/calibrated risk-tight vertices | 26 / 26 |
| Maximum risk excess above either proposed radius | **0 / 0** |
| Minimum affine gap over vertices | **1/300** |
| Bit-pair exchange | PASS |

The vertex parameter projection histogram is `(1/2,1/2):17`, `(8/15,1/2):20`, `(23/30,11/15):20`, `(11/15,11/15):17`. All **74 full joint vertices** were checked, not merely the four parameter corners. For each vertex, source and both centers have nonnegative normalized 16-atom probabilities and
\[
TV(p_x,q_f(t,s))-(8-5t-3s)/10\le0,\qquad
TV(p_x,q_c(t,s))-(9-6t-3s)/11\le0.
\]
Each difference is convex in the joint seven real variables (TV between affine laws minus an affine radius). A convex function on a compact polytope cannot exceed its largest vertex value. Thus the upper bounds hold for **every real** feasible source and parameter in Q, and combine with the explicit lower bounds to prove the theorem.

Exact corner values:

| (t,s) | ρ | ρ_cal | g |
|---|---:|---:|---:|
| (1/2,1/2) | 2/5 | 9/22 | 1/110 |
| (8/15,1/2) | 23/60 | 43/110 | 1/132 |
| (23/30,11/15) | 59/300 | 1/5 | 1/300 |
| (11/15,11/15) | 16/75 | 12/55 | 4/825 |

Reflection swaps the two bit-pairs of K via `k→((k&3)<<2)|((k&12)>>2)`. The transformation sends `(t,s,h,u,v,w,z)→(s,t,h,w,z,u,v)` and preserves all laws and TV; this proves the reflected result without any new sampling.

## Validation, scope and continuation

Reproduce with `python3 R749SPH_TWO_DIM_POSITIVE_TRAPEZOID_EXACT_CERT.py > R749SPH_TWO_DIM_POSITIVE_TRAPEZOID_RESULTS.json`. The run uses only Python's standard library and exact integer/rational arithmetic; no floating-point arithmetic, external LP solver, or finite real-parameter sampling. Local execution on 2026-11-15 produced `PASS` with the counts above. Independent proof review is pending. This is an auxiliary 16-atom Walsh result with frozen scientific input, not a native X6/V29/V39 signed-Port or operation-faithful theorem.

Next: derive the maximal polygon where these same dual event certificates and affine optimal centers remain exact, and study the gap transition at its boundary; independently test whether the four-branch provenance carrier supports an observer-and-future-operation-preserving native map. P000, ACTIVE worldview, frozen science and shared TASK/CLAIM boundaries remain unchanged.
