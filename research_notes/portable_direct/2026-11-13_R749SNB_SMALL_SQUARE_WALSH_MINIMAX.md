# R749SNB — Exact small-square Walsh minimax phase (unrestricted and calibrated)

Date: 2026-11-13 (Asia/Shanghai). Lineage: R749SMX, R749SMY, R749SMZ, R749SNA. Frozen science: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`, unchanged. Mathematical status: author-side proof with exhaustive exact-rational vertex certificate; independent review pending. Auxiliary finite signed-source observer; no claim of native X6/V29/V39 correspondence.

## Setting and sharp theorem

Set `G=F_2^4`, `chi_k(x)=(-1)^{k·x}`, omitted `C={1,2,4,8,15}`, retained `B={3,5,6,7,9,10,11,12,13,14}`. The fiber `F(t,s)` is the set of all probability measures on the sixteen source labels satisfying `m_3=t`, `m_12=s`, and the other eight retained B moments zero, for real `t,s∈[-1,1]`. Let `rho_B(t,s)=min_{q∈Delta(G)}max_{mu∈F(t,s)} TV(q,mu)`; `rho_B^cal` restricts `q∈F(t,s)`.

**Theorem (sharp two-dimensional phase).** For all real `|t|≤1/5`, `|s|≤1/5`,
\[
\boxed{\rho_B(t,s)=\rho_B^{cal}(t,s)=\frac{1-\min(|t|,|s|)}2.}
\]
An explicit optimal calibrated decoder is
\[
q_{t,s}(x)=\frac{1+t\chi_3(x)+s\chi_{12}(x)+h_0\chi_{15}(x)}{16},
\quad h_0=\operatorname{sgn}(ts)\min(|t|,|s|),
\]
with `sgn(0)=0`. In particular, the previously proved radius `1/2` on either entire coordinate axis drops strictly below `1/2` as soon as both coordinates are nonzero and sufficiently close to the origin. There is no positive-area flat neighborhood of the origin.

## Reduction to the ordered positive triangle

Let `A=chi_3`, `D=chi_12`, `P=chi_1`, `Q=chi_4`. These four signs are independent coordinates on `G`; `chi_2=AP`, `chi_8=DQ`, `chi_15=AD`. Signed source translations independently flip the signs of A and D and leave the eight zero B moments zero. The source-bit permutation exchanging the pairs `(1,2)` and `(4,8)` swaps t and s and preserves both C and B. All are bijections preserving TV and calibration. Thus it suffices to prove the theorem for `0≤s≤t≤1/5`, where `h_0=s`.

Walsh inversion gives every compatible law uniquely as
\[
\mu(x)=\frac{1+tA+sD+hAD+uP+vAP+wQ+zDQ}{16}.
\]
Its sixteen nonnegativity inequalities are precisely
\[
1+tA+sD+hAD+uP+vAP+wQ+zDQ\ge0,\quad (A,D,P,Q)\in\{\pm1\}^4.
\]
For the ordered triangle the stated decoder is `q=(1+tA+sD+sAD)/16`. It is a probability measure: among its four class numerators the minimum is `1-t≥4/5`, and every nonconstant retained B moment except t,s is zero. Hence q is calibrated.

## Universal lower bound (explicit compatible pair)

For any `t∈[-1,1]` define
\[
\nu_\pm(x)=\frac{(1+tA)(1\pm P)}{16},\qquad
\eta_t(x)=\frac{(1+tA)(1+D)}{16}.
\]
The two nu laws have retained moments `(t,0)` and disjoint P-supports; eta has retained moments `(t,1)`. Their other retained moments are zero because their Fourier supports are respectively `{0,3,1,2}` and `{0,3,12,15}`. Therefore for `s∈[0,1]`,
\[
\mu_\pm=(1-s)\nu_\pm+s\eta_t\in F(t,s),\qquad
TV(\mu_+,\mu_-)=1-s.
\]
The triangle inequality yields `rho_B(t,s)≥(1-s)/2`, for every t and `0≤s≤1`. The same lower bound holds for calibrated decoders.

## Upper bound: exact finite certificate for the full continuum

Consider the seven-dimensional rational polytope `P_*` of all tuples `(t,s,h,u,v,w,z)` satisfying the sixteen source positivity inequalities and three triangle inequalities
\[
s\ge0,\qquad t-s\ge0,\qquad 1-5t\ge0.
\]
It is bounded (all seven coordinates are moments of a probability measure), and full dimensional (choose `0<s<t<1/5`, `h=u=v=w=z=0`). Every vertex thus has seven linearly independent active inequalities among nineteen. The companion *exact integer/Fraction checker* enumerates all `binom(19,7)=50,388` seven-facet subsets, solves their systems by fraction-free integer elimination and rational back substitution, filters by **all nineteen exact inequalities**, and deduplicates solutions by exact rational tuples. It finds 24,992 nonsingular systems, 1,088 feasible bases and precisely 123 distinct vertices. Vertex parameter projections are exclusively `(t,s)=(0,0),(1/5,0),(1/5,1/5)`, with counts 26, 44 and 53 respectively.

For a feasible tuple, the exact distance from our affine decoder is
\[
TV(\mu,q)=\frac1{32}\sum_{x\in G}
\left|(h-s)AD+uP+vAP+wQ+zDQ\right|.
\]
The checker verifies for **every one of the 123 exact rational vertices**
\[
\sum_{x\in G}|(h-s)AD+uP+vAP+wQ+zDQ|\le16(1-s).
\]
Fifty-nine vertices attain equality. Its exact slack distribution is `{0:59, 16/5:28, 24/5:4, 16/3:8, 6:16, 32/5:8}`. The source-side quantity `TV(\mu,q)-(1-s)/2` is convex in all seven tuple coordinates, because `mu` and `q` are affine and TV is a norm. A convex function on a bounded polytope attains its maximum at a vertex; hence the checked inequality holds for **every real tuple** in `P_*`, not merely rational or sampled points. Consequently the calibrated q proves `rho_B^cal(t,s)≤(1-s)/2`. Together with the explicit pair above it proves equality. Signed transformations and the A/D swap extend it to the full absolute-value square.

All counts and the convexity conclusion can be reproduced by `R749SNB_SMALL_SQUARE_EXACT_CHECK.py` without external packages or floating-point decisions. The accompanying results file records the exact certificate totals.

## Consequences and limits

The calibration penalty is exactly zero throughout the closed square `|t|,|s|≤1/5`, despite the strictly positive previously certified `8/225` penalty at `t=s=1/3`. The diagonal unrestricted radius is `2/5` at `t=s=1/5`, `92/225` at `t=s=1/3`, and `2/5` at `t=s=1/2`; thus these three certified points exhibit non-monotone diagonal behavior. A complete phase diagram beyond the small square and other exact transition curves remain unresolved. The model is an auxiliary Walsh observer and still requires a separately licensed native V29/V39 correspondence for physical attribution. No shared Task CLAIM, independent review, or Foundation acceptance is implied by this author-side research note.
