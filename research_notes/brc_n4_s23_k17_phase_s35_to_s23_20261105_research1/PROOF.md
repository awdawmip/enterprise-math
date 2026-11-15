# Exact BRC S23 N=4, K=17: full phase 3/5 <= s <= 2/3
Date: 2026-11-05 Asia/Shanghai. Author-side result. Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Previous verified research: PR #1765 commit 09af0b3987632f8da6cbab552a24f1b6a6be3daa. Status: ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Theorem and definitions
Write a=11/21,b=10/21. T distributions are P_T=(as,1-s,bs) and Q_T=(bs,1-s,as); B projections are P_B=(as,1-as),Q_B=(bs,1-bs). For 0<=t<=1, define
  fT(t,s)=-ln(1-s+s(a^t b^(1-t)+b^t a^(1-t))),
  fB(t,s)=-ln((as)^t(bs)^(1-t)+(1-as)^t(1-bs)^(1-t)),
  F(m,n;s)=max_t [m fT(t,s)+n fB(t,s)],
  CT(s)=F(1,0;s), CB(s)=F(0,1;s), H(s)=fB(1/2,s).
The same t must optimize a mixture. Counts are integers m,n>=0, satisfying (2-s)m+n<=17.

There exist exactly three unique zero-crossing parameters α,β,γ, such that
  3/5 < α < 601/1000 < 5/8, F(10,3;α)=17CB(α);
  5/8 < β < 313/500 < 7/11, F(8,6;β)=17CB(β);
  7/11 < γ < 7011/11000 < 2/3, F(11,2;γ)=17CB(γ).
For each half-open cell [l,r) with (l,r,m,n) = (3/5,5/8,10,3), (5/8,7/11,8,6), (7/11,2/3,11,2), the unique maximizing count is (m,n) for l<=s<its crossing, (m,n) and (0,17) alone tie at the crossing, and (0,17) uniquely maximizes above the crossing until r. At s=2/3, the unique maximizer is (12,1).

## Proof of global candidate reduction
For s<=2/3, 13(2-s)>=52/3>17, hence m<=12. At fixed m, strict improvement with n gives the maximal n_m=17-2m+floor(ms). The complete change-point set k/m for feasible m=1,...,12 in [3/5,2/3] is {3/5,5/8,7/11,2/3}. Exact exhaustive rational enumeration shows the following upper convex hull vertices of (m,n_m):
  [3/5,5/8): (0,17),(10,3),(12,0);
  [5/8,7/11): (0,17),(8,6),(12,0);
  [7/11,2/3): (0,17),(11,2),(12,0);
  s=2/3: (0,17),(12,1).
Each hull and all 13 integer m positions are explicitly checked by VERIFY.py.

F is convex as a function of real (m,n), since it is the maximum of linear functions. Strictness for nonvertex count points follows from differing unique optimizers: fT uniquely maximizes at t=1/2; the Bernoulli fB maximizes at an interior t_B>1/2 (its derivative at 1/2 is positive by the prior proof using ψ(z)=z/(2sinh(z/2))). Two noncollinear hull vertices cannot share a maximizing t: their stationarity would imply fT'=fB'=0, a contradiction. Thus no proper edge interpolation is another maximizer.

For all s in [3/5,2/3], D(s)=17CB(s)-12CT(s)>0, certified below, eliminates the vertex (12,0). This leaves (0,17) and the named mixed vertex in each cell. At s=2/3 the strict exact bounds 12CT(2/3)+H(2/3)>17CB(2/3) and H(2/3)>0 select (12,1) uniquely.

## Proof that each continuous crossing exists and is unique
For fixed t, fT(t,s) and fB(t,s) are convex in s: the T Chernoff coefficient is affine, while the B coefficient is concave by concavity of weighted geometric mean, followed by the decreasing convex transform -ln. Therefore F(m,n;s), CT and CB are convex in s.

For every rational subcell [x,y] and δ=1/10000, let
  L=[CB(x)-CB(x-δ)]/δ,
  U=[m CT(y+δ)+n CB(y+δ)-m CT(y)-n H(y)]/δ.
For all real x<=u<v<=y, convex secant slopes imply
  [G(v)-G(u)]/(v-u) <= U-17L, G(s)=F(m,n;s)-17CB(s).
Here we use mCT+nH <= F <= mCT+nCB at each endpoint. VERIFY.py subdivides each of the three cells into 12 rational subcells and certifies 17L-U>0 on every one of 36 pieces. Consequently G strictly decreases throughout each real cell. At left endpoint l it certifies mCT(l)+nH(l)-17CB(l)>0; at l+1/1000 it certifies (17-n)CB(l+1/1000)-mCT(l+1/1000)>0. Continuity proves exactly one zero in (l,l+1/1000).

To certify D(s)>0 on the full [3/5,2/3], VERIFY.py uses three exact subcells [x,y], checks D(x)>0, and checks the slope bound
  17[CB(x)-CB(x-δ)]/δ -12[CT(y+δ)-CT(y)]/δ > 0.
Convexity implies strictly positive D on each segment and hence on the entire interval.

## Exact checker and scope
The single-file VERIFY.py uses only Python Fraction and isqrt, a 34-term artanh logarithm series with a proven geometric remainder, outward 10^-48 square-root enclosures, and a rigorous Bernoulli Chernoff tilt enclosure ρ=J/(H0+J), H0=ln(a/b), J=ln((1-bs)/(1-as)). It executes 36 monotonicity assertions, six endpoint-crossing assertions, six competing-vertex assertions and two s=2/3 assertions: 50 strictly positive exact rational certificates, plus complete rational feasibility/hull enumeration. Full actual stdout is saved in RUN_EVIDENCE.txt.

This auxiliary sampling theorem retains the frozen N=4 S23 model and K=17 cost assumption. The separate original ten-label minimax mother target remains open on its recorded [1/2,2/3] bracket. Independent mathematical review and native Result acceptance are pending.
