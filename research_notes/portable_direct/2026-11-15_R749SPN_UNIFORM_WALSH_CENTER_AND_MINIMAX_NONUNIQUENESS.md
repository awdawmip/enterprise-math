# R749SPN — A uniform affine Walsh minimax center and a positive-area continuum of calibrated optima

**Status:** AUTHOR_EXACT_NOT_REVIEWED. **Scope:** the frozen 16-atom *auxiliary* Walsh fiber; this is not a native X6/V29/V39 admission. **Frozen scientific source:** `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. **Predecessors:** R749SPK, https://github.com/awdawmip/enterprise-math/pull/2443; R749SPL–SPM, https://github.com/awdawmip/enterprise-math/pull/2446.

## 1. Exact model

For `k=0,...,15` and Walsh characters `chi_m(k)=(-1)^popcount(k&m)`, let

\[
p_{t,s,h,u,v,w,z}(k)=\frac{1+t\chi_3(k)+s\chi_{12}(k)+h\chi_{15}(k)
+u\chi_1(k)+v\chi_2(k)+w\chi_4(k)+z\chi_8(k)}{16}.
\]

The source fiber `F(t,s)` consists of all complete, nonnegative laws of this form with fixed first two Walsh moments `(t,s)`. With total-variation metric, define

\[
\rho(t,s)=\inf_{q\in\Delta_{16}}\max_{P\in F(t,s)}TV(P,q),\quad
\rho^{\rm cal}(t,s)=\inf_{q\in F(t,s)}\max_{P\in F(t,s)}TV(P,q).
\]

The four-branch provenance-preserving BRC chart groups `a=chi_3,b=chi_12,c=chi_1,d=chi_4` and has `16p_{abcd}=M_{ab}+cU_a+dV_b` with

\[
M_{ab}=1+at+bs+abh,\quad U_a=u+av,\quad V_b=w+bz.
\]

The 16 positivity inequalities are exactly `M_ab >= |U_a|+|V_b|` for the four pairs `(a,b)`.

## 2. New exact theorem: one affine center over a crossing chamber

Let

\[
S=\operatorname{conv}\{(0,0),(0,1),(1/5,1/5)\}
 =\{t\ge0,\ s\ge t,\ 4t+s\le1\}.
\]

For **every real** `(t,s) in S`, the *same affine prescription*

\[
\boxed{q_1(t,s)=p_{t,s,t,0,0,0,0}}
\]

is a calibrated minimax center and

\[
\boxed{\rho(t,s)=\rho^{\rm cal}(t,s)=\frac{1-t}{2},\qquad g(t,s)=0.}
\]

The Walsh bit-pair exchange transports this result to `S^tau=conv{(0,0),(1,0),(1/5,1/5)}` with affine center `p_{t,s,s,0,0,0,0}` and radius `(1-s)/2`. Each triangle has area `1/10`, and their interiors are disjoint.

**Admissibility.** `4t+s<=1` implies `0<=t+s<=1`; for `h=t,U=V=0` the four block masses are `1+2t+s, 1-s, 1+s-2t, 1-s` (in `(++),(+-),(-+),(--)` order), all nonnegative on `S`. Thus `q_1` is in the specified source fiber, not merely the free probability simplex.

**Matching lower bound.** On the larger parameter triangle `{t,s>=0,t+s<=1}`, the complete two compatible source laws

\[
P_\pm=p_{t,s,0,-t,-t,\ \pm s,\ \pm(1-t)}
\]

satisfy the four BRC constraints with equality and have `TV(P_+,P_-)=1-t`. The metric triangle inequality gives `rho(t,s)>=(1-t)/2`.

**Universal matching upper bound.** Consider the compact seven-dimensional rational polytope of `x=(t,s,h,u,v,w,z)` subject to its sixteen atomic positivity inequalities and the three facets defining `S`. On that polytope the excess

\[
E(x)=TV(p_x,q_1(t,s))-\frac{1-t}{2}
\]

is convex because `p_x` and `q_1` are affine in `x`. The polytope is bounded (Walsh moments of probabilities lie in `[-1,1]`) and full dimensional (e.g. `0<t<s,\ 4t+s<1` with sufficiently small five remaining moments). All vertices are therefore obtained by testing the `C(19,7)=50,388` active-facet candidates with nonsingular normals.

The accompanying **executed** standard-library Python exact integer-Bareiss / `Fraction` verifier reports:

| Exact enumeration property | Count |
|---|---:|
| Candidate seven-facet bases | 50,388 |
| Nonsingular bases | 26,976 |
| Feasible bases, repetitions retained | 4,736 |
| Distinct rational vertices | 89 |
| Vertices with `E=0` | 59 |
| Maximum exact excess `E` | **0** |

Its vertex-parameter projections are `(0,0):26, (0,1):2, (0,1/2):4, (1/5,1/5):53, (1/7,3/7):2, (1/9,5/9):2`. Thus convexity gives `E<=0` for **all real** points in this seven-dimensional polytope. Together with the source-pair lower bound, this proves the theorem; it is not an interpolation from only the three parameter corners.

The reflection uses the exact 16-atom bit-pair swap `k -> ((k&3)<<2)|((k&12)>>2)`, which exchanges the two observed moments and preserves `chi_15` and TV.

## 3. New corollary: a positive-area continuum of optimal centers

The existing exact R749SPK theorem gives another calibrated optimal center `q_0=p_{t,s,0,0,0,0,0}` on

\[
T=\{t\ge0,\ s\ge2t,\ 3t+s\le1\}.
\]

The overlap is exactly

\[
S\cap T=\{0\le t\le1/6,\quad 2t\le s\le1-4t\},
\]

with area `1/12`. Hence, at every point of this overlap with `t>0`, every member of the distinct affine family

\[
\boxed{q_\lambda(t,s)=p_{t,s,\lambda t,0,0,0,0},
\qquad 0\le\lambda\le1}
\]

is a calibrated minimax center. The endpoint risk bounds are the same `(1-t)/2`; convexity of total variation in the center and convexity of the fiber preserve the bound throughout the segment. The Walsh coefficient `h=lambda*t` distinguishes the laws for `t>0`. Thus the calibrated minimax center is **nonunique, with a continuum of exact optima over a positive-area parameter region**.

The new `S` triangle is already contained in the union of the previously proved R749SPK wedge `T` and the R749SPL diagonal bridge `Q`: this result improves the *uniformity and multiplicity of optimal center constructions*, not the area of the known zero-gap locus. In particular `S\setminus T` has area `1/60` and belongs to the diagonal bridge.

## 4. Reproduction, scope and next question

- `R749SPN_WALSH_AFFINE_CENTER_MULTIPLICITY_CERT.py`: executable exact vertex enumerator.
- `R749SPN_WALSH_AFFINE_CENTER_MULTIPLICITY_RESULTS.json`: complete observed `PASS` output.
- Execute `python3 R749SPN_WALSH_AFFINE_CENTER_MULTIPLICITY_CERT.py > R749SPN_WALSH_AFFINE_CENTER_MULTIPLICITY_RESULTS.json`.
- Verification is exact rational within the stated auxiliary model. No independent peer review, Lean check, or native V29/V39 operation-fidelity correspondence was performed in this contribution.
- Next scientific unit: classify the full polytope of minimax calibrated centers as `(t,s)` crosses the old `T` and `Q` boundaries. A particularly discriminating question is whether some free minimax centers outside `t+s<=1` admit a similar affine no-switching carrier. Retain the frozen source and signed/provenance BRC typing.
