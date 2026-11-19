# EC49FUA — Full-support stochastic order for every admissible real price tilt

**Date:** 2026-11-19. **Status:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / PARENT_DEPENDENT / NOT_REVIEWED.  
**Scientific pin:** `awdawmip/enterprise-math@fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`; inherited native BRC16943 Bellman branch from [EC49FTH PR #2774](https://github.com/awdawmip/enterprise-math/pull/2774) and price-chart from [EC49FTP PR #2791](https://github.com/awdawmip/enterprise-math/pull/2791). Direct parent [EC49FTZ PR #2813](https://github.com/awdawmip/enterprise-math/pull/2813), with high-gap all-epsilon stochastic order from EC49FTY PR #2811. This paper is postprocessing of an external joint price prior; the independent native-source optimality remains an inherited author claim. No native BRC operation is rerun.

## Theorem: the complete M-support order, not only the clipped high-gap branch

Let `(a,b)` lie in `[3/4,49/64]×[7/16,57/128]` with joint density proportional to
[
h_\varepsilon(a,b)=1-\varepsilon M_*(a,b)Z_*(a,b),\quad
M_*=(525/8)a-(231/4)b-9/8,\quad
Z_*=(35/32)a-b/16-5/96.
]
For **every** real `epsilon<=E=1048576/18958647`, this is a nonnegative integrable density on the full rectangle. Let `M` be the optimal exchange gap and `Z` its optimal q140 discount according to the inherited native Bellman model. On the full interior support
[
m_0=11457/512<m<m_3=187/8
]
the regular conditional law of `Z|M=m` can be chosen so that for every `m<m'`
[
\boxed{Z\mid M=m\ \preceq_{\rm st}\ Z\mid M=m'.}
]
The statement includes the lower previously unproved phases, the transition at `m1=1461/64`, and the new top-atom discontinuity at `m2=1469/64`. At the latter discontinuity use the right-continuous version, or any conditional version lying stochastically between the two one-sided limits. The endpoint laws are obtained by one-sided limits: `Z=4549/6144` at `m0`, and `Z=3/4` at `m3`.

## Exact conditional-fiber geometry

Set `c=16/945`, `U=3/4` and
[
L_1(m)=(4m+2647)/3696,\quad L_2(m)=(8m+173)/480,
\quad R(m)=(64m+1411)/3840.
]
The continuous conditional kernel for all three phases is
[
K_\varepsilon(m,z)=c(1-\varepsilon mz).
]
For `m0<m<m1`, its support is `[L1(m),R(m)]`; for `m1<m<m2`, `[L2(m),R(m)]`. In both there is **no atom**. For `m2<m<m3`, the support is `[L2(m),U]` plus a positive atom at `U`. The atom arises from the clipping fiber `a≥x(m)=(740-m)/945`, `b=(47-m)/54`; its unnormalized mass is
[
B_\varepsilon(m)=\frac{d(m)}{54}\left[1-\varepsilon\left(mU+
\frac{(m\beta+U\alpha)d(m)}2+\frac{\alpha\beta d(m)^2}{3}\right)\right],
\quad d=49/64-x,\quad\alpha=525/8,\quad\beta=35/32.
]
These inherited coordinate formulas are checked at their exact interfaces:
[
L_1(m_1)=L_2(m_1),\quad R(m_2)=U,\quad L_2(m_3)=U.
]
The continuous density is strictly positive for every interior fiber and every admissible finite epsilon.

## New lemma: the lower phases are strictly ordered even for the anti-TP2 epsilon sign

For all `m∈(m0,m2)` the two support endpoints `L(m),R(m)` are increasing. Let `W=R-L`. Exact derivatives give
[
L'\ge1/924,\quad 0\le W'<1/64,\quad
0<W\le9/1280,\quad 0<L<U=3/4,\quad m<23.
]

**Case epsilon<=0.** Writing `s=-epsilon>=0`, the positive kernel is `c(1+smz)`, with
[
\partial_m\partial_z\log K=s/(1+smz)^2\ge0.
]
Its TP2 ordering on the overlap and the increase of *both* endpoints imply stochastic increase after interval truncation. For `s=0`, the moving endpoints alone provide the order.

**Case 0<=epsilon<=E.** The sharp density-domain endpoint satisfies `E<1/18`. Put
[
\delta=1-\varepsilon mL>1/24,\qquad
t=\frac{\varepsilon mW}{\delta},\qquad 0\le t<69/320.
]
For `y=(z-L)/W∈[0,1]`, the exact normalized cumulative distribution is
[
G_t(y)=\frac{y-ty^2/2}{1-t/2},
\qquad
\partial_tG_t(y)=\frac{y(1-y)}{2(1-t/2)^2}.
]
Let `y=y_t(u)` be its `u`-quantile. Implicit differentiation gives
[
\frac{\partial y_t}{\partial t}
=-\frac{y(1-y)}{2(1-t/2)(1-ty)}.
]
For a fixed admissible epsilon,
[
t'=\frac{\varepsilon(W+mW')}{\delta}
+\frac{\varepsilon^2mW(L+mL')}{\delta^2},
\quad 0\le t'<\frac{1303}{1600},
]
using `L'≤1/60`, `W'≤1/64`, `m≤23`, `W≤9/1280` and `delta>1/24`. Therefore the **physical** discount quantile `Q(m,u)=L(m)+W(m)y_t(u)` satisfies
[
\frac{\partial Q}{\partial m}
=L'+W'y+W\,\partial_t y_t\,t'
>\frac1{924}-
\frac{(9/1280)(1303/1600)}
{8(1-69/640)(1-69/320)}
=\boxed{\frac{157483}{2648572080}>0}.
]
Here `0≤y(1-y)≤1/4`, `1-ty≥1-t`; all denominators are positive. The bound holds uniformly for `u∈[0,1]` and the **two entire lower-phase interiors**. It proves strict quantile increase even though for positive epsilon
[
\partial_m\partial_z\log K=-\varepsilon/(1-\varepsilon mz)^2<0.
]
At `m1` the endpoint formulas agree, so the two ordered families join continuously.

## Joining the top-atom boundary and inherited high phase

At `m2`, the left continuous law has support `[L2(m2),U]`, whereas immediately to the right the same limiting continuous fiber is supplemented by a top atom at `U`. For the natural right version the atom fraction is
[
q_{\varepsilon}(m2+)=\frac{B_\varepsilon(m2)}{A_\varepsilon(m2)+B_\varepsilon(m2)}>0.
]
In particular, exact evaluation gives
[
q_0(m2+)=115/223,\qquad
q_E(m2+)=3310244525/8132285009.
]
This inserts only probability at the maximum `U`, and therefore preserves (indeed strengthens) first-order stochastic order across `m2`. EC49FTY proves stochastic increase on the entire `(m2,m3)` phase for **all** admissible real epsilon. Transitivity joins both lower phases and the high phase. QED.

## Evidence, limits, and next unit

- `EC49FUA_FULL_SUPPORT_VERIFY.py` is an independent standard-library Fraction checker. It checks the quantitative rational quantile bound, exact phase interfaces, exact top-atom jump, and 1,700 cross-phase CDF order comparisons on a finite rational grid. The finite grid is a regression; the all-real theorem follows from the analytic derivative and the inherited high-phase theorem.
- All statements concern **externally chosen price-prior postprocessing**. `a,b` are neither native X6 Cell coordinates nor a native two-dimensional plane. The P000/ACTIVE worldview, original 228-query native input and frozen science pin are unchanged.
- Status: AUTHOR_PROVED / EXACT_RATIONAL_VERIFIED / PARENT_DEPENDENT / NOT_REVIEWED. This is not a new native Bellman run or a formal Task Result/Review.
- **Next discriminating research:** classify whether full-support stochastic order persists under simultaneous `epsilon` and `m` variation (use the fixed-m MLR theorem from EC49FTZ and transitivity); seek sharp quantitative coupling/quantile sensitivity and general non-product priors with sign-changing continuous TP2. Separately retain the actual native `z<11/16` Bellman expansion as an open original-index computation.